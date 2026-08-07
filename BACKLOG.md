# Backlog

Open work, with the reason it matters and where the evidence sits. Tick a box when the thing is *measured
or fixed*, not when it is understood — this project has repeatedly found that a discipline nobody has seen
bind is not a discipline.

Convention: `- [ ]` open · `- [x]` done, with the commit or run that closed it.

---

## Now — comparing the tree back against the text

Two mechanisms, often called the same thing, answering different questions. Keep them apart: one is a
**statistic over many trees** aimed at a constant, the other is an **audit of one tree** aimed at its
correctness. Design in `docs/proposal_reverse_comparison.md`.

### A. The behaviour inventory — is leaf count derivable from the text?

The one unpinned parameter. Everything else in the sensor holds across models to within 3%; leaf count moves
by ×1.97 (run16). Closing it is the difference between an instrument and a reading of a model.

- [ ] **Measure the ruler before using it.** Build the inventory from the source text n=10 and measure the CV
      of the count. If the inventory is as unstable as leaf count, the problem has been *relocated, not
      solved*, and nothing downstream is worth building.
- [ ] **Then measure it across models.** Cross-model stability is the property leaf count failed. Within-model
      stability is only the precondition.
- [ ] **Score the twenty existing trees against one inventory.** run16's Opus (157 leaves) and Sonnet (80) are
      already on record; no new estimation runs are needed to find out whether one tracks the text and the
      other does not — or whether both miss, in different directions.
- [ ] **Only then decide whether a constant is possible**, and register predictions before running it.

### B. The full reverse audit — is *this* decomposition correct?

Take a completed WBS and read it against the **whole** source text, both directions, and judge the
decomposition rather than count it. Distinct from C6, which compares a tree only against *itself*: this
compares it against the thing it claims to describe. Two failure modes, and they are not symmetric —

- **coverage:** something the text requires has no line in the tree (silent omission, the expensive kind);
- **traceability:** something in the tree traces to nothing in the text (invented work, the kind that
  inflates and looks thorough).

- [ ] **Define the audit output**: a verdict per finding, not a score. Each finding names the text it came
      from and the node it lands on, so it can be checked rather than believed.
- [ ] **Run it on one Opus tree and one Sonnet tree from run16** — the same project, ×2 apart, both already
      written. If the audit cannot tell them apart it is not an audit.
- [ ] **Settle branch 9 with it.** Whether migration work is in this RFP is exactly a coverage question, and
      the two models answered it 10–0 in opposite directions. The audit is the instrument that decides it,
      and it decides it from the text rather than by preference.
- [ ] **Keep it out of the estimating run.** The auditor sees the text and the tree; the estimator never sees
      the audit. If the run that built the tree also scores it, the tree gets adjusted to match and the
      judgement C1 removed comes back — the same reason `calibration-rates` is kept blind to the gap it
      explains.

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
