# Run 27 — Step C rates, `Lytin-K 1.0` (via the re-registered `rates-step-c` definition)

Transcribed from the sensor's reply, condensed only where marked. `tool_uses: 0`. Model: Opus 5
(orchestrator-recorded). Gap-blind: the task carried no class forecast, no quantiles, no target, no
gap. Pairing recorded by the run itself: `Lytin-K 1.0` rates over
`Hotyn-M 1.1 / Hotyn-W 1.1 / Hotyn-D 2.0` × rate table v0.1 — not transferable to another chain
without re-derivation.

## Contamination advisory — a pipeline defect, found by the sensor

**The task prompt was clean; the ambient context was not.** The harness auto-injected a `gitStatus`
block whose recent-commit subjects include *"the x1.97 gap is coverage"* — a gap-shaped ratio from
the Lytin era. The run quarantined it (named it, did not use it, noted it belongs to a different
engine generation), proceeded rather than hard-stopping, and recommended the standing fix:
**re-issue Step C sensors in a context with `gitStatus` and commit subjects stripped.** Recorded
here as run 27's protocol finding; every sensor launched from a session anchored in this repository
receives the same injection.

## The corrections (verbatim values)

| name | blind spot | form | low | central | high | source (condensed) |
|---|---|---|---|---|---|---|
| **G1** scope volatility | new obligations beyond the 68, RFP-stage under-specification, reading-change churn (merged: generic omitted-category residual) | **global** | ×1.08 | ×1.15 | ×1.28 | Capers Jones creep 1–2%/month; PMI incidence; McConnell cone. Reduced from generic ×1.12/1.22/1.35 for the 68-pinned-obligation discipline |
| **G2** cross-company coordination friction | A6: approval latency effort, specialist chasing, late-feedback rework, UAT participant churn | **global** | ×1.06 | ×1.12 | ×1.22 | COCOMO II SITE/TEAM. Vendor-internal coordination already priced; residual is the multi-company axis only |
| **T1** external-interface realisation risk | residual beyond PERT-P on 6+2 counterparties | **targeted** ×[…] on the 8 interface elements + their contract tests + their own assembly share (×1.2) — **never** on the ≈371 pd integration line | ×1.20 | ×1.40 | ×1.75 | COCOTS; COCOMO II PVOL. Two counterparties are client-internal systems whose documented-API status is an assumption |
| **H1** audit-trail store construction | named hole (N82) | **addition, pd** (assembly-inclusive; no further 20%) | 12 | 19 | 34 | priced on the run's own pinned table, store ≥M, ×1.2 assembly |
| **H2** "clear business processes" realisation, narrow reading | named hole (N68) | **addition, pd** (once-layer character, no assembly) | 5 | 15 | 40 | broad reading (a configurable process engine) excluded — a scope event for the tail |
| **H3** performance & availability verification | named hole (A9 zero-target statements) | **addition, pd** (once-layer character) | 10 | 22 | 45 | ~5–10% of test effort norm; low stated volumes; DR rehearsal dominates. **Blocked on two client questions** |
| **A-RAMP** new-team forming loss | mobilisation priced once; the productivity deficit is not | **addition, pd, outside both globals** | 20 | 45 | 85 | Tuckman/Brooks/COCOMO II TEAM; 5.5–6.5 FTE × 20–40 days forming × 20–35% deficit, low end shaded −10% for overlap with priced mobilisation |

## How the coverage report moved the rates (the §12a fix, working)

Against a generic bottom-up the sensor would have emitted: omitted-categories ×1.20–1.30 global ·
integration +10–20% · test-cycle +10–15% · environments 30–60 pd · documentation 20–40 pd ·
security 15–30 pd · seed data 10–25 pd. **All seven removed entirely** — the composition carries
them. G1, G2, T1 reduced from their generic bands (stated side by side in the raw reply). The three
named holes are priced at full weight — "the estimate flagged them and did not price them, so they
are unambiguously mine."

## The partition (26 rows, condensed to the boundary calls)

Carried (no correction): integration incl. root · delivery-process internals · environments/release
· test cycles & defect rework · UAT · documentation · security · seed data · elaboration of the 68.
Open (the corrections above): the three holes, ramp-up deficit, A6 residual, scope volatility,
interface residual. Other sensor: refused-reading step changes and failure events (tail) ·
rate-table calibration status (spread — "I do not know the sign of any table bias and inventing one
is exactly the failure my definition exists to prevent") · effort→calendar conversion (staffing).
Not calibratable: the carried service (needs "the term") · the 1342/1353 branch (an adjudication
debt — preserve as a discrete branch, never smooth into low/high). Flags returned, not priced:
DPA/privacy work presence · responsive baseline of the rate table · legacy-migration absence —
each "presumed carried; if not, it is a hole and comes back as an addition, never absorbed into G1."

Four boundary warnings stated for the applier: elaboration-of-the-68 vs arrival-beyond-the-68 ·
defect rework vs changed-requirement rework · G2 is the *people*, T1 is the *artifact* (same
counterparties, disjoint mechanisms) · mobilisation set-up vs forming deficit.

## Order of application (fixed; the applier has no discretion)

B ∈ {1342.13, 1352.92} carried as a discrete branch throughout.

1. **T1** on the interface subset only → record ΔT1 in pd.
2. **+ H1 + H2 + H3** (inside the globals — base-like scope).
3. **× G1**, 4. **× G2** (commuting; order fixed for comparability).
5. **+ A-RAMP** last, outside both globals (one-time cost, not proportional).

Constraints: low-with-low / central-with-central / high-with-high only as a naive band — **the
compounded high is not a percentile and no distributional claim is made**; the §4 tail items are in
none of these numbers; the global count is capped at two — any third global overlaps and must merge;
the sensor computed no calibrated total and offered no view on whether the base is high or low.
