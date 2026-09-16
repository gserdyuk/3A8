# run 65 — Outside view (Lytin-R 1.1), n = 2 — MANIFEST

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

- Launched in parallel with the first product-model launch, separate instances, same prompt `prompt_R.md`.
- Description = `SYSTEM.md` with four passages struck in place (the calendar period of the work; the acquisition,
  its price and revenue and a dating inference; the pointer to where the outcome is kept; the closing note on
  `REQUIREMENTS.md`). The assumption log is pasted verbatim — it still carries the era (A5, 2007–2009) and the
  immersion stage's ~1–2 months (A1, A3); both sensors declared the latter and did not use it as an anchor.

## Readings — per sensor, per turn

| reading | subagent | engine (as printed) | prompt | prompt md5 | received = saved | turns | stop reason(s) | output tokens | continuations | tool uses |
|---|---|---|---|---|---|---|---|---|---|---|
| RC65-1 | `3a8:estimator-reference-class` | Lytin-R 1.1 | `prompt_R.md` | `a433c52a04f1a6fd39836f83dde136f8` | yes | 1 | end_turn | 8310 | none | 0 |
| RC65-2 | `3a8:estimator-reference-class` | Lytin-R 1.1 | `prompt_R.md` | `a433c52a04f1a6fd39836f83dde136f8` | yes | 1 | end_turn | 10190 | none | 0 |

## Files

| file | bytes | md5 |
|---|---:|---|
| `RC65-1.md` | 16215 | `d8291ff3eae52f63515efbc914c3e651` |
| `RC65-2.md` | 18766 | `68557cbee6de5b9a3fc049de3a9ce391` |
| `prompt_R.md` | 10544 | `a433c52a04f1a6fd39836f83dde136f8` |
| `turns.jsonl` | 921 | `9ee62a20804b6756ed7998140308fbaa` |
