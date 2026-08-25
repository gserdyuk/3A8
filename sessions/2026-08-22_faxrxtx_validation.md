# Session record — 2026-08-22 — stage 3: the Hotyn chain run end to end against a fact

**Written to be read without the conversation.** Facts separated from readings; the numbers separated
from what they are taken to mean. Repository state: everything in the working tree, nothing committed
(the author's standing choice).

## 1. What this session did, in one paragraph

Executed stage 3 of `sessions/2026-08-22_course_correction_and_first_deliverable.md` §8 item 1 in full:
pinned a FaxRxTx obligation list (N = 52 → 47 product + 5 work), wrote the technology declaration from
catalogue 1.4 with four visible scope decisions, ran `Hotyn-M 1.1` (n = 2), crossed the first model with
`Hotyn-W 1.1` in three batches, classified sizes with `Hotyn-D 2.0` (n = 2, three batches), obtained
eleven gap-blind rate rows for the demanded work that no dimension absorbs, assembled — **69.2 pm** —
wrote the assembly down, **then** opened `FACT.md`: **~120 pm**. The chain under-estimates by **×1.735**
and fails the exit criterion's centre test. Four new registered runs (29–32), all raw output
transcribed.

## 2. Instrument state

| instrument | change this session |
|---|---|
| `Hotyn-M 1.1` · `Hotyn-W 1.1` · `Hotyn-D 2.0` | unchanged; all three printed correct stamps; probe returned `Lytin-F 5.0` before the first batch |
| `docs/rate_table.md` | **unchanged at v0.1 + A1**, deliberately. Two FaxRxTx-specific addenda were produced (**A2**, **A3**: eleven rows for the demanded-work branches) and live with the case, not in the table |
| `docs/technology_catalogue.md` | unchanged at 1.4 |
| `docs/exit_criterion.md` | unchanged at v1.0; **applied for the first time** |
| new chain-level parameter | **`L-1` = ×1.735**, a global level factor fitted on FaxRxTx at n = 1. Recorded in `examples/FaxRxTx/run32_fact_comparison.md` §5 with three binding conditions, **not** in the rate table |

## 3. Pinned inputs created

`examples/FaxRxTx/requirements_pinned.md` N = 52 (md5 `473d9789f000da3cbf563c4f008fd9d5`) ·
`requirements_product.md` N = 47 (`306046dc6cab35147040224e7a4e9662`) · `requirements_work.md` N = 5
(`b25463f3a0a56d227e3348b76e35d26c`) · `requirements_split.md` · `assumptions_product.md` v1 ·
`technology_declaration.md` · product model `HM29-OA1` (97 nodes) · work model `HW30-A1/B1/C1`
(570 crossing items + 4 demanded branches).

## 4. Facts

- **Run 29** (`Hotyn-M 1.1`, n = 2): 98/92 nodes before normalisation, **anchored structure ×1.024**,
  derived ×1.40, coverage assignments ×1.171, co-location Jaccard **0.406** at sizes 21 and 24. Both
  runs placed all 47 obligations wholly, zero partial marks at closure.
- **Run 30** (`Hotyn-W 1.1`, n = 1, three batches): 198 + 140 + 232 = **570 crossing items** over 96
  elements, plus 4 demanded-work branches. **70 refusals: 50 filter, 20 judgement.** Batch A logged 9
  contested classifications. One of five demanded items absorbed (F51 at E6); four stand alone.
- **Run 31** (`Hotyn-D 2.0`, n = 2, three batches): 79 elements each repeat, **74 sized in each**, five
  refused in each — **but not the same five**: HM1-75 unsizeable in repeat 1 and M in repeat 2, HM1-57
  the reverse. **Ten element-class divergences of 79 (87.3% agreement)** plus one special-count
  divergence. **Zero XL elements in either repeat.**
- **Run 31 assembly:** 1475.4 / 1429.7 pd, **repeat spread ×1.0319**, centre **1452.5 pd = 69.2 pm**.
  Layers: element leaf 897/865 · C3 397/384 (root C3 179.5) · once + per-environment **63.96** ·
  demanded work **117.33**. Honest extreme band ΣO…ΣP = **30.4 … 130.4 pm**.
- **Run 32** (fact opened after the assembly was written): fact **~120 pm**, window 96–144.
  **Chain ×0.58 of fact; the fact is ×1.735 higher.** Exit criterion: centre **FAIL**, corridor **not
  scoreable**, provenance **PASS**.
- **Rate rows:** gap-blind `Hotyn-K 1.0` refused all four demanded items as single rows on the first
  round, gave decompositions, and on the second round wrote **nine rows, none refused**. It caught the
  duration inside F48 and quarantined it; it corrected its own driver ("cycle count does not determine
  effort — cycle *ordinal* does") and split one row rather than average across the ceiling.
- **Historical comparison on the same project:** bottom-up centres of **111.6 pm** (2026-07-17,
  manual), **237.8 / 503 pm** (2026-08-05, Lytin agent pipeline), **69.2 pm** (today). Reference-class
  P50s: **160** and **135**.

## 5. Rule and input defects found by the runs

- **`HM1-61` (system database schemas) is unsizeable and it is the input's fault, not the model's.**
  F28 reads "A database is part of the system (the DBMS is not specified)" — it names a platform and
  not one entity kind. Both repeats refused it independently. Nine items unpriced.
- **`HM1-83`, `HM1-78`, `HM1-84` likewise**, and all three trace to the source naming a thing without
  content: *"what happens when there is no delivery"*, *"Integration with the old system"* (no
  direction, no payload), *"the core functionality of the first version"* (no function named).
- **`A10` cannot reach the system's own inter-component API.** `interface` is defined as an exchange
  with a system *outside* this one, so F29's internal API is a `behaviour` and draws no contract test.
  Either the class definition or A10's applicability is too narrow. Reported by run 30, not repaired.
- **`A9` cannot reach a mandatory availability property.** F44/F45 make distribution and failure
  survival mandatory and state no measurable target; the statements are filtered out of performance
  testing, and the behaviours that carry the same obligations are not of a class A9 applies to. No
  measurable availability threshold exists anywhere in the model.
- **The rate rows' boundaries are holes where the model has no other home.** `W-F49.3a/3b` price the
  real-stream execution cycles and exclude fixing the defects they surface. `A6` is per-parent and
  scoped to the ordinary cycles. Nothing prices that fixing.

## 6. Readings — each with what would overturn it

- **R5. The ×1.56 anchored spread of BMS run 19 was a property of the BMS input, not of `Hotyn-M
  1.1`.** Here two identical runs agreed to ×1.024 on anchored structure while exercising the same
  partition freedom (1.74 against 2.04 nodes per requirement). Two candidate mechanisms — the input
  describes structure rather than obligations, and the assumption projection pinned ten readings
  against BMS's six — are **not separated**. *Overturned by:* a FaxRxTx pair run without the projection
  reproducing run 19's spread, or a BMS pair with a dense projection coming down near ×1.0.
- **R6/R7. The once-layer and the root C3 are near-identical across two unrelated projects** (63.96
  against 63.7; 179.5 against ≈181). That is the bracket structure of the table, not a fact about the
  projects.
- **R8. The total is, to first order, element count × a constant.** BMS 78 elements → 17.3 pd each;
  FaxRxTx 97 → 15.0 pd each; totals 7.7% apart for projects that are not remotely the same size.
  *Overturned by:* a model of materially different granularity over the same obligations producing a
  materially unchanged total.
- **R9. The bottom-up centre has swung ×3.4 across three generations on one unchanged project** —
  111.6 → 237.8 → 69.2 pm. *Overturned by:* showing the three priced different scopes. They did not.
- **R10. The reference class has been the closest instrument to the fact, twice, and it is the one the
  project has invested least in** (×1.33 and ×1.13, against the bottom-up's ×0.93, ×1.98, ×4.19,
  ×0.58). *Overturned by:* a second outcome case where the class misses and the bottom-up hits.
- **R11. Every generation removed a degree of freedom; agreement improved and accuracy did not — the
  error changed sign.** Judgement pricing overshot ×4.2 calibrated; tabled pricing agrees to ×1.032
  between repeats and undershoots ×1.735. *Overturned by:* three further outcome cases inside ×1.3.

## 7. The author's decisions still outstanding

None was taken this session; the session executed a plan the author had already approved. Two
decisions are now **waiting**, and both are named in `run32_fact_comparison.md`:

1. **Run the granularity experiment, or not.** One `Hotyn-M` run at ~160–170 elements on the same
   pinned list, crossed, sized and priced with **no rate changed**. It separates R8 (the total is a
   function of the modelling act) from the vintage explanation (modern norms on a 2007-era stack).
   Nothing else in the backlog separates them, and at n = 1 the global factor `L-1` conflates them.
2. **Whether `L-1` stands at all.** If the experiment shows element count carrying the gap, `L-1` must
   be **withdrawn**, not re-fitted — a factor correcting for a modelling artefact double-counts the
   moment the modelling changes.

## 8. Debts, cheapest first

1. **The granularity experiment** (§7.1). The one measurement that makes today's result actionable.
2. **The chain has no corridor instrument.** Exit-criterion test 2 could not be applied: the chain
   produces a centre and ΣO…ΣP, which is a perfect-correlation extreme band spanning ×4.3 and is not a
   probabilistic interval. Until a corridor exists, only one of the criterion's three tests is
   scoreable.
3. **Protocol fix, third and fourth independent catch:** strip `gitStatus`/commit subjects from sensor
   launches. Every one of the eleven sensors run today reported the injection and quarantined it. The
   explicit quarantine instruction added to the prompts this session **works** — no run stopped, all
   reported — but it is a workaround, not the fix.
4. **Subagent replies can arrive truncated** (new). Run 29's second model reached the orchestrator
   beginning part-way through §7c. Recovered by resuming the agent and asking for a **verbatim
   re-emission**, explicitly forbidding re-derivation; sections 2–5 of that run are permanently lost.
   **Standing practice: check a reply begins at section 1 before transcribing; recover by re-emission,
   never by re-running** — a re-run silently turns n = 2 into n = 3 with one member discarded.
5. **`HM29-OA2` is not crossed** (87 nodes against 97). Under R8 it is the cheapest second data point
   for the granularity question, in the opposite direction from the experiment in §7.1.
6. **The crossing ran at n = 1.** 20 judgement refusals and 9 contested classifications have no
   repeatability reading on this case.
7. **Catalogue defects to adjudicate:** A10's blindness to internal APIs; A9's unreachability from
   behaviour-carried availability obligations; a home for defect-fixing after a parallel-run cycle.

## 9. Open cross-session questions

Does the ×1.032 repeat agreement hold on a third project · is the element-count law (R8) real or a
coincidence of two cases · does the reference class keep out-performing the bottom-up (R10), and if so
what is the bottom-up *for* · is the vintage worth ×1.7 on its own · what corridor instrument can the
Hotyn chain have at all, given that both the independence assumption and the perfect-correlation
assumption are visibly wrong.

## 10. Reproduction

```bash
python examples/FaxRxTx/run31_raw/assemble_faxrxtx.py
```

Runs 29, 30, 32 are prose-only. The chain of documents in reading order:
`requirements_split.md` → `technology_declaration.md` → `run29_product_model_measurement.md` →
`run30_raw/HW30-*.md` → `run31_raw/HD31-repeat*.md` → `run31_whole_model_assembly.md` →
`run32_fact_comparison.md`.

## 11. Amendment, 2026-08-23 — the unit of the fact

The author, answering the question this record put at the top of its elimination programme: **the ten
people are staffed headcount**, and **in this organisation's practice an 8-hour working day is 6
person-hours**. The fact restated in the estimate's unit is **90 pm**, not 120.

Consequences, recorded in `examples/FaxRxTx/run33_unit_of_the_fact.md`:

- the miss goes from **x1.735 to x1.30** — the centre lands **1.35 pd below** the gate on a total of
  1452.5, repeat 1 passes and repeat 2 does not;
- **`L-1` is withdrawn.** x1.735 -> x1.301 on the unit correction -> x1.059 once the two pending
  adjudications are applied. FaxRxTx is **no longer spent** as evidence;
- **R10 is overturned** — against the corrected fact the reference class overshoots x1.50 and x1.78 and
  fails on both readings;
- **R11 is amended** — agreement improved *and* accuracy improved; what survives is the narrower claim
  that the bottom-up centre swung x3.4 across three generations and that swing is still unexplained;
- **R12, new** — every calibration this project has ever applied moved the answer away from the fact,
  all three upward: 111.6 -> 155, 237.8 -> 503, and `L-1` would have taken 69.2 -> 120. The mechanism
  was named as a hypothesis in July 2026: calibration pulls towards the ensemble P50, and the ensemble
  P50 sits x1.5-1.8 above this project's only known outcome;
- the **vintage** and **team-unfamiliarity** candidates are no longer needed to explain anything, and
  the rate table stays at v0.1 + A1;
- the **granularity experiment is demoted** — diagnostic against a x1.735 gap, not against x1.06.

**The methodological finding:** three generations interrogated the estimate and took the fact as given.
The largest single error term in the only comparison that can score any of it was in the fact's unit,
and it cost one question. Standing rule proposed as **A13**: an outcome reconstructed as headcount x
calendar is staffed presence, not delivered work, and converts at the declared utilisation before it is
compared with anything.
