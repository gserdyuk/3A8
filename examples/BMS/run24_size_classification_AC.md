# BMS — Run 24: size classification of batches A and C, `Hotyn-D 2.0` — 2 × n=2

Date: 2026-08-22. **Registered before the runs returned.** Written after the catalogue 1.3
adjudication and before any output was read.

## Design

Two batches, two repeats each, identical prompts within a batch, launched together, Opus 5 by
explicit override. **The definition staleness of run 23 is closed**: a probe returned
`Hotyn-D 2.0` with the correct seven output sections before launch, so these are the first runs
through the real 2.0 definition.

First runs under **catalogue 1.3** — the three enumeration precedents (P-1 channel-as-protocol ·
P-2 name-token-only-if-uncovered · P-3 slash-outcomes) are in force, adjudicated from run 23's
divergences.

## Pinned inputs

- Work models: **HW21-A1** (25 elements, 154 items) and **HW21-C1** (25 elements, 195 items) — the
  repeat-1 crossings, pinned as the work models of record. The known crossing deltas of repeat 2 are
  carried as **declared sensitivities**, to be quantified by table arithmetic once classes exist:
  N06 statement↔store (±7 items) · N87 seeding applied↔declined (±3) · N60 surface↔statement ·
  N65 surface↔behaviour (0 items).
- Element data: id, name, class (from the pinned crossing), parent, own coverage with obligation
  texts verbatim from `requirements_product.md`; derived elements carry their recorded triggers as
  substance. No run outputs, no notes from other runs, no prices, no rate table.
- Special counts requested: batch A — A9 measurable targets on N04, N05, N06; G pre-load kinds on
  N86, N80, N81. Batch C — G pre-load kinds on N87.

## Decisions recorded with this run

1. **Catalogue 1.3** — the three precedents, author-approved 2026-08-22.
2. **N17/N18 reclassified to `statement-behavioural`** (author, 2026-08-22, per both run-23 sensors'
   diagnosis and run 21's own "contested"). Takes effect at the **whole-model assembly**: their
   batch-B items become K3+D4, and N16's subtree loses its surface-gated UAT/documentation items.
   **Not retroactive**: runs 22–23 stand as measured on the model as it was classified then.

## Registered expectations

1. **Executability**: all four runs produce the seven 2.0 sections, verbatim enumerations, and zero
   person-day figures. Primary.
2. **Identity per batch ≥90%**: A — identical outcome on ≥19 of 21 non-aggregates; C — ≥20 of 22.
3. **ΣE through the script ≤×1.05 per batch** (rate table v0.1, C3 = 20%, position sizes computed).
4. **Zero divergence on the three adjudicated boundaries** — the test that 1.3's precedents bind. A
   divergence on P-1/P-2/P-3 ground means adjudication does not transfer and case law is decorative.
5. **Statement kinds agree on ≥5 of the 6 batch-A statements.** The borderline pair is named in
   advance: N69 (SaaS/tenancy — property of delivery or run-time isolation mechanism?) and N08
   ("designed to grow" — pure intent). N04/N05/N06/N70 should be uncontroversial.
6. **Unsizeable ≤3 per batch, each naming its missing enumeration.** Candidates known in advance
   from run 21's substance findings: the R14 trio (N65–N67 — surfaces over a requirement the RFP
   left empty) and N08 (no countable constraint named).

## What this run cannot establish

One pair per batch; nothing about the level (table uncalibrated); nothing about batch-B; the
crossing-delta sensitivities are priced afterwards, not measured here.

---

# Results

Raw: `run24_raw/HD24-{A1,A2,C1,C2}.md`. Arithmetic: `run24_raw/price_run24.py`. All four runs
`tool_uses: 0`, contamination clean, stamped `Hotyn-D 2.0` (the probe held). Both A runs
independently elided R66's numeral from their own output while still counting the target — the
no-figures prohibition enforced by the sensors beyond the letter of the task.

## 1. The readings

| | batch A r1 | batch A r2 | batch C r1 | batch C r2 |
|---|---:|---:|---:|---:|
| elements sized / unsizeable | 20 / 1 (N82) | 21 / 0 | 21 / 1 (N68) | 21 / 1 (N68) |
| identical outcome (class+kind or same refusal) | **16 of 21** | | **22 of 22** | |
| ΣE leaf · C3 · **total** | 255.42 · 75.01 · **330.43** | 244.25 · 72.78 · **317.03** | 295.90 · 59.07 · **354.97** | same to the cent |
| holes | 7 (2 × A9 zero-targets + 5 × N82) | 2 (A9 zero-targets) | 1 (K3-N68) | 1 (same) |
| **ΣE ratio** | **×1.042** | | **×1.0000** | |

**Scope caveat on batch A's ×1.042, stated before anything else:** the two runs' holes differ — r1
refused N82 (5 items unpriced), r2 sized it (~6.96 pd + 1.39 C3). On matched scope (N82 removed from
both) the ratio is **×1.070**. The registered metric was the raw script ΣE, and both figures are
reported; the honest reading is "between ×1.04 and ×1.07".

**Pooled, all three batches** (B from run 23): r1 1033.10 · r2 1025.31 → **×1.008** — partly by
offset between batches, quoted only with that caveat. Per-batch is the honest unit.

## 2. Scoring the registered expectations

| # | expectation | outcome |
|---|---|---|
| 1 | executability, zero pd figures | **CONFIRMED** — all four runs |
| 2 | identity ≥90% per batch | **C: CONFIRMED, 100%** (22/22, first perfect pair in the project's history). **A: NOT CONFIRMED, 76%** (16/21) |
| 3 | ΣE ≤×1.05 per batch | **C: CONFIRMED, ×1.0000.** A: **×1.042 on the registered metric, ×1.070 scope-matched** — passed as registered, failed matched; both on record |
| 4 | zero divergence on adjudicated boundaries | **CONFIRMED** — P-1/P-2/P-3 applied identically in all four runs; every batch-A divergence sits on a boundary 1.3 does *not* cover |
| 5 | statement kinds ≥5 of 6 | **NOT CONFIRMED: 4 of 6.** N69 diverged as pre-named; N08 agreed as pre-named; **N06 diverged un-named** |
| 6 | unsizeable ≤3 per batch, enumeration named | **CONFIRMED**: A 1 (N82), C 1 (N68) — but the *predicted* candidates (N65–N67, N08) sized fine under P-2; the actual refusals were elsewhere |

## 3. Where batch A's five differences live — three new boundaries, none of them adjudicated yet

Every difference traces to a question catalogue 1.3 does not answer, and in each case **at least one
of the two runs pre-named the other's reading in its doubts**:

1. **The kind tie-break for mixed statements** (N69, N06 — behavioural↔compliance). Run 23's B pair
   used "the obligation that entails run-time behaviour decides"; A1 applied the same tie-break, A2
   read the architectural phrasing as configuration. Price consequence: K3-behavioural ≈ ×2.7 the
   compliance row. *Adjudication candidate P-4.*
2. **The unnamed catch-all** (N29 — "and other details": a kind or not). A1 counted it, A2 excluded
   it — and C1/C2 both excluded the same phrase at N47. The count-by-naming rule already implies
   exclusion; it was never stated as a precedent. *Candidate P-5: an unnamed catch-all is not a
   named thing.*
3. **A stated cardinality without named members** (N82 — "three amendment origins"). A1: not an
   enumeration → unsizeable (M10). A2: sized the narrow reading, gap recorded. *Candidate P-6:
   decide whether a bare count is countable.*

**The relocation law, now at case-law granularity.** Run 23's three boundaries were adjudicated;
all four run-24 runs honoured them perfectly and diverged only on boundaries the case law does not
yet cover. The freedom keeps relocating — but each relocation is now a one-line precedent instead of
a version of the method, and batch C shows what it looks like when the case law happens to cover
everything: ×1.0000.

## 4. Findings beyond the expectations

1. **The A9 driver has a zero case the catalogue does not handle.** Both A runs, independently and
   identically: N05 and N06 carry A9 items (the crossing judged the activity applicable) yet their
   obligations state **zero measurable targets** (R68, R63, R13 quantify nothing). Both refused to
   invent a target; both holes are named. Fix belongs in the catalogue: A9's applicability should
   require *at least one stated target*, moving the zero case from a pricing hole to a crossing
   filter — and the two zeroes are themselves questions for the client (what availability level? what
   volumes?).
2. **N68 refused by both C runs** with the same M10 diagnosis (R10 "Clear business processes" names
   no component), kind still recorded (compliance ×2). With run 23's N17/N18, the classifier keeps
   converging on the same holes in the product model.
3. **Six unresolved obligation contradictions surfaced** (three per A run, overlapping): R04
   sole-source vs CTC-driven R21/R31/R32 · R33 merge vs R44 override precedence · SSO regime vs
   suppliers-outside-SSO · R05's actor list omits hotel suppliers vs R38 · R67's test deferred to
   design stage · N56 vs N67 configuration surfaced twice. All are open-questions material.
4. **Closure violations: 10 distinct across A and C** (audit trail never written to · effective-dated
   config never read · retention never executed · no tenant entity · stated properties never
   measured · supplier account provisioning · N87 never populated · feedback never consumed ·
   amendment propagation between portals · incidents never resolved). The gap-finding capability
   scales with scope.
5. **Totals so far** (uncalibrated table v0.1, partial scope, holes named): A ≈ 317–330 · B ≈
   348–353 · C ≈ 355 → three batches ≈ **1030 pd ± the named holes**, whole-model layer and the
   N17/N18 reclass delta still uncrossed. **Not a project estimate** until those land.

## 5. What this run does not establish

Two pairs, one model each; the level (table uncalibrated); the crossing-delta sensitivities of
HW21-A2/C2 (priceable now that classes exist, not yet priced); nothing about the whole-model layer.
