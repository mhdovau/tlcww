#!/usr/bin/env python3
"""Back up a CitSci.org account and its projects to local files.

Authenticates against the CitSci API (https://api.citsci.org) with an account
email/password, then walks the account, its projects, datasheets, records,
observations and uploaded files, writing everything to an output directory in a
stable, diffable structure.

Only the Python standard library is used so the script can run on a clean
GitHub Actions runner with no `pip install` step.

Environment variables
---------------------
CITSCI_USER       (required)  Account email used to log in.
CITSCI_PASS       (required)  Account password.
CITSCI_USER_ID    (optional)  Account id/IRI. If unset, it is resolved from the
                              JWT and/or by probing /users/{id}.
CITSCI_API_BASE   (optional)  API base URL. Default: https://api.citsci.org
CITSCI_FILES_BASE (optional)  Base URL for downloading file/photo binaries when
                              a file record only stores a relative path.
CITSCI_OUTPUT_DIR (optional)  Output directory. Default: ./data
CITSCI_DOWNLOAD_FILES (optional) "0" to skip binary photo/file downloads
                              (metadata is always saved). Default: "1".
"""

from __future__ import annotations

import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

API_BASE = os.environ.get("CITSCI_API_BASE", "https://api.citsci.org").rstrip("/")
FILES_BASE = os.environ.get("CITSCI_FILES_BASE", "").rstrip("/")
OUTPUT_DIR = os.environ.get("CITSCI_OUTPUT_DIR", "data")
DOWNLOAD_FILES = os.environ.get("CITSCI_DOWNLOAD_FILES", "1") != "0"
# Include the values of observation fields flagged isPrivate (e.g. the
# "Monitor's Name(s) - NOT published publically" field). Off by default so
# private volunteer data is not written to a public repository.
INCLUDE_PRIVATE = os.environ.get("CITSCI_INCLUDE_PRIVATE", "0") == "1"

# Account fields that must never be written to disk even if the API returns
# them. These are credentials / third-party tokens, not backup data.
SENSITIVE_KEYS = {
    "password", "oldPassword", "confirmPassword", "token", "refresh_token",
    "refreshToken", "googleToken", "airtableToken", "airtableRefresh",
    "sciStarterToken", "recaptchaToken",
}
# Personal data fields masked (not dropped) in saved JSON. Only the backup
# account's own profile carries an email; mask it rather than publish it.
EMAIL_KEYS = {"email"}

USER_AGENT = "citsci-backup/1.0 (+github-actions)"
PAGE_SIZE = 100
MAX_RETRIES = 4

# Accumulates every file/photo reference discovered while walking the API so
# the binaries can be downloaded once at the end (de-duplicated by URL).
FILE_REFS: dict[str, dict] = {}

# Records what the API actually returned for fields flagged isPrivate, so a run
# can confirm whether the account's token is served private content at all.
PRIVATE_STATS: dict = {
    "private_records_seen": 0,
    "private_records_with_content": 0,
    "content_keys_returned": {},
}


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc):%H:%M:%S}] {msg}", flush=True)


class CitSciClient:
    """Minimal authenticated JSON client for the CitSci API."""

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.token: str | None = None
        self.refresh_token: str | None = None

    # -- low level ---------------------------------------------------------
    def _request(self, method: str, path: str, *, body: dict | None = None,
                 accept: str = "application/ld+json", raw: bool = False,
                 auth: bool = True, _retry_auth: bool = True):
        url = path if path.startswith("http") else f"{API_BASE}{path}"
        data = None
        headers = {"Accept": "*/*" if raw else accept, "User-Agent": USER_AGENT}
        if body is not None:
            data = json.dumps(body).encode()
            headers["Content-Type"] = "application/ld+json"
        # Only attach our bearer token to the API host; never leak it to
        # third-party file hosts (e.g. the public S3 bucket).
        if self.token and auth and url.startswith(API_BASE):
            headers["Authorization"] = f"Bearer {self.token}"

        last_err = None
        for attempt in range(1, MAX_RETRIES + 1):
            req = urllib.request.Request(url, data=data, headers=headers, method=method)
            try:
                with urllib.request.urlopen(req, timeout=120) as resp:
                    payload = resp.read()
                    if raw:
                        return payload, resp.headers
                    return json.loads(payload) if payload else None
            except urllib.error.HTTPError as e:
                # Token expired mid-run: refresh once and retry.
                if e.code == 401 and _retry_auth and self.refresh_token and self.token:
                    log("Access token rejected (401); refreshing…")
                    if self._refresh():
                        return self._request(method, path, body=body, accept=accept,
                                             raw=raw, _retry_auth=False)
                if e.code in (429, 500, 502, 503, 504) and attempt < MAX_RETRIES:
                    wait = 2 ** attempt
                    log(f"HTTP {e.code} on {path}; retry {attempt}/{MAX_RETRIES} in {wait}s")
                    time.sleep(wait)
                    last_err = e
                    continue
                raise
            except urllib.error.URLError as e:
                if attempt < MAX_RETRIES:
                    wait = 2 ** attempt
                    log(f"Network error on {path}: {e}; retry {attempt}/{MAX_RETRIES} in {wait}s")
                    time.sleep(wait)
                    last_err = e
                    continue
                raise
        if last_err:
            raise last_err

    def get(self, path: str):
        return self._request("GET", path)

    # -- auth --------------------------------------------------------------
    def login(self) -> None:
        log("Authenticating with email/password…")
        resp = self._request("POST", "/login",
                             body={"email": self.email, "password": self.password})
        self.token = resp.get("token")
        self.refresh_token = resp.get("refresh_token")
        if not self.token:
            raise RuntimeError("Login succeeded but no access token was returned.")
        log("Authenticated; access token acquired.")

    def _refresh(self) -> bool:
        try:
            resp = self._request("POST", "/token/refresh",
                                 body={"refresh_token": self.refresh_token},
                                 _retry_auth=False)
            self.token = resp.get("token")
            self.refresh_token = resp.get("refresh_token") or self.refresh_token
            return bool(self.token)
        except urllib.error.HTTPError:
            log("Refresh token rejected; re-authenticating from scratch.")
            self.login()
            return True

    # -- pagination --------------------------------------------------------
    def collect(self, path: str) -> list:
        """Fetch every item of a Hydra collection, following pagination."""
        items: list = []
        sep = "&" if "?" in path else "?"
        next_url = f"{path}{sep}itemsPerPage={PAGE_SIZE}&page=1"
        while next_url:
            resp = self.get(next_url)
            if resp is None:
                break
            if isinstance(resp, list):
                items.extend(resp)
                break
            members = resp.get("hydra:member", resp.get("member", []))
            items.extend(members)
            view = resp.get("hydra:view", resp.get("view", {}))
            nxt = view.get("hydra:next") or view.get("next")
            if nxt:
                next_url = nxt
            elif len(members) == PAGE_SIZE:
                # No hydra:next but a full page came back; advance manually.
                m = re.search(r"[?&]page=(\d+)", next_url)
                page = int(m.group(1)) + 1 if m else 2
                next_url = re.sub(r"([?&]page=)\d+", rf"\g<1>{page}", next_url)
            else:
                next_url = None
        return items


def mask_email(value):
    """Mask an email like a***@e***.com, preserving shape but not the address."""
    if not isinstance(value, str) or "@" not in value:
        return "***REDACTED***"
    local, _, domain = value.partition("@")
    return f"{local[:1]}***@{domain[:1]}***"


def redact(obj):
    """Recursively strip credentials and mask personal data in a structure."""
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k in SENSITIVE_KEYS:
                out[k] = "***REDACTED***"
            elif k in EMAIL_KEYS and v:
                out[k] = mask_email(v)
            else:
                out[k] = redact(v)
        return out
    if isinstance(obj, list):
        return [redact(v) for v in obj]
    return obj


def harvest_files(obj) -> None:
    """Recursively record file/photo references (FileObjects) for download.

    CitSci embeds uploads as objects with an S3 `path` (and sometimes a
    `filename`/`mimeType`); the listable `/file_objects` collection only covers
    files the account owns, so photos must be gathered from the resources they
    are attached to (observations, records, project resources, avatars)."""
    if isinstance(obj, dict):
        # A FileObject carries an http `path`; `file` may be a string URL too.
        path = obj.get("path")
        if not isinstance(path, str):
            path = obj.get("file") if isinstance(obj.get("file"), str) else None
        if isinstance(path, str) and path.startswith("http"):
            iri = obj.get("@id", "")
            FILE_REFS.setdefault(path, {
                "url": path,
                "id": iri.rsplit("/", 1)[-1] or obj.get("id", ""),
                "filename": obj.get("filename") or path.rsplit("/", 1)[-1],
            })
        for v in obj.values():
            harvest_files(v)
    elif isinstance(obj, list):
        for v in obj:
            harvest_files(v)


# The content-bearing keys of an observation record. For a record flagged
# isPrivate we blank these and leave every other key (label, recordType,
# orderNumber, description, isPrivate, timestamps, nested structure) intact.
PRIVATE_VALUE_KEYS = ("value", "optionValue", "multiSelectOptionValues",
                      "organism", "files")


def redact_private_records(observation: dict) -> dict:
    """Withhold the *content* of records flagged isPrivate (unless
    CITSCI_INCLUDE_PRIVATE=1), preserving all other field metadata.

    Always records, in PRIVATE_STATS, whether the API actually returned any
    content for private fields — so a run can prove what the account can see."""
    if not isinstance(observation, dict):
        return observation

    def walk(rec):
        if isinstance(rec, dict):
            if rec.get("isPrivate"):
                # Did the API actually send content for this private field?
                returned = [k for k in PRIVATE_VALUE_KEYS
                            if rec.get(k) not in (None, [], "", {})]
                if rec.get("isPrivate") and "recordType" in rec:
                    PRIVATE_STATS["private_records_seen"] += 1
                    if returned:
                        PRIVATE_STATS["private_records_with_content"] += 1
                        for k in returned:
                            PRIVATE_STATS["content_keys_returned"][k] = \
                                PRIVATE_STATS["content_keys_returned"].get(k, 0) + 1
                if returned and not INCLUDE_PRIVATE:
                    rec = dict(rec)
                    if rec.get("value") not in (None, ""):
                        rec["value"] = "***PRIVATE — withheld from backup***"
                    for k in ("optionValue", "organism"):
                        if rec.get(k) not in (None, {}):
                            rec[k] = None
                    if rec.get("multiSelectOptionValues"):
                        rec["multiSelectOptionValues"] = []
                    if rec.get("files"):
                        rec["files"] = []
            return {k: walk(v) for k, v in rec.items()}
        if isinstance(rec, list):
            return [walk(v) for v in rec]
        return rec

    return walk(observation)


def write_json(rel_path: str, data, *, harvest: bool = True) -> None:
    if harvest:
        harvest_files(data)
    full = os.path.join(OUTPUT_DIR, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        json.dump(redact(data), f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")


def slugify(value: str, fallback: str) -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"[^a-z0-9._-]+", "-", value).strip("-")
    return value or fallback


def jwt_claims(token: str) -> dict:
    try:
        payload = token.split(".")[1]
        payload += "=" * (-len(payload) % 4)
        return json.loads(base64.urlsafe_b64decode(payload))
    except Exception:
        return {}


def resolve_user_id(client: CitSciClient) -> str:
    """Determine the logged-in user's id, trying several strategies."""
    explicit = os.environ.get("CITSCI_USER_ID")
    if explicit:
        log("Using CITSCI_USER_ID from environment.")
        return explicit.rsplit("/", 1)[-1]

    claims = jwt_claims(client.token or "")
    candidates: list[str] = []
    for key in ("id", "userId", "user_id", "sub", "uuid"):
        val = claims.get(key)
        if isinstance(val, str) and val:
            candidates.append(val.rsplit("/", 1)[-1])
    # Any IRI-looking claim value e.g. "/users/<uuid>".
    for val in claims.values():
        if isinstance(val, str) and "/users/" in val:
            candidates.append(val.rsplit("/", 1)[-1])

    seen = set()
    for cand in candidates:
        if cand in seen:
            continue
        seen.add(cand)
        try:
            user = client.get(f"/users/{cand}")
            if user and user.get("email", "").lower() == client.email.lower():
                log("Resolved user id from token claims.")
                return cand
        except urllib.error.HTTPError:
            continue

    raise RuntimeError(
        "Could not determine the account user id automatically. "
        "Set the CITSCI_USER_ID secret to your user id (visible in your "
        "citsci.org profile URL) and re-run."
    )


def safe(label: str, fn):
    """Run a fetch step, logging and swallowing per-resource errors so one
    failure does not abort the whole backup."""
    try:
        return fn()
    except urllib.error.HTTPError as e:
        log(f"  ! {label}: HTTP {e.code} — skipped")
    except Exception as e:  # noqa: BLE001 - best-effort backup
        log(f"  ! {label}: {e} — skipped")
    return None


def download_file(client: CitSciClient, record: dict, dest_dir: str,
                  errors: list) -> str | None:
    """Best-effort download of a file/photo binary."""
    file_url = record.get("url") or record.get("file") or ""
    path = record.get("path") or ""
    fid = record.get("id", "")
    filename = record.get("filename") or (path.rsplit("/", 1)[-1] if path else f"{fid}")

    if file_url.startswith("http"):
        url = file_url
    elif path.startswith("http"):
        url = path
    elif FILES_BASE and path:
        url = f"{FILES_BASE}/{path.lstrip('/')}"
    else:
        errors.append({"id": fid, "filename": filename,
                       "reason": "no resolvable URL (set CITSCI_FILES_BASE)"})
        return None

    safe_name = f"{slugify(str(fid), 'file')}-{slugify(filename, 'photo')}"
    out_path = os.path.join(dest_dir, safe_name)
    try:
        payload, _ = client._request("GET", url, raw=True)
        os.makedirs(dest_dir, exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(payload)
        return safe_name
    except Exception as e:  # noqa: BLE001
        errors.append({"id": fid, "filename": filename, "url": url, "reason": str(e)})
        return None


def backup_account(client: CitSciClient, uid: str, manifest: dict) -> None:
    log("Backing up account…")
    profile = safe("account profile", lambda: client.get(f"/users/{uid}"))
    if profile:
        write_json("account/profile.json", profile)
        manifest["account_email"] = profile.get("email")
        manifest["account_display_name"] = profile.get("displayName")

    endpoints = {
        "memberships": f"/users/{uid}/memberships",
        "organization_memberships": f"/users/{uid}/organization_memberships",
        "notification_preferences": f"/users/{uid}/notification_preferences",
        "invites": f"/users/{uid}/invites",
        "project_downloads": f"/users/{uid}/project_downloads",
        "project_airtable_history": f"/users/{uid}/project_airtable_history",
        "observations": f"/users/{uid}/observations",
    }
    for name, path in endpoints.items():
        items = safe(f"account {name}", lambda p=path: client.collect(p))
        if items is not None:
            write_json(f"account/{name}.json", items)
    stats = safe("account stats", lambda: client.get(f"/users/{uid}/stats"))
    if stats is not None:
        write_json("account/stats.json", stats)


def backup_datasheets(client: CitSciClient, pid: str, proj_dir: str,
                      counts: dict) -> None:
    sheets = safe("datasheets list", lambda: client.collect(f"/projects/{pid}/datasheets"))
    if not sheets:
        return
    for sheet in sheets:
        sid = (sheet.get("id") or "").rsplit("/", 1)[-1]
        if not sid:
            continue
        sdir = f"{proj_dir}/datasheets/{slugify(sheet.get('name',''), sid)}"
        detail = safe(f"datasheet {sid}", lambda s=sid: client.get(f"/datasheets/{s}"))
        write_json(f"{sdir}/datasheet.json", detail or sheet)
        records = safe(f"datasheet {sid} records",
                       lambda s=sid: client.collect(f"/datasheets/{s}/records"))
        if records is not None:
            write_json(f"{sdir}/records.json", records)
            counts["datasheet_records"] += len(records)
        counts["datasheets"] += 1


def discover_projects(client: CitSciClient, uid: str) -> list[dict]:
    """Build the list of projects to back up.

    `/users/{id}/projects` only returns projects the account *owns/manages*, so
    a member-only account would back up nothing. We merge that with the
    projects referenced by the account's memberships, de-duplicated by id.
    """
    found: dict[str, dict] = {}

    def add(pid: str, name: str, slug: str, source: str) -> None:
        pid = (pid or "").rsplit("/", 1)[-1]
        if not pid:
            return
        entry = found.setdefault(pid, {"id": pid, "name": name, "slug": slug,
                                       "sources": set()})
        entry["sources"].add(source)
        entry["name"] = entry.get("name") or name
        entry["slug"] = entry.get("slug") or slug

    owned = safe("owned projects", lambda: client.collect(f"/users/{uid}/projects")) or []
    for p in owned:
        add(p.get("id", ""), p.get("name") or p.get("urlField") or "",
            p.get("urlField") or p.get("name") or "", "owned")

    members = safe("memberships", lambda: client.collect(f"/users/{uid}/memberships")) or []
    for m in members:
        add(m.get("projectId", ""), m.get("projectName") or "",
            m.get("projectUrl") or m.get("projectName") or "", "member")

    log(f"Found {len(found)} project(s): "
        + ", ".join(f"{e['name']} [{'/'.join(sorted(e['sources']))}]"
                    for e in found.values()))
    for e in found.values():
        e["sources"] = sorted(e["sources"])
    return list(found.values())


def backup_projects(client: CitSciClient, uid: str, counts: dict) -> None:
    log("Backing up projects…")
    for proj in discover_projects(client, uid):
        pid = proj["id"]
        name = proj["name"] or pid
        proj_dir = f"projects/{slugify(proj['slug'] or name, pid)}"
        log(f"  Project: {name}")

        detail = safe(f"project {pid}", lambda: client.get(f"/projects/{pid}"))
        write_json(f"{proj_dir}/project.json", detail or proj)

        sub = {
            "stats": (f"/projects/{pid}/stats", False),
            "members": (f"/projects/{pid}/members", True),
            "locations": (f"/projects/{pid}/locations", True),
            "resources": (f"/projects/{pid}/resources", True),
            "project_posts": (f"/projects/{pid}/project_posts", True),
            "invites": (f"/projects/{pid}/invites", True),
        }
        for fname, (path, is_collection) in sub.items():
            fetch = (lambda p=path: client.collect(p)) if is_collection \
                else (lambda p=path: client.get(p))
            data = safe(f"project {fname}", fetch)
            if data is not None:
                write_json(f"{proj_dir}/{fname}.json", data)
                if fname == "locations":
                    counts["locations"] += len(data)

        backup_observations(client, pid, proj_dir, counts)
        backup_datasheets(client, pid, proj_dir, counts)
        counts["projects"] += 1


def backup_observations(client: CitSciClient, pid: str, proj_dir: str,
                        counts: dict) -> None:
    """Save the observation list plus full per-observation detail.

    The collection endpoint omits the submitted field values and attached
    photos; `/observations/{id}` returns `records[].value`, `records[].files[]`
    and the observation `files[]`, which is where the real data and most photos
    live."""
    obs = safe("project observations", lambda: client.collect(f"/projects/{pid}/observations"))
    if obs is None:
        return
    write_json(f"{proj_dir}/observations.json", obs)
    counts["observations"] += len(obs)
    for o in obs:
        oid = (o.get("id") or o.get("@id", "")).rsplit("/", 1)[-1]
        if not oid:
            continue
        detail = safe(f"observation {oid}", lambda i=oid: client.get(f"/observations/{i}"))
        if detail is not None:
            write_json(f"{proj_dir}/observations/{oid}.json",
                       redact_private_records(detail))
            counts["observation_records"] += len(detail.get("records") or [])


def backup_files(client: CitSciClient, counts: dict) -> None:
    """Download every file/photo referenced anywhere in the backup.

    `harvest_files` (called from `write_json`) has already collected every
    embedded FileObject URL — observation photos, record attachments, project
    resources, avatars — so we download from that set rather than the
    owner-only `/file_objects` collection."""
    log("Backing up files / photos…")
    # Also include the account's own owned files, if any.
    owned = safe("owned file list", lambda: client.collect("/file_objects")) or []
    harvest_files(owned)

    refs = list(FILE_REFS.values())
    write_json("files/index.json", refs, harvest=False)
    counts["files"] = len(refs)
    if not refs:
        log("  No file references discovered.")
        return
    if not DOWNLOAD_FILES:
        log(f"  {len(refs)} file(s) referenced; binary downloads disabled "
            "(CITSCI_DOWNLOAD_FILES=0).")
        return

    errors: list = []
    downloaded = 0
    photo_dir = os.path.join(OUTPUT_DIR, "files", "photos")
    for ref in refs:
        if download_file(client, ref, photo_dir, errors):
            downloaded += 1
    log(f"  Downloaded {downloaded}/{len(refs)} file(s); {len(errors)} error(s).")
    if errors:
        write_json("files/_download_errors.json", errors, harvest=False)
    counts["files_downloaded"] = downloaded


def main() -> int:
    email = os.environ.get("CITSCI_USER")
    password = os.environ.get("CITSCI_PASS")
    if not email or not password:
        sys.stderr.write("ERROR: CITSCI_USER and CITSCI_PASS must be set.\n")
        return 2

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    started = datetime.now(timezone.utc)
    manifest = {
        "generated_at": started.isoformat(),
        "api_base": API_BASE,
    }
    counts = {"projects": 0, "datasheets": 0, "datasheet_records": 0,
              "observations": 0, "observation_records": 0, "locations": 0,
              "files": 0, "files_downloaded": 0}
    manifest["include_private_fields"] = INCLUDE_PRIVATE

    client = CitSciClient(email, password)
    client.login()
    uid = resolve_user_id(client)
    manifest["user_id"] = uid

    backup_account(client, uid, manifest)
    backup_projects(client, uid, counts)
    backup_files(client, counts)

    manifest["counts"] = counts
    manifest["private_fields"] = PRIVATE_STATS
    manifest["completed_at"] = datetime.now(timezone.utc).isoformat()
    manifest["duration_seconds"] = round(
        (datetime.now(timezone.utc) - started).total_seconds(), 1)
    write_json("manifest.json", manifest, harvest=False)

    log(f"Backup complete: {json.dumps(counts)}")
    if PRIVATE_STATS["private_records_seen"]:
        log(f"Private fields: API returned content for "
            f"{PRIVATE_STATS['private_records_with_content']}/"
            f"{PRIVATE_STATS['private_records_seen']} private record(s) "
            f"(withheld={not INCLUDE_PRIVATE}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
