# BMS — Run 12: the seam-mix measurement (raw data, n=10)

Date: 2026-08-06. Engine `Lytin-D 2.3`. Prompt `prompt_decomposition_BMS.txt`, md5
`c33affd709792dfe60531daa3cb42d65` — byte-identical to run6 … run11. Ten runs, one session, launched
simultaneously.

`2.3` changes **reporting only**: §6 now reports node items in three parts (module / branch / top-level
assembly) and adds the seam mix by C3 kind. No constant changed. The batch is therefore both a control on
`2.0` and the first measurement able to say where the integration spread actually lives.

Session protocol: definitions were confirmed loaded by the version probe (`Lytin-F 2.3`) **before** launch.
The probe was *edited*, not created, so its answer proves the harness re-reads modified files — the exact
question a freshly created probe cannot settle. See `PIPELINE.md`.

## Raw data

| Run | ΣE | Mod. | Leaves | Σ leaf E | Integr. | Share | Nodes M/B/T | Inner seams p/d/w | Top seams p/d/w | Top pd | Fallback | M>10 |
|---|---:|---:|---:|---:|---:|---:|---|---|---|---:|---:|---:|
| W-1 | 1549.5 | 22 | 120 | 956.5 | 593.0 | 38.3% | 22/10/1 = 33 | 22/71/39 = 132 | 2/11/8 = 21 | 152.0 | 0 | 0 |
| W-2 | 1690.7 | 20 | 152 | 1080.2 | 610.5 | 36.1% | 20/10/1 = 31 | 27/77/43 = 147 | 2/8/7 = 17 | 124.0 | 0 | 0 |
| W-3 | 1436.2 | 19 | 121 | 922.2 | 514.0 | 35.8% | 19/10/1 = 30 | 20/72/35 = 127 | 1/5/6 = 12 | 93.0 | 0 | 0 |
| W-4 | 1710.4 | 21 | 154 | 1130.4 | 580.0 | 33.9% | 21/10/1 = 32 | 44/79/34 = 157 | 3/8/5 = 16 | 107.0 | 0 | 0 |
| W-5 | 1898.7 | 27 | 172 | 1298.2 | 600.5 | 31.6% | 27/10/1 = 38 | 45/84/36 = 165 | 3/7/5 = 15 | 101.0 | 0 | 0 |
| W-6 | 1557.4 | 23 | 149 | 1111.9 | 445.5 | 28.6% | 23/10/1 = 34 | 25/77/19 = 121 | 2/6/4 = 12 | 82.0 | 0 | 0 |
| W-7 | 1449.4 | 28 | 133 | 1011.4 | 438.0 | 30.2% | 25/10/1 = 36 | 10/70/28 = 108 | 3/4/4 = 11 | 73.0 | 0 | 0 |
| W-8 | 1754.5 | 26 | 154 | 1103.5 | 651.0 | 37.1% | 23/10/1 = 34 | 42/85/46 = 173 | 1/5/7 = 13 | 103.0 | 0 | 0 |
| W-9 | 1879.0 | 27 | 179 | 1334.5 | 544.5 | 29.0% | 27/10/1 = 38 | 37/87/29 = 153 | 3/4/5 = 12 | 83.0 | 0 | 0 |
| W-10 | 1756.3 | 24 | 153 | 1184.8 | 571.5 | 32.5% | 24/10/1 = 35 | 13/85/39 = 137 | 2/6/6 = 14 | 102.0 | 0 | 0 |

## The four measurements of this instrument

| | run7 — 1.0 same session | run9 — 1.0 other session | run11 — 2.0 (C5) | **run12 — 2.3** |
|---|---:|---:|---:|---:|
| Mean ΣE | 1284 | 1410 | 1518 | **1668** |
| Standard deviation | 114 | 141 | 164 | **164** |
| **Coefficient of variation** | **8.9%** | **10.0%** | **10.8%** | **9.85%** |
| Min … max | 1125 … 1436 | 1196 … 1608 | 1330 … 1851 | 1436 … 1899 |
| max / min | 1.28 | 1.35 | 1.39 | **1.32** |
| Leaf count (mean, CV) | 125 | 133 (8.7%) | 139.8 (6.8%) | **148.7 (13.0%)** |
| Price per leaf (mean, CV) | 6.80 (8.0%) | 7.32 | 7.33 (6.2%) | **7.50 (3.5%)** |
| Integration share | 34.0% | 30.6% | 32.3% | **33.3%** |
| **Aggregation nodes (mean, CV)** | 19.0 (36.7%) | 16.7 (44.1%) | 28.6 (23.3%) | **34.1 (8.0%)** |
| Modules (mean, CV) | — | — | 21.7 (11.7%) | **23.7 (13.5%)** |

## 1. The node-count parameter is now closed, and run11 overstated its residual

Node-count CV: **44.1% → 23.3% → 8.0%**. The middle figure was inflated by the readout ambiguity `2.3`
fixes: one run in the `2.0` batch reported 27 modules alongside 11 nodes, because §6 did not say what a
node item was. With the definition stated, the count decomposes as it should:

- **branch nodes: exactly 10 in all ten runs;**
- **top-level assembly: exactly 1 in all ten runs;**
- module nodes: 19 … 27, tracking the module list.

**corr(nodes, Σ integration) = −0.10.** It was 0.90 before C5 and 0.61 in the `2.0` batch. The mechanism by
which node count was a lever on the total is not weakened — it is gone. Node count is now a derived
quantity, and its remaining variation is the variation of the module list.

## 2. Where the integration spread actually lives — and a correction

**It is the seam *count*, not the seam *classification*.** This reverses the reading I was forming while the
batch arrived, and the arithmetic is unambiguous.

Split the inner-node integration exactly: `inner pd = inner seams × price per inner seam`.

| Quantity | Mean | CV |
|---|---:|---:|
| Inner seams | 142.0 | **14.5%** |
| Price per inner seam | 3.200 pd | **5.4%** |

Log-variance decomposition of inner integration cost:

| Factor | Share of Var(ln inner pd) |
|---|---:|
| **Seam count** | **105.1%** |
| Price per seam (i.e. the classification mix) | −5.1% |

The negative share means classification does not add to the spread; it very slightly *damps* it. Runs that
find more seams tend to call them marginally cheaper, cancelling a little of their own effect.

Corroborating correlations: **corr(inner seams, Σ integration) = 0.85**, and
**corr(shared-workflow count, Σ integration) = 0.88** — but the workflow count is itself mostly a function
of the total seam count, which is why price per seam stays near 3.2 pd across runs whose workflow share
ranges from 16% to 27%.

The same pattern holds at the top-level assembly node: seam count 11 … 21 (CV ≈ 20%), price per seam
6.6 … 7.9 pd (CV ≈ 6%).

**Why I read it wrong while the runs arrived.** I was comparing raw class counts between runs of different
sizes, so a run with fewer seams overall looked like a run that classified them cheaply. Dividing by the
seam count removes the illusion. The lesson is procedural, not conceptual: ratios, not counts, when the
denominators differ.

## 3. Consequence for the C3 v2 draft

`docs/proposal_C3v2_and_structure.md` prices a node at **k − 1** joining operations instead of enumerated
pairs. Its stated motivation — node count carrying a third of the spread — is dead, killed by C5. But this
measurement resurrects the draft on better grounds than it was written on: **k − 1 pins the seam count**,
and the seam count is now demonstrably the whole of the integration spread.

What the draft still does not address, and what should be checked before it is applied: whether k − 1
actually binds. Observed inner seams per node run 3.2 … 5.1 with children counts in the same range, so the
runs are already near k − 1 by instinct. If the rule merely writes down what they do, it will not narrow
anything — and this batch does not contain the per-node child counts needed to tell. That reading is owed
before the change is worth a measurement.

## 4. Level and the unresolved confound

Mean 1668 against `2.0`'s 1518: **+9.9%, 2.04 standard errors.** This sits exactly on the resolution limit,
and it is **confounded with the session**: run11 and run12 are different sessions, and run9 measured a
possible session effect of the same ~10% that n = 10 cannot separate from noise.

So the honest statement is that the reporting-only change **cannot be cleared and cannot be blamed**. It is
the same wall run9 hit. Resolving it needs roughly forty runs per condition, or a per-session control
carried inside every batch.

**Pre-registered prediction, scored:** "level and CV will not change materially, since no constant changed."
CV held (10.8% → 9.85%, no distinguishable change). Level moved +9.9% at 2.0 se — neither confirmed nor
refuted, for a reason that was known before the batch and is not the prediction's fault.

## 5. Variance decomposition of the total, and something new

Exact decomposition on **total = leaf count × price per leaf × (1 + integration/leaf sum)**:

| Factor | run7 | run8 | run9 | run11 | **run12** |
|---|---:|---:|---:|---:|---:|
| Leaf count | 30.7% | 62.2% | 76.7% | 50.7% | **120.4%** |
| Price per leaf | 61.5% | 3.9% | 16.3% | 15.4% | **−11.6%** |
| Integration factor | 7.8% | 33.9% | 7.1% | 34.0% | **−8.8%** |

Shares above 100% and below zero are not an error: they are covariance attribution, and they say that
**leaf count now over-explains the total while the other two factors partially cancel it.**

The mechanism is visible directly: **corr(leaf count, integration factor) = −0.51.** A run that splits
finer charges relatively *less* for joining. Both readings are individually defensible — more leaves means
smaller pieces, and smaller pieces meet along cheaper boundaries — but the net effect is that the tree's
granularity is now the single thing that decides the total, with two partial brakes on it.

Note also that leaf-count CV *rose*, 6.8% → 13.0%, while price per leaf fell to its best-ever 3.5%. C1
controls what a leaf costs; nothing controls how many leaves a named module is split into, and that is now
the whole game.

## 6. Two rules the runs derived for themselves

Both are absent from C3, and both were arrived at independently — the same signature that preceded the
activity-branch fix and the node-count fix.

**Single-leaf modules get no node item.** W-7 (28 modules, 25 module nodes) and W-8 (26 modules, 23 module
nodes) both stated it in almost the same words: one child is not an aggregation, so there is nothing to
join. Eight runs never met the case. Two of ten diverged from silence, not from each other.

**Activity-branch nodes: no divergence at all.** W-5 warned that a run pricing no node items on branches 1,
7, 8, 9 and 10 would report roughly 126 pd less — about 7% of a total — and named it the most likely place
for two runs to disagree. **All ten priced all ten branch nodes.** The freedom exists on paper and was not
exercised; it needs no rule yet, but it is now a known place to watch.

## 7. Compliance

Across all ten runs: every report stamped `Lytin-D 2.3`; no leaf with M > 10 and none below 1 pd; no
merging; **zero** of the ~341 node items fell back to the 15% rule; all ten C2 branches filled in every run;
every run printed the function → module map, the three-part node count and the seam mix; every run recorded
that the source fixes no architecture and that none was assumed.

## 8. Status and what is owed

1. **Re-read the C3 v2 draft against §3 above** before applying it. Its motivation is obsolete; its
   mechanism may be right for a reason it does not state. The reading owed first: whether observed seams per
   node already equal k − 1.
2. **Leaf count is the whole remaining spread** (120% of Var, CV 13.0%). C1 fixes the ceiling on a leaf, C5
   fixes which modules exist; how finely a run splits *inside* a module is untouched by either. This is the
   next parameter, and it is bigger than the one C3 v2 addresses.
3. **The session confound is still unresolved** and now blocks two comparisons instead of one. Every batch
   from here should either run inside one session against a same-session control, or accept that level
   differences below ~10% are unreadable.
4. **Single-leaf modules** — candidate minor amendment to C3, on the evidence of two independent
   derivations.
