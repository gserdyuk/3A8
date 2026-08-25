# HW20-P — `Hotyn-W 1.0`, pilot crossing, subtrees N02 and N26 of HM19-OA1

Transcribed from the sensor's reply. `tool_uses: 0`. Contamination check: clean.

**Isolation weakness, on the record:** the run went through a general-purpose agent with the sensor
definition pasted into the task, because `.claude/agents/work-crosser.md` was written during the
session and was not yet available to the Agent tool. Isolation by instruction, verified after the
fact — not by the absence of tools.

Inputs: 17 elements of HM19-OA1 (subtrees N02 and N26), the BMS technology declaration
(`technology_declaration.md`, catalogue 1.0), parameters 3 environments / 2 test cycles / 2 UAT cycles.

**Applicability questions asked: 357** = 17 elements × 21 in-scope activities. Fixed before the run.

---

## Classification (W7)

| element | class | basis |
|---|---|---|
| N02 Platform Foundation | aggregate | children only, no own coverage |
| N69 SaaS Hosting, Tenancy & Isolation | behaviour | tenancy scoping and isolation are enforced at run time |
| N04 Performance & Scalability | statement | *"Screen loads under 2 seconds"*, *"Highly performant… high demand"* |
| N05 Availability & Resilience | statement | *"Highly available and resilient"* |
| N06 Data Platform | store | the structured platform the system holds its data in |
| N70 Security, Data Protection & Retention | statement | *"TLS 1.2 minimum…"*, *"…compliant with the Data Protection Act"* |
| N08 Growth Architecture | statement | *"Designed to grow in the future"* |
| N26 Booking Domain Core | aggregate | children only, no own coverage |
| N27 Booking Register | store | the authoritative booking records |
| N28 Booking Requirements Management | store | **not an aggregate** despite having a child: carries own coverage |
| N74 CTC Update Ingestion & Scheduling | interface | scheduled exchange with an outside system; **not an aggregate**: own coverage |
| N75 Update Classification & Downstream Propagation | behaviour | classifying and propagating happen at run time |
| N77 Merge Policy & Conflict Alerting | behaviour | "the name reads like a policy, the content is a doing" |
| N29 Supplier Inventory Store | store | uploaded inventory and pricing |
| N80 Supplier Registry | store | supplier entities |
| N81 Traveller Profile | store | person records |
| N82 Audit Trail | store | the record of who changed what and when |

Counts: aggregate 2 · behaviour 3 · interface 1 · store 7 · statement 4 · **surface 0**.

## The crossing — 94 items

Lossless compaction of the sensor's 21 per-activity tables: one row per element, the activities that
fired on it. Item ids are `activity·element`, with `·c1 / ·c2` for cycles.

| element | class | activities that fired | items |
|---|---|---|---:|
| N69 | behaviour | K1 K2 A2 A3 A4 D4 | 6 |
| N04 | statement | K3 A9 D4 | 3 |
| N05 | statement | K3 A9 D4 | 3 |
| N06 | store | K1 K2 A2 A3 A4 D4 | 6 |
| N70 | statement | K3 D4 | 2 |
| N08 | statement | K3 D4 | 2 |
| N02 | aggregate | A5×2 A6×2 A7 A8 D2 | 7 |
| N26 | aggregate | A5×2 A6×2 A7 A8 D2 | 7 |
| N27 | store | K1 K2 A2 A3 A4 D4 | 6 |
| N28 | store | K1 K2 A2 A3 A4 D4 | 6 |
| N74 | interface | K1 K2 A2 A3 A4 A10 D4 | 7 |
| N75 | behaviour | K1 K2 A2 A3 A4 D4 | 6 |
| N77 | behaviour | K1 K2 A2 A3 A4 D4 | 6 |
| N29 | store | K1 K2 A2 A3 A4 D4 | 6 |
| N80 | store | K1 K2 A2 A3 A4 G1 G2 G3 | 8 |
| N81 | store | K1 K2 A2 A3 A4 G1 G2 G3 | 8 |
| N82 | store | K1 K2 A2 A3 A4 | 5 |

By activity: K1 11 · K2 11 · K3 4 · A2 11 · A3 11 · A4 11 · A5 4 · A6 4 · A7 2 · A8 2 · A9 2 · A10 1 ·
D2 2 · D4 12 · G1 2 · G2 2 · G3 2 · **U1 0 · U2 0 · U3 0 · O1 0**.

By scope: per element 80 · per aggregate 6 · per aggregate × cycles 8 · once 0 (deferred) ·
per environment 0 (deferred).

## The `no` log — 30 answers, split by kind

The run introduced a distinction the definition did not ask for and which is worth keeping:

- **filter (15)** — the declaration's own further condition excluded it. Mechanical.
- **judgement (15)** — class and condition both matched and the applicability question was answered
  `no` on the element's content.

Filter negatives: N70, N08 against A9 (their content is not a performance or availability property) ·
N02, N26 against U1, U2, U3, O1 (no surface element inside) · N02, N26, N80, N81, N82 against D4 (no
own requirement coverage).

**Every one of the 15 judgement negatives is a store against G1, G2 or G3** — N06, N27, N28, N29, N82,
each three times. The reason given in each case: the store's content arrives at run time (CTC
ingestion, supplier upload, change events) and no reference or master data set precedes it.

Cycles do not multiply negatives: a per-aggregate × cycles activity is logged once per element.

## Demanded work

Out of scope, not absent. Every demanded item is absorbed by a once-scoped activity, and once-scoped
activities are deferred in a partial run. **0 absorbed · 0 standing alone · 0 lost**; the whole list
stays open for the whole-model crossing.

## W5 findings, verbatim in substance

- **F1 — four activities applied to nothing: U1, U2, U3, O1.** All gated on an aggregate containing a
  `surface` element, and no element in scope is a surface. The run named three obligations inside the
  scope that presuppose surfaces anyway: R66 *"Screen loads under 2 seconds"* names a screen; R37 and
  R47 have suppliers *"manually upload"*; R44 is an *"Ability to override"*.
- **F2 — no element went untouched.** All 17 are the element of at least one item.
- **F3 — N69 is a leaf that is really two things**: a delivery-model property and a run-time mechanism.
  Crossed as behaviour; the property half draws no statement realisation.
- **F4 — N29 is declared a store, but R37 and R47 describe an upload channel.** The channel a supplier
  uploads through is declared nowhere in scope, so it draws no design, implementation or contract test.
- **F5 — N77 bundles an unrelated capability**: R44, a user-facing override, sits inside merge policy
  and conflict alerting.
- **F6 — N05 bundles a property with a behaviour**: degraded-mode operation is something the system
  does, inside an element whose declared content is otherwise an availability property.
- **F7 — only two aggregates exist in scope.** N28 and N74 carry own coverage and so are not
  aggregates by rule, and the booking-requirements branch has no aggregation node of its own for test
  execution, defect resolution, regression, test data or planning.
- **F8 — `G-SEED` reaches 2 of 7 stores.** Five hold content that no seed set precedes.

## Projection onto the requirement anchor

| requirement | covering elements | items |
|---|---|---:|
| R01 | N69 | 6 |
| R04 | N27 | 6 |
| R12 | N04 | 3 |
| R13 | N05 | 3 |
| R21 | N28 | 6 |
| R31 | N74 | 7 |
| R32 | N74, N75 | 13 |
| R33 | N77 | 6 |
| R34 | N77 | 6 |
| R37 | N29 | 6 |
| R44 | N77 | 6 |
| R47 | N29 | 6 |
| R63 | N06 | 6 |
| R66 | N04 | 3 |
| R68 | N05 | 3 |
| R71 | N08 | 2 |
| R72 | N70 | 2 |
| R73 | N70 | 2 |

Rows overlap where one element covers several requirements. **59 of 94 items trace to an element that
carries requirement coverage; 35 trace to elements that carry none** — N02 (7), N26 (7), N80 (8),
N81 (8), N82 (5).

## Instrument readings — `Hotyn-W 1.0`

| reading | value |
|---|---|
| scope | partial: subtrees N02, N26 — 17 of 78 elements |
| total work items | **94** |
| items per element | mean **5.53**, min 2 (N70, N08), max 8 (N80, N81) |
| applicability questions | 357 |
| `no` answers | 30 — 15 filter, 15 judgement |
| elements untouched | 0 |
| activities unused | 4 — U1, U2, U3, O1 |
| activities deferred to the whole-model run | 17 |
| demanded items | 0 absorbed, 0 standing alone, whole list open |
