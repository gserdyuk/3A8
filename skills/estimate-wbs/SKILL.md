---
name: estimate-wbs
description: "Bottom-up WBS + PERT estimate of a software project from its description, by the single Lytin-D sensor. Use for a quick one-sensor reading, or to reproduce the closed Lytin generation for comparison. Not the current instrument: the magnitude is sampled by the model. Invoke as /3a8:estimate-wbs."
author: "Gennadiy Serdyuk <gserdyuk@gmail.com>"
---

# /3a8:estimate-wbs — bottom-up WBS + PERT (one sensor)

You are the **orchestrator** (the main session). You prepare the inputs, launch one isolated
sensor, keep its raw output, and write the run record. You never estimate yourself.

## What this gives

A work breakdown structure with O / M / P per leaf, PERT expectation, integration priced at 20%
of each node's leaf sum, and the split-consistency check — one reading of engine **`Lytin-D 5.0`**
(`agents/estimator-decomposition.md`).

**What it is not.** This is the closed `Lytin` generation: the sensor both structures the work
*and* chooses the numbers. Repeat spread of that design is CV 9–11% on one model and **×2.02
between models** on the same prompt (`PIPELINE.md`, "The model is the second coordinate"). The
current instrument (`/3a8:estimate-product`) takes the magnitude out of the model. Use this
sensor when you want a fast single reading, or a Lytin-comparable number for a case that already
has one.

## Inputs to prepare (Step 0 — yours, not the sensor's)

Follow the pinning order of `docs/case_profile.md`; the layout is `examples/<case>/`:

| file | what |
|---|---|
| `case_profile.md` | conditions the work is done under — team grade, site, presence fraction, whether an outcome is known. **Pinned before any number exists.** |
| `requirements_pinned.md` + `requirements.pin.txt` | the obligation list with stable ids and its md5. Never reshaped afterwards. |
| `assumptions.md` | every open reading of the documents, adjudicated once. |
| the **projection axis** (C2) | one declared axis the tree is decomposed along — a sentence, recorded in the run record. |

Before pinning, scan the source for anything a sensor may not see — effort, cost, duration,
deadline, budget, team size, "projects like this cost X" — and strike it. Record what was struck.

## Launch

- Subagent: **`3a8:estimator-decomposition`**. It has `tools: Glob` only and must not read files:
  **paste** the requirement list, the assumption log and the axis into the prompt. Nothing else.
- Must never see: any other method's numbers, any target, budget or deadline, any prior tree.
- Choose the model deliberately and **record it yourself** — the sensor's own claim about its model
  is a belief, not a fact. The reading is a property of (project × engine × model × axis).
- Repeats: the sensor's spread is the measurement. n = 2 minimum if the number will be compared
  with anything.

## Keep and report

1. Save each raw reply verbatim under `examples/<case>/run<N>_raw/LD<N>-<repeat>.md`; a
   `MANIFEST.md` lists prompts, model, and what was struck.
2. Write `examples/<case>/run<N>_decomposition.md`: engine stamp as the sensor printed it, model
   as you launched it, total and leaf distribution, the assumption-log exceptions the sensor named,
   the repeat spread.
3. Report **in the sensor's declared unit** (person-days, presence excluded); convert only in the
   comparison layer by `docs/constants.md` §4a.

## Isolation, restated

The value of the reading is what the sensor could not see. If the prompt carried an anchor, the run
is not a reading: discard it, fix the prompt, relaunch. See `PIPELINE.md`, Lytin matrix, row A.1.
