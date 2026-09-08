# SAS — Assumption Log

**Version 1, 2026-09-08.** Written by the orchestrator from the RFP alone; adjudicated and approved
by the author the same day (A4, A6, A9, A16 explicitly).

Assumptions that close the RFP's gaps. Agreed before estimation begins; all runs must use the same
assumptions — otherwise their ranges are not comparable. Every narrowing names the reading taken
**and** the reading refused, per A0.

---

## A0. The imperative

`examples/BMS/assumptions.md` v2 **A0 applies verbatim**: an obligation the client stated cannot be
removed by an assumption. A log may bound what a number prices; every obligation ends as *priced
here*, *priced by another instrument*, or *not priceable without a named parameter*. An id that
appears nowhere is an exception, not a footnote.

## A1. What this estimate prices

Design, development, testing, data migration, deployment on the four-environment path, acceptance
and production cutover of the **first release** of the three modules, covering all product
obligations of `requirements_product.md` (N = 146) and the demanded work of `requirements_work.md`
(N = 7) to the extent A0 permits.

- **Included:** the four environments (NFR-11); migration of current data and users (NFR-12);
  performance testing against NFR-14 (NFR-15); acceptance support; the hand-over residue of W-4 —
  the support handover pack and the cutover itself.
- **Carried, not priced** (A0, outcome 3):
  - **W-4, the post-production support period and the transition service.** Missing parameters: the
    term and the service level. An open-ended obligation has no effort figure until somebody says
    for how long, and the instrument that prices it is a rate per unit time. *Question for the
    client: over what period, at what service level, does post-production support run?*
  - **NFR-5, the impact analysis on deviation from X-Customer technical standards.** Conditional
    work. Missing parameter: whether the proposed solution deviates. **Reading taken: it does not;
    count 0.** *The reading refused:* one or more deviations, each an analysis with technical,
    operational, support and financial parts.
- **Not applicable — excluded by the RFP itself, nothing is removed here:** onboarding of members
  and management of prefix attributes (Business Overview); the payment process (D-8.1); development
  of training materials (G-11.1); the future expansion of I-5 — the design must accommodate it, not
  contain it.

Every output produced under this log must show the carried-not-priced list above.

## A2. Definition of Done

The first release runs in production having passed through the four environments; acceptance has
passed (the RFP's contract term covers "design, development, testing, and acceptance"); migrated
data is loaded and reconciled; operational documentation exists — the runbook including the backup
and disaster-recovery procedures of NFR-9 and the failover procedure of NFR-8 — and the in-application
help content of G-10 is in place. Matches the declared `C-UAT`, `G-MIGRATE`, `U-OPS-USER`.

## A3. Team and delivery organisation

**Not assumed here.** Team grade, domain experience and staffing are case conditions and live in
`case_profile.md`, pinned before any run. The declaration assumes **one team at one site**
(`D-TEAM`) as a visible scope decision; the header of the document names an outsourcing vendor, so
the distributed alternative is real and is priced as a sensitivity in the declaration.

## A4. Identity — the reading of NFR-3 against G-1 and G-4

NFR-3 puts user accounts and roles in an enterprise Identity Management system; G-1 puts user
administration in the hands of a company admin inside the application. **Reading taken:** the IdM
issues claims through **one** claims-based protocol (SAML 2.0 or OpenID Connect over OAuth 2.0 —
one integration, whichever the client finalises); the application keeps its **own** company–user–role
model, maps claims onto it, and hosts the administration of G-1 (company admin adds users, assigns
roles and tasks). Password reset (G-4) is initiated in the application and executed by the IdM.
*The reading refused:* all user and role administration lives in the IdM, which would reduce
G-1.1, G-1.2 and G-4 to interface calls. Narrowing declared.

## A5. API management — 3scale exists and is used, not built

NFR-4 and G-7.2 name 3scale. **Reading taken:** the member-facing REST APIs (D-7, G-12.1) are
registered in the client's 3scale; usage reports by hour, day, week, month and year (G-7.2) are
read from 3scale's analytics API. *The reading refused:* building an API gateway, key management or
usage analytics of our own.

## A6. Import and export — six file formats plus the API, one adapter each

G-12.1 names Excel, CSV, Numbers (Apple), XML, tab-delimited, iDocs (SAP IDoc) and the API.
**Reading taken:** six file formats plus the API path, **each format a separate adapter** for import
and for export, validated on import (G-12.4). "PC and Mac formats" (G-12.2) are encoding and
line-ending variants handled inside the adapters, not further formats. **P-19 and L-15** ("use an
external system such as QuickBooks or SAP … and import it") are read as import through these
adapters and the API — IDoc is the SAP path — with **no bespoke QuickBooks or SAP connector**.
*The reading refused:* direct integrations with named accounting or ERP products. Narrowing declared.

## A7. Notifications and alerts

Email through the client's SMTP relay; SMS through an external gateway of the Twilio class, not our
own infrastructure; onscreen notifications in the application. G-3.2, G-8.x, P-11.5 and L-10.3 use
this one mechanism with preferences (G-8.5). NFR-17 and NFR-18 (system errors, critical business
function failures) are administrator alerts through the same mechanism, fed by application
monitoring hooks; **no monitoring product is built.** *The reading refused:* own SMS infrastructure;
a monitoring platform.

## A8. Data marts — a separate read store fed near-real-time

NFR-2 asks for non-transactional data marts and near-real-time latency. **Reading taken:** one
non-transactional read store, fed from the transactional store as changes occur; Access Data search
(D-1) and reports (G-7) read from it. "Near real-time" has no stated number; none is pinned. The
database platform is not named (NFR-1) and is not guessed. *The reading refused:* overnight batch
replication only.

## A9. Barcodes and the digital GIN — assumed content

P-13 and P-14 say "X-Customer Standard supported barcodes of various types and sizes" — a stated
plurality without named members. So that the model has something to count: **four symbologies —
UPC-A, EAN-13, ITF-14, GS1-128 —** generated with a barcode library, not written, at selectable sizes,
exported as PNG and SVG. **P-16**, the digital GIN embeddable in a web site, is read as an embeddable
snippet the solution generates — a QR image plus structured markup carrying the GIN — with **no
resolver service** behind it. *The reading refused:* a public resolver, which is I-5's future
expansion.

## A10. Industry variation is configuration, not variants

P-1, L-1, P-10.3, L-9.3, L-2.1 and G-10.1 say attribute sets, validation and reuse rules, LN pool
assignment and help content "may vary by industry". The RFP names 25 industries. **Reading taken:**
one configurable mechanism per varying thing, with per-industry parameters held as **configuration
data maintained by X-Customer**. The industry count is a data volume and multiplies no element.
*The reading refused:* industry-specific code paths.

## A11. Hierarchies — the two are different

P-11.x: GIN hierarchies have **pre-defined levels**, read as the three the RFP names — each, case,
pallet — with the physical-fit check of P-11.3 on height and weight between adjacent levels.
L-10.x: LN hierarchies have **unlimited depth** organised by attributes. Both are created manually,
by import, and by drag-and-drop.

## A12. Help content — an in-application editor

G-10.2 requires help content maintained by non-technical X-Customer staff. **Reading taken:** an
in-application help content editor with industry variants (G-10.1), contextual to screens.
*The reading refused:* integration with an external content management system.

## A13. Feedback and payment information — the thin entries

G-9: feedback submitted in the application and delivered by email to one configured X-Customer
address. *Refused:* integration with a ticketing system. D-8: an informational page maintained by
X-Customer explaining how to pay for ad hoc access; nothing transactional (D-8.1).

## A14. Reports — built in, over the read store

G-7.x: report definitions built into the solution — adds/changes/deletes with user customisation
(filters, columns, periods), scheduling, run history (G-7.3), audit reports (G-7.4) over the audit
trail of NFR-20 — reading from the store of A8. *Refused:* a third-party business-intelligence product.

## A15. Publish-and-subscribe is one mechanism seen from two sides

G-13.x, P-17 and L-12 state the **owner's** side; D-2, D-2.1, D-3 and D-4 state the **consumer's**
side; I-8–I-11 state the module. One mechanism realises all of them. M1 forbids merging the entries,
so the sensors cover them jointly and record the overlap. **Public access** (I-10): anonymous users
search a limited data set through the same Access Data module and cannot export.

## A16. Migration — source and entity kinds

NFR-12: the source is **the current member applications** (several; I-1 says "applications"). The
entity kinds migrated: **companies and their prefixes · users and roles · GIN records · LN records ·
hierarchies · publish/subscribe permissions · product images** — seven. Volumes as NFR-2 states them
for the current record counts. Migration rehearsal cycles are a declaration parameter: **2**.

## A17. Environments — four, and a catalogue mapping to declare

NFR-11 names four: development, test, staging/pre-production, production. Catalogue 1.4's `E1`
mapping names three (dev = S, stage = M, prod = L). **Reading taken: `test` = M** — a shared
integration environment, production-like enough to run the test cycles, not hardened. Recorded in
the declaration as a catalogue amendment proposal; it adds one `E1` item and moves nothing else.

## A18. Organisational context

The client is a large not-for-profit standards organisation serving more than 200 000 member
companies in 25 industries; approval speed and the availability of client specialists are those of
an enterprise. The document header names EPAM Systems as the receiving vendor. Accounted for only in
the reference class; the bottom-up chain does not see it.

## A19. Units and the era

Effort is stated per `docs/instrument.md` §0 — net task hours; the presence conversion of
`docs/constants.md` §4a applies in the comparison layer only. No sensor sees either. The RFP is
dated **September 2018** (Internet Explorer 9 support, SOAP as an option, 3scale); the rate table is
compiled from modern norms and the era transfer is **not pre-adjusted**, as on FaxRxTx.

## A20. This log is checked against the pinned lists before any run

| assumption | touches | relation |
|---|---|---|
| A1 | W-4, NFR-5 | bounds what is priced; carries the remainder under A0 |
| A1 | G-11.1, D-8.1, I-5, Business Overview | records the RFP's own exclusions |
| A2 | W-3, W-4, NFR-8, NFR-9, G-10 | matches `C-UAT`, `G-MIGRATE`, `U-OPS-USER` |
| A3 | — | matches `D-TEAM`; the case profile carries the team |
| A4 | NFR-3, G-1.x, G-4 | narrowing, declared |
| A5 | NFR-4, G-7.2, D-7 | narrowing, declared |
| A6 | G-12.x, D-5, P-19, L-15 | narrowing, declared |
| A7 | G-8.x, G-3.2, P-11.5, L-10.3, NFR-17, NFR-18 | narrowing, declared |
| A8 | NFR-2, D-1, G-7 | reading, declared |
| A9 | P-13, P-14, P-16 | supplies content the RFP omits |
| A10 | P-1, L-1, P-10.3, L-9.3, L-2.1, G-10.1 | reading, declared |
| A11 | P-11.x, L-10.x | reading, declared |
| A12 | G-10.x | narrowing, declared |
| A13 | G-9, D-8 | narrowing, declared |
| A14 | G-7.x, NFR-20 | narrowing, declared |
| A15 | G-13.x, P-17, L-12, D-2–D-4, I-8–I-11 | overlap, declared |
| A16 | NFR-12, NFR-2 | supplies the migration scope the RFP omits |
| A17 | NFR-11 | declaration parameter and a catalogue mapping |
| A21 | the register | points at `open_questions.md` |

Nothing in this log contradicts an entry of either list. Any future edit to the log, the lists or
the declaration re-runs this table.

## A21. Open questions stand behind these assumptions

The register is `open_questions.md`, pinned like the lists. This RFP is a training document with no
client to ask, so every question is `not asked` and the assumptions are what the estimate rests on.
The comparison rule of `examples/BMS/assumptions.md` A11 applies unchanged: every comparison of two
runs is reported over all requirements and excluding the ids the register names.

---

## Changelog

**v1 draft, 2026-09-08** — first version, written from the RFP alone by the orchestrator. Not yet
adjudicated by the author; not yet pinned.
