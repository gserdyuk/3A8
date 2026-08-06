# BMS — Run 9: cross-session replication of Lytin-D 1.0 (raw data)

Date: 2026-08-06. Ten runs, engine `Lytin-D 1.0`, prompt `prompt_decomposition_BMS.txt`
(md5 `c33affd709792dfe60531daa3cb42d65`) — byte-identical to run6, run7 and run8.

## How this measurement came about

These runs were launched as the test of **C5** (modules derived from functions). They are not that test.
The definition file had been edited to `Lytin-D 2.0` with C5 added **before** the launch, but every returned
report stamps `Lytin-D 1.0`, contains no function→module map, and independently flags the `Kosiv 1.0`
defect in output §6 — a defect that had already been fixed on disk. The agents therefore ran the
**pre-edit** definition.

**Established by direct test: agent definitions are read once at session start and edits made during a
session do not take effect.** The earlier belief to the contrary (recorded in run7 and retracted there) is
now falsified in the other direction: the original rule was right. The run7 retraction was correct about
the *mechanism* of the `Kosiv` stamps (a stale literal in the §6 template) but wrong to conclude that
modified definitions are picked up mid-session.

**Rule, stronger than the previous one:** an instrument may only be edited **between sessions**. Editing it
mid-measurement is not merely bad discipline — the edit has no effect at all until restart, so the
measurement silently tests the old version.

What the runs do provide is something the project did not have: a **cross-session** repeatability
measurement of `Lytin-D 1.0` against run7's **within-session** one, on identical input.

## Raw data

| Run | ΣE | Leaves | Σ leaf E | Integration | Int. share | Nodes | Fallback nodes | M in >10 | Stamp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R-1 | 1608.5 | 148 | 1154.5 | 454.0 | 28.2% | 19 | 0 | 0 | Lytin-D 1.0 |
| R-2 | 1511.1 | 136 | 931.1 | 580.0 | 38.4% | 34 | 0 | 0 | Lytin-D 1.0 |
| R-3 | 1361.7 | 126 | 888.2 | 473.5 | 34.8% | 11 | 0 | 0 | Lytin-D 1.0 |
| R-4 | 1548.5 | 141 | 1072.4 | 476.0 | 30.7% | 20 | 0 | 0 | Lytin-D 1.0 |
| R-5 | 1556.6 | 139 | 1038.6 | 518.0 | 33.3% | 22 | 0 | 0 | Lytin-D 1.0 |
| R-6 | 1301.8 | 130 | 894.8 | 407.0 | 31.3% | 14 | 0 | 0 | Lytin-D 1.0 |
| R-7 | 1423.9 | 148 | 1103.4 | 320.5 | 22.5% | 11 | 0 | 0 | Lytin-D 1.0 |
| R-8 | 1334.1 | 133 | 1011.6 | 322.5 | 24.2% | 11 | 0 | 0 | Lytin-D 1.0 |
| R-9 | 1195.5 | 111 | 830.5 | 365.0 | 30.5% | 14 | 0 | 0 | Lytin-D 1.0 |
| R-10 | 1262.5 | 122 | 855.5 | 407.0 | 32.2% | 11 | 0 | 0 | Lytin-D 1.0 |

## The three measurements of this instrument so far

| | run7 — same session | run9 — different session | run8 — table suppressed |
|---|---:|---:|---:|
| Engine | Lytin-D 1.0 | Lytin-D 1.0 | Lytin-D 1.0 |
| Mean ΣE | 1284 | **1410** | 1715 |
| Standard deviation | 114 | 141 | 135 |
| **Coefficient of variation** | **8.9%** | **10.0%** | 7.8% |
| Min … max | 1125 … 1436 | 1196 … 1608 | 1481 … 1908 |
| max / min | 1.28 | 1.35 | 1.29 |
| Leaf count | 125 | 133 | 164 |
| Price per leaf | 6.8 pd | 7.32 pd | 7.17 pd |
| Integration share | 34.0% | 30.6% | 31.4% |
| Aggregation nodes (CV) | 19.0 (36.7%) | 16.7 (44.1%) | 23.7 (42.0%) |

### Repeatability across sessions holds, within the instrument's own resolution

**Spread is not demonstrably wider across sessions.** CV 10.0% against 8.9%; the ratio of variances is
1.52, well inside what an F-test on n=10 versus n=10 cannot distinguish from 1. The instrument repeats
across sessions about as well as it repeats inside one.

**Level differs by +9.8% (1284 → 1410), which is 2.2 standard errors.** This sits exactly on the
resolution limit stated after run7 — that comparison of two ten-run batches can distinguish a level
difference of roughly 8% or more. So the honest reading is: *either* there is a real session-to-session
level effect of about 10%, *or* this is noise, and n=10 cannot separate the two. Resolving it would take
roughly forty runs per condition (resolution improves as the square root of the sample).

This matters for the regression set. If a ~10% session effect is real, then two cases measured in
different sessions are not directly comparable, and the regression protocol must either run a whole set
inside one session or carry a per-session control.

## Where the variance sits now

Exact log-variance decomposition on **total = leaf count × price per leaf × (1 + integration/leaf sum)**:

| Factor | run7 | run8 | **run9** |
|---|---:|---:|---:|
| Leaf count | 30.7% | 62.2% | **76.7%** |
| Price per leaf | 61.5% | 3.9% | **16.3%** |
| Integration factor | 7.8% | 33.9% | **7.1%** |

**Leaf count is now the dominant term in both post-C1 measurements.** C1 fixed the price of a leaf; what it
did not fix is how many leaves a tree has, and that is where the spread went. Leaf counts here range
111 … 148 on identical input.

## The node-count finding replicates

Independently of run8, and on the pre-C5 definition:

- Node count 11 … 34, **CV 44.1%** — again the widest-swinging reading in the instrument.
- corr(nodes, Σ integration) = **0.83** (run8: 0.90).
- corr(leaf count, total) = 0.85.

Two separate ten-run measurements now agree that the number of aggregation nodes is a free parameter of
the same kind the leaf ceiling was before C1. This is the defect C3 v2 is written to remove.

**Run R-5 reached the same conclusion from inside an isolated run**, without seeing any of this analysis.
Its method log states that it fixed the node-creation rule and the O/P uncertainty classes before pricing,
and adds that they "should be pinned into the method constants if this sensor's variance is to be tracked
across runs — they are exactly the kind of free parameter the constants exist to remove."

## Compliance

Across all ten runs: no leaf with M > 10, no leaf below 1 pd, no merging, **zero** of the ~167 node items
fell back to the 15% rule, all ten branches filled in every run, all ten stamped `Lytin-D 1.0`, and all ten
independently reported the `Kosiv 1.0` template defect. The rule-following half of the instrument remains
solid across sessions.

## Status

- This measurement does **not** test C5. That test still requires a session restart; the definition is on
  disk as `Lytin-D 2.0` and will load on the next session start.
- The C3 v2 text (incremental joins, k−1 per node, no pairwise enumeration) is drafted in
  `docs/proposal_C3v2_and_structure.md` and not yet applied.
