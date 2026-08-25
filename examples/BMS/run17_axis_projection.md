# BMS — Run 17: projection axes, `Lytin-D 5.0` — **closed; the axis comparison is discontinued**

Date: 2026-08-18 (axis S, first batch) / 2026-08-19 (axis P, axis S rerun, Haiku, closure).
Design and six predictions registered beforehand in `docs/proposal_axis_projection.md`, committed in
`0f2cec0`, before the engine was implemented in `298eefd`.

**Status: closed.** Axis S and axis P were both measured on two models, n=5 each. A third capability
tier (Haiku 4.5) was attempted. **The axis comparison itself — the gating control and predictions 1,
2 and the cross-axis half of 5 — was discontinued before the control was computed**, for reasons given
in §7. Those predictions are recorded as *not evaluated*, not as confirmed or refuted.

The batches produced several results the design did not anticipate, and those are the substance of
this run. They are in §4–§6.

Probe confirmed `Lytin-F 5.0` on Opus, Sonnet and Haiku before their batches. Every non-Haiku run
stamped `Lytin-D 5.0`.

Prompts, md5 of the LF form, all verified at launch:
`prompt_decomposition_BMS_axisS.txt` = `196524bee339e2da35a293652ca9b00f`,
`prompt_decomposition_BMS_axisP.txt` = `5de455cf8c165be500dc17bf2a09dac3`.

---

## 1. Raw data — axis S, first batch (2026-08-18)

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

**Leaf tables for these ten runs were not preserved** — see §8. That loss is what forced the rerun
in §3, and it is itself one of this run's findings.

## 2. Raw data — axis P (2026-08-19)

| run | model | ΣE | leaves | Σ leaf E | integration | share % | multiplier | modules | branches | C6 checks / outside / mean % |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| PO-1 | Opus 5 | 1699.90 | 154 | 1121.00 | 578.90 | 34.1 | 1.516 | 16 | 6 | 21 / 11 / +10.1 |
| PO-2 | Opus 5 | 1305.11 | 126 | 860.01 | 445.10 | 34.1 | 1.518 | 14 | 6 | 19 / 14 / +25.2 |
| PO-3 | Opus 5 | 1490.40 | 129 | 979.00 | 511.37 | 34.3 | 1.522 | 15 | 6 | 20 / 17 / +19.2 |
| PO-4 | Opus 5 | 1347.24 | 133 | 884.68 | 462.56 | 34.3 | 1.523 | 18 | 6 | 23 / 18 / +18.4 |
| PO-5 | Opus 5 | 1558.06 | 153 | 1036.06 | 522.00 | 33.5 | 1.504 | 17 | 6 | 22 / 12 / +15.6 |
| PS-1 | Sonnet 5 | 594.53 | 66 | 395.83 | 198.70 | 33.4 | 1.502 | 14 | 4 | 15 / 3 / +6.4 |
| PS-2 | Sonnet 5 | 651.80 | 61 | 434.20 | 217.70 | 33.4 | 1.500 | 12 | 6 | 13 / 11 / +23.3 |
| PS-3 | Sonnet 5 | 791.25 | 68 | 526.23 | 265.02 | 33.5 | 1.500 | 14 | 6 | 16 / 8 / +7.0 |
| PS-4 | Sonnet 5 | 787.80 | 88 | 525.56 | 262.24 | 33.3 | 1.500 | 12 | 5 | 15 / 8 / **−9.1** |
| PS-5 | Sonnet 5 | 781.30 | 72 | 525.35 | 255.98 | 32.8 | 1.487 | 15 | 6 | 15 / 13 / +16.9 |

Full leaf inventories preserved (see §8 on where).

## 3. Raw data — axis S rerun for structure (2026-08-19)

Run to recover the leaf-level data missing from §1. **These are different runs from SO-1…5 / SS-1…5;
their levels must not be substituted for the §1 numbers.** Registered as such before results were read.

| run | model | ΣE | leaves | Σ leaf E | integration | share % | multiplier | modules | branches | C6 checks / outside / mean % | gates |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| RO-1 | Opus 5 | 1444.88 | 124 | 938.99 | 505.88 | 35.0 | 1.539 | 26 | 8 | 33 / 7 / +3.9 | pass |
| RO-2 | Opus 5 | 1221.30 | 115 | 792.10 | 429.20 | 35.1 | 1.542 | 27 | 8 | 28 / 8 / +1.8 | pass |
| RO-3 | Opus 5 | 1326.03 | 123 | 850.60 | 475.43 | 35.9 | 1.559 | 37 | 9 | 41 / 5 / +5.2 | pass |
| RO-4 | Opus 5 | 1349.60 | 108 | 861.60 | 488.00 | 36.2 | 1.566 | 28 | 10 | 29 / 15 / +9.0 | pass |
| RO-5 | Opus 5 | 1486.07 | 133 | 946.00 | 540.07 | 36.3 | 1.571 | 39 | 10 | 39 / 26 / +20.5 | pass |
| RS-1 | Sonnet 5 | 422.58 | 45 | 287.20 | 135.38 | 32.0 | 1.471 | 24 | 6 | 11 / 9 / +26.0 | pass |
| RS-2 | Sonnet 5 | 600.02 | 71 | 388.97 | 211.04 | 35.2 | 1.543 | 16 | 6 | 19 / 12 / +13.1 | pass |
| RS-3 | Sonnet 5 | 746.80 | 84 | 483.04 | 263.76 | 35.3 | 1.546 | 16 | 5 | 21 / 9 / **−7.5** | pass |
| RS-4 | Sonnet 5 | 649.40 | 63 | 442.20 | 207.20 | 31.9 | 1.470 | 29 | 5 | 17 / 3 / +1.9 | **note** |
| RS-5 | Sonnet 5 | 461.40 | 41 | 309.65 | 151.77 | 32.9 | 1.490 | 19 | 5 | 7 / 3 / +10.1 | **violation** |

### Batch means

| | axis S §1 | axis S rerun | axis P |
|---|---:|---:|---:|
| **Opus** ΣE | 1458.7 (CV 6.23%) | 1365.6 (CV 7.63%) | 1480.1 (CV 10.83%) |
| **Sonnet** ΣE | 710.0 (CV 17.54%) | 576.0 (CV **23.26%**) | 721.3 (CV 12.75%) |

Opus reproduced within spread (−6.4%). **Sonnet came in 18.9% lower with a wider spread**, and that is
not explained. Two of the five Sonnet rerun trees carry structural defects (§6), and both are among
the three lowest levels — a plausible but unproven mechanism.

---

## 4. What the batches established

### 4a. The leaf is a unit of generation, not a fraction of a whole

Moving from Sonnet to Opus, leaf **count** rises ×1.87…×1.97 while leaf **size** does not move:

| instrument | Opus pd/leaf | Sonnet pd/leaf | size ratio | count ratio |
|---|---:|---:|---:|---:|
| `4.0` mixed axis | 6.756 | 6.661 | 1.014 | 1.969 |
| `5.0` axis S §1 | 7.068 | 6.637 | 1.065 | 1.873 |
| `5.0` axis P | 7.023 | 6.781 | 1.036 | 1.958 |

Partitioning a fixed quantity into twice as many pieces would halve the piece. It does not. The models
are not cutting one pie into different numbers of slices — **they produce slices of a characteristic
size and stop at different points.** C1 fixes the size and leaves the count free; the total is their
product, so the constrained factor is not the one that carries the variance. This is the same
unpinned parameter run16 identified, now seen directly.

Consistent with it: C6 is systematically positive (Opus axis P mean +17.7%, axis S rerun +8.1%,
with individual runs up to +20.5% and 26 of 39 rows outside ±10%). Splitting does not conserve the
sum; it produces it.

### 4b. Σ E ≈ 10.4 × leaf count, with an honest band of ±9%

Across eight batches, two models and four instruments:

`10.33 · 10.07 · 11.00 · 10.03 · 10.65 · 10.16 · 11.32 · 9.47` → **mean 10.38, range 9.47–11.32, ±8.9%**

Everything else in the method — PERT on O/M/P, C3 at 20%, C6, the C5 module derivation — either
cancels or is a deterministic transform of this. The output of the instrument is (number of pieces
named) × (a constant near 10.4 pd).

**Correction on the record:** after six batches this was reported in-session as ±5%. The seventh and
eighth batches widened it to ±8.9%. The mean barely moved; the claimed precision was too tight.

### 4c. The model gap is large and reframing does not move it — but it is not a publishable constant

| instrument | Opus ÷ Sonnet |
|---|---:|
| no method (run14/15) | 1.409 |
| `4.0`, ten fixed mixed-axis branches | 2.021 |
| `5.0`, axis S §1 | 2.055 |
| `5.0`, axis P | 2.052 |
| `5.0`, axis S rerun | 2.371 |

Adding constants, removing C2 and changing the axis all leave the gap where it is, at roughly ×2.
The rerun's ×2.371 is **not a significant departure** (1.2 standard errors, n=5 each).

**Correction on the record.** After the first three of these, the inverse ratio was reported
in-session as `0.4896 ± 0.9%` and offered as a conversion coefficient stable enough to publish as
part of the engine spec. That was wrong in method: 0.9% was the scatter of three point estimates,
each of which carries its own standard error of 3–10%. Four batches give **0.4727 ± 7.2%**. The gap
is a real and stable *order of magnitude*; it is not measured to anything like the precision claimed,
and the proposal to publish it as a coefficient is withdrawn pending a proper error budget.

### 4d. The engine has a capability floor, and Haiku 4.5 is below it

Five runs, axis P, same prompt, same engine:

| run | ΣE | multiplier | what broke |
|---|---:|---:|---|
| HA-1 | 1373.59 | 1.533 | **C1**: 8 leaves above the ceiling, up to M=30 |
| HA-2 | 329.52 | 1.314 | **C3**: top-level assembly node dropped from the sum |
| HA-3 | 741.40 | 1.400 | **C3**: entire module layer of integration dropped; **C1**: 5 leaves above ceiling |
| HA-4 | 447.89 | 1.271 | **C1** + **C3**, and the instrument-readings block reports compliance falsely |
| HA-5 | 577.28 | 1.526 | clean |

**One of five executed the protocol.** CV **59.0%**, range ×4.17, against 10.8% (Opus) and 12.8%
(Sonnet) on the same axis. The multiplier is arithmetic under C3 and must land near 1.50; three runs
did not reproduce it.

Because C1 was not applied, the Haiku leaf counts are not leaf counts in the sense the other batches
use, so the §4b constant cannot be tested at this tier. Recorded as a property of the engine.

HA-4 is the worst case for a measurement pipeline: it printed `>10 pd: 0 (none — C1 ceiling enforced)`
above its own table containing seven leaves with M between 12 and 22, and declared its 1.271
multiplier arithmetically consistent. **A sensor can report compliance it did not achieve.**

### 4e. Three mechanical gates on the readings block

Derived from 4d and 6. All are arithmetic on the run's own output; no model is needed.

1. **Multiplier.** Recompute ΣE ÷ Σ leaf E and check it against the tree shape. Catches HA-2, HA-3, HA-4.
2. **Ceiling bucket.** Compare the reported M-distribution against the leaf table. Catches HA-1, HA-3, HA-4.
3. **Every leaf has a branch parent.** Added after RS-4 (§6). Neither of the first two catches it.

Gates 1 and 2 together catch all four broken Haiku runs and pass the clean one. **None of the three
catches an axis violation** (§6, RS-5) — that remains unguarded.

---

## 5. Predictions

Registered in `docs/proposal_axis_projection.md` before implementation.

| # | Prediction | Outcome |
|---|---|---|
| 1 | Axis effect on ΣE below ×1.4 | **NOT EVALUATED** — gating control discontinued, §7 |
| 2 | Σ leaf E converges better than ΣE; leaf ratio below ×1.25 | **NOT EVALUATED** — same |
| 3 | Spread rises with C2 gone; Opus CV 9.25% → 12…20% | **REFUTED for Opus, CONFIRMED for Sonnet** |
| 4 | Level falls 10…30% on Opus | **CONFIRMED**, at the lower half of the band |
| 5 | Top level stable within an axis, different between axes | **within-axis: CONFIRMED with one violation. cross-axis: NOT EVALUATED** |
| 6 | Testing placed ≥4 of 5; transition in fewer than 3 of 5 | **CONFIRMED** |

**Prediction 3.** Opus CV came out 6.23% (axis S §1), 10.83% (axis P), 7.63% (axis S rerun) against a
9.25% baseline — no consistent rise, and never inside the predicted 12–20% band. Sonnet rose in all
three: 11.56% → 17.54%, 12.75%, 23.26%. The reading the prediction pre-committed to therefore applies
only to the strong model, where the fixed mixed-axis branch list **was adding variance rather than
controlling it** on two of three batches. The clean statement is the one already in the earlier
version of this file and it survives: **C2 was a floor for the weak estimator and noise for the
strong one.** One constant cannot be both.

**Prediction 4.** Opus level against `4.0`'s 1625.5: −10.3% (axis S §1), −8.9% (axis P), −16.0%
(axis S rerun); mean of the three batches −13.8%. Inside the 10…30% band, at its lower half.

**Prediction 5, within-axis.** Both axes carry their own stable top level. Axis P produced a lifecycle
top level in 10 of 10 runs, with Requirements / Design / Implementation / Verification / Environments
/ Launch recurring; Opus gave exactly six branches in all five runs (sd 0.00), Sonnet 4–6 (sd 0.89).
Axis S produced Employees Portal, Administration Portal, Suppliers Portal, a booking core and a
platform/hosting branch in essentially every run on both models. **The one violation is RS-5** (§6),
which produced a lifecycle top level under the subsystem prompt.

**Prediction 6.** Scoring rule, fixed before the placement data was read across batches but **after
collection** — a weaker guarantee than pre-registration, and flagged as such: *transition off the
manual process* means work that moves the client's people and suppliers off the manual channel —
parallel run, decommissioning, change management, migration of in-flight or historical bookings.
Technical go-live cutover and initial reference-data seeding are **not** transition; they would exist
with no predecessor process at all.

- **Testing: placed in 20 of 20 runs**, both axes, both models. Confirmed with no exception.
- **Transition:** Opus axis P 3 of 5 · Sonnet axis P **0 of 5** · Opus axis S rerun 0 of 5 ·
  Sonnet axis S rerun **0 of 5**. Below the "fewer than 3 of 5" threshold on three batches of four,
  and exactly at it on the fourth. Confirmed.

The uncomfortable prediction was right, and more strongly than expected: with the branch slot removed,
the work of moving an organisation off a manual process is simply not generated. Sonnet never produced
it at all — 0 of 10 across both axes.

---

## 6. Structural violations found in the axis S rerun

**RS-4 — leaves with no branch parent.** Thirteen activity leaves hang directly off the root, bypassing
the branch layer, so they carry only the top-level C3 item (×1.2) rather than branch + top (×1.4). The
arithmetic self-reconciles and the multiplier 1.470 is internally consistent; gates 1 and 2 pass. Axis
S declares branches as the top level, so a leaf with no branch parent sits outside the declared
partition. **This produced gate 3.**

**RS-5 — the declared axis was not applied.** Its top level is Requirements · Design · Development ·
Testing · Deployment · Documentation — a **lifecycle cut, produced under the subsystem-axis prompt**.
The subsystem structure appears only inside the Development branch. The multiplier reconciles (1.490),
no leaf exceeds the ceiling, and all three gates pass.

This is the more serious of the two. The axis is an input the instrument does not reliably apply, and
nothing in the readings block reveals when it has not been. One violation in five axis-S runs; the
ten axis-P runs and the five §1 axis-S runs whose branch names are recorded show none. It is also the
proximate reason the axis comparison was discontinued (§7).

---

## 7. Why the axis comparison was discontinued

The control — leaf-set overlap between axes, above 90% meaning the axes are not distinct — was
specified in the proposal and gates predictions 1, 2 and the cross-axis half of 5. The measurement
procedure was pinned in writing before any overlap was computed: project each tree's leaves onto the
fixed RFP requirement list and compare the induced partitions of that list.

It was then discontinued, before computation, on four grounds:

1. **What the control was to establish is available more directly.** Its purpose was to show whether
   an axis-independent structure of the product exists. It does, and it is legible by eye from the
   trees already collected: the modules inside axis P's Implementation branch — Employees Portal,
   Administration Portal, Suppliers Portal, booking core, common UI, reporting, integration layer,
   search, identity, notifications, configuration and rules, transport combining, support tooling —
   are the same set that axis S puts one level higher. Comparing two name sets needs no metric, no
   90% threshold named before the metric existed, and no requirement-mapping judgement that would
   itself be a new uncontrolled sensor.
2. **The axis is not a controllable factor.** RS-5 produced the wrong axis under an explicit
   declaration. Comparing along a dimension the instrument does not reliably set measures the rig.
3. **The mechanism never fired.** Both axes agree closely on level. A coherence check that always
   passes carries no information, and the reason it passes is now understood: both axes find the same
   structure and differ only in where they hang it.
4. **Nothing else in this run depended on it.** §4a–§4e all came from the batches without the axis
   comparison.

**Consequence, stated plainly.** The axis effect of ×1.015 on ΣE (Opus) and ×1.016 (Sonnet), computed
from §1 against §2, is **provisional and must not be cited as a result.** Its gating control was never
run. It appears nowhere in §4 for that reason. Predictions 1 and 2 stand unevaluated.

**What survives of the idea.** The coherence principle — that disagreement between projections proves
an error without knowledge of the truth — is not discarded with its implementation. Under the
product-model-then-WBS design now being drafted, projecting one model onto two axes is a *rendering*
of an existing requirement mapping, not a second independent construction. Coverage under both views
becomes arithmetic on the mapping, and a mismatch is a demonstrated error, as the proposal intended —
without twenty runs.

---

## 8. The run-log format lost what later checks consume

The ten axis-S runs of §1 were recorded as instrument readings. Their **leaf tables were not kept**,
and the control specified in the same proposal consumes exactly those. The information was not
unknowable: the control was written down before the runs happened. The log recorded the derived
statistics and discarded the sample.

A statistic is always recomputable from the sample; a sample is never recoverable from a statistic.
The §1 table is derivable from those trees; the trees are not derivable from the table.

**Adopted for future runs:** keep the raw sensor output verbatim alongside the analysis.

- `examples/BMS/runNN_<name>.md` — the readable analysis, as now
- `examples/BMS/runNN_raw/` — verbatim output, one file per run
- a manifest in the same directory: prompt md5, model per run, engine stamp as printed, launch order

Note also that the harness does not persist subagent output: the per-task `.output` files were empty
(16 KB across 29 files). Transcription into the repository is the only durable path.

Applied to this run: the axis-P and axis-S-rerun leaf inventories, the readings tables, the Haiku
violation log and both pre-registrations are in **`examples/BMS/run17_raw/`**, with a manifest
recording prompt md5s, models, engine stamps and the known gaps. The ten axis-S runs of §1 remain
without leaf inventories — unrecoverable, and the reason the directory exists.

---

## 9. Corrections made in the course of this run

Recorded because the project's discipline is that a claim and its withdrawal both go on the record.

1. **`10.37 pd/leaf ± 5%` → `10.38 ± 8.9%`** (§4b). The mean held; the precision did not.
2. **`Sonnet ÷ Opus = 0.4896 ± 0.9%`, offered as a publishable coefficient → `0.4727 ± 7.2%`,
   proposal withdrawn** (§4c). The error was treating the scatter of three means as if the means
   themselves were exact.
3. **"The run-log format loses what later checks need" → it was a specific, avoidable omission**
   (§8), not an inherent property of the format. The control was already specified when the log was
   written.
4. **"A third capability tier tests whether the leaf count saturates" → it does not** (§4d). Saturation
   means increments shrink as capability *rises*, which needs a point above Opus. Haiku extends the
   sequence downward only. Corrected in writing before the Haiku results were read.
5. **The axis effect ×1.015 was reported in-session as an established headline** before its gating
   control had run (§7). It is provisional and is withdrawn from the results.

---

## 10. Outstanding

- Fable 5 as a fourth capability tier: parked. It would add a point to a question that the
  product-model design may dissolve.
- `findings.md` has not been updated with §4a–§4e.
- The proposal for the successor design — closure of a node's children against the parent's declared
  content, anchored at the root in the requirement list, with the axis demoted to a view — is not yet
  written.
