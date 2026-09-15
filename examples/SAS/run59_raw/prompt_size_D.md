Size the elements of the work model batch below by classifying, not pricing. Everything you need is in this message; read no files.

**Scope: the subtrees rooted at N11, N12 of the product model `HM57-1`, as classified and crossed by `Hotyn-W 1.2`** — 24 sized elements (aggregates are listed for context and are never sized). Other subtrees and the model root are outside this batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, sections 1 to 7 as your engine definition requires. In the sizing table quote the enumeration verbatim, one row per sized element, grouped by subtree. Every number you output is a count of named things; nothing else.

---

# INPUT 1 — the work model batch: elements with class, parent, declared content, covered obligations (with their texts) and the activities crossed onto them

In this model coverage lives in leaves only: an aggregate's content is its children. A derived leaf has no covered obligation; its declared content is its name read with the trigger that called for it (the elements named after `trigger:`).


**N11 — Import and export** · aggregate (not sized) · parent N01

**N12 — Publish and subscribe** · aggregate (not sized) · parent N01
- **A010 — Subscription entitlement model (viewable data, export options)** · class **store** · parent N12
  - covered obligations: I-9: A client's subscription determines which data can be viewed and which export options are available; G-13: A publish (select for sharing by the data owner) and subscribe (request viewing by data consumers) model with multiple share/view functions; G-13.5: Based on subscription, a data consumer can view published data; D-5: Export one or more records to any format detailed in the General Requirements
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A051 — Record import pipeline (parse, map, validate, load)** · class **behaviour** · parent N11
  - covered obligations: G-12: Allow import and export of records, as referenced in the Product, Location and Data Access modules; G-12.1: Import and export formats include at least Excel, CSV, Numbers, XML, tab-delimited, iDocs, and through the API; G-12.4: All records are validated upon import; P-1: Create GIN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry; P-5: Edit record attributes manually or via import; P-11: Create, edit and view a hierarchy of GINs (e.g. each → case → pallet) manually, via import, or via a visual format such as drag-and-drop; P-11.2: Imports can include full records with hierarchy information, or hierarchy information for existing records; P-19: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; L-1: Create LN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry; L-5: Edit record attributes manually or via import; L-10.2: Imports can include full records with hierarchy information, or hierarchy information for existing records; L-15: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A052 — Record export pipeline (serialise, deliver)** · class **behaviour** · parent N11
  - covered obligations: G-12: Allow import and export of records, as referenced in the Product, Location and Data Access modules; G-12.1: Import and export formats include at least Excel, CSV, Numbers, XML, tab-delimited, iDocs, and through the API; P-12: Export and print hierarchies in a user-friendly format; D-5: Export one or more records to any format detailed in the General Requirements; I-8: The Access Data module allows users to search for, view and export prefix, GIN and LN data — the subscribe side of the publish-and-subscribe model — and contains no editing functionality
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A053 — Excel import and export adapter** · class **interface** · parent N11
  - covered obligations: G-12.1: Import and export formats include at least Excel, CSV, Numbers, XML, tab-delimited, iDocs, and through the API; G-12.2: Import and export must include PC and Mac formats; P-19: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; L-15: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; D-5: Export one or more records to any format detailed in the General Requirements
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A054 — CSV import and export adapter** · class **interface** · parent N11
  - covered obligations: G-12.1: Import and export formats include at least Excel, CSV, Numbers, XML, tab-delimited, iDocs, and through the API; G-12.2: Import and export must include PC and Mac formats; P-19: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; L-15: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; D-5: Export one or more records to any format detailed in the General Requirements
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A055 — Numbers import and export adapter** · class **interface** · parent N11
  - covered obligations: G-12.1: Import and export formats include at least Excel, CSV, Numbers, XML, tab-delimited, iDocs, and through the API; G-12.2: Import and export must include PC and Mac formats; P-19: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; L-15: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; D-5: Export one or more records to any format detailed in the General Requirements
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A056 — XML import and export adapter** · class **interface** · parent N11
  - covered obligations: G-12.1: Import and export formats include at least Excel, CSV, Numbers, XML, tab-delimited, iDocs, and through the API; G-12.2: Import and export must include PC and Mac formats; P-19: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; L-15: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; D-5: Export one or more records to any format detailed in the General Requirements
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A057 — Tab-delimited import and export adapter** · class **interface** · parent N11
  - covered obligations: G-12.1: Import and export formats include at least Excel, CSV, Numbers, XML, tab-delimited, iDocs, and through the API; G-12.2: Import and export must include PC and Mac formats; P-19: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; L-15: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; D-5: Export one or more records to any format detailed in the General Requirements
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A058 — IDoc import and export adapter** · class **interface** · parent N11
  - covered obligations: G-12.1: Import and export formats include at least Excel, CSV, Numbers, XML, tab-delimited, iDocs, and through the API; G-12.2: Import and export must include PC and Mac formats; P-19: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; L-15: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution; D-5: Export one or more records to any format detailed in the General Requirements
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A060 — Record selection for import and export** · class **behaviour** · parent N11
  - covered obligations: G-12.3: A user can select one or more records to be imported or exported; D-5: Export one or more records to any format detailed in the General Requirements
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A061 — Import validation result report** · class **surface** · parent N11
  - covered obligations: G-12.4: All records are validated upon import
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A062 — Publication registry (what, to whom, attribute tier)** · class **store** · parent N12
  - covered obligations: G-13: A publish (select for sharing by the data owner) and subscribe (request viewing by data consumers) model with multiple share/view functions; G-13.1: The data owner can publish records at any level in the hierarchy; G-13.2: The data owner can publish (grant access to view) a basic or a full set of record attributes; G-13.3: The data owner can publish data for a group of records; G-13.4: The data owner can share records with an individual, a user-defined group, a controlled group managed by X-Customer, or the public; P-17: Permission records for publishing; published records are viewed within the Data Access module; L-12: Permission records for publishing; published records are viewed within the Data Access module; I-1: A web-based application solution for members to create, manage and share data related to prefixes, Global Item Numbers (GIN) and Location Numbers (LN), replacing the applications currently available to members
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A063 — Published-data access evaluation** · class **behaviour** · parent N12
  - covered obligations: G-13: A publish (select for sharing by the data owner) and subscribe (request viewing by data consumers) model with multiple share/view functions; G-13.5: Based on subscription, a data consumer can view published data; P-17: Permission records for publishing; published records are viewed within the Data Access module; L-12: Permission records for publishing; published records are viewed within the Data Access module
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A064 — Hierarchy-level publication** · class **behaviour** · parent N12
  - covered obligations: G-13.1: The data owner can publish records at any level in the hierarchy
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A065 — Basic and full attribute tiers** · class **statement** · parent N12
  - covered obligations: G-13.2: The data owner can publish (grant access to view) a basic or a full set of record attributes; D-2: Request access to a basic or full record (subscribe to the record)
  - activities crossed onto it: D4, K3
- **A066 — Publication for a group of records** · class **behaviour** · parent N12
  - covered obligations: G-13.3: The data owner can publish data for a group of records
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A067 — Sharing target selection (individual, group, controlled group, public)** · class **behaviour** · parent N12
  - covered obligations: G-13.4: The data owner can share records with an individual, a user-defined group, a controlled group managed by X-Customer, or the public
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A068 — User-defined group management** · class **behaviour** · parent N12
  - covered obligations: G-13.4: The data owner can share records with an individual, a user-defined group, a controlled group managed by X-Customer, or the public
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A069 — Controlled group management by X-Customer** · class **behaviour** · parent N12
  - covered obligations: G-13.4: The data owner can share records with an individual, a user-defined group, a controlled group managed by X-Customer, or the public; D-3: Request to be added to a controlled group
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A071 — Access request submission** · class **behaviour** · parent N12
  - covered obligations: G-13.6: Based on subscription, a data consumer can request access to view data from the data owner; G-13.7: The data owner can approve or reject view requests; D-2: Request access to a basic or full record (subscribe to the record); D-2.1: The request is sent to the data owner, who must approve before the data becomes available
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A072 — Access request approval and rejection by owner** · class **behaviour** · parent N12
  - covered obligations: G-13.7: The data owner can approve or reject view requests; D-2.1: The request is sent to the data owner, who must approve before the data becomes available
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A085 — Import update mode for existing records** · class **behaviour** · parent N11
  - covered obligations: P-5: Edit record attributes manually or via import; P-11.2: Imports can include full records with hierarchy information, or hierarchy information for existing records; L-5: Edit record attributes manually or via import; L-10.2: Imports can include full records with hierarchy information, or hierarchy information for existing records
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A137 — Controlled group join request with X-Customer approval** · class **behaviour** · parent N12
  - covered obligations: D-3: Request to be added to a controlled group
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **C09 — Publication overview and revocation** · class **surface** · parent N12
  - covered obligations: — (derived element, no covered obligation; trigger:A062)
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
