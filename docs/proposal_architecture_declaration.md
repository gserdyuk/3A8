# Proposal — the architecture declaration: a property is realised by a mechanism, and the mechanism is an input

Status: **design, nothing implemented.** Written 2026-09-15 at the author's request, from the
record only. The form of the mechanism catalogue (§4) is **deliberately left open** — the author will
settle it in discussion; this document fixes what the declaration must do, not what it looks like.
Predictions in §7 are registered before any run. Prior art this generalises:
`docs/parked_architecture_as_rate_step.md` (2026-08-06: a boundary is an input a run may not choose),
`docs/proposal_product_model.md` §3 (the technology declaration as a pinned input) and `findings.md`
§12e (a large opaque transformation is cut into seams with a named artefact at each).

---

## 1. The claim

**Between "requirements" and "the thing to be built" there is a step the chain does not perform: the
architecture, and in particular the part of it that non-functional requirements induce.** The chain
as it stands is

```
requirements ──split──▶ product obligations ──Hotyn-M──▶ product model ──Hotyn-W (× technology)──▶ work model ──Hotyn-D──▶ classes ──table──▶ number
```

The author's chain, stated 2026-09-15, is *requirements (structured, functional and non-functional)
→ architecture (structure from the NFRs, functions distributed over it) → module decomposition
(may coincide with the previous step) → implementation steps (the WBS)*. Laid over the pipeline:

| author's step | what exists | status |
|---|---|---|
| structured requirements | the pinned lists, split product / work | flat by design; the run builds its own tree in the skeleton phase (M4) |
| **architecture: NFR → structure** | **no artefact** | a property-type obligation becomes a leaf of class `statement`, which the crossing prices as decision, configuration and evidence — never as construction |
| module decomposition | the product model: a leaf is one thing to be built (M2 v2.1) | coincides with the previous step, as the author suspected |
| implementation steps, WBS | the work model = product model × technology declaration | exists; the declaration is what turns modules into steps |

One step is missing, and it is the one that turns a property into the things that realise it. The
remedy proposed is the same shape as the remedy that closed the technology hole in August: **not a new
engine, but a pinned input** — an *architecture declaration* — consumed by `Hotyn-M` through the
input it already has and has never used, *existing structure to start from*.

## 2. What the record shows

The mechanism is visible in the raw SAS records, and it is not a sensor defect: the sensors did what
the rules say.

**When an obligation names components, the model builds them.** NFR-2 names data marts, a
transactional store and near-real-time latency. Run 44 (both orders) produced a transactional store
schema, a non-transactional read store and a near-real-time feed between them — three constructible
leaves, classes `store` / `store` / `behaviour`, priced by the crossing as design, build, migration
mapping, ETL, load and reconciliation (`HW45-A1`: 23 work items traced to NFR-2).

**When an obligation states a property, the model builds a statement about it.** NFR-8 (99.9%
availability, a failover process developed and tested, failover monitoring) produced in `HM44-OA1`:

| leaf | name | class at crossing | work generated |
|---|---|---|---|
| A-145 | High-availability design to the 99.9% level | `statement` | K3 statement realisation and evidence · D4 · **A9 availability test** (the one A9 item of 24 statements) |
| A-146 | Failover process design, needs identified, test procedure defined | `statement` | K3 · D4; A9 refused as a **filter** — no measurable target |
| A-147 | Failover monitoring with administrator notification | `behaviour` | K1, K2, A2… — a real thing |

The obligation is reported **whole**, honestly: the run says in its own words that *"the failover
process design and its test procedure are artefacts; the act of running the test is work and is not in
this model."* What is nowhere is what an architect would write first: the redundant deployment, the
replicated database, the load balancer, the health checks, the second site — the *mechanism* by which
99.9% is achieved. Its cost is the cost of a design statement plus one test.

The same pattern: NFR-6 cloud-ready → A-142 "Cloud-readiness design statement" (`statement`, K3 +
D4, A9 filter). NFR-7's user population and concurrency → A-144 "design target" (`statement`).
NFR-3 claims-based identity → A-137 "authentication boundary statement" plus A-135/A-136, which are
constructible because NFR-3 itself names an integration. Run 44 collected **eleven design statements
under one posited node** (`S-01.3 Solution-level design statements`), and the run-45 record notes
that this subtree "receives K3 and D4 and nothing else". Twenty-four of 246 elements are statements.

**The gaps the diagnostician finds are of the same kind.** On BMS, two instruments across six runs
converged on the same seven holes: *no store for bookings — every behaviour writes to something nobody
builds*; *nothing prices the six subtrees meeting each other* (`run22`). On SAS the calibration step
had to add, from outside the chain, "a failover and backup/DR exercise" and "a load test against the
five response-time targets" (`estimate_SAS_2026-09-08.md` §3). These are not technology-derived
work, which `Hotyn-W` now generates; they are **structure the product needs that no obligation names
and that completion (M6) — "the one phase with no external bound" — was left to invent.**

**The FaxRxTx stage that the chain under-priced ×8.5 is the concept stage** — the design act itself.
That is adjacent evidence, not the same hole (§5), but it points the same way: the chain has no place
where architecture happens, neither as a structure nor as work.

## 3. Design

### AD1 — The architecture declaration is a pinned input, written before any run

A file per case, `architecture_declaration.md`, of the same standing as `technology_declaration.md`:
approved by the author, md5 recorded, built from the pinned lists and the case profile **only**, and
written by someone who has seen **no estimate and no product model of the case** (the gap-blind
discipline of `Hotyn-K` applies: a declaration written in sight of a hole is a repair of that hole).

One row per **mechanism**: an id · the mechanism, drawn from the catalogue (§4) · the obligation ids it
realises · the elements it induces, each with a name and a class from catalogue §2
(`store` / `behaviour` / `interface` / `surface`) · a group name for the elements · the pinned source
that justifies the choice, or **"scope decision, visible"** exactly as the technology declaration does.

**Coverage of the declaration is checkable.** Every obligation of the product list whose content is a
property, policy or constraint — the ones that would become a `statement` — appears in the
declaration exactly once: with a mechanism, or with the verdict **`stays a statement`** and a one-line
reason. An obligation appearing in neither is a defect of the declaration, not a footnote (the A0
discipline, applied one step earlier).

### AD2 — The declaration contains things to be built, and nothing else

Induced elements are constructible: `store`, `behaviour`, `interface`, `surface`. The declaration may
not induce a `statement` — statements are the model's own reading of the obligation and they **stay**;
the mechanism is added beside them, it does not replace them (A-145 keeps its A9 test; the cluster
that makes the 99.9% true is a new leaf). It may not contain work — that is the technology's — and it
carries no numbers (M8 holds for it as for every model-side artefact).

Cross-cutting structure is in scope and is the reason the author names coherence: a shared
authorisation mechanism (I-6/G-2 on SAS: "one authorisation mechanism, not one per module"), a
shared master store, an integration mechanism between subsystems (an API gateway, a bus) are
mechanisms with the product's *organisation* as their source (I-2 "three integrated modules"). This is
where "nothing prices the subsystems meeting each other" gets a leaf.

### AD3 — `Hotyn-M` consumes it as existing structure, with its own origin label

The engine already accepts "optionally an existing structure to start from" and has never been given
one. The declaration enters through that door, with four rules:

- **Declared elements are leaves with origin `declared`** — a fourth label beside `posited`,
  `accreted`, `derived`, never changed, and counted separately in the instrument readings. Like every
  leaf they are never deleted and never moved.
- **A declared leaf carries the obligation ids the declaration gave it** and may gain more during
  accretion; accretion may give the verdict `covered` against a declared leaf exactly as against an
  accreted one.
- **The declaration's group names are posited nodes the run must include** in its skeleton. The run
  posits the rest of the skeleton as before; grouping freedom above the declared nodes is unchanged
  (it is already the least-agreed part of step 1, Jaccard 0.31–0.41, and this adds nothing to it).
- **Completion (M6) may not derive what the declaration already induced.** A derived leaf whose
  trigger is a declared leaf is legal; a derived leaf that duplicates a declared one is a defect
  report on the run.

This is a change to `Hotyn-M`'s input contract and output counts and therefore a version bump; whether
2.x or 3.0 is decided at implementation by `PIPELINE.md`'s rule, and readings with and without a
declaration are kept apart in any case.

### AD4 — The mechanism catalogue: what a mechanism induces belongs to the document, not to a run

The principle is the technology catalogue's, verbatim in spirit: *"if a run may decide what a technology
implies, the free parameter is back."* A mechanism entry names the elements it induces, by class, so
that two people declaring "active-passive failover" for two projects induce the same kinds of things.
The declaration chooses mechanisms; the catalogue says what they consist of; the run places them.

**The form of this catalogue is open** — by dimension like the technology catalogue, by quality
attribute (availability, scalability, security, observability…), or by NFR pattern — and is to be
settled with the author. What is fixed here is only what any form must satisfy: an entry induces
elements of the four constructible classes, an entry is applicable under a stated condition, and the
document is versioned like the other catalogue, with a declaration citing the version it drew from.

### AD5 — Everything downstream is untouched

`Hotyn-W`, `Hotyn-D`, the rate table and the assembly change nothing. A declared `store` is crossed,
sized and priced exactly as an accreted `store`. This is what makes the experiment in §6 clean: the
only variable is whether the structure contains the mechanisms.

## 4. What is not decided here

- **The catalogue's form** (AD4). Deferred to discussion with the author, in Russian.
- **Who writes the declaration for a case.** Today a human, gap-blind. Whether a sensor can produce
  a candidate declaration is a separate question with its own measurement, and it is not asked here:
  a declaration is a pinned input precisely so that a run does not choose it.
- **Whether the seeded model's grouping spread rises or falls.** The declaration pins some nodes and
  leaves; it may make the skeletons more alike or push the free grouping elsewhere. Measured, not
  assumed (§7, prediction 4).

## 5. What this proposal does not fix, and names so it is not confused with it

**The act of architecting as work.** The catalogue has `K1 element design` per element and `S1
security review of the design` once; it has **no once-scoped solution architecture activity**. The
FaxRxTx concept stage (17% of the fact, priced at 2%) is evidence that such an activity is missing
from the technology side. That is a catalogue amendment on the `Hotyn-W` side, not an architecture
declaration, and it should be proposed and measured on its own so the two effects are not summed
into one unattributable move.

**The seam between statement and mechanism is not the only place work hides.** The rate table's level
(×1.38–×1.50 on re-sampling), team grade (×2–3) and the calibration rates all move the number more
than this proposal is expected to (§7). This is about *what* is priced, not about the price.

## 6. Measurement design

One case, SAS, whose pinned inputs and run-44 pair already exist. Same model alias, same processing
order, same thinking budget as run 44 (recorded in the launch record with the harness preamble size,
per the 2026-09-15 review).

1. **Write and pin** `examples/ignored/SAS/architecture_declaration.md` from the pinned list and case
   profile, gap-blind — by someone who has not read `estimate_SAS_2026-09-08.md`, `run45_work_model.md`
   or the diagnostician's list of holes.
2. **`Hotyn-M` seeded, n = 2.** Register before launch: the number of declared leaves, and the
   verdict list (mechanism / stays a statement) per NFR id.
3. **Cross, classify, price with no rate changed** (the run-42 protocol: a second structure through
   an unchanged table).
4. **Compare** against the run-44/45/47 chain on: leaves by origin · `statement` count · derived
   fraction · anchored-structure ratio between the seeded repeats · table-priced assembly ·
   which of the calibration's named additions are now inside the raw chain.
5. **Falsification form, afterwards.** Hold the requirement list and the model fixed; change one
   mechanism in the declaration (availability: active-passive failover → backup-and-restore). The
   assembly must move. If it does not, the crossing is not reading the declared elements, and the
   declaration is decorative under this catalogue — the same verdict prediction 2 of the product-model
   proposal reserves for the technology declaration.

## 7. Registered predictions

Scored only after the runs. Each names the reading that would refute it.

1. **The declaration induces 10–30 constructible leaves on SAS**, from the property-type obligations
   (NFR-3, 6, 8, 9, 10, 14, 17–20 and the organisation statements I-2, I-6). Below 10: SAS's NFRs
   are mostly component-naming already and the hole is smaller than §2 reads; above 40: the
   declaration is rewriting the product, not adding its architecture.
2. **The `statement` count does not fall** (24 in run 45; at or above 20 seeded). A sharp fall means
   the run replaced statements with mechanisms instead of adding beside them — a violation of AD2 to
   be fixed in the rule, not accepted as a reading.
3. **The table-priced assembly rises ×1.10–×1.35** against 38 118 net hours. Below ×1.05: the
   mechanisms are priced like the statements they sit beside and the table cannot see architecture —
   the result is a finding on the table, not a refutation of the hole. Above ×1.5: see prediction 1's
   upper edge.
4. **The anchored-structure ratio between the two seeded repeats is not larger than the run-44
   pair's.** Pinned leaves cannot add freedom; if the ratio grows, the run is reacting to a foreign
   structure (the §12e warning about hand-made trees) and the seeding rules in AD3 need tightening.
5. **At least two of the calibration's named additions move inside the raw chain**: the failover and
   backup/DR exercise, and per-mechanism build work that no current item carries. If none moves, the
   crossing does not reach the declared elements (see §6 step 5).
6. **The derived fraction of completion does not rise.** The declaration takes over part of what M6
   was inventing; if M6 derives more with a declaration than without, it is deriving *from* the
   mechanisms, which is legal, and the trigger column will say so — this prediction is scored on
   derived leaves whose trigger is not a declared leaf.

## 8. What comes next, in order

1. Settle the catalogue's form with the author (§4, AD4). Nothing below can start before it.
2. Write catalogue version 0.1 with only the mechanisms SAS needs plus one undeclared alternative per
   entry — the scope rule the technology catalogue 1.0 used.
3. Write and pin the SAS declaration, gap-blind (§6 step 1).
4. Bump `Hotyn-M` for the `declared` origin and the seeding rules (AD3); probe the version before
   the batch (`Hotyn-F`).
5. Run §6, score §7, write the run record. Only then decide whether the declaration becomes a
   standing input of `/3a8:estimate-product`.
