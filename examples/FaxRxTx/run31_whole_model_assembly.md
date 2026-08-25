# Run 31 — the FaxRxTx whole-model assembly

**2026-08-22. Written before `FACT.md` was opened.** That ordering is the point of the exercise and it
is recorded here so the reader can check it: the number below was fixed, the file written, and only
then was the project's actual outcome read. Session record `sessions/2026-08-22_…` §8 step (d).

Raw: `run31_raw/HD31-repeat1.md`, `run31_raw/HD31-repeat2.md`, `run31_raw/assemble_faxrxtx.py`.
Reproduce with:

```bash
python examples/FaxRxTx/run31_raw/assemble_faxrxtx.py
```

---

## 1. The chain that produced it

| step | instrument | output | run |
|---|---|---|---|
| obligation list | (orchestrator, once for everybody) | N = 52 → 47 product + 5 work | pins in `requirements.pin.txt` |
| product model | `Hotyn-M 1.1` × Opus 5, n = 2 | `HM29-OA1`, 97 nodes (the pair agreed to ×1.024 on the anchored part) | 29 |
| technology declaration | (orchestrator, visible scope decisions) | `K-BESPOKE · A-TB · C-DIRECT · D-TEAM · E-DSP · G-SEED · U-OPS-USER · SA-NONE` | — |
| crossing | `Hotyn-W 1.1` × Opus 5, n = 1, three batches | 570 crossing items + 4 demanded branches | 30 |
| size classes | `Hotyn-D 2.0` × Opus 5, n = 2, three batches | 74 of 79 elements sized in each repeat | 31 |
| prices | `docs/rate_table.md` v0.1 + A1; FaxRxTx addenda **A2, A3** (gap-blind `Hotyn-K 1.0` × Fable 5) | 11 demanded-work rows | 31 |
| arithmetic | script | below | 31 |

No engine in the chain produced an effort figure. Every person-day in the result comes from a pinned
table row joined to a classification by arithmetic performed outside every sensor.

## 2. The number

| layer | repeat 1 | repeat 2 |
|---|---:|---:|
| element leaf effort (incl. the root's own per-parent items) | 897.28 | 864.65 |
| C3 integration at every parent, 20% | 396.80 | 383.75 |
| — of which the root's C3 | 179.46 | 172.93 |
| once + per-environment layer | 63.96 | 63.96 |
| demanded-work branches | 117.33 | 117.33 |
| **total** | **1475.36 pd** | **1429.69 pd** |
| **in the case's own unit** (A9: 1 pm = 21 pd) | **70.3 pm** | **68.1 pm** |

**Repeat spread ×1.0319. Centre 1452.5 pd = 69.2 pm.**

The demanded-work layer in detail — the four branches no declared dimension absorbed, priced by the
gap-blind addenda against orchestrator-declared multiplicands (4 domain areas · 2 candidate mechanisms
· 2 tap points · 2 test cycles · 2 message types · 4 comparison runs):

| branch | items | pd |
|---|---|---:|
| F48 immersion and architecture selection | W-F48.1 ×4, W-F48.2 ×2, W-F48.3 | 43.50 |
| F49 integration tests on the real stream | W-F49.1 ×2, W-F49.2, W-F49.3a, W-F49.3b | 36.83 |
| F50 comparison against the predecessor | W-F50.1, W-F50.2 ×4, W-F50.3 ×2 | 29.33 |
| F52 decommission-readiness | W-F52 | 7.67 |

## 3. What is *not* in the number — the named holes

Priced at zero, deliberately, each because a sensor refused rather than guessed. **The estimate is
understated by whatever these are worth, and that is the honest form.**

| element | items unpriced | why |
|---|---|---|
| HM1-61 System database schemas | 9 (incl. all three seed items) | F28 names a platform and not one entity kind; the store's driver counts zero. Both repeats refused |
| HM1-83 Non-delivery handling | 6 | the content is *"what happens when there is no delivery"* — a question, not an act. Both repeats refused |
| HM1-78 Old-system integration interface | 7 (incl. A10) | F42 gives the word "Integration" and names neither direction nor payload. Both repeats refused |
| HM1-84 Core-parity scope baseline | 2 | declares itself the boundary of "which core functions" and names none. Both repeats refused |
| HM1-63 seed items | 3 | the one named kind is created at run time; nothing is declared as pre-existing. Both repeats refused the seed count while sizing the element itself |
| HM1-75 Private cluster network topology (repeat 1) / HM1-57 Fax lifecycle stage machine (repeat 2) | 2 / 6 | one refusal each, on opposite elements — each repeat named the other's reading in its own doubts before choosing |

**A seventh hole, of a different kind, named by the rate author rather than by a sizing sensor:**
`W-F49.3a/3b` price the real-stream execution cycles *and explicitly exclude fixing the defects those
cycles surface*. Nothing in the model prices that fixing — `A6` defect resolution is per-parent and
scoped to the ordinary test cycles, not to a parallel-run shakeout against live traffic. Hotyn-K said
it plainly: *"if the estimator has no other home for those excluded things, the exclusions are holes,
not savings."* There is no other home. It is a hole.

## 4. The three readings this assembly forces, before any fact is consulted

**R6 — the once-layer is invariant across two unrelated projects, and that is arithmetic, not
insight.** FaxRxTx's once-and-per-environment layer is **63.96 pd**; BMS's was **63.7 pd**. The
declarations differ substantially — FaxRxTx has no acceptance stage and no security dimension, BMS had
both; FaxRxTx sits in the L model bracket (97 elements), BMS in M (78). The additions and subtractions
happen to cancel. Two projects with nothing in common agreeing to 0.4% on a whole layer is a fact about
the bracket structure of the table, not about the projects.

**R7 — the root C3 is the same number too: 179.5 here, ≈181 on BMS.** C3 is 20% of everything beneath,
so the root's C3 tracks the total, and the totals are close. That is consistent, not independent.

**R8 — and this is the one that matters: the two totals are 7.7% apart for projects that are not
remotely the same size.** BMS: 1348 pd, 78 elements, 68 obligations, an RFP for a booking system.
FaxRxTx: 1452 pd, 97 elements, 47 obligations, a worldwide fax platform on a 16–20 node cluster with
hand-built distributed delivery control. **Per element the two land at 17.3 and 15.0 pd.** The
instrument's output is, to first order, *element count × a constant*, and element count is set by how
finely `Hotyn-M` chose to cut — a property of the modelling act, not of the project.

*What would overturn R8:* a case where two models of materially different granularity over the same
obligations produce materially different totals — which is exactly what the OA2 structure axis (87
nodes against 97) would measure, and which is not run here. *What would confirm it hardest:* the fact
comparison landing far from this number in the direction the element count predicts.

R8 is not a defect discovered by this run; it is `docs/technology_catalogue.md` §14's registered
concern arriving in numerical form. It is registered here **before** the fact is read, so that whatever
the fact says cannot be used to invent it afterwards.

## 5. Sensitivities carried, not resolved

- **Structure.** `HM29-OA2` — the pair's second model, 87 nodes against 97 — is not crossed, not sized
  and not priced. Under R8 its total would be lower roughly in proportion. Named, not quantified.
- **Crossing.** n = 1. The three batches logged **20 judgement refusals** (9 in B, 11 in C) against 50
  filters; a second crossing could differ on those 20 lines and on the 9 contested classifications
  batch A recorded. No repeatability reading exists for this step on this case.
- **The four scope decisions** of the declaration — `C-DIRECT`, `E-DSP`, `G-SEED`, `U-OPS-USER` —
  each priced in the declaration's §5 as a one-line edit. `G-SEED → G-MIGRATE` is the largest and its
  ground is the thinnest.
- **W-F48.1's headcount.** The immersion row aggregates two people per domain area, stated in the row
  and linear in it. Four areas × that assumption is 23.3 pd of the 43.5 pd immersion branch.
- **W-F50.3's proxy.** Priced per message type because the true driver — distinct difference classes —
  is unknowable in advance. Hotyn-K flagged it as the **highest calibration priority of any row it has
  written**, with P/O = 10, and stated that its error is one-sided: it can understate and cannot
  overstate.
- **The vintage question**, from the declaration §4(i): the rate table's norms are modern, the project
  ran 2007–2009 on own hardware with no cloud and no orchestrator. **Not pre-adjusted**, by design.

## 6. The claim being tested

**69.2 person-months, spread 68.1–70.3 from classification repeatability alone**, on a chain in which
no engine saw a number and the orchestrator saw no outcome.

The next document opens `FACT.md`.
