---
name: 3A8 — TriAngulEight
description: "Software estimation factory: a three-sensor bottom-up chain with a pinned rate table, a reference class run blind to it, gap-blind calibration and a diagnosis; divergence explained, not averaged; a range with its residual."
owner: Gennadiy Serdyuk
authors:
  - "Gennadiy Serdyuk <gennadiy_serdyuk@epam.com>"
install_script: "git clone https://github.com/gserdyuk/3A8.git"
install_script_unix: "git clone https://github.com/gserdyuk/3A8.git"
sdlc_phase: Planning & Analysis
support_level: Self-Serve
use_cases:
  - Effort estimation from an RFP or a requirement list
  - Diagnosing divergence between estimation methods
  - Calibration on completed projects with known outcomes
---

# 3A8 — TriAngulEight

A software project estimation methodology for the AI-assisted era. It replaces
independence of *experts* with independence of *techniques*, and takes the
magnitude out of the model altogether: **numbers come from a pinned table, the
model only chooses rows.**

## Why it exists

Wideband Delphi works because experts are independent. A single LLM asked
several times gives well-anchored guesses, not independent opinions. So the
source of diversity is not different "roles" of one model but different
estimation methods that structurally cannot see what the others see.

Measured on the way: a baseline with no method at all gave CV 8.55%, and no
version of the method that let the model pick numbers significantly beat it.
The magnitude has to leave the model, or it is sampled afresh on every run.

## What runs

Four sensors, none of which may see what the others see. Three produce no
effort figures of any kind:

1. **Product model** — a pinned requirement list becomes a structure of the
   thing to be built. No numbers.
2. **Work model** — that structure is crossed with a declared technology,
   producing one work item per (element × mandated activity). No numbers;
   work no declared activity covers is reported as a finding, not invented.
3. **Size classes** — each element is classified by counting named things,
   with the enumeration as its justification. Refuses to run if shown a rate
   or a price.
4. **Rate table join** — a script joins those classes to a gap-blind rate
   table written by a role that has never seen a project total.

In parallel and in ignorance of all of it: the **reference class** sensor,
which looks only at the class of projects. When the two disagree, the gap is
**diagnosed** through each method's known blind spot, and the output is a
range with an explained residual.

## The isolation discipline — read before running anything

The agents in this repository are **not a pick-and-mix set.** Each one is
hired for what it is forbidden to see. Who may see what is defined in
[`PIPELINE.md`](../../PIPELINE.md); the run order, step by step, is in
[`docs/instrument.md`](../../docs/instrument.md). Running an agent outside
that order, or feeding it an artifact the matrix says it may not see, breaks
the method silently: the estimate will still come out, it just stops meaning
anything.

Every agent stamps its engine name and version at the head of its output.
A run is reproducible only if the versions of everything it combined are on
the record.

## How to use

1. The repository is a Claude Code plugin. Install it into any project:
   `/plugin marketplace add gserdyuk/3A8`, then `/plugin install 3a8@3a8`.
   For work inside a clone, start Claude Code with `claude --plugin-dir .`
2. Four entry points, each a skill that carries the orchestrator's run order:
   - `/3a8:estimate-product` — the current instrument, bottom-up half
     (product model → work model → size classes → rate-table join), net person-hours;
   - `/3a8:estimate-reference-class` — the outside view, P10 / P50 / P80 / P90;
   - `/3a8:estimate-wbs` — one-sensor bottom-up WBS + PERT (closed generation, quick reading);
   - `/3a8:estimate` — the whole instrument: both halves in ignorance of each other,
     diagnosis, gap-blind calibration, a range with an explained residual.
3. Pin the case profile **before** any estimate exists
   (see [`docs/exit_criterion.md`](../../docs/exit_criterion.md) and
   [`docs/case_profile.md`](../../docs/case_profile.md)).
4. Raw sensor output is transcribed verbatim under `examples/<case>/run*_raw/`;
   the report is built by `tools/report/build_report.py`.

Worked cases in `examples/`: **FaxRxTx** (real project, outcome sealed before
the estimate, ×1.21 against actual), **BMS** (training RFP, issuer anonymised, full deliverable
format). A third case, SAS, is kept outside the public repository because its source document is not ours to publish.

## Standing and limits

Definition of done is pinned in advance: over at least four cases with
documented outcomes, none used for fitting, the calibrated P50 lands within
×1.3 of actual on at least three. Today: 1 of ≥4 cases, 1 of 1 passing on the
centre. The chain declares no P10–P90 yet; the corridor test is the one
structural gap left.

Current state of every claim, including which documents are stale:
[`docs/status_2026-08-25.md`](../../docs/status_2026-08-25.md).

## Further reading

- [`METHODOLOGY.md`](../../METHODOLOGY.md) — the frame: methods, blind spots, boundaries.
- [`PIPELINE.md`](../../PIPELINE.md) — the visibility matrix.
- [`findings.md`](../../findings.md) — the working log: *why* it is built this way.
- [`README.md`](../../README.md) — repository map.

License: Apache 2.0. Canonical repository: https://github.com/gserdyuk/3A8.
