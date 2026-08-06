# BMS — Run 13: integration priced by size (raw data, n=10)

Date: 2026-08-06. Engine `Lytin-D 3.0` — C3 replaced: the integration item at every aggregation node is
**20% of the sum of leaf E beneath it**, with no seam enumeration, no rate table and no 15% fallback.
Prompt `prompt_decomposition_BMS.txt`, md5 `c33affd709792dfe60531daa3cb42d65`, byte-identical to run6 … run12.
Ten runs, one session, launched simultaneously. Loading confirmed before launch by the version probe
(`Lytin-F 3.0`), which on this cycle was an **edited** file rather than a created one — so its answer proves
the harness re-reads modified definitions, which is the question a freshly created probe cannot settle.

## Raw data

| Run | ΣE | Mod. | Leaves | Σ leaf E | Integr. | Share | Nodes M/B/T | Multiplier | Single-leaf mod. | M>10 |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| X-1 | 1577.2 | 22 | 147 | 1030.7 | 546.5 | 34.6% | 22/10/1 = 33 | 1.530 | 0 | 0 |
| X-2 | 1456.1 | 19 | 134 | 956.7 | 499.4 | 34.3% | 19/10/1 = 30 | 1.522 | 0 | 0 |
| X-3 | 1363.0 | 25 | 121 | 898.9 | 464.0 | 34.0% | 21/10/1 = 32 | 1.516 | 4 | 0 |
| X-4 | 1752.8 | 25 | 152 | 1145.4 | 607.4 | 34.7% | 24/10/1 = 35 | 1.530 | 1 | 0 |
| X-5 | 1806.2 | 25 | 150 | 1185.3 | 620.9 | 34.4% | 24/10/1 = 35 | 1.524 | 1 | 0 |
| X-6 | 1727.1 | 22 | 155 | 1129.7 | 597.4 | 34.6% | 22/10/1 = 33 | 1.529 | 0 | 0 |
| X-7 | 1766.3 | 24 | 159 | 1156.7 | 609.6 | 34.5% | 22/10/1 = 33 | 1.527 | 2 | 0 |
| X-8 | 1746.2 | 26 | 157 | 1141.8 | 604.3 | 34.6% | 25/10/1 = 36 | 1.529 | 1 | 0 |
| X-9 | 1977.4 | 31 | 203 | 1285.0 | 692.4 | 35.0% | 29/10/1 = 40 | 1.539 | 2 | 0 |
| X-10 | 1565.9 | 26 | 146 | 1028.2 | 537.8 | 34.3% | 21/10/1 = 32 | 1.523 | 5 | 0 |

## The five measurements of this instrument

| | run7 — 1.0 | run9 — 1.0, other session | run11 — 2.0 (C5) | run12 — 2.3 | **run13 — 3.0** |
|---|---:|---:|---:|---:|---:|
| Mean ΣE | 1284 | 1410 | 1518 | 1668 | **1674** |
| Standard deviation | 114 | 141 | 164 | 164 | **182** |
| **Coefficient of variation** | **8.9%** | **10.0%** | **10.8%** | **9.85%** | **10.86%** |
| Min … max | 1125 … 1436 | 1196 … 1608 | 1330 … 1851 | 1436 … 1899 | 1363 … 1977 |
| Leaf count (mean, CV) | 125 | 133 (8.7%) | 139.8 (6.8%) | 148.7 (13.0%) | **152.4 (13.9%)** |
| Price per leaf (mean, CV) | 6.80 (8.0%) | 7.32 | 7.33 (6.2%) | 7.50 (3.5%) | **7.22 (5.6%)** |
| **Integration share (mean, CV)** | 34.0% | 30.6% | 32.3% | 33.3% (**10.4%**) | **34.5% (0.78%)** |
| Multiplier ΣE ÷ Σ leaf E (CV) | — | — | — | — | **1.527 (0.40%)** |
| Aggregation nodes (mean, CV) | 19.0 (36.7%) | 16.7 (44.1%) | 28.6 (23.3%) | 34.1 (8.0%) | **33.9 (8.2%)** |

## 1. Prediction 1 — confirmed, and by a wide margin

**Integration-share CV: 10.4% → 0.78%.** A thirteen-fold collapse. The share now sits in a band 0.7
percentage points wide (34.0 … 35.0) where it previously ranged over 9.7 (28.6 … 38.3).

The **implied multiplier** — the new §6 reading — is tighter still: **CV 0.40%**, range 1.516 … 1.539.
Every run computed it and every run reconciled it against the shape of its own tree, exactly as the
self-check was meant to work. The residual variation is fully explained by one thing: what fraction of leaf
weight sits under functional branches (three assembly levels, ×1.6) versus activity branches and single-leaf
modules (two levels, ×1.4). It is arithmetic, not judgement.

**The sharpest single demonstration is X-9 against the rest.** It built 203 leaves where the others built
121…159 — a tree half again as fine — and returned an integration share of 35.0% and a multiplier of 1.539,
inside the same band as everyone else. Under the old rule a tree that fine would almost certainly have
enumerated far more seams. **Splitting no longer drags integration behind it.**

## 2. Prediction 2 — confirmed to within 0.3%

Predicted before the batch: integration = 0.532 × Σ leaf E, total = **1.532** × Σ leaf E, level +2%.

Observed multiplier: **1.527**. Mean level 1674 against run12's 1668 — **+0.4%, 0.08 standard errors.**

**A side finding on the session confound.** run12 and run13 are different sessions, and run9 left open the
possibility of a ~10% session effect that n=10 cannot resolve. These two batches landed 0.4% apart. One pair
(run7 vs run9) differed by 9.8%; this pair differs by 0.4%. That is not the signature of a systematic drift
— it is the signature of noise, and it weakens the case for a real session effect without settling it.

## 3. Prediction 3 — the mechanism is confirmed exactly; the headline number is not

Predicted: total CV rises from 9.85% to roughly 12%, because the old rule was accidentally damping
leaf-count variation and strict proportionality removes the damper.

Observed: **10.86%.** Direction right, magnitude short. The variance ratio against run12 is 1.22, far inside
what an F-test on 10 versus 10 can distinguish from 1. **On the headline number alone, the prediction is
neither confirmed nor refuted.**

But the headline number is the wrong place to look, and the right place settles it cleanly. Compare each
batch's output spread against the spread of its *own* leaf sum:

| | CV of Σ leaf E | CV of ΣE | ratio |
|---|---:|---:|---:|
| run12 (old rule) | 12.0% | 9.85% | **0.82** |
| run13 (new rule) | 10.6% | 10.86% | **1.03** |

Under the old rule the total varied **less** than the leaf sum it was built from — that is what damping
means, stated without interpretation. Under the new rule it varies very slightly **more**. The damper is
gone, exactly as predicted; the headline CV moved less than forecast only because this batch's leaf spread
happened to be smaller than the last one's.

Corroborating correlation: `corr(leaf count, integration factor)` was **−0.51** under the old rule and is
**+0.93** now. The sign flipped from damping to mild amplification, and the magnitude of the amplification
is negligible because the multiplier itself barely moves.

## 4. Prediction 4 — confirmed

Exact log-variance decomposition on **total = leaf count × price per leaf × multiplier**:

| Factor | run7 | run8 | run9 | run11 | run12 | **run13** |
|---|---:|---:|---:|---:|---:|---:|
| Leaf count | 30.7% | 62.2% | 76.7% | 50.7% | 120.4% | **108.8%** |
| Price per leaf | 61.5% | 3.9% | 16.3% | 15.4% | −11.6% | **−11.8%** |
| Integration factor | 7.8% | 33.9% | 7.1% | 34.0% | −8.8% | **3.0%** |

**Integration now accounts for 3% of the sensor's variance.** It was 34% two versions ago. For practical
purposes the estimate is a function of one variable: ΣE ≈ 1.527 × Σ leaf E ≈ **11.0 pd per leaf**.

Price per leaf keeps its small negative share — runs that split finer price each piece slightly cheaper,
which partly cancels the leaf-count effect. That is the one remaining structural counterweight, and it is
weak.

## 5. Compliance

Across all ten runs: every report stamped `Lytin-D 3.0`; **no run mentioned seams, seam kinds or a rate
card anywhere** — the second, independent confirmation that the new definition loaded; every run printed the
three-part node count and the implied multiplier, and every run reconciled the multiplier against its own
tree shape; no leaf with M > 10 (one leaf in the 1–2 bucket, in X-9, which C1 permits); none below 1 pd; no
merging; all ten C2 branches filled in every run.

**The single-leaf rule earned its place.** Seven of ten runs met the case and correctly charged no item —
X-10 had five such modules, X-3 four. Without the rule those thirteen would have collected roughly 25 pd of
integration for joining nothing. Both this rule and the non-compounding base were specifications added
beyond the bare "20% per node", and both were applied by every run that met them.

## 6. What this batch cost in exchange

Stated plainly, because it is a real loss and not a rounding error.

The integration figure no longer carries any information about the specific system. It is `multiplier × leaf
sum`, and the multiplier is a property of the drawn tree. A loosely coupled system and one where state
crosses every boundary now receive the same share. Several runs noticed this unprompted and said so — one
wrote that the 34.7% share is "a structural consequence of C3 and C5, not a judgement about this project".
That is correct, and it is the price paid for removing a quantity that swung by half on identical input.

The architecture blind spot is now explicit in the rule text and was reported by every run: a uniform rate
cannot express the step between joining two modules inside one deployable and joining two independently
deployed services. The correction, when it comes, is a labelling of nodes — not a multiplier on any total.
Parked in `docs/parked_architecture_as_rate_step.md`.

## 7. Where the instrument now stands

| Parameter | Pinned by | Evidence |
|---|---|---|
| Price of a leaf | C1 | CV 15.9% → 5.6% |
| Which modules exist | C5 | corr(modules, ΣE) ≈ 0 |
| Number of aggregation nodes | C5 | CV 44.1% → 8.2% |
| Cost of integration | C3 (`3.0`) | share CV 10.4% → 0.78%; 3% of variance |
| **How finely a module is split into leaves** | **nothing** | **CV 13.9%; 108.8% of variance** |

Four rounds of constants have each closed the parameter they targeted, confirmed by measurement each time.
The output spread has not improved across any of them — 8.9%, 10.0%, 10.8%, 9.85%, 10.86% — because the
variance moved to the next unpinned parameter every time. There is now exactly one left, it carries
essentially all of the spread, and the total is a simple multiple of it.

## 8. Status and what is owed

1. **The splitting rule is the whole remaining task.** Leaf counts ran 121 … 203 on identical input;
   X-9 alone built 34% more leaves than the next-finest run. Nothing in C1 (a ceiling of 10 pd), C2 (ten
   branches) or C5 (which modules exist) constrains how many pieces a named module is cut into.
2. **C3's 20% remains uncalibrated**, and no repeatability measurement can check it — it moves the level,
   not the spread. It waits for a case with a documented actual outcome. Stating it as one named parameter
   rather than three hidden rates was the point of the change.
3. **The session confound is weaker than feared** but not resolved: two pairs of batches, one differing by
   9.8% and one by 0.4%. Treat level differences below ~10% as unreadable until a batch carries its own
   same-session control.
4. **Architecture as a rate step** stays parked, with the splitting rule as its first prerequisite.
