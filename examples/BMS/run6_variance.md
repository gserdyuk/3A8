# BMS — Run 6: repeat-run variance of the decomposition sensor (n = 10)

Date: 2026-08-05. Ten runs of `estimator-decomposition` on byte-identical prompts (the RFP digest +
assumption log), each in a fresh isolated context. BMS was chosen deliberately: it has no recorded
actual outcome, so nothing here can be tuned toward a known answer. Runs 1–5 and 6–10 were launched
as two batches on the same day with no change to the prompt or the agent definition between them.

## Raw data

| Run | ΣE (pd) | Leaves | Σ leaves | Integration | Integration share | pd per leaf |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 894.5 | 75 | 676.0 | 218.5 | 24.4% | 9.0 |
| 2 | 1317.0 | 99 | 1073.7 | 243.0 | 18.5% | 10.8 |
| 3 | 1083.7 | 81 | 798.0 | 285.6 | 26.4% | 9.9 |
| 4 | 1078.0 | 76 | 781.4 | 296.7 | 27.5% | 10.3 |
| 5 | 1242.5 | 80 | 931.0 | 311.5 | 25.1% | 11.6 |
| 6 | 988.0 | 76 | 787.0 | 201.0 | 20.3% | 10.4 |
| 7 | 1283.2 | 89 | 1062.6 | 220.6 | 17.2% | 11.9 |
| 8 | 1164.1 | 73 | 826.6 | 337.5 | 29.0% | 11.3 |
| 9 | 896.6 | 74 | 697.1 | 199.5 | 22.3% | 9.4 |
| 10 | 1525.0 | 80 | 1213.4 | 311.4 | 20.4% | 15.2 |

Sorted totals: 894, 897, 988, 1078, 1084, 1164, 1242, 1283, 1317, 1525.

## Statistics

| Quantity | Value |
|---|---|
| Mean | **1147 pd** |
| Median | 1124 pd |
| Standard deviation | **200 pd** |
| Coefficient of variation | **17.4%** |
| Min … max | 894 … 1525 (max/min = **1.70**) |
| Geometric mean | 1132 pd |
| σ in log space | 0.173 |
| Sample skewness (raw / log) | 0.44 / 0.12 |
| Standard error of the mean | 63 pd → 95% CI ≈ 1023 … 1271 |
| Standard error of the sd | 47 pd (24% in relative terms) |

Batch check: runs 1–5 gave mean 1123, sd 164; runs 6–10 gave mean 1171, sd 248. The two halves are
consistent — no drift between batches, and the wider second half is what a 24% standard error on the
sd looks like in practice.

## What drives the spread

| Component | Mean | Spread |
|---|---|---|
| Number of leaves | 80.3 | CV 10.0% (73 … 99) |
| Price of one leaf | 11.0 pd | CV 15.9% (9.0 … 15.2) |
| Integration share of the total | 23.1% | 17.2% … 29.0% |

**How the spread was attributed — and how it was first attributed wrongly.** The initial write-up
correlated the total against the price per leaf and reported 0.91. That number is an artifact: price
per leaf is the leaf sum divided by the leaf count, the leaf count varies by only 10%, and the total
is the leaf sum plus integration — so the "correlation" was largely the leaf sum against itself. A
ratio correlated with a quantity it is derived from will always look strong; it measures the
construction, not the instrument. (Caught by the project's author, 2026-08-05.)

The honest attribution uses an exact identity instead of a correlation:

> total = (leaf count) × (price per leaf) × (1 + integration ÷ leaf sum)

Three factors, none contained in another. In logs the identity becomes a sum, so the variance of
log(total) splits additively and the shares total exactly 100%:

| Factor | sd in log space | Share of Var(log total) |
|---|---|---|
| Price per leaf | 0.148 | **77.7%** |
| Leaf count | 0.095 | 31.7% |
| Integration factor | 0.052 | −9.4% |

The conclusion survives the correction, but is now derived rather than assumed: **the price attached
to a leaf is the dominant source of run-to-run spread**, leaf count is second, and the integration
factor is a mild *damper* — the negative share means runs with larger leaf sums tended to charge a
smaller integration proportion, partly cancelling their own excess. Leaf count and price move
together in log space (correlation +0.26), so they reinforce rather than offset; note that the
ratio-construction artifact would have biased that correlation *negative*, and it did not.

This is a different statement from the level shift against the July manual run (26 leaves, 18.7 pd
each, 486 pd total): **across specifications** granularity dominates; **within one specification** the
per-leaf price does. Both remain unpinned by the method.

## The level shift (unchanged conclusion, now on n = 10)

All ten runs sit above the July manual estimate of 486 pd; ratios 1.84 … 3.14, mean 2.36. The August
specification is not noisier than the July one so much as it is **systematically larger**, and the
n = 10 sample says the shift is real and not an artifact of the first five draws.

## What n = 10 can and cannot support

**Can:** the mean, to about ±6% (95% CI 1023–1271). The sd, to about ±24%. The statement that
run-to-run spread is ~15–20% and that the extremes differ by a factor of ~1.7.

**Cannot: the shape of the distribution.** Sample skewness is 0.44 raw and 0.12 in log space — both
within what pure noise produces at n = 10, so the data do not distinguish a normal from a lognormal
law. Nor would more runs settle it cheaply: at σ_log ≈ 0.17 the two laws are nearly identical over
the range where the mass sits, and separating them needs a sample in the hundreds. Fitting a "law"
here would be a description of ten draws dressed up as a property of the instrument.

The practically useful targets are cheaper: n ≈ 30 pins the sd to about ±13% and gives usable sample
quantiles; going to n ≈ 50 buys ±10% on the sd and little else.

**And a caveat that no sample size fixes:** this is the variance of one sensor specification on one
case. It does not transfer to another project, and it says nothing about whether the level is right —
BMS has no recorded outcome, which is precisely why it was safe to measure on.

## What this implies for the pipeline

1. **Fix the granularity and the per-leaf pricing convention.** They are the two free parameters, and
   the second one carries most of the within-specification spread (78% of the variance of log total,
   per the decomposition above — not the retracted 0.91 correlation).
2. **Fix the seam rate card as a method constant**, not a per-run invention: integration is 23% of the
   estimate on average and ranges 17–29%.
3. **Then re-measure.** The 17.4% above is the variance of an unconstrained instrument; the number
   worth knowing is what survives after the parameters are pinned.
4. **Report the sensor's reading as a range, not a point.** Whatever the shape of the law, a single run
   of this sensor is a draw from something ~±17% wide, and downstream steps currently treat it as a
   fixed base to multiply.
