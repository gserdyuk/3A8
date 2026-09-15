# Run 56 — the SAS product model under `Hotyn-M 2.0`, the harness lever, n = 2

**2026-09-15.** Run 55 repeated with the per-turn output cap raised: **Opus 5 × order A**, step 1 only, stopped there.
The inputs are md5-identical to runs 44, 53 and 55. The prompt is run 55's, byte for byte. The engine is the `Hotyn-M
2.0` on disk. The variable is the harness: the orchestrating process runs with `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`.

Raw: `run56_raw/HM56-1.md`, `run56_raw/HM56-2.md`. Launch record, prompt, pins, per-turn audit and every deviation from
run 55: `run56_raw/MANIFEST.md`. `tool_uses: 0` in both. Both sensors printed the stamp `Hotyn-M 2.0`. The pre-launch
probe and `tools/check_probe.py` agreed: 11 agents, 0 failing. The model half of the stamp is the orchestrator's
record: launched with the harness's `opus` alias; the transcripts record `claude-opus-5`.

The readings below were computed by script. `compare56.py` runs run 55's `compare55.py` unchanged and adds the J
ceiling and the containment column. `logcheck56.py` generalises run 55's log checks. Before use, both reproduced run
55's recorded figures exactly. Co-location is taken on **leaves' coverage sets**, as in run 55.

---

## 1. Protocol facts first

**The variable reaches subagents. Registered outcome (a); n = 2.** HM56-1's only turn ended `end_turn` at **79 883**
output tokens, and no continuation message was injected. By the rule, HM56-2 was launched the same way. It also ended
`end_turn` in one turn, at **92 565**, with no continuation. Both turns exceed the 64 000 cap that cut every audited
turn 1 in runs 53–55. Run 56 is the first pair of SAS product models written without a continuation message.

**Total output did not change with the cap.** HM55-1 wrote 78 592 output tokens (64 000 + 14 592) across the
continuation. HM56-1 wrote 79 883 in one turn. The thinking phases were of similar length: 11 min 48 s (HM55-1),
11 min 36 s (HM56-1), 14 min 23 s (HM56-2).

**Both models are complete.** Each reply is one text block, from the title to §9, and each reached the orchestrator
whole. The raw files were taken from the per-agent transcripts, with no seam. §6 counts parsed by script equal each
sensor's own §8.

---

## 2. The readings, beside runs 55, 53 and 44

**Rows** = leaves + internal nodes, as in run 55's table.

| reading | **HM56-1** | **HM56-2** | HM55-1 | HM53-1 | HM53-2 | run 44 OA1 | run 44 OA2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| posited (skeleton), before closure | **28** | **28** | 27 | 64 | 74 | 72 | 69 |
| accreted | **154** | **117** | 112 | 43 | 64 | 160 | 167 |
| **anchored (posited + accreted)** | **182** | **145** | **139** | **107** | **138** | **232** | **236** |
| derived (completion) | **16** (15 leaves, 1 node) | **13** (12 leaves, 1 node) | 15 | 10 | 12 | 27 | 20 |
| rows before closure | **198** | **158** | 154 | 117 | 150 | 259 | 256 |
| **rows after closure** | **198** | **156** | **154** | **117** | **150** | **246** | **242** |
| leaves before / after closure | **169 / 169** | **129 / 129** | 127 / 127 | 103 / 103 | 133 / 133 | — / 187 | — / 187 |
| internal nodes before / after closure | **29 / 29** | **29 / 27** | 27 / 27 | 14 / 14 | 17 / 17 | — / 59 | — / 55 |
| posited things that ended as leaves | **0** | **0** | 0 | 50 | 57 | 0 | 0 |
| anchored leaves (posited leaves + accreted) | **154** | **117** | 112 | 93 | 121 | 160 | 167 |
| nodes deleted childless | **0** | **0** | 0 | 0 collapsed | 0 collapsed | 13 collapsed | 14 collapsed |
| nodes deleted by lifting | **0** | **2** (N06, N23) | 0 | (1.1 did not separate) | | | |
| internal nodes carrying coverage | **0** | **0** | 0 | 0 | 0 | 0 | 1 |
| coverage assignments on leaves | **314** | **245** | 283 | 239 | 281 | 257 | 277 |
| leaf assignments per requirement | **2.15** | **1.68** | 1.94 | 1.64 | 1.92 | 1.76 | 1.90 |
| co-located requirement pairs (leaves) | **292** | **294** | 494 | 347 | 359 | 155 | 153 |
| leaves covering both a `P-` and an `L-` id | **41** | **30** | 30 | 26 | 33 | 37 | 33 |
| accretion verdicts, pass 1: covered / partial / not covered / deferred | **33 / 51 / 60 / 2** | **41 / 44 / 61 / 0** | 33 / 71 / 40 / 2 | 112 / 17 / 17 / 0 | 89 / 44 / 11 / 2 | 23 / 18 / 105 / 0 | *not tabulated* |
| rows that added | **111** | **105** | 112 | 34 | 55 or 57 | 123 | — |
| **leaves added per row that added** | **1.39** (154 / 111) | **1.11** (117 / 105) | 1.00 (112 / 112) | 1.26 (43 / 34) | ≈ 1.12–1.16 | 1.30 (160 / 123) | — |
| rows adding more than one leaf | **26** | **7** | 0 | | | | |
| accreted leaves sharing a coverage set: groups / leaves | **15 / 39** | **0 / 0** | 0 / 0 | not checked | not checked | not checked | not checked |
| ambiguity flags | **18** | **19** | 11 | 13 | 12 | 17 | 25 |
| partial marks standing at closure | **0** | **0** | 0 | 0 | 0 | 0 | 0 |
| completion leaves covering a requirement | **0** | **0** | 0 | 0 | 0 | 0 | 0 |
| **obligations placed / unplaced** | **146 / 0** | **146 / 0** | 146 / 0 | 146 / 0 | 146 / 0 | 146 / 0 | 146 / 0 |
| residues (§7c) | **1 (NFR-5)** | **1 (NFR-5)** | 0 | 0 | 1 (NFR-5) | 0 | 0 |
| requirements covered by leaves, checked from §6 by script | **146 of 146** | **146 of 146** | 146 of 146 | 146 of 146 | 146 of 146 | 146 of 146 | 146 of 146 |
| **turns · first turn stop · output tokens · continuations** | **1 · `end_turn` · 79 883 · 0** | **1 · `end_turn` · 92 565 · 0** | 2 · `max_tokens` · 64 000 · 1 | 2 · `max_tokens` · 64 000 · 1 | 3 · `max_tokens` · 64 000 · 2 | not audited | not audited |

The provenance counts are each sensor's own (§8). HM56-2's two lifts removed two posited nodes at closure. Its §6
therefore shows 26 posited rows against 28 before closure. Both residues are NFR-5's "at no cost to X-Customer", which
each sensor reports as a commercial term on the work that was left in the product list.

**Log checks (by script).**
- No covering column in §3 names a node (both).
- No node carries coverage. Derived leaves carry no requirement id (both).
- All §2 scopes are at most eight words (both).
- HM56-1's 15 groups of leaves with identical sets include:
  - the six format adapters A050–A055 (each `D-5, G-12.1, G-12.2, L-15, P-19`);
  - the four NFR-8 leaves A139–A142;
  - the four NFR-2 leaves A126–A129;
  - A070–A072 (`P-1, L-1`).
- HM56-2 has no two accreted leaves with the same set.
- The largest leaf sets: A035 with 10 ids (HM56-1) and A045 with 10 ids (HM56-2). In HM55-1 it was A037 with 16.

**The pair's spread.** Anchored ×1.26 (182 / 145), leaves ×1.31, rows after closure ×1.27. For comparison: run 44
×1.017, run 53 ×1.29.

**Level against the earlier runs.** The pair's mean anchored level is 163.5:
- ×1.18 on run 55 (139);
- ×1.33 on run 53's mean (122.5);
- ×0.70 on run 44's mean (234).

Members: HM56-1 is ×1.31 on run 55 and ×0.78 on run 44's mean; HM56-2 is ×1.04 and ×0.62. On leaves (mean 149) the
same ratios are ×1.17, ×1.26 and ×0.80. HM56-1's accreted count, 154, is ×0.96 of run 44 OA1's 160. Its gap to
run 44 on anchored is mostly the skeleton: 28 posited against 72.

**Where the pair's spread sits.** The two relations are the same size (292 and 294 pairs), yet the models differ by
37 anchored rows. Identical coverage sets add rows but no pairs. HM56-1 holds 39 accreted leaves in 15 groups of
identical sets, which is 24 leaves beyond one per set. On distinct accreted sets, the pair is 130 against 117 (×1.11).
Two thirds of the anchored spread is same-set splitting.

**Jaccard of the leaf co-location relations.**

| pair | shared / union | J | ceiling on J from the two sizes | shared / smaller relation |
|---|---|---:|---:|---:|
| **HM56-1 vs HM56-2 (within run)** | **219 / 367** | **0.597** | 0.993 | 0.750 |
| HM56-1 vs HM55-1 | 249 / 537 | 0.464 | 0.591 | 0.853 |
| HM56-2 vs HM55-1 | 252 / 536 | 0.470 | 0.595 | 0.857 |
| HM56-1 vs HM53-1 | 196 / 443 | 0.442 | 0.841 | 0.671 |
| HM56-2 vs HM53-1 | 202 / 439 | 0.460 | 0.847 | 0.687 |
| HM56-1 vs HM53-2 | 199 / 452 | 0.440 | 0.813 | 0.682 |
| HM56-2 vs HM53-2 | 239 / 414 | 0.577 | 0.819 | 0.813 |
| HM56-1 vs run 44 OA1 | 94 / 353 | 0.266 | 0.531 | 0.606 |
| HM56-2 vs run 44 OA1 | 106 / 343 | 0.309 | 0.527 | 0.684 |
| HM56-1 vs run 44 OA2 | 104 / 341 | 0.305 | 0.524 | 0.680 |
| HM56-2 vs run 44 OA2 | 113 / 334 | 0.338 | 0.520 | 0.739 |

For reference, the within-run pairs on the same relation: run 53, 0.569 (256 / 450); run 44, 0.453 (96 / 212).

Run 56's within-run J, 0.597, is the highest SAS pair so far. With the two relations the same size (ceiling 0.993), it
reads at face value. Both members contain about 85% of HM55-1's relation in their own (0.853 and 0.857 of the smaller).
HM55-1's 494 pairs are coarser groups over much the same co-location. Against run 44 the ceiling is about 0.52, and
J is 0.27–0.34.

---

## 3. Whether the 2.0 output format was followed

| requirement of the 2.0 *Output format* | HM56-1 | HM56-2 |
|---|---|---|
| sections in the order the phases run: 1, 2, 3, 4, 5, 6, 7, 7c, 8, 9 | **followed**; §3 with `Pass 1`, `Pass 2` | **followed**; §3 with `Pass 1 (order A)`, `Pass 2` |
| each section closed by one terminator line carrying its counts | **partly**: 10 terminators, each wrapped in inline-code backticks (HM55-1's were bare). **§1 has none** | **partly**: 11 terminators, wrapped in backticks; `-- end §1 --` and `-- end §5 --` carry no counts |
| §2: id · parent · name · scope ≤ 8 words; nothing attached | **followed**; `28 nodes posited · 0 requirements attached` | **followed**; the same terminator |
| §3: one table per pass, 8 columns | **followed** | **followed**. NFR-5's last column names its residue |
| §4: id · trigger · justification · pass | **followed**; 16 rows including one derived **node** XN1, whose trigger equals derived leaf X03's | **followed**; 13 rows including one derived **node** CN01 |
| §5 convergence trace reaching zero | **followed**, with a closure-normalisation row | **followed**, without that row |
| **§6 as one fenced TSV block**, `id · parent · origin · coverage set · name` | **followed**: one ` ```tsv ` block, header + 198 rows, 5 fields each. Derived leaves' coverage column is **empty** | **followed**: header + 156 rows, 5 fields each. Derived leaves carry `trigger: <id>` in the coverage column, as HM55-1 did. Ids are separated by `, ` |
| §7 closure log: every deletion and lift, in order | **present**: 0 deletions, 0 lifts | **followed**: `lifted A109 from N06 to N02; deleted N06`, `lifted A088 from N23 to N16; deleted N23` |
| §7c: "N of N whole", then residue rows | **followed**: `145 of 146 whole`, NFR-5 | **followed**: `145 of 146 whole`, NFR-5 |
| §8: engine stamp verbatim, then the eight counts only | **followed**: `Engine: Hotyn-M 2.0` | **followed**: `Engine: Hotyn-M 2.0` |
| §9: unplaced; ambiguous ids with reasons ≤ 10 words; interpretations | **followed**: none unplaced; 18 flag rows (= §8) | **followed**: none unplaced; 19 flag rows (= §8) |

---

## 4. Whether the sensor again read M2's identity rule as a merge rule

M2 in `agents/model-builder.md`: "**Identity.** A leaf's identity is its coverage set (or its trigger); a node's
identity is the union it computes. **Names are labels for readers and are never identity.** Two leaves are the same
leaf when they cover the same set."

HM55-1 read it as a merge rule (run 55 §4): "a leaf is identified by its coverage set, so any parts of a requirement
that no other requirement shares end up in one leaf." Its grain was 1.00 leaves per adding row.

**HM56-1: no.** Its §9 says nothing about identity. Its §6 keeps 39 accreted leaves in 15 groups with identical sets:
six adapters with one set, four NFR-8 leaves, four NFR-2 leaves. That follows the assumption projection's "each format
its own import and export adapter" and departs from M2's identity sentence as written. Grain: 1.39.

**HM56-2: yes, where sets would collide.** Its §9, verbatim:

> 3. **Identity.** In rows that added several leaves at once (I-1, I-8, G-12, G-12.1, G-13.4, P-1, P-11), those
> leaves briefly shared one coverage set. At closure all 129 leaf loads are distinct: coverage sets for accreted
> leaves, trigger sets for derived ones.

> 4. **G-12.2.** Covered by A047, reading P3: PC and Mac are variants inside the adapters. The format set of G-12.1 is
> one adapter leaf, because separate leaves per format would all carry the same coverage.

It split a requirement into several leaves only where later rows made their sets distinct. Where they could not
become distinct (the six formats), it merged them. In doing so it set the axiom above the pinned projection's P3. Grain:
1.11.

**Three readings, three treatments of one sentence, and the grain follows the treatment:**

| reading | treatment of M2 identity | leaves per adding row | rows that added | anchored |
|---|---|---:|---:|---:|
| HM55-1 | merge: one leaf per requirement's unshared part | 1.00 | 112 | 139 |
| HM56-2 | merge only where sets cannot become distinct | 1.11 | 105 | 145 |
| HM56-1 | not applied: equal sets kept as separate leaves | 1.39 | 111 | 182 |

The number of rows that add is nearly constant (105–112). In each reading, anchored ≈ posited + adding rows × grain.
The level varies with the grain, and the grain varies with how the identity sentence is read.

---

## 5. The reading, against the registered outcomes, and what would overturn it

**Registered before launch:** (a) if HM56-1's first turn ends `end_turn` with no continuation, the variable applies to
subagents and the harness factor is removed, and HM56-2 is launched; (b) if it stops at `max_tokens`, it does not.
Either way, HM56-1's anchored count beside run 55's 139 says whether the cap and the injected message moved the level.

**R9 — Outcome (a) holds: `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000` reaches the subagents, and run 56 has no harness
factor. The cap and the injected message did not move the level beyond repeat spread.** HM56-1's 182 is ×1.31 on run
55's 139. HM56-2 ran under the identical harness and reads 145, ×1.04 on run 55. The move from HM55-1 to HM56-1 is the
size of the uncapped pair's own spread (×1.26). It is also accounted for by the sensor's treatment of M2's identity
sentence (§4), which varies between repeats with no continuation in either.

**What this settles from run 55's overturn list.**
- *"HM55-2, or any 2.0 relaunch of this cell, whose rows add more than one leaf per requirement … and whose anchored
  level returns toward 232. That would make the one-leaf grain a trait of this reading, not of the axiom."* **Met by
  HM56-1**:
  - 1.39 leaves per adding row, 24 of them same-set leaves the sensor treats as distinct;
  - anchored 182, which closes 46% of the 139 → 232 gap, and accreted 154 against run 44 OA1's 160.

  **The one-leaf grain was a trait of HM55-1's reading, not of the axiom.**
- *"A 2.0 reading whose first turn ends `end_turn` at anchored ≈ 232. That would put the grain on the continuation."*
  **Not met.** Both readings end `end_turn`, at 182 and 145.
- *"Another 2.0 reading at 1.00 leaves per addition and anchored ≈ 120–140."* **Not met.** The grains are 1.39 and
  1.11. R8's confirmation at n = 2 did not happen.

**Where the freedom sits now.** It sits in M2's identity sentence: whether parts of one requirement that end with the
same coverage set are one leaf or several. The three 2.0 readings take three positions on it, and those positions
carry the level from 139 to 182. Deciding the sentence is an engine revision; this record does not propose one. The
rest of the gap to run 44 is the skeleton (28 posited against 72), not accretion.

*Overturned by:*
- **Further uncapped 2.0 relaunches of this cell (n ≥ 3) all at anchored ≳ 175, next to capped relaunches at ≲ 140.**
  That would make HM56-2 the outlier and put a level shift of about ×1.3 on the continuation message after all.
- **A 2.0 reading that states the merge reading of M2 in §9, keeps no identical sets, and still adds ≳ 1.3 leaves per
  adding row at anchored ≳ 175.** That would decouple the grain from the identity sentence and leave the spread
  unexplained.

**What this run cannot say.**
- Whether run 44's 1.30 grain contained same-set leaves: 1.1 §6 tables were not checked for identical sets.
- Where in the thinking the grain was fixed: the thinking content is empty in both transcripts.

---

## 6. The model carried forward

The first-of-pair rule used for BMS, FaxRxTx and run 44 applies. It gives **HM56-1 — 198 rows, 169 leaves, 29 nodes**.
That is the first SAS 2.0 model produced without a continuation message, from a pair at ×1.26 anchored spread and
within-run J 0.597. HM56-1 is also the reading that departs from M2's identity sentence (§4). Whether step 2 should
wait for that sentence to be decided is a decision for the step-2 launch. This record does not take it.

- **Copied into place** 2026-09-15 from the child session scratchpad by the orchestrating session, byte for byte.
