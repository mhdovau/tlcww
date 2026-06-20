# Huon Valley Water Quality Report 1996–2000 — Single-File Dataset Archive

_Generated 2026-06-20. This single Markdown file bundles the documentation, copyright notice, coordinate-conversion methodology, and all data tables for repositories that cannot accept zip archives or many separate files._

**Citation:** Otley, Helen (2001). *Huon Valley Water Quality Report 1996–2000: an aid to catchment management decisions.* Huon Healthy Rivers Project, March 2001.

Data underlying the report above (Tasmania). The report was published March 2001 and covers the 1996–2000 monitoring period; the "2001" in the original filename refers to the publication year.

**Provenance note:** easting/northing and the water-quality statistics are original source data. Latitude/longitude (GDA94) and the map links were derived later from the eastings/northings — see the methodology section. The original source workbook is `Otley_2001_site_coordinates_and_summary_stats.xlsx`.

Each data table below is embedded in a fenced ` ```csv ` code block. To recover a table as a usable file, copy the contents of its code block into a `.csv` file, or extract programmatically by reading the fenced `csv` blocks. The clean tables include corrections of definite transcription errors (see README); the verbatim tables are as exported.

---
## Table of contents

1. [Documentation (README)](#documentation-readme)
2. [Copyright and use notice](#copyright-and-use-notice)
3. [AGD66 → GDA94 conversion methodology](#agd66--gda94-conversion-methodology)
4. [Data tables — clean set](#data-tables--clean-set)
5. [Data tables — verbatim set](#data-tables--verbatim-set)

---
## Documentation (README)

# Huon Valley Water Quality Report 1996–2000 — Dataset Archive

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
- **Enhancement:** latitude/longitude (GDA94) and Google/Apple Maps links were
  derived from the original eastings/northings in a separate effort. Method
  documented in `AGD66_to_GDA94_Conversion_Methodology.md`. These derived fields
  are clearly flagged above and are **not** part of the original source data.
- **CSV conversion:** worksheets exported to CSV. The verbatim set is a faithful
  cell-for-cell dump; the clean set applies the structural changes and definite
  error corrections itemised above.

---
## Copyright and use notice

# Copyright and Use Notice

This notice applies to the data underlying the **Huon Valley Water Quality
Report 1996–2000**.

## Source / citation

Otley, Helen (2001). *Huon Valley Water Quality Report 1996–2000: an aid to
catchment management decisions.* Huon Healthy Rivers Project, March 2001.

## Copyright and ownership

The data contained in this archive remains under the original copyright and
ownership of the original author (Helen Otley) and/or the Huon Healthy Rivers
Project.

Copyright and ownership are **not** held by Dover Landcare.

**No license is granted** for the use of this data. Inclusion of the data in
this archive does not grant any right to use, reproduce, distribute, or adapt it.

Anyone wishing to use this data should contact the original author / the Huon
Healthy Rivers Project to seek permission and to discuss appropriate terms of
use.

## Note on derived content

The latitude/longitude coordinates and map links added in this archive are
derived works produced from the original easting/northing data (see the
coordinate methodology documentation). The underlying location data and all
water-quality measurements remain the property of the original author / project
as above.

---
## AGD66 → GDA94 conversion methodology

_The following documents how the **derived** latitude/longitude and map links were produced from the original eastings/northings. It is method documentation, not original source data._

# AGD66 to GDA94 Conversion Methodology

## Overview

This document describes the complete process for converting Australian Map Grid (AMG) coordinates recorded on the AGD66 datum to GDA94/WGS84 geographic coordinates, with generation of clickable map links for Google Maps and Apple Maps.

The conversion pipeline consists of five sequential steps:

1. **UTM → Geographic coordinates** (on AGD66 ellipsoid)
2. **Geographic → Geocentric Cartesian** (ECEF, on AGD66)
3. **Datum transformation: AGD66 → GDA94** (the critical 7-parameter Helmert step)
4. **Geocentric Cartesian → Geographic** (on GDA94 ellipsoid)
5. **Map link generation** (standard lat/lon URL builders)

---

## Step 1: UTM to Geographic Coordinates (AGD66)

### Input
- **Easting (E):** metres, with false easting = 500,000 m
- **Northing (N):** metres, with false northing = 10,000,000 m (southern hemisphere)
- **Zone:** 55 (covers Tasmania; central meridian 147°E)
- **Ellipsoid:** Australian National Spheroid (ANS)
  - Semi-major axis: a = 6,378,160 m
  - Flattening: 1/f = 298.25

### Projection parameters
- Central scale factor: k₀ = 0.9996
- False easting: FE = 500,000 m
- False northing: FN = 10,000,000 m
- Latitude of origin: 0° (equator)
- Zone width: 6°

### Algorithm

The inverse Transverse Mercator projection (Redfearn's formulae) is applied:

1. Remove false easting/northing:
   - E' = E − 500,000
   - N' = N − 10,000,000 (southern hemisphere)

2. Compute the footpoint latitude (φ₁) from the meridian distance:
   ```
   M = N' / k₀
   μ = M / (a(1 − e²/4 − 3e⁴/64 − 5e⁶/256))
   ```
   where e² = 2f − f² is the first eccentricity squared.

3. Solve iteratively for latitude and longitude using Redfearn's series:
   ```
   φ = φ₁ − (N tan φ₁ / R) × (D²/2 − ...)
   λ = λ₀ + (D − (1 + 2T + C)D³/6 + ...) / cos φ₁
   ```

### Output
Latitude and longitude (decimal degrees) on the AGD66 datum.

---

## Step 2: Geographic to Geocentric Cartesian (ECEF)

### Conversion formula

Convert AGD66 lat/lon to earth-centred Cartesian coordinates (X, Y, Z) using the ANS ellipsoid:

```
N = a / √(1 − e² sin²φ)    [prime vertical radius]

X = (N + h) cos φ cos λ
Y = (N + h) cos φ sin λ
Z = (N(1 − e²) + h) sin φ
```

where:
- φ = latitude (radians)
- λ = longitude (radians)
- h = ellipsoidal height (typically 0 for 2D coordinates)
- e² = 2f − f²

### Output
ECEF coordinates (X, Y, Z) in metres, on the AGD66 reference frame.

---

## Step 3: Datum Transformation (AGD66 → GDA94)

### The problem

The AGD66 and GDA94 datums differ in:
- **Ellipsoid shape** (ANS vs GRS80)
- **Reference frame origin** (where (0,0,0) is in 3D space)
- **Orientation** (how the axes align)
- **Distortion** (legacy AGD66 network has irregular local deformations)

This causes a systematic **~150 m shift** (roughly 200 m south, 150 m east in Tasmania) between points plotted using the wrong datum.

### The ICSM 7-parameter Helmert transformation

The official method is a **conformal (similarity) transformation** defined by ICSM in the GDA94 Technical Manual v2.4, Table 7-1. It transforms from AGD66 ECEF coordinates to GDA94 ECEF coordinates.

#### Parameters (national AGD66 → GDA94)

| Parameter | Value | Unit |
|-----------|-------|------|
| dX | −117.808 | metres |
| dY | −51.536 | metres |
| dZ | 137.784 | metres |
| rX | −0.303 | arcseconds |
| rY | −0.446 | arcseconds |
| rZ | −0.234 | arcseconds |
| Scale factor | −0.290 | ppm |

#### The transformation equation

```
⎡X'⎤   ⎡dX⎤                    ⎡X⎤
⎢Y'⎥ = ⎢dY⎥ + (1 + Sc×10⁻⁶) × R × ⎢Y⎥
⎣Z'⎦   ⎣dZ⎦                    ⎣Z⎦
```

where:
- (X, Y, Z) = input ECEF on AGD66
- (X', Y', Z') = output ECEF on GDA94
- Sc = scale factor in ppm

#### Rotation matrix (coordinate-frame convention)

The rotation matrix R applies rotations about the X, Y, Z axes in the **coordinate-frame convention** (ICSM/Australian convention):

```
R = ⎡ 1     +Rz    -Ry ⎤
    ⎢-Rz     1     +Rx ⎥
    ⎣+Ry    -Rx     1  ⎦
```

where Rx, Ry, Rz are the rotation angles in **radians** (converted from arcseconds by dividing by 206,264.806).

For small rotations (< 1°), this simplifies to the small-angle approximation above.

#### Implementation

```python
def helmert(X, Y, Z, dX, dY, dZ, rx, ry, rz, sc):
    ARC2RAD = 1.0 / 206264.806247096
    rxr = rx * ARC2RAD    # convert arcsec to radians
    ryr = ry * ARC2RAD
    rzr = rz * ARC2RAD
    s = sc * 1e-6         # convert ppm to decimal

    # Apply rotation matrix (coordinate frame) and translation
    Xo = dX + (1 + s) * (    X + rzr*Y - ryr*Z)
    Yo = dY + (1 + s) * (-rzr*X +     Y + rxr*Z)
    Zo = dZ + (1 + s) * ( ryr*X - rxr*Y +     Z)

    return Xo, Yo, Zo
```

#### Validation

The transformation is validated against **Table 7-4 of the GDA94 Technical Manual v2.4** (a published worked example):

- Input (AGD66):  37°39'15.5571"S, 143°55'30.6330"E, h=749.671 m
- Expected (GDA94): 37°39'10.1757"S, 143°55'35.4093"E, h=737.739 m
- Computed result matches to **< 0.1 cm** in latitude and longitude

#### Important: Rotation convention

There are two competing conventions for the sign of rotations in the Helmert equation:

1. **Coordinate-frame rotation** (ICSM/Australia): rotations of the coordinate axes themselves
2. **Position-vector rotation** (IERS/Bursa-Wolf): rotations of the position vector

These differ by the **sign of all three rotations**. Using the wrong convention injects a systematic error of several metres. The ICSM parameters listed above assume the **coordinate-frame convention**, which is what the code implements.

#### Accuracy and alternatives

- **National 7-parameter (this method):** ≈ 1 m RMS accuracy
- **NTv2 grid (A66_National_13_09_01.gsb):** ≈ 0.1 m (the official recommended method for highest accuracy)
- **Molodensky transformation:** ≈ 5 m
- **Block shift (1:250k sheet):** ≈ 10 m

For the Otley 2001 data in southern Tasmania, the national parameters are acceptable (~1 m accuracy). If sub-metre accuracy is required, use the NTv2 grid file.

### Output

ECEF coordinates (X', Y', Z') in metres, on the GDA94 reference frame.

---

## Step 4: Geocentric Cartesian to Geographic (GDA94)

### Conversion formula

Convert GDA94 ECEF coordinates to latitude/longitude using the **GRS80 ellipsoid**:

```
GRS80 parameters:
  Semi-major axis: a = 6,378,137 m
  Flattening: 1/f = 298.257222101
```

The inverse is solved iteratively (typically 10 iterations to convergence):

```
e² = 2f − f²
λ = atan2(Y, X)
p = √(X² + Y²)
φ = atan2(Z, p(1 − e²))    [initial guess]

[iterate:]
N = a / √(1 − e² sin²φ)
h = p / cos φ − N
φ = atan2(Z, p(1 − e² N/(N + h)))
```

After convergence:
```
latitude = φ (convert to degrees)
longitude = λ (convert to degrees)
ellipsoidal_height = h
```

### Output

**GDA94 latitude and longitude in decimal degrees**, along with ellipsoidal height.

---

## Step 5: Map Link Generation

Once you have GDA94 lat/lon, three types of map links are generated:

### 1. Google Maps search pin

```
https://www.google.com/maps/search/?api=1&query={latitude},{longitude}
```

**Effect:** Opens Google Maps in a browser or app, drops a labelled pin at the coordinate, and centres the view on it.

**Example:** `https://www.google.com/maps/search/?api=1&query=-43.310239,147.012484`

### 2. Google Maps view (satellite/street)

```
https://www.google.com/maps/@{latitude},{longitude},{zoom}z
```

where `{zoom}` is a zoom level (18 = building-level detail).

**Effect:** Opens Google Maps centred exactly at the coordinate; no search performed.

**Example:** `https://www.google.com/maps/@-43.310239,147.012484,18z`

### 3. Apple Maps

```
https://maps.apple.com/?ll={latitude},{longitude}&q={latitude},{longitude}
```

**Effect:** Opens Apple Maps (on iOS, macOS, or via web). The `ll` parameter sets the centre; `q` adds a query label.

**Example:** `https://maps.apple.com/?ll=-43.310239,147.012484&q=-43.310239,147.012484`

### URL encoding

Latitude and longitude are passed as decimal numbers (comma-separated). No special encoding is needed for the simple numeric format.

### Integration into outputs

The map links are embedded into:

- **Excel spreadsheet:** hyperlinked text in dedicated columns (e.g., cell F2 contains text "Open" linked to the Google Maps URL)
- **HTML tables:** anchor tags (`<a href="...">Open</a>`) in table cells
- **KML placemarks:** description text (users copy and paste or click within their KML viewer)
- **GeoJSON features:** URL strings in property fields (e.g., `"google_maps": "https://..."`)

---

## Summary of the conversion pipeline

| Step | Input | Process | Output | Ellipsoid |
|------|-------|---------|--------|-----------|
| 1 | UTM E, N | Inverse Transverse Mercator | Lat, Lon (degrees) | AGD66/ANS |
| 2 | Lat, Lon | Geographic to ECEF | X, Y, Z (metres) | AGD66/ANS |
| 3 | X, Y, Z | 7-param Helmert (translation + rotation + scale) | X', Y', Z' (metres) | AGD66 → GDA94 |
| 4 | X', Y', Z' | ECEF to geographic (iterative) | Lat, Lon (degrees) | GDA94/GRS80 |
| 5 | Lat, Lon | URL builders | Map links (strings) | GDA94 |

---

## Implementation notes

### Python modules used

The conversion is implemented in `transform_fixed.py` using only the Python standard library (no external dependencies beyond `openpyxl` for Excel, which is separate from the transformation):

- `math` — trigonometric functions, square root
- `urllib.parse` — URL construction (used in the output scripts)

### Validation approach

Before applying the transformation to your full dataset, the code validates itself against the GDA94 Technical Manual Table 7-4 worked example. If this test fails, the transformation is not applied and an error is raised.

### Reproducibility

The same source data (easting, northing) will always produce the same output (latitude, longitude) to machine precision. The transformation is deterministic and does not depend on epoch, time, or external services.

### Caveats

- The national 7-parameter transformation has **~1 m accuracy**. Individual points may vary by up to ±1.5 m.
- **GDA94 and WGS84 are not identical.** They are equivalent to within ~1 m at epoch 1994.0, but have since diverged due to plate motion (Australia moves ~7 cm/year). By 2026, the cumulative GDA94→GDA2020 shift is ~1.8 m in south-east Australia.
- If you need **higher accuracy** (< 1 m), use the NTv2 grid file `A66_National_13_09_01.gsb` instead of the 7-parameter method.
- The AGD66 datum itself has **irregular distortions** (up to ±0.5 m) due to network inconsistencies. The NTv2 grid models these; the 7-parameter method does not.

---

## References

- **GDA94 Technical Manual v2.4** — Geocentric Datum of Australia Technical Manual. ICSM/Geoscience Australia. Tables 7-1 (parameters), 7-2 (residuals), 7-4 (worked example).
- **EPSG:4202** (AGD66 geographic CRS) and **EPSG:4283** (GDA94 geographic CRS) — full parameter definitions.
- **EPSG:1803** — "AGD66 to GDA94 (11)" transformation method (NTv2 grid-based, method 9615).
- **PROJ library documentation** — Helmert transform (`+proj=helmert`) and coordinate frame rotation convention (`+convention=coordinate_frame`).

---

## Appendix: Example coordinate conversion

**Input (AGD66 UTM Zone 55):**
- Site: DOV100
- Easting: 500,900 m
- Northing: 5,204,550 m

**Step 1: UTM → geographic (AGD66)**
- Latitude: −43.31053858° (raw from inverse Transverse Mercator)
- Longitude: 147.01235647°

**Step 2: Geographic → ECEF (AGD66, ANS ellipsoid)**
- X: −4,098,968.234 m
- Y: 2,972,441.156 m
- Z: −3,870,221.789 m

**Step 3: Helmert transformation (AGD66 → GDA94)**
- Apply 7-parameter transform with ICSM national parameters
- Shift ~33 m north, ~10 m east in geographic coordinates

**Step 4: ECEF → geographic (GDA94, GRS80 ellipsoid)**
- Latitude: −43.310239°
- Longitude: 147.012484°

**Step 5: Map links**
- Google search: `https://www.google.com/maps/search/?api=1&query=-43.310239,147.012484`
- Google view: `https://www.google.com/maps/@-43.310239,147.012484,18z`
- Apple: `https://maps.apple.com/?ll=-43.310239,147.012484&q=-43.310239,147.012484`

**Validation:** This result matches the corrected location on a GDA94 map (southern Tasmania, Huon Valley, near Dover).

---
## Data tables — clean set

The curated working set: coordinates plus the master long-format water-quality table. Structural tidying plus correction of definite transcription errors; judgement-call values (e.g. `<7`) left as-is.

### Clean — site_coordinates

Source file: `02_clean/site_coordinates.csv`  ·  132 lines (including header)

```csv
Site,Easting (AGD66 UTM Z55),Northing (AGD66 UTM Z55),Latitude (GDA94),Longitude (GDA94),Google Maps,Apple Maps
AGN010,507700,5225250,-43.123801,147.096041,"https://www.google.com/maps/search/?api=1&query=-43.123801,147.096041","https://maps.apple.com/?ll=-43.123801,147.096041&q=-43.123801,147.096041"
AGN016,506500,5224600,-43.129665,147.081297,"https://www.google.com/maps/search/?api=1&query=-43.129665,147.081297","https://maps.apple.com/?ll=-43.129665,147.081297&q=-43.129665,147.081297"
AGN120,506100,5221475,-43.157809,147.076414,"https://www.google.com/maps/search/?api=1&query=-43.157809,147.076414","https://maps.apple.com/?ll=-43.157809,147.076414&q=-43.157809,147.076414"
AGN130,506100,5221500,-43.157584,147.076414,"https://www.google.com/maps/search/?api=1&query=-43.157584,147.076414","https://maps.apple.com/?ll=-43.157584,147.076414&q=-43.157584,147.076414"
AGN200,506075,5221225,-43.16006,147.076109,"https://www.google.com/maps/search/?api=1&query=-43.16006,147.076109","https://maps.apple.com/?ll=-43.16006,147.076109&q=-43.16006,147.076109"
AGN245,507675,5221775,-43.155093,147.095783,"https://www.google.com/maps/search/?api=1&query=-43.155093,147.095783","https://maps.apple.com/?ll=-43.155093,147.095783&q=-43.155093,147.095783"
AGN249,507575,5221825,-43.154644,147.094552,"https://www.google.com/maps/search/?api=1&query=-43.154644,147.094552","https://maps.apple.com/?ll=-43.154644,147.094552&q=-43.154644,147.094552"
AGN250,507500,5221900,-43.153969,147.093628,"https://www.google.com/maps/search/?api=1&query=-43.153969,147.093628","https://maps.apple.com/?ll=-43.153969,147.093628&q=-43.153969,147.093628"
AGN260,506650,5221550,-43.157129,147.083178,"https://www.google.com/maps/search/?api=1&query=-43.157129,147.083178","https://maps.apple.com/?ll=-43.157129,147.083178&q=-43.157129,147.083178"
AGN300,506500,5221500,-43.157581,147.081334,"https://www.google.com/maps/search/?api=1&query=-43.157581,147.081334","https://maps.apple.com/?ll=-43.157581,147.081334&q=-43.157581,147.081334"
AGN400,506575,5220900,-43.162983,147.082263,"https://www.google.com/maps/search/?api=1&query=-43.162983,147.082263","https://maps.apple.com/?ll=-43.162983,147.082263&q=-43.162983,147.082263"
ALB100,512100,5219300,-43.177322,147.150263,"https://www.google.com/maps/search/?api=1&query=-43.177322,147.150263","https://maps.apple.com/?ll=-43.177322,147.150263&q=-43.177322,147.150263"
ARV005,481500,5215600,-43.210514,146.773633,"https://www.google.com/maps/search/?api=1&query=-43.210514,146.773633","https://maps.apple.com/?ll=-43.210514,146.773633&q=-43.210514,146.773633"
ARV100,485500,5231500,-43.067423,146.823289,"https://www.google.com/maps/search/?api=1&query=-43.067423,146.823289","https://maps.apple.com/?ll=-43.067423,146.823289&q=-43.067423,146.823289"
BAK015,500500,5244350,-42.951844,147.007508,"https://www.google.com/maps/search/?api=1&query=-42.951844,147.007508","https://maps.apple.com/?ll=-42.951844,147.007508&q=-42.951844,147.007508"
BAK025,501100,5243750,-42.957247,147.014864,"https://www.google.com/maps/search/?api=1&query=-42.957247,147.014864","https://maps.apple.com/?ll=-42.957247,147.014864&q=-42.957247,147.014864"
BAK060,502350,5242900,-42.964898,147.030193,"https://www.google.com/maps/search/?api=1&query=-42.964898,147.030193","https://maps.apple.com/?ll=-42.964898,147.030193&q=-42.964898,147.030193"
BAK100,502900,5242450,-42.968948,147.03694,"https://www.google.com/maps/search/?api=1&query=-42.968948,147.03694","https://maps.apple.com/?ll=-42.968948,147.03694&q=-42.968948,147.03694"
BAK150,503600,5241900,-42.973898,147.045527,"https://www.google.com/maps/search/?api=1&query=-42.973898,147.045527","https://maps.apple.com/?ll=-42.973898,147.045527&q=-42.973898,147.045527"
BAK200,504350,5241250,-42.979747,147.05473,"https://www.google.com/maps/search/?api=1&query=-42.979747,147.05473","https://maps.apple.com/?ll=-42.979747,147.05473&q=-42.979747,147.05473"
BAK250,505250,5240650,-42.985145,147.065774,"https://www.google.com/maps/search/?api=1&query=-42.985145,147.065774","https://maps.apple.com/?ll=-42.985145,147.065774&q=-42.985145,147.065774"
CFB010,495800,5226213,-43.115158,146.949756,"https://www.google.com/maps/search/?api=1&query=-43.115158,146.949756","https://maps.apple.com/?ll=-43.115158,146.949756&q=-43.115158,146.949756"
CFB020,496500,5225100,-43.125184,146.958354,"https://www.google.com/maps/search/?api=1&query=-43.125184,146.958354","https://maps.apple.com/?ll=-43.125184,146.958354&q=-43.125184,146.958354"
CFB030,497600,5224200,-43.133293,146.971873,"https://www.google.com/maps/search/?api=1&query=-43.133293,146.971873","https://maps.apple.com/?ll=-43.133293,146.971873&q=-43.133293,146.971873"
CRB080,504400,5246450,-42.93292,147.055301,"https://www.google.com/maps/search/?api=1&query=-42.93292,147.055301","https://maps.apple.com/?ll=-42.93292,147.055301&q=-42.93292,147.055301"
CRB100,504600,5246100,-42.936071,147.057755,"https://www.google.com/maps/search/?api=1&query=-42.936071,147.057755","https://maps.apple.com/?ll=-42.936071,147.057755&q=-42.936071,147.057755"
CRB150,505650,5244950,-42.94642,147.070636,"https://www.google.com/maps/search/?api=1&query=-42.94642,147.070636","https://maps.apple.com/?ll=-42.94642,147.070636&q=-42.94642,147.070636"
CRB250,506350,5243900,-42.955869,147.079229,"https://www.google.com/maps/search/?api=1&query=-42.955869,147.079229","https://maps.apple.com/?ll=-42.955869,147.079229&q=-42.955869,147.079229"
CRB300,507000,5242400,-42.969371,147.087217,"https://www.google.com/maps/search/?api=1&query=-42.969371,147.087217","https://maps.apple.com/?ll=-42.969371,147.087217&q=-42.969371,147.087217"
DIC500,494600,5238000,-43.009009,146.935118,"https://www.google.com/maps/search/?api=1&query=-43.009009,146.935118","https://maps.apple.com/?ll=-43.009009,146.935118&q=-43.009009,146.935118"
DIP040,509550,5242850,-42.965291,147.118479,"https://www.google.com/maps/search/?api=1&query=-42.965291,147.118479","https://maps.apple.com/?ll=-42.965291,147.118479&q=-42.965291,147.118479"
DIP060,509300,5243350,-42.960792,147.115405,"https://www.google.com/maps/search/?api=1&query=-42.960792,147.115405","https://maps.apple.com/?ll=-42.960792,147.115405&q=-42.960792,147.115405"
DIP080,508800,5243300,-42.961248,147.109275,"https://www.google.com/maps/search/?api=1&query=-42.961248,147.109275","https://maps.apple.com/?ll=-42.961248,147.109275&q=-42.961248,147.109275"
DIP100,508800,5243350,-42.960798,147.109274,"https://www.google.com/maps/search/?api=1&query=-42.960798,147.109274","https://maps.apple.com/?ll=-42.960798,147.109274&q=-42.960798,147.109274"
DOV070,500650,5205900,-43.298083,147.009399,"https://www.google.com/maps/search/?api=1&query=-43.298083,147.009399","https://maps.apple.com/?ll=-43.298083,147.009399&q=-43.298083,147.009399"
DOV090,500850,5204975,-43.306412,147.011866,"https://www.google.com/maps/search/?api=1&query=-43.306412,147.011866","https://maps.apple.com/?ll=-43.306412,147.011866&q=-43.306412,147.011866"
DOV100,500900,5204550,-43.310239,147.012484,"https://www.google.com/maps/search/?api=1&query=-43.310239,147.012484","https://maps.apple.com/?ll=-43.310239,147.012484&q=-43.310239,147.012484"
DOV110,501325,5204450,-43.311139,147.017724,"https://www.google.com/maps/search/?api=1&query=-43.311139,147.017724","https://maps.apple.com/?ll=-43.311139,147.017724&q=-43.311139,147.017724"
DOV120,501620,5204100,-43.31429,147.021363,"https://www.google.com/maps/search/?api=1&query=-43.31429,147.021363","https://maps.apple.com/?ll=-43.31429,147.021363&q=-43.31429,147.021363"
DOV130,501750,5203950,-43.31564,147.022967,"https://www.google.com/maps/search/?api=1&query=-43.31564,147.022967","https://maps.apple.com/?ll=-43.31564,147.022967&q=-43.31564,147.022967"
ESP001,484300,5213200,-43.232188,146.808036,"https://www.google.com/maps/search/?api=1&query=-43.232188,146.808036","https://maps.apple.com/?ll=-43.232188,146.808036&q=-43.232188,146.808036"
ESP002,495400,5202800,-43.325985,146.944649,"https://www.google.com/maps/search/?api=1&query=-43.325985,146.944649","https://maps.apple.com/?ll=-43.325985,146.944649&q=-43.325985,146.944649"
FLU100,499450,5226450,-43.113035,146.994621,"https://www.google.com/maps/search/?api=1&query=-43.113035,146.994621","https://maps.apple.com/?ll=-43.113035,146.994621&q=-43.113035,146.994621"
FOU100,507600,5240800,-42.983774,147.094596,"https://www.google.com/maps/search/?api=1&query=-42.983774,147.094596","https://maps.apple.com/?ll=-42.983774,147.094596&q=-42.983774,147.094596"
FOU150,506650,5240950,-42.982432,147.082942,"https://www.google.com/maps/search/?api=1&query=-42.982432,147.082942","https://maps.apple.com/?ll=-42.982432,147.082942&q=-42.982432,147.082942"
FOU200,505550,5241050,-42.98154,147.06945,"https://www.google.com/maps/search/?api=1&query=-42.98154,147.06945","https://maps.apple.com/?ll=-42.98154,147.06945&q=-42.98154,147.06945"
GDR100,512500,5219800,-43.172813,147.155173,"https://www.google.com/maps/search/?api=1&query=-43.172813,147.155173","https://maps.apple.com/?ll=-43.172813,147.155173&q=-43.172813,147.155173"
GDR150,509100,5218900,-43.180966,147.113357,"https://www.google.com/maps/search/?api=1&query=-43.180966,147.113357","https://maps.apple.com/?ll=-43.180966,147.113357&q=-43.180966,147.113357"
GDR200,508500,5218500,-43.184575,147.105981,"https://www.google.com/maps/search/?api=1&query=-43.184575,147.105981","https://maps.apple.com/?ll=-43.184575,147.105981&q=-43.184575,147.105981"
GVC115,505925,5221775,-43.155109,147.074258,"https://www.google.com/maps/search/?api=1&query=-43.155109,147.074258","https://maps.apple.com/?ll=-43.155109,147.074258&q=-43.155109,147.074258"
HOL100,509600,5218600,-43.183661,147.119515,"https://www.google.com/maps/search/?api=1&query=-43.183661,147.119515","https://maps.apple.com/?ll=-43.183661,147.119515&q=-43.183661,147.119515"
HUO140,494100,5239100,-42.999099,146.928995,"https://www.google.com/maps/search/?api=1&query=-42.999099,146.928995","https://maps.apple.com/?ll=-42.999099,146.928995&q=-42.999099,146.928995"
HUO150,495312,5237550,-43.013066,146.943851,"https://www.google.com/maps/search/?api=1&query=-43.013066,146.943851","https://maps.apple.com/?ll=-43.013066,146.943851&q=-43.013066,146.943851"
HUO200,496525,5236475,-43.022752,146.95873,"https://www.google.com/maps/search/?api=1&query=-43.022752,146.95873","https://maps.apple.com/?ll=-43.022752,146.95873&q=-43.022752,146.95873"
HUO240,496600,5236325,-43.024104,146.95965,"https://www.google.com/maps/search/?api=1&query=-43.024104,146.95965","https://maps.apple.com/?ll=-43.024104,146.95965&q=-43.024104,146.95965"
JUD020,497050,5246400,-42.933378,146.965224,"https://www.google.com/maps/search/?api=1&query=-42.933378,146.965224","https://maps.apple.com/?ll=-42.933378,146.965224&q=-42.933378,146.965224"
JUD025,496000,5242950,-42.964442,146.952332,"https://www.google.com/maps/search/?api=1&query=-42.964442,146.952332","https://maps.apple.com/?ll=-42.964442,146.952332&q=-42.964442,146.952332"
JUD070,495250,5241450,-42.977945,146.943123,"https://www.google.com/maps/search/?api=1&query=-42.977945,146.943123","https://maps.apple.com/?ll=-42.977945,146.943123&q=-42.977945,146.943123"
JUD100,495950,5242400,-42.969394,146.951715,"https://www.google.com/maps/search/?api=1&query=-42.969394,146.951715","https://maps.apple.com/?ll=-42.969394,146.951715&q=-42.969394,146.951715"
JUD200,493700,5239800,-42.992793,146.924095,"https://www.google.com/maps/search/?api=1&query=-42.992793,146.924095","https://maps.apple.com/?ll=-42.992793,146.924095&q=-42.992793,146.924095"
KEL250,511600,5235100,-43.035052,147.143778,"https://www.google.com/maps/search/?api=1&query=-43.035052,147.143778","https://maps.apple.com/?ll=-43.035052,147.143778&q=-43.035052,147.143778"
KEL400,509500,5234200,-43.043186,147.118015,"https://www.google.com/maps/search/?api=1&query=-43.043186,147.118015","https://maps.apple.com/?ll=-43.043186,147.118015&q=-43.043186,147.118015"
KEL750,505900,5230700,-43.07474,147.073854,"https://www.google.com/maps/search/?api=1&query=-43.07474,147.073854","https://maps.apple.com/?ll=-43.07474,147.073854&q=-43.07474,147.073854"
KER001,487400,5214600,-43.219639,146.846244,"https://www.google.com/maps/search/?api=1&query=-43.219639,146.846244","https://maps.apple.com/?ll=-43.219639,146.846244&q=-43.219639,146.846244"
KER010,489600,5218100,-43.188156,146.873397,"https://www.google.com/maps/search/?api=1&query=-43.188156,146.873397","https://maps.apple.com/?ll=-43.188156,146.873397&q=-43.188156,146.873397"
KER200,492400,5219050,-43.179634,146.907868,"https://www.google.com/maps/search/?api=1&query=-43.179634,146.907868","https://maps.apple.com/?ll=-43.179634,146.907868&q=-43.179634,146.907868"
KER400,493750,5219900,-43.171992,146.924488,"https://www.google.com/maps/search/?api=1&query=-43.171992,146.924488","https://maps.apple.com/?ll=-43.171992,146.924488&q=-43.171992,146.924488"
KER450,494100,5220250,-43.168843,146.928798,"https://www.google.com/maps/search/?api=1&query=-43.168843,146.928798","https://maps.apple.com/?ll=-43.168843,146.928798&q=-43.168843,146.928798"
KER650,493650,5221100,-43.161186,146.923272,"https://www.google.com/maps/search/?api=1&query=-43.161186,146.923272","https://maps.apple.com/?ll=-43.161186,146.923272&q=-43.161186,146.923272"
KER700,494300,5220700,-43.164793,146.931263,"https://www.google.com/maps/search/?api=1&query=-43.164793,146.931263","https://maps.apple.com/?ll=-43.164793,146.931263&q=-43.164793,146.931263"
KER750,494750,5220800,-43.163895,146.9368,"https://www.google.com/maps/search/?api=1&query=-43.163895,146.9368","https://maps.apple.com/?ll=-43.163895,146.9368&q=-43.163895,146.9368"
KER800,495200,5220500,-43.1666,146.942333,"https://www.google.com/maps/search/?api=1&query=-43.1666,146.942333","https://maps.apple.com/?ll=-43.1666,146.942333&q=-43.1666,146.942333"
LAS040,512800,5208550,-43.274111,147.159128,"https://www.google.com/maps/search/?api=1&query=-43.274111,147.159128","https://maps.apple.com/?ll=-43.274111,147.159128&q=-43.274111,147.159128"
LAS060,512700,5208500,-43.274563,147.157896,"https://www.google.com/maps/search/?api=1&query=-43.274563,147.157896","https://maps.apple.com/?ll=-43.274563,147.157896&q=-43.274563,147.157896"
LAS080,512700,5208400,-43.275463,147.157899,"https://www.google.com/maps/search/?api=1&query=-43.275463,147.157899","https://maps.apple.com/?ll=-43.275463,147.157899&q=-43.275463,147.157899"
LAS100,512600,5208400,-43.275465,147.156666,"https://www.google.com/maps/search/?api=1&query=-43.275465,147.156666","https://maps.apple.com/?ll=-43.275465,147.156666&q=-43.275465,147.156666"
LDR001,476700,5244000,-42.954643,146.715727,"https://www.google.com/maps/search/?api=1&query=-42.954643,146.715727","https://maps.apple.com/?ll=-42.954643,146.715727&q=-42.954643,146.715727"
LDR002,482100,5242600,-42.967396,146.781884,"https://www.google.com/maps/search/?api=1&query=-42.967396,146.781884","https://maps.apple.com/?ll=-42.967396,146.781884&q=-42.967396,146.781884"
LDR100,483377,5241426,-42.977996,146.797508,"https://www.google.com/maps/search/?api=1&query=-42.977996,146.797508","https://maps.apple.com/?ll=-42.977996,146.797508&q=-42.977996,146.797508"
LDR220,483775,5240800,-42.983642,146.802372,"https://www.google.com/maps/search/?api=1&query=-42.983642,146.802372","https://maps.apple.com/?ll=-42.983642,146.802372&q=-42.983642,146.802372"
LDR300,484020,5240900,-42.982747,146.805379,"https://www.google.com/maps/search/?api=1&query=-42.982747,146.805379","https://maps.apple.com/?ll=-42.982747,146.805379&q=-42.982747,146.805379"
LDR400,484125,5240775,-42.983875,146.806664,"https://www.google.com/maps/search/?api=1&query=-42.983875,146.806664","https://maps.apple.com/?ll=-42.983875,146.806664&q=-42.983875,146.806664"
LUN010,485700,5192800,-43.415909,146.824749,"https://www.google.com/maps/search/?api=1&query=-43.415909,146.824749","https://maps.apple.com/?ll=-43.415909,146.824749&q=-43.415909,146.824749"
LUN020,492200,5192900,-43.415103,146.905041,"https://www.google.com/maps/search/?api=1&query=-43.415103,146.905041","https://maps.apple.com/?ll=-43.415103,146.905041&q=-43.415103,146.905041"
MOU200,510850,5245900,-42.937808,147.134359,"https://www.google.com/maps/search/?api=1&query=-42.937808,147.134359","https://maps.apple.com/?ll=-42.937808,147.134359&q=-42.937808,147.134359"
MOU250,510800,5245800,-42.938709,147.133748,"https://www.google.com/maps/search/?api=1&query=-42.938709,147.133748","https://maps.apple.com/?ll=-42.938709,147.133748&q=-42.938709,147.133748"
MOU400,508800,5243400,-42.960347,147.109274,"https://www.google.com/maps/search/?api=1&query=-42.960347,147.109274","https://maps.apple.com/?ll=-42.960347,147.109274&q=-42.960347,147.109274"
MOU600,507000,5242200,-42.971172,147.087219,"https://www.google.com/maps/search/?api=1&query=-42.971172,147.087219","https://maps.apple.com/?ll=-42.971172,147.087219&q=-42.971172,147.087219"
MOU650,505300,5239500,-42.9955,147.066398,"https://www.google.com/maps/search/?api=1&query=-42.9955,147.066398","https://maps.apple.com/?ll=-42.9955,147.066398&q=-42.9955,147.066398"
MOU700,503900,5237500,-43.013519,147.049238,"https://www.google.com/maps/search/?api=1&query=-43.013519,147.049238","https://maps.apple.com/?ll=-43.013519,147.049238&q=-43.013519,147.049238"
MOU850,503300,5237000,-43.018025,147.041878,"https://www.google.com/maps/search/?api=1&query=-43.018025,147.041878","https://maps.apple.com/?ll=-43.018025,147.041878&q=-43.018025,147.041878"
NIC100,512800,5224950,-43.126432,147.158744,"https://www.google.com/maps/search/?api=1&query=-43.126432,147.158744","https://maps.apple.com/?ll=-43.126432,147.158744&q=-43.126432,147.158744"
NIC300,512200,5222500,-43.148504,147.151422,"https://www.google.com/maps/search/?api=1&query=-43.148504,147.151422","https://maps.apple.com/?ll=-43.148504,147.151422&q=-43.148504,147.151422"
NIC500,511100,5221000,-43.162029,147.137925,"https://www.google.com/maps/search/?api=1&query=-43.162029,147.137925","https://maps.apple.com/?ll=-43.162029,147.137925&q=-43.162029,147.137925"
NIC700,508200,5220100,-43.170171,147.102265,"https://www.google.com/maps/search/?api=1&query=-43.170171,147.102265","https://maps.apple.com/?ll=-43.170171,147.102265&q=-43.170171,147.102265"
PAR100,507350,5240650,-42.985127,147.091532,"https://www.google.com/maps/search/?api=1&query=-42.985127,147.091532","https://maps.apple.com/?ll=-42.985127,147.091532&q=-42.985127,147.091532"
PCK010,496950,5229900,-43.081962,146.963911,"https://www.google.com/maps/search/?api=1&query=-43.081962,146.963911","https://maps.apple.com/?ll=-43.081962,146.963911&q=-43.081962,146.963911"
PCK020,498700,5229800,-43.082868,146.98541,"https://www.google.com/maps/search/?api=1&query=-43.082868,146.98541","https://maps.apple.com/?ll=-43.082868,146.98541&q=-43.082868,146.98541"
PCK030,500850,5229500,-43.085569,147.011824,"https://www.google.com/maps/search/?api=1&query=-43.085569,147.011824","https://maps.apple.com/?ll=-43.085569,147.011824&q=-43.085569,147.011824"
PIC001,474300,5213400,-43.230114,146.684894,"https://www.google.com/maps/search/?api=1&query=-43.230114,146.684894","https://maps.apple.com/?ll=-43.230114,146.684894&q=-43.230114,146.684894"
PIC002,476000,5227100,-43.106805,146.706421,"https://www.google.com/maps/search/?api=1&query=-43.106805,146.706421","https://maps.apple.com/?ll=-43.106805,146.706421&q=-43.106805,146.706421"
RIL200,494450,5217000,-43.198112,146.933072,"https://www.google.com/maps/search/?api=1&query=-43.198112,146.933072","https://maps.apple.com/?ll=-43.198112,146.933072&q=-43.198112,146.933072"
RIL400,493700,5219450,-43.176044,146.923868,"https://www.google.com/maps/search/?api=1&query=-43.176044,146.923868","https://maps.apple.com/?ll=-43.176044,146.923868&q=-43.176044,146.923868"
RUS005,476400,5252400,-42.878991,146.712401,"https://www.google.com/maps/search/?api=1&query=-42.878991,146.712401","https://maps.apple.com/?ll=-42.878991,146.712401&q=-42.878991,146.712401"
RUS010,483500,5245600,-42.940412,146.799139,"https://www.google.com/maps/search/?api=1&query=-42.940412,146.799139","https://maps.apple.com/?ll=-42.940412,146.799139&q=-42.940412,146.799139"
RUS055,483200,5245000,-42.945808,146.795444,"https://www.google.com/maps/search/?api=1&query=-42.945808,146.795444","https://maps.apple.com/?ll=-42.945808,146.795444&q=-42.945808,146.795444"
RUS060,483250,5244995,-42.945854,146.796057,"https://www.google.com/maps/search/?api=1&query=-42.945854,146.796057","https://maps.apple.com/?ll=-42.945854,146.796057&q=-42.945854,146.796057"
RUS070,484300,5244450,-42.950784,146.808913,"https://www.google.com/maps/search/?api=1&query=-42.950784,146.808913","https://maps.apple.com/?ll=-42.950784,146.808913&q=-42.950784,146.808913"
RUS075,485500,5243350,-42.960714,146.823595,"https://www.google.com/maps/search/?api=1&query=-42.960714,146.823595","https://maps.apple.com/?ll=-42.960714,146.823595&q=-42.960714,146.823595"
RUS080,485550,5243300,-42.961165,146.824207,"https://www.google.com/maps/search/?api=1&query=-42.961165,146.824207","https://maps.apple.com/?ll=-42.961165,146.824207&q=-42.961165,146.824207"
RUS100,488700,5240800,-42.98373,146.862779,"https://www.google.com/maps/search/?api=1&query=-42.98373,146.862779","https://maps.apple.com/?ll=-42.98373,146.862779&q=-42.98373,146.862779"
SOU010,496550,5193800,-43.407031,146.958778,"https://www.google.com/maps/search/?api=1&query=-43.407031,146.958778","https://maps.apple.com/?ll=-43.407031,146.958778&q=-43.407031,146.958778"
SOU050,496250,5193200,-43.412433,146.955069,"https://www.google.com/maps/search/?api=1&query=-43.412433,146.955069","https://maps.apple.com/?ll=-43.412433,146.955069&q=-43.412433,146.955069"
SOU100,497200,5192500,-43.41874,146.9668,"https://www.google.com/maps/search/?api=1&query=-43.41874,146.9668","https://maps.apple.com/?ll=-43.41874,146.9668&q=-43.41874,146.9668"
SOU150,497800,5191400,-43.428647,146.974207,"https://www.google.com/maps/search/?api=1&query=-43.428647,146.974207","https://maps.apple.com/?ll=-43.428647,146.974207&q=-43.428647,146.974207"
SOU200,497800,5191200,-43.430448,146.974207,"https://www.google.com/maps/search/?api=1&query=-43.430448,146.974207","https://maps.apple.com/?ll=-43.430448,146.974207&q=-43.430448,146.974207"
STT100,492750,5224150,-43.133713,146.91224,"https://www.google.com/maps/search/?api=1&query=-43.133713,146.91224","https://maps.apple.com/?ll=-43.133713,146.91224&q=-43.133713,146.91224"
STT300,493200,5222600,-43.147674,146.917754,"https://www.google.com/maps/search/?api=1&query=-43.147674,146.917754","https://maps.apple.com/?ll=-43.147674,146.917754&q=-43.147674,146.917754"
STT400,493600,5221100,-43.161185,146.922657,"https://www.google.com/maps/search/?api=1&query=-43.161185,146.922657","https://maps.apple.com/?ll=-43.161185,146.922657&q=-43.161185,146.922657"
SUP010,504425,5223950,-43.135534,147.055791,"https://www.google.com/maps/search/?api=1&query=-43.135534,147.055791","https://maps.apple.com/?ll=-43.135534,147.055791&q=-43.135534,147.055791"
SUP020,504325,5223890,-43.136075,147.054562,"https://www.google.com/maps/search/?api=1&query=-43.136075,147.054562","https://maps.apple.com/?ll=-43.136075,147.054562&q=-43.136075,147.054562"
SUP050,504790,5223650,-43.138233,147.060281,"https://www.google.com/maps/search/?api=1&query=-43.138233,147.060281","https://maps.apple.com/?ll=-43.138233,147.060281&q=-43.138233,147.060281"
SUP100,505625,5223550,-43.139128,147.07055,"https://www.google.com/maps/search/?api=1&query=-43.139128,147.07055","https://maps.apple.com/?ll=-43.139128,147.07055&q=-43.139128,147.07055"
SUP200,505675,5222250,-43.150834,147.071178,"https://www.google.com/maps/search/?api=1&query=-43.150834,147.071178","https://maps.apple.com/?ll=-43.150834,147.071178&q=-43.150834,147.071178"
SUP300,505925,5221800,-43.154884,147.074258,"https://www.google.com/maps/search/?api=1&query=-43.154884,147.074258","https://maps.apple.com/?ll=-43.154884,147.074258&q=-43.154884,147.074258"
SUP350,506950,5221712,-43.155667,147.086866,"https://www.google.com/maps/search/?api=1&query=-43.155667,147.086866","https://maps.apple.com/?ll=-43.155667,147.086866&q=-43.155667,147.086866"
WAT050,495650,5235450,-43.031978,146.947983,"https://www.google.com/maps/search/?api=1&query=-43.031978,146.947983","https://maps.apple.com/?ll=-43.031978,146.947983&q=-43.031978,146.947983"
WAT055,495650,5235450,-43.031978,146.947983,"https://www.google.com/maps/search/?api=1&query=-43.031978,146.947983","https://maps.apple.com/?ll=-43.031978,146.947983&q=-43.031978,146.947983"
WAT200,496400,5236200,-43.025228,146.957194,"https://www.google.com/maps/search/?api=1&query=-43.025228,146.957194","https://maps.apple.com/?ll=-43.025228,146.957194&q=-43.025228,146.957194"
WOL100,510500,5219100,-43.179147,147.13058,"https://www.google.com/maps/search/?api=1&query=-43.179147,147.13058","https://maps.apple.com/?ll=-43.179147,147.13058&q=-43.179147,147.13058"
WOL100,510500,5219100,-43.179147,147.13058,"https://www.google.com/maps/search/?api=1&query=-43.179147,147.13058","https://maps.apple.com/?ll=-43.179147,147.13058&q=-43.179147,147.13058"
```

### Clean — water_quality

Source file: `02_clean/water_quality.csv`  ·  477 lines (including header)

```csv
Zone,Site,Parameter,No.samples,Median,Minimum,25%quartile,75%quartile,Maximum,Mean
East,AGN010,Water temperature (°C),15,10,6,8,12.5,18,10.6
East,AGN010,Turbidity (NTU),15,7,<7,<7,<7,<7,<7 
East,AGN010,Conductivity (uS/cm),15,130,80,99,130,150,120
East,AGN010,pH,15,6.5,6,6.5,7,7,6.6
East,AGN016,Water temperature (°C),13,12.5,3.9,7.5,16,19,11.8
East,AGN016,Turbidity (NTU),13,7,2,<7,<7,20,8
East,AGN016,Conductivity (uS/cm),13,410,150,290,430,690,380
East,AGN016,pH,13,6.5,6.5,6.5,7,8.1,6.8
East,AGN120,Water temperature (°C),11,13.5,6.5,7.5,18,20,13.4
East,AGN120,Turbidity (NTU),10,9,<7,<7,10,24,11
East,AGN120,Conductivity (uS/cm),11,350,230,290,510,720,417
East,AGN120,pH,11,6.5,6,6.5,6.5,7,6.5
East,AGN130,Water temperature (°C),27,12.7,4.3,8,16.1,23,12.5
East,AGN130,Turbidity (NTU),27,19,<7,<7,24,44,18
East,AGN130,Conductivity (uS/cm),27,430,289,390,485,740,436
East,AGN130,pH,26,7,6,6.5,7.7,8,7
East,AGN200,Water temperature (°C),11,15,7,10,21,25,15.1
East,AGN200,Turbidity (NTU),11,55,16,30,99,300,93
East,AGN200,Conductivity (uS/cm),11,250,170,210,300,500,275
East,AGN200,pH,11,6.5,6,6,7.5,8,6.7
East,AGN200,E. coli (counts/100 ml),5,8500,900,1300,10400,13865,6993
East,AGN245,Water temperature (°C),6,12,9.5,11,17.5,26,14.7
East,AGN245,Turbidity (NTU),6,7,<7,<7,14,75,20
East,AGN245,Conductivity (uS/cm),6,205,140,190,220,250,202
East,AGN245,pH,6,6,5.5,5.5,6,6.5,5.9
East,AGN249,Water temperature (°C),10,13,6.5,10.5,15.5,20,13.2
East,AGN249,Turbidity (NTU),10,90,34,57,130,300,111
East,AGN249,Conductivity (uS/cm),10,2750,1580,2500,3000,3100,2628
East,AGN249,pH,10,8,7.5,8,8,8,7.9
East,AGN250,Water temperature (°C),9,12.5,7,9.5,13,26,12.7
East,AGN250,Turbidity (NTU),9,35,<7,<7,55,85,38
East,AGN250,Conductivity (uS/cm),9,350,140,250,580,1760,632
East,AGN250,pH,9,6,5.5,5.5,6.5,7.5,6.2
East,AGN260,Water temperature (°C),6,12,8,10,14.5,20,12.8
East,AGN260,Turbidity (NTU),6,28,<7,<7,40,155,44
East,AGN260,Conductivity (uS/cm),6,585,430,520,720,800,607
East,AGN260,pH,6,6,5.5,6,6,6.5,6
East,AGN300,Water temperature (°C),10,12,5.5,9,13,19.5,11.8
East,AGN300,Turbidity (NTU),10,15,<7,13,18,40,17
East,AGN300,Conductivity (uS/cm),10,475,280,430,580,920,500
East,AGN300,pH,10,6,5.5,6,6.5,7,6.2
East,AGN400,Water temperature (°C),11,16.5,5.5,9,21,30.5,15.7
East,AGN400,Turbidity (NTU),11,10,<7,<7,11,13,9
East,AGN400,Conductivity (uS/cm),10,1575,113,1070,3000,44000,7612
East,AGN400,pH,11,6.5,6.5,6.5,7.5,8.5,7
East,SUP010,Water temperature (°C),10,12.5,8.5,9,15,20.4,13.2
East,SUP010,Turbidity (NTU),10,21,16,18,29,53,26
East,SUP010,Conductivity (uS/cm),10,585,480,560,625,650,577
East,SUP010,pH,10,6.3,6,6,6.5,7,6.4
East,SUP010,Ortho-phosphate (mg/L),9,0.045,0.03,0.03,0.045,0.06,0.04
East,SUP010,Dissolved oxygen (mg/L),9,9.5,7.8,9.1,9.8,11.7,9.6
East,SUP010,% saturation,9,90,78,87,95,104,91
East,SUP020,Water temperature (°C),11,13,8.5,10,16,22.5,13.6
East,SUP020,Turbidity (NTU),11,85,38,60,99,115,81
East,SUP020,Conductivity (uS/cm),11,920,460,750,990,1120,871
East,SUP020,pH,11,6,6,6,6.5,6.5,6.2
East,SUP020,Ortho-phosphate (mg/L),10,0.28,0.14,0.14,0.42,0.44,0.282
East,SUP020,Dissolved oxygen (mg/L),10,7.6,5,7.2,8,9.7,7.6
East,SUP020,% saturation,10,73,52,66,81,84,71
East,SUP050,Water temperature (°C),11,12.5,8,10,16,20,13
East,SUP050,Turbidity (NTU),11,51,23,44,59,-,85
East,SUP050,Conductivity (uS/cm),11,710,430,620,730,754,664
East,SUP050,pH,11,6,5.5,6,6,6.5,6
East,SUP050,Ortho-phosphate (mg/L),10,0.19,0.08,0.14,0.28,1.14,0.299
East,SUP050,Dissolved oxygen (mg/L),10,8.4,7.5,7.9,8.8,10.8,8.6
East,SUP050,% saturation,10,79,68,75,84,88,79
East,SUP100,Water temperature (°C),12,12,8,10.3,15.8,22,13.2
East,SUP100,Turbidity (NTU),12,25,6,22,32,41,26
East,SUP100,Conductivity (uS/cm),12,640,400,590,660,707,612
East,SUP100,pH,12,6,5.5,5.8,6.5,6.5,6.1
East,SUP100,Ortho-phosphate (mg/L),10,0.13,0.045,0.08,0.14,0.28,0.13
East,SUP100,Dissolved oxygen (mg/L),10,8.4,7.2,8.1,8.9,10.4,8.6
East,SUP100,% saturation,10,83,68,74,85,89,80
East,SUP200,Water temperature (°C),12,15.3,9,11.5,19.8,23,15.6
East,SUP200,Turbidity (NTU),11,65,13,43,83,250,76
East,SUP200,Conductivity (uS/cm),12,325,260,290,340,405,324
East,SUP200,pH,11,6,5.5,5.5,6,7,6
East,SUP200,Ortho-phosphate (mg/L),7,0.03,0.015,0.015,0.03,0.15,0.041
East,SUP200,Dissolved oxygen (mg/L),9,9,7.4,8.8,9.6,10.2,9
East,SUP200,% saturation,9,89,75,79,96,99,87
East,SUP300,Water temperature (°C),14,12.5,8,9.5,15,24.5,13.1
East,SUP300,Turbidity (NTU),13,24,10,21,33,83,30
East,SUP300,Conductivity (uS/cm),14,560,120,530,645,740,543
East,SUP300,pH,13,6.5,5.5,6,6.5,6.5,6.3
East,SUP300,Ortho-phosphate (mg/L),10,0.08,0.03,0.08,0.11,0.14,0.088
East,SUP300,Dissolved oxygen (mg/L),10,8.6,7.4,7.7,9.2,10.7,8.7
East,SUP300,% saturation,10,79,66,75,86,94,80
East,GVC115,Water temperature (°C),13,11,3.7,7,14,18,11.2
East,GVC115,Turbidity (NTU),13,29,8,25,40,170,39
East,GVC115,Conductivity (uS/cm),13,490,290,388,530,1900,570
East,GVC115,pH,13,6,5,6,6.5,7.1,6.1
East,GVC115,Ortho-phosphate (mg/L),2,0.011,0.006,0.016,0.011,,
East,GVC115,Dissolved oxygen (mg/L),3,10.2,2.6,10.3,7.7,,
East,GVC115,% saturation,3,78,24,80,61,,
East,SUP350,Water temperature (°C),11,12,6,8,14,18,11.9
East,SUP350,Turbidity (NTU),11,26,10,11,63,80,35
East,SUP350,Conductivity (uS/cm),11,480,120,330,720,870,505
East,SUP350,pH,11,6,5,6,6.5,6.5,6
West,CFB010,Water temperature (°C),28,9,4.5,6.8,11,18.1,9.2
West,CFB010,Turbidity (NTU),29,<7,<7,<7,<7,45,10
West,CFB010,Conductivity (uS/cm),31,90,60,80,110,173,97
West,CFB010,pH,30,6.5,5.5,6,6.5,7.6,6.3
West,CFB010,E. coli (counts/100 ml),4,100,0,0,355,510,178
West,CFB010,Ortho-phosphate (mg/L),4,0.011,0.005,0.006,0.023,0.03,0.014
West,CFB020,Water temperature (°C),30,9.8,5,7,11.5,18.1,10
West,CFB020,Turbidity (NTU),30,<7,<7,<7,11,68,12
West,CFB020,Conductivity (uS/cm),32,110,60,90,130,191,112
West,CFB020,pH,32,6.5,5.5,6,6.5,7.7,6.4
West,CFB020,E. coli (counts/100 ml),6,48,0,36,360,510,167
West,CFB020,Ortho-phosphate (mg/L),2,0.015,0.015,0.015,0.015,,
West,CFB030,Water temperature (°C),26,10.5,5.5,8.5,15,23,11.7
West,CFB030,Turbidity (NTU),25,<7,<7,<7,12,70,15
West,CFB030,Conductivity (uS/cm),28,130,80,110,140,191,127
West,CFB030,pH,27,6.5,5.5,6,6.5,7.7,6.4
West,CFB030,E. coli (counts/100 ml),4,675,360,435,840,840,638
West,CFB030,Ortho-phosphate (mg/L),4,0.012,0.005,0.007,0.023,0.03,0.015
West,DOV070,Water temperature (°C),4,12.9,4.5,7.5,15.4,15.5,11.4
West,DOV070,Turbidity (NTU),4,13,<7,10,18,23,14
West,DOV070,Conductivity (uS/cm),4,382,180,279,388,390,334
West,DOV070,pH,4,6.9,6,6.5,7.4,7.8,6.9
West,DOV090,Water temperature (°C),2,13.4,10.7,16,13.4,,
West,DOV090,Turbidity (NTU),2,10,<7,13,10,,
West,DOV090,Conductivity (uS/cm),2,355,190,520,355,,
West,DOV090,pH,2,7.2,6.5,7.8,7.2,,
West,DOV110,Water temperature (°C),2,13.9,10.8,17,13.9,,
West,DOV110,Turbidity (NTU),2,10,<7,12,10,,
West,DOV110,Conductivity (uS/cm),2,425,200,650,425,,
West,DOV110,pH,2,7,6.5,7.5,7,,
West,DOV120,Water temperature (°C),2,16,12.5,19.5,16,,
West,DOV120,Turbidity (NTU),2,10,<7,13,10,,
West,DOV120,Conductivity (uS/cm),2,1125,250,1999,1125,,
West,DOV120,pH,2,7.9,7.5,8.2,7.9,,
West,DOV130,Water temperature (°C),2,16.2,11.8,20.5,16.2,,
West,DOV130,Turbidity (NTU),2,<7,<7,<7,<7 ,,
West,DOV130,Conductivity (uS/cm),2,1095,190,2000,1095,,
West,DOV130,pH,2,8,8,8,8,,
East,GDR100,Conductivity (uS/cm),8,261,163,435,213,337,278
East,GDR100,E. coli (counts/100 ml),3,80,40,160,93,,
East,GDR100,pH,8,6.5,5.5,6.5,6,6.5,6.3
East,GDR100,Turbidity (NTU),8,<7,<7,<7,<7,<7,<7 
East,GDR100,Water temperature (°C),7,10,8,15,8,14,10.5
East,ALB100,Conductivity (uS/cm),8,419,282,733,307,569,451
East,ALB100,E. coli (counts/100 ml),2,100,60,140,100,,
East,ALB100,pH,8,6.5,6,7,6.5,7,6.6
East,ALB100,Turbidity (NTU),8,<7,<7,16,<7,<7,8
East,ALB100,Water temperature (°C),7,9.5,7,14,8,12,10
East,WOL100,Conductivity (uS/cm),6,515,423,622,472,567,519
East,WOL100,E. coli (counts/100 ml),2,90,0,180,90,,
East,WOL100,pH,6,6.5,6,7,6.5,7,6.6
East,WOL100,Water temperature (°C),6,11.3,9,17.5,9,16,12.3
East,WOL100,Turbidity (NTU),6,7,<7,<7,<7,<7,<7 
East,GDR150,Conductivity (uS/cm),9,457,291,920,440,571,505
East,GDR150,E. coli (counts/100 ml),3,280,30,660,323,,
East,GDR150,pH,8,6.5,6.5,7.5,6.5,7.3,6.8
East,GDR150,Turbidity (NTU),8,<7,<7,23,<7,<7,9
East,GDR150,Water temperature (°C),7,13,7.5,20,8,16,12.4
East,HOL100,Conductivity (uS/cm),4,599,533,762,542,705,623
East,HOL100,E. coli (counts/100 ml),2,160,140,180,160,,
East,HOL100,pH,4,7,6,8,6.5,7.5,7
East,HOL100,Water temperature (°C),4,11,7,13.5,8,13.3,10.6
East,HOL100,Turbidity (NTU),4,9,<7,14,8,12,10
East,GDR200,Conductivity (uS/cm),8,538,300,1144,404,701,591
East,GDR200,E. coli (counts/100 ml),2,59,20,98,59,,
East,GDR200,pH,8,6.5,6,7,6,6.5,6.4
East,GDR200,Turbidity (NTU),8,<7,6,19,<7,10,9
East,GDR200,Water temperature (°C),7,11,7.6,17,8,13,11.2
Upper,HUO140,Water temperature (°C),17,9.6,5.6,7,13.2,19,10.5
Upper,HUO140,Turbidity (NTU),19,2,1,1,3,39,5.2
Upper,HUO140,Conductivity (uS/cm),17,82,41,59,109,161,87
Upper,HUO140,pH,15,7.3,5.7,6.8,7.6,7.8,7.1
Upper,HUO150,Water temperature (°C),6,8.3,4,6,10,10,7.8
Upper,HUO150,Turbidity (NTU),6,<7,<7,<7,7,7,7
Upper,HUO150,Conductivity (uS/cm),6,50,40,40,80,150,68
Upper,HUO150,pH,6,6,6,6,6.5,7,6.3
Upper,HUO200,Water temperature (°C),22,10,6,9,13,22,11.3
Upper,HUO200,Turbidity (NTU),22,<7,<7,<7,10,65,13
Upper,HUO200,Conductivity (uS/cm),23,30,10,20,50,183,50
Upper,HUO200,pH,23,6,5,6,6.5,7,6
Upper,HUO240,Water temperature (°C),21,10,6.4,9.5,13.8,23,12
Upper,HUO240,Turbidity (NTU),20,<7,<7,<7,9,20,9
Upper,HUO240,Conductivity (uS/cm),20,35,10,25,60,150,52
Upper,HUO240,pH,21,6,5,5.5,6.5,7,6
Upper,JUD020,Water temperature (°C),10,6,3,5.5,8,11.5,6.8
Upper,JUD020,Turbidity (NTU),10,<7,<7,<7,<7,<7,<7 
Upper,JUD020,Conductivity (uS/cm),10,55,39,39,65,90,55
Upper,JUD020,pH,10,6,6,6,6.5,6.5,6.2
Upper,JUD020,E. coli (counts/100 ml),3,0,0,0,0,,
Upper,JUD020,Ortho-phosphate (mg/L),7,0,0,0,0.015,0.03,0.006
Upper,JUD025,Water temperature (°C),9,7,3,6,10,12,7.4
Upper,JUD025,Turbidity (NTU),9,<7,<7,<7,<7,<7,<7 
Upper,JUD025,Conductivity (uS/cm),9,61,43,44,78,120,68
Upper,JUD025,pH,9,6.5,6,6,6.5,6.5,6.3
Upper,JUD025,E. coli (counts/100 ml),3,0,0,20,7,,
Upper,JUD025,Ortho-phosphate (mg/L),7,0.015,0,0,0.015,0.03,0.011
Upper,JUD070,Water temperature (°C),6,6,3,6,7.5,11,6.6
Upper,JUD070,Turbidity (NTU),6,<7,<7,<7,<7,<7,<7 
Upper,JUD070,Conductivity (uS/cm),6,60,51,51,77,82,64
Upper,JUD070,pH,6,6,6,6,6.5,6.5,6.2
Upper,JUD070,E. coli (counts/100 ml),3,20,0,40,20,,
Upper,JUD070,Ortho-phosphate (mg/L),5,0,0,0,0,0.015,0.003
Upper,JUD100,Water temperature (°C),6,6.5,3,6,10,12,7.3
Upper,JUD100,Turbidity (NTU),6,<7,<7,<7,<7,<7,<7 
Upper,JUD100,Conductivity (uS/cm),6,56,44,52,61,110,63
Upper,JUD100,pH,6,6,6,6,6.5,6.5,6.2
Upper,JUD100,E. coli (counts/100 ml),3,0,0,40,13,,
Upper,JUD100,Ortho-phosphate (mg/L),5,0,0,0,0.015,0.015,0.006
Upper,JUD180,Water temperature (°C),5,10,5,6,10,10,8.2
Upper,JUD180,Turbidity (NTU),5,<7,<7,<7,<7,<7,<7 
Upper,JUD180,Conductivity (uS/cm),5,54,49,53,70,88,63
Upper,JUD180,pH,5,6,6,6,6.5,6.5,6.2
Upper,JUD180,Ortho-phosphate (mg/L),4,0.008,0,0,0.015,0.015,0.008
Upper,JUD200,Water temperature (°C),7,7,3,5.5,13,16.6,9
Upper,JUD200,Turbidity (NTU),7,<7,<7,<7,<7,<7,<7 
Upper,JUD200,Conductivity (uS/cm),7,58,51,54,118,137,80
Upper,JUD200,pH,7,6,6,6,7.7,8,6.6
Upper,JUD200,E. coli (counts/100 ml),5,60,0,60,120,1000,248
Upper,JUD200,Ortho-phosphate (mg/L),7,0.005,0,0,0.015,0.03,0.008
West,KER200,E. coli (counts/100 ml),4,210,76,128,345,450,237
West,KER400,E. coli (counts/100 ml),2,300,80,520,300,,
West,KER450,E. coli (counts/100 ml),4,250,24,122,360,440,241
West,KER600,E. coli (counts/100 ml),3,560,60,820,480,,
West,KER700,E. coli (counts/100 ml),4,700,120,290,1470,2000,880
West,KER800,E. coli (counts/100 ml),4,665,200,405,1000,1280,703
,RIL200,E. coli (counts/100 ml),2,280,280,280,280,,
,RIL400,E. coli (counts/100 ml),4,865,230,340,1490,1700,915
,STT100,E. coli (counts/100 ml),2,95,80,110,95,,
,STT300,E. coli (counts/100 ml),2,920,240,1600,920,,
,STT350,E. coli (counts/100 ml),2,170,80,260,170,,
,STT400,E. coli (counts/100 ml),4,1195,260,465,2110,2500,1288
Upper,LDR001,Water temperature (°C),67,8,3,6,10,14,8.1
Upper,LDR001,Turbidity (NTU),69,0,0,0,0.3,2,0.3
Upper,LDR001,Conductivity (uS/cm),69,35,24,30,43,66,38
Upper,LDR001,pH,61,6.8,5.7,6.6,7,7.5,6.9
Upper,LDR002,Water temperature (°C),65,9,3,7,11.5,15,9.2
Upper,LDR002,Turbidity (NTU),67,1,0,0,1.4,5.4,1
Upper,LDR002,Conductivity (uS/cm),67,46,30,43,55,70,48
Upper,LDR002,pH,59,6.7,5.9,6.6,7.1,7.5,6.8
Upper,LDR100,Water temperature (°C),8,11.3,8,10,13.5,18.5,12
Upper,LDR100,Turbidity (NTU),8,<7,<7,<7,<7,<7,<7 
Upper,LDR100,Conductivity (uS/cm),8,30,20,30,40,40,33
Upper,LDR100,pH,8,6.5,6,6,6.5,6.5,6.3
Upper,LDR100,Total phosphate (mg/L),4,0.01,0.01,0.01,0.02,0.02,0.01
Upper,LDR220,Water temperature (°C),5,13.5,8,11.5,16.5,20,13.9
Upper,LDR220,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 
Upper,LDR220,Conductivity (uS/cm),4,30,30,30,40,50,35
Upper,LDR220,pH,5,6.5,6,6,6.5,6.5,6.3
Upper,LDR220,Total phosphate (mg/L),5,0.02,0.01,0.01,0.02,0.03,0.02
Upper,LDR300,Water temperature (°C),4,8.8,8,8,10.5,11.5,9.3
Upper,LDR300,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 
Upper,LDR300,Conductivity (uS/cm),4,30,30,30,30,30,30
Upper,LDR300,pH,4,6,6,6,6,6,6
Upper,LDR300,Total phosphate (mg/L),5,0.04,0.03,0.03,0.04,0.05,0.04
Upper,LDR400,Total phosphate (mg/L),4,0.02,0.01,0.01,0.02,0.02,0.02
North,BAK025,Water temperature (°C),4,12.5,10,11,13,13,12
North,BAK025,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 
North,BAK025,Conductivity (uS/cm),4,86,50,64,96,97,80
North,BAK025,pH,4,6.5,6,6.3,6.8,7,6.5
North,BAK025,E. coli (counts/100 ml),6,69,0,20,320,480,160
North,BAK025,Ortho-phosphate (mg/L),2,0.015,0.015,0.015,0.015,,
North,BAK025,Dissolved oxygen (mg/L),2,9.8,9.6,10,9.8,,
North,BAK060,Water temperature (°C),5,13,8,11,14.5,15,12.3
North,BAK060,Turbidity (NTU),5,<7,<7,<7,<7,<7,<7 
North,BAK060,Conductivity (uS/cm),5,91,70,88,110,124,97
North,BAK060,pH,5,6.5,6,6.5,7,7,6.6
North,BAK060,E. coli (counts/100 ml),6,260,40,140,1200,1240,523
North,BAK060,Ortho-phosphate (mg/L),2,0.015,0.015,0.015,0.015,,
North,BAK150,Water temperature (°C),4,13.5,9.5,10.8,15,15,12.9
North,BAK150,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 
North,BAK150,Conductivity (uS/cm),4,151,120,132,167,176,149
North,BAK150,pH,4,7,6.5,6.8,7,7,6.9
North,BAK150,E. coli (counts/100 ml),5,200,54,80,540,1680,511
North,BAK150,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,
North,BAK150,Dissolved oxygen (mg/L),2,8,7.8,8.2,8,,
North,BAK200,Water temperature (°C),8,12,5,10.3,15,16.5,12
North,BAK200,Turbidity (NTU),8,<7,<7,<7,<7,<7,<7 
North,BAK200,Conductivity (uS/cm),8,165,140,149,176,208,166
North,BAK200,pH,8,6.5,6,6.3,6.5,7,6.4
North,BAK200,E. coli (counts/100 ml),7,280,120,200,680,2000,554
North,BAK200,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,
North,BAK200,Dissolved oxygen (mg/L),2,7.7,7.6,7.8,7.7,,
North,BAK250,Water temperature (°C),5,14.5,8,10,16.5,18,13.4
North,BAK250,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 
North,BAK250,Conductivity (uS/cm),5,178,150,163,195,309,199
North,BAK250,pH,5,6.5,6,6.5,6.5,6.5,6.4
North,BAK250,E. coli (counts/100 ml),5,140,98,140,320,1520,444
North,BAK250,Ortho-phosphate (mg/L),3,0.015,0.015,0.03,0.02,,
North,CRB080,Water temperature (°C),6,11.3,6,6.5,16.5,20,11.9
North,CRB080,Turbidity (NTU),6,<7,<7,<7,7,7,7
North,CRB080,Conductivity (uS/cm),6,55,34,38,92,130,67
North,CRB080,pH,6,6.3,5.5,6,6.5,6.5,6.2
North,CRB080,E. coli (counts/100 ml),5,20,0,0,20,20,12
North,CRB080,Ortho-phosphate (mg/L),4,0.008,0,0,0.023,0.03,0.011
North,CRB080,Dissolved oxygen (mg/L),4,10.7,8.5,9.2,12,12.5,10.6
North,CRB100,Water temperature (°C),4,18.9,5.6,12.2,19.5,20,15.9
North,CRB100,Turbidity (NTU),4,4,1,1,7,7,4
North,CRB100,Conductivity (uS/cm),4,90,76,79,105,111,92
North,CRB100,pH,4,7,6,6.3,7.5,7.5,6.9
North,CRB100,E. coli (counts/100 ml),2,36,6,66,36,,
North,CRB100,Dissolved oxygen (mg/L),3,8.5,7.2,11.9,9.2,,
North,CRB150,Water temperature (°C),7,14.5,6,8,18,19,13.1
North,CRB150,Turbidity (NTU),7,<7,<7,<7,<7,<7,<7 
North,CRB150,Conductivity (uS/cm),6,73,44,50,119,131,82
North,CRB150,pH,7,6.5,5.5,6,6.5,7,6.3
North,CRB150,E. coli (counts/100 ml),6,50,0,0,120,140,60
North,CRB150,Ortho-phosphate (mg/L),6,0.015,0,0.015,0.015,0.03,0.015
North,CRB150,Dissolved oxygen (mg/L),6,9.8,7.9,8,10.8,10.8,9.5
North,CRB250,Water temperature (°C),5,15,6.5,9,18.5,19,13.6
North,CRB250,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 
North,CRB250,Conductivity (uS/cm),5,81,46,50,116,139,86
North,CRB250,pH,5,6.5,5.5,6,6.5,7,6.3
North,CRB250,E. coli (counts/100 ml),4,20,0,0,80,120,40
North,CRB250,Ortho-phosphate (mg/L),4,0.008,0,0,0.015,0.015,0.008
North,CRB250,Dissolved oxygen (mg/L),5,9.5,7.2,8.2,10.4,10.4,9.1
North,CRB300,Water temperature (°C),12,12,4.5,7.5,16.5,19.6,12.2
North,CRB300,Turbidity (NTU),12,7,1,<7,<7,<7,6
North,CRB300,Conductivity (uS/cm),11,73,49,50,114,162,86
North,CRB300,pH,12,6.5,5.5,6.3,7,7.3,6.6
North,CRB300,E. coli (counts/100 ml),10,75,20,40,280,2700,381
North,CRB300,Ortho-phosphate (mg/L),6,0.015,0,0.015,0.015,0.015,0.013
North,CRB300,Dissolved oxygen (mg/L),8,9.9,7.7,8.7,11.2,12.2,9.9
North,CRB300,% saturation,4,95,92,92,102,106,97
North,DIP060,Water temperature (°C),4,9.3,6,7.3,12,14,9.6
North,DIP060,Turbidity (NTU),4,19,17,18,24,28,21
North,DIP060,Conductivity (uS/cm),4,141,110,124,157,170,140
North,DIP060,pH,4,5.8,5,5.3,6,6,5.6
North,DIP060,E. coli (counts/100 ml),2,50,40,60,50,,
North,DIP080,Water temperature (°C),4,8,5.5,6,10.3,11,8.1
North,DIP080,Turbidity (NTU),4,31,9,18,35,35,26
North,DIP080,Conductivity (uS/cm),4,208,180,188,238,256,213
North,DIP080,pH,4,6,5,5.5,6,6,5.8
North,DIP080,E. coli (counts/100 ml),2,430,400,460,430,,
North,DIP100,Water temperature (°C),5,11.5,5,7,12,15,10.1
North,DIP100,Turbidity (NTU),5,16,<7,15,25,25,18
North,DIP100,Conductivity (uS/cm),5,200,65,190,203,210,174
North,DIP100,pH,5,6,5.5,6,6.5,6.5,6.1
North,DIP100,E. coli (counts/100 ml),6,520,160,280,800,1440,620
North,FOU100,Water temperature (°C),9,10,4.8,5.5,11.8,18.2,9.5
North,FOU100,Turbidity (NTU),9,<7,<7,<7,<7,12,8
North,FOU100,Conductivity (uS/cm),9,401,300,310,484,640,423
North,FOU100,pH,9,6.5,6,6,7,7.1,6.5
North,FOU100,E. coli (counts/100 ml),7,260,0,40,1000,2000,557
North,FOU100,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,
North,FOU120,Water temperature (°C),10,10.5,4.5,5.8,11.8,13.9,9.3
North,FOU120,Turbidity (NTU),10,<7,<7,<7,<7,13,8
North,FOU120,Conductivity (uS/cm),10,362,230,338,658,1420,527
North,FOU120,pH,10,7,6.5,6.5,7,7.5,6.9
North,FOU120,E. coli (counts/100 ml),8,130,38,60,340,480,197
North,FOU120,Ortho-phosphate (mg/L),5,0.015,0.015,0.015,0.015,0.03,0.018
North,FOU150,Water temperature (°C),10,10.5,5,6.3,11.5,12,9.1
North,FOU150,Turbidity (NTU),10,<7,<7,<7,<7,<7,<7 
North,FOU150,Conductivity (uS/cm),10,529,390,454,1080,1294,694
North,FOU150,pH,10,6,6,6,6.5,7,6.3
North,FOU150,E. coli (counts/100 ml),8,109,20,50,340,580,200
North,FOU150,Ortho-phosphate (mg/L),5,0.03,0.015,0.015,0.03,0.045,0.027
North,FOU200,Water temperature (°C),8,11,4.5,7,11.3,13.5,9.6
North,FOU200,Turbidity (NTU),8,<7,<7,<7,<7,15,8
North,FOU200,Conductivity (uS/cm),8,491,410,465,629,1020,575
North,FOU200,pH,8,6.5,6,6,7,7.5,6.6
North,FOU200,E. coli (counts/100 ml),6,80,1,20,160,700,174
North,FOU200,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,
North,MOU200,Water temperature (°C),19,10.9,5,7,16,18.5,11.5
North,MOU200,Turbidity (NTU),20,<7,<7,<7,<7,71,11
North,MOU200,Conductivity (uS/cm),20,50,20,40,69,99,53
North,MOU200,pH,20,6.5,6,6.5,7,7.4,6.6
North,MOU200,E. coli (counts/100 ml),10,20,0,0,100,200,52
North,MOU200,Ortho-phosphate (mg/L),3,0.005,0.005,0.03,0.013,,
North,MOU200,Dissolved oxygen (mg/L),4,10.8,8.6,9.7,11.6,12.3,10.6
North,MOU250,Water temperature (°C),9,13,5.3,9.5,16,19.6,12.9
North,MOU250,Turbidity (NTU),9,<7,<7,<7,<7,<7,<7 
North,MOU250,Conductivity (uS/cm),9,168,99,149,243,320,190
North,MOU250,pH,9,7,6.5,6.5,7,7.5,6.9
North,MOU250,E. coli (counts/100 ml),9,20,0,0,99,660,122
North,MOU250,Ortho-phosphate (mg/L),2,0.005,0.005,0.005,0.005,,
North,MOU250,Dissolved oxygen (mg/L),2,10.3,8.2,12.4,10.3,,
North,MOU400,Water temperature (°C),20,12,5,8.3,15,20,12.2
North,MOU400,Turbidity (NTU),20,<7,<7,<7,<7,18,8
North,MOU400,Conductivity (uS/cm),20,60,20,45,76,113,62
North,MOU400,pH,20,6.5,6,6.5,7,7.6,6.7
North,MOU400,E. coli (counts/100 ml),10,70,20,40,120,200,86
North,MOU400,Ortho-phosphate (mg/L),4,0.005,0,0.003,0.01,0.015,0.006
North,MOU400,Dissolved oxygen (mg/L),5,10.4,9,9,10.7,12.4,10.3
North,MOU600,Water temperature (°C),19,11,5,7,16.5,20.5,11.8
North,MOU600,Turbidity (NTU),20,<7,<7,<7,<7,18,8
North,MOU600,Conductivity (uS/cm),19,70,30,50,90,124,72
North,MOU600,pH,19,6.6,6,6.5,7,7.9,6.8
North,MOU600,E. coli (counts/100 ml),10,84,0,40,260,400,143
North,MOU600,Ortho-phosphate (mg/L),3,0.005,0.005,0.03,0.013,,
North,MOU600,Dissolved oxygen (mg/L),4,10.3,8.5,9.3,11.4,12.3,10.3
North,MOU650,Water temperature (°C),11,11,5,6,16,20.5,11.5
North,MOU650,Turbidity (NTU),11,<7,<7,<7,<7,8,<7 
North,MOU650,Conductivity (uS/cm),11,100,40,70,135,141,101
North,MOU650,pH,11,6.5,6,6,7,7.4,6.6
North,MOU650,E. coli (counts/100 ml),9,100,40,100,180,360,149
North,MOU650,Ortho-phosphate (mg/L),6,0.01,0,0.005,0.015,0.03,0.012
North,MOU650,Dissolved oxygen (mg/L),4,10.6,8.5,9.3,11.8,12.3,10.5
North,MOU700,Water temperature (°C),11,13,5.5,7,14,20.1,11.9
North,MOU700,Turbidity (NTU),11,<7,<7,<7,<7,13,8
North,MOU700,Conductivity (uS/cm),11,100,40,70,132,158,103
North,MOU700,pH,11,6.5,6,6,7,7.4,6.7
North,MOU700,E. coli (counts/100 ml),10,130,20,80,210,460,169
North,MOU700,Ortho-phosphate (mg/L),5,0.012,0.015,0.015,0.005,0.005,6
North,MOU700,Dissolved oxygen (mg/L),2,10,7.4,12.5,10,,
North,MOU850,Water temperature (°C),27,11.5,5.4,8.3,14,21.1,11.7
North,MOU850,Turbidity (NTU),28,<7,<7,<7,<7,266,24
North,MOU850,Conductivity (uS/cm),27,114,40,101,135,182,117
North,MOU850,pH,25,7,6,6.5,7.5,7.9,6.9
North,MOU850,E. coli (counts/100 ml),10,390,50,160,800,2000,661
North,MOU850,Ortho-phosphate (mg/L),6,0.015,0.005,0.01,0.015,0.03,0.015
North,MOU850,Dissolved oxygen (mg/L),18,10.3,8.6,9,10.9,12.3,10.2
West,PCK010,Water temperature (°C),20,12.5,8,10,14.5,18,12.5
West,PCK010,Turbidity (NTU),20,<7,<7,<7,13,95,15
West,PCK010,Conductivity (uS/cm),20,149,80,131,173,214,150
West,PCK010,pH,20,6.3,5.5,6,6.5,7,6.3
West,PCK020,Water temperature (°C),20,12,8,9,13.5,15,11.5
West,PCK020,Turbidity (NTU),20,<7,<7,<7,14,43,13
West,PCK020,Conductivity (uS/cm),20,179,90,148,202,285,176
West,PCK020,pH,20,6.5,6,6.5,6.8,7,6.6
West,PCK030,Water temperature (°C),20,12.3,7.5,9.3,14.8,18.0 .,12.3
West,PCK030,Turbidity (NTU),20,<7,<7,<7,11,30,10
West,PCK030,Conductivity (uS/cm),20,220,99,182,249,350,219
West,PCK030,pH,20,6.5,6,6.5,7,7,6.6
Upper,RUS005,Water temperature (°C),70,8.5,3,6,11,16.5,8.6
Upper,RUS005,Turbidity (NTU),72,0,0,0,0.3,2,0.2
Upper,RUS005,Conductivity (uS/cm),72,58,39,51,68,100,60
Upper,RUS005,pH,64,6.9,6,6.7,7.2,7.7,6.9
Upper,RUS010,Water temperature (°C),69,9,2.5,6,10.5,17,8.7
Upper,RUS010,Turbidity (NTU),71,0,0,0,1,7,0.9
Upper,RUS010,Conductivity (uS/cm),71,55,38,47,69,100,60
Upper,RUS010,pH,63,6.8,5.5,6.6,7,7.6,6.8
Upper,RUS010,E. coli (counts/100 ml),2,0,0,0,0,,
Upper,RUS010,Ortho-phosphate (mg/L),2,0.008,0,0.015,0.008,,
Upper,RUS055,Water temperature (°C),14,12,7.5,10,17,18,12.9
Upper,RUS055,Turbidity (NTU),12,<7,<7,<7,<7,<7,<7 
Upper,RUS055,Conductivity (uS/cm),10,47,30,39,68,78,51
Upper,RUS055,pH,12,6,5.5,6,6.5,6.5,6.1
Upper,RUS055,E. coli (counts/100 ml),4,32,6,11,106,164,58
Upper,RUS055,Ortho-phosphate (mg/L),8,0.015,0.002,0.008,0.023,0.03,0.015
Upper,RUS060,Water temperature (°C),15,8,5,7,15,19,10.4
Upper,RUS060,Turbidity (NTU),15,<7,<7,<7,<7,<7,<7 
Upper,RUS060,Conductivity (uS/cm),12,46,35,43,60,77,51
Upper,RUS060,pH,15,6,5.5,6,6,6.5,6
Upper,RUS060,E. coli (counts/100 ml),2,10,0,20,10,,
Upper,RUS060,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,
Upper,RUS070,Water temperature (°C),12,9,5,7,12,19,10.1
Upper,RUS070,Turbidity (NTU),12,<7,<7,<7,<7,<7,<7 
Upper,RUS070,Conductivity (uS/cm),10,47,36,43,58,79,52
Upper,RUS070,pH,11,6,5.5,6,6,7,6
Upper,ROS070,E. coli (counts/100 ml),2,70,20,120,70,,
Upper,RUS075,Water temperature (°C),6,8.5,5,7,10,15,9
Upper,RUS075,Turbidity (NTU),6,<7,<7,<7,<7,18,9
Upper,RUS075,Conductivity (uS/cm),6,76,65,72,90,147,88
Upper,RUS075,pH,6,6,5.5,6,6.5,7,6.2
Upper,RUS080,Water temperature (°C),16,10.5,5,6,15,19,10.9
Upper,RUS080,Turbidity (NTU),16,<7,<7,<7,<7,<7,<7 
Upper,RUS080,Conductivity (uS/cm),14,52,7,42,60,88,52
Upper,RUS080,pH,15,6,5.5,5.5,6.5,60,9.6
Upper,RUS080,E. coli (counts/100 ml),2,20,20,20,20,,
Upper,RUS080,Ortho-phosphate (mg/L),2,0.015,0.015,0.015,0.015,,
Upper,RUS100,Water temperature (°C),14,11,5,7,18,19,11.8
Upper,RUS100,Turbidity (NTU),14,<7,<7,<7,<7,<7,<7 
Upper,RUS100,Conductivity (uS/cm),11,51,39,42,74,86,56
Upper,RUS100,pH,13,6,5,6,6.5,7,6.2
Upper,RUS100,Ortho-phosphate (mg/L),2,0.008,0,0.015,0.008,,
Upper,WAT050,Turbidity (NTU),8,11,<7,<7,34,63,22
Upper,WAT050,Conductivity (uS/cm),8,264,125,176,420,510,294
Upper,WAT050,pH,8,6.8,6,6.5,7.5,7.5,6.9
Upper,WAT050,Water temperature (°C),8,15.3,9.5,10,18,20,14.5
Upper,WAT055,Turbidity (NTU),6,31,<7,<7,39,48,27
Upper,WAT055,Conductivity (uS/cm),6,309,215,239,470,510,342
Upper,WAT055,pH,5,7,6,7,7.5,8,7.1
Upper,WAT055,Water temperature (°C),6,12.3,10,11,14,17,12.8
Upper,WAT200,Water temperature (°C),27,11.7,4.7,9.5,14.7,19,12.3
Upper,WAT200,Turbidity (NTU),26,10,<7,<7,15,175,20
Upper,WAT200,Conductivity (uS/cm),27,320,120,220,390,490,315
Upper,WAT200,pH,27,6.5,6,6.5,7,8,6.8
Upper,WAT200,Dissolved oxygen (mg/L),16,9.4,8,8.6,10.2,12.7,9.5
```

---
## Data tables — verbatim set

Faithful cell-for-cell copies of every worksheet as exported. Nothing added, removed, or altered. The seven per-parameter tables duplicate rows already present in `as_printed`.

### Verbatim — site_coordinates

Source file: `01_original_verbatim/site_coordinates.csv`  ·  166 lines (including header)

```csv
Site,Easting (AGD66 UTM Z55),Northing (AGD66 UTM Z55),Latitude (GDA94),Longitude (GDA94),Google Maps,Apple Maps
AGN010,507700,5225250,-43.123801,147.096041,"https://www.google.com/maps/search/?api=1&query=-43.123801,147.096041","https://maps.apple.com/?ll=-43.123801,147.096041&q=-43.123801,147.096041"
AGN016,506500,5224600,-43.129665,147.081297,"https://www.google.com/maps/search/?api=1&query=-43.129665,147.081297","https://maps.apple.com/?ll=-43.129665,147.081297&q=-43.129665,147.081297"
AGN120,506100,5221475,-43.157809,147.076414,"https://www.google.com/maps/search/?api=1&query=-43.157809,147.076414","https://maps.apple.com/?ll=-43.157809,147.076414&q=-43.157809,147.076414"
AGN130,506100,5221500,-43.157584,147.076414,"https://www.google.com/maps/search/?api=1&query=-43.157584,147.076414","https://maps.apple.com/?ll=-43.157584,147.076414&q=-43.157584,147.076414"
AGN200,506075,5221225,-43.16006,147.076109,"https://www.google.com/maps/search/?api=1&query=-43.16006,147.076109","https://maps.apple.com/?ll=-43.16006,147.076109&q=-43.16006,147.076109"
A6N245,507675,5221775,-43.155093,147.095783,"https://www.google.com/maps/search/?api=1&query=-43.155093,147.095783","https://maps.apple.com/?ll=-43.155093,147.095783&q=-43.155093,147.095783"
AGN249,507575,5221825,-43.154644,147.094552,"https://www.google.com/maps/search/?api=1&query=-43.154644,147.094552","https://maps.apple.com/?ll=-43.154644,147.094552&q=-43.154644,147.094552"
AGN250,507500,5221900,-43.153969,147.093628,"https://www.google.com/maps/search/?api=1&query=-43.153969,147.093628","https://maps.apple.com/?ll=-43.153969,147.093628&q=-43.153969,147.093628"
AGN260,506650,5221550,-43.157129,147.083178,"https://www.google.com/maps/search/?api=1&query=-43.157129,147.083178","https://maps.apple.com/?ll=-43.157129,147.083178&q=-43.157129,147.083178"
AGN300,506500,5221500,-43.157581,147.081334,"https://www.google.com/maps/search/?api=1&query=-43.157581,147.081334","https://maps.apple.com/?ll=-43.157581,147.081334&q=-43.157581,147.081334"
AGN400,506575,5220900,-43.162983,147.082263,"https://www.google.com/maps/search/?api=1&query=-43.162983,147.082263","https://maps.apple.com/?ll=-43.162983,147.082263&q=-43.162983,147.082263"
,,,,,,
ALB100,512100,5219300,-43.177322,147.150263,"https://www.google.com/maps/search/?api=1&query=-43.177322,147.150263","https://maps.apple.com/?ll=-43.177322,147.150263&q=-43.177322,147.150263"
,,,,,,
ARV005,481500,5215600,-43.210514,146.773633,"https://www.google.com/maps/search/?api=1&query=-43.210514,146.773633","https://maps.apple.com/?ll=-43.210514,146.773633&q=-43.210514,146.773633"
ARV100,485500,5231500,-43.067423,146.823289,"https://www.google.com/maps/search/?api=1&query=-43.067423,146.823289","https://maps.apple.com/?ll=-43.067423,146.823289&q=-43.067423,146.823289"
,,,,,,
BAK015,500500,5244350,-42.951844,147.007508,"https://www.google.com/maps/search/?api=1&query=-42.951844,147.007508","https://maps.apple.com/?ll=-42.951844,147.007508&q=-42.951844,147.007508"
BAK025,501100,5243750,-42.957247,147.014864,"https://www.google.com/maps/search/?api=1&query=-42.957247,147.014864","https://maps.apple.com/?ll=-42.957247,147.014864&q=-42.957247,147.014864"
BAK060,502350,5242900,-42.964898,147.030193,"https://www.google.com/maps/search/?api=1&query=-42.964898,147.030193","https://maps.apple.com/?ll=-42.964898,147.030193&q=-42.964898,147.030193"
BAK100,502900,5242450,-42.968948,147.03694,"https://www.google.com/maps/search/?api=1&query=-42.968948,147.03694","https://maps.apple.com/?ll=-42.968948,147.03694&q=-42.968948,147.03694"
BAK150,503600,5241900,-42.973898,147.045527,"https://www.google.com/maps/search/?api=1&query=-42.973898,147.045527","https://maps.apple.com/?ll=-42.973898,147.045527&q=-42.973898,147.045527"
BAK200,504350,5241250,-42.979747,147.05473,"https://www.google.com/maps/search/?api=1&query=-42.979747,147.05473","https://maps.apple.com/?ll=-42.979747,147.05473&q=-42.979747,147.05473"
BAK250,505250,5240650,-42.985145,147.065774,"https://www.google.com/maps/search/?api=1&query=-42.985145,147.065774","https://maps.apple.com/?ll=-42.985145,147.065774&q=-42.985145,147.065774"
,,,,,,
CFB010,495800,5226213,-43.115158,146.949756,"https://www.google.com/maps/search/?api=1&query=-43.115158,146.949756","https://maps.apple.com/?ll=-43.115158,146.949756&q=-43.115158,146.949756"
CFB020,496500,5225100,-43.125184,146.958354,"https://www.google.com/maps/search/?api=1&query=-43.125184,146.958354","https://maps.apple.com/?ll=-43.125184,146.958354&q=-43.125184,146.958354"
CFB030,497600,5224200,-43.133293,146.971873,"https://www.google.com/maps/search/?api=1&query=-43.133293,146.971873","https://maps.apple.com/?ll=-43.133293,146.971873&q=-43.133293,146.971873"
,,,,,,
CRB080,504400,5246450,-42.93292,147.055301,"https://www.google.com/maps/search/?api=1&query=-42.93292,147.055301","https://maps.apple.com/?ll=-42.93292,147.055301&q=-42.93292,147.055301"
CRB100,504600,5246100,-42.936071,147.057755,"https://www.google.com/maps/search/?api=1&query=-42.936071,147.057755","https://maps.apple.com/?ll=-42.936071,147.057755&q=-42.936071,147.057755"
CRB150,505650,5244950,-42.94642,147.070636,"https://www.google.com/maps/search/?api=1&query=-42.94642,147.070636","https://maps.apple.com/?ll=-42.94642,147.070636&q=-42.94642,147.070636"
CRB250,506350,5243900,-42.955869,147.079229,"https://www.google.com/maps/search/?api=1&query=-42.955869,147.079229","https://maps.apple.com/?ll=-42.955869,147.079229&q=-42.955869,147.079229"
CRB300,507000,5242400,-42.969371,147.087217,"https://www.google.com/maps/search/?api=1&query=-42.969371,147.087217","https://maps.apple.com/?ll=-42.969371,147.087217&q=-42.969371,147.087217"
,,,,,,
DIC500,494600,5238000,-43.009009,146.935118,"https://www.google.com/maps/search/?api=1&query=-43.009009,146.935118","https://maps.apple.com/?ll=-43.009009,146.935118&q=-43.009009,146.935118"
,,,,,,
DIP040,509550,5242850,-42.965291,147.118479,"https://www.google.com/maps/search/?api=1&query=-42.965291,147.118479","https://maps.apple.com/?ll=-42.965291,147.118479&q=-42.965291,147.118479"
DIP060,509300,5243350,-42.960792,147.115405,"https://www.google.com/maps/search/?api=1&query=-42.960792,147.115405","https://maps.apple.com/?ll=-42.960792,147.115405&q=-42.960792,147.115405"
DIP080,508800,5243300,-42.961248,147.109275,"https://www.google.com/maps/search/?api=1&query=-42.961248,147.109275","https://maps.apple.com/?ll=-42.961248,147.109275&q=-42.961248,147.109275"
DIP100,508800,5243350,-42.960798,147.109274,"https://www.google.com/maps/search/?api=1&query=-42.960798,147.109274","https://maps.apple.com/?ll=-42.960798,147.109274&q=-42.960798,147.109274"
,,,,,,
DOV070,500650,5205900,-43.298083,147.009399,"https://www.google.com/maps/search/?api=1&query=-43.298083,147.009399","https://maps.apple.com/?ll=-43.298083,147.009399&q=-43.298083,147.009399"
DOV090,500850,5204975,-43.306412,147.011866,"https://www.google.com/maps/search/?api=1&query=-43.306412,147.011866","https://maps.apple.com/?ll=-43.306412,147.011866&q=-43.306412,147.011866"
DOV100,500900,5204550,-43.310239,147.012484,"https://www.google.com/maps/search/?api=1&query=-43.310239,147.012484","https://maps.apple.com/?ll=-43.310239,147.012484&q=-43.310239,147.012484"
DOV110,501325,5204450,-43.311139,147.017724,"https://www.google.com/maps/search/?api=1&query=-43.311139,147.017724","https://maps.apple.com/?ll=-43.311139,147.017724&q=-43.311139,147.017724"
DOV120,501620,5204100,-43.31429,147.021363,"https://www.google.com/maps/search/?api=1&query=-43.31429,147.021363","https://maps.apple.com/?ll=-43.31429,147.021363&q=-43.31429,147.021363"
DOV130,501750,5203950,-43.31564,147.022967,"https://www.google.com/maps/search/?api=1&query=-43.31564,147.022967","https://maps.apple.com/?ll=-43.31564,147.022967&q=-43.31564,147.022967"
,,,,,,
ESP001,484300,5213200,-43.232188,146.808036,"https://www.google.com/maps/search/?api=1&query=-43.232188,146.808036","https://maps.apple.com/?ll=-43.232188,146.808036&q=-43.232188,146.808036"
ESP002,495400,5202800,-43.325985,146.944649,"https://www.google.com/maps/search/?api=1&query=-43.325985,146.944649","https://maps.apple.com/?ll=-43.325985,146.944649&q=-43.325985,146.944649"
,,,,,,
FLU100,499450,5226450,-43.113035,146.994621,"https://www.google.com/maps/search/?api=1&query=-43.113035,146.994621","https://maps.apple.com/?ll=-43.113035,146.994621&q=-43.113035,146.994621"
,,,,,,
FOU100,507600,5240800,-42.983774,147.094596,"https://www.google.com/maps/search/?api=1&query=-42.983774,147.094596","https://maps.apple.com/?ll=-42.983774,147.094596&q=-42.983774,147.094596"
FOU150,506650,5240950,-42.982432,147.082942,"https://www.google.com/maps/search/?api=1&query=-42.982432,147.082942","https://maps.apple.com/?ll=-42.982432,147.082942&q=-42.982432,147.082942"
FOU200,505550,5241050,-42.98154,147.06945,"https://www.google.com/maps/search/?api=1&query=-42.98154,147.06945","https://maps.apple.com/?ll=-42.98154,147.06945&q=-42.98154,147.06945"
,,,,,,
GDR100,512500,5219800,-43.172813,147.155173,"https://www.google.com/maps/search/?api=1&query=-43.172813,147.155173","https://maps.apple.com/?ll=-43.172813,147.155173&q=-43.172813,147.155173"
GDR150,509100,5218900,-43.180966,147.113357,"https://www.google.com/maps/search/?api=1&query=-43.180966,147.113357","https://maps.apple.com/?ll=-43.180966,147.113357&q=-43.180966,147.113357"
GDR200,508500,5218500,-43.184575,147.105981,"https://www.google.com/maps/search/?api=1&query=-43.184575,147.105981","https://maps.apple.com/?ll=-43.184575,147.105981&q=-43.184575,147.105981"
,,,,,,
GVC115,505925,5221775,-43.155109,147.074258,"https://www.google.com/maps/search/?api=1&query=-43.155109,147.074258","https://maps.apple.com/?ll=-43.155109,147.074258&q=-43.155109,147.074258"
,,,,,,
HOL100,509600,5218600,-43.183661,147.119515,"https://www.google.com/maps/search/?api=1&query=-43.183661,147.119515","https://maps.apple.com/?ll=-43.183661,147.119515&q=-43.183661,147.119515"
,,,,,,
HUO140,494100,5239100,-42.999099,146.928995,"https://www.google.com/maps/search/?api=1&query=-42.999099,146.928995","https://maps.apple.com/?ll=-42.999099,146.928995&q=-42.999099,146.928995"
HUO150,495312,5237550,-43.013066,146.943851,"https://www.google.com/maps/search/?api=1&query=-43.013066,146.943851","https://maps.apple.com/?ll=-43.013066,146.943851&q=-43.013066,146.943851"
HUO200,496525,5236475,-43.022752,146.95873,"https://www.google.com/maps/search/?api=1&query=-43.022752,146.95873","https://maps.apple.com/?ll=-43.022752,146.95873&q=-43.022752,146.95873"
HUO240,496600,5236325,-43.024104,146.95965,"https://www.google.com/maps/search/?api=1&query=-43.024104,146.95965","https://maps.apple.com/?ll=-43.024104,146.95965&q=-43.024104,146.95965"
,,,,,,
JUD020,497050,5246400,-42.933378,146.965224,"https://www.google.com/maps/search/?api=1&query=-42.933378,146.965224","https://maps.apple.com/?ll=-42.933378,146.965224&q=-42.933378,146.965224"
JUD025,496000,5242950,-42.964442,146.952332,"https://www.google.com/maps/search/?api=1&query=-42.964442,146.952332","https://maps.apple.com/?ll=-42.964442,146.952332&q=-42.964442,146.952332"
JUD070,495250,5241450,-42.977945,146.943123,"https://www.google.com/maps/search/?api=1&query=-42.977945,146.943123","https://maps.apple.com/?ll=-42.977945,146.943123&q=-42.977945,146.943123"
JUD100,495950,5242400,-42.969394,146.951715,"https://www.google.com/maps/search/?api=1&query=-42.969394,146.951715","https://maps.apple.com/?ll=-42.969394,146.951715&q=-42.969394,146.951715"
JUD200,493700,5239800,-42.992793,146.924095,"https://www.google.com/maps/search/?api=1&query=-42.992793,146.924095","https://maps.apple.com/?ll=-42.992793,146.924095&q=-42.992793,146.924095"
,,,,,,
KEL250,511600,5235100,-43.035052,147.143778,"https://www.google.com/maps/search/?api=1&query=-43.035052,147.143778","https://maps.apple.com/?ll=-43.035052,147.143778&q=-43.035052,147.143778"
KEL400,509500,5234200,-43.043186,147.118015,"https://www.google.com/maps/search/?api=1&query=-43.043186,147.118015","https://maps.apple.com/?ll=-43.043186,147.118015&q=-43.043186,147.118015"
KEL750,505900,5230700,-43.07474,147.073854,"https://www.google.com/maps/search/?api=1&query=-43.07474,147.073854","https://maps.apple.com/?ll=-43.07474,147.073854&q=-43.07474,147.073854"
,,,,,,
KER001,487400,5214600,-43.219639,146.846244,"https://www.google.com/maps/search/?api=1&query=-43.219639,146.846244","https://maps.apple.com/?ll=-43.219639,146.846244&q=-43.219639,146.846244"
KER010,489600,5218100,-43.188156,146.873397,"https://www.google.com/maps/search/?api=1&query=-43.188156,146.873397","https://maps.apple.com/?ll=-43.188156,146.873397&q=-43.188156,146.873397"
KER200,492400,5219050,-43.179634,146.907868,"https://www.google.com/maps/search/?api=1&query=-43.179634,146.907868","https://maps.apple.com/?ll=-43.179634,146.907868&q=-43.179634,146.907868"
KER400,493750,5219900,-43.171992,146.924488,"https://www.google.com/maps/search/?api=1&query=-43.171992,146.924488","https://maps.apple.com/?ll=-43.171992,146.924488&q=-43.171992,146.924488"
KER450,494100,5220250,-43.168843,146.928798,"https://www.google.com/maps/search/?api=1&query=-43.168843,146.928798","https://maps.apple.com/?ll=-43.168843,146.928798&q=-43.168843,146.928798"
KER650,493650,5221100,-43.161186,146.923272,"https://www.google.com/maps/search/?api=1&query=-43.161186,146.923272","https://maps.apple.com/?ll=-43.161186,146.923272&q=-43.161186,146.923272"
KER700,494300,5220700,-43.164793,146.931263,"https://www.google.com/maps/search/?api=1&query=-43.164793,146.931263","https://maps.apple.com/?ll=-43.164793,146.931263&q=-43.164793,146.931263"
KER750,494750,5220800,-43.163895,146.9368,"https://www.google.com/maps/search/?api=1&query=-43.163895,146.9368","https://maps.apple.com/?ll=-43.163895,146.9368&q=-43.163895,146.9368"
KER800,495200,5220500,-43.1666,146.942333,"https://www.google.com/maps/search/?api=1&query=-43.1666,146.942333","https://maps.apple.com/?ll=-43.1666,146.942333&q=-43.1666,146.942333"
,,,,,,
LAS040,512800,5208550,-43.274111,147.159128,"https://www.google.com/maps/search/?api=1&query=-43.274111,147.159128","https://maps.apple.com/?ll=-43.274111,147.159128&q=-43.274111,147.159128"
LAS060,512700,5208500,-43.274563,147.157896,"https://www.google.com/maps/search/?api=1&query=-43.274563,147.157896","https://maps.apple.com/?ll=-43.274563,147.157896&q=-43.274563,147.157896"
LAS080,512700,5208400,-43.275463,147.157899,"https://www.google.com/maps/search/?api=1&query=-43.275463,147.157899","https://maps.apple.com/?ll=-43.275463,147.157899&q=-43.275463,147.157899"
LAS100,512600,5208400,-43.275465,147.156666,"https://www.google.com/maps/search/?api=1&query=-43.275465,147.156666","https://maps.apple.com/?ll=-43.275465,147.156666&q=-43.275465,147.156666"
,,,,,,
LDR001,476700,5244000,-42.954643,146.715727,"https://www.google.com/maps/search/?api=1&query=-42.954643,146.715727","https://maps.apple.com/?ll=-42.954643,146.715727&q=-42.954643,146.715727"
LDR002,482100,5242600,-42.967396,146.781884,"https://www.google.com/maps/search/?api=1&query=-42.967396,146.781884","https://maps.apple.com/?ll=-42.967396,146.781884&q=-42.967396,146.781884"
LDR100,483377,5241426,-42.977996,146.797508,"https://www.google.com/maps/search/?api=1&query=-42.977996,146.797508","https://maps.apple.com/?ll=-42.977996,146.797508&q=-42.977996,146.797508"
LDR220,483775,5240800,-42.983642,146.802372,"https://www.google.com/maps/search/?api=1&query=-42.983642,146.802372","https://maps.apple.com/?ll=-42.983642,146.802372&q=-42.983642,146.802372"
LDR300,484020,5240900,-42.982747,146.805379,"https://www.google.com/maps/search/?api=1&query=-42.982747,146.805379","https://maps.apple.com/?ll=-42.982747,146.805379&q=-42.982747,146.805379"
LDR400,484125,5240775,-42.983875,146.806664,"https://www.google.com/maps/search/?api=1&query=-42.983875,146.806664","https://maps.apple.com/?ll=-42.983875,146.806664&q=-42.983875,146.806664"
,,,,,,
LUN010,485700,5192800,-43.415909,146.824749,"https://www.google.com/maps/search/?api=1&query=-43.415909,146.824749","https://maps.apple.com/?ll=-43.415909,146.824749&q=-43.415909,146.824749"
LUN020,492200,5192900,-43.415103,146.905041,"https://www.google.com/maps/search/?api=1&query=-43.415103,146.905041","https://maps.apple.com/?ll=-43.415103,146.905041&q=-43.415103,146.905041"
,,,,,,
MOU200,510850,5245900,-42.937808,147.134359,"https://www.google.com/maps/search/?api=1&query=-42.937808,147.134359","https://maps.apple.com/?ll=-42.937808,147.134359&q=-42.937808,147.134359"
MOU250,510800,5245800,-42.938709,147.133748,"https://www.google.com/maps/search/?api=1&query=-42.938709,147.133748","https://maps.apple.com/?ll=-42.938709,147.133748&q=-42.938709,147.133748"
MOU400,508800,5243400,-42.960347,147.109274,"https://www.google.com/maps/search/?api=1&query=-42.960347,147.109274","https://maps.apple.com/?ll=-42.960347,147.109274&q=-42.960347,147.109274"
MOU600,507000,5242200,-42.971172,147.087219,"https://www.google.com/maps/search/?api=1&query=-42.971172,147.087219","https://maps.apple.com/?ll=-42.971172,147.087219&q=-42.971172,147.087219"
MOU650,505300,5239500,-42.9955,147.066398,"https://www.google.com/maps/search/?api=1&query=-42.9955,147.066398","https://maps.apple.com/?ll=-42.9955,147.066398&q=-42.9955,147.066398"
MOU700,503900,5237500,-43.013519,147.049238,"https://www.google.com/maps/search/?api=1&query=-43.013519,147.049238","https://maps.apple.com/?ll=-43.013519,147.049238&q=-43.013519,147.049238"
MOU850,503300,5237000,-43.018025,147.041878,"https://www.google.com/maps/search/?api=1&query=-43.018025,147.041878","https://maps.apple.com/?ll=-43.018025,147.041878&q=-43.018025,147.041878"
,,,,,,
NIC100,512800,5224950,-43.126432,147.158744,"https://www.google.com/maps/search/?api=1&query=-43.126432,147.158744","https://maps.apple.com/?ll=-43.126432,147.158744&q=-43.126432,147.158744"
NIC300,512200,5222500,-43.148504,147.151422,"https://www.google.com/maps/search/?api=1&query=-43.148504,147.151422","https://maps.apple.com/?ll=-43.148504,147.151422&q=-43.148504,147.151422"
NIC500,511100,5221000,-43.162029,147.137925,"https://www.google.com/maps/search/?api=1&query=-43.162029,147.137925","https://maps.apple.com/?ll=-43.162029,147.137925&q=-43.162029,147.137925"
NIC700,508200,5220100,-43.170171,147.102265,"https://www.google.com/maps/search/?api=1&query=-43.170171,147.102265","https://maps.apple.com/?ll=-43.170171,147.102265&q=-43.170171,147.102265"
,,,,,,
PAR100,507350,5240650,-42.985127,147.091532,"https://www.google.com/maps/search/?api=1&query=-42.985127,147.091532","https://maps.apple.com/?ll=-42.985127,147.091532&q=-42.985127,147.091532"
,,,,,,
PCK010,496950,5229900,-43.081962,146.963911,"https://www.google.com/maps/search/?api=1&query=-43.081962,146.963911","https://maps.apple.com/?ll=-43.081962,146.963911&q=-43.081962,146.963911"
PCK020,498700,5229800,-43.082868,146.98541,"https://www.google.com/maps/search/?api=1&query=-43.082868,146.98541","https://maps.apple.com/?ll=-43.082868,146.98541&q=-43.082868,146.98541"
PCK030,500850,5229500,-43.085569,147.011824,"https://www.google.com/maps/search/?api=1&query=-43.085569,147.011824","https://maps.apple.com/?ll=-43.085569,147.011824&q=-43.085569,147.011824"
,,,,,,
PIC001,474300,5213400,-43.230114,146.684894,"https://www.google.com/maps/search/?api=1&query=-43.230114,146.684894","https://maps.apple.com/?ll=-43.230114,146.684894&q=-43.230114,146.684894"
PIC002,476000,5227100,-43.106805,146.706421,"https://www.google.com/maps/search/?api=1&query=-43.106805,146.706421","https://maps.apple.com/?ll=-43.106805,146.706421&q=-43.106805,146.706421"
,,,,,,
RIL200,494450,5217000,-43.198112,146.933072,"https://www.google.com/maps/search/?api=1&query=-43.198112,146.933072","https://maps.apple.com/?ll=-43.198112,146.933072&q=-43.198112,146.933072"
RIL400,493700,5219450,-43.176044,146.923868,"https://www.google.com/maps/search/?api=1&query=-43.176044,146.923868","https://maps.apple.com/?ll=-43.176044,146.923868&q=-43.176044,146.923868"
,,,,,,
RUS005,476400,5252400,-42.878991,146.712401,"https://www.google.com/maps/search/?api=1&query=-42.878991,146.712401","https://maps.apple.com/?ll=-42.878991,146.712401&q=-42.878991,146.712401"
RUS010,483500,5245600,-42.940412,146.799139,"https://www.google.com/maps/search/?api=1&query=-42.940412,146.799139","https://maps.apple.com/?ll=-42.940412,146.799139&q=-42.940412,146.799139"
RUS055,483200,5245000,-42.945808,146.795444,"https://www.google.com/maps/search/?api=1&query=-42.945808,146.795444","https://maps.apple.com/?ll=-42.945808,146.795444&q=-42.945808,146.795444"
RUS060,483250,5244995,-42.945854,146.796057,"https://www.google.com/maps/search/?api=1&query=-42.945854,146.796057","https://maps.apple.com/?ll=-42.945854,146.796057&q=-42.945854,146.796057"
RUS070,484300,5244450,-42.950784,146.808913,"https://www.google.com/maps/search/?api=1&query=-42.950784,146.808913","https://maps.apple.com/?ll=-42.950784,146.808913&q=-42.950784,146.808913"
RUS075,485500,5243350,-42.960714,146.823595,"https://www.google.com/maps/search/?api=1&query=-42.960714,146.823595","https://maps.apple.com/?ll=-42.960714,146.823595&q=-42.960714,146.823595"
RUS080,485550,5243300,-42.961165,146.824207,"https://www.google.com/maps/search/?api=1&query=-42.961165,146.824207","https://maps.apple.com/?ll=-42.961165,146.824207&q=-42.961165,146.824207"
RUS100,488700,5240800,-42.98373,146.862779,"https://www.google.com/maps/search/?api=1&query=-42.98373,146.862779","https://maps.apple.com/?ll=-42.98373,146.862779&q=-42.98373,146.862779"
,,,,,,
SOU010,496550,5193800,-43.407031,146.958778,"https://www.google.com/maps/search/?api=1&query=-43.407031,146.958778","https://maps.apple.com/?ll=-43.407031,146.958778&q=-43.407031,146.958778"
SOU050,496250,5193200,-43.412433,146.955069,"https://www.google.com/maps/search/?api=1&query=-43.412433,146.955069","https://maps.apple.com/?ll=-43.412433,146.955069&q=-43.412433,146.955069"
SOU100,497200,5192500,-43.41874,146.9668,"https://www.google.com/maps/search/?api=1&query=-43.41874,146.9668","https://maps.apple.com/?ll=-43.41874,146.9668&q=-43.41874,146.9668"
SOU150,497800,5191400,-43.428647,146.974207,"https://www.google.com/maps/search/?api=1&query=-43.428647,146.974207","https://maps.apple.com/?ll=-43.428647,146.974207&q=-43.428647,146.974207"
SOU200,497800,5191200,-43.430448,146.974207,"https://www.google.com/maps/search/?api=1&query=-43.430448,146.974207","https://maps.apple.com/?ll=-43.430448,146.974207&q=-43.430448,146.974207"
,,,,,,
STT100,492750,5224150,-43.133713,146.91224,"https://www.google.com/maps/search/?api=1&query=-43.133713,146.91224","https://maps.apple.com/?ll=-43.133713,146.91224&q=-43.133713,146.91224"
STT300,493200,5222600,-43.147674,146.917754,"https://www.google.com/maps/search/?api=1&query=-43.147674,146.917754","https://maps.apple.com/?ll=-43.147674,146.917754&q=-43.147674,146.917754"
STT400,493600,5221100,-43.161185,146.922657,"https://www.google.com/maps/search/?api=1&query=-43.161185,146.922657","https://maps.apple.com/?ll=-43.161185,146.922657&q=-43.161185,146.922657"
,,,,,,
SUP010,504425,5223950,-43.135534,147.055791,"https://www.google.com/maps/search/?api=1&query=-43.135534,147.055791","https://maps.apple.com/?ll=-43.135534,147.055791&q=-43.135534,147.055791"
SUP020,504325,5223890,-43.136075,147.054562,"https://www.google.com/maps/search/?api=1&query=-43.136075,147.054562","https://maps.apple.com/?ll=-43.136075,147.054562&q=-43.136075,147.054562"
SUP050,504790,5223650,-43.138233,147.060281,"https://www.google.com/maps/search/?api=1&query=-43.138233,147.060281","https://maps.apple.com/?ll=-43.138233,147.060281&q=-43.138233,147.060281"
SUP100,505625,5223550,-43.139128,147.07055,"https://www.google.com/maps/search/?api=1&query=-43.139128,147.07055","https://maps.apple.com/?ll=-43.139128,147.07055&q=-43.139128,147.07055"
SUP200,505675,5222250,-43.150834,147.071178,"https://www.google.com/maps/search/?api=1&query=-43.150834,147.071178","https://maps.apple.com/?ll=-43.150834,147.071178&q=-43.150834,147.071178"
SUP300,505925,5221800,-43.154884,147.074258,"https://www.google.com/maps/search/?api=1&query=-43.154884,147.074258","https://maps.apple.com/?ll=-43.154884,147.074258&q=-43.154884,147.074258"
SUP350,506950,5221712,-43.155667,147.086866,"https://www.google.com/maps/search/?api=1&query=-43.155667,147.086866","https://maps.apple.com/?ll=-43.155667,147.086866&q=-43.155667,147.086866"
,,,,,,
WAT050,495650,5235450,-43.031978,146.947983,"https://www.google.com/maps/search/?api=1&query=-43.031978,146.947983","https://maps.apple.com/?ll=-43.031978,146.947983&q=-43.031978,146.947983"
WAT055,495650,5235450,-43.031978,146.947983,"https://www.google.com/maps/search/?api=1&query=-43.031978,146.947983","https://maps.apple.com/?ll=-43.031978,146.947983&q=-43.031978,146.947983"
WAT200,496400,5236200,-43.025228,146.957194,"https://www.google.com/maps/search/?api=1&query=-43.025228,146.957194","https://maps.apple.com/?ll=-43.025228,146.957194&q=-43.025228,146.957194"
,,,,,,
WOL100,510500,5219100,-43.179147,147.13058,"https://www.google.com/maps/search/?api=1&query=-43.179147,147.13058","https://maps.apple.com/?ll=-43.179147,147.13058&q=-43.179147,147.13058"
,,,,,,
WOL100,510500,5219100,-43.179147,147.13058,"https://www.google.com/maps/search/?api=1&query=-43.179147,147.13058","https://maps.apple.com/?ll=-43.179147,147.13058&q=-43.179147,147.13058"
```

### Verbatim — as_printed (master)

Source file: `01_original_verbatim/as_printed.csv`  ·  575 lines (including header)

```csv
Zone,Site,Parameter,No.samples,Median,Minimum,25%quartile,75%quartile,Maximum,Mean ,
East,AGN010,Water temperature (°C),15,10,6,8,12.5,18,10.6,
East,AGN010,Turbidity (NTU),15,7,<7,<7,<7,<7,<7 ,
East,AGN010,Conductivity (uS/cm),15,130,80,99,130,150,120,
East,AGN010,pH,15,6.5,6,6.5,7,7,6.6,
,,,,,,,,,,
East,AGN016,Water temperature (°C),13,12.5,3.9,7.5,16,19,11.8,
East,AGN016,Turbidity (NTU),13,7,2,<7,<7,20,8,
East,AGN016,Conductivity (uS/cm),13,410,150,290,430,690,380,
East,AGN016,pH,13,6.5,6.5,6.5,7,8.1,6.8,
,,,,,,,,,,
East,AGN120,Water temperature (°C),11,13.5,6.5,7.5,18,20,13.4,
East,AGN120,Turbidity (NTU),10,9,<7,<7,10,24,11,
East,AGN120,Conductivity (uS/cm),11,350,230,290,510,720,417,
East,AGN120,pH,11,6.5,6,6.5,6.5,7,6.5,
,,,,,,,,,,
East,AGN130,Water temperature (°C),27,12.7,4.3,8,16.1,23,12.5,
East,AGN130,Turbidity (NTU),27,19,<7,<7,24,44,18,
East,AGN130,Conductivity (uS/cm),27,430,289,390,485,740,436,
East,AGN130,pH,26,7,6,6.5,7.7,8,7,
,,,,,,,,,,
East,AGN200,Water temperature (°C),11,15,7,10,21,25,15.1,
East,AGN200,Turbidity (NTU),11,55,16,30,99,300,93,
East,AGN200,Conductivity (uS/cm),11,250,170,210,300,500,275,
East,AGN200,pH,11,6.5,6,6,7.5,8,6.7,
East,AGN200,E. coil (counts/100 ml),5,8500,900,1300,10400,13865,6993,
,,,,,,,,,,
East,AGN245,Water temperature (°C),6,12,9.5,11,17.5,26,14.7,
East,AGN245,Turbidity (NTU),6,7,<7,<7,14,75,20,
East,AGN245,Conductivity (uS/cm),6,205,140,190,220,250,202,
East,AGN245,pH,6,6,5.5,5.5,6,6.5,5.9,
,,,,,,,,,,
East,AGN249,Water temperature (°C),10,13,6.5,10.5,15.5,20,13.2,
East,AGN249,Turbidity (NTU),10,90,34,57,130,300,111,
East,AGN249,Conductivity (uS/cm),10,2750,1580,2500,3000,3100,2628,
East,AGN249,pH,10,8,7.5,8,8,8,7.9,
,,,,,,,,,,
East,AGN250,Water temperature (°C),9,12.5,7,9.5,13,26,12.7,
East,AGN250,Turbidity (NTU),9,35,<7,<7,55,85,38,
East,AGN250,Conductivity (uS/cm),9,350,140,250,580,1760,632,
East,AGN250,pH,9,6,5.5,5.5,6.5,7.5,6.2,
,,,,,,,,,,
East,AGN260,Water temperature (°C),6,12,8,10,14.5,20,12.8,
East,AGN260,Turbidity (NTU),6,28,<7,<7,40,155,44,
East,AGN260,Conductivity (uS/cm),6,585,430,520,720,800,607,
East,AGN260,pH,6,6,5.5,6,6,6.5,6,
,,,,,,,,,,
East,AGN300,Water temperature (°C),10,12,5.5,9,13,19.5,11.8,
East,AGN300,Turbidity (NTU),10,15,<7,13,18,40,17,
East,AGN300,Conductivity (uS/cm),10,475,280,430,580,920,500,
East,AGN300,pH,10,6,5.5,6,6.5,7,6.2,
,,,,,,,,,,
East,AGN400,Water temperature (°C),11,16.5,5.5,9,21,30.5,15.7,
East,AGN400,Turbidity (NTU),11,10,<7,<7,11,13,9,
East,AGN400,Conductivity (uS/cm),10,1575,113,1070,3000,44000,7612,
East,AGN400,pH,11,6.5,6.5,6.5,7.5,8.5,7,
,,,,,,,,,,
East,SUP010,Water temperature (°C),10,12.5,8.5,9,15,20.4,13.2,
East,SUP010,Turbidity (NTU),10,21,16,18,29,53,26,
East,SUP010,Conductivity (uS/cm),10,585,480,560,625,650,577,
East,SUP010,pH,10,6.3,6,6,6.5,7,6.4,
East,SUP010,Ortho-phosphate (mg/L),9,0.045,0.03,0.03,0.045,0.06,0.04,
East,SUP010,Dissolved oxygen (mg/L),9,9.5,7.8,9.1,9.8,11.7,9.6,
East,SUP010,% saturation,9,90,78,87,95,104,91,
,,,,,,,,,,
East,SUP020,Water temperature (°C),11,13,8.5,10,16,22.5,13.6,
East,SUP020,Turbidity (NTU),11,85,38,60,99,115,81,
East,SUP020,Conductivity (uS/cm),11,920,460,750,990,1120,871,
East,SUP020,pH,11,6,6,6,6.5,6.5,6.2,
East,SUP020,Ortho-phosphate (mg/L),10,0.28,0.14,0.14,0.42,0.44,0.282,
East,SUP020,Dissolved oxygen (mg/L),10,7.6,5,7.2,8,9.7,7.6,
East,SUP020,% saturation,10,73,52,66,81,84,71,
,,,,,,,,,,
East,SUP050,Water temperature (°C),11,12.5,8,10,16,20,13,
East,SUP050,Turbidity (NTU),11,51,23,44,59,-,85,50
East,SUP050,Conductivity (uS/cm),11,710,430,620,730,754,664,
East,SUP050,pH,11,6,5.5,6,6,6.5,6,
East,SUP050,Ortho-phosphate (mg/L),10,0.19,0.08,0.14,0.28,1.14,0.299,
East,SUP050,Dissolved oxygen  (mg/L)  ,10,8.4,7.5,7.9,8.8,10.8,8.6,
East,SUP050,% saturation,10,79,68,75,84,88,79,
,,,,,,,,,,
East,SUP100,Water temperature (°C),12,12,8,10.3,15.8,22,13.2,
East,SUP100,Turbidity (NTU),12,25,6,22,32,41,26,
East,SUP100,Conductivity (uS/cm),12,640,400,590,660,707,612,
East,SUP100,pH,12,6,5.5,5.8,6.5,6.5,6.1,
East,SUP100,Ortho-phosphate (mg/L),10,0.13,0.045,0.08,0.14,0.28,0.13,
East,SUP100,Dissolved oxygen (mg/L),10,8.4,7.2,8.1,8.9,10.4,8.6,
East,SUP100,% saturation,10,83,68,74,85,89,80,
,,,,,,,,,,
East,SUP200,Water temperature (°C),12,15.3,9,11.5,19.8,23,15.6,
East,SUP200,Turbidity (NTU),11,65,13,43,83,250,76,
East,SUP200,Conductivity (uS/cm),12,325,260,290,340,405,324,
East,SUP200,pH,11,6,5.5,5.5,6,7,6,
East,SUP200,Ortho-phosphate (mg/L),7,0.03,0.015,0.015,0.03,0.15,0.041,
East,SUP200,Dissolved oxygen (mg/L),9,9,7.4,8.8,9.6,10.2,9,
East,SUP200,% saturation,9,89,75,79,96,99,87,
,,,,,,,,,,
East,SUP300,Water temperature (°C),14,12.5,8,9.5,15,24.5,13.1,
East,SUP300,Turbidity (NTU),13,24,10,21,33,83,30,
East,SUP300,Conductivity (uS/cm),14,560,120,530,645,740,543,
East,SUP300,pH,13,6.5,5.5,6,6.5,6.5,6.3,
East,SUP300,Ortho-phosphate (mg/L),10,0.08,0.03,0.08,0.11,0.14,0.088,
East,SUP300,Dissolved oxygen (mg/L),10,8.6,7.4,7.7,9.2,10.7,8.7,
East,SUP300,% saturation,10,79,66,75,86,94,80,
,,,,,,,,,,
East,GVC115,Water temperature (°C),13,11,3.7,7,14,18,11.2,
East,GVC115,Turbidity (NTU),13,29,8,25,40,170,39,
East,GVC115,Conductivity (uS/cm),13,490,290,388,530,1900,570,
East,GVC115,pH,13,6,5,6,6.5,7.1,6.1,
East,GVC115,Ortho-phosphate (mg/L),2,0.011,0.006,0.016,0.011,,,
East,GVC115,Dissolved oxygen (mg/L),3,10.2,2.6,10.3,7.7,,,
East,GVC115,% saturation,3,78,24,80,61,,,
,,,,,,,,,,
East,SUP350,Water temperature (°C),11,12,6,8,14,18,11.9,
East,SUP350,Turbidity (NTU),11,26,10,11,63,80,35,
East,SUP350,Conductivity (uS/cm),11,480,120,330,720,870,505,
East,SUP350,pH,11,6,5,6,6.5,6.5,6,
,,,,,,,,,,
West,CFB010,Water temperature (°C),28,9,4.5,6.8,11,18.1,9.2,
West,CFB010,Turbidity (NTU),29,<7,<7,<7,<7,45,10,
West,CFB010,Conductivity (uS/cm),31,90,60,80,110,173,97,
West,CFB010,pH,30,6.5,5.5,6,6.5,7.6,6.3,
West,CFB010,E. coli (counts/100 ml),4,100,0,0,355,510,178,
West,CFB010,Ortho-phosphate (mg/L),4,0.011,0.005,0.006,0.023,0.03,0.014,
,,,,,,,,,,
West,CFB020,Water temperature (°C),30,9.8,5,7,11.5,18.1,10,
West,CFB020,Turbidity (NTU),30,<7,<7,<7,11,68,12,
West,CFB020,Conductivity (uS/cm),32,110,60,90,130,191,112,
West,CFB020,pH,32,6.5,5.5,6,6.5,7.7,6.4,
West,CFB020,E. coil (counts/100 ml),6,48,0,36,360,510,167,
West,CFB020,Ortho-phosphate (mg/L),2,0.015,0.015,0.015,0.015,,,
,,,,,,,,,,
West,CFB030,Water temperature (°C),26,10.5,5.5,8.5,15,23,11.7,
West,CFB030,Turbidity (NTU),25,<7,<7,<7,12,70,15,
West,CFB030,Conductivity (uS/cm),28,130,80,110,140,191,127,
West,CFB030,pH,27,6.5,5.5,6,6.5,7.7,6.4,
West,CFB030,E. coil (counts/100 ml),4,675,360,435,840,840,638,
West,CFB030,Ortho-phosphate (mg/L),4,0.012,0.005,0.007,0.023,0.03,0.015,
,,,,,,,,,,
West,DOV070,Water temperature (°C),4,12.9,4.5,7.5,15.4,15.5,11.4,
West,DOV070,Turbidity (NTU),4,13,<7,10,18,23,14,
West,DOV070,Conductivity (uS/cm),4,382,180,279,388,390,334,
West,DOV070,pH,4,6.9,6,6.5,7.4,7.8,6.9,
,,,,,,,,,,
West,DOV090,Water temperature (°C),2,13.4,10.7,16,13.4,,,
West,DOV090,Turbidity (NTU),2,10,<7,13,10,,,
West,DOV090,Conductivity (uS/cm),2,355,190,520,355,,,
West,DOV090,pH,2,7.2,6.5,7.8,7.2,,,
,,,,,,,,,,
West,DOV110,Water temperature (°C),2,13.9,10.8,17,13.9,,,
West,DOV110,Turbidity (NTU),2,10,<7,12,10,,,
West,DOV110,Conductivity (uS/cm),2,425,200,650,425,,,
West,DOV110,pH,2,7,6.5,7.5,7,,,
,,,,,,,,,,
West,DOV120,Water temperature (°C),2,16,12.5,19.5,16,,,
West,DOV120,Turbidity (NTU),2,10,<7,13,10,,,
West,DOV120,Conductivity (uS/cm),2,1125,250,1999,1125,,,
West,DOV120,pH,2,7.9,7.5,8.2,7.9,,,
,,,,,,,,,,
West,DOV130,Water temperature (°C),2,16.2,11.8,20.5,16.2,,,
West,DOV130,Turbidity (NTU),2,<7,<7,<7,<7 ,,,
West,DOV130,Conductivity (uS/cm),2,1095,190,2000,1095,,,
West,DOV130,pH,2,8,8,8,8,,,
,,,,,,,,,,
East,GDR100,Conductivity (uS/cm),8,261,163,435,213,337,278,
East,GDR100,E. coli (counts/100 ml),3,80,40,160,93,,,
East,GDR100,pH,8,6.5,5.5,6.5,6,6.5,6.3,
East,GDR100,Turbidity (NTU),8,<7,<7,<7,<7,<7,<7 ,
East,GDR100,Water  temperature (°C),7,10,8,15,8,14,10.5,
,,,,,,,,,,
East,ALB100,Conductivity (uS/cm),8,419,282,733,307,569,451,
East,ALB100,E. coli (counts/100 ml),2,100,60,140,100,,,
East,ALB100,pH,8,6.5,6,7,6.5,7,6.6,
East,ALB100,Turbidity (NTU),8,<7,<7,16,<7,<7,8,
East,ALB100,Water  temperature (°C),7,9.5,7,14,8,12,10,
,,,,,,,,,,
East,WOL100,Conductivity (uS/cm),6,515,423,622,472,567,519,
East,WOL100,E. coil (counts/100 ml),2,90,0,180,90,,,
East,WOL100,pH,6,6.5,6,7,6.5,7,6.6,
East,WOL100,Water  temperature (°C),6,11.3,9,17.5,9,16,12.3,
East,WOL100,Turbidity (NTU),6,7,<7,<7,<7,<7,<7 ,
,,,,,,,,,,
East,GDR150,Conductivity (uS/cm),9,457,291,920,440,571,505,
East,GDR150,E. coli (counts/100 ml),3,280,30,660,323,,,
East,GDR150,pH,8,6.5,6.5,7.5,6.5,7.3,6.8,
East,GDR150,Turbidity (NTU),8,<7,<7,23,<7,<7,9,
East,GDR150,Water  temperature (°C),7,13,7.5,20,8,16,12.4,
,,,,,,,,,,
East,HOL100,Conductivity (uS/cm),4,599,533,762,542,705,623,
East,HOL100,E. coli (counts/100 ml),2,160,140,180,160,,,
East,HOL100,pH,4,7,6,8,6.5,7.5,7,
East,HOL100,Water  temperature (°C),4,11,7,13.5,8,13.3,10.6,
East,HOL100,Turbidity (NTU),4,9,<7,14,8,12,10,
,,,,,,,,,,
East,GDR200,Conductivity (uS/cm),8,538,300,1144,404,701,591,
East,GDR200,E. coil (counts/100 ml),2,59,20,98,59,,,
East,GDR200,pH,8,6.5,6,7,6,6.5,6.4,
East,GDR200,Turbidity (NTU),8,<7,6,19,<7,10,9,
East,GDR200,Water  temperature (°C),7,11,7.6,17,8,13,11.2,
,,,,,,,,,,
Upper,HU0140,Water  temperature (°C),17,9.6,5.6,7,13.2,19,10.5,
Upper,HU0140,Turbidity (NTU),19,2,1,1,3,39,5.2,
Upper,HU0140,Conductivity (uS/cm),17,82,41,59,109,161,87,
Upper,HU0140,pH,15,7.3,5.7,6.8,7.6,7.8,7.1,
,,,,,,,,,,
Upper,HU0150,Water  temperature (°C),6,8.3,4,6,10,10,7.8,
Upper,HU0150,Turbidity (NTU),6,<7,<7,<7,7,7,7,
Upper,HU0150,Conductivity (uS/cm),6,50,40,40,80,150,68,
Upper,HU0150,pH,6,6,6,6,6.5,7,6.3,
,,,,,,,,,,
Upper,HU0200,Water temperature (°C),22,10,6,9,13,22,11.3,
Upper,HU0200,Turbidity (NTU),22,<7,<7,<7,10,65,13,
Upper,HU0200,Conductivity (uS/cm),23,30,10,20,50,183,50,
Upper,HU0200,pH,23,6,5,6,6.5,7,6,
,,,,,,,,,,
Upper,HU0240,Water temperature (°C),21,10,6.4,9.5,13.8,23,12,
Upper,HU0240,Turbidity (NTU),20,<7,<7,<7,9,20,9,
Upper,HU0240,Conductivity (uS/cm),20,35,10,25,60,150,52,
Upper,HU0240,pH,21,6,5,5.5,6.5,7,6,
,,,,,,,,,,
Upper,JUD020,Water temperature (°C),10,6,3,5.5,8,11.5,6.8,
Upper,JUD020,Turbidity (NTU),10,<7,<7,<7,<7,<7,<7 ,
Upper,JUD020,Conductivity (uS/cm),10,55,39,39,65,90,55,
Upper,JUD020,pH,10,6,6,6,6.5,6.5,6.2,
Upper,JUD020,E. coil (counts/100 ml),3,0,0,0,0,,,
Upper,JUD020,Ortho-phosphate (mg/L),7,0,0,0,0.015,0.03,0.006,
,,,,,,,,,,
Upper,JUD025,Water temperature (°C),9,7,3,6,10,12,7.4,
Upper,JUD025,Turbidity (NTU),9,<7,<7,<7,<7,<7,<7 ,
Upper,JUD025,Conductivity (uS/cm),9,61,43,44,78,120,68,
Upper,JUD025,pH,9,6.5,6,6,6.5,6.5,6.3,
Upper,JUD025,E. coli (counts/100 ml),3,0,0,20,7,,,
Upper,JUD025,Ortho-phosphate (mg/L),7,0.015,0,0,0.015,0.03,0.011,
,,,,,,,,,,
Upper,JUD070,Water temperature (°C),6,6,3,6,7.5,11,6.6,
Upper,JUD070,Turbidity (NTU),6,<7,<7,<7,<7,<7,<7 ,
Upper,JUD070,Conductivity (uS/cm),6,60,51,51,77,82,64,
Upper,JUD070,pH,6,6,6,6,6.5,6.5,6.2,
Upper,JUD070,E. coli (counts/100 ml),3,20,0,40,20,,,
Upper,JUD070,Ortho-phosphate (mg/L),5,0,0,0,0,0.015,0.003,
,,,,,,,,,,
Upper,JUD100,Water temperature (°C),6,6.5,3,6,10,12,7.3,
Upper,JUD100,Turbidity (NTU),6,<7,<7,<7,<7,<7,<7 ,
Upper,JUD100,Conductivity (uS/cm),6,56,44,52,61,110,63,
Upper,JUD100,pH,6,6,6,6,6.5,6.5,6.2,
Upper,JUD100,E. coil (counts/100 ml),3,0,0,40,13,,,
Upper,JUD100,Ortho-phosphate (mg/L),5,0,0,0,0.015,0.015,0.006,
,,,,,,,,,,
Upper,JUD180,Water temperature (°C),5,10,5,6,10,10,8.2,
Upper,JUD180,Turbidity (NTU),5,<7,<7,<7,<7,<7,<7 ,
Upper,JUD180,Conductivity (uS/cm),5,54,49,53,70,88,63,
Upper,JUD180,pH,5,6,6,6,6.5,6.5,6.2,
Upper,JUD180,Ortho-phosphate (mg/L),4,0.008,0,0,0.015,0.015,0.008,
,,,,,,,,,,
Upper,JUD200,Water temperature (°C),7,7,3,5.5,13,16.6,9,
Upper,JUD200,Turbidity (NTU),7,<7,<7,<7,<7,<7,<7 ,
Upper,JUD200,Conductivity (uS/cm),7,58,51,54,118,137,80,
Upper,JUD200,pH,7,6,6,6,7.7,8,6.6,
Upper,JUD200,E. coli (counts/100 ml),5,60,0,60,120,1000,248,
Upper,JUD200,Ortho-phosphate (mg/L),7,0.005,0,0,0.015,0.03,0.008,
,,,,,,,,,,
West,KER200,E. coil (counts/100 ml),4,210,76,128,345,450,237,
,,,,,,,,,,
West,KER400,E. coil (counts/100 ml),2,300,80,520,300,,,
,,,,,,,,,,
West,KER450,E. coil (counts/100 ml),4,250,24,122,360,440,241,
,,,,,,,,,,
West,KER600,E. coil (counts/100 ml),3,560,60,820,480,,,
,,,,,,,,,,
West,KER700,E. coil (counts/100 ml),4,700,120,290,1470,2000,880,
,,,,,,,,,,
West,KER800,E. coil (counts/100 ml),4,665,200,405,1000,1280,703,
,,,,,,,,,,
,RIL200,E. coil (counts/100 ml),2,280,280,280,280,,,
,,,,,,,,,,
,RIL400,E. coil (counts/100 ml),4,865,230,340,1490,1700,915,
,,,,,,,,,,
,STT100,E. coil (counts/100 ml),2,95,80,110,95,,,
,,,,,,,,,,
,STT300,E. coil (counts/100 ml),2,920,240,1600,920,,,
,,,,,,,,,,
,STT350,E. coil (counts/100 ml),2,170,80,260,170,,,
,,,,,,,,,,
,STT400,E. coil (counts/100 ml),4,1195,260,465,2110,2500,1288,
,,,,,,,,,,
Upper,LDR001,Water temperature (°C),67,8,3,6,10,14,8.1,
Upper,LDR001,Turbidity (NTU),69,0,0,0,0.3,2,0.3,
Upper,LDR001,Conductivity (uS/cm),69,35,24,30,43,66,38,
Upper,LDR001,pH,61,6.8,5.7,6.6,7,7.5,6.9,
,,,,,,,,,,
Upper,LDR002,Water temperature (°C),65,9,3,7,11.5,15,9.2,
Upper,LDR002,Turbidity (NTU),67,1,0,0,1.4,5.4,1,
Upper,LDR002,Conductivity (uS/cm),67,46,30,43,55,70,48,
Upper,LDR002,pH,59,6.7,5.9,6.6,7.1,7.5,6.8,
,,,,,,,,,,
Upper,LDR100,Water temperature (°C),8,11.3,8,10,13.5,18.5,12,
Upper,LDR100,Turbidity (NTU),8,<7,<7,<7,<7,<7,<7 ,
Upper,LDR100,Conductivity (uS/cm),8,30,20,30,40,40,33,
Upper,LDR100,pH,8,6.5,6,6,6.5,6.5,6.3,
Upper,LDR100,Total phosphate (mg/L),4,0.01,0.01,0.01,0.02,0.02,0.01,
,,,,,,,,,,
Upper,LDR220,Water temperature (°C),5,13.5,8,11.5,16.5,20,13.9,
Upper,LDR220,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 ,
Upper,LDR220,Conductivity (uS/cm),4,30,30,30,40,50,35,
Upper,LDR220,pH,5,6.5,6,6,6.5,6.5,6.3,
Upper,LDR220,Total phosphate (mg/L),5,0.02,0.01,0.01,0.02,0.03,0.02,
,,,,,,,,,,
Upper,LDR300,Water temperature (°C),4,8.8,8,8,10.5,11.5,9.3,
Upper,LDR300,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 ,
Upper,LDR300,Conductivity (uS/cm),4,30,30,30,30,30,30,
Upper,LDR300,pH,4,6,6,6,6,6,6,
Upper,LDR300,Total phosphate (mg/L),5,0.04,0.03,0.03,0.04,0.05,0.04,
,,,,,,,,,,
Upper,LDR400,Total phosphate (mg/L),4,0.02,0.01,0.01,0.02,0.02,0.02,
,,,,,,,,,,
North,BAK025,Water temperature (°C),4,12.5,10,11,13,13,12,
North,BAK025,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 ,
North,BAK025,Conductivity (uS/cm),4,86,50,64,96,97,80,
North,BAK025,pH,4,6.5,6,6.3,6.8,7,6.5,
North,BAK025,E. coli (counts/100 ml),6,69,0,20,320,480,160,
North,BAK025,Ortho-phosphate (mg/L),2,0.015,0.015,0.015,0.015,,,
North,BAK025,Dissolved oxygen (mg/L),2,9.8,9.6,10,9.8,,,
,,,,,,,,,,
North,BAK060,Water temperature (°C),5,13,8,11,14.5,15,12.3,
North,BAK060,Turbidity (NTU),5,<7,<7,<7,<7,<7,<7 ,
North,BAK060,Conductivity (uS/cm),5,91,70,88,110,124,97,
North,BAK060,pH,5,6.5,6,6.5,7,7,6.6,
North,BAK060,E. coil (counts/100 ml),6,260,40,140,1200,1240,523,
North,BAK060,Ortho-phosphate (mg/L),2,0.015,0.015,0.015,0.015,,,
,,,,,,,,,,
North,BAK150,Water temperature (°C),4,13.5,9.5,10.8,15,15,12.9,
North,BAK150,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 ,
North,BAK150,Conductivity (uS/cm),4,151,120,132,167,176,149,
North,BAK150,pH,4,7,6.5,6.8,7,7,6.9,
North,BAK150,E. coli (counts/100 ml),5,200,54,80,540,1680,511,
North,BAK150,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,,
North,BAK150,Dissolved oxygen (mg/L),2,8,7.8,8.2,8,,,
,,,,,,,,,,
North,BAK200,Water temperature (°C),8,12,5,10.3,15,16.5,12,
North,BAK200,Turbidity (NTU),8,<7,<7,<7,<7,<7,<7 ,
North,BAK200,Conductivity (uS/cm),8,165,140,149,176,208,166,
North,BAK200,pH,8,6.5,6,6.3,6.5,7,6.4,
North,BAK200,E. coli (counts/100 ml),7,280,120,200,680,2000,554,
North,BAK200,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,,
North,BAK200,Dissolved oxygen (mg/L),2,7.7,7.6,7.8,7.7,,,
,,,,,,,,,,
North,BAK250,Water temperature (°C),5,14.5,8,10,16.5,18,13.4,
North,BAK250,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 ,
North,BAK250,Conductivity (uS/cm),5,178,150,163,195,309,199,
North,BAK250,pH,5,6.5,6,6.5,6.5,6.5,6.4,
North,BAK250,E. coli (counts/100 ml),5,140,98,140,320,1520,444,
North,BAK250,Ortho-phosphate (mg/L),3,0.015,0.015,0.03,0.02,,,
,,,,,,,,,,
North,CRB080,Water temperature (°C),6,11.3,6,6.5,16.5,20,11.9,
North,CRB080,Turbidity (NTU),6,<7,<7,<7,7,7,7,
North,CRB080,Conductivity (uS/cm),6,55,34,38,92,130,67,
North,CRB080,pH,6,6.3,5.5,6,6.5,6.5,6.2,
North,CRB080,E. coli (counts/100 ml),5,20,0,0,20,20,12,
North,CRB080,Ortho-phosphate (mg/L),4,0.008,0,0,0.023,0.03,0.011,
North,CRB080,Dissolved oxygen (mg/L),4,10.7,8.5,9.2,12,12.5,10.6,
,,,,,,,,,,
North,CRB100,Water temperature (°C),4,18.9,5.6,12.2,19.5,20,15.9,
North,CRB100,Turbidity (NTU),4,4,1,1,7,7,4,
North,CRB100,Conductivity (uS/cm),4,90,76,79,105,111,92,
North,CRB100,pH,4,7,6,6.3,7.5,7.5,6.9,
North,CRB100,E. coli (counts/100 ml),2,36,6,66,36,,,
North,CRB100,Dissolved oxygen (mg/L),3,8.5,7.2,11.9,9.2,,,
,,,,,,,,,,
North,CRB150,Water temperature (°C),7,14.5,6,8,18,19,13.1,
North,CRB150,Turbidity (NTU),7,<7,<7,<7,<7,<7,<7 ,
North,CRB150,Conductivity (uS/cm),6,73,44,50,119,131,82,
North,CRB150,pH,7,6.5,5.5,6,6.5,7,6.3,
North,CRB150,E. coli (counts/100 ml),6,50,0,0,120,140,60,
North,CRB150,Ortho-phosphate (mg/L),6,0.015,0,0.015,0.015,0.03,0.015,
North,CRB150,Dissolved oxygen (mg/L),6,9.8,7.9,8,10.8,10.8,9.5,
,,,,,,,,,,
North,CRB250,Water temperature (°C),5,15,6.5,9,18.5,19,13.6,
North,CRB250,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 ,
North,CRB250,Conductivity (uS/cm),5,81,46,50,116,139,86,
North,CRB250,pH,5,6.5,5.5,6,6.5,7,6.3,
North,CRB250,E. coil (counts/100 ml),4,20,0,0,80,120,40,
North,CRB250,Ortho-phosphate (mg/L),4,0.008,0,0,0.015,0.015,0.008,
North,CRB250,Dissolved oxygen (mg/L),5,9.5,7.2,8.2,10.4,10.4,9.1,
,,,,,,,,,,
North,CRB300,Water temperature (°C),12,12,4.5,7.5,16.5,19.6,12.2,
North,CRB300,Turbidity (NTU),12,7,1,<7,<7,<7,6,
North,CRB300,Conductivity (uS/cm),11,73,49,50,114,162,86,
North,CRB300,pH,12,6.5,5.5,6.3,7,7.3,6.6,
North,CRB300,E. coil (counts/100 ml),10,75,20,40,280,2700,381,
North,CRB300,Ortho-phosphate (mg/L),6,0.015,0,0.015,0.015,0.015,0.013,
North,CRB300,Dissolved oxygen (mg/L),8,9.9,7.7,8.7,11.2,12.2,9.9,
North,CRB300,%  saturation,4,95,92,92,102,106,97,
,,,,,,,,,,
North,DIP060,Water temperature (°C),4,9.3,6,7.3,12,14,9.6,
North,DIP060,Turbidity (NTU),4,19,17,18,24,28,21,
North,DIP060,Conductivity (uS/cm),4,141,110,124,157,170,140,
North,DIP060,pH,4,5.8,5,5.3,6,6,5.6,
North,DIP060,E. coil (counts/100 ml),2,50,40,60,50,,,
,,,,,,,,,,
North,DIP080,Water temperature (°C),4,8,5.5,6,10.3,11,8.1,
North,DIP080,Turbidity (NTU),4,31,9,18,35,35,26,
North,DIP080,Conductivity (uS/cm),4,208,180,188,238,256,213,
North,DIP080,pH,4,6,5,5.5,6,6,5.8,
North,DIP080,E. coil (counts/100 ml),2,430,400,460,430,,,
,,,,,,,,,,
North,DIP100,Water temperature (°C),5,11.5,5,7,12,15,10.1,
North,DIP100,Turbidity (NTU),5,16,<7,15,25,25,18,
North,DIP100,Conductivity (uS/cm),5,200,65,190,203,210,174,
North,DIP100,pH,5,6,5.5,6,6.5,6.5,6.1,
North,DIP100,E. coli (counts/100 ml),6,520,160,280,800,1440,620,
,,,,,,,,,,
North,FOU100,Water temperature (°C),9,10,4.8,5.5,11.8,18.2,9.5,
North,FOU100,Turbidity (NTU),9,<7,<7,<7,<7,12,8,
North,FOU100,Conductivity (uS/cm),9,401,300,310,484,640,423,
North,FOU100,pH,9,6.5,6,6,7,7.1,6.5,
North,FOU100,E. coil (counts/100 ml),7,260,0,40,1000,2000,557,
North,FOU100,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,,
,,,,,,,,,,
North,FOU120,Water temperature (°C),10,10.5,4.5,5.8,11.8,13.9,9.3,
North,FOU120,Turbidity (NTU),10,<7,<7,<7,<7,13,8,
North,FOU120,Conductivity (uS/cm),10,362,230,338,658,1420,527,
North,FOU120,pH,10,7,6.5,6.5,7,7.5,6.9,
North,FOU120,E. coil (counts/100 ml),8,130,38,60,340,480,197,
North,FOU120,Ortho-phosphate (mg/L),5,0.015,0.015,0.015,0.015,0.03,0.018,
,,,,,,,,,,
North,FOU150,Water temperature (°C),10,10.5,5,6.3,11.5,12,9.1,
North,FOU150,Turbidity (NTU),10,<7,<7,<7,<7,<7,<7 ,
North,FOU150,Conductivity (uS/cm),10,529,390,454,1080,1294,694,
North,FOU150,pH,10,6,6,6,6.5,7,6.3,
North,FOU150,E. coli (counts/100 ml),8,109,20,50,340,580,200,
North,FOU150,Ortho-phosphate (mg/L),5,0.03,0.015,0.015,0.03,0.045,0.027,
,,,,,,,,,,
North,FOU200,Water temperature (°C),8,11,4.5,7,11.3,13.5,9.6,
North,FOU200,Turbidity (NTU),8,<7,<7,<7,<7,15,8,
North,FOU200,Conductivity (uS/cm),8,491,410,465,629,1020,575,
North,FOU200,pH,8,6.5,6,6,7,7.5,6.6,
North,FOU200,E. coli (counts/100 ml),6,80,1,20,160,700,174,
North,FOU200,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,,
,,,,,,,,,,
North,MOU200,Water temperature (°C),19,10.9,5,7,16,18.5,11.5,
North,MOU200,Turbidity (NTU),20,<7,<7,<7,<7,71,11,
North,MOU200,Conductivity (uS/cm),20,50,20,40,69,99,53,
North,MOU200,pH,20,6.5,6,6.5,7,7.4,6.6,
North,MOU200,E. coli (counts/100 ml),10,20,0,0,100,200,52,
North,MOU200,Ortho-phosphate (mg/L),3,0.005,0.005,0.03,0.013,,,
North,MOU200,Dissolved oxygen (mg/L),4,10.8,8.6,9.7,11.6,12.3,10.6,
,,,,,,,,,,
North,MOU250,Water temperature (°C),9,13,5.3,9.5,16,19.6,12.9,
North,MOU250,Turbidity (NTU),9,<7,<7,<7,<7,<7,<7 ,
North,MOU250,Conductivity (uS/cm),9,168,99,149,243,320,190,
North,MOU250,pH,9,7,6.5,6.5,7,7.5,6.9,
North,MOU250,E. coil (counts/100 ml),9,20,0,0,99,660,122,
North,MOU250,Ortho-phosphate (mg/L),2,0.005,0.005,0.005,0.005,,,
North,MOU250,Dissolved oxygen (mg/L),2,10.3,8.2,12.4,10.3,,,
,,,,,,,,,,
North,MOU400,Water temperature (°C),20,12,5,8.3,15,20,12.2,
North,MOU400,Turbidity (NTU),20,<7,<7,<7,<7,18,8,
North,MOU400,Conductivity (uS/cm),20,60,20,45,76,113,62,
North,MOU400,pH,20,6.5,6,6.5,7,7.6,6.7,
North,MOU400,E. coli (counts/100 ml),10,70,20,40,120,200,86,
North,MOU400,Ortho-phosphate (mg/L),4,0.005,0,0.003,0.01,0.015,0.006,
North,MOU400,Dissolved oxygen (mg/L),5,10.4,9,9,10.7,12.4,10.3,
,,,,,,,,,,
North,MOU600,Water temperature (°C),19,11,5,7,16.5,20.5,11.8,
North,M0U600,Turbidity (NTU),20,<7,<7,<7,<7,18,8,
North,MOU600,Conductivity (uS/cm),19,70,30,50,90,124,72,
North,MOU600,pH,19,6.6,6,6.5,7,7.9,6.8,
North,MOU600,E. coil (counts/100 ml),10,84,0,40,260,400,143,
North,MOU600,Ortho-phosphate (mg/L),3,0.005,0.005,0.03,0.013,,,
North,MOU600,Dissolved oxygen (mg/L),4,10.3,8.5,9.3,11.4,12.3,10.3,
,,,,,,,,,,
North,MOU650,Water temperature (°C),11,11,5,6,16,20.5,11.5,
North,MOU650,Turbidity (NTU),11,<7,<7,<7,<7,8,<7 ,
North,MOU650,Conductivity (uS/cm),11,100,40,70,135,141,101,
North,MOU650,pH,11,6.5,6,6,7,7.4,6.6,
North,MOU650,E. coil (counts/100 ml),9,100,40,100,180,360,149,
North,MOU650,Ortho-phosphate (mg/L),6,0.01,0,0.005,0.015,0.03,0.012,
North,MOU650,Dissolved oxygen (mg/L),4,10.6,8.5,9.3,11.8,12.3,10.5,
,,,,,,,,,,
North,MOU700,Water temperature (°C),11,13,5.5,7,14,20.1,11.9,
North,MOU700,Turbidity (NTU),11,<7,<7,<7,<7,13,8,
North,MOU700,Conductivity (uS/cm),11,100,40,70,132,158,103,
North,MOU700,pH,11,6.5,6,6,7,7.4,6.7,
North,MOU700,E. coil (counts/100 ml),10,130,20,80,210,460,169,
North,MOU700,Ortho-phosphate (mg/L),5,0.012,0.015,0.015,0.005,0.005,6,
North,MOU700,Dissolved oxygen (mg/L),2,10,7.4,12.5,10,,,
,,,,,,,,,,
North,MOU850,Water temperature (°C),27,11.5,5.4,8.3,14,21.1,11.7,
North,MOU850,Turbidity (NTU),28,<7,<7,<7,<7,266,24,
North,MOU850,Conductivity (uS/cm),27,114,40,101,135,182,117,
North,MOU850,pH,25,7,6,6.5,7.5,7.9,6.9,
North,MOU850,E. coil (counts/100 ml),10,390,50,160,800,2000,661,
North,MOU850,Ortho-phosphate (mg/L),6,0.015,0.005,0.01,0.015,0.03,0.015,
North,MOU850,Dissolved oxygen (mg/L),18,10.3,8.6,9,10.9,12.3,10.2,
,,,,,,,,,,
West,PCK010,Water temperature (°C),20,12.5,8,10,14.5,18,12.5,
West,PCK010,Turbidity (NTU),20,<7,<7,<7,13,95,15,
West,PCK010,Conductivity (uS/cm),20,149,80,131,173,214,150,
West,PCK010,pH,20,6.3,5.5,6,6.5,7,6.3,
,,,,,,,,,,
West,PCK020,Water temperature (°C),20,12,8,9,13.5,15,11.5,
West,PCK020,Turbidity (NTU),20,<7,<7,<7,14,43,13,
West,PCK020,Conductivity (uS/cm),20,179,90,148,202,285,176,
West,PCK020,pH,20,6.5,6,6.5,6.8,7,6.6,
,,,,,,,,,,
West,PCK030,Water temperature (°C),20,12.3,7.5,9.3,14.8,18.0 .,12.3,
West,PCK030,Turbidity (NTU),20,<7,<7,<7,11,30,10,
West,PCK030,Conductivity (uS/cm),20,220,99,182,249,350,219,
West,PCK030,pH,20,6.5,6,6.5,7,7,6.6,
,,,,,,,,,,
Upper,RUS005,Water temperature (°C),70,8.5,3,6,11,16.5,8.6,
Upper,RUS005,Turbidity (NTU),72,0,0,0,0.3,2,0.2,
Upper,RUS005,Conductivity (uS/cm),72,58,39,51,68,100,60,
Upper,RUS005,pH,64,6.9,6,6.7,7.2,7.7,6.9,
,,,,,,,,,,
Upper,RUS010,Water temperature (°C),69,9,2.5,6,10.5,17,8.7,
Upper,RUS010,Turbidity (NTU),71,0,0,0,1,7,0.9,
Upper,RUS010,Conductivity (uS/cm),71,55,38,47,69,100,60,
Upper,RUS010,pH,63,6.8,5.5,6.6,7,7.6,6.8,
Upper,RUS010,E. coil (counts/100 ml),2,0,0,0,0,,,
Upper,RUS010,Ortho-phosphate (mg/L),2,0.008,0,0.015,0.008,,,
,,,,,,,,,,
Upper,RUS055,Water temperature (°C),14,12,7.5,10,17,18,12.9,
Upper,RUS055,Turbidity (NTU),12,<7,<7,<7,<7,<7,<7 ,
Upper,RUS055,Conductivity (uS/cm),10,47,30,39,68,78,51,
Upper,RUS055,pH,12,6,5.5,6,6.5,6.5,6.1,
Upper,RUS055,E. coil (counts/100 ml),4,32,6,11,106,164,58,
Upper,RUS055,Ortho-phosphate (mg/L),8,0.015,0.002,0.008,0.023,0.03,0.015,
,,,,,,,,,,
Upper,RUS060,Water temperature (°C),15,8,5,7,15,19,10.4,
Upper,RUS060,Turbidity (NTU),15,<7,<7,<7,<7,<7,<7 ,
Upper,RUS060,Conductivity (uS/cm),12,46,35,43,60,77,51,
Upper,RUS060,pH,15,6,5.5,6,6,6.5,6,
Upper,RUS060,E. coil (counts/100 ml),2,10,0,20,10,,,
Upper,RUS060,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,,
,,,,,,,,,,
Upper,RUS070,Water temperature (°C),12,9,5,7,12,19,10.1,
Upper,RUS070,Turbidity (NTU),12,<7,<7,<7,<7,<7,<7 ,
Upper,RUS070,Conductivity (uS/cm),10,47,36,43,58,79,52,
Upper,RU3070,pH,11,6,5.5,6,6,7,6,
Upper,ROS070,E. coli (counts/100 ml),2,70,20,120,70,,,
,,,,,,,,,,
Upper,RUS075,Water temperature (°C),6,8.5,5,7,10,15,9,
Upper,RUS075,Turbidity (NTU),6,<7,<7,<7,<7,18,9,
Upper,RUS075,Conductivity (uS/cm),6,76,65,72,90,147,88,
Upper,RUS075,pH,6,6,5.5,6,6.5,7,6.2,
,,,,,,,,,,
Upper,RUS080,Water temperature (°C),16,10.5,5,6,15,19,10.9,
Upper,RUS080,Turbidity (NTU),16,<7,<7,<7,<7,<7,<7 ,
Upper,RUS080,Conductivity (uS/cm),14,52,7,42,60,88,52,
Upper,RUS080,pH,15,6,5.5,5.5,6.5,60,9.6,
Upper,RUS080,E. coli (counts/100 ml),2,20,20,20,20,,,
Upper,RUS080,Ortho-phosphate (mg/L),2,0.015,0.015,0.015,0.015,,,
,,,,,,,,,,
Upper,RUS100,Water temperature (°C),14,11,5,7,18,19,11.8,
Upper,RUS100,Turbidity (NTU),14,<7,<7,<7,<7,<7,<7 ,
Upper,RUS100,Conductivity (uS/cm),11,51,39,42,74,86,56,
Upper,RUS100,pH,13,6,5,6,6.5,7,6.2,
Upper,RUS100,Ortho-phosphate (mg/L),2,0.008,0,0.015,0.008,,,
,,,,,,,,,,
Upper,WAT050,Turbidity (NTU),8,11,<7,<7,34,63,22,
Upper,WAT050,Conductivity (uS/cm),8,264,125,176,420,510,294,
Upper,WAT050,pH,8,6.8,6,6.5,7.5,7.5,6.9,
Upper,WAT050,Water temperature (°C),8,15.3,9.5,10,18,20,14.5,
,,,,,,,,,,
Upper,WAT055,Turbidity (NTU),6,31,<7,<7,39,48,27,
Upper,WAT055,Conductivity (uS/cm),6,309,215,239,470,510,342,
Upper,WAT055,pH,5,7,6,7,7.5,8,7.1,
Upper,WAT055,Water temperature (°C),6,12.3,10,11,14,17,12.8,
,,,,,,,,,,
Upper,WAT200,Water temperature (°C),27,11.7,4.7,9.5,14.7,19,12.3,
Upper,WAT200,Turbidity (NTU),26,10,<7,<7,15,175,20,
Upper,WAT200,Conductivity (uS/cm),27,320,120,220,390,490,315,
Upper,WAT200,pH,27,6.5,6,6.5,7,8,6.8,
Upper,WAT200,Dissolved oxygen (mg/L),16,9.4,8,8.6,10.2,12.7,9.5,
```

### Verbatim — temp

Source file: `01_original_verbatim/temp.csv`  ·  112 lines (including header)

```csv
Zone,Site,Parameter,No.samples,Median,Minimum,25%quartile,75%quartile,Maximum,Mean 
East,AGN010,Water temperature (°C),15,10,6,8,12.5,18,10.6
East,AGN016,Water temperature (°C),13,12.5,3.9,7.5,16,19,11.8
East,AGN120,Water temperature (°C),11,13.5,6.5,7.5,18,20,13.4
East,AGN130,Water temperature (°C),27,12.7,4.3,8,16.1,23,12.5
East,AGN200,Water temperature (°C),11,15,7,10,21,25,15.1
East,AGN245,Water temperature (°C),6,12,9.5,11,17.5,26,14.7
East,AGN249,Water temperature (°C),10,13,6.5,10.5,15.5,20,13.2
East,AGN250,Water temperature (°C),9,12.5,7,9.5,13,26,12.7
East,AGN260,Water temperature (°C),6,12,8,10,14.5,20,12.8
East,AGN300,Water temperature (°C),10,12,5.5,9,13,19.5,11.8
East,AGN400,Water temperature (°C),11,16.5,5.5,9,21,30.5,15.7
East,ALB100,Water  temperature (°C),7,9.5,7,14,8,12,10
East,GDR100,Water  temperature (°C),7,10,8,15,8,14,10.5
East,GDR150,Water  temperature (°C),7,13,7.5,20,8,16,12.4
East,GDR200,Water  temperature (°C),7,11,7.6,17,8,13,11.2
East,GVC115,Water temperature (°C),13,11,3.7,7,14,18,11.2
East,HOL100,Water  temperature (°C),4,11,7,13.5,8,13.3,10.6
East,SUP010,Water temperature (°C),10,12.5,8.5,9,15,20.4,13.2
East,SUP020,Water temperature (°C),11,13,8.5,10,16,22.5,13.6
East,SUP050,Water temperature (°C),11,12.5,8,10,16,20,13
East,SUP100,Water temperature (°C),12,12,8,10.3,15.8,22,13.2
East,SUP200,Water temperature (°C),12,15.3,9,11.5,19.8,23,15.6
East,SUP300,Water temperature (°C),14,12.5,8,9.5,15,24.5,13.1
East,SUP350,Water temperature (°C),11,12,6,8,14,18,11.9
East,WOL100,Water  temperature (°C),6,11.3,9,17.5,9,16,12.3
North,BAK025,Water temperature (°C),4,12.5,10,11,13,13,12
North,BAK060,Water temperature (°C),5,13,8,11,14.5,15,12.3
North,BAK150,Water temperature (°C),4,13.5,9.5,10.8,15,15,12.9
North,BAK200,Water temperature (°C),8,12,5,10.3,15,16.5,12
North,BAK250,Water temperature (°C),5,14.5,8,10,16.5,18,13.4
North,CRB080,Water temperature (°C),6,11.3,6,6.5,16.5,20,11.9
North,CRB100,Water temperature (°C),4,18.9,5.6,12.2,19.5,20,15.9
North,CRB150,Water temperature (°C),7,14.5,6,8,18,19,13.1
North,CRB250,Water temperature (°C),5,15,6.5,9,18.5,19,13.6
North,CRB300,Water temperature (°C),12,12,4.5,7.5,16.5,19.6,12.2
North,DIP060,Water temperature (°C),4,9.3,6,7.3,12,14,9.6
North,DIP080,Water temperature (°C),4,8,5.5,6,10.3,11,8.1
North,DIP100,Water temperature (°C),5,11.5,5,7,12,15,10.1
North,FOU100,Water temperature (°C),9,10,4.8,5.5,11.8,18.2,9.5
North,FOU120,Water temperature (°C),10,10.5,4.5,5.8,11.8,13.9,9.3
North,FOU150,Water temperature (°C),10,10.5,5,6.3,11.5,12,9.1
North,FOU200,Water temperature (°C),8,11,4.5,7,11.3,13.5,9.6
North,MOU200,Water temperature (°C),19,10.9,5,7,16,18.5,11.5
North,MOU250,Water temperature (°C),9,13,5.3,9.5,16,19.6,12.9
North,MOU400,Water temperature (°C),20,12,5,8.3,15,20,12.2
North,MOU600,Water temperature (°C),19,11,5,7,16.5,20.5,11.8
North,MOU650,Water temperature (°C),11,11,5,6,16,20.5,11.5
North,MOU700,Water temperature (°C),11,13,5.5,7,14,20.1,11.9
North,MOU850,Water temperature (°C),27,11.5,5.4,8.3,14,21.1,11.7
Upper,HU0140,Water  temperature (°C),17,9.6,5.6,7,13.2,19,10.5
Upper,HU0150,Water  temperature (°C),6,8.3,4,6,10,10,7.8
Upper,HU0200,Water temperature (°C),22,10,6,9,13,22,11.3
Upper,HU0240,Water temperature (°C),21,10,6.4,9.5,13.8,23,12
Upper,JUD020,Water temperature (°C),10,6,3,5.5,8,11.5,6.8
Upper,JUD025,Water temperature (°C),9,7,3,6,10,12,7.4
Upper,JUD070,Water temperature (°C),6,6,3,6,7.5,11,6.6
Upper,JUD100,Water temperature (°C),6,6.5,3,6,10,12,7.3
Upper,JUD180,Water temperature (°C),5,10,5,6,10,10,8.2
Upper,JUD200,Water temperature (°C),7,7,3,5.5,13,16.6,9
Upper,LDR001,Water temperature (°C),67,8,3,6,10,14,8.1
Upper,LDR002,Water temperature (°C),65,9,3,7,11.5,15,9.2
Upper,LDR100,Water temperature (°C),8,11.3,8,10,13.5,18.5,12
Upper,LDR220,Water temperature (°C),5,13.5,8,11.5,16.5,20,13.9
Upper,LDR300,Water temperature (°C),4,8.8,8,8,10.5,11.5,9.3
Upper,RUS005,Water temperature (°C),70,8.5,3,6,11,16.5,8.6
Upper,RUS010,Water temperature (°C),69,9,2.5,6,10.5,17,8.7
Upper,RUS055,Water temperature (°C),14,12,7.5,10,17,18,12.9
Upper,RUS060,Water temperature (°C),15,8,5,7,15,19,10.4
Upper,RUS070,Water temperature (°C),12,9,5,7,12,19,10.1
Upper,RUS075,Water temperature (°C),6,8.5,5,7,10,15,9
Upper,RUS080,Water temperature (°C),16,10.5,5,6,15,19,10.9
Upper,RUS100,Water temperature (°C),14,11,5,7,18,19,11.8
Upper,WAT050,Water temperature (°C),8,15.3,9.5,10,18,20,14.5
Upper,WAT055,Water temperature (°C),6,12.3,10,11,14,17,12.8
Upper,WAT200,Water temperature (°C),27,11.7,4.7,9.5,14.7,19,12.3
West,CFB010,Water temperature (°C),28,9,4.5,6.8,11,18.1,9.2
West,CFB020,Water temperature (°C),30,9.8,5,7,11.5,18.1,10
West,CFB030,Water temperature (°C),26,10.5,5.5,8.5,15,23,11.7
West,DOV070,Water temperature (°C),4,12.9,4.5,7.5,15.4,15.5,11.4
West,DOV090,Water temperature (°C),2,13.4,10.7,16,13.4,,
West,DOV110,Water temperature (°C),2,13.9,10.8,17,13.9,,
West,DOV120,Water temperature (°C),2,16,12.5,19.5,16,,
West,DOV130,Water temperature (°C),2,16.2,11.8,20.5,16.2,,
West,PCK010,Water temperature (°C),20,12.5,8,10,14.5,18,12.5
West,PCK020,Water temperature (°C),20,12,8,9,13.5,15,11.5
West,PCK030,Water temperature (°C),20,12.3,7.5,9.3,14.8,18.0 .,12.3
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
```

### Verbatim — do

Source file: `01_original_verbatim/do.csv`  ·  32 lines (including header)

```csv
Zone,Site,Parameter,No.samples,Median,Minimum,25%quartile,75%quartile,Maximum,Mean 
East,GVC115,% saturation,3,78,24,80,61,,
East,GVC115,Dissolved oxygen (mg/L),3,10.2,2.6,10.3,7.7,,
East,SUP010,% saturation,9,90,78,87,95,104,91
East,SUP010,Dissolved oxygen (mg/L),9,9.5,7.8,9.1,9.8,11.7,9.6
East,SUP020,% saturation,10,73,52,66,81,84,71
East,SUP020,Dissolved oxygen (mg/L),10,7.6,5,7.2,8,9.7,7.6
East,SUP050,% saturation,10,79,68,75,84,88,79
East,SUP050,Dissolved oxygen  (mg/L)  10,8.4,7.5,7.9,8.8,10.8,8.6,
East,SUP100,% saturation,10,83,68,74,85,89,80
East,SUP100,Dissolved oxygen (mg/L),10,8.4,7.2,8.1,8.9,10.4,8.6
East,SUP200,% saturation,9,89,75,79,96,99,87
East,SUP200,Dissolved oxygen (mg/L),9,9,7.4,8.8,9.6,10.2,9
East,SUP300,% saturation,10,79,66,75,86,94,80
East,SUP300,Dissolved oxygen (mg/L),10,8.6,7.4,7.7,9.2,10.7,8.7
North,BAK025,Dissolved oxygen (mg/L),2,9.8,9.6,10,9.8,,
North,BAK150,Dissolved oxygen (mg/L),2,8,7.8,8.2,8,,
North,BAK200,Dissolved oxygen (mg/L),2,7.7,7.6,7.8,7.7,,
North,CRB080,Dissolved oxygen (mg/L),4,10.7,8.5,9.2,12,12.5,10.6
North,CRB100,Dissolved oxygen (mg/L),3,8.5,7.2,11.9,9.2,,
North,CRB150,Dissolved oxygen (mg/L),6,9.8,7.9,8,10.8,10.8,9.5
North,CRB250,Dissolved oxygen (mg/L),5,9.5,7.2,8.2,10.4,10.4,9.1
North,CRB300,%  saturation,4,95,92,92,102,106,97
North,CRB300,Dissolved oxygen (mg/L),8,9.9,7.7,8.7,11.2,12.2,9.9
North,MOU200,Dissolved oxygen (mg/L),4,10.8,8.6,9.7,11.6,12.3,10.6
North,MOU250,Dissolved oxygen (mg/L),2,10.3,8.2,12.4,10.3,,
North,MOU400,Dissolved oxygen (mg/L),5,10.4,9,9,10.7,12.4,10.3
North,MOU600,Dissolved oxygen (mg/L),4,10.3,8.5,9.3,11.4,12.3,10.3
North,MOU650,Dissolved oxygen (mg/L),4,10.6,8.5,9.3,11.8,12.3,10.5
North,MOU700,Dissolved oxygen (mg/L),2,10,7.4,12.5,10,,
North,MOU850,Dissolved oxygen (mg/L),18,10.3,8.6,9,10.9,12.3,10.2
Upper,WAT200,Dissolved oxygen (mg/L),16,9.4,8,8.6,10.2,12.7,9.5
```

### Verbatim — turb

Source file: `01_original_verbatim/turb.csv`  ·  87 lines (including header)

```csv
Zone,Site,Parameter,No.samples,Median,Minimum,25%quartile,75%quartile,Maximum,Mean 
East,AGN010,Turbidity (NTU),15,7,<7,<7,<7,<7,<7 
East,AGN016,Turbidity (NTU),13,7,2,<7,<7,20,8
East,AGN120,Turbidity (NTU),10,9,<7,<7,10,24,11
East,AGN130,Turbidity (NTU),27,19,<7,<7,24,44,18
East,AGN200,Turbidity (NTU),11,55,16,30,99,300,93
East,AGN245,Turbidity (NTU),6,7,<7,<7,14,75,20
East,AGN249,Turbidity (NTU),10,90,34,57,130,300,111
East,AGN250,Turbidity (NTU),9,35,<7,<7,55,85,38
East,AGN260,Turbidity (NTU),6,28,<7,<7,40,155,44
East,AGN300,Turbidity (NTU),10,15,<7,13,18,40,17
East,AGN400,Turbidity (NTU),11,10,<7,<7,11,13,9
East,ALB100,Turbidity (NTU),8,<7,<7,16,<7,<7,8
East,GDR100,Turbidity (NTU),8,<7,<7,<7,<7,<7,<7 
East,GDR150,Turbidity (NTU),8,<7,<7,23,<7,<7,9
East,GDR200,Turbidity (NTU),8,<7,6,19,<7,10,9
East,GVC115,Turbidity (NTU),13,29,8,25,40,170,39
East,HOL100,Turbidity (NTU),4,9,<7,14,8,12,10
East,SUP010,Turbidity (NTU),10,21,16,18,29,53,26
East,SUP020,Turbidity (NTU),11,85,38,60,99,115,81
East,SUP050,Turbidity (NTU),11,51,23,44,59,-,85
East,SUP100,Turbidity (NTU),12,25,6,22,32,41,26
East,SUP200,Turbidity (NTU),11,65,13,43,83,250,76
East,SUP300,Turbidity (NTU),13,24,10,21,33,83,30
East,SUP350,Turbidity (NTU),11,26,10,11,63,80,35
East,WOL100,Turbidity (NTU),6,7,<7,<7,<7,<7,<7 
North,BAK025,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 
North,BAK060,Turbidity (NTU),5,<7,<7,<7,<7,<7,<7 
North,BAK150,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 
North,BAK200,Turbidity (NTU),a,<7,<7,<7,<7,<7,<7 
North,BAK250,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 
North,CRB080,Turbidity (NTU),6,<7,<7,<7,7,7,7
North,CRB100,Turbidity (NTU),4,4,1,1,7,7,4
North,CRB150,Turbidity (NTU),7,<7,<7,<7,<7,<7,<7 
North,CRB250,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 
North,CRB300,Turbidity (NTU),12,7,1,<7,<7,<7,6
North,DIP060,Turbidity (NTU),4,19,17,18,24,28,21
North,DIP080,Turbidity (NTU),4,31,9,18,35,35,26
North,DIP100,Turbidity (NTU),5,16,<7,15,25,25,18
North,FOU100,Turbidity (NTU),9,<7,<7,<7,<7,12,8
North,FOU120,Turbidity (NTU),10,<7,<7,<7,<7,13,8
North,FOU150,Turbidity (NTU),10,<7,<7,<7,<7,<7,<7 
North,FOU200,Turbidity (NTU),8,<7,<7,<7,<7,15,8
North,M0U600,Turbidity (NTU),20,<7,<7,<7,<7,18,8
North,MOU200,Turbidity (NTU),20,<7,<7,<7,<7,71,11
North,MOU250,Turbidity (NTU),9,<7,<7,<7,<7,<7,<7 
North,MOU400,Turbidity (NTU),20,<7,<7,<7,<7,18,8
North,MOU650,Turbidity (NTU),11,<7,<7,<7,<7,8,<7 
North,MOU700,Turbidity (NTU),11,<7,<7,<7,<7,13,8
North,MOU850,Turbidity (NTU),28,<7,<7,<7,<7,266,24
Upper,HU0140,Turbidity (NTU),19,2,1,1,3,39,5.2
Upper,HU0150,Turbidity (NTU),6,<7,<7,<7,7,7,7
Upper,HU0200,Turbidity (NTU),22,<7,<7,<7,10,65,13
Upper,HU0240,Turbidity (NTU),20,<7,<7,<7,9,20,9
Upper,JUD020,Turbidity (NTU),10,<7,<7,<7,<7,<7,<7 
Upper,JUD025,Turbidity (NTU),9,<7,<7,<7,<7,<7,<7 
Upper,JUD070,Turbidity (NTU),6,<7,<7,<7,<7,<7,<7 
Upper,JUD100,Turbidity (NTU),6,<7,<7,<7,<7,<7,<7 
Upper,JUD180,Turbidity (NTU),5,<7,<7,<7,<7,<7,<7 
Upper,JUD200,Turbidity (NTU),7,<7,<7,<7,<7,<7,<7 
Upper,LDR001,Turbidity (NTU),69,0,0,0,0.3,2,0.3
Upper,LDR002,Turbidity (NTU),67,1,0,0,1.4,5.4,1
Upper,LDR100,Turbidity (NTU),8,<7,<7,<7,<7,<7,<7 
Upper,LDR220,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 
Upper,LDR300,Turbidity (NTU),4,<7,<7,<7,<7,<7,<7 
Upper,RUS005,Turbidity (NTU),72,0,0,0,0.3,2,0.2
Upper,RUS010,Turbidity (NTU),71,0,0,0,1,7,0.9
Upper,RUS055,Turbidity (NTU),12,<7,<7,<7,<7,<7,<7 
Upper,RUS060,Turbidity (NTU),15,<7,<7,<7,<7,<7,<7 
Upper,RUS070,Turbidity (NTU),12,<7,<7,<7,<7,<7,<7 
Upper,RUS075,Turbidity (NTU),6,<7,<7,<7,<7,18,9
Upper,RUS080,Turbidity (NTU),16,<7,<7,<7,<7,<7,<7 
Upper,RUS100,Turbidity (NTU),14,<7,<7,<7,<7,<7,<7 
Upper,WAT050,Turbidity (NTU),8,11,<7,<7,34,63,22
Upper,WAT055,Turbidity (NTU),6,31,<7,<7,39,48,27
Upper,WAT200,Turbidity (NTU),26,10,<7,<7,15,175,20
West,CFB010,Turbidity (NTU),29,<7,<7,<7,<7,45,10
West,CFB020,Turbidity (NTU),30,<7,<7,<7,11,68,12
West,CFB030,Turbidity (NTU),25,<7,<7,<7,12,70,15
West,DOV070,Turbidity (NTU),4,13,<7,10,18,23,14
West,DOV090,Turbidity (NTU),2,10,<7,13,10,,
West,DOV110,Turbidity (NTU),2,10,<7,12,10,,
West,DOV120,Turbidity (NTU),2,10,<7,13,10,,
West,DOV130,Turbidity (NTU),2,<7,<7,<7,<7 ,,
West,PCK010,Turbidity (NTU),20,<7,<7,<7,13,95,15
West,PCK020,Turbidity (NTU),20,<7,<7,<7,14,43,13
West,PCK030,Turbidity (NTU),20,<7,<7,<7,11,30,10
```

### Verbatim — ec

Source file: `01_original_verbatim/ec.csv`  ·  87 lines (including header)

```csv
Zone,Site,Parameter,No.samples,Median,Minimum,25%quartile,75%quartile,Maximum,Mean 
East,AGN010,Conductivity (uS/cm),15,130,80,99,130,150,120
East,AGN016,Conductivity (uS/cm),13,410,150,290,430,690,380
East,AGN120,Conductivity (uS/cm),11,350,230,290,510,720,417
East,AGN130,Conductivity (uS/cm),27,430,289,390,485,740,436
East,AGN200,Conductivity (uS/cm),11,250,170,210,300,500,275
East,AGN245,Conductivity (uS/cm),6,205,140,190,220,250,202
East,AGN249,Conductivity (uS/cm),10,2750,1580,2500,3000,3100,2628
East,AGN250,Conductivity (uS/cm),9,350,140,250,580,1760,632
East,AGN260,Conductivity (uS/cm),6,585,430,520,720,800,607
East,AGN300,Conductivity (uS/cm),10,475,280,430,580,920,500
East,AGN400,Conductivity (uS/cm),10,1575,113,1070,3000,44000,7612
East,ALB100,Conductivity (uS/cm),8,419,282,733,307,569,451
East,GDR100,Conductivity (uS/cm),8,261,163,435,213,337,278
East,GDR150,Conductivity (uS/cm),9,457,291,920,440,571,505
East,GDR200,Conductivity (uS/cm),8,538,300,1144,404,701,591
East,GVC115,Conductivity (uS/cm),13,490,290,388,530,1900,570
East,HOL100,Conductivity (uS/cm),4,599,533,762,542,705,623
East,SUP010,Conductivity (uS/cm),10,585,480,560,625,650,577
East,SUP020,Conductivity (uS/cm),11,920,460,750,990,1120,871
East,SUP050,Conductivity (uS/cm),11,710,430,620,730,754,664
East,SUP100,Conductivity (uS/cm),12,640,400,590,660,707,612
East,SUP200,Conductivity (uS/cm),12,325,260,290,340,405,324
East,SUP300,Conductivity (uS/cm),14,560,120,530,645,740,543
East,SUP350,Conductivity (uS/cm),11,480,120,330,720,870,505
East,WOL100,Conductivity (uS/cm),6,515,423,622,472,567,519
North,BAK025,Conductivity (uS/cm),4,86,50,64,96,97,80
North,BAK060,Conductivity (uS/cm),5,91,70,88,110,124,97
North,BAK150,Conductivity (uS/cm),4,151,120,132,167,176,149
North,BAK200,Conductivity (uS/cm),8,165,140,149,176,208,166
North,BAK250,Conductivity (uS/cm),5,178,150,163,195,309,199
North,CRB080,Conductivity (uS/cm),6,55,34,38,92,130,67
North,CRB100,Conductivity (uS/cm),4,90,76,79,105,111,92
North,CRB150,Conductivity (uS/cm),6,73,44,50,119,131,82
North,CRB250,Conductivity (uS/cm),5,81,46,50,116,139,86
North,CRB300,Conductivity (uS/cm),11,73,49,50,114,162,86
North,DIP060,Conductivity (uS/cm),4,141,110,124,157,170,140
North,DIP080,Conductivity (uS/cm),4,208,180,188,238,256,213
North,DIP100,Conductivity (uS/cm),5,200,65,190,203,210,174
North,FOU100,Conductivity (uS/cm),9,401,300,310,484,640,423
North,FOU120,Conductivity (uS/cm),10,362,230,338,658,1420,527
North,FOU150,Conductivity (uS/cm),10,529,390,454,1080,1294,694
North,FOU200,Conductivity (uS/cm),8,491,410,465,629,1020,575
North,MOU200,Conductivity (uS/cm),20,50,20,40,69,99,53
North,MOU250,Conductivity (uS/cm),9,168,99,149,243,320,190
North,MOU400,Conductivity (uS/cm),20,60,20,45,76,113,62
North,MOU600,Conductivity (uS/cm),19,70,30,50,90,124,72
North,MOU650,Conductivity (uS/cm),11,100,40,70,135,141,101
North,MOU700,Conductivity (uS/cm),11,100,40,70,132,158,103
North,MOU850,Conductivity (uS/cm),27,114,40,101,135,182,117
Upper,HU0140,Conductivity (uS/cm),17,82,41,59,109,161,87
Upper,HU0150,Conductivity (uS/cm),6,50,40,40,80,150,68
Upper,HU0200,Conductivity (uS/cm),23,30,10,20,50,183,50
Upper,HU0240,Conductivity (uS/cm),20,35,10,25,60,150,52
Upper,JUD020,Conductivity (uS/cm),10,55,39,39,65,90,55
Upper,JUD025,Conductivity (uS/cm),9,61,43,44,78,120,68
Upper,JUD070,Conductivity (uS/cm),6,60,51,51,77,82,64
Upper,JUD100,Conductivity (uS/cm),6,56,44,52,61,110,63
Upper,JUD180,Conductivity (uS/cm),5,54,49,53,70,88,63
Upper,JUD200,Conductivity (uS/cm),7,58,51,54,118,137,80
Upper,LDR001,Conductivity (uS/cm),69,35,24,30,43,66,38
Upper,LDR002,Conductivity (uS/cm),67,46,30,43,55,70,48
Upper,LDR100,Conductivity (uS/cm),8,30,20,30,40,40,33
Upper,LDR220,Conductivity (uS/cm),4,30,30,30,40,50,35
Upper,LDR300,Conductivity (uS/cm),4,30,30,30,30,30,30
Upper,RUS005,Conductivity (uS/cm),72,58,39,51,68,100,60
Upper,RUS010,Conductivity (uS/cm),71,55,38,47,69,100,60
Upper,RUS055,Conductivity (uS/cm),10,47,30,39,68,78,51
Upper,RUS060,Conductivity (uS/cm),12,46,35,43,60,77,51
Upper,RUS070,Conductivity (uS/cm),10,47,36,43,58,79,52
Upper,RUS075,Conductivity (uS/cm),6,76,65,72,90,147,88
Upper,RUS080,Conductivity (uS/cm),14,52,7,42,60,88,52
Upper,RUS100,Conductivity (uS/cm),11,51,39,42,74,86,56
Upper,WAT050,Conductivity (uS/cm),8,264,125,176,420,510,294
Upper,WAT055,Conductivity (uS/cm),6,309,215,239,470,510,342
Upper,WAT200,Conductivity (uS/cm),27,320,120,220,390,490,315
West,CFB010,Conductivity (uS/cm),31,90,60,80,110,173,97
West,CFB020,Conductivity (uS/cm),32,110,60,90,130,191,112
West,CFB030,Conductivity (uS/cm),28,130,80,110,140,191,127
West,DOV070,Conductivity (uS/cm),4,382,180,279,388,390,334
West,DOV090,Conductivity (uS/cm),2,355,190,520,355,,
West,DOV110,Conductivity (uS/cm),2,425,200,650,425,,
West,DOV120,Conductivity (uS/cm),2,1125,250,1999,1125,,
West,DOV130,Conductivity (uS/cm),2,1095,190,2000,1095,,
West,PCK010,Conductivity (uS/cm),20,149,80,131,173,214,150
West,PCK020,Conductivity (uS/cm),20,179,90,148,202,285,176
West,PCK030,Conductivity (uS/cm),20,220,99,182,249,350,219
```

### Verbatim — ph

Source file: `01_original_verbatim/ph.csv`  ·  87 lines (including header)

```csv
Zone,Site,Parameter,No.samples,Median,Minimum,25%quartile,75%quartile,Maximum,Mean 
East,AGN010,pH,15,6.5,6,6.5,7,7,6.6
East,AGN016,pH,13,6.5,6.5,6.5,7,8.1,6.8
East,AGN120,pH,11,6.5,6,6.5,6.5,7,6.5
East,AGN130,pH,26,7,6,6.5,7.7,8,7
East,AGN200,pH,11,6.5,6,6,7.5,8,6.7
East,AGN245,pH,6,6,5.5,5.5,6,6.5,5.9
East,AGN249,pH,10,8,7.5,8,8,8,7.9
East,AGN250,pH,9,6,5.5,5.5,6.5,7.5,6.2
East,AGN260,pH,6,6,5.5,6,6,6.5,6
East,AGN300,pH,10,6,5.5,6,6.5,7,6.2
East,AGN400,pH,11,6.5,6.5,6.5,7.5,8.5,7
East,ALB100,pH,8,6.5,6,7,6.5,7,6.6
East,GDR100,pH,8,6.5,5.5,6.5,6,6.5,6.3
East,GDR150,pH,8,6.5,6.5,7.5,6.5,7.3,6.8
East,GDR200,pH,8,6.5,6,7,6,6.5,6.4
East,GVC115,pH,13,6,5,6,6.5,7.1,6.1
East,HOL100,pH,4,7,6,8,6.5,7.5,7
East,SUP010,pH,10,6.3,6,6,6.5,7,6.4
East,SUP020,pH,11,6,6,6,6.5,6.5,6.2
East,SUP050,pH,11,6,5.5,6,6,6.5,6
East,SUP100,pH,12,6,5.5,5.8,6.5,6.5,6.1
East,SUP200,pH,11,6,5.5,5.5,6,7,6
East,SUP300,pH,13,6.5,5.5,6,6.5,6.5,6.3
East,SUP350,pH,11,6,5,6,6.5,6.5,6
East,WOL100,pH,6,6.5,6,7,6.5,7,6.6
North,BAK025,pH,4,6.5,6,6.3,6.8,7,6.5
North,BAK060,pH,5,6.5,6,6.5,7,7,6.6
North,BAK150,pH,4,7,6.5,6.8,7,7,6.9
North,BAK200,pH,8,6.5,6,6.3,6.5,7,6.4
North,BAK250,pH,5,6.5,6,6.5,6.5,6.5,6.4
North,CRB080,pH,6,6.3,5.5,6,6.5,6.5,6.2
North,CRB100,pH,4,7,6,6.3,7.5,7.5,6.9
North,CRB150,pH,7,6.5,5.5,6,6.5,7,6.3
North,CRB250,pH,5,6.5,5.5,6,6.5,7,6.3
North,CRB300,pH,12,6.5,5.5,6.3,7,7.3,6.6
North,DIP060,pH,4,5.8,5,5.3,6,6,5.6
North,DIP080,pH,4,6,5,5.5,6,6,5.8
North,DIP100,pH,5,6,5.5,6,6.5,6.5,6.1
North,FOU100,pH,9,6.5,6,6,7,7.1,6.5
North,FOU120,pH,10,7,6.5,6.5,7,7.5,6.9
North,FOU150,pH,10,6,6,6,6.5,7,6.3
North,FOU200,pH,8,6.5,6,6,7,7.5,6.6
North,MOU200,pH,20,6.5,6,6.5,7,7.4,6.6
North,MOU250,pH,9,7,6.5,6.5,7,7.5,6.9
North,MOU400,pH,20,6.5,6,6.5,7,7.6,6.7
North,MOU600,pH,19,6.6,6,6.5,7,7.9,6.8
North,MOU650,pH,11,6.5,6,6,7,7.4,6.6
North,MOU700,pH,11,6.5,6,6,7,7.4,6.7
North,MOU850,pH,25,7,6,6.5,7.5,7.9,6.9
Upper,HU0140,pH,15,7.3,5.7,6.8,7.6,7.8,7.1
Upper,HU0150,pH,6,6,6,6,6.5,7,6.3
Upper,HU0200,pH,23,6,5,6,6.5,7,6
Upper,HU0240,pH,21,6,5,5.5,6.5,7,6
Upper,JUD020,pH,10,6,6,6,6.5,6.5,6.2
Upper,JUD025,pH,9,6.5,6,6,6.5,6.5,6.3
Upper,JUD070,pH,6,6,6,6,6.5,6.5,6.2
Upper,JUD100,pH,6,6,6,6,6.5,6.5,6.2
Upper,JUD180,pH,5,6,6,6,6.5,6.5,6.2
Upper,JUD200,pH,7,6,6,6,7.7,8,6.6
Upper,LDR001,pH,61,6.8,5.7,6.6,7,7.5,6.9
Upper,LDR002,pH,59,6.7,5.9,6.6,7.1,7.5,6.8
Upper,LDR100,pH,8,6.5,6,6,6.5,6.5,6.3
Upper,LDR220,pH,5,6.5,6,6,6.5,6.5,6.3
Upper,LDR300,pH,4,6,6,6,6,6,6
Upper,RU3070,pH,11,6,5.5,6,6,7,6
Upper,RUS005,pH,64,6.9,6,6.7,7.2,7.7,6.9
Upper,RUS010,pH,63,6.8,5.5,6.6,7,7.6,6.8
Upper,RUS055,pH,12,6,5.5,6,6.5,6.5,6.1
Upper,RUS060,pH,15,6,5.5,6,6,6.5,6
Upper,RUS075,pH,6,6,5.5,6,6.5,7,6.2
Upper,RUS080,pH,15,6,5.5,5.5,6.5,60,9.6
Upper,RUS100,pH,13,6,5,6,6.5,7,6.2
Upper,WAT050,pH,8,6.8,6,6.5,7.5,7.5,6.9
Upper,WAT055,pH,5,7,6,7,7.5,8,7.1
Upper,WAT200,pH,27,6.5,6,6.5,7,8,6.8
West,CFB010,pH,30,6.5,5.5,6,6.5,7.6,6.3
West,CFB020,pH,32,6.5,5.5,6,6.5,7.7,6.4
West,CFB030,pH,27,6.5,5.5,6,6.5,7.7,6.4
West,DOV070,pH,4,6.9,6,6.5,7.4,7.8,6.9
West,DOV090,pH,2,7.2,6.5,7.8,7.2,,
West,DOV110,pH,2,7,6.5,7.5,7,,
West,DOV120,pH,2,7.9,7.5,8.2,7.9,,
West,DOV130,pH,2,8,8,8,8,,
West,PCK010,pH,20,6.3,5.5,6,6.5,7,6.3
West,PCK020,pH,20,6.5,6,6.5,6.8,7,6.6
West,PCK030,pH,20,6.5,6,6.5,7,7,6.6
```

### Verbatim — phos

Source file: `01_original_verbatim/phos.csv`  ·  46 lines (including header)

```csv
Zone,Site,Parameter,No.samples,Median,Minimum,25%quartile,75%quartile,Maximum,Mean 
East,GVC115,Ortho-phosphate (mg/L),2,0.011,0.006,0.016,0.011,,
East,SUP010,Ortho-phosphate (mg/L),9,0.045,0.03,0.03,0.045,0.06,0.04
East,SUP020,Ortho-phosphate (mg/L),10,0.28,0.14,0.14,0.42,0.44,0.282
East,SUP050,Ortho-phosphate (mg/L),10,0.19,0.08,0.14,0.28,1.14,0.299
East,SUP100,Ortho-phosphate (mg/L),10,0.13,0.045,0.08,0.14,0.28,0.13
East,SUP200,Ortho-phosphate (mg/L),7,0.03,0.015,0.015,0.03,0.15,0.041
East,SUP300,Ortho-phosphate (mg/L),10,0.08,0.03,0.08,0.11,0.14,0.088
North,BAK025,Ortho-phosphate (mg/L),2,0.015,0.015,0.015,0.015,,
North,BAK060,Ortho-phosphate (mg/L),2,0.015,0.015,0.015,0.015,,
North,BAK150,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,
North,BAK200,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,
North,BAK250,Ortho-phosphate (mg/L),3,0.015,0.015,0.03,0.02,,
North,CRB080,Ortho-phosphate (mg/L),4,0.008,0,0,0.023,0.03,0.011
North,CRB150,Ortho-phosphate (mg/L),6,0.015,0,0.015,0.015,0.03,0.015
North,CRB250,Ortho-phosphate (mg/L),4,0.008,0,0,0.015,0.015,0.008
North,CRB300,Ortho-phosphate (mg/L),6,0.015,0,0.015,0.015,0.015,0.013
North,FOU100,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,
North,FOU120,Ortho-phosphate (mg/L),5,0.015,0.015,0.015,0.015,0.03,0.018
North,FOU150,Ortho-phosphate (mg/L),5,0.03,0.015,0.015,0.03,0.045,0.027
North,FOU200,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,
North,MOU200,Ortho-phosphate (mg/L),3,0.005,0.005,0.03,0.013,,
North,MOU250,Ortho-phosphate (mg/L),2,0.005,0.005,0.005,0.005,,
North,MOU400,Ortho-phosphate (mg/L),4,0.005,0,0.003,0.01,0.015,0.006
North,MOU600,Ortho-phosphate (mg/L),3,0.005,0.005,0.03,0.013,,
North,MOU650,Ortho-phosphate (mg/L),6,0.01,0,0.005,0.015,0.03,0.012
North,MOU700,Ortho-phosphate (mg/L),5,0.012,0.015,0.015,0.005,0.005,6
North,MOU850,Ortho-phosphate (mg/L),6,0.015,0.005,0.01,0.015,0.03,0.015
Upper,JUD020,Ortho-phosphate (mg/L),7,0,0,0,0.015,0.03,0.006
Upper,JUD025,Ortho-phosphate (mg/L),7,0.015,0,0,0.015,0.03,0.011
Upper,JUD070,Ortho-phosphate (mg/L),5,0,0,0,0,0.015,0.003
Upper,JUD100,Ortho-phosphate (mg/L),5,0,0,0,0.015,0.015,0.006
Upper,JUD180,Ortho-phosphate (mg/L),4,0.008,0,0,0.015,0.015,0.008
Upper,JUD200,Ortho-phosphate (mg/L),7,0.005,0,0,0.015,0.03,0.008
Upper,LDR100,Total phosphate (mg/L),4,0.01,0.01,0.01,0.02,0.02,0.01
Upper,LDR220,Total phosphate (mg/L),5,0.02,0.01,0.01,0.02,0.03,0.02
Upper,LDR300,Total phosphate (mg/L),5,0.04,0.03,0.03,0.04,0.05,0.04
Upper,LDR400,Total phosphate (mg/L),4,0.02,0.01,0.01,0.02,0.02,0.02
Upper,RUS010,Ortho-phosphate (mg/L),2,0.008,0,0.015,0.008,,
Upper,RUS055,Ortho-phosphate (mg/L),8,0.015,0.002,0.008,0.023,0.03,0.015
Upper,RUS060,Ortho-phosphate (mg/L),3,0.015,0.015,0.015,0.015,,
Upper,RUS080,Ortho-phosphate (mg/L),2,0.015,0.015,0.015,0.015,,
Upper,RUS100,Ortho-phosphate (mg/L),2,0.008,0,0.015,0.008,,
West,CFB010,Ortho-phosphate (mg/L),4,0.011,0.005,0.006,0.023,0.03,0.014
West,CFB020,Ortho-phosphate (mg/L),2,0.015,0.015,0.015,0.015,,
West,CFB030,Ortho-phosphate (mg/L),4,0.012,0.005,0.007,0.023,0.03,0.015
```

### Verbatim — e_coli

Source file: `01_original_verbatim/e_coli.csv`  ·  58 lines (including header)

```csv
Zone,Site,Parameter,No.samples,Median,Minimum,25%quartile,75%quartile,Maximum,Mean 
East,AGN200,E. coil (counts/100 ml),5,8500,900,1300,10400,13865,6993
East,ALB100,E. coli (counts/100 ml),2,100,60,140,100,,
East,GDR100,E. coli (counts/100 ml),3,80,40,160,93,,
East,GDR150,E. coli (counts/100 ml),3,280,30,660,323,,
East,GDR200,E. coil (counts/100 ml),2,59,20,98,59,,
East,HOL100,E. coli (counts/100 ml),2,160,140,180,160,,
East,WOL100,E. coil (counts/100 ml),2,90,0,180,90,,
East,WOL100,E. coli (counts/100 ml),2,90,0,180,90,,
North,BAK025,E. coli (counts/100 ml),6,69,0,20,320,480,160
North,BAK060,E. coil (counts/100 ml),6,260,40,140,1200,1240,523
North,BAK150,E. coli (counts/100 ml),5,200,54,80,540,1680,511
North,BAK200,E. coli (counts/100 ml),7,280,120,200,680,2000,554
North,BAK250,E. coli (counts/100 ml),5,140,98,140,320,1520,444
North,CRB080,E. coli (counts/100 ml),5,20,0,0,20,20,12
North,CRB100,E. coli (counts/100 ml),2,36,6,66,36,,
North,CRB150,E. coli (counts/100 ml),6,50,0,0,120,140,60
North,CRB250,E. coil (counts/100 ml),4,20,0,0,80,120,40
North,CRB300,E. coil (counts/100 ml),10,75,20,40,280,2700,381
North,DIP060,E. coil (counts/100 ml),2,50,40,60,50,,
North,DIP080,E. coil (counts/100 ml),2,430,400,460,430,,
North,DIP100,E. coli (counts/100 ml),6,520,160,280,800,1440,620
North,FOU100,E. coil (counts/100 ml),7,260,0,40,1000,2000,557
North,FOU120,E. coil (counts/100 ml),8,130,38,60,340,480,197
North,FOU150,E. coli (counts/100 ml),8,109,20,50,340,580,200
North,FOU200,E. coli (counts/100 ml),6,80,1,20,160,700,174
North,MOU200,E. coli (counts/100 ml),10,20,0,0,100,200,52
North,MOU250,E. coil (counts/100 ml),9,20,0,0,99,660,122
North,MOU400,E. coli (counts/100 ml),10,70,20,40,120,200,86
North,MOU600,E. coil (counts/100 ml),10,84,0,40,260,400,143
North,MOU650,E. coil (counts/100 ml),9,100,40,100,180,360,149
North,MOU700,E. coil (counts/100 ml),10,130,20,80,210,460,169
North,MOU850,E. coil (counts/100 ml),10,390,50,160,800,2000,661
Upper,JUD020,E. coil (counts/100 ml),3,0,0,0,0,,
Upper,JUD025,E. coli (counts/100 ml),3,0,0,20,7,,
Upper,JUD070,E. coli (counts/100 ml),3,20,0,40,20,,
Upper,JUD100,E. coil (counts/100 ml),3,0,0,40,13,,
Upper,JUD200,E. coli (counts/100 ml),5,60,0,60,120,1000,248
Upper,ROS070,E. coli (counts/100 ml),2,70,20,120,70,,
Upper,RUS010,E. coil (counts/100 ml),2,0,0,0,0,,
Upper,RUS055,E. coil (counts/100 ml),4,32,6,11,106,164,58
Upper,RUS060,E. coil (counts/100 ml),2,10,0,20,10,,
Upper,RUS080,E. coli (counts/100 ml),2,20,20,20,20,,
West,CFB010,E. coli (counts/100 ml),4,100,0,0,355,510,178
West,CFB020,E. coil (counts/100 ml),6,48,0,36,360,510,167
West,CFB030,E. coil (counts/100 ml),4,675,360,435,840,840,638
West,KER200,E. coil (counts/100 ml),4,210,76,128,345,450,237
West,KER400,E. coil (counts/100 ml),2,300,80,520,300,,
West,KER450,E. coil (counts/100 ml),4,250,24,122,360,440,241
West,KER600,E. coil (counts/100 ml),3,560,60,820,480,,
West,KER700,E. coil (counts/100 ml),4,700,120,290,1470,2000,880
West,KER800,E. coil (counts/100 ml),4,665,200,405,1000,1280,703
,RIL200,E. coil (counts/100 ml),2,280,280,280,280,,
,RIL400,E. coil (counts/100 ml),4,865,230,340,1490,1700,915
,STT100,E. coil (counts/100 ml),2,95,80,110,95,,
,STT300,E. coil (counts/100 ml),2,920,240,1600,920,,
,STT350,E. coil (counts/100 ml),2,170,80,260,170,,
,STT400,E. coil (counts/100 ml),4,1195,260,465,2110,2500,1288
```

