# Technology catalogue 1.4 — what each way of working obliges you to do

**Version 1.4, 2026-08-22.** Three further enumeration precedents (P-4, P-5, P-6 in §3a),
adjudicated by the author from run 24's batch-A divergences, and one applicability fix: **A9 now
applies only to behavioural statements with at least one stated measurable target** — run 24 found
the crossing generating A9 items on statements whose obligations quantify nothing (R68, R63), and
the zero case belongs in the crossing filter, not in a sizing hole. Work models crossed under 1.1
carry such items; they are priced as named zero-holes, which is arithmetically identical. Also
noted: rate table v0.1 labels `E7`'s rows "model bracket" while the pinned driver is environment
count — the values stand, the label is the table's defect, recorded there at next version.

**Version 1.3, 2026-08-22.** Adds the **enumeration precedents** to §3a — three count-by-naming
boundaries that run 23 caught as the only sources of divergence between two identical
classification runs, adjudicated by the author once for everybody. No activity, scope, class or
threshold changed; work models and sizes produced under 1.2 remain valid, and the precedents bind
from the next classification run onward.

**Version 1.2, 2026-08-21.** Adds §3a — size classes and drivers (W10) — so that `Hotyn-D 2.0` can
price from a rate table (`docs/proposal_rate_card.md`). **Nothing in 1.2 changes which work items
exist**: applicability, scopes and element classes are untouched, so work models built under 1.1
(runs 21–22) remain valid inputs and their counts are unaffected. The author's four decisions of
2026-08-21 are recorded inline in §3a.

**Version 1.1, 2026-08-20.** One change from 1.0, forced by the pilot crossing (run 20): the scope
formerly written **per aggregate** is now **per parent**. Everything else is unchanged. Run 20 was
performed under 1.0 and its counts are 1.0 counts.

The pinned input `Hotyn-W` cannot run without (`docs/proposal_product_model.md` §5, W1). A **technology**
here is a declared way of building or assuring the product; a **catalogue entry** names one and lists
**the activities it mandates**. A **declaration** picks one entry per dimension.

**The activity list belongs to this document, not to a run.** If a run may decide what a technology
implies, the free parameter is back and the whole three-step chain is decorative. Extending this
catalogue is a separate, deliberate act — like revising a requirement list.

Scope of version 1.0: **only the choices BMS needs**, plus, in each dimension, one alternative that is
not declared. A dimension with a single choice cannot be varied, and varying the declaration while the
product model is held fixed is the falsification test the whole design turns on
(`proposal_product_model.md` prediction 2).

---

## 1. Two rules this catalogue needs and the proposal does not yet state

Writing it surfaced two holes. Both are recorded here as proposed amendments and are used below.

**W7 — Applicability is judged against a fixed set of element classes.** W3 asks, for every product
element and every mandated activity, *does this activity apply to this element?* If the run answers
from the element's name, the answer is free association. Every element is therefore first assigned
**one class** from the closed list in §2, and every activity states the classes it applies to. The run
classifies; it does not decide what an activity means.

The classification is still a judgement, and it is now the place where this step's freedom sits —
which is why W3 already requires the negatives to be logged. Log the class too.

**W8 — Every activity declares its scope, and scope is not the run's to choose.** "Write test cases"
is per element; "write the test strategy" is once for the whole model. If the run decides which,
the size of the work model is set by the run and prediction 1 is unscoreable. The five scopes are in
§3.

**W9 — A refusal is either a filter or a judgement, and the run says which** *(added in 1.1, invented
by the pilot run before it was a rule).* A `no` where the declaration's own further condition excluded
the element — no surface in the subtree, no requirement coverage — is a **filter**: mechanical, and two
runs cannot differ on it. A `no` where class and condition both matched and the run still declined is a
**judgement**. Only judgements measure this step's freedom, and mixing the two hides how much of it
there is. Run 20 logged 30 refusals: 15 filter, 15 judgement, and all 15 judgements were one question
asked five times.

**A third hole, recorded but not closed: §5's six dimensions contain no way to build anything.**
Assurance, acceptance, delivery process, environments, data and documentation between them mandate no
construction, so the crossing in W3 would generate a work model with testing and no implementation.
This catalogue therefore adds a seventh dimension, **construction**, and an eighth, **security and
compliance assurance**, for work that is neither functional testing nor acceptance. §5 says "at
minimum", so this extends rather than contradicts it.

---

## 2. Element classes (W7)

Assigned to every element of the product model, exactly one each, from its **declared content** at
closure — not from its name.

| class | the declared content is | BMS examples |
|---|---|---|
| **behaviour** | something the system does at run time | requirement-match ranking · merge policy engine · automated booking execution |
| **surface** | something a user meets: a screen, a portal area, a printable document | booking detail & status view · prioritisation rule editor · printable reservation |
| **interface** | an exchange with a system outside this one | CTC integration · UPSA integration · SSO integration · SMS gateway connector |
| **store** | data the system holds and is responsible for | authoritative booking registry · supplier & location master data · configuration store |
| **statement** | a property, policy or constraint rather than a run-time behaviour | TLS 1.2 · data protection compliance · screen load under 2 s · high availability |
| **aggregate** | its children, and nothing of its own | notification subsystem · reporting subsystem · employees portal |

Two notes that keep the classification honest:

- **A leaf is never an aggregate**, and after M7 normalisation an aggregate always has two or more
  children. M10 says a leaf is a function; if a leaf looks like an aggregate, that is an M10 report on
  the product model, not a class.
- **`statement` is not a synonym for "hard to place".** A statement element generates real work — a
  decision is taken, a configuration is made, evidence is kept — but never the work of building a
  feature. Misclassifying a behaviour as a statement is the cheapest way to lose work in this step,
  so every `statement` classification is logged with the sentence from the element's content that
  justifies it.

---

## 3. Activity scopes (W8)

| scope | one work item per | multiplied by |
|---|---|---|
| **once** | the whole work model | — |
| **per element** | product element of the named classes | — |
| **per parent** | element that has children — a position in the tree, not a class | — |
| **per environment** | environment named in the declaration | — |
| **× cycles** | modifier on either of the two above | the cycle count named in the declaration |

**Why `per parent` and not `per aggregate`** *(1.1)*. Version 1.0 scoped test execution, defect
resolution, regression, test data and planning to the **class** `aggregate` — children and nothing of
its own. Under `Hotyn-M 1.1` coverage is declared at the element that realises it, so an internal node
that realises something of its own is not of that class, and drew no per-aggregate work however large
its subtree. On the run-19 model that excluded 5 of 18 elements with children, on a ground unrelated to
whether they aggregate anything. Tree position and declared content are two questions and were being
answered by one word.

Cycle counts are **policy parameters of the declaration**, not estimates: "two test cycles" is a
choice about how you work, the same kind of thing as "UAT rather than direct to production". A
parameter that could only be known from a duration or an effort figure may not enter a declaration —
that would make the technology an output of the estimate.

---

## 3a. Size classes and drivers (W10) — added in 1.2

**W10 — Every work item's size is a class from a pinned driver, and prices live in a rate table,
not in a run.** A run assigns each item a size class — **S / M / L / XL** — by **counting named
things**; person-day values per (activity × element class × size class) live in `rate_table.md`, a
pinned input with per-row provenance. No engine of this generation produces an effort figure.

Six rules:

- **One size class per element, assigned once, reused everywhere.** The class is a property of the
  **element** — a leaf, or an internal node carrying own content; a pure aggregate is never sized.
  Every per-element activity uses the element's class by default; activities whose cost scales
  differently override with their own driver below, each with its reason.
- **Count by naming.** A size justification is an **enumeration**, not a number: "M — 3 actions:
  rank offers, re-rank on change, explain ranking." Two runs that disagree disagree on a visible,
  arguable list.
- **An uncountable driver is a defect report, not a guess** — the element is reported
  *unsizeable, model defect (M10)* and gets no class.
- **Position-derived sizes are computed, never judged** — per-parent and once-scoped activities take
  their class from tree arithmetic.
- **Thresholds live here.** Changing one is a version bump.
- **Drivers count scope, never effort.** No driver may reference difficulty, risk, novelty or time —
  those belong to the table's O–P width and to the reference class.

### Element size classes

Counted from the element's declared content plus own coverage:

| element class | what is enumerated | S | M | L | XL |
|---|---|---|---|---|---|
| behaviour | distinct actions (verb on object) the declared content names | 1 | 2–3 | 4–6 | ≥7 |
| interface | operations consumed or exposed; a named protocol/auth concern counts as one | 1 | 2–4 | 5–8 | ≥9 |
| surface | distinct user tasks the surface serves | 1 | 2–3 | 4–6 | ≥7 |
| store | entity kinds the store is responsible for | 1 | 2–3 | 4–6 | ≥7 |
| statement (both kinds, below) | systems or components the property constrains | 1 | 2–4 | 5–8 | ≥9 |
| aggregate | — never sized: no per-element construction; its work is position-derived | | | | |

**XL is a price and a signal at once** *(author, 2026-08-21)*: an XL element is priced as XL **and**
reported as a probable M10 coarseness finding. The class prevents silent under-pricing; the report
sends the model back for splitting. Neither substitutes for the other.

**`statement` splits into two sizing kinds** *(author, 2026-08-21)*: **`statement-compliance`** — the
content names a standard, configuration or policy and no run-time scenario (TLS 1.2, data-protection
regime); **`statement-behavioural`** — the content entails run-time behaviour (high availability with
degraded mode, screen load under 2 s). The kind is logged with the sentence that justifies it. This
is a **sizing subclass only**: W7's six element classes are unchanged, so existing work models remain
valid. Behavioural statements with measurable targets additionally draw A9, as before.

### Default use of the element class

`K1` · `K2` · `K3` · `A2` · `A3` · `A4` · `F1` · `F2` · `F3` · `F4` · `F6` use the element's class
as is.

### Activity-specific overrides (the exceptions, each with its reason)

| id | driver enumerated | S | M | L | XL | why the default is wrong |
|---|---|---|---|---|---|---|
| A8 | store + interface elements in the parent's subtree | ≤1 | 2–3 | 4–6 | ≥7 | data volume follows stores and feeds, not the parent's own content |
| A9 | measurable targets the statement names (thresholds, SLOs) | 1 | 2–3 | 4–6 | ≥7 | one property may carry several distinct measurements |
| A10 | uses the interface element's class | | | | | same count, listed for completeness |
| D4 | requirement ids in the element's own coverage | 1 | 2–3 | 4–6 | ≥7 | elaboration scales with obligations, not implementation size |
| G1–G3 | entity kinds in the store needing pre-load | 1 | 2–3 | 4–6 | ≥7 | only seeded entities cost; run-time-filled ones do not |
| U1–U3 | surface elements in the parent's subtree | 1 | 2–3 | 4–6 | ≥7 | UAT scales with screens under acceptance |
| O1 | surface elements in the parent's subtree | 1 | 2–3 | 4–6 | ≥7 | same |
| S2–S3 | surface + interface elements in the crossed model | ≤5 | 6–12 | 13–25 | ≥26 | attack surface, not model size |

### Position-derived classes — computed, no judgement

| scope | class comes from | S | M | L | XL |
|---|---|---|---|---|---|
| per parent (`A5`, `A6`, `A7`, `D2`) | leaf elements in the parent's subtree | ≤3 | 4–8 | 9–14 | ≥15 |
| once (`A1`, `D1`, `D3`, `D6`, `E2`, `E4`, `E6`, `F5`, `O2`, `O3`, `S1`, `U4`) | elements in the crossed scope — the model bracket | ≤30 | 31–90 | ≥91 | — |
| per environment (`E1`) | fixed mapping: dev = S, stage = M, prod = L | | | | |
| `E3`, `E7` | environments in the declaration | 1 | 2 | ≥3 | — |

The model bracket keeps three classes: it is arithmetic, no judgement is involved, and no model near
the XL scale exists; extend it when one does. **`U4` is bracket-sized** (author, 2026-08-21 — not
single-size), and **`D2`/`D3` stay bracket-sized**: the rate-row alternative for the delivery
dimension (proportional, like C3) stays recorded in §7 as that dimension's known weakness, to be
revisited on evidence from the first `Hotyn-D 2.0` runs, not before.

### Single-size activities

One row in the table, no classes: `O4` release notes · `U1d` production verification checklist.

### Cycles

Unchanged: cycle counts are declaration parameters. A driver sizes **one cycle**.

### Enumeration precedents — adjudicated by the author, 2026-08-22 (added in 1.3)

Case law for count-by-naming. Run 23's two identical runs diverged on exactly three boundaries, each
pre-named by both runs as the arguable reading; decided here once, so no later run re-litigates them.

- **P-1 — a named delivery channel is a protocol concern.** An interface whose obligation names a
  delivery channel counts the channel alongside the operation: *"notifications via email"* = the
  dispatch operation + the email channel = 2. A channel carries its own integration substance
  (gateway contract, formats), and counting it S equals asserting "one operation, no protocol".
- **P-2 — a name token counts only when no counted obligation already covers its action.**
  *"ranking"* in "Prioritisation (ranking & recalculation)" is the umbrella over the counted
  matching and rule-evaluation obligations — not counted. *"normalised"* and *"cached"* in a search
  element are covered by no obligation — counted. The test is coverage, not position in name or text.
- **P-3 — slash-separated outcomes are distinct actions.** *"Accepted/Rejected"* names two
  transitions, not one; R25-style stage lists count by outcome. An XL reached this way still fires
  the standing rule: priced as XL **and** reported as a probable M10 coarseness finding.

Adjudicated 2026-08-22 from run 24's batch-A divergences (added in 1.4):

- **P-4 — the kind tie-break: run-time wins.** A statement whose covered obligations mix kinds is
  `behavioural` when **any** covered obligation entails run-time behaviour ("high-performing … for
  large volumes", "multi-tenant service" with enforced isolation), `compliance` only when none does.
  This pins the rule run 23's pair already used on N16 and makes the run-time readings of N69 and
  N06 canonical.
- **P-5 — an unnamed catch-all is not a named thing.** *"and other details"* names no kind and
  counts nothing; count-by-naming already implied it, now it is precedent. (Three of four run-24
  readings of the phrase already excluded it.)
- **P-6 — a stated cardinality without named members is not an enumeration.** *"three amendment
  origins"* is a number, not a list; an element whose declaration counts things it never names is
  **unsizeable — model defect (M10)**, never sized on a guessed reading. The stricter of run 24's
  two readings, chosen because the refusal is also the defect signal the model owner needs.

### Contamination note

The drivers and thresholds were authored with knowledge of run-22 outputs. They count scope, not
effort, so the anchoring surface is small — and the check is cheap: **the rate-table author
(`Hotyn-K`, gap-blind) sees the drivers and may object to any threshold as un-priceable before
writing values.** An objection is a finding about the drivers, not about the table.

---

## 4. Dimension 1 — construction

### `K-BESPOKE` — bespoke web application on a mainstream stack *(declared for BMS)*

| id | activity | scope | applies to | note |
|---|---|---|---|---|
| K1 | element design | per element | behaviour, surface, interface, store | how this element is built and what it promises its neighbours |
| K2 | element implementation | per element | behaviour, surface, interface, store | includes the persistence for a `store` and the adapter for an `interface` |
| K3 | statement realisation and evidence | per element | statement | the decision, the configuration that enforces it, and what shows it holds |

**No assembly or integration activity, deliberately.** `Hotyn-D` adds C3 — 20% of the leaf effort
beneath every aggregation node — and an assembly activity here would be the same work twice.

### `K-PACKAGE-CONFIG` — configuration of a commercial booking package *(not declared)*

| id | activity | scope | applies to | note |
|---|---|---|---|---|
| K1p | fit assessment against package capability | per element | behaviour, surface, store | the answer is configure, extend, or accept a gap |
| K2p | configuration | per element | elements assessed as configure | |
| K3p | extension development | per element | elements assessed as extend | |
| K4p | package installation and baseline set-up | once | | |
| K5p | statement realisation and evidence | per element | statement | |

Present so the construction dimension can be varied. Not costed, not recommended, not assessed.

---

## 5. Dimension 2 — assurance

### `A-TB` — test-based assurance *(declared for BMS)*

| id | activity | scope | applies to | note |
|---|---|---|---|---|
| A1 | test strategy | once | | what is tested, at which levels, against what exit criteria |
| A2 | test design | per element | behaviour, surface, interface, store | the cases, not their execution |
| A3 | unit and component test implementation | per element | behaviour, surface, interface, store | |
| A4 | code review | per element | behaviour, surface, interface, store | verification by reading; belongs to assurance, not to construction |
| A5 | test execution | per parent × cycles | | |
| A6 | defect resolution | per parent × cycles | | fixing and retesting what execution found |
| A7 | automated regression suite | per parent | | |
| A8 | test data preparation | per parent | | |
| A9 | performance and availability testing | per element | statement elements whose content is a performance, capacity or availability property **and states at least one measurable target** *(condition added in 1.4)* | this is how an NFR statement gets tested rather than merely asserted; a property with no stated target is a crossing filter refusal and an open question for the client, not a test item |
| A10 | interface contract testing | per element | interface | against the external system or a stand-in for it |

### `A-FV` — formal verification *(not declared; it is the falsification test)*

| id | activity | scope | applies to | note |
|---|---|---|---|---|
| F1 | formal specification of the element | per element | behaviour, interface, store | |
| F2 | proof obligation derivation | per element | behaviour, interface, store | |
| F3 | proof construction and checking | per element | behaviour, interface, store | |
| F4 | specification review | per element | behaviour, interface, store, surface | replaces A4 |
| F5 | verification report | once | | |
| F6 | validation of surfaces by inspection | per element | surface | screens are not provable; this is the honest residue |

Prediction 2 registers that swapping `A-TB` for `A-FV`, with the requirement list and the product model
held fixed, must move the estimate by more than ×1.3. **The swap is structural, not a re-pricing**: it
removes execution cycles, defect cycles, regression and test data, and it adds three per-element
activities. If the estimate does not move, the instrument is measuring the document.

---

## 6. Dimension 3 — acceptance

### `C-UAT` — staged user acceptance with sign-off *(declared for BMS)*

| id | activity | scope | applies to | note |
|---|---|---|---|---|
| U1 | UAT scenario preparation | per parent | parents whose subtree contains at least one `surface` element | written with the client, in the client's language |
| U2 | UAT support | per parent × cycles | same | the supplier's side of a cycle the client runs |
| U3 | UAT defect triage and fix | per parent × cycles | same | |
| U4 | acceptance record and sign-off | once | | |

### `C-DIRECT` — direct to production, no acceptance stage *(not declared)*

| id | activity | scope | applies to | note |
|---|---|---|---|---|
| U1d | production verification checklist | once | | |

---

## 7. Dimension 4 — delivery process

### `D-TEAM` — one team, planning and reporting ceremonies *(declared for BMS)*

Matches `assumptions.md` A3: 1 PM/BA, 1 part-time architect, 3–4 developers, 1 QA, 1 part-time DevOps.

| id | activity | scope | applies to | note |
|---|---|---|---|---|
| D1 | mobilisation and set-up | once | | |
| D2 | planning and tracking | per parent | | the subsystem's plan; the project's plan is D1 and D3 |
| D3 | status reporting and client communication | once | | |
| D4 | requirement elaboration | per element | any element covering at least one requirement | the business analysis run 18 found had no home anywhere in the model |
| D6 | risk and dependency management | once | | |

### `D-DISTRIBUTED` — two sites, formal hand-offs *(not declared)*

Same five activities plus D7 *cross-site coordination*, per aggregate. Present so the dimension varies.

**This is the weakest dimension in the catalogue, and it is worth saying why.** Coordination work is
naturally proportional to everything else, and Hotyn's rule — every item traces to (element, activity)
— fits proportional work badly. D2 attaches it to aggregates because that is the closest thing to a
unit of coordination the product model contains. Lytin met the same difficulty and answered it with a
rate (C3, 20%). If D2 turns out to behave like a rate in disguise, that is a finding about this
dimension and not about the project.

---

## 8. Dimension 5 — environments

### `E-DSP` — dev, stage and production *(declared for BMS)*

Matches A1, which includes environment set-up in scope.

| id | activity | scope | applies to | note |
|---|---|---|---|---|
| E1 | environment provisioning | per environment | | |
| E2 | build and deployment pipeline | once | | |
| E3 | promotion procedure, defined and rehearsed | once | | **absorbs demanded work R70** |
| E4 | configuration management and version control set-up | once | | **absorbs demanded work R69** |
| E6 | production cutover | once | | run 18 flagged go-live cutover as work nobody could price |
| E7 | hosting set-up: tenancy, capacity, runtime | once | | the part of demanded work **R02** that survives A1 |

### `E-SINGLE` — one environment *(not declared)*

E1 once, E2 once. No promotion, no cutover.

---

## 9. Dimension 6 — data

### `G-SEED` — reference and master data seeded, no legacy migration *(declared for BMS)*

| id | activity | scope | applies to | note |
|---|---|---|---|---|
| G1 | seed data set specification | per element | store | what must be in it before the system is usable |
| G2 | seed data preparation and load | per element | store | |
| G3 | load reconciliation | per element | store | |

### `G-MIGRATE` — migration from a predecessor system *(not declared)*

| id | activity | scope | applies to | note |
|---|---|---|---|---|
| G1m | source profiling | once | | |
| G2m | field mapping specification | per element | store | |
| G3m | extraction and transformation | per element | store | |
| G4m | load and reconciliation | per element | store | |
| G5m | migration rehearsal | × cycles | | |

**Both models in run 18 flagged data migration as work they could not price.** With this dimension
declared as `G-SEED`, migration work is *absent by declaration* rather than absent by oversight — and
one edit to the declaration produces all of it. That is the difference this step was built for.

---

## 10. Dimension 7 — documentation

### `U-OPS-USER` — operational and user documentation *(declared for BMS)*

Matches A2, which requires basic operational and user documentation at done.

| id | activity | scope | applies to | note |
|---|---|---|---|---|
| O1 | user documentation | per parent | parents whose subtree contains at least one `surface` element | |
| O2 | operational runbook | once | | |
| O3 | support handover pack | once | | the part of demanded work **R03** that survives A1 |
| O4 | release notes | once | | |

### `U-NONE` — no documentation deliverable *(not declared)*

No activities. Present because "none" is a real choice and its cost is worth being able to see.

---

## 11. Dimension 8 — security and compliance assurance

### `SA-PENTEST` — external penetration test and remediation *(declared for BMS)*

| id | activity | scope | applies to | note |
|---|---|---|---|---|
| S1 | security review of the design | once | | |
| S2 | penetration test engagement | once | | |
| S3 | remediation of findings | once | | |

Declared because R72 and R73 put authenticated traffic and personal data under the Data Protection Act
in scope, and because run 18 flagged penetration testing as unpriced work. It is a **scope decision and
it is visible**: switching to `SA-NONE` removes exactly three items and nothing else.

### `SA-NONE` *(not declared)*

No activities.

**Accessibility conformance is not a dimension in version 1.0.** Run 18 flagged it, no requirement
demands it, and inventing a dimension to cover it would be the same invention the design exists to
prevent. It is named here so its absence is on the record.

---

## 12. Double-count guards

Three places where the same work could be produced twice, and the rule for each.

1. **Integration.** No activity assembles or integrates elements. `Hotyn-D`'s C3 prices integration at
   every aggregation node. An activity that did it too would double it.
2. **Demanded work.** Where a catalogue activity covers an item on the demanded-work list, W6 applies:
   the item is recorded **once**, in the technology-derived branch, and the demanded entry is marked
   *accounted for at that activity*. The absorbing activities are marked in §8 and §10 above.
3. **Verification.** Everything whose purpose is to establish that the product is right lives in the
   assurance dimension — code review included. Construction builds; assurance checks. Otherwise the
   assurance swap in prediction 2 would leave verification work behind in the construction branch and
   the falsification test would be blunted.

---

## 13. What this catalogue does not contain, on the record

- **Training.** Excluded by A1.
- **Internationalisation and localisation.** No requirement demands it; run 18 flagged it.
- **Accessibility conformance.** As above, §11.
- **Legacy data migration.** In the catalogue as `G-MIGRATE`, not declared.
- **Transition off the manual process** — parallel running, decommissioning, change management,
  in-flight bookings. Twenty `Lytin` runs and four `Hotyn` runs failed to generate it, and this
  catalogue does not generate it either: no dimension mandates it and no requirement demands it. **If
  that work is to appear, it must enter as a requirement.** This is the design's known, registered,
  reproducible failure and it is not fixed here.

---

## 14. Registered before the crossing runs

Written down now so it can be scored rather than rationalised.

**Measured, 2026-08-20 (run 20, under 1.0).** A pilot crossing of 17 elements produced 94 items —
**5.53 items per element** — against 357 applicability questions. Projected: ~450 items for a 78-element
model, ~730 for a 129-element one. The registered band below was written for a 109-element model and
the projection lands inside it. The `per parent` change in 1.1 raises these numbers, by roughly the
ratio of parents to class-aggregates in the model being crossed.

**The cardinality of the crossing is set by this document, not by the run.** For a model of the size
run 18 produced — 109 elements, of which about 86 leaves and 23 aggregates — the declared BMS
technology yields on the order of **650–750 work items**: roughly 450 from per-element activities,
220 from per-aggregate activities and cycles, and some 30 once-and-per-environment items. Any run
whose work model is far from that has either classified elements differently or answered W3's
applicability question differently, and the log of `no` answers says which.

**The risk this creates, named before it bites.** `Hotyn-D`'s C1 forbids a leaf under 1 pd. Per-element
activities on a fine product model will produce many items that are honestly worth a fraction of a
day, and the floor would round every one of them up. If that happens, the answer is either to lift the
floor for technology-derived items or to coarsen the per-element activities here — **and the choice
must be made once, in a document, not inside a run.**

---

## 15. Pin

Version 1.0, 2026-08-20. Recompute with:

    tr -d '\r' < docs/technology_catalogue.md | md5sum

Declarations that consume it: `examples/BMS/technology_declaration.md`.
