# run 67 — Steps B and D (Lytin-G 1.1), one reading — MANIFEST

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

- Prompt built by `make_prompt_67.py`: description, log, case profile §1–§4 (its header disclosure and §5 withheld),
  `docs/instrument.md` §0 verbatim, the bottom-up reading with its declaration and `docs/instrument.md` §4 verbatim
  (one clause naming this case's outcome struck), RC65-1 and RC65-2 verbatim, RK66-1 verbatim, the priced chain.
  No outcome, no pointer to one beyond the pinned texts.

## Readings — per sensor, per turn

| reading | subagent | engine (as printed) | prompt | prompt md5 | received = saved | turns | stop reason(s) | output tokens | continuations | tool uses |
|---|---|---|---|---|---|---|---|---|---|---|
| RG67-1 | `3a8:diagnostician` | Lytin-G 1.1 | `prompt_G.md` | `97be5776420293c1d92e817e549345b8` | yes | 1 | end_turn | 21461 | none | 0 |

## Files

| file | bytes | md5 |
|---|---:|---|
| `RG67-1.md` | 18276 | `5df8342de761cf4ee5cc7bdec9ad9c83` |
| `make_prompt_67.py` | 10515 | `2f13ecd82c77a466cb4c7816f983c98c` |
| `prompt_G.md` | 86696 | `97be5776420293c1d92e817e549345b8` |
| `turns.jsonl` | 449 | `cf08a384ca9966465b4cac2a614a7bd2` |
