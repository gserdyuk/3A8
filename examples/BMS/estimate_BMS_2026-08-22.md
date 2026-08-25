# BMS — the estimate, v1 — 2026-08-22

**The first complete answer this pipeline has produced in the format its methodology promised**:
a centre with its calibration, a corridor with its sources named, the outside view with its tail,
the scope that is *not* in any number, and the questions that move the answer. Written to be read
without the conversation behind it.

**Read this box before any number.**
- Every bottom-up figure rests on **rate table v0.1 — external industry norms, uncalibrated against
  any outcome**. The centre is "norms passed through a measured size vector", not a validated cost.
- The bottom-up stands on **one** product model (HM19-OA1). A second model of the same requirements
  differs ×1.65 in structure (run 19) and has not been priced; the structure axis is a named,
  unquantified width source.
- BMS is a training RFP. **No outcome exists**; nothing here is validated. The validation path and
  the fit-for-use gate are `docs/exit_criterion.md`; the first validation case is FaxRxTx.

---

## 1. The answer, three parts, not summable

| part | value (person-days, net, A1 scope) | what it is |
|---|---|---|
| **Centre** | **1899 – 1913** | the calibrated bottom-up: table-priced assembly 1342–1353 × the gap-blind Step C chain (×1.41): interface-risk residual + three named holes + scope volatility ×1.15 + cross-company friction ×1.12 + team-forming deficit |
| **Corridor** | **1611 – 2504** | the spread of the calibration rates (low/central/high) — **a naive band, not percentiles**, per the rate agent's own constraint |
| **Reserve** | **— none available — resolved as conditionality + priced options** | the raw class tail is P90 = 1650–2050; the centre already sits at ≈P87 (repeat 1) / above P90 (repeat 2), so the tail provides no headroom. **Resolution (author, 2026-08-22):** the bid is **conditional on the pinned readings** — a reversal is a scope change, not an in-price risk — **and carries the priced options table of §5a**, so the reserve decision is the client's, with a price on it |

**The outside view, for the same scope** (`Lytin-R 1.0`, two independent repeats):

| P10 | P50 | P80 | P90 |
|---|---|---|---|
| 420–650 | 800–1050 | 1250–1600 | 1650–2050 |

Right-skewed; class floor ≈ 350–500 pd; the pair's own spread is ×1.31 at P50, narrowing to ×1.24
at P90.

## 2. What the diagnosis established (run 27, Steps B–D)

- **The two methods disagree by ×1.28–1.69 at the centre, and the bottom-up is the high one** — the
  inverse of this pipeline's historical case. Corrections were gap-blind hole-fills, all upward:
  **explained share 0%**, stated in those words. The methods have not converged, and the report
  calls that the correct outcome, not a defect.
- The gap is attributed **directionally** to three named causes, none priceable by any rate:
  **D1** — the recursive assembly convention (C3 at 20% at all 18 parents; the ≈181 pd of
  root-level assembly alone spans 33–62% of the gap) — a modelling-rule question;
  **D4** — class assignment (the RC's own flag: its most likely error is upward; at the mildest
  up-neighbour factor its P50 brackets the raw base);
  **D6** — unit provenance (net vs assigned person-days), a **×1.25 lever on the whole comparison**,
  carried as two forks and applied in neither direction.
- **False convergence was checked in three frames and refused in all three**, including the
  seductive near-match of base×0.8 to repeat 1's P50 (within 3% — flagged as exactly what a unit
  artefact looks like when it masquerades as agreement).

## 3. What is inside the centre

68 pinned product obligations → 78-element product model → 553 crossed work items + whole-model
layer, priced by size classes counted from named things (repeat agreement ×1.000–×1.016 per batch).
Includes: construction and test-based assurance ×2 cycles per element · staged UAT ×2 + user
documentation at every screen-bearing subtree · integration at 20% of subtree leaf effort at all 18
parents **including the root assembly (~181 pd)** · environments ×3, pipeline, rehearsed promotion,
cutover, hosting set-up · security review + external pentest + remediation · seed data where stores
need pre-load · ops/user documentation, release notes, acceptance record · mobilisation, planning,
reporting, risk · the technology-currency policy (R64) · via the calibration: the audit-trail store,
the process-clarity residue, performance/DR verification, team-forming deficit, interface-risk
residual, scope volatility, cross-company friction.

## 4. What is NOT in any number, by name

1. **The continuing service** — running the hosted system (R02), operating support (R03), periodic
   technology reviews/upgrades (R64): carried on both sides, awaiting **the term**. Priced by a rate
   per unit time once the term exists — a different instrument.
2. **The four refused readings** (declared narrowings that may reverse): dozens of direct hotel
   integrations instead of 1–2 aggregators (A4) · own SMS infrastructure (A5) · mass re-booking
   during disruption (A8) · a configurable process engine behind "clear business processes". Each is
   a step change, not a multiplier — not in the base, and **priced as conditional options in §5a**:
   a row enters only if its trigger fires, at full magnitude with its netting rule.
3. **Three coverage verifications returned by the rate agent**: is DPA/privacy work actually carried
   by the 68 obligations · is the rate table's front-end baseline responsive or desktop-only · is
   there truly no legacy data to migrate. Any "no" is a new named hole, never a silent uplift.
4. **The structure axis**: the second product model (×1.65 in nodes) — unpriced width.
5. **Effort→calendar conversion** and team availability: a separate step, deliberately.

## 5. The decisions and questions that move this answer

**Two adjudications, each a single question, each moving more than any run could:**

1. **Unit provenance of rate table v0.1** — ✅ **adjudicated 2026-08-22: assigned working days**
   (`assumptions.md` A7 v3). Both sensors' sources are natively assigned-day, so the face-value
   comparison is the units-consistent one, both ×0.8 forks dissolve, and the ×1.28–1.69 centre gap
   is real. The diagnosis's most-suspicious near-coincidence (base×0.8 ≈ repeat 1's P50) is closed
   as an artefact of a conversion that does not exist.
2. **Class assignment** — ✅ **adjudicated 2026-08-22: conditional on the pinned narrowings
   (A4/A5/A8/A9 + single-client hosting), the class is the stated one, weight ≈ 1 for this bid's
   conditional scope.** Grounds — findings §11.4 applied as designed (decomposition as the
   membership test): the built 78-element model carries **every** structural membership branch both
   RC runs listed, and **none** of any neighbour's (no payment/PCI, no inventory management, no
   tenant billing or onboarding, no direct-integration fan-out, no migration). The neighbour mass is
   not smeared into the quantiles; it lives, named, in the four refused-reading step events —
   priced as conditional options by run 28. **Consequence for the diagnosis:** the class side of
   the gap closes; the ×1.28–1.69 face-value gap stands and attributes to the bottom-up side — the
   rate-table level (D2) and the root-assembly convention (D1) — which is exactly what the FaxRxTx
   validation tests next.

**The reserve decision — ✅ resolved (author, 2026-08-22), both halves:** the bid goes out
conditional on the pinned readings, *and* the gap-blind step-event round was run (run 28). Its
output is §5a below.

## 5a. Conditional option prices for the refused readings (run 28, `Lytin-K 1.0`, gap-blind)

**Client-facing option prices — not reserves, not contingency, not part of the centre or corridor.**
A row enters a total only when its trigger fires, at full magnitude with its netting; no probability
or expected value may be attached without a separately-sourced act. Bands are magnitude bands within
the fired reading, not confidence intervals; bands do not mix across events.

| event (trigger = the refused reading) | netting vs the base | low | central | high |
|---|---|---:|---:|---:|
| **E-1 · direct supplier integrations** instead of 1–2 aggregators | aggregator adapter stays by default (removal −9.9 only on explicit substitution) | 12.8 pd/integration + 45 once | 23.6 + 124 | 51.6 + 149 |
| — illustrative totals at N = 10 / 20 / 30 (N is the client's number, never a central case) | | 173 / 301 / 429 | 360 / 596 / 832 | 665 / 1181 / 1697 |
| **E-2 · own SMS infrastructure** instead of a gateway | gateway adapter replaced (−18…−20) | 60 | 178 | 239 · + separate switch 5/10/20: carrier commercial onboarding, zeroable |
| **E-3 · disruption-response capability** (mass re-booking) | none — purely additive; the technical reading stays | 112 | 212 | 288 |
| **E-4 · configurable process engine** | supersedes the narrow reading (H2 −5/−15/−40) | 117 | 192 | 252 |
| **X-13 · interaction** — only if E-1 **and** E-3 both fire | — | 12 | 22 | 37 |

Named and deliberately unpriced by the round: the E-3×E-4 interaction (sign unsourceable — an
engine-hosted disruption response could cut or raise E-3); money terms; schedule and team-shape
consequences (E-1 at N=20-high changes hiring, not just person-days); the tail failure scenarios of
the options themselves. Full derivations, netting rules and the six binding usage constraints:
`run28_raw/options.md`.

**For the client (from the open-questions register and the runs):** the term for R02/R03/R64 · the
two zero-target NFRs (what availability level? what volumes?) — currently verified by nothing
because the RFP names no number · R29 "automatic booking" vs R38 "hotel supplier booking is handled
manually" — both estimator pairs called this the largest basis risk · the R05 actor list omits hotel
suppliers while R38 gives them booking work · plus the pinned register's remaining questions.

**Known model defects (converged on by independent instruments):** the audit-trail store's
declaration counts things it never names · "clear business processes" names no component · two
statements carry unmeasurable NFRs — all three surfaced as refusals, priced via the calibration's
H-additions, and belong on the model owner's desk.

## 6. Provenance

`Hotyn-M 1.1` (product model, Opus) → `Hotyn-W 1.1` (crossing × technology declaration, catalogue
1.4) → `Hotyn-D 2.0` (size classification, Opus, case law P-1…P-6) × rate table v0.1 + addendum A1
(`Hotyn-K 1.0` × Fable 5, gap-blind) → assembly script → base branch {1342.13, 1352.92} ·
`Lytin-R 1.0` ×2 (outside view, Opus, gap-blind) · `Lytin-K 1.0` (Step C rates, gap-blind; via the
re-registered `rates-step-c` definition) · `Lytin-G 1.0` (Steps B–D, Opus). Runs 19–27; raw
transcriptions and scripts under `examples/BMS/run*_raw/`. Every isolation layer held; two protocol
findings are on record (the stale-definition load in run 23; the `gitStatus` injection caught by the
rates sensor in run 27).
