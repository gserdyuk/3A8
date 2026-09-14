---
name: estimate-product
description: "The current 3A8 instrument, bottom-up half: product model, work model, size classes by three isolated Hotyn sensors, then a script joins classes to the pinned rate table. Numbers come from the table, the model only chooses rows. Output in net person-hours with named holes. Invoke as /3a8:estimate-product."
author: "Gennadiy Serdyuk <gserdyuk@gmail.com>"
---

# /3a8:estimate-product — WBS through a product model (Hotyn chain, steps 0–4)

You are the **orchestrator** (the main session). You pin the inputs, launch three isolated sensors
in order, write the assembly script, and keep every raw reply. You never size or price anything
yourself, and you never let a sensor see what the matrix forbids.

`docs/instrument.md` §3 says what each step does; `PIPELINE.md` says who may see what. This skill
is the run order. Read both before the first case.

## What this gives

The total in **net person-hours** (working time, presence excluded — `docs/instrument.md` §0), the
layer breakdown, and the list of **named holes** the chain could not size. Deterministic in its last
step: the same classes and the same table give the same number. Measured repeat spread of the
whole chain: ×1.03 on the total from sizing; the product model is the least stable step
(structure size ×1.02–×1.56 depending on the source's density).

## Step 0 — pin, split, declare (yours)

In `examples/<case>/`, in this order (`docs/case_profile.md`):

| file | what |
|---|---|
| `case_profile.md` | team grade and domain experience, site, presence fraction, process, whether an outcome exists. **Before any number.** |
| `requirements_pinned.md`, `requirements.pin.txt` | the obligation list with stable ids, md5-pinned |
| `requirements_split.md` → `requirements_product.md` + `requirements_work.md` | **product obligations** (what the thing must be) vs **demanded work** (migration, parallel run, decommissioning) |
| `assumptions.md`, `assumptions_product.md`, `open_questions.md` | adjudicated readings; the product projection is what the model builder sees |
| `technology_declaration.md` | one entry per dimension of `docs/technology_catalogue.md`, the activities each mandates, parameters (environments, cycles), and every **scope decision** as a named fork |

Scan the source for effort, cost, duration, deadline, budget, team size; strike it and record what
was struck. Worked example of a complete Step 0: `examples/SAS/README.md`.

## Steps 1–3 — three sensors, each blind to the others

All three have `tools: Glob` only and must not read files: **paste** their inputs. Choose the model
deliberately and record it yourself. Launch **n = 2 repeats** per step; the spread is part of the
result. Large models are crossed and sized in batches by parent (SAS: seven batches).

| step | subagent | paste in | must never see |
|---|---|---|---|
| 1 product model | `3a8:model-builder` (`Hotyn-M`) | `requirements_product.md`, the declared processing order, `assumptions_product.md` | any estimate, any prior tree, budget / deadline / team size |
| 2 work model | `3a8:work-crosser` (`Hotyn-W`) | the **closed** product model from step 1, `technology_declaration.md` with parameters, `requirements_work.md` | any estimate, any prior work model, any cost anchor |
| 3 size classes | `3a8:work-estimator` (`Hotyn-D`) | the work model: each element with class, parent, covered obligations **with their texts**, its items; plus the sizing rules — `docs/technology_catalogue.md` §3a verbatim | **any rate, price, person-day, budget, duration or prior estimate** |

Between steps, close the artefact: every obligation placed or reported unplaced (step 1); every
refusal labelled *filter* or *judgement* (step 2); every unsizeable element a **named hole**
(step 3). A sensor that reports contamination has done its job — fix the prompt, relaunch.

Prompt generators from the last case are reusable patterns: `examples/SAS/run47_raw/make_sizing_prompts.py`.

## Step 4 — the arithmetic (a script, no model)

Join classes to `docs/rate_table.md`: `E = (O + 4M + P) / 6` per cell; integration **C3 = 20% of the
rooted subtree's leaf effort at every parent, never compounding**; once-scoped, per-environment
and demanded items enter no C3 base.

There is no generic joiner yet: write `examples/<case>/run<N>_raw/assemble_<case>.py` following
`examples/SAS/run47_raw/assemble_sas.py` (reads the rate table from `docs/rate_table.md`; prices
each repeat as a variant; prints total, layers, holes, repeat ratio). Run it:

```bash
python examples/<case>/run<N>_raw/assemble_<case>.py
```

## Keep and report

- Raw replies verbatim: `run<N>_raw/HM<N>-<batch><repeat>.md`, `HW…`, `HD…`, plus `MANIFEST.md`
  (prompts, model, batches, what was struck).
- One run record per step: `run<N>_product_model_measurement.md`, `run<N>_work_model.md`,
  `run<N>_sizing_and_assembly.md` — engine stamp as printed, model as launched, counts, Jaccard
  between repeats, holes.
- The number is **net person-hours**. Days of presence only in the comparison layer, by
  `docs/constants.md` §4a.

## What this half does not give

No corridor (no P10–P90), no team-capability term, no brake on over-counting
(`docs/instrument.md` §4). The outside view and the diagnosis are `/3a8:estimate-reference-class`
and `/3a8:estimate`.
