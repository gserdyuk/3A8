# FaxRxTx — demanded-work list (`Hotyn-W` input)

The five entries of `requirements_pinned.md` (N = 52) that fail the hand-over test of
`examples/BMS/requirements_split.md` §1 S2. **Ids are unchanged.** The other 47 are in
`requirements_product.md`.

These are obligations the source states about the **doing**. `Hotyn-W` takes them as W6 input: each
enters the work model as its own branch unless a mandated activity of the declaration absorbs it, in
which case it is recorded once, at that activity, and marked *accounted for*.

**A0 applies** (`examples/BMS/assumptions.md` v2/v3): an obligation the source states cannot be
removed by an assumption. It may be bounded, and the remainder must then name its instrument or the
parameter without which nothing can price it. An id appearing neither in the priced work nor in a
carried list is an **exception** — a defect report, not an estimate.

---

## The list

| id | obligation | source | why it is work |
|---|---|---|---|
| F48 | A stage of domain immersion and architecture/technology selection, about 1–2 months (DHT and the like were studied) | §6 / A1 | a period of people learning and deciding; no property of the delivered artefact satisfies it |
| F49 | Integration tests on the real message stream | §6 / A2 | an activity performed on live traffic, not a capability of the thing |
| F50 | The integration-test results are compared with the "old system" and must agree | §6 / A2 | an act of comparison and adjudication, performed by people against a running predecessor |
| F51 | Rollout to production: the new system takes production traffic in prod | A1 / A2 | a transition event, not a property; the artefact can be complete and correct and not yet be carrying traffic |
| F52 | The old version can be decommissioned | A2 | the *establishing* of this is work — traffic cut over, parallel period ended, no obligation left on the predecessor |

**N = 5.**

---

## Registered expectation, before the declaration is written

Written down now so the outcome can be scored rather than rationalised — the same act
`examples/BMS/requirements_work.md` performed on 2026-08-20.

- **F51 will be absorbed** by the environments dimension (`E6` production cutover). It is the
  clearest case: a declared way of working mandates exactly this.
- **F49 and F50 will be contested.** The assurance dimension mandates test design, execution and
  defect resolution, but nothing in `A-TB` says *on the real message stream, against a running
  predecessor*. If the crossing absorbs them into `A5`/`A6`, that is the catalogue asserting that a
  parallel-run comparison is an ordinary test cycle — which is a claim worth seeing made explicitly.
- **F48 will not be absorbed.** No dimension of catalogue 1.4 mandates a domain-immersion or
  technology-selection stage. This is the FaxRxTx analogue of BMS's R64: a stated obligation that no
  way of building implies. If it is absorbed anyway, a dimension has been read more generously than
  it is written.
- **F52 will not be absorbed.** Catalogue 1.4 §13 records the absence of transition work —
  parallel running, decommissioning, change management — as the design's known, registered,
  reproducible failure, and says explicitly that such work can only enter **as a requirement**.
  Here it does enter as one. F52 is therefore the first live test of that escape hatch.

If four of five stand outside the declaration, the FaxRxTx case is telling us the catalogue was
written for the BMS shape of project and is thin where this one is thick — a finding about the
catalogue, not about the estimate.
