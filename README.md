# tlcww — CitSci.org Backup

Automated backups of a [CitSci.org](https://citsci.org) account and its
projects, using the CitSci API (`https://api.citsci.org`).

A scheduled GitHub Action logs in with your account credentials, walks the
account and every project you own/manage, and commits a structured snapshot
(JSON metadata **and** photo/file binaries) back into this repository.

## Setup

1. Create (or reuse) a CitSci account that has access to the projects you want
   to back up.
2. In this repo, go to **Settings → Secrets and variables → Actions** and add:

   | Secret | Required | Purpose |
   | --- | --- | --- |
   | `CITSCI_USER` | yes | Account email used to log in |
   | `CITSCI_PASS` | yes | Account password |
   | `CITSCI_USER_ID` | optional | Your user id — only needed if it can't be auto-resolved from the login token |
   | `CITSCI_FILES_BASE` | optional | Base URL for downloading photo/file binaries when a file record stores only a relative path |

3. Run it: **Actions → CitSci Backup → Run workflow** (or wait for the weekly
   schedule). The first manual run is the easiest way to confirm credentials
   and the resolved user id are correct.

## Schedule

- **Weekly**, Mondays at 06:00 UTC (`.github/workflows/backup.yml`).
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
│       ├── locations.json
│       ├── resources.json
│       ├── project_posts.json
│       ├── invites.json
│       ├── observations.json      # all observations in the project
│       └── datasheets/
│           └── <datasheet-slug>/
│               ├── datasheet.json
│               └── records.json
└── files/
    ├── index.json                 # metadata for every file object
    ├── _download_errors.json      # any binaries that couldn't be fetched
    └── photos/                    # downloaded photo/file binaries
```

### Notes

- **Credentials are never written to disk.** Password and third-party tokens
  (Google, Airtable, SciStarter, reCAPTCHA, JWTs) are stripped from saved JSON.
- **Photo/file downloads are best-effort.** File records expose a `file` /
  `path`; if the binary lives at a relative path, set `CITSCI_FILES_BASE` so
  the script can build the full URL. Anything that fails to download is recorded
  in `files/_download_errors.json` and does not stop the run.
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

## API reference

The CitSci OpenAPI 3.1 specification is vendored at
[`spec/citsci-openapi.json`](spec/citsci-openapi.json) for reference. It is
served live at `https://api.citsci.org/docs.jsonopenapi`.
