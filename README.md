# tlcww — Dover Landcare Water Watch - CitSci.org Backup

## License
Usage Terms [`LICENSE.md`](LICENSE.md)

## Historic Data
Archive Here [`historic-data/`](historic-data/)

## CitSci Project
Backup / Extract Here [`data/projects/`](data/projects/)

# Automated Backups

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

- **Daily**, at 10:51 UTC (`.github/workflows/backup.yml`) — evening in Tasmania,
  after the day's observations are usually entered.
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
├── projects/<project-slug>/field_aliases.json         # hand-maintained field merges
├── projects/<project-slug>/observations.csv           # every value, long format
├── projects/<project-slug>/locations.csv              # sites + coordinates
├── projects/<project-slug>/datasheets/<ds>/README.md  # rendered observations
├── projects/<project-slug>/datasheets/<ds>/observations.csv  # wide table
└── files/
    ├── index.json                 # URL → local_path map (+ download status)
    ├── _download_errors.json      # any binaries that couldn't be fetched
    └── photos_and_files/          # downloaded photos / documents / resources
```

### Human-readable views

Each run also renders browsable markdown (so the archive is legible without
parsing JSON, and GitHub shows it automatically when you open a folder):

- `projects/<slug>/README.md` — project summary (description, counts) with links
  to each datasheet's view and to the CSV extracts.
- `projects/<slug>/datasheets/<ds>/README.md` — the datasheet's field list plus
  every observation, with all collected values in a table and inline photo
  thumbnails / document links resolved to the local copies under
  `files/photos_and_files/`.

The renderer is generic: it reflects whatever fields and record types each
datasheet defines, with no project-specific assumptions.

### CSV extracts (spreadsheets)

The same data is also written as CSV, so it can be opened directly in Excel /
LibreOffice / Google Sheets or loaded with pandas/R without parsing JSON. Every
markdown page links to its CSV, and GitHub renders CSVs as a sortable table in
the browser.

- `projects/<slug>/datasheets/<ds>/observations.csv` — **wide**: one row per
  observation, one column per field that datasheet defines (plus any field that
  holds data but has since been removed from the datasheet). Best for analysing
  a single datasheet.
- `projects/<slug>/observations.csv` — **long/tidy**: one row per recorded field
  value (`observation_id`, `observed_at`, `datasheet`, `location`, `latitude`,
  `longitude`, `observer`, `field`, `record_type`, `value`, `files`), covering
  every datasheet in one file — including observations whose datasheet no longer
  exists upstream. Best for combining datasheets or plotting one parameter over
  time.
- `projects/<slug>/locations.csv` — every monitoring site with its coordinates
  and observation count; ready to import into a GIS or mapping tool.

#### Renamed fields are merged into one column

Datasheets get edited: a field is renamed (`Ph` → `pH`), or deleted and re-added
with a tweaked name — CitSci gives the replacement a **new** `datasheet_record`
id, so the same measurement can sit under several labels across a project's
history. The CSV extracts merge those variants into **one column named by the
current datasheet definition**, so a parameter forms a single continuous series.
Only rules that can't change meaning are applied automatically:

| # | Rule | Example |
| --- | --- | --- |
| 1 | Same `datasheet_record` id — a rename in place, so it's the same field by definition | any label change on one field |
| 2 | Labels equal once case, whitespace, quotes and punctuation are normalised | `Ph` → `pH` |
| 3 | A legacy label matching a current label after each side's trailing unit/qualifier parenthetical is dropped — **and exactly one** current field matches | `Electrical Conductivity` → `Electrical Conductivity (mS / uS)` |

Two guard rails keep this safe on scientific data:

- **Live fields are never merged into each other.** If a rule would join two
  fields the datasheet still defines, the whole group is left alone and the
  collision is reported — distinct current fields are distinct on purpose.
- **Ambiguity is never guessed.** A legacy label matching zero or several
  current fields keeps its own column and is reported, in the log, in the
  datasheet's page (with candidate targets) and under `field_name_merges` in
  `manifest.json`.

Those leftovers are resolved by hand in `projects/<slug>/field_aliases.json`,
which overrides every rule above. The script reads it and never rewrites it:

```jsonc
{
  "dover-landcare-water-quality": {          // datasheet slug, name, or "*"
    "Temperature (C)": "Water Temperature (C)"
  }
}
```

This project needs exactly one such alias: the legacy `Temperature (C)` (6
observations to Jun 2026) could be claimed by three current fields — `Water`,
`Air` or `Dissolved Oxygen Temperature (C)`. It sat between `Ph` and `Electrical
Conductivity`, i.e. in the Hanna combo meter's readings, so it is mapped to
`Water Temperature (C)`.

Each datasheet's `README.md` gains a **Field name changes** section listing every
merge and its reason, so the CSV columns explain themselves. The markdown
observation tables keep showing names exactly as recorded, and the long CSV
keeps the recorded name in `field_as_recorded` beside the merged `field` — the
raw JSON is never rewritten, so nothing is lost.

Both observation extracts carry the same metadata columns and are sorted
oldest-first, so daily re-runs produce minimal diffs. Photo/document cells hold
the backup-root-relative path of the local copy (e.g.
`files/photos_and_files/<name>.jpg`), matching the `localFile` keys in the JSON;
where a binary was never downloaded, the original URL is kept instead.

#### Photo columns

Each photo field keeps its **own column under its own name** — a datasheet can
define several (e.g. a site-conditions shot and a noteworthy shot), and which
photo answers which prompt is part of the record. The wide CSV's `photos`
column is the union of every photo on the observation, in field order, as a
convenience handle whose name is the same in every datasheet; the per-field
columns are what tell them apart. In the long CSV each photo field gets its own
rows, so `record_type == "image"` selects every photo across the project
without needing to know the field names. `featuredPhoto` is a pointer to a photo
already attached to a field, not a separate upload, so it never produces a
duplicate row; a genuine observation-level upload (attached to no field) is the
only thing listed under `Observation photos`. Values of
private-flagged fields are withheld in the CSVs exactly as they are in the JSON
and markdown.

To regenerate the markdown and CSV views from the JSON already in `data/`
without contacting the API (no credentials needed):

```bash
python3 scripts/citsci_backup.py --render-only
```

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

Re-render only the markdown views and CSV extracts from the JSON already in
`./data` (no API calls, no credentials):

```bash
python3 scripts/citsci_backup.py --render-only
```

## Historic data

Curated historic datasets that predate (or sit outside) the automated CitSci
backup live under [`historic-data/`](historic-data/), kept separate from `data/`
so a backup run never touches them. The backup script only ever writes under
`data/`. See [`historic-data/README.md`](historic-data/README.md) for the
catalogue. This is third-party material (original source data plus Dover
Landcare's reformatting/derivations) and is **not** licensed for reuse — see
each dataset's `COPYRIGHT.md` and [`LICENSE.md`](LICENSE.md).

## License

Brief summary — see [`LICENSE.md`](LICENSE.md) for authoritative terms:

- **Data & documents created by the project and its contributors** (`data/`) —
  **CC BY 4.0** (credit Dover Landcare Tasmania; no implied endorsement; no
  rights to names/logos/trademarks).
- **Code** (`scripts/`, `.github/workflows/`) — **MIT**.
- **Third-party material** — uploaded project resources captured in `data/`, and
  everything under `historic-data/` — owned by others and **not** licensed for
  reuse; seek permission first.

All of it is provided **as is, without warranty or liability**.

## API reference

The CitSci OpenAPI 3.1 specification is vendored at
[`spec/citsci-openapi.json`](spec/citsci-openapi.json) for reference. It is
served live at `https://api.citsci.org/docs.jsonopenapi`.
