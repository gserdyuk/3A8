# 3A8 — TriAngulEight (Triangulate)

A software project estimation methodology for the AI-assisted era. It replaces
independence of *experts* with independence of *techniques*.

## Why

Wideband Delphi works because experts are independent. An LLM has no such
independence: a single model asked several times gives not independent opinions but
well-anchored guesses (rephrasing the question shifts its estimate more than it would
a human's). So the source of diversity is not different "roles" of one model, but
different estimation methods.

## How it works

The same project is estimated with several independent techniques (WBS decomposition
+ PERT, analogy / reference class, throughput Monte Carlo, parametric models). Each
technique's blind spots are **guaranteed by construction**, not random. When they
disagree, the gap is not averaged away but **diagnosed** through each method's known
blind spot — for example, a WBS leaf-sum below the analogy => the charge for the seams
between tasks was left out. We calibrate one method with another. The output is a range
with an explained residual, not a single number.

## In this repository

- `METHODOLOGY.md` — the framework: methods, their blind spots, pipeline, boundaries.
- `findings.md` — working log: *why* the methodology is built the way it is (sources, experiments).
- `examples/` — worked cases: `BMS`, `FaxRxTx` (blind estimation).
- `mars_model/` — hypothesis checks on open datasets (PROMISE); `results.md` + fitting code.
- `pitch_en.md` — a short project pitch.

## State

Early stage. The methodology is worked out on two cases (`n=2`); the empirical part
runs on open data and is reproducible (data + code in the repository). The claims are
deliberately modest: this is a skeleton with checkable results.

## Next

1. Validation on more real projects with known actuals.
2. Agent wrapper: automating the pipeline as **isolated agents, one per method** —
   deliberately not one model in several "roles".
