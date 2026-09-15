Size the elements of the work model batch below by classifying, not pricing. Everything you need is in this message; read no files.

**Scope: the subtrees rooted at N02 of the product model `HM57-1`, as classified and crossed by `Hotyn-W 1.2`** — 30 sized elements (aggregates are listed for context and are never sized). Other subtrees and the model root are outside this batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, sections 1 to 7 as your engine definition requires. In the sizing table quote the enumeration verbatim, one row per sized element, grouped by subtree. Every number you output is a count of named things; nothing else.

---

# INPUT 1 — the work model batch: elements with class, parent, declared content, covered obligations (with their texts) and the activities crossed onto them

In this model coverage lives in leaves only: an aggregate's content is its children. A derived leaf has no covered obligation; its declared content is its name read with the trigger that called for it (the elements named after `trigger:`).


**N02 — Platform architecture** · aggregate (not sized) · parent N01

**N03 — Data stores** · aggregate (not sized) · parent N02

**N04 — Service and API layer** · aggregate (not sized) · parent N02

**N05 — Web client** · aggregate (not sized) · parent N02

**CN01 — Background processing** · aggregate (not sized) · parent N02
- **A001 — Shared domain data model (companies, users, prefixes, records, identifiers)** · class **store** · parent N03
  - covered obligations: I-2: Three integrated modules — Product (GIN), Location (LN), Access Data — using the same data and system architecture and running on the same development platform; I-6: Functionality available to all members based on permissions, regardless of which module they use; data and functions are shared across modules; NFR-2: Data marts (non-transactional) to support data access; transactional and non-transactional databases scalable for the projected growth (company prefixes 500 000 → 700 000 records, GIN 10 000 000 → 70 000 000, LN 550 000 → 3 500 000, by 2024); data latency is currently overnight and must support near-real-time updates; I-1: A web-based application solution for members to create, manage and share data related to prefixes, Global Item Numbers (GIN) and Location Numbers (LN), replacing the applications currently available to members
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A002 — Unified application shell with Product, Location, Access Data areas** · class **surface** · parent N05
  - covered obligations: I-2: Three integrated modules — Product (GIN), Location (LN), Access Data — using the same data and system architecture and running on the same development platform; I-6: Functionality available to all members based on permissions, regardless of which module they use; data and functions are shared across modules; D-7: Perform all Access Data functions via the web interface or the API; NFR-7: Web-based, built on industry-standard web design patterns, frameworks and components, with no client-side software installation; roughly 38 000 users today, approximately 256 000 by 2024, up to 10% of them concurrent; I-1: A web-based application solution for members to create, manage and share data related to prefixes, Global Item Numbers (GIN) and Location Numbers (LN), replacing the applications currently available to members
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A005 — Architecture design: enterprise alignment, maintainability, growth scalability** · class **statement** · parent N02
  - covered obligations: I-4: An application architecture aligned with the existing enterprise architecture, maintainable by X-Customer resources, and scalable and sustainable given the projected member and application growth
  - activities crossed onto it: D4, K3
- **A006 — Future-expansion design provisions (further data types, field-level sharing)** · class **statement** · parent N02
  - covered obligations: I-5: The final design accommodates future expansion — data other than GIN or LN, and sharing privileges down to field level — while that expansion itself stays out of scope
  - activities crossed onto it: D4, K3
- **A012 — X-Customer reference data set (prefix registry, controlled groups)** · class **store** · parent N03
  - covered obligations: I-11: X-Customer-owned data as well as data published by data owners can be accessed in the Access Data module; I-1: A web-based application solution for members to create, manage and share data related to prefixes, Global Item Numbers (GIN) and Location Numbers (LN), replacing the applications currently available to members
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A019 — Role-driven UI composition** · class **behaviour** · parent N05
  - covered obligations: G-2: Present a role-driven UI based on user role
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A034 — 3scale analytics API client** · class **interface** · parent N04
  - covered obligations: G-7.2: View usage reports by hour, day, week, month and year *(current reporting utilises 3scale)*
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A059 — Record import and export API** · class **interface** · parent N04
  - covered obligations: G-12.1: Import and export formats include at least Excel, CSV, Numbers, XML, tab-delimited, iDocs, and through the API; P-19: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; L-15: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; NFR-4: A service-oriented architecture: REST (preferred) or SOAP web services integrate functionality and data across the suite instead of direct database access or copying; REST APIs available to members and compatible with an API management solution (currently 3scale)
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A076 — Industry configuration store** · class **store** · parent N03
  - covered obligations: P-1: Create GIN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry; L-1: Create LN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A089 — Binary asset store for images** · class **store** · parent N03
  - covered obligations: P-6: Upload product images and add them to records
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A140 — Access Data REST API** · class **interface** · parent N04
  - covered obligations: D-7: Perform all Access Data functions via the web interface or the API; NFR-4: A service-oriented architecture: REST (preferred) or SOAP web services integrate functionality and data across the suite instead of direct database access or copying; REST APIs available to members and compatible with an API management solution (currently 3scale)
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A141 — Member API registration in 3scale** · class **interface** · parent N04
  - covered obligations: D-7: Perform all Access Data functions via the web interface or the API; NFR-4: A service-oriented architecture: REST (preferred) or SOAP web services integrate functionality and data across the suite instead of direct database access or copying; REST APIs available to members and compatible with an API management solution (currently 3scale)
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A143 — Non-transactional read store** · class **store** · parent N03
  - covered obligations: NFR-2: Data marts (non-transactional) to support data access; transactional and non-transactional databases scalable for the projected growth (company prefixes 500 000 → 700 000 records, GIN 10 000 000 → 70 000 000, LN 550 000 → 3 500 000, by 2024); data latency is currently overnight and must support near-real-time updates
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A144 — Near-real-time feed to read store** · class **behaviour** · parent N03
  - covered obligations: NFR-2: Data marts (non-transactional) to support data access; transactional and non-transactional databases scalable for the projected growth (company prefixes 500 000 → 700 000 records, GIN 10 000 000 → 70 000 000, LN 550 000 → 3 500 000, by 2024); data latency is currently overnight and must support near-real-time updates
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A145 — Data volume scalability design** · class **statement** · parent N02
  - covered obligations: NFR-2: Data marts (non-transactional) to support data access; transactional and non-transactional databases scalable for the projected growth (company prefixes 500 000 → 700 000 records, GIN 10 000 000 → 70 000 000, LN 550 000 → 3 500 000, by 2024); data latency is currently overnight and must support near-real-time updates
  - activities crossed onto it: D4, K3
- **A148 — Internal REST service layer** · class **behaviour** · parent N04
  - covered obligations: NFR-4: A service-oriented architecture: REST (preferred) or SOAP web services integrate functionality and data across the suite instead of direct database access or copying; REST APIs available to members and compatible with an API management solution (currently 3scale)
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A149 — Technical standards conformance design** · class **statement** · parent N02
  - covered obligations: NFR-5: Adherence to X-Customer technical standards — coding, database connection and naming, integration, approved technologies and products; a deviation requires an impact analysis (technical, operational, support, financial) by the project core team at no cost to X-Customer
  - activities crossed onto it: D4, K3
- **A150 — Standards deviation impact analysis procedure** · class **statement** · parent N02
  - covered obligations: NFR-5: Adherence to X-Customer technical standards — coding, database connection and naming, integration, approved technologies and products; a deviation requires an impact analysis (technical, operational, support, financial) by the project core team at no cost to X-Customer
  - activities crossed onto it: D4, K3
- **A151 — Cloud-readiness design provisions** · class **statement** · parent N02
  - covered obligations: NFR-6: The architecture is designed to be cloud-ready
  - activities crossed onto it: D4, K3
- **A152 — Standard web framework foundation (no client install)** · class **statement** · parent N05
  - covered obligations: NFR-7: Web-based, built on industry-standard web design patterns, frameworks and components, with no client-side software installation; roughly 38 000 users today, approximately 256 000 by 2024, up to 10% of them concurrent; NFR-13: Accessible on Internet Explorer 9 and above, and on the current and previous versions of Chrome, Firefox, Safari and Edge; NFR-21: WCAG 2.0 Level A compliance, within reasonable accommodation
  - activities crossed onto it: D4, K3
- **A153 — User volume and concurrency capacity design** · class **statement** · parent N02
  - covered obligations: NFR-7: Web-based, built on industry-standard web design patterns, frameworks and components, with no client-side software installation; roughly 38 000 users today, approximately 256 000 by 2024, up to 10% of them concurrent
  - activities crossed onto it: D4, K3
- **A163 — Cross-browser compatibility** · class **statement** · parent N05
  - covered obligations: NFR-13: Accessible on Internet Explorer 9 and above, and on the current and previous versions of Chrome, Firefox, Safari and Edge
  - activities crossed onto it: D4, K3
- **A171 — WCAG 2.0 Level A conformance** · class **statement** · parent N05
  - covered obligations: NFR-21: WCAG 2.0 Level A compliance, within reasonable accommodation
  - activities crossed onto it: D4, K3
- **C05 — Background job scheduler** · class **behaviour** · parent CN01
  - covered obligations: — (derived element, no covered obligation; trigger:A032,A045,A104)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **C08 — Asynchronous import job queue with progress status** · class **behaviour** · parent CN01
  - covered obligations: — (derived element, no covered obligation; trigger:A051,A145)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **C10 — Industry configuration maintenance screens** · class **surface** · parent N03
  - covered obligations: — (derived element, no covered obligation; trigger:A076)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **C12 — Search index maintenance from read-store feed** · class **behaviour** · parent CN01
  - covered obligations: — (derived element, no covered obligation; trigger:A133,A144)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **C13 — User-facing error handling** · class **behaviour** · parent N05
  - covered obligations: — (derived element, no covered obligation; trigger:A002)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **C14 — API caller identity mapping from 3scale credentials** · class **behaviour** · parent N04
  - covered obligations: — (derived element, no covered obligation; trigger:A140,A059,A007)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **C16 — Job run log and retry** · class **behaviour** · parent CN01
  - covered obligations: — (derived element, no covered obligation; trigger:C05,C08)
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
