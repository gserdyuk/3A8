# FaxRxTx — Run 3: Diagnosing the divergence and mechanical calibration (Steps B, C, D-preliminary)

**Method:** decomposing the gap between decomposition (run1) and reference class (run2)
across decomposition's structural blind spots; transferring external base rates onto the
run1 WBS without fitting to the class P50.
**Input:** SYSTEM.md, assumptions.md, run1_decomposition.md, run2_reference_class.md.
FACT.md, findings.md, METHODOLOGY.md, REQUIREMENTS.md, the BMS directory were not opened;
web search was not used. The methods' results were **not averaged**.
**Run date:** 2026-07-17.

---

## Step B.1 — The raw divergence

| Metric | Decomposition (run1) | Reference class (run2) | Gap |
|---|---:|---:|---:|
| Center | E ≈ **111.6 pm** | P50 ≈ **160 pm** | **+48.4 pm** (×1.43) |
| Tail | E + 2σ ≈ **120.5 pm** | P90 ≈ **320 pm** | **+199.5 pm** (×2.66) |
| Lower edge | E − 2σ ≈ 102.8 pm (honest ΣO = 51) | P10 ≈ 85 pm | the class is below the "narrow" edge of the WBS |

The character of the divergence is typical: the centers diverge moderately (~1.4×), the tails —
by a multiple (~2.7×). This is the expected signature: part of the center gap is systematically
undercounted work (fixable by calibration), and the tail gap is events
that are not in the WBS as items (unfixable by calibrating multipliers, see D.5).

Separately: the narrowness of run1's E±2σ is an artifact of the leaf-independence
assumption, acknowledged by run1 itself; it is not what should be compared with the class P90 — and that is exactly why
the tail gap is decomposed separately from the center gap.

---

## Step B.2 — Which blind spots are already partly covered by WBS leaves

The check is needed to avoid assigning a correction for what is already counted (double counting).

| Decomposition's blind spot | What covers it in the run1 WBS | What stays open |
|---|---|---|
| Immersion in a new domain | Section 1 entirely (1.1–1.4, **13.9 pm**) — unusually honest for a WBS | Only the unknown unknowns surfacing *during the build* (fax-protocol quirks, machine compatibility, line quality) — leaf 1.1 does not cover them by definition |
| Integration tests on live traffic | Section 8 (8.1–8.4, **13.7 pm**), including the traffic-duplication framework and comparison with v1 | The length of the "last 10%" convergence tail on the live stream — the foreseeable part is counted, the tail underestimation remains |
| Organizational overhead | Leaves 9.1–9.2 (**10.2 pm** ≈ 9% of the sum) — QA regression and PM/scrum | The systemic tax beyond QA/PM: onboarding, waiting for decisions, changes of priority, context switches |
| Graph edges (integration of the parts) | Explicit edge leaves: 3.1, 4.7, 7.1, 8.1, 8.3 ≈ **14.6 pm** | The combinatorics of interactions is wider than the list: the missing edges (workers↔core↔Lustre↔DB↔NOC, degradations at the seams) |
| Burst/load | Leaf 2.7 (load testing, 3.25 pm) | A correlated rework of the core if the first watchdog/token scheme does not withstand real failures (run2: a typical class event) |
| Scope creep | Leaf 4.6 (reserve for 1–3 forgotten formats, 1.67 pm) — pointwise | The general scope growth of "reworks to management's taste": wishes for the NOC, portal, reporting |
| Tail events (failure scenarios) | Nothing | Fully open — they do not exist as WBS items (see D.5) |

Implications for calibration: **do not** introduce a "domain immersion" correction,
**do not** introduce a separate "integration tests" item, **do not** introduce the full
organizational tax (only the residual beyond 9.x), compute the edge item
**net of** the 14.6 pm already counted.

---

## Step B.3 — Decomposing the center gap into named items

The rates are taken from general engineering base rates and justified independently;
no fitting to P50 = 160 was done (the sum check is in Step D.1).
Notation: "the build" = sections 2–8 (Σ E = 87.5 pm); "the nodes" = the build minus
the explicit edge leaves (87.5 − 14.6 = 72.9 pm).

### (a) Pure additions — work that is not in the WBS at all

| ID | Item | Base of application | Rate (range / center) | Rate justification | Contribution, pm (center) |
|---|---|---|---|---|---:|
| D1 | Domain unknown unknowns: fax-protocol quirks (T.30 and relatives), fax-machine fleet compatibility, line quality, encodings/anomalies of inbound email | the build, 87.5 pm | 5–15% / **10%** | The typical share of "discovered in the process" work for a team entering the telecom domain for the first time; leaf 1.1 covers what is *studied in advance*, not what is discovered under traffic. Mitigated by v1 as an oracle (otherwise it would be 15–25%) | **+8.8** |
| D2 | Missing integration edges: the seams workers↔core↔DB↔Lustre↔NOC, the behavior of the seams under partial failures | the nodes, 72.9 pm | integration ≈ 20–30% of the nodes, minus the 14.6 pm already counted / **25%** | The classic share of inter-component integration in a system of ~8–10 subsystems communicating through the DB and an API. 25% × 72.9 = 18.2 pm of expected edge work; 14.6 already in the WBS → a deficit of 3.6 | **+3.6** |

### (b) Targeted multipliers on subsets of leaves

| ID | Item | Leaves (Σ E) | Multiplier (range / center) | Rate justification | Contribution, pm (center) |
|---|---|---|---|---|---:|
| D3 | A correlated rework of the distributed core: the first watchdog/token/lease-logic scheme does not survive real failures, the redesign cycle touches 2.1–2.4 simultaneously | 2.1–2.4 (16.4 pm) | ×1.3–1.5 / **×1.4** | The base rate of home-grown guaranteed-delivery layers before the broker era: one big rework cycle after meeting real failures is the norm, not the tail. The PERT-P of each leaf covers "this leaf is harder," but not a simultaneous redesign of four leaves (this is exactly the center component of risk correlation) | **+6.6** |
| D4 | Rendering stabilization via the printer driver: hangs of office applications, leaks, the non-determinism of DOC/XLS/PPT automation of the mid-2000s | 4.2–4.6 (11.5 pm) | ×1.2–1.3 / **×1.25** | Automating printing of office formats of that era is a known source of drawn-out stabilization beyond "integration by the manual"; part is already in the M/P of the leaves, the multiplier is only on the systematic shortfall | **+2.9** |
| D5 | The convergence tail with v1 on live traffic: waves of discrepancies, rediscovery of v1's implicit fixes | 8.2–8.4 (9.3 pm) | ×1.25–1.5 / **×1.35** | A property of the rewrite class: a significant share of v1's behavior is unwritten edge fixes; comparison on the live stream mercilessly converts them into work. The framework (8.1) is left untouched — it is counted honestly | **+3.3** |

### (c) Global multipliers

| ID | Item | Base of application | Rate (range / center) | Rate justification | Contribution, pm (center) |
|---|---|---|---|---|---:|
| D6 | Scope creep: the scope growth of "reworks to management's taste" — wishes for the NOC/portal/reporting along the way | everything after (a)+(b), minus the completed section 1 → 122.9 pm | 8–15% / **10%** | The industrial requirements-growth rate ~1–2%/month for internal projects; here we take the lower edge in per-project terms: v1 fixes a functional anchor, and reserve 4.6 already covers the pointwise creep of formats | **+12.3** |
| D7 | The residual organizational tax: onboarding, waiting for decisions, context switches, "pressure without a deadline" (A8) | the total after D6 → 149.1 pm | +3–5% / **+4%** | The full coordination tax of a blended team ~12–15%; leaves 9.1–9.2 already carry ~9% — the residual 3–5% | **+6.0** |

**Order of application:** additions and targeted multipliers → creep → org tax
(creep work also requires coordination, the reverse order would understate D7).

---

## Step C — Mechanical calibration (parameter transfer onto the run1 WBS)

| Step | Operation | pm |
|---|---|---:|
| 0 | Σ E run1 (without corrections) | 111.6 |
| 1 | + D1 (domain unknown unknowns, 10% × 87.5) | +8.8 |
| 2 | + D2 (edge deficit, 25% × 72.9 − 14.6) | +3.6 |
| 3 | + D3 (core 2.1–2.4 ×1.4) | +6.6 |
| 4 | + D4 (rendering 4.2–4.6 ×1.25) | +2.9 |
| 5 | + D5 (convergence 8.2–8.4 ×1.35) | +3.3 |
| | *intermediate* | *136.8* |
| 6 | + D6 (creep 10% × (136.8 − 13.9)) | +12.3 |
| 7 | + D7 (org residual 4% × 149.1) | +6.0 |
| | **Calibrated decomposition center** | **≈ 155 pm** |

**The parametric calibration bracket** (all rates at the lower / upper edges
of their independently justified ranges, the same mechanics):

- lower edge: ≈ **138 pm** (D1 5%, D2 20% → ~0, D3 ×1.3, D4 ×1.2, D5 ×1.25, creep 8%, org +3%);
- upper edge: ≈ **177 pm** (D1 15%, D2 30%, D3 ×1.5, D4 ×1.3, D5 ×1.5, creep 15%, org +5%).

Given that the multipliers also scale the spread of the leaves, and correlation
(run1, blind spot #1) widens it further, the working range of the
calibrated decomposition estimate: **≈ 135–180 pm, center ≈ 155 pm**.

A note on identifiability: we have one external point (the class P50) and
seven parameters — fitting would give infinitely many "solutions," so all
rates are transferred by name from general base rates, and the sum is only *checked*
against the class after the fact (the next step).

---

## Step D (preliminary) — The result with an explained residual

### D.1 The explained share of the center gap

| | pm |
|---|---:|
| Center gap (160 − 111.6) | 48.4 |
| Explained by items D1–D7 (155.1 − 111.6) | 43.5 |
| **Explained share** | **≈ 90%** |
| Unexplained center residual | ≈ 4.9 |

The residual ~5 pm is inside the noise of the rates (the calibration bracket 138–177 covers P50
from both sides). Its honest candidate carriers, indistinguishable on these data:
(a) the class median may have been slightly inflated by the greenfield admixture of candidate B
(run2 itself notes this); (b) the strength of the specific Venali team — a quantile in either
direction; (c) the coarseness of the base rates themselves.

**A caution against false pointwise convergence.** The center 155 is close to
P50 = 160, but this is largely a consequence of choosing the *midpoints* of independently
justified rate ranges; the honest statement is interval: the calibration
bracket (138–177) intersects the neighborhood of the class P50. The methods converged
in ranges, not in a point — a pointwise coincidence would itself be suspicious.

### D.2 Tails: why the class P90 is unreachable by multipliers on the WBS — here too

Even the upper edge of the calibration (all seven rates at their maxima at once) gives
≈ 177 pm against P90 ≈ 320. To get 320 from the WBS, a global
multiplier of ×2.9 to the raw E (×2.1 to the calibrated) is needed — no item with
a justifiable base rate gives such a thing, and this is not a defect of the rates
but a structural fact: **multipliers scale existing leaves, while the mass of the
class P50→P90 consists of discrete events that have no leaf**:

- a second full rework of the orchestration (not the D3 cycle, but a change of architecture);
- a cutover postponed by waves of discrepancies on live traffic — months
  of parallel operation of v1+v2 with double support;
- the second-system sweep (DHT ambitions), materializing into an over-complicated core;
- the organizational disruptions of this specific company: the patent lawsuit with j2,
  the sale of the business — a change of priorities/financing mid-project.

Such events are a change of regime, not a rise in the cost of items; they are unrepresentable
in the WBS in principle. Therefore the right tail is taken **only** from reference class, and
no calibration of decomposition replaces it.

### D.3 The final recommended range for a decision

| Quantity | Value | Source |
|---|---|---|
| Planning center | **≈ 155 pm** | Calibrated decomposition (structure from run1, rates from external base rates) |
| Working planning range | **≈ 135–180 pm** | The parametric calibration bracket |
| Optimistic floor (not a plan!) | ≈ 110–120 pm | Raw E run1: the scenario "not one base-rate item fired"; the class P10 (85) is to be considered unreachable for this team in this domain |
| Reserve / right tail | **P90 ≈ 320 pm** | Reference class only; in the risk budget and the stopping criteria — from there |
| Probability of "v1 was never decommissioned within a reasonable term" | ~15–30% | Reference class only (the P99 tail of run2); the WBS does not contain this outcome |

Usage recommendation: commitments and work breakdown — by the calibrated
decomposition (135–180, center 155); reserves, stage-gates, and "stop/reconsider"
criteria — by the class tail (up to 320). The difference between
180 and 320 is not "a margin just in case" but the probabilistic mass of the discrete
events from D.2, managed not by estimation but by early checks (the first cycle
of live traffic through the core as a kill criterion for the watchdog/token scheme).

### D.4 The unexplained residual (an honest measure of uncertainty)

1. ~5 pm of the center gap — not attributed on these data (class admixture /
   team strength / coarseness of the rates).
2. The entire mass of the P50→P90 tail (~160 pm) — exists only in the outside view;
   the inside model does not reproduce it and should not.
3. The strength and composition of the team (A3 deliberately does not fix it) — a shift by a quantile
   in either direction.
4. The observability of v1 as an oracle (logs, capturability of behavior) — determines
   whether D1 and D5 are closer to the lower or upper edges of their ranges.
5. Venali's org dynamics (the lawsuit with j2 from 2006, the sale in 2010) — a specific factor
   with dates, visible to both methods only as an anonymous tail.
6. The two-sided error of the class itself: if the run2 median is inflated by the
   greenfield admixture, the "true" gap is smaller and the calibration is slightly
   over-corrected.

Full convergence was not the goal and was not achieved: the center residual is
fixed, the tail gap is explained structurally and left to reference
class. A pointwise coincidence of the methods would be a signal of fitting, not of accuracy.

---

*The file was generated by an isolated diagnosis/calibration run. FACT.md,
findings.md, and the other project files were not opened.*
