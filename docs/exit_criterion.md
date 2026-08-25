# Exit criterion — when the instrument is fit for use

**Version 1.0, approved by the author 2026-08-21.** Proposed in
`docs/review_2026-08-21_running_in_circles.md` §7.1; this file is the pinned record. Changing a
threshold is a version bump with a stated reason, never a silent edit — and never an edit made while
looking at a result the change would rescue.

## The gate

The estimation instrument is declared **fit for use at its stated accuracy** when, over **at least 4
cases with documented outcomes**, none of them used for fitting:

1. **Center.** The calibrated P50 lands within `[actual ÷ 1.3, actual × 1.3]` on **at least 3 of
   every 4** cases.
2. **Corridor.** The declared P10–P90 contains the actual on **at least 3 of every 4** cases.
3. **Provenance.** No parameter — a rate-table row, a calibration factor — was fitted on the case it
   is evaluated against.

## Why these numbers

- **3 of 4 on the corridor is what the interval itself claims.** An 80% interval is expected to miss
  about 1 case in 5; demanding 4 of 4 would demand more than the interval promises and reward
  inflated corridors.
- **3 of 4 on the center** tolerates one tail-event project, whose reserve is the class tail's job,
  not the center's.
- **×1.3 is deliberately tighter than uncalibrated RFP-stage practice** (×1.5–2, the cone of
  uncertainty at that maturity). The instrument's claim is exactly that calibration buys the
  difference; this gate is where the claim is tested.

## What this gate is and is not

- It is a **gross-error acceptance test** — it will catch a ×4 miss (the FaxRxTx overshoot of
  2026-08-05 would have failed it). At n = 4 it cannot see a ±20% systematic bias; fine calibration
  needs more history and is a later, separate claim.
- It **replaces findings §12d's "repeatability first"** as the terminating condition of the project.
  Repeatability obligations move to where they are checkable per experiment: determinism of the
  arithmetic (script), stability of ensemble statistics, classification agreement — registered in
  `docs/proposal_rate_card.md` §8.
- **Standing at approval:** outcomes in hand — FaxRxTx only (a participant's memory, ±20%). The gate
  is not evaluable today; it defines *done*, and the work it makes urgent is acquiring documented
  outcomes.
