# Sensor note — reference class (the outside view)

**Eight sections:** 1 how it was conceived · 2 the question it answers · 3 what its width means ·
4 what it sees and must never see · 5 measured properties · 6 how to read a reading · 7 versions ·
8 what we want to add. Sections 2–7 are what the sensor is; 1 is what it was meant to be; 8 is what
it may become. **This note is expected to disagree with the code** — the disagreement is the record of
what came from the idea, what was added, and what arrived by accident.

Engine: `Lytin-R`. Invoked by `/3a8:estimate-reference-class`. Curve on the panel: one per class
reading, never pooled.

---

## 1. How it was conceived

**The idea.** Sensor #2 of `METHODOLOGY.md` from the first day: reference class forecasting after
Flyvbjerg — look only at the class of projects, never at the parts of this one, and report where
such projects actually land relative to their own early estimates. Its value to the pipeline is
exactly what it cannot see (`findings.md` §4, §6): the decomposition sensor sees the parts and is
blind to systemic risk; this one sees systemic risk and is blind to the parts. A divergence between
the two is the signal the diagnostician interprets.

**Designed to survive generations.** It never sees the chain, so it needed no port from `Lytin` to
`Hotyn`; it keeps its `Lytin` stamp inside a `Hotyn` pipeline by design (`PIPELINE.md`, engine
table).

**What arrived unplanned.**
- **The unit became the main event.** Two readings that disagreed by ×1.31 turned out to disagree
  partly about what a person-month *is* — recorded days, attended days, task hours, leave inside or
  outside. Three days went to that before the four-field declaration was made mandatory
  (`docs/constants.md` §5a–5f). Nobody designed the declaration; a fact forced it.
- **The class disagrees with itself more than with the chain.** Three BMS readings on one basis
  spread ×2.12 at P50 while the chain sat inside them (`docs/constants.md` §5g). The sensor was built
  to supply the *other* side of a divergence; its own run-to-run variation became the largest single
  quantity in the comparison.
- **It went unused for three weeks.** The review of 2026-08-21 noted the reference class had not run
  since 2026-08-05 while the project tuned the other sensor. Restoring it was one of the review's
  three recommendations.
- Both SAS readings quarantined the harness's git status on their own and refused to adjust for the
  era gap between a 2018 RFP and 2013–2022 base rates — behaviours the definition never asked for.

## 2. The question it answers

*Where do projects of this class land — in absolute cost and relative to their own early estimates —
and what run of events puts one at each quantile?* Nothing about this project's parts enters the
answer; decomposition is a hard prohibition.

## 3. What the width of its curve means

**Two widths, and they are different things.**
- The width of **one** reading is the heterogeneity of the class: real projects of this kind spread
  this much. That is project risk, the only place in the instrument where it is reported as such,
  and the reason the outside view is today the instrument's sole corridor.
- The distance **between** readings is the uncertainty of the sensor's own act of placing this
  project in a class and choosing its anchors — on SAS, one reading staffed the class from vendor
  patterns (15–30 FTE, 14–24 months) and the other sized it in functional units against ISBSG
  rates, and their medians differ ×1.95 (`run46_reference_class.md`, in `examples/ignored/SAS`, outside the public repository).

Pooling the readings into one curve would erase the second width. The panel draws them separately for
that reason.

## 4. What it sees and what it must never see

`PIPELINE.md` matrix, step 5 (identical in both generations): sees the **project description and the
assumption log**; must never see the model, the work items, the rate table, any bottom-up number,
any target. In practice the orchestrator also **withholds the pipeline's own unit convention and the
obligation counts** — run 36 showed that handing the sensor our unit is worse than handing it none;
it must declare its own.

**Static blind-spot list, given not derived** (`agents/estimator-reference-class.md`): the specifics
of this team; of these integrations; the real difficulty of the particular features; this client;
the dating of the base rates; management interventions that truncate the tail; **misclassification**
— the class itself may be wrong, and the sensor states its confidence split across neighbours.

## 5. Measured properties

| property | value | run |
|---|---|---|
| repeat, P50, one pair | ×1.31 apart, spread narrowing toward the tail: ×1.55 at P10 → ×1.24 at P90 | run 26 (BMS) |
| repeat across three readings on one basis | **×2.12** at P50; class-to-chain gap ×1.05–×2.24 | runs 26, 36 (`constants.md` §5g) |
| repeat on SAS, first `1.1` pair | **×1.95** at P50; raw medians ×1.77 before any conversion; same eight-branch class, same neighbours excluded, same relative anchors — **absolute anchors are where they differ** | run 46 |
| own conversion to task hours, as declared | ×0.65–0.75 and ×0.70–0.80, both containing the house ×0.75 | run 46 |
| skew | P90/P50 ≈ 2.05–2.24; P50/P10 ≈ 1.72–2.11 | run 46 |
| placement of the chain inside the class | BMS: above P90 / ~P84 / ~P53 by reading; FaxRxTx: below the one reading; SAS: P35 / P80 — first time between two medians | runs 26, 36, 46 |

## 6. How to read a reading

- **Read the declaration first.** Unit, whether leave sits inside, whose roles are counted, and how
  far the sensor's own sources disagree. Two readings with different declarations are not yet
  comparable; the orchestrator converts, once, visibly (`docs/constants.md` §5b: recorded or charged
  hours ×0.75 to net task hours).
- The quantiles come **with a scenario each**; the scenario is the reading, the number is its
  summary.
- The **relative anchors** (cone of uncertainty, overrun surveys, the 1-in-6 tail, the winner's
  curse) are shared across readings and stable; the **absolute anchors** are where the level is
  decided and where readings diverge. Ask which kind of anchor set the level before trusting it.
- The sensor's static list is method metadata, not findings of this run; project-specific remarks
  are in a separate part.
- Confidence in the class is stated (60% on SAS) with named neighbours and the direction each would
  move the answer. A narrow class range is a suspicious one.

## 7. Versions

| engine | change | date |
|---|---|---|
| `Lytin-R 1.0` | the definition as first run on BMS, n = 2 | 2026-08-05 |
| `Lytin-R 1.0 → 1.1` | the four-field declaration and the scope boundary, before any figure; "do not adopt this project's convention in place of your own" | 2026-08-26 |

Readings from `.0` are the same instrument with a thinner report.

## 8. What we want to add or change

| idea | would move | where it lives |
|---|---|---|
| **Make the sizing basis an explicit input** rather than the sensor's free choice — the SAS pair split on exactly this (team pattern vs functional-unit size), and it is the dominant source of the ×1.95 | spread between readings (down), level (unknown direction) | not yet in `BACKLOG.md`; raised 2026-09-14 |
| **Era adjustment** for base rates against a dated RFP — today refused by the sensor as blind spot 5's concrete face | level | not yet in `BACKLOG.md` |
| **Is `L-1` a correction for our method, or for corpus-average optimism?** The ×1.735 fitted on FaxRxTx sits close to how much the professional market misses low | interpretation of the diagnosis | `docs/status_2026-08-27.md` §4d |
| **A clean n = 3** on one input — the ×2.12 mixes sensor variance with an input change | spread (measurement) | `docs/constants.md` §5g |
| **A third model family** — both models measured are one vendor, one generation | spread across models | `BACKLOG.md` "Consequences of σ_model" |
