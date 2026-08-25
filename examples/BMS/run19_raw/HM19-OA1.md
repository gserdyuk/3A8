# HM19-OA1 — `Hotyn-M 1.1`, Opus 5, order A, repeat 1

Transcribed from the sensor's reply. `tool_uses: 0`. Contamination check: clean.

**Omitted from this transcription and stated so it is not mistaken for absent:** the per-requirement
accretion tables for passes 1 and 2 (68 rows each). Their content is summarised below; the final
model, the completeness table and the readings are verbatim.

Inputs: `requirements_product.md` md5 `0c2dea478b993e4451a66f9468633f1e` (N=68),
`assumptions_product.md` md5 `8c622930655540d5fceb0d58d7482f8d`, order A.

---

## Accretion, summarised

Skeleton posited **68 nodes** — close to one per requirement, at leaf granularity.

Pass 1: **9 added, 0 deferred.** Verdicts: 7 partial (R01, R73, R15, R24, R29, R31, R32), 2 not
covered (R33, R34), the rest covered. Pass 2: 0 added, 0 deferred → fixpoint.

Nodes added by accretion: N69 Tenancy & Isolation · N70 Data Retention & Subject Rights · N71 Source
Federation & Result Normalisation · N72 Prioritisation Recalculation on Change · N73 Automatic Booking
Orchestration & Fallback · N74 CTC Update Ingestion & Scheduling · N75 Update Classification &
Downstream Propagation · N76 Merge Policy Engine · N77 Merge Conflict Alerting.

## Completion — 10 derived nodes, none carrying coverage

| node | name | parent | trigger | pass |
|---|---|---|---|---|
| N78 | Supplier Credential Management | N13 | suppliers are outside client SSO | 1 |
| N80 | Supplier Registry | N26 | uploads and reports need a supplier entity | 1 |
| N81 | Traveller Profile | N26 | requirements, locations, views, feedback attach to a person | 1 |
| N82 | Audit Trail | N26 | three amendment origins plus a merge policy | 1 |
| N83 | Notification Delivery Tracking & Retry | N35 | external channels fail silently | 1 |
| N84 | Integration Fault Handling & Retry | N19 | adapters fail; the fallback needs a failure signal | 1 |
| N85 | Candidate Set Cache | N71 | ranking and recalculation need a stable normalised set | 1 |
| N86 | Configuration Versioning & Effective Dating | N10 | a past booking must be explicable against past config | 1 |
| N87 | Reporting Read Model | N60 | three report families over one read path | 1 |
| N79 | Credential Recovery | N78 | a credential that can be issued can be lost | 2 |

Completion-covers-a-requirement defects: 0.

## Convergence

skeleton 68 posited · accretion 9 then 0 · completion 9, then 1, then 0 · closure collapsed 9.

## Normalisation log (9 collapses)

| collapsed | into | coverage carried |
|---|---|---|
| N03 SaaS Hosting | N69 Tenancy & Isolation | R01 |
| N07 Security & Data Protection | N70 Data Retention & Subject Rights | R72, R73 |
| N10 Configuration Model & Store | N86 Configuration Versioning | R11, R54, R65 |
| N71 Source Federation | N85 Candidate Set Cache | R15, R16 |
| N31 Search | N85 | R15, R16, R17 |
| N32 Prioritisation | N72 Recalculation on Change | R18, R19, R24 |
| N76 Merge Policy Engine | N77 Merge Conflict Alerting | R33, R44 |
| N35 Stage Notifications | N83 Notification Delivery | R26, R27 |
| N78 Supplier Credential Mgmt | N79 Credential Recovery | ∅ |

## Final model — 78 nodes after normalisation

| id | name | parent | own coverage |
|---|---|---|---|
| N01 | BMS Product | — | ∅ |
| N02 | Platform Foundation | N01 | ∅ |
| N69 | SaaS Hosting, Tenancy & Isolation | N02 | R01 |
| N04 | Performance & Scalability | N02 | R12, R66 |
| N05 | Availability & Resilience | N02 | R13, R68 |
| N06 | Data Platform | N02 | R63 |
| N70 | Security, Data Protection & Retention | N02 | R72, R73 |
| N08 | Growth Architecture | N02 | R71 |
| N09 | Configuration Subsystem | N01 | ∅ |
| N86 | Configuration Model, Store & Versioning | N09 | R11, R54, R65 |
| N11 | Rules Engine | N09 | R11, R19 |
| N12 | Process Configuration | N09 | R11, R28, R65 |
| N13 | Identity & Access | N01 | ∅ |
| N14 | SSO Integration | N13 | R08, R52 |
| N15 | Roles & Authorisation | N13 | R65 |
| N79 | Supplier Credential Management & Recovery | N13 | ∅ |
| N16 | UX Foundation | N01 | R61, R66 |
| N17 | Design System & Common Look and Feel | N16 | R09, R61 |
| N18 | Responsive Presentation | N16 | R62 |
| N19 | Integration Layer | N01 | ∅ |
| N20 | CTC Integration | N19 | R06, R21, R31, R41 |
| N21 | UPSA Integration | N19 | R07 |
| N22 | Travel Content Aggregator Integration | N19 | R15 |
| N23 | Uber Integration | N19 | R39 |
| N24 | Email Channel Integration | N19 | R26 |
| N25 | SMS Gateway Integration | N19 | R27 |
| N84 | Integration Fault Handling & Retry | N19 | ∅ |
| N26 | Booking Domain Core | N01 | ∅ |
| N27 | Booking Register | N26 | R04 |
| N28 | Booking Requirements Management | N26 | R21 |
| N74 | CTC Update Ingestion & Scheduling | N28 | R31, R32 |
| N75 | Update Classification & Downstream Propagation | N74 | R32 |
| N77 | Merge Policy & Conflict Alerting | N74 | R33, R34, R44 |
| N29 | Supplier Inventory Store | N26 | R37, R47 |
| N80 | Supplier Registry | N26 | ∅ |
| N81 | Traveller Profile | N26 | ∅ |
| N82 | Audit Trail | N26 | ∅ |
| N30 | Search & Prioritisation | N01 | ∅ |
| N85 | Search (federated, normalised, cached) | N30 | R15, R16, R17 |
| N72 | Prioritisation (ranking & recalculation) | N30 | R18, R19, R24 |
| N33 | Approval & Booking Workflow | N01 | ∅ |
| N34 | Stage Model & Transitions | N33 | R25 |
| N83 | Stage Notifications & Delivery | N33 | R26, R27 |
| N73 | Automatic Booking Orchestration & Fallback | N33 | R29 |
| N36 | Hotel Booking | N01 | ∅ |
| N37 | Automatic Hotel Booking | N36 | R29 |
| N38 | Manual Hotel Booking | N36 | R30, R38 |
| N39 | Hotel Selection Change | N36 | R35 |
| N40 | Transport Booking | N01 | ∅ |
| N41 | Automatic Transport Booking | N40 | R29, R39 |
| N42 | Manual Transport Booking | N40 | R40, R48 |
| N43 | Journey Locations | N40 | R41, R44 |
| N44 | Transport Booking Combination | N40 | R45 |
| N45 | Suppliers Portal | N01 | ∅ |
| N46 | Supplier Access | N45 | R36, R46 |
| N47 | Supplier Upload | N45 | R37, R47 |
| N48 | Supplier Booking Workspace | N45 | R05, R38, R48 |
| N49 | Employees Portal | N01 | ∅ |
| N50 | Employee Booking Workspace | N49 | R05, R49 |
| N51 | Reservation Confirmation | N49 | R50 |
| N52 | Reservation Printout | N49 | R51 |
| N53 | Employee Amendment | N49 | R22, R42 |
| N54 | Feedback Capture | N49 | R53 |
| N55 | Administration Portal | N01 | R57 |
| N56 | System Configuration UI | N55 | R54, R57 |
| N57 | Prioritisation Rule Management | N55 | R20 |
| N58 | Admin Amendment | N55 | R23, R43 |
| N59 | Booking Oversight Workspace | N55 | R05, R55 |
| N60 | Reporting | N01 | R56, R67 |
| N61 | Booking Details Reporting | N60 | R58 |
| N62 | Suppliers Reporting | N60 | R59 |
| N63 | Financial Reporting | N60 | R60 |
| N87 | Reporting Read Model | N60 | ∅ |
| N64 | Admin & Support Console | N01 | ∅ |
| N65 | Incident Intake | N64 | R14 |
| N66 | Diagnostic Inspection | N64 | R14 |
| N67 | Configuration Inspection | N64 | R14 |
| N68 | Process Transparency | N01 | R10 |

## Coverage completeness

**68 of 68 whole. 0 residues. 0 unplaced. No partial mark standing at closure.** The per-requirement
table with the part each node realises is in the sensor's reply; every row's verdict was `whole`.

## Instrument readings — `Hotyn-M 1.1`

| reading | value |
|---|---|
| nodes before normalisation | 87 |
| nodes after normalisation | 78 |
| skeleton size | 68 |
| accretion additions | 9 |
| completion additions | 10 |
| **anchored (skeleton + accretion)** | **77** |
| nodes collapsed at closure | 9 |
| stated after normalisation | 59 |
| implied after normalisation | 19 (13 aggregates + 6 derived) |
| coverage assignments (requirement, node) | 96 |
| nodes per requirement | mean 1.41, max 3 |
| skeleton nodes with empty total coverage | 0 |
| skeleton nodes with empty own coverage | 13 |
| deferrals | 0 |
| ambiguity flags | 16 — R01, R05, R07, R10, R11, R13, R14, R15, R25, R29, R33, R37, R44, R61, R65, R67 |
| completion-covers-a-requirement defects | 0 |
| partial marks standing at closure | 0 |

## Findings the run reported about the rules

1. **Provenance no longer means what it meant in 1.0.** An aggregate carries no own coverage, so
   `implied` conflates a grouping node with a genuinely derived one. The derived count must be taken
   from the completion log, not from the provenance column.
2. **Three collapses moved coverage onto derived leaves** (N10→N86, N31/N71→N85, N35→N83), so after
   normalisation "derived" and "carries no coverage" are different sets. The derived fraction is only
   stable measured **before** normalisation.
3. **M4's empty-skeleton test must be applied to total coverage, not own coverage.** Applied to own
   coverage it reports all 13 aggregates as findings — a false positive manufactured by the 1.1 rule.
4. **The engine stamp in the output format section of the definition still said `Hotyn-M 1.0`** while
   the identity section said 1.1. The run stamped 1.1 and reported the inconsistency rather than
   honouring the stale literal.
5. **Boundary crossings refused under P1**, each named: an operations/hosting function, a backup and
   restore procedure, environment and release management. Acts performed on the system, not
   components of it.
