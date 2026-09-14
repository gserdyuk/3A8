# Run 53 — the SAS product model through the plugin entry point, `Hotyn-M 1.1`, n = 2

**2026-09-15.** Stage 1 of a regression run of `/3a8:estimate-product` against runs 44–47: step 1 only, stopped
there. One cell, the cell of run 44: **Opus 5 × order A × n = 2**, on md5-identical inputs. The variable is the entry
point: the plugin subagent `3a8:model-builder`, launched from the plugin skill, where run 44 used the repository agent
before packaging.

Raw: `run53_raw/HM53-1.md`, `run53_raw/HM53-2.md`. Launch record, prompt composition, pins and every deviation from
run 44: `run53_raw/MANIFEST.md`. Inputs: `requirements_product.md` (md5 `db9fdc8ff77844f0b9bbb3881d292587`,
N = 146) + `assumptions_product.md` v1 (md5 `2540cfb1fca7a90a9f9c5cfb937718f1`), both pasted whole into each prompt,
with order A declared and the standing quarantine paragraph. No file was read by either sensor; `tool_uses: 0` in
both. Both printed the stamp `Hotyn-M 1.1`. The pre-launch manifest probe agreed with the on-disk stamps (the check
script itself was refused and its comparison was done by hand, see the manifest). The model half of the stamp is
the orchestrator's record: both were launched with the harness's `opus` alias, and both transcripts record
`claude-opus-5` on every turn.

The readings below were computed by the run 44 comparison method (section 6 parsed, co-location pairs, Jaccard). A
scratchpad copy of `run44_raw/compare_run44.py` was generalised to read column positions from the table header,
because run 53's §6 calls the provenance column `origin`. Before use, it was run on run 44's two raw files and
reproduced run 44's figures exactly (246 / 242 nodes, 257 / 279 assignments, 155 / 154 pairs, J = 0.451). The script
is not among the run's files.

---

## 1. Protocol facts first

**Both models are complete.** HM53-1's reply reached the orchestrator whole. HM53-2's reached it truncated at the
head, beginning inside §5, which is the transit failure of run 29 §6 and run 44 §1. This time it was recoverable for
both members: the harness's per-agent transcript (`subagents/agent-<id>.jsonl`) held every text block the sensor
emitted. Both raw files were extracted from it by script, verbatim. The task output files were empty, as run 44's OA1
file was. Every section from §1 to §9 is present in both files, including the two accretion logs run 44 lost for OA1.

**Both sensors hit the output limit and were resumed by the harness.** Each agent's first turn was thinking only and
stopped at 64 000 output tokens. HM53-2 stopped a second time partway through its reply text. After each stop the
harness injected a meta message into the sensor's context ("Output token limit hit. Resume directly — … Break
remaining work into smaller pieces."). It carries no case material and no estimate, so it is not contamination in the
matrix's sense. It is still a text the prompt did not contain, reaching the sensor mid-run. It is deviation 9 in the
manifest. Whether run 44's sensors met the same limit is unknown: run 44's transcripts were not audited this way.

**Confound.** Run 44's prompt text was not kept, so run 53's framing was rebuilt from run 44's record (manifest,
deviation 2). The inputs are byte-identical after CR stripping; the framing wording is not verifiable. The entry
point, the rebuilt framing and the output-limit continuations all moved together. This run cannot attribute the
difference below to any one of them.

---

## 2. The readings, beside run 44's

| reading | HM53-1 | HM53-2 | ratio | run 44 OA1 | run 44 OA2 | run 44 ratio |
|---|---:|---:|---|---:|---:|---|
| skeleton (posited) | 64 | 74 | ×1.16 | 72 | 69 | ×1.04 |
| accretion (accreted) | 43 | 64 | ×1.49 | 160 | 167 | ×1.04 |
| **anchored (posited + accreted)** | **107** | **138** | **×1.29** | **232** | **236** | **×1.017** |
| completion (derived) | 10 | 12 | ×1.20 | 27 | 20 | ×1.35 |
| nodes before normalisation | 117 | 150 | ×1.28 | 259 | 256 | ×1.012 |
| **nodes after normalisation** | **117** | **150** | **×1.28** | **246** | **242** | **×1.017** |
| nodes collapsed at closure | 0 | 0 | — | 13 | 14 | — |
| leaves after normalisation | 103 | 133 | ×1.29 | 187 | 187 | ×1.00 |
| coverage assignments (requirement, node) | 239 | 281 | ×1.18 | 257 | 279 | ×1.086 |
| nodes per requirement, mean | 1.64 | 1.92 | ×1.18 | 1.76 | 1.91 | ×1.09 |
| co-located requirement pairs | 347 | 359 | ×1.035 | 155 | 154 | ×1.006 |
| nodes covering both a `P-` and an `L-` id | 26 | 33 | ×1.27 | 37 | 33 | ×1.12 |
| skeleton nodes ending with empty **total** coverage | 0 of 64 | 0 of 74 | — | 0 of 72 | 0 of 69 | — |
| accretion verdicts, pass 1: covered / partial / not covered / deferred | 112 / 17 / 17 / 0 | 89 / 44 / 11 / 2 | — | 23 / 18 / 105 / 0 (OA1 §8) | *not tabulated* | — |
| ambiguity flags | 13 | 12 | — | 17 | 25 | — |
| partial marks standing at closure | 0 | 0 | — | 0 | 0 | — |
| completion-covers-a-requirement defects | 0 | 0 | — | 0 | 0 | — |
| **obligations placed / unplaced** | **146 / 0** | **146 / 0** | — | 146 / 0 | 146 / 0 | — |
| residue defect reports (§7c) | 0 | 1 (NFR-5) | — | 0 | 0 | — |
| requirements covered, checked from §6 by script | 146 of 146 | 146 of 146 | — | 146 of 146 | 146 of 146 | — |

Provenance counts are the sensors' own, taken before normalisation; with no collapse in either run 53 member, the
script's §6 counts equal them exactly. Run 44's OA2 reported no pass-1 verdict totals in §8.

**Jaccard of the co-location relations, HM53-1 vs HM53-2: 256 shared pairs, 450 in the union → 0.569.**
Run 44: 96 / 213 → 0.451.

Across the two runs, member against member: HM53-1 vs OA1 0.252 · HM53-1 vs OA2 0.325 · HM53-2 vs OA1 0.360 ·
HM53-2 vs OA2 0.343. Every cross-run pair is lower than either run's own pair.

**Run 53 against run 44, by level.** Anchored: mean 122.5 against 234, **×0.52**. Nodes after normalisation: 133.5
against 244, ×0.55. Coverage assignments: 260 against 268, ×0.97. The obligations were placed about as many times as
in run 44, onto about half as many nodes. Co-located pairs are more than twice as many (353 against 154.5), so the
groups are coarser.

The NFR-5 residue in HM53-2 is the commercial clause "by the project core team at no cost to X-Customer". HM53-2
reports it as a work/contract obligation in the product list that no node can realise. HM53-1 flags the same clause in
§9 and still marks NFR-5 whole. The two members disagree on one verdict; they do not disagree on placement.

---

## 3. Scoring run 19's predictions: run 53 beside run 44

| # | prediction | BMS run 19 | FaxRxTx run 29 | SAS run 44 | **SAS run 53 (plugin)** |
|---|---|---|---|---|---|
| 1 | executability: all nine sections, a parent for every node | held | held in content, broken in transit | held in content, broken in transit — both members | **held in content; HM53-2 broken in transit, recovered whole from the per-agent transcript** |
| 2 | anchored total agrees within ±5% | REFUTED, ×1.56 | CONFIRMED, ×1.024 | CONFIRMED, ×1.017 | **REFUTED, ×1.29** |
| 3 | derived spread exceeds anchored spread | REFUTED and inverted | CONFIRMED, ×1.40 > ×1.024 | CONFIRMED, ×1.35 > ×1.017 | **REFUTED and inverted, ×1.20 < ×1.29** |
| 4 | relations within ×2 in size **and** Jaccard above 0.5 | SPLIT: ×1.07, J = 0.308 | SPLIT: ×1.14, J = 0.406 | SPLIT: ×1.006, J = 0.451 | **CONFIRMED: ×1.035, J = 0.569** |
| 6 | fewer than 20% of skeleton nodes end with empty total coverage | not scoreable | CONFIRMED: 0% and 7.7% | CONFIRMED: 0% and 0% | **CONFIRMED: 0% and 0%** |

On the same case and inputs, run 53 scores 2 and 3 as BMS did, not as run 44 did. Prediction 4 is confirmed for the
first time. The Jaccard is not comparable at face value, though: run 53's relation has more than twice as many pairs
(coarse groups make many pairs), and a larger relation built from the same 146 ids overlaps more easily.

---

## 4. The reading, and what would overturn it

**R7 — Through the plugin entry point, on byte-identical inputs, `Hotyn-M 1.1` builds about half of run 44's anchored
structure (×0.52) and its repeat spread rises from ×1.017 to ×1.29. Run 44 R6 does not reproduce: a dense projection
did not by itself hold SAS's structure size to FaxRxTx's figure.**

**Where the difference sits** can be read from the accretion logs, which this run has for both members. The skeleton
is the same size as run 44's (64 and 74 against 72 and 69). The difference is in accretion (43 and 64 against 160 and
167), and it follows from the verdict run 44 §4 named as this engine's remaining freedom. Run 53's sensors gave
`covered` whenever an already-posited leaf's intended scope realised a requirement: 112 and 89 pass-1 verdicts,
against 23 in run 44 OA1, where 105 requirements were `not covered` and grew their own accreted leaf. Both sensors
state the reading themselves: HM53-1 §9, "Posited leaves count as existing structure"; HM53-2 §9, "Covered verdicts
on posited leaves … A finer or coarser skeleton would move requirements between covered and not covered." Run 53's
skeletons are made of leaves that take coverage; run 44's were aggregates that accretion filled. The number of times
obligations were placed barely moved (×0.97). What moved is how many distinct nodes they were placed on.

**Why the spread rose** follows from the same verdict. Once structure size is decided by how far each skeleton leaf is
read to reach, two sensors that draw slightly different skeletons (64 against 74) diverge further in accretion
(43 against 64). Run 44's sensors accreted almost one node per requirement whatever the skeleton, which pinned the
anchored total to the list.

**What this run cannot say** is which of the three co-moving changes produced the reading (§1): the entry point, the
rebuilt framing, or the output-limit continuations mid-run. The continuation instruction "break remaining work into
smaller pieces" arrived after the thinking turn had already run to the limit. The skeleton and the verdict policy were
probably fixed in that turn, but the transcript records no thinking content to check it (the thinking blocks are
empty in the transcript).

*Overturned by:* a run 44-framing replay. That is an n = 2 run through the plugin entry point with run 45's prompt
generator conventions and an output budget that does not trip the continuation. If it returns anchored ≈ 232 at
×1.02, the plugin entry point is cleared and the difference goes to the framing or the continuation. If it returns
≈ 120 again, the entry point, or the model behind the alias on this date, is the cause. A cheaper first
discriminator: the same prompt launched through the repository agent path, if it can still be registered alongside the
plugin.

**Consequence for the regression.** Step 1 through the plugin does **not** reproduce run 44 within the repeat spread
either run measured. The structure handed to step 2 would be about half the size. Downstream, run 45 crossed 246
nodes and run 47 priced them; a 117- or 150-node model will cross and price differently, and by more than run 44's
declared structural sensitivity (×1.017). This is recorded as a finding of stage 1, not corrected here.

---

## 5. The model carried forward

By the rule BMS, FaxRxTx and run 44 used (the first of the pair, on no property of the model), **`HM53-1` —
117 nodes, 103 leaves** — is the model stage 2 would cross. `HM53-2` (150 nodes, 133 leaves, J = 0.569 against
HM53-1) stands as the declared structural sensitivity, now ×1.28 on nodes rather than run 44's ×1.017.

Whether stage 2 should proceed on this pair, or wait for the discriminating relaunch of §4, is a decision for the
stage 2 launch. This record does not take it.
