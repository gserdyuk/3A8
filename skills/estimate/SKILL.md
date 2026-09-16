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

## Step 7 — the deliverable: the estimate document and the report (yours, every run)

The run is not finished when the diagnosis returns. It is finished when two artefacts exist in
`examples/<case>/`, written by you from the run records and the sensors' outputs only. Nothing in them
may be a number that is not in a sensor's output, the assembly's output or the diagnosis; every figure
carries the run it came from.

1. **`report_numbers.json`** — every figure of the chart and the tiles, in net task hours, with its
   source run: the raw chain (centre, repeat band, the ρ = 0.5 sd from the assembly), the calibration
   (centre band, corridor, central factor — or `null` if Steps C, B, D did not run), each outside-view
   reading (its declared unit and its quantiles after the conversion the diagnosis applied), the
   no-method family if one was run, the parametric readings if any, the outcome only if it exists and
   has been opened, the engine versions and model, one provenance row per sensor. Schema and an example:
   `tools/report/REPORT_INPUTS.md`.
2. **`report_text.json`** — the prose slots: subject, standfirst, the paragraph under the chart (say
   what each curve's width is and is not — `docs/sensors/README.md`), the divergence rows from Steps
   B–D, the findings, the estimate gaps, the outcome rows if there is one. Same schema file.
3. Build:

   ```bash
   python tools/report/make_report_data.py examples/<case>
   python tools/report/build_report.py examples/<case>/report_data.json
   ```

   The first joins the two files with the case's own `requirements_*.md`, `open_questions.md` and
   `assumptions.md` into `report_data.json`; the second writes `reports/report_<timestamp>.html` and a
   line in `reports/README.md` — fill that line's `_(fill in)_` with one sentence on what this build
   shows. **Never overwrite a build**; a new run is a new file beside the old ones.
4. **`estimate_<case>_<date>.md`** — the document, from `docs/templates/estimate_document.md`: the
   answer in three parts, what the diagnosis established, what is inside the centre, what is in no
   number by name, the decisions and questions that move the answer, provenance. Written knowing
   nothing of the outcome; if an outcome exists, Step 6 comes after this document is fixed, and its
   comparison goes into the run record, not into the document's centre. Worked example:
   `examples/BMS/estimate_BMS_2026-08-22.md`.

Every curve on the chart is a sensor's reading or the assembly's; a curve from a retired engine version
is not one of this instrument's readings and does not go on the chart — it may be a tile and a
paragraph. Two readings of one instrument (two engine versions, two repeats) may be drawn together as
`bottom_up_alt`, dashed, and are never averaged.

## What full convergence would mean

Nothing good. The two sides answer structurally different questions; if they land on one point they
have either coincided or lost their independence. The output is a range with a reason, not a number.
