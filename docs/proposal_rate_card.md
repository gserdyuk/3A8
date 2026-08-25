# Proposal — the rate card: `Hotyn-D 2.0` prices from a pinned table, and no engine produces a number

Status: **design, nothing implemented.** Written 2026-08-21, following
`docs/review_2026-08-21_running_in_circles.md` (§6–§7.2). Predictions in §8 are registered before any
implementation or run. Adjacent prior art: `docs/parked_architecture_as_rate_step.md` (2026-08-06)
already states the two safeguards this design generalises — parameters are inputs a run may not
choose, and unmeasured parameters are calibrated against outcomes or not added at all.

---

## 1. The claim

**The model may not be asked for a magnitude.** Every reproducibility success in the project's record
is a rule or a pinned scalar; every failure is a sampled magnitude:

- pinned scalars transfer across models within 3% (facts pack §2.2); sampled magnitudes carry
  ×1.3–×2 (runs 16, 22);
- step 2, which is classification plus arithmetic, repeats at Jaccard 0.969 (run 21); step 3, which
  samples prices, repeats at ×1.288 (run 22);
- the ×1.288 is a **uniform level** (per-obligation ratios 1.13–1.46, sd 0.105) — the exact shape of
  one missing constant, not of scattered judgement;
- integration share, set by a table rate, came out identical in both runs: 16.67%.

So the split of labour becomes: **the LLM classifies and finds gaps; a pinned table prices; a script
sums.** After this change all three Hotyn engines produce no effort figures — M8 finally holds for the
whole chain — and the only numbers in the pipeline live in two versioned documents (the catalogue and
the rate table) plus the reference-class quantiles.

## 2. Why this is not "dissolving a sensor" (the §11.5 guard)

Findings §11.5 warns against quietly enriching a sensor into a fitted model. This proposal does the
opposite of quietly: it names the two sensors that were braided inside `Hotyn-D 1.0` — a **size
measurer** (items, counts, classes; measured reproducible to ×1.005) and a **rate holder** (pd per
item; never calibrated, sampled per run) — and separates them. The rate table is the **parametric
method of METHODOLOGY §2**, entering with its honest name and its known blind spots (quality equals
calibration quality; tables age; insensitive to specifics), carried as C4 metadata. The reference
class remains the independent outside view and owns the tail. Decomposition-as-structure remains the
specifics sensor. Sensor diversity is not reduced; it is restored to the original three-method design.

## 3. Design

### 3.1 The size vector

From a work model (run-21 form), the deterministic part is already there: items as
(element, class, activity) triples plus the per-parent C3 bases. The vector adds one judgement per
item: a **size class**.

### 3.2 Size classes, from countable drivers

Three classes — `S` / `M` / `L` — assigned per item by the run, from **drivers declared per activity
in the catalogue**, not from impression. A driver is something countable in the element's declared
content and coverage. Examples of the form (final wording belongs to catalogue 1.2):

| activity | driver counted | S | M | L |
|---|---|---|---|---|
| K2 implementation of a `behaviour` | distinct actions in the declared content | 1 | 2–3 | ≥4 |
| K2 implementation of an `interface` | operations consumed/exposed named in content + obligations | 1 | 2–4 | ≥5 |
| K2 implementation of a `surface` | distinct user tasks the surface serves | 1 | 2–3 | ≥4 |
| A2 test design (any constructible) | inherits the element's K-size | — | — | — |
| G2 seed preparation for a `store` | entity kinds the store holds | 1 | 2–3 | ≥4 |
| K3 statement realisation | systems/components the property constrains | 1 | 2–4 | ≥5 |

The justification per item is one line **citing the count** ("3 actions: rank, re-rank on change,
explain ranking → M"). A driver that cannot be counted from the declared content is a **model or
catalogue defect, reported not repaired** — same rule as everywhere else in the chain.

### 3.3 The rate table

One row per (activity × element class × size class) that the catalogue's applies-to column permits —
on catalogue 1.1 that is roughly 100–150 real cells, most activities needing only the three size
columns. Each cell: **O / M / P person-days**, and each row a **provenance note** naming its source.
The table is:

- **pinned and versioned** (md5, like every other input);
- **model-free** — a table is a table; the `(engine × model)` stamp reduces to the classifier, which
  is where the residual model-dependence now lives;
- **gap-blind by construction** (§4);
- the home of the existing constants: C3's 20% is a row of it; cycle counts stay in the declaration.

### 3.4 `Hotyn-D 2.0`, the sensor

Input: the work model plus the drivers section of the catalogue. Output: per item — size class and the
counting line; plus everything 1.0 already produces that is *not* a number: doubts, **closure
violations**, the projection onto requirement ids (as item lists, not sums). **No person-days
anywhere in the output.** Contamination surface shrinks accordingly: a sensor that emits no numbers
has nothing to anchor.

### 3.5 The arithmetic, outside any LLM

A script joins vector × table: leaf O/M/P/E per item, C3 from the table rate over the same bases,
ΣE, per-requirement projection, and the aggregation of O/M/P (aggregation rule stated in the script,
not chosen per run). C1 changes role: a table cell whose M exceeds 10 pd is a **table defect** — the
split belongs in the catalogue's activity definitions, once, for everybody. The 1-pd floor becomes a
lint on the table for the same reason.

### 3.6 The falsification test gets sharper

Prediction 2 of `proposal_product_model.md` (swap `A-TB` → `A-FV`, estimate must move >×1.3) becomes
auditable line by line: the crossing re-runs (classification only), the script re-prices, and the
size of the move is arithmetic over two declared documents. If it fails to move, the fault is
locatable in a table row rather than in a judgement.

## 4. Who writes the table, and the contamination rule for tables

The Step-C discipline, applied one level up: **no table value may be a function of any run output.**
Version 0.1 is drafted by the gap-blind rate role (fresh session, sees the catalogue, the declaration,
the team grade — never any Hotyn ΣE, never a run file), from external base rates with each row's
source named. The colleague drafting it blind would be better still, and doubles as the human control
the review recommends.

**Disclosure, on the record:** this proposal's author has seen run 22's outputs (4.57 and 3.57 pd per
leaf). That is why §3.2's table shows driver *format* and no person-day values: values written here
would be anchored. The illustrative rows above contain counts, not prices, deliberately.

## 5. Calibration protocol

1. **v0.1 — external, uncalibrated.** Usable immediately; its provenance column says exactly what the
   center then means: *industry norms passed through this project's measured size vector.*
2. **First calibration — FaxRxTx**, the only case with a fact. Replay the chain (model → crossing →
   classify → price), compare raw against FACT.md **before** any adjustment. At n=1 exactly **one
   global level factor** may be fitted — the y=ax+b lesson (findings §11.1): more parameters than
   points is fitting the illusion of precision. Per-activity or per-dimension factors require ≥3
   cases.
3. **Validation is never on a fitted case.** The success metric lives in the review §7.1; the table
   may not be edited while looking at a gap it would explain (the provenance gate, verbatim, applied
   to tables).
4. Each calibration bumps the table version; estimates cite the table version they were priced under.

## 6. What this does not solve, named before anyone asks

- **The table's truth.** Until outcomes exist, the center is a declared prior, not a measurement. The
  proposal moves the unknown into a document that *can* be calibrated; it does not calibrate it.
- **Step-1 structure spread** (×1.56–1.65). Out of scope here; the review recommends propagation
  (carry both models through, report the induced width) and the human control — not more rules.
- **The tail.** Stays with the reference class; quantiles need points, not parameters (findings §11.5).
- **Correlation between items.** PERT independence is still an artifact; Steps B–D own it, as before.
- **Proportional work** (the D-TEAM weakness the catalogue names): if coordination behaves like a
  rate, the honest form is a rate row, not a per-item price. To be decided in the catalogue, once.

## 7. Migration

- Run 22 stands as the record of judgement-priced `Hotyn-D 1.0`. No conversion across the boundary;
  2.0 is a new instrument.
- Catalogue **1.2**: add the drivers per activity; split any activity whose honest L exceeds the
  ceiling.
- `work-estimator.md` → 2.0: identity section; PERT section replaced by size classes; C1 rewritten as
  above; prohibitions extended with "no person-day figures, anywhere, in any form."
- New: `rate_table.md` v0.1 (gap-blind author), `price_work_model.py` (~100 lines, plus a repeat-run
  comparator reusing `compare_run22.py`'s form).

## 8. Registered predictions

Scored after the first 2.0 batch; the failure conditions are part of the registration.

1. **Repeatability.** Two `Hotyn-D 2.0` runs on the batch-B work model: identical size class on ≥90%
   of items; ΣE through the script differs ≤ **×1.05** (was ×1.288 under 1.0). *Failure above ×1.15
   means the drivers are not countable as written — a catalogue defect, and the design holds only if
   fixing the drivers fixes the spread.*
2. **The model axis collapses on step 3.** Opus-classified vs Sonnet-classified vector, same work
   model, same table: ΣE ratio ≤ **×1.15** (the Lytin-era gap was ×2.0). *This is the test that the
   ×2 lived in sampled magnitudes, not in classification. Failure above ×1.4 kills the central claim
   of this proposal and the honest next step is measuring where the classification diverges, not
   defending the table.*
3. **Localisation.** Whatever differences remain trace to the three classification boundaries run 21
   already named (aggregate/constructible · statement/constructible · store) plus size-class
   boundaries, each visible in the logs with its count cited.
4. **FaxRxTx: recorded, not predicted.** n=1 supports no prediction; the raw ratio to FACT.md is
   written down before calibration, whatever it is. Registering a hoped-for closeness would be the
   §12b error (tuning toward a known outcome) one level up.

## 9. Cost

One table-drafting session (gap-blind role) · one catalogue edit · one sensor edit · ~100 lines of
script · two runs on an existing work model. Everything else — the work models, the comparison
scripts, the raw-preservation protocol — is already built and is reused unchanged.
