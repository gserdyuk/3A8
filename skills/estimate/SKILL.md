---
name: estimate
description: "The full 3A8 instrument: the bottom-up product-model chain and the outside view run in ignorance of each other, then the divergence is diagnosed rather than averaged, gap-blind calibration rates are applied, and a range with an explained residual is reported. Invoke as /3a8:estimate for a complete estimate of a case."
author: "Gennadiy Serdyuk <gserdyuk@gmail.com>"
---

# /3a8:estimate — the whole instrument (steps 0–6)

You are the **orchestrator**. This skill sequences the other three and adds the comparison.
The frame is `METHODOLOGY.md` (steps A–D); the current implementation is `docs/instrument.md`;
the visibility matrix is `PIPELINE.md`. Nothing here overrides those; this is the run order.

## The order

1. **Step 0 — pin.** `case_profile.md` first, then the requirement list and its split, the
   assumption log, the technology declaration. Exactly as in `/3a8:estimate-product`, Step 0.
   If an outcome exists, seal it in `FACT.md` **and do not open it** until step 6 is written and
   closed.
2. **Step A, bottom-up half:** run `/3a8:estimate-product` (steps 1–4) → net person-hours,
   layers, holes.
3. **Step A, outside view:** run `/3a8:estimate-reference-class` → P10 / P50 / P80 / P90.
   **Separate launches, clean prompts, in either order.** Neither side may see the other.
4. **Step C — calibration rates, gap-blind.** Subagent `3a8:rates-step-c` (`Lytin-K`). Paste:
   the project description, the assumption log, the bottom-up **structure** (elements, items,
   classes). Must never see: the reference class result, the size of the gap, any target. It
   proposes **named corrections** from external base rates; that it never saw the gap is what
   makes them corrections rather than fitted parameters.
5. **Steps B and D — diagnosis and final range.** Subagent `3a8:diagnostician` (`Lytin-G`). It is
   the only participant that sees both sides: paste the bottom-up reading with its declaration,
   the reference class reading with its declaration, the Step C corrections, and each sensor's
   blind-spot list. Must never see: the actual outcome. It reconciles the two declarations and
   sizes the **units** component of the gap first, then attributes the rest through each method's
   blind spot, applies the corrections, and reports the range with its **explained and unexplained
   residual**.
6. **Reveal (yours, only if `FACT.md` exists).** Open the outcome after the diagnosis is fixed;
   write the comparison in the outcome's own unit, converted by `docs/constants.md` §4a; score
   against `docs/exit_criterion.md`. A case whose conditions arrived after its number can be
   learned from; it cannot score.

## Launch discipline, all steps

- Sensors have `tools: Glob` only: paste inputs, never point at files.
- Record the model you launched each sensor on; an estimate is a property of
  (project × engine × model). A batch on another model is a different instrument.
- Before the first launch of a session, run `3a8:version-probe` and compare with
  `tools/check_probe.py`: definitions are read at session start.
- Raw replies verbatim under `examples/<case>/run<N>_raw/`, one run record per step, one
  `MANIFEST.md`. The harness does not persist subagent output; those files are the record.

## The deliverable

Written knowing nothing of the outcome, in the format of `examples/BMS/estimate_BMS_2026-08-22.md` (the fuller SAS documents of 2026-09-08 and 2026-09-16 are kept outside the public repository, `examples/ignored/SAS`):

- **the centre** and its calibration (what moved it and by how much);
- **the corridor** with its sources named — today this comes from the outside view only;
  the chain declares no P10–P90 of its own (`docs/instrument.md` §4);
- **the outside view** with its tail and its class-membership test;
- **what is in no number**: the named holes, the scope forks declared in step 0, the
  team-capability term the table does not carry;
- **the questions that move the answer**, from `open_questions.md`.

Built reports: `tools/report/build_report.py` from `report_data.json`; never overwrite a build.

## What full convergence would mean

Nothing good. The two sides answer structurally different questions; if they land on one point they
have either coincided or lost their independence. The output is a range with a reason, not a number.
