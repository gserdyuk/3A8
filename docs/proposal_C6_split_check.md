# C6 — the split consistency check

Status: **measured, n = 10 on each of two models (run16).** Predictions below were registered before any
run and are committed in a separate, earlier commit than this result, so the pre-registration is verifiable
in the history rather than asserted. **Scored at the end of this file: 1 partial, 1 failed, 2 confirmed —
and the one that failed is the one the proposal itself named as the one that mattered.**

## The idea, and where it came from

Estimate a node whole before splitting it. Split it. Compare the sum of the leaves against the figure you
committed to beforehand. Where they disagree, do not correct anything — look at *why*.

This is the first **feedback** mechanism in the sensor. Every constant before it is a constraint: a ceiling
on a leaf (C1), a fixed branch list (C2), a rule for deriving modules (C5), a rate for integration (C3).
A constraint says what you may not do. This says: check yourself against yourself.

It costs almost nothing, because **the pre-split estimate already exists and is currently thrown away.**
C1 reads "split anything whose M exceeds 10", so a run must already have formed a size judgement about the
whole in order to decide to split it. C6 is the instruction not to discard it.

## Why now

Four rounds of constants each closed the parameter they targeted, and the output spread never moved:
8.9%, 10.0%, 10.8%, 9.85%, 10.86%. The variance relocated every time. One parameter is left — how finely a
module is cut into leaves — and it now carries essentially all of the spread (108.8% of variance, leaf-count
CV 13.9%, counts running 121 … 203 on identical input).

Constraints have had four attempts at this shape of problem. A feedback loop is a different instrument, and
worth one measurement before writing a fifth constraint.

## Decisions taken, and by whom

- **Which figure is right: neither.** There is a difference; analyse it. The leaf sum stands in every case —
  parts are known better than wholes, and that premise is what bottom-up estimation rests on. The check
  corrects nothing.
- **Threshold ±10%**, stated as a named parameter of the method rather than buried. It enters no arithmetic
  and controls only how often the check speaks, so getting it wrong is cheap — unlike C3's 20%, which sets a
  third of the level.
- **The check is knowingly a step toward top-down.** The whole-node figure is a coarser judgement than the
  leaf sum, and consulting it at all gives coarse judgement a voice in a method built to replace it. Adopted
  deliberately, not by accident.
- **Adjustment versus reconciliation cannot be told apart from outside**, so preference goes to the detailed
  level and the inconsistency is *reported* rather than resolved. That is the whole return on the change.

## The design flaw, stated before the measurement rather than after

Asking a run to estimate a node whole **before** splitting it may anchor the leaf estimates that follow.
A run that writes "this module is about 40 pd" and then produces leaves summing to 40 has told us nothing,
and the check will look like a clean pass.

This cannot be prevented inside a single generation. It can only be read afterwards, and it makes the result
**asymmetric**:

- a systematically **positive** mean discrepancy is informative — unpacking is real and anchoring did not
  suppress it;
- a mean **near zero** is ambiguous — it could mean there is no unpacking, or it could mean the anchor did
  its work. Nothing in the data will separate the two.

A suspiciously tight cluster around zero is the signature to watch for. If that is what comes back, the
honest reading is "this design cannot answer the question", not "the question is answered".

## Why a major version

`4.0` rather than `3.1`. The convention makes major the test of whether a change *can* move the level, and
the anchoring risk above says this one can — a new estimation step sits upstream of every leaf figure in the
tree. It is a judgement call: the change is designed to be diagnostic and should move nothing. Erring toward
major costs a version number; erring toward minor would mean discovering after the fact that two batches
were not comparable, which is exactly what the stamp convention exists to prevent.

## Registered predictions

1. **Mean signed discrepancy is positive**, in the range +5% to +20%. Basis: the unpacking effect (Tversky &
   Koehler), which the method already names as its reason for having a splitting ceiling and no floor. If it
   comes back near zero, see the design flaw above before concluding anything.
2. **Discrepancy grows with splitting depth.** Runs that build more leaves per module should show larger
   positive gaps. This is the prediction that matters, because it is the one that would connect the check to
   the parameter we are actually trying to close. A flat relationship means the check, whatever else it
   shows, will not help with leaf count.
3. **Level does not move materially** from `3.0`'s 1674 — the check changes no figure by construction. A
   level shift beyond a few per cent would be evidence of anchoring, not of the method.
4. **Spread does not narrow.** The check is diagnostic; nothing in it pulls two runs together. Expect CV
   near 10.9%. A narrowing would be surprising and would need explaining before being believed.

Prediction 3 and prediction 1 pull against each other in an informative way: strong anchoring would satisfy
3 while destroying 1, and that combination is itself a reading.

## What comes after, depending on the result

- **Positive mean, growing with depth** → the mechanism is real and a corrective version becomes worth
  designing, with the question of what "reconsider" means answered explicitly rather than left to the run.
- **Positive mean, flat with depth** → unpacking exists but is not what drives leaf count; the check earns
  its place as a reading and the leaf-count problem needs a different tool.
- **Near zero** → inconclusive by construction. Do not read it as a pass.

---

# Result (2026-08-07, run16 — n = 10 on Opus 5, n = 10 on Sonnet 5)

## 1. Mean signed discrepancy positive, +5% … +20% — **partial**

| | mean | range | runs inside the predicted band |
|---|---:|---:|---:|
| × Opus 5 | **+28.88%** | +10.0 … +45.5 | **2 / 10** |
| × Sonnet 5 | +24.64% | +2.3 … +59.2 | 2 / 10 |

The **sign** is right and is not in doubt: across twenty runs and roughly four hundred individual node
checks, essentially every discrepancy came back positive, and several runs reported zero negative rows in
the whole tree. The **magnitude** was under-predicted by about half again — +28.9% against a band whose top
was +20%, with 8 of 10 runs above the band on each model.

The under-prediction is itself informative. The band was reasoned from the unpacking effect alone. The runs
consistently attribute the gap to something more specific: **this RFP names large mechanisms in short
phrases** ("high configurability", "capabilities for the Travel Manager", "intelligent search"), so the
whole-node figure prices the phrase and the split prices the work. If that reading is right the magnitude is
a property of *the source text's density*, not of the method, and the band was never a constant to predict.

## 2. Discrepancy grows with splitting depth — **failed, and decisively**

| | leaves per module | Pearson r | Spearman |
|---|---:|---:|---:|
| × Opus 5 | 6.38 | **−0.285** (t = −0.84) | −0.285 |
| × Sonnet 5 | 4.16 | **−0.304** (t = −0.90) | −0.297 |
| **pooled, n = 20** | 3.09 … 7.55 | **−0.035** (t = −0.15) | +0.014 |

Not merely non-significant — **flat**, and if anything faintly the wrong way in each batch on its own.

The pooled test is the one to read. Combining the two models more than doubles the range of splitting depth
(3.09 to 7.55 leaves per module, a 2.4× span, far wider than either batch could offer alone) and gives the
prediction its best chance of showing up. The correlation vanishes completely: **r = −0.035.** A run that
cuts a module into seven leaves shows no larger a gap against its own whole-node figure than a run that cuts
it into three.

This is the branch the proposal itself pre-committed to:

> **Positive mean, flat with depth** → unpacking exists but is not what drives leaf count; the check earns
> its place as a reading and the leaf-count problem needs a different tool.

Taken at its word: **C6 will not close leaf count.** It stays as a reading — a good one — and the search for
the next constant has to look somewhere other than at the sensor checking itself.

## 3. Level does not move materially from `3.0` — **confirmed**

1673.8 → **1625.5**, i.e. **−2.9%**, t = −0.65 against the combined standard error of the two batch means.
Inside noise. The check changed no figure, as designed, and no anchoring toward the pre-split estimate is
detectable.

Prediction 3 and prediction 1 were written to pull against each other — strong anchoring would have
satisfied 3 while destroying 1. Both held in the informative combination: **the gap is large (+28.9%) and
the level did not move**, which is exactly what "diagnostic only" is supposed to look like and is the
cleanest evidence in this project that a stated discipline actually bound.

## 4. Spread does not narrow — **confirmed**

CV **9.25%** against `3.0`'s 10.86%; variance ratio 1.38 against a 5% critical value of 4.03. No narrowing,
as predicted, and the sixth consecutive version to leave the output spread where it was.

## What this changes

**The check is kept and its purpose is re-stated.** C6 was proposed as a possible route to the leaf-count
problem and does not solve it. What it does deliver is the most useful *reading* the sensor has ever
produced about itself: twenty runs, two models, and the same diagnosis in every one — the whole-node figure
prices what the source text *says*, the split prices what the work *is*, and the gap is where the text
compresses a mechanism into a phrase.

That diagnosis points at the next constant, and it points away from self-checking. If leaf count should
follow the count of distinct behaviours the source names, then that count is a property of the text,
measurable once, independent of the model — which is exactly what run16 shows is needed, since every pinned
parameter held across models to within 3% while leaf count moved by ×1.97.

**One structural condition on whatever comes next.** Scoring a tree against the source text must not happen
inside the run that built the tree, or the run will adjust the tree to match and reintroduce the judgement
C1 removed — the same failure the pipeline already guards against by keeping `calibration-rates` blind to
the gap it explains. The behaviour inventory has to come from a separate agent that has seen only the source
text, with the estimator blind to it. Otherwise it is fitting, and C6's own discipline — *no figure was
changed on the strength of this table* — is what would be lost.
