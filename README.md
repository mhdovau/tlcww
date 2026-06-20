# tlcww — CitSci.org Backup

Automated backups of a [CitSci.org](https://citsci.org) account and its
projects, using the CitSci API (`https://api.citsci.org`).

A scheduled GitHub Action logs in with a CitSci account's credentials, walks the
account and every project it owns, manages or is a member of, and commits a
structured snapshot (JSON metadata **and** photo/file binaries) back into this
repository.

## Setup

1. **Use a dedicated, low-privilege CitSci account for backups — not a personal
   or admin account.** Create a separate, single-purpose account and add it to
   the project(s) you want to back up at the **lowest role that can still see
   the data** you want to preserve (a regular *member*/contributor is usually
   enough). See [Account & privacy](#account--privacy-important) below for why
   this matters.
2. In this repo, go to **Settings → Secrets and variables → Actions** and add:

   | Secret | Required | Purpose |
   | --- | --- | --- |
   | `CITSCI_USER` | yes | Account email used to log in |
   | `CITSCI_PASS` | yes | Account password |
   | `CITSCI_USER_ID` | optional | Your user id — only needed if it can't be auto-resolved from the login token |
   | `CITSCI_FILES_BASE` | optional | Base URL for downloading file binaries that store only a relative path (most are already absolute S3 URLs) |
   | `CITSCI_INCLUDE_PRIVATE` | optional | `1` to include the values of fields flagged *private* (e.g. "Monitor's Name(s) - NOT published publically"). Default `0` — withheld so they aren't published. Only set this if the repo is private. |

3. Run it: **Actions → CitSci Backup → Run workflow** (or wait for the daily
   schedule). The first manual run is the easiest way to confirm credentials
   and the resolved user id are correct.

## Account & privacy (important)

Use a **dedicated, low-privilege CitSci account** for backups. Two reasons:

- **Least privilege / blast radius.** The account's email and password live in
  GitHub Actions secrets. A single-purpose account used only for backups means a
  leak can't touch a personal identity or other projects, and it's trivially
  rotated. **Don't use a personal account, and don't grant it site-admin.**
- **Data minimization.** CitSci returns *less* data to lower-privilege accounts.
  Fields a datasheet marks *private* (e.g. monitors' real names) are **withheld
  by the API** from a regular member/contributor — they never reach the backup.
  A manager/admin account, by contrast, can read that private content, which
  would then be committed to this repository. Grant only the role needed to see
  the data you actually want to preserve.

As an extra safeguard the script masks email addresses, and values of
private-flagged fields are withheld unless `CITSCI_INCLUDE_PRIVATE=1` (only set
that on a private repo). But choosing a low-privilege account is the primary
control — the API simply won't hand it sensitive data in the first place. If you
do need the richer data a manager account can see, **make this repository
private.**

## Schedule

- **Daily**, at 06:00 UTC (`.github/workflows/backup.yml`).
- **On demand** via the *Run workflow* button, with an option to skip binary
  downloads (metadata only).

## What gets backed up

```
data/
├── manifest.json                  # run timestamp, resolved user id, counts
├── account/
│   ├── profile.json               # account info (credentials/tokens redacted)
│   ├── memberships.json
│   ├── organization_memberships.json
│   ├── notification_preferences.json
│   ├── invites.json
│   ├── project_downloads.json
│   ├── project_airtable_history.json
│   ├── observations.json          # all of your observations
│   └── stats.json
├── projects/
│   └── <project-slug>/
│       ├── project.json           # full project settings
│       ├── stats.json
│       ├── members.json
│       ├── locations.json         # every project area/location
│       ├── resources.json
│       ├── project_posts.json
│       ├── invites.json
│       ├── observations.json      # observation list (summary)
│       ├── observations/
│       │   └── <id>.json          # full detail: field values + attached files
│       └── datasheets/
│           └── <datasheet-slug>/
│               ├── datasheet.json
│               └── records.json   # field definitions for the datasheet
├── projects/<project-slug>/README.md                  # rendered project summary
├── projects/<project-slug>/datasheets/<ds>/README.md  # rendered observations
└── files/
    ├── index.json                 # URL → local_path map (+ download status)
    ├── _download_errors.json      # any binaries that couldn't be fetched
    └── photos_and_files/          # downloaded photos / documents / resources
```

### Human-readable views

Each run also renders browsable markdown (so the archive is legible without
parsing JSON, and GitHub shows it automatically when you open a folder):

- `projects/<slug>/README.md` — project summary (description, counts) with links
  to each datasheet's view.
- `projects/<slug>/datasheets/<ds>/README.md` — the datasheet's field list plus
  every observation, with all collected values in a table and inline photo
  thumbnails / document links resolved to the local copies under
  `files/photos_and_files/`.

The renderer is generic: it reflects whatever fields and record types each
datasheet defines, with no project-specific assumptions.

Every file reference in the saved JSON (e.g. an observation's `featuredPhoto`,
a record's attached photo, a project resource) keeps its original `path` URL
**and** gains a `localFile` property pointing at the downloaded copy under
`files/photos_and_files/`. `files/index.json` is the authoritative map of every
referenced URL to its `local_path`, its `etag` and `content_length`, whether the
binary was `downloaded`, and whether it is now `orphaned`.

### Efficient re-fetches (conditional GET)

File downloads use the stored S3 `ETag` with an `If-None-Match` conditional
`GET`: unchanged files return `304 Not Modified` and are not re-downloaded, so
repeated/daily runs transfer almost nothing. A genuinely changed object returns
`200` and is re-fetched (and its ETag updated). The manifest reports
`files_downloaded` vs `files_unchanged`. Because each backup is idempotent and
the commit step skips no-op manifest-only changes, running daily is cheap.

### Nothing is ever deleted (preservation)

This is an archival backup, so data removed upstream is **kept**, not dropped.
The script never deletes files, and the workflow stages with `git add` (never
`git add -A`), so a photo, file or observation removed from CitSci stays on disk
and in git history. Files no longer referenced by the current snapshot are
retained and flagged `"orphaned": true` in `files/index.json` (the prior URL is
carried forward where known), and the manifest reports `files_referenced` vs
`files_orphaned` counts.

Observation detail files are handled the same way: an observation that
disappears upstream keeps its `projects/<slug>/observations/<id>.json` on disk
and is listed under `orphaned_observations` in `manifest.json` (with its id,
project and `observedAt`), so removals are visible at a glance. Orphans are only
recorded when the observation list was fetched successfully — a failed fetch
never flags existing files as removed.

### Notes

- **Credentials are never written to disk.** Password and third-party tokens
  (Google, Airtable, SciStarter, reCAPTCHA, JWTs) are stripped from saved JSON,
  and email addresses are masked (e.g. `s***@i***`).
- **Observation detail.** The project observation *list* omits submitted values
  and photos, so each observation is also fetched individually
  (`/observations/{id}`) to capture `records[].value`, attached photos and
  comments.
- **Photos / files.** Uploads are absolute S3 URLs embedded across observations,
  records, project resources and avatars (the `/file_objects` collection only
  lists files the account *owns*). The script harvests every referenced URL,
  lists them in `files/index.json`, and downloads the binaries to
  `files/photos/`. Our auth token is never sent to the file host. Failures are
  recorded in `files/_download_errors.json` and don't stop the run.
- **Private fields.** Values of fields the datasheet marks *private* are
  withheld by default (see `CITSCI_INCLUDE_PRIVATE`) so volunteer PII isn't
  published to a public repo.
- **Resilient by design.** A single failing endpoint is logged and skipped
  rather than aborting the whole backup. Network/5xx/429 responses are retried
  with exponential backoff, and an expired access token is refreshed mid-run.

## Running locally

The script uses only the Python standard library (3.10+):

```bash
export CITSCI_USER="you@example.com"
export CITSCI_PASS="your-password"
# export CITSCI_USER_ID="..."        # if auto-resolution fails
# export CITSCI_FILES_BASE="https://..."
python3 scripts/citsci_backup.py     # writes to ./data
```

## Historic data

Curated historic datasets that predate (or sit outside) the automated CitSci
backup live under [`historic-data/`](historic-data/), kept separate from `data/`
so a backup run never touches them. The backup script only ever writes under
`data/`. See [`historic-data/README.md`](historic-data/README.md) for the
catalogue.

### Licensing of historic data (important)

This repository's [`LICENSE.md`](LICENSE.md) (CC BY 4.0) covers **only** Dover
Landcare Tasmania's own content — the CitSci backup under `data/` and the code.
It does **not** cover the third-party material under `historic-data/`, which is
owned by others. Each dataset there carries its own `COPYRIGHT.md`; read it
before reusing the data.

- **Huon Valley Water Quality 1996–2000**
  ([`historic-data/huon-valley-wq-1996-2000/`](historic-data/huon-valley-wq-1996-2000/)):
  © Helen Otley and/or the Huon Healthy Rivers Project. Copyright is **not** held
  by Dover Landcare, and **no license is granted** — seek permission from the
  original author / project before any use. See its
  [`COPYRIGHT.md`](historic-data/huon-valley-wq-1996-2000/COPYRIGHT.md).

## API reference

The CitSci OpenAPI 3.1 specification is vendored at
[`spec/citsci-openapi.json`](spec/citsci-openapi.json) for reference. It is
served live at `https://api.citsci.org/docs.jsonopenapi`.
