# Projection axes — decomposing the same system twice and comparing

Status: **implemented as `Lytin-D 5.0`, not yet run.** Predictions below were registered before the
implementation and are committed in an earlier commit than any result.

Pinned inputs, md5 of the LF form as run13 records them:

| file | md5 |
|---|---|
| `examples/BMS/prompt_decomposition_BMS.txt` (unchanged base) | `c33affd709792dfe60531daa3cb42d65` |
| `examples/BMS/prompt_decomposition_BMS_axisS.txt` | `196524bee339e2da35a293652ca9b00f` |
| `examples/BMS/prompt_decomposition_BMS_axisP.txt` | `5de455cf8c165be500dc17bf2a09dac3` |

Each axis file is the base prompt plus one declaration line and nothing else.

**Original status line:** design only. Not implemented, not run. Predictions registered at the end, before any measurement,
per the pattern that made C6's result readable.

## The idea

The work of building a system is a fixed quantity. Any complete, non-overlapping decomposition of it is a
partition of the same thing, so **different cuts of the same system must sum to the same total**. Cut by
subsystem, cut by process, cut by counterparty — the pie is one pie.

From which follows a property this project has never had:

> **A disagreement between projections proves an error without requiring knowledge of the truth.**

Everything measured so far is *spread*: one method, repeated, dispersion recorded. That is precision and
nothing else. Agreement between projections is a different class of evidence — if two correct cuts of one
object do not reconcile, at least one is wrong, and that is known **without an outcome**.

This matters practically because validity is blocked: BMS has no `FACT.md` and FaxRxTx is n=1. Axis
invariance does not say whether the instrument is right. It says whether it is **coherent**, and incoherence
is a demonstrated error.

## Why this is not another patch

It is METHODOLOGY §1–2 applied one level down. That section's founding move is decorrelation through
**structurally different blind spots** rather than through different experts. Axes have structurally
different blind spots by construction: a cut by process naturally surfaces state transitions and is blind to
screens; a cut by surface does the reverse.

The mechanism is derived from the principle already written, not appended beside it.

## What is removed, and what that costs

**C2 — the fixed list of ten top-level branches — is removed for this experiment.** It cannot stay: it is
itself an axis, and a mixed one. Its ten branches sit on three different cuts at once — product (2–6),
lifecycle activity (1, 7, 8, 10), and project transition (9). No clean projection is possible underneath a
list that already commits to three.

Removing it is deliberate and it is not free. Two things go:

- **The completeness report loses its meaning.** "9 of 9 filled" requires a fixed list to be filled.
- **With it goes the ability to see an omission.** The 10–0 disagreement on migration between the two models
  was visible *only because the slot existed*. Without slots, a run that omits migration simply does not
  write it, and nothing shows.

The second loss is the serious one, and it is replaced rather than accepted.

### The replacement: ask afterwards instead of prescribing beforehand

After the tree is built, each run is asked where four kinds of work ended up: **testing, transition off the
predecessor process, documentation, environments and release.** Not "you must have a branch for these" —
only "where in your tree does this live". **"Nowhere" is a permitted answer and is itself a finding.**

This keeps the diagnostic while imposing no structure, and it recovers something C2 could never see: the
difference between *"QA is in branch 7"* and *"QA is inside every feature leaf"*. Under C2 those two were
indistinguishable, and the suspected double count between phase packages and in-sprint QA lived exactly in
that blind spot.

## What stays

C1 (ceiling, never merge), C3 (integration at 20% per node), C5 (modules from functions), C6 (split check).
One constant is replaced, four are untouched. This is a new instrument but not a rewrite.

## The axis is a coordinate, not a version

The same move already made for the model in run16. The engine is `Lytin-D 5.0` — major, because removing C2
can move the level. The **axis is declared in the prompt as an input**, so one definition serves both axes
and the agent definition does not fork.

A batch is therefore stamped **(project × engine × model × axis)**, and the pinned RFP text and assumption
log are unchanged from run6…run16 — only a single declared axis line is appended.

**The two axes:**

- **S — subsystem / surface.** Decompose the product by the parts that are built and delivered.
- **P — process / booking lifecycle.** Decompose the product by the stages a booking passes through.

Chosen because they are maximally unlike each other. If these two reconcile, the reconciliation means
something.

## Design

| | |
|---|---|
| batches | 2 axes × 2 models × n = 5 = **20 runs** |
| invariant under test | **Σ leaf E** converges across axes |
| C3 diagnostic | if leaves converge and totals do not, C3 is measuring the cut rather than the project |
| main question | **is the axis effect smaller than the model effect (×2.021)?** |
| by-product | is the first level stable within an axis — the open question about whether each axis carries its own natural top level |
| control | leaf-set overlap between axes. Above 90% the axes are not distinct and the experiment did not happen |

Comparison across two differently-shaped trees needs a common substrate, and it is the requirement list —
each tree projected onto the same fixed set of RFP requirements. **The tree builds; the matrix only
compares.** No matrix is ever constructed as a decomposition device, which was the objection to it.

## Registered predictions

Measured against `Lytin-D 4.0` (Opus: ΣE 1625.5, Σleaf 1062.7, 157.3 leaves, CV 9.25% · Sonnet: ΣE 804.2,
Σleaf 532.2, 79.9 leaves, CV 11.56% · model effect ×2.021).

1. **The axis effect on ΣE is below ×1.4** — materially smaller than the model effect. *This is the
   prediction that matters.* At ×1.7 or above, the decomposition is governed by the arbitrary choice of
   frame rather than by the project, and no constant applied *inside* a frame can help; the repair belongs a
   level up and this whole line of work is misdirected.
2. **Σ leaf E converges better than ΣE**, and the leaf-level axis ratio lands **below ×1.25**. Integration is
   charged per node and node count follows the cut, so the totals should disagree more than the leaves. If
   the leaves disagree *more* than the totals, the invariant argument is wrong at its root.
3. **Spread rises with C2 gone** — Opus CV from 9.25% into the 12…20% band. Registered with its opposite
   named, because the opposite is genuinely possible and would be informative: C2 forces work into a
   mixed-axis list, and mixed axes create ambiguity about where a thing belongs. **A fall in CV would mean
   C2 was itself a source of variance**, not a control on it.
4. **The level falls, 10…30% on Opus.** The four activity branches carry roughly 20% of the `4.0` tree
   (QA 159, infrastructure 82, migration 39, documentation 38 pd of 1625). If an axis does not reproduce
   them the level drops by about that much. **If the level does not fall, the axis regenerated those
   categories unprompted** — which would be a strong result for axes and a weak one for C2.
5. **First level: stable within an axis, different between axes.** Concretely: ≥70% of top-level branch
   names shared across the five runs of one axis, <30% shared between axes. Instability *within* an axis is
   the informative failure — it would mean the axis does not determine a top level and C2's fixity was doing
   real work after all.
6. **Post-hoc placement.** Testing is placed somewhere in ≥4 of 5 runs per axis; **transition off the manual
   process in fewer than 3 of 5.** Migration vanished 10–0 on one model *with* a slot present; without a
   slot it should mostly vanish on both.

Predictions 1 and 2 are the pair that carries the argument, and prediction 6 is the one most likely to be
uncomfortable.

## What comes after, depending on the result

- **Axis effect small, leaves converge** → the decomposition is a property of the project, projections
  become a working cross-check that needs no ground truth, and the next constant can be designed inside a
  frame with confidence that the frame is not the problem.
- **Axis effect small, leaves do not converge** → the invariant is wrong, which means the cuts are not
  partitions of one quantity. Most likely cause to investigate first: the cuts overlap, so MECE is being
  violated and work is being counted twice in at least one of them.
- **Axis effect large** → framing dominates. Everything from C1 to C7 is tuning inside a frame that carries
  more variance than anything it contains, and the work moves to fixing the frame — which is what C2 was,
  badly.
