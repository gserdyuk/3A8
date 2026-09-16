# Run 66 — Step C corrections, `Lytin-K 1.1` × Claude Opus 5, gap-blind (FaxRxTx, 2026-09-16)

Launched with `rates-step-c` on `prompt_C.md` (`7e8f83bd…`, built by `make_prompt_66.py`): the description and log as
run 65 saw them, and the bottom-up reading of runs 61–64 — structure with classes and sizes, totals, composition,
coverage report (carried categories, refused rows, holes, what the declaration excludes, the sizing sensors'
closure findings). **No outside-view figure and no target** (asserted by the script). Reading RK66-1: engine
`Lytin-K 1.1`, end_turn, 17 948 output tokens, no tool use; contamination check clean.

## The corrections as supplied (RK66-1 §3, low – central – high)

| id | form | what | rate |
|---|---|---|---|
| A1 | addition (elements) | named holes: L27 1/2/3 × S · L38 S/M/L · L51 S/M/L · L46 (rep 2) 0/S/M · L56 0 · seed items 0 | table-priced |
| A2 | addition (elements) | 10 closure findings (inbound hand-off, unknown numbers, rejection notices, routing fallback, status recording, clean-up, PoP-registry maintenance, account provisioning, v1 function inventory, ending coexistence) | low 5S · central 8S+1M · high 6S+4M |
| A3 | addition (element) | initial load of user accounts from v1 | S / M / L |
| A4 | addition (rows + element) | performance and burst testing (A6 gives targets) + a load generator | L47 only · L46+L47 + gen M · + gen L |
| A5 | addition (re-pricing) | production cluster build-out: E1-prod and E7 one/two classes up | 0 / +1 / +2 |
| T1 | targeted × | complexity of hand-built distributed delivery (N30, N40, L46, L47) — COCOMO II CPLX | ×1.00 / 1.17 / 1.34 |
| T2 | targeted × | unnamed requirement growth — McConnell/Boehm/Jones, lowered for v1 reference and itemised findings | ×1.05 / 1.12 / 1.25 |
| T3 | share of B | W-F48 immersion — COCOMO II Inception | +4 / +8 / +15% |
| T4 | share of B | W-F50 parallel run, soak, stabilisation — COCOMO II Transition less ~2% carried | +3 / +7 / +14% |
| T5 | share of B | PM / product-owner residual — ~8–14% less ~4% carried | +2 / +5 / +8% |
| G1 | global × | within-day overhead, "net task hours vs working hours" — Cohn, Scrum Guide, Peopleware | ×1.15 / 1.25 / 1.40 |
| G2 | global × | era tooling + domain learning curve, merged — COCOMO II TOOL, APEX | ×1.00 / 1.15 / 1.27 |

Declaration: additions land in net task hours through the same chain; losses outside; delivery-team roles;
COCOMO II's 152-h month enters only as ratios. Deliberately uncorrected: step-1 variance, optimism bias, security,
archive/config migration, v1 operation and hyper-care, tail events, calendar/headcount effects, leave. Two global
multipliers exactly. Order of application fixed in §5.

## Pricing and application (`price_fills66.py` → `calibration_66.json`)

Choices the orchestrator made where RK66 was silent are in the script docstring (class and parent per fill;
per-element activity set by class; C3 = 20% × ancestors; A4 rows once without C3; T1 base = inner subtotals of N30,
N40 + own items of L46, L47). **A5 is not priceable** — the table has no XL row for E1 or E7 — and is carried at 0.

| repeat | level | raw | + fills | B | after T3–T5 + addendum | **after G2** | after G1 | × raw to G2 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | low | 10 194 | 491 | 11 094 | 12 192 | **12 192** | 14 021 | ×1.196 |
| 1 | central | 10 194 | 1 000 | 12 668 | 15 301 | **17 597** | 21 996 | ×1.726 |
| 1 | high | 10 194 | 1 514 | 15 060 | 20 733 | **26 330** | 36 862 | ×2.583 |
| 2 | low | 9 846 | 491 | 10 730 | 11 795 | **11 795** | 13 564 | ×1.198 |
| 2 | central | 9 846 | 1 024 | 12 308 | 14 869 | **17 100** | 21 374 | ×1.737 |
| 2 | high | 9 846 | 1 562 | 14 700 | 20 239 | **25 704** | 35 986 | ×2.610 |

Run 67 accepted these choices, recomputed the chain to ±0.5 h, and ruled that **G1 is a unit step, not a
correction** — the figure after G1 is in attended hours; the last line in net task hours is after G2.
