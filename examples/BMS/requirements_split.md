# BMS — the split: obligations on the product, obligations on the work

Date: 2026-08-20. Performed once, for everybody, per `docs/proposal_product_model.md` §3 and §10 item 1.

**Input:** `requirements.md`, md5 `554ea3608dd0602f0ddf2f7e7b82178c`, N = 73.
**Outputs:** `requirements_product.md` (N = 68) and `requirements_work.md` (N = 5).

An RFP states obligations of two kinds and does not distinguish them. Some bind the **product** — what
must exist when the thing is delivered. Others bind the **work** — what somebody must do. The second
kind must not be handed to `Hotyn-M`, because it is not product structure and would distort the model;
and it must not be left to `Hotyn-W` to invent from the catalogue either, because a demanded
obligation has to trace to the requirement that demands it.

---

## 1. The rules used, stated so they can be criticised

**S1 — Assign, never reshape.** Every entry goes to exactly one list. Ids are unchanged. The union of
the two lists is exactly the pinned list, and the intersection is empty. M1 continues to hold on both
halves: neither list may be added to, split or merged by a run.

**S2 — The hand-over test.** *If a complete and correct system were handed over, would this obligation
already be satisfied by the artefact itself?*

- **yes** → obligation on the **product**. It describes a property or a capability of the thing.
- **no, because it names something a person must keep doing** → obligation on the **work**.

The discriminator is grammatical as often as not: the product entries say what the system *is* or
*does*; the work entries say what *the Supplier* does.

**S3 — Dual entries are recorded once, with a pointer.** Where an entry carries obligations of both
kinds, it is placed on the side of its **primary** obligation and the secondary reading is recorded in
§3 below. It does not appear on both lists. This is the same mechanism as W6 and for the same reason:
an obligation counted twice is work counted twice.

**S4 — Contradictions are reported, not resolved.** Where a split entry collides with the assumption
log, the collision is written down and left to the owner of the inputs. Same discipline as M1's
ambiguity flags.

**S5 — Pinned like the parent.** Both output lists are pinned by md5 in §5. Revising either is a
separate, deliberate act.

---

## 2. What moved, and why

Five entries of 73 fail the hand-over test. Every one of them names the Supplier as the actor, or
names a procedure rather than a property.

| id | entry | verdict | reading |
|---|---|---|---|
| R02 | The Supplier hosts the system | **work** | hosting is an activity performed continuously after delivery; no property of the artefact satisfies it |
| R03 | The Supplier supports the system | **work** | likewise: a support function is people and a process, not a component |
| R64 | Keep technologies up to date; periodic reviews and planned upgrades | **work** | "periodic reviews and planned upgrades" is a programme with a cadence |
| R69 | Configuration management and version control across all environments and documents | **work** | a practice applied to the work products, documents included, and documents are not part of the product |
| R70 | Robust release and patch promotion procedures minimising business impact | **work** | a procedure operated by people; the automation that supports it is not what the entry demands |

**Five of seventy-three, 7%.** The RFP is overwhelmingly product-worded. That is worth registering
before step 2: if delivery work turns out to be a large fraction of the estimate — prediction 4 puts it
above 30% — then almost all of it will come from the **technology catalogue** and almost none from
anything the client wrote down. The client demanded 7% of the delivery work explicitly.

---

## 3. Entries that were judged rather than read

The other 68 went to the product list. Most were immediate. These were not, and each is recorded with
the reading taken, per S3 and S4.

| id | entry | placed | the other reading, and why it lost |
|---|---|---|---|
| R01 | SaaS-based booking management system | product | "as a service" implies somebody runs it — but that act is stated separately as R02 and R03, so R01 keeps only the artefact property: architected as a hosted, multi-tenant service |
| R10 | Clear business processes | product | could be read as "deliver business process documentation", which is work. The RFP states it under *Simplistic and Intuitive*, as a quality of what the user meets. Documentation, if wanted, is technology-derived work from the documentation dimension, not a demanded item |
| R14 | Admin and Support component | product | the word *Support* invites the service reading; the RFP names it in the **context diagram**, as a box inside the system. The service obligation is R03 and is on the work list. The entry remains contentless — the known defect, unchanged |
| R67 | Report generation not excessive; criteria defined at design stage | product | the clause "criteria defined at design stage" is a work obligation embedded in a performance requirement. The primary obligation is the product property; the clause is a specification activity that the assurance technology will mandate anyway |
| R73 | Customer data compliant with the Data Protection Act | product | compliance produces work — assessments, audits — but that work is mandated by an assurance technology, not demanded by this entry. The entry demands a property of the data |
| R37 R38 R40 R47 R48 | supplier uploads, manual handling | product | these read like descriptions of how the business will operate. They are product obligations because they constrain what the system must support and what it must **not** automate — a scope statement on the artefact |
| R08 | Integration with SSO per the client's documentation | product | "per the client's documentation" constrains the design, not the process |

The remaining 60 entries were product by inspection and raised no doubt.

---

## 4. Findings

**F1 — Three of the five demanded-work items were excluded by the assumption log. Fixed 2026-08-20,
and by a rule rather than by a scope decision.** A1 v1 removed "subsequent operation (hosting &
support), user training, the warranty period"; R02, R03 and R64 demand exactly that. Run 18 caught the
R03 case; the split showed it was systematic.

`assumptions.md` v2 adds **A0, the imperative**: *an obligation the client stated cannot be removed by
an assumption.* A log may bound what a number prices and must then name the instrument that prices the
rest or the parameter without which nothing can. An id appearing in neither the priced work nor the
carried list is an **exception** — a defect report, no estimate.

So the three resolve without anybody shrinking the project: the hand-over residue is priced (`E7`,
`O3`, and one policy item for R64) and the continuing service is carried with **the term** named as
the missing parameter and the question going back to the client. Details in `requirements_work.md`.

**F2 — The run-18 product models were built before the split, and contain work.** Nodes such as
*Release & Environment Management* {R69,R70}, *Support & Service Operations* {R03,R14}, *Technology
Currency & Upgrade Programme* {R64} and *Hosting & Runtime Platform* {R01,R02,R12} are work structure
sitting inside a product model. This affects the next step in a specific way:

- running `Hotyn-W` on the run-18 model keeps comparability with run 18's closure test, at the cost of
  crossing those four nodes with the mandated activities as though they were product elements;
- rebuilding the model from `requirements_product.md` is clean, but it is a new run and it moves the
  baseline the closure test was measured against.

Recommendation: **both, in that order** — `Hotyn-W` first on the existing model with the affected
nodes marked, because what is being tested there is the crossing; then a rebuild when `Hotyn-M` is
next run with n > 1 per cell.

**F3 — N moved from 73 to 68, so counts do not cross the split boundary.** Run 18's anchored total of
82–87 nodes was measured at N = 73. The comparable figure on the split list is unknown and will be
lower. Anything quoted across that line must name the list it was measured on.

**F4 — The split is cheap, and it runs in one direction only.** No entry was rescued from the work
side back into the product, because the RFP contains no entry of the form "the system shall be
tested". Testing, UAT, project management, migration and the rest of run 18's closure-violations list
appear **nowhere** in the requirement list, in either half. That confirms the reading that reshaped
the design: those eleven items are not missing from the product model, they are technology-derived,
and only a declared technology can generate them.

---

## 5. Pins

```
0c2dea478b993e4451a66f9468633f1e  requirements_product.md   (N = 68)
330826122b607088df3499e3e71cd103  requirements_work.md      (N = 5)
```

Pinned 2026-08-20. Recompute with:

    tr -d '\r' < requirements_product.md | md5sum

Parent list and its pin: `requirements.md`, `requirements.pin.txt`.
