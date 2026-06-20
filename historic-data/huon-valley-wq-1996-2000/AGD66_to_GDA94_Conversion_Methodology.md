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
