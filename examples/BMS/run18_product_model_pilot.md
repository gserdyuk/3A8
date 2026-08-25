# BMS — Run 18: the product model, `Hotyn-M 1.0` — pilot, 2×2

Date: 2026-08-19. First run of the **Hotyn** generation. Rules registered beforehand in
`docs/proposal_product_model.md`, with six predictions, before any run.

**Design:** 2 models (Opus 5, Sonnet 5) × 2 processing orders = 4 runs, n=1 per cell. A pilot, not a
measurement: it asks whether the rules are executable at all and where the variance sits, not how
large the variance is.

**Inputs, pinned:** requirement list `requirements.md`, md5 `554ea3608dd0602f0ddf2f7e7b82178c`, **N=73**.
Order A — top-down by breadth of impact, criterion stated in the list. Order B — the exact reverse,
chosen as the adversarial case: details first, system-level statements last.

**Isolation:** all four runs reported `tool_uses: 0`. The prohibition on reading repository files held
in every run. Note the weakness anyway: the pilot ran through a general-purpose agent with the rules
pasted in, so isolation was enforced by instruction and verified after the fact, not enforced by the
absence of tools. The sensor definition `.claude/agents/model-builder.md` (`tools: Glob`) exists and
should be used from here on.

---

## 1. Raw readings

| run | model | order | skeleton | accretion | completion | total | **anchored** | empty skel | deferrals | ambiguity |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| HM-SA | Sonnet 5 | A | 16 | 71 | 4 | 91 | **87** | 0 | 0 | 2 |
| HM-SB | Sonnet 5 | B | 15 | 71 | 5 | 91 | **86** | 0 | 0 | 9 |
| HM-OA | Opus 5 | A | 23 | 62 | 24 | 109 | **85** | 0 | 0 | 9 |
| HM-OB | Opus 5 | B | 75 | 7 | 17 | 99 | **82** | 12 | 0 | 12 |

**anchored** = skeleton + accretion, the part the requirement list bounds.
Completion-covers-a-requirement defects: **0 in all four runs**.

Full models in `run18_raw/models.md`.

---

## 2. The result

### 2a. The anchored structure is invariant; the split that produced it is not

| quantity | min | max | mean | CV | max/min |
|---|---:|---:|---:|---:|---:|
| skeleton | 15 | 75 | 32.2 | 89.1% | **×5.00** |
| accretion | 7 | 71 | 52.8 | — | **×10.1** |
| completion | 4 | 24 | 12.5 | 77.4% | ×6.00 |
| **skeleton + accretion** | **82** | **87** | **85.0** | **2.5%** | **×1.06** |

One run posited 15 skeleton nodes and accreted 71. Another posited 75 and accreted 7. **Their totals
are 86 and 82.** The division of labour between positing and accreting is nearly arbitrary; the sum
is not.

That is the anchor working. Where the structure comes from is a free choice; how much of it there is
answers to the requirement list.

### 2b. The model gap collapses on structure and survives in derivation

| | Opus | Sonnet | gap |
|---|---:|---:|---:|
| anchored structure (nodes) | 83.5 | 86.5 | **×1.036** |
| completion (derived nodes) | 20.5 | 4.5 | **×4.56** |
| — for contrast, `Lytin-D` on effort | | | ×2.05 |

The two models produce the same amount of anchored structure to within 4%, and differ by a factor of
four and a half on the part nothing bounds. Run 17 measured a ×2.05 gap on effort with no way to say
where it lived. It lives here.

### 2c. Nothing was ever deferred

Zero deferrals across all four runs and all passes. Every requirement found an attachment point on
first presentation, including under order B where the system-level statements arrive last. Accretion
converged in two passes in every run (pass 1 places everything, pass 2 confirms nothing is left).

M4's claim — that positing the skeleton from the list *as a set* removes the dependence on processing
order — is supported by the mechanism it predicted: the "cannot place this yet" verdict was never
needed.

### 2d. Empty skeleton nodes behaved exactly as designed

Three runs ended with none. HM-OB ended with twelve — every one a second-level aggregate (Booking
Domain Core, Integration Layer, Identity & Access, UI Foundation…), every one judged **genuine
infrastructure that no requirement names**, none dropped, none kept silently. All 59 of its skeleton
*leaves* received requirements.

HM-OA reported the more useful version of the same signal: no node ended empty, but four held exactly
one requirement and would have gone empty under a slightly different posit — and it named which, and
which reading of which requirement was holding them up.

---

## 3. Predictions

| # | Prediction | Outcome |
|---|---|---|
| 1 | Order-independence: coverage comparison agrees above 90% | **PROVISIONAL** — see below |
| 2 | Structures agree better than ×1.3, against ×2.05 on effort | **NOT CONFIRMED** on the registered test — see §3a |
| 3 | The derived fraction differs between models more than the stated | **CONFIRMED**: ×4.56 vs ×1.036 |
| 4 | Skeleton size varies less than leaf count did (CV under 10%) | **REFUTED**: CV 89.1%, ×5 range |
| 5 | Fewer than 20% of skeleton nodes end empty, and those are infrastructure | **CONFIRMED**: 0, 0, 0, 16%; all judged infrastructure |
| 6 | Transition off the predecessor process is still not generated | **CONFIRMED**, as the predicted failure |

**Prediction 1 stays provisional even though the comparison has now been made** (§3a). Under the two
orders the same model agrees on a Jaccard of 0.161 (Sonnet) and 0.270 (Opus) — far below the
registered 90%, but so is every other pairing, including model-against-model. The order effect
therefore cannot be separated from whatever is depressing all four figures, and with n=1 per cell it
cannot be separated from ordinary run-to-run variance either. Recomputing on normalised models (M7)
has since been done — §3c — and moves nothing: this prediction stays not scoreable in either
direction, and what depresses the figures is now known to be the metric's sensitivity to how much
coverage each run declares, not wrapping depth.

**Prediction 6, the registered failure, held.** No run produced any node for moving the client's
people or suppliers off the manual process — no parallel run, no decommissioning, no change
management, no migration of in-flight bookings. Accretion could not, because no requirement names it;
completion did not, because completion is triggered by structure and not by the client's situation.
Twenty `Lytin` runs failed to generate this work and four `Hotyn` runs failed in the same way. **A
requirement list built from an RFP cannot surface work the RFP does not describe**, and no rule in
this design changes that. If that work is to appear, it must enter as a requirement.

---

## 3a. The coverage comparison — computed, and it does not confirm prediction 2

M2 says a node's identity is the set of requirements it covers. The registered test is therefore
agreement of the **requirement partitions**: over all 2628 pairs from 73 requirements, do the two
models place the pair under a common node or not?

| comparison | agreement | **Jaccard** |
|---|---:|---:|
| Sonnet A ↔ B (order) | 98.2% | **0.161** |
| Opus A ↔ B (order) | 94.4% | **0.270** |
| Sonnet ↔ Opus, order A | 94.5% | **0.220** |
| Sonnet ↔ Opus, order B | 97.6% | **0.195** |

**The percentage agreement is inflated by sparsity and must not be quoted.** The co-location relation
holds for only 21–183 pairs out of 2628, so the overwhelming majority of pairs are co-located in
neither model and agree for free. Jaccard — the overlap of the two relations against their union — is
the honest figure, and it is **0.16–0.27**.

Restricting to nodes covering three requirements or fewer, to remove the effect of runs declaring
coverage at different levels of the tree, gives 0.18–0.28. The picture does not change.

**So node-count convergence is not structural convergence.** The four models agree closely on *how
much* structure to build (82–87 anchored nodes, ×1.036) and agree on roughly a fifth of *what goes
with what*. Prediction 2 as registered is not confirmed, and the earlier reading of it in this file —
confirmed on node counts — was the wrong measure applied to the right prediction.

One candidate explanation is checkable without new runs: the runs declared coverage at different tree
depths, so part of the disagreement is wrapping depth rather than structure. `M7` now normalises
single-child chains at closure; recomputing this table on normalised models is outstanding.

---

## 3b. The closure test — prediction 7 confirmed at its lower edge

One shared closed product model (HM-OA, 109 nodes) handed to both models, each decomposing it under
M9 with C1, C3 and PERT.

| | Opus | Sonnet | ratio |
|---|---:|---:|---:|
| leaves | 132 | 109 | ×1.211 |
| pd per leaf | 6.65 | 6.05 | ×1.099 |
| Σ leaf E | 878.33 | 659.96 | ×1.331 |
| **Σ E** | **1281.77** | **953.55** | **×1.344** |

Registered band was ×1.4–×1.8, with below ×1.2 meaning closure binds harder than claimed and above
×1.9 meaning it binds nothing. **×1.344 sits just under the band's lower edge: confirmed, at the
strong end.**

**67% of the model gap removed** — the excess over parity fell from 1.052 (Lytin, ×2.05) to 0.344.
The mechanism is visible: **leaf count ratio fell from ×1.96 to ×1.21.** Sonnet read closure literally
and produced exactly one leaf per node, 109 of 109; Opus subdivided 22 nodes. That subdivision *is*
the residual granularity freedom M9 says it cannot bind — predicted at ×1.63, measured at ×1.21.

One thing moved the wrong way: **price per leaf went from ×1.03 under Lytin to ×1.099 here.** It was
the most stable quantity the old instrument had. Small, but the direction is unwelcome and it is not
explained.

The levels converged from opposite sides: Opus 1480 → 1282 (−13%), Sonnet 721 → 954 (+32%).

### And the finding that reshaped the design

Both runs produced the M9-mandated list of work they judged necessary and did **not** add. Opus listed
eleven items, Sonnet four. Both flagged data migration, internationalisation, accessibility and
penetration testing. **Only Opus caught the structural absence**: system testing, test design,
regression, UAT support, project management, business analysis, go-live cutover.

Its own words: *"the model has no node anywhere whose declared content is quality assurance or project
governance. Under M9 that work cannot be priced at all, which is the single largest reason to distrust
the total below as a delivery number."*

That list is **not a defect in closure — it is closure working.** Under Lytin this work was invented
silently by every run and folded into the total indistinguishably. Here invention is impossible, so it
surfaces as a report.

Every item on the list is **technology-derived work**: it is not missing from the product model, it is
not product structure at all. `docs/proposal_product_model.md` gained a second step and the technology
declaration because of this result.

Note also that the diagnostic value differed sharply between models even where the estimate did not:
Sonnet produced a comparable number while failing to notice that QA and project governance had no home
anywhere in the model.

Raw readings: `run18_raw/closure_test_readings.tsv`.

---

## 3c. Normalisation recomputed — it changes nothing, and the reason the Jaccard is low is elsewhere

Done 2026-08-20 on the run-18 data, no new runs. Script: `run18_raw/coverage_metric.py`; numbers:
`run18_raw/coverage_normalised.tsv`. The script reproduces §3a's four figures exactly before changing
anything, which pins two conventions that were implicit: **a partial-coverage mark counts as
coverage**, and co-location is judged on a node's **declared** coverage set, never on the union of its
subtree — under subtree union the root covers everything and every pair agrees for free.

| pairing | J as recorded | **J normalised** | max J at these sizes | overlap coefficient |
|---|---:|---:|---:|---:|
| Sonnet A ↔ B | 0.161 | **0.161** | 0.477 | 0.429 |
| Opus A ↔ B | 0.270 | **0.277** | 0.410 | 0.747 |
| Sonnet ↔ Opus, order A | 0.220 | **0.220** | 0.240 | 0.932 |
| Sonnet ↔ Opus, order B | 0.195 | **0.185** | 0.280 | 0.714 |

**M7 normalisation added four pairs in one model of four and none in the other three.** The mechanism
is narrow: collapsing a single-child parent into its leaf creates a new co-location only when parent
and child both declare coverage *and* declare different coverage. In HM-SA every such collapse was
already recorded by a partial-coverage mark — `S1.5 {R11,R65p} → S1.5.1 {R65}` merges to `{R11,R65}`,
which is what the marks already said. In HM-SB both single-child parents cover nothing. HM-OB gained
`R25-R29`, `R29-R45`, `R29-R50`, `R45-R48`, and that is the whole effect: one figure up by 0.007, one
*down* by 0.010, because pairs added on one side of a comparison lower the Jaccard when the other side
does not match them.

**So the candidate explanation is dead.** Wrapping depth is not what depresses the agreement, and the
open question in `docs/proposal_product_model.md` §8 is answered: normalisation does not improve
coverage agreement. Prediction 2 stays not confirmed, and it is now known that it is not confirmed for
some other reason.

**HM-OA could not be normalised at all**, because `models.md` records no parent for its nodes. The
sensor definition requires parent per node in the final model; the transcription into the raw file
dropped it. That is a protocol defect, not a result — **raw model records must carry the parent
pointer**, or M7 cannot be applied after the fact and no structural comparison beyond coverage is
possible later.

### What the same computation does show

The four runs declare very different **amounts** of co-location:

| model | nodes covering 2+ requirements | largest coverage set | co-located pairs |
|---|---:|---:|---:|
| HM-SB | 18 | 3 | 21 |
| HM-SA | 28 | 4 | 44 |
| HM-OB | 31 | 5 | 71 |
| HM-OA | 45 | 9 | 183 |

A Jaccard between two relations of size 44 and 183 **cannot exceed 44/183 = 0.24** however well they
agree. Measured against that ceiling the four pairings reach 34%, 70%, 92% and 66% of the maximum
available to them. The overlap coefficient — the share of the smaller relation contained in the larger
— is 0.43, 0.76, **0.93** and 0.71.

Read plainly: **93% of the co-location statements Sonnet-A makes, Opus-A also makes.** The two models
do not contradict each other about what goes with what nearly as much as the Jaccard suggests; they
differ in how much co-location they declare at all, and the sparse relation sits almost entirely
inside the dense one. Between the two *orders* of the same model the picture is worse (0.43 for
Sonnet), which is the one place the disagreement looks genuinely structural.

Three cautions, because this reading is easy to over-sell:

- **The overlap coefficient was not registered and is post-hoc.** It is also trivially satisfied: a run
  that declares almost no co-location scores high against a run that declares a lot. It means something
  only quoted next to the two sizes, as above. If it is to be used as a test, it is registered before
  the next run, not after it.
- **The registered test was Jaccard and Jaccard is not confirmed.** Nothing here rescues prediction 2.
- **n = 1 per cell.** The order effect still cannot be separated from run-to-run variance.

### A rule gap this exposed

Excluding partial-coverage marks collapses Sonnet's relation from 44 pairs to **3** while leaving
Opus's at 183 — the two runs use the mark for entirely different things. M2 says a node's identity is
the set of requirements it covers, and says nothing about whether a partly-covered requirement is in
that set. Until it does, "the same node" is not a defined predicate and any structural comparison
inherits the ambiguity. **Decided 2026-08-20 as M2 v1.1**, in three parts. Partial coverage *is*
coverage at the node — a node realising part of a requirement carries its id. But **a part is not an
answer**: no requirement may leave closure partially covered, because a missing part is missing
structure and the run's job is to add it; a partial mark left standing looks like a record and is a
debt. And, the half this comparison could not see, **coverage is declared at the node that realises
the obligation, not at the node that presides over it**. A parent no longer claims what a child realises, which is what M7 already required of a
node's content and never required of its coverage. Registered as prediction 6 in the proposal: under
1.1 the relation sizes should come within ×2 of each other instead of ×8.7, and the Jaccard above 0.5.
The sensor is now `Hotyn-M 1.1`; these four models cannot be recomputed under it.


---

## 3d. The input-ambiguity component, measured

Added 2026-08-20 under `assumptions.md` A11: *a comparison is reported twice — over all requirements,
and excluding those under an open question* — because a disagreement caused by a question nobody asked
the client is not method variance.

Run 18 predates the register, so the stand-in filter here is the union of the runs' own ambiguity
flags: **19 requirements of 73, a quarter of the list**, flagged by at least one run.

| pairing | J, all 73 | J, excl. 19 | containment, all 73 | containment, excl. 19 |
|---|---:|---:|---:|---:|
| Opus A ↔ B | 0.277 | **0.362** | 0.747 | 0.829 |
| Sonnet ↔ Opus, order A | 0.220 | **0.284** | 0.932 | 0.962 |
| Sonnet A ↔ B | 0.161 | 0.172 | 0.429 | **0.625** |
| Sonnet ↔ Opus, order B | 0.185 | 0.167 | 0.714 | 0.875 |

**Input ambiguity is a component of the disagreement and not the explanation of it.** Removing a
quarter of the list raises Jaccard on three pairings of four — by up to a third — and leaves every
figure far below the registered 90%. Containment rises on all four, most sharply where it was weakest.

**The stand-in filter is itself the argument for the register.** Scored on their own flags, a run that
flags more requirements shrinks what it is judged on and improves its own number: HM-OB flagged twelve
and HM-SA two. That is why A11 makes the filter a pinned input — `open_questions.md`, fixed before the
runs and shared by all of them — and demotes the runs' flags to evidence that the register needs
revising.

Reproduce: `python examples/BMS/run18_raw/coverage_metric.py`.

---

## 4. Correction on the record

`docs/proposal_product_model.md` M4 states, and this run refutes:

> **The skeleton's size is the concentrated free parameter of this method.** It is deliberately
> concentrated there: one number per run, visible and comparable across models.

Skeleton size ranges ×5 across four runs and correlates with nothing that matters — the anchored
total is stable at 82–87 regardless. **The skeleton is not where the freedom concentrates; it is a
presentation choice about when structure gets written down.** The freedom concentrates in
**completion**, which the same document already identified as the one unbounded phase (M6) and
instrumented rather than constrained.

So the design was right about where to put the instrument and wrong about where the parameter would
land. M4's claim about concentration should be struck; M6's should be strengthened.

---

## 5. A defect in the pinned inputs, found by a run

HM-OA flagged a contradiction that is real and is mine:

> **R03** "The Supplier supports the system" — an obligation on the product.
> **A1** "Not included: subsequent operation, user training, the warranty period" — removes it.

The run placed R03, declined to reconcile, and said the client's answer is needed before the model is
trusted. That is correct behaviour under M1. The other three runs placed R03 without noticing.

The cause: the assumption log was carried over unchanged from the `Lytin` era, where it bounded an
**estimate**; the requirement list states what the **product** must be. The two were never checked
against each other.

**Fixed 2026-08-20 in `assumptions.md` v2, and not by choosing either of the two options this file
named.** Both were scope decisions; the fix is a rule — **A0, the imperative**: an obligation the
client stated cannot be removed by an assumption. A log may bound what a number prices, and must then
name the instrument that prices the rest or the parameter without which nothing can. An id in neither
the priced work nor the carried list raises an **exception**: defect report, no estimate. R03's
hand-over residue is priced, the support service is carried with **the term** as the missing parameter,
and the question goes to the client. R13 and R14 were settled in the same pass, as A8 and A9.

A second reading worth carrying: HM-OA flagged **R13** ("support for critical instances such as major
disruption situations") as readable two ways — IT disaster recovery, or mass re-booking during a
travel event. It proceeded on the technical reading and stated that the business reading, if correct,
"is the largest single omission in this model". HM-OB attached it to both rather than choosing.

---

## 6. Behavioural differences that node counts hide

The four runs reached similar structures by visibly different reasoning.

- **Verdict distribution.** HM-OA: covered 11, partial 61, **not covered 1**. HM-SA: covered 3,
  partial ~20, not covered ~49. Opus almost never met a requirement wholly foreign to its structure;
  Sonnet routinely did. Same destination, opposite route.
- **Ambiguity flags:** 2, 9, 9, 12. HM-SA raised two where the others raised nine or more against the
  identical list.
- **Where the freedom was exercised.** HM-OA named it precisely: *"I treated skeleton nodes as
  realising a requirement only when the requirement's whole obligation was that node's posited scope.
  That rule produced the 11 covered verdicts and is the main place this run's remaining freedom was
  exercised; a stricter rule would have produced a larger tree, a looser one a shallower tree."*

That last is the clearest statement anywhere in this run of what the coverage judgement actually is,
and it came from the sensor, unprompted.

---

## 7. Outstanding

- ~~Recompute the coverage comparison on normalised models.~~ **Done 2026-08-20, §3c: normalisation
  changes four pairs in one model of four and explains nothing.** What remains open is the M2 rule gap
  it exposed — whether partial coverage counts towards a node's identity — and the protocol defect that
  HM-OA's parent pointers were never transcribed.
- ~~Split `requirements.md` into product obligations and demanded work.~~ **Done 2026-08-20:**
  `requirements_split.md`, giving `requirements_product.md` (N=68) and `requirements_work.md` (N=5).
  R02 and R64 joined the three that were expected.
- **Resolve R03 vs A1** in the inputs, and decide on R13's two readings.
- **Rerun through the real sensor definition** (`model-builder`, now `Hotyn-M 1.1`, `tools: Glob`)
  rather than a general-purpose agent with pasted rules, and with n>1 per cell so the order effect
  separates from run-to-run variance.
- **Raw records carry the parent of every node, and the part each partial verdict realises.** HM-OA's
  carried no parents, which alone made it impossible to normalise or to recompute coverage at
  declaration depth; and no run's record carries *which part* of a requirement a partial mark stands
  for, so whether these four models were complete under M2 v1.1's closure check cannot be answered
  from the record. The rule for transcription: what the sensor definition asked for goes into the raw
  file in full, whether or not today's analysis needs it.
- **Everything downstream** — the technology catalogue, `Hotyn-W`, the falsification test — is listed
  in `docs/proposal_product_model.md` §10.

---

## 8. Procedural note

The sensor definition `.claude/agents/model-builder.md` was written during this session and became
available to the Agent tool **within the same session**, without a restart. The project's standing
note that agent definitions are read once at session start no longer holds on this harness. The pilot
had already been launched through a general-purpose agent by then; future runs should use the real
definition, whose tool restriction enforces isolation rather than requesting it.
