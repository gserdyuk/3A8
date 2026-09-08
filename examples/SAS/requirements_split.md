# SAS — the split: obligations on the product, obligations on the work

Date: 2026-09-08. Performed once, for everybody, by the rules of the BMS split
(`examples/BMS/requirements_split.md` §1, S1–S5). Those rules are not restated here; only what they
produced on this input and where the input made them work harder.

**Input:** `requirements_pinned.md`, N = 153.
**Outputs:** `requirements_product.md` (N = 146) and `requirements_work.md` (N = 7).

---

## 1. What moved

| id | entry | verdict | reading |
|---|---|---|---|
| W-1 | project component 1, Requirements and Design | **work** | a stage the vendor performs; the RFP words it as something done, not as a property of the artefact |
| W-2 | project component 2, Development and Testing | **work** | same |
| W-3 | project component 3, Implementation | **work** | same — deployment, migration, acceptance, cutover are acts |
| W-4 | project component 4, Post-production Support and Transition | **work** | a service performed after delivery; the BMS R03 shape |
| NFR-11 | deployment to four environments, with deployment processes | **work** | the artefact can be complete and correct and not yet deployed anywhere; the entry names an act and a procedure |
| NFR-12 | migration of the current application data, including users | **work** | an act performed once against a predecessor's data; no property of the new system satisfies it |
| NFR-15 | performance testing processes to ensure the response times are met | **work** | an assurance activity. Its first clause — exceptions for time-consuming transactions — qualifies NFR-14 and is recorded as a pointer, S3 |

**Seven of 153, 4.6%** — against BMS's 5 of 73 (6.8%) and FaxRxTx's 5 of 52 (9.6%). The RFP is
overwhelmingly product-worded, like BMS; but unlike BMS, four of its seven demanded items name the
project's own stages (W-1–W-4) rather than a continuing service, and one (NFR-12) names the one kind
of work the catalogue keeps behind a declared dimension. This split therefore predicts a *high*
absorption rate; the prediction is registered in `requirements_work.md`.

---

## 2. The difference from the two earlier cases, stated before anything is estimated

BMS demanded **operational** work (hosting, support, currency). FaxRxTx demanded **transitional**
work (immersion, parallel run, cutover, decommissioning). SAS demands **the lifecycle itself**:
requirements and design, build and test, implementation, post-production support — the four
components of §1 Project Structure — plus two named acts inside implementation (deploy to four
environments, migrate). All but the post-production period are things every declared dimension
already mandates. If the crossing absorbs six of seven, that is the catalogue asserting that an RFP's
project structure is a way of building and nothing more, which is the claim worth seeing made.

---

## 3. Entries that were judged rather than read

The other 146 went to the product list. Most were immediate. These were not.

| id | entry | placed | the other reading, and why it lost |
|---|---|---|---|
| I-7 | all functionality validated against X-Customer Standards and business rules, **which will be defined as part of the project** | product | the primary obligation is a property: the system validates against the rules. The clause "defined as part of the project" is elaboration work, and the delivery dimension mandates that (D4) without being asked. S3: the pointer stands here |
| NFR-8 | highly available, 99.9%; failover process **developed and tested**; failover monitoring | product | the property (availability, failover, monitoring that notifies) is the artefact's. "Developed and tested" is what the construction and assurance dimensions do to every element; "respondents should provide a plan" is a proposal obligation. Primary: product |
| NFR-9 | backup and disaster recovery **procedures** complying with X-Customer policies | product | a procedure is a document, and documents are not the product (BMS R69 reasoning) — but the obligation is that the system *can be* backed up and recovered under the client's policies, which is a property; the written procedure is the operational runbook the documentation dimension mandates. Primary: product, pointer to O2 |
| NFR-10 | security configuration, processes and procedures; the security design and the components used | product | "processes and procedures" invite the work reading; the obligation as worded is that the solution *includes* them — a property. The security review is what the declared security dimension mandates |
| NFR-5 | adhere to technical standards; **on deviation, an impact analysis at no cost** | product | the primary obligation is adherence, a constraint on the artefact. The impact analysis is conditional work and is carried under A0 outcome 3 in `assumptions.md` A1 (missing parameter: whether the solution deviates; reading: it does not) |
| W-1 … W-3 | the project's stages | work | could be read as "not obligations at all — merely the RFP's outline of the engagement". They are kept because the RFP states the vendor **performs** them and structures pricing by them; a stage the client names is a demanded item even when every dimension implies it. Absorption then records that it is implied rather than leaving it unstated |
| I-1 | a web-based solution **replacing the applications currently available** | product | "replacing" invites migration and decommissioning; the obligation as worded is a scope statement on the artefact — what it is *instead of* — exactly as FaxRxTx F47. The migration act is NFR-12 and is on the work list |
| G-10.2 | help content is maintained by X-Customer non-technical resources | product | reads as an operating arrangement; it constrains the artefact — there must be something a non-technical person can maintain content with |
| L-13 | record annual verification of records | product | "annual" names a cadence, which smells of a programme; but the obligation is that the system *records* a verification, a capability. Operating the annual campaign is nobody's obligation in this RFP |
| D-8 | easily access information on how to pay for ad hoc access | product | with D-8.1 excluding the payment process, what remains is an informational surface. Kept, thin |

The remaining 136 entries were product by inspection and raised no doubt.

---

## 4. Findings

**F1 — The assumption log strikes out no demanded item.** As on FaxRxTx, A0 is not exercised on the
lists themselves. It *is* exercised on one clause: the post-production support period of W-4 is
carried, not priced, with the term as the missing parameter — the BMS R03 shape exactly.

**F2 — Three entries are thin, and all stayed on the product side.** D-8 (information on how to pay),
G-11 (a link to training) and I-11 (X-Customer-owned data is accessible) each name a capability and
almost nothing else. They are carried, not repaired; expect thin nodes and sizing doubts downstream.
`assumptions_product.md` P4 supplies content for the two the sensors cannot size otherwise.

**F3 — The product list is large, and the reason is the source, not the system.** N = 146 against
BMS's 68 for a system that is perhaps twice BMS's size and certainly not twice FaxRxTx's. This RFP
enumerates sub-obligations under every heading (G-13 alone is eight rows); BMS stated one obligation
per sentence. Any per-requirement ratio carried across cases — nodes per requirement, items per
requirement — measures the document's granularity as much as the project's, and must name the list
it was measured on (FaxRxTx F4, the same warning from the other direction).

**F4 — The Product and Location modules are near-duplicates by construction.** Twenty-one of the 36
Product entries have a Location twin with the same wording (P-1/L-1, P-2/L-2, P-5.2/L-5.1, …). The
RFP says so itself ("Location Numbers are similar in format … but have a different set of
attributes"). M1 forbids merging them, so a product model will either build two parallel subtrees or
one shared mechanism covering both ids — and the two readings differ in structure size by nearly a
factor of two on those branches. **This is named now, before any run, as the expected largest source
of between-run disagreement**, and `assumptions_product.md` P3 pins the reading.

---

## 5. Pins

Recorded in `requirements.pin.txt`, computed after all three files were closed. Recompute with:

    tr -d '\r' < examples/SAS/requirements_product.md | md5sum
