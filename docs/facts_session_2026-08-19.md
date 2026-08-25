# Session record — 2026-08-19 — axis closure, and the first Hotyn runs

**Purpose.** One session's facts and materials, written to be merged with other session records in a
later analysis. Numbers, their sample sizes, and where the raw data sits — separated from
interpretation, and followed by a list of claims this session made and then withdrew.

**Scope, stated so the merge does not double-count.** This record covers the closing of `run 17` and
the whole of `run 18`. **It does not cover runs 19–22, `docs/technology_catalogue.md`, the split
requirement lists, `run18` §3c, or the `work-crosser` / `work-estimator` sensors** — all of which
exist in the repository and were produced by other sessions. Where this record and those disagree,
those are later and win.

**Repository state at the end of this session: nothing committed.** Everything below is in the working
tree only.

---

## 1. Facts — the Lytin generation (run 17)

Instrument: `Lytin-D 5.0`, one-step decomposition of an RFP into a work breakdown. Raw data in
`examples/BMS/run17_raw/`, analysis in `examples/BMS/run17_axis_projection.md`.

| # | Fact | Evidence | Confidence |
|---|---|---|---|
| L1 | **ΣE ≈ 10.38 pd × leaf count**, range 9.47–11.32 (±8.9%) | 8 batches, 2 models, 4 instruments, n=5 each | strong |
| L2 | **Leaf size does not move between models** (×1.01–1.07) while **leaf count does** (×1.87–1.97) | 3 instruments | strong |
| L3 | Model gap on effort: ×2.021 (mixed axis) · ×2.055 (axis S) · ×2.052 (axis P) · ×2.371 (axis S rerun) | 4 batches, n=5 each | strong |
| L4 | Sonnet ÷ Opus conversion **0.4727 ± 7.2%** | same 4 batches | moderate — see C2 |
| L5 | **Haiku 4.5 is below the engine's capability floor**: 1 of 5 runs executed the protocol, CV 59%, range ×4.17 | n=5, axis P | strong |
| L6 | C6 (split consistency) is **systematically positive**, batch means +8% to +20%, one run 22 of 22 rows positive | ~20 runs | strong |
| L7 | **Transition off the predecessor process is not generated**: Sonnet 0 of 10, Opus 3 of 5 on axis P and 0 of 5 on axis S | 20 runs, scoring rule fixed after collection | moderate — rule not pre-registered |
| L8 | Testing is placed in **20 of 20** runs | 20 runs | strong |
| L9 | Two mechanical gates on the readings block catch all 4 broken Haiku runs and pass the clean one; a third gate was added after RS-4 | n=5 Haiku + 1 case | strong |
| L10 | One run in 5 (**RS-5**) produced a lifecycle top level under a subsystem-axis prompt — the declared axis was not applied, and no gate detects it | n=5 | single observation |

**Axis effect ×1.015 is NOT a fact of this record.** It was computed, reported in-session as a
headline, and is **provisional**: the gating control that decides whether the two axes are distinct
was never run, and the axis comparison was discontinued (§4 below). It must not be cited.

### Materials

- `run17_raw/axisP_trees_opus.md`, `axisP_trees_sonnet.md` — leaf inventories, 10 runs
- `run17_raw/axisS_rerun_trees_*.md` — leaf inventories, 10 runs
- `run17_raw/haiku_readings.tsv`, `haiku_protocol_violations.md`
- `run17_raw/prereg_overlap_metric.md`, `prereg_haiku_third_point.md` — both pinned before results
- `run17_raw/MANIFEST.md` — prompt md5s, models, engine stamps, known gaps

**Gap in the materials, permanent:** the ten axis-S runs of 2026-08-18 (SO-1…5, SS-1…5) have **no leaf
inventory**. Their trees were not preserved and are unrecoverable; only their instrument readings
survive. This is what forced the axis-S rerun.

---

## 2. Facts — the Hotyn generation (run 18)

Instrument: `Hotyn-M 1.0`, requirement list → product model, no numbers. Then a closure test with
`Hotyn-D`. Raw data in `examples/BMS/run18_raw/`, analysis in
`examples/BMS/run18_product_model_pilot.md`.

Input: `examples/BMS/requirements.md`, md5 `554ea3608dd0602f0ddf2f7e7b82178c`, N=73.
Design: 2 models × 2 processing orders, **n=1 per cell**.

| # | Fact | Evidence | Confidence |
|---|---|---|---|
| H1 | **Anchored structure (skeleton + accretion) is 82–87 nodes, CV 2.5%**, model gap ×1.036 | 4 runs | moderate — n=1 per cell |
| H2 | The split producing it is nearly arbitrary: **skeleton 15–75 (×5), accretion 7–71 (×10)** | 4 runs | moderate |
| H3 | **Derived (completion) nodes carry the model gap**: Opus 20.5, Sonnet 4.5 — **×4.56** | 4 runs | moderate |
| H4 | **Zero deferrals**, all runs, all passes, including the adversarial reverse order | 4 runs | moderate |
| H5 | Empty skeleton nodes: 0, 0, 0, 12 of 75 (16%); all judged infrastructure, none dropped silently | 4 runs | moderate |
| H6 | **Closure test: ΣE ratio ×1.344** (Opus 1281.77, Sonnet 953.55) on one shared closed model, against ×2.05 for the one-step instrument — **67% of the gap removed** | n=1 per model | single observation, but decisive direction |
| H7 | Mechanism: **leaf count ratio ×1.96 → ×1.21**. Sonnet produced exactly 1 leaf per model node (109/109); Opus subdivided 22 of 109 | n=1 per model | single observation |
| H8 | **Price per leaf moved the wrong way**: ×1.03 under Lytin → ×1.099 here. Unexplained. | n=1 per model | single observation |
| H9 | Coverage agreement between models is **Jaccard 0.16–0.27** while anchored size agrees to ×1.036 | 4 runs, 2628 pairs each | moderate |
| H10 | Percentage agreement (94–98%) on the same comparison is **inflated by sparsity and must not be quoted** | arithmetic | certain |
| H11 | Under closure both decomposers reported work they judged necessary and did not add: **Opus 11 items, Sonnet 4**. Every item is technology-derived work | n=1 per model | single observation |
| H12 | Only Opus caught the structural absence (QA, project governance had no node anywhere); Sonnet produced a comparable estimate without noticing | n=1 per model | single observation |
| H13 | `R03` ("the Supplier supports the system") contradicts `A1` ("not included: subsequent operation"). One run of four caught it | 4 runs | certain, and it is a defect in the inputs |
| H14 | All 4 model runs and both closure runs reported `tool_uses: 0` | 6 runs | strong |

### Materials

- `run18_raw/models.md` — all four product models, node by node with coverage sets
- `run18_raw/closure_test_readings.tsv`
- `docs/proposal_product_model.md` — the rules, with predictions registered before the runs
- `.claude/agents/model-builder.md` — the sensor definition (`tools: Glob`)

**Protocol weaknesses in this run, recorded so they are not read as results:**

- The pilot ran through a **general-purpose agent with rules pasted in**, not through the sensor
  definition. Isolation was by instruction and verified after the fact, not enforced by tool absence.
- **n=1 per cell.** Order effect and ordinary run-to-run variance are confounded and cannot be
  separated.
- `run18_raw/models.md` **records no parent pointer for HM-OA's nodes**. Later sessions found this
  blocks normalisation and any structural comparison beyond coverage. Raw model records must carry the
  parent.

---

## 3. Corrections — claims this session made and then withdrew

**Read this section before trusting any figure quoted from the session transcript.** Each of these was
stated confidently before being corrected.

| # | Claimed | Corrected to | Why it was wrong |
|---|---|---|---|
| C1 | ΣE ≈ 10.37 pd/leaf, **±5%** | **±8.9%** | Two further batches widened it; the mean barely moved |
| C2 | Conversion 0.4896 **± 0.9%**, "stable enough to publish as part of the engine spec" | **0.4727 ± 7.2%**, proposal withdrawn | 0.9% was the scatter of three point estimates, each carrying its own standard error of 3–10%. Three numbers landing close cannot give precision better than the error of each |
| C3 | "The run-log format loses what later checks consume" | A **specific, avoidable omission** | The control was already specified in writing before the runs; the log recorded statistics and discarded the sample |
| C4 | A third capability tier "tests whether leaf count saturates" | It does not | Saturation needs a point **above** Opus; Haiku extends the sequence downward only. Corrected in writing before the Haiku results were read |
| C5 | Axis effect ×1.015 reported as an established headline | **Provisional**, withdrawn from results | Its gating control had not run, and then was discontinued |
| C6 | Prediction 2 "confirmed on node counts" (×1.036) | **Not confirmed** on the registered test | The registered test was coverage-partition agreement, not node counts. Right prediction, wrong measure |
| C7 | "The skeleton is the concentrated free parameter of the method" | **Refuted** | Skeleton size ranges ×5 with the anchored total unchanged. The freedom is in completion |
| C8 | "Normalisation makes the closed model canonical" | Removes **one** kind of spurious difference | A canonical form makes equivalent things identical; collapsing single-child chains does not |

---

## 4. Decisions taken this session

- **The axis comparison was discontinued** before its gating control was computed. Four grounds, in
  `run17_axis_projection.md` §7: what the control was to establish is legible directly from the trees;
  the axis is not a controllable factor (RS-5); the mechanism never fired (both axes agree); nothing
  else in the run depended on it. Predictions 1, 2 and the cross-axis half of 5 stand **unevaluated**.
- **`Hotyn` was named as a new generation**, not a version of Lytin. Estimates do not cross the
  generation boundary without a measured conversion. What carries over is what is not about level: the
  capability floor, the gates, the logging discipline.
- **Raw sensor output is preserved in the repository**, alongside the analysis, with a manifest. The
  harness does not persist subagent output — the per-task `.output` files were empty — so
  transcription is the only durable path.
- **Model roles were separated**: readings are produced on Opus and Fable; a weaker tier is still run
  but its numbers are **not part of any estimate** — they are the diagnostic. Every defect this
  project has found was found by disagreement between capability tiers.

---

## 5. Open at the end of this session

Some of these have since been addressed by other sessions; the analysis should check.

- **Completion is unbounded** and carries ×4.56. No constant designed.
- **Granularity inside a declared element** remains free, measured at ×1.21.
- **Why coverage agreement is low** (Jaccard 0.16–0.27) while anchored size agrees to ×1.036.
  *(Later work has answered part of this — see `run18` §3c, not this record.)*
- **Price per leaf drifted** from ×1.03 to ×1.099 and nobody knows why.
- **The requirement list mixes product obligations with work obligations** (R03, R69, R70). Splitting
  it was named as the first next step. *(Done by a later session.)*
- **`R13`** is readable two ways — IT disaster recovery, or mass re-booking during a travel
  disruption. One run called the second reading "the largest single omission in this model". Unresolved.
- **The requirement list's granularity** is one person's judgement, pinned rather than correct.

---

## 6. Procedural findings worth carrying to any session

- **Agent definitions are picked up within the same session.** The project's standing note that they
  are read once at session start no longer holds on this harness; verified on `model-builder`. The
  memory entry has been corrected.
- **`.output` task files are empty.** Subagent output is not persisted by the harness. If it is not
  transcribed, it is lost at the session boundary — which is exactly how the axis-S trees were lost.
- **Windows Python writes cp1252 to the console.** Scripts that print Cyrillic fail on the print, after
  the file write has already succeeded. Check the file, not the exit code.
- **Heredocs with apostrophes break under Git Bash.** Use the Write tool for prose files.
