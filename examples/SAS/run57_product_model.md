# Run 57 — the SAS product model under `Hotyn-M 2.1`, re-baseline, n = 2

**2026-09-15.** Run 56 repeated under the revised engine: **Opus 5 × order A**, step 1 only, stopped there.
The inputs are md5-identical to runs 44, 53, 55 and 56. The prompt is run 56's, byte for byte. The harness is run 56's:
`CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`. The variable is the engine: `Hotyn-M 2.1` changes one sentence of M2. Identity
by coverage set is for comparing models, not for building one. Distinct things that realise the same obligations are
distinct leaves and may share a coverage set, and a count the assumption log fixes stands.

Raw: `run57_raw/HM57-1.md`, `run57_raw/HM57-2.md`. Launch record, prompt, pins, per-turn audit, ambient context and
every deviation from run 56: `run57_raw/MANIFEST.md`. `tool_uses: 0` in both. Both sensors printed the stamp
`Hotyn-M 2.1`; HM57-2 printed it without the word `Engine:`. The pre-launch probe and `tools/check_probe.py` agreed:
11 agents, 0 failing, `model-builder Hotyn-M 2.1`. The model half of the stamp is the orchestrator's record: launched
with the harness's `opus` alias; the transcripts record `claude-opus-5`.

The readings below were computed by script (`analyze57.py`, `logcheck57.py`). Before use, `analyze57.py` reproduced run
56's recorded figures exactly: every count in run 56's table that it computes, and every J, ceiling and containment.
Co-location is taken on **leaves' coverage sets**, as in runs 55–56.

---

## 1. Protocol facts first

**Both turns ended `end_turn`, in one API message each, with no continuation message.**
- HM57-1: **64 004** output tokens.
- HM57-2: **69 987** output tokens.
- "Output token limit hit" occurs 0 times in either transcript. No message reached either sensor after the prompt.
- HM57-1's turn would have been cut by 4 tokens under the old 64 000 cap. Under the raised cap it was not, so run 57 is
  the same harness instrument as run 56 and may be set beside it.

**Output was shorter than run 56's.** Run 57 wrote 64 004 and 69 987 output tokens against run 56's 79 883 and 92 565.
The thinking phases were also shorter: 9 min 13 s and 10 min 08 s against 11 min 36 s and 14 min 23 s. The two sensors
ran concurrently (MANIFEST, deviation 2).

**Both models are complete.** Each reply is one text block, from the title to §9, and each reached the orchestrator
whole. The raw files were taken from the per-agent transcripts, with no seam. §6 parsed by script gives 211 rows / 187
leaves / 24 nodes (HM57-1) and 235 / 195 / 40 (HM57-2), equal to each sensor's own §6 terminator and §8.

---

## 2. The readings, beside runs 56, 55, 53 and 44

**Rows** = leaves + internal nodes, as in runs 55–56.

| reading | **HM57-1** | **HM57-2** | HM56-1 | HM56-2 | HM55-1 | HM53-1 | HM53-2 | run 44 OA1 | run 44 OA2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| engine | **2.1** | **2.1** | 2.0 | 2.0 | 2.0 | 1.1 | 1.1 | 1.1 | 1.1 |
| posited (skeleton), before closure | **23** | **41** | 28 | 28 | 27 | 64 | 74 | 72 | 69 |
| accreted | **171** | **175** | 154 | 117 | 112 | 43 | 64 | 160 | 167 |
| **anchored (posited + accreted)** | **194** | **216** | **182** | **145** | **139** | **107** | **138** | **232** | **236** |
| derived (completion) | **17** (16 leaves, 1 node) | **20** (20 leaves) | 16 | 13 | 15 | 10 | 12 | 27 | 20 |
| rows before closure | **211** | **236** | 198 | 158 | 154 | 117 | 150 | 259 | 256 |
| **rows after closure** | **211** | **235** | **198** | **156** | **154** | **117** | **150** | **246** | **242** |
| leaves before / after closure | **187 / 187** | **195 / 195** | 169 / 169 | 129 / 129 | 127 / 127 | 103 / 103 | 133 / 133 | — / 187 | — / 187 |
| internal nodes before / after closure | **24 / 24** | **41 / 40** | 29 / 29 | 29 / 27 | 27 / 27 | 14 / 14 | 17 / 17 | — / 59 | — / 55 |
| posited things that ended as leaves | **0** | **0** | 0 | 0 | 0 | 50 | 57 | 0 | 0 |
| anchored leaves (posited leaves + accreted) | **171** | **175** | 154 | 117 | 112 | 93 | 121 | 160 | 167 |
| nodes deleted childless | **0** | **0** | 0 | 0 | 0 | 0 collapsed | 0 collapsed | 13 collapsed | 14 collapsed |
| nodes deleted by lifting | **0** | **1** (N4.5) | 0 | 2 | 0 | (1.1 did not separate) | | | |
| internal nodes carrying coverage | **0** | **0** | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| coverage assignments on leaves | **356** | **396** | 314 | 245 | 283 | 239 | 281 | 257 | 277 |
| leaf assignments per requirement | **2.44** | **2.71** | 2.15 | 1.68 | 1.94 | 1.64 | 1.92 | 1.76 | 1.90 |
| co-located requirement pairs (leaves) | **310** | **418** | 292 | 294 | 494 | 347 | 359 | 155 | 153 |
| leaves covering both a `P-` and an `L-` id | **45** | **43** | 41 | 30 | 30 | 26 | 33 | 37 | 33 |
| accretion verdicts, pass 1: covered / partial / not covered / deferred | **30 / 62 / 52 / 2** | **32 / 77 / 36 / 1** | 33 / 51 / 60 / 2 | 41 / 44 / 61 / 0 | 33 / 71 / 40 / 2 | 112 / 17 / 17 / 0 | 89 / 44 / 11 / 2 | 23 / 18 / 105 / 0 | *not tabulated* |
| rows that added | **114** | **113** | 111 | 105 | 112 | 34 | 55 or 57 | 123 | — |
| **leaves added per row that added** | **1.50** (171 / 114) | **1.55** (175 / 113) | 1.39 | 1.11 | 1.00 | 1.26 | ≈ 1.12–1.16 | 1.30 | — |
| rows adding more than one leaf | **37** | **36** | 26 | 7 | 0 | | | | |
| accreted leaves sharing a coverage set: groups / leaves | **21 / 52** | **15 / 37** | 15 / 39 | 0 / 0 | 0 / 0 | not checked | not checked | **20 / 52** (new, by script) | **22 / 58** (new, by script) |
| distinct coverage sets among accreted leaves | **140** | **153** | 130 | 117 | 112 | | | 128 | 131 |
| ambiguity flags (§3 marks) | **9** (§8 prints 7; see below) | **12** | 18 | 19 | 11 | 13 | 12 | 17 | 25 |
| partial marks standing at closure | **0** | **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| completion leaves covering a requirement | **0** | **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **obligations placed / unplaced** | **146 / 0** | **146 / 0** | 146 / 0 | 146 / 0 | 146 / 0 | 146 / 0 | 146 / 0 | 146 / 0 | 146 / 0 |
| residues (§7c) | **0** | **0** | 1 (NFR-5) | 1 (NFR-5) | 0 | 0 | 1 (NFR-5) | 0 | 0 |
| requirements covered by leaves, checked from §6 by script | **146 of 146** | **146 of 146** | 146 of 146 | 146 of 146 | 146 of 146 | 146 of 146 | 146 of 146 | 146 of 146 | 146 of 146 |
| **turns · first turn stop · output tokens · continuations** | **1 · `end_turn` · 64 004 · 0** | **1 · `end_turn` · 69 987 · 0** | 1 · `end_turn` · 79 883 · 0 | 1 · `end_turn` · 92 565 · 0 | 2 · `max_tokens` · 64 000 · 1 | 2 · `max_tokens` · 64 000 · 1 | 3 · `max_tokens` · 64 000 · 2 | not audited | not audited |

Run 53–56 and run 44 columns are copied from `run56_product_model.md`. The exceptions are run 44's identical-set and
distinct-set rows, computed now by `analyze57.py` on the same §6 tables its `compare_run44.py` parses. Run 44's
anchored count includes 13–14 nodes that 1.1 collapsed at closure; **rows after closure** is the like-for-like
structure size across engines.

**The flag count.** HM57-1's §3 carries 9 `flag` marks and its §9 table has 9 rows. Its §8 prints 7. The sensor
notices this itself in §9: "That table has 9 rows but the count in §8 is 7 … read by the §3 log (the rule in M3) the
count should be 9, not 7." The table uses 9. HM57-2's §3, §8 and §9 agree on 12.

**NFR-5.** Neither sensor reports a residue. HM57-1 realises the conformance design and the deviation procedure (A149,
A150), flags NFR-5, and says in §9 that the no-cost clause "obliges the work and no product leaf can realise it". HM57-2
realises the analyses as a product artefact (E160). The same clause was a §7c residue in HM56-1 and HM56-2.

**Log checks (by script).**
- No covering column in §3 names a node (both).
- No node carries coverage. Derived leaves carry no requirement id (both).
- All §2 scopes are at most eight words (both). HM57-2's §2 header omits the "(≤ 8 words)" label.
- HM57-1's closure log is empty: 0 deletions, 0 lifts. HM57-2's is `lifted E130 from N4.5 to N4; deleted N4.5`.
- The largest leaf sets: A051, the import pipeline, with 12 ids (HM57-1); E59, import job handling, with 10 ids
  (HM57-2).

**Identical coverage sets.**
- HM57-1 has 21 groups. They include:
  - the six format adapters A053–A058 (each `D-5, G-12.1, G-12.2, L-15, P-19`);
  - the four NFR-8 leaves A154–A157;
  - three each for G-7.1, NFR-2, NFR-10 and the P-1/L-1 creation modes;
  - pairs such as the check digit and the composition rules (A003/A004), and the IdM leaves A146/A147.
- HM57-2 has 15 groups. They include:
  - the six format adapters E61–E66 (the same set);
  - three NFR-8 leaves E162–E164;
  - three G-6 dashboard panels E31–E33;
  - three G-7.1 leaves E37–E39.

**The pair's spread.** Anchored ×1.11 (216 / 194). Rows after closure ×1.11 (235 / 211). Leaves ×1.04 (195 / 187).
Accreted ×1.02 (175 / 171). Posited ×1.78 (41 / 23). For comparison: run 56 ×1.26 anchored, ×1.31 leaves; run 44
×1.017 anchored; run 53 ×1.29.

**Where the pair's spread sits now: in the skeleton.** Of the 22 anchored rows between the two readings, 18 are
posited nodes (41 against 23) and 4 are accreted leaves. The leaf counts differ by 8, and the grains by 0.05.

**Level against the earlier runs.** The pair's mean anchored level is 205:
- ×1.25 on run 56's mean (163.5);
- ×1.47 on run 55 (139);
- ×1.67 on run 53's mean (122.5);
- ×0.88 on run 44's mean (234).

Members: HM57-1 is ×0.83 of run 44's mean, HM57-2 ×0.92.

The other measures, against run 44's means:
- **Rows after closure:** mean 223 against 244, ×0.91.
- **Leaves:** mean 191 against 187, ×1.02. HM57-1's 187 equals both run 44 readings.
- **Accreted:** mean 173 against 163.5, ×1.06.

What remains between 2.1 and run 44 is the skeleton: 32 posited on average against 70.5. It is not accretion, which
now slightly exceeds run 44.

**Jaccard of the leaf co-location relations**, and, in the last two columns, Jaccard on the **families of distinct leaf
coverage sets** (each distinct non-empty set counted once).

| pair | shared / union | J | ceiling on J from the two sizes | shared / smaller relation | sets shared / union | J on sets |
|---|---|---:|---:|---:|---|---:|
| **HM57-1 vs HM57-2 (within run)** | **250 / 478** | **0.523** | 0.742 | **0.806** | **92 / 201** | **0.458** |
| HM57-1 vs HM56-1 | 192 / 410 | 0.468 | 0.942 | 0.658 | 93 / 177 | 0.525 |
| HM57-1 vs HM56-2 | 217 / 387 | 0.561 | 0.948 | 0.738 | 86 / 171 | 0.503 |
| HM57-1 vs HM55-1 | 267 / 537 | 0.497 | 0.628 | 0.861 | 71 / 181 | 0.392 |
| HM57-2 vs HM56-1 | 230 / 480 | 0.479 | 0.699 | 0.788 | 84 / 199 | 0.422 |
| HM57-2 vs HM56-2 | 244 / 468 | 0.521 | 0.703 | 0.830 | 80 / 190 | 0.421 |
| HM57-2 vs HM55-1 | 295 / 617 | 0.478 | 0.846 | 0.706 | 68 / 197 | 0.345 |
| HM57-1 vs run 44 OA1 | 116 / 349 | 0.332 | 0.500 | 0.748 | 81 / 187 | 0.433 |
| HM57-1 vs run 44 OA2 | 112 / 351 | 0.319 | 0.494 | 0.732 | 81 / 190 | 0.426 |
| HM57-2 vs run 44 OA1 | 111 / 462 | 0.240 | 0.371 | 0.716 | 79 / 202 | 0.391 |
| HM57-2 vs run 44 OA2 | 132 / 439 | 0.301 | 0.366 | 0.863 | 73 / 211 | 0.346 |

The within-run pairs on the same two measures, for reference:

| within-run pair | co-location J | J on sets |
|---|---:|---:|
| run 56 | 0.597 (219 / 367, ceiling 0.993, containment 0.750) | 0.583 (91 / 156) |
| run 44 | 0.453 (96 / 212) | 0.589 (96 / 163) |
| run 53 | 0.569 (256 / 450) | — |

**What the Jaccard says.**
- **Agreement within the pair did not rise with the narrower level spread.** The co-location J is 0.523, against run
  56's 0.597. The relations now differ in size (310 against 418), which caps J at 0.742. Containment rose from 0.750
  to 0.806: the smaller relation sits more inside the larger. On exact coverage sets, agreement fell from 0.583 to
  0.458.
- **Against run 44 the structures did not converge, although the counts did.** The co-location J is 0.24–0.33 (run 56:
  0.27–0.34). J on sets is 0.35–0.43 (run 56: 0.47–0.53).
- **The 2.x relations are about twice run 44's size** (310–418 pairs against 153–155). 2.x leaves carry 2.44–2.71 ids
  per requirement against 1.76–1.90. That is a trait of "coverage lives in leaves only" and did not change in 2.1.

---

## 3. Whether the 2.1 output format was followed

| requirement of the *Output format* (unchanged from 2.0) | HM57-1 | HM57-2 |
|---|---|---|
| sections in the order the phases run: 1, 2, 3, 4, 5, 6, 7, 7c, 8, 9 | **followed**; §3 with `Pass 1`, `Pass 2 (retrying pass-1 deferrals only)` | **followed**; §3 with `Pass 1`, `Pass 2` |
| each section closed by one terminator line carrying its counts | **mostly**: 11 terminators, bare (not in backticks), §1 included; `-- end §9 --` carries no counts | **followed**: 11 terminators, each in backticks and each with counts |
| §2: id · parent · name · scope ≤ 8 words; nothing attached | **followed**; `23 nodes posited · 0 leaves` | **followed** in content; header omits "(≤ 8 words)"; `41 nodes posited · 0 requirements attached` |
| §3: one table per pass, 8 columns | **followed** | **followed** |
| §4: id · trigger · justification · pass | **followed**; 17 rows including one derived **node** CN01 ("several derived background leaves need a grouping") | **followed**; 20 rows, no derived node |
| §5 convergence trace reaching zero | **followed**, with a closure-normalisation row | **followed**, without that row |
| §6 as one fenced TSV block, `id · parent · origin · coverage set · name` | **followed**: header + 211 rows, 5 fields each; derived leaves carry `trigger:A…` | **followed**: header `coverage set`, + 235 rows, 5 fields each; root parent `—`; derived leaves carry `trigger:E…` |
| §7 closure log: every deletion and lift, in order | **followed**: 0 deletions, 0 lifts | **followed**: one lift and deletion |
| §7c: "N of N whole", then residue rows | **followed**: `146 of 146 whole` | **followed**: `146 of 146 whole` |
| §8: engine stamp verbatim, then the eight counts only | **partly**: `**Engine: Hotyn-M 2.1**`; reading 7 prints 7 flags against 9 in §3 and §9 | **partly**: `**Hotyn-M 2.1**` without `Engine:`; reading 2 gives derived 20 without a leaf/node split; reading 5 omits closure normalisation |
| §9: unplaced; ambiguous ids with reasons ≤ 10 words; interpretations | **followed**: none unplaced; 9 flag rows, a note on the §8 discrepancy | **followed**, as a bulleted list rather than a table: none unplaced; 12 flags (= §8) |

---

## 4. Whether either sensor read M2's identity sentence as a merge rule

M2 in `agents/model-builder.md` (2.1): "**Identity — for comparing models, not for building one.** … It is not a rule
about how many leaves to make. **A leaf is one thing to be built** … Two distinct things that realise the same
obligations — six format adapters, one per format; a product twin and a location twin of one screen — are two leaves,
and they may carry the same coverage set. Do not merge leaves because their sets coincide, and do not split a leaf so
that its set becomes unique. Where the assumption log fixes the count of things (one adapter per format), that count
stands."

**HM57-1: keep apart, stated.** Neither its §9 nor its §3 invokes identity by coverage set. What it states is a count
of things fixed by the assumption log. §9:

> - **Formats.** There is one adapter per file format, six in total (A053–A058), each doing both import and export,
>   as the assumption log fixes. The API is a separate leaf (A059). The four barcode symbologies are one library-backed
>   generation leaf, because the log fixes them as library output rather than as separate things.

§3, row G-12.1: "one adapter per format, fixed by assumption log". Its §6 keeps 52 accreted leaves in 21 groups of
identical sets, 31 leaves beyond one per set. Grain: **1.50**.

**HM57-2: keep apart, stated as the projection's count.** Its §9 does not mention identity or coinciding sets. §3,
row G-12.1: "six adapters fixed by P3". §9:

> - **G-12.2:** PC/Mac read as variants inside the six adapters (P3), not a separate leaf.

Its §6 keeps 37 accreted leaves in 15 groups of identical sets, 22 beyond one per set. Grain: **1.55**. The sentence
HM56-2 wrote in run 56 does not appear: "separate leaves per format would all carry the same coverage". HM57-2 has
no row where leaves "briefly shared one coverage set" and were then made distinct.

**The four 2.x treatments, side by side:**

| reading | engine | treatment of M2 identity | leaves per adding row | rows that added | same-set groups / leaves | anchored |
|---|---|---|---:|---:|---|---:|
| HM55-1 | 2.0 | merge: one leaf per requirement's unshared part | 1.00 | 112 | 0 / 0 | 139 |
| HM56-2 | 2.0 | merge only where sets cannot become distinct | 1.11 | 105 | 0 / 0 | 145 |
| HM56-1 | 2.0 | not applied: equal sets kept apart, silently | 1.39 | 111 | 15 / 39 | 182 |
| **HM57-1** | **2.1** | **keep apart; count fixed by the assumption log, stated** | **1.50** | **114** | **21 / 52** | **194** |
| **HM57-2** | **2.1** | **keep apart; count fixed by P3, stated** | **1.55** | **113** | **15 / 37** | **216** |
| run 44 OA1 / OA2 | 1.1 | (no identity sentence) | 1.30 / — | 123 / — | 20 / 52 · 22 / 58 | 232 / 236 |

The number of rows that add is still nearly constant: 105–114 across all five 2.x readings. Anchored ≈ posited + adding
rows × grain holds in both new readings (23 + 114 × 1.50 = 194; 41 + 113 × 1.55 = 216). Run 44's same-set counts
(20 / 52, 22 / 58) were not checked before this run. They sit where HM57-1's are (21 / 52). So run 44's 1.30 grain did
contain same-set leaves, at the 2.1 rate.

---

## 5. The reading, against the registered outcomes, and what would overturn it

**Registered before launch:**
- 2.1 pins the HM56-1 reading: both repeats at ≥ 1.3 leaves per adding row, accreted in the region of 150–160, and a
  pair spread narrower than run 56's ×1.26.
- A repeat that again merges equal-set leaves (§9 stating a merge, ≤ 1.1 leaves per adding row) means the sentence is
  still read as a build rule.
- A pair at ≈ 140 with ≥ 1.3 leaves per row means the remaining gap to run 44 is elsewhere (the skeleton's size).

| registered expectation | reading | verdict |
|---|---|---|
| both repeats ≥ 1.3 leaves per adding row | 1.50, 1.55 | **met** |
| accreted in the region of 150–160 | 171, 175 | **not met — above the region**, and above both run 44 readings (160, 167) |
| pair spread narrower than ×1.26 | anchored ×1.11; leaves ×1.04 | **met** |
| a repeat merging equal-set leaves (§9 merge, ≤ 1.1) | no merge stated; 21 and 15 same-set groups; 1.50, 1.55 | **did not occur** |
| a pair at ≈ 140 with ≥ 1.3 | 194, 216 | **did not occur** |

**R10 — 2.1 pins the keep-apart reading at n = 2, and the level rises past HM56-1's.** Both repeats keep equal-set
leaves apart, and both say so in terms of a count fixed by the assumption log. Neither states a merge, and the grain is
1.50–1.55 in both. The two merge treatments of run 55–56 (1.00, 1.11) did not recur. The anchored spread narrowed from
×1.26 to ×1.11, and the leaf spread to ×1.04.

**The accretion level overshot the registered region.** 171 and 175 accreted leaves sit above 150–160, at ×1.11–1.14
of HM56-1's 154. This has two sources:
- a higher grain than HM56-1 (1.50–1.55 against 1.39), with 31 and 22 same-set leaves beyond one per set against 24;
- slightly more adding rows (114, 113 against 111).

Leaves now match run 44 (mean 191 against 187). On anchored, what remains of the gap to run 44 is the skeleton alone:
32 posited on average against 70.5. This is not the registered "≈ 140" outcome, but the skeleton conclusion it pointed
to holds. The skeleton is now also where the pair's own spread sits (23 against 41).

**Agreement did not improve with the level.**
- Within-pair co-location J fell from 0.597 to 0.523; containment rose from 0.750 to 0.806.
- J on exact coverage sets fell from 0.583 to 0.458.
- Against run 44, J did not rise: co-location 0.24–0.33, sets 0.35–0.43.

2.1 fixed how many leaves a requirement yields. It did not fix which requirements a leaf carries.

**Attribution limit.** HM56-1 already showed a keep-apart grain (1.39) under 2.0. What run 57 shows 2.1 doing is
removing the merge readings: 0 of 2 under 2.1, against 2 of 3 under 2.0. Whether 2.1 also raised the grain from 1.39 to
1.5 is not separable at these n.

*Overturned by:*
- **A 2.1 relaunch of this cell (n ≥ 3) whose §9 states a merge or whose grain is ≤ 1.1.** That would make the pinning
  a probability, not a rule.
- **Uncapped 2.0 relaunches of this cell that reach grain ≥ 1.5 with no merge, in most repeats.** That would put HM55-1
  and HM56-2 in the tail of 2.0's distribution, not in the sentence, and 2.1 would have changed nothing measurable.
- **A 2.1 pair with the ambient commit subjects removed that returns to grain ≤ 1.2.** The `e8f8d07` subject restating
  the change reached both sensors (MANIFEST, ambient context). That would put part of the effect on the channel, not
  the definition.
- **A 2.1 pair whose posited counts agree (for example both ≈ 25 or both ≈ 40) but whose anchored spread stays
  ≳ ×1.1.** That would move the spread off the skeleton, where this reading puts it.

**What this run cannot say.**
- Why the skeleton varies ×1.78 between two repeats of one prompt. The skeleton is posited before any accretion. No
  reading here explains its size.
- Whether concurrent launch mattered. Run 56's pair was sequential.
- Where in the thinking the grain was fixed: the thinking content is empty in both transcripts.

---

## 6. The model carried forward

The first-of-pair rule used for BMS, FaxRxTx and runs 44 and 56 applies. It gives **HM57-1 — 211 rows, 187 leaves, 24
nodes**:
- the first SAS model under `Hotyn-M 2.1`;
- from a pair at ×1.11 anchored spread, ×1.04 on leaves, within-run co-location J 0.523;
- its §8 flag count (7) disagrees with its own §3 and §9 (9), a discrepancy the sensor reports itself.

Whether step 2 should take HM57-1 or wait for more readings is a decision for the step-2 launch. This record does not
take it.

- **Where this file is.** Written to the session scratchpad
  (`<scratchpad>/examples/SAS/run57_product_model.md`), with `run57_raw/MANIFEST.md` beside it. The permission layer
  refused the write into `examples/SAS/`. To be copied into place. The raw replies and the prompt are already in place
  in `examples/SAS/run57_raw/`.

- **MANIFEST.md and this record copied into place** 2026-09-15 from the child session scratchpad by the orchestrating session, byte for byte; the three raw files were written into the repository by the child directly.
