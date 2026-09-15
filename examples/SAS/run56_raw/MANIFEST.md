# Run 56 — manifest (step 1 only: the SAS product model, `Hotyn-M 2.0`, the harness lever, n = 2)

**2026-09-15.** Run 55 repeated with the per-turn output cap raised. Step 1 only, stopped there. The variable is the
harness: this orchestrating process runs with `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`. The engine (`Hotyn-M 2.0` on
disk), the prompt (run 55's, byte for byte), the inputs, the model and the order are unchanged. The run record is
`../run56_product_model.md`.

**Where this file is.** `mkdir examples/SAS/run56_raw` was not approved by the permission layer in this
non-interactive session, as in runs 53–55. All run 56 files were written under the session scratchpad at the same
relative paths (`<scratchpad>/examples/SAS/…`), to be copied into place.

## Registered before launch (from the launch instruction, verbatim in substance)

(a) If HM56-1's first turn ends `end_turn` with no continuation message, the variable applies to subagents and the
harness factor is removed; then launch HM56-2 the same way, so that run 56 gives the 2.0 pair. (b) If it stops at
`max_tokens` again, the variable does not reach subagents; do not launch HM56-2. Either way, HM56-1's anchored count
beside run 55's 139 says whether the cap and the injected message moved the level.

**Outcome: (a).** HM56-1's only turn ended `end_turn` at 79 883 output tokens with no continuation message. HM56-2 was
launched the same way and also ended `end_turn` (92 565), with no continuation.

## Launch record

| field | value |
|---|---|
| entry point | `/3a8:estimate-product` (plugin skill), step 1 — as run 55 |
| subagent | `3a8:model-builder` (plugin registration of `agents/model-builder.md`, stamp line `You are engine \`Hotyn-M 2.0\``) |
| model | **claude-opus-5**, launched with the harness's `opus` alias (the launch tool offers `opus`, not a model id) — as run 55. Meta files: `"model":"opus"`, `"requestShape":"background"`, `"requestNonInteractive":true`. The `model` attachment records `claude-opus-5`; every assistant record records `claude-opus-5` |
| **output cap** | **`CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`**, read from this orchestrating process's environment (by script, `os.environ`) before launch. Subagents run inside this process; the value is not separately observable per subagent — the evidence that it reached them is each sensor's single turn exceeding 64 000 output tokens. Run 55's manifest did not record the variable; its first turn stopped at exactly 64 000 |
| harness | Claude Agent SDK `0.3.270` (`CLAUDE_AGENT_SDK_VERSION`), entry point `claude-desktop` |
| repeats | **n = 2**. `HM56-1` launched alone, in the background; `HM56-2` launched alone, in the background, after HM56-1's transcript audit returned outcome (a) |
| prompt | 29 262 chars, md5 `3fb20734599dfbf7ef1debee4b4c342d`. **Copied byte for byte** from `run55_raw/prompt.md` (29 410 bytes, no CR, final newline) to `run56_raw/prompt.md` before the first launch, by script; md5 of the copy `3fb20734599dfbf7ef1debee4b4c342d`, bytes identical. Both transcripts' prompt records equal the saved file, final newline included |
| processing order | order A (I → G → P → L → D → NFR) |
| repository state at launch | `main` at `53a8a4e`, `git status --porcelain` empty |
| HM56-1 | `tool_uses: 0` · 849 702 ms · 90 630 subagent tokens · sensor stamp `Hotyn-M 2.0` |
| HM56-2 | `tool_uses: 0` · 999 862 ms · 104 294 subagent tokens · sensor stamp `Hotyn-M 2.0` |

## Version gate before the launch

- `3a8:version-probe` answered with 11 lines, `tool_uses: 0`: `calibration-rates Lytin-K 1.1 · diagnostician Lytin-G
  1.1 · estimator-decomposition Lytin-D 5.0 · estimator-reference-class Lytin-R 1.1 · fp-counter Hotyn-P 1.0 ·
  fp-norms-author Hotyn-N 1.0 · model-builder Hotyn-M 2.0 · rate-table-author Hotyn-K 1.1 · rates-step-c Lytin-K 1.1 ·
  work-crosser Hotyn-W 1.2 · work-estimator Hotyn-D 2.0`.
- `PYTHONUTF8=1 py tools/check_probe.py` **ran** (Bash): every agent `ok`, `11 agents, 0 failing`.
- The probe's answer equals the script's on-disk list line for line. **Gate: agree. Launch proceeded.**

## Pinned inputs

Computed as `md5(file bytes with CR removed)` immediately before the launch (by script):

| file | md5 | run 55 manifest | match |
|---|---|---|---|
| `requirements_product.md` (N = 146) | `db9fdc8ff77844f0b9bbb3881d292587` | `db9fdc8ff77844f0b9bbb3881d292587` | yes |
| `assumptions_product.md` v1 | `2540cfb1fca7a90a9f9c5cfb937718f1` | `2540cfb1fca7a90a9f9c5cfb937718f1` | yes |

The same script confirmed that both files, CR stripped, appear whole in the prompt text.

## Prompt composition

Run 55's prompt file itself (hence run 53's composition): framing sentence; input statement; **declared processing
order A**; the quarantine paragraph; the output instruction; `# INPUT 1 — requirements_product.md` pasted whole;
`# INPUT 2 — assumptions_product.md` pasted whole. **Not given:** any prior tree, any run 44 / 53 / 55 reading, any
work model, rate, estimate, budget, deadline, duration or team size, `requirements_work.md`, the technology
declaration, the case profile.

## Per-sensor audit (from `subagents/agent-<id>.jsonl`, by script)

| | HM56-1 | HM56-2 |
|---|---|---|
| prompt record | 05:58:42.119Z | 06:14:42.734Z |
| API messages | 1 | 1 |
| turn 1: first record (thinking block, content empty in the transcript) | 06:10:17.730Z (11 min 36 s after the prompt) | 06:29:05.662Z (14 min 23 s after the prompt) |
| turn 1: text block | one, **42 009 chars**, title to §9 | one, **38 467 chars**, title to §9 |
| turn 1: end | 06:12:51.753Z | 06:31:22.530Z |
| **turn 1: stop reason · output tokens** | **`end_turn` · 79 883** | **`end_turn` · 92 565** |
| continuation message injected | **no** ("Output token limit hit" occurs 0 times in the transcript) | **no** (0 times) |
| turns | 1 | 1 |
| output tokens, total | 79 883 | 92 565 |
| `tool_uses` | 0 | 0 |
| models recorded | `claude-opus-5` only | `claude-opus-5` only |
| harness attachments | environment, model, instructions (`memory/MEMORY.md`), session_context, date, prompt_snapshot — the types run 55 listed | the same |
| engine stamp printed (§8) | `Engine: Hotyn-M 2.0` | `Engine: Hotyn-M 2.0` |

For comparison, the earlier audits (`run54_raw/MANIFEST.md`, `run55_raw/MANIFEST.md`):

| | turn 1 | continuation 1 | turn 2 | continuation 2 | turn 3 |
|---|---|---|---|---|---|
| HM53-1 | thinking · `max_tokens` · 64 000 · 12 min 10 s | yes | text · `end_turn` · 62 073 | — | — |
| HM53-2 | thinking · `max_tokens` · 64 000 · 12 min 30 s | yes | text · `max_tokens` · 64 000 | yes | text · `end_turn` · 14 746 |
| HM54-1 | thinking · `max_tokens` · 64 000 · 12 min 57 s | yes | no record (watchdog abort) | — | — |
| HM55-1 | thinking + 3 200 chars text · `max_tokens` · 64 000 · 11 min 58 s | yes | text · `end_turn` · 14 592 | — | — |
| **HM56-1** | **thinking + 42 009 chars text · `end_turn` · 79 883 · 14 min 10 s** | **no** | — | — | — |
| **HM56-2** | **thinking + 38 467 chars text · `end_turn` · 92 565 · 16 min 40 s** | **no** | — | — | — |

Both run 56 turns exceed the 64 000 cap that cut every audited run 53–55 turn 1. Under that cap both would have been
cut.

## Transcription

Each raw file was produced by script (`build_raw56.py`): the orchestrator header, a blank line, then the single
assistant text block from the per-agent transcript, verbatim. The script checked that each file's body equals the
extracted text. There is no seam in either file.

| reading | reached the orchestrator | source of the raw file | text blocks | body md5 |
|---|---|---|---|---|
| HM56-1 | whole, title to §9 | per-agent transcript | 1 (42 009 chars) | `d22a2deff87cf3ad7eae7dd26e6e999b` |
| HM56-2 | whole, title to §9 | per-agent transcript | 1 (38 467 chars) | `4ce63c5bf3abe3d39d9f26d32f59ffd5` |

## Deviations from run 55

1. **`CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`** in the orchestrating process. **This is the variable the run measures.**
   Run 55 did not record the variable.
2. **n = 2, not n = 1**: registered outcome (a) held, so HM56-2 was launched.
3. **Launch shape.** Two background launches, each alone, the second after the first's audit. Run 55 had one.
4. **Prompt copied from `run55_raw/prompt.md`**, not recovered from transcripts; byte-identical to run 55's.
5. **Repository** at `53a8a4e`; run 55 at `a120b2a`. The ambient material the harness prepends differs in the commit
   subjects: the newest subject visible to the sensors is run 55's commit ("measure: run 55 - first Hotyn-M 2.0 reading
   on SAS, n = 1; the smoke test fails on the harness cap"). It names no count. Both sensors reported the ambient
   context present and quarantined.
6. **No output-limit continuation** in either sensor; run 55's HM55-1 had one.
7. **Transit**: no truncation, no seam; run 55's notification was truncated at the head.
8. **Files written to the scratchpad**, not `examples/SAS/` (permission layer), as in run 55.
9. **Scripts.** `pins56.py` (environment value, pins, input presence, repository state), `copy_prompt56.py` (prompt
   copy and md5), `audit56.py` (per-record audit and reply extraction; `audit55.py` for this session), `build_raw56.py`
   (raw files), `logcheck56.py` (`logcheck55.py` generalised to any id scheme and to backticked terminators; before use
   it reproduced run 55's recorded HM55-1 checks: 112 / 112 leaves per adding row, 0 identical sets, 11 flags),
   `compare56.py` (runs run 55's `compare55.py` unchanged and adds the J ceiling and the containment column; before use
   it reproduced run 55's recorded figures: J 0.418 / 0.471 / 0.258 / 0.207, ceilings 0.702 / 0.727 / 0.314 / 0.310,
   containment 0.715 / 0.760 / 0.858 / 0.725). All live in the session scratchpad and are not part of the run's files.
