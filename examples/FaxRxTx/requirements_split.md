# FaxRxTx — the split: obligations on the product, obligations on the work

Date: 2026-08-22. Performed once, for everybody, by the same rules as the BMS split of 2026-08-20
(`examples/BMS/requirements_split.md` §1, rules S1–S5). Those rules are not restated here; only what
they produced on this input, and where this input made them work harder than BMS did.

**Input:** `requirements_pinned.md`, N = 52.
**Outputs:** `requirements_product.md` (N = 47) and `requirements_work.md` (N = 5).

---

## 1. What moved

| id | entry | verdict | reading |
|---|---|---|---|
| F48 | domain immersion and architecture/technology selection, ~1–2 months | **work** | a period of learning and deciding; no property of a handed-over artefact satisfies it |
| F49 | integration tests on the real message stream | **work** | an activity performed on live traffic |
| F50 | integration-test results compared with the old system and agreeing | **work** | an act of comparison and adjudication against a running predecessor |
| F51 | rollout to production; the new system takes production traffic | **work** | a transition event; the artefact can be complete and correct and not yet carrying traffic |
| F52 | the old version can be decommissioned | **work** | establishing it is work: traffic cut over, the parallel period ended |

**Five of fifty-two, 9.6%** — against BMS's 5 of 73, 6.8%. Close enough that the ratio is not the
interesting number; **what kind** of work is demanded is.

---

## 2. The difference from BMS that matters, stated before anything is estimated

BMS's five demanded items were all **operational**: hosting, support, technology currency,
configuration management, release procedure — obligations about the years after delivery, from a
client buying a service.

FaxRxTx's five are all **transitional**: immersion, parallel-stream testing, comparison against the
predecessor, cutover, decommissioning — obligations about getting from a running old system to a
running new one, from a company reworking its own product.

This is the first case in the project where the demanded-work list points straight at catalogue 1.4
§13's registered failure — *"transition off the manual process — parallel running, decommissioning,
change management … If that work is to appear, it must enter as a requirement."* Here it does enter
as one. Whether that escape hatch actually works is now measurable rather than arguable, and
`requirements_work.md` registers the prediction before the declaration is written.

---

## 3. Entries that were judged rather than read

The other 47 went to the product list. Most were immediate. These were not.

| id | entry | placed | the other reading, and why it lost |
|---|---|---|---|
| F19 | 8–10 formats; **each format is a separate piece of integration and stabilisation work** | product | the clause says "work" in as many words. But the obligation is that 8–10 formats are supported; the clause is A7 forbidding the reader to treat extra formats as free. A handed-over system supporting ten formats satisfies it. The clause survives as a **sizing** instruction, and that is where it belongs |
| F43 | coexistence with the old system for the duration of the transition | product | parallel running is unmistakably work — but the obligation as worded is a **capability**: the new system must be able to run alongside the old one. The work of *operating* the parallel period is F49/F50/F51/F52's business. Split deliberately, and it is the sharpest S3 case in this list |
| F42 | integration with the old system | product | an interface of the artefact; no supplier act is named |
| F47 | the new system replaces the core functionality of the first version | product | reads as a project goal, but it constrains the artefact's scope: what must be in it. Kept as a scope statement on the product, exactly as BMS kept R37/R38/R40/R47/R48 |
| F09 F11 | OCR workers, conversion-and-sending workers | product | "workers" here names **components of the system**, not people. §4 and §6 make this explicit ("the printing (rendering) and OCR workers" is listed among things the team *built*) |
| F08 F15 | OCR on a third-party library; rendering via a Black Ice-class driver | product | these read like procurement decisions. They are constraints on the artefact's construction, and A4 confirms them as integration obligations, not activities |
| F30 | the development language is C# | product | a constraint on the artefact, in the same class as BMS R61 "modern web technologies" |
| F21 F35 | cluster management tool; user portal | product | contentless entries kept on the product side. See §4 |

The remaining 39 entries were product by inspection and raised no doubt.

---

## 4. Findings

**F1 — Nothing in the assumption log strikes out a demanded item.** BMS's split found three of five
demanded items excluded by A1 v1 and needed A0 to rescue them. Here A1 excludes only components (PoP,
routing, billing, v1) and post-launch operation — and no demanded item asks for those. **A0 is not
exercised on this case.** That is a fact about the input, not a repair: it means the FaxRxTx run
tests the crossing and the rates without the A0 dispute on top.

**F2 — Two entries are contentless and both stayed on the product side.** F21 (cluster management
tool, "queue lengths and so on") and F35 (user portal, no detail anywhere) are the FaxRxTx analogues
of BMS R14. They are carried, not repaired. Expect them to appear as thinly-covered nodes in the
product model and as sizing doubts downstream; that is the correct behaviour and it is what a
contentless input should cost.

**F3 — The split does not run in one direction only, unlike BMS.** BMS's F4 recorded that no entry
could be rescued from the work side back into the product, because the RFP contained no entry of the
form "the system shall be tested". This source **does** contain such entries (F49, F50), and it
contains the transition work (F51, F52) whose absence twenty-four earlier runs had failed to
generate. The direction of the surprise is reversed: BMS under-demanded work and the catalogue had
to supply it; FaxRxTx demands work the catalogue does not have.

**F4 — N = 52 against BMS's N = 73, for a system that is plainly not smaller.** Worth registering
before any count is compared across the two cases: this input is a **recollection**, not an RFP. It
states the system's structure densely and its obligations sparsely. Any per-requirement ratio carried
across from BMS — nodes per requirement, work items per requirement — is measuring the document as
much as the project, and must name the list it was measured on.

---

## 5. Pins

Recorded in `requirements.pin.txt` together with the parent list's pin, computed after all three
files were closed. Recompute any of them with:

    tr -d '\r' < examples/FaxRxTx/requirements_product.md | md5sum
