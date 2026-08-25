# BMS — Run 23: two size classifications of one work model, `Hotyn-D 2.0`

Date: 2026-08-22. **Registered before the runs returned.** Everything above the results line was
written while the two agents were launched.

## What this measures

The first outing of the rate-card design (`docs/proposal_rate_card.md`): the estimator stops
producing person-days and only **classifies**. Two runs of `Hotyn-D 2.0` on the **batch-B work
model** (run 21 — the batch whose two crossings were identical, item for item), then a script joins
the classes to the pinned `docs/rate_table.md` v0.1 and computes ΣE outside any LLM.

Comparison target from the previous instrument: `Hotyn-D 1.0` on the same work model gave
**×1.288 on ΣE** between two identical runs (run 22), the whole gap in sampled price per leaf.

## What the sensor is given, and what it is not

Given: the 27 batch-B elements — id, name, class (from the identical crossings), parent, own
coverage with the **texts** of the covered obligations — and the sizing rules of catalogue 1.2 §3a
(enumeration definitions, S/M/L/XL thresholds, statement kinds, the two special counts this batch
needs: A9 measurable targets on N16, seeded entity kinds on N43).

**Not given, by design:** the rate table (a classifier that has seen prices can steer classes toward
a total), any person-day figure, any team or duration, any prior run's output. Position-derived
sizes (per-parent buckets, model bracket) are the script's arithmetic, not the sensor's judgement.

Both runs: the real `work-estimator` definition (2.0, `tools: Glob`), identical prompts, launched
together, neither told of the other. Model: Opus 5, recorded by the orchestrator.

## Division of labour, stated before the numbers

| quantity | produced by |
|---|---|
| size class of each sized element (drives K1, K2, K3, A2, A3, A4, A10) | **sensor** (count by naming) |
| statement kind of N16 (compliance / behavioural) | **sensor** |
| A9 measurable-target count (N16) · seeded entity kinds (N43) | **sensor** |
| D4 size (requirement ids in own coverage) | **script** — mechanical from the coverage sets |
| per-parent buckets (A5–A8, D2, U1–U3, O1) · surface and store+interface counts per subtree | **script** — tree arithmetic |
| every person-day figure, C3, ΣE, per-requirement projection | **script × rate table v0.1** |

21 of 27 elements are sized (aggregates never are): 10 behaviour · 6 interface · 4 surface ·
1 statement · 1 store.

## Registered expectations

1. **Executability, the primary reading.** Both runs produce the sizing table with a verbatim
   enumeration for every sized element, and **zero person-day figures anywhere in the output**. A
   single effort figure with a unit is a hard failure of the 2.0 design, whatever else succeeds.
2. **P1, identity half: size classes identical on ≥19 of 21 elements (≥90%).** Below 17 of 21 means
   the drivers are not countable as written — a catalogue defect (the registered failure condition
   of proposal §8.1), and the design holds only if fixing the drivers fixes the spread.
3. **P1, level half: ΣE through the script differs ≤×1.05** (was ×1.288 under 1.0). With one work
   model, one table, and position sizes computed, ΣE can differ only through the classes of
   expectation 2 — so this bound tests that the residual class disagreements are few and cheap.
4. **P3, localisation: every ΣE difference traces to a named enumeration difference** — a visible
   item present in one run's list and absent from the other's — never to an unexplained level.
5. **N16's kind agrees between the runs.** It is the only statement, it carries K3 and A9, and
   run 21 flagged it as the most fragile classification in the batch.
6. **Continuity, soft: at least one run names the R29/R38 contradiction** among its doubts (both 1.0
   runs called it the largest basis risk; the texts are unchanged, so a reader of the same texts
   should see it), **and the closure-violation lists stay non-empty**, naming product-model gaps
   consistent with the seven of run 22.

## What this run cannot establish

- One pair, one batch, one model: a difference, not a spread.
- Nothing about validity: the table is uncalibrated external norms; ΣE agreement between runs says
  nothing about ΣE being right.
- P2 (the cross-model bound, ≤×1.15) needs a Sonnet-classified pair and is a separate run.

---

# Results

Raw: `run23_raw/HD23-B1.md`, `HD23-B2.md`. Arithmetic: `run23_raw/price_work_model.py`. Both runs
`tool_uses: 0`, contamination clean.

## 0. Protocol defects, recorded before the numbers

1. **The harness loaded the stale definition.** Both runs executed `Hotyn-D 1.0`'s definition — the
   2.0 text had been written to disk minutes before launch and was not yet picked up. Both runs
   caught the mismatch, executed the task-pinned 2.0 sizing rules, produced zero person-day figures,
   **stamped 1.0 and refused to adopt the task's 2.0 designation**. These readings are honestly
   "the 2.0 rule set carried by the task over a 1.0 definition"; the next batch should verify the
   registered definition with a probe before launch, as the Lytin protocol always did.
2. **The task header said "Elements to size: 21"; the true count is 22.** My arithmetic error in the
   prompt and in the registration above (the registration's "≥19 of 21" inherits it). **Both runs
   caught it independently and sized all 22 rather than dropping one to satisfy the header.**
3. **The pricing script initially dropped N38 and N42** (185 items instead of 197). Caught by the
   item-count crosscheck against run 21's 197 before any number was read as a result; fixed, rerun.
4. **Model coordinates, checked after the author queried them (2026-08-22).** Run 22's ×1.288 was
   Opus (`compare_run22.py` header); run 23's pair ran on **Opus 5 by explicit override** — so the
   ×1.288 → ×1.016 comparison stays within one model. The one Fable-produced artifact in this chain
   is the **rate table itself** (`Hotyn-K 1.0` × Fable 5 — launched without an override, inherited
   the session model; its header now carries the stamp). The deferred P2 is registered against the
   historical pair specifically: **Opus ↔ Sonnet**, since that is the pair the ×2 was measured on.

## 1. The readings

| reading | repeat 1 | repeat 2 |
|---|---|---|
| elements presented / sized / unsizeable | 22 / 20 / 2 | 22 / 20 / 2 |
| identical sizing outcome (class or refusal) | **19 of 22** | |
| size classes differing | 3 — N24, N25 (S↔M), N72 (L↔M) | |
| unsizeable, both runs, same diagnosis | **N17, N18** — surface class, zero user tasks named | |
| N16 kind (statement) | behavioural | behavioural |
| special counts (N16 targets · N43 pre-load) | S · M | S · M |
| items priced by the script (of 197) | 187 + 10 named holes | 187 + the same 10 holes |
| ΣE leaves · C3 · **total** | 289.75 · 57.95 · **347.70** | 294.43 · 58.89 · **353.31** |
| **ΣE ratio** | **×1.016** | |

Per-requirement projection: **24 of 27 rows identical to the cent (×1.000)**; the three that move are
R18/R19/R24 (×1.77 — N72's class) and R26/R27 (×1.26 — N24/N25's class). Both disagreements were
**pre-named by both runs in their own doubts sections** — each run listed the other's reading as the
plausible alternative before any comparison existed.

## 2. Scoring the registered expectations

| # | expectation | outcome |
|---|---|---|
| 1 | executable, zero person-day figures | **CONFIRMED** — both runs; each also cleared R66's "2 seconds" explicitly as product substance, not effort |
| 2 | identical on ≥19 of 21 (≥90%) | **CONFIRMED on the registered count** (19 identical), narrowly short of the 90% form once the denominator is corrected to 22 (86.4%). The failure condition (<17) is far away |
| 3 | ΣE ≤ ×1.05 | **CONFIRMED: ×1.016**, against ×1.288 for judgement pricing of the same work model (run 22) |
| 4 | differences localise to named enumerations | **CONFIRMED** — two decisions carry everything: "does a named channel count as a protocol concern" (N24+N25, one decision applied twice) and "is a name token an action" (N72). No unexplained level anywhere |
| 5 | N16 kind agrees | **CONFIRMED** — behavioural in both, same justifying phrase |
| 6 | R29/R38 contradiction named · closure lists non-empty | **CONFIRMED** — both runs flagged N37-vs-R38; 7 violations each, overlapping run 22's list and adding four new ones |

**Honest cap on the headline:** ~40% of the 197 items (parent-position and D4 items) are priced by
tree arithmetic identical in both runs by construction. The sensor's judgement surface is the
~116 element-class-driven items, and within it the disagreement is 3 elements of 22. ×1.016 is the
end-to-end figure; the judgement-only figure is what expectation 2 measures.

## 3. The level moved, and that is a different question from the spread

The same 197-item work model priced at 890–1147 pd by `Hotyn-D 1.0`'s sampled prices prices at
**~350 pd** from the uncalibrated table (plus ~50–70 pd sitting in the N17/N18 holes, by 1.0's own
account of those elements). A ×2.6–2.9 level shift. **No conversion crosses an instrument boundary**:
which level is right is exactly the validity question, answerable only against outcomes (FaxRxTx
first), and is untouched by this run. The claim this run establishes is about **spread**: the
run-to-run ratio fell from ×1.288 to ×1.016 — the disagreement that remains is three named
enumeration calls, each visible, arguable, and cheap to adjudicate in the catalogue.

## 4. Findings beyond the expectations

1. **Both runs refused to size N17 and N18, identically and independently** — surface class with
   statement-shaped substance ("common look and feel", "responsive presentation" name no user task).
   Under 1.0 these two priced silently at ~72 pd (repeat 1) / ~52 pd (repeat 2) — a ×1.4 wobble
   nobody could attribute. The refusal is a **W7/M10 finding about the product model**: either these
   are statements, or the model owes them user tasks. The class question goes to the model owner.
2. **8 of 20 S classes sit at the floor because the requirement text names exactly one thing**
   (N21 UPSA is the sharpest: "Integration with UPSA via API" names no operation at all). This is a
   measured reading on the RFP's thinness at specific elements — the sizing analogue of the
   ambiguity register, and a concrete list of questions for the client.
3. **Four closure violations are new against run 22's seven**: credential/token handling for six
   adapters · substance behind the "Paid" stage · supplier-side cancellation · an actor for R44's
   override (in-batch, the strongest). The size-classification pass reads the model with different
   questions than the pricing pass did, and finds different holes.
4. **N34 went XL in both runs** (8 stage transitions) — the first XL the pipeline has produced, and
   both runs flagged the same alternative (5 slash-groups → L) as the largest sizing risk in the
   batch.

## 5. What this run does not establish

- One pair, one batch, one model, and a stale-definition protocol blemish: a difference, not a
  spread, measured under an impure stamp.
- Nothing about the level (see §3) — the table is uncalibrated external norms.
- P2 (cross-model ≤×1.15) is unmeasured; it needs a Sonnet-classified pair on the same input.
