# BMS — Steps B, C, D: diagnosing the divergence, parameter transfer, final range

Date: 2026-07-17. Inputs: [run1_decomposition.md](run1_decomposition.md) (E = 486 pd), [run2_reference_class.md](run2_reference_class.md) (P10 600 / P50 950 / P80 1400 / P90 1800).

## Step B — diagnosing the divergence

Center divergence: 950 / 486 ≈ **×1.95**. Per the methodology we do not average, but decompose across decomposition's known blind spots:

| Gap component | Decomposition's blind spot | Functional form | Estimate (from base rates, not fitting) |
|---|---|---|---|
| Scope growth from RFP detailing → delivered | Scope creep: the WBS estimates the RFP text of 2016-06-10, not what the project turns out to be | **Multiplicative** (grows the whole body of work) | ×1.25 (1.15–1.40); requirements creep ~1–3%/month × 8–12 months |
| Integration "icebergs" (CTC merge policy, the real quality of the aggregator API) | Systemic/integration risks: the WBS does not contain what is not in the text | **Targeted addition** — a multiplier only on the integration items (97.5 pd); in terms of the total sum this is an addition, not a proportion | ×1.5 (1.25–2.0) on the integration share → +30…+135 pd |
| Coordination / organizational overhead (meetings, approvals, waiting for access, fragmentation) | Organizational overhead: not tied to tasks, absent from the items' pd estimates | **Multiplicative** (proportional to volume and headcount) | ×1.30 (1.15–1.45); a class-typical focus factor ~0.7–0.85 |
| PM/BA over the real duration | The PM item of the WBS was implicitly scaled to an "optimistic" calendar | **Addition** (item replacement: 31 → 40–60 pd, linear in duration) | +10…+30 pd |
| An extra UAT cycle with an enterprise client | Organizational + systemic risk | **Pure addition** | +10…+40 pd |
| The fat right tail (P90 = 1800) | Risk correlation + events beyond any multiplier | **Not transferred at all** (see Step D) | — |

**A note on form (recorded from the project's author):** calibration is not a single number. Part of the cost is "items" that are not in the WBS at all, and a simple multiplier will not catch them: the "multiply and add" form is needed. The affine model y = a·x + b is not identifiable from one project (needs ≥2 points), so here the parameters are not *fitted* but *transferred* by name from external base rates — each with its own form. Fitting becomes possible in Phase 2, on one's own history from several projects/sprints.

## Step C — parameter transfer (mechanical calibration)

The chain (W = 455 pd of work without the PM item; integration share 97.5 pd):

| Step | low | central | high |
|---|---:|---:|---:|
| W × scope | 523 | 569 | 637 |
| + iceberg on the integration share | 551 | 630 | 774 |
| × coordination | 634 | 819 | 1122 |
| + PM/BA (recomputed) | 674 | 864 | 1182 |
| + extra UAT cycle | **684** | **884** | **1222** |

- Calibrated decomposition: **~884 pd**, range 684–1222.
- The total implied multiplier ×1.82 against ×1.95 for reference class — the components, taken from independent base rates, almost reproduce the class coefficient. This is cross-validation, not fitting: no component was chosen by looking at 950.
- Spread correction via risk correlation: at ρ = 0.3–0.6 between WBS items, σ grows from 17 to 45–61 pd (after calibration 82–112 pd) → P90 of the calibrated decomposition ≈ **990–1030 pd**.

## Step D — final range and explained residual

**Final Phase 1 estimate: center ~900 pd (884–950), working range P10–P80 ≈ 650–1400 pd.**
(~5.5–6 FTE × 7–9 months at the center of the scenarios.)

The residual, explained and unexplained:
- **Explained by parameter transfer:** ~93% of the center gap (486 → 884 out of 950); each component is named and tied to a blind spot.
- **Unexplained residual #1 — the center gap ~66 pd (7%):** either imprecision of the component base rates, or a share of tail scenarios sitting in the class median. Honest uncertainty, not noise.
- **Unexplained residual #2 — the tail:** P90 of the calibrated decomposition ≈ 1000 pd, class P90 = 1800 pd. The ×1.8 gap in the tail **is not removed by calibration in principle**: tail events (redoing the sync architecture, a change in the client's environment requirements) do not exist as WBS items with any multiplier. The tail is the unique contribution of reference class, and for contract decisions (fixed price vs. T&M, buffers) it is the one to use.

**A check against false convergence (METHODOLOGY §3):** there is no full convergence — the centers came together, the tails did not. This is the correct outcome: the methods answer different questions (what this work *usually* costs vs. what *happens* to such projects), and the residual tail divergence is their preserved diagnostic independence.

## Process findings of the run (for findings)

1. **Independence protocol:** run #2 was performed by an isolated subagent (RFP + assumptions only, without the numbers of run #1) — in one session the second run would be anchored. A requirement for Phase 1: each method is a separate session/agent.
2. **"Multiply and add":** the calibration of Step C is a composition of differently-shaped corrections (multipliers, targeted and pure additions), not a single scalar; the affine fit is unidentifiable on one point — until one's own history appears (Phase 2), the parameters are transferred from external base rates.
3. **Unintended validation:** the isolated agent independently named the typical range of RFP-stage bid estimates, 400–700 pd; our decomposition (486) landed inside it — confirmation that decomposition behaves like a typical RFP bid, and that its gap with reference class is a systematic feature of the class, not an error of this particular WBS.
