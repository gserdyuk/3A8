# The agent wrapper — who is allowed to see what

The methodology (METHODOLOGY.md) says the methods must be independent sensors. In practice, running two methods in one conversation does not produce two sensors: the second run is anchored by the first (findings §1, §9). This file specifies the pipeline as a set of **isolated agents with disjoint inputs**, and states which disciplines are enforced by machinery rather than by good faith.

The agents are hired for what they are **forbidden to see**, not for autonomy or throughput. Their definitions live in `.claude/agents/`.

## The visibility matrix

| Step | Agent | Sees | Must never see |
|---|---|---|---|
| A.1 | `estimator-decomposition` | project description, assumption log | any other method's numbers, any target/budget/deadline |
| A.2 | `estimator-reference-class` | project description, assumption log | the WBS, any bottom-up number, any target/budget/deadline |
| C-params | `calibration-rates` | project description, assumption log, the WBS (run 1) | the reference class result, the size of the gap, any target |
| B, D | `diagnostician` | everything above | the project's **actual outcome** |
| D-reveal | the orchestrator (main session) | everything, including the actual outcome | — (writes the comparison only after the diagnosis is fixed) |

The orchestrator assembles the inputs and is the only participant that touches files. Anything the orchestrator pastes into a prompt becomes part of that agent's world, so the matrix is a statement about **prompt contents**, not only about file permissions.

## The two checkable disciplines

### 1. Provenance of the calibration parameters

> No parameter used in Step C may be a function of the gap it explains.

Written in prose (findings §11.1, step 3) this rests on good faith: the same session that sees a 48-unit gap can always talk itself into rates that sum to 48. The wrapper makes it structural: the rates are produced by `calibration-rates`, which is never shown the reference class output or the gap, and the `diagnostician` may only apply the supplied rates — never edit, add, or drop one. If the diagnostician finds a blind spot the rates do not cover, it requests another gap-blind round instead of filling the hole itself.

This is checkable by **provenance, not by value**: no inspection of a rate's number can tell you whether it was fitted, but the data flow can.

### 2. The tail is not calibrated

Tail events do not exist as items in a bottom-up structure, so no multiplier on a WBS reaches them (reproduced in both worked examples). The final answer is therefore reported in three separate parts, and only the first two come from calibration:

- **center** — from the calibrated bottom-up estimate,
- **corridor** — from the spread of the calibration,
- **reserve** — from the raw reference class tail, uncalibrated.

## Contamination refusal

Every agent begins by checking its own input and **aborts with a contamination report** if it finds something the matrix forbids. This is the layer that can actually fire during a run, so it is the layer worth testing: a check that has never gone red is not yet a check (findings §12). Testing it means deliberately feeding a forbidden input — a target number to an estimator, a class quantile to the rate agent, an actual outcome to the diagnostician — and confirming the refusal.

Status of that test (2026-08-04):

- `estimator-decomposition` — **fired correctly, twice**: once with the role text pasted into a general agent, once as the registered agent itself. In both cases the prompt carried four separate anchors (a budget, a class median, an explicit "land close to that", and an instruction to open another method's run file). The agent refused to estimate, named all four anchors, did not open the file (zero tool calls), listed which parts of the input were still clean, and observed that an anchored run is dangerous precisely because downstream it is indistinguishable from a clean one. So the refusal holds on prompt text alone.
- `estimator-reference-class`, `calibration-rates`, `diagnostician` — **all three fired correctly**, and against the harder form of the test: the forbidden material was embedded as neutral "context" with no instruction to converge on it, so the agent had to notice the contamination itself rather than decline an order. The reference class agent was handed a WBS total and its three heaviest items; the rate agent was handed the class quantiles; the diagnostician was handed the project's actual outcome. Each stopped before producing anything.
- Three observations from those runs are worth keeping:
  - **Contamination is sticky.** Two of the three noted independently that a corrected follow-up message does not repair the run: the number stays in the context window, so the fix is a fresh instance, not a fresh prompt.
  - **Partial output is refused too.** The reference class agent declined even to give the "safe" part (the class definition), on the grounds that its structural reasoning was already downstream of the WBS it had seen.
  - **Even the fact of a prior run leaks.** The rate agent observed that "the other sensor has already run" is borderline on its own, and fatal together with numbers — the gap was one subtraction away inside its context.
- **Bonus: the sensors caught a defect in the test input.** Two agents independently flagged that the WBS handed to them contained items (a hotel-aggregator integration, a search engine) that the project description did not mention — about 14% of the total priced against undescribed scope. The test prompt was indeed sloppily assembled, but the lesson generalises: a sensor that is given both a description and a WBS doubles as a consistency check between them, and that check costs nothing extra.

### An observed failure mode: fabricated tool output

On its first contamination test the diagnostician reached the right verdict but its report contained a block formatted as a directory listing of the project root — including files that do not exist and one entry appearing as both a file and a directory. The harness recorded **zero tool calls** for that run: nothing was executed; the listing was invented and presented as observation. A repeat of the same test produced a clean refusal with no fabricated block, but the repeat also carried an explicit "do not open any files" instruction, so the two runs differ in more than luck and the failure cannot be called a one-off.

Consequence: **treat any file-system or repository claim inside an agent's report as unverified narration unless the tool call is visible.** This is also the strongest practical argument for making the tool restriction real rather than declared — an agent that cannot reach the file system has nothing to fabricate about it.

### The enforcement that turned out not to exist

The first version of these definitions carried `tools: []`, intended as "this agent structurally cannot open a sibling's artifacts". On registration the harness reported all four agents as having **all tools**: the empty list was silently treated as "unspecified", i.e. inherit everything. The definition read like enforcement and enforced nothing — a config-shaped placebo. It was found only because the negative test was run against the registered agent rather than against the text of the definition.

This is the same lesson as F8 in findings §12, in a new place: **a restriction that has never been observed to bind is not a restriction.** Anything in this pipeline described as machine-enforced must be demonstrated firing, not merely written down.

Current state: the definitions declare `tools: Glob` — the least capable tool available, which can list paths but cannot read file contents, so a sensor still cannot ingest a sibling's numbers. Whether the field binds at all is **unverified**, because agent definitions load at session start; check the registration line on the next fresh session, and if it does not read "Tools: Glob", the tool layer must be treated as absent and isolation rests entirely on prompt-layer refusal plus orchestrator discipline.

## Running the pipeline

Prompts are currently assembled by hand, which is the weakest link: every contamination test in this file describes a leak that a careless copy-paste would produce for real. The next hardening step is to assemble each agent's prompt from a fixed template with a whitelisted set of fields, so that a forbidden field cannot be pasted in rather than merely being refused after the fact. Until that exists, the refusal layer is the only thing standing between a sloppy prompt and a laundered estimate.

1. Prepare the case directory: the project description and `assumptions.md`. If a known actual exists, seal it in `FACT.md` and do not paste it into any agent prompt until Step D is written.
2. Run A.1 and A.2 — separate agent calls, each given only the description and the assumption log. They may run in parallel; they must not run in one context.
3. Run `calibration-rates` with the description, the assumption log and run 1. Check the prompt for class numbers before sending it.
4. Run `diagnostician` with runs 1 and 2 plus the rate table.
5. The orchestrator writes Step D artifacts, and only then opens `FACT.md` for the comparison.

## Deliberately not automated

- **The assumption log** stays a human decision: it is where the tacit knowledge of the team enters, and that is the one kind of uncertainty no method covers (METHODOLOGY §4).
- **Class membership** stays a judgement call reported by the reference class agent, not a computed lookup — until there is enough own history to stratify (findings §11.4).
- **No fitting anywhere in the pipeline.** The moment a step tunes parameters on history, it stops being a coarse independent sensor and becomes a model with hidden assumptions (findings §11.5).
