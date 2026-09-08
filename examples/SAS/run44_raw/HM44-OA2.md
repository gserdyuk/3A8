<!-- ORCHESTRATOR HEADER, added at transcription 2026-09-08. Not part of the sensor's reply.
run: 44 · reading: HM44-OA2 · engine (sensor's own stamp): Hotyn-M 1.1 · model (launch record): the harness's
`opus` alias, i.e. Claude Opus 5 · order A · prompt identical to HM44-OA1 · tool_uses: 0.
PROVENANCE OF THIS TEXT: the reply reached the orchestrator truncated at the head (inside the pass-1 accretion
row for P-17). The complete text below was recovered later the same day from the harness's own transcript of
the agent (the task output file), which held the full assistant message; it is the same text the sensor
emitted, not a re-emission and not a re-run. HM44-OA1's transcript file was empty and could not be recovered
the same way. -->

# SAS — product model (`Hotyn-M 1.1`)

## 1. Contamination check

**Clean, with one quarantine.** The pasted input contains a pinned obligation list (N = 146), a declared processing order (order A), and an assumption projection. It contains no effort figure, no budget, no deadline, no duration, no team size, no cost anchor and no pre-existing tree. The harness prepended ambient repository information (a git status line, a branch name, recent commit subjects, a memory index, a working-directory path). **That material was quarantined: not read as input, not acted on, not used in any judgement here.** Per the quarantine instruction it is reported rather than treated as a stop condition. No repository file was read. The run proceeds on the pasted input alone.

---

## 2. Skeleton log

Read as a set, not a sequence. Nothing attached; no coverage assigned. All nodes `posited`; all `implied` at this stage.

| id | name | intended scope |
|---|---|---|
| S-0 | SAS member application solution | root of the modelled artefact |
| S-1 | Platform & architecture | the shared technical substrate the three modules stand on |
| S-1.1 | Architecture & technical standards | composition, alignment, extensibility, standards, cloud-readiness |
| S-1.2 | Data stores | transactional store, non-transactional read store, feed between them |
| S-1.3 | Service & API layer | internal services and externally exposed APIs |
| S-1.4 | Web client foundation | delivery channel, browser reach, accessibility |
| S-1.5 | Operational design | availability, failover, backup/recovery, security, performance targets |
| S-2 | Identity & access | who the user is, what they may do |
| S-2.1 | Company & user administration | company admin, user accounts, administrative scopes |
| S-2.2 | Roles & permissions | role catalogue, role/task assignment, permission evaluation |
| S-2.3 | Authentication & IdM integration | claims, single sign-on, password reset initiation |
| S-2.4 | Role-driven UI presentation | what the interface shows per role |
| S-3 | Shared record services | behaviour common to GIN and LN records |
| S-3.1 | Record workflow & approval | submit, review, approve/reject, verification, action lists |
| S-3.2 | Record locking | concurrent-edit exclusion |
| S-3.3 | Validation & business rules | rule evaluation against X-Customer Standards |
| S-3.4 | Record status | record status model, draft, editability by status |
| S-3.5 | Record ownership | who owns a record and transfer of it |
| S-3.6 | Duplicate detection | alerts and duplicate resolution |
| S-3.7 | Record list & view framework | list, filter, sort, selection, bulk action |
| S-3.8 | Hierarchy framework | hierarchy model, editing, impact, export |
| S-4 | Identifier management | prefixes, GINs, LNs as numbers |
| S-4.1 | Prefix registry & capacity | licensed prefix data and capacity reporting |
| S-4.2 | Identifier assignment | rules, pools, auto/manual, check digit, preferences |
| S-4.3 | Identifier status lifecycle | reservation, status, retirement, reuse, back-references |
| S-5 | Product (GIN) module | what is specific to product records |
| S-5.1 | GIN record management | GIN creation, attributes, images |
| S-5.2 | GIN hierarchy | each/case/pallet levels and their rules |
| S-5.3 | Barcodes | symbology generation, view, export/print |
| S-5.4 | Product information sheets | sheet generation and layouts |
| S-5.5 | Digital GIN | embeddable representation |
| S-6 | Location (LN) module | what is specific to location records |
| S-6.1 | LN record management | LN creation and attributes |
| S-6.2 | LN hierarchy | depth and organisation rules for locations |
| S-6.3 | Location verification | annual verification recording |
| S-7 | Access Data module | the subscribe side: search, view, output |
| S-7.1 | Search & discovery | search entry points and filters |
| S-7.2 | Published record viewing | rendering of what a consumer is entitled to |
| S-7.3 | Consumer access requests | requests for records and for group membership |
| S-7.4 | Public (non-member) access | anonymous, limited use |
| S-7.5 | Access Data output | print and export from the module |
| S-8 | Publish & subscribe | the owner side of sharing and the entitlement it creates |
| S-8.1 | Publication by data owner | what is published and at what scope |
| S-8.2 | Share targets & groups | individuals, user groups, controlled groups, public |
| S-8.3 | View request approval | owner decision on consumer requests |
| S-8.4 | Subscription entitlement | what a subscription grants |
| S-9 | Import & export | record movement in and out |
| S-9.1 | Format adapters | one adapter per file format |
| S-9.2 | Import processing | ingestion, validation, staging, update modes |
| S-9.3 | Export processing | extraction and production of output |
| S-10 | Reporting & dashboard | what the user is shown and can generate |
| S-10.1 | Dashboard | start screen panels |
| S-10.2 | Report engine | definitions, scheduling, history, audit reports |
| S-11 | Notifications & communication | messages out of the system and between users |
| S-11.1 | Notification engine & channels | composition, routing, email/SMS/onscreen |
| S-11.2 | Notification types | global, member-specific, member-to-member |
| S-11.3 | Communication preferences | user choice of method and frequency |
| S-11.4 | Application feedback | feedback capture and routing |
| S-12 | Help & training | in-application guidance |
| S-12.1 | Contextual help | help surfaced in context |
| S-12.2 | Help content authoring | editing and industry variants |
| S-12.3 | Training links | links out to training material |
| S-13 | Configuration & reference data | what X-Customer maintains rather than codes |
| S-13.1 | Industry configuration | per-industry attribute, rule and content variation |
| S-13.2 | System configuration | rule sets and system-wide settings |
| S-14 | Audit, logging & monitoring | the record of what happened and alerts when it goes wrong |
| S-14.1 | Audit trail | activity record |
| S-14.2 | Application logging | troubleshooting and process verification |
| S-14.3 | Monitoring & event alerts | error, failure and failover alerting |

**Skeleton size: 69 nodes.** Stop condition met: every requirement in the pinned list has at least one plausible attachment point.

---

## 3. Accretion log

Order A, one row per requirement per pass. `amb` = flagged as apparently holding more than one obligation (flagged and proceeded; not resolved).

### Pass 1

| req | pass | verdict | covering node(s) | added (parent) | missing part (partial) | reason | amb |
|---|---|---|---|---|---|---|---|
| I-1 | 1 | deferred | — | — | — | roll-up over module, sharing and delivery structure that no node yet realises; retry next pass | |
| I-2 | 1 | not covered | A-001, A-002 | A-001 Single-platform module composition (S-1.1); A-002 Unified domain data model (S-1.2) | — | organisation statement: one platform, one data model, three modules | ✔ |
| I-3 | 1 | not covered | A-003 | A-003 Identifier format & check-digit rules (S-4.2) | — | the digit-length, prefix and check-digit rules are a stated rule set | |
| I-4 | 1 | not covered | A-004, A-005 | A-004 Enterprise-architecture alignment & maintainability design (S-1.1); A-005 Scalability & growth design (S-1.1) | — | property the design must hold, per assumption P3 | ✔ |
| I-5 | 1 | not covered | A-006 | A-006 Extensibility design — further data types, field-level sharing (S-1.1) | — | accommodation only; the expansion itself is out of scope (P1) | |
| I-6 | 1 | not covered | A-007, A-008 | A-007 Cross-module permission evaluation (S-2.2); A-008 Common record service layer (S-3) | — | one authorisation mechanism across modules, one shared service layer (P3) | |
| I-7 | 1 | not covered | A-009, A-010 | A-009 Configurable validation rule set (S-13.2); A-010 Validation service on all record operations (S-3.3) | — | rules as configuration, validation as behaviour (P3) | |
| I-8 | 1 | deferred | — | — | — | roll-up over Access Data functions not yet realised; retry next pass | |
| I-9 | 1 | not covered | A-011, A-012 | A-011 Subscription entitlement model (S-8.4); A-012 Entitlement enforcement on view and export (S-7) | — | the subscription defines scope; something must enforce it | |
| I-10 | 1 | not covered | A-013 | A-013 Anonymous public search, limited set, no export (S-7.4) | — | anonymous case of the same module (P3) | |
| I-11 | 1 | deferred | — | — | — | needs the access-path structure of D-1/D-4 before the data set can be placed against it | |
| G-1 | 1 | not covered | A-014, A-015 | A-014 Role assignment to users (S-2.2); A-015 Task assignment to users (S-2.2) | — | "roles and tasks" are two assignments; tasks are workflow responsibilities (P3) | ✔ |
| G-1.1 | 1 | not covered | A-016, A-017 | A-016 Company administrator designation (S-2.1); A-017 User account administration in a company (S-2.1) | — | designation and the administration it enables are distinct | |
| G-1.2 | 1 | partially covered | A-014, A-015, A-018 | A-018 Company-scoped administration rights (S-2.1) | the restriction of the admin's reach to their own company | assignment mechanism already exists; its scoping did not | |
| G-1.3 | 1 | not covered | A-019 | A-019 Configurable role catalogue with the four named roles (S-2.2) | — | "other roles may be added" = configurable set (P3) | |
| G-1.4 | 1 | not covered | A-020 | A-020 X-Customer-level Super-User scope (S-2.2) | — | a scope above any single company | |
| G-2 | 1 | not covered | A-021 | A-021 Role-driven UI composition (S-2.4) | — | interface composed from role | |
| G-3 | 1 | not covered | A-022 | A-022 Record approval workflow (S-3.1) | — | the workflow itself | |
| G-3.1 | 1 | partially covered | A-014, A-023 | A-023 Approval rule configuration per company (S-3.1) | the rules for record approval | role designation is A-014; the rules were nowhere | |
| G-3.2 | 1 | not covered | A-024, A-025 | A-024 Approval-status change notification trigger (S-3.1); A-025 Notification delivery engine (S-11.1) | — | a status change must raise an event and something must deliver it | |
| G-3.3 | 1 | not covered | A-026 | A-026 Action queue, "records requiring my action" (S-3.1) | — | finding one's own pending work | |
| G-4 | 1 | not covered | A-027, A-028 | A-027 Password reset initiation, self/admin/help desk, executed by IdM (S-2.3); A-028 Help-desk cross-company user-support scope (S-2.1) | — | three initiators, one of which is not a company user and needs its own scope | |
| G-5 | 1 | not covered | A-029 | A-029 Record edit lock (S-3.2) | — | single-writer exclusion | |
| G-6 | 1 | not covered | A-030 | A-030 User dashboard with notification, report and prefix panels (S-10.1) | — | "and other information" names nothing and adds nothing (P3) | |
| G-6.1 | 1 | not covered | A-031 | A-031 Prefix capacity counter (S-4.1) | — | used vs available indicators against the licensed prefix | |
| G-7 | 1 | not covered | A-032 | A-032 Report generation service (S-10.2) | — | the generation capability | |
| G-7.1 | 1 | partially covered | A-032, A-033, A-034, A-035 | A-033 Report definition & customisation (S-10.2); A-034 Report scheduling (S-10.2); A-035 Change-activity report set (S-10.2) | customisation, scheduling, and the adds/changes/deletes definitions | running and viewing existed; the rest did not | ✔ |
| G-7.2 | 1 | not covered | A-036 | A-036 API usage reports from the API-management analytics feed (S-10.2) | — | figures are read from 3scale, not produced here (P2) | |
| G-7.3 | 1 | not covered | A-037 | A-037 Report run history (S-10.2) | — | history of runs is its own store | |
| G-7.4 | 1 | not covered | A-038 | A-038 Audit report set over the audit trail (S-10.2) | — | reports whose source is the audit trail | |
| G-8 | 1 | partially covered | A-025, A-039, A-040, A-041 | A-039 Email channel adapter (S-11.1); A-040 SMS channel adapter (S-11.1); A-041 Onscreen notification centre (S-11.1) | the three delivery channels | the engine existed from G-3.2; the channels did not | |
| G-8.1 | 1 | not covered | A-042 | A-042 Global broadcast notifications (S-11.2) | — | X-Customer to all users | |
| G-8.2 | 1 | not covered | A-043 | A-043 Member subscription to record-event notifications (S-11.2) | — | user opts in to record events | |
| G-8.3 | 1 | not covered | A-044 | A-044 Member-to-member and member-to-X-Customer messages, incl. record challenge (S-11.2) | — | two directions stated in one entry | ✔ |
| G-8.5 | 1 | not covered | A-045 | A-045 User communication preferences (S-11.3) | — | method and frequency held per user | |
| G-9 | 1 | not covered | A-046 | A-046 Feedback submission and routing to a configured address (S-11.4) | — | delivered by email to one address (P3) | |
| G-10 | 1 | not covered | A-047 | A-047 Contextual help display (S-12.1) | — | help surfaced in context | |
| G-10.1 | 1 | not covered | A-048, A-049 | A-048 Industry-variant help content (S-12.2); A-049 Industry configuration store (S-13.1) | — | the variant content and the industry dimension it is keyed by | |
| G-10.2 | 1 | not covered | A-050 | A-050 In-application help content editor for non-technical staff (S-12.2) | — | authoring without technical resources | |
| G-11 | 1 | not covered | A-051 | A-051 Configurable training link set (S-12.3) | — | links only; training material is out of scope (P1) | |
| G-12 | 1 | not covered | A-052, A-053 | A-052 Record import service (S-9.2); A-053 Record export service (S-9.3) | — | the two directions | |
| G-12.1 | 1 | not covered | A-054–A-060 | A-054 Excel adapter, A-055 CSV, A-056 Numbers, A-057 XML, A-058 Tab-delimited, A-059 IDoc (all S-9.1); A-060 API import/export path (S-1.3) | — | six formats, each its own adapter, plus the API (P3) | ✔ |
| G-12.2 | 1 | not covered | A-061 | A-061 PC/Mac encoding and line-ending handling (S-9.1) | — | variants inside the adapters, not further formats (P3); no node yet handled them | |
| G-12.3 | 1 | not covered | A-062 | A-062 Record selection for import/export, single and multiple (S-9) | — | selection is distinct from the transfer | |
| G-12.4 | 1 | partially covered | A-010, A-063 | A-063 Import validation step (S-9.2) | validation applied at the point of import | the rule evaluation existed; its application on import did not | |
| G-13 | 1 | not covered | A-064, A-065 | A-064 Publication service (S-8.1); A-065 Subscription service (S-8.4) | — | the two sides of the stated model | |
| G-13.1 | 1 | not covered | A-066 | A-066 Publication at any hierarchy level (S-8.1) | — | level-independent publication | |
| G-13.2 | 1 | not covered | A-067 | A-067 Basic/full attribute scope of publication (S-8.1) | — | the scope choice | |
| G-13.3 | 1 | not covered | A-068 | A-068 Bulk publication for a set of records (S-8.1) | — | group publication | |
| G-13.4 | 1 | not covered | A-069, A-070, A-071 | A-069 Share targets: individual, group, controlled group, public (S-8.2); A-070 User-defined sharing groups (S-8.2); A-071 X-Customer-controlled groups registry & membership (S-8.2) | — | four targets, two of which are group constructs that must exist | ✔ |
| G-13.5 | 1 | partially covered | A-011, A-065, A-072 | A-072 Published-record view, basic/full (S-7.2) | the viewing itself | entitlement existed; nothing rendered the data | |
| G-13.6 | 1 | not covered | A-073 | A-073 View-access request by consumer (S-7.3) | — | the request path | |
| G-13.7 | 1 | not covered | A-074 | A-074 View-request approval/rejection by owner (S-8.3) | — | the owner decision | |
| P-1 | 1 | partially covered | A-075, A-076, A-077, A-078, A-052, A-049 | A-075 GIN record creation, individual (S-5.1); A-076 GIN creation wizard (S-5.1); A-077 GIN record cloning (S-5.1); A-078 GIN attribute model, required/optional, industry-varied (S-5.1) | individual creation, wizard, cloning, the attribute model | the import path and the industry dimension existed; the GIN-specific creation and attributes did not | ✔ |
| P-1.1 | 1 | not covered | A-079 | A-079 Draft state for incomplete records (S-3.4) | — | shared node: draft is identical for both record kinds | |
| P-2 | 1 | partially covered | A-003, A-080, A-081, A-082 | A-080 Identifier assignment engine, auto/manual, at any point (S-4.2); A-081 Automatic check-digit computation (S-4.2); A-082 GIN pool within licensed prefix (S-4.2) | the assignment act, the check-digit computation, the GIN pool | I-3 gave the rules only | ✔ |
| P-2.1 | 1 | not covered | A-083 | A-083 GIN assignment-mode preference (S-4.2) | — | the stored choice | |
| P-2.2 | 1 | not covered | A-084 | A-084 Identifier reservation, held out from auto-assign (S-4.3) | — | shared node: reservation is identical for GIN and LN | |
| P-3 | 1 | covered | A-083 | — | — | P-3 and P-2.1 state the same obligation; one node realises both ids, no addition | |
| P-4 | 1 | not covered | A-085 | A-085 Record edit before finalisation (S-3) | — | shared node: pre-commit editing is common to both kinds | |
| P-5 | 1 | partially covered | A-085, A-052, A-086 | A-086 Update of existing records via import (S-9.2) | update-by-import semantics | manual editing and import ingestion existed; updating existing records by import did not | |
| P-5.1 | 1 | not covered | A-087 | A-087 Status-based attribute editability rules (S-3.4) | — | stated for product records only; no LN twin in the list | |
| P-5.2 | 1 | not covered | A-088 | A-088 Identifier-change back-reference (S-4.3) | — | shared node: the same back-reference serves P-5.2 and L-5.1 | |
| P-6 | 1 | not covered | A-089 | A-089 Product image upload and attachment (S-5.1) | — | images are product-only in the list | |
| P-7 | 1 | not covered | A-090 | A-090 Record list view with filter and sort (S-3.7) | — | shared node across both record kinds | |
| P-7.1 | 1 | not covered | A-091 | A-091 Single-record selection and action (S-3.7) | — | shared node | |
| P-7.2 | 1 | not covered | A-092 | A-092 Multi-record selection and bulk action (S-3.7) | — | shared node | |
| P-8 | 1 | not covered | A-093 | A-093 GIN inventory view (S-5) | — | a view over identifiers, not records; per-kind | |
| P-9 | 1 | not covered | A-094 | A-094 Duplicate review and resolution (S-3.6) | — | shared node | |
| P-9.1 | 1 | not covered | A-095, A-096 | A-095 Duplicate alert during creation (S-3.6); A-096 Duplicate report over completed records (S-3.6) | — | two different moments stated in one entry | ✔ |
| P-10 | 1 | not covered | A-097 | A-097 Record/identifier status view and management (S-3.4) | — | shared node | |
| P-10.1 | 1 | not covered | A-098, A-099 | A-098 GIN status model, Reserved/In Use/For Reuse/Available (S-4.3); A-099 Record-status → identifier-status propagation (S-4.3) | — | the value set is per-kind; the propagation is shared | ✔ |
| P-10.2 | 1 | not covered | A-100 | A-100 Record status model (S-3.4) | — | shared node | |
| P-10.3 | 1 | partially covered | A-101, A-102, A-049 | A-101 Retirement and reuse dates (S-4.3); A-102 Reuse-interval rules by industry and product type (S-13.1) | the dates displayed and the rules that set them | the industry store existed; the reuse rules and dates did not | |
| P-11 | 1 | partially covered | A-103, A-104, A-105 | A-103 Hierarchy model, manual create/edit/view (S-3.8); A-104 Visual drag-and-drop hierarchy editor (S-3.8); A-105 Hierarchy import path (S-9.2) | manual editing, the visual editor, the hierarchy import path | generic import existed; nothing carried hierarchy | |
| P-11.1 | 1 | not covered | A-106 | A-106 GIN hierarchy level scheme — each, case, pallet (S-5.2) | — | pre-defined levels are per-kind (P3) | |
| P-11.2 | 1 | partially covered | A-105, A-107 | A-107 Import modes: full record with hierarchy, or hierarchy-only (S-9.2) | the two import modes | the path existed, the mode distinction did not | |
| P-11.3 | 1 | not covered | A-108 | A-108 Physical-fit check between adjacent levels, height and weight (S-5.2) | — | product-only rule | |
| P-11.4 | 1 | not covered | A-109 | A-109 Item-level change during hierarchy creation (S-5.2) | — | item level exists only in the GIN scheme | |
| P-11.5 | 1 | partially covered | A-110, A-025 | A-110 Hierarchy status-impact evaluation and notification (S-3.8) | the impact evaluation across the hierarchy | delivery existed; nothing decided that an impact occurred | |
| P-12 | 1 | partially covered | A-053, A-111 | A-111 Hierarchy export and print layout (S-3.8) | the user-friendly hierarchy layout | record export existed; hierarchy shape did not | |
| P-13 | 1 | not covered | A-112, A-113 | A-112 Barcode generation via barcode library, four symbologies, selectable sizes (S-5.3); A-113 Barcode preview (S-5.3) | — | generation and viewing are two obligations in one entry; library is used, not built (P2) | ✔ |
| P-14 | 1 | not covered | A-114 | A-114 Barcode export and print as PNG and SVG (S-5.3) | — | image output distinct from generation | |
| P-15 | 1 | not covered | A-115 | A-115 Product Information Sheet generate, save, export, print (S-5.4) | — | one artefact with four operations on it | ✔ |
| P-15.1 | 1 | not covered | A-116 | A-116 Product sheet layout templates, selectable and editable (S-5.4) | — | templates are their own content | |
| P-16 | 1 | not covered | A-117 | A-117 Digital GIN embeddable snippet, QR plus structured markup (S-5.5) | — | no resolver service behind it (P3) | |
| P-17 | 1 | covered | A-064, A-072 | — | — | publication service plus the

Access Data view already realise this; no addition |  |
| P-18 | 1 | not covered | A-118 | A-118 Record ownership transfer (S-3.5) | — | shared node; transfer is identical for both kinds | |
| P-19 | 1 | covered | A-052, A-060 | — | — | external systems arrive through the import service and the API; no bespoke connector (P3) | |
| L-1 | 1 | partially covered | A-119, A-120, A-121, A-122, A-052, A-049 | A-119 LN record creation, individual (S-6.1); A-120 LN creation wizard (S-6.1); A-121 LN record cloning (S-6.1); A-122 LN attribute model, industry-varied (S-6.1) | LN-specific creation flows and attribute model | import and industry configuration are shared; the creation flows follow the kind's attribute model and are per-kind | ✔ |
| L-1.1 | 1 | covered | A-079 | — | — | shared draft node already realises it | |
| L-2 | 1 | partially covered | A-003, A-080, A-081, A-123 | A-123 LN pool within licensed prefix (S-4.2) | the LN number pool | rules, assignment engine and check digit are shared; the pool is per-kind | ✔ |
| L-2.1 | 1 | partially covered | A-049, A-124 | A-124 Shared LN pool with industry-driven automatic assignment (S-4.2) | the shared pool and its industry trigger | industry configuration existed; the shared-pool construct did not | |
| L-2.2 | 1 | not covered | A-125 | A-125 LN assignment-mode preference at prefix-licensee level (S-4.2) | — | held at licensee level, not user level; per-kind | |
| L-2.3 | 1 | covered | A-084 | — | — | shared reservation node already realises it | |
| L-3 | 1 | covered | A-125 | — | — | L-3 and L-2.2 state the same obligation; one node realises both ids | |
| L-4 | 1 | covered | A-085 | — | — | shared pre-commit edit node | |
| L-5 | 1 | covered | A-085, A-052, A-086 | — | — | manual edit, import ingestion and update-by-import all already realised | |
| L-5.1 | 1 | covered | A-088 | — | — | shared back-reference node | |
| L-6 | 1 | covered | A-090 | — | — | shared list view | |
| L-6.1 | 1 | covered | A-091 | — | — | shared single selection | |
| L-6.2 | 1 | covered | A-092 | — | — | shared multi selection | |
| L-7 | 1 | not covered | A-126 | A-126 LN inventory view (S-6) | — | identifier view, per-kind, twin of P-8 | |
| L-8 | 1 | covered | A-094 | — | — | shared duplicate resolution | |
| L-8.1 | 1 | covered | A-095, A-096 | — | — | shared alert and duplicate report | ✔ |
| L-9 | 1 | covered | A-097 | — | — | shared status view and management | |
| L-9.1 | 1 | partially covered | A-127, A-099 | A-127 LN status model (S-4.3) | the LN status value set and its transitions | propagation is shared; the value set is per-kind | ✔ |
| L-9.2 | 1 | covered | A-100 | — | — | shared record status model | |
| L-9.3 | 1 | covered | A-101, A-102 | — | — | dates and industry reuse rules already realised | |
| L-10 | 1 | covered | A-103, A-104, A-105 | — | — | hierarchy model, visual editor and import path are shared | |
| L-10.1 | 1 | not covered | A-128 | A-128 LN hierarchy: unlimited depth, attribute-organised (S-6.2) | — | depth and organisation rules differ from the GIN scheme (P3) | |
| L-10.2 | 1 | covered | A-105, A-107 | — | — | shared import modes | |
| L-10.3 | 1 | covered | A-110 | — | — | shared hierarchy status-impact node | |
| L-11 | 1 | covered | A-053, A-111 | — | — | shared hierarchy export/print layout | |
| L-12 | 1 | covered | A-064, A-072 | — | — | publication and published view already realised | |
| L-13 | 1 | not covered | A-129, A-130 | A-129 Annual verification record — who, when, outcome (S-6.3); A-130 Verification-due view (S-6.3) | — | the system records and can show what is due; it runs no campaign (P3) | |
| L-14 | 1 | covered | A-118 | — | — | shared ownership transfer | |
| L-15 | 1 | covered | A-052, A-060 | — | — | same paths as P-19 | |
| D-1 | 1 | not covered | A-131 | A-131 Access Data search over prefix, GIN and LN (S-7.1) | — | search reads the non-transactional store (P3) | |
| D-1.1 | 1 | not covered | A-132 | A-132 Field-level search (S-7.1) | — | named fields as search entries | |
| D-1.2 | 1 | not covered | A-133 | A-133 Advanced search and filter (S-7.1) | — | distinct from simple field search | |
| D-2 | 1 | partially covered | A-073, A-134 | A-134 Basic/full scope selection on an access request (S-7.3) | the scope choice carried on the request | the request path existed; it carried no scope | |
| D-2.1 | 1 | covered | A-074, A-011 | — | — | owner approval and the entitlement it creates already realised | |
| D-3 | 1 | not covered | A-135 | A-135 Controlled-group membership request and X-Customer approval (S-7.3) | — | a different approver from D-2.1; uses the registry A-071 | |
| D-4 | 1 | partially covered | A-072, A-136 | A-136 Published hierarchy view (S-7.2) | the hierarchy view for consumers | basic/full record view existed; hierarchy rendering did not | |
| D-5 | 1 | covered | A-053, A-062, A-012, A-054–A-060 | — | — | export service, selection, entitlement gate and the format adapters already realise it | |
| D-6 | 1 | not covered | A-137 | A-137 Record print output, one or more records (S-7.5) | — | print is not export | |
| D-7 | 1 | partially covered | S-7 (own residue), A-138 | A-138 Access Data REST API (S-1.3) | the API channel | the web channel is realised by S-7's subtree; the both-channels constraint is S-7's own residue, delegated to no child | |
| D-8 | 1 | not covered | A-139 | A-139 Pay-for-ad-hoc-access information page (S-7) | — | informational only; nothing transactional (P1, P3) | |
| NFR-2 | 1 | partially covered | A-140, A-141, A-142, A-005 | A-140 Non-transactional read store (S-1.2); A-141 Near-real-time feed to the read store (S-1.2); A-142 Transactional store schema (S-1.2) | the two stores and the feed between them | growth capacity was already a design statement; the stores were not | ✔ |
| NFR-3 | 1 | partially covered | A-143, A-144, A-007, A-019 | A-143 Claims-based IdM integration and SSO (S-2.3); A-144 Claim-to-role mapping (S-2.3) | the claims exchange and the mapping onto the application's roles | authorisation and the role catalogue existed; the IdM exchange did not | ✔ |
| NFR-4 | 1 | partially covered | A-145, A-146, A-060, A-138 | A-145 Internal REST service layer, no direct database access (S-1.3); A-146 Member-facing REST API registered with the API-management platform (S-1.3) | the internal service layer and the managed member-facing API | two API surfaces existed; the architectural rule and the registration did not | ✔ |
| NFR-5 | 1 | not covered | A-147, A-148 | A-147 Technical-standards conformance design (S-1.1); A-148 Deviation register with impact analysis (S-1.1) | — | the entry states adherence and a deviation procedure; both are design artefacts here | ✔ |
| NFR-6 | 1 | not covered | A-149 | A-149 Cloud-readiness design (S-1.1) | — | property the design must hold (P3) | |
| NFR-7 | 1 | partially covered | A-150, A-005 | A-150 Web client on standard patterns, zero client-side installation (S-1.4) | the web client itself and the no-install constraint | the volume figures were already a design statement | ✔ |
| NFR-8 | 1 | not covered | A-151, A-152, A-153 | A-151 High-availability design to the stated service level (S-1.5); A-152 Failover process design with identified hardware and software needs (S-1.5); A-153 Failover monitoring with administrator alerting (S-14.3) | — | three obligations: the level, the process, the monitoring | ✔ |
| NFR-9 | 1 | not covered | A-154 | A-154 Backup and disaster-recovery design conforming to X-Customer policy (S-1.5) | — | part of the product's operational design (P3) | |
| NFR-10 | 1 | not covered | A-155, A-156 | A-155 Security design — controls, configuration, procedures (S-1.5); A-156 Security components, frameworks and libraries (S-1.5) | — | the design and the things it is built from are separately named | ✔ |
| NFR-13 | 1 | not covered | A-157 | A-157 Browser compatibility set (S-1.4) | — | an enumerated support matrix | |
| NFR-14 | 1 | not covered | A-158 | A-158 Response-time design targets under stated concurrency (S-1.5) | — | property the design must meet (P3) | |
| NFR-16 | 1 | partially covered | A-022, A-160, A-010, A-063, A-161, A-159 | A-159 Record verification workflow (S-3.1); A-160 Submission of imported records into approval (S-9.2); A-161 Identifier compliance validation (S-3.3) | the verification workflow, the import→approval submission path, identifier-level compliance checking | approval and generic validation existed; the third workflow and the import entry into approval did not | ✔ |
| NFR-17 | 1 | partially covered | A-162, A-025 | A-162 System-error event detection and administrator notification (S-14.3) | detection of the error condition | delivery existed; nothing raised the event | |
| NFR-18 | 1 | partially covered | A-163, A-025 | A-163 Critical business-function failure alerting (S-14.3) | detection of a failed business function | as above, a different trigger source | |
| NFR-19 | 1 | not covered | A-164 | A-164 Application logging (S-14.2) | — | logging is not the audit trail | |
| NFR-20 | 1 | not covered | A-165 | A-165 System-wide audit trail (S-14.1) | — | activity record at any point in the system | |
| NFR-21 | 1 | not covered | A-166 | A-166 WCAG 2.0 Level A conformance in the web client (S-1.4) | — | conformance property of the client | |

**Pass 1: 166 nodes added (A-001 – A-166), 3 deferrals (I-1, I-8, I-11).**

### Pass 2 — the deferred entries only, in declared order

| req | pass | verdict | covering node(s) | added (parent) | missing part (partial) | reason | amb |
|---|---|---|---|---|---|---|---|
| I-1 | 2 | covered | A-150 (web delivery); A-075, A-076, A-077, A-078 (create GIN data); A-119, A-120, A-121, A-122 (create LN data); A-085, A-090, A-097 (manage); A-031, A-082, A-123 (prefix data as members use it); A-064, A-065 (share) | — | — | the structure now realises every part; "replacing the applications currently available" is a scope statement on the artefact, not a further component (P3) — it is realised by the same set | ✔ |
| I-8 | 2 | covered | A-131 (search), A-072 and A-136 (view), A-053 and A-012 (export under entitlement), S-7 own residue (the module contains no editing) | — | — | the negative composition constraint is residue at S-7 because no child realises an absence | |
| I-11 | 2 | partially covered | A-167, A-131, A-072 | A-167 X-Customer-owned reference data — prefix registry, controlled groups — held in the access read store under the same access rules (S-1.2) | the X-Customer-owned data set itself | the access path existed after pass 1; the data set in the store did not | |

**Pass 2: 1 node added (A-167), 0 deferrals.**

### Pass 3

| req | pass | verdict | covering node(s) | added | missing | reason |
|---|---|---|---|---|---|---|
| — | 3 | — | — | none | — | no unresolved requirement remains; the pass adds nothing and defers nothing. Accretion fixpoint. |

---

## 4. Completion log

Derived nodes only. None covers a requirement.

| node | name | parent | trigger | justification | pass |
|---|---|---|---|---|---|
| C-001 | Session establishment, carriage and termination | S-2.3 | A-143 | claims arrive once at sign-on; nothing states how the authenticated session is carried across requests or ended | 1 |
| C-002 | Member/company registry as ownership and administration scope | S-2.1 | A-016, A-018, A-118 | company-scoped administration and record ownership both presuppose a company entity the list never defines; populated outside the product, since onboarding is out of scope | 1 |
| C-003 | Notification templates per channel | S-11.1 | A-025, A-039, A-040, A-041 | every notification type must render differently for email, SMS and screen; no entry names the rendering | 1 |
| C-004 | Notification delivery retry and failure handling | S-11.1 | A-039, A-040 | delivery depends on an external relay and an external gateway, either of which can refuse | 1 |
| C-005 | Asynchronous job execution | S-1 | A-034, A-052, A-141 | scheduled reports, bulk imports and the store feed cannot run inside a request | 1 |
| C-006 | Import staging, per-record error report, rollback | S-9.2 | A-052, A-063 | validating all records on import implies a per-record outcome and a decision about partial batches | 1 |
| C-007 | Export artefact production and download | S-9.3 | A-053 | an export of many records is produced, held and fetched; the entry states only the capability | 1 |
| C-008 | Binary and file storage service | S-1.2 | A-089, A-114, A-115 | product images, barcode images and sheets are binary content the record stores do not hold | 1 |
| C-009 | Read-store index build and maintenance | S-1.2 | A-131, A-141 | search over a continuously fed store requires an index that is built and kept current | 1 |
| C-010 | Configuration change propagation | S-13.2 | A-009, A-049 | rule sets and industry configuration change while the system runs; consumers must observe the change | 1 |
| C-011 | API versioning and deprecation | S-1.3 | A-146 | an API published to members outlives any single shape of it | 1 |
| C-012 | Machine-client API credentials | S-1.3 | A-138, A-146, A-143 | browser single sign-on does not serve a machine client calling the API | 1 |
| C-013 | Error and validation-message presentation | S-1.4 | A-010, A-150 | validation produces outcomes that must reach the user; no entry says how failure is shown | 1 |
| C-014 | Identifier allocation concurrency control | S-4.2 | A-080, A-082, A-123, A-124 | auto-assignment from pools — one of them shared across companies — must not issue a number twice | 1 |
| C-015 | Record ownership relation | S-3.5 | A-118, A-064 | the transfer of ownership and publication by "the data owner" are stated; the relation they act on is not | 1 |
| C-016 | Audit store retention and immutability | S-14.1 | A-165, A-154 | an audit trail of all activity implies a retention rule and protection from alteration | 1 |
| C-017 | X-Customer staff maintenance console | S-13 | A-050, A-042, A-139, A-102, A-009 | several stated maintenance functions are performed by X-Customer staff and have no stated home | 1 |
| C-018 | Job status view | S-1 | C-005 | asynchronous work whose outcome nobody can see is not usable; triggered by a derived node | 2 |
| C-019 | Storage lifecycle for import files and export artefacts | S-1.2 | C-007, C-008 | retained input and output files accumulate and need a defined end; triggered by derived nodes | 2 |
| C-020 | Published-scope index schema, basic and full | S-1.2 | C-009, A-067 | the index must distinguish the basic and full attribute scopes or entitlement cannot be applied at search time | 2 |

**Completion pass 3 added nothing. Completion fixpoint.**

---

## 5. Convergence trace

| phase | pass | nodes added | deferrals |
|---|---|---|---|
| accretion | 1 | 166 | 3 |
| accretion | 2 | 1 | 0 |
| accretion | 3 | 0 | 0 |
| completion | 1 | 17 | — |
| completion | 2 | 3 | — |
| completion | 3 | 0 | — |

Both fixpoints reached zero.

---

## 6. Final model

Post-closure, post-normalisation. Provenance uses the M4 origin labels; the mapping to the output format's two-value scheme is `accreted` = stated, `posited` and `derived` = implied. Own coverage only; total coverage is computed and is not written out.

### Root and platform

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| S-0 | SAS member application solution | — | posited | ∅ |
| S-1 | Platform & architecture | S-0 | posited | ∅ |
| S-1.1 | Architecture & technical standards | S-1 | posited | ∅ |
| A-001 | Single-platform module composition | S-1.1 | accreted | I-2 |
| A-004 | Enterprise-architecture alignment & maintainability design | S-1.1 | accreted | I-4 |
| A-005 | Scalability & growth design | S-1.1 | accreted | I-4, NFR-2, NFR-7 |
| A-006 | Extensibility design — further data types, field-level sharing | S-1.1 | accreted | I-5 |
| A-147 | Technical-standards conformance design | S-1.1 | accreted | NFR-5 |
| A-148 | Deviation register with impact analysis | S-1.1 | accreted | NFR-5 |
| A-149 | Cloud-readiness design | S-1.1 | accreted | NFR-6 |
| S-1.2 | Data stores | S-1 | posited | ∅ |
| A-002 | Unified domain data model | S-1.2 | accreted | I-2 |
| A-140 | Non-transactional read store (data mart) | S-1.2 | accreted | NFR-2 |
| A-141 | Near-real-time feed to the read store | S-1.2 | accreted | NFR-2 |
| A-142 | Transactional store schema | S-1.2 | accreted | NFR-2 |
| A-167 | X-Customer-owned reference data in the access read store | S-1.2 | accreted | I-11 |
| C-008 | Binary and file storage service | S-1.2 | derived | ∅ |
| C-009 | Read-store index build and maintenance | S-1.2 | derived | ∅ |
| C-019 | Storage lifecycle for import files and export artefacts | S-1.2 | derived | ∅ |
| C-020 | Published-scope index schema | S-1.2 | derived | ∅ |
| S-1.3 | Service & API layer | S-1 | posited | ∅ |
| A-060 | API import/export path | S-1.3 | accreted | G-12.1, P-19, L-15, D-5, NFR-4 |
| A-138 | Access Data REST API | S-1.3 | accreted | D-7, NFR-4 |
| A-145 | Internal REST service layer, no direct database access | S-1.3 | accreted | NFR-4 |
| A-146 | Member-facing REST API registered with the API-management platform | S-1.3 | accreted | NFR-4 |
| C-011 | API versioning and deprecation | S-1.3 | derived | ∅ |
| C-012 | Machine-client API credentials | S-1.3 | derived | ∅ |
| S-1.4 | Web client foundation | S-1 | posited | ∅ |
| A-150 | Web client on standard patterns, zero client-side installation | S-1.4 | accreted | NFR-7, I-1 |
| A-157 | Browser compatibility set | S-1.4 | accreted | NFR-13 |
| A-166 | WCAG 2.0 Level A conformance | S-1.4 | accreted | NFR-21 |
| C-013 | Error and validation-message presentation | S-1.4 | derived | ∅ |
| S-1.5 | Operational design | S-1 | posited | ∅ |
| A-151 | High-availability design to the stated service level | S-1.5 | accreted | NFR-8 |
| A-152 | Failover process design with identified hardware and software needs | S-1.5 | accreted | NFR-8 |
| A-154 | Backup and disaster-recovery design | S-1.5 | accreted | NFR-9 |
| A-155 | Security design | S-1.5 | accreted | NFR-10 |
| A-156 | Security components, frameworks and libraries | S-1.5 | accreted | NFR-10 |
| A-158 | Response-time design targets under stated concurrency | S-1.5 | accreted | NFR-14 |
| C-005 | Asynchronous job execution | S-1 | derived | ∅ |
| C-018 | Job status view | S-1 | derived | ∅ |

### Identity & access

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| S-2 | Identity & access | S-0 | posited | ∅ |
| S-2.1 | Company & user administration | S-2 | posited | ∅ |
| A-016 | Company administrator designation | S-2.1 | accreted | G-1.1 |
| A-017 | User account administration within a company | S-2.1 | accreted | G-1.1 |
| A-018 | Company-scoped administration rights | S-2.1 | accreted | G-1.2 |
| A-028 | Help-desk cross-company user-support scope | S-2.1 | accreted | G-4 |
| C-002 | Member/company registry as ownership and administration scope | S-2.1 | derived | ∅ |
| S-2.2 | Roles & permissions | S-2 | posited | ∅ |
| A-007 | Cross-module permission evaluation | S-2.2 | accreted | I-6, NFR-3 |
| A-014 | Role assignment to users | S-2.2 | accreted | G-1, G-1.2, G-3.1 |
| A-015 | Task (workflow responsibility) assignment to users | S-2.2 | accreted | G-1, G-1.2 |
| A-019 | Configurable role catalogue | S-2.2 | accreted | G-1.3, NFR-3 |
| A-020 | X-Customer-level Super-User scope | S-2.2 | accreted | G-1.4 |
| S-2.3 | Authentication & IdM integration | S-2 | posited | ∅ |
| A-027 | Password reset initiation, executed by the IdM | S-2.3 | accreted | G-4 |
| A-143 | Claims-based IdM integration and single sign-on | S-2.3 | accreted | NFR-3 |
| A-144 | Claim-to-role mapping | S-2.3 | accreted | NFR-3 |
| C-001 | Session establishment, carriage and termination | S-2.3 | derived | ∅ |
| A-021 | Role-driven UI composition | S-2 | accreted | G-2 |

### Shared record services

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| S-3 | Shared record services | S-0 | posited | ∅ |
| A-008 | Common record service layer shared by the three modules | S-3 | accreted | I-6 |
| A-085 | Record edit before finalisation | S-3 | accreted | P-4, P-5, L-4, L-5, I-1 |
| A-029 | Record edit lock | S-3 | accreted | G-5 |
| S-3.1 | Record workflow & approval | S-3 | posited | ∅ |
| A-022 | Record approval workflow | S-3.1 | accreted | G-3, NFR-16 |
| A-023 | Approval rule configuration per company | S-3.1 | accreted | G-3.1 |
| A-024 | Approval-status change notification trigger | S-3.1 | accreted | G-3.2 |
| A-026 | Action queue — records requiring my action | S-3.1 | accreted | G-3.3 |
| A-159 | Record verification workflow | S-3.1 | accreted | NFR-16 |
| S-3.3 | Validation & business rules | S-3 | posited | ∅ |
| A-010 | Validation service on all record operations | S-3.3 | accreted | I-7, G-12.4, NFR-16 |
| A-161 | Identifier compliance validation | S-3.3 | accreted | NFR-16 |
| S-3.4 | Record status | S-3 | posited | ∅ |
| A-079 | Draft state for incomplete records | S-3.4 | accreted | P-1.1, L-1.1 |
| A-087 | Status-based attribute editability | S-3.4 | accreted | P-5.1 |
| A-097 | Record/identifier status view and management | S-3.4 | accreted | P-10, L-9, I-1 |
| A-100 | Record status model | S-3.4 | accreted | P-10.2, L-9.2 |
| S-3.5 | Record ownership | S-3 | posited | ∅ |
| A-118 | Record ownership transfer | S-3.5 | accreted | P-18, L-14 |
| C-015 | Record ownership relation | S-3.5 | derived | ∅ |
| S-3.6 | Duplicate detection | S-3 | posited | ∅ |
| A-094 | Duplicate review and resolution | S-3.6 | accreted | P-9, L-8 |
| A-095 | Duplicate alert during creation | S-3.6 | accreted | P-9.1, L-8.1 |
| A-096 | Duplicate report over completed records | S-3.6 | accreted | P-9.1, L-8.1 |
| S-3.7 | Record list & view framework | S-3 | posited | ∅ |
| A-090 | Record list view with filter and sort | S-3.7 | accreted | P-7, L-6, I-1 |
| A-091 | Single-record selection and action | S-3.7 | accreted | P-7.1, L-6.1 |
| A-092 | Multi-record selection and bulk action | S-3.7 | accreted | P-7.2, L-6.2 |
| S-3.8 | Hierarchy framework | S-3 | posited | ∅ |
| A-103 | Hierarchy model, manual create/edit/view | S-3.8 | accreted | P-11, L-10 |
| A-104 | Visual drag-and-drop hierarchy editor | S-3.8 | accreted | P-11, L-10 |
| A-110 | Hierarchy status-impact evaluation and notification | S-3.8 | accreted | P-11.5, L-10.3 |
| A-111 | Hierarchy export and print layout | S-3.8 | accreted | P-12, L-11 |

### Identifier management

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| S-4 | Identifier management | S-0 | posited | ∅ |
| A-031 | Prefix capacity counter | S-4 | accreted | G-6.1, I-1 |
| S-4.2 | Identifier assignment | S-4 | posited | ∅ |
| A-003 | Identifier format & check-digit rules | S-4.2 | accreted | I-3, P-2, L-2 |
| A-080 | Identifier assignment engine, auto/manual, at any point | S-4.2 | accreted | P-2, L-2 |
| A-081 | Automatic check-digit computation | S-4.2 | accreted | P-2, L-2 |
| A-082 | GIN pool within licensed prefix | S-4.2 | accreted | P-2, I-1 |
| A-083 | GIN assignment-mode preference | S-4.2 | accreted | P-2.1, P-3 |
| A-123 | LN pool within licensed prefix | S-4.2 | accreted | L-2, I-1 |
| A-124 | Shared LN pool with industry-driven automatic assignment | S-4.2 | accreted | L-2.1 |
| A-125 | LN assignment-mode preference at prefix-licensee level | S-4.2 | accreted | L-2.2, L-3 |
| C-014 | Identifier allocation concurrency control | S-4.2 | derived | ∅ |
| S-4.3 | Identifier status lifecycle | S-4 | posited | ∅ |
| A-084 | Identifier reservation | S-4.3 | accreted | P-2.2, L-2.3 |
| A-088 | Identifier-change back-reference | S-4.3 | accreted | P-5.2, L-5.1 |
| A-098 | GIN status model | S-4.3 | accreted | P-10.1 |
| A-099 | Record-status → identifier-status propagation | S-4.3 | accreted | P-10.1, L-9.1 |
| A-101 | Retirement and reuse dates | S-4.3 | accreted | P-10.3, L-9.3 |
| A-127 | LN status model | S-4.3 | accreted | L-9.1 |

### Product (GIN) module

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| S-5 | Product (GIN) module | S-0 | posited | ∅ |
| A-093 | GIN inventory view | S-5 | accreted | P-8 |
| A-117 | Digital GIN embeddable snippet | S-5 | accreted | P-16 |
| S-5.1 | GIN record management | S-5 | posited | ∅ |
| A-075 | GIN record creation, individual | S-5.1 | accreted | P-1, I-1 |
| A-076 | GIN creation wizard | S-5.1 | accreted | P-1, I-1 |
| A-077 | GIN record cloning | S-5.1 | accreted | P-1, I-1 |
| A-078 | GIN attribute model, industry-varied | S-5.1 | accreted | P-1, I-1 |
| A-089 | Product image upload and attachment | S-5.1 | accreted | P-6 |
| S-5.2 | GIN hierarchy | S-5 | posited | ∅ |
| A-106 | GIN hierarchy level scheme — each, case, pallet | S-5.2 | accreted | P-11.1 |
| A-108 | Physical-fit check, height and weight | S-5.2 | accreted | P-11.3 |
| A-109 | Item-level change during hierarchy creation | S-5.2 | accreted | P-11.4 |
| S-5.3 | Barcodes | S-5 | posited | ∅ |
| A-112 | Barcode generation, four symbologies, selectable sizes | S-5.3 | accreted | P-13 |
| A-113 | Barcode preview | S-5.3 | accreted | P-13 |
| A-114 | Barcode export and print, PNG and SVG | S-5.3 | accreted | P-14 |
| S-5.4 | Product information sheets | S-5 | posited | ∅ |
| A-115 | Product Information Sheet generate, save, export, print | S-5.4 | accreted | P-15 |
| A-116 | Product sheet layout templates | S-5.4 | accreted | P-15.1 |

### Location (LN) module

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| S-6 | Location (LN) module | S-0 | posited | ∅ |
| A-126 | LN inventory view | S-6 | accreted | L-7 |
| A-128 | LN hierarchy — unlimited depth, attribute-organised | S-6 | accreted | L-10.1 |
| S-6.1 | LN record management | S-6 | posited | ∅ |
| A-119 | LN record creation, individual | S-6.1 | accreted | L-1, I-1 |
| A-120 | LN creation wizard | S-6.1 | accreted | L-1, I-1 |
| A-121 | LN record cloning | S-6.1 | accreted | L-1, I-1 |
| A-122 | LN attribute model, industry-varied | S-6.1 | accreted | L-1, I-1 |
| S-6.3 | Location verification | S-6 | posited | ∅ |
| A-129 | Annual verification record | S-6.3 | accreted | L-13 |
| A-130 | Verification-due view | S-6.3 | accreted | L-13 |

### Access Data module

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| S-7 | Access Data module | S-0 | posited | **I-8** (the module's content is read-only — no editing capability is included), **D-7** (every module function is reachable on both the web and API channels) |
| A-012 | Entitlement enforcement on view and export | S-7 | accreted | I-9, I-8, D-5 |
| A-013 | Anonymous public search, limited set, no export | S-7 | accreted | I-10 |
| A-137 | Record print output | S-7 | accreted | D-6 |
| A-139 | Pay-for-ad-hoc-access information page | S-7 | accreted | D-8 |
| S-7.1 | Search & discovery | S-7 | posited | ∅ |
| A-131 | Access Data search over prefix, GIN and LN | S-7.1 | accreted | D-1, I-8, I-11 |
| A-132 | Field-level search | S-7.1 | accreted | D-1.1 |
| A-133 | Advanced search and filter | S-7.1 | accreted | D-1.2 |
| S-7.2 | Published record viewing | S-7 | posited | ∅ |
| A-072 | Published-record view, basic/full | S-7.2 | accreted | G-13.5, P-17, L-12, D-4, I-8, I-11 |
| A-136 | Published hierarchy view | S-7.2 | accreted | D-4, I-8 |
| S-7.3 | Consumer access requests | S-7 | posited | ∅ |
| A-073 | View-access request by consumer | S-7.3 | accreted | G-13.6, D-2 |
| A-134 | Basic/full scope selection on an access request | S-7.3 | accreted | D-2 |
| A-135 | Controlled-group membership request and approval | S-7.3 | accreted | D-3 |

### Publish & subscribe

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| S-8 | Publish & subscribe | S-0 | posited | ∅ |
| A-074 | View-request approval/rejection by owner | S-8 | accreted | G-13.7, D-2.1 |
| S-8.1 | Publication by data owner | S-8 | posited | ∅ |
| A-064 | Publication service | S-8.1 | accreted | G-13, P-17, L-12, I-1 |
| A-066 | Publication at any hierarchy level | S-8.1 | accreted | G-13.1 |
| A-067 | Basic/full attribute scope of publication | S-8.1 | accreted | G-13.2 |
| A-068 | Bulk publication for a set of records | S-8.1 | accreted | G-13.3 |
| S-8.2 | Share targets & groups | S-8 | posited | ∅ |
| A-069 | Share targets — individual, group, controlled group, public | S-8.2 | accreted | G-13.4 |
| A-070 | User-defined sharing groups | S-8.2 | accreted | G-13.4 |
| A-071 | X-Customer-controlled groups registry & membership | S-8.2 | accreted | G-13.4 |
| S-8.4 | Subscription entitlement | S-8 | posited | ∅ |
| A-011 | Subscription entitlement model | S-8.4 | accreted | I-9, G-13.5, D-2.1 |
| A-065 | Subscription service | S-8.4 | accreted | G-13, G-13.5, I-1 |

### Import & export

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| S-9 | Import & export | S-0 | posited | ∅ |
| A-062 | Record selection for import/export | S-9 | accreted | G-12.3, D-5 |
| S-9.1 | Format adapters | S-9 | posited | ∅ |
| A-054 | Excel adapter | S-9.1 | accreted | G-12.1, D-5 |
| A-055 | CSV adapter | S-9.1 | accreted | G-12.1, D-5 |
| A-056 | Numbers adapter | S-9.1 | accreted | G-12.1, D-5 |
| A-057 | XML adapter | S-9.1 | accreted | G-12.1, D-5 |
| A-058 | Tab-delimited adapter | S-9.1 | accreted | G-12.1, D-5 |
| A-059 | IDoc adapter | S-9.1 | accreted | G-12.1, D-5 |
| A-061 | PC/Mac encoding and line-ending handling | S-9.1 | accreted | G-12.2 |
| S-9.2 | Import processing | S-9 | posited | ∅ |
| A-052 | Record import service | S-9.2 | accreted | G-12, P-1, P-5, P-19, L-1, L-5, L-15 |
| A-063 | Import validation step | S-9.2 | accreted | G-12.4, NFR-16 |
| A-086 | Update of existing records via import | S-9.2 | accreted | P-5, L-5 |
| A-105 | Hierarchy import path | S-9.2 | accreted | P-11, P-11.2, L-10, L-10.2 |
| A-107 | Import modes — full record with hierarchy, or hierarchy-only | S-9.2 | accreted | P-11.2, L-10.2 |
| A-160 | Submission of imported records into approval | S-9.2 | accreted | NFR-16 |
| C-006 | Import staging, per-record error report, rollback | S-9.2 | derived | ∅ |
| S-9.3 | Export processing | S-9 | posited | ∅ |
| A-053 | Record export service | S-9.3 | accreted | G-12, P-12, L-11, D-5, I-8 |
| C-007 | Export artefact production and download | S-9.3 | derived | ∅ |

### Reporting & dashboard

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| S-10 | Reporting & dashboard | S-0 | posited | ∅ |
| A-030 | User dashboard | S-10 | accreted | G-6 |
| S-10.2 | Report engine | S-10 | posited | ∅ |
| A-032 | Report generation service | S-10.2 | accreted | G-7, G-7.1 |
| A-033 | Report definition & customisation | S-10.2 | accreted | G-7.1 |
| A-034 | Report scheduling | S-10.2 | accreted | G-7.1 |
| A-035 | Change-activity report set | S-10.2 | accreted | G-7.1 |
| A-036 | API usage reports from the analytics feed | S-10.2 | accreted | G-7.2 |
| A-037 | Report run history | S-10.2 | accreted | G-7.3 |
| A-038 | Audit report set | S-10.2 | accreted | G-7.4 |

### Notifications & communication

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| S-11 | Notifications & communication | S-0 | posited | ∅ |
| A-045 | User communication preferences | S-11 | accreted | G-8.5 |
| A-046 | Feedback submission and routing | S-11 | accreted | G-9 |
| S-11.1 | Notification engine & channels | S-11 | posited | ∅ |
| A-025 | Notification delivery engine | S-11.1 | accreted | G-3.2, G-8, P-11.5, L-10.3, NFR-17, NFR-18 |
| A-039 | Email channel adapter | S-11.1 | accreted | G-8 |
| A-040 | SMS channel adapter | S-11.1 | accreted | G-8 |
| A-041 | Onscreen notification centre | S-11.1 | accreted | G-8 |
| C-003 | Notification templates per channel | S-11.1 | derived | ∅ |
| C-004 | Notification delivery retry and failure handling | S-11.1 | derived | ∅ |
| S-11.2 | Notification types | S-11 | posited | ∅ |
| A-042 | Global broadcast notifications | S-11.2 | accreted | G-8.1 |
| A-043 | Member record-event notification subscriptions | S-11.2 | accreted | G-8.2 |
| A-044 | Member-to-member and member-to-X-Customer messages | S-11.2 | accreted | G-8.3 |

### Help, configuration, audit

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| S-12 | Help & training | S-0 | posited | ∅ |
| A-047 | Contextual help display | S-12 | accreted | G-10 |
| A-051 | Configurable training link set | S-12 | accreted | G-11 |
| S-12.2 | Help content authoring | S-12 | posited | ∅ |
| A-048 | Industry-variant help content | S-12.2 | accreted | G-10.1 |
| A-050 | In-application help content editor | S-12.2 | accreted | G-10.2 |
| S-13 | Configuration & reference data | S-0 | posited | ∅ |
| C-017 | X-Customer staff maintenance console | S-13 | derived | ∅ |
| S-13.1 | Industry configuration | S-13 | posited | ∅ |
| A-049 | Industry configuration store | S-13.1 | accreted | G-10.1, P-1, P-10.3, L-1, L-2.1 |
| A-102 | Reuse-interval rules by industry and product type | S-13.1 | accreted | P-10.3, L-9.3 |
| S-13.2 | System configuration | S-13 | posited | ∅ |
| A-009 | Configurable validation rule set | S-13.2 | accreted | I-7 |
| C-010 | Configuration change propagation | S-13.2 | derived | ∅ |
| S-14 | Audit, logging & monitoring | S-0 | posited | ∅ |
| A-164 | Application logging | S-14 | accreted | NFR-19 |
| S-14.1 | Audit trail | S-14 | posited | ∅ |
| A-165 | System-wide audit trail | S-14.1 | accreted | NFR-20 |
| C-016 | Audit store retention and immutability | S-14.1 | derived | ∅ |
| S-14.3 | Monitoring & event alerts | S-14 | posited | ∅ |
| A-153 | Failover monitoring with administrator alerting | S-14.3 | accreted | NFR-8 |
| A-162 | System-error event detection and administrator notification | S-14.3 | accreted | NFR-17 |
| A-163 | Critical business-function failure alerting | S-14.3 | accreted | NFR-18 |

---

## 7. Empty skeleton nodes

Test applied to **total** coverage at accretion convergence, never to own coverage.

**None.** All 69 posited nodes have non-empty total coverage. The reason is procedural rather than lucky: M4 requires the skeleton be posited only until every requirement has a plausible attachment point, and the list was read as a set before positing, so no branch was invented ahead of the obligations. Two candidates that a reader might expect — a prefix-licensing workflow and a legacy-data-loading branch — were deliberately **not** posited, because assumption P1 places them outside the product; had they been posited they would now appear here as wrong guesses.

## 7b. Normalisation log

Fourteen nodes resolved to a single leaf at closure and were collapsed into it. In each case the leaf takes the collapsed node's parent; no coverage moved, because every collapsed node had empty own coverage.

| collapsed node | merged into leaf | coverage carried across | leaf's new parent |
|---|---|---|---|
| S-2.4 Role-driven UI presentation | A-021 | ∅ (A-021 retains G-2) | S-2 |
| S-3.2 Record locking | A-029 | ∅ (A-029 retains G-5) | S-3 |
| S-4.1 Prefix registry & capacity | A-031 | ∅ (A-031 retains G-6.1, I-1) | S-4 |
| S-5.5 Digital GIN | A-117 | ∅ (A-117 retains P-16) | S-5 |
| S-6.2 LN hierarchy | A-128 | ∅ (A-128 retains L-10.1) | S-6 |
| S-7.4 Public (non-member) access | A-013 | ∅ (A-013 retains I-10) | S-7 |
| S-7.5 Access Data output | A-137 | ∅ (A-137 retains D-6) | S-7 |
| S-8.3 View request approval | A-074 | ∅ (A-074 retains G-13.7, D-2.1) | S-8 |
| S-10.1 Dashboard | A-030 | ∅ (A-030 retains G-6) | S-10 |
| S-11.3 Communication preferences | A-045 | ∅ (A-045 retains G-8.5) | S-11 |
| S-11.4 Application feedback | A-046 | ∅ (A-046 retains G-9) | S-11 |
| S-12.1 Contextual help | A-047 | ∅ (A-047 retains G-10) | S-12 |
| S-12.3 Training links | A-051 | ∅ (A-051 retains G-11) | S-12 |
| S-14.2 Application logging | A-164 | ∅ (A-164 retains NFR-19) | S-14 |

Three further one-child aggregates existed at accretion convergence and were rescued by completion nodes, so they were **not** collapsed: S-3.5 (A-118 + C-015), S-9.3 (A-053 + C-007), S-13.2 (A-009 + C-010), S-14.1 (A-165 + C-016).

## 7c. Coverage completeness

One row per pinned requirement. "Whole" is asserted, not inferred.

| id | covering nodes · part each realises | verdict |
|---|---|---|
| I-1 | A-150 web-based delivery · A-075/076/077/078 create and hold GIN data · A-119/120/121/122 create and hold LN data · A-085 manage (edit) · A-090 manage (find) · A-097 manage (status) · A-031 + A-082 + A-123 prefix data as members use it · A-064 + A-065 share. "Replacing the applications currently available" is a scope statement realised by this same set (P3), not a further part | whole |
| I-2 | A-001 one platform, three modules · A-002 same data across them | whole |
| I-3 | A-003 lengths, prefix range, serial part, check digit | whole |
| I-4 | A-004 alignment and maintainability · A-005 scalability and sustainability | whole |
| I-5 | A-006 accommodation of further data types and field-level sharing | whole |
| I-6 | A-007 permission-based availability across modules · A-008 shared data and functions | whole |
| I-7 | A-009 the rule set as configuration · A-010 validation applied to all functionality | whole |
| I-8 | A-131 search · A-072 + A-136 view · A-053 + A-012 export under entitlement · S-7 residue: no editing functionality | whole |
| I-9 | A-011 subscription defines viewable data and export options · A-012 enforcement | whole |
| I-10 | A-013 anonymous limited search, no export | whole |
| I-11 | A-167 X-Customer-owned data in the access store under the same rules · A-131 reached by search · A-072 rendered on view | whole |
| G-1 | A-014 role assignment · A-015 task assignment | whole |
| G-1.1 | A-016 the administrator exists per member · A-017 add and edit users of that company | whole |
| G-1.2 | A-014 + A-015 the assignments · A-018 performed by the company admin within their company | whole |
| G-1.3 | A-019 the four named roles plus configurable additions | whole |
| G-1.4 | A-020 customer-level scope over all data | whole |
| G-2 | A-021 UI composed from role | whole |
| G-3 | A-022 workflow for new and edited records | whole |
| G-3.1 | A-014 designation of Editor and Approver · A-023 the approval rules | whole |
| G-3.2 | A-024 the status-change event · A-025 delivery to Editors and Approvers | whole |
| G-3.3 | A-026 the action list | whole |
| G-4 | A-027 initiation by user and by company admin, execution by the IdM · A-028 the help-desk initiator's cross-company scope | whole |
| G-5 | A-029 single-writer lock | whole |
| G-6 | A-030 notifications, reports and prefix data on a start screen | whole |
| G-6.1 | A-031 used and available counts | whole |
| G-7 | A-032 generation | whole |
| G-7.1 | A-033 customise · A-034 schedule · A-032 run and view · A-035 the adds/changes/deletes definitions | whole |
| G-7.2 | A-036 usage by hour, day, week, month, year from the analytics feed | whole |
| G-7.3 | A-037 run history | whole |
| G-7.4 | A-038 audit reports | whole |
| G-8 | A-025 composition and routing · A-039 email · A-040 SMS · A-041 onscreen | whole |
| G-8.1 | A-042 global broadcast | whole |
| G-8.2 | A-043 opt-in to record add/update events | whole |
| G-8.3 | A-044 both directions, including the record challenge | whole |
| G-8.5 | A-045 method and frequency | whole |
| G-9 | A-046 submission and routing to one configured destination | whole |
| G-10 | A-047 contextual display | whole |
| G-10.1 | A-048 the variant content · A-049 the industry key it varies on | whole |
| G-10.2 | A-050 authoring by non-technical staff | whole |
| G-11 | A-051 the configurable external links | whole |
| G-12 | A-052 import · A-053 export | whole |
| G-12.1 | A-054 Excel · A-055 CSV · A-056 Numbers · A-057 XML · A-058 tab-delimited · A-059 IDoc · A-060 the API path | whole |
| G-12.2 | A-061 PC and Mac encoding and line-ending variants inside the adapters | whole |
| G-12.3 | A-062 one or many records selected | whole |
| G-12.4 | A-010 the rule evaluation · A-063 applied to every record on import | whole |
| G-13 | A-064 publish side · A-065 subscribe side | whole |
| G-13.1 | A-066 any hierarchy level | whole |
| G-13.2 | A-067 basic or full attribute set | whole |
| G-13.3 | A-068 a group of records | whole |
| G-13.4 | A-069 the four target kinds · A-070 the user-defined group · A-071 the controlled group | whole |
| G-13.5 | A-011 entitlement from subscription · A-065 the subscription itself · A-072 the view | whole |
| G-13.6 | A-073 the request to the owner | whole |
| G-13.7 | A-074 approve or reject | whole |
| P-1 | A-075 individually · A-052 via import · A-076 wizard · A-077 cloning · A-078 required and non-required attributes · A-049 variation by industry | whole |
| P-1.1 | A-079 draft | whole |
| P-2 | A-080 auto or manual at any point · A-082 from the licensed GIN pool · A-003 the rule · A-081 automatic check digit | whole |
| P-2.1 | A-083 the user's choice | whole |
| P-2.2 | A-084 reservation out of auto-assign | whole |
| P-3 | A-083 the stored preference | whole |
| P-4 | A-085 editing before finalisation | whole |
| P-5 | A-085 manually · A-052 + A-086 via import | whole |
| P-5.1 | A-087 editability constrained by status | whole |
| P-5.2 | A-088 back-reference to the old number | whole |
| P-6 | A-089 upload and attach | whole |
| P-7 | A-090 view, filter, sort in one view | whole |
| P-7.1 | A-091 individual selection and action | whole |
| P-7.2 | A-092 multiple selection, one action | whole |
| P-8 | A-093 all GINs in one view with filter and sort | whole |
| P-9 | A-094 view duplicates, remove or edit | whole |
| P-9.1 | A-095 alert during creation · A-096 report over completed records | whole |
| P-10 | A-097 view and manage record and identifier status | whole |
| P-10.1 | A-098 the GIN status values and their assignment · A-099 update from record status | whole |
| P-10.2 | A-100 record status assignment | whole |
| P-10.3 | A-101 the out-of-use and reuse dates · A-102 the rules by industry and product type · A-049 where they are held | whole |
| P-11 | A-103 create, edit, view manually · A-105 via import · A-104 visual drag-and-drop | whole |
| P-11.1 | A-106 pre-defined levels | whole |
| P-11.2 | A-105 the import path · A-107 both import modes | whole |
| P-11.3 | A-108 fit check on height and weight | whole |
| P-11.4 | A-109 item-level change during creation | whole |
| P-11.5 | A-110 impact evaluation · A-025 notifying the user | whole |
| P-12 | A-053 the export · A-111 the user-friendly hierarchy layout and print | whole |
| P-13 | A-112 generation of the symbologies at selectable sizes · A-113 viewing | whole |
| P-14 | A-114 export and print as image | whole |
| P-15 | A-115 create, save, export and print with attributes and images | whole |
| P-15.1 | A-116 selectable and editable templates | whole |
| P-16 | A-117 the embeddable snippet | whole |
| P-17 | A-064 permissioning for publication · A-072 viewed in the Access Data module | whole |
| P-18 | A-118 transfer to another member | whole |
| P-19 | A-052 file import from external systems · A-060 the API route | whole |
| L-1 | A-119 individually · A-052 via import · A-120 wizard · A-121 cloning · A-122 required and non-required attributes · A-049 variation by industry | whole |
| L-1.1 | A-079 draft | whole |
| L-2 | A-080 auto or manual at any point · A-123 from the licensed LN pool · A-003 the rule · A-081 automatic check digit | whole |
| L-2.1 | A-124 the shared pool and automatic assignment from it · A-049 which industries | whole |
| L-2.2 | A-125 the licensee's choice | whole |
| L-2.3 | A-084 reservation out of auto-assign | whole |
| L-3 | A-125 the stored preference | whole |
| L-4 | A-085 editing before finalisation | whole |
| L-5 | A-085 manually · A-052 + A-086 via import | whole |
| L-5.1 | A-088 back-reference to the old number | whole |
| L-6 | A-090 view, filter, sort in one view | whole |
| L-6.1 | A-091 individual selection and action | whole |
| L-6.2 | A-092 multiple selection, one action | whole |
| L-7 | A-126 all LNs in one view with filter and sort | whole |
| L-8 | A-094 view duplicates, remove or edit | whole |
| L-8.1 | A-095 alert during creation · A-096 report over completed records | whole |
| L-9 | A-097 view and manage record and identifier status | whole |
| L-9.1 | A-127 the LN status values and their assignment · A-099 update from record status | whole |
| L-9.2 | A-100 record status assignment | whole |
| L-9.3 | A-101 the out-of-use and reuse dates · A-102 the rules by industry | whole |
| L-10 | A-103 create, edit, view manually · A-105 via import · A-104 visual drag-and-drop | whole |
| L-10.1 | A-128 unlimited levels, organised by attributes | whole |
| L-10.2 | A-105 the import path · A-107 both import modes | whole |
| L-10.3 | A-110 impact evaluation and notification | whole |
| L-11 | A-053 the export · A-111 the layout and print | whole |
| L-12 | A-064 permissioning for publication · A-072 viewed in the Access Data module | whole |
| L-13 | A-129 the verification record · A-130 what is due | whole |
| L-14 | A-118 transfer to another member | whole |
| L-15 | A-052 file import from external systems · A-060 the API route | whole |
| D-1 | A-131 search across prefix, GIN and LN | whole |
| D-1.1 | A-132 several named fields | whole |
| D-1.2 | A-133 advanced search and filters | whole |
| D-2 | A-073 the request · A-134 basic or full scope on it | whole |
| D-2.1 | A-074 the owner's decision · A-011 data available only once approved | whole |
| D-3 | A-135 request and X-Customer approval into the controlled group | whole |
| D-4 | A-072 basic and full records · A-136 their hierarchies | whole |
| D-5 | A-053 the export · A-062 one or more records · A-054–A-060 every format of the General Requirements · A-012 within entitlement | whole |
| D-6 | A-137 print one or more records | whole |
| D-7 | S-7 residue: every module function on both channels · A-138 the API channel | whole |
| D-8 | A-139 the informational page | whole |
| NFR-2 | A-140 the non-transactional data mart · A-142 the transactional store · A-005 both scalable to the projected volumes · A-141 near-real-time rather than overnight latency | whole |
| NFR-3 | A-143 claims-based authentication and single sign-on against the enterprise IdM, protocol-agnostic across SAML and OpenID Connect · A-144 claims mapped to application roles · A-019 the roles they map onto · A-007 claims-based authorisation | whole |
| NFR-4 | A-145 services instead of direct database access or copying · A-146 REST APIs to members, registered with the API-management platform · A-060 + A-138 the exposed surfaces | whole |
| NFR-5 | A-147 adherence to the technical standards · A-148 the deviation impact analysis and its record | whole |
| NFR-6 | A-149 cloud-ready architecture | whole |
| NFR-7 | A-150 web-based on standard patterns, no client installation · A-005 the user and concurrency volumes | whole |
| NFR-8 | A-151 the service level · A-152 the failover process and its hardware and software needs · A-153 failover monitoring that notifies administrators | whole |
| NFR-9 | A-154 backup and disaster recovery to X-Customer policy | whole |
| NFR-10 | A-155 the security design, configuration, processes and procedures · A-156 the components, frameworks, libraries and tools | whole |
| NFR-13 | A-157 the named browsers and versions | whole |
| NFR-14 | A-158 the response-time targets under the stated concurrency | whole |
| NFR-16 | A-022 + A-160 record approval for records entered by UI and by import · A-010 + A-063 + A-161 record validation of identifiers and attributes against the Standards · A-159 record verification | whole |
| NFR-17 | A-162 detection of system errors · A-025 near-real-time delivery | whole |
| NFR-18 | A-163 detection of critical business-function failure · A-025 near-real-time delivery | whole |
| NFR-19 | A-164 detailed logging for troubleshooting and process verification | whole |
| NFR-20 | A-165 audit trail of all activity | whole |
| NFR-21 | A-166 WCAG 2.0 Level A conformance | whole |

**146 of 146 requirements verdict `whole`. Zero residues. Zero requirements absent.**

---

## 8. Instrument readings

**Engine: `Hotyn-M 1.1`.**

| reading | value |
|---|---|
| node count before normalisation | 256 |
| node count after normalisation | 242 |
| provenance, before normalisation — `posited` | 69 |
| provenance, before normalisation — `accreted` | 167 |
| provenance, before normalisation — `derived` | 20 |
| derived fraction (before normalisation) | 20 of 256 |
| skeleton size | 69 |
| skeleton nodes with empty **total** coverage at accretion convergence | 0 |
| nodes collapsed at closure | 14 |
| accretion passes to convergence | 3 (166 added / 3 deferred; 1 added / 0 deferred; 0 / 0) |
| completion passes to convergence | 3 (17; 3; 0) |
| coverage assignments (node–requirement pairs) | 279 |
| nodes per requirement | min 1 · max 17 (I-1) · 279 over 146 |
| coverage-bearing nodes | 168 (167 accreted + S-7's own residue) |
| requirements per node | min 1 · max 7 (A-052, record import service) · 279 over 168 |
| nodes carrying no coverage | 88 (68 posited aggregates + 20 derived) |
| ambiguity flags raised | 25 — I-2, I-4, G-1, G-7.1, G-8.3, G-12.1, G-13.4, P-1, P-2, P-9.1, P-10.1, P-13, P-15, L-1, L-2, L-8.1, L-9.1, NFR-2, NFR-3, NFR-4, NFR-5, NFR-7, NFR-8, NFR-10, NFR-16 |
| completion-covers-a-requirement defects | 0 |
| **partial marks standing at closure** | **0** |

Per M8 this section contains no effort, size, duration, cost or complexity figure, and none appears anywhere above. Every number here is a count of nodes, requirements, assignments or passes.

---

## 9. Assumption log

**Nothing could not be placed.** No requirement is unplaced, and no defect report is raised.

### Entries flagged ambiguous, verbatim from the pinned list

Flagged and proceeded; not resolved, not split, not merged.

- **I-2** — "Three integrated modules — Product (GIN), Location (LN), Access Data — using the same data and system architecture and running on the same development platform"
- **I-4** — "An application architecture aligned with the existing enterprise architecture, maintainable by X-Customer resources, and scalable and sustainable given the projected member and application growth"
- **G-1** — "Allow assignment of user roles and tasks"
- **G-7.1** — "Customise, schedule, run and view reports for adds, changes and deletes"
- **G-8.3** — "Member-to-member and member-to-X-Customer notifications (e.g. a user can challenge record data)"
- **G-12.1** — "Import and export formats include at least Excel, CSV, Numbers, XML, tab-delimited, iDocs, and through the API"
- **G-13.4** — "The data owner can share records with an individual, a user-defined group, a controlled group managed by X-Customer, or the public"
- **P-1** / **L-1** — "Create GIN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry" (and its LN twin)
- **P-2** / **L-2** — "Assign a GIN to a record automatically or manually at any point during record creation; a check digit is assigned automatically" (and its LN twin)
- **P-9.1** / **L-8.1** — "Alert the user of possible duplicate records during creation, and run duplicate reports for completed records"
- **P-10.1** / **L-9.1** — "The system or the user assigns a status to each GIN (currently Reserved, In Use, For Reuse, Available); GIN status may update to reflect record status"
- **P-13** — "Generate and view X-Customer Standard supported barcodes of various types and sizes"
- **P-15** — "Create, save, export and print Product Information Sheets for each record, with all record attributes and images"
- **NFR-2** — "Data marts (non-transactional) to support data access; transactional and non-transactional databases scalable for the projected growth …; data latency is currently overnight and must support near-real-time updates"
- **NFR-3** — "Claims-based authentication and authorisation; user accounts and roles defined in an enterprise Identity Management system enabling single sign-on; the IdM solution is not finalised …"
- **NFR-4** — "A service-oriented architecture: REST (preferred) or SOAP web services integrate functionality and data across the suite instead of direct database access or copying; REST APIs available to members and compatible with an API management solution (currently 3scale)"
- **NFR-5** — "Adherence to X-Customer technical standards …; a deviation requires an impact analysis (technical, operational, support, financial) by the project core team at no cost to X-Customer"
- **NFR-7** — "Web-based, built on industry-standard web design patterns, frameworks and components, with no client-side software installation; roughly 38 000 users today …"
- **NFR-8** — "Highly available with a 99.9% service level; a failover process developed and tested, with the hardware and software needs identified, and failover monitoring that notifies administrators of a failure"
- **NFR-10** — "Appropriate security configuration, processes and procedures, with a security design and the components, frameworks, libraries and tools used to secure the application solution"
- **NFR-16** — "Business process workflows: record approval …, record validation …, record verification …"

### Redundant pairs observed but not reshaped

- **P-2.1 and P-3** state the same obligation in different words; likewise **L-2.2 and L-3**. M1 forbids merging, so both ids in each pair are carried by one node (A-083, A-125 respectively) — identical coverage would make them the same node, which is the correct reading.

### Shared versus per-kind, as assumption P3 requires be stated

**Modelled once and covering both twin ids:** draft state (A-079), pre-commit edit (A-085), edit-by-import update (A-086), identifier back-reference (A-088), list view / single selection / multi selection (A-090–A-092), duplicate review, alert and report (A-094–A-096), record status view and model (A-097, A-100), record-status→identifier-status propagation (A-099), retirement and reuse dates and their industry rules (A-101, A-102), hierarchy model, visual editor, import path and modes, status impact, export layout (A-103–A-105, A-107, A-110, A-111), reservation (A-084), assignment engine and check-digit computation (A-080, A-081), identifier rules (A-003), ownership transfer (A-118), import and export services and adapters.

**Modelled per kind:** attribute models and creation flows (A-075–A-078 against A-119–A-122), because the wizard and clone paths follow the kind's attribute set; number pools and assignment preferences (A-082/A-083 against A-123/A-124/A-125), because LN has a shared industry pool and a licensee-level preference that GIN does not; status value sets (A-098 against A-127); hierarchy rules (A-106, A-108, A-109 against A-128), because the level scheme and depth differ; identifier inventory views (A-093 against A-126). Product-only, with no LN twin in the list: images (A-089), status-based editability (A-087), barcodes, product sheets, digital GIN. Location-only: annual verification (A-129, A-130).

### Where interpretation was required rather than reading

- **I-8 and D-7 are declared as own residue at S-7.** Both are constraints over the module's composition — "contains no editing functionality" and "all functions on either channel" — that no child can realise, an absence and a cross-child property respectively. Every other coverage assignment in this model sits at a leaf.
- **NFR-8's "developed and tested" and NFR-5's "impact analysis … by the project core team".** Only the artefacts are modelled: the failover process design, the identified hardware and software needs, the deviation register and the analyses it holds. Whatever in those phrases is an obligation on the doing rather than on the thing was not modelled here and is not this run's to place.
- **Design-property nodes.** I-4, I-5, NFR-6, NFR-7, NFR-8, NFR-9, NFR-10, NFR-14 and part of NFR-2 are modelled as design statements the solution carries (A-004, A-005, A-006, A-149, A-151, A-152, A-154, A-155, A-158), not as components, following P3. They are nodes because the RFP obliges the design; they are not machinery.
- **Boundaries held, per P1.** No prefix-licensing workflow, no payment flow, no training module, no generic any-data-type engine, and no legacy-loading component appears. The structure did not need them; where it came close — I-1's "data related to prefixes", D-8, G-11, I-5 — the obligation was placed against capacity reporting and pool draw, an informational page, a link set, and an extensibility statement respectively.
- **Two external exchanges are modelled as the exchange only:** A-036 reads usage figures from the API-management analytics feed, and A-146 registers the member-facing API with it; A-027 initiates a reset that the IdM executes; A-039 and A-040 hand off to the client's relay and an external gateway; A-112 calls a barcode library. Nothing behind those boundaries is a node.
- **A-167 was added in accretion pass 2**, not pass 1: I-11 could not be judged until the Access Data access path existed, which is a deferral in the M5 sense and the sole reason accretion needed a second pass.