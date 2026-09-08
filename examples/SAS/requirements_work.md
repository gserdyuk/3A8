# SAS — demanded-work list (`Hotyn-W` input)

The seven entries of `requirements_pinned.md` (N = 153) that fail the hand-over test of
`examples/BMS/requirements_split.md` §1 S2. **Ids are unchanged.** The other 146 are in
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

| id | obligation | source |
|---|---|---|
| W-1 | Project component 1, Requirements and Design, performed by the vendor | Project Structure |
| W-2 | Project component 2, Development and Testing, performed by the vendor | Project Structure |
| W-3 | Project component 3, Implementation, performed by the vendor | Project Structure |
| W-4 | Project component 4, Post-production Support and Transition, performed by the vendor | Project Structure |
| NFR-11 | Deployment to four environments — development, test, staging/pre-production, production — with appropriate deployment processes | Technical |
| NFR-12 | Migration of the current application data, including users, to the new solution | Technical |
| NFR-15 | Exceptions may be made for some time-consuming transactions (e.g. barcode generation); performance testing processes ensure the response times are met at the appropriate user load | Technical |

**N = 7.**

Why each is work: W-1–W-4 name stages the vendor performs and the RFP prices by; NFR-11 names an act
(deploying) and a procedure; NFR-12 names a one-time act against a predecessor's data; NFR-15 names
an assurance activity. The readings are in `requirements_split.md` §1.

---

## Registered expectation, before the declaration is written

Written down so the outcome can be scored rather than rationalised — the same act the BMS and FaxRxTx
lists performed. Both this file and `technology_declaration.md` were written on 2026-09-08 by the
same orchestrator; the expectation was fixed first and the declaration's §3 scores it.

- **W-1, W-2, W-3 will be absorbed wholesale.** They are the names of what the construction,
  assurance, environments, data and acceptance dimensions do. If any of the three stands alone, a
  dimension has been read more narrowly than it is written.
- **NFR-11 will be absorbed** by the environments dimension (`E1` per environment, `E2`, `E3`), with
  the environment count raised to four — a parameter, not a new activity.
- **NFR-12 will be absorbed** by `G-MIGRATE` (`G1m`–`G5m`). This is the first case in the project to
  declare that dimension; it exists in the catalogue precisely for this entry's shape.
- **NFR-15 will be absorbed** by `A9`, performance testing of behavioural statements with measurable
  targets — NFR-14 supplies five. If the crossing refuses because A9 is per-element and NFR-15 asks
  for a *process*, that is the catalogue reading "process" as "an item per target", which is what it
  has always done.
- **W-4 will be partially absorbed, and the remainder carried.** `O3` (support handover pack) and
  `E6` (production cutover) price the hand-over; the post-production support period itself has no
  dimension and no term. The BMS R03 shape, with the term as the missing parameter.

**Expected: six of seven absorbed, one partial.** If fewer are absorbed, the catalogue is thinner
than an ordinary RFP's project structure — a finding about the catalogue. If the declaration absorbs
W-4 whole, a dimension has been invented.
