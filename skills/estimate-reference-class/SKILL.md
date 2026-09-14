---
name: estimate-reference-class
description: "Outside-view reference class forecast for a software project by the isolated Lytin-R sensor: a named class, its base rates with sources, P10 / P50 / P80 / P90 with the scenario behind each, and the static blind-spot list. Sees the project description and the assumption log only. Invoke as /3a8:estimate-reference-class."
author: "Gennadiy Serdyuk <gserdyuk@gmail.com>"
---

# /3a8:estimate-reference-class — the outside view (one sensor)

You are the **orchestrator** (the main session). You prepare two inputs, launch one isolated
sensor, keep its raw output, and write the run record. You never forecast yourself.

## What this gives

A forecast that looks only at the **class of projects** and never at the parts of this one:
the class and its membership test, absolute and relative base rates with their sources,
**P10 / P50 / P80 / P90** with the run of events behind each quantile, and the seven-item static
blind-spot list. Engine **`Lytin-R 1.1`** (`agents/estimator-reference-class.md`).

It is generation-agnostic by construction — it never sees the chain — so it is the same sensor
in the Lytin and Hotyn pipelines, and it is the only part of the instrument that declares a
corridor. Measured repeat spread: P50s ×1.31 apart, narrowing toward the tail.

## Inputs to prepare (yours)

| file | what |
|---|---|
| `case_profile.md` | pinned before any number — in particular the **stage of estimation** (RFP / post-discovery / mid-project), which changes the class's systematic error |
| project description | the RFP digest or system description, stripped of effort, cost, duration, deadline, budget and team size. Record what was struck. |
| `assumptions.md` | the adjudicated readings |

## Launch

- Subagent: **`3a8:estimator-reference-class`**, `tools: Glob` only: **paste** the description and
  the assumption log. Nothing else.
- Must never see: a work breakdown, any bottom-up number, the product or work model, the rate
  table, any target. If the case's bottom-up half has already run, that is the reason this
  sensor runs **in a separate launch with a clean prompt**, not later in the same conversation.
- Choose the model deliberately and record it yourself. n = 2 repeats if the reading will be
  compared with anything.

## Keep and report

1. Raw replies verbatim: `examples/<case>/run<N>_raw/LR<N>-<repeat>.md` + `MANIFEST.md`.
2. Run record `examples/<case>/run<N>_reference_class.md`: engine stamp as printed, model as
   launched, the class and its membership test, the quantiles **with the sensor's declared unit**
   (it declares unit, leave inclusion and whose roles are counted before any figure), the
   sources it named, and the repeat spread per quantile.
3. Do not average the two repeats into one number; the spread is the reading.

## Where it goes next

The forecast is one of the two sides the diagnostician compares. On its own it is a corridor for
the class, not for this project — the blind-spot list says exactly what it cannot see. The
comparison is `/3a8:estimate`.
