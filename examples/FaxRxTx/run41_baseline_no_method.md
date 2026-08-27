# FaxRxTx — Run 41: the baseline, n=10 — the same source with no method at all, against a fact

Date: 2026-08-27. The `run14` experiment (BMS, 2026-08-07) repeated on **the one case that has a
documented outcome**. Ten runs of the pinned prompt `run41_raw/prompt_baseline_faxrxtx.txt` (md5 of
the LF form `c17b874b1101f32f6d8c1ff7a151e7df`) sent to a general agent with **no method definition**,
on `claude-opus-5` — the same model coordinate as runs 29–31, the chain this is compared against.

The prompt is a bare instruction plus `SYSTEM.md` and `assumptions.md` verbatim. Not
`requirements_pinned.md`: extracting that list of 52 obligations **is the method's first act**, and
handing it to the baseline would credit the baseline with work the chain performs.

**Why this batch exists.** `run14` established that on BMS the method does not narrow the spread
below a no-method floor. It could not say anything about *level*, because BMS has no outcome. This
batch asks the question the project had never asked: **the chain lands at ×1.21 of the fact — where
does one prompt with no method land?**

All ten runs reported `tool_uses: 0`. Raw replies: `run41_raw/B-1.md` … `B-10.md`; manifest and
protocol notes: `run41_raw/MANIFEST.md`; arithmetic: `run41_raw/readout.py`.

## Raw data

| Run | TOTAL, A9 pm | own range | team × months | staffed pm |
|---|---:|---|---|---:|
| B-1 | 130 | 90 … 190 | 9 × 18 | 162 |
| B-2 | 90 | 60 … 140 | 7 × 13 | 91 |
| B-3 | 120 | 85 … 175 | 7 × 19 | 133 |
| B-4 | 120 | 85 … 180 | 8 × 15 | 120 |
| B-5 | 120 | 80 … 190 | 8 × 17 | 136 |
| B-6 | 105 | 70 … 160 | 7 × 18 | 126 |
| B-7 | 155 | 110 … 225 | 8 × 22 | 176 |
| B-8 | 120 | 85 … 175 | 8 × 18 | 144 |
| B-9 | 125 | 80 … 200 | 8 × 18 | 144 |
| B-10 | 120 | 80 … 190 | 7 × 19 | 133 |

`A9 pm` = the pinned assumption log's unit, 21 person-days = 168 net hours — **the same unit for all
ten runs**, imposed by the prompt, so the `TOTAL` column needs no conversion to be compared across
runs. `staffed pm` = the run's own `TEAM × DURATION`. It looks like the fact's unit, but it is **not
constant-free**: it is each run's own conversion of its own total, and the runs' private yield
constants differ (B-4 turns 120 pm into 8 × 15 while B-3 turns the same 120 into 7 × 19 — a ×1.11
gap made entirely of the constant). §1 explains why the column must not be used to score against the
chain.

## 1. The result — and it turns on one constant belonging to neither instrument

**Between the ten runs there is no unit problem.** All ten were handed the same definition in the
prompt (A9: 1 pm = 21 person-days = 168 net task hours), all ten reported `TOTAL` in it, and the
spread in §2 is measured inside that one unit with nothing converted.

**The unit problem is between any instrument and the fact.** Both instruments emit **net task
hours**, and in that unit they compare directly, with no constant on either side:

| | net task hours |
|---|---:|
| baseline, mean of 10 (120.5 A9 pm × 168 h) | **20 244** |
| Hotyn chain (1423.2 table pd × 8 h) | **11 386** |
| | baseline = **×1.78** of the chain |

The fact is in neither unit. It is **presence**: ≈10 heads × ≈12 months = 2 291 present days.
Converting presence into net task hours needs one number — what a day of presence yields — and that
number is a property of the **organisation**, not of any instrument:

| net task h per present day | fact, net h | chain | baseline | closer |
|---:|---:|---|---|---|
| 5.0 | 11 455 | **×0.99** | ×1.77 | chain |
| 5.5 | 12 600 | ×0.90 | ×1.61 | chain |
| 6.0 | 13 745 | ×0.83 | ×1.47 | chain |
| **6.63** | 15 189 | ×0.75 | ×1.33 | *equidistant* |
| 7.0 | 16 036 | ×0.71 | ×1.26 | baseline |
| 8.0 | 18 327 | ×0.62 | ×1.10 | baseline |

- This project's own gap-blind measurement — three `Hotyn-K` runs, `docs/constants.md` — puts the
  yield at **5–6 net task hours**.
- The baseline runs, unprompted and unanimously, assumed **≈7**.

**Under this project's declared constant the chain is the closer of the two** — ×1.21 low against the
baseline's ×1.47 high — and at the bottom of the declared band it sits at ×0.99 of the fact. Under
the baseline's own assumption the baseline is closer. The crossover falls at 6.63, between the two
conventions.

> **A single organisational constant decides which instrument is closer, and it moves the answer
> further than the distance between the two instruments does.**

**Settled the same day, by the author's ruling.** The constant is pinned at **6 net task hours per
present day, ×1.10 for leave, 21 days a month** — `docs/constants.md` §4a — for this comparison and
every later one, in place of re-arguing an organisation's behaviour each time a number needs placing
next to a fact. Under it:

| | net task hours | against the fact |
|---|---:|---|
| FaxRxTx fact, 120 staffed pm | **13 745** | — |
| **Hotyn chain** | 11 386 | **×1.21 low** |
| no-method baseline, mean of 10 | 20 244 | **×1.47 high** |

**The chain is the closer of the two, by roughly a factor of two in log distance** (0.082 against
0.168). Under the pinned convention the fact's own ±20% band is 96–144 staffed pm = **10 996 … 16 488 net
task hours**: the chain's 11 386 falls **inside** it, the baseline's 20 244 falls **23% above its top
edge**. What keeps this from being a victory is n = 1, a remembered outcome, and a result that would
have read the other way under a convention the project could equally have adopted.

The ruling is checkable against the fitting rule rather than merely asserted: **6 was measured on
2026-08-25** by three gap-blind `Hotyn-K` runs, before this batch existed, and **within the measured
5–6 band it is the end least favourable to the chain** — at 5 the chain would read ×0.99. A constant
chosen to rescue this result would have been 5.

**Correction to the record, 2026-08-27.** The first reading of this batch reported the baseline at
×1.14 and concluded it beat the chain. That reading took the baseline through **the runs' own**
staffing statements (which embed a ≈7-hour day) while taking the chain through **this project's**
constant (6 hours) — two different constants on the two sides of one comparison. In any single
constant the conclusion does not hold. The ×1.14 figure is withdrawn.

**What survives the correction:** the batch does not establish that the apparatus buys accuracy — one
case, a remembered outcome at ±20%, and a result that would flip under a different declared
convention. What it does establish is that **the conversion between effort and presence had to stop
being an open slot**, and it now is not: `docs/case_profile.md` §2 asks for the yield as a *number*
from case 2 on, with 6 as the standing default.

## 2. The spread, and the one axis where this batch is the project's only measurement

| | n | CV | max ÷ min |
|---|---:|---:|---:|
| BMS baseline, `run14` (a structured RFP) | 10 | 8.55% | 1.263 |
| **FaxRxTx baseline, this batch** (one participant's hedged recollection) | **10** | **13.75%** | **1.722** |
| Hotyn chain, FaxRxTx | 2 | — | 1.033 *(classification repeats on a **fixed** product model)* |

The chain's ×1.033 is not comparable and must stop being quoted as though it were: both repeats were
sized on top of the single product model `HM29-OA1`. The pair's second model, `HM29-OA2` (87 nodes
against 97), was never crossed and never priced.

> **This batch is currently the only end-to-end repeatability measurement the project owns, and it
> belongs to the instrument with no method in it.** Gate v2.0 test 1 asks for ≤ ×1.3 end to end; the
> baseline's max/min is 1.722 and the chain's is unknown. Action 1 of `docs/status_2026-08-27.md` §7
> is what settles this.

That the FaxRxTx spread (13.75%) is wider than the BMS spread (8.55%) is what the inputs predict: a
structured RFP pins more than a recollection carrying "it seems", "probably 20, maybe 16" and two
different date ranges.

## 3. The unit disagreement, found inside single runs

Every run states two things that should be one: a `TOTAL` in A9 person-months and a
`TEAM × DURATION`. Converting between them requires knowing what a working day yields — and the runs
and this project disagree about that constant.

| | net task hours per present day | 1 head-month = |
|---|---|---|
| the runs, self-stated | ≈7 of 8, leave ~10–15% | ≈0.87 A9 pm |
| `docs/constants.md`, three gap-blind `Hotyn-K` runs | **5–6 of 8** | ≈0.68 A9 pm |

That single constant is what §1 shows deciding an instrument comparison, and it moves the corridor
result even harder:

| the fact expressed in A9 pm using… | value | runs whose declared range covers it |
|---|---:|---|
| the runs' own convention | 104.4 | **9 of 10** |
| this project's constant | 81.8 | **5 of 10** |

> The choice of a yield constant nobody in this batch was asked about changes the corridor score from
> a pass to a coin flip. This is the third time the project has found the unit doing more work than
> the estimate, and it is the argument for asking every producer of a number for its staffing in
> heads × months — a statement that carries no constant at all.

## 4. What "no method" turned out to mean, again

All ten runs, unprompted, did the same thing `run14`'s ten did: **decomposition into 11–15 named
components, a role loading for QA and PM, a contingency or bias correction, and a cross-check.**
Nine of ten volunteered a size/productivity cross-check (KLOC per person-month); four named COCOMO II
explicitly and **all four rejected its number as miscalibrated for a small product company**, keeping
it only as evidence that the upper tail is fat.

This confirms `run14`'s finding on a second case and sharpens it. The chain is not decomposition
replacing nothing. It is **a constrained decomposition replacing the corpus's default one, and the
default is the same family of method** — which is exactly what the 2026-08-27 goal statement predicts,
and exactly why the goal claims speed, repeatability and correctability rather than better judgement.

Every run also converged on the same cost driver without being told: the hand-rolled watchdog/token
orchestrator, priced at 15–24 pm, the single largest line in nine of ten decompositions.

## 5. Protocol — the injection, caught 10 times out of 10

Every run reported ambient repository material reaching it unbidden: git branch, status, and **recent
commit subjects naming this very case** ("run 40", "Hotyn-P counts FaxRxTx twice", "UFP 78 vs 82",
"the enumeration floor"). Several said outright that these looked like leaked prior results for the
object under estimate.

No effort figure is in those subjects — the leaked numbers are function-point counts, which cannot
anchor a person-month estimate — so the batch stands. But this is the **sixth** independent catch,
and the standing item to strip `gitStatus` from sensor launches has stopped being tidiness: one commit
subject worded differently would put a person-month figure into a blind run.

## 6. What this changes

- **`docs/status_2026-08-27.md` §5's last bullet is now answered** and the answer is unfavourable.
  The apparatus's value proposition cannot rest on accuracy; on the evidence available it must rest
  on repeatability, auditability and correctability — which is what the 2026-08-27 goal already says,
  and this batch is the first hard evidence that the goal was reframed in the right direction.
- **What the chain still has and the baseline does not**, and it is not nothing: a named-hole list, a
  scope-decision fork that can be re-priced without re-estimating, an auditable trail from obligation
  to price, and a pinned table that makes the level correctable by one constant. The baseline
  produces a number and a paragraph, and there is nothing in it to calibrate.
- **Action 1 is now the load-bearing measurement of the project.** Accuracy at n=1 is undecidable
  here (§1); repeatability is not, and it needs no constant at all. If the chain's end-to-end spread
  comes in under the baseline's max/min of 1.722, the apparatus has bought the thing the goal actually
  claims. If it comes in above, the apparatus has bought nothing measurable at all.
- **The presence-yield constant is promoted to a case-profile field that must be pinned.** §1 shows it
  deciding the outcome of an instrument comparison. It is already implied by `docs/case_profile.md` §2
  ("what a booked day contains"), but it was never asked as a number. It must be, from case 2 on.
