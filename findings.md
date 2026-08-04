# Findings — accumulated conclusions for the 3A8 project

A working log of the insights and empirical findings that METHODOLOGY.md rests on. It does not duplicate the methodology but records *why* it was made the way it is — sources, experiments, open questions.

## 1. Why you cannot simply ask one LLM several times (the single-model diversity problem)

- Classic Wideband Delphi works through the independence of *human experts* — different experience and different information. One model across different sessions has no structural independence: its "ceiling of ignorance" is systematic, not random.
- Persona prompting (different "roles" of one model) gives diversity of focus but not diversity of the reasoning apparatus — under the hood it is the same statistical mechanism.
- **Empirical confirmation (anchoring bias is stronger in LLMs than in humans):** a replication of the classic Jørgensen–Halkjelsvik experiment on GPT-4, Llama 3.1, Gemini 1.5 Pro showed that when the phrasing of the question changes ("how long is needed for X" vs. "how much can you finish in Y hours") the LLMs' estimates diverge **at least 6× more strongly** than humans' in the original. For GPT-4: 4000 vs. 150 work hours on the same set of user stories — i.e. the anchoring almost completely suppresses the substantive signal of the task. (Çalıklı & Alhamed, FSE 2025)
- Conclusion: varying the prompt/phrasing is not a source of independent opinion but controlled anchoring. If building a multi-persona debate, it is critical to keep the question format identical for all personas.
- LLMs do not behave like humans even where similarity was expected: comparative (pairwise) judgments do not come more easily to LLMs than direct estimates, though for humans they do. This means debias techniques that work for humans (comparison instead of absolute estimation) cannot be transferred to LLMs automatically.

## 2. Three different kinds of "not knowing" — where LLMs beat humans and where they do not

- **Breadth problem (breadth of pattern coverage)** — the LLM really is stronger than a team of humans; it has seen orders of magnitude more post-mortems and project patterns.
- **Calibration problem (weighting of known risks)** — not clear the LLM is stronger; RLHF pulls toward "balanced" answers, which may systematically underweight chaotic organizational factors.
- **Local/tacit knowledge** — data that does not exist in the nature of text (this particular team, this particular person, this particular legacy service). No LLM and no estimation method covers it in principle — only living people with a history in this specific organization.

## 3. Multi-agent debate — the only LLM-native approach with independent empirical confirmation

- SEEAgent (Bui et al., 2025) — a multi-agent framework in which LLM agents give estimates, justify them, and debate with other agents/humans until consensus. It outperformed state-of-the-art methods on most metrics on a real dataset; practitioners rated the collaborative experience positively.
- This is direct empirical confirmation that the combination *persona + reference-class + multi-agent debate* is not only theoretically sound but works in practice.

## 4. The key shift: different techniques instead of different experts ("experts with a different apparatus")

Instead of decorrelation through people — decorrelation through mathematically different methods. Their blind spots are not empirically random (as with people) but **guaranteed by the construction of the method** — i.e. predictable in advance.

| Method | Strength | Structural blind spot |
|---|---|---|
| Decomposition (bottom-up + PERT) | Specifics of the particular task | Correlation of risk across tasks; systemic/integration risks; overhead |
| Reference class forecasting | Systemic risk as a whole (the "outside view") | Specifics of this particular task/team |
| Throughput Monte Carlo | Organizational overhead and fragmentation — empirically, automatically | Does not explain causes; requires history; assumes future tasks resemble past ones |
| Parametric (COCOMO-like) | Independence from subjective judgment | Quality = quality of calibration; models age |
| ML/regression on history | Semantic patterns of similar tasks | Explainability; new task types outside the sample |

Additionally mentioned but not included in the main pipeline: relative estimation / planning poker (more robust to anchoring in humans, but not clearly so in LLMs — see §1), probabilistic PERT accounting for risk correlation.

## 5. An observation about Scrum overhead (sprints) → throughput as a natural corrector

- Personal observation: a lot of time goes into (a) sprint start-up, (b) hand-off/review, (c) unusable "scraps" of time.
- This matches known concepts: "focus factor" in Scrum, "flow efficiency" in Kanban/Lean. Point (c) is essentially a bin-packing problem, statistically inevitable with granular tasks and a fixed sprint capacity.
- Throughput Monte Carlo accounts for this automatically and empirically (from the fact of past sprints); decomposition fundamentally cannot, because overhead is not tied to a particular task.
- There is a separate research line — agent-based/system-dynamics modeling of developer behavior (SPSM — Software Process Simulation Modeling): historically discrete-event and system-dynamics approaches dominate; an agent-based case (AVL) proposes a "practical effort function" for modeling developer behavior, including interruptions for mentoring and so on. The results "look promising, but more work is needed" — i.e. a working direction, not a finished product.
- The classic of the genre — Abdel-Hamid & Madnick, "Software Project Dynamics" (1991): a system-dynamics model with Brooks's effect, ramp-up of new hires, accumulation of undetected rework, and the effect of pressure on quality.
- Practical conclusion: for a pure "how long" estimate a simple correction coefficient suffices (actual throughput / nominal capacity over N sprints). A full behavioral simulation is justified only for "what if" questions (comparing ways of organizing the work), not for a point estimate.

## 6. The convergence problem in a cross-method approach

- In human Delphi, convergence is the result of an *expert* changing *their own* opinion after new information. With different estimation techniques this is impossible: a method cannot "reconsider" and start accounting for what it does not account for by construction.
- Convergence must be engineered explicitly, by a separate mechanism:
  1. **Independent runs** — each method gives a range + an assumption log.
  2. **Diagnosing the divergence** — not "whose number is more correct," but which specific blind spot explains the difference.
  3. **Parameter transfer** — mechanical calibration, not agreement of opinions (example: throughput → overhead coefficient as an explicit multiplier to decomposition).
  4. **Final range with explained residual** — what was not removed by parameter transfer is an honest measure of uncertainty, not noise to be averaged away.
- **Important:** full convergence after explicit corrections is not always a success — if the methods answer structurally different questions yet converge to a single point, it is either a coincidence or one method was forced under another and lost its diagnostic independence.

## 7. Are historical data needed to compare decomposition vs. reference class?

**No.** Reference class forecasting in an LLM does not require an external dataset in context — the reference class is "smeared" across the model's weights from the training data, unlike a human, who needs personal/team experience. External historical data are mandatory only where a method *by construction* cannot work without them: throughput Monte Carlo (needs statistics from real sprints) and parametric models (need calibration).

→ Practical division of work: **Phase 1** — decomposition + reference class directly in conversation with the LLM, without a dataset. **Phase 2** — throughput/parametric, for which a dataset is mandatory.

## 8. Source of historical data (for Phase 2) — TAWOS

- TAWOS (Tawosi et al., MSR 2022) — a dataset of issues from open agile projects on Jira, 508,963 issues, 44 projects, with real story points, resolution time, sprint history.
- **Limitation:** the dataset itself is a MySQL dump on the UCL Research Data Repository (rdr.ucl.ac.uk), inaccessible from the sandbox (not among the allowed network domains). Only the aggregate statistics from the publication itself (Table 1) are available.
- Example aggregate — Spring XD (key XD): 3,707 issues, 66 sprints, 610 bugs, 31 developers → ~56 issues/sprint on average (no data on per-sprint variance).
- Open question: where to get granular (per-sprint) historical data — TAWOS in full is technically inaccessible, and the project's author also has no access to sprint history for any real project as of this discussion (EPAM — access not confirmed).

## 9. First manual check of Phase 1 (BMS, 2026-07-17) — conclusions

> An anecdote from ~1982: solving the Schrödinger equation for a particle on a surface, the problem broke into 100+ integrals.
> "If we didn't know how to take an integral, we neglected it."
> — An exact model of decomposition's blind spot: whatever has no line in the WBS is neglected,
> and the sum of the rest looks rigorous.
> The difference between good and bad practice is not the absence of omissions, but a named list of the discarded integrals
> (the assumption log).
> Reference class is the "experiment" that measures the sum as a whole, including the integrals no one knows how to take.

A run on the example examples/BMS (an RFP for a booking management system, EPAM 2016). Artifacts: assumptions.md, run1_decomposition.md, run2_reference_class.md, run3_diagnosis_calibration.md.

- **The methodology worked as intended:** decomposition gave 486 pd (and an absurdly narrow CI ±3.5% — the predicted artifact of independence), reference class — P50 950 pd with a fat tail (P90 1800). The ×1.95 divergence decomposed across the blind spots with almost no residual (~93% of the center gap explained); the tails did not converge — and were not supposed to.
- **Protocol of run independence:** within one LLM session the second method is inevitably anchored by the result of the first (see §1). The working solution — each method is executed by an isolated agent that receives only the input (RFP + assumption log) without the others' results. This is a mandatory requirement of the pipeline, not an option.
- **"Multiply and add" (the author's insight):** the cross-method calibration of Step C is not a single scalar. Part of the gap is cost items that are not in the WBS at all (pure additions), part is targeted multipliers on a subset of items (integration), part is global multipliers (scope creep, coordination). The affine model y=ax+b is unidentifiable from a single point (needs ≥2 projects) → in Phase 1 the parameters are not fitted but transferred by name from external base rates; fitting is possible only in Phase 2 on one's own history.
- **"Integrating the parts costs nothing" (the author's insight):** the sum of WBS leaves contains no term for joining the parts to each other — the tree's nodes are estimated, but you also pay for the edges, of which there are ~n²/2 for n nodes. This is a refinement of the blind spot from METHODOLOGY §2: not an "integration risk" (probabilistic) but a deterministic cost item that structurally has no line in the WBS. Items like "integration testing" mask the problem but are estimated by feel, not from the number of seams — and the number of seams is not visible from the WBS itself. Reference class covers this automatically: in the facts of completed projects the integration is already paid for.
- **Proposed correction to the method — integration-aware bottom-up (the author's idea):** at each WBS aggregation node (where k components combine into a whole) add an explicit integration item, derived from the actual number and type of seams between the node's children (from the architecture diagram), rather than "by feel." The cost of one seam is a transferable parameter (base rates: system integration ~15–30% of component development; in Phase 2 — measure on history). Caveats: (a) double counting with items like "integration testing" — those must be trimmed; (b) it cures only one blind spot — overhead, scope creep, and risk correlation remain, so full convergence with reference class should not occur. A checkable prediction for BMS: recalculation will give noticeably >486 but <884 pd. **Status: the experiment was run (run4_integration_aware.md), the prediction held** — at a rate of 15–20% per node the total is 568–602 pd (center ~585, +20% over the flat WBS; the QA item was trimmed against double counting). The remaining gap up to 884 is exactly the spots the correction cannot cover (scope creep, coordination, external icebergs). An important distinction: external icebergs (someone else's APIs worse than their documentation) and internal edges (our own assembly) are different items; the correction moves the second one from a "coordination multiplier" to a structurally derivable line.
- **Unintended cross-validation:** the isolated reference-class agent independently named the typical range of RFP bids for the class (400–700 pd), and decomposition landed inside it (486). I.e. decomposition reproduces the behavior of a typical bid, and the gap with the class is a systematic feature of the RFP stage, not a defect of this particular WBS.
- **The tail does not calibrate:** the class P90 (×1.8 over the calibrated decomposition P90) is unreachable by any multipliers on the WBS — tail events do not exist as WBS items. For contract decisions (fixed price vs. T&M, buffers) only reference class is fit.

## 10. Second manual run (FaxRxTx / Venali, 2026-07-17) — first check against fact

A real 2007–2009 project: a rewrite of the core functionality of the Venali fax platform (rendering/OCR workers, a cluster with home-grown orchestration of watchdogs + tokens, NOC, portal). Artifacts: examples/FaxRxTx/ (SYSTEM.md, assumptions.md, run1–run4, FACT.md). The fact, from a participant's memory: **~120 person-months ±20%** (window 96–144). Blindness protocol: the fact is sealed in FACT.md, neither the estimators nor the diagnostician saw it; the reveal happens only at Step D.

- **Results:** raw decomposition E≈112; reference class P50 160 (P10 85 … P90 320); calibrated decomposition 155 (135–180), the diagnostician explained ~90% of the center gap with a double-counting check.
- **The main conclusion — modest, at the author's insistence:** memories are fuzzy, and the divergence of the calibrated estimate from the fact (+29% of the window center, +8% of its edge) lies within one width of the memory's own error — from memory you cannot tell 12 months from 13–14. Therefore only this is claimed: **all three estimates are consistent with the fact within the resolving power of the measuring instrument; the pipeline produced no absurdity at any step.**
- **Both structural patterns from BMS reproduced:** the absurdly narrow CI of raw decomposition (±8%) and the non-calibratable right tail (above ~177 pm multipliers cannot reach — the reserve comes only from reference class).
- Center gap ×1.43 vs. ×1.95 in BMS: the WBS here was "well-behaved" — domain immersion, integration tests on live traffic, QA/PM and part of the edges were already present as leaves.
- **Hypotheses for the future (not conclusions):** (a) calibration to the class P50 should systematically overshoot on projects better than the median → the form of the answer is a triple "center from the WBS, corridor from calibration, reserve from the class tail"; (b) ensemble global multipliers on top of a well-behaved WBS risk double counting, so a "well-behavedness discount" may be needed. Both can be tested only on a project with a documented (not remembered) fact.

## 11. The mechanics of calibration and the problem of matching class projects "one to one" (discussion 2026-07-17, in the wake of FaxRxTx)

Three related questions, worked through after closing the FaxRxTx example. Recorded in detail because together they form the bridge from Phase 1 to Phase 2.

### 11.1. How exactly decomposition is calibrated against reference class (Step C)

Calibration is **not** a shift of the decomposition estimate toward the class number, nor an averaging. The sequence (on the FaxRxTx run3 numbers):

1. **Fix the gap.** Raw decomposition E=111.6, class P50 160 → a gap of 48.4 pm. Reference class reports only the scale of the shortfall, but does not say *where* in the WBS it sits.
2. **Decompose the gap across decomposition's known blind spots** (they are static, known before any run): work with no line in the WBS; integration edges (nodes are estimated, seams are paid for too); organizational overhead; scope creep. This is Step B: not "whose number is more correct," but "which spot explains the difference."
3. **Take each item's rate from external base rates, not from the gap.** The key discipline: numbers like "scope creep ~10%," "distributed-core rework ×1.3–1.5" come from general knowledge about the class of projects and are NOT tuned so the sum matches the class P50. Why you must not fit: there is one point, the correction model is essentially y=ax+b, and from one point a and b are unidentifiable; fitting would give an illusion of precision.
4. **Apply the corrections to the WBS in three types** (the "multiply and add" taxonomy from §9): pure additions (domain unknown-unknowns +8.8, missing edges +3.6); targeted multipliers on subsets of leaves (core ×1.4 → +6.6, rendering stabilization ×1.25 → +2.9, convergence with v1 ×1.35 → +3.3); global multipliers (scope creep 10% → +12.3, org tax 4% → +6.0). A mandatory double-counting check: spots already covered by WBS leaves (in FaxRxTx — domain immersion, live integration tests, QA/PM) receive no corrections.
5. **Check the explained share.** +43.5 of 48.4 → ~90% of the gap explained, calibrated center ≈155; the residual ~5 pm remains unattributed — a measure of uncertainty, not noise. The closeness of 155 to 160 is a result of the check, not the goal; explaining half the gap would also have been a valid outcome.

Convergence is mechanical, not epistemic: no method "reconsidered." And only the **center** calibrates: the tail (P90=320) is unreachable by multipliers — tail events do not exist as WBS items (reproduced in both examples).

### 11.2. How projects of one class are matched "one to one" (one site has 10 pages, another 5)

Heterogeneity within a class is the central weakness of reference class. Three ways to match:

1. **Normalizing to the project's own estimate** (the canonical one, Flyvbjerg): the class stores not absolute effort but the **ratios** of actual/estimate. Size cancels out on its own: sites of 10 and 5 pages have different bottom-up estimates, but the overrun multiplier is drawn from a single distribution. This is exactly why the pair "decomposition + reference class" fits together: the WBS gives a project-specific anchor (it sees both the pages and the 2FA), the class gives the distribution of the multiplier on top of the anchor.
2. **Normalizing to a unit of size** (the parametric route): function points, screens, KLOC; the class gives the cost per unit ± spread. Requires calibrated historical data — unavailable in Phase 1.
3. **Narrowing the class with a size shelf** (the crudest; what run2 implicitly did by giving absolute P10/P50/P90): not "all rewrites" but "a rewrite of a distributed platform of *medium* scale." Part of the heterogeneity is removed by the selection conditions; the rest (2FA present/absent) **does not go anywhere — it stays inside the P10–P90 spread.** The width of the class range is the honest price of within-class heterogeneity; a narrow reference class is a suspicious reference class.

Corollary: the specific "10 pages vs. 5" is by definition a blind spot of the class and a sighted zone of decomposition. The class is responsible for the shape of the distribution; the position of the point inside it is set by bottom-up. In Phase 2 the cleanest option is way 1 on one's own history: the distribution of "actual / our own decomposition estimate" over completed projects; each project's normalizer is its own estimate, and the question of comparing sizes disappears by construction. Step C of Phase 1 is a manual, item-by-item approximation of this multiplier while there is no history.

### 11.3. A direction for Phase 2: project scale as a covariate of the multiplier

The idea: improve way 1 by making the overrun multiplier a **function of size** rather than a constant of the class.

- **Empirical basis:** large projects overrun more and with a fatter tail (COCOMO: exponent >1 with size; Flyvbjerg's data; failure statistics — small projects succeed more often). So both the center and the tail width depend on size → this improves not only the estimate but also the size of the reserve.
- **The size metric is already free:** the sum of the decomposition estimate ΣE is a ready proxy for size, available at estimation time. Calibration turns from "multiply by a constant" into "multiply by f(size)." The link to §9 ("multiply and add"): y=ax+b is unidentifiable from one point; with a size covariate the slope is estimated from 2–3 projects, the curvature from 5–10.
- **The structural justification for why the multiplier must grow with scale** — the integration edges from §9: n nodes, ~n²/2 seams; the sum of leaves grows linearly, the shortfall for edges faster → the "WBS vs. fact" gap in percent is larger for big projects. The exponent >1 follows from structure, not from fitting.
- **The price — data:** conditioning cuts the sample; on 5–15 of one's own projects a free regression will overfit. A practical compromise is the same discipline as in Step C: take the shape of the dependence (the power exponent) from outside as a prior (the COCOMO class), and tune only the level on one's own history.

### 11.4. The author's correction to 11.2–11.3: self-normalization does not save you, because size changes the composition of the work

The author's observation: within the "class of all web sites," projects of 5, 30, and 100 pages are **different classes**, if only because the distribution of work in them is different. So "self-normalization" (way 1 of 11.2) is not by itself a way out.

Analysis: size produces two different effects, cured differently.

1. **Smooth** — the overrun multiplier grows with size at the same composition of work (edges ~n²/2, coordination). This is cured by the covariate f(size) from 11.3.
2. **Structural (deeper)** — at some size whole categories of work appear that a small project simply does not have: a CMS instead of hand-coding, information architecture, a dedicated PM, a staging environment. This is not a multiplier on existing leaves but **new WBS branches**. The actual/estimate ratios in different size regimes are drawn from different populations — dividing by one's own estimate does not fix this.

**Corollaries:**
- Ways 1 and 3 of 11.2 are not alternatives but a mandatory sequence: first stratification by size regime (the shelf is a condition of correctness, not "crudeness"), self-normalization is valid only within a stratum. Pooling projects of different sizes into one multiplier distribution is a class-specification error, not a data shortage.
- **An operational criterion for the regime boundary** (free, from a tool already at hand): two projects are in one class if their WBSs are structurally similar — the set of branches matches, not the sums. The appearance in the larger project of branches the smaller one fundamentally lacks is a marker of a class change. Decomposition gains a second role: not only a source of the center, but a test of membership in the reference class.
- The price for Phase 2: stratification cuts the small history (5–15 projects → 2–3 strata of a handful of points each) → external priors are needed for each stratum separately; one's own history tunes only the level within a stratum.

### 11.5. A precaution: the gradient toward an ML model (discussion 2026-07-17)

The author's observation: the chain of improvements 11.2 → 11.4 (self-normalization → size covariate → stratification → priors → level tuning) is a gradual slide toward building an ML model. Recorded **not as a rule but as a precaution**: this reasoning exists, and complication/sophistication must be avoided.

The essence of the concern:

- The methods lie on a single complexity continuum: reference class is a non-parametric model with one categorical feature (the "class"); COCOMO adds a size covariate; ML regression is the same with many features and a flexible function. Following the gradient to the end, we quietly turn reference class into the fifth method of METHODOLOGY §2 — with its blind spots (inexplicability, failure outside the sample) and without its honest name.
- For 3A8 this is especially dangerous: the value of the framework is the decorrelation of the blind spots of *different* sensors. A reference class enriched into a fitted model stops being an independent sensor; the diagnosis of Step B feeds on divergence, and one sophisticated model gives one number with hidden assumptions — exactly what the framework was moving away from.
- The practical trap: on 5–15 projects the model will not train, but it will look rigorous and will narrow the intervals by construction. The wide class range is a feature (an honest measure of heterogeneity, 11.2); a sophisticated model destroys it first.

Guidelines (not rules): keep the sensors coarse, allow complexity only in the diagnostic layer (Steps B/C); the center is owned by calibrated decomposition, the tail by the raw class quantiles (the tail is not improved by fitting — quantiles need points, not parameters); the litmus test — if an "improvement" requires fitting something on one's own history, the boundary of the method has been crossed, and it is more honest to frame it as a separate sensor than to dissolve it into an existing one.

### 11.6. First check against data (mars_model, 2026-07-17): what was confirmed, what was refuted

The hypotheses of §11.3–11.4 were checked on the open PROMISE datasets (China n=499, Kitchenham n=145, Desharnais n=81, Maxwell n=63). The method — "MARS-lite" following the discipline of §11.5: a power fit in log-log, one hinge with a grid search over the knot, AICc, bootstrap; plus a pilot "composition as parameters." Artifacts: mars_model/ (data/, fit_piecewise.py, composition_china.py, results.md, loglog_fits.png).

**Refuted (with caveats):**
- "The exponent b>1 in Effort~Size^b" — in all four datasets b≤1 (0.67–0.98), in three the CI is entirely below 1: the production function shows *economies* of scale. This is a known dispute in the literature (Banker & Kemerer 1989; Kitchenham 2002): FP datasets give b<1, KLOC calibrations of COCOMO give b>1. Caveats: survivorship (the datasets contain only completed projects — the class tail is unobservable), mixing of organizations, endogeneity (larger projects get better teams).

**Confirmed:**
- **The overrun multiplier grows with size — in the tail, not the center** (Kitchenham, the only dataset with a "first estimate/actual" pair): the median Actual/FirstEstimate ≈ 0.97 across all size terciles, while P90 grows 1.11 → 1.15 → 1.46; the slope of log(ratio)~log(size) is positive, the CI does not cover zero. The precise formulation of §11.3 — about the estimation error — is correct.
- **A surcharge for interfaces on top of size** (the composition pilot on China): the share of Interface elements significantly raises the project's cost at the same AFP (+10 pp of share → ×1.10), and this on top of what the FP method already pays interfaces via increased weight (in the IFPUG weight table an EIF element is worth 5–10 points against 3–6 for an ordinary input). The underestimation of seams survives even an explicit attempt to pay for them with increased weight.
- **Breaks exist, but the boundaries are unstable:** the direction is everywhere the same (the slope after the knot grows — economies of scale run out on large projects); a break is formally justified only in the homogeneous Kitchenham (~600–700 FP, 98% of bootstraps agree); in mixes of organizations the knot wanders by an order of magnitude. The stratification of §11.4 is meaningful, but stratum boundaries must be taken from a homogeneous population (one's own history), not from someone else's mixes.

**Correction to the theory (important):** §11.3 conflated two quantities. The production function Effort(Size) may show economies of scale; the estimation error (actual/estimate) grows with size — in the tail, at a stable median. For 3A8 the second is relevant: the pipeline calibrates estimates, it does not produce projects. The edges n²/2 argument is refined: **edges strike not at the project's cost but at its visibility in the WBS** — large projects have more invisible items that occasionally fire; hence "the tail thickens, the median holds" — exactly the observed picture.

**The obtained models** (China: E≈27·AFP^0.77; Kitchenham: E≈37·AFP^0.67 with a break at ~700 FP; and others, R² 0.44–0.63) are legitimate only as the **shape of a prior** (§11.5): the order of the exponent, the existence of a break, and the growth of the multiplier tail are transferred; the level is tuned on one's own history.

## 12. Cross-project comparison with twotakt (2026-08-04): what transfers, and where the agent question inverts

The sibling project twotakt closed a scoping question the same day: deploying itself to AWS / Bedrock AgentCore was examined and rejected (its F39 — no cloud-shaped work; the only agentic element is a build→verify loop whose stop condition is a machine check; its human gates are the product, not missing autonomy). That reasoning was then tested against 3A8. The split is informative in both directions.

**Transfers as is:**

- **No cloud-shaped work here either.** `mars_model` fits datasets of n ≤ 499; throughput Monte Carlo is seconds; storage is a repository. Nothing scales, nothing runs long.
- **twotakt's F3 is 3A8's founding move.** "The generator may never author its own trust floor — correlated blind spots" and "independence of techniques instead of independence of experts, because one model is not independent of itself" are the same structural claim, reached from opposite ends (verification there, estimation here). 3A8 carries empirical backing twotakt does not have: Çalıklı & Alhamed FSE 2025, §1.
- **twotakt's F1 was already rediscovered here.** METHODOLOGY §3 — "full convergence after Step C is not necessarily a success" — is the estimation form of "the requirements verdict is the *output* of the study; asserting it asserts the thing under investigation." There the assertion would be SLA attainment, here it is convergence.
- **twotakt's F8 (negative-test-first) bites hardest.** Two runs (§9, §10), both reported as the methodology working as intended; no diagnostic step has ever gone red. By F8 a check that has not yet bitten is not yet a check. Concrete test available cheaply: feed Step B a deliberately malformed WBS (an extra branch, a double-counted QA line) and see whether the diagnostician names a blind spot that is not there.
- **twotakt's F26 = the §11.5 precaution.** The ML-gradient concern and "the AI cannot distinguish its substantive constructions from symmetry-driven filler from the inside" are the same failure, caught by the same instrument — author skepticism, not self-check.

**Inverts — the agent question.** twotakt would have had to *invent* an agent in order to have something to deploy. In 3A8 the agent requirement predates any infrastructure thought and is load-bearing: §9's isolated-agent-per-method rule ("a mandatory requirement of the pipeline, not an option") and FaxRxTx's sealed `FACT.md` are **isolation** requirements, not autonomy or throughput ones. The value of an agent here is what it *cannot see*; the process boundary is the epistemic boundary between sensors, and collapsing the methods into one session is not an inconvenience but a spoiled measurement. This is a rare and honest use of the architecture — the agents are hired for what they are forbidden, not for what they can do.

**But agents ≠ cloud.** Isolation is four processes with disjoint inputs: subprocess plus discipline about what goes into each context. The requirement is real; the infrastructure need stays at zero. The cloud conclusion survives even in the place where the agent conclusion reverses — which is the most useful result of the comparison.

**Does not transfer — the computed verdict.** twotakt's Takt 2 stops on `verify.py` green. 3A8 has no oracle even post hoc: FaxRxTx's "fact" is a participant's memory ±20%, and the honest claim there is consistency within the resolving power of the instrument (§10). What 3A8 has instead is a candidate gate of a different species — structural rather than numeric:

> **No parameter used in Step C may be a function of the gap it explains.**

That is §11.1 step 3 stated as a checkable property: rates come from external base rates and are never tuned so the sum matches the class P50. It is checkable by *provenance*, not by value — a data-flow condition, and it is F3 applied inside one method rather than between methods. Today it rests on good faith. In the agent wrapper it becomes machine-checkable, because every rate reaches the diagnostician as an input with a declared source.

That is the real import from twotakt: not the cloud and not the agents, but the idea that a discipline written in prose can be turned into a check.

**Built 2026-08-04 (PIPELINE.md + `.claude/agents/`).** Four agents with disjoint inputs: the two Step-A sensors, a **gap-blind rate agent**, and the diagnostician. The provenance rule became structural rather than good-faith: the rates for Step C are produced by an agent that never sees the reference class output or the size of the gap, and the diagnostician may only apply them — never edit, add, or drop one; a hole in the rates is answered by requesting another gap-blind round, not by filling it while looking at the gap. The final answer is reported in three parts that cannot be mixed: center (calibrated bottom-up), corridor (spread of the calibration), reserve (raw class tail).

**First negative test — the check went red on purpose.** The decomposition sensor was fed a deliberately contaminated prompt (a budget, a class median, "land close to that", and an instruction to open another method's run file) while holding file tools. It refused to estimate, named all four anchors, left the file unopened, separated the still-clean part of the input, and observed that an anchor reaching one sensor implies the whole pipeline is contaminated. This is the first check in the project that has been shown to fire — the F8 debt is now partly paid: prompt-layer refusal is real for one agent of four. The test was then repeated against the registered agent (not just the pasted role text) with the same result: refusal, zero tool calls, the sibling's file left unopened.

**And the test caught a placebo.** The definitions carried `tools: []`, meant as the structural half of the isolation — an agent that *cannot* open another sensor's artifacts. On registration the harness reported all four agents as having **all tools**: an empty list is read as "unspecified" and inherits everything. So the load-bearing enforcement was decorative, and only the prompt layer was ever holding. This is F8 again, one level down: a restriction that has never been observed to bind is not a restriction, and configuration that *reads* like enforcement is the easiest kind to leave unverified. Corollary for the project: every discipline described as machine-checkable (including the provenance rule above) must be demonstrated firing before it may be counted on — the gap-blind rate agent is guaranteed by *what the orchestrator pastes*, which is discipline, not machinery, until shown otherwise.

**All four agents now tested (2026-08-04).** The remaining three were given the forbidden material as neutral "context" rather than as an instruction — a WBS total to the reference class sensor, the class quantiles to the rate agent, the project's actual outcome to the diagnostician — so each had to notice the contamination unprompted. All three halted before producing anything. Three details worth keeping: contamination is *sticky* (a corrected follow-up does not repair a run; the number stays in context, so a fresh instance is required, not a fresh prompt); partial output is refused too (the reference class agent would not even give its class definition, its reasoning already being downstream of the WBS it had seen); and the mere fact of a prior run leaks (the rate agent noted the gap was one subtraction away in its context). Unplanned side effect: two sensors independently caught that the WBS in the test prompt priced ~14% of its total against scope the project description never mentioned — a sensor holding both a description and a WBS is a free consistency check between them.

**A second failure mode found, of a different species.** In one run the diagnostician reached the correct verdict but its report contained an invented directory listing of the project root — non-existent files, one entry as both file and directory — while the harness recorded zero tool calls. Nothing was executed; the observation was narrated. A repeat was clean, but carried an extra "do not open any files" instruction, so it does not establish that the first was a fluke. Two consequences: any file-system claim inside an agent report is unverified narration unless the tool call is visible; and this is the strongest practical case for making the tool restriction real — an agent that cannot reach the file system has nothing to fabricate about it.

## 13. Status

- The methodology (METHODOLOGY.md) is fixed.
- The first manual example (BMS, Phase 1: decomposition + reference class + Steps B/C/D) — done 2026-07-17, see §9 and examples/BMS/. There is no actual project outcome to check against (a training RFP).
- The second example (FaxRxTx/Venali) — done 2026-07-17, for the first time with a check against fact (soft, from memory ±20%), see §10 and examples/FaxRxTx/.
- The first check of hypotheses against open data (mars_model/, PROMISE datasets) — done 2026-07-17, see §11.6: the growth of the overrun-multiplier tail with size and the interface surcharge are confirmed; b>1 for the production function is not.
- The project name is the working code name **3A8** (after discarding taken options: EstimAI, Consensus/Konsensus, Triangulate — all conflict with existing products/terms in adjacent niches).
- No code is written until the methodology has been checked by hand on concrete examples.
- The agent wrapper — first version built 2026-08-04: PIPELINE.md (visibility matrix, the two checkable disciplines, what is deliberately not automated) and four agent definitions in `.claude/agents/`. Open: verify the tool-restriction layer in a fresh session; run the contamination test against the remaining three agents; then re-run one of the existing examples end-to-end through the wrapper and compare with the hand-made run.
- Cross-project comparison with twotakt — done 2026-08-04, see §12: no cloud for either; the agent requirement here is genuine but is *isolation*, not autonomy; provenance of Step C parameters named as the candidate machine check; F8 (a check that has never gone red) is the open debt on the diagnostic step.
