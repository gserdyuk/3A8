# Backlog

Open work, with the reason it matters and where the evidence sits. Tick a box when the thing is *measured
or fixed*, not when it is understood — this project has repeatedly found that a discipline nobody has seen
bind is not a discipline.

Convention: `- [ ]` open · `- [x]` done, with the commit or run that closed it.

---

## Now — projection axes (decided 2026-08-18)

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
