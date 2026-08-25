# BMS — Run 20: the crossing, `Hotyn-W 1.0` — pilot on two subtrees

Date: 2026-08-20. **Registered before the run returned.**

## Why a pilot before a measurement

The catalogue registered the cardinality of the crossing before any run existed: for a model of run
18's size — 109 elements — the declared BMS technology should yield **650–750 work items**. Two things
follow that are worth knowing before spending a measurement run:

1. A work model of that size may not fit in one sensor reply at all. If it does not, the answer is to
   coarsen the activity set **in the catalogue**, once, for everybody — never inside a run.
2. `Hotyn-D`'s C1 forbids a leaf under 1 person-day. Per-element activities on a fine product model
   produce items honestly worth a fraction of a day, and the floor would round every one of them up.

Both are questions about the instrument, and one cheap partial run answers them.

## Design

**Two subtrees of HM19-OA1** (the 78-node model), 17 elements of 78:

- **N02 Platform Foundation** — six children, five of them properties rather than run-time behaviour.
  Chosen because `statement` is the class the catalogue itself flags as the cheapest way to lose work,
  so the hardest classification case is in the sample deliberately.
- **N26 Booking Domain Core** — nine descendants: stores, behaviours, and three derived elements that
  cover no requirement at all.

The mix leaves out `surface` and `interface`, which is a known limitation of this sample: the UAT and
documentation activities are gated on an aggregate containing a surface, so they cannot fire here.

**Partial-run rule under test.** Once-scoped and per-environment activities belong to the whole model
and must not be generated in a subtree run — otherwise they are counted again when the rest is
crossed. Whether the sensor honours that is itself a reading.

## Isolation, and its weakness in this run, stated plainly

The sensor definition `.claude/agents/work-crosser.md` was written during this session and **was not
available to the Agent tool** — agent definitions are read at session start on this harness, and the
correction recorded on 2026-08-19 claiming otherwise was an error of observation. The pilot therefore
ran through a general-purpose agent with the definition pasted into the task: **isolation enforced by
instruction, not by the absence of tools**, and verified after the fact.

Acceptable for a pilot, whose questions are cardinality and executability. **Not acceptable for the
two measurement runs**, which need a fresh session and the real definition.

## Registered expectations

1. **Items per element between 5 and 8.** Arithmetic from the declaration, not a guess: an element of
   class behaviour, surface, interface or store draws K1, K2, A2, A3, A4 and D4 — six — with stores
   drawing G1–G3 on top and interfaces A10; a statement draws K3, D4 and, where it is a performance or
   availability property, A9. Outside that band the classification or the applicability judgement is
   doing something the declaration did not ask for.
2. **The partial-run rule is honoured**: no once-scoped item, no per-environment item, and the
   demanded-work list reported as out of scope rather than as absent.
3. **Every element is touched.** The three derived elements — Supplier Registry, Traveller Profile,
   Audit Trail — cover no requirement, so D4 cannot fire on them, but K1, K2, A2, A3, A4 and the store
   activities all can. An element nothing touches would be a W5 finding and would say the declaration
   is incomplete.
4. **The `no` log is not empty.** If every class match becomes an item, the applicability question in
   W3 is decorative and the crossing is arithmetic on the classification alone. That is a real
   possible outcome and it would relocate this step's entire freedom into W7.
5. **The projection onto the requirement anchor is produced** — work items per requirement. Without
   it, two work models built on different product models cannot be compared at all, which is the whole
   reason the section exists.

---

# Results

Returned with `tool_uses: 0`. Raw in `run20_raw/crossing_pilot.md`.

**94 work items from 17 elements, against 357 applicability questions fixed before the run began.**

## 1. Scoring the registered expectations

| # | expectation | outcome |
|---|---|---|
| 1 | items per element between 5 and 8 | **CONFIRMED**: mean **5.53**. Per element the range is 2–8, and the 2s are statements that draw only K3 and D4 — the arithmetic of the declaration, not a judgement |
| 2 | the partial-run rule is honoured | **CONFIRMED**, and sharpened: the run separated **deferred** (17 once- and per-environment activities, belonging to the whole model) from **unused** (4 that applied to nothing). The definition did not ask for that distinction and it is worth keeping |
| 3 | every element is touched | **CONFIRMED**: 0 untouched. The three derived elements that cover no requirement drew 8, 8 and 5 items |
| 4 | the `no` log is not empty | **CONFIRMED**: 30 negatives — and the split matters more than the count, see §2 |
| 5 | the projection onto the requirement anchor is produced | **CONFIRMED**, and it produced the run's most uncomfortable number, §3 |

## 2. Half the negatives are mechanical, and all the judgement sits in one place

The run split its refusals without being asked:

- **15 `filter`** — the declaration's own further condition excluded the element. No surface inside an
  aggregate, so no UAT; no own requirement coverage, so no requirement elaboration. Mechanical, and
  two runs cannot differ on them.
- **15 `judgement`** — class and condition both matched and the run still answered `no`.

**Every one of the fifteen judgement negatives is a store against G1, G2 or G3** — the seed-data
activities — with the same reason each time: the content arrives at run time, from CTC ingestion,
supplier upload or change events, and no reference set precedes it.

So in this sample the discretionary space of the whole crossing was one question, asked five times:
*does this store need seed data?* Everything else fell out of the classification and the declaration.
**That is the finding the pilot was for.** It says the freedom of this step lives in W7's
classification, not in W3's applicability question — and it means the measurement runs should be read
as a measurement of classification agreement.

## 3. A third of the work traces to nothing the client asked for

The projection: **59 of 94 items trace to an element carrying requirement coverage, 35 do not** — the
two aggregates and the three derived elements. Legal under W2, which requires an item to trace to a
product element, not to a requirement. But it puts a number on something previously invisible:
**37% of the work in this sample hangs off structure the requirement list never asked for**, and that
structure came from the product model's completion phase and its aggregation spine.

Under `Lytin` this work existed too and was indistinguishable from the rest. It is now countable, and
the count is large enough that the completion phase's ×4.56 model-dependence — measured in run 18 —
matters directly to the estimate rather than only to the shape of the tree.

## 4. A defect in the catalogue, found by the crossing

**F7: `per aggregate` attaches to the wrong thing.** The catalogue scopes test execution, defect
resolution, regression, test data and planning "per aggregate", where `aggregate` is a **class**:
children and nothing of its own. But M2 v1.1 makes coverage get declared at the element that realises
it, so an internal node that realises something of its own is not of class `aggregate` — and draws no
per-aggregate work at all, however large its subtree.

In this sample the whole booking-requirements branch — N28 → N74 → {N75, N77} — has no aggregation
node of its own, so its test execution, regression and planning all land on N26 above it. Across the
whole HM19-OA1 model: **18 elements have children, only 13 of them are of class `aggregate`.** The
five excluded are excluded by a coverage-declaration rule that has nothing to do with whether they
aggregate anything.

**The fix, applied to the catalogue as version 1.1:** the scope becomes **per parent** — one item per
element that has children — and the class `aggregate` keeps its meaning for the classes an activity
applies to. Tree position and content are two different questions and were being answered by one word.

The same conflation would have reached `Hotyn-D`, whose C3 adds integration effort at every
aggregation node. It is worth knowing before that step rather than after.

## 5. Four findings about the product model, from a second reader

The crossing read HM19-OA1 as a second pair of eyes and reported four bundling defects the model
builder did not: N69 mixes a delivery-model property with a run-time mechanism; N29 is declared a
store while its obligations describe an upload channel that exists nowhere; N77 carries R44, a
user-facing override, inside merge-policy machinery; N05 mixes an availability property with
degraded-mode behaviour.

**A leaf that bundles two things is an M10 violation**, and M10 says report it at closure. The model
builder reported none of these. Whether the crossing is systematically better at spotting them, or
whether it simply reads the model with different questions in hand, is worth one line of attention
when the measurement runs land.

## 6. The size question the pilot was run to answer

At 5.53 items per element:

| model | elements | projected items |
|---|---:|---:|
| HM19-OA1 | 78 | **~450** |
| HM19-OA2 | 129 | **~730** |

The catalogue registered 650–750 for a 109-element model before any of this existed; the larger of the
two lands inside that band and the smaller below it, which is what a smaller model should do.

**94 items fitted comfortably in one reply. 450 will not, at this level of detail** — the pilot's
output ran to twenty-one per-activity tables plus a thirty-line negative log for seventeen elements.
Two ways forward, and the choice belongs to the catalogue rather than to a run:

- **coarsen the activity set** — merge K1 with K2, A2 with A3, so a per-element crossing yields three
  or four items rather than six. This changes every count and makes the pilot's numbers historical;
- **cross subtree by subtree** and assemble, generating the once-scoped activities exactly once. The
  partial-run rule already exists and the pilot demonstrated it works, including its careful
  distinction between deferred and unused.

The second costs more runs and changes no numbers. The first is cheaper to run and changes what is
being measured. **Recommendation: subtree by subtree**, because the measurement runs exist to compare
two crossings of one model, and an instrument that is re-scaled between the pilot and the measurement
compares nothing.

