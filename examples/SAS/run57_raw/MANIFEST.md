# Run 57 — manifest (step 1 only: the SAS product model, `Hotyn-M 2.1`, re-baseline, n = 2)

**2026-09-15.** Run 56 repeated under engine `Hotyn-M 2.1`. Step 1 only, stopped there. The variable is the engine:
one sentence of M2 changed (identity by coverage set is for comparing models, not for building one). The prompt (run
56's, byte for byte), the inputs, the model, the order and the harness cap are unchanged. The run record is
`../run57_product_model.md`.

**Where the files are.** Split by how they were written:
- **In place** in `examples/SAS/run57_raw/`, by Python scripts, each with exclusive create: `prompt.md` (before launch),
  `HM57-1.md` and `HM57-2.md` (after the audit).
- **In the session scratchpad** at the same relative paths (`<scratchpad>/examples/SAS/…`): this `MANIFEST.md` and
  `run57_product_model.md`. The permission layer refused the Write tool's edit into `examples/SAS/` as a sensitive
  file, and the refusal was not worked around. Both are to be copied into place.

## Registered before launch (from the launch instruction, verbatim in substance)

2.1 pins the HM56-1 reading. Expected:
- both repeats at ≥ 1.3 leaves per adding row;
- accreted in the region of 150–160 (HM56-1: 154; run 44 OA1: 160);
- a pair spread narrower than run 56's ×1.26.

Alternative outcomes:
- A repeat that again merges equal-set leaves (§9 stating a merge, ≤ 1.1 leaves per adding row) means the sentence is
  still read as a build rule.
- A pair at ≈ 140 with ≥ 1.3 leaves per row means the remaining gap to run 44 is elsewhere (the skeleton's size).

**Outcome (by script; reading in the run record §5):** ≥ 1.3 met (1.50, 1.55); accreted 150–160 **not met**, above it
(171, 175); spread narrower met (anchored ×1.11); no merge; not ≈ 140 (194, 216).

## Launch record

| field | value |
|---|---|
| entry point | `/3a8:estimate-product` (plugin skill), step 1 — as run 56 |
| subagent | `3a8:model-builder` (plugin registration of `agents/model-builder.md`, stamp line ``You are engine `Hotyn-M 2.1` ``) |
| model | **claude-opus-5**, launched with the harness's `opus` alias (the launch tool offers `sonnet`, `opus`, `haiku`, `fable`, not a model id) — as run 56. Meta files: `"model":"opus"`, `"requestShape":"background"`, `"requestNonInteractive":true`. The `model` attachment records `claude-opus-5` ("Opus 5"); every assistant record records `claude-opus-5`. Assistant records carry `effort: "high"` (not recorded in run 56's manifest) |
| **output cap** | **`CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`**, read from this orchestrating process's environment (by script, `os.environ`) before launch — the same value as run 56. Not separately observable per subagent; HM57-2's single turn at 69 987 output tokens exceeds 64 000, and HM57-1's ended `end_turn` at 64 004 |
| harness | Claude Agent SDK `0.3.270` (`CLAUDE_AGENT_SDK_VERSION`), entry point `claude-desktop` — as run 56 |
| repeats | **n = 2**. `HM57-1` and `HM57-2` launched in **one orchestrator message**, both in the background, each in its own context. Prompt records 14:11:31.888Z and 14:12:53.060Z; they ran concurrently |
| prompt | 29 262 chars, md5 `3fb20734599dfbf7ef1debee4b4c342d`. **Copied byte for byte** from `run56_raw/prompt.md` (29 410 bytes, no CR, final newline) to `run57_raw/prompt.md` before launch, by script (exclusive create); md5 of the copy `3fb20734599dfbf7ef1debee4b4c342d`, bytes identical. Both transcripts' prompt records equal the saved file, final newline included (by script) |
| processing order | order A (I → G → P → L → D → NFR) |
| repository state at launch | `main` at `2faaad3`, `git status --porcelain` empty before the prompt copy; `?? examples/SAS/run57_raw/` after it |
| HM57-1 | `tool_uses: 0` · 710 688 ms · 74 989 subagent tokens · sensor stamp `Hotyn-M 2.1` |
| HM57-2 | `tool_uses: 0` · 778 232 ms · 80 249 subagent tokens · sensor stamp `Hotyn-M 2.1` |

## Version gate before the launch

- `3a8:version-probe` answered with 11 lines, `tool_uses: 0`: `calibration-rates Lytin-K 1.1 · diagnostician Lytin-G
  1.1 · estimator-decomposition Lytin-D 5.0 · estimator-reference-class Lytin-R 1.1 · fp-counter Hotyn-P 1.0 ·
  fp-norms-author Hotyn-N 1.0 · model-builder Hotyn-M 2.1 · rate-table-author Hotyn-K 1.1 · rates-step-c Lytin-K 1.1 ·
  work-crosser Hotyn-W 1.2 · work-estimator Hotyn-D 2.0`.
- `PYTHONUTF8=1 py tools/check_probe.py` **ran** (Bash): every agent `ok`, `11 agents, 0 failing`,
  `model-builder Hotyn-M 2.1`.
- The probe's answer equals the script's on-disk list line for line. **Gate: agree. Launch proceeded.**

## Pinned inputs

Computed as `md5(file bytes with CR removed)` immediately before the launch (by script):

| file | md5 | run 56 manifest | match |
|---|---|---|---|
| `requirements_product.md` (N = 146) | `db9fdc8ff77844f0b9bbb3881d292587` | `db9fdc8ff77844f0b9bbb3881d292587` | yes |
| `assumptions_product.md` v1 | `2540cfb1fca7a90a9f9c5cfb937718f1` | `2540cfb1fca7a90a9f9c5cfb937718f1` | yes |

The same script confirmed that both files, CR stripped, appear whole in the prompt text.

## Prompt composition

Run 56's prompt file itself (hence runs 53 and 55's composition): framing sentence; input statement; **declared
processing order A**; the quarantine paragraph; the output instruction; `# INPUT 1 — requirements_product.md` pasted
whole; `# INPUT 2 — assumptions_product.md` pasted whole. **Not given:** any prior tree, any run 44 / 53 / 55 / 56
reading, any work model, rate, estimate, budget, deadline, duration or team size, `requirements_work.md`, the
technology declaration, the case profile.

## Per-sensor audit (from `subagents/agent-<id>.jsonl`, by script)

| | HM57-1 | HM57-2 |
|---|---|---|
| prompt record | 14:11:31.888Z | 14:12:53.060Z |
| user records after the prompt | none | none |
| API messages | 1 (`msg_011Cf5Msiv1pkRUAD2SkW7Lv`) | 1 (`msg_011Cf5MyhjjkcQYeVo7AsAmp`) |
| turn 1: first record (thinking block, content empty in the transcript) | 14:20:44.927Z (9 min 13 s after the prompt) | 14:23:01.489Z (10 min 08 s after the prompt) |
| turn 1: text block | one, **39 228 chars**, title to §9 | one, **41 269 chars**, title to §9 |
| turn 1: end | 14:23:22.533Z | 14:25:51.250Z |
| **turn 1: cap in force · stop reason · output tokens** | **128 000 · `end_turn` · 64 004** | **128 000 · `end_turn` · 69 987** |
| continuation message injected | **no** ("Output token limit hit" occurs 0 times in the transcript) | **no** (0 times) |
| turns | 1 | 1 |
| output tokens, total | 64 004 | 69 987 |
| `tool_uses` | 0 | 0 |
| models recorded | `claude-opus-5` only | `claude-opus-5` only |
| harness attachments | environment, model, instructions (`memory/MEMORY.md`), session_context, date, prompt_snapshot ×2 | the same |
| engine stamp printed (§8) | `**Engine: Hotyn-M 2.1**` | `**Hotyn-M 2.1**` (the word `Engine:` omitted) |

For comparison, the earlier audits (`run55_raw/MANIFEST.md`, `run56_raw/MANIFEST.md`):

| | engine | turn 1 | continuation 1 | turn 2 | turn 3 |
|---|---|---|---|---|---|
| HM53-1 | 1.1 | thinking · `max_tokens` · 64 000 | yes | text · `end_turn` · 62 073 | — |
| HM53-2 | 1.1 | thinking · `max_tokens` · 64 000 | yes | text · `max_tokens` · 64 000 | text · `end_turn` · 14 746 |
| HM55-1 | 2.0 | thinking + text · `max_tokens` · 64 000 | yes | text · `end_turn` · 14 592 | — |
| HM56-1 | 2.0 | thinking + text · `end_turn` · 79 883 | no | — | — |
| HM56-2 | 2.0 | thinking + text · `end_turn` · 92 565 | no | — | — |
| **HM57-1** | **2.1** | **thinking + 39 228 chars text · `end_turn` · 64 004 · 11 min 51 s** | **no** | — | — |
| **HM57-2** | **2.1** | **thinking + 41 269 chars text · `end_turn` · 69 987 · 12 min 58 s** | **no** | — | — |

Both run 57 turns are shorter in output than run 56's. HM57-1's 64 004 would have been cut under the old 64 000 cap by
4 tokens. Under the raised cap it was not cut, so the pair is one instrument with run 56.

## Ambient context the sensors received (by script, from the attachments)

The `session_context` attachment carried the git snapshot taken at subagent launch:
- `Status: ?? examples/SAS/run57_raw/`;
- recent commit subjects, newest first:
  - `2faaad3 docs: estimate-product skill - the corridor line matches instrument.md §4 (assumed ρ = 0.5, not measured)`
  - `e8f8d07 feat: Hotyn-M 2.1 - identity by coverage set is for comparing models, not for building one; the output cap is a launch coordinate`
  - `8a1f01f measure: run 56 - the first Hotyn-M 2.0 pair on SAS; the output cap reaches subagents`
  - `53a8a4e measure: run 55 - …`, `a120b2a feat: Hotyn-M 2.0 - …`

The `instructions` attachment carried the memory index. None of it names a count or an estimate. The `e8f8d07` subject
restates the change that the engine definition itself states in *Engine identity*. Both sensors reported the ambient
context present and quarantined.

## Transcription

Each raw file was produced by script (`build_raw57.py`): the orchestrator header, a blank line, then the single
assistant text block from the per-agent transcript, verbatim. The script refuses to overwrite and checked that each
file's body equals the extracted text. There is no seam in either file.

| reading | reached the orchestrator | source of the raw file | text blocks | body md5 | file md5 |
|---|---|---|---|---|---|
| HM57-1 | whole, title to §9 | per-agent transcript | 1 (39 228 chars) | `a314277d7b30a4d4e4318fa1e211b52a` | `fe3f91c7aef9e55b499b24e884625014` |
| HM57-2 | whole, title to §9 | per-agent transcript | 1 (41 269 chars) | `68137e3a6f30c3e08b5b15f9907ce422` | `98890f98f6d38d9863f8836a63b41659` |

## Deviations from run 56

1. **Engine `Hotyn-M 2.1`** on disk and in the probe; run 56 ran `2.0`. **This is the variable the run measures.**
2. **Launch shape.** Both repeats launched together, in one orchestrator message, and ran concurrently; run 56 launched
   HM56-2 only after HM56-1's audit (its registered gate). Run 57 had no such gate.
3. **Repository** at `2faaad3`; run 56 at `53a8a4e`. The newest subjects visible to the sensors now include the 2.1
   change (`e8f8d07`) and run 56's result line (`8a1f01f`). Neither names a count. The ambient git status also showed
   the untracked `examples/SAS/run57_raw/` (the prompt copy made before launch).
4. **File placement split.** `prompt.md` and the two raw files were written in place by scripts. This manifest and the
   run record were refused by the permission layer and live in the scratchpad. Runs 53–56 put everything in the
   scratchpad.
5. **`effort: "high"`** is recorded on the assistant records. Run 56's manifest does not mention the field, so whether
   it differed is unknown.
6. **Probe prompt.** The version probe was launched with the one-word prompt `Manifest.`; run 56's manifest does not
   record its probe prompt.
7. **Scripts.**
   - `pins57.py`: environment value, pins, input presence, repository state.
   - `copy_prompt57.py`: prompt copy and md5.
   - `promptcheck57.py`: transcript prompt against the file.
   - `audit57.py`: per-record audit and reply extraction.
   - `ambient57.py`: attachment contents.
   - `build_raw57.py`: raw files.
   - `analyze57.py`: parses §3, §6, §9 of 2.x replies and run 44's 1.1 tables; leaf co-location relations, Jaccard,
     identical sets, grain. Before use it reproduced run 56's recorded figures exactly: rows 198 / 156 / 154; leaf
     assignments 314 / 245 / 283; pairs 292 / 294 / 494 and run 44's 155 / 153; rows that added 111 / 105 / 112; rows
     adding more than one leaf 26 / 7 / 0; identical-set groups 15 / 39, 0, 0; flags 18 / 19 / 11; every J, ceiling
     and containment in run 56's table.
   - `logcheck57.py`: §2 scope length, §3 node references, derived coverage, §7 lifts, terminators.

   All live in the session scratchpad and are not part of the run's files.
