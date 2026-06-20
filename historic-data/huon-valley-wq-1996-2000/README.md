# Huon Valley Water Quality Report 1996–2000 — Dataset Archive

> **About this package.** This is the *full archive*: the curated clean tables
> (`02_clean/`), the cell-for-cell verbatim worksheet dump (`01_original_verbatim/`),
> the documentation, and the original source workbook
> (`Otley_2001_site_coordinates_and_summary_stats.xlsx`, the authoritative
> reference copy). For convenience, the same documentation and every data table
> are also bundled into a single Markdown file,
> `Otley_2001_single-file_archive.md`, for tools or repositories that prefer one
> file over many. A scanned **partial extract of the original report**
> (chapters 4.10–4.18) is also included as
> `Otley_2000_Huon_water_quality_report_ch4.10_to_4.18.pdf`.

This archive preserves the water-quality dataset underlying the **Huon Valley
Water Quality Report 1996–2000** (Tasmania). The data covers monitoring sites
across the Huon Valley catchment.

**Source / citation:** Otley, Helen (2001). *Huon Valley Water Quality Report
1996–2000: an aid to catchment management decisions.* Huon Healthy Rivers
Project, March 2001.

The original source workbook is
`Otley_2001_site_coordinates_and_summary_stats.xlsx`. The report was published
in **March 2001** and covers the **1996–2000** monitoring period; the "2001" in
the filename refers to the report's publication year. The original filename has
been retained unchanged for traceability. ("Otley" in the filename is the
author, Helen Otley.)

The workbook has been converted to plain-text CSV for long-term preservation and
ease of reuse.

CSV was chosen as the archival format because it is non-proprietary, plain-text,
human-readable, and openable by virtually any analysis tool (R, Python, QGIS,
spreadsheets, text editors) without special libraries or risk of format
obsolescence.

All files are **UTF-8 encoded** with comma delimiters and `CRLF` line endings.
The `°` (degree) and other non-ASCII characters require a UTF-8-aware reader.

---

## Important: original data vs. later enhancements

To keep provenance honest, this archive distinguishes between what is **original
source data** and what was **added later** by a separate data-enhancement effort.

**Original source data** (from `Otley_2001_site_coordinates_and_summary_stats.xlsx`):
- Site identifiers
- **Easting and Northing only** (AGD66, UTM Zone 55) — the sole location
  information in the original
- All water-quality summary statistics (the measurement tables)

**Added by the later enhancement effort (NOT original source data):**
- **Latitude and Longitude (GDA94)** — derived from the original eastings/northings
- **Google Maps and Apple Maps links** — generated from the derived lat/long

The original workbook contained **no** latitude, longitude, or map links; its
coordinate sheet held easting/northing only. The latitude/longitude were computed
from those eastings/northings using a documented AGD66→GDA94 datum
transformation, and the map links were then built from the computed lat/long.
The full method is recorded in the accompanying file
`AGD66_to_GDA94_Conversion_Methodology.md`.

Practical implications for reuse:
- Treat easting/northing as the **authoritative, original** location record.
- Treat lat/long and map links as **convenience derivations** (~1 m accuracy
  from the national 7-parameter transformation; see the methodology document for
  accuracy caveats and the higher-accuracy NTv2 alternative).
- Map links are convenience artefacts and may rot over time.

---

## Directory structure

```
.
├── README.md                                              <- this file
├── COPYRIGHT.md                                           <- copyright / use notice
├── AGD66_to_GDA94_Conversion_Methodology.md               <- how lat/long + links were derived
├── Otley_2001_single-file_archive.md                      <- all docs + every table bundled in one file
├── Otley_2000_Huon_water_quality_report_ch4.10_to_4.18.pdf <- ORIGINAL report (partial extract, chs 4.10–4.18)
├── Otley_2001_site_coordinates_and_summary_stats.xlsx     <- ORIGINAL source workbook (unaltered)
├── 01_original_verbatim/         <- every sheet of the enhanced workbook, dumped exactly as-is
│   ├── site_coordinates.csv
│   ├── as_printed.csv
│   ├── temp.csv
│   ├── do.csv
│   ├── turb.csv
│   ├── ec.csv
│   ├── ph.csv
│   ├── phos.csv
│   └── e_coli.csv
└── 02_clean/                     <- curated working set
    ├── site_coordinates.csv
    └── water_quality.csv
```

### `01_original_verbatim/` — faithful copies
One CSV per worksheet, reproducing the cell contents **exactly** as exported.
No values were changed, added, or removed. Empty cells become empty CSV fields
(CSV has no concept of a null). Blank separator rows and trailing empty columns
are preserved. Use these files if you need the unmodified record of the
worksheet contents.

Note: the `site_coordinates.csv` in this folder includes the **derived** lat/long
and map-link columns (the enhancement), because the verbatim set documents the
worksheet as it stood after enhancement. The original easting/northing values
within it are unchanged from source. For the pristine original (easting/northing
only), see `Otley_2001_site_coordinates_and_summary_stats.xlsx`.

### `02_clean/` — curated working set
A reduced, tidier set intended for day-to-day analysis. It applies structural
tidying **and** corrects definite, unambiguous transcription errors (misspellings
and clear digit-for-letter typos), while leaving any value that requires a
judgement about the measurement itself (such as censored `<7` values) untouched.
See "What was changed in the clean set" below for the complete, itemised list.
The seven per-parameter worksheets are **omitted here** because they are subsets
of the master table (`water_quality.csv`) and contain only duplicates and a few
transcription variants of rows already present in the master (documented below).
Nothing unique to those sheets is lost — the verbatim copies retain everything.

---

## File contents

### `site_coordinates.csv`
Lookup table of monitoring site locations.

| Column | Description | Origin |
|---|---|---|
| `Site` | Site identifier (e.g. `AGN010`) | original |
| `Easting (AGD66 UTM Z55)` | Easting, AGD66 datum, UTM Zone 55 (≈ EPSG:20255) | original |
| `Northing (AGD66 UTM Z55)` | Northing, AGD66 datum, UTM Zone 55 (≈ EPSG:20255) | original |
| `Latitude (GDA94)` | Latitude, GDA94 datum (≈ EPSG:4283) | **derived (enhancement)** |
| `Longitude (GDA94)` | Longitude, GDA94 datum (≈ EPSG:4283) | **derived (enhancement)** |
| `Google Maps` | Google Maps URL for the site's coordinates | **derived (enhancement)** |
| `Apple Maps` | Apple Maps URL for the site's coordinates | **derived (enhancement)** |

> The `Google Maps` / `Apple Maps` columns originally displayed the word "Open"
> as clickable hyperlinks in the enhanced workbook. The underlying URL has been
> extracted into the cell value so the link is preserved in plain text (CSV
> cannot store a hidden hyperlink). Both URLs derive from the computed GDA94
> latitude/longitude. See `AGD66_to_GDA94_Conversion_Methodology.md` for how the
> coordinates and links were produced.

The verbatim version contains 131 site rows plus 34 blank separator rows
(used in the original as visual spacing between site groups). The clean version
contains the 131 site rows only.

**Coordinate reference systems** (record these — coordinates are meaningless
without a stated datum):
- Easting/Northing: AGD66, UTM Zone 55 South. EPSG:20255 is the conventional
  code. **This is the original measured location data.**
- Latitude/Longitude: GDA94 geographic. EPSG:4283. **Derived** from the
  easting/northing via the AGD66→GDA94 7-parameter Helmert transformation
  (~1 m accuracy).
  (These EPSG codes are provided here as guidance and are **not** written into
  the data files, which retain the original column labels.)

### `water_quality.csv` (clean) / `as_printed.csv` (verbatim)
The master measurement table, in long format (one row per site × parameter).
Summary statistics, not raw observations. All original source data.

| Column | Description |
|---|---|
| `Zone` | Catchment zone (East, West, North, Upper, …) |
| `Site` | Site identifier; joins to `site_coordinates.csv` |
| `Parameter` | Measured parameter and unit |
| `No.samples` | Number of samples the statistics summarise |
| `Median` | Median value |
| `Minimum` | Minimum value |
| `25%quartile` | First quartile |
| `75%quartile` | Third quartile |
| `Maximum` | Maximum value |
| `Mean` | Mean value |

Parameters present (master table, 476 rows): Turbidity (NTU), Conductivity
(uS/cm), pH, Water temperature (°C), Ortho-phosphate (mg/L), Total phosphate
(mg/L), Dissolved oxygen (mg/L), % saturation, and E. coli (counts/100 ml).

---

## What was changed in the clean set (and only there)

The clean files aim to be as clean and faithful a representation of the source
data as possible: structural tidying **plus** correction of *definite,
unambiguous* transcription errors. Anything requiring a judgement call about the
underlying measurement (e.g. censored `<7` values) was **left untouched** for the
data user to decide. The verbatim set (`01_original_verbatim/`) retains every
value as exported.

### Structural changes
1. **Header whitespace trimmed.** The original `Mean ` header (trailing space)
   became `Mean`. Other headers left as-is.
2. **Stray trailing column dropped.** The "As printed" sheet had an empty 11th
   column; omitted in `water_quality.csv`.
3. **Blank separator rows dropped.** Empty spacing rows in the coordinate sheet
   are removed in the clean version (kept in verbatim).
4. **Redundant per-parameter sheets omitted** (see above).

### Definite error corrections (data cells)
Each correction below is an unambiguous transcription error — a misspelling, a
stray double space, or a single digit-for-letter confusion (`0`↔`O`, `6`↔`G`,
`3`↔`S`) where exactly one valid target exists. Where a site-code fix was made,
it also reconciles the site between `water_quality.csv` and
`site_coordinates.csv`. Counts are rows affected.

**Parameter labels (`water_quality.csv`):**
- `E. coil (counts/100 ml)` → `E. coli (counts/100 ml)` — 34 rows (misspelling of
  *Escherichia coli*)
- `Water  temperature (°C)` → `Water temperature (°C)` — 8 rows (double space)
- `Dissolved oxygen  (mg/L)  ` → `Dissolved oxygen (mg/L)` — 1 row (double/trailing space)
- `%  saturation` → `% saturation` — 1 row (double space)

**Site codes (`water_quality.csv`):**
- `HU0140` → `HUO140`, `HU0150` → `HUO150`, `HU0200` → `HUO200`,
  `HU0240` → `HUO240` — `0` (zero) typed for `O` (letter); 4 rows each
- `M0U600` → `MOU600` — `0` for `O`; 1 row
- `RU3070` → `RUS070` — `3` for `S`; 1 row

**Site code (`site_coordinates.csv`):**
- `A6N245` → `AGN245` — `6` for `G`; 1 row. (`AGN245` is the form used in
  `water_quality.csv` and matches the `AGN200/245/249/250/260` series.)

Total: 63 cell edits, all in the clean set.

---

## Known data quirks (left as-is; for the analyst to decide)

These were intentionally **not** changed, because correcting them would require a
decision about the underlying measurement rather than fixing an obvious
transcription slip. Handle them in your own analysis as appropriate.

- **Censored / below-detection values.** Turbidity and some other fields contain
  the literal text `<7` (and trailing-space variants like `<7 `) in otherwise
  numeric columns. These indicate a value below the detection limit (turbidity
  detection limit appears to be 7 NTU). Because they are text, affected columns
  will not parse as purely numeric without handling. **Left as-is in both the
  clean and verbatim sets** — how to treat non-detects is the analyst's call.
- **Total vs ortho-phosphate.** The data distinguishes `Ortho-phosphate (mg/L)`
  (41 rows) from `Total phosphate (mg/L)` (4 rows). These are different
  measurements and were **not** merged.
- **Unmatched site codes (ambiguous — not corrected).** After the definite fixes
  above, five sites in `water_quality.csv` still have no matching row in
  `site_coordinates.csv`. Each *might* be a typo, but each has either zero or
  several plausible targets, so changing it could fabricate a location. They are
  left unchanged for you to judge:
  - `FOU120` (no coord; near `FOU100`/`FOU150`)
  - `JUD180` (no coord; near `JUD100`)
  - `KER600` (no coord; near `KER200`/`KER400`/`KER650`/`KER700`/`KER800`)
  - `ROS070` (no coord; near `RUS070`, which already exists separately)
  - `STT350` (no coord; near `STT300`)
  Conversely, some sites have coordinates but no measurements — that is expected
  and not an error.
- **BAK200 Turbidity sample count.** The clean `water_quality.csv` already shows
  the correct `No.samples` value of `8` for this row (it is built from the master
  `as_printed` sheet). The OCR-style `a`-for-`8` error appears **only** in the
  redundant verbatim per-parameter file `turb.csv`, which is not part of the
  clean set. No action needed in the clean set.
- **WOL100 E. coli duplicate.** The clean `water_quality.csv` contains a single
  WOL100 E. coli row, correctly spelled `E. coli` (the `E. coil`→`E. coli`
  correction was applied). The duplicate (one `E. coil`, one `E. coli`) existed
  **only** in the redundant verbatim per-parameter file `e_coli.csv`. The clean
  set is unaffected.

---

## Provenance

- **Original source workbook:** `Otley_2001_site_coordinates_and_summary_stats.xlsx`
  — contains site identifiers, easting/northing (AGD66 UTM Z55), and the
  water-quality summary statistics. Retained unaltered as the reference copy.
- **Original report (partial extract):**
  `Otley_2000_Huon_water_quality_report_ch4.10_to_4.18.pdf` — a partial extract
  of the original report (chapters 4.10–4.18), included as supporting context for
  the data. This is a copyrighted source document, not data derived by this
  archive; see `COPYRIGHT.md`.
- **Enhancement:** latitude/longitude (GDA94) and Google/Apple Maps links were
  derived from the original eastings/northings in a separate effort. Method
  documented in `AGD66_to_GDA94_Conversion_Methodology.md`. These derived fields
  are clearly flagged above and are **not** part of the original source data.
- **CSV conversion:** worksheets exported to CSV. The verbatim set is a faithful
  cell-for-cell dump; the clean set applies the structural changes and definite
  error corrections itemised above.
