# 3A8 — TriAngulEight (Triangulate)

A software project estimation methodology for the AI-assisted era. It replaces
independence of *experts* with independence of *techniques* — and, in its current
generation, takes the magnitude out of the model altogether: **numbers come from a
pinned table, and the model only chooses rows.**

## Why

Wideband Delphi works because experts are independent. An LLM has no such
independence: a single model asked several times gives not independent opinions but
well-anchored guesses (rephrasing the question shifts its estimate more than it would
a human's). So the source of diversity is not different "roles" of one model, but
different estimation methods.

Six weeks of measurement then produced a second, sharper finding. Rules that constrain the
*form* of an estimate bind exactly what they name — and the magnitude relocates into whatever
variable was left free. Pin the size of a task and the count of tasks moves; pin the count and
the price per task moves. The floor was measured directly: **a baseline with no method at all
gave CV 8.55%, and no version of the method significantly beat it.** The magnitude has to leave
the model, or it is sampled afresh on every run.

## How it works

**Four sensors, none of which may see what the others see.** Three of them produce no
effort figures of any kind:

1. **Product model** — a pinned requirement list becomes a structure of the thing to be built.
   No numbers.
2. **Work model** — that structure is crossed with a *declared* technology, producing one work
   item per (element × mandated activity). No numbers, and no activity may be invented: work
   the product needs but no declared activity covers is reported as a **finding**.
3. **Size classes** — each element is classified by counting named things, with the enumeration
   as its justification. Still no numbers: it must refuse to run if shown a rate or a price.
4. **A script** joins those classes to a **gap-blind rate table** — external norms, written by a
   role that has never seen a project total or a gap a rate would explain.

Running in parallel and in ignorance of all of it: the **reference class** sensor, which looks
only at the class of projects and never at the parts of this one. When the two disagree, the gap
is not averaged away but **diagnosed** through each method's structurally known blind spot, and
the output is a range with an explained residual.

Full procedure: [`docs/instrument.md`](docs/instrument.md). Who may see what, and how the
isolation is enforced: [`PIPELINE.md`](PIPELINE.md).

## Standing

**1 of ≥ 4 cases · 1 of 1 passing on the centre.**

The definition of done is pinned in advance ([`docs/exit_criterion.md`](docs/exit_criterion.md)):
over at least four cases with documented outcomes, none used for fitting, the calibrated P50 lands
within ×1.3 of actual on at least three, and the declared P10–P90 covers actual on at least three.

- **FaxRxTx** (real project, 2007–2009): estimated end to end with the outcome sealed, then
  compared. **99.4 against 120 staffed person-months — ×1.21, inside the gate**, both classification
  repeats inside, nothing fitted on the case. It gets there *despite* a known ×8.5 under-pricing of
  one stage.
- **BMS** (training RFP, no outcome): the only place the full deliverable format has been produced —
  a centre with its calibration, a corridor with its sources named, the outside view with its tail,
  the scope that is in no number, and the questions that move the answer.
- **Not yet scoreable:** the corridor test. The chain declares no P10–P90, and that is the one
  structural gap left in it.

Case 1 was admitted on conventions supplied after the estimate existed, so it sets the **floor,
not the standard**: for cases 2–4 the case profile is pinned before any estimate exists.

Current state of every claim, including which documents are stale and how:
[`docs/status_2026-08-25.md`](docs/status_2026-08-25.md).

## In this repository

- [`METHODOLOGY.md`](METHODOLOGY.md) — the frame: methods, their blind spots, the pipeline, boundaries. Unchanged.
- [`docs/instrument.md`](docs/instrument.md) — the current chain, step by step, with what is pinned where.
- [`PIPELINE.md`](PIPELINE.md) — the visibility matrix and the disciplines that are machine-checkable.
- [`docs/status_2026-08-25.md`](docs/status_2026-08-25.md) — what may be claimed today, and what may not.
- [`docs/exit_criterion.md`](docs/exit_criterion.md) — when the instrument is fit for use.
- [`docs/rate_table.md`](docs/rate_table.md) · [`docs/technology_catalogue.md`](docs/technology_catalogue.md) — the pinned constants and the declaration vocabulary.
- [`findings.md`](findings.md) — the working log: *why* the methodology is built the way it is.
- `docs/sensors/` — one note per curve on the panel: how each sensor was conceived, what its width means, what was measured, what we want to change. Expected to disagree with the code; that is what they record.
- [`BACKLOG.md`](BACKLOG.md) — open work, cheapest first. `sessions/` — one record per working session.
- `examples/` — worked cases: `BMS`, `FaxRxTx`. Raw sensor output is transcribed verbatim under `run*_raw/`.
- `mars_model/` — hypothesis checks on open datasets (PROMISE); results and fitting code.

## Working method

Four rules, adopted after a spiral they explain: **one question per run**, written before launch;
**by-products are parked, not promoted** — an incidental observation may not change a conclusion in
the turn it appeared; **no document without the author's word**, raw transcripts excepted; and
**"nothing came of it" is a legitimate result.** Treating every run as owing a finding is what
manufactures the spiral.

Two more, learned the expensive way: **an outcome is an input, and inputs are pinned and
interrogated** — the largest single error in the project's only outcome comparison was in the
*fact's* unit. And **the unit of a comparison is part of the comparison, on both sides.**

## Next

1. Adjudicate what is already written down — the named holes and the declared scope forks.
2. A corridor instrument, so the second of the three tests becomes scoreable at all.
3. A second documented outcome, with its case profile collected **first**.

## Entry points

Four things you can invoke; everything else in `agents/` is an internal sensor that runs only
inside one of these, blind to the others.

| invoke | what it does | engine(s) | gives |
|---|---|---|---|
| `/3a8:estimate-product` | **the current instrument, bottom-up half** — product model → work model → size classes, then a script joins classes to the pinned rate table | `Hotyn-M`, `Hotyn-W`, `Hotyn-D` + script | net person-hours, layers, named holes |
| `/3a8:estimate-reference-class` | **the outside view** — the class of projects, never the parts of this one | `Lytin-R` | P10 / P50 / P80 / P90, blind-spot list |
| `/3a8:estimate-wbs` | **one-sensor bottom-up WBS + PERT** — the closed `Lytin` generation, kept for quick readings and comparison; the magnitude is sampled by the model | `Lytin-D` | WBS with O/M/P, PERT total |
| `/3a8:estimate` | **the whole instrument** — the two halves above in ignorance of each other, then diagnosis, gap-blind calibration, a range with an explained residual | + `Lytin-K`, `Lytin-G` | centre, corridor, residual, what is in no number |

Each entry is a skill in `skills/`: the orchestrator's run order, what to paste into which sensor,
what the sensor must never see, and where the raw output goes. The sensors read no files; the
orchestrator pastes, records the model, and keeps the record.

## Install as a Claude Code plugin

The repository is a Claude Code plugin: the sensor definitions live in
`agents/` and register as `3a8:<name>`.

```text
/plugin marketplace add gserdyuk/3A8
/plugin install 3a8@3a8
```

Working inside a clone: `claude --plugin-dir .` Inventory check:
`claude --plugin-dir . plugin details 3a8`. Current release: **0.2.0** (tag `v0.2.0`, 2026-09-16 — the first
that passed its regression, runs 52–60); engines `Hotyn-M 2.1` / `Hotyn-W 1.2` / `Hotyn-D 2.0`, `Lytin-R 1.1`,
`Lytin-K 1.1`, `Lytin-G 1.1`. **Launch the orchestrating process with `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`**:
the product-model sensor needs 65 000–95 000 output tokens on a 150-obligation list, and the default cap of
64 000 cuts its turn and injects a continuation message that no prompt contains (runs 53–56). The agents are not a pick-and-mix
set — who may see what is in [`PIPELINE.md`](PIPELINE.md), the run order in
[`docs/instrument.md`](docs/instrument.md).

## Maintainer

Gennadiy Serdyuk <gserdyuk@gmail.com> (at EPAM: gennadiy_serdyuk@epam.com)
