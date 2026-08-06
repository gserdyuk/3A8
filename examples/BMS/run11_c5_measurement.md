# BMS — Run 11: the C5 measurement (raw data, n=10)

Date: 2026-08-06. Engine `Lytin-D 2.0` (C5 present; the activity-branch scope statement of `2.1` was **not**
in the loaded definition — see below). Prompt `prompt_decomposition_BMS.txt`, md5
`c33affd709792dfe60531daa3cb42d65`, byte-identical to run6, run7, run8, run9 and run10.

All ten runs are from **one session**. V-1 and V-2 are the pilot pair recorded in run10; the remaining eight
were relaunched into the same session after a token top-up, deliberately, so that they pool with the pair
rather than confounding with the ~10% session effect measured in run9. Residual confound: time passed
between the pair and the eight. Within-session drift has never been measured, so it is not zero — but it is
smaller than the cross-session alternative.

## Raw data

| Run | ΣE | Modules | Leaves | Σ leaf E | Integration | Int. share | Nodes | Fallback | M in >10 | Stamp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| V-1 | 1404.5 | 21 | 133 | 920.5 | 484.0 | 34.5% | 29 | 0 | 0 | Lytin-D 2.0 |
| V-2 | 1666.8 | 25 | 148 | 1060.3 | 606.5 | 36.4% | 34 | 0 | 0 | Lytin-D 2.0 |
| V-3 | 1353.0 | 27 | 144 | 1026.0 | 327.0 | 24.2% | 11 | 0 | 0 | Lytin-D 2.0 |
| V-4 | 1477.0 | 19 | 142 | 967.5 | 509.5 | 34.5% | 31 | 0 | 0 | Lytin-D 2.0 |
| V-5 | 1416.1 | 20 | 133 | 978.6 | 437.5 | 30.9% | 33 | 0 | 0 | Lytin-D 2.0 |
| V-6 | 1664.1 | 23 | 144 | 1200.1 | 464.0 | 27.9% | 33 | 0 | 0 | Lytin-D 2.0 |
| V-7 | 1536.1 | 20 | 137 | 1023.6 | 512.5 | 33.4% | 30 | 0 | 0 | Lytin-D 2.0 |
| V-8 | 1330.0 | 21 | 128 | 917.0 | 413.0 | 31.1% | 28 | 0 | 0 | Lytin-D 2.0 |
| V-9 | 1477.3 | 21 | 130 | 1016.3 | 461.0 | 31.2% | 26 | 0 | 0 | Lytin-D 2.0 |
| V-10 | 1850.7 | 20 | 159 | 1135.2 | 715.5 | 38.7% | 31 | 0 | 0 | Lytin-D 2.0 |

## The four measurements of this instrument

| | run7 — 1.0, same session | run9 — 1.0, other session | run8 — 1.0, table off | **run11 — 2.0 (C5)** |
|---|---:|---:|---:|---:|
| Mean ΣE | 1284 | 1410 | 1715 | **1518** |
| Standard deviation | 114 | 141 | 135 | **164** |
| **Coefficient of variation** | **8.9%** | **10.0%** | **7.8%** | **10.8%** |
| Min … max | 1125 … 1436 | 1196 … 1608 | 1481 … 1908 | 1330 … 1851 |
| max / min | 1.28 | 1.35 | 1.29 | **1.39** |
| Leaf count (mean, CV) | 125 | 133 (8.7%) | 164 | **139.8 (6.8%)** |
| Price per leaf (mean, CV) | 6.80 (8.0%) | 7.32 | 7.17 (2.0%) | **7.33 (6.2%)** |
| Integration share | 34.0% | 30.6% | 31.4% | **32.3%** |
| **Aggregation nodes (mean, CV)** | 19.0 (36.7%) | 16.7 (44.1%) | 23.7 (42.0%) | **28.6 (23.3%)** |
| Modules | — | — | — | **21.7 (11.7%)** |

## What C5 did: the node-count parameter is closed

**This is the result the change was made for, and it landed.**

- Node-count CV: **44.1% → 23.3%**. Excluding the single outlier V-3 (11 nodes, see below), **8.5%** across
  the other nine. Pre-registered prediction 1 — "node count spread collapses" — is confirmed, and by more
  than the headline figure suggests.
- **corr(nodes, Σ integration) = 0.61**, down from 0.90 (run8) and 0.83 (run9). Excluding V-3: **0.33**.
  The mechanism that made node count a lever on the total is broken: the count is now largely determined by
  the module list, and the module list is derived rather than chosen.
- **corr(modules, ΣE) = −0.07.** Module count varies 19…27 but does not drive the level at all. That is the
  right shape for a derived quantity: runs disagree about how finely to name modules, and it costs nothing.

Compare what node count used to be: run8 called it "a free parameter of the same kind as the leaf ceiling
was before C1, and now the second-largest contributor to the spread". It is no longer that.

## What C5 did not do: the total spread did not improve

CV **10.8%** against 8.9% (run7) and 10.0% (run9). The variance ratio against run7 is 2.08, inside what an
F-test on 10 versus 10 cannot distinguish from 1 — so this is *not* evidence that C5 made the instrument
worse. But it is also not the improvement the change was aimed at, and it must be said plainly: **pinning
the middle of the tree closed one free parameter without narrowing the output.**

The variance moved rather than disappeared. This is now the third time:

| Factor | run7 | run8 | run9 | **run11** |
|---|---:|---:|---:|---:|
| Leaf count | 30.7% | 62.2% | 76.7% | **50.7%** |
| Price per leaf | 61.5% | 3.9% | 16.3% | **15.4%** |
| Integration factor | 7.8% | 33.9% | 7.1% | **34.0%** |

(Exact log-variance decomposition on **total = leaf count × price per leaf × (1 + integration/leaf sum)**;
shares by covariance attribution, summing to 100.1% with rounding. sd of ln(total) = 0.105, consistent with
the arithmetic CV.)

Leaf count came *down* from 76.7% to 50.7% and its own CV narrowed 8.7% → 6.8% — pre-registered
prediction 4, "leaf-count spread narrows somewhat", confirmed. But the integration factor went back up to
34.0%, and this time it is **not** riding on node count. With corr(nodes, integration) at 0.33 among the
nine consistent runs, the remaining integration spread comes from **which seams a run counts and how it
classifies them** — plain call vs shared data vs shared workflow — not from how many nodes it builds. C3
prices a seam; nothing pins what counts as a seam or which of the three kinds it is.

That is the next unpinned parameter, and it is a different one from the one C3 v2 was drafted to fix.

## Level

Mean 1518 against run9's 1410: **+7.7%, 1.6 standard errors of the difference.** Not distinguishable from
noise, and in any case below the ~10% session effect that run9 could not resolve. Against run7's 1284 it is
+18.2% (3.7 se), but run7 is a different session and the confound is unbounded in that comparison.

**Honest reading: C5 did not measurably move the level, and this instrument cannot say whether it moved it
by less than ~10%.** No prediction was registered on level before this batch — I had missed twice on
direction and said so — so there is nothing to score. The draft proposal's prediction 3 ("total level falls")
belongs to C3 v2, which was not applied.

## The V-3 anomaly is a readout defect, not a tree defect

V-3 reports **27 modules and 11 nodes**. Under C5 a node exists per module, per branch, plus the top-level
assembly, so 27 modules cannot coexist with 11 nodes. 11 is exactly 10 branches + 1 assembly: V-3 counted
only branch-level node items and omitted the module nodes from its §6 reading. Its integration total (327,
the lowest in the batch) is consistent with having *priced* fewer nodes, so the omission may be real work
skipped rather than a pure reporting slip — the report alone cannot distinguish the two.

The same value 11 appeared four times in run9 (R-3, R-7, R-8, R-10), which suggests this is a recurring
convention collision, not a one-off.

**Cause: §6 asks for "node items" without saying what counts as one.** Before C5 the ambiguity was invisible
because runs invented their own node structure anyway. C5 made the structure derivable, and the readout
ambiguity became measurable — as a single point at 11 dragging a CV from 8.5% to 23.3%.

**Fix owed:** §6 must state that the node count is *module nodes + branch nodes + the top-level assembly
node*, counted separately if that helps. This is a reporting change, not a constant change — a **minor**
version by the engine convention, and it should not move the level.

## C5's scope statement is confirmed as necessary, not merely redundant

`Lytin-D 2.1` added the rule that branches 1, 7, 8, 9 and 10 carry no modules. The runs here ran on `2.0`,
without it, so this batch tests whether the rule codifies universal behaviour or forbids real divergence:

- **Nine of ten** left all five activity branches flat, and several stated the reasoning unprompted in almost
  the same words ("serves every function rather than implementing any").
- **V-9 did not**: it derived `M-CUTOVER-DATA` as a module of branch 9 and reported 21 modules including it.

So the rule was not redundant. One run in ten diverged, and `2.1` closes it. That is the intended kind of
change: codify what the instrument mostly does, and remove the residual freedom.

## A second C5 gap this batch exposed, still open

Cross-cutting *technical* foundations — persistence, caching, background jobs, API contracts, audit — serve
every function and are named by none. C5 derives modules from functions, so the rule has no clean answer for
them, and the runs split three ways:

- **V-10** derived them as a module (`M20 Platform Foundation`) under rule 2, on the grounds that a capability
  used by essentially every function is exactly what rule 2 describes. It flagged the derivation as unusual.
- **V-8** did the same (`M0 Platform base`).
- **V-7** put three such leaves (persistence, async jobs, performance foundation) **directly under branch 2**,
  stating explicitly that they "correspond to no derived module" and that it refused to invent an
  intermediate level for them.

All three are defensible readings of the same rule, and they produce different trees. This is the same class
of defect as the activity-branch gap, found the same way: by three independent runs disagreeing in the open.
It is not fixed by `2.1`, and it should be the subject of its own minor amendment to C5 — not folded into
the C3 change.

## Compliance

Across all ten runs, without exception: no leaf with M > 10 (the `>10` bucket empty everywhere, no C1
exception claimed); no leaf below 1 pd; no merging; **zero** of the ~290 node items fell back to the 15%
rule; all ten branches filled in every run; all ten stamped `Lytin-D 2.0`; every run printed the
function → module map and stated whether the source fixes an architecture (all ten: it does not).

The rule-following half of the instrument remains solid, as in every previous measurement. That is worth
restating each time, because it is what makes the quantitative findings interpretable: the spread is not
sloppiness, it is genuine freedom left by the constants.

## Status and what is owed

1. **`Lytin-D 2.1`** is on disk and loads next session. This batch measured `2.0`; the difference between
   them is the activity-branch scope statement, which nine of ten runs already obeyed.
2. **§6 amended — done, `Lytin-D 2.2`.** Node items are now reported as three numbers (module nodes, branch
   nodes, top-level assembly), which closes the V-3 ambiguity; and a **seam mix by C3 kind** was added,
   because nothing in the current output lets the integration residual be split between *how many seams a
   run finds* and *which of the three kinds it calls them*. Only V-6 printed a mix (plain 24, data 61,
   workflow 20), and one run is not a measurement. Reporting-only change, so minor by convention — but
   run8's finding that output format alone moved the level by 33% means the next batch must be treated as a
   new baseline rather than assumed comparable.
3. **No amendment to C5 for cross-cutting technical foundations — deliberately.** The three-way divergence
   (V-10 and V-8 derived a foundation module under rule 2; V-7 hung the leaves directly on branch 2 and
   said explicitly that they correspond to no derived module) does not predict the total: V-10 and V-8 are
   the batch maximum and minimum and made the *same* choice. Legislating now would pin a parameter never
   shown to be harmful — the same error as the retracted "nesting charges more" mechanism. The choice is
   already visible in the function → module map that every run prints, so it can be classified from
   existing output with no change to the instrument and no risk of making the fork salient. Revisit when a
   later batch either shows a correlation with the total or confirms there is none.
4. **C3 v2** (incremental joins, k−1 per node) is still drafted and unapplied in
   `docs/proposal_C3v2_and_structure.md`. Its pre-registered predictions 2, 3 and 5 remain untested.
   Note that this batch changes what C3 v2 is *for*: it was written against node count, and node count is
   now closed. The integration spread it must now address is seam **identification and classification**,
   which the current draft does not touch.
5. **Leaf count** remains the largest single term (50.7%). C1 fixes the ceiling on a leaf and C5 fixes which
   parts exist; how finely a run splits *inside* a named part is still open.

## Note on comparability

Node counts under `2.0` are **not** comparable to pre-C5 node counts, and the run7/run8/run9 rows in the
table above are retained only to show the direction of change. Module count is a new reading with no
baseline. Level comparisons across these four measurements are bounded by the unresolved ~10% session
effect and by run8's finding that the output format alone moves the level by 33%.
