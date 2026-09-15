<!-- RECOVERED PROMPT, saved 2026-09-16 by the orchestrating session. Run 48 (2026-09-08) did not save its prompts; this is the
first user message of the sensor's harness transcript (~/.claude/projects/C--home-OhmNova-3A8/1aa37d94-54a2-4aac-be66-6c31c082b401/
subagents/agent-a000e47f2e80cc8d6.jsonl), extracted by script, nothing inserted or removed. md5 of the body: 38fada9cd66ff17a45d29bc237af892d. -->

You are performing Steps B and D for the project described below. Everything you need is in this message; read no files.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, a branch name, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your input inventory that it was present and that you quarantined it, and proceed on the pasted input alone.

**On the actual outcome: there is none.** This RFP was never awarded to the estimating side and no delivery record exists; the case has no outcome to open now or later. Nothing below is an actual. Your report is a diagnosis between instruments, not a validation of either.

**Engine chain of your inputs, from the launch records (the sensors' own stamps are inside their texts):**
- bottom-up: product model `Hotyn-M 1.1` (n = 2, first reading carried) → work model `Hotyn-W 1.1` (seven batches) → size classes `Hotyn-D 2.0` (n = 2, both repeats priced) × rate table v0.1-h (`Hotyn-K`), assembled by script; all sensors on Claude Opus 5;
- reference class: `Lytin-R 1.1`, two identical launches, RC46-1 and RC46-2, Claude Opus 5;
- rates: `Lytin-K 1.1`, one launch, gap-blind — it saw the bottom-up and the coverage report, never the class readings or any target; Claude Opus 5.

**Units.** The bottom-up is in **net hours of work on the task** — no leave, no holidays, no sickness, no presence overhead; the rate table's cells are so defined. The two class readings each declare their own unit inside their text; they differ from each other and from the bottom-up. Reconciling the three declarations is your first job, as your definition says, and the house conversion the orchestrator would otherwise apply is deliberately not stated here so that you reconcile from the declarations themselves. The rates from Step C are stated as multipliers and as net-hour additions on the bottom-up's own unit.

---

# INPUT 1 — the project description

The RFP's section 1 (introduction, business overview, project goals, project structure) verbatim below. Its section 2, the requirement list, is not repeated here: it was pinned as 153 obligations (interfaces 11, work 4, general 42, product/GIN 36, location/LN 29, data access 11, non-functional 20), of which 146 are product obligations and 7 are work obligations; the assumption log (INPUT 2) records every reading taken on it, and both class readings (INPUT 4) describe it in their own words.

```
1. INTRODUCTION 
This document is a Request for Proposal ("RFP") for the design and implementation of a Member 
Application Solution. The member application solution must meet the functionality, user and technical 
requirements. The contract term will cover the design, development, testing, and acceptance of the 
revised member application and architecture solution. 
X-Customer serves more than 200,000 businesses in 25 industries in the United States by facilitating 
industry initiatives, administrating the X-Customer system of standards, providing education and support, 
and connecting communities through events and online forums. 
 STATEMENT OF WORK BUSINESS OVERVIEW  
As part of its mission to "generate supply chain visibility, efficiency, safety, and collaboration" X-
Customer sets the standards for and enables its members to identify products and/or locations with 
numeric indicators that can be used to facilitate the supply chain process.  
For example, a X-Customer member can create a 12- or 14-digit number to identify a product and 
translate the number to a barcode format that can be used in retail transactions. The project scope 
includes the design and development of a B2B application solution used to create, manage, and share 
data related to these numeric indicators. The application solution will be used by businesses that range 
from one-person start-up companies to large corporations to facilitate their supply chain activities. 
 
Figure 1 shows the process for creating and sharing these numbers. 
 
The process starts with new membership; X-Customer licenses a 6-9 digit prefix, which is the baseline 
for a company to enumerate their products and/or locations. Onboarding members and managing prefix 
attributes are outside of the scope of this project. 
[Figure 1, legend: actions performed by Company / by X-Customer / by third party; RFP scope. Flow: Prospect (Company) comes to X-Customer to license a prefix → X-Customer issues a prefix to Company → X-Customer grants access to tools, standards and trainings, etc. → Company IDs for Products (identifies products, assigns Global Item Numbers, renders barcodes) · Company IDs for Locations (identifies locations, assigns Location Numbers, creates relationships between locations, shares location information for business transactions) · Access to X-Customer Data (search/view prefixes/attributes, search/view Global Item Numbers, search/view Location Numbers) → Company shares with Trading Partners; Company provides visibility to Business Partners; Solution Providers, Retailers access data to validate]

Once a company has licensed a prefix, they can create additional numeric identifiers for their products 
or locations and add identifying attributes to each. 
• Products are identified by 12- or 14-digit Global Item Numbers (GIN) that can be represented 
visually by a barcode. 
• Locations are identified by 13-digit Location Number (LN). Location Numbers are similar in 
format to Entity Global Item Numbers but have a different set of attributes. 
GIN and LNs are comprised of the prefix + a series of unique numbers. For example, 9-digit prefix can be 
used to create 100 unique 12-digit GIN by adding unique numbers for the last three digits. The same 
prefix can be used to create 1000 13-digit LNs by adding unique numbers for the last four digits. 
 
GIN example: [figure]
Barcode example: [figure]
 
 PROJECT GOALS 
Currently, X-Customer has several applications available to their members. To support the needs of their 
growing member base and increase the compliance of global standards, X-Customer intends to implement 
web-based application solution that is built on a scalable, sustainable architecture.  
 
This project will design and build an integrated solution with the following modules: 
• Create and manage GIN for Products 
• Create and manage LN for Locations 
• Access data related to Prefixes, GIN, and LN created and shared by others 
 
Each module in the integrated solution will use the same data and system architectures and run on the 
same development platform. Final front end design will define whether these modules will appear as a 
single application or as a suite of related applications. 
 
The project goals are: 
1. Design and implement a web-based application solution that extends application 
functionality and enhances the end user experience through intuitive navigation, work process 
flows, and new look and feel.  
2. Design and implement an application architecture that is able to support the application 
requirements and align with the existing enterprise architecture. The application architecture 
should be designed and implemented in a way that is maintainable by X-Customer resources 
and is scalable and sustainable given the projected member and application growth.  
3. Create efficiencies and cost reductions for future enhancements through a standard 
application framework and scalable application architecture. 

Future expansion may include creation, management, and sharing of data other than GIN or LN as well 
as increasing data sharing privileges to the field level. While these expansions are outside the scope of 
the project, the final design should be scalable to accommodate that.  
 
 PROJECT STRUCTURE 
To complete the project goals, the Member Application Solution project is divided into four primary 
components: 
1. Requirements and Design  
2. Development and Testing  
3. Implementation  
4. Post-production Support and Transition 
X-Customer prefers to select a vendor who will perform all four functions for both the web-based 
application solution and the application architecture. If, however, a respondent chooses to partner 
with a subcontractor(s) to complete any part of the project, all components, including pricing for each 
component, should be structured similarly and submitted as one response. 
```

# INPUT 2 — the assumption log (v1, approved 2026-09-08), run-history narration elided

## A0. The imperative

**A0, the imperative, applies**: an obligation the client stated cannot be
removed by an assumption. A log may bound what a number prices; every obligation ends as *priced
here*, *priced by another instrument*, or *not priceable without a named parameter*. An id that
appears nowhere is an exception, not a footnote.

## A1. What this estimate prices

Design, development, testing, data migration, deployment on the four-environment path, acceptance
and production cutover of the **first release** of the three modules, covering all product
obligations of `requirements_product.md`  and the demanded work of `requirements_work.md`
 to the extent A0 permits.

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

**From the case profile, pinned before any run:** a middle/senior mixed team of an outsourcing vendor, one team at one site, building its first system in this domain. The declaration assumes **one team at one site**
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

## A19. The era

The RFP is
dated **September 2018** (Internet Explorer 9 support, SOAP as an option, 3scale); the rate table is
compiled from modern norms and the era transfer is **not pre-adjusted**.

---

# INPUT 3 — the bottom-up estimate (run 1): the assembly of the sized work model, both repeats, script output verbatim

Conventions of the assembly: rooted subtrees; every element carries its crossed activities as items; each item is priced from the rate table cell (activity × element class × size class) as E = (O + 4M + P) / 6; C3 (coordination) is 20% of the leaf-item effort at every parent including the root; once-scoped and per-environment items sit outside every C3 base. Holes are items the sizing refused (unsizeable elements); they are named, never guessed, and priced at nothing. The corridor line is the O/M/P of every priced item summed at an equicorrelation of ρ = 0.5 — the declared convention, not a measurement.

Carried-not-priced beside the number, per A1: W-4 (the post-production support period and the transition service — no term, no service level) and NFR-5 (impact analysis on deviation, read at count 0).

```
=== repeat 1: sized elements 187 · distribution {'L': 23, 'M': 105, 'S': 52, 'unsizeable': 4, 'XL': 3} · statement kinds 23 · special counts 23
  element leaf E (incl. root per-parent items): 24163.5 h
  C3 all parents:                               13065.4 h   of which root C3: 4832.7
  once + per-environment layer [L]:            840.3 h
  GRAND TOTAL:                                  38069 net person-hours  (= 4758.7 pd at 8 h)
  corridor, rho = 0.5:  sd 6317 h · P10 29973 · P90 46165  (x0.79 / x1.21 of the centre)
  named holes (31):
      ('C-011', 'G2m', 'special count unsizeable')
      ('C-011', 'G3m', 'special count unsizeable')
      ('C-011', 'G4m', 'special count unsizeable')
      ('C-016', 'K3', 'unsizeable (M10)')
      ('A-065', 'K1', 'unsizeable (M10)')
      ('C-020', 'K1', 'unsizeable (M10)')
      ('A-065', 'K2', 'unsizeable (M10)')
      ('C-020', 'K2', 'unsizeable (M10)')
      ('A-065', 'A2', 'unsizeable (M10)')
      ('C-020', 'A2', 'unsizeable (M10)')
      ('A-065', 'A3', 'unsizeable (M10)')
      ('C-020', 'A3', 'unsizeable (M10)')
      ('A-065', 'A4', 'unsizeable (M10)')
      ('C-020', 'A4', 'unsizeable (M10)')
      ('C-001', 'G2m', 'special count unsizeable')
      ('A-043', 'G2m', 'special count unsizeable')
      ('A-159', 'G2m', 'special count unsizeable')
      ('C-001', 'G3m', 'special count unsizeable')
      ('A-043', 'G3m', 'special count unsizeable')
      ('A-159', 'G3m', 'special count unsizeable')
      ('C-001', 'G4m', 'special count unsizeable')
      ('A-043', 'G4m', 'special count unsizeable')
      ('A-159', 'G4m', 'special count unsizeable')
      ('A-013', 'K1', 'unsizeable (M10)')
      ('A-013', 'K2', 'unsizeable (M10)')
      ('A-013', 'A2', 'unsizeable (M10)')
      ('A-013', 'A3', 'unsizeable (M10)')
      ('A-013', 'A4', 'unsizeable (M10)')
      ('A-013', 'G2m', 'special count unsizeable')
      ('A-013', 'G3m', 'special count unsizeable')
      ('A-013', 'G4m', 'special count unsizeable')
=== repeat 2: sized elements 187 · distribution {'L': 25, 'M': 101, 'S': 55, 'unsizeable': 3, 'XL': 3} · statement kinds 23 · special counts 23
  element leaf E (incl. root per-parent items): 24220.9 h
  C3 all parents:                               13106.3 h   of which root C3: 4844.2
  once + per-environment layer [L]:            840.3 h
  GRAND TOTAL:                                  38168 net person-hours  (= 4770.9 pd at 8 h)
  corridor, rho = 0.5:  sd 6346 h · P10 30034 · P90 46301  (x0.79 / x1.21 of the centre)
  named holes (14):
      ('C-005', 'K1', 'unsizeable (M10)')
      ('C-005', 'K2', 'unsizeable (M10)')
      ('C-005', 'A2', 'unsizeable (M10)')
      ('C-005', 'A3', 'unsizeable (M10)')
      ('C-005', 'A4', 'unsizeable (M10)')
      ('C-011', 'G2m', 'special count unsizeable')
      ('C-011', 'G3m', 'special count unsizeable')
      ('C-011', 'G4m', 'special count unsizeable')
      ('C-016', 'K3', 'unsizeable (M10)')
      ('C-020', 'K1', 'unsizeable (M10)')
      ('C-020', 'K2', 'unsizeable (M10)')
      ('C-020', 'A2', 'unsizeable (M10)')
      ('C-020', 'A3', 'unsizeable (M10)')
      ('C-020', 'A4', 'unsizeable (M10)')
=== composition, repeat 1 - per top-level subtree: element items + C3 inside the subtree
   S-01     Platform and architecture foundation     elements  28  items   1857 h  C3    671 h  subtotal   2528 h
   S-02     Identity, users and roles                elements  16  items   1435 h  C3    527 h  subtotal   1961 h
   S-03     Shared record core                       elements  39  items   3957 h  C3   1456 h  subtotal   5413 h
   S-04     Workflow and validation                  elements  10  items   1141 h  C3    402 h  subtotal   1542 h
   S-05     Product (GIN) module                     elements  19  items   2202 h  C3    778 h  subtotal   2980 h
   S-06     Location (LN) module                     elements  11  items   1208 h  C3    403 h  subtotal   1611 h
   S-07     Publish and subscribe                    elements  18  items   1790 h  C3    633 h  subtotal   2423 h
   S-08     Access Data module                       elements  10  items    932 h  C3    258 h  subtotal   1190 h
   S-09     Import and export                        elements  20  items   2283 h  C3    809 h  subtotal   3092 h
   S-10     Notifications and communications         elements  15  items   1512 h  C3    543 h  subtotal   2055 h
   S-11     Reporting and audit                      elements  13  items   1308 h  C3    433 h  subtotal   1742 h
   S-12     User interface shell                     elements  17  items   1571 h  C3    485 h  subtotal   2055 h
   S-13     Operational design                       elements  19  items   1008 h  C3    340 h  subtotal   1348 h
   S-14     Configuration and reference data         elements  10  items   1348 h  C3    494 h  subtotal   1843 h
   root own per-parent items 612 h · root C3 4833 h · once/per-env 840 h
=== composition, repeat 1 - per activity (element-attached items only, hours)
   K2      3407
   A6      2892
   A3      2716
   A5      1913
   A7      1743
   K1      1508
   U3      1419
   A2      1404
   D4      1031
   U2      1031
   D2      1007
   A4       709
   G3m      560
   U1       525
   O1       525
   A8       471
   K3       465
   G2m      341
   G4m      288
   A10      192
   A9        17
=== once/per-environment items, repeat 1:
   A1 test strategy [bracket]                       E =  42.7
   U4 acceptance record [bracket]                   E =  17.3
   D1 mobilisation [bracket]                        E =  49.3
   D3 status reporting [bracket]                    E =  66.7
   D6 risk & dependency [bracket]                   E =  34.7
   E2 build/deploy pipeline [bracket]               E =  46.7
   E3 promotion procedure [4 envs: L]               E =  17.3
   E4 configuration management [bracket]            E =  22.0
   E6 production cutover [bracket]                  E =  44.0
   E7 hosting set-up [bracket]                      E =  46.7
   G1m source profiling [bracket]                   E =  52.0
   G5m migration rehearsal #1 [bracket]             E =  46.7
   G5m migration rehearsal #2 [bracket]             E =  46.7
   O2 operational runbook [bracket]                 E =  38.0
   O3 support handover pack [bracket]               E =  33.3
   O4 release notes [single]                        E =   4.3
   S1 security design review [bracket]              E =  42.7
   S2 penetration test [45 surf+int: XL]            E =  42.7
   S3 remediation [45 surf+int: XL]                 E =  72.0
   E1 environment: dev [S]                          E =   9.3
   E1 environment: test [M, declared]               E =  17.3
   E1 environment: stage [M]                        E =  17.3
   E1 environment: prod [L]                         E =  30.7
=== size-class agreement: 187 elements in both, 28 differ (85.0% agree)
      ('A-138', 'L', 'M') ('C-014', 'M', 'S') ('A-133', 'M', 'S') ('C-011', 'S', 'M') ('C-012', 'M', 'S') ('A-001', 'M', 'L') ('A-134', 'M', 'L') ('A-137', 'M', 'L') ('A-141', 'M', 'L') ('A-024', 'L', 'M') ('C-004', 'M', 'S') ('C-005', 'S', None) ('A-017', 'S', 'L') ('A-070', 'S', 'M') ('A-025', 'S', 'M') ('A-021', 'L', 'M') ('A-068', 'M', 'L') ('A-065', None, 'S') ('A-124', 'S', 'M') ('A-032', 'M', 'S') ('A-034', 'M', 'S') ('A-044', 'M', 'S') ('A-145', 'M', 'S') ('A-152', 'S', 'M') ('C-009', 'S', 'M') ('A-098', 'L', 'M') ('A-013', None, 'S') ('C-015', 'M', 'S')
=== statement-kind divergences: []
=== special-count divergences: [('A-043', None, 'S'), ('A-017', 'S', 'L'), ('A-159', None, 'S'), ('A-013', None, 'S'), ('C-015', 'M', 'S'), ('C-001', None, 'S'), ('A-098', 'L', 'M')]
=== XL elements (either repeat): ['A-036', 'A-049', 'A-062']
=== repeat spread: 38069 .. 38168 net person-hours (x1.0026); centre 38118 h
=== unit: net hours of work on the task (docs/instrument.md section 0). Leave, holidays, sickness and
===       presence are NOT included; the comparison-layer conversion is docs/constants.md section 4a.
```

---

# INPUT 4 — the reference class forecast (run 2), two readings, verbatim

## Reading RC46-1

**Engine: `Lytin-R 1.1`** — reference class forecasting (outside view), single sensor.

---

## 0. Contamination check (pre-flight)

- **Pasted input:** no work breakdown, no bottom-up estimate, no target, no budget, no deadline. The assumption log carries *scope readings and counts* (four symbologies, six formats, two rehearsal cycles, four environments) — these are class-placement facts, not effort anchors. **Clean; run proceeds.**
- **Ambient harness material:** the context carried a git status, a branch name, directory names and recent commit subjects, one of which contained a numeric result from another run. **Quarantined and not read as input.** It played no part in class definition, anchor selection, or any quantile. Per instruction this does not stop the run.
- I have read no files. The two INPUTs are the whole basis.

---

## 1. The declaration

**1. Unit.** One unit is **one person-month (PM) of a full-time assigned team member** = **21 recorded, assigned working days**. A day here is a *recorded, assigned working day*, not hours-on-task: it contains that day's stand-ups, reviews, coordination, context switching, waiting on the client, and rework. Conversion I use internally: **1 PM = 21 days = 168 recorded hours @ 8 h/day.** I do **not** claim 168 hours of touch-time; the effective touch-time inside a recorded day in this class is conventionally taken at 5–6 h, so a reader converting to touch-hours should multiply my figures by roughly **0.65–0.75**, and must say so if they do.

**2. Losses.** Annual leave, public holidays and sickness are **outside** my effort figures (they are not charged working days) but **inside** my calendar-duration figures. Conversion a reader needs: **1 FTE-year ≈ 10.5–11.0 charged PM** (≈ 220–230 charged days against 365 calendar). So a 20-FTE team running 18 calendar months yields ≈ 20 × 18 × 0.88 ≈ **317 charged PM**, not 360. Every PM number below is charged effort; every month number below is calendar.

**3. Roles.** **Every vendor role charged to the project**: business analysis, solution/data architecture, UX and visual design, development, QA/test automation, performance testing, DevOps/environment build, data-migration engineering, technical writing, project and delivery management, and the vendor's share of governance. Explicitly **outside**: client-side staff time (SMEs, X-Customer approvers, help-desk, their IdM and 3scale administrators), infrastructure and licence cost, hosting, third-party product cost, the vendor's pre-sale/bid effort, and any margin or rate — **I output effort, not price.**

**4. Sources' conventions, and where they disagree.**
- The **team × duration** anchor family is natively in *calendar months × headcount*, all roles, losses inside the calendar. Native to my unit; converted only by the 0.88 utilisation factor above.
- The **ISBSG / function-point** family is natively in *project work-effort hours*, and its default recording level is **Level 1 (development team only)** — it commonly **excludes** part of PM, and its handling of BA/UX varies by submitter. To use it I inflated its hours by **1.25–1.40** to reach all-roles, then divided by 168.
- The **COCOMO II** family is natively in *person-months of 152 hours*, all-roles, and explicitly **excludes** the requirements phase that this project's "Requirements and Design" component contains. I converted 152→168 h and added the front-end phase at the model's own published proportion.
- **Size of the inconsistency between families: about 30–40% at the point of contact**, driven almost entirely by role coverage (dev-team-only vs. all-roles), not by productivity disagreement. I have converted rather than absorbed; the residual disagreement after conversion is roughly **±15%**, which is small relative to the class spread and I have not tried to remove it.

**Scope boundary of my figures.**
Covered: the **first release** of the three modules through requirements, design, build, test, data migration, the four-environment deployment path, performance testing, acceptance, and production cutover, plus the handover pack and runbook — i.e. A1's *Included* list and A2's Definition of Done.
Excluded, honouring the log: **project component 4** (the post-production support period and transition service — unparameterised, priced by a rate-per-time instrument, not by me); **NFR-5 impact analysis** (counted 0 per the reading taken); member onboarding and prefix attribute administration; the payment process (D-8.1); training material development (G-11.1); the named future expansion.
**Categories I judge to sit at the edge** and that a reader should confirm are landed somewhere: (a) knowledge transfer sufficient to make the architecture "maintainable by X-Customer resources" — goal 2 asserts it, A2 does not name it beyond documentation; (b) the client-side effort to define "X-Customer Standards and business rules … as part of the project" — the RFP says they do not yet exist; (c) hardening and the failover *test* implied by NFR-8 as distinct from the failover *plan*; (d) any second migration rehearsal beyond the declared two. My distribution assumes (a)–(c) inside, (d) at the declared count.

---

## 2. The reference class

**Class definition.** *RFP-stage, pre-discovery estimates of a greenfield multi-module enterprise B2B web platform, built to fixed published requirements by a large outsourcing vendor for an enterprise client, replacing several incumbent applications, and delivered through first production release.*

**Membership criteria — structural, i.e. which categories of work such projects contain.** A project is in this class if it carries **all** of the following branches, and is in a different class if it is missing one of them or carries an extra one:

1. **Multi-module transactional application** with role-driven UI and an approval workflow — not a single-purpose tool, not a portal veneer.
2. **A cross-cutting sharing/permission mechanism** spanning the modules (publish/subscribe here) — this is the branch that distinguishes this class from ordinary CRUD platforms, because it makes every module's data model answerable to a second, orthogonal model.
3. **A bulk data interchange branch** — multi-format import/export with validation, plus a public/partner API under third-party API management.
4. **A reporting/analytics branch fed by a separate read store**, i.e. a second persistence tier with its own consistency story.
5. **A migration branch** from multiple live incumbent systems at production volume, with rehearsals.
6. **An external identity integration** on a standard not yet chosen by the client.
7. **A heavy NFR envelope treated as contractual**: stated response times at stated concurrency, 99.9% availability with a tested failover, four environments, WCAG, audit trail of all activity.
8. **A fixed, published, pre-discovery requirement set** authored by the client, with the vendor bidding against it competitively.

**Why this project is in it.** All eight branches are present and none is a stretch; branches 2, 4 and 5 in particular are stated obligations, not inferred. Size regime: enterprise, 200k+ member companies, 38k→256k users, tens of millions of records. Supplier regime: large outsourcing vendor, one mixed middle/senior team at one site, **first system in this domain** (A3) — the class's normal competence profile, not its best case. Client regime: large not-for-profit standards body, enterprise approval cadence (A18). Stage: **RFP, before discovery** — the single most important class attribute, because it fixes which systematic error applies.

**Which neighbouring classes it is *not* in.**
- Not **"mid-size B2B SaaS product built by a product team"** — that class lacks branches 5 and 7 and usually 3; it runs 3–5× cheaper and its estimates are made after discovery, not before.
- Not **"multi-year enterprise modernization *programme*"** — that class carries branches this one explicitly disowns: member onboarding, billing/payment, the resolver/future expansion, and an open-ended run service. The RFP fences those out and A1 honours the fence.
- Not **"COTS/package configuration"** — NFR-1 declines to constrain the platform and the requirement set is bespoke throughout; no product is being configured.
- Not **"data migration / integration project"** — migration is one branch of eight here, not the spine.

---

## 3. Base rates and anchors

### 3a. Absolute anchors — what such projects actually cost

All values are **charged, all-roles person-months for first production release**, converted into my unit per §1.4.

| # | Anchor | Value (PM) | Source | Confidence (shape / number) |
|---|---|---|---|---|
| A1 | Team × duration for a legacy-replacement enterprise platform delivered by a tier-1 outsourcing vendor, all four SDLC components, single site | 15–30 FTE over 14–24 calendar months → **250–600 PM** (centre ~370) | Practitioner consensus on vendor delivery patterns for this bid size | shape **high** / number **medium** |
| A2 | ISBSG Development & Enhancement repository, business applications in the large size band (>1,000 FP), median project delivery rate; inflated 1.25–1.40 to all-roles | **240–430 PM** (centre ~320) | ISBSG D&E repository, as reported in its release analyses | shape **medium-high** / number **medium**, and see blind spot 5 on dating |
| A3 | COCOMO II nominal, large business-application regime, requirements phase added back, 152→168 h converted | **260–500 PM** (centre ~360) | Boehm et al., *Software Cost Estimation with COCOMO II* | shape **medium** / number **low-medium** — its size input is itself an outside-view guess |
| A4 | Standards-body / member-data platforms of this description that reached production: successive releases over 2–4 years; first release is typically 40–60% of the programme | first release **300–550 PM** | Public record of comparable industry-body member platforms; inference, not measurement | shape **medium** / number **low** |
| A5 | Enterprise portal/platform replacements at 100k+ user scale carrying migration + SSO + published API | **250–700 PM** | Practitioner consensus | shape **medium** / number **low-medium** |
| A6 | Calendar duration for the class, first release, one team at one site | **12–28 months** (centre 17–18) | A1/A4 combined | shape **high** / number **medium** |

### 3b. Relative anchors — how such projects' actuals relate to their own early estimates

These do not enter my quantiles as multipliers on a number I do not have; they set the **shape and the skew** of the distribution and calibrate how far above the absolute centre the upper tail must reach.

| # | Anchor | Value | Source | Confidence (shape / number) |
|---|---|---|---|---|
| R1 | Cone of Uncertainty at "product definition / approved product requirements", which is where a pre-discovery RFP sits | actual ranges **0.5×–2.0×** the estimate made at this stage | McConnell, *Software Estimation*, after Boehm | shape **high** / number **medium-high** |
| R2 | IT project cost overrun distribution: mean ≈ **+27%**, fat right tail, **1 in 6** exceeding **+200%** | overrun is lognormal-ish, not normal | Flyvbjerg & Budzier, *HBR* 2011 (n≈1,471 IT projects) | shape **high** / number **medium** |
| R3 | Expert-judgement optimism bias in software effort | median effort overrun **+30–40%**; optimism is systematic, not random | Jørgensen & Moløkken, review of effort-estimation surveys | shape **high** / number **medium** |
| R4 | Winner's curse in competitive fixed-scope bidding: the winning bid is the most optimistic draw from the bidder population | winning bid systematically **below** the population median cost | Jørgensen, work on bidding and contracting | shape **high** / number **low** |
| R5 | Requirements creep during delivery | **1–2% per month** of schedule → **+20–40%** over an 18-month release | Jones, *Applied Software Measurement* | shape **medium-high** / number **medium** |
| R6 | Large projects (>$10M class) fail or overrun far more often than small ones | large-project on-target rate an order of magnitude below small | Standish CHAOS series | shape **medium** / number **low** — the dataset's definitions are contested |

---

## 4. Synthesis

**Do the independent absolute anchors agree?** Largely, yes — and this is the only cross-check available inside a single-sensor method. A1 (370), A2 (320), A3 (360) and A4 (300–550) all place the class centre in the **320–400 PM** band from three genuinely different derivations: empirical vendor staffing patterns, a measured repository, and a parametric model. A5 agrees but is much wider and carries little information. **The concordance is real but partially illusory**: A1 and A4 are both practitioner/inference anchors and are not fully independent of each other, and A3's size input is not independently observed. I treat the effective agreement as **two-and-a-half independent anchors**, not five.

**Where the anchors disagree:** on the *upper* end, not the centre. A2 (repository) tops out near 430 because repositories under-sample abandoned and catastrophic projects — survivorship. A5 and A4 reach 550–700. The relative anchors resolve this in favour of the wider families: R2's 1-in-6-over-200% and R1's 2.0× ceiling both say the class's right tail must extend well past any repository median, and R4 says that a project entering through a competitive RFP is *selected* for being on the optimistic side of its own class. I therefore let the absolute anchors set P50 and let the relative anchors set the distance from P50 to P80/P90.

**The class heterogeneity is high and I have not narrowed it.** The dominant within-class variance drivers are, in outside-view terms: whether the client's undefined business rules (the RFP states the standards "will be defined as part of the project") converge quickly or churn; whether the unchosen identity platform arrives early or late; whether the incumbent data proves migratable at stated volume; and whether the contract model absorbs or resists scope growth. None of these is observable at RFP stage, in any project of this class. A narrow answer here would be a false one.

---

## 5. Distribution

**Unit: charged, all-roles person-months, first production release. Calendar shown alongside; it is not independent of effort but it is not proportional to it either.**

| Quantile | Effort (PM) | ≈ recorded hours | Calendar (months) | Implied avg. team |
|---|---|---|---|---|
| **P10** | **180** | ~30,000 | 11–13 | ~17 FTE |
| **P50** | **380** | ~64,000 | 16–19 | ~24 FTE |
| **P80** | **640** | ~108,000 | 23–27 | ~29 FTE |
| **P90** | **850** | ~143,000 | 28–34 | ~32 FTE |

**Skew: strongly right.** P50 − P10 = 200; P90 − P50 = 470. The upper half is **2.35×** the lower half. P90/P10 ≈ 4.7. This is not a symmetrised range and must not be re-centred: the class's own overrun distribution (R2) is lognormal with a fat tail, and truncating it would be the single largest error available here.

**The scenario behind each quantile — these are *class* runs of events, not features of this project:**

- **P10 (180 PM).** The good-luck corner of the class. The client's undefined business rules turn out to already exist informally and are handed over in the first weeks; the identity platform is chosen before design closes; the incumbent data is cleaner than its age suggests; the vendor lands a genuinely reusable framework early and the three modules share it as intended; the NFR envelope is accepted as met on evidence rather than re-litigated; and — the largest single contributor at this quantile — the first release is quietly narrowed, with the thinner obligations deferred to a second release without a contract change. Roughly 1 project in 10 in this class runs this way.
- **P50 (380 PM).** The class's ordinary run. Discovery expands the requirement set by the usual fifth (R5); two or three of the eight branches cost meaningfully more than the bid assumed and one costs less; the identity and API-management integrations each lose a few weeks to a client-side dependency; migration takes its two rehearsals and then a third that nobody planned; performance work against the stated concurrency targets becomes a distinct late effort rather than a test pass; acceptance runs longer than the plan because the acceptance criteria are being written during acceptance. Nothing goes badly wrong. This is what "on plan, in this class" actually looks like.
- **P80 (640 PM).** One structural surprise plus the ordinary run. The class's characteristic P80 events: the cross-cutting permission model proves incompatible with the read-store design chosen for reporting and one of the two is rebuilt mid-project; **or** the incumbent data fails reconciliation at production volume and migration becomes a project inside the project; **or** the identity decision arrives late and wrong-shaped, forcing rework of the whole role model; **or** enterprise governance at a standards body imposes a review cadence the vendor's plan did not carry, and elapsed time inflates effort through carrying cost. Also at this quantile: the first-in-domain penalty (A3) is paid in full — the team learns the standards domain by getting it wrong once.
- **P90 (850 PM).** Two structural surprises, or one plus a relationship failure. The class's tail is not made of technical difficulty; it is made of **the requirement set moving while it is being built**, which here is licensed by the RFP's own statement that the standards and business rules will be defined during the project. Add a partial team turnover across a 30-month calendar, a re-baselining that resets acceptance, and a fixed-scope contract that converts every disagreement into a negotiation rather than a decision. R2's 1-in-6-over-200% cases live above this line; my P90 is deliberately *below* the class's true worst case, and there is real probability mass above 850 that no quantile here reports.

**Above P90:** the class contains outright non-delivery and restart. I do not quote it as a number; a reader should hold perhaps 3–5% probability that this class of project, at this stage, does not produce a first release under the original contract at all.

---

## 6. Assumption log of the method

### Part A — static blind-spot list (method metadata, reported verbatim; these are what an outside view cannot see **in any project**)

1. The specifics of this team.
2. The specifics of these integrations and dependencies.
3. The real difficulty of the particular features (no decomposition was done).
4. The quality and stability of this particular client or sponsor.
5. The dating of the base rates.
6. Management interventions that truncate the tail (de-scoping, changing the contract model, declaring victory early).
7. **Misclassification** — the risk that the class itself is wrong.

**On item 7, the required self-assessment.** My confidence is split:

| Class | Confidence | Direction it would move the answer |
|---|---|---|
| **Stated class** — RFP-stage, multi-module enterprise B2B platform, legacy replacement, outsourced, all eight branches | **60%** | — |
| Neighbour: **mid-size B2B product build, single team, branches 5 and 7 absent or nominal** | **15%** | **Down**, hard: P50 would fall to roughly 0.4–0.5× (150–200 PM) |
| Neighbour: **enterprise modernization programme** — if the "first release" boundary does not hold in practice and the release absorbs programme-level work | **20%** | **Up**: P50 would rise to roughly 1.5–2.0× (570–760 PM), and the P90 tail past 1,200 PM |
| Neighbour: **package/COTS-led delivery**, if a product exists in this niche that the vendor would configure rather than build | **5%** | **Down**, sharply, but with a different and worse tail (fit failure) |

The split is asymmetric upward, which is consistent with the skew I report and is a second reason not to symmetrise it.

### Part B — project-specific limits I noticed, kept separate from the list above

These are observations about *this input*, deliberately not mixed into the seven and deliberately **not** used to adjust any quantile:

- The assumption log resolves roughly a dozen genuine ambiguities by explicitly **choosing the narrower reading** (A4, A6, A9, A12, A13, A14, and the count-0 on NFR-5). Each refused reading is a real branch that a contract could still put back. My class-based P50 is drawn from projects whose scope was set by ordinary RFP ambiguity, i.e. *not* pre-narrowed. If every narrowing in the log holds through negotiation, the outside view is mildly conservative at the centre; if any two of them are reversed, the project moves toward the modernization-programme neighbour above.
- **Component 4 (post-production support) is carried, not priced.** My figures exclude it. Because the class's absolute anchors (A1, A4, A5) sometimes include a warranty or hypercare period inside the delivered team's tenure, there is a real risk of **double-counting or gapping** at this seam when my number is combined with a rate-per-time instrument. The orchestrator should perform that reconciliation visibly, once.
- The document is dated **September 2018** and it is now 2026. My base rates are not vintage-matched to 2018 and I have not attempted to age them. Direction is genuinely ambiguous: eight years of tooling and platform improvement pushes effort down; eight years of raised expectations on security, accessibility and cloud-native operability pushes it up. I did not adjust, and this is a real unquantified term, distinct from blind spot 5.
- I performed **no decomposition**. No requirement was counted, priced, weighted, or used to move a quantile. The requirement inventory was used **only** as evidence of class membership and size regime.

---

## Reading RC46-2

# Lytin-R 1.1 — reference-class forecast (outside view)

**Contamination check.** The pasted input contains no work breakdown, no bottom-up estimate, no target, no budget, no deadline. The assumption log is scope-bounding (readings and exclusions), not an estimate; A16's "2 rehearsal cycles" and A9's "four symbologies" are counts of *content*, not of effort, and I have used neither. Ambient repository material was present in my context — a git status, branch name and recent commit subjects, some carrying numerals. **I quarantined it: not read as input, not used as an anchor.** Run proceeds on the pasted input alone.

---

## 1. The declaration

**1. Unit.** One unit is a **staffed person-month (PM)** — one person assigned full time to this project for one calendar month. It is *recorded, assigned working time*, not hours-on-task: it contains that month's stand-ups, reviews, client calls, coordination, context switching and waiting. Numerically I fix **1 PM = 19 attended working days = 152 charged hours**. If a reader wants hours-of-work-on-the-task, apply a further 0.70–0.80 (≈ 105–120 task-hours per PM); that second conversion is not mine and I do not report in it.

**2. Losses.** Annual leave, public holidays and sickness are **inside** my figures. A staffed person-month is 21.7 nominal working days less ≈ 2.7 days of average absence (≈ 30 working days/year of leave + holidays + sick, Central/Eastern European outsourcing norm) = 19 attended days. **Conversion for a reader working in an absence-free convention:** divide my PM count by 0.875 to get "nominal working months", or equivalently expect ~14% more calendar time than an absence-free plan implies for the same headcount.

**3. Roles.** **Every role charged to the project**: project manager, business analysts, solution architect, UX design, developers, QA/test engineers, DevOps/release engineering, technical writing. Explicitly **outside**: all client-side effort (X-Customer product owners, SMEs, their infrastructure and identity teams, their acceptance testers); bid and pre-sales cost; third-party licences, hosting and infrastructure spend; and the post-production support period itself (A1, carried-not-priced).

**4. My sources' conventions, and where they disagree.** Three families, and they do **not** agree:
- *Benchmark-repository family* (ISBSG-type delivery rates): native unit is **recorded project effort hours at a stated resource level**, most records at level 1 = development team only. Absence is **outside** (nobody books leave to a project code), and PM/BA/DevOps are frequently **outside** too.
- *Parametric family* (COCOMO II): person-month is defined as **152 hours**, includes project management, and typically **excludes** a full requirements phase (added as a percentage).
- *Vendor-bid family* (practitioner consensus on how firms of this class actually staff and bill): **staffed FTE-months**, absence **inside**, all charged roles inside.

The gap between the repository family and the vendor-bid family is roughly **12% (absence) compounded with 10–20% (roles the repository omits) ≈ 22–35%** on the same physical project. I adopted the **vendor-bid convention** as my own and uplifted the repository-family anchor by ~25% to enter it. I am naming that adjustment rather than absorbing it; it is a real source of disagreement, not noise, and it is roughly the size of the difference between my P50 and my P10-to-P50 midpoint.

**Scope boundary of my figures.** They cover **first release** of the integrated three-module solution through design, build, test, data migration, the four-environment path, performance/HA/DR/security/accessibility work, acceptance and production cutover, plus the handover pack — i.e. A1's "included" list and A2's Definition of Done. I **honour** the project's stated exclusions: post-production support period and transition service (component 4), NFR-5 impact analysis (read as 0), member onboarding and prefix administration, the payment process (D-8.1), training-material development (G-11.1), and the future expansion.

**Categories I judge to sit at the edge of that boundary**, and which the class routinely mis-assigns:
- The *definition* of "X-Customer Standards and business rules", which the RFP says will be defined as part of the project. In this class that work lands on the vendor's analysts about as often as on the client. My figures assume it is shared; a client-side collapse here is a right-tail driver, not a scope addition.
- Failover hardware/software identification and DR procedure authoring (NFR-8, NFR-9): I include the engineering and documentation, exclude the procurement and the client's operational rehearsal.
- The identity solution itself (NFR-3, "has not been finalized"): integration inside, selection and IdM build outside.
- Brand / design-system work behind the "new look and feel": product UX inside, a separately-run brand engagement outside.

---

## 2. The reference class

**Class:** *RFP-stage, pre-discovery estimates for a greenfield multi-module custom B2B web application that replaces several incumbent applications for a large enterprise or enterprise-scale membership body, delivered by a single co-located team of a mid-to-large outsourcing vendor building its first system in that domain.*

**Membership criteria — structural, by which categories of work the class contains.** A project is in this class if it carries **all** of:
1. A client-driven, enumerated requirement set that must be *elaborated* (business rules explicitly deferred into the project), not discovered from scratch;
2. Multi-module transactional record management with role-based permissions and an approval workflow;
3. Bulk interchange — many-format import/export with validation — as a first-class obligation, not an afterthought;
4. A search-and-report surface over a separate read store, with a stated freshness expectation;
5. Migration of live data and users from several incumbent systems;
6. Integration with externally-owned platform services (identity, API management, messaging) that the vendor consumes rather than builds;
7. A named non-functional programme: quantified response times, high-availability/failover, DR, security, audit trail, accessibility;
8. A four-environment delivery path ending in production cutover and acceptance.

This project carries all eight. Stage is **RFP / pre-discovery**, which is a class-defining attribute in its own right: the systematic error at this stage is different in size *and in shape* from post-discovery error, and I did not pool the two.

**Neighbouring classes it is *not* in, and why:**
- *Package/ERP implementation programme* — no product configuration, no bespoke ERP or accounting connectors (A6 refuses them). Whole branches of integration work absent.
- *Enterprise data-platform / analytics programme* — the read store is a serving store for one application, not a warehouse with independent modelling, governance and BI-tool branches (A14 refuses a BI product).
- *Platform / API product build* — 3scale is consumed, not built (A5); no gateway, key management or resolver service (A9).
- *Regulated safety-critical build* — no certification branch, no formal-evidence regime. WCAG A and audit trail are ordinary enterprise obligations.
- *Multi-channel product programme* — web only, no native mobile branch.
- *Startup/MVP discovery build* — requirements exist and are the client's; the uncertainty here is elaboration uncertainty, not product-market uncertainty. Different error shape entirely.

---

## 3. Base rates and anchors

### Absolute anchors — what such projects actually cost

| # | Anchor | Value (in my unit) | Source | Confidence |
|---|---|---|---|---|
| A1 | Benchmark delivery-rate anchor: class size regime × delivery rate. Projects of this structural description sit in the ~1,200–3,000 functional-size-unit band; delivery rate median ~12 charged h/unit, inter-quartile ~7–22 | central ~24,000 charged h ≈ **158 PM** before convention uplift; band 55–430 PM. **After +25% convention/role uplift: central ≈ 195 PM** | ISBSG Development & Enhancement repository, new-development business/web application subsets (releases ~2013–2020), as reported in practitioner summaries | Shape: **high**. Number: **low-medium** — the size band is a class judgement, and repository delivery rates are notoriously heteroscedastic |
| A2 | Vendor-bid staffing shape: a three-module enterprise web solution with SSO, member API, legacy migration and a stated NFR programme is staffed by firms of this class at 12–20 FTE over 10–16 calendar months | **120–320 PM**, central **180–210 PM** | Practitioner consensus on RFP-stage staffing plans of mid-to-large outsourcing vendors, 2015–2022 | Shape: **high**. Number: **medium** |
| A3 | Schedule-compression floor: first release in this class is rarely achievable under ~9–10 calendar months at any staffing, because elaboration → build → migration rehearsal → performance/HA → acceptance is partly serial; typical 12–18 months; tail 24–30 | duration band **10–24+ months**; effort grows in the tail mainly through *duration at partial idle*, not headcount | Putnam/QSM software-equation tradition; Brooks-line practitioner consensus | Shape: **high** (one of the better-replicated findings). Number: **medium** |
| A4 | Enterprise/membership-body client cadence: committee-governed, multi-constituency clients (25 industry groups here) lengthen approval cycles without reducing team size | multiplies calendar by ~1.15–1.4 in the class; effort follows partially | Practitioner consensus; governance-effect literature adjacent to Flyvbjerg's IT work | Shape: **medium-high**. Number: **low** |

### Relative anchors — how such projects' actuals relate to their own early estimates

| # | Anchor | Value | Source | Confidence |
|---|---|---|---|---|
| R1 | Mean effort overrun across software estimation-accuracy surveys | **+30–40%**, most studies in +20–50%; overruns dominate underruns asymmetrically | Moløkken & Jørgensen, *A review of surveys on software effort estimation* (2003) and Jørgensen's subsequent reviews | Shape: **high**. Number: **medium** — my best-quality relative anchor |
| R2 | Early-phase estimation range at feasibility/RFP, before discovery | actual/estimate spans ≈ **0.5x–2.5x**, wider tail to 4x at true feasibility stage; narrows to ~0.7x–1.5x only after requirements are agreed | Boehm's cone of uncertainty, as corrected by Jørgensen (the cone is an envelope of *best achievable*, not of observed) | Shape: **high**. Number: **medium** |
| R3 | Fat right tail specific to IT: average overrun modest, but ~**1 in 6** large IT projects overruns cost by **~200%** | sets P90-to-P50 ratio near or above 2 | Flyvbjerg & Budzier, "Why Your IT Project May Be Riskier Than You Think", *HBR* 2011 | Shape: **high**. Number: **medium-high** |
| R4 | Competitive-bid optimism (winner's curse): RFP-stage bids in competitive procurement are systematically below delivered effort | delivered/bid ≈ **1.3–1.8x** on won fixed-scope bids once change requests are counted | Practitioner consensus, outsourcing sector | Shape: **high**. Number: **low-medium** |
| R5 | Large-custom-software cost overrun, historical headline | **1.4–1.9x** average | Standish CHAOS-family reporting | Shape: **medium**. Number: **low** — methodology is contested and the sample is self-selected |

Note on R1–R5: they do not calibrate *my* number, since I forecast the class actual directly rather than estimating and then inflating. They do two things: they tell me the **shape** (right-skewed, fat-tailed) and they warn me that if my P50 landed at the level of a typical winning bid, it would be wrong by construction.

---

## 4. Synthesis

Three absolute anchors converge more than I expected, which is the only cross-check available inside this method:

- A1, once lifted into my unit convention, gives a central ≈ **195 PM**.
- A2 gives a central of **180–210 PM**.
- A3 crossed with A2's staffing gives 12–18 months × 13–17 FTE = **160–270 PM**, centre ≈ 210.

These are not fully independent — A1's size band and A2's staffing plans are both informed by the same practitioner population — but they are methodologically distinct (functional-size benchmark vs. staffing shape vs. schedule physics), and their agreement inside ±15% is meaningful. **I therefore place P50 at ~215 PM**, marginally above the anchors' centre because A4 (committee-governed multi-constituency client) pushes the class centre up and nothing in the outside view pushes it down.

The relative anchors then set the spread, not the centre. R3 fixes P90/P50 at ≈ 2. R2 fixes the pre-discovery width and forbids a narrow interval. R1 and R4 confirm the right skew and confirm that a P50 near 215 sits *above* where a competitive bid for this class would sit — which is what an outside view should do.

The left side is not the mirror of the right. The class has an irreducible floor: even the luckiest run of this structure carries eight categories of work and a serial path through four environments. So I compress P10 above a pure lognormal.

---

## 5. Distribution

All figures are **staffed person-months** as declared (1 PM = 19 attended days = 152 charged hours, absence inside, all charged roles inside), for the first release only.

| Quantile | Effort (PM) | Charged hours | Indicative calendar | Indicative avg team |
|---|---|---|---|---|
| **P10** | **125** | ~19,000 | 10–11 months | ~12 FTE |
| **P50** | **215** | ~32,700 | 13–15 months | ~15 FTE |
| **P80** | **330** | ~50,200 | 18–20 months | ~17 FTE |
| **P90** | **440** | ~66,900 | 23–26 months | ~18 FTE |

**Skew is right and deliberate**: P50/P10 = 1.72, P90/P50 = 2.05. I have not symmetrised it. Note that the tail grows through *duration* faster than through *headcount* — that is anchor A3 speaking, and it is the class's characteristic failure mode.

**Class scenarios behind each quantile:**

- **P10 — the clean run.** Client fields decisive, empowered product owners; the deferred business rules arrive early and stay stable; the identity platform is chosen before build starts and speaks one mainstream protocol; the legacy data proves cleaner than feared and two migration rehearsals suffice; the non-functional programme is satisfied by platform and framework choices rather than bespoke engineering; the first release is agreed as a genuine first release. Roughly the best decile of the class, and it still is not cheap.

- **P50 — the ordinary run.** Elaboration of the business rules takes longer than planned and overlaps build; the identity choice arrives mid-project and one integration is reworked; migration reveals two or three legacy data conditions nobody documented; performance targets are missed on the first load run and cost a rework cycle in search and reporting; a slice of the requirement set is negotiated into a second release. Acceptance takes two rounds. This is the modal history of the class.

- **P80 — the elaboration-drag run.** The deferred standards and business rules become a running negotiation across multiple industry constituencies rather than a phase; the read store's freshness expectation is pinned late and forces a design change; the incumbent applications turn out to disagree with each other about the same entities, and migration becomes a reconciliation programme with the client; the four-environment path is blocked by client-side infrastructure availability. The team stays staffed through the waiting. This is the ~1-in-5 outcome, and it is not exotic.

- **P90 — the fat-tail run.** Two or more of: sponsor turnover or a governance re-set at the client; the architecture proves not to meet the growth-projected load and is partly re-cut after the first performance campaign; the identity platform is changed after integration; migration cannot be reconciled and a parallel-run period is imposed. This is Flyvbjerg's 1-in-6, and it is the reason the interval is not narrower. Beyond P90 the class contains genuine catastrophes; I do not quote a P95 because the outside view cannot bound it.

**On the width:** this class is heterogeneous, and a narrow range would be a false report. The P10–P90 span is a factor of 3.5. At pre-discovery, that is honest; anything materially tighter would be an inside-view number wearing an outside-view label.

---

## 6. Assumption log of the method

### Part A — the static blind-spot list (method metadata, reported verbatim; these are what an outside view cannot see in *any* project, not findings of this run)

1. The specifics of this team.
2. The specifics of these integrations and dependencies.
3. The real difficulty of the particular features (no decomposition was done).
4. The quality and stability of this particular client or sponsor.
5. The dating of the base rates.
6. Management interventions that truncate the tail (de-scoping, changing the contract model, declaring victory early).
7. **Misclassification** — the risk that the class itself is wrong.

**On item 7, my confidence split across the stated class and its nearest neighbours:**

| Class | Confidence | Direction if this is the true class |
|---|---|---|
| **Stated class** — multi-module custom B2B web replacement, outsourced, RFP stage | **60%** | — |
| *Data-intensive replacement programme* — if the read store, the freshness requirement, the growth projections and the multi-source migration dominate rather than accompany the build | 15% | **Up**, ×1.3–1.6 on every quantile |
| *Conventional enterprise CRUD suite with heavy NFR paperwork* — if the non-functional requirements are largely satisfied by platform selection and the modules are more uniform than the requirement list suggests | 20% | **Down**, ×0.6–0.75 |
| *Multi-year phased enterprise programme* — if no first-release cut is accepted and the full requirement set plus the support component must land at once | 5% | **Up**, ×2 or more; my P90 would become a P50 |

### Part B — project-specific observations this method noticed but did not price

These are separate from the seven above and are offered to the diagnostician, not folded into any quantile:

- **Era effect (A19).** The RFP is dated September 2018 and my base rates are drawn largely from 2013–2022 delivery. A 2018-vintage build carries obligations a 2026 build would not (IE9 in the browser matrix, SOAP as a live option). If the work is actually executed with 2026 tooling against a 2018 requirement set, the two eras pull in opposite directions and I cannot say which wins. This is the concrete face of blind-spot 5.
- **The estimate/actual dating asymmetry.** My relative anchors (R1–R5) predate or straddle the current delivery-tooling generation. If class productivity has genuinely moved since they were gathered, my absolute anchors are stale in the *same* direction as my relative ones, so the ratios survive better than the levels.
- **The carried-not-priced item is a live boundary risk.** Component 4 (post-production support term and service level) sits outside my figures by A1's own decision. In this class, a support obligation whose term is unstated at RFP is a frequent route by which the delivery team is retained past cutover — which is an *effort* event even though it is a *scope* exclusion. My quantiles do not contain it; a reader must not assume they do.

---

# INPUT 5 — the calibration rates from Step C, gap-blind, verbatim

# Step C calibration parameters

**Engine: `Lytin-K 1.1`**
**Calibrating: `Hotyn-M 1.1` / `Hotyn-W 1.1` / `Hotyn-D 2.0` × rate table `v0.1-h`**

Pairing note for downstream: the structure engines are at 1.1 while the sizing engine is at 2.0. My rates are stated against a structure of the `Hotyn-*1.1` shape and a net-task-hour rate convention. If either the structure engines or the rate table are re-versioned, this parameter set does not transfer without re-derivation.

---

## 1. Input inventory

Received:

1. Project description — X-Customer Member Application Solution RFP, September 2018, three modules plus cross-cutting obligations.
2. Assumption log v1 (approved): A1, A2, A4–A12, A16, A17, A19, and the A0 carried-unpriced list.
3. Bottom-up estimate: engine chain, two independent repeats, layer table (element-attached / integration / once-scoped), composition by top-level subsystem, composition by activity, element-class and size-class counts.
4. Coverage report: carried categories, named holes (31 items repeat 1 / 14 items repeat 2), the performance-test closure violation, carried-unpriced A0 obligations, ~30 sizing-sensor closure violations, and the structural facts bearing on blind spots.

**Explicit confirmation:** I was given **no reference-class forecast, no quantiles, no target total, no budget, no deadline, no outcome, and no statement of any gap.** Nothing in this message asks me to make corrections sum to anything. No contamination to report.

**Quarantined, not used:** the harness prepended ambient repository information (a git status line, a branch name, recent commit subjects, an untracked directory name, and a memory index). I did not read it as input and did not act on it. It contains no forecast or target that would trigger a contamination stop; it is simply not my input. No repository files were read.

**Anomaly noted, not a stop:** the totals of the two repeats (38 069 / 38 168) are present. These are the estimate's own output, which I am supposed to see — they are not a target and not a class number, and I have used them only to identify which layer each multiplier attaches to.

---

## 2. Double-counting check

Base: the coverage report, item by item, against the standard blind spots of bottom-up estimation.

| Blind spot | What the estimate already carries | What stays open (mine) |
|---|---|---|
| Decomposition incompleteness — missed low-level items | 1 650 work items over 245 elements; requirement elaboration per covering element | The **named holes** (31 items r1 / 14 r2) and the genuinely-missing share of the **~30 flagged closure violations** → T1, T2 |
| Requirements volatility after baseline | *Elaboration* of what is already known (1 031 h) | *Change and rework* once I-7 business rules and the NFR-3 protocol land → G1. Elaboration ≠ change; the split is clean |
| Integration and interface effort | 20% of subtree leaf effort at 59 parents incl. root (13 065 h); contract tests on 10 interfaces | **Nothing.** No integration uplift from me |
| Functional test and defect rework | Test design, implementation, review; 2 execution cycles + 2 defect-resolution cycles at every parent; regression suites; test data; 2 UAT support + 2 triage cycles; defect resolution 2 892 h | **Nothing on functional rework.** Only non-functional *execution* → A-1…A-4 |
| Non-functional verification | *Realisation and evidence* for 24 design statements; performance test on 1 statement (availability) | *Independent verification*: load test vs the five NFR-14 targets, failover exercise, backup/DR rehearsal, WCAG evaluation, browser matrix → A-1…A-4. Realisation carried / verification open — clean split |
| Project management and overhead | Planning per parent (1 007 h); mobilisation, status reporting, risk management, configuration management | **Nothing as a separate line.** Client-side approval friction only, folded into G2 |
| Environments, pipeline, deployment | Four environments, pipeline, promotion procedure, cutover, hosting set-up, runbook, release notes | **Nothing** |
| Migration | Source profiling, field mapping, ETL, load/reconciliation across 22 stores; two rehearsals | Four stores of undeclared predecessor origin (already inside T1's hole list) and the binary-content inventory (inside T2). Not charged twice |
| Security | Security review, external penetration test, remediation | **Nothing** |
| Documentation and handover | User documentation at every surface-bearing parent, runbook, handover pack, release notes, help *editor* | Initial in-application help **content** (A2 requires it in place; editor ≠ content) → A-5 |
| Precedentedness / team learning | Nothing — rate table v0.1-h is external norms at implied nominal experience | First-in-domain team, dense obligation set, committee-governed client → G2 |
| Size-class coarseness | Sizing at class level, two repeats, 85% agreement | Three XL leaves are coarse aggregates → T3 |
| Post-production support, NFR-5 analysis | Nothing — carried unpriced by A0 decision | **Left uncorrected** (parameterless; see §4) |
| Tail / failure events | Nothing | **Left uncorrected** — another sensor's tail (see §4) |

**Partition result: satisfied.** Every category above sits in exactly one column, or is split on an explicitly named seam. Three categories required a seam, and each seam is stated rather than assumed:

- requirements work — *elaboration* carried, *post-baseline change* mine;
- non-functional work — *realisation and evidence* carried, *independent verification execution* mine;
- migration — 22 declared stores carried, 4 undeclared-origin stores mine (once, inside T1).

One soft edge I will not pretend is sharp: accessibility and performance **fixes** arising from my added verification passes fall into the estimate's defect-resolution line, which is sized per parent and not per defect source. I am charging only for verification and re-verification, not for the fixes. If the applying step wants the fix work explicit, that is a scope question for Step B, not a rate for me.

### How the coverage report moved my rates

Decisively downward, and this is the single largest effect in this run. This estimate is thorough. It carries, with priced items, seven of the categories a generic "bottom-up forgets things" correction normally charges for: integration at every parent including the root, two full test-execution and defect cycles, two UAT cycles, four environments with pipeline and promotion, migration with two rehearsals, security review with external penetration test *and* remediation, and per-parent planning with once-scoped mobilisation, status reporting and risk management.

Concretely, the report suppressed corrections I would otherwise have proposed by default:

- **no integration uplift** (would normally be ×1.05–1.15 on a structure that priced integration only at the root) — the 20% non-compounding constant is applied at 59 parents, so the category is paid;
- **no test/rework multiplier** (would normally be ×1.15–1.35 where a single test pass is priced) — two execution cycles plus two defect cycles plus regression are carried, and defect resolution is 2 892 h, 12% of the element-attached layer, which is inside published rework norms;
- **no PM/overhead uplift** (would normally be +8–15%) — planning is per parent and the once-scoped management items exist;
- **no security uplift, no environment uplift, no documentation uplift**;
- **T2 placed at the low-middle of its external range, not the top** — because the closure violations were *enumerated by the estimate's own sensors and declared*, which is evidence of a thorough sweep, and because the report states in its own words that "some may be covered in another subtree."

What the report moved **upward**: nothing generic. It created exactly five pure additions, all of them non-functional verification and content items that the report itself names as absent, plus the two targeted multipliers whose *existence* the report established by enumerating the holes. I would not have known to charge for the load test at all without it; equally, I would have charged twice for testing without it.

Net: the report converted this from a "sparse estimate" profile — which would carry two globals in the 1.25–1.40 region plus an omissions charge — into a "thorough estimate" profile with modest globals and named, bounded, itemised residuals.

---

## 3. Corrections

### Declaration (applies to the pure additions A-1…A-5 only)

1. **Unit of my additions:** **net person-hours of work on the task.** Not days. No day-to-hour conversion is embedded.
2. **Losses:** **outside** the amounts. Leave, public holidays, sickness, presence overhead and within-day overhead are *not* included in any figure I state.
3. **Roles:** stated per addition in the table.
4. **Unit relative to the estimate:** **identical.** Rate table v0.1-h is stated in net person-hours of work on the task with losses outside every row. **No conversion is required, and I supply none.** The consumer may add my amounts to the estimate's layers directly. If the consuming step later converts to calendar days or billable days, it must convert my additions and the estimate together, by the same factor.
5. **Sources' conventions and the size of their disagreement:** my external anchors for the additions come from two convention families. Consultancy and vendor scoping figures are quoted in **8-hour billable days that include within-day overhead** but exclude leave. Engineering-norm sources (COCOMO II, ISBSG-style effort reporting) are in **effort hours excluding leave** but with varying treatment of within-day overhead. The disagreement between "billable day" and "net task hour" is conventionally **10–20%**. I deflated all vendor-day-derived central figures by **15%** to land in net task hours. The low/high spread of each addition therefore carries this convention disagreement *in addition to* substantive scope uncertainty — which is one reason the ranges are wide. Two of my sources (NIST SP 800-34 Rev.1, W3C WCAG-EM) publish **scope and procedure but no effort figures at all**; for those I derived hours from the described exercise scope and marked confidence down accordingly. This is stated so the downstream reader does not mistake a derived figure for a published one.

**Which corrections the declaration governs:** A-1 through A-5 are **amounts** and carry the unit. G1, G2, T1, T2, T3 are **dimensionless factors** and need none of it.

### Corrections table

| # | Name | Blind spot addressed | Form | Low / Central / High | External source | Confidence |
|---|---|---|---|---|---|---|
| **G1** | Undiscovered scope growth | Requirements volatility after baseline; rules and protocol not yet chosen | **Global multiplier** | **×1.10 / ×1.18 / ×1.30** | Capers Jones, *Estimating Software Costs* / *Applied Software Measurement*: requirements creep ~1–2% per calendar month after requirements sign-off for large projects, 10–35% total on projects of this class; Boehm's cone of uncertainty at pre-discovery / competitive-bid stage | Medium-high on the range, medium on the placement |
| **G2** | Precedentedness, coordination and estimator optimism (**merged**) | First-in-domain team; committee-governed enterprise client; generic optimism | **Global multiplier** | **×1.08 / ×1.15 / ×1.25** | COCOMO II (Boehm et al., 2000): APEX applications-experience effort multiplier, Low = 1.10, Very Low = 1.22; PREC precedentedness scale factor, Nominal→Low adds ≈0.0124 to the effort exponent (≈5–10% at this size); TEAM/SITE cohesion factors for a single-site single team are favourable and pull the low end down | Medium |
| **T1** | Declared holes, completion | Enumerated unpriced items in the existing structure | **Targeted multiplier** on the **element-attached layer** | **repeat 1: +1.5% / +2.5% / +4.0%**; **repeat 2: +0.7% / +1.2% / +2.0%** | Count is external to me (coverage report: 31 items r1, 14 r2, of 1 650). Range anchored on completion-by-class-mean substitution, standard practice for declared-hole closure; upper end reflects that several hole-bearing items (A-013 reference data store, A-065 group management) are aggregates likely above item mean | **High** — the count is enumerated, only per-item size is inferred |
| **T2** | Closure violations, real share | Missing *elements*, not merely missing items | **Targeted multiplier** on the **element-attached layer** | **+5% / +9% / +15%** | Jones: requirements completeness at RFP/pre-discovery typically 75–90%; Moløkken & Jørgensen (2003) review of estimation-error studies — omitted work is the dominant contributor to bottom-up underestimation, commonly 10–20% of eventual effort. Placement inside that range set by the report's own statement that some of the ~30 flagged items are covered elsewhere ("several are not"), implying roughly 40–60% real | Medium |
| **T3** | XL coarseness | Under-decomposed leaves are systematically underestimated | **Targeted multiplier** on the **three XL leaves only** (notification engine, record import service, basic/full attribute profiles) | **×1.15 / ×1.30 / ×1.50** | Jørgensen (2004), on decomposition and estimation accuracy: coarse work items show systematic downward bias relative to decomposed equivalents; standard three-point/PERT practice for un-decomposed aggregates | Medium-low. Note: 3 leaves of 187 — the total effect is small whatever the applying step chooses |
| **A-1** | Load and performance test vs NFR-14 | Non-functional verification, named hole | **Pure addition** | **180 / 320 / 560 net person-hours** | Industry performance-engineering engagement norms for a multi-module B2B application at production-like volume (500k prefixes / 10M GIN / 550k LN, five response-time targets at stated concurrency): scenario design, script build for key journeys, data seeding, two execution rounds, analysis, one retest after tuning. Vendor-day figures deflated 15% | Medium |
| **A-2** | Failover test execution + backup/DR rehearsal | Non-functional verification, named hole | **Pure addition** | **90 / 160 / 280 net person-hours** | NIST SP 800-34 Rev.1, contingency-plan testing and exercise guidance (functional exercise scope; **publishes procedure, not effort** — hours derived from described scope). Two exercises against the 99.9%-with-tested-failover obligation | Medium-low |
| **A-3** | WCAG 2.0 A conformance evaluation + re-verification | Non-functional verification; realisation carried, verification not | **Pure addition** | **120 / 200 / 340 net person-hours** | W3C WCAG-EM sampled-evaluation methodology (**publishes method, not effort**); vendor accessibility-audit scoping conventions of 40–120 h per sampled evaluation, scaled for three modules + admin + public anonymous tier, plus one re-verification pass. **Excludes remediation coding** — that sits in the estimate's defect-resolution line | Medium-low |
| **A-4** | Cross-browser verification matrix | Non-functional verification, named hole | **Pure addition** | **70 / 130 / 220 net person-hours** | Standard compatibility-matrix test practice: one full pass plus one regression pass across the surface set for IE9+ and current browsers. Vendor-day derived, deflated 15% | Medium |
| **A-5** | Initial in-application help content | Documentation residual — editor priced, content absent; A2 requires it in place | **Pure addition** | **90 / 160 / 280 net person-hours** | Technical-writing productivity norms (topic-based authoring, ~2–4 net hours per help topic including SME review) applied to three modules plus administration. **Scoped to in-app help only** — training materials are excluded by the RFP | Medium |

**Global-multiplier count: 2.** Compounded, G1×G2 spans **×1.19 (low·low) to ×1.63 (high·high)**, central **×1.36**. I state this only so the applying step sees the compounding it is committing to; it is a factor range, not a total. Generic optimism bias was **merged into G2**, not added as a third global, per the merge rule — it overlaps both precedentedness and creep, and charging it separately is exactly the failure mode the two-global cap exists to prevent. This is also why G1's central sits mid-range rather than at the top of the published creep band.

**Roles covered by the additions:** A-1 performance engineer, plus developer and infrastructure support. A-2 infrastructure/operations engineer, developer, test lead. A-3 accessibility-competent tester, plus front-end developer for verification only. A-4 tester. A-5 technical writer plus SME review time.

---

## 4. Deliberately uncorrected

1. **Post-production support period and transition service (A0).** Term and service level are unstated. A rate requires a base; there is none. This is a scope resolution for Step B, not a calibration parameter. I emit nothing for it — and specifically, I did **not** smuggle it into G1.
2. **NFR-5 impact analysis (A0, count 0).** Read as no deviation. If that reading changes, this returns as an addition, not as a multiplier.
3. **Tail and failure events.** The identity protocol being chosen late or changed mid-flight; the client failing to define I-7 business rules at all; committee stalemate on approval; predecessor migration data proving structurally unusable; loss of the competitive bid. None of these is a multiplier on anything — they are discrete branches with their own probabilities. **Another sensor's tail.** G1 covers ordinary creep, not scenario failure, and the two must not be conflated.
4. **The 15% class disagreement between repeats.** That is dispersion, not bias. It belongs to whatever step propagates spread, not to a central-value correction. I made no attempt to convert it into a rate.
5. **Era adjustment (A19).** The RFP is 2018, the norms are modern. I can defend no direction — tooling productivity has risen, but so have browser-matrix, accessibility and security expectations. No sourced index, so no correction. Flagged, not priced.
6. **The 20% non-compounding integration constant itself.** I do not second-guess the method's own constant. Adjusting it would be a third global effect by another name.
7. **The rate table's own uncalibrated status (v0.1-h, "uncalibrated against any outcome").** Whether the per-item rates are right is a question about the rate table, not about this estimate's structure. Correcting it here would require a global multiplier I cannot source, and I have spent both globals on effects I can.
8. **Losses, calendar and duration.** My unit is net task hours throughout. Any conversion to elapsed time or billable capacity is downstream and not mine.

---

## 5. Order of application

Apply in exactly this sequence. The applying step has no freedom to reorder.

1. **T1** — apply to the **element-attached layer** of the repeat in use (24 163 r1 / 24 221 r2), using the repeat-specific rate. Repeat 1 and repeat 2 take **different** T1 rates; do not average them before applying.
2. **T2** — apply to the **element-attached layer**, same base as step 1. T1 and T2 are both computed against the *original* element-attached figure, not against each other's output — they are disjoint item sets and must not compound.
3. **T3** — apply to the element-attached effort of the **three XL leaves only**. If that subset's effort is not separable, the applying step must say so and skip T3 rather than approximate it against the whole layer.
4. **Integration on the increments.** Apply the method's **own** 20% non-compounding constant to the sum of the T1+T2+T3 increments. Added items sit under parents like every other item and must carry integration exactly as the structure carries it. Do not apply my own factor here — use the structure's constant, unchanged.
5. **Structural subtotal** = estimate total + (T1+T2+T3 increments) + their integration from step 4. *I do not compute this and express no opinion on it.*
6. **Additions A-1…A-5** — add flat. These are once-scoped and environment-level items of the same family as the estimate's 840-hour once-scoped layer, which takes no integration. **They do not take the 20% constant.** (Sanity note for the applying step, not a target: my central additions sum to roughly the same magnitude as that existing once-scoped layer, which is the scale one should expect for five once-scoped verification and content items.)
7. **G2** — apply to the result of step 6. Precedentedness and coordination friction act on all work the team performs, including the added verification passes.
8. **G1** — apply last, to the G2-adjusted figure. Scope growth is growth in the body of work as it will actually be executed, i.e. at the team's real productivity, so it sits outside G2. The product is order-independent, but the order is fixed anyway to remove discretion.

Steps 7 and 8 are the only compounding in this parameter set. Everything else is additive by construction.

---

# Precomputed bases for the rate agent's targeted steps (you have no access to the leaf tables and may not derive quantities of your own)

- element-attached layer (T1, T2 base): repeat 1 **24 163 h**, repeat 2 **24 221 h**;
- the three XL leaves' own element-attached effort (T3 base), identical in both repeats: A-036 197.7 h, A-049 206.3 h, A-062 189.0 h — **593.0 h**;
- C3 (the structure's 20% constant) on the increments: 20% of the T1+T2+T3 increment, per step 4 of the order;
- once-scoped layer, both repeats: 840 h; C3 layer: 13 065 h (r1), 13 106 h (r2); totals 38 069 h (r1), 38 168 h (r2).

# What is asked of you

Your definition's output format, sections 1–7, with the declaration reconciliation before Step B. Keep the two repeats as a band and the two class readings as a band; never average either. Apply the rates exactly in the fixed order, low / central / high, showing running totals so the chain can be recomputed by hand. The tail of the final answer comes from the class readings' quantiles as they stand — both readings, in one unit, stated separately. Address the sensor-flagged cross-cutting issues rather than absorbing them: the unit disagreement between the two class readings, both readings' warning about the seam with the carried post-production period, the era mismatch both refused to adjust for, and the rate agent's tail hand-off list. Close with the one or two facts that would most move the answer.