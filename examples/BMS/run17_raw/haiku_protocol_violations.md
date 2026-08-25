# Haiku 4.5 on Lytin-D 5.0 — protocol violations, run HA-4

## 1. C1 violated — the load-bearing constant
C1: split any item whose M exceeds 10 pd. The Testing phase leaves carry
M = 18, 18, 22, 14, 12, 20, 18 pd. Seven leaves, every one above the ceiling,
none split, no C1 exception logged.

## 2. The run's own instrument readings contradict its own leaf table
Reported M-distribution: ">10 pd: 0 (none - C1 ceiling enforced)".
Actual: 7 leaves above 10. The self-report is false, not merely incomplete.
Also reports "<1 pd: 1 leaf (Feedback capture @ 1.08)" - 1.08 is not below 1.

## 3. C3 top-level assembly node dropped
Sigma integration = 25.11 (module) + 70.46 (phase) = 95.57.
The top-level assembly item (70.46) was computed, then annotated
"already included in the Phase Total line above" and omitted from the sum.
Implied multiplier came out 1.271 against ~1.50 for every Opus and Sonnet run.

## Consequence for the third-point experiment
Leaf count 38 is NOT a leaf count under Lytin-D 5.0: the tree was not split to
the C1 ceiling, so N does not mean the same thing it means in the other 60 runs.
The pd-per-leaf reading (447.89/38 = 11.79) is therefore not comparable either -
it is inflated by unsplit leaves, not measured at the same granularity.

Per the pre-registration: this is recorded as an ENGINE CAPABILITY FLOOR, and is
not treated as a data point on either the primary or secondary reading.
