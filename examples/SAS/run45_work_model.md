# Run 45 — the SAS work model, `Hotyn-W 1.1` × `HM44-OA1`, n = 1, seven batches

**2026-09-08.** Case 3, step 2. The product model `HM44-OA1` (246 nodes, 187 leaves) crossed with the
approved technology declaration in seven partial runs by top-level subtree — A: S-01, S-02 · B: S-03 ·
C: S-04, S-05, S-06 · D: S-07, S-08 · E: S-10, S-11 · F: S-12, S-13 · G: S-09, S-14 (+ the demanded-work
list) — the same design as FaxRxTx run 30, with more batches because the model is 2.5× larger.

Raw: `run45_raw/HW45-A1.md` … `HW45-G1.md`. Prompts: `run45_raw/make_prompts.py` (deterministic from the
model and the declaration; the activity tables are catalogue 1.4's declared entries verbatim, with the
integration note reworded so that no pricing vocabulary reaches the sensor). Consolidation:
`run45_raw/consolidate_run45.py` → `classes.tsv`, `work_model.tsv`. All seven stamped `Hotyn-W 1.1`,
`tool_uses: 0`, launched on Claude Opus 5 (the harness's `opus` alias), all quarantined the git status.
Every reply arrived complete from §1; the raw headers say which were taken from the harness transcript
(C, F, G) and which were transcribed from the delivered reply (A, B, D, E).

---

## 1. The readings

| reading | value |
|---|---:|
| elements crossed | 245 of 246 (the root `S-00` is outside every batch; its per-parent items are computed at assembly) |
| elements by class | behaviour 93 · aggregate 58 · surface 35 · store 25 · statement 24 · interface 10 |
| **crossing items** | **1 650** (A 224 · B 284 · C 324 · D 195 · E 214 · F 187 · G 222) |
| items by activity | K1 163 · K2 163 · K3 24 · A2 163 · A3 163 · A4 163 · A5 108 · A6 108 · A7 54 · A8 54 · A9 1 · A10 10 · U1 32 · U2 64 · U3 64 · D2 58 · D4 160 · G2m 22 · G3m 22 · G4m 22 · O1 32 |
| items per crossed element | 6.73 |
| refusals | 237 — **filter 212 · judgement 25** (A 10 · E 3 · F 12 · B, C, D, G 0) |
| elements untouched | 0 |
| demanded ids | 7 of 7 accounted for (batch G): W-1, W-2, W-3, NFR-11, NFR-12 absorbed; W-4 partial, the support period carried; NFR-15 entered as a standing branch `DW-NFR-15` with a reconciliation flag — **retired at consolidation**, because A9 fired on A-145 in batch F (the declaration's absorption claim is realised there) |
| deferred to assembly | once-scoped A1, U4, D1, D3, D6, E2, E3, E4, E6, E7, G1m, G5m ×2, O2, O3, O4, S1, S2, S3 · per-environment E1 ×4 · the root's per-parent items |

For scale: FaxRxTx run 30 crossed 96 elements into 570 items (5.9 per element); BMS run 21 measured
5.5–6.0. **6.7 per element here**, the difference being `C-UAT` (U1–U3 on every surface-bearing parent)
and `G-MIGRATE` (three activities per store), neither of which FaxRxTx declared.

## 2. Where the step's freedom sat

All 25 judgement refusals are one question asked in two places: **does a parent whose subtree holds only
`statement` elements draw the per-parent test activities** (S-01.3, S-12.6, S-13.2, S-13.3 × A5–A8, 16
lines), and **is a store fed internally a migration target** (A-132, C-012, A-034 × G2m–G4m, 9 lines). Both
are declaration gaps, not sensor whims: the catalogue says nothing about statement-only subtrees and nothing
about stores populated from inside the system. Recorded as catalogue findings; not repaired here.

The classifications the sensors themselves flagged as load-bearing: A-003 (statement, not store), A-017
(store), A-011 (store), A-012 (behaviour, not statement), A-062, A-056/A-057 (interface), A-074/A-098/A-117
(store), C-008, C-025, A-112 (interface), A-099 (store). A repeat crossing would be compared there.

## 3. Findings the crossing surfaced, none repaired

1. **A9 reached one element.** Of 24 statements, only A-145 ("high-availability design to the 99.9%
   level") carries a measurable target *in its declared content*. A-154 ("response-time design targets
   under load", covering NFR-14's five thresholds), A-134 (volumes), A-144 (user population and
   concurrency) were filtered because the element's **name** states no figure — the figures live in the
   obligation texts, which the crosser does not receive (it sees ids). On FaxRxTx the targets were in the
   element names (F36/F37) and A9 fired. **This is an input-format finding about the chain, not a
   product-model defect**: the sizing step *does* receive obligation texts and counts A9 targets from
   them, so the assembly will show exactly what A9 lost. Named now, before any number exists.
2. **Statement-only subtrees draw no assurance** (S-01.3, S-12.6, S-13.2, S-13.3): eleven design
   statements under S-01.3 receive K3 and D4 and nothing else. The catalogue's own note that a statement
   "generates real work — evidence is kept — but never the work of building a feature" is honoured; whether
   the evidence should be tested is the open catalogue question above.
3. **No `surface` under S-01/S-02**: company and user administration (A-015, C-005, C-006) is modelled
   as behaviour with no screen, so U1–U3 and O1 generate nothing for identity. Batch A named it (F-2). If
   the product model is right, the admin screens are inside S-12; if not, UAT work for identity is lost.
4. **Derived leaves with empty coverage** (C-001…C-027, 27 nodes) carry construction and assurance items
   that project onto no requirement — 13% of the leaves. A property of the product model, stated so the
   requirement-anchored comparison is not misread.
5. **Granularity**: A-060, A-099, A-107, A-110, A-111, A-129, A-141, A-024, A-029, A-044, C-008, C-025
   named as leaves that read as two things. Crossed as they stand; expected to reappear as XL or doubts at
   sizing.
6. **S-06.2 does not exist** (batch C asked). Correct: `HM44-OA1` collapsed it at closure (§7b: S-06.2 →
   A-120). Not a gap.

## 4. Registered expectation, scored

`requirements_work.md` predicted six absorbed and W-4 partial. Batch G returned exactly that for six of
seven and entered NFR-15 as a standing branch on the ground that A9 generated nothing *in its batch*; the
whole-model view retires the branch. **Six absorbed, one partial — as registered.**

## 5. Carried forward

`work_model.tsv` (1 650 rows, cycles expanded) and `classes.tsv` (245 elements) are the pinned input of
step 3. The sizing prompts are generated from them by `run47_raw/make_sizing_prompts.py` and carry, for
every sized element, its covered obligations **with their texts** — so the A9 count, unlike the A9
applicability, is taken from the figures the client wrote.
