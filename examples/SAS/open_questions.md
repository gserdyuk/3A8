# SAS — open questions to the client, and the assumptions standing in for the answers

**Pinned input, version 1, 2026-09-08.** Consumed by every run alongside the requirement
lists. The procedure and the comparison rule are those of `examples/BMS/open_questions.md` and are
not restated.

The RFP is a training document with no client to ask, so every question is `not asked` and the
assumptions are what the estimate rests on. In a live engagement the first move is to send this file.

---

## The register

| # | ids | the question | reading taken | status | where declared |
|---|---|---|---|---|---|
| Q1 | NFR-3, G-1.x, G-4 | Where does user and role administration live — in the application, with the IdM authenticating, or entirely in the IdM? Which protocol will the IdM speak? | in the application; the IdM issues claims through one protocol | not asked | `assumptions.md` A4 |
| Q2 | P-19, L-15, G-12.1 | Do "external systems such as QuickBooks, SAP" require connectors to those products, or is import through the named file formats and the API sufficient? | file formats and API; IDoc is the SAP path; no product connector | not asked | A6 |
| Q3 | G-12.1, G-12.2 | Is the format list closed at six plus the API? What do "PC and Mac formats" add? | closed; encoding and line-ending variants inside the adapters | not asked | A6 |
| Q4 | G-7.2, NFR-4 | Are usage reports to be read from 3scale, or produced by the solution? | read from 3scale's analytics API | not asked | A5 |
| Q5 | P-13, P-14 | Which barcode symbologies and sizes does "X-Customer Standard supported barcodes of various types and sizes" mean? | four: UPC-A, EAN-13, ITF-14, GS1-128; selectable sizes; PNG and SVG | not asked | A9 |
| Q6 | P-16 | What is a "digital GIN that can be embedded in a web site" — a snippet, or a resolvable identifier with a resolver service behind it? | a snippet: QR image plus structured markup; no resolver | not asked | A9 |
| Q7 | P-1, L-1, P-10.3, L-9.3, L-2.1, G-10.1 | How many industries vary, and in what — attributes, rules, help, LN pools? Is the variation configuration or separate behaviour? | configuration data per industry, one mechanism per varying thing; 25 industries is a volume | not asked | A10 |
| Q8 | P-11.1, P-11.3 | What are the pre-defined GIN hierarchy levels, and which dimensions does the fit check use? | each, case, pallet; height and weight | not asked | A11 |
| Q9 | G-10.2 | Is help content maintained in the application or in an existing content management system? | in the application | not asked | A12 |
| Q10 | G-9 | "A single X-Customer contact or feedback tracking system" — which, and if a system, which one? | email to one configured address | not asked | A13 |
| Q11 | G-7.x | Are reports built into the solution or delivered through a business-intelligence tool the client has? | built in | not asked | A14 |
| Q12 | NFR-2 | What is the target latency behind "near real-time"? | none pinned; the property is that updates flow as changes occur, not overnight | not asked | A8 |
| Q13 | NFR-12, NFR-2 | Which applications are the migration source, and which entity kinds move? Are images and sharing permissions among them? | several current applications; seven kinds: companies and prefixes, users and roles, GIN records, LN records, hierarchies, sharing permissions, product images | not asked | A16 |
| Q14 | W-4 | Over what period, at what service level, does post-production support run? | none available — the term is the missing parameter; the period is carried, not priced | not asked | A1 |
| Q15 | NFR-5 | Does the proposed solution deviate from any X-Customer technical standard, so that an impact analysis is owed? | no deviation; count 0 | not asked | A1 |
| Q16 | NFR-11 | Is the fourth environment ("test") a shared integration environment or a second production-like environment? | shared integration environment; `E1` class M | not asked | A17 |
| Q17 | G-1, G-1.2 | What is a "task" assigned to a user? | a responsibility inside the record workflow — which records or kinds a user edits or approves | not asked | `assumptions_product.md` P3 |
| Q18 | G-1.3 | "Other roles may be added" — configurable roles, or a fixed set of four? | a configurable role set with four named | not asked | P3 |
| Q19 | L-13 | Does "record annual verification" mean the system runs the annual campaign, or records the outcome? | records the outcome and shows what is due | not asked | P3 |
| Q20 | I-2 | One application or a suite? | left to design, as the RFP says; modelled as one product with three module areas | not asked | P3 |
| Q21 | G-13.4, D-3 | Who administers the "controlled group managed by X-Customer"? | X-Customer staff, in the application | not asked | P4 |
| Q22 | NFR-8 | What does the failover process cover — application tier only, or the databases and the read store too? | all tiers the solution owns | not asked | P3 |

---

## How this register is used in a comparison

As on BMS: every comparison of two runs is reported twice — over all requirements, and excluding
the ids named above. The difference is the input-ambiguity component. The filter is this register,
never the runs' own ambiguity flags.
