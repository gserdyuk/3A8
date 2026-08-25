# Axis S rerun — leaf inventory, Sonnet 5, runs RS-1 … RS-5

Prompt md5 `196524bee339e2da35a293652ca9b00f`. Engine `Lytin-D 5.0`. All five passed both gates
(RS-4 with a structural note, below).

**Headline for this batch:** Sonnet on axis S came in **18.9% below** the level recorded in run17
(576.0 vs 710.0) with CV **23.26%** against the recorded 17.54%. Single-leaf modules are far more
prevalent here than on axis P.

---

## RS-1 — ΣE 422.58 | 45 leaves | 24 modules (19 single-leaf) | 6 branches | C6 11 checks, 9 outside, mean +26.0%

Branches: A Employees Portal · B Administration Portal · C Suppliers Portal · D Core Booking & Matching Engine · E Integration Layer · F Platform, Environments & Release

**A Employees Portal** (6 single-leaf modules): booking list & status view · confirm/reject reservation workflow UI · view/print/export reservations · feedback capture · requirement amendment UI (employee) · user documentation

**B Administration Portal** — B1 Config & Rules (2): core configuration UI · prioritisation & rules builder. B5 Reporting (3): booking details reports · supplier reporting · financial reporting. Single-leaf: booking status dashboard · manual hotel booking web forms · requirement amendment & conflict UI · admin user documentation

**C Suppliers Portal** (4 single-leaf): portal access & authentication · hotel availability/pricing upload · transport pricing upload · supplier user documentation

**D Core Booking & Matching Engine** — D1 Search/Match/Prioritise (4): search aggregation logic · requirement matching algorithm · prioritisation rules engine · requirements data model & CRUD. D2 Workflow engine (2): core state machine · manual booking support logic. D3 Sync & merge (2): CTC ingestion & merge policy · conflict detection & alerting. Single-leaf: transport combining engine · notifications dispatch service

**E Integration Layer** (6 single-leaf): Cost Tracking Center API · UPSA API · external hotel booking aggregator · Uber API · SMS gateway · SSO integration backend

**F Platform, Environments & Release** (activity-shaped, 10 leaves): dev environment · stage environment · production environment & hosting · CI/CD & release/patch promotion · configuration mgmt & version control · monitoring/logging/alerting · security hardening & TLS 1.2 · system/E2E integration & regression test · UAT support · operational documentation & runbooks

**Placement:** testing distributed (inside functional leaves) + F8 system/E2E and F9 UAT · **transition NOWHERE** — no migration of suppliers/travel dept/employees off the manual process, no data migration of 2015-era records, no change-management/cutover leaf · documentation distributed (A6, B6, C4) plus F10 operational · environments gathered in F

**Run's own C2 note:** the context diagram names four boxes; branches D (Core Booking & Matching) and E (Integration Layer) were added because shared search/workflow/sync logic and external adapters are substantial independently-buildable parts belonging inside no single portal. Logged as an interpretive step, not a departure from the single-axis rule.

---

## RS-2 — ΣE 600.02 | 71 leaves | 16 modules (0 single-leaf) | 6 branches | C6 19 checks, 12 outside, mean +13.1%

Branches: A Core Booking Engine & Platform Services · B Employees Portal · C Administration Portal · D Suppliers Portal · E Admin & Support Console · F Infrastructure, Environments & Release

**A Core Booking Engine & Platform Services** (10 modules, 31 leaves) — A1 Supplier search & prioritisation (5): requirement intake & normalisation · matching engine · prioritisation rules engine · rules engine admin API · search ranking & caching. A2 Approval & booking workflow (5): booking stage state machine · automatic booking execution · manual hotel booking backend · booking extensibility framework · payment status tracking hooks. A3 Changes management (4): CTC change intake & diff · merge policy engine · conflict detection & alerting · manual hotel change override. A5 Transport auto-integration & location (2): Uber API integration · pickup/drop-off location mgmt. A6 Transport combining (2): combining algorithm · combining rules configuration. A7 Notifications/messaging (3): email notification integration · SMS gateway integration · notification templating/rules. A8 CTC integration (3): CTC API client & mapping · CTC inbound sync scheduler · CTC error handling/reconcile. A9 UPSA integration (2): UPSA API client & mapping · UPSA integration testing. A10 External booking aggregator (3): aggregator search client · aggregator booking execution · aggregator data normalisation. A11 SSO/identity (2): SSO protocol backend · role-based access control

**B Employees Portal** (7 leaves direct): booking list & detail view · confirmation/acceptance workflow UI · print/export confirmed reservation · SSO login (front-end) · feedback capture UI & backend · requirement amendment UI · responsive/mobile layout

**C Administration Portal** — C1 Configuration mgmt (4): system configuration UI · prioritisation rules config UI · booking process config UI · config versioning/audit trail. C2 Booking oversight (3): booking status dashboard · manual hotel booking web form · manual change-of-hotel UI. C3 Reporting (4): booking details reporting · suppliers reporting · financial reporting · reporting engine/framework. C4 Admin portal shell (2): SSO login (front-end) · admin portal responsive layout

**D Suppliers Portal** — D1 Hotel supplier management (3): hotel supplier login/access · manual booking upload UI · hotel supplier data validation/storage. D2 Transport supplier management (3): transport supplier login/access · manual pricing upload UI · transport supplier data validation/storage

**E Admin & Support Console** (2 leaves direct): system administration console · support/issue-tracking tools

**F Infrastructure, Environments & Release** (activity-shaped, 12 leaves): dev environment setup · stage environment setup · production environment (HA/resilience) · CI/CD & release/patch promotion · DB platform setup & scalability tuning · security hardening & TLS 1.2 · performance engineering (critical-situation load) · config mgmt & version control across envs · system integration/regression testing · UAT support · operational & user documentation · production deployment & go-live cutover

**Placement:** testing distributed per-leaf + gathered F.9 and F.10 · **transition NOWHERE** — F.12 covers only the technical go-live step, not organisational transition; explicitly flagged as a real absence · documentation lightly distributed + gathered F.11 · environments gathered in F

---

## RS-3 — ΣE 746.80 | 84 leaves | 16 modules (0 single-leaf) | 5 branches | C6 21 checks, 9 outside, mean −7.5%

Branches: A Employees Portal · B Administration Portal · C Suppliers Portal · D Booking Engine & Integrations · E Admin & Support / Platform Operations

**A Employees Portal** (9 leaves direct, no modules): portal shell/nav/SSO client login · booking list & status view · confirm/accept/reject workflow UI · view & print confirmed reservation · requirement amendment UI (employee-side) · feedback capture · responsive/mobile layout · functional/integration testing · user documentation

**B Administration Portal** — B1 Configuration management (6): business/prioritisation rules config UI · general system configuration · approval workflow stage config UI · notification templates/rules config UI · role & permission management UI · module testing. B2 Booking oversight & manual booking (6): booking status dashboard · manual hotel booking web form · manual hotel change/override UI · approve/decline stage actions UI · alerts & notification review UI · module testing. B3 Reporting (5): booking details report · suppliers reporting · financial reporting · export/scheduling · module testing. Branch-direct: admin portal user documentation

**C Suppliers Portal** — C1 Supplier access & common UI (3): supplier auth & account mgmt · supplier dashboard shell · module testing. C2 Hotel supplier module (3): manual upload of hotel bookings · pricing & details management UI · module testing. C3 Transport supplier module (2): manual upload of pricing details · module testing. Branch-direct: suppliers portal documentation

**D Booking Engine & Integrations** — D1 Search & prioritisation engine (5): requirement intake & normalization · search orchestration (manual + aggregator) · prioritisation rules evaluation engine · result caching/refresh · module testing. D2 Approval & booking workflow engine (6): stage state machine core · transition triggers from portals · extensibility hooks for future stages · payment stage tracking · workflow audit trail · module testing. D3 Changes management / CTC sync (4): merge policy engine · conflict detection & alert triggering · change history/versioning · module testing. D4 Transport combining (3): combining algorithm · combined-booking presentation hooks · module testing. D5 Notifications (4): email dispatch service · SMS gateway integration · trigger wiring across event sources · module testing. D6 CTC integration (3): CTC API client & data mapping · CTC polling/sync & change feed · module testing. D7 UPSA integration (2): UPSA API client & data mapping · module testing. D8 External hotel/transport aggregator (4): hotel aggregator API integration · transport aggregator integration (non-Uber) · result normalization & error handling · module testing. D9 Uber integration (2): Uber API integration · module testing. D10 SSO/identity integration (3): SSO protocol integration & session mgmt · role/claims mapping to user models · module testing. Branch-direct: booking engine technical documentation

**E Admin & Support / Platform Operations** (activity-shaped, 11 leaves): IT support / system admin tooling · dev environment · staging environment · production environment (incl. HA) · CI/CD & release/patch promotion · security hardening & compliance (TLS 1.2, DPA) · performance engineering & load testing · monitoring/logging/alerting · config mgmt / version control tooling · UAT coordination & cross-portal support · operational documentation

**Placement:** testing DISTRIBUTED — every module and every branch carries its own "module/functional testing" leaf; no separate system-test node beyond UAT coordination in E · **transition NOWHERE** — no data migration, no organisational change management; training excluded by A1 · documentation distributed by subsystem + operational in E · environments gathered in E

*Note: this is the only Sonnet axis-S rerun with a negative C6 mean (−7.5%) and zero single-leaf modules — it is also the highest-level of the five (746.80). The pattern "no single-leaf modules ⇒ higher level" is worth checking against the whole corpus.*

---

## RS-4 — ΣE 649.40 | 63 leaves | 29 modules (18 single-leaf) | 5 branches | C6 17 checks, 3 outside, mean +1.9% | gates: pass-with-note

Branches: A Employees Portal · B Administration Portal · C Suppliers Portal · D Admin and Support · E Core Platform / Backend Services — **plus 13 activity leaves hanging directly off the ROOT**

**A Employees Portal** (7 single-leaf modules): booking view & status · accept/reject & confirm booking UI · view & print confirmed reservations · SSO client login integration · feedback capture · trip/requirement amendment UI (incl. pickup/drop-off) · portal shell/infrastructure

**B Administration Portal** — B-Config (2): general config screens · prioritisation/rules configuration UI. B-BookingMgmt (4): dashboard/status visibility · approve/decline action UI · manual hotel booking web forms · conflict alert & manual hotel-change UI. Single-leaf: reporting UI · portal shell/infrastructure

**C Suppliers Portal** — C-Core (3): supplier access & account management · hotel supplier data upload UI · transport supplier data upload UI. Single-leaf: portal shell/infrastructure

**D Admin and Support** (3 single-leaf): user & role administration · system monitoring & support console · portal shell

**E Core Platform / Backend Services** — E1 Booking domain core (3): data model & schema design · core booking/requirement CRUD services · audit/history tracking. E2 CTC integration (2): inbound sync connector · requirement mapping/transformation. E4 External booking aggregator (2): aggregator API client & search · result normalisation/mapping. E5 Search & prioritisation engine (3): matching/core engine · rules engine · re-prioritisation/scheduling logic. E6 Approval & booking workflow engine (3): workflow/state machine core · stage-transition rules & extensibility · manual-booking backend support. E7 Changes management / merge engine (3): merge policy engine · conflict detection & alerting logic · manual hotel-change backend. E10 Notifications service (3): dispatch & template engine · email gateway integration · SMS gateway integration. E11 Reporting engine (4): reporting data aggregation/backend · booking reports logic · suppliers reports logic · financial reports logic. Single-leaf: E3 UPSA integration · E8 Uber integration · E9 transport combining logic · E12 SSO backend integration · E13 core platform infrastructure/shared services

**Root-level activity leaves (13, bypassing the branch layer entirely):** system architecture & technical design (incl. NFR design) · dev environment setup · staging environment setup · production environment & hosting setup · system integration testing cycle 1 · regression/system testing cycle 2 · performance/load testing (incl. disruption scenarios) · security & compliance testing (TLS/DPA) · UAT cycle support & defect fixing · system operational documentation · user documentation · production release/deployment & cutover · release/patch promotion & config-mgmt procedures

**STRUCTURAL NOTE (why "pass-with-note"):** those 13 leaves have no branch parent, so they carry only
the top-level C3 item (×1.2) instead of branch+top (×1.4). The arithmetic self-reconciles and the
multiplier 1.470 is internally consistent — but axis S declares branches as the top level, and a leaf
with no branch parent sits outside the declared partition. **This is a third failure mode the two
existing gates do not catch.** A third gate is indicated: every leaf must have a branch parent.

**Placement:** testing distributed (unit inside subsystem leaves) + gathered at root (T5–T8) · **transition essentially NOWHERE** beyond the technical cutover T12 · documentation gathered at root (T10, T11) · environments gathered at root (T2–T4, T12, T13)

---

## RS-5 — ΣE 461.40 | 41 leaves | 19 modules (13 single-leaf) | 5 branches | C6 7 checks, 3 outside, mean +10.1%

Branches: 1 Requirements & Analysis · 2 Design · 3 Development · 4 Testing · 5 Deployment & Environments · 6 Documentation

**⚠ AXIS VIOLATION — read before using this run in the control.** The declared axis is S
(subsystem/surface), but this run's top level is **Requirements / Design / Development / Testing /
Deployment / Documentation** — a *lifecycle* cut. That is axis P's shape, produced under the axis-S
prompt. The subsystem structure appears only *inside* branch 3 (Development) as modules. Neither
existing gate catches this: the multiplier reconciles (1.490) and no leaf exceeds the C1 ceiling.

**1 Requirements & Analysis** (6): discovery & stakeholder workshops · functional spec Search/Prioritisation/Booking · functional spec Portals · integration requirements & API contracts · NFR & architecture constraints spec · data model & reporting requirements

**2 Design** (9): system architecture (HA/resilience) · integration architecture (CTC/UPSA/SSO/Uber/aggregator) · data model / DB schema · UX/UI Employees Portal · UX/UI Administration Portal · UX/UI Suppliers Portal · security & auth design · common look-and-feel / design system · notifications design

**3 Development** (15 modules, 36 leaves) — M1 Search & prioritisation engine (5): aggregator API integration · search query builder & requirement matching · prioritisation rules engine · manual-upload results into search · search results API for portals. M2 Approval & booking workflow engine (4): booking state machine (8 stages) · stage-transition/extensibility framework · manual hotel booking web forms · booking API for portals. M3 Changes & requirements sync (3): merge policy engine · conflict detection & alerting · manual hotel change override. M4 Suppliers Portal (2): portal shell & login/access control · supplier dashboard. M5 Supplier data upload (2): manual upload forms/UI · upload validation & storage. M6 Transport integration Uber (2): Uber API integration · pickup/dropoff location mgmt. M8 Employees Portal (4): booking view & status dashboard · confirm/accept/reject actions · view/print confirmed reservations · feedback capture. M9 Administration Portal (3): system configuration UI · booking status visibility dashboard · admin front end (users/roles/config). M10 Reporting (3): booking details reporting · suppliers reporting · financial reporting. M-CTC Cost Tracking Center integration (3): CTC API client & data mapping · requirements sync (poll/webhook) · error handling/retry/logging. Single-leaf modules: M7 transport combining · M11 admin & support console · M-Notify notifications (email/SMS gateway, templates, triggers) · M-Auth authentication/SSO & RBAC · M-UPSA UPSA integration

**4 Testing** (9): test planning & case design · system testing Booking & Search · system testing Portals · integration testing external systems · performance & load / disruption scenarios · security testing · regression cycles · UAT support · defect fixing/retest

**5 Deployment & Environments** (8): dev environment setup · stage/QA environment setup · production environment (HA/scale) · CI/CD & release automation · config mgmt & version control · release & patch promotion procedures · production deployment/cutover · DevOps monitoring/alerting setup

**6 Documentation** (4): user docs Employees Portal · user docs Administration Portal · user docs Suppliers Portal · operational documentation

**Placement:** testing gathered in branch 4 · **transition NOWHERE** · documentation gathered in branch 6 · environments gathered in branch 5

---

## Cross-run observations for the control

| run | ΣE | leaves | modules | single-leaf | branches | top-level shape |
|---|---:|---:|---:|---:|---:|---|
| RS-1 | 422.58 | 45 | 24 | **19** | 6 | subsystem (S), core+integration branches added |
| RS-2 | 600.02 | 71 | 16 | 0 | 6 | subsystem (S) |
| RS-3 | 746.80 | 84 | 16 | 0 | 5 | subsystem (S) |
| RS-4 | 649.40 | 63 | 29 | **18** | 5 | subsystem (S) + 13 root-level activity leaves |
| RS-5 | 461.40 | 41 | 19 | **13** | 5 | **LIFECYCLE (P shape) under an S prompt** |

Two of five Sonnet axis-S runs have structural defects that neither gate catches (RS-4 root-level
leaves, RS-5 wrong axis). Both are among the three lowest levels. **Before the overlap control is
computed, a decision is needed on whether RS-5 may be used as an axis-S sample at all** — it is
arguably an axis-P tree, and including it would contaminate exactly the comparison the control makes.
Register that decision before looking at any overlap number.
