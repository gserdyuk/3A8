# FaxRxTx — Run 42: the chain's first end-to-end repeatability figure

Date: 2026-08-27. Registered as **action 1** of `docs/status_2026-08-27.md` §7, with its comparators
**pre-registered in `BACKLOG.md` before the measurement ran**.

**What was missing.** The ×1.03 quoted throughout this project is *classification* repeats on top of a
single fixed product model. `run31` says so itself: the pair's second model, `HM29-OA2` (87 nodes
against `HM29-OA1`'s 97), was never crossed and never sized, and "no repeatability reading exists for
this step on this case." Step 1 is the chain's least stable step and it had never been measured
through to a price.

**What run 42 did.** Crossed `HM29-OA2` with `Hotyn-W 1.1` (3 batches), sized it with `Hotyn-D 2.0`
(3 batches), and priced it with **the run-31 assembly, not one rate changed** — same table v0.1 + A1,
same FaxRxTx addenda A2/A3, same declaration, same conventions, same script logic. The OA1 assembly
was re-run first and reproduced 1446.0 / 1400.4 table pd exactly, so the reference is sound.

Eleven sensor runs, **`tool_uses: 0` in every one**, and every one reported and quarantined the
harness injection unprompted — catches seven through eleven of that standing defect.

---

## 1. The result

| | table pd | net task hours |
|---|---:|---:|
| `HM29-OA1`, run 31 repeat 1 / repeat 2 | 1446.0 / 1400.4 | 11 568 / 11 203 |
| **`HM29-OA1` centre** | **1423.2** | **11 385.5** |
| **`HM29-OA2`, this run** | **1351.3** | **10 810.0** |

> ### End-to-end spread: **×1.0532**
> Against the whole OA1 range: ×1.0364 … ×1.0701.

**Against the comparators, both fixed before the number existed:**

| test | threshold | result |
|---|---|---|
| beat the no-method instrument on equal terms (run 41's mean pairwise ratio) | under **×1.168** | **passed** — 3.0× tighter in log distance |
| **gate v2.0 test 1** (`docs/status_2026-08-27.md` §6c) | under **×1.30** | **passed** — 5.1× tighter |
| for scale: the market's interquartile spread on one specification (Jørgensen & Grimstad, 46 companies) | ×1.9 … ×2.6 | 12–18× tighter |

**The declared expectation was wrong, and in the conservative direction.** `BACKLOG.md` predicted
×1.11–1.12 if price tracked node count. The models differ by ×1.115 in node count and the price
differs by only ×1.053, because two effects pulled against each other — see §3.

---

## 2. Where the difference sits

| layer | OA1 centre | OA2 | delta | share of the gap |
|---|---:|---:|---:|---:|
| element leaf E (incl. root) | 7 047.70 | 6 713.93 | −333.77 | **58.0%** |
| C3 integration, all parents | 3 122.16 | 3 019.09 | −103.07 | 17.9% |
| once + per-environment | 511.67 | 373.00 | −138.67 | **24.1%** |
| demanded-work branches | 704.00 | 704.00 | **0.00** | 0.0% |
| **total, net task hours** | **11 385.53** | **10 810.02** | **−575.51** | |

Three readings of that table:

- **A quarter of the whole gap is pure arithmetic, no judgement in it.** The model bracket is
  ≤30 / 31–90 / ≥91 elements. OA1's 97 nodes take the **L** once-rows; OA2's 87 take **M**. A ten-node
  difference straddles a threshold and steps thirteen once-scoped items down a band, unaided by any
  sensor's opinion. Once-scoped items enter no C3 base, so it passes straight to the total.
- **C3 is not an independent contributor.** Its 17.9% is a fixed 20% of the leaf layer at every parent
  — it moves because the leaf moved, and it amplifies whatever the leaf does.
- **The demanded-work branches came out identical to the last hour.** Both crossings disposed the five
  stated work obligations the same way — F51 absorbed at `E6`, F48/F49/F50/F52 standing alone — and
  their addendum rows are rate rows independent of which model was built. **Zero variance, by
  construction**, on 704 net hours, 6.5% of the total.

---

## 3. Why the two models did not differ as much as their node counts

**OA2 is 10% smaller and produced 2.5% *more* work items** — 584 crossing items against OA1's 570.
The cause is one structural choice, verified in both model files:

- **All 18 of OA1's parents have empty own coverage (`∅`)** — they are true aggregates, and the OA1
  assembly's `CLS[parent]="aggregate"` matched the model rather than overriding it.
- **OA2 places obligations on five parents** — HM2-02 and HM2-03 (the F47 parity claim), HM2-18 (F02,
  F10), HM2-26 (F06), HM2-27 (F07). The crossing therefore priced them as elements **and** parents:
  K1/K2/A2/A3/A4/D4 *and* A5/A6/A7/A8/D2.

Same sensor, same version, same pinned input, same declared processing order — and a different answer
to *where an obligation attaches, to a leaf or to the node above it.* **That is a class of variance
step-wise repeatability could not see**, because sizing repeats sit on one fixed tree by construction.

Pulling the other way, the class mix moved against the more expensive rows:

| class | OA1 | OA2 |
|---|---:|---:|
| behaviour | 42 | 43 |
| store | 9 | 10 |
| surface | 8 | 9 |
| **interface** | **12** | **7** |
| **statement** | **8** | **5** |

Interfaces nearly halved, and `K1`/`K2` for an interface are the dearest rows in the table while `A10`
attaches to nothing else. The two forces very nearly cancelled.

---

## 4. What each model refused, and one striking agreement

| | OA1 | OA2 |
|---|---|---|
| named holes | 24–28 items on 6 elements | 18 items on 4 elements |
| elements | HM1-57, 61, 63, 75, 78, 83, 84 | HM2-61, 83, 84, 91 |

**Both models independently refused the seed count of their `HM*-61` — "System database schemas" — and
for the same stated reason.** In OA2 the sizer put it plainly: the model places G1/G2/G3 on the store
while F28 says only *"A database is part of the system (the DBMS is not specified)"* and declares no
entity kind that must exist before the system is usable. *"I will not invent reference or configuration
tables to fill the gap."*

**OA2's other three holes are one finding.** HM2-83, HM2-84 and HM2-91 — the whole access-control
subtree — are `derived`, carry no coverage, and **no obligation anywhere names authentication, session,
role or credential recovery**, while a customer portal (F35) and an internal control centre (F31) both
exist and both presuppose identity. The sizer refused all three rather than guess, and named the
closure: because `D4` sits only on elements with coverage, **no work item in the model produces the
declaration whose absence makes them unsizeable.**

---

## 5. What this measurement may and may not claim

**It may claim:** on this case, the chain's end-to-end spread is ×1.05, it passes gate v2.0 test 1 with
five-fold margin, and it is three times tighter than a no-method prompt's own run-to-run agreement on
the same input. This is the **first evidence in the project's history that the apparatus buys something
measurable over the bare corpus** — and it is on the one axis that needs no fact, no outcome and no
conversion constant, because a ratio of two numbers in one unit cancels every constant applied to both.

**It may not claim any of the following, and the reasons are not cosmetic:**

1. **n = 2 models, one ratio.** A point estimate of a spread, with wide uncertainty of its own.
2. **The two sides are not symmetric.** OA1's figure is the centre of two sizing repeats; OA2's is a
   single sizing pass. The sizing-repeat spread on OA1 was ×1.033, so a single pass can sit ~1.6% off
   its own centre — inside the noise of ×1.053, but not nothing.
3. **This was measured on the favourable case, and that must not be buried.** The two FaxRxTx models
   agreed to ×1.024 on their anchored part. On **BMS the same sensor pair differed by ×1.56 in
   structure size** with a Jaccard of 0.31 against FaxRxTx's 0.41. **The BMS end-to-end figure could be
   far worse, and it has not been measured.** Gate test 1 asks for repeatability, not for repeatability
   on the case that flatters it.

**The obvious next measurement, and it is now the cheapest one that could overturn today's result:**
cross and price BMS's second product model the same way.
