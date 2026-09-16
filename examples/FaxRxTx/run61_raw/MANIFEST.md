# run 61 — Product model (Hotyn-M 2.1), n = 2, and the pre-launch version probe — MANIFEST

Case `examples/FaxRxTx` · 2026-09-16 · orchestrator: the main session (Claude Opus 5).

## Launch coordinates (all sensors of this run)

- **Model:** every sensor launched through the Agent tool with the model alias `opus`; every turn in the transcript
  records `claude-opus-5`. Harness: Claude Code 2.1.270 (from the transcripts).
- **Output cap:** `CLAUDE_CODE_MAX_OUTPUT_TOKENS` was raised by the launcher of this session (the task statement says
  so); its value **could not be read from inside the session** — `printenv` and `Get-ChildItem Env:` were refused by
  the permission layer. No turn came near 64 000 output tokens (largest: 23 537), so the cap did not bind either way.
- **Process:** the sensors are subagents of the orchestrating session (not child `claude -p` processes), launched in
  parallel where independent. Tools: `Glob` only; `tool_uses` recorded per reading below.
- **Raw replies:** transcribed by `run61_raw/extract_reply.py` from the harness's subagent transcripts — the assistant
  text blocks, in order, unchanged — under an HTML-comment orchestrator header (reading, engine stamp as printed,
  model, prompt md5 and the md5 of the message the sensor actually received, turns, stop reasons, output tokens,
  continuation messages). Every prompt below was saved before its launch unless the notes say otherwise.
- **Ambient context:** every sensor reported a harness-prepended git status, commit subjects and a memory index, and
  quarantined it (quarantine paragraph in every prompt).
- **Location:** writing into `examples/FaxRxTx/` was refused by the harness ("sensitive file"); this folder lives in
  the session scratchpad at the same relative path.

## Notes

- **Version probe** (`3a8:version-probe`, before the first sensor launch): manifest identical to disk,
  `tools/check_probe.py` → 11 agents, 0 failing. Its one-word prompt was saved *after* the launch (`prompt_probe.md`);
  the md5 check against the transcript still matches.
- **First launch (`prompt_M.md`) stopped for contamination in both repeats** (`HM61-x1`, `HM61-x2`): the pinned
  `assumptions_product.md` quotes the immersion stage's duration inside its own "Removed here" paragraph. The pinned
  file was not edited; `prompt_M2.md` is `prompt_M.md` with that one figure struck in place
  (`the ~1–2 month figure` → `[struck by the orchestrator: a figure]`). Fresh instances were launched on it.
  The two contaminated readings are kept, are not readings of the model, and do not count towards n.
- **Closed model:** `HM61-1` (orchestrator's decision: the repeat that closed 47/47 whole with no defect report;
  `HM61-2` left F19 with a residue). `compare_models.py` prints the comparison.
- **Pinned inputs copied byte for byte** from `examples/FaxRxTx/` by `make_prompts_61_65.py` (md5 printed there);
  `FACT.md` was neither opened nor copied.

## Readings — per sensor, per turn

| reading | subagent | engine (as printed) | prompt | prompt md5 | received = saved | turns | stop reason(s) | output tokens | continuations | tool uses |
|---|---|---|---|---|---|---|---|---|---|---|
| HM61-x1 | `3a8:model-builder` | Hotyn-M 2.1 | `prompt_M.md` | `b7eb5e73e2b2d09df2839e15b32bb459` | yes | 1 | end_turn | 2283 | none | 0 |
| HM61-x2 | `3a8:model-builder` | Hotyn-M 2.1 | `prompt_M.md` | `b7eb5e73e2b2d09df2839e15b32bb459` | yes | 1 | end_turn | 1763 | none | 0 |
| HM61-1 | `3a8:model-builder` | Hotyn-M 2.1 | `prompt_M2.md` | `849067816a0e54d0f710c0f6dca43fc0` | yes | 1 | end_turn | 20412 | none | 0 |
| HM61-2 | `3a8:model-builder` | Hotyn-M 2.1 | `prompt_M2.md` | `849067816a0e54d0f710c0f6dca43fc0` | yes | 1 | end_turn | 23537 | none | 0 |
| PROBE61 | `3a8:version-probe` | (manifest of all stamps) | `prompt_probe.md` | `26e491006687eb4b1605e1cdc8533698` | yes | 1 | end_turn | 209 | none | 0 |

## Files

| file | bytes | md5 |
|---|---:|---|
| `HM61-1.md` | 17442 | `a06715b7d019a04a830baa57fb75822d` |
| `HM61-2.md` | 19556 | `ba8a6c6ce5b63303005d11c1d72302d0` |
| `HM61-x1.md` | 4251 | `716988ef5afa434cb4cee2e03c53b1e3` |
| `HM61-x2.md` | 3193 | `3380dc869358f20a9a9cffb666615783` |
| `PROBE61.md` | 1275 | `a5c1bc0dcb064bb8b0bc05cde7c75ec5` |
| `compare_models.py` | 1738 | `532857ff5678e1603d4a09250ef40cfc` |
| `extract_reply.py` | 5671 | `ca88a9a35be9a7b458c51beca8f737f8` |
| `make_prompts_61_65.py` | 6236 | `fb319feeafbb33fc034b3bbb42d501d7` |
| `prompt_M.md` | 12774 | `b7eb5e73e2b2d09df2839e15b32bb459` |
| `prompt_M2.md` | 12789 | `849067816a0e54d0f710c0f6dca43fc0` |
| `prompt_probe.md` | 6 | `26e491006687eb4b1605e1cdc8533698` |
| `turns.jsonl` | 2246 | `b112f756ab72d92987369196f9433723` |
