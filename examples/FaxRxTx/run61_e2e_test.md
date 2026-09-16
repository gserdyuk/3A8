# Run 61 — the end-to-end test of the instrument on FaxRxTx, scored (2026-09-16)

The registration is `run61_e2e_registration.md`, written before launch. This record scores the run against it and
lists what the run found about the instrument. The estimate itself is `estimate_FaxRxTx_2026-09-16.md`; the run
records are `run61_product_model_measurement.md` … `run68_fact_comparison.md`, the raw material `run61_raw/` …
`run67_raw/`, the report `reports/report_2026-09-16T1408.html`.

## The launch

One child process, `claude --plugin-dir . --model claude-opus-5 --permission-mode acceptEdits -p`, with
`CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`; the prompt (`C:\…\Temp\run53\prompt61.txt`, kept out of the repository) said
"estimate `examples/FaxRxTx` end to end as the skill prescribes", named the pinned inputs, forbade reading runs 1–43
and their reports, sealed `FACT.md` until the document was fixed, and said that if writing into the case folder was
refused the same files were to be written under the session's scratchpad. The orchestrating session watched the
transcripts and touched nothing. **13:23 → 14:09, 46 minutes, no intervention.**

| | |
|---|---|
| sensor launches | 22 (4 product-model, of which 2 contamination stops · 1 version probe · 4 crossing · 8 sizing · 1 rate author · 2 outside view · 1 Step C · 1 diagnosis) |
| turns per launch | 1, every one `end_turn`, no continuation message, no tool use |
| output tokens, all sensors | 213 465 (largest: RG67-1 21 461, HM61-2 23 537) |
| model per turn | `claude-opus-5` in all 22; harness 2.1.270 |
| prompt integrity | md5 of the saved prompt = md5 of the text the sensor received, in all 22 |
| engine stamps | `Hotyn-M 2.1`, `Hotyn-W 1.2`, `Hotyn-D 2.0`, `Hotyn-K 1.1`, `Lytin-R 1.1`, `Lytin-K 1.1`, `Lytin-G 1.1` — all current |

## Registered outcomes, scored

| # | registered | happened | |
|---|---|---|---|
| 1 | **Process.** Step 0 (`case_profile.md`), Steps 1–4 through the sensors and `tools/chain`, outside view n = 2, Steps C, B, D, Step 7 (both input files, the report, the document), in one process, no intervention | all of it, in order; the case profile written and md5-recorded before the first launch; Step 6 (the reveal) after the document was fixed | **met** |
| 2 | **Sensors.** Every turn `end_turn`, no continuation; every stamp current | 22 of 22; two product-model launches stopped at §1 by design (contamination, below) — refusals, not cuts | **met** |
| 3 | **The chain.** Raw chain ×0.70–0.95 of the outcome; sizing spread ≤ ×1.10; class agreement ≥ 75% | raw chain **10 020 h = ×0.73** of 13 745 h (the outcome at the case's conversion, run 68); spread **×1.035**; agreement **95.6%** | **met** |
| 4 | **Calibrated.** ×1.05–1.4 of the outcome if Step C lands near ×1.5; inside the ×1.3 gate on at least one side | Step C chain **×1.73** (to G2; G1 dropped by the diagnosis as a double count of the pinned 6 h/day); centre **17 350 h = ×1.26**, whole repeat band 17 100–17 597 inside the gate; the corridor 11 795–26 330 contains the outcome | **met** |
| 5 | **Artefacts.** Document in the template's form; report with the chain bell, the class curves, the outcome line, the tiles; both report inputs present, every number traceable | all present; `report_numbers.json` names a run for every figure; the report checked in the browser after the run (the child could only check it structurally) | **met** |

Nothing on the "what would overturn the reading" list happened: no missing artefact, the chain inside its region,
no sensor cut or resumed.

**Note on the outcome's unit.** The registration quoted the outcome as ≈ 13 304 h (run 33's conversion); the child
converted 120 staffed person-months by the pinned `docs/constants.md` §4a (114.5 net h per staffed month) to 13 745 h
and the score above uses the child's figure, as the estimate does. Against 13 304 h the ratios are ×0.75 raw and
×1.30 calibrated — the calibrated centre would sit **on** the gate. The conversion is the pinned one; the run
33 figure is superseded by it.

## The not-registered questions (item 6), read afterwards

- **`C-DIRECT`, `G-SEED`, `SA-NONE`** (the first 2.x crossing on a declaration other than SAS's): the crossing filtered
  D4 (migration) on 27 elements and O1 on 11, refused A9 on both statements (the crossing sees coverage ids, not
  texts, so F36's "~30/s" was invisible to it — performance testing enters the estimate only through Step C), and
  refused the seed-data activities as judgement on six stores whose content is produced at run time (18 judgement
  refusals, all in batch C). 521 items on 83 elements, 0 row mismatches.
- **Seed counts:** the sizing assigned G1–G3 classes on D01 (M, both repeats), L01 (M), D03 (S, one repeat) and
  found count 0 on L32 — reported, not guessed.
- **The demanded items F48, F49, F50, F52:** carried into the assembly as standing branches; `Hotyn-K 1.1` (run 64)
  priced W-F49 (62.7 h) and W-F52 (37.3 h) and **refused W-F48 and W-F50** because their headcount and period are
  undeclared in the case profile — carried, not priced, exactly as run 31 had them. The addendum adds 100 h to the
  chain (9 920 → 10 020).
- **The product-model pair:** leaves 68 vs 75 (×1.10), coverage-set Jaccard 0.51; only `HM61-1` was priced, so this
  spread is in no number and the document says so.

## What the run found about the instrument (acted on in this commit)

1. **A pinned projection contaminated its own consumer.** `assumptions_product.md` v1 named the "~1–2 month" figure
   it said it had removed; both first product-model launches stopped at §1, correctly. The child struck the figure in
   the prompt and relaunched. → `assumptions_product.md` **version 2** (the figure replaced by the words "the
   duration figure"; nothing else changed).
2. **`consolidate_crossing.py` did not read a group defined as `**PAR7** is the 7 nodes: …`** — 5 rows, 49 items,
   dropped with a printed mismatch; the child wrapped the tool (`run62_raw/consolidate_62.py`). → the group
   definition now also reads `is / are / denotes / means`. Re-run without the wrapper: `classes.tsv`,
   `work_model.tsv`, `crossing_summary.json` byte-identical to the child's.
3. **`assemble.py` did not read five special-count phrasings** ("so the class is **M**", "**Count: 2. Class: M.**",
   "**L01, count 2, M.**", "**Count: 0.** … I assign no special class"); unparsed they become holes silently. The
   child overlaid them (`run63_raw/assemble_63.py`). → the phrasings added; re-run without the overlay:
   `assembly_summary.json` identical. SAS runs 58–59 re-run with both fixes: identical.
4. **Auto-batching put two root-level leaves alone in batch D** (L39, L56 — one launch for two elements). → a trailing
   batch smaller than a quarter of the target now joins the smallest earlier batch (on this model: A = N10 + L39 +
   L56, 17 elements; SAS's seven batches unchanged).
5. **The child could not write into `examples/FaxRxTx/`** — the harness refused the case folder as a sensitive path in
   the non-interactive process, so every artefact went to the scratchpad and was copied here by hand, byte for byte
   (the ten pinned inputs it copied are identical to the case's). The report's footer therefore names the scratchpad
   path of its data file; the report is kept as generated. Open: whether the skill should name the case folder
   explicitly for the permission layer, or the runner should be launched with the case folder added.
6. **The demanded-work list rides with the last batch only** (by design of `make_crossing_prompts.py`); batches A–C
   each flagged its absence. Not a defect, recorded so the flag is not read as one.

## What it means for the instrument's standing

This is the first estimate produced by the packaged plugin alone, from pinned inputs to the document and the report,
with the outcome sealed. It scores nothing new for `docs/exit_criterion.md`: FaxRxTx is case 1, admitted on
conventions supplied after its number, and `run68_fact_comparison.md` says so. What it establishes is that the
instrument runs as written: 22 launches, one turn each, and the whole chain reproducible from the raw replies by
`tools/chain` without hand work.
