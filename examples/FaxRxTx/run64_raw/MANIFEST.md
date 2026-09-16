# run 64 — Demanded-work addendum (Hotyn-K 1.1), one reading — MANIFEST

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

- Instrument named by `technology_declaration.md` §3 and `tools/chain/README.md` for the demanded-work branches
  the crossing left standing (W-F48, W-F49, W-F50, W-F52). Prompt hand-written: the activities as worded, the
  sizing rule (once, single), the case profile's staffing rule (headcount undeclared → refuse), the team grade line.
  No figure of any kind.
- `price_addendum_64.py` prices the two rows it priced (E = (O+4M+P)/6), adds the layer to each repeat of run 63
  (no C3), and writes `addendum_summary.json`. W-F48 and W-F50 refused: carried, not priced.
- `docs/rate_table.md` was **not** amended (no existing file may be modified); the rows live here.

## Readings — per sensor, per turn

| reading | subagent | engine (as printed) | prompt | prompt md5 | received = saved | turns | stop reason(s) | output tokens | continuations | tool uses |
|---|---|---|---|---|---|---|---|---|---|---|
| HK64-1 | `3a8:rate-table-author` | Hotyn-K 1.1 | `prompt_K.md` | `4e77ebdc35e3ec98b2fecfff92da40f0` | yes | 1 | end_turn | 6106 | none | 0 |

## Files

| file | bytes | md5 |
|---|---:|---|
| `HK64-1.md` | 8780 | `6c556f6079c7cedc88da753d0a95402f` |
| `addendum_summary.json` | 680 | `4dd096a7a29577ed7d10d60566fb66c2` |
| `price_addendum_64.py` | 2402 | `fe058e494178aa1d9db93b249a6cb4b0` |
| `prompt_K.md` | 3144 | `4e77ebdc35e3ec98b2fecfff92da40f0` |
| `turns.jsonl` | 451 | `1b324b23a683d7fb10c7fbf3105ea8f4` |
