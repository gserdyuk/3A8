# Run 42 — `Hotyn-W 1.1` × Opus 5 — FaxRxTx crossing of **HM29-OA2**, batch C

Subtrees HM2-08, HM2-09, HM2-10, HM2-11, HM2-13 (HM2-12 with HM2-77/78 sits inside HM2-08) =
**23 elements**, **plus** all model-wide once-scoped items (13) and per-environment items (E1 × 3),
**plus** the demanded-work list. `tool_uses: 0`.

## Contamination — NOT clean, and the run said so

**F48 contains a duration** — *"about 1–2 months"*. The engine's strict rule is to stop. It did not,
and stated the exception for the orchestrator to overrule: the figure sits inside a **verbatim client
obligation**, the demanded list does not pass through the crossing, so it could not reach any
applicability judgement; and this batch is the sole carrier of the 16 model-wide items. **The figure
was struck**; F48 enters as `DW-F48` with the duration removed.

> **Orchestrator's ruling, 2026-08-27: the exception is accepted, on precedent.** `HW30-C1` met the
> same figure on the OA1 crossing and made the same call on the same ground. Accepting it here keeps
> the two crossings comparable, which is the entire point of run 42. Recorded, not hidden.

Harness injection also quarantined (branch, status, commit subjects naming `Hotyn-P`, runs 38–40, UFP
figures). **Ninth independent catch.**

## Class roster

| class | n | elements |
|---|---:|---|
| surface | 7 | HM2-64, 65, 67, 68, 69, 70, 71 |
| aggregate | 6 | HM2-08, 09, 10, 11, 12, 13 |
| interface | 3 | HM2-38, 39, 77 |
| store | 3 | HM2-14, 75, 76 |
| behaviour | 3 | HM2-83, 84, 91 |
| statement | 1 | HM2-78 |

**Parents in scope (6):** HM2-08, 09, 10, 11, 12, 13.

## Item sets

- **K1, K2, A2, A3, A4** on 16: HM2-14, 38, 39, 77, 64, 65, 67, 68, 69, 70, 71, 75, 76, 83, 84, 91.
- **K3** on HM2-78. **A10** on HM2-38, 39, 77. **A9: zero.**
- **D4** on 14 (those with own coverage): HM2-14, 38, 39, 77, 78, 64, 65, 67, 68, 69, 70, 71, 75, 76.
- **G1, G2, G3** on **HM2-14 only**.
- **per parent** on all 6: A5×2, A6×2, A7, A8, D2. **O1** on HM2-09 and HM2-10 only.
- **model-wide:** A1, U1d, D1, D3, D6, E2, E3, E4, E6, E7, O2, O3, O4 (13) + E1 × 3.

## Demanded work (W6) — all five accounted for

| id | disposition | ground |
|---|---|---|
| F48 | **stands alone** `DW-F48` | no declared activity's content is domain immersion or technology selection; D1 is mobilisation, K1 is design *downstream of* a selection already made — the declaration is a pinned input, so nothing in it performs the choosing |
| F49 | **stands alone** `DW-F49` | A5/A8 mandate no tap on the *real* stream, a once-only condition over the whole system; absorbing at A5 would silently delete "real stream" |
| F50 | **stands alone** `DW-F50` | no declared activity performs back-to-back comparison against a legacy system; G3 reconciles a seed load, and G-SEED declares no legacy migration |
| F51 | **absorbed at `E6@MODEL`** | E6 production cutover is exactly this obligation under C-DIRECT |
| F52 | **stands alone** `DW-F52` | E6 cuts the new system over; it does not retire the old one. `K3@HM2-78` realises the *during-transition* split, not the terminal decommission |

**4 standing alone, 1 absorbed, 0 unaccounted — identical to the OA1 crossing's disposition.**

## Instrument readings

| reading | value |
|---|---|
| total work items | **165** (161 mandated-derived + 4 demanded) |
| by scope | per element 101 · per parent 20 · per parent × cycles 24 · once 13 · per environment 3 · demanded 4 |
| items per element | mean 6.30 · min 2 (HM2-78) · max 9 (HM2-14) |
| `no` answers | **20 — filter 14, judgement 6** |
| elements untouched | 0 of 23 |

## Findings (W5)

- **W5-e — the root falls between batches.** HM2-01 is a parent above all five named subtrees and
  received nothing in any batch. **Handled at assembly**, exactly as the OA1 assembly did
  (`PARENT["HM1-01"] = P7 + O1`, "the root, computed here: not in any batch").
- **W5-b — access control is entirely unanchored.** HM2-83, 84, 91 — the whole HM2-13 subtree — carry
  no own coverage and are all `derived`. No D4 items, and no authentication requirement exists to
  project onto. Either the requirement set is missing one, or these three exist on the model-builder's
  inference alone.
- **W5-c — three leaves each read as two things:** HM2-14 (a reach *footprint* welded to a *registry*),
  HM2-75 (a writer and a store), HM2-76 (an extract and a store). **HM2-14's `store` reading carries
  the only G1/G2/G3 in the batch — reclassify it and all three vanish.**
- **W5-d — the declaration does not cover four stated obligations.** F48, F49, F50, F52 reach the work
  model only through the demanded branch. Either the declaration is incomplete for a system replacing
  a running predecessor, or they are correctly outside it. **No activity invented.**
- **The six judgement refusals** are one reading twice: CDR and billing-extract stores fill from the
  system's own run-time output, so under `G-SEED` there is no reference or master data to seed. Flip
  that reading and the total rises by six.
- **A9 deferred, not unused:** its candidate statements (HM2-72, 73, 74) sit in batch B, which
  classified them `behaviour` — so A9 is **zero across the whole model**. See `HW42-B.md` F-3.

**Where this run's freedom sat:** five contested classifications, the consequential one being
HM2-83/84/91 as `behaviour` — had any been read `surface`, HM2-13 would gain an O1 item.
