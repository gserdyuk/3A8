# Backlog

Open work, with the reason it matters and where the evidence sits. Tick a box when the thing is *measured
or fixed*, not when it is understood — this project has repeatedly found that a discipline nobody has seen
bind is not a discipline.

Convention: `- [ ]` open · `- [x]` done, with the commit or run that closed it.

---

## Now — adjudicate what is already written down (settled 2026-08-25)

**The units are settled on both sides and the table is fixed.** `docs/rate_table.md` is a **set of
constants** at 1 pd = 8 net hours; the 2026-08-22 relabelling is withdrawn; the A2/A3 addendum rows are
converted into that unit (117.33 assigned-days = 704 net person-hours = 88.0 table pd). FaxRxTx now
stands at **99.4 staffed person-months against a fact of 120 — x1.21, inside the x1.3 gate** — and it
gets there *despite* pricing the concept stage at 2% of the project where the fact puts it at 17%.
Record: `sessions/2026-08-25_units_discipline_and_the_fixed_table.md`.

- [ ] **Adjudicate the 5 unsizeable elements and the 13 closure violations, gap-blind** (+182 pd). The
      sizing sensors wrote the list themselves before any fact was opened; it owes nothing to the fact.
- [ ] **Rule on the four scope decisions** (`C-DIRECT`, `E-DSP`, `G-SEED`, `U-OPS-USER`), +151 pd if all
      four go the other way. Pure arithmetic afterwards.
- [ ] **`W-F48` is low by x8.5 — the defect is structural.** Stage headcount is a **declaration
      parameter**, like environment count and cycle count; a gap-blind rate author has nothing to make it
      from. Any row that scales linearly in a headcount should refuse to price until it is declared.
- [ ] **A case profile, pinned with the requirements, before any estimate.** Team grade and domain
      experience * declared overheads and what is inside them * the presence fraction * the process *
      **the staffing of every stage the method prices separately**. Everything asked of the author over
      three days was a case condition; none of it was a requirement; all of it was available on day one.
- [ ] **A corridor instrument** — still the only structural gap in the chain. Exit-criterion test 2
      still cannot be applied. The rate-sampling candidate is **withdrawn**: a fixed table is a constant
      and a constant has no dispersion between runs.
- [ ] **A second documented outcome, with its case profile collected first.**
- [ ] **Catalogue defects from run 30**, untouched: `A10` cannot reach the system's own internal API;
      `A9` cannot reach an availability obligation carried by a `behaviour`.
- [ ] **Protocol, carried**: strip `gitStatus` from sensor launches; a truncated subagent reply is
      recovered by asking for a verbatim re-emission, never by re-running.
- [x] **Answered by the author 2026-08-25: yes, it counts.** *"An explanation after the fact is a poor
      explanation — but it is still an explanation."* **FaxRxTx is case 1 of the exit criterion's four and
      passes on the centre: ×1.21, gate [92.3 … 156.0], both repeats inside.** Standing: **1 of ≥ 4 cases,
      1 of 1 passing**; corridor test not scoreable; provenance test passes, nothing is fitted.
- [ ] **Hold cases 2–4 to the stricter rule.** Case 1 is admitted on conventions supplied after the
      estimate existed, which the author's own wording marks as weaker evidence. It sets the **floor**,
      not the standard: for every further case the **profile is pinned before any estimate**. Otherwise
      the gate measures how well conditions can be reconstructed afterwards.

## Suspended — R9–R12, the cross-generation readings (2026-08-25)

All four compared this project's estimates across generations (111.6 → 237.8 → 503 → 69.2 pm, class at
135 and 160) **in units that were never declared**. The Lytin-era runs said "person-months" without
saying whether that meant staffed presence, assigned days or net hours — the same ambiguity that took
three days to resolve for one table. Reinstating any of them requires first recovering the unit of the
run it cites: cheap for the two July 2026 runs, possibly impossible for the August pipeline.

## Superseded — level, not variance (written 2026-08-22, before the unit correction)

**The chain was run end to end against the one documented outcome and missed low by x1.735.** Two
independent classification repeats agreed to x1.032, so the variance programme has done its job; the
binding question is now the *level*, and it has exactly two candidate homes that n=1 cannot separate.
Evidence: `examples/FaxRxTx/run32_fact_comparison.md`, session record
`sessions/2026-08-22_faxrxtx_validation.md`.

- [ ] **The granularity experiment — the one measurement that makes today's result actionable.** Re-run
      `Hotyn-M 1.1` on the same pinned FaxRxTx list with a granularity instruction producing ~160-170
      elements; cross, size and price it with **no rate changed**. If the total tracks element count
      towards ~2500 pd, the instrument is measuring the modelling act (R8) and the rate table's level is
      innocent. If it does not move, the level is the problem and the vintage is the candidate.
- [ ] **Decide whether `L-1` = x1.735 stands.** Fitted on FaxRxTx at n=1, recorded outside the rate table
      with three binding conditions. If the experiment above shows element count carrying the gap, `L-1`
      must be **withdrawn, not re-fitted** — a factor correcting for a modelling artefact double-counts the
      moment the modelling changes.
- [ ] **Cross `HM29-OA2`** (87 nodes against 97): the cheapest second granularity point, in the opposite
      direction from the experiment above, and the structure sensitivity everything downstream currently
      carries unquantified.
- [ ] **Give the chain a corridor instrument.** Exit-criterion test 2 could not be applied at all: the
      chain declares no P10-P90. Leaf independence gives an absurdly narrow CI (the artefact both earlier
      generations flagged); SigmaO..SigmaP assumes perfect correlation and spans x4.3. Neither is an 80%
      interval. Until this exists, only one of the criterion's three tests is scoreable.
- [ ] **Acquire a second documented outcome.** The gate needs four cases and has one — and that one is now
      **spent** for the calibrated chain, because `L-1` was fitted on it.

## Protocol — three carried, one new

- [ ] **Strip `gitStatus`/commit subjects from sensor launches.** Fourth independent catch; all eleven
      sensors run on 2026-08-22 reported the injection and quarantined it. The explicit quarantine
      paragraph now added to every prompt works — no run stopped, all reported — but it is a workaround.
      Mechanism to investigate: launching sensors from a cwd outside the repository, or a harness setting.
- [x] **Probe before the first batch** — held again 2026-08-22 (`Lytin-F 5.0`), and all eleven sensors
      printed their own correct engine stamps.
- [ ] **A subagent reply can arrive truncated** *(new, 2026-08-22)*. Run 29's second product model reached
      the orchestrator beginning part-way through §7c; sections 2-5 are permanently lost. **Standing
      practice: check a reply begins at section 1 before transcribing, and recover by asking the agent for
      a verbatim re-emission — never by re-running**, because a re-run silently turns n=2 into n=3 with one
      member discarded.

## Catalogue defects found by the FaxRxTx crossing — to adjudicate

- [ ] **`A10` cannot reach the system's own inter-component API.** `interface` means an exchange with a
      system *outside* this one, so a named internal API is a `behaviour` and draws no contract test.
      Either the class definition or A10's applicability is too narrow.
- [ ] **`A9` cannot reach an availability obligation carried by a behaviour.** Mandatory distribution and
      failure survival state no measurable target, so their statements are filtered out of performance
      testing, and the behaviours realising the same obligations are not of a class A9 applies to. The
      model ends with no measurable availability threshold anywhere.
- [ ] **No home for fixing the defects a parallel-run cycle surfaces.** The gap-blind rate rows price the
      real-stream execution cycles and exclude the fixing; `A6` is per-parent and scoped to the ordinary
      cycles. Named as a hole in `run31_whole_model_assembly.md` §3.

---

## Earlier — projection axes (decided 2026-08-18, superseded in priority)


**The frame is checked before anything inside the frame.** Different cuts of one system are partitions of
one quantity, so they must sum alike — which makes a disagreement between projections *proof of error
without a fact*. That is a class of evidence this project has never had, and it partly unblocks validity
while BMS has no outcome and FaxRxTx has one.

Design and six registered predictions in `docs/proposal_axis_projection.md`.

- [ ] **Implement as `Lytin-D 5.0`**: C2 removed, axis declared in the prompt as an input coordinate. Batch
      the `run12` path removal into the same bump. C1, C3, C5, C6 untouched.
- [ ] **Add the post-hoc placement question** — where did testing, transition, documentation and environments
      end up. "Nowhere" is a permitted answer. This replaces the completeness report, which loses its meaning
      once the fixed branch list is gone, and it recovers what C2 could never see: whether QA sits in a phase
      branch or inside every feature leaf.
- [ ] **Run 2 axes × 2 models × n=5 = 20** and score the predictions. The one that matters: axis effect below
      ×1.4 against a model effect of ×2.021. At ×1.7 or above the frame dominates and everything from C1 to
      C7 is tuning inside the wrong thing.
- [ ] **Check the control first.** Leaf-set overlap between axes above 90% means the axes are not distinct
      and nothing else in the batch is worth reading.
- [ ] **Answer the open question as a by-product** — is the first level stable within an axis. Instability
      there would mean C2's fixity was load-bearing and something has to go back.

## Then — closing the last unpinned parameter

**The ×1.97 leaf-count gap is coverage, and the arithmetic settles it.** Splitting conserves the sum, so
covering identical work in half the leaves needs leaves averaging **13.3 pd** — above C1's ten-day ceiling,
and no run reported a leaf that heavy. Either C1 was violated or the trees cover different work. C1 was not
violated.

The mechanism: C1 is monotone *given a starting judgement*, and the judgement — *is this node above ten days?*
— is free and self-reinforcing. Judged small → not split → stays small. Judged large → split → unpacking adds
+28.9% → larger still. C1 fixed the price of a leaf and left the **entry into splitting** free, and the total
is price × count.

### C7 — coverage at every split *(first: it targets the dominant cause)*

Children must account for everything their parent names; a node that cannot cover its own content with one
leaf is split **regardless of size**. By induction, with the root checked against the source text, the tree
covers the text — and the full text is read once, in one place, instead of being audited globally.
Design and six registered predictions in `docs/proposal_C7_coverage_at_every_split.md`.

- [ ] **Implement as a major version after the axis batch** — number deliberately left open, since the axis
      experiment takes `5.0` and may change what C7 should say. A second splitting trigger adds leaves and
      leaves are priced, so it is major whenever it lands.
- [ ] **Measure n=10 on each of two models** and score the six predictions. The one that matters: cross-model
      ratio falls below 1.4, from 2.021. Above 1.7 the rule is reverted, not tuned.
- [ ] **Watch prediction 2 as the honesty check.** The ratio can close for the wrong reason — by the rule
      inflating both trees rather than repairing the deficient one. Only Sonnet gaining far more than Opus
      distinguishes repair from inflation.
- [ ] **Report leaves gained per branch.** C7 is expected to bind on branches 2–6 and be near-vacuous on
      1, 7, 8, 9, 10, whose content the source text does not name. Equal gains across both would mean the
      circularity flaw in the design is real.

### B — the full reverse audit *(second: it covers the direction C7 cannot)*

C7 only **adds** work that is missing. It has no power to remove work that traces to nothing in the source —
invented work, the failure that inflates a total while looking thorough. That direction needs an inspection,
and it is what the audit is now for. Design in `docs/proposal_reverse_comparison.md` (mechanism B).

- [ ] **Define the audit output**: named findings with citations, not a score. Each names the passage it came
      from and the node it lands on, so it can be checked rather than believed. This is the audit's advantage
      over any count — findings are falsifiable one at a time.
- [ ] **Measure the auditor before trusting it.** The auditor is itself a model. Same tree, both models: if
      the findings differ the way leaf counts did, the problem has been relocated again.
- [ ] **Run it on one Opus tree and one Sonnet tree from run16** — same project, ×2 apart, both already
      written. If the audit cannot tell them apart it is not an audit.
- [ ] **Settle branch 9 with it.** Whether migration work is in this RFP is a coverage question the two models
      answered 10–0 in opposite directions. The audit decides it from the text rather than by preference.
- [ ] **Keep it out of the estimating run.** The auditor sees the text and the tree; the estimator never sees
      the audit. Otherwise the tree gets adjusted to match and the judgement C1 removed comes back — the same
      reason `calibration-rates` is kept blind to the gap it explains.

### A — the behaviour inventory *(demoted: it targeted the wrong half)*

Written when the gap was thought to be part coverage, part granularity. Granularity is now arithmetically
excluded, so a ruler for counting behaviours is aimed at a problem that is not the dominant one. Kept because
it may still be the right **unit of pricing** if C7 fails, but not run first.

- [ ] **Hold until C7 reports.** If C7 closes the ratio, the count question is moot. If it does not, the
      inventory becomes the way to stop pricing by artifact altogether.

## Next — validity

Forty runs, four batches, two models, and not one comparison against an outcome. This is the thing that
decides whether any of the rest was worth doing.

- [ ] **FaxRxTx against `FACT.md`, raw first.** Record the uncalibrated residual before any calibration, then
      calibrate and record how much of the residual the calibration removed. Order matters: calibrating first
      can make a broken instrument and a working one look identical (METHODOLOGY §3 — convergence is not
      automatically success).
- [ ] **Set the expectation for n=1.** One project is a gross-error gate, not a calibration set. It will catch
      a ×4 miss (the FaxRxTx overshoot history says that is a real risk) and will say nothing about a 20%
      bias.
- [ ] **BMS has no `FACT.md`.** Either find the outcome or stop treating BMS as anything but a variance rig.

## Pipeline defects found and not yet fixed

- [ ] **Branch 9 / C2 has no applicability criterion.** All ten Sonnet runs marked migration
      `none, because greenfield`; all ten Opus runs filled it at 32–67 pd. C2's wording is not violated —
      the rule has no way to say the judgement was wrong (run16 §4).
- [ ] **The completeness report can read 100% on a tree missing a branch.** "none, because …" is excluded
      from the denominator, so the rate agent receives a clean signal for an omission. This breaks the
      PIPELINE §1a partition: migration ends up in *neither* the tree nor the blind-spot list, and is
      therefore priced nowhere.
- [ ] **The sensor definition names a sibling run file** — `estimator-decomposition.md:131` points at
      `examples/BMS/run12_seam_readout.md`. The refusal layer held (an Opus run declined it explicitly and
      opened nothing), but the citation is a pointer no sensor needs. Batch the fix with the next version
      bump rather than spending a bump on it alone.
- [ ] **`calibration-rates` did not register as an agent in this session** while the other four did, despite
      the file existing on disk. Verify before the next full pipeline run — an agent that silently fails to
      load is run9's failure in a new place.

## Consequences of σ_model, not yet acted on

- [ ] **Stamp rate cards and multipliers with the model, and treat the model's lifetime as their shelf life.**
      Anything calibrated on one model is a calibration *of that model* (run16).
- [ ] **A third model family.** Both models measured so far are one vendor, one generation. ×2 may be the
      scale of model disagreement in general or a property of this pair; nothing on record separates the two.

## Longer-range

- [ ] **Phase 2 needs granular history** (throughput Monte Carlo, parametric). TAWOS is technically
      inaccessible and no real sprint history is in hand (findings §8). Until that changes, Phase 2 is a
      design, not a method.
- [ ] **Prompt assembly is still manual.** Every contamination test in PIPELINE.md describes a leak a careless
      paste would produce for real. A fixed template with whitelisted fields would make a forbidden field
      impossible to paste rather than merely refused afterwards.

- [ ] **Finish the whole-project estimate.** Everything upstream exists; what is missing is arithmetic plus
      three runs. (a) The work models for batches A and C are already built and transcribed
      (`run21_raw/`), so only the **whole-model layer** is uncrossed: 16 once-scoped activities, E1 across
      three environments, the root's own per-parent items, and the demanded-work branch — R02 at `E7`,
      R03 at `O3`, R69 at `E4`, R70 at `E3`, R64 as its own item. That layer is one small crossing run, and
      the one judgement in it is whether the root's per-parent items reach N68. (b) `Hotyn-D` on batch A
      (154 items) and batch C (195 items); batch B is done. (c) Sum, and project onto all 68 obligations.
      **The honest output is a range with its sources named, not a point**: the estimator's own spread is
      ×1.288 (run 22) and the product model it rests on is one of two that differ ×1.65 in size (run 19).
      Deferred by the author 2026-08-20 — the method question was answered, the number is not urgent.

---

## Done

- [x] **Baseline: what the number is with no method at all.** mean 1074, CV 8.55% — below every version ever
      measured. The output spread was never going to narrow by pinning parameters. `d51646f`, run14.
- [x] **σ_model measured.** Same prompt, second model: mean 762, CV 20.92%. The model alone moves the level
      −29% and produced the first significant difference in spread this project has found. `d51646f`, run15.
- [x] **Does the method reduce σ_model?** No — it widens it, 1.409× → 2.021×, t = 14.70. Cause located: price
      per leaf indistinguishable across models, leaf count ×1.97. `d51646f`, run16.
- [x] **Model added to the stamp.** `(project × engine × model)`; the model half is written by the
      orchestrator, never self-reported by the sensor, so the two halves have different provenance. No sensor
      edit, no version bump, `4.0` keeps its measurements. `d51646f`, PIPELINE.md.
- [x] **C6 measured against predictions registered beforehand.** 2 confirmed, 1 partial, 1 failed — and the
      failure is the prediction the proposal itself named as the one that mattered: discrepancy does *not*
      grow with splitting depth (r = −0.035 pooled, n=20). C6 stays as a reading and will not close leaf
      count. `5f82cdb` (registration) then `21071a0` (result).
- [x] **The constants are a floor, not a narrower.** On the strong model they changed the spread not at all;
      on the weak one they halved it. Invisible in any batch run on a single model. run16 §3.
