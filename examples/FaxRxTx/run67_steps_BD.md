# Run 67 — Steps B and D, `Lytin-G 1.1` × Claude Opus 5 (FaxRxTx, 2026-09-16)

The only participant that saw both sides. Prompt `prompt_G.md` (`97be5776…`, built by `make_prompt_67.py`): the
description and log, the case profile §1–§4, `docs/instrument.md` §0 and §4 (one clause naming this case's outcome
struck), the bottom-up reading (runs 61–64) with its declaration, RC65-1 and RC65-2 verbatim, RK66-1 verbatim, and
the priced chain. **No outcome.** Reading RG67-1: engine `Lytin-G 1.1`, end_turn, 21 461 output tokens, no tool
use, contamination check clean, answered in English. Raw reply: `run67_raw/RG67-1.md`.

## Units first

| input | declared unit | to net task hours | source |
|---|---|---|---|
| bottom-up | net task hours, leave out | — | — |
| RC65-1 | recorded pm = 168 attended h, leave out | × **126** (6 net h × 21 days; no ×1.10) | `docs/instrument.md` §0 |
| RC65-2 | staffed pm, leave in | × **114.5** | same, verbatim |
| RK66 G1 | turns net hours into attended hours | **the same step as the pinned 6-h day** | — |

- **G1 and the convention overlap**: applying both counts within-day overhead twice. G1 is applied in the chain
  table but its output is in attended hours; **the final answer is the post-G2 line**, and the orchestrator's
  conversion at 114.5 takes G1's place. Request to the rate agent: restate G1 as a unit step.
- Disputed factor bands: RC65-1 100–146 h per unit, RC65-2 101–133.
- **Units component of the unit-blind gap at P50:** 6 300 h (31%) against RC65-1, 5 618 h (68%) against RC65-2.
- Possible units issue inside the bottom-up: HK64-1 declares its day-based sources may have meant assigned days
  (×1.23–1.45 overstatement); whether rate table v0.1-h shares that looseness is not declared.

## Divergence (net task hours)

| | bottom-up raw | RC65-1 @126 | RC65-2 @114.5 |
|---|---:|---:|---:|
| P10 | ~7 840 | 10 080 | 6 298 |
| centre / P50 | **10 020** | **18 900** (×1.886) | **12 023** (×1.200) |
| P80 | — | 30 240 | 20 038 |
| P90 | ~12 000 | 39 060 | 27 480 |

The two outside readings differ ×1.57 at P50 — more than the whole converted gap to RC65-2.

## Calibration (RK66 order, INPUT-7 pricing accepted, recomputed ±0.5 h)

Net task hours, repeat 1 / repeat 2: low 12 192 / 11 795 · **central 17 597 / 17 100** · high 26 330 / 25 704
(after G2). After G1 (attended hours, not to be converted again): 14 021–36 862.

Corrections add +7 328 h at central: fills +1 012 · T1 +262 · T2 +1 294 · T3 +999 · T4 +874 · T5 +624 · G2 +2 263.
G2 (31%) and T3–T5 (34%) carry most of it and are the lowest-confidence rates; itemised fills are 14%.

## The answer (Step D)

| part | net task hours |
|---|---|
| **Centre** | **17 350** (repeat band 17 100–17 597), ×1.73 the raw centre |
| **Corridor** | **11 795 – 26 330** — the envelope of all lows and all highs; not a P10–P90; step-1 variance not in it |
| **Reserve** | the raw class tails: RC65-1 P80 30 240 · P90 39 060 (band 31 000–45 260); RC65-2 P80 20 038 · P90 27 480 (band 24 190–31 920) |

**Explained share:** against RC65-1, 83% (residual +1 552, ×1.09 — its sign flips across the unit band, −2 348 to
+4 552); against RC65-2, **overshoot** (calibrated ×1.44 above its P50 at every factor).

**False convergence:** the calibrated centre lands near RC65-1 (×0.92) — weak evidence: RK66's T1, T3, T4, G2 and
RC65-1's anchor A-3 share COCOMO II; the agreement sits inside the unit band; and it is disagreement with RC65-2.
The raw chain's near-match with RC65-2 (×1.20) was a coincidence of an incomplete chain and a low-anchored reading.

## Named items the rates do not cover — requests for a further gap-blind round

- archive and configuration migration, v1 upkeep, hyper-care — first a scope ruling;
- production cluster build-out beyond size L (A5 unpriceable);
- the additive-only design — run the reverse audit (every correction here points up);
- the team's grade (×2–3 between bands).

## What would change it

1. The net task hours this organisation's month actually yields (the band alone flips the residual's sign).
2. Whether rate table v0.1-h's "day" was a net or an assigned day; and the migration / v1-upkeep scope ruling.
