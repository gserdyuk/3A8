# Axis S — rerun for structure, leaf inventory

Prompt: `prompt_decomposition_BMS_axisS.txt`, md5 `196524bee339e2da35a293652ca9b00f` (verified).
Engine `Lytin-D 5.0`. Same session as the axis-P batch; probes confirmed `Lytin-F 5.0` on both
models earlier in the session, definitions unchanged since.

**Registered before reading any result:** these are *different runs* from SO-1…5 / SS-1…5 whose
numbers are recorded in `run17_axis_projection.md`. Axis-S leaf tables were never preserved, so
the overlap control could not be executed against the original runs. Using fresh axis-S runs is
legitimate for the control, because the control asks whether the two **axes** partition the
requirement list differently — a property of the axes, not of particular runs. Levels from these
reruns must NOT be substituted for the recorded run17 numbers.

Labels: `RO-n` = rerun Opus, `RS-n` = rerun Sonnet.

---

## RO-4 — ΣE 1349.6 | 108 leaves | 28 modules | 10 branches | C6 29 checks, 15 outside, mean +8.96% | gates: PASS

Top level (10 branches): Shared UI Foundation · Employees Portal · Administration Portal ·
Suppliers Portal · Booking Core Services · Supply & Booking Adapters · Enterprise Integration &
Identity · Reporting & Data Platform · Admin & Support Subsystem · Platform, Environments & Release

**S1 Shared UI Foundation** — M-UI Design system & responsive shell (5): component library core (forms, tables, modals) · responsive layout & mobile breakpoints · navigation shell, theming, look-and-feel config · FE scaffolding, routing, state mgmt, build · accessibility & cross-browser conformance pass. M-PR Document & print rendering (2): PDF/print rendering service & reservation templates · report export renderer (PDF/XLSX/CSV)

**S2 Employees Portal** — M-EV Booking view & status (3): booking list, filters, status indicators · booking detail (hotel + transport, itinerary) · printable confirmed reservation view. M-EC Confirmation & feedback (2): accept/reject reservation flow · feedback capture per booking. M-EA Requirement & location amendment (2): requirement amendment screens with validation · pickup/dropoff edit & override (address picker)

**S3 Administration Portal** — M-AC Configuration & rules admin screens (4): system configuration screens (policy, org, ref data) · prioritisation rule editor UI · booking process/stage configuration UI · notification template & channel configuration UI. M-AB Booking management & manual booking (4): Travel Manager booking overview/status dashboard · manual hotel booking web forms · manual hotel change / re-search & swap UI · alerts & conflict resolution work queue UI. M-AR Report & dashboard screens (2): report parameter & scheduling screens · report viewing / dashboard screens

**S4 Suppliers Portal** — M-SPS Supplier portal screens (4): supplier account/profile & invite registration · hotel availability & pricing management screens · transport pricing management screens · supplier booking request handling (manual booking). M-UP Bulk upload & validation (2): file upload pipeline (parse, schema mapping) · validation, error reporting, re-upload handling

**S5 Booking Core Services** — M-RQ Booking requirements (3): requirement domain model & persistence · requirement versioning & amendment API · requirement validation & policy constraints. M-BL Booking lifecycle engine (5): state machine core, configurable transitions · transition guards, permissions, audit hooks · extensibility mechanism for future stages · booking aggregate model & persistence · Paid-stage handling & reconciliation flags. M-RC Rules & configuration engine (4): configuration store & schema (typed, versioned) · rule definition model & evaluation engine · rule authoring API, validation & simulation · configuration change propagation & caching. M-NT Notifications (4): notification service core (event→template→channel) · email channel adapter & templating · SMS gateway adapter · delivery tracking, retry, preferences. M-CM Changes, merge & conflict (4): change intake & diff of incoming updates · merge policy implementation (configurable) · conflict detection & alert raising · cancellation & re-booking cascade. M-TC Transport combining (2): combining candidate detection (time/route/pax) · combined booking representation, split/unsplit

**S6 Supply & Booking Adapters** — M-SP Search & prioritisation engine (5): federated search orchestration (async, timeouts) · normalised offer model & de-duplication · matching & scoring against requirements · rule-driven prioritisation & re-prioritisation · search result caching & performance tuning. M-HA Hotel aggregator adapters (4): aggregator #1 search & availability · aggregator #1 booking/cancel · aggregator #2 (search + book) · adapter errors, retries, sandbox & credentials. M-TA Transport adapters (3): Uber search/estimate · Uber booking, status, cancel · manual transport supplier request/response flow. M-MS Manual supply catalogue (2): manual inventory model (availability, price, attrs) · catalogue exposure to search; expiry/staleness

**S7 Enterprise Integration & Identity** — M-CTC Cost Tracking Center integration (4): CTC client, auth & contract mapping · requirement intake job (frequent sync, idempotent) · trip detail & location sync back to CTC · failure handling, replay & sync monitoring. M-UPSA UPSA integration (2): UPSA client & employee/org data mapping · synchronisation & caching of UPSA reference data. M-ID Identity & access (3): SSO integration & session handling · role & permission model across four surfaces · supplier external account auth & isolation. M-SEC Security & data protection (3): TLS 1.2 enforcement, transport & secrets config · data protection (PII handling, retention, at-rest) · application security hardening & endpoint authz

**S8 Reporting & Data Platform** — M-DP Data platform (3): schema design & migration tooling · scalability/performance design (index, partition) · reporting data model / read-side projections. M-RP Reporting engine & report set (5): reporting engine & parameterised query framework · booking details reports · supplier reports · financial reports · report scheduling & delivery

**S9 Admin & Support Subsystem** — M-AS Support & operations console (3): support console (lookup, diagnostics, intervention) · system health & integration status dashboard · user & role administration screens. M-AU Audit trail & logging (2): audit trail storage & write path across domains · log aggregation, structured logging, alert rules

**S10 Platform, Environments & Release** (activity-shaped, no modules, 17 leaves): CI/CD pipeline (build, test, artefact, deploy) · development environment setup · staging environment setup · production environment (HA, resilience, scaling) · config management & version control across envs · release & patch promotion procedure · monitoring, backup & disaster recovery · automated regression suite (end-to-end) · system test cycle 1 (execution + triage) · system test cycle 2 (regression + fix verify) · performance & load test cycle (incl. peak) · security test cycle & remediation verification · UAT support cycle (env, data, defect turnaround) · operational documentation (runbooks, ops manual) · user documentation (employee/TM/supplier guides) · production cutover & go-live support · initial data load / reference & supplier data

**Placement:** testing distributed AND gathered, deliberately separated — developer-level testing inside every feature leaf's M with no line of its own; cycle-level verification gathered in S10 (regression suite, two system cycles, performance, security, UAT); component-joining verification priced by C3 node items, not by a leaf (a provisional ~8 pd integration-testing leaf was trimmed) · transition PARTIAL — has: initial data load (L108), production cutover & go-live (L107), supplier onboarding by invite (L25); has NO LINE: user training (A1), parallel run of the manual process, migration of historical booking records, change-management inside the travel department · documentation BOTH — operational and user docs gathered in S10; design/technical documentation distributed inside feature leaves · environments GATHERED in S10

**Axis-purity judgement the run flagged itself:** under a strict subsystem cut, system test cycles,
UAT and documentation produce no product part of their own. They were placed in S10, declared as a
*delivered part* (the hosted releasable service and its environments) rather than as a lifecycle
phase — the alternative, a separate "verification & acceptance" branch, would have been a process
cut sitting beside nine product cuts, which C2 forbids. **Relevant to the overlap control:** this is
where axis S absorbs the work that axis P spreads across B1/B2/B4/B5/B6.
