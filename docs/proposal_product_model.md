# Hotyn — build a model of the thing, then a model of the doing, then estimate

Status: **step 1 piloted (run 18); step 2's inputs now exist and its rules are complete; step 3
designed only.** Rules are written to be pasted into sensor definitions; predictions are registered
before measurement. Last change 2026-08-20: the requirement list is split, the technology catalogue
and the BMS declaration are written, and the normalisation question is closed (§8).

**A project is a program plus a technology.** That sentence is the whole design. The product model
says what must exist. It cannot say what work is needed, because the work depends on how you intend
to build and assure it — and that is a separate, declarable choice.

Testing is the clearest case. It is not an inherent activity of software delivery; it is a consequence
of choosing test-based assurance. A mechanism that produced provably correct programs would need no
testing. Formal verification would need proof obligations instead. UAT is not a law of nature; it is a
technology of staged acceptance. None of this work belongs in a model of the product, and none of it
can be invented by a decomposer without reopening the hole this design exists to close.

---

## 1. Three steps, three engines

```
                    ┌── product requirements ──Hotyn-M──▶ product model ──┐
project             │                                                     ├──Hotyn-W──▶ work model ──Hotyn-D──▶ estimate
requirements ──split┤                                                     │                 ▲            (walk the tree)
                    └── demanded work ────────────────────────────────────┘                 │
                                          (carried, not transformed)            technology declaration
```

| step | engine | consumes | produces | numbers? |
|---|---|---|---|---|
| **split** | — | project requirements | two lists: obligations on the *product*, obligations on the *work* | none |
| 1 | **`Hotyn-M 1.0`** | product requirement list | product model — the structure of the thing | none |
| 2 | **`Hotyn-W 1.0`** | product model × technology, **plus the demanded-work list** | work model — the structure of the doing | none |
| 3 | **`Hotyn-D 1.0`** | work model | sizes, integration, totals | yes, and only here |

**Hotyn is a new generation, not a new version of Lytin.** The city names a generation, the letter the
role, the number the version. Lytin decomposed an RFP into work in one step. Estimates do not cross
the generation boundary without a measured conversion: a `Hotyn` number and a `Lytin` number are not
two readings of one scale.

Two of the three engines produce **no numbers at all**. That is what keeps the models reusable — for
additive costing, for simulating the build, for comparing implementation variants, for an RFP
response where the coverage matrix *is* the deliverable, for brownfield work where the model is seeded
with what exists, and for change requests where a new requirement yields a delta.

---

## 2. What run 18 measured, and what it changed here

The pilot: 4 runs of `Hotyn-M` (2 models × 2 processing orders) plus 2 runs of a closure test.

**The anchor holds.** Skeleton size varied ×5 across runs (15 to 75 nodes) and accretion varied ×10
(7 to 71), but **their sum was 82–87 nodes, CV 2.5%**. Where structure comes from is a free choice;
how much of it there is answers to the requirement list. Model gap on anchored structure: **×1.036**.

**The freedom lives in completion.** Derived nodes: Opus 20.5, Sonnet 4.5 — **×4.56**, against ×1.036
on the anchored part. The one unbounded phase is the one that diverges.

**Closure binds.** Given one shared closed model, two decomposers produced ΣE of 1281.77 and 953.55 —
**×1.344**, against **×2.05** for the one-step Lytin instrument on the same project. **67% of the gap
removed.** Leaf count ratio fell from ×1.96 to **×1.21**.

**Node counts converging is not structures converging.** Compared by the registered test — agreement
of the requirement partitions, which requirements share a node — the four models agree on a Jaccard
of only **0.16–0.27**. Raw percentage agreement is 94–98% but is inflated by sparsity and must not be
quoted. Prediction 2 as registered is **not confirmed**.

**The closure-violations list was the most informative output of the whole pilot.** Told it could not
add work the model did not declare, the Opus decomposer listed eleven things it therefore did not
price: system testing, test design, regression, UAT support, project management, business analysis,
data migration, go-live cutover, penetration testing, accessibility, per-screen UX, i18n, test data.
Its own reading: *"the model has no node anywhere whose declared content is quality assurance or
project governance."*

**Every item on that list is technology-derived work.** It is not missing from the product model; it
is not product structure at all. That finding is why this document now has a second step.

Three rules changed as a result:

- **M4's claim that the skeleton is the concentrated free parameter is struck.** Refuted: skeleton
  size ranges ×5 and correlates with nothing that matters.
- **Closure now includes normalisation** (M7). A node whose content resolves to a single leaf is
  reduced into its parent. No rule is needed to prevent such nodes from arising — they are observed
  and collapsed. This removes one known obstacle to comparing two models by coverage; it does not
  remove all of them.
- **A second step exists** (§5), and with it the technology declaration as a pinned input.

### What run 19 measured, and what it changed here

Two repeats of `Hotyn-M 1.1`, Opus, order A, on the split list. The first within-cell measurement this
project has: run 18's cells were all n=1.

**The freedom moved.** Completion — the unbounded phase, ×4.56 between models in run 18 — came out at
**×1.10** between the repeats, and the two runs derived much the same infrastructure independently.
The anchored part — skeleton plus accretion, the part the requirement list is supposed to bound — came
out at **×1.56**, 77 nodes against 120.

**The mechanism is the partition of an obligation into parts.** M2 v1.1 pushes coverage to the node
that realises the obligation and forbids a partial verdict from surviving closure, so a run must
enumerate the parts of each requirement as nodes — and nothing bounds how many parts an obligation
has. One run read requirements as mostly single-part (1.41 nodes per requirement), the other as
compound (2.00). That ratio, ×1.42, carries almost the whole node-count gap.

**This is the third relocation of the same freedom**: C1 fixed leaf size and leaf count went free;
closure fixed leaf count and within-element granularity went free; M2 v1.1 fixed declaration depth and
the number of parts went free. Each rule moves the freedom somewhere countable, which is worth doing,
and none of them has yet removed it. The honest description of this design is that it makes the free
parameter visible and names it, not that it binds it.

**What 1.1 did bind**: the amount of declared co-location, ×8.7 across run 18's four models against
**×1.07** across run 19's two. Readings are comparable between runs in a way they were not.

Two rule defects were found by the runs themselves and are fixed above: M4's empty-skeleton test had
to move from own coverage to total coverage, and provenance had to stop being inferred from an empty
coverage set. Both runs also caught a stale engine stamp left in the sensor definition's output format
and reported it rather than honouring it.

Full write-up: `examples/BMS/run19_product_model_measurement.md`.

---

## 3. Inputs, pinned

Nothing a run may reshape.

| input | consumed by | form |
|---|---|---|
| **product** requirement list | `Hotyn-M` | `R1 … RN`, one atomic obligation per entry, md5 recorded |
| **demanded-work** list | `Hotyn-W` | obligations on the work, drawn from the same source and pinned the same way |
| processing order | `Hotyn-M` | a declared permutation; the criterion is stated, not implied |
| existing structure | `Hotyn-M` | optional: for brownfield, a model to start from |
| **technology catalogue** | `Hotyn-W` | named technologies, each with the activities it mandates |
| **technology declaration** | `Hotyn-W` | one choice per dimension, drawn from the catalogue |
| assumption log | both | scope boundaries, and what may not be struck out (A0) |
| **open-questions register** | both | requirements that read two ways, the question, and the reading assumed while it is unanswered |

For BMS, **split 2026-08-20** (`examples/BMS/requirements_split.md`), from `requirements.md`,
md5 `554ea3608dd0602f0ddf2f7e7b82178c`, N=73:

| list | file | md5 | N |
|---|---|---|---:|
| product obligations | `requirements_product.md` | `0c2dea478b993e4451a66f9468633f1e` | 68 |
| demanded work | `requirements_work.md` | `330826122b607088df3499e3e71cd103` | 5 |
| technology catalogue | `docs/technology_catalogue.md` | version 1.0 | 8 dimensions |
| technology declaration | `examples/BMS/technology_declaration.md` | — | one choice per dimension |

Five entries of 73 failed the hand-over test — *if a complete system were handed over, would this
already be satisfied?* — and moved to the work list: R02, R03, R64, R69, R70. **N for `Hotyn-M` is
therefore 68, and node counts do not cross that boundary**: run 18's anchored 82–87 was measured at
N=73.

### The split, and why it comes first

An RFP states obligations of two kinds and does not distinguish them. Some bind the **product**:
*intelligent search across third-party systems*. Others bind the **work**: `R69` configuration
management and version control across all environments and documents, `R70` robust release and patch
promotion procedures, `R03` the Supplier supports the system.

The second kind is technology-shaped work that the client has **explicitly demanded**. It must not be
handed to `Hotyn-M`, because it is not product structure and would distort the model. It must not be
left to `Hotyn-W` to generate from the catalogue either, because then it would lose its anchor — it is
demanded, and a demanded obligation has to trace to the requirement that demands it.

So there are two lists, both pinned, and a work item may be anchored either way:

- **demanded work** traces to a requirement, and is carried through step 1 untouched;
- **technology-derived work** traces to a (product element, mandated activity) pair, and is generated
  in step 2.

Everything in the work model traces to one or the other. Nothing traces to neither.

### A0 — the imperative: what the client explicitly requires cannot be struck out

Run 18 found `R03` ("the Supplier supports the system") contradicting `A1` ("not included: subsequent
operation"). The log had been carried over from the Lytin era, where it bounded an *estimate*; the
requirement list states what the *product* must be. One run caught it; three priced over it.

The fix is not a scope decision but a rule, and it belongs with the inputs because that is where the
damage is done (author, 2026-08-20):

> **An obligation the client stated cannot be removed by an assumption.** A log may bound what a given
> number prices; it must then name either the instrument that prices the rest, or the parameter that
> is missing without which nothing can price it.

Three permitted outcomes per obligation — **priced here**, **priced by another instrument**, **not
priceable without a parameter the client has not given** — and one forbidden: an obligation appearing
in neither the priced work nor the carried list.

**The failure mode is an exception, not a footnote.** If an id from either pinned list appears in
neither, the run emits a defect report and **no estimate**. A number produced over a struck-out
obligation is not a worse estimate; it is an estimate of a different project, and the number does not
say which.

**What it outlaws is silence, not scope.** The run always has a legal path — carry the obligation with
its reason. That distinction is deliberate: run 18's most informative single output was the list of
work a decomposer judged necessary and refused to invent, produced by a run that proceeded and
reported. An exception on every scope boundary destroys that signal; an exception on silence produces
more of it.

Applied to BMS in `examples/BMS/assumptions.md` v2: the hand-over residue of R02, R03 and R64 is
priced, the continuing service is carried with **the term** named as the missing parameter, and the
question goes back to the client.

### The open-questions register, and the comparison rule that needs it

Where a requirement reads two ways, the procedure is **ask the client; if no answer, assume; declare
the assumption; and exclude the resulting differences when runs are compared** (author, 2026-08-20).
The first three steps are ordinary practice. The fourth is a measurement rule and it is the reason the
register is a pinned input rather than a note:

> **Every comparison of two runs is reported twice — over all requirements, and excluding those the
> register names. The gap between the two readings is the input-ambiguity component of the
> disagreement: a reading on the RFP, not on the method.**

**The filter must be the register and never the runs' own ambiguity flags.** A run that flags more
requirements would otherwise improve its own agreement score by shrinking what it is scored on.

Measured retroactively on run 18, with the runs' flags standing in for a register that did not exist:
19 of 73 requirements were flagged by at least one run, and excluding them raises coverage agreement
on three pairings of four — Jaccard 0.277 → 0.362 on the closest pair, containment 0.43 → 0.63 on the
weakest. It does not approach the registered 90%. **Input ambiguity is a component of the
disagreement, not the explanation of it.**

---

## 4. Step 1 — the product model (`Hotyn-M`)

### M1 — The requirement list is the anchor and the run may not reshape it

No adding, removing, splitting or merging. If an entry appears to hold two obligations, **flag it
ambiguous and proceed**; do not resolve it. The moment a run can reshape the list, the anchor is
internal and nothing is fixed. Ambiguity flags accumulate as evidence that the list needs revising —
a separate, deliberate act performed once for everybody.

### M2 (v1.1) — A node's identity is the set of requirements it covers, declared where they are realised

Names are labels for readers and are never identity. Two nodes are the same node when they cover the
same set. Coverage is a many-to-many relation that only grows. A derived node covers nothing; its
identity is the pointer to whatever required it.

Two things the first version left undefined, both found by run 18's coverage comparison and both
decided here on 2026-08-20.

**Partial coverage is coverage at the node, and a debt at the requirement.** A node that realises part
of a requirement participates in it and carries its id — there is no second, weaker kind of membership,
and without that decision "the same node" was not a defined predicate (counting the marks one run
declared 44 co-located pairs, excluding them 3, against 183 either way for another run on the same
list).

But the mark is a statement about *which part*, and a part is not an answer. **No requirement may
remain partially covered when the model closes** (author, 2026-08-20): if a part is missing, what is
missing is structure, and the run adds it. A partial mark that survives closure is a debt dressed as a
record — it looks like an answer and it is the mechanism by which work disappears quietly. So:

> **At closure, for every requirement, the parts realised by its covering nodes must union to the
> whole obligation.** A residue that cannot be closed is a defect report naming what is left over —
> never a mark left standing.

This is what the imperative (§3, A0) actually requires, and the weaker form — *the id appears
somewhere* — does not: an id can appear while most of what it obliges is nowhere.

**Coverage is declared at the node that realises the obligation, not at the node that presides over
it.** A parent does not declare what it has delegated to a child. This is exactly what M7's *declare*
step already requires of a node's content — *the enumeration of its children plus whatever of its own
is not delegated* — and it was simply never required of coverage. So:

- **own coverage** — what this node realises and does not delegate. This is its identity, and this is
  what two models are compared on.
- **total coverage** — own, plus the union of the children's. **Computed, never declared.**
- **the check at every split**: a parent's total coverage equals the union of its children's totals
  plus its own residue. Nothing appears in a parent that is in no child and in no residue; nothing
  disappears. That is C7 and M9 stated at the level of coverage rather than content, and it is
  mechanical.

**Identity is evaluated on the normalised model** (M7). Normalisation was the registered candidate
explanation for run 18's low coverage agreement; it was recomputed on 2026-08-20 and **explains
nothing** — four pairs added in one model of four. The depth of declaration is the replacement
hypothesis, and this rule is what tests it: one run declared nine requirements on a single portal
aggregate while another declared them across that aggregate's leaves, and no comparison can tell that
apart from real disagreement.

**Consequence for the record:** run 18's four models were built under M2 1.0 and cannot be recomputed
under 1.1 — three of them lack the structure and the fourth records no parents at all. The rule is
tested on the next batch, not on the old one.

### M3 — Four phases, ordered, each doing one job

**skeleton → accretion → completion → closure.** No phase may do another's work. Mixing derivation
into accretion makes the fixpoint unstable and reintroduces dependence on processing order.

### M4 — Skeleton: read the whole list at once, posit structure, attach nothing

Accretion has nowhere to start: the first requirement has no parent, so structure must be posited
before any requirement is placed — and positing is derivation.

Read the requirement list **as a set, not as a sequence**. Posit a tree with names and intended scope.
**Attach no requirements. Assign no coverage.** Stop when every requirement has at least one plausible
attachment point.

**Provenance is recorded by origin** — `posited`, `accreted`, `derived` — and never inferred from an
empty coverage set. Under M2 v1.1 an aggregate holds no own coverage by rule, so `implied` would
otherwise conflate a grouping node with a derived one. **Counts by provenance are taken before
normalisation**, because a collapse can merge a stated node into a derived leaf.

**A skeleton node is a finding when its *total* coverage is empty at convergence** — nothing in its
subtree covers anything. Say per node whether it is a wrong guess or genuine infrastructure no
requirement names; never keep or drop one silently. Applying the test to *own* coverage reports every
aggregate as a finding, which is a false positive manufactured by the coverage rule. Run 19 found this
in both runs, independently, on the first outing of 1.1.

**How coarse or fine the skeleton is does not matter.** Run 18 measured skeleton sizes of 15 and 75 on
the same list with anchored totals of 86 and 82. The split between positing and accreting is a
presentation choice; normalisation at closure removes what is left of it. Earlier drafts of this
document claimed the skeleton was where the method's freedom concentrated. **That claim is withdrawn.**

### M5 — Accretion: one requirement at a time, four verdicts, additions only

Walk the list in the declared order. Against the structure as it stands:

| verdict | action |
|---|---|
| **covered** | record which node(s) cover it; add nothing |
| **partially covered** | record which node(s) cover which part; **add what is missing in the same pass** — the verdict is a debt, not a resting place |
| **not covered** | add node(s) under an existing parent |
| **deferred** | record why; retry next pass |

- **Only additions.** Nodes are never removed and never moved. An assignment once made is never withdrawn.
- **Resolution is final.** A resolved requirement is never reopened and may not cause a further addition. Additions are therefore bounded by N.
- **Repeat until a pass adds nothing and defers nothing.**

**Log every verdict, including `covered`.** The judgement "this is already realised" is where the
remaining freedom lives; a log of additions alone loses what is being measured.

*Observed in run 18: `deferred` was never used, in any run, in any pass, including under the
adversarial reverse order. The skeleton gave every requirement an attachment point on first
presentation. The verdict stays in the rule because its absence is the evidence.*

### M6 — Completion: add only what the structure requires, and name the trigger

After accretion converges, add what the structure implies but no requirement names. Worked example:
"login is stepped — login on one screen, password on the next" yields an authentication subsystem by
accretion; **password recovery** arrives by completion.

Every completion node records the **trigger**, a one-line **justification**, and its pass number.
Completion has its own fixpoint with the same only-adds rule.

**Completion may not create a node that covers a requirement.** If it does, that requirement was
mis-judged in accretion — flag it as a defect, do not silently repair it.

**This is the one unbounded phase, and run 18 confirmed it is where the model-dependence lives**:
derived nodes differed ×4.56 between models while anchored structure differed ×1.036. It is
instrumented rather than constrained: **the fraction of derived nodes is the primary reading of this
engine.** A bound on completion is the next constant that will be needed, and none is designed yet.

### M7 — Closure: freeze, declare, normalise

When completion converges:

1. **Declare.** Every node's content is the enumeration of its children plus whatever of its own is
   not delegated to a child.
1a. **Check completeness.** For every requirement, the parts realised by its covering nodes union to
   the whole obligation. No requirement leaves closure partially covered: either the missing structure
   was added during accretion, or the residue is reported as a defect and named.
2. **Normalise.** Any node whose content resolves to a **single leaf** is collapsed into that leaf.
   Its coverage set merges into the leaf; the collapse is recorded. A one-child node is not an
   aggregation and carries no information.
3. **Freeze.** From this point the model admits no addition.

Normalisation is not a defence against a rule being broken — it is hygiene applied after the fact.
Observe, collapse, record.

It does **not** make the model canonical, and an earlier draft of this document claimed it did. It
removes one specific kind of spurious difference: a chain of single-child nodes wrapped around one
leaf. Where one model writes `Notifications → Channels → SMS → leaf` and another writes the SMS leaf
alone, a coverage comparison sees two structures with identical content. Collapsing removes that.
Two models with the same coverage do not become identical — grouping and the depth of genuine
multi-child aggregation still differ.

### M10 — The product model is detailed down to functions, and no further

A leaf of the product model is a **function**: one named capability that does one identifiable thing,
describable as an action on an object — *validate an uploaded inventory file*, *resolve notification
recipients*, *rank offers against a requirement*.

- **Too coarse** — the leaf is a container whose name is a noun and inside which two or more distinct
  capabilities can be named immediately. That is a module, and it must be split.
- **Too fine** — the leaf cannot be described without saying how it is built rather than what it does.
  That is below the function level; do not create it.

At closure, any leaf that is still a module is **reported, not repaired**.

**Why this rule now exists.** Run 18's closure test produced 1.00 leaves per model node (Sonnet) and
1.21 (Opus). The work breakdown is now very nearly a copy of the model, so **the granularity of the
product model has become the granularity of the estimate**, and nothing was specifying it.

The interaction with C1 is the reason it matters. C1 splits anything above 10 person-days:

- a **fine** model — C1 almost never fires, the model determines everything, and nothing is free;
- a **coarse** model — a node worth 40 pd is split by C1 into four or more leaves, and **leaf count is
  free again**, which is precisely the defect this generation was built to remove.

In run 18 C1 barely fired. That was luck, not design: both models happened to land near function
granularity. **M10 makes it design.**

### C1 becomes a backstop, not the primary control

Under Lytin, C1 fixed leaf size and left leaf count free — the arrangement that produced the ×2 model
gap. Under Hotyn the model fixes the count and C1 only catches functions that turn out unusually
large.

That gives a free diagnostic: **if C1 fires often, the product model is too coarse.** The firing rate
is a reading on the model, not on the estimator.

### M8 — The models carry no numbers

No effort, size, duration, cost or complexity score — not in the product model, not in the work model.
Counts of nodes, requirements and work items are readings, not estimates.

---

## 5. Step 2 — the work model (`Hotyn-W`)

### W1 — Technology is declared, and drawn from a catalogue

A **technology catalogue** names each technology and, for each, **the activities it mandates**. A
**technology declaration** picks one entry per dimension. Both are pinned inputs; a run chooses
nothing and invents nothing.

Dimensions, at minimum:

| dimension | example choices | example mandated activities |
|---|---|---|
| assurance | test-based · formal verification · review-only | test strategy, test design per element, execution cycles, defect cycle **or** specification, proof obligations, proof checking |
| acceptance | UAT · pilot · direct to production | UAT preparation, cycles, sign-off |
| delivery process | small co-located team · distributed with ceremonies | coordination, planning, status reporting |
| environments | dev/stage/prod · single environment | provisioning per environment, promotion procedure |
| data | migration from legacy · seeding · greenfield | extraction, mapping, load, reconciliation |
| documentation | operational + user · none | per-audience document set |

**The mandated activity list belongs to the catalogue entry, not to the run.** If a run may decide
what a technology implies, the free parameter is back and the whole chain is decorative. Extending the
catalogue is a separate, deliberate act — like revising the requirement list.

**The catalogue exists as of 2026-08-20**: `docs/technology_catalogue.md` 1.0, eight dimensions.
Writing it exposed three holes in this section, all closed there and recorded here.

### W7 — Applicability is judged against a fixed set of element classes

W3 asks, for every product element and every mandated activity, *does this activity apply to this
element?* Answered from the element's name, that is free association. Every element is therefore first
assigned **one class** — `behaviour`, `surface`, `interface`, `store`, `statement`, `aggregate` — from
its declared content at closure, and every catalogue activity names the classes it applies to. The run
classifies; it does not decide what an activity means.

The classification is itself a judgement, and it is now where this step's freedom sits. W3 already
requires the negative answers to be logged; **log the class with them**.

### W8 — Every activity declares its scope, and scope is not the run's to choose

*Write test cases* is per element; *write the test strategy* is once for the whole model. If the run
decides which, the size of the work model is set by the run and prediction 1 is unscoreable. Five
scopes: `once`, `per element`, `per aggregate`, `per environment`, and `× cycles` as a modifier on
either of the last two.

**Cycle counts are policy parameters of the declaration, not estimates.** "Two test cycles" is a
choice about how you work. A parameter that could only be known from a duration or an effort figure
may not enter a declaration — that would make the technology an output of the estimate.

### The six dimensions could not build anything

Assurance, acceptance, delivery process, environments, data and documentation between them mandate no
construction, so the crossing in W3 would have generated testing for a product nobody built. The
catalogue adds **construction** as a seventh dimension and **security and compliance assurance** as an
eighth. §5 says "at minimum", so this extends rather than contradicts it — but the omission is worth
recording, because it is the kind that a run would have silently repaired.

### W2 — Work model closure: every work item traces to a pair

**Every work item traces to (a product-model element, a technology-mandated activity).** Nothing else
may appear. A work item with no product element is invention; a work item with no mandated activity is
invention.

This is M9 applied at the second boundary, and it is what carries the anchor from the requirement
list all the way into the work: requirements bound the product model, the product model and the
catalogue jointly bound the work model.

### W3 — Work is found by answering a fixed set of questions, not by listing work

**Never ask "what work does this project need?"** That question has no bounded answer, and it is the
question that let leaf count run free under Lytin.

Ask instead, for every element of the product model and every activity the declared technology
mandates: **does this activity apply to this element?**

The number of questions is known before the run begins: (product elements) × (mandated activities).
Neither factor is the run's to choose. Every **yes** becomes exactly one work item. Every **no**
becomes nothing.

Worked example. The declaration sets assurance = test-based; the catalogue says that technology
mandates three activities — *write test cases*, *run a test cycle*, *fix defects*.

| product element | activity | answer |
|---|---|---|
| SMS notification channel | write test cases | **yes** → one work item |
| SMS notification channel | run a test cycle | **yes** → one work item |
| business process definition (a document) | run a test cycle | **no** — nothing to execute |
| business process definition (a document) | write test cases | **no** |

**Record the `no` answers, each with a one-line reason.** Same rule and same reason as accretion's
`covered` verdict: a run that logs only the work it created cannot be compared with another. If two
runs produce different work models, the difference lies in the applicability judgements — and those
are visible only if the negatives are written down. **The negative answers are the measurement of
this step's remaining freedom.**

### W4 — The work model carries no numbers

Same rule as M8, same reason. Sizing is `Hotyn-D`'s job and nobody else's.

### W6 — Demanded work joins the work model without being transformed

The demanded-work list from the split is already work. It does not pass through `Hotyn-M` and it is
not generated by the crossing in W3 — it enters the work model directly, as its own branches, each
item carrying the requirement id that demands it.

So the work model has branches of two provenances, and every item declares which:

| provenance | traces to | produced by |
|---|---|---|
| **demanded** | a requirement id | carried from the split |
| **derived** | (product element, mandated activity) | the crossing in W3 |

An item that would be both — demanded by a requirement *and* mandated by the declared technology — is
recorded **once, in the technology-derived branch**, because that is what it is and where it belongs.
The entry in the demanded-work list is then marked *accounted for at `W-nnn`* and produces no item of
its own.

Counting it twice would double the work. Placing it on the demanded side would scatter technological
work across two branches according to whether the client happened to write it down, which would make
the technology branch un-varyable — and varying it is the whole point of the falsification test
(prediction 2). The pointer keeps the requirement answered without moving the work.

### W5 — Two findings the crossing produces for free

- **A mandated activity that applies to no product element.** Either the technology is wrong for this
  product, or the product model is missing something.
- **A product element no activity touches.** Either it needs no work — possible, for a pure
  declaration — or the technology declaration is incomplete.

Both are reported, neither is repaired.

---

## 6. M9 — Closure propagates all the way down

The rule "children are exactly the parent's declared content, possibly subdivided" holds at **every**
level and across **every** boundary: within the product model, from the product model into the work
model, and from the work model into the estimate. A leaf of the estimate must trace to an element of
its parent's declared content.

Without this, each step constrains nothing about the next.

**What it binds, measured.** Run 18's closure test gave two decomposers one shared closed model:

- leaf count ratio fell from **×1.96** (Lytin, free) to **×1.21**
- ΣE ratio fell from **×2.05** to **×1.344**
- one decomposer produced exactly one leaf per model node; the other subdivided 22 of 109

**What it does not bind.** How many pieces one declared element becomes. That residual was predicted
at ×1.63 and measured at ×1.21 — smaller than expected, but not zero. A constant that binds it,
without reintroducing the order-dependence a merge rule would create, is not designed.

**What it buys outright.** Under closure a pre-split whole-node figure and the sum of the leaves
beneath it cover **provably the same content**, so any discrepancy is estimation error and cannot be
scope drift. Under Lytin the two were confounded, which is why C6's systematic +8…+20% was
uninterpretable.

**And it makes invention visible.** The closure-violations list is not a side effect; it is the
mechanism by which work that nothing declared stops being silently priced and starts being reported.

---

## 7. Step 3 — the estimate (`Hotyn-D`)

Sizes the work model and nothing else. Inherits from Lytin what measurement showed to be sound:

- **C1** — split above 10 pd of most-likely effort, stop below, never merge, no leaf under 1 pd.
- **C3** — at every aggregation node, an integration item of 20% of the leaf effort beneath it; the
  base is leaf work only, so the rate does not compound; a node resolving to a single leaf gets none.
- **PERT** — O, M, P per leaf; E = (O + 4M + P)/6.
- **C4** — the static blind-spot list, verbatim, as method metadata.
- **M9** — closure, above, which is new and is what makes the rest mean anything.

### The walk of the tree is the estimate, and it is also the simplest execution model

The work breakdown is obtained by **walking the work model**. That walk is a degenerate simulation of
the build: one worker, strictly sequential, no dependencies, no state. Additive costing is that walk
with nothing carried between steps.

This means the two routes named at the outset — *cost it additively* and *simulate the build* — are
not two designs. They are the same object at two levels of richness:

| | what the walk carries |
|---|---|
| additive estimate | nothing; each item is priced in isolation and the prices are summed |
| simulation | state — what is already done, what that makes cheaper, who is free, what blocks what |

A richer walk is where reuse accumulating, learning, ordering and correlated risk become expressible,
because all four are statements about state carried between steps. The additive sum is the case where
that state is empty. **Nothing in this design has to change to move from one to the other** — only the
traversal does.

`C2` (the projection axis) does not exist in this generation. The product model has no axis; a
projection onto process or subsystem is a *rendering* of an existing structure, computed, not a second
independent construction. Run 17 discontinued the axis comparison for reasons that apply here too.

---

## 8. Open questions, named rather than hidden

- **Nothing bounds how finely an obligation is divided into parts.** Run 19's two repeats read the
  same 68 requirements as 96 and 136 (requirement, node) assignments — 1.41 against 2.00 nodes per
  requirement — and that ratio carries a ×1.56 gap in anchored structure. This is the current location
  of the method's free parameter and no rule addresses it. M10 fixes the *level* of a leaf; it says
  nothing about how many leaves one obligation becomes.
- **Completion is unbounded** (M6). Measured at ×4.56 between models in run 18 and at **×1.10 between
  two repeats of one model** in run 19 — so between-model spread and within-cell spread are very
  different quantities on this phase, and only one of them has been measured twice.
- **Whether the anchored spread is new.** Run 19 measured ×1.56 between identical runs on the part the
  requirement list bounds; run 18 measured 82–87 across four runs that differed in model and order.
  Both cannot be typical. The discriminating experiment is two repeats under `Hotyn-M 1.0` on the same
  list, and it has not been run.
- **Granularity inside a declared element remains free** (M9). Measured at ×1.21.
- **Coverage agreement between models is low** (0.16–0.27 Jaccard) even though anchored size agrees to
  ×1.036. **Checked 2026-08-20 and closed as an explanation**: normalisation adds four pairs in one
  model of four and none in the other three (run 18 §3c). What the recomputation did find is that the
  four runs declare very different *amounts* of co-location — 21, 44, 71 and 183 pairs — which caps the
  Jaccard mechanically, and that 43–93% of the sparser relation sits inside the denser one. One of the two things it opened is now
  decided — **M2 v1.1**: partial coverage counts, and coverage is declared where it is realised. The
  other is not: a size-insensitive measure of structural agreement has to be chosen and registered
  *before* the next batch rather than after it, because after the runs every alternative measure is a
  way of getting the answer you now want.
- **Whether declaration depth is what depressed the coverage agreement** — the replacement hypothesis
  after normalisation failed. M2 v1.1 states the rule that tests it; prediction 6 registers what it
  must do. Until the next batch runs, the honest position is that structural agreement between two
  product models has never been measured with a rule that fixes where coverage is declared.
- **"Function" is a judgement, even bounded by M10.** The rule fixes the *level*; it does not make
  two readers draw the same functions. What it removes is the licence to stop at modules or to
  descend into implementation, which is where the ×5 spread came from — not all disagreement.
- **The technology catalogue exists as of 2026-08-20** (`docs/technology_catalogue.md` 1.0) and its
  granularity is the free parameter this document predicted — now with a measured shape. The count of
  work items is (elements × applicable per-element activities) + (aggregates × per-aggregate activities
  × cycles) + fixed items, so **each per-element activity multiplies the whole product model**. For a
  model the size of run 18's the declared BMS technology projects **650–750 work items**, registered
  before the crossing runs. Two consequences are named there and neither is settled: C1's 1 pd floor
  will round up a large number of honestly sub-day items, and the delivery-process dimension mandates
  work that is proportional by nature and fits the (element, activity) trace badly.
- **The requirement list's own granularity** is one person's judgement, pinned rather than correct.

---

## 9. Registered predictions

Scored only after the runs.

**Settled by run 18** (recorded here, not re-registered): anchored structure invariant to ±3%
(confirmed) · derived fraction carries the model gap (confirmed, ×4.56) · skeleton size stable
(**refuted**, ×5) · empty skeleton nodes under 20% and infrastructural (confirmed) · transition off
the predecessor process not generated (confirmed as a predicted failure) · coverage agreement above
90% (**not confirmed**, Jaccard 0.16–0.27) · closure cuts the model gap to ×1.4–×1.8 (**confirmed at
the lower edge**, ×1.344).

**Open, for the work model:**

1. **Work-model size is bounded on both sides.** The model gap on work-item count is **below ×1.2**,
   because neither |product elements| nor |mandated activities| is the run's to choose. Above ×1.5
   would mean the applicability judgement in W3 is a free parameter of the same order as the leaf
   count was, and W3 needs constraining.

2. **The falsification test, now with a mechanism.** Hold the requirement list and the product model
   fixed; change the assurance dimension from test-based to formal verification. The estimate must
   move by **more than ×1.3**. **If it does not move, the instrument is measuring the document and not
   the project**, and that is a verdict on the whole three-step design, not on one constant.

3. **The closure-violations list shrinks to near-empty.** Run 18's eleven items were all
   technology-derived. With a technology declared, at most two should survive — and any that do
   identify a dimension the catalogue does not yet cover. If the list stays long, the crossing in W3
   is not generating the work the catalogue mandates.

4. **Delivery work is a large fraction of the total, and it is now visible.** Technology-derived work
   exceeds **30%** of ΣE. Under Lytin this work was present but inseparable from product work; under
   Hotyn it is a distinct subtree and can be varied independently. If it comes out below 15%, the
   catalogue is under-specified rather than the project being unusually lean.

5. **C1 fires rarely, and when it does the model is at fault.** With M10 in force, fewer than **15%**
   of work items require a C1 split, and leaves per work item stays under **1.3**. Above 30% means the
   product model is sitting at module level rather than function level, and the reading is on the
   model, not on the estimator.

6. **M2 v1.1 is what was depressing the coverage agreement.** With coverage declared where it is
   realised, the four runs' co-location relations stop differing by ×8.7 in size (21 to 183 pairs) and
   come within **×2 of each other**, and Jaccard between models rises above **0.5**.

   **Scored by run 19, and it splits.** Two repeats of one model on one order gave relations of 44 and
   41 pairs — **×1.07**, against ×8.7 in run 18. The size cap that made run 18's Jaccard figures
   uninterpretable is gone, and that half is confirmed with room to spare. **Jaccard came out at
   0.308**, below the registered 0.5, in the easiest case the design admits: same engine, same input,
   no order effect, no model gap. So declaration depth was one mechanism and not the mechanism, and
   what is left is real structural disagreement — 20 shared statements out of 65.

Predictions 1 and 2 carry the argument. **Prediction 2 is the one that can end the design.**

---

## 10. What comes next, in order

1. ~~Split the BMS requirement list.~~ **Done 2026-08-20** — `examples/BMS/requirements_split.md`.
   Five entries moved, not three: R02 and R64 joined R03, R69 and R70. Three of the five are excluded
   by assumption A1, which is the same input defect run 18 caught on R03, now shown to be systematic.
2. ~~Write the technology catalogue.~~ **Done 2026-08-20** — `docs/technology_catalogue.md` 1.0, with
   `examples/BMS/technology_declaration.md` as the BMS declaration and a second declaration `BMS-FV`
   for the falsification test. Writing it required two rules this document did not state (W7, W8, §5)
   and two dimensions beyond the six listed here — **construction**, without which the crossing
   generates testing and no implementation, and **security and compliance assurance**.
3. ~~Check whether normalisation improves coverage agreement.~~ **Done 2026-08-20, run 18 §3c: it does
   not.** See §8 for what replaced it as the open question.
4. ~~Run `Hotyn-M` on the split list.~~ **Done 2026-08-20** — run 19, two repeats, Opus, order A.
   Executability confirmed; two rule defects found and fixed; the freedom relocated to the partition
   of obligations into parts.
5. **Attribute run 19's ×1.56.** Two repeats under `Hotyn-M 1.0` on the same split list, changing
   nothing else. Either 1.1 loosened the anchor or run 18's tight cluster was luck, and two runs
   settle it. Cheapest outstanding experiment, and everything downstream inherits the answer.
6. **Run `Hotyn-W`** on a run-19 product model with the declared technology, then `Hotyn-D` on the
   result. Note that the two run-19 models differ by ×1.65 in node count, so **which one is crossed
   changes the work model materially** — run both, or the crossing measures the choice of model rather
   than the crossing.
7. **Run the falsification test** (prediction 2). It is cheap once step 3 exists and it is the one
   that matters.

**On which models to use.** `Hotyn` readings are produced on Opus and Fable. A weaker tier is still
run, but its numbers are **not part of any estimate** — they are the diagnostic. Every defect this
project has found was found by disagreement between capability tiers: the ×2.05 that showed leaf count
was unpinned, the ×5 skeleton spread that showed the anchor held anyway, the ×1.344 that showed
closure binds. A single tier is always self-consistent, and self-consistency is not evidence. Where
tiers diverge, the method is under-determined at that point.
