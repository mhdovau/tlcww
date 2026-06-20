# Historic data

Curated **historic** datasets that predate, or sit outside, the automated
CitSci.org backup. These are added and maintained by hand — the backup workflow
(`scripts/citsci_backup.py`) never touches anything here; it only ever writes
under `data/`.

Keeping this directory separate from `data/` means a backup run can never
overwrite, reorganise, or flag these files as orphaned. Each dataset lives in
its own subdirectory with its own README, copyright/use notice, and provenance.

## Datasets

| Directory | Dataset | Period | Source |
| --- | --- | --- | --- |
| [`huon-valley-wq-1996-2000/`](huon-valley-wq-1996-2000/) | Huon Valley Water Quality Report — site coordinates and summary statistics | 1996–2000 | Otley, H. (2001), Huon Healthy Rivers Project |

## Use / copyright

These datasets are **not** Dover Landcare's work and are **not** covered by this
repository's `LICENSE.md`. Each carries its own `COPYRIGHT.md` — read it before
reusing the data. In particular, the Huon Valley dataset has **no licence
granted**; permission must be sought from the original author / project.
