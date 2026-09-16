# run 66 — Step C corrections (Lytin-K 1.1), one reading — MANIFEST

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

- Prompt built by `make_prompt_66.py`: the same description as run 65, the assumption log, and the bottom-up
  reading (structure with classes and size classes, totals, composition, coverage report, closure findings).
  It asserts that no outside-view figure is present (A8 of the pinned log names the method; it carries no result).
- `price_fills66.py` prices RK66's element fills A1–A4 through rate table v0.1-h and applies T1–T5, G2, G1 in RK66's
  §5 order per repeat → `calibration_66.json`. A5 is not priceable (no XL row for E1/E7). The pricing choices the
  orchestrator made are in the script's docstring and were pasted to the diagnosis, which accepted them.

## Readings — per sensor, per turn

| reading | subagent | engine (as printed) | prompt | prompt md5 | received = saved | turns | stop reason(s) | output tokens | continuations | tool uses |
|---|---|---|---|---|---|---|---|---|---|---|
| RK66-1 | `3a8:rates-step-c` | Lytin-K 1.1 | `prompt_C.md` | `7e8f83bd9c1f2391e2a32c8625f9fd85` | yes | 1 | end_turn | 17948 | none | 0 |

## Files

| file | bytes | md5 |
|---|---:|---|
| `RK66-1.md` | 17324 | `61abdd09f4e0fe366af7634880766cd8` |
| `calibration_66.json` | 14478 | `b67a98478cba3ac45c51f135b961de77` |
| `make_prompt_66.py` | 11334 | `c41f947ea0c92be0a46123203f1f4ca9` |
| `price_fills66.py` | 8431 | `1f273e6e1cfe2d644c870a3d26098ef6` |
| `prompt_C.md` | 27900 | `7e8f83bd9c1f2391e2a32c8625f9fd85` |
| `turns.jsonl` | 448 | `f29dab80f1f39ece6c3caf80331dea3f` |
