# Run 54 — manifest (step 1 only: the SAS product model, `Hotyn-M`, n = 2) — VOID, no reply

**2026-09-15.** Planned as the discriminating replay of run 53 stage 1: run 53 verbatim, with one factor removed.
That factor is the output-limit continuation, to be removed by a bounded thinking budget in the orchestrating
process. **The run produced no reply.** Both sensors were aborted by the harness's stream watchdog. Before the abort,
HM54-1's transcript shows that the budget was **not in force** for the sensor: its first turn again ran to the
64 000-token output limit and received the continuation message. The run record is `../run54_product_model.md`.

No raw reply files exist. `HM54-1.md` and `HM54-2.md` were **not written**, because neither sensor emitted a text
block.

**Where this file is.** Writing into `examples/SAS/` was refused by the permission layer ("sensitive file"). Both run
54 files were written under the session scratchpad at the same relative paths (`<scratchpad>/examples/SAS/…`), to be
copied into place.

## Launch record

| field | value |
|---|---|
| entry point | `/3a8:estimate-product` (plugin skill), step 1 — as run 53 |
| subagent | `3a8:model-builder` (stamp line `Hotyn-M 1.1` on disk) — as run 53 |
| model | **claude-opus-5**, launched with the harness's `opus` alias — as run 53. Meta files: `"model":"opus"`, `"requestShape":"background"`. The `model` attachment in both transcripts: `claude-opus-5`. HM54-1's one assistant turn records `claude-opus-5` |
| thinking budget | `MAX_THINKING_TOKENS=16000` in the orchestrating process's environment (read by a child process of the session: `os.environ`). `CLAUDE_CODE_MAX_OUTPUT_TOKENS` unset |
| repeats | n = 2, `HM54-1` and `HM54-2`, launched in one message, in the background, independent contexts |
| prompt | identical for both: 29 261 chars, md5 `d7ae952e153d9de062590b4229cb19b9`, computed from each agent's transcript. It equals run 53's prompt byte for byte **except the final newline**. With `\n` appended, md5 = `3fb20734599dfbf7ef1debee4b4c342d`, run 53's |
| system prompt | the harness's `prompt_snapshot` in both transcripts: 4 parts, 14 782 chars, md5 `6a2c08f25cb91c27b999ac18384a4827`. This is identical to both run 53 transcripts |
| harness attachments | environment, model, instructions (`memory/MEMORY.md`), session_context, date, prompt_snapshot. The same types, in the same order, as run 53. The MEMORY.md content was not compared |
| repository state at launch | `main` at `e96a8a8` (`.git/refs/heads/main`); working tree clean per the session's start snapshot |
| processing order | order A (I → G → P → L → D → NFR) |

## Version gate

- `3a8:version-probe` answered with 11 lines, `tool_uses: 0`: `calibration-rates Lytin-K 1.1 · diagnostician Lytin-G
  1.1 · estimator-decomposition Lytin-D 5.0 · estimator-reference-class Lytin-R 1.1 · fp-counter Hotyn-P 1.0 ·
  fp-norms-author Hotyn-N 1.0 · model-builder Hotyn-M 1.1 · rate-table-author Hotyn-K 1.1 · rates-step-c Lytin-K 1.1 ·
  work-crosser Hotyn-W 1.1 · work-estimator Hotyn-D 2.0`.
- `PYTHONUTF8=1 py tools/check_probe.py` **ran** in this session (Bash): `11 agents, 0 failing`, with every stamp as
  above.
- **Gate: agree. Launch proceeded.**

## Pinned inputs

Computed as `md5(file bytes with CR removed)` immediately before the launch:

| file | md5 | run 53 manifest | match |
|---|---|---|---|
| `requirements_product.md` (N = 146) | `db9fdc8ff77844f0b9bbb3881d292587` | `db9fdc8ff77844f0b9bbb3881d292587` | yes |
| `assumptions_product.md` v1 | `2540cfb1fca7a90a9f9c5cfb937718f1` | `2540cfb1fca7a90a9f9c5cfb937718f1` | yes |

## Prompt composition

This is **run 53's prompt itself, not a rebuild.** It was recovered from run 53's per-agent transcripts (session
`342e40fd…`, both agents, md5 `3fb20734…`) and pasted into both launches. So the composition is run 53's exactly: the
framing sentence, the input statement, order A, the quarantine paragraph with "a memory index", the output
instruction, then INPUT 1 and INPUT 2 pasted whole. The one byte of difference is noted above.

## Per-sensor audit (from `subagents/agent-<id>.jsonl`, by script)

| | HM54-1 | HM54-2 |
|---|---|---|
| launched (prompt record) | 2026-09-14T22:50:39.952Z | 2026-09-14T22:52:01.073Z |
| turn 1 | thinking only · **stop `max_tokens`** · **output 64 000** · ended 23:03:36.968Z (12 min 57 s) · the thinking block's content is empty in the transcript | **no assistant record** |
| continuation message injected | **yes, once**, at 23:03:36.980Z, `isMeta: true`, verbatim: "Output token limit hit. Resume directly — no apology, no recap of what you were doing. Pick up mid-thought if that is where the cut happened. Break remaining work into smaller pieces." | no |
| turn 2 | **no assistant record** | — |
| end | `[Request interrupted by user]` at 2026-09-15T04:01:15.660Z. Task status `failed`: "Agent stalled: no progress for 600s (stream watchdog did not recover)" | the same record, **the same timestamp to the millisecond**, the same failure |
| any turn hit `max_tokens` | yes (turn 1) | no turn completed |
| output tokens, total | 64 000 (all thinking) | 0 |
| text blocks emitted | 0 | 0 |
| `tool_uses` | 0 | 0 |

For comparison, run 53, audited from its transcripts by the same script:

| | turn 1 | continuation 1 | turn 2 | continuation 2 | turn 3 |
|---|---|---|---|---|---|
| HM53-1 | thinking · `max_tokens` · 64 000 · 12 min 10 s | yes | text · `end_turn` · 62 073 | — | — |
| HM53-2 | thinking · `max_tokens` · 64 000 · 12 min 30 s | yes | text · `max_tokens` · 64 000 | yes | text · `end_turn` · 14 746 |

The interrupt is not a user action. The user issued no interrupt, and `[Request interrupted by user]` is the record
the harness writes when the watchdog aborts. The two sensors stopped progressing at different points (HM54-1 after
the continuation, HM54-2 before its first turn ended), yet were aborted in the same millisecond, about five hours
after launch. That fits one abort of the whole background stream, not two independent sensor failures. The cause of
the stall is not recorded in the transcripts.

## Deviations from run 53

1. **Thinking budget.** `MAX_THINKING_TOKENS=16000` was set in the orchestrator's environment. This was the
   manipulation. **It did not take effect in the sensor**: HM54-1's first turn produced 64 000 output tokens of
   thinking, four times the budget, and stopped at `max_tokens` as run 53's did. The transcript does not show
   whether the variable failed to reach the sensor's request or reached it and was ignored for this model.
2. **Prompt final newline** absent (29 261 against 29 262 chars). Everything else is byte-identical.
3. **Check script executed** (`tools/check_probe.py`); run 53's was refused and done by hand.
4. **Repository** at `e96a8a8`; run 53 at `5971dc1`. Only the commit subjects in the quarantined ambient material
   differ.
5. **Transport failure**: both sensors aborted by the stream watchdog. No reply exists, no reading was taken, and the
   run is void.
6. **Files written to the scratchpad**, not `examples/SAS/` (permission refusal, as in run 53).

## Scripts

`find_prompt53.py` (prompt recovery and environment read), `audit54.py` (per-record audit and prompt comparison),
`parity54.py` (prompt bytes and attachment parity), `timeline54.py` (the timeline above) and run 53's
`compare_models.py` all live in session scratchpads and are not part of the run's files. `compare_models.py`
re-ran on run 44 and run 53 before this run's failure. It reproduced their figures exactly: 246 / 242 and 117 / 150
nodes, J = 0.451 and 0.569, cross-run 0.252 / 0.360 / 0.325 / 0.343.
