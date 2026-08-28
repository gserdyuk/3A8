# FaxRxTx — Run 43: the no-method baseline run a second time, and what the first batch was hiding

Date: 2026-08-28. Ten more runs of the **identical** pinned prompt of run 41
(`run41_raw/prompt_baseline_faxrxtx.txt`, md5 `c17b874b1101f32f6d8c1ff7a151e7df`), same model
`claude-opus-5`, `tool_uses: 0` in every one, launched a day later.

**Why.** The author, reading the three-curve chart: *"the meaning of the first two curves is clear;
the meaning of this one — not yet, but I suspect it is volatile."* Run 41 measured the instrument
once. A second batch measures whether **the measurement itself** reproduces.

**Control on the input.** Both batches quarantined the same injected material — the session-start git
snapshot, whose commit subjects name runs 38–40 and "UFP 78 vs 82". Batch 2's runs cite exactly those
same subjects, not the run 41/42 commits made in between, confirming the injection is identical across
batches and cannot explain any difference.

---

## 1. The two batches

| | n | mean | median | sd | CV | min … max |
|---|---:|---:|---:|---:|---:|---|
| batch 1, run 41 | 10 | 120.5 | 120.0 | 16.6 | 13.75% | 90 … 155 |
| **batch 2, run 43** | 10 | **138.0** | 137.5 | 18.6 | 13.47% | 110 … 165 |
| pooled | 20 | 129.2 | 122.5 | 19.3 | 14.97% | 90 … 165 |

All figures in A9 person-months. Batch 2 runs: 120 · 160 · 150 · 150 · 145 · 165 · 130 · 120 · 110 · 130.

> ### The level moved ×1.145 between batches
> Difference of means 17.5 pm, standard error 7.9, **t = 2.22 on 18 df, p ≈ 0.04**. Same prompt, same
> model, same injected context, a day apart. **The shift is larger than sampling noise accounts for.**

And the within-batch spread barely moved — 13.75% against 13.47%. **Each batch, looked at alone,
reports a well-behaved instrument.** That is precisely the trap: the number a single batch produces
for its own stability is silent about the thing that actually moves.

Pooled max/min is **×1.83**, against ×1.72 and ×1.50 for the batches taken separately.

---

## 2. The finding, and it is the one that matters

Every run declares its own P10–P90 corridor. Fitting each run's declared range as a lognormal, in
table person-days (1 A9 pm = 168 net task hours = 21 table pd — **no presence constant enters**):

| | |
|---|---|
| spread of the twenty runs' medians | **×1.85** (1 942 … 3 600 pd) |
| each run's **own** declared P10–P90 corridor | **×1.51** on average (×1.44 … ×1.59) |

> **The instrument's run-to-run instability is wider than the uncertainty it declares.** Every single
> run states a corridor narrower than the distance between it and its neighbours. Twenty estimators
> who each say "I am confident to within ×1.5" and who disagree with each other by ×1.85.

That is not a wide instrument. It is a **confident** instrument that is wrong about its own precision.

---

## 3. Against the documented outcome

The fact is 1 718 table pd (120 staffed person-months under the pinned conversion,
`docs/constants.md` §4a).

| | |
|---|---|
| runs whose **median** sits above the fact | **20 of 20** |
| runs whose own **P10** reaches down to the fact | **1 of 20** |
| median across the runs of P(≤ fact) | **0.003** |
| range of P(≤ fact) | 0.000 … 0.234 |

For comparison on the same axis: **the chain puts the fact at P89, the reference class at P39.**

Twenty independent draws, not one of them centred below the outcome, and nineteen of twenty declaring
a corridor that does not reach it. The bias is not a property of one unlucky batch.

---

## 4. What this settles

**On the earlier reading of run 41.** That batch's mean of 120.5 pm, converted, gave ×1.47 against the
fact. It was treated as *the* baseline level. It was one draw from a distribution whose level moves;
batch 2's ×1.68 is an equally valid draw. **The honest statement of the no-method level is not a
number but a band**, and the band is wide enough that the ×1.47 figure quoted in
`run41_baseline_no_method.md` §1 should be read as one sample, not as the instrument's level.

**On the chart.** Drawing the no-method instrument as a *single* curve — as the first three-curve
example did — asserts a stability the instrument does not have. **Twenty thin curves is the honest
drawing.** The family is the finding; the pooled curve was a summary of one batch that concealed it.

**On what the third curve means**, which is the question that prompted this run: it means *this is
where a fast, unstructured answer lands, and how far it moves when you ask again.* The first two
curves answer once each. The third only has a meaning in the plural.

**On the comparison with the chain.** Run 42 measured the chain end to end at **×1.05** between two
product models. The no-method instrument moves **×1.145 in level between batches** and **×1.85 across
runs**, while declaring ×1.51. On repeatability — the one axis needing no fact and no constant — the
gap between the two instruments is now measured on both sides and is not close.

---

## 5. What it does not settle

- **Two batches is n = 2 on the level.** The shift is significant against within-batch noise; whether
  ×1.145 is typical, small or large for this instrument would need a third and fourth batch.
- **The chain has been measured across models, not across days.** Run 42's ×1.05 is two product models
  in one session. Whether the chain's level also drifts between sessions is **unmeasured**, and the
  symmetric experiment — re-run the whole chain a day later on the same pinned model — has not been
  done. It is the obvious next control, and until it exists the comparison in §4 is between a
  cross-model figure and a cross-batch one.
- The fact remains one remembered outcome at ±20%.

Raw: `run43_raw/ranges.json` (all twenty declared low/mode/high), `run43_raw/curves_pd.json` (the
fitted per-run curves). The twenty-curve chart was built from a scratch copy of `tools/report/` and
the production report was not modified.
