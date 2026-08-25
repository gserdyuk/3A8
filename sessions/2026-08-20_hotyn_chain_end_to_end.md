# Session record — 2026-08-20 — the `Hotyn` chain run end to end for the first time

**Written to be read on its own, alongside other session records, by someone who was not in the
conversation.** Facts are separated from readings on purpose: §3 is what was measured and where it
came from, §5 is what I made of it. The two can be disagreed with independently.

Repository: `C:\home\OhmNova\3A8`. Nothing was committed during this session; all files below are
working-tree state.

---

## 1. What this session did, in one paragraph

Repaired the pinned inputs of the BMS case (a training RFP with no known outcome), then ran the
three-step `Hotyn` chain end to end for the first time: requirements → product model → work model →
person-days. Each step was run **twice on identical input**, so each has its own measure of run-to-run
agreement. Two sensor definitions were written from scratch during the session (`Hotyn-W`, `Hotyn-D`);
three rule defects were found by the runs themselves and fixed.

---

## 2. Instrument state, before and after

Readings from different versions are **not** the same instrument and must not be pooled.

| engine | at session start | at session end | what changed |
|---|---|---|---|
| `Hotyn-M` (product model) | 1.0 | **1.1** | M2: partial coverage is coverage at the node and a debt at the requirement (no requirement may leave closure partially covered); coverage is declared where the obligation is realised, never at a node that presides over it; closure asserts whole/residue per requirement. M4: provenance recorded by origin, empty-skeleton test moved from own coverage to total coverage |
| `Hotyn-W` (crossing) | did not exist | **1.1** | written this session at 1.0; 1.1 after the pilot: scope `per aggregate` → `per parent`; every refusal labelled `filter` or `judgement` (W9) |
| `Hotyn-D` (estimate) | did not exist | **1.0** | written this session. One wording fix after the runs: C3's base is the element's own items plus every descendant's, stated explicitly |
| technology catalogue | 1.0 (written 2026-08-20, earlier) | **1.1** | `per aggregate` → `per parent`; W9 added |

Definitions live in `.claude/agents/model-builder.md`, `work-crosser.md`, `work-estimator.md`.

### Pinned inputs as they now stand

| file | md5 (LF) | note |
|---|---|---|
| `examples/BMS/requirements_product.md` | `0c2dea478b993e4451a66f9468633f1e` | N = 68 |
| `examples/BMS/requirements_work.md` | `330826122b607088df3499e3e71cd103` | N = 5 |
| `examples/BMS/assumptions_product.md` | `8c622930655540d5fceb0d58d7482f8d` | the projection of the assumption log a product-model run may see |
| `examples/BMS/assumptions.md` | — | **version 2** (v1 governed runs 1–18) |
| `examples/BMS/open_questions.md` | — | version 1, 11 questions, all `not asked` |
| `docs/technology_catalogue.md` | — | version 1.1 |
| `examples/BMS/technology_declaration.md` | — | one entry per dimension, 8 dimensions |

---

## 3. Facts

Every figure below is from a run whose raw output is transcribed in the repository. All runs reported
`tool_uses: 0`. Isolation was enforced by the sensor definitions' tool restriction (`tools: Glob`)
except where noted.

### 3.1 Run 19 — `Hotyn-M 1.1`, Opus, order A, n = 2, N = 68

Raw: `examples/BMS/run19_raw/HM19-OA1.md`, `HM19-OA2.md`. Comparison: `run19_raw/coverage_run19.py`.
Write-up: `examples/BMS/run19_product_model_measurement.md`.

| reading | repeat 1 | repeat 2 | ratio |
|---|---:|---:|---:|
| skeleton nodes posited | 68 | 21 | ×3.24 |
| accretion additions | 9 | 99 | ×11.0 |
| **anchored (skeleton + accretion)** | **77** | **120** | **×1.56** |
| completion (derived) nodes | 10 | 11 | ×1.10 |
| nodes after normalisation | 78 | 129 | ×1.65 |
| coverage assignments (requirement, node) | 96 | 136 | ×1.42 |
| mean nodes per requirement | 1.41 | 2.00 | ×1.42 |
| co-located requirement pairs declared | 44 | 41 | ×1.07 |
| **Jaccard on requirement co-location** | **0.308** | | |
| requirements closed whole | 68 / 68 | 68 / 68 | — |
| residues at closure · deferrals | 0 · 0 | 0 · 0 | — |
| ambiguity flags | 16 | 17 | — |

### 3.2 Run 20 — `Hotyn-W 1.0`, pilot, 17 of 78 elements, n = 1

Raw: `examples/BMS/run20_raw/crossing_pilot.md`. Write-up: `run20_work_crossing_pilot.md`.
**Isolation weakness:** the definition was not yet available to the Agent tool, so this run went
through a general-purpose agent with the rules pasted in — isolation by instruction, verified after
the fact, not by the absence of tools.

- 94 work items from 17 elements: **5.53 items per element**, against **357** applicability questions
  fixed before the run.
- **30 refusals: 15 `filter`, 15 `judgement`.** All 15 judgement refusals were one question — *does
  this store need seed data?* — asked of five stores.
- 0 elements untouched. 4 activities applied to nothing (all gated on a `surface`, of which the sample
  contained none). 17 activities correctly deferred as whole-model scope.
- **59 of 94 items trace to an element carrying requirement coverage; 35 do not** (37%).

### 3.3 Run 21 — `Hotyn-W 1.1`, three batches × 2 repeats, 77 of 78 elements

Raw: `examples/BMS/run21_raw/HW21-{A1,A2,B1,B2,C1,C2}.md`. Comparison:
`run21_raw/compare_run21_all.py`. Write-up: `run21_work_model_measurement.md`. All six through the
real definition.

| batch | elements | repeat 1 | repeat 2 | Jaccard on (element, activity) pairs | class agreement |
|---|---:|---:|---:|---:|---|
| A — platform, configuration, identity, domain core | 25 | 154 | 157 | 0.956 | 24 / 25 |
| B — UX, integrations, search, workflow, hotel, transport | 27 | 197 | 197 | **1.000** | 27 / 27 |
| C — portals, reporting, support console | 25 | 195 | 189 | 0.949 | 23 / 25 |
| **all** | **77** | **546** | **543** | **0.969** | **74 / 77** |

Every difference in 553 distinct items traces to four classification calls:

| element | repeat 1 | repeat 2 | items affected |
|---|---|---|---:|
| N06 Data Platform | statement | store | 7 |
| N60 Reporting | surface | statement | 7 |
| N87 Reporting Read Model — seed activities | applied | refused by judgement | 3 |
| N65 Incident Intake | surface | behaviour | **0** |

Judgement refusals by batch: A 13 and 16 · B 0 and 0 · C 0 and 3. Filter refusals were identical
within every pair.

### 3.4 Run 22 — `Hotyn-D 1.0`, batch B work model (197 items), n = 2

Raw: `examples/BMS/run22_raw/HD22-B1.md`, `HD22-B2.md`. Comparison: `run22_raw/compare_run22.py`.
Write-up: `run22_estimate_measurement.md`. The work model used is the one both crossings of batch B
produced **identically**, so no step-2 disagreement is mixed into this measurement.

| reading | repeat 1 | repeat 2 | ratio |
|---|---:|---:|---:|
| items priced | 197 | 197 | — |
| leaves after C1 | 209 | 208 | ×1.005 |
| ΣE of leaves | 955.47 | 741.75 | ×1.288 |
| ΣE of integration (C3) | 191.09 | 148.34 | ×1.288 |
| **ΣE total, person-days** | **1146.56** | **890.09** | **×1.288** |
| integration share of total | 16.67% | 16.67% | — |
| person-days per leaf | 4.57 | 3.57 | ×1.282 |
| C1 split rate | 3.0% | 2.54% | — |
| items floored at 1 pd | 0 | 0 | — |
| closure violations reported | 7 | 8 | — |

**Effort per requirement, 27 obligations in scope:** ratio between the two runs ranges ×1.128 to
×1.456, mean ×1.276, standard deviation 0.105. **No requirement differs by more than ×1.5.**

**Seven closure violations were reported by both runs independently** (neither could see the other):
nothing prices the six subtrees meeting each other · no design activity on the aggregates · no store
for bookings or booking requirements · nothing uploads the manually uploaded bookings R16 searches ·
no surface where the Travel Manager defines the rules R19 demands · no UAT beneath the integration,
search and approval-workflow subtrees · no seed or reference data outside journey locations.

**Scope caveat, load-bearing:** this is six subtrees of a 78-element product with every whole-project
activity deliberately outside the work model. **1146.56 and 890.09 are not estimates of the BMS
project** and must not be quoted as such.

### 3.5 Historical figures this session compared against

From earlier sessions, restated here so a cross-session reader does not have to fetch them:

| figure | value | source |
|---|---|---|
| `Lytin` free decomposition, ΣE model gap | ×2.05 | run 17 |
| `Lytin` leaf count between models | ×1.87–1.97 | run 17 |
| `Lytin` price per leaf between models | ×1.01–1.07 | run 17, three instruments |
| closure test, one shared model, two decomposers | ×1.344 ΣE, ×1.21 leaves | run 18 §3b |
| `Hotyn-M 1.0`, anchored nodes across 2 models × 2 orders, N=73 | 82–87, CV 2.5% | run 18 |
| `Hotyn-M 1.0`, completion nodes between models | ×4.56 | run 18 |
| `Hotyn-M 1.0`, requirement co-location Jaccard | 0.16–0.27 | run 18 §3a |

### 3.6 Facts about the inputs, established this session

- **The assumption log contradicted the requirement list.** `assumptions.md` v1 excluded "subsequent
  operation (hosting & support)"; R02, R03 and R64 demand exactly that. Run 18 caught it on R03 in one
  run of four. The split showed it was systematic: 3 of the 5 demanded-work items.
- **19 of 73 requirements were flagged ambiguous by at least one run of run 18.** Excluding them
  raises coverage agreement on three pairings of four — Jaccard 0.277 → 0.362 on the closest pair,
  containment 0.43 → 0.63 on the weakest — and leaves every figure far below the registered 90%.
  Computed 2026-08-20 in `run18_raw/coverage_metric.py`.
- **Normalisation (M7) explains nothing.** Recomputed on the run-18 models: four co-location pairs
  added in one model of four. The registered candidate explanation for the low Jaccard is dead.

### 3.7 Facts about the harness, which affect reproducibility

- **A newly written agent definition is picked up by the same session, but not immediately.**
  `work-crosser` failed with "agent type not found" on first call and became available a few minutes
  later without a restart. Both previously recorded claims — "requires a restart" and "available
  instantly" — are wrong.
- **The subagent `.output` files are empty (0 bytes).** Raw output survives only by being transcribed
  into the repository by hand. Every raw file in `run19_raw/`, `run20_raw/`, `run21_raw/`,
  `run22_raw/` is such a transcription; where a section was omitted for length, the file says so.

---

## 4. Rule defects found by the runs themselves

A pattern worth watching across sessions: in every case below the defect was in **my** rules, and the
sensor found it while obeying them.

| # | defect | found by | fix |
|---|---|---|---|
| 1 | The sensor definition's output-format section still said `Hotyn-M 1.0` while its identity section said 1.1 | both run-19 repeats; both stamped 1.1 and reported the inconsistency instead of honouring the stale literal | the stamp now refers to the identity section, never a literal |
| 2 | M4's empty-skeleton test broke under M2 v1.1: applied to *own* coverage it reports every aggregate as a finding | both run-19 repeats, independently | test moved to *total* coverage |
| 3 | `stated` / `implied` conflated grouping nodes with derived ones once coverage moved to the realiser | run 19 repeat 1 | provenance recorded by origin: posited / accreted / derived, counted before normalisation |
| 4 | Catalogue scoped test execution, regression, planning "per aggregate" — a class — so an internal node carrying coverage drew none, however large its subtree. 5 of 18 parents excluded on an unrelated ground | run 20 | scope became **per parent** — a tree position |
| 5 | C3's base was ambiguous: does "leaf E beneath that element" include the element's own items? | run 22 repeat 2, which declared its reading before using it and quantified the alternative: total 890.09 → 843.67, **a 5.2% swing out of one word** | base stated explicitly |

Two distinctions the runs invented that the rules did not ask for, and which were then promoted to
rules: **`filter` versus `judgement` refusals** (run 20), and **"a declared boundary is not a
violation"** (run 22 repeat 2).

---

## 5. Readings — mine, and separable from the facts

Each is stated with what would overturn it.

**R1. The instability of the chain is concentrated in step 1.** Size ratios in one unit: ×1.65 nodes
(step 1), ×1.02 items (step 2), ×1.29 person-days (step 3). *Overturned by:* a second product-model
pair that agrees closely, which would make run 19's ×1.56 a one-off.

**R2. The freedom relocates rather than disappearing.** C1 fixed leaf size and leaf count went free;
closure fixed leaf count and within-element granularity went free; M2 v1.1 fixed declaration depth and
the number of parts an obligation is divided into went free (×1.42, run 19). *Overturned by:* a rule
that binds one of these without a new free parameter appearing behind it.

**R3. Step 3's disagreement is a level, not a shape, and is therefore of the correctable kind.** Leaf
count ×1.005, price per leaf ×1.282, and the per-requirement ratio has standard deviation 0.105 around
a mean of 1.276 with no outliers. *Overturned by:* a second estimator pair whose per-requirement
ratios scatter.

**R4. `Lytin`'s stable price per leaf was an artefact of free decomposition.** There, count varied
×1.96 and price held to ×1.03; here, with count pinned by the chain, price carries the whole gap.
*Overturned by:* evidence that the two "leaves" are the same kind of object — they are not, a Lytin
leaf being a WBS item at ~10.4 pd and a Hotyn leaf one activity on one element at ~4 pd.

**R5. The crossing is a second reader of the product model, and a good one.** Six crossing runs and
two estimator runs converged on the same list of gaps in the product model — no store for bookings, no
surface for the rules R19 demands, nothing pricing the subsystems meeting each other — none of which
the model builder reported, though M10 requires it to. *Overturned by:* finding those gaps are
artefacts of the partial-run boundary rather than of the model.

**R6. Input ambiguity is a component of run-to-run disagreement, not its explanation.** Excluding the
19 flagged requirements moves Jaccard 0.277 → 0.362 at best. *Overturned by:* a run batch on a
requirement list with the ambiguities actually resolved by a client.

---

## 6. Method decisions taken this session

Recorded because they are the author's, not derivable from the numbers.

- **A0, the imperative (`assumptions.md` v2):** an obligation the client stated cannot be removed by an
  assumption. A log may bound what a number prices, and must then name the instrument that prices the
  rest or the parameter that is missing. **An id appearing in neither the priced work nor the carried
  list raises an exception: defect report, no estimate.** What it outlaws is silence, not scope.
- **The procedure for a requirement that reads two ways:** ask the client · if no answer, assume ·
  declare the assumption · and **exclude the resulting differences when runs are compared**. The
  filter must be a register pinned before the runs (`open_questions.md`), never the runs' own
  ambiguity flags, because a run that flags more shrinks what it is scored on.
- **A partial verdict is a debt, not a state:** no requirement may leave closure partially covered.
- **Each step is compared in its own measure, and all three project onto one common frame** — the 68
  obligations. Nodes per requirement, work items per requirement, person-days per requirement.
- **The estimator is not told the team composition.** Effort in person-days does not depend on
  headcount; headcount decides the calendar, which is a different step.

---

## 7. Debts, in the order they would be cheapest to clear

1. **Finish the whole-project estimate.** Work models for batches A and C exist; missing are the
   whole-model layer (16 once-scoped activities, E1 × 3 environments, the root's own per-parent items,
   the demanded-work branch) and `Hotyn-D` on batches A and C. Recorded in `BACKLOG.md`. The honest
   output is a range with its sources named, not a point.
2. **Whether run 19's ×1.56 is new.** Run 18's cells were all n = 1, so there is no within-cell
   measurement under `Hotyn-M 1.0` to compare against. The author declined this experiment on the
   ground that no decision hangs on it — 1.0 would not be reverted whatever it showed.
3. **Nothing bounds how finely an obligation is divided into parts** (×1.42, run 19). No rule
   addresses it; M10 fixes the *level* of a leaf, not how many leaves one obligation becomes.
4. **A size-insensitive measure of structural agreement must be registered before the next batch**,
   not chosen after it.
5. **Q11 in `open_questions.md`**: R29 (automatic booking) against R38 (hotel supplier booking is
   manual, no external automation). Both estimators named it their largest basis risk.

---

## 8. Questions a cross-session analysis could answer that this session cannot

- **Does the step-1 instability reproduce?** One pair, one model, one order. If a second session's
  pair also lands near ×1.5–1.7 on node count, the anchor claim from run 18 is dead; if it lands near
  ×1.05, run 19 was an outlier and something else explains it.
- **Is the estimator's ×1.288 a stable property or a draw?** And is the offset always in the same
  direction, or does it wander? A stable direction would be a calibration constant; a wandering one
  would be noise of the same size.
- **Does the "freedom relocates" pattern hold across generations?** Three instances so far, all inside
  this project. A fourth would make it a law of this design rather than an anecdote.
- **Do the sensors keep finding defects in their own rules at this rate?** Five this session. If the
  rate does not fall as the rules mature, that says something about how the rules are written.
- **Do independent instruments keep converging on the same gaps in the product model?** Eight runs did
  this session. That is the strongest single signal produced, and one session cannot tell whether it
  is a property of the method or of this particular RFP.

---

## 9. How to reproduce every number above

```bash
python examples/BMS/run18_raw/coverage_metric.py     # run 18 coverage, normalisation, ambiguity component
python examples/BMS/run19_raw/coverage_run19.py      # step 1 agreement
python examples/BMS/run21_raw/compare_run21_all.py   # step 2 agreement, all three batches
python examples/BMS/run22_raw/compare_run22.py       # step 3 agreement and the per-requirement profile
```

Each script carries its input inline, transcribed from the raw files, so it runs without the raw
directory and can be checked against it.
