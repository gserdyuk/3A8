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
