# Sensor note — bottom-up direct (WBS + PERT, one sensor)

**Eight sections:** 1 how it was conceived · 2 the question it answers · 3 what its width means ·
4 what it sees and must never see · 5 measured properties · 6 how to read a reading · 7 versions ·
8 what we want to add. Sections 2–7 are what the sensor is; 1 is what it was meant to be; 8 is what
it may become. **This note is expected to disagree with the code** — the disagreement is the record of
what came from the idea, what was added, and what arrived by accident.

Engine: `Lytin-D`. Invoked by `/3a8:estimate-wbs`. Curve on the panel: a family of one-sensor
readings. **Closed generation** — it does not run inside the current instrument.

---

## 1. How it was conceived

**The idea.** Sensor #1 of `METHODOLOGY.md`: decomposition, bottom-up plus PERT — the method that
captures the specifics of individual tasks and is blind by construction to correlated and systemic
risk. The first tree was drawn by hand (`Lytin-D 0.1`, 26 leaves, 486 pd, July 2026, `findings.md`
§9); the sensor definition followed on 2026-08-05 with the first end-to-end wrapper run, which was
wrong by ×4 and said so (`findings.md` §12a).

**What it was then turned into.** Ten identical runs showed the sensor *repeatable and biased, not
unstable* (`findings.md` §12b), and the programme became: pin the constants the measurement showed
to be loose. C1 the leaf ceiling, C2 the fixed top level, C3 integration as a rate, C5 modules from
functions, C6 the split check — versions 1.0 to 4.0 in three weeks, each confirmed by a batch of ten
(`PIPELINE.md`, the `Lytin-D` table).

**What arrived unplanned — and closed the generation.**
- **The variance relocates.** Each constant closed the parameter it named (leaf price CV 15.9% →
  5.6%; node count 44.1% → 8.2%; integration share 10.4% → 0.78%) and the total's CV did not narrow,
  because the spread moved to the next free parameter. Splitting depth was the last one, and it
  carried essentially all of it (`docs/review_2026-08-21_running_in_circles.md`).
- **The floor.** With no method at all the same prompt gave CV 8.55% — below every version ever
  measured. The variance had been moving inside a band that existed before the method did (run 14).
- **The model is the second coordinate.** `4.0` on one model: mean 1625; on another: 804. ×2.02,
  t = 14.70, same words, same constants. The model outweighs the entire version history (run 16).
  Until run 16 nobody had recorded which model a batch ran on.

These three findings are why the `Hotyn` chain exists. The sensor was not a failure: it produced the
measurements that showed where the magnitude was coming from.

## 2. The question it answers

*If one estimator reads this description, breaks the work into leaves under a fixed set of rules,
and prices each leaf as O / M / P, what total comes out?* It answers about the parts, with the
magnitude chosen by the estimator — here, by the model.

## 3. What the width of its curve means

**Model sampling of the magnitude.** The family of thin curves is n readings of one sensor on one
input; the spread is how differently the model prices the same leaves each time (CV 9–17% across
versions). The sensor's own O…P range per run is *not* a corridor either — it is the sum of leaf
ranges and assumes a correlation nobody measured. Neither width is project risk. And the whole
family shifts by ×2 when the model changes.

## 4. What it sees and what it must never see

`PIPELINE.md`, Lytin matrix, row A.1: sees the **project description, the assumption log, and one
declared projection axis**; must never see any other method's numbers, any target, budget or
deadline, any prior tree. It stops and reports contamination if it does.

**Static blind spots** (`METHODOLOGY.md` §2): correlation of risk across tasks; systemic and
integration risk; organisational overhead. The sensor carries the list symmetrical to the reference
class's so the diagnostician has both catalogues.

## 5. Measured properties

| property | value | run |
|---|---|---|
| repeat, one model, by version | CV 9.25–17.4% (`0.9` → `4.0`); levels 1147 → 1674 pd on BMS, only some of it method | runs 6–13, 17 |
| **across models, same engine, same prompt** | **×2.02** (1625 vs 804), t = 14.70; CV 9.25% vs 11.56% | run 16 |
| the no-method floor on the same prompt | CV 8.55% (one model), 20.92% (the other); no version significantly beat it | runs 14, 16 |
| what each constant closed | leaf price, node count, integration share — each confirmed; total unchanged | facts pack §1–2 |
| first end-to-end wrapper on a case with a fact | wrong by ×4, the report flagged it | run 5 (FaxRxTx) |
| branch 9 (migration) on a greenfield RFP | one model: `none` in 10 of 10; the other: 32–67 pd in 10 of 10 — C2 cannot say which is wrong | run 16 §4 |

## 6. How to read a reading

- The unit is whatever the run declared — person-days of the sensor's own convention; convert only
  in the comparison layer (`docs/constants.md` §4a).
- Stamp the reading with **engine × model × axis**; a number with fewer coordinates cannot be
  compared with anything (`agents/estimator-decomposition.md`, engine identity).
- Read the leaf distribution and the assumption-log exceptions, not just the total: they say where
  C1 bound and where the sensor kept a leaf whole.
- A reading from this sensor beside a chain reading is a **cross-generation** comparison and needs a
  measured conversion; there is none (`docs/instrument.md`, head).

## 7. Versions

| engine | change | measured |
|---|---|---|
| `0.1` | the manual July tree | 486 pd, n = 1 |
| `0.9` | unconstrained definition | 1147, CV 17.4% |
| `1.0` | C1 leaf ceiling, C2 fixed top level, C3, C4 | 1284, CV 8.9% |
| `2.0` / `2.1` / `2.3` | C5 modules from functions; scope; three-part node report | 1518 → 1668, CV ~10% |
| `3.0` | C3 replaced: integration = 20% of the leaf sum beneath each node | 1674, CV 10.86% |
| `4.0` | C6 split-consistency check, diagnostic only | 1625 / 804 by model |
| `5.0` | C2 replaced by a **declared projection axis** in the prompt; the sibling-run pointer removed | axis batch not yet run |

Full table with what each was and what it bought: `PIPELINE.md`, "Labels for the decomposition
sensor".

## 8. What we want to add or change

The generation is closed; these are kept because each is a registered experiment with predictions
written down, and because the sensor is the cheapest way to measure a model.

| idea | would move | where it lives |
|---|---|---|
| **The axis batch** — 2 axes × 2 models × n = 5; the prediction that matters: axis effect below ×1.4 against a model effect of ×2.02 | spread (attribution) | `BACKLOG.md` "Earlier — projection axes"; `docs/proposal_axis_projection.md` |
| **C7 — coverage at every split**, a second splitting trigger; major whenever it lands; reverted, not tuned, if the cross-model ratio stays above 1.7 | level, spread | `BACKLOG.md` C7; `docs/proposal_C7_coverage_at_every_split.md` |
| **Branch 9 has no applicability criterion**; the completeness report can read 100% on a tree missing a branch | level (omission) | `BACKLOG.md` "Pipeline defects" |
| **The reverse audit** on one tree from each model of run 16 — if it cannot tell them apart it is not an audit | level (down) | `BACKLOG.md` B |
| **Behaviour inventory** as the unit of pricing — held until C7 reports | level | `BACKLOG.md` A |
