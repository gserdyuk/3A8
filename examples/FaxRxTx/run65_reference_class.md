# Run 65 — the outside view, `Lytin-R 1.1` × Claude Opus 5, n = 2 (FaxRxTx, 2026-09-16)

Two separate launches on one prompt (`prompt_R.md`, `a433c52a…`): `SYSTEM.md` with four passages struck in place (the
calendar period of the work; the acquisition, price, revenue and a dating inference; where the outcome is kept; the
note on `REQUIREMENTS.md`) and `assumptions.md` verbatim. Launched in parallel with the first product-model launch;
neither side saw the other. Raw replies: `run65_raw/RC65-1.md`, `RC65-2.md`.

| reading | engine as printed | stop · output tokens | tool uses | contamination check |
|---|---|---|---:|---|
| RC65-1 | `Lytin-R 1.1` | end_turn · 8 310 | 0 | clean; the ~1–2 month immersion figure (A1, A3) declared and not used as an anchor |
| RC65-2 | `Lytin-R 1.1` | end_turn · 10 190 | 0 | clean; same declaration |

## Declarations

| | RC65-1 | RC65-2 |
|---|---|---|
| unit | **recorded person-month = 168 attended hours** (meetings etc. inside; 60–70% of it is task time) | **staffed person-month** (one person, one calendar month) |
| leave, holidays, sickness | **outside** | **inside** |
| roles | whole project team incl. QA, PM, immersion phase | whole project team incl. QA, PM, cutover and parallel run |
| sources and their disagreement | ISBSG, COCOMO II, practitioner team × duration; conventions ±30–40% unconverted, ±10% after; levels ×1.7 apart | practitioner team × duration (native), ISBSG, QSM; 15–30% in level from conventions alone |
| scope edges | migration of accounts/configs/archive **inside**; cluster set-up partly inside | hyper-care, migration, v1 upkeep partly inside; cluster set-up, licensing, runbooks mostly outside |

## The class and the quantiles

Both chose essentially one class — an **in-house second-generation rewrite of a distributed high-throughput
back-end with hand-built reliability, an ops console, a customer portal and a parallel-run cutover, 2000s .NET/Java,
own hardware** — at 55% confidence, with neighbours up (platform/middleware build, ~20%) and down (line-of-business
web app, ~20%; partial rework / skunkworks, 5%).

| declared unit | P10 | P50 | P80 | P90 | P90/P50 |
|---|---:|---:|---:|---:|---:|
| RC65-1, recorded pm | 80 | 150 | 240 | 310 | ×2.07 |
| RC65-2, staffed pm | 55 | 105 | 175 | 240 | ×2.29 |
| ratio RC65-1 / RC65-2 (native units) | ×1.45 | ×1.43 | ×1.37 | ×1.29 | |

The spread narrows toward the tail, as `docs/instrument.md` §5 recorded for this sensor. The level difference
comes from the weighting (RC65-1 leans on COCOMO II, middle ~190; RC65-2 on team × duration, 100–120), not from the
units — converting widens it (below).

**In net task hours, by the conversion the diagnosis applied (run 67, `docs/instrument.md` §0):** RC65-1 × 126
(6 net h × 21 present days; its unit already excludes leave) and RC65-2 × 114.5 (the pinned staffed month).

| net task hours | P10 | P50 | P80 | P90 |
|---|---:|---:|---:|---:|
| RC65-1 (× 126) | 10 080 | 18 900 | 30 240 | 39 060 |
| RC65-2 (× 114.5) | 6 298 | 12 023 | 20 038 | 27 480 |

Disputed factor bands (the sensors' own declarations vs the convention): RC65-1 100–146 h per unit, RC65-2 101–133.
At P50 the two readings are **×1.57 apart** in net hours. Not averaged.
