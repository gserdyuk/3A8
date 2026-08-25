# BMS — product obligation list (`Hotyn-M` input)

Derived from `requirements.md` (md5 `554ea3608dd0602f0ddf2f7e7b82178c`, N=73) by the split recorded in
`requirements_split.md`. Five entries — R02, R03, R64, R69, R70 — are obligations on the **work** and
live in `requirements_work.md`. **Ids are unchanged**, so the two lists together are exactly the
pinned list and every id still means what it meant.

This is the **external anchor** for `Hotyn-M` per `docs/proposal_product_model.md` §3 and M1.

**A run may not add, remove, split or merge entries.** Where an entry looks like it contains two
obligations, the run flags it as ambiguous and proceeds. Revising this list is a separate, deliberate
act performed once for everybody.

Granularity rule inherited from `requirements.md`: **one entry per obligation as the RFP words it.**

---

## The list

| id | requirement | source section |
|---|---|---|
| R01 | SaaS-based booking management system | Project Overview |
| R04 | The system is the sole source of accurate hotel and transport bookings | Project Overview |
| R05 | Access for the travel department, transport suppliers and employees to manage their confirmed bookings | Project Overview |
| R06 | Integration with EPAM's Cost Tracking Center via API | Project Overview / Integration |
| R07 | Integration with UPSA via API | Project Overview / Integration |
| R08 | Integration with SSO per the client's documentation | Project Overview / Integration |
| R09 | Common look and feel for all users | Project Overview / Simplistic and Intuitive |
| R10 | Clear business processes | Project Overview / Simplistic and Intuitive |
| R11 | Highly configurable solution that supports the client's evolution | Project Overview / Flexibility |
| R12 | Highly performant system supporting high demand | Project Overview / Performance |
| R13 | Support for critical instances such as major disruption situations | Project Overview / Performance |
| R14 | Admin and Support component *(named in the context diagram; no functional detail given anywhere in the RFP)* | Context diagram |
| R15 | Intelligent search across multiple third-party systems | Supplier Search and Prioritization |
| R16 | Search across manually uploaded bookings | Supplier Search and Prioritization |
| R17 | Search based on requirements specified in the system | Supplier Search and Prioritization |
| R18 | Prioritisation based on matching to booking requirements | Supplier Search and Prioritization |
| R19 | Prioritisation based on custom rules defined by the Travel Manager | Supplier Search and Prioritization |
| R20 | Custom prioritisation rules are defined in the Administration Portal | Supplier Search and Prioritization |
| R21 | Booking requirements are initially defined in the Cost Tracking Center | Supplier Search and Prioritization |
| R22 | Booking requirements are amendable in the Employees Portal | Supplier Search and Prioritization |
| R23 | Booking requirements are amendable in the Administration Portal | Supplier Search and Prioritization |
| R24 | Prioritisation may change over time as requirements or rules change | Supplier Search and Prioritization |
| R25 | Approval and booking process with stages Proposed, Accepted/Rejected, Approved/Declined, Booked/Cancelled, Paid | Approval and Booking |
| R26 | Stage changes supported by notifications via email | Approval and Booking |
| R27 | Stage changes supported by notifications via SMS | Approval and Booking |
| R28 | Ability to change and extend the booking process in future | Approval and Booking |
| R29 | Automatic booking | Approval and Booking |
| R30 | Manual hotel booking managed by the Travel Manager via web site forms | Approval and Booking |
| R31 | Frequent integration to the Cost Tracking Center to update booking requirements | Changes Management |
| R32 | New requirements, changes and cancellations are driven by CTC updates | Changes Management |
| R33 | Merging of incoming updates according to a defined policy | Changes Management |
| R34 | On merge conflicts, alerts to the parties | Changes Management |
| R35 | Manual change of a selected hotel as required | Changes Management |
| R36 | Third-party hotel suppliers have access to the system | 3rd Party Hotel Suppliers |
| R37 | Hotel suppliers manually upload available booking, pricing and other details | 3rd Party Hotel Suppliers |
| R38 | Hotel supplier booking is handled manually | 3rd Party Hotel Suppliers |
| R39 | One transport supplier (Uber) is integrated automatically | Support Transport Suppliers |
| R40 | All other transport suppliers are manual | Support Transport Suppliers |
| R41 | Pick-up and drop-off locations initially loaded from the Cost Tracking Center | Support Transport Suppliers |
| R42 | Pick-up and drop-off locations amendable in the Employees Portal | Support Transport Suppliers |
| R43 | Pick-up and drop-off locations amendable in the Administration Portal | Support Transport Suppliers |
| R44 | Ability to override pick-up and drop-off locations | Support Transport Suppliers |
| R45 | Combining of multiple transport bookings | Transport Combining Opportunities |
| R46 | Third-party transport suppliers have access to the system | 3rd Party Transport Suppliers |
| R47 | Transport suppliers manually upload pricing details | 3rd Party Transport Suppliers |
| R48 | Transport supplier booking is handled manually | 3rd Party Transport Suppliers |
| R49 | View details and status of each booking | Employees Portal |
| R50 | Confirm hotel and transport reservations | Employees Portal |
| R51 | View and print confirmed reservations | Employees Portal |
| R52 | Seamless access via SSO | Employees Portal |
| R53 | Capture feedback from employees, associated to a particular booking | Employees Portal |
| R54 | System configuration for the Travel Manager | Administration Portal |
| R55 | Visibility of booking statuses for the Travel Manager | Administration Portal |
| R56 | Reporting for the Travel Manager | Administration Portal |
| R57 | Front end to administer the system and control the configuration | Administration Portal |
| R58 | Booking details reporting | Reporting Capabilities |
| R59 | Suppliers reporting | Reporting Capabilities |
| R60 | Financial reporting | Reporting Capabilities |
| R61 | Modern web-based technologies, fresh / clean / intuitive UX | NFR / Usability |
| R62 | Multiple display resolutions including mobile and portable devices | NFR / Usability |
| R63 | Scalable, high-performing structured database platform for large volumes | NFR / Architectural |
| R65 | High configurability for changes in legislation, policy, process, organisation structure | NFR / Architectural |
| R66 | Screen loads under 2 seconds | NFR / Availability & Performance |
| R67 | Report generation not excessive; criteria defined at design stage | NFR / Availability & Performance |
| R68 | Highly available and resilient | NFR / Disaster Recovery |
| R71 | Designed to grow in the future | NFR / Scalability |
| R72 | TLS 1.2 minimum for all authenticated client traffic | NFR / Data Security |
| R73 | Customer data compliant with the Data Protection Act | NFR / Data Security |

**N = 68.**

---

## Processing orders

The two orders declared in `requirements.md` with the five work entries removed and nothing else
changed. Both are deterministic; neither is the source order.

### Order A — "top-down", by breadth of impact

Criterion, stated explicitly: **a requirement comes before another when it constrains more of the
system than the other does.** Four bands, in this sequence:

1. **System-level** — what the system *is*: R01, R04, R05
2. **Cross-cutting quality** — properties every part must have: R09, R11, R12, R13, R61, R62, R63,
   R65, R66, R67, R68, R71, R72, R73, R10
3. **Surfaces and external boundaries** — what the system talks to and who uses it: R06, R07, R08,
   R14, R36, R46, R52, R57
4. **Behaviours** — everything else, in list order: R15, R16, R17, R18, R19, R20, R21, R22, R23, R24,
   R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R37, R38, R39, R40, R41, R42, R43, R44,
   R45, R47, R48, R49, R50, R51, R53, R54, R55, R56, R58, R59, R60

### Order B — exact reverse of order A

Chosen because it is the **adversarial** case, not a mild reshuffle: detailed behaviours arrive first
and the system-level statements arrive last.

R60, R59, R58, R56, R55, R54, R53, R51, R50, R49, R48, R47, R45, R44, R43, R42, R41, R40, R39,
R38, R37, R35, R34, R33, R32, R31, R30, R29, R28, R27, R26, R25, R24, R23, R22, R21, R20, R19,
R18, R17, R16, R15, R57, R52, R46, R36, R14, R08, R07, R06, R10, R73, R72, R71, R68, R67, R66,
R65, R63, R62, R61, R13, R12, R11, R09, R05, R04, R01

---

## Known weaknesses of this list, recorded before use

Inherited from `requirements.md`, plus what the split adds.

1. **The granularity is one person's judgement**, made once. Pinned rather than correct.
2. **R14 has no content.** It is in the list because the RFP names it.
3. **Some entries overlap** (R11/R65 on configurability, R12/R13/R66/R68 on performance and
   availability, R05 against the portal requirements). Overlap is deliberate; M1 forbids merging.
4. **Nothing in this list names transition off the manual process**, because the RFP does not.
5. **New with the split:** R01 ("SaaS-based") keeps its product reading — the system is architected
   as a hosted multi-tenant service — while the *acts* of hosting and supporting it moved to
   `requirements_work.md` as R02 and R03. A run that finds itself positing an operations or support
   subsystem under R01 should flag it rather than build it.
6. **New with the split:** N fell from 73 to 68, so node counts from run 18 are **not** directly
   comparable with node counts from any run on this list. Anything quoted across that boundary must
   say which list it was measured on.
