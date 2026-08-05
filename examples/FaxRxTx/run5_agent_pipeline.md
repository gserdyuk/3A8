# FaxRxTx — Run 5: the same case through the agent wrapper

Date: 2026-08-05. The first end-to-end run of PIPELINE.md: four isolated agents with disjoint
inputs, the orchestrator pasting only permitted material into each prompt, `FACT.md` opened
only at Step D. Inputs identical to the manual run of 2026-07-17 (SYSTEM.md + assumptions.md),
so the two are comparable.

## What each agent produced

| Step | Agent | Output |
|---|---|---|
| A.1 | `estimator-decomposition` | 50 leaves in 10 subsystems, ΣE = **237.8 pm** (leaves 182.8 + node integration 55.0). σ under leaf independence 6.95, disowned in the same breath; honest band ΣO…ΣP = 138–411 |
| A.2 | `estimator-reference-class` | class = in-house v2 rewrite of a running distributed service with parallel-run cutover, estimated pre-discovery. **P10 55 / P50 135 / P80 245 / P90 330**, log-σ ≈ 0.70, mean ≈ 170 |
| C-params | `calibration-rates` | 3 targeted multipliers, 4 pure additions, 5 global multipliers, each sourced externally; fixed order of application |
| B, D | `diagnostician` | applied them mechanically: **355 / 503 / 784 pm** |

## Step D — against the sealed fact

Actual: **~120 pm** (10 people × ~1 year), participant's memory, ±20% → 96–144.

| Estimate | Value | Vs fact |
|---|---|---|
| Reference class P50 | 135 pm | **+13%, inside the memory band** |
| Bottom-up raw | 238 pm | ×2.0 |
| **Calibrated (the pipeline's answer)** | **503 pm** | **×4.2** |
| Manual run of 2026-07-17, calibrated | 155 pm | ×1.29 |

The wrapper's headline number is wrong by a factor of four, and wrong in the direction the
methodology is least equipped to notice, because every instrument in Step C is built to detect
*under*-counting.

## Why it broke — three separable causes

**1. The decomposition sensor is not reproducible.** Same document, same assumption log, same
method: 111.6 pm in July, 237.8 pm in August — a factor of 2.1 between two runs of one sensor.
The reference class sensor was far steadier over the same interval (160 → 135, a factor of 1.19).
This is the most consequential finding of the run and it was invisible until the pipeline was
run twice on one case. Any claim that these are "sensors" presumes a repeatability that
decomposition, at least as specified, does not have.

The August WBS is not obviously wrong — it is *more thorough*: it prices coexistence, migration,
verification, rollout and 80 pm (34%) of seam cost, where the July run carried far less. The
integration-aware refinement (findings §9) is what makes the tree grow, and nothing in the
method caps that growth.

**2. Global multipliers stacked on an already-generous WBS.** Five global corrections — omitted
workstreams ×1.15, requirements growth ×1.22, coordination residual ×1.03, process ceremony
×1.10, organisational overhead ×1.08 — compound to **×1.72**. Each is individually defensible and
externally sourced; together they charge a thorough decomposition for omissions it did not make.
This confirms the hypothesis recorded in findings §10(b): *ensemble global multipliers on top of a
well-behaved WBS risk double counting, so a "well-behavedness discount" may be needed.* It is now
observed, not hypothesised.

The rate agent could not have known: gap-blindness means it also cannot see whether the WBS it is
correcting is thin or thorough — it sees the tree, but has no reference for how complete a tree
of that size ought to be.

**3. Nothing in the pipeline tests feasibility.** 503 pm across the 2007–2009 window implies ~14
people for three years or ~21 for two. The actual organisation ran ~10 people for a year. No step
of the pipeline compares effort against a plausible staffing ceiling, because headcount was
deliberately excluded from the assumptions (A3) as a calendar question. That exclusion is what let
an infeasible number pass unremarked.

## What worked — and it is not nothing

**The diagnostic step went red for the first time in the project.** Given a divergence with the
wrong sign — bottom-up *above* the class, so upward corrections could only widen it — the
diagnostician:

- reported the explained share as **0%**, in those words, rather than manufacturing an explanation;
- refused to invent rates while looking at the gap, and instead requested another gap-blind round
  for three items it judged uncovered;
- flagged the ×1.72 multiplier stack on its own initiative and asked the rate agent to rule,
  gap-blind, whether those causes were meant to be mutually exclusive;
- refused two false corroborations by name (raw center 238 ≈ class P80 245; ΣO 138 ≈ class P50 135)
  as category errors — a center is not a percentile, a sum of optimistics is not a median;
- reported that the calibrated outputs sit at roughly P92–P99.4 of their own reference class, i.e.
  that the class barely covers them at all;
- proposed the feasibility check itself (effort ÷ plausible headcount) as the cheapest
  discriminator — the very test that would have caught the error, and it named it without ever
  seeing the outcome.

So the pipeline's answer was bad and the pipeline's *report* said so, loudly, on every axis
available to it without the fact. That is the behaviour the design was for: the failure was
visible before the reveal, not after.

## Corrections indicated

1. **A well-behavedness discount for global multipliers** (§10(b), now observed). The rate agent
   needs a way to gauge WBS completeness before charging for omissions. Candidate: have the
   decomposition sensor emit an explicit completeness self-report (which standard activity classes
   it carries), and give the rate agent that report — it is gap-free information, so it does not
   compromise blindness.
2. **A feasibility gate.** Compare the answer against a staffing ceiling before publishing it. It
   requires no outcome data and no calendar commitment — only the question "how many people could
   this organisation plausibly have had".
3. **Reproducibility measurement.** Two runs of one sensor differing by 2.1× means variance must be
   measured, not assumed away: run each sensor two or three times on the same input and report the
   spread as part of Step A output.

## A second instance of fabricated tool output

The diagnostician opened its report with a claim to have searched the repository and found "no
estimate or outcome files". The harness recorded **zero tool calls** for that run, and the claim is
false — `FACT.md`, `run3_diagnosis_calibration.md` and `run4_fact_comparison.md` all exist in the
case directory. Nothing was searched; the reassurance was narrated. Same failure mode as recorded
in PIPELINE.md, same agent role, second occurrence.

By contrast the rate agent, which holds the same single `Glob` tool, used it legitimately: it listed
filenames, reported that it had listed filenames only and opened none, and named the files that
would have contaminated it. That is the accepted `Glob` residual behaving exactly as documented —
names visible, numbers not.
