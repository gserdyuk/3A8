# Parked: architecture as a step in the integration rate

Status: **parked, not a proposal.** Recorded 2026-08-06, while `Lytin-D 3.0` was being written. Nothing
here is to be built until the prerequisites at the end are met.

## The idea

`Lytin-D 3.0` prices integration at a single uniform rate — 20% of the leaf sum beneath every node. That is
a fair description of a monolith, where joining any two parts is work of one kind.

It is not a fair description of a service architecture, where there are **two** kinds of join: two modules
*inside* one service behave like the monolith case, while two *services* carry a network contract,
serialisation, versioning, partial failure and independent deployment. The true cost is not a rate but a
**step**, and where the step falls depends on service granularity — whether a given part is a service of
its own or a module inside one.

So the method would gain:

- **two parameters** — `k_module` and `k_service`, or better `k_module` plus the *ratio* between them;
- **one label per node** — whether that join crosses a service boundary or stays inside one.

## Why this shape is worth keeping

**The current rule is the monolith case of the extended one.** With no service boundaries, every join is
priced at `k_module` and the extended rule collapses to exactly `3.0`. The extension therefore does not
invalidate anything measured under `3.0`; it contains it. That is worth a great deal — it means the
measurement being run now is not spent if this is adopted later.

Order of magnitude, at plausible values. Under `3.0` a functional leaf carries 0.6 in integration (three
assembly levels × 20%) and an activity leaf 0.4, giving a blended multiplier of 1.53. If the service
boundary sits at the module level and `k_service` = 40%, a functional leaf carries 0.2 + 0.4 + 0.4 = 1.0
and an activity leaf 0.8, and the multiplier becomes **1.93** — about **+26%** on the total. That is the
right order for monolith-versus-services: substantial, not threefold.

## Two safeguards it cannot go in without

**The boundary level must be an input, never a run's choice.** Taken from the source text when the source
fixes an architecture; otherwise the run treats the system as a monolith and says so. Without this rule the
extension manufactures exactly the kind of free parameter the last four rounds were spent closing — the run
picks a level, and the spread moves there.

**Two unmeasured numbers instead of one.** Neither `k_module` nor `k_service` is visible to a repeatability
measurement: both move the level, not the spread. Only comparison with a known outcome can check them. So
the second parameter is worth adding only once there is a case with a documented actual to calibrate
against — otherwise the method acquires two invented numbers in place of one. Parameterising as
`k_module` + a ratio is probably better than two absolute rates, since "crossing a network boundary costs
n times an in-process one" should transfer between projects better than either rate alone.

## The boundary is a labelling of nodes, not a level of the tree

An earlier draft of this note proposed naming *the level* at which the service boundary sits. That is
wrong, and the correct form is per-node labelling. Recorded here with the reasoning, so the inferior version
is not re-invented.

**A level assumes a clean horizontal cut, and reality need not oblige.** Three modules may live in one
service while two neighbours are each their own. A level cannot say that; a label per node can.

**A level has to be inferred; a label is stated.** A source says "the booking engine is a separate service",
not "the boundary is at depth two". Deriving a level from such sentences means guessing — which is the very
thing the first safeguard exists to prevent.

**Labelling adds expressiveness without adding freedom, which is the non-obvious part.** One decision per
tree versus N decisions per tree looks like a loss for repeatability. It is not, because of the safeguard
above: every label is either taken from the source or defaults to `module`. A run with no architectural
information labels everything `module` and lands exactly on the monolith case; a run with information
labels what the source states. Neither run chooses anything.

**And it is checkable at the point of disagreement.** The label is printed beside its node, as the
function → module map already is, so a reader can dispute one node rather than the whole tree. It also
becomes a third instrument reading — how many joins were labelled `service` — so that if a source is vague
and runs diverge, the divergence is *visible in the readout* instead of hidden inside the total.

**Two framings of the same label, both to appear in the rule text.** From the pricing side: do the children
being joined sit in the same unit of deployment, or in different ones? From the construction side, which is
how it will actually be used: when a part is split, is it split into modules or into services? They describe
one node from two directions, and stating only one of them invites a reading where they come apart.

## Prerequisites before this is unparked

1. The splitting rule (how finely a module is cut into leaves) is pinned. It currently carries ~100% of the
   sensor's variance; nothing else is worth attention until it is closed.
2. `Lytin-D 3.0` has been measured, so there is a monolith-case baseline to extend from.
3. A validation case exists with a documented actual outcome, against which `k_module` and the ratio can be
   calibrated rather than invented.
