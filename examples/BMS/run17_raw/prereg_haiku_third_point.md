# Third capability point (Haiku 4.5, axis P, n=5) — registered BEFORE results

Written after launch, before any Haiku output was seen.

## Standing data (axis P, Lytin-D 5.0)
Opus   n=5: Sigma E 1480.14, leaves 139.0, 10.65 pd/leaf
Sonnet n=5: Sigma E  721.34, leaves  71.0, 10.16 pd/leaf
Sonnet/Opus leaf ratio = 0.511

Across 6 batches (2 models x 3 instruments): Sigma E = 10.37 x leaves, -5.7%..+3.4%.

## PRIMARY reading — does the pd-per-leaf constant survive a third capability tier?
This is the payload. 10.37 pd/leaf is the best calibration anchor the project has:
it is invariant across two models and three top-level structures. A third tier tests it.
- Haiku lands in 9.5..11.5 pd/leaf  -> constant holds across three tiers; the reduction
  Sigma E = k x N is a property of the METHOD, not a two-model coincidence. Calibrate k.
- Haiku lands outside that band     -> the reduction was a coincidence of two adjacent
  models, and k is itself model-dependent. That kills the calibration anchor and is the
  more important finding of the two.

## SECONDARY reading — structure of the leaf-count ratio
- Haiku/Sonnet ~ 0.5 (leaves ~35): constant ratio per tier, multiplicative in capability.
  No additive correction can ever reconcile models.
- Haiku/Sonnet ~ 0.8 (leaves ~57): ratio compresses downward, relation is not simply
  multiplicative.

## CORRECTION to how this was framed in conversation
I called this a test of "does N saturate - is N a property of the project or the reader".
It is NOT that test, and I should not have said so. Saturation means increments shrink as
capability RISES; testing it requires a point ABOVE Opus, which does not exist here.
Haiku extends the sequence DOWNWARD only. It can show whether the relation is multiplicative
or additive; it cannot locate a ceiling. The saturation question stays open and needs a
different design.

## Executability
Haiku may fail to execute the protocol (C6 pre-split figures, C5 derivation, instrument
readings block). That outcome is recorded as a capability floor of the engine and is not
treated as a data point on either reading above.
