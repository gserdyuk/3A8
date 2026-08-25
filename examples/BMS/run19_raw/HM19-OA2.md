# HM19-OA2 — `Hotyn-M 1.1`, Opus 5, order A, repeat 2

Transcribed from the sensor's reply. `tool_uses: 0`. Contamination check: clean — the run noted that
the session context listed filenames of prior runs and recorded that **no file was read**.

**Omitted from this transcription and stated so it is not mistaken for absent:** the per-requirement
accretion tables for passes 1 and 2 (68 rows each). Summarised below; the final model, the
completeness verdicts and the readings are verbatim.

Inputs: identical to HM19-OA1, to the letter.

---

## Accretion, summarised

Skeleton posited **21 nodes** — subsystem granularity, no coverage attached.

Pass 1: **99 added, 0 deferred.** Verdicts: 2 covered outright (R28, R54 — realised by structure added
for earlier requirements), 25 partial, the rest not covered. Pass 2: 0 added, 0 deferred → fixpoint.

The additions are the `Axxx` nodes in the final model below.

## Completion — 11 derived nodes, none carrying coverage

| node | name | parent | trigger | pass |
|---|---|---|---|---|
| C01 | Tenant Provisioning & Baseline Configuration | A001 | a tenancy model needs the act that creates a tenant | 1 |
| C02 | Booking Reference Issuance | A002 | a record cited by three audiences needs a stable identifier | 1 |
| C03 | External Supplier Credential Recovery | A038 | suppliers hold their own credentials | 1 |
| C04 | Notification Delivery Status & Retry | S15 | external channels fail silently | 1 |
| C05 | Integration Failure Handling & Dead-Letter Quarantine | S08 | sync and booking calls fail transiently | 1 |
| C06 | Outbound Integration Credential Store & Rotation | S08 | four adapters authenticate | 1 |
| C07 | Configuration Change History & Rollback | S16 | runtime config needs a way back | 1 |
| C08 | Reference Data Management (currency, geography) | S18 | locations, pricing and finance resolve against vocabularies | 1 |
| C09 | Report Output Rendering & Download | S13 | a report needs a rendered form to leave the system | 1 |
| C10 | Credential Recovery Rate Limiting & Lockout | C03 | a self-service recovery endpoint is an abuse surface | 2 |
| C11 | Dead-Letter Requeue Action | C05 | a quarantine with no way back is a sink | 2 |

Completion-covers-a-requirement defects: 0.

## Convergence

skeleton 21 posited · accretion 99 then 0 · completion 9, then 2, then 0 · closure collapsed 2.

## Normalisation log (2 collapses)

| collapsed | into | new parent | coverage carried |
|---|---|---|---|
| S07 Supplier Manual Channel | A076 Supplier Inventory Upload Ingest & Validation | S01 | ∅ |
| S21 Feedback | A092 Feedback Record | S01 | ∅ |

Not collapsed, with the reason given: A001, A002, A038, C03, C05 each have one child but content of
their own. A one-child node with content is an aggregation of something; only a contentless wrapper
carries no information.

## Final model — 129 nodes after normalisation

Aggregates (own coverage empty): S01 BMS Platform (root) · S02 Booking Domain Core · S03 Search &
Selection · S04 Approval & Booking Workflow · S05 Hotel Booking · S06 Transport Booking · S08
Integration Layer · S09 Employees Portal · S10 Administration Portal · S11 Suppliers Portal · S12
Admin & Support Console · S13 Reporting · S14 Identity & Access · S15 Notifications · S16
Configuration Subsystem · S17 UI Foundation · S18 Data Platform · S19 Platform Runtime & Resilience ·
S20 Security & Compliance. All parented to S01.

| id | name | parent | own coverage |
|---|---|---|---|
| A001 | Multi-Tenant Service Delivery | S01 | R01 |
| C01 | Tenant Provisioning & Baseline Configuration | A001 | ∅ |
| A026 | Modular Architecture & Extension Points | S01 | R71 |
| A002 | Canonical Booking Record | S02 | R04 |
| C02 | Booking Reference Issuance | A002 | ∅ |
| A047 | Booking Requirement Record | S02 | R17, R21 |
| A069 | CTC Update Application (create/amend/cancel) | S02 | R32, R04 |
| A070 | Update Merge Policy Engine | S02 | R33, R04 |
| A072 | Merge Conflict Detection & Record | S02 | R34 |
| A081 | Journey Location Record | S02 | R41 |
| A084 | Location Override (precedence over source) | S02 | R44 |
| A092 | Feedback Record (linked to a booking) | S01 | R53 |
| A045 | Federated Inventory Search & Normalisation | S03 | R15, R16 |
| A046 | Manual Inventory Source & Index | S03 | R16 |
| A048 | Requirement-Driven Query Construction | S03 | R17 |
| A049 | Prioritisation Engine | S03 | R18, R19, R24 |
| A050 | Requirement Match Evaluation | S03 | R18 |
| A052 | Custom Rule Evaluation in Ranking | S03 | R19 |
| A057 | Prioritisation Re-evaluation on Change | S03 | R24 |
| A031 | Booking Process State Visibility | S04 | R10, R49, R55 |
| A058 | Booking Stage Model (Proposed…Paid) | S04 | R25 |
| A059 | Booking Workflow Engine (definition-driven) | S04 | R25, R28, R50 |
| A065 | Automatic-to-Manual Booking Fallback | S04 | R29 |
| A063 | Automatic Hotel Booking via Aggregator | S05 | R29 |
| A066 | Manual Hotel Booking Execution | S05 | R30, R38 |
| A074 | Selected Hotel Change | S05 | R35 |
| A064 | Automatic Transport Booking (integrated supplier) | S06 | R29, R39 |
| A080 | Manual Transport Booking Handling | S06 | R40, R48 |
| A085 | Transport Booking Combination | S06 | R45 |
| A086 | Combination Eligibility Rules | S06 | R45 |
| A076 | Supplier Inventory Upload Ingest & Validation | S01 | R37, R47 |
| A027 | Supplier & Integration Extensibility | S08 | R71 |
| A032 | Cost Tracking Center Integration Adapter | S08 | R06 |
| A033 | UPSA Integration Adapter | S08 | R07 |
| A044 | Hotel Aggregator Integration Adapter | S08 | R15 |
| A054 | Booking Requirement Import from CTC | S08 | R21, R41 |
| A068 | Scheduled CTC Synchronisation | S08 | R31 |
| A079 | Uber Integration Adapter | S08 | R39 |
| C05 | Integration Failure Handling & Dead-Letter Quarantine | S08 | ∅ |
| C11 | Dead-Letter Requeue Action | C05 | ∅ |
| C06 | Outbound Integration Credential Store & Rotation | S08 | ∅ |
| A003 | Employee Booking Management | S09 | R05 |
| A055 | Booking Requirement Amendment (Employees) | S09 | R22 |
| A082 | Journey Location Amendment (Employees) | S09 | R42, R44 |
| A089 | Booking List & Detail View (Employees) | S09 | R49, R51 |
| A090 | Reservation Confirmation Action | S09 | R50 |
| A091 | Printable Reservation Document | S09 | R51 |
| A093 | Feedback Submission Form (Employees) | S09 | R53 |
| A004 | Travel Department Booking Management | S10 | R05 |
| A042 | Configuration Administration UI | S10 | R57, R54 |
| A043 | System Administration UI | S10 | R57 |
| A053 | Prioritisation Rule Authoring Screen | S10 | R20 |
| A056 | Booking Requirement Amendment (Admin) | S10 | R23 |
| A067 | Manual Hotel Booking Form (Travel Manager) | S10 | R30 |
| A075 | Change Selected Hotel Action (Admin) | S10 | R35 |
| A083 | Journey Location Amendment (Admin) | S10 | R43, R44 |
| A094 | Booking Status Dashboard (Travel Manager) | S10 | R55 |
| A096 | Report Catalogue & Runner UI | S10 | R56 |
| A005 | Supplier Booking Management | S11 | R05 |
| A039 | Hotel Supplier Workspace | S11 | R36 |
| A077 | Hotel Availability & Pricing Upload Screen | A039 | R37 |
| A078 | Hotel Supplier Booking Request & Confirmation | A039 | R38 |
| A040 | Transport Supplier Workspace | S11 | R46 |
| A087 | Transport Pricing Upload Screen | A040 | R47 |
| A088 | Transport Supplier Booking Request & Confirmation | A040 | R48 |
| A035 | Support Incident Intake & Case Record | S12 | R14 |
| A036 | Booking & Integration Diagnostics | S12 | R14 |
| A037 | Running Configuration Inspector | S12 | R14 |
| A023 | Asynchronous Report Generation & Delivery | S13 | R67 |
| A024 | Reporting Read Model / Pre-Aggregation | S13 | R67 |
| A095 | Report Definition & Parameterisation | S13 | R56 |
| A097 | Booking Details Report | S13 | R58 |
| A098 | Supplier Report | S13 | R59 |
| A099 | Financial Report | S13 | R60 |
| C09 | Report Output Rendering & Download | S13 | ∅ |
| A006 | Role & Data-Scope Authorization | S14 | R05, R36, R46, R54 |
| A034 | SSO Federation (SAML/OIDC RP) | S14 | R08, R52 |
| A038 | External Supplier Identity & Account Lifecycle | S14 | R36, R46 |
| C03 | External Supplier Credential Recovery | A038 | ∅ |
| C10 | Credential Recovery Rate Limiting & Lockout | C03 | ∅ |
| A041 | Session Management & SSO Experience | S14 | R52 |
| A060 | Notification Composition & Templating | S15 | R26, R27, R34 |
| A061 | Email Delivery Channel | S15 | R26 |
| A062 | SMS Delivery Channel (external gateway) | S15 | R27 |
| A073 | Conflict Alert Dispatch to Affected Parties | S15 | R34 |
| C04 | Notification Delivery Status & Retry | S15 | ∅ |
| A008 | Configuration Model & Store | S16 | R11, R54 |
| A009 | Configuration Activation | S16 | R11 |
| A019 | Policy & Legislative Rule Configuration | S16 | R65, R11 |
| A020 | Organisation Structure Configuration | S16 | R65, R11 |
| A021 | Business Process Definition Configuration | S16 | R65, R11, R28 |
| A051 | Custom Prioritisation Rule Definition & Store | S16 | R19 |
| A071 | Merge Policy Configuration | S16 | R33 |
| C07 | Configuration Change History & Rollback | S16 | ∅ |
| A007 | Design System & Shared UI Component Library | S17 | R09, R61 |
| A014 | Web Client Application | S17 | R61 |
| A015 | Interaction & Navigation Design | S17 | R61, R10 |
| A016 | Responsive Layout & Device Adaptation | S17 | R62 |
| A022 | Front-End Performance Budget & Instrumentation | S17 | R66 |
| A017 | Relational Database Platform | S18 | R63 |
| A018 | Data Growth Management | S18 | R63 |
| C08 | Reference Data Management | S18 | ∅ |
| A010 | Elastic Horizontal Scaling | S19 | R12, R71 |
| A011 | Performance Engineering (caching, query optimisation) | S19 | R12, R66 |
| A012 | Disaster Recovery & Backup/Restore | S19 | R13, R68 |
| A013 | Degraded-Mode Operation | S19 | R13, R68 |
| A025 | Redundancy & Automatic Failover | S19 | R68 |
| A028 | Transport Security (TLS 1.2+ policy) | S20 | R72 |
| A029 | Personal Data Protection | S20 | R73 |
| A030 | Personal Data Access Control & Audit Trail | S20 | R73 |

## Coverage completeness

**68 of 68 whole. 0 residues. 0 unplaced. No partial mark standing at closure.**

## Instrument readings — `Hotyn-M 1.1`

| reading | value |
|---|---|
| nodes before normalisation | 131 |
| nodes after normalisation | 129 |
| skeleton size | 21 |
| accretion additions | 99 |
| completion additions | 11 |
| **anchored (skeleton + accretion)** | **120** |
| nodes collapsed at closure | 2 |
| stated | 99 |
| implied, non-derived | 19 |
| coverage assignments (requirement, node) | 136 |
| nodes per requirement | mean 2.00, max 5 (R11) |
| skeleton nodes with empty own coverage | 21 of 21 |
| skeleton nodes judged wrong guesses | 2 — S07 (partly), S21; both collapsed |
| deferrals | 0 |
| ambiguity flags | 4 AMB (R25, R37, R61, R65) + 13 INT (R05, R07, R10, R11/R65, R13, R14, R15, R29, R35, R44, R49, R56, R67) |
| completion-covers-a-requirement defects | 0 |
| partial marks standing at closure | 0 |

## Findings the run reported about the rules

1. **The only-adds rule left a node under the wrong parent.** A092 Feedback Record sits under S01
   because S21 Feedback collapsed; under a free hand it belongs beneath S02. M5 forbids moving a node
   and M7 permits only the collapse, so the odd parent is **recorded rather than repaired**. A real
   cost of the only-adds rule, visible on purpose.
2. **The same stale stamp**: the output-format section of the definition said `Hotyn-M 1.0` while the
   identity section said 1.1. Stamped 1.1 and reported the inconsistency.
3. **R09 declared once, not on every surface.** Each portal's *use* of the design system is
   enumeration under M7's declare step, not a further coverage claim — "declaring R09 on every surface
   would inflate the coverage relation without adding structure". A direct application of M2 v1.1.
4. **R25 "Paid" read as a stage, not a payment engine.** No requirement obliges payment processing and
   none was built.
5. **R35's actor is unstated**; read as the Travel Manager, and the Employees Portal deliberately not
   given the action, "because inventing it would be adding an obligation".
