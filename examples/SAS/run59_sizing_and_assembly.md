# Run 59 — SAS size classes on the 2.1 chain, `Hotyn-D 2.0`, n = 2, and the whole-model assembly

**2026-09-15 → 16.** Case 3, steps 3 and 4, on the 2.1 chain — the last stage of the regression of the chain
through the plugin entry point. The work model of run 58 (`Hotyn-W 1.2` × `HM57-1`; 210 elements, 1 396 items)
sized by `Hotyn-D 2.0` in the same seven batches as the crossing, **two independent repeats per batch** — fourteen
launches, all on Claude Opus 5 (the harness's `opus` alias), all `tool_uses: 0`, each **one turn ending
`end_turn`, 17 637–28 131 output tokens, no continuation message**, under `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`.
Prompts: `run59_raw/make_sizing_prompts58.py` — for every sized element its class, parent, covered obligations
**with their texts**, and the activities crossed onto it; the rules block (catalogue 1.4 §3a) is taken at run time
from run 47's generator and is byte-identical to run 47's; pinned with their md5 before launch. Raw:
`run59_raw/HD59-A1.md` … `HD59-G2.md` (orchestrator headers; bodies extracted from the per-agent transcripts by
script), `run59_raw/MANIFEST.md`. Assembly: `run59_raw/assemble_sas58.py` — run 47's `assemble_sas.py` with the
2.x model reader (the fenced TSV of `HM57-1` §6, root `N01`) and a wider reader for the sensors' special-count
sections; conventions unchanged, rate table `docs/rate_table.md` v0.1-h read directly.

```bash
python examples/SAS/run59_raw/assemble_sas58.py
```

The comparison is **run 47** (the run 45 work model on `HM44-OA1`, same engine, same rules, same batch count,
same n): 38 069 / 38 168 net person-hours, centre 38 118, repeat spread ×1.0026.

---

## 1. Sizing readings

| reading | repeat 1 | repeat 2 |
|---|---:|---:|
| elements received (sizeable leaves) | 187 | 187 |
| sized | 186 | 184 |
| **S / M / L / XL** | **35 / 94 / 44 / 13** | **45 / 101 / 35 / 3** |
| unsizeable — model defect (M10) | 1: A140 | 3: A140, A158, A159 |
| statement kinds (compliance / behavioural), 20 statements | 12 / 8 | 10 / 8 (+2 unsizeable) |
| special count, A9 (A164, the only A9 item) | L | L |
| special counts, G2m–G4m (24 stores) | 7 classed · 17 no kind reaches the lowest rung | 8 classed · 16 |
| doubts (sum over batches) | 172 | 183 |
| closure violations (sum over batches) | 35 | 35 |
| XL elements | A008, A020, A029, A037, A051, A078, A081, A099, A100, A123, A160, A161, A162 | A029, A037, A051 |

Run 47 for scale: 52 / 105 / 23 / 3 and 55 / 101 / 25 / 3, unsizeable 4 / 3, doubts 126 / 143, closure violations
33 / 28, the three XL identical in both repeats.

**Class agreement between the repeats: 142 of the 184 elements both repeats sized — 77.2%** (run 47: 85.0%,
159 of 187). Of the 42 disagreements, 35 are one step and 7 are two steps (A004, A073, A074, A075, A102 L→S;
A008, A099 XL→M); **37 of the 42 have repeat 1 higher**. Repeat 2's distribution (45 / 101 / 35 / 3) is run 47's
within a few elements; repeat 1's (35 / 94 / 44 / 13) is a class higher across the board. The two repeats did not
disagree at random: they chose opposite rules for one question the catalogue does not settle (§3). XL agree only
on A029 (report engine), A037 (notification dispatch) and A051 (record import pipeline) — the three that are the
same kind of element run 47's XL were (import service, notification engine). Batches A, D and F agree 27/30,
23/24, 26/28; batches B, E and G agree 15/27, 16/31, 16/23.

**Holes.** Repeat 1 leaves 42 items unpriced, repeat 2 47: A140 (Access Data REST API — its content names no
operation to count) in both, all six of its items; A158 and A159 (backup and disaster-recovery procedures: "the
system is never named") in repeat 2; and the G2m–G4m items of every store where the sensor enumerated **no entity
kind that must come from the predecessor** — 17 stores in repeat 1, 16 in repeat 2 (the two repeats agree on 15 of
them; A076, A010 are classed by one repeat and not the other, C06 the reverse). Named, never guessed, listed by the
assembly.

---

## 2. The assembly

Conventions identical to run 47: rooted subtrees, C3 at 20% of leaf-item effort at every parent including the
root, once-scoped and per-environment items outside every C3 base, E = (O + 4M + P) / 6, rate table v0.1-h in
**net person-hours**. Position-derived classes computed by the script: 23 parents plus the root; model bracket
**L** (211 elements); E3 **L** (4 environments); E1 dev S · test M (declared) · stage M · prod L; G5m twice; S2/S3
**XL** (52 surfaces and interfaces — run 47 had 45).

| layer | repeat 1 | repeat 2 | run 47 (r1 / r2) |
|---|---:|---:|---:|
| element items, incl. the root's per-parent items | 23 332 | 21 349 | 24 163 / 24 221 |
| C3, all 24 parents | 10 761 | 9 765 | 13 065 / 13 106 (59 parents) |
| of which the root alone | 4 666 | 4 270 | 4 833 / 4 844 |
| once + per-environment (23 items) | 840 | 840 | 840 / 840 |
| **total, net person-hours** | **34 933** | **31 954** | **38 069 / 38 168** |
| in table person-days (8 h) | 4 367 | 3 994 | 4 759 / 4 771 |

**Repeat spread ×1.093 · centre 33 444 net task hours.** The band at the declared ρ = 0.5 (`docs/constants.md`
§5e, a convention, not a measurement — `docs/instrument.md` §4): sd ≈ 5 300 h, **P10 ≈ 26 700 · P90 ≈ 40 200
(×0.80 / ×1.20 of the centre)**, the same width every case has shown because the rate cells set it. C3 is 30.8% /
30.6% of the total (run 47: 34.3%); delivered against leaf effort it is **46.1% / 45.7%** (run 47: 54%) — the mean
leaf depth of `HM57-1` is 2.32 against `HM44-OA1`'s 2.90, and C3 at every parent is the depth showing itself.

**In the comparison-layer convention** (`docs/constants.md` §4a): 33 444 h ≈ **292 staffed person-months**
(run 47: 333). Stated once, for the report; no sensor saw the conversion.

### 2a. Against run 47 — the 1.1 → 2.1 conversion, measured

| | run 47 centre | run 59 r1 | run 59 r2 | run 59 centre |
|---|---:|---:|---:|---:|
| total | 38 118 | 34 933 (×0.917) | 31 954 (×0.838) | **33 444 (×0.877)** |
| element items | 24 192 | ×0.964 | ×0.882 | ×0.923 |
| C3 | 13 086 | ×0.822 | ×0.746 | ×0.784 |
| once layer | 840 | ×1.00 | ×1.00 | ×1.00 |

**Registered in run 58 §2 before the sizing ran:** C3 about 46% of leaf effort — **met (46.1 / 45.7)**; total
below run 47's, in the region ×0.85–0.95 if the classes distribute as in run 47 — **met on the centre (×0.877)
and on repeat 1 (×0.917)**; repeat 2, whose classes *do* distribute as run 47's, lands at ×0.838, just under the
region. So the skeleton's effect on the price is about ×0.84 at run 47's class mix — per-parent items halved (281
against 574) and C3 shallower — and repeat 1's higher classes (13 XL, 44 L) add ×1.09 on top of it.

Where the ×0.877 sits: **the whole difference is C3 and the per-parent items, both functions of the 2.x
skeleton** (24 parents against 59, depth 2.32 against 2.90). The per-element items at run 47's class mix are
×0.88, and that is the per-parent items inside the element layer (A5–A8, U1–U3, D2, O1: 281 against 574 items)
plus a handful of classes; the leaves' own construction and assurance items (K1, K2, A2–A4, D4) are the same
count and, in repeat 2, very nearly the same classes. **Nothing in the price points at the entry point.** The
chain through the plugin, on a 2.1 model, prices the same 187 leaves the same way and a shallower tree cheaper —
by the mechanism `docs/constants.md` §3 names, C3 as a depth multiplier, now measured on the same case at two
depths: 2.90 → 54% of leaf effort, 2.32 → 46%.

### 2b. Composition, repeat 1 (structure and totals, no class figure — the input of the gap-blind rate source)

| subtree | elements | items, h | C3 inside, h | subtotal, h |
|---|---:|---:|---:|---:|
| N02 Platform architecture | 35 | 3 043 | 1 093 | 4 136 |
| N06 Identity and access | 14 | 1 554 | 311 | 1 864 |
| N07 Record governance | 10 | 1 118 | 224 | 1 342 |
| N08 Notifications | 16 | 1 475 | 295 | 1 770 |
| N09 Reporting and dashboard | 10 | 1 232 | 246 | 1 479 |
| N10 User assistance | 6 | 573 | 115 | 688 |
| N11 Import and export | 12 | 1 502 | 300 | 1 803 |
| N12 Publish and subscribe | 14 | 1 374 | 275 | 1 649 |
| N13 Shared record management | 37 | 5 145 | 1 931 | 7 076 |
| N19 Product module | 19 | 2 316 | 628 | 2 945 |
| N20 Location module | 12 | 1 237 | 247 | 1 484 |
| N21 Access Data module | 9 | 1 088 | 218 | 1 306 |
| N22 Operational properties | 16 | 1 062 | 212 | 1 274 |
| root: own per-parent items 612 · root C3 4 666 · once / per-environment 840 | | | | 6 118 |

By activity (element-attached, repeat 1): K2 4 481 · A3 3 372 · K1 1 981 · A6 1 904 · A2 1 788 · D4 1 365 · A5
1 304 · A7 1 112 · U3 979 · A4 913 · U2 719 · D2 644 · K3 528 · G3m 384 · U1 373 · O1 373 · A8 323 · A10 313 ·
G2m 233 · G4m 197 · A9 47.

---

## 3. What the two repeats show about step 3

**The sizing step's own spread is ×1.09 here against ×1.003 in run 47 — thirty times wider — and it is one
question, not noise.** The 2.1 model keeps distinct leaves that realise the same obligations (52 leaves in 21
equal-set groups; 310 co-located requirement pairs against run 44's 155), so many obligations are covered by
several leaves at once. The rules say to count "from the element's declared content plus its own coverage"; they
do not say whether an obligation shared by several leaves is counted in full on each. The repeats split on exactly
this, and each said so at the top of its reply:

- **Repeat 1 (B1):** "When an obligation is shared by several leaves, its full text is counted on each of them."
  E1 the same (its R1). Result: A008, A020, A165 each count all of NFR-16's workflow verbs; A013, A014, A015 each
  count all of G-1, G-1.2, G-3.1; the security triad A160–A162 each count NFR-10's five systems — 13 XL, 44 L.
- **Repeat 2 (B2):** "Each element counts only the parts of a shared obligation that its name claims. The parts
  claimed by another element's name are counted on that element." E2 the same ("sibling owners"). Result: run 47's
  distribution.

Both readings are legal under P-2 as written (P-2 is about *name tokens* already covered by an obligation, not
about obligations shared *across* leaves), both were declared up front, and each repeat listed the other as its
first doubt. **This is a catalogue gap that the 1.1 model hid and the 2.1 model exposes**: on `HM44-OA1`, with
half as many co-located pairs, the question arose rarely enough for 85% agreement. It is the same shape as run
47's own open question (are the GIN and LN twins one object or two — here E1's R2 and E2's "mirror pairs", both
repeats counting a P-x / L-x pair once), one level up: not "is this one thing or two" but "whose thing is this
obligation". **A precedent for the catalogue, not a repair here**; recorded for BACKLOG. Until it is adjudicated,
the 2.x chain's sizing carries a ×1.09 freedom that the 1.1 chain did not show.

**Two things the repeats did not agree on and the assembly could not settle**, the same two as run 47 §3:

- **Whether a store with no predecessor origin has a migration count at all.** Both repeats agree on 15 of the
  24 stores' G2m–G4m answers — 8 classed the same way (A001 L, A080 M, A087 S, A062 M, A122 / A129 / A109 / A077
  M or S per F, A131 S) and the rest "no kind reaches the lowest rung" — and differ on A076 (M / none), A010
  (S / none) and C06 (none / S), plus A012 (M / S). Batch B's six stores drew no class in either repeat: "no
  predecessor application is named anywhere in the batch". The rate table's G rows have no zero rung; the
  catalogue's driver still reads two ways ("needing pre-load" against "loaded from the predecessor"). Unchanged
  from run 47.
- **A005** (architecture design): behavioural in repeat 1, compliance in repeat 2 — the one K3 kind divergence.

---

## 4. Registered expectation, scored, and the regression question

Registered in the launch instruction: (a) 187 leaves sized and no aggregate, ≤ 5 unsizeable per repeat — **met**
(1 and 3); (b) class agreement 80–90% — **not met, 77.2%**, for the reason in §3; (c) XL ≤ 5 per repeat and the
same set — **not met**: 13 against 3, agreeing on 3; (d) stamp `Hotyn-D 2.0`, one turn, no continuation, every
launch — **met**; (e) no unit of effort, time or money in any reply — **met**: the orchestrator's grep found only
the contamination check's list of forbidden categories, report-period words quoted from G-7.2, and "work on day
one" in A2.

**On the regression of stages 2–3 through the plugin.** Three stages ran through `/3a8:estimate-product` in a
child process, every sensor in one turn under the raised cap, every prompt pinned before launch, every raw reply
transcribed from the transcript. The crossing gave run 45's per-element layer within 4% (run 58). The sizing at
run 47's class mix gives run 47's classes within a few elements (repeat 2). The price differs from run 47 by
×0.877, and the difference decomposes into the skeleton's depth (C3 ×0.78) and the skeleton's parent count
(per-parent items ×0.49), both properties of `Hotyn-M 2.x` that runs 55–57 already measured in nodes. **The entry
point is clean.** What the regression found instead is a property of the 2.1 chain: a sizing freedom of ×1.09
from one unadjudicated question, which the 1.1 chain's denser skeleton did not expose.

**The 1.1 → 2.1 conversion on SAS, n = 2 against n = 2: ×0.877 on the centre, band ×0.84–0.92.** Readings of the
two versions are not to be pooled (`PIPELINE.md`); this is the measured ratio between them on the one case both
have priced.

---

## 5. Carried forward

`assemble_sas58.py` output, both repeats, is the 2.1 chain's reading of SAS: **33 444 net task hours, repeat band
31 954 – 34 933**, 23 once-scoped items, 42 and 47 named holes. The demanded branch `DW-4` (post-production
support period) stands unpriced beside the number, as run 45 §5 and run 58 §1 record; the carried-not-priced list
of `assumptions.md` A1 stands as before. No diagnosis (steps B–D) was run on this reading: the regression's
question was the chain, not the estimate, and the SAS estimate of record remains `estimate_SAS_2026-09-08.md`.

For BACKLOG: the shared-obligation rule of §3 as a catalogue precedent to adjudicate before the next 2.x sizing;
and the fact that with `Hotyn-M 2.x` the sizing step, not the product model, is now the widest of the three on
this case.
