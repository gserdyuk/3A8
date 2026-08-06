# Proposal: C3 v2 (incremental assembly) + structure as an input

Status: **draft for review, not applied.** Written 2026-08-06, after run8.

Motivation, in one line: run8 showed that 34% of the sensor's spread rides on the number of aggregation
nodes (11…43 on one project, correlation with integration 0.90), and the diagnosis is that C3 prices
**pairs of children** while real assembly is **incremental**, and that the tree's middle levels are
currently invented by each run rather than read from the source.

---

## Part 1 — replacement text for C3

### C3 — Seam pricing: integration is priced by assembly, not by pairs

At every aggregation node the children are joined **incrementally**. Joining k children takes **k − 1
joining operations**, not k(k−1)/2 pairs. **Do not enumerate pairs of children.** Nobody assembles a
system by connecting every part to every other part, and pricing it that way charges for work that will
never be done.

A consequence worth knowing, because it is what keeps this rule honest: a tree with L leaves contains
exactly **L − 1** joining operations in total, whatever its shape. Deep or flat, the count is the same.
The shape of the drawing therefore cannot move the total — only the structure of the system can.

Each joining operation is priced by **what is being joined**: the size of the two parts, and the
strongest kind of coupling that crosses the boundary between them.

| Coupling crossing the boundary | Both parts are leaves | One or both parts are already-assembled subtrees |
|---|---|---|
| Plain call — one side calls the other, stable contract, no shared state | 1.5 pd | 3 pd |
| Shared data — both sides must agree on a structure or its meaning | 3 pd | 6 pd |
| Shared workflow — state crosses the boundary; ordering, partial failure, recovery | 5 pd | 10 pd |

The right-hand column replaces the old "top-level assembly node" doubling, and for the same reason: the
cost of a join scales with the size of the parts being joined. It now applies wherever large parts meet,
not only at the root.

Take the **strongest** coupling that crosses the boundary, not the average: if any state crosses, the
join is shared workflow even when most of the traffic is plain calls.

**State the order in which you joined the children.** The order is a real engineering decision — joining
`(A+B)`, then `+C`, then `+D` puts three small-against-large joins in the plan, while `(A+B)`, `(C+D)`,
then `(AB+CD)` puts one large-against-large join there. Both are legitimate; they cost differently, and
the reader must be able to see which one you priced.

If the parts at some node genuinely cannot be identified well enough to say what is joined to what, use
15% of that node's children and declare that you fell back.

---

## Part 2 — new method constant C5

This replaces an earlier draft that tried to supply the structure as a project input (an "A8"). That was
wrong twice over: it would have had the pipeline do the project's design work, and it was unnecessary —
the modular structure follows from the functional description, and what is missing is not data but a
**rule for deriving it**. A rule belongs to the method, not to the project.

### C5 — Modules are derived from the functions, not chosen

The intermediate levels of the tree are modules, and which modules exist is not a matter of taste.
Derive them, and show the derivation:

1. **List the functions named in the source text.** Do not invent functions and do not merge two that the
   text names separately.
2. **A capability used by two or more functions becomes a module of its own.** If stage changes, conflict
   alerts and booking confirmations all send messages, then messaging is a module — not a piece of each of
   the three.
3. **A function whose capabilities are used by nothing else is a module of its own.**
4. Repeat 2–3 until no capability is duplicated across modules. This terminates: every step strictly
   reduces duplication, and like C1 the result does not depend on the order in which you factored.
5. **The intermediate levels of the WBS are exactly these modules.** Do not create an intermediate level
   that does not correspond to a module derived this way, and do not omit one that does.

Report the function → module map, so that a reader can **check** the derivation instead of trusting it.
Two runs that derive different modules from the same text disagree about a fact, and the map is where that
disagreement becomes visible.

Worked example of rule 2, from the transport side: a module that moves a person and a module that delivers
a thing are not wholly separate — both use a common transport capability. That common capability is a
module, and the two functions become its users. That is what decomposing the task means.

### Architecture is not structure, and belongs elsewhere

Whether the system is a monolith, a set of services, or something else is **not** structure and is not
derived here. It does not change **which** modules exist; it changes **what it costs to join them** — an
in-process call against a network contract with versioning and partial failure. Architecture therefore
modulates the C3 rate card, not the shape of the tree.

The BMS source does not state an architecture (it says "SaaS-based", "scalable", "highly configurable",
none of which decides the question). At present every run silently assumes one, and the assumption moves
the join prices. **This is an unstated parameter and it should be named** — but not in the same change as
C3 and C5. It is the next candidate after these two have been measured.

---

## Pre-registered predictions

To be recorded before any run under these rules.

1. **Node count spread collapses.** Today 11…43, CV 42%. Expected after: a much narrower range, because
   the intermediate levels are read rather than chosen. Direction: down. Magnitude not predicted.
2. **Integration share falls.** Today 31.4%. Pairs are being replaced by k−1 joins, which is fewer items
   on every node with more than three children. Direction: down. Magnitude not predicted.
3. **Total level falls**, for the same reason. Direction: down. Magnitude not predicted.
4. **Leaf-count spread narrows somewhat** (today CV 7.3%), because named structure constrains where
   leaves may be created — but less than the node spread, since C1 still leaves the depth of splitting
   inside a part to the run.
5. **The share of variance carried by the integration factor falls below its current 33.9%**, and leaf
   count becomes still more dominant than its current 62.2%.

Prediction 3 is the one to watch: the last two times the level moved, it moved against my prediction
(run7 up when I said unknown-plausibly-up; run8 up when I said down). A third miss would mean the level
is not being driven by anything I currently understand.

---

## What this does not fix

The **leaf count** remains the largest single contributor to the spread (62.2% in run8), and neither of
these changes addresses it directly. C1 fixes the ceiling on a leaf, and A8 fixes which parts exist, but
how finely a run splits *inside* a named part is still open. That is the next thing to look at, and it
should be looked at only after this change has been measured — one change per measurement.
