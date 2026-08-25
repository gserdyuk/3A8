# Axis P — leaf inventory, Sonnet 5, n=5, Lytin-D 5.0

Prompt: `prompt_decomposition_BMS_axisP.txt`, md5 `5de455cf8c165be500dc17bf2a09dac3`.
Companion to `axisP_trees_opus.md`. Captured before session end for the axis-overlap control.

Note for the control: Sonnet branch counts vary (4/6/6/5/6) where Opus is 6/6/6/6/6.
PS-1 and PS-4 generate one requirements leaf and one design leaf **per module** — leaves
derived from the tree's own shape rather than from the source text. Relevant to prediction 5
and to the leaf-as-unit-of-generation reading.

---

## PS-1 — ΣE 594.53 | 66 leaves | 14 modules | 4 branches | C6 mean +6.4% | single-leaf modules: 2 of 14 (dev level)

**Branch A — Analysis & Design.** Cross-cutting leaves (4): solution architecture & tech stack · UX/UI design system (look & feel, responsive) · NFR design (perf/availability/security/DPA) · requirements elaboration & functional spec.
Plus **one design leaf per module (14)**: M1 Booking Core · M2 Search & Prioritization · M3 Config & Rules Engine · M4 Change/Merge Engine · M5 CTC Integration · M6 UPSA Integration · M7 Notifications & Alerts · M8 Auth & Access Control · M9 Suppliers Portal · M10 Uber Integration · M11 Transport Combining · M12 Employees Portal UI · M13 Admin Portal UI · M14 Reporting. *(All 14 resolved to a single leaf each — no integration item.)*

**Branch B — Development, 14 modules (34 leaves):**
- M1 Booking Core (4): data model & schema · workflow/state-machine engine · status/visibility API · manual override & extension hooks
- M2 Search & Prioritization (3): aggregator API integration · manual listing matching · prioritization rule execution
- M3 Config & Rules Engine (3): rules authoring UI · rules evaluation engine · system configuration mgmt
- M4 Change/Merge Engine (2): merge policy execution · conflict detection & alert trigger
- M5 CTC Integration (2): CTC API client & data mapping · sync scheduler & error handling
- M6 UPSA Integration (1, single leaf): UPSA API client
- M7 Notifications & Alerts (2): email integration & templating · SMS gateway integration
- M8 Auth & Access Control (2): SSO integration (Employees) · RBAC & supplier/admin login
- M9 Suppliers Portal (3): portal shell · hotel manual upload workflow · transport pricing upload workflow
- M10 Uber Integration (1, single leaf): Uber API integration
- M11 Transport Combining (2): combining logic · combining UI
- M12 Employees Portal UI (3): booking view/list & detail · confirm/print reservation flow · feedback capture
- M13 Admin Portal UI (3): admin shell & status dashboard · manual hotel booking web forms · reporting front-end integration
- M14 Reporting (3): booking details reports · supplier reporting · financial reporting (incl. UPSA)

**Branch C — Testing (8):** functional/system testing Employees Portal · functional/system testing Admin Portal · functional/system testing Suppliers Portal · integration testing external systems (CTC/UPSA/Uber/aggregator/SSO) · non-functional performance/load · non-functional security · regression cycle · UAT support

**Branch D — Deployment & Release (6):** dev environment setup · stage environment setup · prod environment setup (HA/resilience) · CI/CD pipeline & release automation · production deployment & cutover · documentation (operational & user)

**Placement:** testing partly gathered (branch C), unit-level distributed inside dev leaves · **transition NOWHERE** — no parallel run, no historical data import, no organisational rollout; explicitly named a gap · documentation in Deployment & Release branch, one leaf · environments gathered in Deployment & Release

---

## PS-2 — ΣE 651.80 | 61 leaves | 12 modules | 6 branches | C6 mean +23.3% | single-leaf modules: 3 of 12

**A. Requirements & Design (6):** requirements analysis & functional spec · architecture & integration design (CTC/UPSA/SSO/aggregators/Uber) · UX/UI design & style guide · data model & database design · security/SSO protocol/compliance design · non-functional design (perf/HA/scalability)

**B. Development — 12 modules (33 leaves):**
- B1 Search & Prioritisation Engine (4): requirements matching/search · aggregator integration (1–2 GDS/Booking-class APIs) · prioritisation rules engine · manual-booking matching
- B2 Booking Workflow & Approval (4): stage state machine · stage-change triggers & rules · manual hotel booking web forms · process extensibility (config-driven stages)
- B3 Changes Mgmt & CTC Integration (4): CTC requirement ingestion · merge-policy engine · conflict detection & alerting · manual hotel-change UI
- B4 Suppliers Portal (4): supplier auth & access mgmt · manual hotel-booking upload · manual transport-pricing upload · supplier-facing listing/mgmt UI
- B5 Transport Integration (2): Uber API integration · locations load from CTC + override UI
- B6 Transport Combining (1, single leaf): combining logic
- B7 Notifications (3): email templates & delivery · SMS gateway integration · notification rules/config
- B8 SSO / Authentication (1, single leaf): SSO integration
- B9 Employees Portal (5): booking list/detail/status · confirm/reject reservations · view/print confirmed reservations · feedback capture · mobile-responsive layout
- B10 Administration Portal (4): configuration UI · rule-management UI · booking-status dashboard · manual hotel-booking mgmt screens
- B11 Reporting (3): booking-details reporting · supplier reporting · financial reporting
- B12 UPSA Integration (1, single leaf): UPSA API integration

**C. Testing (9):** test planning & case design · system test Employees/Booking Workflow · system test Admin/Reporting · system test Suppliers/Transport · integration testing (CTC/UPSA/SSO/Uber/aggregators/SMS) · performance & load testing · security testing · regression cycle · defect-fix verification

**D. Deployment & Environments (7):** dev environment · stage/UAT environment · production environment (SaaS hosting, HA) · CI/CD & release/patch promotion · config mgmt & version control · TLS/security hardening · production cutover/go-live

**E. UAT Support (1, single leaf):** UAT support

**F. Documentation (2):** operational documentation · user documentation

**Placement:** testing gathered in C (unit assumed inside dev leaves) · **transition NOWHERE** — explicitly a genuine gap, not a scoped exclusion · documentation gathered in F · environments gathered in D

---

## PS-3 — ΣE 791.25 | 68 leaves | 14 modules | 6 branches | C6 mean +7.0% | single-leaf modules: 3 of 14

**A. Requirements & Design (8):** requirements elaboration & use-case spec · overall system & data architecture · integration architecture (CTC/UPSA/SSO/aggregator/Uber/SMS) · NFR design (perf/HA/security/config-mgmt) · UX/UI Employees Portal · UX/UI Administration Portal · UX/UI Suppliers Portal · design system / shared style guide

**B. Development — 14 modules (34 leaves):**
- B1 Booking Engine & Workflow (4): core data model & stage state machine · approval/booking workflow transition logic · manual hotel booking web forms · extensibility framework for future stages
- B2 Supplier Search & Prioritisation (4): search + prioritisation matching engine · custom prioritisation rules engine · hotel aggregator (GDS/Booking-class) integration · dynamic re-prioritisation on change
- B3 CTC Integration (2): CTC API client & data ingestion · requirement mapping/transformation
- B4 Changes Management (3): merge-policy engine · conflict detection & alerting · manual hotel-change UI
- B5 Suppliers Portal shell (2): portal shell — auth/nav/layout · supplier account/access management
- B6 Hotel Supplier Management (2): manual upload of hotel availability/pricing · hotel booking detail management
- B7 Transport Supplier Management (3): Uber API integration (auto search/booking) · manual transport suppliers booking flow · pickup/drop-off location management
- B8 Transport Combining (1, single leaf): combining logic for multiple transport bookings
- B9 Employees Portal (5): SSO integration · booking view/status display · confirm/accept/reject booking UI · view/print confirmed reservations · feedback capture
- B10 Administration Portal (3): system configuration UI · booking-status visibility dashboard · admin front-end shell
- B11 Reporting (4): booking-details reporting · supplier reporting · financial reporting · reporting infra / export & scheduling
- B12 Transport Supplier Portal content (1, single leaf): manual upload of pricing details
- B13 Admin & Support (1, single leaf): system health/audit/support console
- B14 UPSA Integration (1, single leaf): UPSA API integration (undocumented scope)
- *(also: Notifications single leaf — email/SMS gateway, templates, triggers; Auth/SSO single leaf — SSO integration & RBAC)*

**C. Testing (9):** test planning & case design · system testing Booking & Search · system testing Portals · integration testing external systems · performance & load / disruption scenarios · security testing · regression cycles · UAT support · defect fixing / retest

**D. Deployment & Environments (8):** dev environment setup · stage/QA environment setup · production environment (HA/scale) · CI/CD & release automation · config management & version control · release & patch promotion procedures · production deployment/cutover · DevOps monitoring/alerting setup

**E. Documentation (4):** user docs Employees Portal · user docs Administration Portal · user docs Suppliers Portal · operational documentation

**Placement:** testing gathered in C; unit-level absorbed into dev leaves (stated as a modeling choice) · **transition NOWHERE** — no seeding of supplier relationships, no communication of the new process to suppliers who today upload nothing, no handling of in-flight manual bookings at go-live · documentation gathered in E · environments gathered in D

---

## PS-4 — ΣE 787.80 | 88 leaves | 12 modules | 5 branches | C6 mean −9.1% (only negative mean in 20 runs) | single-leaf modules: 1 of 12 (dev level)

**A. Requirements & Analysis (14):** NFR & acceptance-criteria definition · requirements sign-off & traceability · **plus one requirements leaf per module (12)**: M1 search & prioritisation · M2 approval & booking · M3 changes mgmt · M4 suppliers portal · M5 transport/Uber · M6 transport combining · M7 employees portal · M8 admin portal · M9 reporting · M10 notifications · M11 CTC integration · M12 SSO

**B. Architecture & Design (16):** overall architecture & tech stack · data model design · security architecture · performance/HA architecture · **plus one design leaf per module (12)**, same module list as above

**C. Development — 12 modules (42 leaves):**
- M1 Supplier Search & Prioritisation (4): requirement matching engine · aggregator/GDS integration · prioritisation rules engine · manual-upload matching
- M2 Approval & Booking Workflow (5): booking state machine · manual hotel booking web forms · booking history/audit · UPSA integration ("Paid" stage) · approval routing/escalation
- M3 Changes Management (4): CTC change feed consumption · merge policy engine · conflict detection/alerting · manual override UI
- M4 Suppliers Portal (4): portal shell/supplier auth · hotel manual upload forms · transport manual upload forms · supplier profile/access mgmt
- M5 Transport Booking / Uber (3): Uber API integration · pickup/drop-off location mgmt · transport status sync
- M6 Transport Combining (1, single leaf): combining logic
- M7 Employees Portal (5): booking view/status dashboard · confirm/reject reservation UI · print/export confirmed reservation · portal SSO wiring · feedback capture
- M8 Administration Portal (4): system configuration UI · booking status monitoring dashboard · admin front-end/control · IT support/admin tooling
- M9 Reporting (4): booking details reporting · supplier reporting · financial reporting · report generation/export infra
- M10 Notifications & Alerts (3): email notification integration · SMS gateway integration · notification rules/templates
- M11 Cost Tracking Center Integration (3): CTC inbound API client · CTC outbound sync · data mapping/transformation
- M12 SSO / Authentication (2): SSO protocol integration · role-based access control

**D. Testing (10):** test planning & test-case design · system testing Search & Booking core · system testing Portals · system testing Transport · system testing Reporting/Notifications/Integrations · integration testing (external systems) · performance & load testing · security testing · regression testing · UAT support

**E. Deployment & Release (6):** environment provisioning (dev/stage/prod, CI/CD) · configuration management & version control · release & patch promotion procedures · production deployment & go-live cutover · documentation (operational + user) · DevOps monitoring/alerting setup

**Placement:** testing gathered in D — dev leaves are build-only, no embedded per-feature test leaves · **transition NOWHERE** — no parallel-run against the manual process, no migration of historical/manual booking records, no decommissioning of the manual workflow · documentation one leaf under Deployment & Release · environments gathered in Deployment & Release

*Note: this is the only run in the whole batch whose C6 mean is negative. Its own reading: the whole-node estimates sensed cross-cutting complexity (shared services, configurability, mobile UI, session handling) that the itemised leaves failed to capture — i.e. the split lost work rather than finding it.*

---

## PS-5 — ΣE 781.30 | 72 leaves | 15 modules | 6 branches | C6 mean +16.9% | single-leaf modules: 5 of 15

**1. Requirements & Analysis (6):** discovery & stakeholder workshops · functional spec Search/Prioritisation/Booking · functional spec Portals · integration requirements & API contracts · NFR & architecture constraints spec · data model & reporting requirements

**2. Design (9):** system architecture (HA/resilience) · integration architecture (CTC/UPSA/SSO/Uber/aggregator) · data model / DB schema · UX/UI Employees Portal · UX/UI Administration Portal · UX/UI Suppliers Portal · security & auth design · common look-and-feel / design system · notifications design

**3. Development — 15 modules (36 leaves):**
- M1 Search & Prioritisation Engine (5): aggregator API integration · search query builder & requirement matching · prioritisation rules engine · manual-upload results into search · search results API for portals
- M2 Approval & Booking Workflow Engine (4): booking state machine (8 stages) · stage-transition/extensibility framework · manual hotel booking web forms · booking API for portals
- M3 Changes & Requirements Sync (3): merge policy engine · conflict detection & alerting · manual hotel change override
- M4 Suppliers Portal (2): portal shell & login/access control · supplier dashboard
- M5 Supplier Data Upload (2): manual upload forms/UI · upload validation & storage
- M6 Transport Integration – Uber (2): Uber API integration · pickup/dropoff location mgmt
- M7 Transport Combining (1, single leaf): combine multiple transport bookings
- M8 Employees Portal (4): booking view & status dashboard · confirm/accept/reject actions · view/print confirmed reservations · feedback capture
- M9 Administration Portal (3): system configuration UI · booking status visibility dashboard · admin front end (users/roles/config)
- M10 Reporting (3): booking details reporting · suppliers reporting · financial reporting
- M11 Admin & Support (1, single leaf): system health/audit/support console
- M-Notify Notifications (1, single leaf): email/SMS notifications (gateway, templates, triggers)
- M-Auth Authentication/SSO (1, single leaf): SSO integration & RBAC
- M-CTC Cost Tracking Center Integration (3): CTC API client & data mapping · requirements sync (poll/webhook) · error handling / retry / logging
- M-UPSA Integration (1, single leaf): UPSA API integration (core, undocumented scope)

**4. Testing (9):** test planning & case design · system testing Booking & Search · system testing Portals · integration testing external systems · performance & load / disruption scenarios · security testing · regression cycles · UAT support · defect fixing / retest

**5. Deployment & Environments (8):** dev environment setup · stage/QA environment setup · production environment (HA/scale) · CI/CD & release automation · config mgmt & version control · release & patch promotion procedures · production deployment/cutover · DevOps monitoring/alerting setup

**6. Documentation (4):** user docs Employees Portal · user docs Administration Portal · user docs Suppliers Portal · operational documentation

**Placement:** testing gathered in branch 4; unit-level not itemised (absorbed into dev leaves) · **transition NOWHERE** — today's process is manual/email-based, no legacy system to migrate from, training excluded by A1; nothing manufactured to fill the slot · documentation gathered in branch 6 · environments gathered in branch 5

---

## Cross-run summary for prediction 6 (post-hoc placement), axis P, both models

| | testing placed | transition placed |
|---|---|---|
| Opus | 5 of 5 (gathered, branch of its own) | 5 of 5 — but only PO-3 has an explicit parallel-run leaf; PO-2/PO-4 explicitly thin |
| Sonnet | 5 of 5 (gathered, branch of its own) | **0 of 5 — "nowhere" in every run** |

Registered prediction was: testing ≥4 of 5 per axis; transition off the manual process in fewer
than 3 of 5. Testing confirmed on both models. Transition **confirmed on Sonnet (0/5)**,
**refuted on Opus (5/5)** — though the Opus placements are mostly cutover-and-seeding rather
than transition off the manual process proper. Scoring needs a decision on whether
"cutover + supplier onboarding" counts as transition; that rule was flagged as needing
fixing before the data was read and has NOT been fixed. Do not score until it is.
