# BMS — Run 14: the baseline, n=10 — the same prompt with no method at all

Date: 2026-08-07. Ten runs of the **pinned prompt** `prompt_decomposition_BMS.txt` (md5 of the git blob
`c33affd709792dfe60531daa3cb42d65`; the working-tree file is CRLF on Windows and hashes differently — the
recorded hash is of the LF form, and the content has not changed since run6) sent to a **general agent with
no method definition**. The only thing removed relative to a sensor batch is the method itself: same words,
same assumption log, same unit, same session, same model, launched simultaneously.

Wrapper added to the pinned text, and it is the only deviation: an instruction to work from the prompt alone
and open no file, plus a request for a compact report ending in `TOTAL: <n> pd`. Neither line says anything
about *how* to estimate. All ten runs reported `tool_uses: 0` — nothing on disk was read, so no run file
from this repository could have anchored them.

**Why this batch exists.** Every version of the decomposition sensor has been judged against earlier versions
of itself. Nothing established what the number would be with no method — so nothing established that the
method was doing the work, rather than the pinned prompt and the assumption log doing it.

## Raw data

| Run | TOTAL | Own declared range | Shape of the answer |
|---|---:|---|---|
| B-1 | 1000 | 800 … 1300 | 13 dev blocks + role uplifts, +15% contingency |
| B-2 | 1050 | 850 … 1350 | 10 dev blocks + role uplifts, +20% |
| B-3 | 1010 | 850 … 1250 | 13 dev blocks + role loading, +20% |
| B-4 | 950 | 800 … 1150 | 11 dev blocks + role loading, +22% |
| B-5 | 1150 | 950 … 1400 | 16-row table + uplifts, +17% |
| B-6 | 1020 | 850 … 1250 | 11 dev blocks + overheads, +20% |
| B-7 | 1200 | — (gave risk deltas instead) | 14 dev blocks + overheads, +10% |
| B-8 | 1150 | 950 … 1400 | 19-row table + role ratios, +15% |
| B-9 | 1200 | 950 … 1600 | 15-row table, scaled by the A3 team ratio |
| B-10 | 1010 | 850 … 1250 | 14 dev blocks + role loading, +20% |

## Baseline against the instrument

| | **run14 — no method** | run13 — `Lytin-D 3.0` |
|---|---:|---:|
| Mean ΣE | **1074.0** | 1673.8 |
| Standard deviation | **91.8** | 181.8 |
| **Coefficient of variation** | **8.55%** | **10.86%** |
| Min … max | 950 … 1200 | 1363 … 1977 |
| max ÷ min | **1.263** | 1.451 |
| Standard error of the batch mean | **2.70%** | 3.44% |
| Line items per run | 10 … 19 | 121 … 203 leaves |

## 1. The method does not narrow the spread. Nothing does, yet

**Baseline CV 8.55%. The instrument, across five measured batches, has never gone below 8.9%.** The `3.0`
batch sits at 10.86% — *above* the baseline.

The difference is not significant and must not be reported as one: the ratio of variances is **1.62** against
a two-tailed 5% critical value of 4.03 at 9 and 9 degrees of freedom, and with n=10 the standard error on a
CV estimate is about ±24% of itself (baseline 8.6% ± 2.0 pp, method 10.9% ± 2.6 pp). The honest statement is
therefore not "the method is worse" but the flatter and more damaging one:

> **After five versions and roughly forty measured runs, the spread of the output is statistically
> indistinguishable from what the model produces with no method at all.**

PIPELINE.md already recorded that "none narrowed the output, because the variance moved to the next unpinned
parameter every time." This batch supplies what that sentence was missing — the level it never narrowed
*below*. The variance has been moving around inside a band whose width was set before the method existed.

## 2. "No method" turned out not to mean "no decomposition"

All ten baseline runs, unprompted, did the same thing: **bottom-up decomposition into 10–19 blocks, then a
role uplift for QA/PM/architect/DevOps, then a contingency percentage.** Nine of ten also volunteered a
range. Nobody guessed, nobody used an analogy, nobody asked for more information.

This changes what the version table has been measuring. `Lytin-D` is not decomposition replacing nothing —
it is **a constrained decomposition replacing the model's default one**, and the default is the same family
of method. The comparison that means something is therefore against this batch, not against zero.

One structural difference is worth naming, because it is not cosmetic. The baseline prices *development*
bottom-up and then multiplies for the other roles (QA ≈ 33–40% of dev, PM/BA ≈ 1 FTE, and so on) — roughly a
×2 uplift applied globally. C2 does the opposite: QA, infrastructure, documentation and migration are
**branches inside the tree**, priced item by item. Same intent, and the two shapes are not comparable
leaf-for-leaf even though both end in person-days.

## 3. The level, and the thing that cannot be settled here

**Mean 1674 against 1074 — the method is ×1.558, +55.8% over the model's default.** That is a real and large
effect, far outside any noise: the two batch means are 10 standard errors apart.

It is also the effect for which this project has no evidence of *direction*. BMS has no `FACT.md`. Whether
+56% is the method finding work the default silently drops (which is what C2 and C3 were built to do), or
the unpacking effect inflating a finer tree, cannot be answered from any batch of runs — only from an
outcome. **Every reproducibility measurement in this repository is silent on this question, and it is the
one that decides whether the instrument is any good.**

## 4. Granularity trades spread against level — and the trade runs the wrong way

The baseline is *coarser* (10–19 items) and *tighter* (CV 8.55%). The instrument is *finer* (121–203 leaves)
and *wider* (10.86%). This is not a paradox: an estimate with fifteen knobs has fewer places to disagree
with itself than one with a hundred and fifty. Coarseness is itself a variance-reduction mechanism, and a
cheap one.

So refinement buys auditability, a named assumption log, instrument readings and a level — and pays for all
of it in spread. Any future version that claims to narrow the output has to beat 8.55%, which a fifteen-line
answer already achieves for free.

## 5. The single run is not the unit of output

Every baseline run declared its own uncertainty, and those declarations are **wider than the batch spread by
about a factor of two**: the mean declared range is 43% of the point estimate (roughly ±21%), against a
p10–p90 of ±11% measured between runs.

That comparison is the most useful thing in this batch. The run-to-run wobble that five versions have been
fighting is a *smaller* quantity than the uncertainty a single run already admits to on its own. And the
batch mean is tighter than either: **standard error 2.70% at the baseline, 3.44% for `3.0`**.

The consequence is a change in what gets reported, not a change to the method:

> **The unit of output is the batch, not the run.** A single run of any version — baseline or instrument —
> carries ±11–14% at p10–p90 and cannot support a commercial decision on its own. The mean of ten carries
> ±3%, and can.

## Open, and what would close it

- **σ_model — measured immediately afterwards, in run15, and it is large.** The same baseline prompt on
  Sonnet 5 gave mean 762.5 and CV 20.92%: the model alone moves the level by −29% (t = 5.35) and widens the
  spread by a factor whose variance ratio, 5.99, is the first significant difference in spread this project
  has found. Two consequences land directly on this file: the ±3% batch standard error of §5 is a property
  of Opus and not of the method, and the +55.8% of §3 is the same order of magnitude as a model swap.
- **BMS has no actual outcome.** FaxRxTx does. Validity work belongs there.
- The baseline totals are round (950 … 1200 in steps of 10–50). Rounding *adds* noise rather than removing
  it, so 8.55% is if anything an overstatement of the baseline spread — which strengthens §1, not weakens it.
