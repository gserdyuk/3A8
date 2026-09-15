# Run 55 — the SAS product model under `Hotyn-M 2.0`, smoke test, n = 1

**2026-09-15.** The re-baseline of `Hotyn-M 2.0` on the SAS cell, **Opus 5 × order A**, step 1 only, stopped there.
The inputs are md5-identical to runs 44 and 53. The prompt is run 53's, byte for byte. The variable is the engine: 2.0
declares coverage at leaves only (M2), so a posited thing is a node, and `covered` can name leaves only (M5).

Raw: `run55_raw/HM55-1.md`. Launch record, prompt, pins, per-turn audit and every deviation from run 53:
`run55_raw/MANIFEST.md`. `tool_uses: 0`. The sensor printed the stamp `Hotyn-M 2.0`. The pre-launch probe and
`tools/check_probe.py` agreed: 11 agents, 0 failing. The model half of the stamp is the orchestrator's record: launched
with the harness's `opus` alias; the transcript records `claude-opus-5`.

The readings below were computed by script (`compare55.py`, extending run 53's comparison script). Before use, it
reproduced run 44's and run 53's recorded figures exactly. Because 2.0 nodes carry no coverage, co-location is taken on
**leaves' coverage sets**. For every run 44 and run 53 member that relation equals the all-rows relation run 53 used,
except OA2, where it is 153 pairs against 154.

---

## 1. Protocol facts first

**Smoke test failed; n = 1.** HM55-1's first turn stopped at `max_tokens` (64 000 output tokens), and the harness
injected its continuation message once ("… Break remaining work into smaller pieces."). By the launch protocol, HM55-2
was not launched. There is no repeat spread, no within-run Jaccard, and none of run 19's pairwise predictions can be
scored.

**Where the continuation fell.** Unlike runs 53 and 54, the first turn did not end thinking-only. After about 11 min 48 s
of thinking, the sensor began its reply and wrote the title, §1 and the whole skeleton (§2, 27 nodes) before the limit
cut it inside §3's first table header. **Every accretion verdict, the completion, the closure and the readings were
written after the continuation message.** 2.0's M3 ("the phases are written, not planned") shows here only as text
appearing inside turn 1. It did not keep the first turn under the output limit.

**The model is complete.** The reply reached the orchestrator truncated at the head (from §3), and was recovered whole
from the per-agent transcript. Two text blocks were joined verbatim; the seam is inside §3's pass-1 header row and loses
nothing. §6's counts, parsed by script, equal the sensor's own §8.

**Confound.** The continuation is present in both run 53 and run 55, so it is not the variable between them. It still
reached this sensor at a different point: before accretion, where run 53's came before any text. And no run 44
transcript was audited for it.

---

## 2. The readings, beside run 53's and run 44's

2.0 counts provenance "before closure" and separates leaves from nodes. The 1.1 records counted every row as a "node"
and "normalised" them. The table puts both on one footing: **rows** = leaves + internal nodes.

| reading | **HM55-1 (2.0)** | HM53-1 | HM53-2 | run 44 OA1 | run 44 OA2 |
|---|---:|---:|---:|---:|---:|
| posited (skeleton), before closure | **27** | 64 | 74 | 72 | 69 |
| accreted | **112** | 43 | 64 | 160 | 167 |
| **anchored (posited + accreted)** | **139** | **107** | **138** | **232** | **236** |
| derived (completion) | **15** | 10 | 12 | 27 | 20 |
| rows before closure | **154** | 117 | 150 | 259 | 256 |
| **rows after closure** | **154** | **117** | **150** | **246** | **242** |
| leaves before / after closure | **127 / 127** | 103 / 103 | 133 / 133 | — / 187 | — / 187 |
| internal nodes before / after closure | **27 / 27** | 14 / 14 | 17 / 17 | — / 59 | — / 55 |
| posited things that ended as leaves | **0** | 50 | 57 | 0 | 0 |
| anchored leaves (posited leaves + accreted) | **112** | 93 | 121 | 160 | 167 |
| nodes deleted childless | **0** | 0 collapsed | 0 collapsed | 13 collapsed | 14 collapsed |
| nodes deleted by lifting | **0** | (1.1 did not separate) | | | |
| internal nodes carrying coverage | **0** | 0 | 0 | 0 | 1 |
| coverage assignments on leaves | **283** | 239 | 281 | 257 | 277 |
| leaf assignments per requirement | **1.94** | 1.64 | 1.92 | 1.76 | 1.90 |
| co-located requirement pairs (leaves) | **494** | 347 | 359 | 155 | 153 |
| leaves covering both a `P-` and an `L-` id | **30** | 26 | 33 | 37 | 33 |
| accretion verdicts, pass 1: covered / partial / not covered / deferred | **33 / 71 / 40 / 2** | 112 / 17 / 17 / 0 | 89 / 44 / 11 / 2 | 23 / 18 / 105 / 0 | *not tabulated* |
| **leaves added per row that added** | **1.00** (112 / 112) | 1.26 (43 / 34) | ≈ 1.12–1.16 | 1.30 (160 / 123) | — |
| ambiguity flags | **11** | 13 | 12 | 17 | 25 |
| partial marks standing at closure | **0** | 0 | 0 | 0 | 0 |
| completion leaves covering a requirement | **0** | 0 | 0 | 0 | 0 |
| **obligations placed / unplaced** | **146 / 0** | 146 / 0 | 146 / 0 | 146 / 0 | 146 / 0 |
| residues (§7c) | **0 — 146 of 146 whole** | 0 | 1 (NFR-5) | 0 | 0 |
| requirements covered by leaves, checked from §6 by script | **146 of 146** | 146 of 146 | 146 of 146 | 146 of 146 | 146 of 146 |
| first turn stop · continuations | **`max_tokens` · 1** | `max_tokens` · 1 | `max_tokens` · 2 | not audited | not audited |

The HM55-1 provenance counts are the sensor's own (§8). With 0 deletions and 0 lifts, the §6 counts equal them
exactly. HM55-1's pass 2 retried the two deferrals, I-1 (covered) and I-8 (partial, adding A112). In "leaves added per
row that added", HM53-2's denominator is 55 or 57, depending on its two deferrals, which run 53's record does not
resolve.

**Log checks (by script, HM55-1).**
- No covering column in §3 names a node.
- Every row that added anything added **exactly one** id: 40 not-covered rows and 72 partial rows, 112 leaves.
- No two leaves in §6 have the same coverage set.
- All 27 posited nodes have at least two children, so closure had nothing to delete or lift. 2.0's deletion path was
  not exercised by this reading.
- All §2 scopes are at most eight words.
- Derived leaves carry `trigger:<id>` and no requirement id.

**Level against the two earlier runs.** Anchored 139 is ×1.13 on run 53's mean (122.5) and ×0.59 on run 44's (234).
The other size readings point the same way:
- leaves 127: ×1.08 on run 53's mean (118), ×0.68 on run 44's (187);
- rows after closure 154: ×1.15 / ×0.63;
- anchored leaves 112: ×1.05 / ×0.68.

Coverage assignments barely move: 283 against 260 and 267. As in run 53, the obligations are placed about as often
onto far fewer leaves than run 44. The groups are coarser than in either run: 494 co-located pairs, against 353 and 154.

**Jaccard of the leaf co-location relations.** No within-run pair exists (n = 1).

| HM55-1 vs | shared / union | J | ceiling on J from the two sizes | shared / smaller relation |
|---|---|---:|---:|---:|
| HM53-1 | 248 / 593 | 0.418 | 0.702 | 0.715 |
| HM53-2 | 273 / 580 | 0.471 | 0.727 | 0.760 |
| run 44 OA1 | 133 / 516 | 0.258 | 0.314 | 0.858 |
| run 44 OA2 | 111 / 536 | 0.207 | 0.310 | 0.725 |

For reference, the within-run pairs on the same relation: run 53, 0.569 (256 / 450); run 44, 0.453 (96 / 212).

The J values are not comparable at face value. HM55-1's relation is 3.2 times the size of run 44's, which caps J
against OA1 and OA2 at about 0.31. The last column is the share of the smaller relation contained in HM55-1's. Read that
way, HM55-1 contains most of every earlier relation (0.72–0.86) — including 86% of OA1's, more than of either run 53
member's. Its groups are unions of theirs, not a different partition.

---

## 3. Whether the 2.0 output format was followed

| requirement of the 2.0 *Output format* | HM55-1 |
|---|---|
| sections in the order the phases run: 1, 2, 3, 4, 5, 6, 7, 7c, 8, 9 | **followed**: headings in exactly that order, §3 with `Pass 1 (order A)`, `Pass 2`, `Pass 3` |
| each section closed by one terminator line carrying its counts | **followed**, 12 terminators: §1, §2, one per §3 pass, §4, §5, §6, §7, §7c, §8, §9. `-- end §8 --` and `-- end §9 --` carry no counts (§8 is itself the counts) |
| §2: id · parent · name · intended scope ≤ 8 words; nothing attached | **followed**; every scope ≤ 8 words; terminator `27 nodes posited · 0 requirements attached` |
| §3: one table per pass, row = id · verdict · covering leaf id(s) · id(s) added · missing · reason · ambiguity · whole/residue | **followed** for passes 1 and 2 (8 columns in that order; partial rows name the part in parentheses). Pass 3 has no rows and is written as one sentence plus its terminator. The pass-1 header row is broken by the transit seam, not by the sensor |
| §4: id · trigger · justification · pass | **followed**; 15 derived leaves, 0 derived nodes |
| §5 convergence trace reaching zero | **followed**, including a closure-normalisation row |
| **§6 as one fenced TSV block**, `id · parent · origin · coverage set · name`, node coverage empty, no sub-headings or prose | **followed**: one ` ```tsv ` block, 155 lines (header + 154 rows), every line 5 tab-separated fields, no text in the section outside the fence except the terminator. One addition the format does not define: derived leaves carry `trigger:<id>` in the coverage column, a choice the sensor declares in §9 |
| **§7 closure log**: every deletion and lift, in order | **present**. There were 0 deletions and 0 lifts, so there are no `deleted …` / `lifted …` lines. The section is written as four bullets (declare, completeness, one normalisation pass, freeze) |
| §7c: "N of N whole", then residue rows | **followed**: `146 of 146 whole` |
| §8: engine stamp verbatim, then the eight counts only | **followed**: `Engine: Hotyn-M 2.0`; eight counts; no coverage assignments or per-leaf ratios computed |
| §9: unplaced; ambiguous ids with reasons ≤ 10 words, no quotation; interpretations | **followed**: none unplaced; 11 flag rows (= §8's count); interpretations listed |

---

## 4. The reading, against the registered outcomes, and what would overturn it

**Registered before launch:** anchored ≈ 232 at ≈ ×1.02 means the run 53 mechanism was the covered-by-posited-leaf
verdict and 2.0 removed it; ≈ 120 again means it was not.

**R8 — By the registered rule, HM55-1 falls on the ≈ 120 side: anchored 139, ×1.13 on run 53 and ×0.59 on run 44,
and every other size reading agrees. The spread half of the rule (≈ ×1.02) cannot be read at n = 1. The inference
registered for this side, "the covered verdict was not the mechanism", holds only in part.** The log shows the verdict
did move the way that mechanism predicted, and a different constraint held the level.

**The verdict moved.** Under 2.0, no posited thing is a leaf (0 of 27) and no covering column names a node. Pass-1
`covered` fell to 33, against 112 and 89 in run 53, and close to run 44 OA1's 23. On run 53's account (run 53 §4),
that should have sent about 110 requirements into accretion and brought the structure back toward run 44's size.
It sent 112 rows into additions, and they added 112 leaves.

**What held the level: one leaf per addition.** Every row that added anything added exactly one leaf (1.00). Run 44
OA1 added 1.30 per such row, and run 53's members 1.26 and about 1.1–1.2. The sensor names the rule it applied (§9):
leaf identity is the coverage set (M2), so the parts of a requirement that no other requirement shares go into one
leaf. Its own examples:
- A038 holds all six format adapters and the API exchange;
- A101 holds availability, failover and failover monitoring.

No two leaves in §6 share a coverage set. Read this way, 2.0's identity axiom ("two leaves are the same leaf when they
cover the same set") bounds the accreted count by the number of rows that add. The anchored level becomes roughly
N − covered, plus the skeleton's nodes. Run 44's 1.30 leaves per addition, the grain that made its 232, is out of reach.

**Where the obligations went.** Partial verdicts (71 in pass 1, against 17 / 44 in run 53 and 18 in run 44 OA1)
leave the partial id on the earlier leaf as well as on the new one. Coverage piles onto a few broad leaves: A037
carries 16 ids, A027 and A069 11 each, A042 9. Hence 283 leaf assignments and 494 co-located pairs, the coarsest SAS
relation so far.

**So the freedom moved.** In run 53 it sat in `covered` on posited leaves. In HM55-1 it sits in how finely one
requirement's missing part may be split into leaves. The sensor settled that by reading M2's identity sentence
literally. This is a reading of one sensor, not yet a property of the engine.

**What this run cannot say.**
- **n = 1:** no spread, so run 44's ×1.017 and run 53's ×1.29 have no counterpart here.
- **The continuation:** every accretion verdict was written after the injected "Break remaining work into smaller
  pieces". The continuation alone does not produce one leaf per addition: run 53's sensors received the same message
  and split 1.1–1.26. But run 53's arrived before any text, and this one arrived between the skeleton and accretion.
- **Where the grain was fixed:** the thinking content is empty in the transcript, so the ≈ 64 000 tokens of turn 1
  cannot be read for it.

*Overturned by:*
- **HM55-2, or any 2.0 relaunch of this cell, whose rows add more than one leaf per requirement** (distinct coverage
  sets, or leaves the sensor treats as distinct despite equal sets) **and whose anchored level returns toward 232.**
  That would make the one-leaf grain a trait of this reading, not of the axiom.
- **A 2.0 reading whose first turn ends `end_turn`** (no continuation) at anchored ≈ 232. That would put the grain on
  the continuation.
- **Another 2.0 reading at 1.00 leaves per addition and anchored ≈ 120–140.** That would confirm R8 at n = 2 and make
  the identity sentence of M2 the next thing to decide: whether a requirement's parts may be separate leaves with the
  same singleton coverage. Deciding it is an engine revision; this record does not propose one.

---

## 5. The model carried forward

None is designated. The rule BMS, FaxRxTx and run 44 used (the first of a pair) presumes a pair. HM55-1 — **154 rows,
127 leaves, 27 nodes** — is the only 2.0 reading of SAS. It was produced with a continuation message mid-run and has
no declared structural sensitivity. The skill asks for n = 2 per step. Whether step 2 should wait for HM55-2, or for a
launch that clears the output limit, is a decision for the step-2 launch. This record does not take it.

- **Copied into place** 2026-09-15 from the child session scratchpad by the orchestrating session, byte for byte.
