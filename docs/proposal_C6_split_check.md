# C6 — the split consistency check

Status: **applied as `Lytin-D 4.0`, not yet measured.** Predictions below are registered before any run.

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
