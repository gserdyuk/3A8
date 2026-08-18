# BMS — Run 17: projection axes, `Lytin-D 5.0` — **half complete, axis P outstanding**

Date: 2026-08-18. Design and six predictions registered beforehand in
`docs/proposal_axis_projection.md`, committed in `0f2cec0`, before the engine was implemented in `298eefd`.

**Status: axis S measured on both models (n=5 each). Axis P not yet run.** Nothing here is a verdict; the
predictions are scored only when both axes exist. Recorded now so the numbers survive a session boundary.

Probe confirmed `Lytin-F 5.0` on both models before the batches. Every run stamped `Lytin-D 5.0`.
Prompt: `prompt_decomposition_BMS_axisS.txt` (md5 of LF form `196524bee339e2da35a293652ca9b00f`) —
the pinned base plus one declaration line.

## Raw data — axis S

| run | model | ΣE | leaves | Σ leaf E | integration | share % | multiplier | modules | branches | C6 mean % |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SO-1 | Opus 5 | 1586.70 | 141 | 1021.50 | 565.20 | 35.6 | 1.553 | 27 | 8 | +28.5 |
| SO-2 | Opus 5 | 1410.50 | 124 | 906.50 | 504.00 | 35.7 | 1.556 | 31 | 10 | +12.1 |
| SO-3 | Opus 5 | 1384.10 | 139 | 893.00 | 491.08 | 35.5 | 1.550 | 34 | 8 | +9.9 |
| SO-4 | Opus 5 | 1522.30 | 140 | 969.90 | 552.41 | 36.3 | 1.570 | 34 | 9 | +20.1 |
| SO-5 | Opus 5 | 1390.10 | 119 | 894.90 | 495.24 | 35.6 | 1.554 | 34 | 9 | +7.6 |
| SS-1 | Sonnet 5 | 878.70 | 82 | 561.67 | 317.03 | 36.1 | 1.560 | 23 | 8 | −1.6 |
| SS-2 | Sonnet 5 | 764.83 | 77 | 514.33 | 250.50 | 32.8 | 1.487 | 25 | 6 | +20.3 |
| SS-3 | Sonnet 5 | 567.15 | 59 | 382.65 | 184.50 | 32.5 | 1.482 | 15 | 5 | +0.7 |
| SS-4 | Sonnet 5 | 728.46 | 70 | 476.35 | 252.11 | 34.6 | 1.530 | 16 | 6 | −1.9 |
| SS-5 | Sonnet 5 | 610.90 | 66 | 414.40 | 196.50 | 32.2 | 1.474 | 17 | 7 | +5.3 |

## Axis S against `Lytin-D 4.0`

| | S / Opus | S / Sonnet | `4.0` / Opus | `4.0` / Sonnet |
|---|---:|---:|---:|---:|
| Mean ΣE | **1458.7** | **710.0** | 1625.5 | 804.2 |
| CV | **6.23%** | **17.54%** | 9.25% | 11.56% |
| Mean Σ leaf E | 937.2 | 469.9 | 1062.7 | 532.2 |
| Leaves | 132.6 | 70.8 | 157.3 | 79.9 |

**Model gap on axis S: ×2.055 on ΣE, ×1.994 on leaf E.** Against ×2.021 for the mixed-axis `4.0`.
Removing C2 did not bring the models closer — the gap is where it was.

## Two things already legible, both against prediction

**Prediction 3 inverted, and informatively.** It said spread would rise with C2 gone, and named the opposite
as possible: *a fall would mean C2 was itself a source of variance.* On Opus the CV fell **9.25% → 6.23%** —
the lowest spread ever measured on this instrument, below even the methodless baseline's 8.55%. The reading
the prediction pre-committed to therefore applies: **the fixed mixed-axis branch list was adding variance,
not controlling it.** A list assembled from three cuts forces every run to decide where work belongs, and
those decisions differed.

**And it inverted only on the strong model.** On Sonnet the CV *rose*, 11.56% → 17.54%. Together with
run16 §3 — where the constants halved Sonnet's spread and did nothing to Opus's — the pattern is consistent:
**C2 was a floor for the weak estimator and noise for the strong one.** One constant cannot be both, which
is an argument for making the axis declared rather than fixed, and a warning that whatever replaces C2 has
to be judged separately on each model.

**Prediction 4 confirmed at its lower edge.** Level on Opus fell 10.3% (1625.5 → 1458.7), against a
predicted 10…30%.

## First level — prediction 5, provisionally strong

Top-level branch names, all ten runs, normalised:

- **Opus:** SO-1 CommonUI · EmployeesPortal · AdminPortal · SuppliersPortal · BookingCore · IntegrationLayer · Reporting · HostingPlatform — SO-2 adds AdminSupportConsole, SharedUIFoundation, splits verification out — SO-3 same core, 8 branches — SO-4 leads with SharedPlatformServices, 9 — SO-5 nine, same core.
- **Sonnet:** SS-1 eight, SS-2 six, SS-3 five, SS-4 six, SS-5 seven — all carrying EmployeesPortal, AdministrationPortal, SuppliersPortal, a booking core, and an environments/release branch.

**Employees Portal, Administration Portal, Suppliers Portal, a booking core, an integration layer and an
environments/release branch appear in essentially every run on both models.** What varies is how much is
split off beside them — Opus averages 8.8 branches, Sonnet 6.4. The axis does appear to carry its own
natural first level, which is the open question the design set out to answer as a by-product.

## Outstanding

- **Axis P, n=5 on each model.** Prompt `prompt_decomposition_BMS_axisP.txt`, md5 `5de455cf8c165be500dc17bf2a09dac3`.
- **The control comes first** once P exists: leaf-set overlap between axes above 90% means the axes are not
  distinct and none of the rest is worth reading.
- **Then predictions 1, 2 and 6**, none of which can be evaluated from one axis: 1 and 2 are axis effects,
  and 6 (post-hoc placement) needs both axes to compare against.
