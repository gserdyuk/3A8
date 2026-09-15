Size the elements of the work model batch below by classifying, not pricing. Everything you need is in this message; read no files.

**Scope: the subtrees rooted at N06, N07, N10 of the product model `HM57-1`, as classified and crossed by `Hotyn-W 1.2`** — 27 sized elements (aggregates are listed for context and are never sized). Other subtrees and the model root are outside this batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, sections 1 to 7 as your engine definition requires. In the sizing table quote the enumeration verbatim, one row per sized element, grouped by subtree. Every number you output is a count of named things; nothing else.

---

# INPUT 1 — the work model batch: elements with class, parent, declared content, covered obligations (with their texts) and the activities crossed onto them

In this model coverage lives in leaves only: an aggregate's content is its children. A derived leaf has no covered obligation; its declared content is its name read with the trigger that called for it (the elements named after `trigger:`).


**N06 — Identity and access** · aggregate (not sized) · parent N01

**N07 — Record governance** · aggregate (not sized) · parent N01

**N10 — User assistance** · aggregate (not sized) · parent N01
- **A007 — Cross-module authorisation service** · class **behaviour** · parent N06
  - covered obligations: I-6: Functionality available to all members based on permissions, regardless of which module they use; data and functions are shared across modules; G-2: Present a role-driven UI based on user role
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A008 — Validation rule engine (entry, import, identifier assignment)** · class **behaviour** · parent N07
  - covered obligations: I-7: All functionality is validated against X-Customer Standards and business rules, which will be defined as part of the project; G-12.4: All records are validated upon import; NFR-16: Business process workflows: record approval (records entered via UI or import are submitted, reviewed, rejected or approved), record validation (identifiers, auto-generated or manual, comply with X-Customer Standards), record verification (attributes entered via UI or import are verified for accuracy)
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A009 — Validation rule set held as configuration** · class **store** · parent N07
  - covered obligations: I-7: All functionality is validated against X-Customer Standards and business rules, which will be defined as part of the project
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A013 — User role assignment** · class **behaviour** · parent N06
  - covered obligations: G-1: Allow assignment of user roles and tasks; G-1.2: The company admin can assign roles and tasks to users; G-3.1: The company admin can designate Editor and Approver roles and the rules for record approval
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A014 — Workflow task assignment (edit and approve responsibilities)** · class **behaviour** · parent N07
  - covered obligations: G-1: Allow assignment of user roles and tasks; G-1.2: The company admin can assign roles and tasks to users; G-3.1: The company admin can designate Editor and Approver roles and the rules for record approval
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A015 — Company administrator designation per member** · class **behaviour** · parent N06
  - covered obligations: G-1.1: Each member is assigned a company administrator with the ability to add and edit other users in their company; G-1.2: The company admin can assign roles and tasks to users; G-3.1: The company admin can designate Editor and Approver roles and the rules for record approval
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A016 — Company user administration (add, edit users)** · class **surface** · parent N06
  - covered obligations: G-1.1: Each member is assigned a company administrator with the ability to add and edit other users in their company; NFR-3: Claims-based authentication and authorisation; user accounts and roles defined in an enterprise Identity Management system enabling single sign-on; the IdM solution is not finalised and will support claims-based standards such as OAuth and SAML
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A017 — Configurable role catalogue seeded with four roles** · class **store** · parent N06
  - covered obligations: G-1.3: User roles include Super-User, Approver, Editor, View-only; other roles may be added; G-1.4: A customer-level "Super-User" role with access to manage all data; NFR-3: Claims-based authentication and authorisation; user accounts and roles defined in an enterprise Identity Management system enabling single sign-on; the IdM solution is not finalised and will support claims-based standards such as OAuth and SAML
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A018 — Role permission sets (function and data scope per role)** · class **store** · parent N06
  - covered obligations: G-1.4: A customer-level "Super-User" role with access to manage all data; G-2: Present a role-driven UI based on user role
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A020 — Record approval workflow engine** · class **behaviour** · parent N07
  - covered obligations: G-3: Implement a workflow for new and edited records; G-3.2: Editors and Approvers are notified of a change in approval status; P-10.2: The system or the user can assign a status to each record; L-9.2: The system or the user can assign a status to each record; NFR-16: Business process workflows: record approval (records entered via UI or import are submitted, reviewed, rejected or approved), record validation (identifiers, auto-generated or manual, comply with X-Customer Standards), record verification (attributes entered via UI or import are verified for accuracy)
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A021 — Approval rule configuration per company** · class **store** · parent N07
  - covered obligations: G-3.1: The company admin can designate Editor and Approver roles and the rules for record approval
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A023 — Records-awaiting-my-action work list** · class **surface** · parent N07
  - covered obligations: G-3.3: Users can easily find records requiring their action
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A024 — Password reset initiation (self, company admin, help desk)** · class **behaviour** · parent N06
  - covered obligations: G-4: A user's password can be reset by the user, the company admin, or the X-Customer help desk
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A025 — IdM password reset exchange** · class **interface** · parent N06
  - covered obligations: G-4: A user's password can be reset by the user, the company admin, or the X-Customer help desk; NFR-3: Claims-based authentication and authorisation; user accounts and roles defined in an enterprise Identity Management system enabling single sign-on; the IdM solution is not finalised and will support claims-based standards such as OAuth and SAML
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A026 — Record edit lock** · class **behaviour** · parent N07
  - covered obligations: G-5: Lock records so that only one user at a time can edit a record
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A046 — Application feedback submission to configured address** · class **behaviour** · parent N10
  - covered obligations: G-9: Users can send application feedback to X-Customer, routed to a single X-Customer contact or a feedback tracking system
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A047 — Contextual help display** · class **surface** · parent N10
  - covered obligations: G-10: Display contextual help to the user; G-10.1: Help content may be customised by industry
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A048 — Industry variants of help content** · class **store** · parent N10
  - covered obligations: G-10.1: Help content may be customised by industry
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A049 — Help content editor for non-technical staff** · class **surface** · parent N10
  - covered obligations: G-10.2: Help content is maintained by X-Customer non-technical resources
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A050 — Configurable training link set** · class **store** · parent N10
  - covered obligations: G-11: Link to training — external videos, webinars, quick-start guides — from within the application
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A146 — Claims-based single sign-on integration** · class **interface** · parent N06
  - covered obligations: NFR-3: Claims-based authentication and authorisation; user accounts and roles defined in an enterprise Identity Management system enabling single sign-on; the IdM solution is not finalised and will support claims-based standards such as OAuth and SAML
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A147 — Claims-to-company-user-role mapping** · class **behaviour** · parent N06
  - covered obligations: NFR-3: Claims-based authentication and authorisation; user accounts and roles defined in an enterprise Identity Management system enabling single sign-on; the IdM solution is not finalised and will support claims-based standards such as OAuth and SAML
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A165 — Attribute accuracy verification workflow** · class **behaviour** · parent N07
  - covered obligations: NFR-16: Business process workflows: record approval (records entered via UI or import are submitted, reviewed, rejected or approved), record validation (identifiers, auto-generated or manual, comply with X-Customer Standards), record verification (attributes entered via UI or import are verified for accuracy)
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **C01 — X-Customer staff accounts and staff roles** · class **store** · parent N06
  - covered obligations: — (derived element, no covered obligation; trigger:A024,A041,A049,A069,A137)
  - activities crossed onto it: A2, A3, A4, G2m, G3m, G4m, K1, K2
- **C02 — Session management and sign-out** · class **behaviour** · parent N06
  - covered obligations: — (derived element, no covered obligation; trigger:A146)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **C03 — IdM user provisioning and deprovisioning exchange** · class **interface** · parent N06
  - covered obligations: — (derived element, no covered obligation; trigger:A016,A146)
  - activities crossed onto it: A2, A3, A4, A10, K1, K2
- **C04 — Record lock expiry and administrative release** · class **behaviour** · parent N07
  - covered obligations: — (derived element, no covered obligation; trigger:A026)
  - activities crossed onto it: A2, A3, A4, K1, K2

---

# INPUT 2 — the sizing rules (catalogue 1.4 §3a, verbatim where it binds)

**W10.** Every sized element receives one size class — **S / M / L / XL** — by **counting named things**. The
enumeration is the justification; a bare number is not acceptable. Thresholds are pinned here and are not
yours to bend. Drivers count scope, never effort: no driver may reference difficulty, risk, novelty or time.

**One size class per element, assigned once.** The class is a property of the element — a leaf, or an
internal node carrying own content. **A pure aggregate is never sized.** Every per-element activity uses the
element's class by default. **Position-derived sizes are not yours** (per-parent, once-scoped, per-environment
items are tree arithmetic computed outside you) — do not report them.

## Element size classes — counted from the element's declared content plus its own coverage

| element class | what is enumerated | S | M | L | XL |
|---|---|---|---|---|---|
| behaviour | distinct actions (verb on object) the declared content names | 1 | 2–3 | 4–6 | ≥7 |
| interface | operations consumed or exposed; a named protocol/auth concern counts as one | 1 | 2–4 | 5–8 | ≥9 |
| surface | distinct user tasks the surface serves | 1 | 2–3 | 4–6 | ≥7 |
| store | entity kinds the store is responsible for | 1 | 2–3 | 4–6 | ≥7 |
| statement (both kinds) | systems or components the property constrains | 1 | 2–4 | 5–8 | ≥9 |
| aggregate | — never sized | | | | |

**XL is a class and a signal at once:** an XL element is classed XL **and** reported as a probable coarseness
finding about the product model (M10). Neither substitutes for the other.

**`statement` splits into two kinds**, logged with the phrase that justifies the kind: **`compliance`** — the
content names a standard, configuration or policy and no run-time scenario; **`behavioural`** — the content
entails run-time behaviour. **P-4, the kind tie-break: run-time wins** — a statement whose covered obligations
mix kinds is `behavioural` when any covered obligation entails run-time behaviour, `compliance` only when none does.

## Special counts — enumerated the same way, where the element carries the activity

| activity on the element | driver enumerated | S | M | L | XL |
|---|---|---|---|---|---|
| **A9** (performance and availability testing, on a behavioural statement) | measurable targets the statement names (thresholds, service levels) — count from the content **and the covered obligations' texts** | 1 | 2–3 | 4–6 | ≥7 |
| **G2m / G3m / G4m** (field mapping, extraction and transformation, load and reconciliation, on a store) | entity kinds in the store that are loaded from the predecessor applications — say per kind why it must arrive from the predecessor rather than be created at run time | 1 | 2–3 | 4–6 | ≥7 |

The **D4** driver (requirement ids in the element's own coverage) is computed outside you from the coverage
sets; do not report it.

## Enumeration precedents — case law adjudicated once for everybody (catalogue 1.3 and 1.4)

- **P-1 — a named delivery channel is a protocol concern.** An interface whose obligation names a delivery
  channel counts the channel alongside the operation: "notifications via email" = the dispatch operation + the
  email channel = 2.
- **P-2 — a name token counts only when no counted obligation already covers its action.** A token in the
  element's name that an enumerated obligation already covers is not counted again; a token covered by no
  obligation is counted. The test is coverage, not position in name or text.
- **P-3 — slash-separated outcomes are distinct actions.** "Accepted/Rejected" names two transitions, not one;
  stage lists count by outcome.
- **P-4 — the kind tie-break: run-time wins** (above).
- **P-5 — an unnamed catch-all is not a named thing.** "and other details" names no kind and counts nothing.
- **P-6 — a stated cardinality without named members is not an enumeration.** "three amendment origins" is a
  number, not a list; an element whose declaration counts things it never names is **unsizeable — model
  defect (M10)**, never sized on a guessed reading.

An element you cannot count is a finding, not a guess: report it as *unsizeable — model defect (M10)* with what
is missing, and assign no class. You may not add, remove, merge or reshape elements or work items; work you
judge necessary and absent is a **closure violation** — name it, say what it would cover, do not size it.
