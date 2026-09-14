# Sensor note — parametric (function points)

**Eight sections:** 1 how it was conceived · 2 the question it answers · 3 what its width means ·
4 what it sees and must never see · 5 measured properties · 6 how to read a reading · 7 versions ·
8 what we want to add. Sections 2–7 are what the sensor is; 1 is what it was meant to be; 8 is what
it may become. **This note is expected to disagree with the code** — the disagreement is the record of
what came from the idea, what was added, and what arrived by accident.

Engines: `Hotyn-N` (the norms — IFPUG tables) · `Hotyn-P` (the counter) · a script
(`tools/parametric/parametric.py`). Run by hand today. Curve on the panel: level from a size count,
corridor from the residual scatter of real projects; drawn on the log panel when off the density
scale.

---

## 1. How it was conceived

**The idea.** The parametric row of `METHODOLOGY.md` §2: a method whose value is *independence from
subjective judgement altogether*, and whose weakness is that it lives or dies by calibration data.
Built on 2026-08-26 as "iteration 0 of the parametric — level from a table, corridor from residuals"
(commit `cbe9a6a`), with the same construction principle as the chain: the sensor counts and
classifies, and every number with a unit comes from a pinned table or a fitted curve it never sees.

**Two roles, on purpose.** `Hotyn-N` states the published standard's numeric tables — complexity
threshold matrices and component weights — from the standard alone, so the counting rules rest on a
stated norm rather than the orchestrator's recall. `Hotyn-P` classifies the pinned requirement list
into data functions and transactions by enumerating named things, sees the thresholds and never the
weights. The script joins classes to weights (UFP), refits two published effort-size curves from the
data in `mars_model/data/` at every run (China, n = 499; Kitchenham, n = 145; recorded person-hours),
and takes the corridor from the empirical P10/P50/P90 of the fit residuals in log space.

**What it was meant to buy.** A third, judgement-free side for the diagnosis, and — the thing the chain
lacks — **a corridor whose width comes from the scatter of real projects**, not from a declared
correlation.

**What arrived unplanned.**
- **The enumeration floor.** On both cases nearly every item classifies Low, because no pre-contract
  document enumerates fields: "the RFP names workflows and sources far more richly than it names
  fields" — both runs, unprompted, in almost the same words (runs 39, 40). The count's transaction
  axis follows the document's density; its complexity axis does not move. The level lands an order of
  magnitude below every other sensor.
- **The two datasets disagree in level**, and the script reports both rows rather than choosing.
- The norms author flagged, on both runs, the commonly misremembered rule (EQ graded on the EO/EQ
  matrix, weighted on the EI row) — a check nobody asked for.

## 2. The question it answers

*How much functionality does this document imply, in the standard's own units, and what did real
projects of that functional size cost?* It answers about size, not about work, and about the corpus,
not about this team.

## 3. What the width of its curve means

**Residual scatter of real projects around a size–effort curve** — the only corridor in the
instrument that is empirical: China ×0.28 / ×1.04 / ×3.16 and Kitchenham ×0.47 / ×1.00 / ×2.11 at
P10 / P50 / P90 around the fitted level. That is genuine dispersion of outcomes at a given size. But
the *level* it is drawn around sits on the enumeration floor for pre-contract documents, so on the
panel the curve is honest about its shape and wrong about its place. The repeat spread of the count
itself is small (×1.05–×1.09 on UFP) and is not what the width shows.

## 4. What it sees and what it must never see

| role | sees | must never see |
|---|---|---|
| `Hotyn-N` | the task statement naming which tables are asked for | any requirement list, any project, any count, any effort figure |
| `Hotyn-P` | the pinned requirement list, the assumption log (team and unit lines withheld), the component definitions and threshold matrices | **the weight table**, any product or work model, any prior count, any effort figure, any other instrument's output |
| script | classes × weights × the two datasets | — |

**Static blind spots** (`METHODOLOGY.md` §2, parametric row): quality depends entirely on the
calibration data; models age; the datasets' role coverage is inconsistent (the ISBSG resource-level
problem, declared in every readout); VAF is out of scope by ruling, so nothing about the technical
environment enters.

## 5. Measured properties

| property | value | run |
|---|---|---|
| norms, two gap-blind runs | **exact agreement** on 18 boundary values and 15 weight cells; IFPUG CPM 4.x / ISO/IEC 20926 | run 38 |
| count repeat, FaxRxTx | UFP 78 vs 82 = ×1.051; item Jaccard 0.833; class agreement 14/15 | run 39 |
| count repeat, BMS | UFP 195 vs 213 = ×1.092; data-function inventory identical 14/14; 92 of 99 items Low | run 40 |
| **against the FaxRxTx fact** | P50 ≈ 5 staffed pm on either dataset against **120** staffed pm — more than ×20 low; the count sat on the floor (16–17 items, 23–27 of 52 obligations outside scope) | run 39 vs `FACT.md` |
| document density effect | transactions ×2.5 on BMS vs FaxRxTx; complexity unchanged | run 40 |
| level disagreement between datasets | China P50 1 219 vs Kitchenham 960 net h on BMS | run 40 |

## 6. How to read a reading

- The readout prints every figure in **four units with every conversion named**: recorded
  person-hours (native), net task hours (×0.75), table person-days (/8), staffed person-months
  (/6 per present day, ×1.10, /21). Read the native column; the rest are the house ladder applied.
- Read the **outside-scope list** and the **under-enumerated list** before the number. On a
  pre-contract document they are most of the input.
- Two rows, two datasets, neither chosen. A reader who averages them has made a decision the
  instrument declined to make.
- The corridor's shape is trustworthy; its centre is a floor reading until the driver problem in §8
  is solved. Drawn on the log panel for that reason.

## 7. Versions

| component | state | date |
|---|---|---|
| `Hotyn-N 1.0` | first and only; tables pinned on exact cross-run agreement | 2026-08-26 |
| `Hotyn-P 1.0` | first and only | 2026-08-26 |
| `docs/fp_counting_rules.md` v0.1 → v0.2 | numeric half moved to `tools/parametric/thresholds.md`, `weights.tsv` | 2026-08-26 |
| `tools/parametric/parametric.py` | iteration 0; refits curves at every run, carries no constants | 2026-08-26 |

## 8. What we want to add or change

| idea | would move | where it lives |
|---|---|---|
| **A size driver a pre-contract document actually names** — the floor is a property of the input, not of the count; drafts exist for drivers other than fields | level (up, by an order of magnitude) | `docs/draft_catalogue_1.2_size_drivers.md` |
| **Decide what the curve is on the panel** — an instrument, or a floor marker labelled as such; today it is drawn with a caption saying it is off scale | report only | `tools/report/build_report.py`, "the parametric instrument" |
| **Calibrate on outcomes** — one fact exists and the instrument missed it by ×20; a second fact is the gate | level | `BACKLOG.md` "Next — validity" |
| **Phase 2 — granular history** (throughput Monte Carlo, parametric on own data); TAWOS inaccessible, no sprint history in hand | new sensor | `BACKLOG.md` "Longer-range", `findings.md` §8 |
