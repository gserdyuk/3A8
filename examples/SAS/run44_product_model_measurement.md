# Run 44 — the SAS product model, `Hotyn-M 1.1`, n = 2

**2026-09-08.** Case 3, step 1, first sensor. One cell: **Opus 5 × order A × n = 2** — deliberately
the same cell as BMS run 19 and FaxRxTx run 29, so the three cases are comparable and the only
difference is the project.

Raw: `run44_raw/HM44-OA1.md`, `run44_raw/HM44-OA2.md`. Comparison script: `run44_raw/compare_run44.py`.
Inputs: `requirements_product.md` (md5 `db9fdc8ff77844f0b9bbb3881d292587`, N = 146) +
`assumptions_product.md` v1 (md5 `2540cfb1fca7a90a9f9c5cfb937718f1`), both pasted whole into each
prompt, with order A declared and the standing quarantine paragraph. No file was read by either
sensor; `tool_uses: 0` in both. Both printed the stamp `Hotyn-M 1.1`; the pre-batch probe returned
`Lytin-F 5.0`. The model half of the stamp is the orchestrator's record: both were launched with the
harness's `opus` alias, i.e. Claude Opus 5. The case profile, the lists, the log and the declaration
were committed (`73357e9`) before the launch.

---

## 1. Protocol fact first: both replies arrived truncated at the head, and this time it is not recoverable

Run 29 §6 recorded that a subagent reply can reach the orchestrator with its head missing, and set
the recovery: ask the same agent to re-emit verbatim, never re-run. Both replies of this run arrived
that way — OA1 from the pass-2 accretion row for I-8, OA2 from inside the pass-1 row for P-17. The
recovery could not be applied: **`SendMessage` is disabled in this session**, so the agents cannot be
addressed after their first reply. A re-run is not a recovery (it turns n = 2 into n = 3 with a member
discarded), so the record stands as received.

What was absent from both as received: §1 (the contamination check as the sensor wrote it), §2 (the
skeleton log) and all or most of §3 (the accretion log — the place where the `covered` verdicts, this
engine's remaining freedom, are written). What was complete in both: §4 completion log, §5 convergence
trace, **§6 the final model with every parent**, §7 empty skeleton nodes, §7b normalisation, **§7c
coverage completeness per requirement**, §8 instrument readings, §9 assumption log.

**Recovered later the same day, for OA2 only.** The harness keeps a transcript file per agent, and
OA2's held the complete assistant message — the same text the sensor emitted, not a re-emission and
not a re-run. `HM44-OA2.md` now carries all nine sections and its header says where the text came
from. OA1's transcript file was empty, so OA1 stands as received: sections 1–3 lost. (The transcript
files of the seven crossing runs of run 45 behaved the same way — four survived, three were empty —
and the cause is not known; the raw file headers say which is which.)

Consequences, stated plainly. For OA1 the contamination check is attested only by the harness
(`tool_uses: 0`) and by the sensor's §8 and §9 texts, not by the section itself; its skeleton is
recoverable in content from §6 (every node carries its provenance label) but not in the order it was
posited; its accretion verdicts are lost as a log and survive only as their result, the coverage sets.
Everything the downstream chain consumes — the tree, its parents, its coverage — is intact in both, so
**the run is usable; one member's own trace is not.** The cause is the same as run 29's: a reply
longer than what the harness relays whole, and this input is three times run 29's. Debt: a way to
launch a sensor whose long reply survives transit, recorded in `BACKLOG.md`.

---

## 2. The readings

| reading | OA1 | OA2 | ratio |
|---|---:|---:|---|
| skeleton (posited) | 72 | 69 | ×1.04 |
| accretion (accreted) | 160 | 167 | ×1.04 |
| **anchored (posited + accreted)** | **232** | **236** | **×1.017** |
| completion (derived) | 27 | 20 | ×1.35 |
| nodes before normalisation | 259 | 256 | ×1.012 |
| **nodes after normalisation** | **246** | **242** | **×1.017** |
| nodes collapsed at closure | 13 | 14 | — |
| leaves after normalisation | 187 | 187 | ×1.00 |
| coverage assignments (requirement, node) | 257 | 279 | ×1.086 |
| nodes per requirement, mean | 1.76 | 1.91 | ×1.09 |
| co-located requirement pairs | 155 | 154 | ×1.006 |
| nodes covering both a `P-` and an `L-` id (the twin reading of P3) | 37 | 33 | ×1.12 |
| skeleton nodes ending with empty **total** coverage | 0 of 72 | 0 of 69 | — |
| ambiguity flags | 17 | 25 | — |
| partial marks standing at closure | 0 | 0 | — |
| completion-covers-a-requirement defects | 0 | 0 | — |
| unplaceable requirements | 0 | 0 | — |
| requirements covered, checked from §6 by script | 146 of 146 | 146 of 146 | — |

**Jaccard of the co-location relations: 96 shared pairs, 213 in the union → 0.451.**

Provenance counts are the sensors' own, taken before normalisation as the engine requires; the
script's post-normalisation counts (59 / 55 posited) differ by exactly the collapsed nodes.

---

## 3. Scoring run 19's predictions on a third case

| # | prediction | BMS run 19 | FaxRxTx run 29 | SAS run 44 |
|---|---|---|---|---|
| 1 | executability: all nine sections, a parent for every node | held | held in content, broken in transit | **held in content, broken in transit — both members** |
| 2 | anchored total agrees within ±5% | REFUTED, ×1.56 | CONFIRMED, ×1.024 | **CONFIRMED, ×1.017** |
| 3 | derived spread exceeds anchored spread | REFUTED and inverted | CONFIRMED, ×1.40 > ×1.024 | **CONFIRMED, ×1.35 > ×1.017** |
| 4 | relations within ×2 in size **and** Jaccard above 0.5 | SPLIT: ×1.07, J = 0.308 | SPLIT: ×1.14, J = 0.406 | **SPLIT: ×1.006, J = 0.451** |
| 6 | fewer than 20% of skeleton nodes end with empty total coverage | not scoreable | CONFIRMED: 0% and 7.7% | **CONFIRMED: 0% and 0%** |

The same three predictions hold that held on FaxRxTx; prediction 4 splits the same way for the third
time, with the Jaccard rising case by case (0.31 → 0.41 → 0.45) and never crossing its threshold.

---

## 4. The reading, and what would overturn it

**R6 — On an RFP that enumerates its obligations finely, two runs agree on structure size to ×1.017,
which is FaxRxTx's figure and not BMS's.** Run 29 R5 left two mechanisms undistinguished for why
FaxRxTx did not reproduce BMS's ×1.56: the input describes structure, or the projection pinned more
readings. SAS is an RFP, like BMS, and unlike a recollection it names no architecture — yet it
agrees like FaxRxTx. What it shares with FaxRxTx and not with BMS is a **dense projection**: P3 fixes
twenty-seven readings against BMS's six, and pre-names the one partition that could have doubled the
tree (the P-/L- twins). The twin reading is the measurable part: both runs built one shared record
core and per-kind residues, 37 against 33 shared nodes, and the Location module came out small in
both. Without P3 that partition was free and could have gone either way in each run.

This moves the weight from "the document" to "the projection", without settling it: n = 1 case per
condition. *Overturned by:* an SAS pair run with P3's twin row removed that reproduces BMS's spread —
which would settle it for the projection; or a BMS rerun under a P5 as dense as this one that stays
at ×1.56 — which would send it back to the document.

**What the two models disagree about** is, as before, grouping rather than content: J = 0.45 on
co-location with equal pair counts means the two runs put the same 146 obligations into groups of the
same size and drew the group boundaries differently in about half the places. The largest visible
differences: OA2 declares I-8 and D-7 as own residue on the Access Data aggregate (the only
aggregate-held coverage in either model, the same move run 29's OA2 made with F47); OA1 keeps the
identifier rules of I-3 as three nodes where OA2 folds them into the assignment engine; OA2 covers
I-1 with seventeen nodes, OA1 with far fewer. The lost accretion logs would have shown *where* each
reading was taken; §7c shows only that both close.

---

## 5. The model carried forward

**`HM44-OA1` — 246 nodes after normalisation, 187 leaves — is crossed with the declared technology in
the next step.** Chosen as the first of the pair, the rule BMS and FaxRxTx used, and not on any
property of the model.

`HM44-OA2` stands as the **declared structural sensitivity** of everything downstream: 242 nodes
against 246, a different grouping in half the places, and the differences named in §4. On FaxRxTx the
same sensitivity was later crossed and priced (run 42) at ×1.053 end to end; whether SAS's pair
behaves the same is the repeatability measurement this case owes, and it is cheaper here than it was
there because the two models are closer in size.
