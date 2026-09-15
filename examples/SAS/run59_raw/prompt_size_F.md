Size the elements of the work model batch below by classifying, not pricing. Everything you need is in this message; read no files.

**Scope: the subtrees rooted at N19, N20 of the product model `HM57-1`, as classified and crossed by `Hotyn-W 1.2`** — 28 sized elements (aggregates are listed for context and are never sized). Other subtrees and the model root are outside this batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, sections 1 to 7 as your engine definition requires. In the sizing table quote the enumeration verbatim, one row per sized element, grouped by subtree. Every number you output is a count of named things; nothing else.

---

# INPUT 1 — the work model batch: elements with class, parent, declared content, covered obligations (with their texts) and the activities crossed onto them

In this model coverage lives in leaves only: an aggregate's content is its children. A derived leaf has no covered obligation; its declared content is its name read with the trigger that called for it (the elements named after `trigger:`).


**N19 — Product module** · aggregate (not sized) · parent N01

**N20 — Location module** · aggregate (not sized) · parent N01

**N23 — Product outputs** · aggregate (not sized) · parent N19
- **A077 — Product attribute sets by industry** · class **store** · parent N19
  - covered obligations: P-1: Create GIN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A078 — Product record import mapping** · class **behaviour** · parent N19
  - covered obligations: P-1: Create GIN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry; P-5: Edit record attributes manually or via import; P-19: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A086 — Product attribute freeze by status** · class **behaviour** · parent N19
  - covered obligations: P-5.1: Some attributes cannot be edited, based on status (e.g. once a product has gone to market)
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A088 — Product image upload and attachment** · class **behaviour** · parent N19
  - covered obligations: P-6: Upload product images and add them to records
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A096 — Product duplicate match criteria** · class **behaviour** · parent N19
  - covered obligations: P-9: View potential duplicate records and easily remove or edit duplicates
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A101 — GIN status model (Reserved, In Use, For Reuse, Available)** · class **behaviour** · parent N19
  - covered obligations: P-10.1: The system or the user assigns a status to each GIN (currently Reserved, In Use, For Reuse, Available); GIN status may update to reflect record status
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A103 — Product record status model** · class **behaviour** · parent N19
  - covered obligations: P-10.2: The system or the user can assign a status to each record
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A105 — Product identifier reuse rules by industry and product type** · class **behaviour** · parent N19
  - covered obligations: P-10.3: If a GIN is no longer in use, display the date it was taken out of use and when it becomes available for reuse; rules may vary by industry and product type
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A109 — GIN hierarchy model (each, case, pallet)** · class **store** · parent N19
  - covered obligations: P-11: Create, edit and view a hierarchy of GINs (e.g. each → case → pallet) manually, via import, or via a visual format such as drag-and-drop; P-11.1: Hierarchies can have pre-defined levels
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A110 — Physical fit check (height, weight)** · class **behaviour** · parent N19
  - covered obligations: P-11.3: The system checks that each item type can physically fit into the next item type in the hierarchy (height and weight)
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A111 — Item level change while building hierarchy** · class **behaviour** · parent N19
  - covered obligations: P-11.4: A user can change the item level on a record while creating a hierarchy
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A115 — Barcode generation service (UPC-A, EAN-13, ITF-14, GS1-128; selectable sizes)** · class **behaviour** · parent N23
  - covered obligations: P-13: Generate and view X-Customer Standard supported barcodes of various types and sizes; P-14: Export and print X-Customer Standard supported barcodes in standard image formats
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A116 — Barcode viewer** · class **surface** · parent N23
  - covered obligations: P-13: Generate and view X-Customer Standard supported barcodes of various types and sizes
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A117 — Barcode image export (PNG, SVG) and print** · class **surface** · parent N23
  - covered obligations: P-14: Export and print X-Customer Standard supported barcodes in standard image formats
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A118 — Product information sheet generator (create, save, export, print)** · class **surface** · parent N23
  - covered obligations: P-15: Create, save, export and print Product Information Sheets for each record, with all record attributes and images; P-15.1: Users can select from and edit multiple page-layout templates for product sheets
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A119 — Sheet page-layout template library and editor** · class **surface** · parent N23
  - covered obligations: P-15.1: Users can select from and edit multiple page-layout templates for product sheets
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A120 — Digital GIN embeddable snippet generator (QR plus markup)** · class **behaviour** · parent N23
  - covered obligations: P-16: Create a digital GIN that can be embedded in a web site
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A122 — Location attribute sets by industry** · class **store** · parent N20
  - covered obligations: L-1: Create LN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A123 — Location record import mapping** · class **behaviour** · parent N20
  - covered obligations: L-1: Create LN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry; L-5: Edit record attributes manually or via import; L-15: Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A124 — Shared LN pool assignment by industry** · class **behaviour** · parent N20
  - covered obligations: L-2.1: Some industries automatically assign LNs from a shared pool
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A125 — Location duplicate match criteria** · class **behaviour** · parent N20
  - covered obligations: L-8: View potential duplicate records and easily remove or edit duplicates
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A126 — LN status model** · class **behaviour** · parent N20
  - covered obligations: L-9.1: The system or the user assigns a status to each LN; LN status may update to reflect record status
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A127 — Location record status model** · class **behaviour** · parent N20
  - covered obligations: L-9.2: The system or the user can assign a status to each record
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A128 — Location identifier reuse rules by industry** · class **behaviour** · parent N20
  - covered obligations: L-9.3: If an LN is no longer in use, display the date it was taken out of use and when it becomes available for reuse; rules may vary by industry
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A129 — LN hierarchy model (unlimited depth)** · class **store** · parent N20
  - covered obligations: L-10: Create, edit and view a hierarchy of LNs manually, via import, or via a visual format such as drag-and-drop; L-10.1: Hierarchies can have an unlimited number of levels and be organised by various attributes
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A130 — Attribute-based organisation of LN hierarchies** · class **behaviour** · parent N20
  - covered obligations: L-10.1: Hierarchies can have an unlimited number of levels and be organised by various attributes
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A131 — Annual verification record (who, when, outcome)** · class **store** · parent N20
  - covered obligations: L-13: Record annual verification of records
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A132 — Verification due list** · class **surface** · parent N20
  - covered obligations: L-13: Record annual verification of records
  - activities crossed onto it: A2, A3, A4, D4, K1, K2

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
