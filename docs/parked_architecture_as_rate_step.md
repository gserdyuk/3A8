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
- **one structural input** — where the boundary between them sits in the tree.

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

## The complication, written down now so it is not rediscovered

"Which level of the tree" assumes the service boundary is a clean horizontal cut. It need not be. Three
modules may live in one service while two neighbours are each their own. In the general case the boundary
is not a level but a **labelling of nodes**.

Starting with the level version is a reasonable simplification — but it is a simplification of the same
kind as the uniform rate it replaces, and it should be called that in the text rather than presented as the
whole truth.

## Prerequisites before this is unparked

1. The splitting rule (how finely a module is cut into leaves) is pinned. It currently carries ~100% of the
   sensor's variance; nothing else is worth attention until it is closed.
2. `Lytin-D 3.0` has been measured, so there is a monolith-case baseline to extend from.
3. A validation case exists with a documented actual outcome, against which `k_module` and the ratio can be
   calibrated rather than invented.
