# Run 68 — Step 6, the reveal: the run 61–67 estimate against `FACT.md` (FaxRxTx, 2026-09-16)

**Order held.** `estimate_FaxRxTx_2026-09-16.md` was written and fixed first (md5
`9edf77f255ffa4c9db85d6ecb3ba421a`, 2026-09-16 14:05:58 local); only then were `FACT.md`, `docs/constants.md` §4a and
the exit-criterion files opened. Nothing below was fed back into the document, and the document's centre does not
mention the outcome. No sensor saw the outcome (run 67's prompt was checked for it; its contamination check was
clean).

**Disclosures that bound what this comparison can mean.**
- The orchestrator had read `docs/instrument.md` §5 before the run, which states that an *earlier* chain landed
  ×1.21 from this outcome. The value of the outcome was not known; the existence of an earlier ratio was.
- The presence convention used below (6 net h per present day, ×1.10 leave) was pinned on 2026-08-27, **after** this
  case's outcome was known (`docs/constants.md` §4a says so and argues why it is not a fit). By the rule
  "a case whose conditions arrive after its number can be learned from; it cannot score", **this case can be learned
  from; it does not score** — as `docs/instrument.md` §5 already records for case 1.
- `docs/constants.md` §4a, opened now, carries an earlier chain's figure for this case; it is not used here.

## The outcome, in its own unit and converted

`FACT.md`: team **~10 people** including QA/PM, **about 1 year**, total **~120 person-months**; a participant's memory,
no documents; the participant's own accuracy on the duration **±20% → 96–144 person-months**. The unit is a
team × duration figure — **staffed person-months** (leave inside), exactly as the case profile §5 declared before
the run.

By `docs/constants.md` §4a (1 staffed pm = 21 ÷ 1.10 × 6 ≈ 114.5 net task hours):

| | staffed pm | net task hours |
|---|---:|---:|
| outcome | **120** | **13 745** |
| outcome band (±20%) | 96 – 144 | 10 996 – 16 494 |

## The comparison

| reading | net task hours | ≈ staffed pm | against the outcome |
|---|---:|---:|---|
| **Calibrated centre** (run 67) | **17 350** (17 100 – 17 597) | 151.5 (149 – 154) | **×1.26 high** (×1.24 – ×1.28); above the outcome's ±20% band by ×1.05 |
| **Corridor** (run 67, rate envelope) | 11 795 – 26 330 | 103 – 230 | **contains the outcome**, in its lower part (13% of the way from the low end, linear) |
| **Reserve** (raw class tails) | P80 20 038 / 30 240 · P90 27 480 / 39 060 | | not reached — the outcome sits below both P80s |
| raw chain (runs 61–64) | 10 020 (9 846 – 10 194) | 87.5 | ×0.73 — **×1.37 low** |
| raw chain, ρ = 0.5 band | ≈ 7 764 – 12 337 | 68 – 108 | does **not** contain the outcome |
| RC65-1 P50 (× 126) | 18 900 | 165 | ×1.38 high; the outcome sits near its P30 (log-interpolated between P10 and P50) |
| RC65-2 P50 (× 114.5) | 12 023 | 105 | ×0.87 — 1.14 low; the outcome sits near its P58 |
| after G1, attended hours (not an answer; shown because run 67 ruled it must not be converted again) | 21 685 | — | converting it at 114.5 would read ×1.58 — the double count the diagnosis caught |

In the outside view's own units: 120 staffed pm against RC65-2 (staffed pm) is between its P50 105 and P80 175;
against RC65-1 (recorded 168-h months) it is ≈ 109 recorded pm (× 114.5 / 126), between its P10 80 and P50 150.

## What the reveal says about the named items (learning, not scoring)

- **The direction flipped between raw and calibrated.** The table-priced chain was low (×0.73); the gap-blind
  Step C chain added ×1.73 and overshot to ×1.26. The calibration was not fitted to anything, and it overshot by
  roughly the size of its two lowest-confidence components: G2 (era + learning curve, +2 263 h) and T3–T5 (immersion,
  parallel run, PM residual as COCOMO II phase shares, +2 497 h). Without G2 the centre would read ≈ 15 090 h
  (×1.10); without T3–T5 ≈ 14 480 h (×1.05) (repeat means of the central chain with the step removed). These are observations about which rate carries the miss, not
  corrections — the rates stay as supplied, and any change is a later, dated act made on more than this case.
- **The diagnosis's first lever is where the outcome sits.** At the pinned 6 net h/day the centre is ×1.26 high; the
  sensors' own factor band (up to ~146 net h per month) would move the reading toward ×1.0. The outcome cannot tell
  which factor is right — it is a memory of heads × months — so this stays a declared unknown of the case, not a
  finding about the factor.
- **The two outside readings bracket the outcome** (RC65-2 P50 low by ×0.87, RC65-1 P50 high by ×1.38); the
  calibrated centre landed closer to RC65-1, and the diagnosis had already flagged that closeness as partly one
  source (COCOMO II) seen twice. The reveal supports that warning.
- **Unpriced items in §4 of the document** (archive migration, v1 upkeep, hyper-care, cluster build-out) all point
  up; the outcome says the centre did not need them — consistent with the diagnosis's request for the reverse audit
  (the chain and its calibration can only add).

## Against the exit criterion

`docs/exit_criterion.md` v1.0 is **superseded** by `docs/status_2026-08-27.md` §6c (v2.0).

| test | v2.0 | this run |
|---|---|---|
| 1 · repeatability, end-to-end from step 1, ≤ ×1.3 | needs no fact | **not measured end to end**: only `HM61-1` was crossed and sized. Sizing spread on that model ×1.035; the product-model pair differs ×1.10 on leaves, unpriced |
| 2 · position inside the human interquartile corridor | needs a human scale on a shared input | not evaluable (no shared human input) |
| 3 · calibratability on held-out cases | needs 3 outcomes | not evaluable (1 outcome in hand) |
| provenance — nothing fitted on the scored case | carried from v1.0 | **held for the rates** (table constants; Step C gap-blind); **the presence convention post-dates this outcome** → the case is learnable-from, not scoring |

For the record only (v1.0 is withdrawn): the calibrated P50 is inside ×1.3 of the outcome (×1.26), and the declared
corridor contains it.

**One line:** calibrated centre 17 350 net task hours (≈ 152 staffed pm) against the remembered 120 staffed pm
(13 745 h) — **×1.26 high, inside the corridor 11 795–26 330, outside the outcome's own ±20% band by ×1.05**; the raw
chain was ×1.37 low.
