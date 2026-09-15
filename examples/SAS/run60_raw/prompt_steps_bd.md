You are performing Steps B and D for the project described below. Everything you need is in this message; read no files.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, a branch name, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your input inventory that it was present and that you quarantined it, and proceed on the pasted input alone.

**On the actual outcome: there is none.** This RFP was never awarded to the estimating side and no delivery record exists; the case has no outcome to open now or later. Nothing below is an actual. Your report is a diagnosis between instruments, not a validation of either.

**Engine chain of your inputs, from the launch records (the sensors' own stamps are inside their texts):**
- bottom-up: product model `Hotyn-M 2.1` (n = 2, first reading carried; in this generation coverage lives in leaves only and distinct leaves realising the same obligations are kept apart) → work model `Hotyn-W 1.2` (seven batches) → size classes `Hotyn-D 2.0` (n = 2, both repeats priced; the repeats declared opposite rules for obligations shared by several leaves and differ ×1.09 on the total) × rate table v0.1-h (`Hotyn-K`), assembled by script; all sensors on Claude Opus 5;
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

Conventions of the assembly: rooted subtrees; every element carries its crossed activities as items; each item is priced from the rate table cell (activity × element class × size class) as E = (O + 4M + P) / 6; C3 (coordination) is 20% of the leaf-item effort at every parent including the root; once-scoped and per-environment items sit outside every C3 base. Holes are items the sizing refused (unsizeable elements, or migration counts for which no entity kind was shown to need loading from a predecessor); they are named, never guessed, and priced at nothing. The corridor line is the O/M/P of every priced item summed at an equicorrelation of ρ = 0.5 — the declared convention, not a measurement. The model's ids: N = node, A = accreted leaf (placed at a requirement), C = derived leaf (added at completion, no requirement of its own), CN = derived node.

Carried-not-priced beside the number, per A1: W-4 (the post-production support period and the transition service — no term, no service level; the crossing entered it as a demanded branch `DW-4` without an activity) and NFR-5 (impact analysis on deviation, read at count 0).

The two repeats of the sizing step declared opposite rules for one question the sizing rules do not settle — whether an obligation shared by several leaves is counted in full on each leaf (repeat 1) or only for the part each leaf's name claims (repeat 2) — and this, not random disagreement, is why repeat 1 sits a class higher across the board (13 XL against 3). Both are legal readings; keep them as a band.

```
=== repeat 1: sized elements 187 · distribution {'L': 44, 'M': 94, 'S': 35, 'unsizeable': 1, 'XL': 13} · statement kinds 20 · special counts 25
  element leaf E (incl. root per-parent items): 23331.6 h
  C3 all parents:                               10761.2 h   of which root C3: 4666.3
  once + per-environment layer [L]:            840.3 h
  GRAND TOTAL:                                  34933 net person-hours  (= 4366.6 pd at 8 h)
  corridor, rho = 0.5:  sd 5473 h · P10 27919 · P90 41947  (x0.80 / x1.20 of the centre)
  named holes (42):
      ('A140', 'K1', 'unsizeable (M10)')
      ('A140', 'K2', 'unsizeable (M10)')
      ('A140', 'A2', 'unsizeable (M10)')
      ('A140', 'A3', 'unsizeable (M10)')
      ('A140', 'A4', 'unsizeable (M10)')
      ('A140', 'A10', 'unsizeable (M10)')
      ('A089', 'G2m', 'special count unsizeable')
      ('A089', 'G3m', 'special count unsizeable')
      ('A089', 'G4m', 'special count unsizeable')
      ('A009', 'G2m', 'special count unsizeable')
      ('A018', 'G2m', 'special count unsizeable')
      ('A021', 'G2m', 'special count unsizeable')
      ('A048', 'G2m', 'special count unsizeable')
      ('A050', 'G2m', 'special count unsizeable')
      ('C01', 'G2m', 'special count unsizeable')
      ('A009', 'G3m', 'special count unsizeable')
      ('A018', 'G3m', 'special count unsizeable')
      ('A021', 'G3m', 'special count unsizeable')
      ('A048', 'G3m', 'special count unsizeable')
      ('A050', 'G3m', 'special count unsizeable')
      ('C01', 'G3m', 'special count unsizeable')
      ('A009', 'G4m', 'special count unsizeable')
      ('A018', 'G4m', 'special count unsizeable')
      ('A021', 'G4m', 'special count unsizeable')
      ('A048', 'G4m', 'special count unsizeable')
      ('A050', 'G4m', 'special count unsizeable')
      ('C01', 'G4m', 'special count unsizeable')
      ('A035', 'G2m', 'special count unsizeable')
      ('A044', 'G2m', 'special count unsizeable')
      ('C06', 'G2m', 'special count unsizeable')
      ('A035', 'G3m', 'special count unsizeable')
      ('A044', 'G3m', 'special count unsizeable')
      ('C06', 'G3m', 'special count unsizeable')
      ('A035', 'G4m', 'special count unsizeable')
      ('A044', 'G4m', 'special count unsizeable')
      ('C06', 'G4m', 'special count unsizeable')
      ('A083', 'G2m', 'special count unsizeable')
      ('A083', 'G3m', 'special count unsizeable')
      ('A083', 'G4m', 'special count unsizeable')
      ('A170', 'G2m', 'special count unsizeable')
      ('A170', 'G3m', 'special count unsizeable')
      ('A170', 'G4m', 'special count unsizeable')
=== repeat 2: sized elements 185 · distribution {'S': 45, 'M': 101, 'L': 35, 'unsizeable': 1, 'XL': 3} · statement kinds 18 · special counts 25
  element leaf E (incl. root per-parent items): 21348.6 h
  C3 all parents:                               9765.2 h   of which root C3: 4269.7
  once + per-environment layer [L]:            840.3 h
  GRAND TOTAL:                                  31954 net person-hours  (= 3994.3 pd at 8 h)
  corridor, rho = 0.5:  sd 5103 h · P10 25413 · P90 38495  (x0.80 / x1.20 of the centre)
  named holes (47):
      ('A140', 'K1', 'unsizeable (M10)')
      ('A140', 'K2', 'unsizeable (M10)')
      ('A140', 'A2', 'unsizeable (M10)')
      ('A140', 'A3', 'unsizeable (M10)')
      ('A140', 'A4', 'unsizeable (M10)')
      ('A140', 'A10', 'unsizeable (M10)')
      ('A076', 'G2m', 'special count unsizeable')
      ('A089', 'G2m', 'special count unsizeable')
      ('A076', 'G3m', 'special count unsizeable')
      ('A089', 'G3m', 'special count unsizeable')
      ('A076', 'G4m', 'special count unsizeable')
      ('A089', 'G4m', 'special count unsizeable')
      ('A009', 'G2m', 'special count unsizeable')
      ('A018', 'G2m', 'special count unsizeable')
      ('A021', 'G2m', 'special count unsizeable')
      ('A048', 'G2m', 'special count unsizeable')
      ('A050', 'G2m', 'special count unsizeable')
      ('C01', 'G2m', 'special count unsizeable')
      ('A009', 'G3m', 'special count unsizeable')
      ('A018', 'G3m', 'special count unsizeable')
      ('A021', 'G3m', 'special count unsizeable')
      ('A048', 'G3m', 'special count unsizeable')
      ('A050', 'G3m', 'special count unsizeable')
      ('C01', 'G3m', 'special count unsizeable')
      ('A009', 'G4m', 'special count unsizeable')
      ('A018', 'G4m', 'special count unsizeable')
      ('A021', 'G4m', 'special count unsizeable')
      ('A048', 'G4m', 'special count unsizeable')
      ('A050', 'G4m', 'special count unsizeable')
      ('C01', 'G4m', 'special count unsizeable')
      ('A035', 'G2m', 'special count unsizeable')
      ('A044', 'G2m', 'special count unsizeable')
      ('A035', 'G3m', 'special count unsizeable')
      ('A044', 'G3m', 'special count unsizeable')
      ('A035', 'G4m', 'special count unsizeable')
      ('A044', 'G4m', 'special count unsizeable')
      ('A010', 'G2m', 'special count unsizeable')
      ('A010', 'G3m', 'special count unsizeable')
      ('A010', 'G4m', 'special count unsizeable')
      ('A083', 'G2m', 'special count unsizeable')
      ('A083', 'G3m', 'special count unsizeable')
      ('A083', 'G4m', 'special count unsizeable')
      ('A158', 'K3', 'no size in reading')
      ('A159', 'K3', 'no size in reading')
      ('A170', 'G2m', 'special count unsizeable')
      ('A170', 'G3m', 'special count unsizeable')
      ('A170', 'G4m', 'special count unsizeable')
=== composition, repeat 1 - per top-level subtree: element items + C3 inside the subtree
   N02    Platform architecture                    elements  35  items   3043 h  C3   1093 h  subtotal   4136 h
   N06    Identity and access                      elements  14  items   1554 h  C3    311 h  subtotal   1864 h
   N07    Record governance                        elements  10  items   1118 h  C3    224 h  subtotal   1342 h
   N08    Notifications                            elements  16  items   1475 h  C3    295 h  subtotal   1770 h
   N09    Reporting and dashboard                  elements  10  items   1232 h  C3    246 h  subtotal   1479 h
   N10    User assistance                          elements   6  items    573 h  C3    115 h  subtotal    688 h
   N11    Import and export                        elements  12  items   1502 h  C3    300 h  subtotal   1803 h
   N12    Publish and subscribe                    elements  14  items   1374 h  C3    275 h  subtotal   1649 h
   N13    Shared record management                 elements  37  items   5145 h  C3   1931 h  subtotal   7076 h
   N19    Product module                           elements  19  items   2316 h  C3    628 h  subtotal   2945 h
   N20    Location module                          elements  12  items   1237 h  C3    247 h  subtotal   1484 h
   N21    Access Data module                       elements   9  items   1088 h  C3    218 h  subtotal   1306 h
   N22    Operational properties                   elements  16  items   1062 h  C3    212 h  subtotal   1274 h
   root own per-parent items 612 h · root C3 4666 h · once/per-env 840 h
=== composition, repeat 1 - per activity (element-attached items only, hours)
   K2      4481
   A3      3372
   K1      1981
   A6      1904
   A2      1788
   D4      1365
   A5      1304
   A7      1112
   U3       979
   A4       913
   U2       719
   D2       644
   K3       528
   G3m      384
   U1       373
   O1       373
   A8       323
   A10      313
   G2m      233
   G4m      197
   A9        47
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
   S2 penetration test [52 surf+int: XL]            E =  42.7
   S3 remediation [52 surf+int: XL]                 E =  72.0
   E1 environment: dev [S]                          E =   9.3
   E1 environment: test [M, declared]               E =  17.3
   E1 environment: stage [M]                        E =  17.3
   E1 environment: prod [L]                         E =  30.7
=== size-class agreement: 185 elements in both, 42 differ (77.3% agree)
      ('A034', 'M', 'L')
      ('C14', 'S', 'M')
      ('A007', 'L', 'M')
      ('A015', 'L', 'M')
      ('A017', 'M', 'S')
      ('A025', 'L', 'M')
      ('A146', 'L', 'M')
      ('A147', 'L', 'M')
      ('A008', 'XL', 'M')
      ('A020', 'XL', 'L')
      ('A021', 'M', 'S')
      ('A026', 'S', 'M')
      ('A165', 'L', 'M')
      ('A046', 'L', 'M')
      ('A022', 'M', 'S')
      ('A038', 'M', 'L')
      ('A044', 'M', 'S')
      ('A035', 'M', 'S')
      ('A036', 'S', 'M')
      ('A071', 'L', 'M')
      ('A004', 'L', 'S')
      ('A081', 'XL', 'L')
      ('A082', 'M', 'S')
      ('A100', 'XL', 'L')
      ('A102', 'L', 'S')
      ('A073', 'L', 'S')
      ('A074', 'L', 'S')
      ('A075', 'L', 'S')
      ('A084', 'L', 'M')
      ('A099', 'XL', 'M')
      ('A094', 'L', 'M')
      ('A097', 'M', 'S')
      ('A098', 'M', 'S')
      ('A107', 'L', 'M')
      ('A108', 'L', 'M')
      ('A078', 'XL', 'L')
      ('A123', 'XL', 'L')
      ('A011', 'L', 'M')
      ('A160', 'XL', 'L')
      ('A161', 'XL', 'L')
      ('A162', 'XL', 'L')
      ('C11', 'L', 'M')
=== statement-kind divergences: [('A005', 'behavioural', 'compliance'), ('A158', 'compliance', None), ('A159', 'compliance', None)]
=== special-count divergences: [('A076', 'M', None), ('C06', None, 'S'), ('A010', 'S', None), ('A012', 'M', 'S')]
=== XL elements (either repeat): ['A008', 'A020', 'A029', 'A037', 'A051', 'A078', 'A081', 'A099', 'A100', 'A123', 'A160', 'A161', 'A162']
=== repeat 1: XL leaves 13, their own element-attached effort 2085.0 h: A008, A020, A029, A037, A051, A078, A081, A099, A100, A123, A160, A161, A162
=== repeat 2: XL leaves 3, their own element-attached effort 601.7 h: A029, A037, A051
=== repeat spread: 31954 .. 34933 net person-hours (x1.0932); centre 33444 h
=== tree: 211 elements, 187 leaves, 24 parents; mean leaf depth 2.32
=== unit: net hours of work on the task (docs/instrument.md section 0). Leave, holidays, sickness and
===       presence are NOT included; the comparison-layer conversion is docs/constants.md section 4a.
```

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

# Lytin-K 1.1: Step C calibration parameters

**Engine:** `Lytin-K 1.1`
**Calibrating the run:** `Hotyn-M 2.1` / `Hotyn-W 1.2` / `Hotyn-D 2.0` × rate table `v0.1-h`. These parameters are only valid on this pairing. If any of these engines or the rate table changes, re-derive them rather than carrying them over.

---

## 1. Input inventory

| # | Input | Received |
|---|---|---|
| 1 | Project description (the RFP in brief, plus the case profile: middle/senior team, one site, first system in this domain, enterprise approval cadence) | yes |
| 2 | Assumption log v1 (A0, A1, A2, A4 to A17, A19) | yes |
| 3 | Bottom-up estimate: engine chain, declared technology, three-layer totals for both repeats, breakdown by subsystem and by activity, element classes, size-class counts | yes |
| 4 | Coverage report: what is carried, named holes, work carried but unpriced, closure violations (work the sizing sensors judged missing), structural facts | yes |

**No target, budget, deadline, reference-class forecast, quantiles, outcome, other estimate of this project or statement of any gap was given.** I checked the task message and found none. Nothing asks for the corrections to add up to anything.

**Ambient material, quarantined.** The harness put three things into my context: a git status, recent commit subjects and a memory index. One commit subject contains a ratio between two earlier runs. None of it is input to this run. I did not use it for any rate below and did not treat it as contamination. Every parameter below comes only from the pasted input and external sources. I read no files and used no tools.

---

## 2. Double-counting check

Terms used here:
- **Carried** means the structure has priced items for the work.
- **Hole** means the structure has the item but the sensors would not size it.
- **Closure violation** means a sizing sensor named the work as necessary and missing from its batch.

| # | Blind spot | What the estimate already carries | What stays open |
|---|---|---|---|
| 1 | Missing activity categories (testing, UAT, docs, deployment, migration, security, environments) | All carried: unit tests, test design, code review, 2 test cycles with 2 defect cycles per parent, regression suites, test data, UAT prep with 2 support and 2 triage cycles, user docs, runbook, handover pack, pipeline, 4 environments, cutover, migration with 2 rehearsals, security review, pen test, remediation | **Nothing at category level.** Specific named items remain (rows 4 to 6). |
| 2 | Integration and assembly (includes the diseconomy of scale that summing leaves misses) | Method constant: 20% at every parent including the root. In practice about 46% of element-attached work (r1 10 761 / 23 332; r2 9 765 / 21 349) | **None.** No residual. I do not correct in either direction. |
| 3 | Work that runs for the whole project but is priced once (project management, configuration management, keeping environments and the pipeline running) | Planning per parent (r1 644). Mobilisation, status reporting, risk management, configuration management, pipeline and promotion priced **once**, inside 840 h shared by 23 items. Carried share about 2–3% of the total. | **Residual** against the norm share. Correction T2. |
| 4 | Named holes (in the structure, unpriced) | The item exists and no hours are attached | **Genuine holes:** Access Data REST API (6 items, both repeats); migration of stores that match an A16 entity kind (product images; the permission model for users and roles); backup/DR statements (r2 only). **Not genuine, set to zero:** the other migration holes (validation rules, approval rules, help content, training links, report history, communication preferences, notification templates, identifier-assignment preferences, audit trail, and in r2 the industry configuration and subscription entitlement stores). None of these is an A16 entity kind, and most are new under A7, A10, A12 and I-7. Correction H. |
| 5 | Missing functions (closure violations) | Not carried | **Genuine after triage against the assumption log:** see correction C. **Closed by assumptions (zero):** QuickBooks/SAP connectors (A6), feedback tracker interface and store (A13), password-reset surfaces (A4, credentials live in the identity provider), module-level record stores for GIN, LN, images, hierarchy, attribute sets, LN pool and reuse rules (the report says the shared domain data model and named stores carry them), notification delivery and dispatch interfaces (notification dispatch plus the SMTP and SMS interfaces), record import beyond hierarchy (the record import pipeline and its two mappings), SMS number store (communication preferences). |
| 6 | Checking non-functional requirements (NFRs) | One performance test (response time at stated concurrency, 47 h in r1). Statements carried for capacity, availability, failover and backup/DR. | **Open:** volume and capacity test, near-real-time latency test, availability and failover test. Also no initial population of the read store and no initial search-index build at go-live. Correction C. |
| 7 | Requirements growth after the baseline | Not carried. Requirement elaboration (r1 1 365 h) works out stated requirements only. | **Open.** Correction G1. |
| 8 | Team learning, first system in the domain | Not carried. I read rate table v0.1-h as norms for a team of nominal application experience. | **Open.** Correction G2. |
| 9 | Enterprise client approval cadence | UAT ×2 and the acceptance record are carried | The effort part (rework from late decisions) is a requirement change and sits **inside G1**. The calendar part (waiting, a longer project) is outside net task hours, so I leave it uncorrected. |
| 10 | Business rules "to be defined as part of the project" (I-7) | The validation rule engine and its elaboration are carried | The rule catalogue's content is scope that arrives during the build. It sits **inside G1**, not in C. |
| 11 | Post-production support period, NFR-5 impact analysis | Carried unpriced by A0 | Neither the estimate's job nor mine: A0 marks it as a missing parameter. This is a deliberate, declared exception to "nothing in neither". See section 4. |

**Partition result.** Every open category above is owned by exactly one of H, C, T2, G1 or G2. Nothing carried is also corrected, except the declared residual in T2, which is the norm share minus the carried share. Specific overlaps I checked:
- C and G1: C is work already implied by the RFP; G1 is growth after the baseline.
- C and H: holes are existing items; closure violations are items that do not exist.
- T2 and planning per parent: T2 is residual only.
- G2 and the rate table: G2 relies on the declared reading that the table assumes nominal experience.
- Row 11 and the RFP exclusions fall in neither, by declaration.

**How the coverage report moved my rates:**
- **The generic missing-work percentage went to zero.** The usual rate for bottom-up task lists is 20–30% underestimation from forgotten activities and optimism (van Genuchten 1991, via McConnell 2006, ch. 4). This estimate carries every activity category, so charging that rate would bill it for omissions it did not make. I replaced it with counted fills (H, C) covering only the named items that survive triage.
- **Integration: no correction.** It is carried at about 46% of element work.
- **Testing, UAT, security and migration: none beyond the named items.**
- **Project management and similar ongoing work went up from zero.** The coverage report shows it is priced once rather than over the project's duration.
- **G1's central value moved** from the lower end of the source range (1%/month) to the middle (1.5%/month). The reasons are structural facts: rules to be defined (I-7), identity protocol not chosen (NFR-3), a client governed by committee, and a pre-discovery RFP.
- **G2 was not moved by the coverage report**, which cannot carry team experience. It is set by the case profile.

---

## 3. Corrections

### Unit declaration (applies to H, C and the hours T2 produces)

1. **Unit:** net person-hours of work on the task. This is the same unit as the estimate and rate table v0.1-h, so no conversion is needed.
2. **Losses:** leave, public holidays, sickness, attendance and within-day overheads (including team meetings) are **outside** every amount. T2 covers project-manager and build/configuration-engineer hours, not team meeting time. If a later step's conversion to recorded time already includes a management allowance, T2 counts that twice.
3. **Roles:**
   - H and C cover whatever roles the v0.1-h rows assign to each activity (analyst, developer, tester, migration engineer, performance tester).
   - T2 covers the project manager and the configuration/environment engineer.
4. **Source conventions:**
   - v0.1-h uses net task hours.
   - COCOMO II counts a person-month as 152 h of paid time, with within-day non-task time inside it.
   - Jones works in staff-months under his own convention.
   - T2, G1 and G2 are ratios, so these differences cancel in them.
   - The only absolute conversion I made is the 12-month growth window for G1. It comes from COCOMO II's schedule equation applied to the estimate's size. Switching between net hours and 152 h/month changes that size by about 15–20%, which changes the schedule by about 5% (under one month). That sits inside G1's 9–15 month range.

**Amounts:** H and C. **Factors:** T2 (a rate on a named base), G1 and G2 (global).

### Rules for pricing fills (H and C)

- **Price each fill with the method itself:** the Hotyn-W 1.2 element-attached items for its element class, priced in v0.1-h.
- **Size class:** **M** as the central value (the most common class in both repeats), **S** for low and **L** for high.
- **Exception for NFR test items:** each new verification target costs the same as the performance-test items on the one carried response-time element, in the same repeat and at that element's class.
- **Integration:** apply the estimate's own 20% constant at every ancestor.
  - Holes use their real parent path.
  - Closure fills go under the named top-level subsystem, or its matching child node where one exists. Otherwise treat them as depth 2, which gives ×1.40.
- **Per-parent items** (test execution, defect resolution, UAT) get re-priced only if v0.1-h sizes them by subtree content. Otherwise they are not added again.

### H: named hole fills (pure addition)

| Fill | Parent | Items per fill | Count low / central / high | Repeats |
|---|---|---|---|---|
| Access Data REST API | Access Data module | 6 (its own items) | 1 / 1 / 1 | r1, r2 |
| Migration of stores matching an A16 kind: product image store; permission model (users and roles); staff account store | real path | 3 per store (mapping, ETL, load) | 1 / 2 / 3 stores | r1, r2 |
| Backup and DR procedure statements | Operational properties | 2 | 1 / 1 / 1 | r2 only (r1 priced them) |

### C: closure-violation fills (pure addition)

| Fill (element class) | Parent | Count low / central / high |
|---|---|---|
| Surfaces for behaviours that have no screens: record entry/edit/cloning and hierarchy editor (one each in Product and Location in the central case, because A11 makes them differ; shared in the low case), duplicate review, status and reuse date | Product, Location, Shared record management | 4 / 6 / 8 |
| Other surfaces: approval and attribute-verification review-and-decision; admin assignment of roles, tasks and approval rules; owner publish/share; consumer access request and owner decision; training links; (high only) help-desk reset trigger | Record governance, Identity and access, Publish and subscribe, User assistance | 2 / 5 / 6 |
| Behaviours: deactivate company user; entitlement check before viewing; (central) enforcing subscription export options at export, follow-up after a data challenge; (high) edit-lock release, seeding the four roles | Identity and access, Access Data, Import and export, Record governance | 2 / 4 / 6 |
| Interfaces: collecting 3scale usage data (A5); (high) import/export through the API | Reporting and dashboard, Import and export | 1 / 1 / 2 |
| Stores: report definitions and schedules; groups and members with pending access requests; (central) per-user record subscriptions, onscreen notifications; (high) pending requests as a separate store, page-layout templates | Reporting, Publish and subscribe, Notifications, Product module | 2 / 4 / 6 |
| NFR verification: capacity and volume test (10M GINs, 256k users, concurrency); availability and failover test (99.9%); (central) near-real-time read-store latency test | Operational properties | 2 / 3 / 3 |
| Go-live initial load: read-store initial population; (central) initial search-index build. Each is one ETL item plus one load/reconciliation item. | Platform architecture | 1 / 2 / 2 |

### Correction table

| Name | Blind spot | Form | Rate low / central / high | External source | Confidence |
|---|---|---|---|---|---|
| **H** Hole fills | Items carried but unpriced (row 4) | Pure addition, net task hours | counts × class S / M / L, as above | Rate table v0.1-h (the estimate's own external norms). Counts come from the coverage report checked against A16. | Existence high; size medium |
| **C** Closure fills | Missing functions, NFR checks, go-live load (rows 5, 6) | Pure addition, net task hours | counts × class S / M / L, as above | Rate table v0.1-h. Counts come from the coverage report after triage against A4 to A16. Replaces the generic 20–30% omission rate (van Genuchten 1991; McConnell 2006, ch. 4), which I declined because of the coverage. | Medium-low (I triaged without the leaf name list) |
| **T2** Level-of-effort residual | Project-long PM, configuration management and environment work priced once (row 3) | Targeted multiplier on base **B_T2** = estimate total + H + C (after integration) | 6% / 8% / 11% | Norm share of project management plus configuration management is about 9–14% of effort: Boehm, *Software Engineering Economics* (1981), COCOMO activity distribution (project office about 7–8%, CM/QA about 6–7%, of which QA is already carried by review and testing); Jones, *Estimating Software Costs* 2nd ed. (2007), activity tables (PM about 10% for mid-to-large IT systems). Carried share of about 2–3% is subtracted. | Medium-low |
| **G1** Requirements growth | Scope growth after the baseline, including rules "to be defined" and late client decisions (rows 7, 9, 10) | Global multiplier | ×1.09 / ×1.18 / ×1.30 | Jones, "Software Estimating Rules of Thumb", *IEEE Computer* 29(3), 1996: requirements creep about 2% per calendar month through design and coding. Jones, *Applied Software Measurement* 3rd ed. (2008): about 1–2%/month for information systems. Window from design to end of coding is declared as **12 months** (9–15), from the COCOMO II.2000 schedule equation on the estimate's size (about 20 months total, of which about 60% is design and code). Low = 9 × 1%, central = 12 × 1.5%, high = 15 × 2%. | Medium |
| **G2** Domain inexperience | Team building its first system in this domain (row 8) | Global multiplier | ×1.05 / ×1.10 / ×1.22 | COCOMO II.2000 effort multiplier APEX (applications experience): Low (about 6 months) 1.10, Very Low (2 months or less) 1.22. Central is Low, because experience builds over the project. Low sits halfway between Nominal and Low, allowing for adjacent B2B master-data experience in a middle/senior team. PLEX, LTEX and SITE stay nominal (mainstream stack, one site). | Medium |

Two global multipliers: G1 and G2. There is no third. The client's approval cadence and the undefined business rules were merged into G1, not multiplied separately.

---

## 4. Deliberately uncorrected

- **Post-production support and transition (A0):** term and service level are unknown. It is not a multiplier on build work. It is owned by the assumption log as a missing parameter.
- **NFR-5 impact analysis (A0, count 0).**
- **Scope the RFP excludes:** member onboarding, prefix attributes, the payment process, training materials, future expansion.
- **The split between repeats** (whether a shared obligation counts in full on every leaf or in part): this is spread, not bias. Apply the same parameters to r1 and r2 separately and carry the spread forward.
- **The open-ended XL class and the right skew of task effort** (rate-table rows possibly being medians rather than means): an external rate would need the class boundaries and the row statistic of v0.1-h, which I don't have. Any number I gave would be invented. This belongs to calibrating the rate table and to the spread, not Step C. Base kept for any later use: **the XL leaves' element-attached effort, per repeat** (13 leaves in r1, 3 in r2).
- **The integration constant may be generous (about 46%):** it is a method constant, not a blind spot. No downward correction.
- **Era (A19):** there is no external productivity index from 2018 to now at the level needed.
- **Calendar effects of committee approvals** (waiting, a longer project): outside net task hours.
- **Tail events that no multiplier expresses:** identity protocol changing mid-project; the rules committee stalling; migrated data too poor to load without cleansing beyond reconciliation; a failed failover or 10M-record performance test forcing redesign; IE9 compatibility blowing up. These belong to the tail sensor.
- **Omissions no sensor named:** I apply no generic rate, because coverage is thorough. Unknown unknowns go to spread and tail.
- **Client-side effort:** not the vendor's hours.

---

## 5. Order of application

Run each repeat on its own and never mix r1 and r2. Keep the low, central and high sets together (low with low, and so on) unless the applying step has its own convention for independent propagation. Every step acts on the result of the step before, and no step may be reordered.

1. **H:** price the hole fills per the fill rules, add them as leaf effort, and apply the integration constant along each real parent path.
2. **C:** price the closure fills the same way, add them as leaf effort, and apply the integration constant along the declared parent path.
3. **T2:** compute T2 × (estimate total + H + C) and add it.
4. **G1:** multiply the step 3 subtotal by G1.
5. **G2:** multiply the step 4 result by G2.

Targeted rates apply only to the bases named above. No targeted correction applies to another targeted correction's output except T2, whose base includes H and C by declaration.

# Precomputed bases for the rate agent's targeted steps (you have no access to the leaf tables or the rate table and may not derive quantities of your own)

RK60 prices its fills H and C with the estimate's own rate table by element class and size, with the method's 20% integration constant along the parent path. The orchestrator has done that arithmetic; the priced amounts below are the bases you apply in RK60's order. Each is stated low / central / high (size S / M / L per RK60's fill rule; D4 at S; NFR targets at the carried response-time element's A9 cell, class L, 46.7 h each; integration x1.4 under a top-level subsystem, x1.6 under its matching child node, and along the real path for holes). Apply low with low, central with central, high with high. Unit: net person-hours of work on the task, integration included where stated.

## Repeat 1 — estimate total 34 933 h

| fill (RK60 §3) | low | central | high |
|---|---:|---:|---:|
| H: A140 Access Data REST API, 6 items | 81 | 153 | 262 |
| H: A089 migration items G2m/G3m/G4m | 58 | 117 | 191 |
| H: A018 migration items G2m/G3m/G4m | — | 103 | 167 |
| H: C01 migration items G2m/G3m/G4m | — | — | 167 |
| **H, hole fills, integration included** | **138** | **373** | **787** |
| C: surfaces for screenless behaviours: record entry/edit (and cloning at high) and hierarchy editor, Product and Location, under the module (x1.4); duplicate review and status/reuse-date under the shared-record child nodes (x1.6) | 208 | 569 | 1365 |
| C: other surfaces: approval review-and-decision (N07), admin assignment (N06), owner publish/share and consumer request/decision (N12), training links (N10), help-desk reset trigger (N06, high only) | 91 | 453 | 988 |
| C: behaviours: deactivate company user (N06), entitlement check before viewing (N21), export-option enforcement (N11), data-challenge follow-up (N07), edit-lock release (N07, high), role seeding (N06, high) | 91 | 362 | 988 |
| C: interfaces: 3scale usage collection (N09); import/export through the API (N11, high only) | 77 | 140 | 471 |
| C: stores: report definitions and schedules (N09), groups and members (N12), per-user subscriptions and onscreen notifications (N08, central), pending requests (N12) and page-layout templates (N19) at high | 91 | 336 | 916 |
| C: NFR verification targets: capacity/volume, availability/failover, (central) latency | 131 | 196 | 196 |
| C: go-live initial load: read-store population, (central) search-index build | 43 | 166 | 271 |
| **C, closure fills, integration included** | **731** | **2222** | **5196** |
| **B_T2 = estimate total + H + C** | **35802** | **37528** | **40916** |

## Repeat 2 — estimate total 31 954 h

| fill (RK60 §3) | low | central | high |
|---|---:|---:|---:|
| H: A140 Access Data REST API, 6 items | 81 | 153 | 262 |
| H: A089 migration items G2m/G3m/G4m | 58 | 117 | 191 |
| H: A158 K3 | 7 | 18 | 30 |
| H: A159 K3 | 7 | 18 | 30 |
| H: A018 migration items G2m/G3m/G4m | — | 103 | 167 |
| H: C01 migration items G2m/G3m/G4m | — | — | 167 |
| **H, hole fills, integration included** | **152** | **409** | **847** |
| C: surfaces for screenless behaviours: record entry/edit (and cloning at high) and hierarchy editor, Product and Location, under the module (x1.4); duplicate review and status/reuse-date under the shared-record child nodes (x1.6) | 208 | 569 | 1365 |
| C: other surfaces: approval review-and-decision (N07), admin assignment (N06), owner publish/share and consumer request/decision (N12), training links (N10), help-desk reset trigger (N06, high only) | 91 | 453 | 988 |
| C: behaviours: deactivate company user (N06), entitlement check before viewing (N21), export-option enforcement (N11), data-challenge follow-up (N07), edit-lock release (N07, high), role seeding (N06, high) | 91 | 362 | 988 |
| C: interfaces: 3scale usage collection (N09); import/export through the API (N11, high only) | 77 | 140 | 471 |
| C: stores: report definitions and schedules (N09), groups and members (N12), per-user subscriptions and onscreen notifications (N08, central), pending requests (N12) and page-layout templates (N19) at high | 91 | 336 | 916 |
| C: NFR verification targets: capacity/volume, availability/failover, (central) latency | 131 | 196 | 196 |
| C: go-live initial load: read-store population, (central) search-index build | 43 | 166 | 271 |
| **C, closure fills, integration included** | **731** | **2222** | **5196** |
| **B_T2 = estimate total + H + C** | **32837** | **34585** | **37997** |

- C3 layer (the structure's 20% constant, already inside the totals): 10 761 h (r1), 9 765 h (r2); once-scoped layer 840 h both; element-attached layer 23 332 h (r1), 21 349 h (r2).
- The XL leaves' own element-attached effort, should you need it: repeat 1 2 085.0 h over 13 leaves, repeat 2 601.7 h over 3 leaves (RK60 names this base and leaves it uncorrected).

# What is asked of you

Your definition's output format, sections 1–7, with the declaration reconciliation before Step B. Keep the two repeats as a band and the two class readings as a band; never average either. Apply the rates exactly in the fixed order, low / central / high, showing running totals so the chain can be recomputed by hand. The tail of the final answer comes from the class readings' quantiles as they stand — both readings, in one unit, stated separately. Address the sensor-flagged cross-cutting issues rather than absorbing them: the unit disagreement between the two class readings, both readings' warning about the seam with the carried post-production period, the era mismatch both refused to adjust for, and the rate agent's tail hand-off list. Close with the one or two facts that would most move the answer.
