# Run 18 — the four product models, `Hotyn-M 1.0`

Pinned requirement list `requirements.md`, md5 `554ea3608dd0602f0ddf2f7e7b82178c`, N=73.
Orders A (top-down by breadth of impact) and B (exact reverse of A).
All four runs reported `tool_uses: 0` — isolation held.

Format below: **node → coverage set**. Nodes with no coverage are `implied` (skeleton aggregates that
ended empty, or completion-derived). Parent structure is shown by indentation.

---

## HM-SA — Sonnet 5, order A — 91 nodes (16 skeleton + 71 accretion + 4 completion)

**S1 Platform & Infrastructure** — S1.1 SaaS Delivery Model {R01} · S1.2 Hosting Ownership {R02} · S1.3 Support Ownership {R03} · S1.4 System of Record Authority {R04} · S1.5 Configurability for Business Evolution {R11,R65p} → S1.5.1 Regulatory & Policy Configurability {R65} · S1.6 Performance & Capacity {R12,R63p,R71p} → S1.6.1 Screen Load Time Target {R66} · S1.7 Disruption-Critical Operation Support {R13} · S1.8 Database Platform Scalability {R63} · S1.9 High Availability & Resilience {R68} · S1.10 Future Growth Extensibility {R71}

**S2 Security & Compliance** — S2.1 Transport Encryption Standard {R72} · S2.2 Data Protection Compliance {R73}

**S3 Presentation & UX** — S3.1 Unified UI Standard {R09} · S3.2 Modern UX Design {R61} · S3.3 Responsive Multi-Device Support {R62} · S3.4 Seamless SSO Login Experience {R52}

**S4 External Integrations** — S4.1 CTC API Integration {R06,R21p,R31p} · S4.2 UPSA API Integration {R07} · S4.3 SSO Integration {R08,R52p}

**S5 Employees Portal** — S5.1 Employee Confirmed-Booking Management {R05,R50p} · S5.2 Booking Detail & Status View {R49,R51p} · S5.3 Reservation Confirmation Action {R50} · S5.4 Confirmed Reservation View & Print {R51} · S5.5 Employee Booking Feedback Capture {R53}

**S6 Administration Portal** — S6.1 Travel Dept Confirmed-Booking Management {R05,R55p} · S6.2 System Administration & Configuration Front End {R57,R54,R20p} → S6.2.1 Prioritisation Rule Configuration Screen {R20} · S6.3 Booking Status Visibility TM {R55}

**S7 Admin & Support Component** — stated directly {R14}

**S8 Supplier Portals** — S8.1 Transport Supplier Confirmed-Booking Management {R05,R46p} · S8.2 Hotel Supplier Access {R36,R37p} → S8.2.1 Hotel Supplier Manual Upload {R37} · S8.3 Transport Supplier General System Access {R46,R47p} → S8.3.1 Transport Supplier Pricing Upload {R47}

**S9 Booking Requirements Management** — S9.1 Requirements Sourced from CTC {R21,R31p,R41p} · S9.2 Requirement Amendment Employees Portal {R22,R42p} · S9.3 Requirement Amendment Admin Portal {R23,R43p} · S9.4 Frequent CTC Synchronisation {R31,R32p} · S9.5 CTC-Driven Requirement Change Handling {R32,R33p} · S9.6 Update Merge Policy {R33,R34p}

**S10 Search & Prioritisation** — S10.1 Multi-System Intelligent Search {R15,R17p} · S10.2 Manual Upload Search {R16,R17p} · S10.3 Requirement-Driven Search Criteria {R17} · S10.4 Requirement-Match Prioritisation {R18,R24p} · S10.5 Custom Rule-Based Prioritisation {R19,R20p,R24p} · S10.6 Dynamic Re-Prioritisation {R24}

**S11 Booking Workflow** — S11.1 Business Process Definition & Clarity {R10} · S11.2 Booking Approval Process Stages {R25,R28p} · S11.3 Process Extensibility {R28} · S11.4 Automatic Booking Capability {R29}

**S12 Hotel Booking Fulfilment** — S12.1 Manual Hotel Booking TM Web Forms {R30,R38} · S12.2 Manual Hotel Change Override {R35}

**S13 Transport Booking Fulfilment** — S13.1 Automatic Uber Integration {R39} · S13.2 Manual Transport Suppliers {R40,R48} · S13.3 Location Data Sourced from CTC {R41,R42p,R43p} · S13.4 Location Amendment Employees Portal {R42,R44p} · S13.5 Location Amendment Admin Portal {R43,R44p} · S13.6 Location Override Capability {R44} · S13.7 Transport Booking Combination {R45}

**S14 Notifications** — S14.1 Email Notifications {R26} · S14.2 SMS Notifications {R27} · S14.3 Merge Conflict Alerts {R34}

**S15 Reporting** — S15.1 Report Performance Criteria {R67} · S15.2 Travel Manager Reporting Access {R56,R58p,R59p,R60p} · S15.3 Booking Details Report {R58} · S15.4 Suppliers Report {R59} · S15.5 Financial Report {R60}

**S16 Configuration & Release Management** — S16.1 Technology Currency Reviews {R64} · S16.2 Environment & Document Config Control {R69} · S16.3 Release & Patch Management {R70}

**Completion (4, cover nothing):** C1 Shared UI Component Library / Design System ← S3.1+portals · C2 Role-Based Access Control ← S4.3+portals · C3 Data Backup & Disaster Recovery ← S1.4+S1.9+S1.7 · C4 Proposal Generation Bridge ← S10+S11.2

**Empty skeleton nodes:** none. **Ambiguity flags:** R05, R10.

---

## HM-SB — Sonnet 5, order B — 91 nodes (15 skeleton + 71 accretion + 5 completion)

**S1 Booking Requirements Intake** — N24 CTC-Driven Requirement Updates {R32,R31p,R21p} · N25 Frequent CTC Sync {R31} · N33 Requirement Amendment Admin Portal {R23,R05p} · N34 Requirement Amendment Employee Portal {R22,R05p} · N35 Initial Requirement Definition from CTC {R21,R06p}

**S2 Hotel Booking Subsystem** — N19 Manual Hotel Booking Handling {R38} · N20 Hotel Availability/Pricing Upload {R37} · N21 Manual Hotel Change {R35} · N26 TM Manual Hotel Booking Web Forms {R30} · N39 Requirement-Based Search {R17} · N40 Manual-Upload Search {R16}

**S3 Transport Booking Subsystem** — N11 Manual Transport Booking Handling {R48,R40} · N12 Transport Pricing Upload {R47} · N13 Transport Booking Combination {R45} · N14 Pickup/Dropoff Override {R44} · N15 Pickup/Dropoff Amendment Admin {R43} · N16 Pickup/Dropoff Amendment Employee {R42} · N17 Pickup/Dropoff Initial Load from CTC {R41,R06p} · N18 Automatic Transport Integration Uber {R39}

**S4 Booking Workflow Engine** — N22 Merge Conflict Alerts {R34} · N23 Merge Policy Engine {R33} · N27 Automatic Booking Capability {R29} · N28 Extensible Booking Process Design {R28,R71p,R11} · N29 SMS Stage-Change Notifications {R27} · N30 Email Stage-Change Notifications {R26} · N31 Booking Approval Stage Lifecycle {R25} · N32 Dynamic Prioritisation Re-evaluation {R24} · N36 Prioritisation Rule Definition Admin {R20,R19p} · N37 Rule-Based Prioritisation Logic {R19} · N38 Requirement-Matching Prioritisation Logic {R18} · **C2 Booking Audit Trail** (derived)

**S5 Booking Review & Confirmation** — N7 Booking Feedback Capture {R53} · N8 View/Print Confirmed Reservations {R51} · N9 Reservation Confirmation {R50} · N10 Booking Details & Status View {R49}

**S6 Employee Portal** — N67 Confirmed Booking Management Access TM & Employees {R05}

**S7 Travel Department / Admin Portal** — N5 Booking Status Visibility TM {R55} · N6 System Configuration TM {R54,R57p}

**S8 Reporting Subsystem** — N1 Financial Reporting {R60} · N2 Suppliers Reporting {R59} · N3 Booking Details Reporting {R58} · N4 Travel Manager Reporting Access {R56} · N57 Report Generation Volume Constraint {R67}

**S9 Supplier Portal** — N44 Transport Supplier Portal Access {R46,R05p} · N45 Hotel Supplier Portal Access {R36,R05p}

**S10 Integration Layer** — N41 Third-Party Aggregator Search {R15} · N47 SSO Technical Integration {R08} · N48 UPSA API Integration {R07} · N49 CTC API Integration Technical {R06} · **C3 Notification Dispatch Infrastructure** · **C5 Notification Template Management** (both derived)

**S11 Admin and Support Component** — N42 Administration Front End {R57,R14p} · N46 IT Support Function/Tooling {R14}

**S12 Security & Compliance** — N43 SSO-Based Seamless Access {R52,R08p} · N51 Data Protection Act Compliance {R73} · N52 TLS 1.2 Minimum Enforcement {R72} · **C1 Identity, Role & Permission Management** (derived)

**S13 Platform / Non-functional Foundation** — N53 System-Wide Growth/Extensibility Design {R71,R11} · N56 High Availability & Resilience {R68} · N58 Screen Load Performance Target {R66,R12p} · N59 Legislative/Policy/Org-Structure Configurability {R65,R11} · N60 Technology Currency & Upgrade Reviews {R64} · N61 Scalable Database Platform {R63} · N62 Multi-Resolution Display Support {R62} · N63 Modern Web UX/Technology {R61} · N64 Critical/Disruption Situation Support {R13} · N65 High-Demand Performance Capacity {R12} · N66 Common Look and Feel {R09} · N68 System-of-Record Authority {R04} · **C4 Backup & Disaster Recovery** (derived)

**S14 Hosting & Delivery Model** — N54 Release & Patch Promotion {R70} · N55 Configuration Mgmt & Version Control {R69} · N69 Vendor Support Obligation {R03,R01p} · N70 Vendor Hosting Obligation {R02,R01p} · N71 SaaS Delivery Model Overall {R01}

**S15 Business Process Documentation** — N50 Business Process Documentation {R10}

**Empty skeleton nodes:** none. **Ambiguity flags (9):** R56, R49, R40, R37, R29, R25, R57, R11, R05.

---

## HM-OA — Opus 5, order A — 109 nodes (23 skeleton + 62 accretion + 24 completion)

**Skeleton spine, all became stated:** N01 Booking Management System {R01} · N02 Presentation Layer & UI Platform {R09,R49,R61,R62} · N03 Employees Portal {R05,R22,R42,R50,R53} · N04 Administration Portal {R14,R20,R23,R30,R43,R54,R55,R56,R57} · N05 Supplier Portal {R05,R36,R46} · N06 Booking Domain Core {R04,R05,R25,R29} · N07 Requirement Intake & Amendment {R17,R21,R22,R23} · N08 Search & Prioritisation Engine {R15,R16,R17,R18,R19} · N09 Hotel Booking Subsystem {R30,R35,R38} · N10 Transport Booking Subsystem {R39,R40,R45,R48} · N11 Notification Subsystem {R26,R27,R34} · N12 Reporting Subsystem {R56,R58,R59,R60,R67} · N13 Integration Subsystem {R06,R07,R15,R39} · N14 Identity & Access Management {R05,R08,R52} · N15 Configuration & Business Rules {R11,R19,R28,R54,R57,R65,R71} · N16 Data Platform {R63} · N17 Hosting & Runtime Platform {R01,R02,R12} · N18 Release & Environment Management {R69,R70} · N19 Security & Data Protection {R72,R73} · N20 Support & Service Operations {R03,R14} · N21 Feedback Subsystem {R53} · N22 Business Process Definition {R10} · N23 Resilience & Continuity {R13,R68}

**Accretion nodes (62):** N24 Tenancy & Service Delivery {R01} · N25 Authoritative Booking Registry {R04} · N26 Role & Ownership Authorisation {R05,R36,R46} · N27 Shared Design System {R09,R61} · N28 Performance & Scalability Engineering {R12,R66,R71} · N29 Web Front-End Technology Stack {R61} · N30 Responsive Multi-Device Layout {R62} · N31 Database Scaling & Volume Mgmt {R63} · N32 Technology Currency & Upgrade Programme {R64} · N33 Organisation & Policy Model {R65} · N34 Front-End Performance Budget {R66} · N35 Report Generation Performance & Criteria {R67} · N36 Config Mgmt & Version Control {R69} · N37 Extensibility Architecture {R71} · N38 Transport Security TLS {R72} · N39 Data Protection Compliance Controls {R73} · N40 CTC Integration {R06,R21,R31,R41} · N41 UPSA Integration {R07} · N42 SSO Integration {R08,R52} · N43 Support Console & Incident Tooling {R14} · N44 Hotel Supplier Workspace {R36,R37,R38} · N45 Transport Supplier Workspace {R40,R46,R47,R48} · N46 Third-Party Inventory Search Connectors {R15,R29} · N47 Federated Search Aggregation {R15} · N48 Internal Inventory Search {R16} · N49 Requirement-Driven Search Criteria {R17} · N50 Requirement Match Ranking {R18,R24} · N51 Custom Prioritisation Rule Engine {R19,R20,R24} · N52 Prioritisation Rule Editor {R20} · N53 Requirement Intake from CTC {R21,R31,R32,R41} · N54 Employee Requirement Amendment {R22,R42} · N55 Administrator Requirement Amendment {R23,R43} · N56 Prioritisation Re-evaluation on Change {R24} · N57 Booking Lifecycle State Machine {R25,R26,R28,R49,R50} · N58 Email Notification Channel {R26} · N59 Lifecycle Event Triggers {R26,R27} · N60 SMS Notification Channel {R27} · N61 Configurable Workflow Definition {R28} · N62 Automated Booking Execution {R29,R39} · N63 Manual Hotel Booking Forms {R30,R35,R38} · N64 Periodic CTC Synchronisation {R31,R32} · N65 Inbound Change & Cancellation Handling {R32,R33} · N66 Update Merge Policy Engine {R33,R34} · N67 Merge Conflict Detection & Alerting {R34} · N68 Hotel Selection Change {R35} · N69 Hotel Inventory Upload {R37} · N70 Manually Uploaded Inventory Store {R37,R47} · N71 Manual Hotel Supplier Booking Handling {R38} · N72 Uber Integration {R39} · N73 Manual Transport Booking Handling {R40,R48} · N74 Journey Location Model {R41,R42,R43,R44} · N75 Employee Location Amendment {R42,R44} · N76 Administrator Location Amendment {R43,R44} · N77 Location Override Policy {R44} · N78 Transport Booking Combination {R45} · N79 Transport Pricing Upload {R47} · N80 Booking Detail & Status View {R49,R51,R55} · N81 Reservation Confirmation Action {R50} · N82 Printable Reservation Document {R51} · N83 Booking Details Report {R58} · N84 Suppliers Report {R59} · N85 Financial Report {R60}

**Completion (24, cover nothing):** N86 External Supplier Identity & Credential Mgmt · N87 Session & Token Lifecycle · N88 Role Administration · N89 Audit Trail & Change History · N90 Notification Templates & Delivery Log · N91 Notification Preferences & Opt-Out · N92 Employee & Contact Profile Store · N93 Supplier & Location Master Data · N94 Currency & Exchange Handling · N95 Data Retention & Archival · N96 Integration Error Handling & Retry · N97 Secret & API Credential Mgmt · N98 Backup & Restore · N99 Monitoring, Logging & Alerting · N100 Environment Topology · N101 Operational & User Documentation Set · N102 Third-Party Search Caching & Throttling · N103 Automated Cancellation & Amendment with Third Parties · N104 Time Zone & Locale Handling · N105 Supplier Credential Recovery · N106 Notification Delivery Failure Handling · N107 Master Data Deduplication · N108 Secret Rotation · N109 Restore Verification & DR Rehearsal

**Empty skeleton nodes:** none, but four held exactly one requirement and are marginal: N16 {R63}, N21 {R53}, N22 {R10}, N01 {R01}. The run flagged N22 as the most marginal — held by a single requirement whose reading it could not settle.
**Verdicts:** covered 11 · partial 61 · not covered 1 · deferred 0. **Ambiguity flags (9):** R01, R03, R10, R13, R14, R29, R44, R67, R71.

---

## HM-OB — Opus 5, order B — 99 nodes (75 skeleton + 7 accretion + 17 completion)

Skeleton posited at leaf granularity, so accretion added almost nothing.

**N0 Booking Management System** {R01}
**N1 Employees Portal** {R05} — N1.1 booking review & acceptance {R49,R50} · N1.2 trip & requirement amendment {R22,R42} · N1.3 feedback capture {R53} · N1.4 confirmed-reservation view & print {R51}
**N2 Administration Portal** {R05,R14,R57} — N2.1 booking administration workbench {R23,R30,R35,R43} · N2.2 configuration & rules admin UI {R20,R54,R57} · N2.3 status dashboard {R55} · N2.4 reporting UI {R56} · *D15 reference data admin screens (derived)*
**N3 Supplier Portal** {R05} — N3.1 supplier access & onboarding {R36,R46} · *D01 supplier account lifecycle admin* · N3.2 hotel inventory & pricing upload {R37} · N3.3 transport pricing upload {R47} · N3.4 manual supplier booking handling {R38,R40,R48}
**N4 Booking Domain Core** *(empty, infrastructure)* — N4.1 booking requirement mgmt {R21,R22,R23} · N4.2 approval & lifecycle workflow {R25,R50} → A04 automated booking orchestrator {R29} · N4.3 booking register {R04,R49,R50} → A01 reservation document rendering {R51}, A07 record reconciliation & audit trail {R04} · N4.4 hotel booking execution {R29,R30,R35,R38} · N4.5 transport booking execution {R29,R48} → A02 transport booking consolidation {R45} · N4.6 pick-up/drop-off location mgmt {R41,R42,R43,R44} · N4.7 update ingestion & merge {R32,R33,R34} · N4.8 feedback records {R53} · *D09 reference & master data* · *D13 time zone & locale handling*
**N5 Search & Selection** *(empty, infrastructure)* — N5.1 requirement-driven search criteria {R17} · N5.2 search over uploaded inventory {R16} · N5.3 search across third-party systems {R15} → A06 cross-provider aggregation & normalisation {R15}
**N6 Prioritisation & Rules** *(empty, infrastructure)* — N6.1 requirement-match prioritisation {R18} · N6.2 custom prioritisation rule engine {R19,R24} → A05 re-evaluation on change {R24} · N6.3 rule authoring & versioning {R20,R24}
**N7 Notifications & Alerts** *(empty, infrastructure)* — N7.1 email channel {R26} · N7.2 SMS channel {R27} · N7.3 alerts to parties {R34} · *D04 notification template mgmt* · *D05 delivery failure handling & retry*
**N8 Reporting** *(empty, infrastructure)* — N8.1 report engine & scheduling {R56,R67} · N8.2 financial report {R60} · N8.3 supplier report {R59} · N8.4 booking details report {R58}
**N9 Integration Layer** *(empty, infrastructure)* — N9.1 CTC integration {R06,R21,R31,R32,R41} → A03 scheduled synchronisation job {R31} · N9.2 UPSA integration {R07} · N9.3 external hotel booking connectors {R15,R29} · N9.4 external transport booking connectors {R15,R29,R39} · N9.5 SMS gateway connector {R27} · *D12 integration contract & version mgmt*
**N10 Identity & Access** *(empty, infrastructure)* — N10.1 authentication & session {R52} → *D02 non-SSO auth path* → *D14 credential reset & recovery* · N10.2 SSO integration {R08,R52} · N10.3 roles, permissions & actor model {R05,R36,R46} → *D10 user provisioning & profile store*
**N11 Platform & Infrastructure** *(empty, infrastructure)* — N11.1 SaaS hosting & environments {R01,R02} → *D06 environment topology* → *D16 per-environment config sets*, *D17 secret & integration credential store* · N11.2 availability & resilience {R13,R68} → *D07 health monitoring* · N11.3 database platform {R63} → *D08 backup & restore* · N11.4 performance & scalability {R12,R66,R67} · N11.5 release & patch promotion {R70} · N11.6 config mgmt & version control {R69} · N11.7 technology currency & upgrades {R64}
**N12 Configuration & Extensibility** *(empty, infrastructure)* — N12.1 configuration store & mgmt {R11,R54,R65} → *D03 admin & config change audit log* · N12.2 business process extensibility {R28,R65} · N12.3 evolution & growth architecture {R11,R71}
**N13 Security & Compliance** *(empty, infrastructure)* — N13.1 data protection compliance {R73} · N13.2 transport-level security {R72}
**N14 UI Foundation** *(empty, infrastructure)* — N14.1 common look & feel design system {R09,R61} · N14.2 responsive multi-device UI {R62} · N14.3 modern front-end stack & UX {R61,R66}
**N15 Service Operations & Support** *(empty, infrastructure)* — N15.1 support component & IT support tooling {R03,R14} → *D11 support diagnostics & incident intake* · N15.2 documented business processes {R10} · N15.3 critical-instance / disruption handling {R13}

**Empty skeleton nodes: 12**, all second-level aggregates, all judged genuine infrastructure, none dropped. **All 59 skeleton leaves received at least one requirement.**
**Ambiguity flags (12):** R25, R37, R15, R14, R07, R10, R71, R67, R13, R11, R05, R03.

---

## Defect found in the pinned inputs, not in the runs

**HM-OA flagged a contradiction between the requirement list and the assumption log**, and it is real:

> R03 "The Supplier supports the system" obliges ongoing support.
> A1 "Not included: subsequent operation, user training, the warranty period" removes it.

The run placed R03 and declined to reconcile, which is correct behaviour under M1. **This is an error in
how the inputs were constructed** — the assumption log was carried over from the `Lytin` era, where it
bounded an *estimate*; the requirement list states what the *product* must be. The two were never
checked against each other. Both HM-OB and HM-SA/SB placed R03 without noticing.

Fix belongs to the inputs, not the engine: either A1 is amended, or R03 is marked out-of-scope in the
list with a stated reason. Not fixed here — recording it before deciding.
