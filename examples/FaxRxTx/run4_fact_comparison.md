# FaxRxTx — Step D: unsealing FACT.md and checking against fact (2026-07-17)

All blind runs (run1–run3) are complete before the unsealing. The fact from FACT.md:
**~120 person-months** (a team of ~10 people × ~1 year), the accuracy of the duration
estimate per the participant **±20% → a window of 96–144 pm**.

## Summary table

| Estimate | Center | Range | Against the fact window 96–144 |
|---|---|---|---|
| Run 1 — decomposition (raw) | E ≈ 111.6 | E±2σ: 103–120.5; honest ΣO…ΣP: 51–205 | in the window (−7% of 120) |
| Run 2 — reference class | P50 ≈ 160 | P10 85 … P90 320 | fact ≈ P25–P35 of the class, inside the distribution |
| Run 3 — calibrated decomposition | ≈ 155 | 135–180 | +29% of the window center, +8% of its edge; the ranges overlap (135–144) |

## Interpretation

**The main caveat — the measuring instrument itself is soft.** The fact is reconstructed from
memory ~18 years old with a stated accuracy of ±20%. The divergence of the calibrated
estimate from the fact (155 vs. 120) is within one width of the error
of the recollection itself: if the project actually took not 12 but 13–14 months,
there is no "miss" at all, and the participant cannot tell this apart from memory.

Therefore the result is stated modestly:

- **All three estimates are consistent with the fact within the accuracy of the recollection.**
  On such a fact one can assert neither "raw decomposition hit" nor
  "calibrated missed" — the difference between 112 and 155 is smaller than the
  resolving power of the instrument.
- The pipeline produced no absurdity at any step: the raw center, the calibrated
  corridor, and the fact's quantile in the class (~P30) are mutually compatible.
- **Both structural patterns of BMS reproduced:** the absurdly narrow CI
  of raw decomposition (±8% — an artifact of leaf independence) and
  the non-calibratable right tail (above ~177 pm multipliers on the WBS cannot
  reach; the class P90 320 is taken only from reference class).

## Hypotheses for the future (not conclusions; n=2, the fact is soft)

1. Calibration pulls the estimate toward the ensemble P50 and therefore should systematically
   overshoot on projects better than the median — the price of insurance against the right tail.
   A possible form of the answer — a triple: the center from the WBS, the corridor from calibration,
   the reserve from the class tail. To be tested on a project with a documented
   (not remembered) fact.
2. A "well-behaved" WBS (blind spots already itemized as leaves) + ensemble
   global multipliers (scope creep, org tax) = a risk of double counting;
   a "well-behavedness discount on the WBS" may be needed.
