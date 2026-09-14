# Sensor notes — one per curve on the panel

A sensor here is anything that produces a curve on the estimate report's price × probability-density
panel (`tools/report/build_report.py`). Five do today. Each has one note, written for two readers:
the person looking at the panel, and the diagnostician that needs both sides' blind-spot catalogues.

| note | curve | engines | invoked by |
|---|---|---|---|
| [`bottom-up-model.md`](bottom-up-model.md) | a bell around the calibrated centre, built on an assumed ρ = 0.5 between items | `Hotyn-M`, `Hotyn-W`, `Hotyn-D`, `Hotyn-K` + script | `/3a8:estimate-product` |
| [`reference-class.md`](reference-class.md) | one curve per class reading, never pooled | `Lytin-R` | `/3a8:estimate-reference-class` |
| [`bottom-up-direct.md`](bottom-up-direct.md) | a family of one-sensor readings | `Lytin-D` (closed generation) | `/3a8:estimate-wbs` |
| [`parametric.md`](parametric.md) | level from a size count, corridor from real-project residuals | `Hotyn-P`, `Hotyn-N` + script | by hand, `tools/parametric/parametric.py` |
| [`no-method-baseline.md`](no-method-baseline.md) | a family of thin curves, one per bare run | none — that is the point | by hand, pinned prompt |

## What every note contains, in this order

1. **How the sensor was conceived** — the original role, what it was built to close, and what
   arrived unplanned.
2. **The question the method answers.**
3. **What the width of its curve means** — project risk, instrument repeat, model sampling, or
   residual scatter of real projects. These are different quantities and the panel must say which.
4. **What it sees and what it must never see** — its row of the `PIPELINE.md` matrix and its
   static blind-spot list.
5. **Measured properties**, each with the run that measured it.
6. **How to read a reading** — unit, declaration, conversions, the caveats it leaves by construction.
7. **Versions**, and what each changed.
8. **What we want to add or change** — open ideas with what each would move (level, spread, or
   report only), each pointing at its `BACKLOG.md` line.

Sections 2–7 say what the sensor **is**. Section 1 says what it was **meant to be**, section 8 what it
**may become**. The three are kept apart on purpose.

## These notes are expected to disagree with the code

That is their content, not their defect. A note records where the sensor came from and where it is
being pushed; the agent file records what it does today. When the two differ, the difference is one
of three things — an idea not yet implemented, an addition made without an idea, or a property that
arrived by accident — and the note is where that gets named. Nothing here is a spec; when a bump
lands, section 8 empties into section 7 with a date, and section 1 is not rewritten.

## What each width includes — and what it leaves out although it is known

The curves are comparable on the axis (one unit after conversion) and each declares a width. They
are not comparable in what the width contains. Recorded 2026-09-14 from the five notes' sections 3
and 5; every figure has its run there.

| curve | inside the width | outside it, though measured or known |
|---|---|---|
| bottom-up, the chain | co-variation of the rate cells' O/M/P at an assumed ρ = 0.5 | structure spread at step 1 (×1.02–×1.56); the rate table being one sample (×1.38–×1.50 on re-generation); team grade (×2–3 between bands); named holes and findings; the apparatus repeat (×1.05) |
| reference class | heterogeneity of the class — where projects like this land | the level's uncertainty between readings (×1.95–×2.12); each reading is drawn alone, the distance between them is not a width |
| bottom-up direct | the model's sampling of the magnitude (CV ≈ 10%) | the ×2 shift when the model changes |
| parametric | residual scatter of real projects around the size–effort curve | the level sitting on the enumeration floor (×20 against the one fact) |
| no-method baseline | the model's sampling within one batch | the level shift between batches (×1.145) |

Consequence for the chain: even if ρ = 0.5 holds, its bell is a lower bound of its own uncertainty
— four known sources are outside it, and one of them, the table's sampling, is about the size of the
whole bell. The class bell is honestly wide and does not know where it stands. The panel therefore
answers "how wide is each estimate by its own rules"; it does not yet answer "how uncertain is the
project", and no curve claims to. A legend line per curve should carry both columns.

## Two rules

- **Agents never see these notes.** Section 5 is an anchor (a sensor told its own spread will drift
  toward it); section 8 is worse (a sensor will start doing what we only meant to try). The notes are
  orchestrator-side documents like `PIPELINE.md`, and are never pasted into a sensor prompt.
- **The panel's legend takes one line from each note's section 3.** A curve whose width is instrument
  repeat drawn beside a curve whose width is project risk is a picture that invites choosing a price
  "between" two different quantities. The label is what prevents that.
