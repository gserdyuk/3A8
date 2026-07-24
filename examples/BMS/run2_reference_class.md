# BMS — Run #2: Reference Class Forecasting (outside view)

Date: 2026-07-17. Input: [BMS_extracted.md](BMS_extracted.md) + [assumptions.md](assumptions.md).

**Independence protocol:** the run was performed by an isolated agent in a separate session, given only the RFP digest and the assumption log. The results of run #1 (decomposition) were not shown to the agent — to avoid anchoring (see findings §1: anchoring is stronger in LLMs than in humans). The text below is the agent's answer with no substantive edits.

---

## 1. Reference class

**Definition:** custom development of a medium-size enterprise web application (a multi-portal B2E/B2B system with approval workflows and 4–6 external integrations), performed by an external supplier under a fixed-scope contract, estimated at the **RFP stage** (before detailed requirements analysis, the widest part of the "cone of uncertainty").

**Why this one:**
- Technologically this is not a product innovation and not a "big" IT project (>$15M): the typical class "corporate portal + integrations + workflow." The low transaction load (5000 bookings/year) rules out the class of high-load systems.
- The class's key effort drivers are not "features" but: (a) the number of external integrations, (b) the number of roles/portals, (c) an enterprise client with formal approvals and UAT, (d) SaaS obligations (HA/DR, security). On all four the project is the middle of the class, not the edge.
- The estimation stage (RFP) is a critical feature of the class: it is where the systematic error of estimates is at its maximum.

## 2. Class base rates and anchors

**Absolute anchors:**

| Anchor | Value | Confidence |
|---|---|---|
| Typical duration of class projects to first production release | 6–12 calendar months | High |
| Typical team | 5–8 people, ~5–6.5 FTE effectively | High |
| Absolute class range | 5.5 FTE × 21 pd/month × (6…12 months) ≈ **700–1400 pd**, center ~950–1000 pd | Medium |
| Typical RFP budget of such systems at vendors in 2016 | $250–700k at a blended rate of $300–400/day → ~700–1800 pd sold; the bid estimates themselves are usually 400–700 pd | Medium |

**Relative base rates (overrun relative to RFP-stage estimates):**

| Source | Base rate | Confidence |
|---|---|---|
| Boehm, "cone of uncertainty" | at the RFP stage the actual result is ×0.5…×2 of the estimate; systematically biased upward (competitive pressure lowers the bid) | High in form, medium in numbers |
| Standish CHAOS (2000s–2015) | average cost overrun ~45–60%, time overrun ~70–80%; projects <$1M are statistically more successful than large ones | Medium (methodological criticism is known, the order of magnitude is stable) |
| McKinsey–Oxford (2012) | large IT projects: +45% to budget on average; 17% are "black swans" with overruns >200%. The project is below the sample threshold ($15M) → discount the average, the tail applies | Medium-high for the form |
| Flyvbjerg (IT sample, fat tails) | median IT overrun ~10–30%, but a heavy right tail: ~18% of projects go past +50% | High (methodologically the cleanest source on form) |
| Industry experience with fixed-price RFP | the winning RFP estimate is undervalued by 20–40% against the honest internal one; integrations are the main source of the tail | Medium (practical consensus) |

**Synthesis:** the median of the real result ≈ typical RFP estimate (500–650 pd) × 1.4–1.6; the absolute anchor (team × months) independently gives a center of ~950–1000 pd. The two anchors converge.

## 3. Distribution (person-days)

| Quantile | Estimate | Class scenario |
|---|---|---|
| **P10** | **≈ 600 pd** | Integrations work as documented, approvals do not block, UAT in one cycle. ~5.5 FTE × 5–5.5 months. ~10–15% of class projects finish this way |
| **P50** | **≈ 950 pd** | RFP estimate × ~1.5; matches the anchor 5.5–6 FTE × 8 months. Usual scope growth on detailing, 1–2 surprises in integrations, 2 UAT cycles |
| **P80** | **≈ 1400 pd** | One integration is actually not ready, the client reshapes the workflow at UAT, NFRs add a cycle. ~6 FTE × 11 months |
| **P90** | **≈ 1800 pd** | Entering the fat tail (not a black swan — those are past P95): ×2 to the median = the top of Boehm's cone. A change in the client's environment requirements (CTC), a redo of the sync, a drawn-out UAT. ~6.5 FTE × 13–14 months |

The asymmetry is deliberate: P50−P10 = 350 pd, P90−P50 = 850 pd — a consequence of the class's right-skewed shape, not of feature analysis.

## 4. The method's assumption log (does not account for, by construction)

1. **The specifics of this team** — the class averages over all teams; a team's first joint project is usually to the right of the median of its future performance.
2. **The specifics of these integrations** — "CTC and UPSA are documented" is taken as given; the class only says that such assumptions are false often enough to inflate P80/P90.
3. **The real complexity of specific features** (merge policy, search prioritization) — there was no decomposition; the method will not see anomalously complex/simple features.
4. **The quality of the specific client** — an average enterprise is used.
5. **The dating of the base rates** — the sources aggregate different eras and methodologies; applicability to 2016 is assumed without correction.
6. **Management interventions** (de-scoping, T&M instead of fixed-price) — may cut the right tail; the method describes the class "as is."
7. **Misclassification** — the method's main risk: if the project is closer to the class "integration platform," P80/P90 are underestimated.
