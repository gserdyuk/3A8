# BMS — pinned requirement list

Extracted from `BMS_extracted.md` (the RFP as pulled from `BMS_updated.docx`). This list is the
**external anchor** for `Hotyn-M` per `docs/proposal_product_model.md` §3 and M1.

**A run may not add, remove, split or merge entries.** Where an entry looks like it contains two
obligations, the run flags it as ambiguous and proceeds. Revising this list is a separate, deliberate
act performed once for everybody.

Granularity rule used in extraction, stated so it can be criticised: **one entry per obligation as the
RFP words it.** Where the RFP states a single obligation with two objects ("confirm hotel and
transport reservations"), that is one entry, not two. Where it states two obligations in one sentence
("access to the system, manual upload of pricing"), those are two entries. Goals and rationale
("cost reduction", "automation to remove manual processes") are not obligations and are not listed.
Container names whose contents are enumerated elsewhere (Employees Portal, Administration Portal,
Suppliers Portal) are not listed separately; **Admin and Support is listed**, because the RFP names it
and gives it no content anywhere.

---

## The list

| id | requirement | source section |
|---|---|---|
| R01 | SaaS-based booking management system | Project Overview |
| R02 | The Supplier hosts the system | Project Overview |
| R03 | The Supplier supports the system | Project Overview |
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
| R64 | Keep technologies up to date; periodic reviews and planned upgrades | NFR / Architectural |
| R65 | High configurability for changes in legislation, policy, process, organisation structure | NFR / Architectural |
| R66 | Screen loads under 2 seconds | NFR / Availability & Performance |
| R67 | Report generation not excessive; criteria defined at design stage | NFR / Availability & Performance |
| R68 | Highly available and resilient | NFR / Disaster Recovery |
| R69 | Configuration management and version control across all environments and documents | NFR / Configuration Management |
| R70 | Robust release and patch promotion procedures minimising business impact | NFR / Deployability |
| R71 | Designed to grow in the future | NFR / Scalability |
| R72 | TLS 1.2 minimum for all authenticated client traffic | NFR / Data Security |
| R73 | Customer data compliant with the Data Protection Act | NFR / Data Security |

**N = 73.**

---

## Processing orders

Two orders are declared, so that M4's claim — that the skeleton pass makes the result independent of
processing order — can be tested. Both are deterministic; neither is the source order.

### Order A — "top-down", by breadth of impact

Criterion, stated explicitly: **a requirement comes before another when it constrains more of the
system than the other does.** Four bands, in this sequence:

1. **System-level** — what the system *is*: R01, R02, R03, R04, R05
2. **Cross-cutting quality** — properties every part must have: R09, R11, R12, R13, R61, R62, R63,
   R64, R65, R66, R67, R68, R69, R70, R71, R72, R73, R10
3. **Surfaces and external boundaries** — what the system talks to and who uses it: R06, R07, R08,
   R14, R36, R46, R52, R57
4. **Behaviours** — everything else, in list order: R15, R16, R17, R18, R19, R20, R21, R22, R23, R24,
   R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R37, R38, R39, R40, R41, R42, R43, R44,
   R45, R47, R48, R49, R50, R51, R53, R54, R55, R56, R58, R59, R60

### Order B — exact reverse of order A

Chosen because it is the **adversarial** case, not a mild reshuffle: detailed behaviours arrive first
and the system-level statements arrive last. If M4 is right and the skeleton is built from the list as
a set, order B and order A must produce the same model. If M4 is wrong, this is where it shows.

---

## Known weaknesses of this list, recorded before use

1. **The granularity is one person's judgement**, made once. It is pinned rather than correct. The
   free parameter has moved out of the run and into this document, which is an improvement (one
   shared, inspectable decision) but not an elimination.
2. **R14 has no content.** It is in the list because the RFP names it, and it is expected to generate
   an ambiguity flag and possibly an empty skeleton node. That is the intended behaviour, not a defect.
3. **Some entries overlap**: R11 and R65 both say "configurable"; R12/R13 and R66/R68 both bear on
   performance; R05 overlaps the portal requirements. Overlap is deliberate — the RFP states these in
   two places and M1 forbids the run from merging them. Multiple requirements mapping to one node is
   expected and is exactly what the coverage relation is designed to record.
4. **Nothing in this list names transition off the manual process**, because the RFP does not. Run 17
   prediction 6 and `proposal_product_model.md` prediction 6 both turn on this.
