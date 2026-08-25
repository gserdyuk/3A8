# BMS — Run 25: the whole-model layer, and the first full table-priced assembly

Date: 2026-08-22. **Registered before the three outstanding inputs returned** (the N17/N18 sizing
pair and the `Hotyn-K` one-row addendum for R64). Catalogue **1.4** in force.

## What the layer contains

1. **16 once-scoped activities** — A1 · U4 · D1 · D3 · D6 · E2 · E3 · E4 · E6 · E7 · O2 · O3 · O4 ·
   S1 · S2 · S3 — every size **computed**: model bracket M (78 elements), except E3 and E7 by
   environment count (3 → L; the table's E7 rows are labelled "model bracket" — a v0.1 label defect
   recorded in catalogue 1.4; the L-row values are used) and S2/S3 by attack surface
   (surfaces 16 + interfaces 8 = 24 → L).
2. **E1 × three environments** — fixed mapping dev S · stage M · prod L.
3. **The root's per-parent items** — N01 has 16 children and its rooted subtree holds every element:
   A5×2 · A6×2 · A7 · A8 · D2 · U1 · U2×2 · U3×2 · O1. Buckets computed: subtree leaves 61 → XL;
   store+interface count 17 → XL; surface count 16 → XL (after the N17/N18 reclassification).
   **This is the layer that answers run 22's CV-1/CV-6**: the assembly of the top subtrees now has
   items and a C3 base.
4. **Root C3, convention declared:** base = leaf-item E of the 78-element tree — element items plus
   the root's own per-parent items. Once-scoped, per-environment and demanded items attach to the
   work model, not to any element, and enter no C3 base.
5. **The demanded-work branch** (requirements_work.md, W6 pointers): R69 → accounted at E4 ·
   R70 → at E3 · R02 → at E7, running-the-service **carried, parameter: the term** · R03 → at O3,
   operating-support **carried, the term** · **R64 → its own item** (*agree and record the
   technology currency and upgrade policy*), priced by the `Hotyn-K` addendum row; the reviews
   themselves **carried, the term**.
6. **The N17/N18 reclassification delta** (author's decision, run 24): each loses K1/K2/A2/A3/A4
   (were holes anyway — both run-23 sensors refused them as surfaces), gains **K3
   statement-behavioural** at the size the mini-pair returns; D4 stays (computed); **N16's subtree
   loses U1/U2×2/U3×2/O1** — no surface remains beneath it.

## Case law applied to the assembly (canonical sizes)

Under precedents P-1…P-6, run 23/24's divergences resolve: **N24 M, N25 M** (P-1) · **N72 M** (P-2)
· **N69, N06 behavioural** (P-4) · **N29 M** (P-5) · **N82 unsizeable, 5 named holes** (P-6). The
one divergence no precedent covers — **N86 XL ↔ L** — is carried as the assembly's declared spread:
the total is computed at both readings and reported as a range.

## Registered expectations

1. **A0 closes.** Every id of the 68 product obligations and 5 work obligations has a visible
   outcome — priced · carried with its named missing parameter · or a named hole. No id silent.
2. **The layer is small before C3:** once + E1 + demanded items add **less than 15%** of the
   three-batch leaf total. **Root C3 becomes the single largest item of the estimate** — the price
   of the six-plus subtrees meeting, which no previous instrument ever carried.
3. **The mini-pair agrees on N17/N18** within one band.
4. **The assembly's internal spread is narrow:** the N86 range spans **less than ×1.03** on the
   grand total. What remains wide is *named and external to this run*: the uncalibrated table level
   (validity, FaxRxTx) and the structure axis (HM19-OA2 uncrossed, ×1.65 in nodes).
5. **Named holes at close, and no new ones:** N82 × 5 · A9-N05 · A9-N06 · K3-N68 (+ whatever the
   mini-pair refuses, which expectation 3 bets against).

## What run 25 is not

Not the project-estimate deliverable: that is the этап-2 document — this centre **plus** the
reference-class corridor and tail, steps B–D, the open-questions register and the unpriced-scope
list. And no number here is calibrated: every value is `external norm, uncalibrated v0.1` passed
through a measured size vector.

---

# Results

Inputs landed: the N17/N18 pair (`run25_raw/HD25-N17N18.md`) — **identical, L and L**, same five
enumerated regions, same P-5/P-6 exclusions; the `Hotyn-K` addendum row **W-R64 O 0.5 / M 1.5 /
P 4.0**, contamination clean, appended to `docs/rate_table.md` as Addendum A1. Arithmetic:
`run25_raw/assemble.py`.

## 1. The assembly

| component | N86 = L | N86 = XL |
|---|---:|---:|
| element leaf E (78-element tree + root's own items) | 907.08 | 914.78 |
| C3, all 18 parents | 371.35 | 374.43 |
| — of which **root C3** (the six-plus subtrees meeting) | **181.42** | **182.96** |
| once + E1 + W-R64 layer | 63.71 | 63.71 |
| **GRAND TOTAL, person-days** | **1342.13** | **1352.92** |

**Named holes, 8, identical in both variants:** A9-N05, A9-N06 (zero stated targets — the 1.4
filter; two open questions for the client) · N82 × 5 (P-6: a cardinality without named members —
model defect) · K3-N68 (R10 names no component — model defect). R10 is thereby priced almost
entirely by a hole: its one live item is D4-N68.

**The demanded-work branch closed under A0:** R69 → E4 (priced) · R70 → E3 (priced) · R02 → E7
priced, running the service **carried, missing parameter: the term** · R03 → O3 priced, operating
support **carried: the term** · R64 → W-R64 priced (E 1.75), the reviews themselves **carried: the
term**. No id of the 73 is silent.

## 2. Scoring the registered expectations

| # | expectation | outcome |
|---|---|---|
| 1 | A0 closes, no id silent | **CONFIRMED** — with R10 flagged: covered, but carried mostly by a named hole |
| 2 | layer < 15% of leaf; root C3 the largest single item | **CONFIRMED** — layer 7.0%; root C3 ≈ 181 pd, 13.5% of the total, the single largest item, and it is exactly the "nothing prices the subtrees meeting" gap runs 21–22 kept reporting |
| 3 | mini-pair within one band | **CONFIRMED** — identical (L, L; same enumerations) |
| 4 | assembly's internal spread < ×1.03 | **CONFIRMED** — the N86 range spans **×1.008** on the grand total |
| 5 | named holes exactly the predicted set, none new | **CONFIRMED** — the eight above, nothing else |

## 3. What the number is, and is not

**1342–1353 pd is the bottom-up centre of the BMS estimate on rate table v0.1** — external,
uncalibrated norms passed through a measured size vector (68 obligations → 78 elements → 553+ items
→ case-law classes), on **one** product model (HM19-OA1), with eight named holes and three carried
service obligations awaiting one client parameter (the term). It is reproducible to ×1.008 within
this chain — and it is **not yet the deliverable**: the этап-2 document owes the reference-class
corridor and tail, steps B–D, the structure axis (HM19-OA2, ×1.65 in nodes, uncrossed), and the
open-questions register around this centre.

For the record, with no cross-instrument conversion implied: the July manual estimate was 486 pd,
the methodless baseline ~1074, `Lytin-D 4.0` ~1626, and the judgement-priced `Hotyn-D 1.0` would
extrapolate well above all of these. Which level is right is the validity question — FaxRxTx first —
and nothing in this run touches it.
