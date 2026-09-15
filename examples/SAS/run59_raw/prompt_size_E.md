Size the elements of the work model batch below by classifying, not pricing. Everything you need is in this message; read no files.

**Scope: the subtrees rooted at N13 of the product model `HM57-1`, as classified and crossed by `Hotyn-W 1.2`** — 31 sized elements (aggregates are listed for context and are never sized). Other subtrees and the model root are outside this batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, sections 1 to 7 as your engine definition requires. In the sizing table quote the enumeration verbatim, one row per sized element, grouped by subtree. Every number you output is a count of named things; nothing else.

---

# INPUT 1 — the work model batch: elements with class, parent, declared content, covered obligations (with their texts) and the activities crossed onto them

In this model coverage lives in leaves only: an aggregate's content is its children. A derived leaf has no covered obligation; its declared content is its name read with the trigger that called for it (the elements named after `trigger:`).


**N13 — Shared record management** · aggregate (not sized) · parent N01

**N14 — Identifier management** · aggregate (not sized) · parent N13

**N15 — Record lifecycle** · aggregate (not sized) · parent N13

**N16 — Record views and actions** · aggregate (not sized) · parent N13

**N17 — Duplicate handling** · aggregate (not sized) · parent N13

**N18 — Hierarchy management** · aggregate (not sized) · parent N13
- **A003 — Identifier composition rules (prefix plus serial, per-kind length)** · class **behaviour** · parent N14
  - covered obligations: I-3: Identifier rules: a GIN is 12 or 14 digits and an LN is 13 digits, each formed as the company's licensed prefix (6–9 digits) plus a serial part, with a check digit; P-2: Assign a GIN to a record automatically or manually at any point during record creation; a check digit is assigned automatically; L-2: Assign an LN to a record automatically or manually at any point during record creation; a check digit is assigned automatically
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A004 — Check digit calculation** · class **behaviour** · parent N14
  - covered obligations: I-3: Identifier rules: a GIN is 12 or 14 digits and an LN is 13 digits, each formed as the company's licensed prefix (6–9 digits) plus a serial part, with a check digit; P-2: Assign a GIN to a record automatically or manually at any point during record creation; a check digit is assigned automatically; L-2: Assign an LN to a record automatically or manually at any point during record creation; a check digit is assigned automatically
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A073 — Single-record creation form driven by attribute sets** · class **surface** · parent N15
  - covered obligations: P-1: Create GIN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry; L-1: Create LN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry; I-1: A web-based application solution for members to create, manage and share data related to prefixes, Global Item Numbers (GIN) and Location Numbers (LN), replacing the applications currently available to members
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A074 — Step-by-step record creation wizard** · class **surface** · parent N15
  - covered obligations: P-1: Create GIN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry; L-1: Create LN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A075 — Record cloning** · class **behaviour** · parent N15
  - covered obligations: P-1: Create GIN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry; L-1: Create LN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A079 — Draft saving of incomplete records** · class **behaviour** · parent N15
  - covered obligations: P-1.1: Incomplete records can be saved as Draft; L-1.1: Incomplete records can be saved as Draft
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A080 — Identifier registry per prefix** · class **store** · parent N14
  - covered obligations: P-2: Assign a GIN to a record automatically or manually at any point during record creation; a check digit is assigned automatically; P-8: View, filter and sort all GINs in a single view; L-2: Assign an LN to a record automatically or manually at any point during record creation; a check digit is assigned automatically
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A081 — Identifier assignment service (auto or manual at any creation step)** · class **behaviour** · parent N14
  - covered obligations: P-2: Assign a GIN to a record automatically or manually at any point during record creation; a check digit is assigned automatically; P-2.1: Users can opt for auto-assign or manual; P-3: Set a preference for how GINs are assigned (auto-assign or manual); L-2: Assign an LN to a record automatically or manually at any point during record creation; a check digit is assigned automatically; L-2.1: Some industries automatically assign LNs from a shared pool; L-2.2: The prefix licensee can opt for auto-assign or manual; NFR-16: Business process workflows: record approval (records entered via UI or import are submitted, reviewed, rejected or approved), record validation (identifiers, auto-generated or manual, comply with X-Customer Standards), record verification (attributes entered via UI or import are verified for accuracy); I-1: A web-based application solution for members to create, manage and share data related to prefixes, Global Item Numbers (GIN) and Location Numbers (LN), replacing the applications currently available to members
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A082 — Identifier reservation from auto-assign** · class **behaviour** · parent N14
  - covered obligations: P-2.2: A user can reserve GINs to hold them out from auto-assign; L-2.3: The prefix licensee can reserve LNs to hold them out from auto-assign
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A083 — Assignment mode preference** · class **store** · parent N14
  - covered obligations: P-3: Set a preference for how GINs are assigned (auto-assign or manual); L-3: Set a preference for how LNs are assigned (auto-assign or manual)
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A084 — Record edit form with finalise action** · class **surface** · parent N15
  - covered obligations: P-4: Edit record attributes before finalising; P-5: Edit record attributes manually or via import; L-4: Edit record attributes before finalising; L-5: Edit record attributes manually or via import; I-1: A web-based application solution for members to create, manage and share data related to prefixes, Global Item Numbers (GIN) and Location Numbers (LN), replacing the applications currently available to members
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A087 — Prior-identifier reference on number change** · class **store** · parent N14
  - covered obligations: P-5.2: If a GIN changes but the product attributes did not, a reference is kept back to the old number; L-5.1: If an LN changes but the location attributes do not, a reference is kept back to the old number
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A090 — Record list view with filter and sort** · class **surface** · parent N16
  - covered obligations: P-7: View, filter and sort all records in a single view; P-7.1: Select individual records to take any action (edit, export, etc.); P-7.2: Select multiple records and apply the same action to all selected records; L-6: View, filter and sort all records in a single view
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A091 — Single-record action menu** · class **surface** · parent N16
  - covered obligations: P-7.1: Select individual records to take any action (edit, export, etc.); L-6.1: Select individual records to take any action (edit, export, etc.)
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A092 — Multi-record bulk action** · class **behaviour** · parent N16
  - covered obligations: P-7.2: Select multiple records and apply the same action to all selected records; L-6.2: Select multiple records and apply the same action to all selected records
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A093 — Identifier list view with filter and sort** · class **surface** · parent N16
  - covered obligations: P-8: View, filter and sort all GINs in a single view; L-7: View, filter and sort all LNs in a single view
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A094 — Duplicate detection engine** · class **behaviour** · parent N17
  - covered obligations: P-9: View potential duplicate records and easily remove or edit duplicates; P-9.1: Alert the user of possible duplicate records during creation, and run duplicate reports for completed records; L-8: View potential duplicate records and easily remove or edit duplicates
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A095 — Duplicate review and resolution screen** · class **surface** · parent N17
  - covered obligations: P-9: View potential duplicate records and easily remove or edit duplicates; L-8: View potential duplicate records and easily remove or edit duplicates
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A097 — Creation-time duplicate alert** · class **surface** · parent N17
  - covered obligations: P-9.1: Alert the user of possible duplicate records during creation, and run duplicate reports for completed records; L-8.1: Alert the user of possible duplicate records during creation, and run duplicate reports for completed records
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A098 — Duplicate report for completed records** · class **surface** · parent N17
  - covered obligations: P-9.1: Alert the user of possible duplicate records during creation, and run duplicate reports for completed records; L-8.1: Alert the user of possible duplicate records during creation, and run duplicate reports for completed records
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A099 — Record status management** · class **behaviour** · parent N15
  - covered obligations: P-10: View and manage the status of a record or GIN; P-10.2: The system or the user can assign a status to each record; P-11.5: If the status of a record within a hierarchy changes, the user is notified if it affects the status of other records in the hierarchy; L-9: View and manage the status of a record or LN; L-9.2: The system or the user can assign a status to each record; I-1: A web-based application solution for members to create, manage and share data related to prefixes, Global Item Numbers (GIN) and Location Numbers (LN), replacing the applications currently available to members
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A100 — Identifier status management** · class **behaviour** · parent N14
  - covered obligations: P-10: View and manage the status of a record or GIN; P-10.1: The system or the user assigns a status to each GIN (currently Reserved, In Use, For Reuse, Available); GIN status may update to reflect record status; P-10.3: If a GIN is no longer in use, display the date it was taken out of use and when it becomes available for reuse; rules may vary by industry and product type; L-9: View and manage the status of a record or LN; L-9.1: The system or the user assigns a status to each LN; LN status may update to reflect record status
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A102 — Record-to-identifier status synchronisation** · class **behaviour** · parent N14
  - covered obligations: P-10.1: The system or the user assigns a status to each GIN (currently Reserved, In Use, For Reuse, Available); GIN status may update to reflect record status; L-9.1: The system or the user assigns a status to each LN; LN status may update to reflect record status
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A104 — Out-of-use and reuse date display** · class **surface** · parent N14
  - covered obligations: P-10.3: If a GIN is no longer in use, display the date it was taken out of use and when it becomes available for reuse; rules may vary by industry and product type; L-9.3: If an LN is no longer in use, display the date it was taken out of use and when it becomes available for reuse; rules may vary by industry
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A106 — Hierarchy tree editor (create, edit, view)** · class **surface** · parent N18
  - covered obligations: P-11: Create, edit and view a hierarchy of GINs (e.g. each → case → pallet) manually, via import, or via a visual format such as drag-and-drop; P-11.4: A user can change the item level on a record while creating a hierarchy; L-10: Create, edit and view a hierarchy of LNs manually, via import, or via a visual format such as drag-and-drop
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A107 — Drag-and-drop hierarchy canvas** · class **surface** · parent N18
  - covered obligations: P-11: Create, edit and view a hierarchy of GINs (e.g. each → case → pallet) manually, via import, or via a visual format such as drag-and-drop; L-10: Create, edit and view a hierarchy of LNs manually, via import, or via a visual format such as drag-and-drop
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A108 — Hierarchy import handling** · class **interface** · parent N18
  - covered obligations: P-11: Create, edit and view a hierarchy of GINs (e.g. each → case → pallet) manually, via import, or via a visual format such as drag-and-drop; P-11.2: Imports can include full records with hierarchy information, or hierarchy information for existing records; L-10: Create, edit and view a hierarchy of LNs manually, via import, or via a visual format such as drag-and-drop; L-10.2: Imports can include full records with hierarchy information, or hierarchy information for existing records
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A112 — Hierarchy status impact analysis** · class **behaviour** · parent N18
  - covered obligations: P-11.5: If the status of a record within a hierarchy changes, the user is notified if it affects the status of other records in the hierarchy; L-10.3: If the status of a record within a hierarchy changes, the user is notified if it affects the status of other records in the hierarchy
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A114 — Hierarchy export and print rendering** · class **surface** · parent N18
  - covered obligations: P-12: Export and print hierarchies in a user-friendly format; L-11: Export and print hierarchies in a user-friendly format
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A121 — Record ownership transfer** · class **behaviour** · parent N13
  - covered obligations: P-18: Transfer record ownership to another member; L-14: Transfer record ownership to another member
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **C15 — Hierarchy integrity check (cycles, orphans)** · class **behaviour** · parent N18
  - covered obligations: — (derived element, no covered obligation; trigger:A129,A106)
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
