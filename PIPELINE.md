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

## Engine names and versions

Each agent is an **engine** with a name and a version, stamped on every output it produces:

The naming scheme: **city = generation of the whole pipeline, letter = role within it, number = major.minor version.**

| Step | Agent | Engine |
|---|---|---|
| A.1 | `estimator-decomposition` | **Lytin-D 3.0** |
| A.2 | `estimator-reference-class` | **Lytin-R 1.0** |
| C-params | `calibration-rates` | **Lytin-K 1.0** |
| B, D | `diagnostician` | **Lytin-G 1.0** |
| — | `version-probe` | **Lytin-F 3.0** |

One city for all four engines of a generation makes the pipeline version legible as a whole; the letter says which role is speaking. A role can advance on its own (`Lytin-D 1.1`) while the generation stays; a new city means the set was rebased together.

**F is not a step of the pipeline.** The version probe estimates nothing; it answers with its own stamp and stops. It exists because agent definitions are read **once, at session start**, so an edit made during a session has no effect until restart, and nothing on disk reveals whether that has happened — only running an agent does. Run9 established this the expensive way: ten runs launched after an edit in the same session all returned the pre-edit engine. The probe is that check made cheap enough to do every time.

Its version **mirrors the sensor being measured** rather than counting independently, so the expected answer is known without consulting a log and a mismatch is visible at a glance. The two are bumped in one edit. The probe confirms only that the session reloaded; that a particular file's new content is *correct* remains the job of the engine stamp each sensor prints in its own output. Read the two together — probe before a batch, stamps after it.

**The probe must be edited, never created, for its answer to mean anything.** A newly created file appearing in the session proves only that the harness picks up *new* files; the question that matters is whether it re-reads *modified* ones, since that is what a sensor edit always is. A harness that scanned for new files while caching the content of known ones would pass a freshly created probe and still run the old sensor — which is run9's failure in a subtler form. On the cycle where the probe itself is introduced this hole is unavoidable, and the way to close it is a **bump-only cycle**: raise the version on both files with no other change, restart, and read the probe. From then on every ordinary bump is a modified file and the check is sound.

**Major** changes when a constant can move the level (leaf ceiling, branch list, rate card) — estimates across major versions are not comparable without a measured conversion factor. **Minor** changes when only wording, reporting or output format changes.

Labels for the decomposition sensor, so the numbers already on record can be placed:

| Engine | What it was | Measured |
|---|---|---|
| **Lytin-D 0.1** | the manual July tree, 26 leaves, flat list | 486 pd, n = 1 |
| **Lytin-D 0.9** | the unconstrained August definition | mean 1147, CV 17.4%, n = 10 |
| **Lytin-D 1.0** | C1–C4, the constants below | mean 1284, CV 8.9% (same session); mean 1410, CV 10.0% (other session) |
| **Lytin-D 2.0** | + C5, modules derived from functions | mean 1518, CV 10.8%, n = 10 |
| **Lytin-D 2.1** | + C5's scope: activity branches carry no modules | not measured separately; nine of ten `2.0` runs already behaved this way |
| **Lytin-D 2.3** | + §6 reports node items in three parts and the seam mix by kind | mean 1668, CV 9.85%, n = 10 |
| **Lytin-D 3.0** | C3 replaced: integration is 20% of the leaf sum beneath each node, no seam counting | mean 1674, CV 10.86%, n = 10 |

Read the level column across `1.0` and later with the reporting caveat in mind, not as a trend: the four
comparable batches sit at 1284, 1410, 1518, 1668 and 1674, and only some of that movement is method. What
the versions *did* buy is not visible in the level at all — it is visible in which parameter carries the
spread. C1 closed the price of a leaf (own CV 15.9% → 5.6%), C5 closed the module list and with it the node
count (44.1% → 8.2%), `3.0` closed the cost of integration (share CV 10.4% → 0.78%, 3% of variance). Each
was confirmed by measurement; none narrowed the output, because the variance moved to the next unpinned
parameter every time. **How finely a module is split into leaves is the only one left, and it now carries
essentially all of it.**

`2.2` carried exactly the change now labelled `2.3` and produced no runs at all. It was bumped without any further edit, on purpose: see the note on the probe above. A version with no measurement attached to it is not worth preserving as a separate row — it would be a number a future reader could never place against any data.

A separate configuration, not a version: with the leaf table suppressed, `1.0` gave mean 1715 — **+33.5%** on a change to the output format alone. That is why the version convention has to cover reporting and not only constants, and why a batch under a changed §6 is treated as a new baseline rather than a continuation.

Downstream engines record the stamps of what they consumed: the rate agent records which decomposition engine built the tree it is calibrating, and the diagnostician records all three of its inputs. A diagnosis is reproducible only if the versions of everything it combined are on the record.

## Method constants of the decomposition sensor

Ten identical runs of the sensor (examples/BMS/run6_variance.md) showed ±17% spread between runs and a factor-of-two shift between specifications, with the price attached to a leaf carrying most of it. Three constants were therefore moved from the run's judgement into the method definition (2026-08-05):

- **C1 — splitting rule:** split any item whose *most likely* estimate exceeds **10 person-days**; stop as soon as a piece is at or below it; never merge leaves to reach a size; never create a leaf below 1 person-day. A ceiling and no floor, because the inflation direction is one-way — the unpacking effect grows totals when work is cut finer, so splitting needs a limit and coarseness needs none. The rule is monotone: the tree only refines, the procedure terminates, and the result does not depend on the order of splits. A merge rule would break both properties (a merged leaf invites the next pass to re-split it) and would reintroduce the judgement call "merge with which neighbour". Most leaves land in 5–10 — a sprint-sized task, checkable by a human reader — but that is an expectation reported as a distribution, not a constraint.
- **C2 — mandatory top-level branches:** analysis/design, platform, core domain, external integrations, interfaces, reporting, QA, infrastructure and release, **migration/coexistence/cutover**, documentation. A branch with no work is kept and marked "none, because …". The precedent is the **utility tree** of ATAM (SEI): its second level is a fixed vocabulary of quality attributes while the leaves stay project-specific, precisely so that trees of different projects are comparable and no standard category is dropped in silence. Same two jobs here. The migration branch was added last: branches 1–8 and 10 describe the *product*, and without a slot for the *project* work of moving off a predecessor, that work smears across its neighbours — on FaxRxTx it was ~19% of the estimate and it was what defined the class the other sensor chose.
- **C3 — seam rate card:** plain call 1.5 pd, shared data 3 pd, shared workflow 5 pd; doubled at the top-level assembly node because a seam costs more when the parts joined are larger. Seams are counted, not estimated as a percentage; the 15% fallback is allowed only where seams genuinely cannot be enumerated, and must be declared.
- **C4 — the static blind-spot list is given, not derived.** Both Step A sensors carry a fixed list of what their method cannot see in *any* project, reported verbatim and kept separate from the project-specific list. A constant presented as a finding is noise; a finding buried among constants is worse.

The sensor also reports its own **instrument readings** (leaf count, the distribution of M across buckets, integration share, seam-counted versus fallback nodes) and a **completeness report** (which branches are filled, which are marked "none, because …", and filled ÷ *applicable*), so drift can be detected without re-reading the whole tree.

**Not yet re-measured, and the direction is not the obvious one.** The 17% figure describes the *unconstrained* instrument. An earlier note here predicted that C1 would pull the level *down*, reasoning from a mean price per leaf of ~11 pd against a band midpoint of 7.5. That reasoning was wrong: splitting conserves the sum arithmetically (a 14-day leaf becomes 7 + 7), so capping M lowers the price per leaf and raises the leaf count by the same factor, leaving the total unchanged — and the unpacking effect then pushes finer trees *up*. The honest prediction is therefore: **the level may well rise; the spread should narrow.** Which means the level under the constrained instrument must be measured before any calibration is built on top of it.

## The two checkable disciplines

### 1. Provenance of the calibration parameters

> No parameter used in Step C may be a function of the gap it explains.

Written in prose (findings §11.1, step 3) this rests on good faith: the same session that sees a 48-unit gap can always talk itself into rates that sum to 48. The wrapper makes it structural: the rates are produced by `calibration-rates`, which is never shown the reference class output or the gap, and the `diagnostician` may only apply the supplied rates — never edit, add, or drop one. If the diagnostician finds a blind spot the rates do not cover, it requests another gap-blind round instead of filling the hole itself.

This is checkable by **provenance, not by value**: no inspection of a rate's number can tell you whether it was fitted, but the data flow can.

### 1a. The partition, and the cap on global multipliers

A category may be a mandatory branch of the tree, or a blind spot the rate agent corrects for — **never both, and never neither**. If the work has a branch, correcting for it charges twice; if it has neither, it is priced nowhere. This partition is the pipeline's only mechanical protection against double counting, and the FaxRxTx overshoot was that failure in miniature. It became checkable only once the branch list was fixed (C2), because before that there was nothing to partition against.

The rate agent also receives the **completeness report** and must state how it moved the rates. That report is gap-free — no class output, no target, no gap size — so passing it does not break gap-blindness. It is what turns "this tree looks thorough, charge it less for omissions" from a guess into a measurement, and it strikes directly at the cause of the ×4.2 overshoot.

Finally, **at most two global multipliers.** Global corrections compound; targeted and additive ones do not. Five independently sourced globals once produced ×1.72 with nothing behind it. Everything beyond the two genuinely whole-project effects must be expressed as a targeted multiplier on named leaves or a pure addition.

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

Current state: the definitions declare `tools: Glob` — the least capable tool available, which can list paths but cannot read file contents, so a sensor cannot ingest a sibling's numbers.

**Verified 2026-08-04, and this time by probe rather than by declaration.** A sensor was asked to enumerate its own tools and then to attempt a read of a repository file, with substitute routes forbidden. It reported exactly one tool, `Glob`, and reported the read as impossible at the capability level — there was no call to issue, hence no file-access error to quote. `Read`, `Bash`, `Grep`, `Write` and the rest are absent from its context.

So the isolation now has two independent layers: a sensor **cannot** open a sibling's artifact, and **refuses** contaminated material that reaches it through the prompt. The residual capability is that `Glob` can still reveal file *names*; names carry no estimates, so this is accepted rather than fixed — writing it down so that a future reader knows it was a decision and not an oversight.

One cosmetic inconsistency the probe surfaced: the agent's environment preamble still describes a shell tool that is not in its actual tool set. The tool set governs; the preamble text is stale. Worth knowing before it is mistaken for a leak.

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
