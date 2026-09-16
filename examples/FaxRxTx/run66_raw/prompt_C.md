Propose the Step C calibration corrections for the bottom-up estimate below. Everything you need is in this message; read no files.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Your engine definition's output format, sections 1–5, with the declaration before any addition. Record the engine stamps of the bottom-up chain you are calibrating (given in INPUT 3).

---

# INPUT 1 — the project description (`SYSTEM.md`, with the struck lines marked in place)

# FaxRxTx (Venali) — system and task description

**Source:** the recollections of a project participant, recorded 2026-07-17 from their
account. A real commercial project (the company Venali, a data center in Miami).
Markers of uncertainty ("it seems," "I think," "I don't remember") are kept deliberately —
they are part of the input data, not editorial defects.

**Document status:** a fixed input for the 3A8 pipeline (the analog of
BMS_extracted.md in the BMS example). The estimate must rely only on this
document + the assumption log, with no access to the actual outcome.

---

## 1. What the system does

A worldwide fax send-and-receive service: at least Europe and the USA
(possibly Australia too — the participant does not remember exactly). The user receives
incoming faxes by email and sends outgoing faxes by emailing a special address.

## 2. Fax reception (Rx)

1. Geographically distributed points of presence (PoP) are placed at
   telecom providers: they worked with BT and with others too.
   Rack space is rented at the provider, a computer with **Brooktrout**
   boards is installed to receive faxes.
2. Received faxes, as TIFF files, are sent to the company's own data center
   in Miami.
3. In the data center, depending on the user's configuration, the fax is either
   attached to the email page by page (TIFF) or converted to PDF
   and attached to the email. Conversion to PDF included digitization (OCR) —
   this was handled by OCR workers.
4. The email is sent to the user. Conversion and sending are handled by
   **workers**.

## 3. Fax transmission (Tx)

1. The user sends an email to a specific address. The email is parsed,
   the recipient's fax number is extracted from it.
2. The document from the attachment is rendered to TIFF (via, it seems, the **Black Ice**
   printer driver) and sent as an archive to a point of presence, where it
   goes into the PSTN through the Brooktrout boards.
3. A **routing** program (least-cost routing) works: it decides which
   point of presence to send the TIFF files to, so that delivery is cheaper.
4. **Renderers** — for the main document formats: DOC, XLS, PPT, PDF,
   TXT, GIF, TIFF (the list is from memory; the participant may have forgotten
   something; on the order of 8–10 formats in all).

## 4. Infrastructure and key technical decisions

- **Its own cluster of Windows 7 computers** — for rendering and other
  tasks.
- **A cluster management tool** — queue lengths and so on.
- **A job queue (MQ) was not used**: using MSMQ in the previous version of the
  system broke everything. Instead — a home-grown system of
  **watchdogs and tokens** (an unordered store) that kept the status
  of each fax and resumed work if something went wrong. Essentially — an
  orchestrator of a large number of faxes.
- **Storage:** the **Lustre** file system (from HP, it seems) — it stored both the
  fax archive and the working files. There was also a database (the DBMS is not
  specified) — the components communicated through the DB and an API.
- **Development language:** C#.
- **NOC** — an internal control center: the state of the remote nodes (PoP),
  the cluster, and the queues (where there were any).
- **User portal** — the users' website.

## 5. Scale

- The nominal target volume — **~1,000,000 faxes per 10-hour day**
  (~30/s on average). The figure 10,000,000/day (~300/s) is a **burst estimate**,
  the peak mode ~10× the nominal. Actual traffic was even below the
  nominal (the participant's clarification, 2026-07-17).
- Points of presence (PoP): **10–20**.
- Nodes in the render cluster: **~16–20** (from memory: "probably 20," "maybe 16"),
  joined by a private network.

## 6. The team's scope (the object of the estimate)

Context: by the start of the work **a working first version of the system already
existed**. The task was to redo what management did not like in the
original version. The team, meanwhile, **did not know the domain**: about
a month (possibly two) went into discussions, immersion in the subject
area, and technology selection (they studied DHT and other mechanisms).
There was no code reuse ("no reference base classes") —
only integration with the old system and coexistence for the duration
of the transition.

**What the team did (included in the estimate):**

- the stage of domain immersion and architecture/technology selection
  (they considered DHT and the like) — about 1–2 months;
- the printing (rendering) and OCR workers — OCR on a third-party library;
- the cluster itself with the delivery-control mechanism (watchdogs + tokens, §4);
- the NOC;
- the user portal;
- the inbound-email parser (the Tx path);
- saving CDR and billing data (billing itself is out of scope);
- integration tests on the real message stream with comparison of the
  results to the "old system."

**What the team did not do (out of the estimate):**

- the software on the PoPs (reception/sending via Brooktrout) — already existed;
- the routing program (least-cost) — was ready, reused;
- billing — was separate.

The components communicated through the database and an API.

**Process:** "scrum after waterfall" — first a planning phase, then
scrum. There was no hard deadline, but there was pressure. The team included
QA/PM, not just developers. [struck by the orchestrator: the calendar period of the work]

## 7. Public context (open sources, 2026-07-17)

- Venali, Inc. — Miami, hosted enterprise internet fax for Fortune 1000
  (healthcare, retail, finance/insurance).
- [struck by the orchestrator: the company's later acquisition, its price and revenue, and a dating inference for the development period]

## 8. The estimation task

Estimate the **effort in person-months** for the scope from §6 — blind,
from this document and the assumption log only.

[struck by the orchestrator: a note on where the outcome is kept]

---

[struck by the orchestrator: a closing note about an unrelated draft document]

---

# INPUT 2 — the assumption log (`assumptions.md`), verbatim

# FaxRxTx — Assumption Log (fixed before the runs, 2026-07-17)

Assumptions that close the gaps in SYSTEM.md. Agreed before estimation begins; all
runs (decomposition, reference class, …) must use the same assumptions — otherwise
their ranges are not comparable. Run input: SYSTEM.md + this file. FACT.md is not
passed into the runs.

## A1. Estimation scope
The full cycle for the "the team did" list from SYSTEM.md §6: the phase of domain
immersion and architecture/technology selection (~1–2 months) + design + development +
testing + rollout to production of the new version of the core functionality replacing
the first version.
- Included: rendering and OCR workers, the cluster with the delivery-control
  mechanism (watchdogs + tokens), NOC, the user portal, the inbound-email parser,
  saving CDR/billing data, integration tests on the real stream with comparison to the
  old system.
- **Not included:** the PoP software, the routing program, billing, post-launch
  operation, development of the first version of the system.

## A2. Definition of Done
The new system takes production traffic in prod; the integration tests on the real
stream have passed, the results agree with the old system; the old version can be
decommissioned.

## A3. Team and starting conditions
The team **did not know the domain** — immersion in the subject area, discussions,
and technology selection took ~1–2 months (included in A1). Mitigating factor: a
working v1 exists as a live reference of requirements ("like v1, but fix what we don't
like") — there is no full-scale requirements gathering from scratch, but the domain
(fax protocols, telecom, distributed delivery) is new to the team. Blended composition,
including QA and PM. The team's headcount is **not** part of the assumptions
(the volume of work is estimated, not the calendar).

## A4. Reuse
No first-version code in the new one ("no reference base classes"). Reused: the
ready PoP software, the ready routing, a third-party OCR library, rendering via a
printer driver (Black Ice-class), the existing storage infrastructure (Lustre) and the
DB as technologies — we do not develop these, only integrate with them.

## A5. Technological era
2007–2009: C#/.NET ~3.x, a Windows cluster on our own hardware, no clouds and no
ready orchestrators (what a message broker/Kubernetes would give today is written by
hand — watchdogs, tokens, delivery control). MSMQ deliberately excluded from the
negative experience of v1.

## A6. Target scale
The engineering target — **~1 million faxes / 10-hour day (~30/s on average)**,
with bursts up to ~10× (**~300/s**, "10 million/day" — an estimate of the peak mode).
A cluster of ~16–20 nodes, 10–20 PoPs. The estimate is made for designing to the
nominal with burst resilience: distribution, surviving failures, and delivery control
of every fax are mandatory properties, not options.

## A7. Rendering formats
8–10 input formats (DOC, XLS, PPT, PDF, TXT, GIF, TIFF + possibly 1–3 forgotten
ones). Each format is a separate piece of integration and stabilization work, not a
"free" extension of the list.

## A8. Organizational context
A product company (Venali), an internal rework by management decision. There is no
hard deadline, but there is pressure. The process — a planning phase, then scrum.
Approvals are internal, faster than the enterprise client of the BMS example.
Accounted for in reference class (decomposition, by construction, does not see it).

## A9. Units
Estimation in **person-months** (1 pm ≈ 21 pd ≈ 168 hours), the total effort of the
whole team, including QA/PM and the architecture-selection phase. Conversion to a
calendar duration is a separate step, not part of the runs.

---

# INPUT 3 — the bottom-up estimate: structure, totals, composition, coverage report

**Chain and engines.** Product model `HM61-1` by `Hotyn-M 2.1` (one of two repeats; the other, `HM61-2`, built 91 elements / 75 leaves against this one's 84 / 68 — ×1.10 on leaves); work model by `Hotyn-W 1.2` (4 batches, one crossing each); size classes by `Hotyn-D 2.0` (two repeats per batch); prices from a pinned rate table of **external industry norms in net task hours, uncalibrated against any outcome** (rate table v0.1-h), joined by a script; four demanded-work rows priced or refused by a gap-blind `Hotyn-K 1.1` addendum. All sensors ran on Claude Opus 5.

**Unit of every figure below: net hours of work on the task.** Leave, public holidays and sickness are outside; so are within-day overheads (meetings, coordination, interruptions) except where an activity row names them (planning and tracking, status reporting, risk management). Roles: the delivery team's hours on each activity.

**Scope and declaration the chain was built under** (a pinned technology declaration, chosen once for everybody): bespoke construction on a mainstream stack · test-based assurance, 2 test execution cycles · direct to production, **no acceptance stage** · one team with planning and reporting ceremonies · environments dev, stage, production · **reference data seeded, no legacy data migration** · operational and user documentation · **no security or compliance assurance activities**. The declared sensitivities, not priced: acceptance with UAT; migration of legacy data; no documentation; penetration testing.

**The rate table's era.** Its values are modern external norms; the project ran on the era described in A5. No era adjustment has been applied anywhere in the chain.

## Totals

| reading | element items | integration (C3: 20% of the leaf effort beneath every parent, root included) | once and per-environment items | demanded-work addendum | **total** |
|---|---:|---:|---:|---:|---:|
| sizing repeat 1 | 6577 | 3144 | 373 | 100 | **10194** |
| sizing repeat 2 | 6350 | 3023 | 373 | 100 | **9846** |

Repeat spread ×1.035; centre 10020 h. Every figure is E = (O + 4M + P) / 6 of the table's cells.

## Composition (repeat 1), as printed by the assembly script

```
=== composition, repeat 1 - per top-level subtree: element items + C3 inside the subtree
   N10    Inbound fax path                         elements  15  items   1402 h  C3    477 h  subtotal   1878 h
   N20    Outbound fax path                        elements  25  items   2020 h  C3    741 h  subtotal   2761 h
   N30    Job orchestration                        elements   5  items    424 h  C3     85 h  subtotal    508 h
   N40    Processing cluster                       elements   8  items    659 h  C3    204 h  subtotal    862 h
   N50    Storage and records                      elements   9  items    435 h  C3     87 h  subtotal    522 h
   N60    NOC                                      elements   5  items    346 h  C3     69 h  subtotal    416 h
   N70    User portal                              elements   5  items    319 h  C3     64 h  subtotal    382 h
   N80    Old system coexistence                   elements   4  items    176 h  C3     35 h  subtotal    211 h
   N90    System-wide properties                   elements   5  items    337 h  C3     67 h  subtotal    404 h
   L39    Inter-component API                      elements   1  items     65 h  C3      0 h  subtotal     65 h
   L56    First-version core function set, as repl elements   1  items      4 h  C3      0 h  subtotal      4 h
   root own per-parent items 391 h · root C3 1315 h · once/per-env 373 h
=== composition, repeat 1 - per activity (element-attached items only, hours)
   K2      1095  element implementation
   A6      1000  defect resolution
   A3       873  unit and component test implementation
   A5       669  test execution
   A7       600  automated regression suite
   K1       499  element design
   A2       447  test design
   D4       355  requirement elaboration
   D2       332  planning and tracking
   A4       224  code review
   A8       179  test data preparation
   O1       112  user documentation
   A10       99  interface contract testing
   G2        30  seed data preparation and load
   K3        30  statement realisation and evidence
   G1        22  seed data set specification
   G3        11  load reconciliation
=== once / per-environment items:
   A1 test strategy [bracket]                           E =  29.3
   U1d production verification checklist [single]       E =   8.7
   D1 mobilisation and set-up [bracket]                 E =  33.3
   D3 status reporting and client communication [bracket] E =  34.7
   D6 risk and dependency management [bracket]          E =  21.3
   E1 environment: dev [S]                              E =   9.3
   E1 environment: stage [M]                            E =  17.3
   E1 environment: prod [L]                             E =  30.7
   E2 build and deployment pipeline [bracket]           E =  30.7
   E3 promotion procedure, defined and rehearsed [3 envs] E =  17.3
   E4 configuration management and version control set-up [bracket] E =  13.3
   E6 production cutover [bracket]                      E =  30.7
   E7 hosting set-up: tenancy, capacity, runtime [3 envs] E =  46.7
   O2 operational runbook [bracket]                     E =  24.7
   O3 support handover pack [bracket]                   E =  20.7
   O4 release notes [single]                            E =   4.3
```

Demanded-work addendum (once, enters no integration base): W-F49 integration tests on the real message stream, E 62.7 h · W-F52 establishing that the old version can be decommissioned, E 37.3 h.

## Structure — the closed product model with the crossing's element classes and the two sizing repeats

84 elements: 16 parents (never sized), 68 leaves. Coverage lists obligation ids of the pinned list (F01–F47 product obligations; F48–F52 demanded work, carried in the work model, not in the product model). Size classes S / M / L / XL are counts of named things (actions, operations, user tasks, entity kinds), not effort.

| id | name | parent | origin | coverage | class | size (repeat 1 / 2) |
|---|---|---|---|---|---|---|
| N00 | FaxRxTx core system | - | posited | — | aggregate | — |
| N10 | Inbound fax path | N00 | posited | — | aggregate | — |
| N12 | Inbound conversion | N10 | posited | — | aggregate | — |
| N13 | User email delivery | N10 | posited | — | aggregate | — |
| N20 | Outbound fax path | N00 | posited | — | aggregate | — |
| N21 | Submission email intake | N20 | posited | — | aggregate | — |
| N22 | Renderer set | N20 | posited | — | aggregate | — |
| N23 | PoP dispatch | N20 | posited | — | aggregate | — |
| N30 | Job orchestration | N00 | posited | — | aggregate | — |
| N40 | Processing cluster | N00 | posited | — | aggregate | — |
| N41 | Cluster management tool | N40 | accreted | — | aggregate | — |
| N50 | Storage and records | N00 | posited | — | aggregate | — |
| N60 | NOC | N00 | posited | — | aggregate | — |
| N70 | User portal | N00 | posited | — | aggregate | — |
| N80 | Old system coexistence | N00 | posited | — | aggregate | — |
| N90 | System-wide properties | N00 | posited | — | aggregate | — |
| L01 | PoP registry: served PoPs and their reach | N90 | accreted | F01,F38 | store | M / M |
| L02 | Incoming-fax email delivery to user | N13 | accreted | F02,F05,F10 | behaviour | L / L |
| L03 | Submission address mailbox receiver | N21 | accreted | F03 | interface | M / M |
| L04 | PoP inbound TIFF receiver | N10 | accreted | F04,F38 | interface | M / S |
| L05 | Delivery-mode selector per user configuration | N12 | accreted | F05 | behaviour | L / L |
| L06 | Page-by-page TIFF attachment packager | N12 | accreted | F05 | behaviour | L / L |
| L07 | TIFF-to-PDF converter | N12 | accreted | F05,F06 | behaviour | L / L |
| L08 | OCR step within PDF conversion | N12 | accreted | F07 | behaviour | S / S |
| L09 | Third-party OCR library adapter | N12 | accreted | F08 | interface | S / S |
| L10 | OCR worker process | N12 | accreted | F09 | behaviour | S / S |
| L11 | Conversion worker process | N12 | accreted | F11 | behaviour | M / M |
| L12 | Email sending worker process | N13 | accreted | F11 | behaviour | M / M |
| L13 | Submission email parser | N21 | accreted | F12 | behaviour | S / S |
| L14 | Recipient fax number extractor | N21 | accreted | F13 | behaviour | S / S |
| L15 | Attachment-to-TIFF render path | N22 | accreted | F14,F18 | behaviour | XL / S |
| L16 | Black Ice-class printer driver adapter | N22 | accreted | F15 | interface | M / M |
| L17 | TIFF archive packager | N23 | accreted | F16 | behaviour | M / M |
| L18 | PoP outbound handoff | N23 | accreted | F16,F38 | interface | S / S |
| L19 | Least-cost routing program exchange | N23 | accreted | F17 | interface | S / S |
| L20 | DOC renderer | N22 | accreted | F18,F19 | behaviour | S / S |
| L21 | XLS renderer | N22 | accreted | F18,F19 | behaviour | S / S |
| L22 | PPT renderer | N22 | accreted | F18,F19 | behaviour | S / S |
| L23 | PDF renderer | N22 | accreted | F18,F19 | behaviour | S / S |
| L24 | TXT renderer | N22 | accreted | F18,F19 | behaviour | S / S |
| L25 | GIF renderer | N22 | accreted | F18,F19 | behaviour | S / S |
| L26 | TIFF renderer | N22 | accreted | F18,F19 | behaviour | S / S |
| L27 | Further-format renderers, unnamed in source | N22 | accreted | F19 | behaviour | unsizeable / unsizeable |
| L28 | Windows cluster node host | N40 | accreted | F20,F39 | behaviour | M / M |
| L29 | Queue-length view | N41 | accreted | F21,F34 | surface | S / S |
| L30 | Node state view | N41 | accreted | F21,F33 | surface | S / S |
| L31 | Node control: take out, put back, redistribute | N41 | accreted | F21 | behaviour | M / M |
| L32 | Watchdog-and-token store with per-fax status | N30 | accreted | F22,F23,F25,F46 | store | M / M |
| L33 | Watchdog processes | N30 | accreted | F23,F24,F45 | behaviour | M / M |
| L34 | Stalled-job resumption | N30 | accreted | F24,F45 | behaviour | M / M |
| L35 | Job dispatcher: token claim and hand-out to workers | N30 | accreted | F25,F44 | behaviour | M / M |
| L36 | Fax archive store on Lustre | N50 | accreted | F26 | store | S / S |
| L37 | Working-file area on Lustre | N50 | accreted | F27 | store | S / S |
| L38 | System database schema | N50 | accreted | F28,F29 | store | unsizeable / unsizeable |
| L39 | Inter-component API | N00 | accreted | F29 | behaviour | M / M |
| L40 | Common C#/.NET codebase and shared libraries | N90 | accreted | F30 | statement | M / M |
| L41 | NOC console | N60 | accreted | F31,F33,F34 | surface | M / M |
| L42 | PoP state view | N60 | accreted | F32 | surface | S / S |
| L43 | Portal site and user sign-in | N70 | accreted | F35 | surface | S / S |
| L44 | Delivery configuration page | N70 | accreted | F35 | surface | S / S |
| L45 | Fax status and history page | N70 | accreted | F35 | surface | M / M |
| L46 | Capacity provision for nominal volume | N90 | accreted | F36 | statement | S / unsizeable |
| L47 | Burst absorption: backlog and admission control | N90 | accreted | F37 | behaviour | M / M |
| L48 | Cluster membership and private-network addressing | N40 | accreted | F39,F44 | behaviour | M / M |
| L49 | CDR writer and store | N50 | accreted | F40 | store | S / S |
| L50 | Billing data writer and store | N50 | accreted | F41 | store | S / S |
| L51 | Old-system exchange interface | N80 | accreted | F42,F43 | interface | unsizeable / unsizeable |
| L52 | Traffic assignment between old and new system | N80 | accreted | F43 | behaviour | S / S |
| L53 | PoP delivery-result receiver | N23 | accreted | F46 | interface | S / S |
| L54 | Delivery confirmation and failure notice to sender | N23 | accreted | F46 | behaviour | M / M |
| L55 | Email delivery outcome tracking | N13 | accreted | F46 | behaviour | S / S |
| L56 | First-version core function set, as replaced | N00 | accreted | F47 | behaviour | unsizeable / unsizeable |
| D01 | Fax number to user directory | N10 | derived | trigger:L02,L04 | store | M / M |
| D02 | Sender identification and authorisation | N21 | derived | trigger:L03,L13 | behaviour | M / M |
| D03 | User account and service settings records | N50 | derived | trigger:L43,L05,D01,D02 | store | M / M |
| D04 | PoP status collector | N60 | derived | trigger:L42 | behaviour | S / S |
| D05 | Node and queue state collector | N41 | derived | trigger:L29,L30 | behaviour | M / M |
| D06 | Archive retrieval index by fax identity | N50 | derived | trigger:L36,L45 | store | S / S |
| D07 | Working-file cleanup | N50 | derived | trigger:L37 | behaviour | S / S |
| D08 | Render-failure notice to sender | N22 | derived | trigger:L15 | behaviour | S / S |
| D09 | Portal password recovery | N70 | derived | trigger:L43 | behaviour | S / S |
| D10 | Outbound retry and reroute on failed delivery | N23 | derived | trigger:L53 | behaviour | M / M |
| D11 | System event and alarm log | N60 | derived | trigger:L41,L33 | store | M / M |
| D12 | Account data synchronisation with old system | N80 | derived | trigger:D03,L51 | interface | S / S |

Work items: 521 element-attached items from the crossing (per element: design, implementation, test design, unit tests, code review, requirement elaboration, interface contract tests, seed-data items on stores, statement realisation; per parent: test execution ×2 cycles, defect resolution ×2 cycles, regression suite, test data, planning and tracking, user documentation where a surface is beneath), plus the root's per-parent items, plus 16 once/per-environment items, plus the two priced addendum rows.

## Coverage report

**Categories of work the estimate carries** (each is a priced activity): element design and implementation; test design, unit and component tests, code review; test execution and defect resolution (2 cycles per subsystem); automated regression suite; test data preparation; interface contract testing; requirement elaboration per element; planning and tracking per subsystem; integration at every aggregation node (C3); test strategy; production verification checklist; mobilisation and set-up; status reporting; risk and dependency management; provisioning of three environments; build and deployment pipeline; promotion procedure; configuration management and version control set-up; **production cutover**; hosting set-up; operational runbook; support handover pack; release notes; user documentation; seed data specification, load and reconciliation on stores that need it; integration tests on the real message stream (one pass); establishing that the old version can be decommissioned.

**Carried, NOT priced — awaiting a parameter** (refused by the gap-blind rate author):
- **W-F48, domain immersion and architecture/technology selection** — its effort is headcount × stage length; the stage's headcount is undeclared (the case profile records it as unknown; A3 excludes headcount by design).
- **W-F50, comparison of the new system's outputs with the old system's until they agree** — scales with the parallel-run period, which is undeclared; the rate author also judged its honest most-likely above the table's per-row ceiling and asked for a catalogue split (comparator build · per class of discrepancy · per week of monitoring).
- Also named by the rate author: W-F49 prices one pass, **not a sustained soak window** on live traffic.

**Named holes — elements the sizing sensors could not size, priced at nothing** (per-element items on them are absent from the totals):
- L27 further-format renderers (the source says 8–10 formats and names 7) — both repeats.
- L38 system database schema (no entity kinds named) — both repeats.
- L51 old-system exchange interface (no operations named) — both repeats.
- L56 first-version core function set, as replaced (the functions are never listed) — both repeats.
- L46 capacity provision for nominal volume — repeat 2 only.
- Seed-data items on L32 (both) and on D03 (repeat 2) — the sensors found nothing to pre-load.

**Not in the declaration, therefore in no item**: acceptance testing by a separate party; legacy data migration (accounts, configurations, archive); security or compliance assurance; performance, capacity and burst testing (the performance-testing activity applies only to statements with a measurable target, and the crossing refused it on both candidate statements); hyper-care after cutover; operating the old system during coexistence; hardware procurement and cluster installation.

**Closure findings the sizing sensors named** (work they judged necessary and absent; not priced): hand-off of jobs to the workers on the inbound path; handling of faxes for unknown numbers; submission-rejection notices; fallback when the routing program gives no answer; recording outbound status changes in the token store; clean-up of finished status entries; a registry of points of presence maintained after its seed load; account creation / provisioning; an inventory of the first version's core functions; initial migration of user accounts from the old system; ending coexistence.
