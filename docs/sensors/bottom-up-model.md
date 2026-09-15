# Sensor note — bottom-up through a product model (the chain)

**Eight sections:** 1 how it was conceived · 2 the question it answers · 3 what its width means ·
4 what it sees and must never see · 5 measured properties · 6 how to read a reading · 7 versions ·
8 what we want to add. Sections 2–7 are what the sensor is; 1 is what it was meant to be; 8 is what
it may become. **This note is expected to disagree with the code** — the disagreement is the record of
what came from the idea, what was added, and what arrived by accident.

Engines: `Hotyn-M` (product model) · `Hotyn-W` (work model) · `Hotyn-D` (size classes) · `Hotyn-K`
(rate table) · a script (arithmetic). Invoked by `/3a8:estimate-product`. Curve on the panel: a bell
around the calibrated centre, built on an assumed ρ = 0.5 between items.

---

## 1. How it was conceived

**The idea it replaced.** Sensor #1 of `METHODOLOGY.md` was one decomposition sensor that turned an
RFP straight into priced work (`bottom-up-direct.md`). Six weeks of pinning its constants never
narrowed its spread: each rule bound the variable it named and the magnitude moved to the next free
one (`docs/review_2026-08-21_running_in_circles.md`).

**The idea itself, in two steps.** First, the author's observation of 2026-08-14 that
"requirements → WBS" is not a mapping — there is a hidden intermediate, the *thing to be built*,
and the work is derived from it, not from the text (`findings.md` §12e;
`docs/proposal_product_model.md`). That gave `Hotyn-M` → `Hotyn-W` on 2026-08-19. Second, the
review of 2026-08-21: Hotyn had stabilised everything except the magnitude scale, which was still
sampled from the model's prior every run. Pin that last variable in a table the sensors never see,
and the sensors need produce no numbers at all. That gave `Hotyn-D 2.0` (classes, not prices) and
`Hotyn-K` (the table), and the design principle in one sentence: **numbers come from a table; the
model only chooses rows** (`docs/instrument.md` §1).

**What it was meant to buy.** Repeatability first — the goal was to beat the no-method floor of
CV 8.55% that no version of the direct sensor had beaten — and, behind that, a number whose
provenance can be audited row by row.

**What arrived unplanned.**
- The unit. The person-day carried a convention inside it; that cost three days and one ×1.33 error
  in the project's own favour before the table was re-expressed in hours (`docs/constants.md`,
  `docs/the_unit_of_the_rate_table.md`). Nobody designed the unit; it surfaced when a fact was opened.
- The table is one sample. Repeat sampling of the rate role was later measured at ×1.38–×1.50; the
  table is kept as a fixed set of constants because a constant does not vary between runs, and the
  spread is recorded as provenance (`docs/rate_table.md` head).
- FaxRxTx came out **under** the fact although the construction only adds (accretion, crossing,
  splitting, rounding up). Unexplained (`docs/status_2026-08-27.md` §5).
- A quarter of the end-to-end gap in run 42 turned out to be the model-bracket step — pure
  arithmetic, not judgement (`examples/FaxRxTx/run42_measurement.md`).

## 2. The question it answers

*What does this work cost at the pinned rates, once the thing to be built has been named element by
element and the declared technology has said what must be done to each?* It answers about **this
project's parts**, and about nothing outside them.

## 3. What the width of its curve means

**A bell built on an assumed correlation of ρ = 0.5 between items.** The chain produces one number
per run; the panel draws it as a normal around the calibrated centre with sd ≈ 0.166 × centre —
P10–P90 of ×1.54 — obtained by restoring the O/M/P of every rate cell (the assembly had collapsed
each to E before summing) and summing them as equicorrelated items at ρ = 0.5
(`sessions/2026-08-26_the_report_becomes_a_format.md`). The assumption may be true or not: the
correlation between items has not been measured.

Why 0.5, and what other values would do:

| ρ | P10–P90 of the sum, ~580 items | |
|---|---|---|
| 0, independent | ×1.04 | variance averages away; the band both earlier generations flagged as an artefact |
| **0.25 … 0.75** | **edges move about ±20%** | the width changes slowly over this threefold range, so its middle, 0.5, was taken |
| 1, perfectly correlated | ×1.87 | 2.56 σ; ΣO…ΣP (×4.19) is *six* sigma of the same sum, not a percentile band |

0.5 was chosen from that slow change of width across 0.25–0.75, not from the FaxRxTx outcome.

Two other widths exist and are **not** what the bell shows: the repeat spread of the apparatus
(×1.03 from classification, ×1.05 end to end) is narrower and is a property of the instrument; the
dispersion of outcomes of projects like this is the class curve's width, not this one's. The
deliverable reports a third band as its corridor — the spread of the calibration rates, low /
central / high — which is the rates' band and not a percentile either
(`examples/SAS/estimate_SAS_2026-09-08.md` §1).

`docs/instrument.md` §4 predated the session of 2026-08-26 and said the chain declares no P10–P90 —
stale on this point from that day; brought in line 2026-09-14.

## 4. What it sees and what it must never see

From the `PIPELINE.md` matrix, Hotyn rows:

| step | sees | must never see |
|---|---|---|
| model `Hotyn-M` | pinned product obligations, processing order, assumption log | any estimate, any prior tree, budget / deadline / team size |
| work `Hotyn-W` | the closed product model, the technology declaration and parameters, the demanded-work list | any estimate, any prior work model, any cost anchor |
| classes `Hotyn-D` | the work model, the pinned sizing rules | **any rate, price, person-day, budget, duration, prior estimate** |
| rates `Hotyn-K` | a sanitised catalogue extract, one line of team grade | any run output, any total, **any gap a rate would explain** |
| script | classes × table | — |

**Static blind spots, by construction** (`METHODOLOGY.md` §2, decomposition row): correlation of
risk across tasks; systemic and integration risk; organisational overhead. Plus what the chain
itself names: **no knowledge of the team** — capability spans ×2–3 between grade bands, the table
declares the grade it assumes and nothing downstream reads it (`docs/team_grade_as_an_input.md`).

## 5. Measured properties

| property | value | run |
|---|---|---|
| step 1, same obligations placed, different grouping | Jaccard 0.31 (BMS) / 0.41 (FaxRxTx); structure size ×1.56 / ×1.02 | runs 22–24, 29 |
| step 2, work model repeat | Jaccard 0.969 over 77 elements, 553 pairs | run 30 |
| step 3, size-class repeat | 87.3% agreement on 79 element classes → ×1.03 on the total | run 31 |
| end to end, second product model priced with no rate changed | **×1.0532** (FaxRxTx; the favourable case) | run 42 |
| against a documented outcome | **99.4 vs 120 staffed pm, ×1.21 low**, both repeats inside the gate, nothing fitted on the case, despite a known ×8.5 under-pricing of one stage | run 32–34 |
| against the no-method baseline, same case, pinned conversion | chain ×1.21 low, baseline ×1.47 high; n = 1, the fact's own ±20% band contains the chain | run 41 |
| SAS, placed against the class | 38 118 net h sits at P35 of one class reading and P80 of the other | runs 46–47 |
| step 1 human control | **never run** — whether the grouping spread is instrument defect or honest multiplicity of designs is not settled | — |

The end-to-end figure is carried with its caveat: measured on the case whose two models agree best;
the BMS pair differs by ×1.56 in structure size and has not been priced end to end
(`BACKLOG.md` item 1a).

## 6. How to read a reading

- The number is **net person-hours** of work on the task, presence excluded (`docs/instrument.md`
  §0). Days of presence exist only in the comparison layer, by the pinned conversion — 6 net task
  hours per present day, ×1.10 leave, 21 days a month (`docs/constants.md` §4a).
- Every sensor prints its engine stamp; the orchestrator records the model. A reading is a property
  of (project × engine × model); a different model is a different instrument.
- The reading carries **named holes** — elements the rules could not size — and **findings** — work
  the product needs but no declared activity covers. Both are outside the number, by name. A reader
  who ignores them reads a smaller project than the one described.
- The rates are external norms fixed by decision, calibrated against no outcome. The centre is a
  table's opinion of these classes, not a forecast.

## 7. Versions

| engine | change | date |
|---|---|---|
| `Hotyn-M 1.0 → 1.1` | partial coverage counts; coverage declared at the node that realises the obligation; closure check | 2026-08 |
| `Hotyn-W 1.0 → 1.1` | scope *per aggregate* → *per parent*; every refusal labelled filter / judgement | 2026-08 |
| `Hotyn-D 1.0 → 2.0` | **1.0 produced person-days per item; 2.0 produces no numbers with units** — counts only | 2026-08-21 |
| `Hotyn-K 1.0 → 1.1` | required declaration (unit, leave, roles, source disagreement) before any figure | 2026-08-26 |
| rate table v0.1 → v0.1-h | re-expressed in person-hours, ×8, no value reviewed | 2026-08-27 |
| `Hotyn-M 1.1 → 2.0` | **coverage in leaves only**: a leaf carries its load, a node only its children; posited things are nodes, childless nodes deleted and single-child nodes lifted at closure, all logged; `covered` names leaves only. Plus write-as-you-go and the reduced output. Motivated by run 53 (`docs/review_2026-09-15_sensor_texts.md`). No reading yet | 2026-09-15 |
| `Hotyn-M 2.0 → 2.1` | M2: identity by coverage set is for comparing models, not for building one; distinct things with the same coverage are distinct leaves. Runs 55–56 read the 2.0 sentence three ways and the level followed (139 / 145 / 182) | 2026-09-15 |
| `Hotyn-W 1.1 → 1.2` | W7: `aggregate` is the class of every node and of nothing else; declared content of a leaf is its name plus the obligations it covers | 2026-09-15 |

`Lytin-D` is the sensor this chain replaced; it does not run inside it.

## 8. What we want to add or change

| idea | would move | where it lives |
|---|---|---|
| **A measured ρ instead of an assumed one.** The bell rests on ρ = 0.5 taken from the slow change of width across 0.25–0.75; the correlation between items has not been measured. A measured ρ would say whether the assumption holds | report (the bell's width) | `sessions/2026-08-26_…` §9, `docs/status_2026-08-27.md` §5 |
| **Shape from the class, level from the chain** — the division of labour the session named and nobody has decided: the class's shape is triple-sourced and stable, its level spans ×2.12; the chain's level is repeatable and its width is a convention | report (which curve carries which quantity) | `sessions/2026-08-26_…` §9 |
| **Calibrate the table against outcomes**, evidence beside each changed cell; FaxRxTx's ×8.5 stage is the first candidate | level | `docs/rate_table.md` status paragraph |
| **The reverse audit** — the brake on over-counting the construction lacks; designed, never run; the auditor is itself a model and must be measured first | level (down) | `docs/proposal_reverse_comparison.md`, `BACKLOG.md` B |
| **Team grade as an input** the table reads, instead of a line it assumes | level | `docs/team_grade_as_an_input.md` |
| **BMS end to end** — the unfavourable case for repeatability | spread (measurement) | `BACKLOG.md` 1a |
| **A human control on step 1** — whether grouping spread is the instrument or the document | spread (interpretation) | `docs/instrument.md` §3 step 1 |
| **A generic assembler** reading a fixed sensor output format, so step 4 stops being handwork | report only | `BACKLOG.md` 2026-09-14 |
| **Architecture as a rate step** — parked | level | `docs/parked_architecture_as_rate_step.md` |
