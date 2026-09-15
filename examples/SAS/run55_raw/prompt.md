Build the product model of the case below, as your engine definition requires.

**Input.** This message is your whole input. INPUT 1 (the pinned product obligation list) and INPUT 2 (the product assumption projection) are pasted below, each whole. Do not read, open, list or search any file; use no tool.

**Declared processing order: order A** — the table order of INPUT 1, top to bottom (I → G → P → L → D → NFR).

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, a memory index, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, beginning at section 1 and ending at section 9, with every section the engine definition requires. In §6 give every node its parent. Do not compact any section.

---

# INPUT 1 — requirements_product.md

# SAS — product obligation list (`Hotyn-M` input)

Derived from `requirements_pinned.md` (N = 153) by the split recorded in `requirements_split.md`.
Seven entries — W-1, W-2, W-3, W-4, NFR-11, NFR-12, NFR-15 — are obligations on the **work** and live
in `requirements_work.md`. **Ids are unchanged**, so the two lists together are exactly the pinned
list and every id still means what it meant.

This is the **external anchor** for `Hotyn-M` per `docs/proposal_product_model.md` §3 and M1.

**A run may not add, remove, split or merge entries.** Where an entry looks like it contains two
obligations, the run flags it as ambiguous and proceeds. Revising this list is a separate, deliberate
act performed once for everybody.

Granularity rule inherited from `requirements_pinned.md`: **one entry per obligation as the RFP
words it**, under the RFP's own ids where the RFP numbers them.

Declared processing order A: the order of this table (I → G → P → L → D → NFR), which is the RFP's
own order. Order B is the exact reverse.

---

## The list

| id | obligation | source |
|---|---|---|
| I-1 | A web-based application solution for members to create, manage and share data related to prefixes, Global Item Numbers (GIN) and Location Numbers (LN), replacing the applications currently available to members | §1 Introduction · Project Goals |
| I-2 | Three integrated modules — Product (GIN), Location (LN), Access Data — using the same data and system architecture and running on the same development platform | Project Goals |
| I-3 | Identifier rules: a GIN is 12 or 14 digits and an LN is 13 digits, each formed as the company's licensed prefix (6–9 digits) plus a serial part, with a check digit | Business Overview |
| I-4 | An application architecture aligned with the existing enterprise architecture, maintainable by X-Customer resources, and scalable and sustainable given the projected member and application growth | Project Goals, goal 2 |
| I-5 | The final design accommodates future expansion — data other than GIN or LN, and sharing privileges down to field level — while that expansion itself stays out of scope | Project Goals, future expansion |
| I-6 | Functionality available to all members based on permissions, regardless of which module they use; data and functions are shared across modules | General Requirements, preamble |
| I-7 | All functionality is validated against X-Customer Standards and business rules, which will be defined as part of the project | General Requirements, preamble |
| I-8 | The Access Data module allows users to search for, view and export prefix, GIN and LN data — the subscribe side of the publish-and-subscribe model — and contains no editing functionality | Access Data, preamble |
| I-9 | A client's subscription determines which data can be viewed and which export options are available | Access Data, preamble |
| I-10 | Non-members (the general public) can search a limited data set but cannot export | Access Data, preamble |
| I-11 | X-Customer-owned data as well as data published by data owners can be accessed in the Access Data module | Access Data, preamble |
| G-1 | Allow assignment of user roles and tasks | General |
| G-1.1 | Each member is assigned a company administrator with the ability to add and edit other users in their company | General |
| G-1.2 | The company admin can assign roles and tasks to users | General |
| G-1.3 | User roles include Super-User, Approver, Editor, View-only; other roles may be added | General |
| G-1.4 | A customer-level "Super-User" role with access to manage all data | General |
| G-2 | Present a role-driven UI based on user role | General |
| G-3 | Implement a workflow for new and edited records | General |
| G-3.1 | The company admin can designate Editor and Approver roles and the rules for record approval | General |
| G-3.2 | Editors and Approvers are notified of a change in approval status | General |
| G-3.3 | Users can easily find records requiring their action | General |
| G-4 | A user's password can be reset by the user, the company admin, or the X-Customer help desk | General |
| G-5 | Lock records so that only one user at a time can edit a record | General |
| G-6 | Display a user dashboard or start screen with notifications, reports, prefix data and other information | General |
| G-6.1 | A prefix capacity counter displays how many numeric indicators (GINs or LNs) have been used and how many are available | General |
| G-7 | Allow users to generate reports | General |
| G-7.1 | Customise, schedule, run and view reports for adds, changes and deletes | General |
| G-7.2 | View usage reports by hour, day, week, month and year *(current reporting utilises 3scale)* | General |
| G-7.3 | Run report data history | General |
| G-7.4 | Run audit reports | General |
| G-8 | Provide notifications to users in various formats — email, SMS and/or onscreen | General |
| G-8.1 | Global notifications (e.g. scheduled server downtime) | General |
| G-8.2 | Member-specific notifications (e.g. a user opts to be notified when records are updated or added) | General |
| G-8.3 | Member-to-member and member-to-X-Customer notifications (e.g. a user can challenge record data) | General |
| G-8.5 | A user can set communication preferences for the method and frequency of notifications received outside the system | General |
| G-9 | Users can send application feedback to X-Customer, routed to a single X-Customer contact or a feedback tracking system | General |
| G-10 | Display contextual help to the user | General |
| G-10.1 | Help content may be customised by industry | General |
| G-10.2 | Help content is maintained by X-Customer non-technical resources | General |
| G-11 | Link to training — external videos, webinars, quick-start guides — from within the application | General |
| G-12 | Allow import and export of records, as referenced in the Product, Location and Data Access modules | General |
| G-12.1 | Import and export formats include at least Excel, CSV, Numbers, XML, tab-delimited, iDocs, and through the API | General |
| G-12.2 | Import and export must include PC and Mac formats | General |
| G-12.3 | A user can select one or more records to be imported or exported | General |
| G-12.4 | All records are validated upon import | General |
| G-13 | A publish (select for sharing by the data owner) and subscribe (request viewing by data consumers) model with multiple share/view functions | General |
| G-13.1 | The data owner can publish records at any level in the hierarchy | General |
| G-13.2 | The data owner can publish (grant access to view) a basic or a full set of record attributes | General |
| G-13.3 | The data owner can publish data for a group of records | General |
| G-13.4 | The data owner can share records with an individual, a user-defined group, a controlled group managed by X-Customer, or the public | General |
| G-13.5 | Based on subscription, a data consumer can view published data | General |
| G-13.6 | Based on subscription, a data consumer can request access to view data from the data owner | General |
| G-13.7 | The data owner can approve or reject view requests | General |
| P-1 | Create GIN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry | Product |
| P-1.1 | Incomplete records can be saved as Draft | Product |
| P-2 | Assign a GIN to a record automatically or manually at any point during record creation; a check digit is assigned automatically | Product |
| P-2.1 | Users can opt for auto-assign or manual | Product |
| P-2.2 | A user can reserve GINs to hold them out from auto-assign | Product |
| P-3 | Set a preference for how GINs are assigned (auto-assign or manual) | Product |
| P-4 | Edit record attributes before finalising | Product |
| P-5 | Edit record attributes manually or via import | Product |
| P-5.1 | Some attributes cannot be edited, based on status (e.g. once a product has gone to market) | Product |
| P-5.2 | If a GIN changes but the product attributes did not, a reference is kept back to the old number | Product |
| P-6 | Upload product images and add them to records | Product |
| P-7 | View, filter and sort all records in a single view | Product |
| P-7.1 | Select individual records to take any action (edit, export, etc.) | Product |
| P-7.2 | Select multiple records and apply the same action to all selected records | Product |
| P-8 | View, filter and sort all GINs in a single view | Product |
| P-9 | View potential duplicate records and easily remove or edit duplicates | Product |
| P-9.1 | Alert the user of possible duplicate records during creation, and run duplicate reports for completed records | Product |
| P-10 | View and manage the status of a record or GIN | Product |
| P-10.1 | The system or the user assigns a status to each GIN (currently Reserved, In Use, For Reuse, Available); GIN status may update to reflect record status | Product |
| P-10.2 | The system or the user can assign a status to each record | Product |
| P-10.3 | If a GIN is no longer in use, display the date it was taken out of use and when it becomes available for reuse; rules may vary by industry and product type | Product |
| P-11 | Create, edit and view a hierarchy of GINs (e.g. each → case → pallet) manually, via import, or via a visual format such as drag-and-drop | Product |
| P-11.1 | Hierarchies can have pre-defined levels | Product |
| P-11.2 | Imports can include full records with hierarchy information, or hierarchy information for existing records | Product |
| P-11.3 | The system checks that each item type can physically fit into the next item type in the hierarchy (height and weight) | Product |
| P-11.4 | A user can change the item level on a record while creating a hierarchy | Product |
| P-11.5 | If the status of a record within a hierarchy changes, the user is notified if it affects the status of other records in the hierarchy | Product |
| P-12 | Export and print hierarchies in a user-friendly format | Product |
| P-13 | Generate and view X-Customer Standard supported barcodes of various types and sizes | Product |
| P-14 | Export and print X-Customer Standard supported barcodes in standard image formats | Product |
| P-15 | Create, save, export and print Product Information Sheets for each record, with all record attributes and images | Product |
| P-15.1 | Users can select from and edit multiple page-layout templates for product sheets | Product |
| P-16 | Create a digital GIN that can be embedded in a web site | Product |
| P-17 | Permission records for publishing; published records are viewed within the Data Access module | Product |
| P-18 | Transfer record ownership to another member | Product |
| P-19 | Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution | Product |
| L-1 | Create LN records individually, via import, through a step-by-step wizard, or by cloning an existing record; records include required and non-required attributes that may vary by industry | Location |
| L-1.1 | Incomplete records can be saved as Draft | Location |
| L-2 | Assign an LN to a record automatically or manually at any point during record creation; a check digit is assigned automatically | Location |
| L-2.1 | Some industries automatically assign LNs from a shared pool | Location |
| L-2.2 | The prefix licensee can opt for auto-assign or manual | Location |
| L-2.3 | The prefix licensee can reserve LNs to hold them out from auto-assign | Location |
| L-3 | Set a preference for how LNs are assigned (auto-assign or manual) | Location |
| L-4 | Edit record attributes before finalising | Location |
| L-5 | Edit record attributes manually or via import | Location |
| L-5.1 | If an LN changes but the location attributes do not, a reference is kept back to the old number | Location |
| L-6 | View, filter and sort all records in a single view | Location |
| L-6.1 | Select individual records to take any action (edit, export, etc.) | Location |
| L-6.2 | Select multiple records and apply the same action to all selected records | Location |
| L-7 | View, filter and sort all LNs in a single view | Location |
| L-8 | View potential duplicate records and easily remove or edit duplicates | Location |
| L-8.1 | Alert the user of possible duplicate records during creation, and run duplicate reports for completed records | Location |
| L-9 | View and manage the status of a record or LN | Location |
| L-9.1 | The system or the user assigns a status to each LN; LN status may update to reflect record status | Location |
| L-9.2 | The system or the user can assign a status to each record | Location |
| L-9.3 | If an LN is no longer in use, display the date it was taken out of use and when it becomes available for reuse; rules may vary by industry | Location |
| L-10 | Create, edit and view a hierarchy of LNs manually, via import, or via a visual format such as drag-and-drop | Location |
| L-10.1 | Hierarchies can have an unlimited number of levels and be organised by various attributes | Location |
| L-10.2 | Imports can include full records with hierarchy information, or hierarchy information for existing records | Location |
| L-10.3 | If the status of a record within a hierarchy changes, the user is notified if it affects the status of other records in the hierarchy | Location |
| L-11 | Export and print hierarchies in a user-friendly format | Location |
| L-12 | Permission records for publishing; published records are viewed within the Data Access module | Location |
| L-13 | Record annual verification of records | Location |
| L-14 | Transfer record ownership to another member | Location |
| L-15 | Use an external system (e.g. QuickBooks, SAP) to create and manage data and import it into the application solution | Location |
| D-1 | Search for prefix, GIN and LN records | Access Data |
| D-1.1 | Several fields are available for search (e.g. name, city) | Access Data |
| D-1.2 | Advanced search and filter options are available | Access Data |
| D-2 | Request access to a basic or full record (subscribe to the record) | Access Data |
| D-2.1 | The request is sent to the data owner, who must approve before the data becomes available | Access Data |
| D-3 | Request to be added to a controlled group | Access Data |
| D-4 | View basic and full records and their hierarchies | Access Data |
| D-5 | Export one or more records to any format detailed in the General Requirements | Access Data |
| D-6 | Print one or more records | Access Data |
| D-7 | Perform all Access Data functions via the web interface or the API | Access Data |
| D-8 | Easily access information on how to pay for ad hoc access to data | Access Data |
| NFR-2 | Data marts (non-transactional) to support data access; transactional and non-transactional databases scalable for the projected growth (company prefixes 500 000 → 700 000 records, GIN 10 000 000 → 70 000 000, LN 550 000 → 3 500 000, by 2024); data latency is currently overnight and must support near-real-time updates | Technical |
| NFR-3 | Claims-based authentication and authorisation; user accounts and roles defined in an enterprise Identity Management system enabling single sign-on; the IdM solution is not finalised and will support claims-based standards such as OAuth and SAML | Technical |
| NFR-4 | A service-oriented architecture: REST (preferred) or SOAP web services integrate functionality and data across the suite instead of direct database access or copying; REST APIs available to members and compatible with an API management solution (currently 3scale) | Technical |
| NFR-5 | Adherence to X-Customer technical standards — coding, database connection and naming, integration, approved technologies and products; a deviation requires an impact analysis (technical, operational, support, financial) by the project core team at no cost to X-Customer | Technical |
| NFR-6 | The architecture is designed to be cloud-ready | Technical |
| NFR-7 | Web-based, built on industry-standard web design patterns, frameworks and components, with no client-side software installation; roughly 38 000 users today, approximately 256 000 by 2024, up to 10% of them concurrent | Technical |
| NFR-8 | Highly available with a 99.9% service level; a failover process developed and tested, with the hardware and software needs identified, and failover monitoring that notifies administrators of a failure | Technical |
| NFR-9 | Backup and disaster recovery procedures that comply with X-Customer policies and procedures | Technical |
| NFR-10 | Appropriate security configuration, processes and procedures, with a security design and the components, frameworks, libraries and tools used to secure the application solution | Technical |
| NFR-13 | Accessible on Internet Explorer 9 and above, and on the current and previous versions of Chrome, Firefox, Safari and Edge | Technical |
| NFR-14 | Response times, 95% of the time under load: login under 2 s at 250 concurrent users; navigation under 1 s at 250; transactions (saves, form generation) under 2 s at 50; searches under 3 s at 150; API responses under 1 s at 250 | Technical |
| NFR-16 | Business process workflows: record approval (records entered via UI or import are submitted, reviewed, rejected or approved), record validation (identifiers, auto-generated or manual, comply with X-Customer Standards), record verification (attributes entered via UI or import are verified for accuracy) | Technical |
| NFR-17 | Near-real-time event notifications when system errors occur | Technical |
| NFR-18 | Near-real-time event notification when critical business functions fail | Technical |
| NFR-19 | Detailed logging for troubleshooting and process verification | Technical |
| NFR-20 | An audit trail of all activity taking place at any point in the system | Technical |
| NFR-21 | WCAG 2.0 Level A compliance, within reasonable accommodation | Technical |

**N = 146.**

---

## Pin

Recorded in `requirements.pin.txt`. Recompute with:

    tr -d '\r' < requirements_product.md | md5sum

---

# INPUT 2 — assumptions_product.md

# SAS — assumptions a product-model run may see

**Pinned input, version 1, 2026-09-08.** The projection of `assumptions.md` (A1–A21) onto the
product: only what constrains **what must exist**. The SAS analogue of
`examples/BMS/assumptions_product.md`.

Why a projection and not the log itself: the log speaks about what is priced, what is carried, the
team, the definition of done, environments, cycles and units. A product-model run must not see that
vocabulary — a builder shown the language of work starts building work. What is removed is removed
because it is about the doing, never because it is inconvenient.

**Removed here, and where it lives:** what is priced and what is carried (A1) · the definition of
done (A2) · the team and the delivery organisation (A3) · the migration act and its cycles (A16) · the
environments (A17) · the organisational context (A18) · units and the era (A19). None of them says
anything about what the product is.

---

## P1. Scope of the thing being modelled

The **first release** of a web-based member application solution with three integrated modules —
Product (GIN), Location (LN), Access Data — covering every obligation in `requirements_product.md`
(N = 146). It replaces the applications members use today (I-1); what is modelled is the new
solution, not its predecessors.

**The following are not part of the product and are not in your list:** onboarding of members and
management of prefix attributes (the RFP places them outside scope — prefixes arrive already
licensed, with their attributes); the payment process for ad hoc access (D-8 is an informational
page only); training materials (G-11 links to them); the future expansion of I-5 (data types other
than GIN and LN, field-level sharing) — the design must accommodate it, not contain it.

If your structure seems to need a prefix-licensing workflow, a payment flow, a training module or a
generic "any data type" engine as a component, that is the signal you have crossed out of the
product; say so rather than building it.

## P2. External and pre-existing things the system integrates with

Each is **used, not built**. Model the exchange, never the thing.

- **The enterprise Identity Management system** (NFR-3) — issues claims through one claims-based
  protocol (SAML 2.0 or OpenID Connect; the client has not finalised which). The application keeps
  its own company–user–role model and maps claims onto it; the administration of G-1 happens in the
  application; password reset (G-4) is initiated in the application and executed by the IdM.
- **3scale, the client's API management platform** (NFR-4, G-7.2, D-7) — the member-facing REST
  APIs are registered there; API usage figures for the usage reports of G-7.2 are read from its
  analytics API. No gateway, key management or usage analytics of our own.
- **The client's SMTP relay** and **an external SMS gateway** (Twilio class) — email and SMS delivery
  for G-8. Onscreen notifications are the application's own.
- **A barcode library** — the symbologies of P-13/P-14 are generated with it, not written.
- **External systems such as QuickBooks or SAP** (P-19, L-15) — sources of data that arrive through
  the import formats and the API of G-12.1. **No bespoke connector to any named product**; SAP's path
  is IDoc.
- **The current member applications** — the predecessors. Their data will be loaded into the new
  system's stores; that loading is not a component of the product and is not in your list. What *is*
  in your list is every property the new system must have about old identifiers (P-5.2, L-5.1: a
  reference back to a changed number).
- **The database and data-mart platforms** — not named (NFR-1) and not to be guessed. Read them as
  *stores the system owns schemas in*; do not model a DBMS.

## P3. Readings taken where an entry can be read two ways

| ids | reading taken |
|---|---|
| **P-* / L-* twins** (P-1/L-1, P-1.1/L-1.1, P-2/L-2, P-3/L-3, P-4/L-4, P-5/L-5, P-5.2/L-5.1, P-7/L-6, P-7.1/L-6.1, P-7.2/L-6.2, P-8/L-7, P-9/L-8, P-9.1/L-8.1, P-10/L-9, P-10.1/L-9.1, P-10.2/L-9.2, P-10.3/L-9.3, P-11/L-10, P-11.2/L-10.2, P-11.5/L-10.3, P-12/L-11, P-17/L-12, P-18/L-14, P-19/L-15) | the RFP states the same obligation once for products and once for locations, and says the two record kinds differ in attributes, identifier format, hierarchy rules and status rules. **Model what is genuinely shared once, and what differs per kind separately.** You may not merge the twin entries (M1); a shared node covers both ids, and a per-kind node covers one. Say which you did |
| I-2 | "three integrated modules" is a statement about the **product's organisation** — one platform, shared data — not a requirement to build three separate applications. Whether the modules are one application or a suite is left to design by the RFP itself |
| I-6, G-2 | permission-based, role-driven access applies **across** modules — one authorisation mechanism, not one per module |
| I-7, NFR-16 | validation against X-Customer Standards and business rules is a **behaviour** of the system (validation on entry, on import, on identifier assignment). The rules themselves will be defined during the project; treat them as a configurable rule set, not as content you invent |
| NFR-3 / G-1.x / G-4 | see P2: the application owns its user model and administration; the IdM authenticates |
| G-12.1, G-12.2, D-5 | **six file formats** — Excel, CSV, Numbers, XML, tab-delimited, IDoc — plus the API, each format its own import and export adapter; PC/Mac are encoding and line-ending variants inside the adapters, not further formats. Do not invent formats |
| P-19, L-15 | import from external systems goes through the adapters and API above; there is no connector to QuickBooks or SAP as such |
| G-13.x, P-17, L-12, D-2, D-2.1, D-3, D-4, I-8–I-11 | **one publish-and-subscribe mechanism** stated from the owner's side (G-13, P-17, L-12) and the consumer's side (D-2–D-4); cover jointly, record the overlap. Public, non-member access (I-10) is the anonymous case of the same module: limited data, no export |
| P-1, L-1, P-10.3, L-9.3, L-2.1, G-10.1 | "may vary by industry" means **configuration data** per industry — attribute sets, validation and reuse rules, LN pool assignment, help content — held in a configuration store maintained by X-Customer. 25 industries is a volume, not 25 variants |
| P-11.x | GIN hierarchies have **pre-defined levels: each, case, pallet**, with a physical-fit check on height and weight between adjacent levels |
| L-10.x | LN hierarchies have **unlimited depth**, organised by attributes |
| P-13, P-14 | **four barcode symbologies — UPC-A, EAN-13, ITF-14, GS1-128 —** at selectable sizes, exported as PNG and SVG. Do not invent further symbologies |
| P-16 | a digital GIN is an **embeddable snippet** the solution generates — a QR image plus structured markup carrying the GIN. No resolver service behind it |
| G-7.x | reports are **built into the solution** — definitions for adds/changes/deletes with customisation, scheduling, run history, audit reports over the audit trail of NFR-20 — reading from a non-transactional read store (NFR-2) |
| NFR-2 | one **non-transactional read store** fed near-real-time from the transactional store; Access Data search (D-1) and reports read from it. "Near real-time" carries no number; do not pin one |
| G-10.x | an **in-application help content editor** for non-technical X-Customer staff, with industry variants |
| G-9 | feedback is submitted in the application and delivered by email to one configured address |
| D-8 | an informational page, maintained by X-Customer, on how to pay; nothing transactional |
| NFR-17, NFR-18 | administrator alerts through the notification mechanism of G-8, fed by application monitoring hooks; no monitoring product |
| NFR-8, NFR-9 | availability, failover with monitoring, backup and recovery are **properties the design must meet**; the failover process and the recovery procedures are part of the product's operational design |
| NFR-2, NFR-7, NFR-14 | the volume, user and response-time figures are **properties the design must meet**, not components |
| G-6 | "and other information" names nothing and adds nothing (precedent P-5 of the catalogue); the dashboard shows notifications, reports, prefix data and the capacity counter of G-6.1 |
| G-1.3 | four named roles; "other roles may be added" means the role set is **configurable**, not that further roles exist |
| G-1, G-1.2 | "tasks" are responsibilities inside the record workflow — which records or record kinds a user edits or approves — realised through the approval rules of G-3.1 and the action lists of G-3.3 |
| L-13 | the system **records** an annual verification per location record (who, when, outcome) and can show what is due; it does not run a campaign |
| I-1 | "replacing the applications currently available" is a scope statement on the artefact — what it is instead of — not a migration and not a decommissioning |
| I-4, I-5, NFR-6 | architectural properties — alignment, maintainability, scalability, cloud-readiness, room for future data types and field-level sharing — are **statements** the design must hold, not components |

## P4. Thin entries and their assumed content

- **G-11**, the link to training: a configurable set of external links surfaced in the application.
- **I-11**, X-Customer-owned data is accessible: the read store holds X-Customer's own reference
  data (prefix registry, controlled groups) alongside members' published data, under the same
  access rules.
- **D-3**, request to be added to a controlled group: a request to X-Customer, approved by
  X-Customer staff, that changes the requester's membership of a group X-Customer manages (G-13.4).

## Pin

    tr -d '\r' < assumptions_product.md | md5sum

Parents: `assumptions.md` v1 draft, `open_questions.md` v1 draft, `requirements_product.md`
(N = 146; md5 in `requirements.pin.txt`).
