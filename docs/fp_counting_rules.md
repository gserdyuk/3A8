# The parametric instrument — function-point counting rules

**Version 0.2, 2026-08-26** (0.1-frame same day; bumped when §4's tables were pinned from run 38).
The third instrument. `METHODOLOGY.md` has listed it since day one; the author's condition, stated
2026-08-25, is what finally shapes it: **it is worth building only if its level comes from a table
rather than from recall.** A third instrument that samples its magnitude from a model is a third
voice with the same defect as the reference class — whose shape is triple-sourced and stable while
its level descends from a single remembered anchor and spans ×2.12.

This file is the frame: the procedure, the provenance discipline, and the declarations. The numeric
tables it needs (§4) are **not written here** — they are pinned at `tools/parametric/weights.tsv`
and `tools/parametric/thresholds.md` from gap-blind first-approximation runs (run 38, n=2, exact
agreement on every cell; transcripts in `tools/parametric/run38_raw/`).

---

## 1. How the author's condition is met

Every magnitude in the instrument has a named home, and none of the homes is recall:

| quantity | where it comes from |
|---|---|
| **size** (function points) | classification of the pinned requirement list against these rules, by `Hotyn-P 1.0` — the same act `Hotyn-D` performs, measured at ×1.03 repeat agreement |
| **weights and complexity thresholds** | the published counting standard, stated by a gap-blind norms author `Hotyn-N 1.0` (§4) — the same pattern as the rate table: the orchestrator's recall is not a source |
| **level** | curves fitted on open datasets in this repository (`mars_model/`): China `Effort ≈ 27.1·AFP^0.77` (n=499), Kitchenham `≈ 37.1·AFP^0.67` (n=145), both in person-hours — and the script **refits them from `mars_model/data/` at every run** rather than carrying copied constants |
| **corridor** | the empirical residual quantiles of those fits — a P10–P90 whose width comes from the scatter of hundreds of real projects, not from a declared correlation |
| **arithmetic** | a script, `tools/parametric/parametric.py`, deterministic |

## 2. What a function point is, in one paragraph

A **function point** is a standard measure of a system's functional size: the count of its
user-visible functions — inputs, outputs, queries, stored data — each weighted by a small integer
from a published table according to its complexity. The measure is fifty years old, has an ISO
standard behind it (IFPUG — the International Function Point Users Group, whose counting manual is
the de-facto reference), and is the size axis of the open effort datasets this repository already
holds. It measures **what the system does, not how hard it is to build** — which is exactly the
blind spot declared in §6.

## 3. The components — structure, method-authored

The taxonomy is the standard's, restated here in plain language. `Hotyn-N` is asked to state the
standard's own taxonomy independently; a difference between its statement and this table is a
finding against this file, not against the run.

Two **data functions** — things the system keeps:

| component | plain meaning |
|---|---|
| **ILF** — internal logical file | a coherent group of data the system itself maintains (an entity with its records, not a physical table) |
| **EIF** — external interface file | a coherent group of data the system reads but some other system maintains |

Three **transactions** — things a user or another system does with it:

| component | plain meaning |
|---|---|
| **EI** — external input | an elementary process that brings data in and changes what the system keeps |
| **EO** — external output | an elementary process that sends data out with some derivation in it — a calculation, an aggregation |
| **EQ** — external inquiry | an elementary process that retrieves and shows data as it is, nothing derived |

Complexity of each item is classified **Low / Average / High** by counting named things — for data
functions the distinct record types and data elements they hold; for transactions the data elements
crossing the boundary and the files referenced. The threshold matrices are numeric and belong to §4.

## 4. The numeric tables — pending, and from whom

Two tables are required and **neither may be written by the orchestrator**:

1. **the complexity threshold matrices** — per component, the counts that make an item Low /
   Average / High;
2. **the weight table** — component × complexity → points.

Both are stated by **`Hotyn-N 1.0`** (`.claude/agents/fp-norms-author.md`), gap-blind, from the
published standard only, at **n ≥ 2 independent runs**; agreement between runs is the check, the
same way three independent `Hotyn-K` runs confirming "1 pd = 8 net hours" was the check on the
table's unit.

**Done, 2026-08-26 — run 38, n=2, on `claude-fable-5`: exact agreement on every numeric cell.**
Both runs named the same standard (IFPUG CPM 4.x / ISO/IEC 20926, unadjusted), stated identical
threshold matrices (18 boundary values) and an identical weight table (15 cells), independently
flagged the same commonly-misremembered rule (EQ shares the EO/EQ matrix, takes the EI weight
row), and declined the adjustment factor per the ruling. Pinned: `tools/parametric/weights.tsv`,
`tools/parametric/thresholds.md`; transcripts verbatim in `tools/parametric/run38_raw/`.

## 5. Declarations

- **Input of the sensor: the pinned requirement list and the assumption log — never the product
  model.** The instrument is a third voice only if it is independent of the chain's least stable
  step (`Hotyn-M`, agreement on what-goes-with-what J 0.31–0.41). It shares its input with
  `Lytin-R` and nothing downstream of step 0.
- **The sensor produces no points, no sums, no totals.** It classifies and enumerates; the script
  multiplies and adds. The sensor never sees the weight table, the same way `Hotyn-D` never sees
  the rate table.
- **VAF = 1.0, declared.** The standard's value adjustment factor is fourteen subjective ratings —
  precisely a magnitude sampled by a model, which this pipeline forbids. Its published range,
  ×0.65–1.35, is small against the class's own ×2.12 level spread. The fitted curves use adjusted
  counts (AFP); treating our unadjusted count as AFP is this declaration, stated in every report.
- **The unit chain, stated at every output.** The curves are fitted on **recorded timesheet
  person-hours**: leave, holidays and sickness excluded (booked elsewhere), within-day overheads
  included (`docs/constants.md` §5a). Conversion to this project's net task hours: **×0.75** — the
  same declared factor, with the same provenance, as the reference class conversion
  (`docs/constants.md` §5b). Onward conversions (table person-days ÷ 8, staffed person-months by
  the settled ladder) are printed with every factor named.
- **The two curves are two rows, not a choice.** China and Kitchenham are two samples of the same
  kind of table; the report carries both, with n, the fitted exponent and the residual spread of
  each. Picking one would be a decision the data does not make.

## 6. The blind spot, declared

Function points measure **functional size only**. Invisible to this instrument, by construction:
nonfunctional obligations (performance, availability, security hardening), migration and parallel-run
demands beyond their data-conversion functionality, environment and process costs, and everything
`Hotyn-W` derives from the technology declaration. The sensor reports every requirement it cannot
place as **outside the instrument's scope** — that list is the boundary of what the number means,
and on a case rich in demanded work the parametric figure is expected to sit low for exactly this
reason. A divergence explained by the scope list is the instrument working, not failing.

Second declared weakness, inherited from the data: the datasets are other people's organisations of
the 1990s–2000s, R² 0.44–0.53 — half the variance is outside size — and only completed projects are
in them. The corridor carries the scatter; nothing carries the survivorship.

## 7. The run protocol

1. `Hotyn-N 1.0`, n ≥ 2, gap-blind → pin `weights.tsv` + `thresholds.md`, record agreement.
2. `Hotyn-P 1.0` on the pinned requirement list, n = 2 — component inventory and complexity
   classes, enumerations verbatim.
3. `tools/parametric/parametric.py` — UFP, both curves, P10/P50/P90 from residuals, the unit chain
   printed, the out-of-scope list attached.
4. The result enters the report as the third instrument's row, units declared on both sides of any
   comparison.
