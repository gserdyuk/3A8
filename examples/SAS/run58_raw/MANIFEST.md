# Run 58 — manifest (step 2 only: the SAS work model, `Hotyn-W 1.2` × `HM57-1`, seven batches, n = 1)

**2026-09-15.** The product model `HM57-1` (`Hotyn-M 2.1`, run 57; 211 rows, 187 leaves, 24 nodes) crossed with the
approved SAS technology declaration by engine `Hotyn-W 1.2`, in seven partial runs by top-level subtree, n = 1 per
batch. Step 2 only, stopped there: nothing sized, nothing priced. This is the regression of stages 2–3 through the plugin
entry point on a 2.x model; the comparison is run 45 (`../run45_work_model.md`, `../run45_raw/`). **No run record is
written here**: the orchestrating session consolidates the seven replies and writes `run58_work_model.md`.

**Where the files are.** All in place in `examples/SAS/run58_raw/`:
- **Before this session:** `make_prompts58.py` and `prompt_A.md` … `prompt_G.md`, generated and pinned by the
  orchestrating session.
- **Written by this session, by Python scripts with exclusive create:** `HW58-A1.md` … `HW58-G1.md` and this
  `MANIFEST.md`. Nothing was refused and nothing went to the scratchpad.

## Registered before launch (from the launch instruction, verbatim in substance)

- (a) 210 of 210 batched elements classified; exactly 23 `aggregate` (the nodes below `N01`); no leaf `aggregate`.
- (b) Items per crossed element in the region 6.0–7.5 (run 45: 6.73).
- (c) Every refusal labelled filter or judgement. Judgement refusals are expected where run 45 had them (A5–A8 on
  parents whose subtree holds only statements; G2m–G4m on stores fed internally), and few elsewhere.
- (d) Each sensor prints `Hotyn-W 1.2` and finishes in one turn, without a continuation message, under the raised cap.
- A batch that classes a leaf `aggregate`, or generates an activity absent from INPUT 2, overturns that batch's reading.
  It is reported, not repaired.

**Outcome (by script from the replies as printed; the consolidated reading belongs to the run record):**
- **(a) met.** 210 of 210 classified. `aggregate` falls on exactly the 23 nodes: 5 + 3 + 2 + 2 + 6 + 3 + 2. No leaf is
  `aggregate` and every node is. Classes: behaviour 89 · surface 36 · store 26 · statement 20 · interface 16 ·
  aggregate 23.
- **No batch generated an activity absent from INPUT 2.** Checked on every activity id in §4 and §5. No batch is
  overturned.
- **(b) on the batch sums, not the consolidation:** 1 396 technology items / 210 = 6.65, inside 6.0–7.5. Batch G
  also stands one demanded branch, `DW-4`. Once-scoped and per-environment items and the root's per-parent items are
  outside every batch, as in run 45; the consolidated figure is the run record's.
- **(c) labelling met; the judgement pattern differs from run 45.**
  - 76 refusals: filter 70 · judgement 6.
  - The 6 judgement refusals: G2m–G4m on `A143` (batch A, the read store fed by `A144`) and G2m–G4m on `A017`
    (batch B, the role catalogue seeded with four roles).
  - None on A5–A8. Under 1.2, A5–A8 fired on every node of every batch.
  - Filter refusals by batch: A 30 · B 7 · C 4 · D 4 · E 7 · F 3 · G 15.
- **(d) met.** Seven of seven print `Hotyn-W 1.2`. Each ran one turn ending `end_turn`, with output tokens
  10 345–13 778 and no continuation message.

## Launch record

| field | value |
|---|---|
| entry point | `/3a8:estimate-product` (plugin skill), step 2 only |
| subagent | `3a8:work-crosser` (plugin registration of `agents/work-crosser.md`, stamp line ``You are engine `Hotyn-W 1.2` ``) |
| model | **claude-opus-5**, launched with the harness's `opus` alias (the launch tool offers `sonnet`, `opus`, `haiku`, `fable`, not a model id). Meta files: `"model":"opus"`, `"requestShape":"background"`, `"requestNonInteractive":true`. The `model` attachment records `claude-opus-5` ("Opus 5"); every assistant record records `claude-opus-5`, with `effort: "high"` |
| **output cap** | **`CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`**, read from this orchestrating process's environment (by script, `os.environ`) before launch. Not separately observable per subagent; no turn came near 64 000 (largest 13 778) |
| harness | Claude Agent SDK `0.3.271` (`CLAUDE_AGENT_SDK_VERSION`), entry point `claude-desktop` |
| repeats | **n = 1 per batch**, seven batches, each in its own context. Prompt text = the file's content, verbatim and entire, nothing added before or after |
| concurrency | at most four at once. A, B, C, D launched in one orchestrator message (prompt records 20:26:47Z–20:28:15Z); E launched after A's completion notification (prompt record 20:30:04Z); F and G in one message after B's and C's notifications (20:30:45Z, 20:31:18Z). Largest overlap by the transcript timestamps: 4 (A–D, 20:28:15Z–20:29:17Z) |
| repository state at launch | `main` at `eb40827`. `git status --porcelain` at the pre-launch check (after the probe, before A): `?? docs/proposal_architecture_declaration.md`, `?? examples/SAS/run58_raw/` |
| inputs | `prompt_A.md` … `prompt_G.md` (below). INPUT 2 (declaration) and INPUT 3 (demanded-work list, batch G only) are, per the launch instruction, byte-identical to run 45's. This session verified by script that the text from `# INPUT 2` to the end is identical across A–F, and that G has the same text followed by INPUT 3. It did not re-derive run 45's prompts |

## Version gate before the launch

- `3a8:version-probe` was launched in the foreground with the one-word prompt `Manifest.`. It answered with 11 lines,
  `tool_uses: 0`, 3 735 ms, 3 646 subagent tokens: `calibration-rates Lytin-K 1.1 · diagnostician Lytin-G 1.1 ·
  estimator-decomposition Lytin-D 5.0 · estimator-reference-class Lytin-R 1.1 · fp-counter Hotyn-P 1.0 ·
  fp-norms-author Hotyn-N 1.0 · model-builder Hotyn-M 2.1 · rate-table-author Hotyn-K 1.1 · rates-step-c Lytin-K 1.1 ·
  work-crosser Hotyn-W 1.2 · work-estimator Hotyn-D 2.0`.
- `PYTHONUTF8=1 py tools/check_probe.py` **ran** (Bash): every agent `ok`, `11 agents, 0 failing`,
  `work-crosser Hotyn-W 1.2`, `model-builder Hotyn-M 2.1`.
- The probe's answer equals the script's on-disk list line for line. **Gate: agree. Launch proceeded.**

## Prompt pins

md5 of the file bytes as on disk (no CR, final newline), computed by script before launch and again at manifest time:

| batch | subtrees · elements | chars | md5 on disk | expected (launch instruction) | transcript prompt record |
|---|---|---|---|---|---|
| A | N02 · 35 | 10 143 | `8d71d1e69559b1273629b91d4cda1c16` | `8d71d1e69559b1273629b91d4cda1c16` | equal to the file, byte for byte, final newline included |
| B | N06, N07, N10 · 30 | 9 805 | `f9c0bdc9b3e5d2e0e0ca76b7c858c7c4` | `f9c0bdc9b3e5d2e0e0ca76b7c858c7c4` | equal to the file, byte for byte, final newline included |
| C | N08, N09 · 26 | 9 319 | `e2b7f7b25500a281e666406575bc00ca` | `e2b7f7b25500a281e666406575bc00ca` | equal to the file, byte for byte, final newline included |
| D | N11, N12 · 26 | 9 699 | `ab8f59e36c65b2348ea345fc36541b1a` | `ab8f59e36c65b2348ea345fc36541b1a` | equal to the file, byte for byte, final newline included |
| E | N13 · 37 | 10 243 | `ab99d1d05404cbb543283e55a96f7f2b` | `ab99d1d05404cbb543283e55a96f7f2b` | equal to the file, byte for byte, final newline included |
| F | N19, N20 · 31 | 9 732 | `9ae9aa8b95ecb1b5a9541677f4a0e928` | `9ae9aa8b95ecb1b5a9541677f4a0e928` | equal to the file, byte for byte, final newline included |
| G | N21, N22 · 25 (+ INPUT 3) | 10 798 | `5bc0e7106ac0ab799b052fdd066a032a` | `5bc0e7106ac0ab799b052fdd066a032a` | equal to the file, byte for byte, final newline included |

## Per-sensor audit (from `subagents/agent-<id>.jsonl`, by script)

| | HW58-A1 | HW58-B1 | HW58-C1 | HW58-D1 | HW58-E1 | HW58-F1 | HW58-G1 |
|---|---|---|---|---|---|---|---|
| scope · elements | N02 · 35 | N06, N07, N10 · 30 | N08, N09 · 26 | N11, N12 · 26 | N13 · 37 | N19, N20 · 31 | N21, N22 · 25 (+ INPUT 3) |
| prompt record | 20:26:47.355Z | 20:27:17.166Z | 20:27:45.300Z | 20:28:15.286Z | 20:30:04.236Z | 20:30:45.122Z | 20:31:18.364Z |
| user records after the prompt | none | none | none | none | none | none | none |
| API messages | 1 (`msg_011Cf5rVRbjGEEBtR5RZSexu`) | 1 (`msg_011Cf5rXdokYw1SDxAqKipxe`) | 1 (`msg_011Cf5rZiDUAwvuwuRJMZroM`) | 1 (`msg_011Cf5rbutjbA2BdvKGY1eai`) | 1 (`msg_011Cf5rjwCb34Pog9sAKwrQv`) | 1 (`msg_011Cf5rnxsPDhMFWqAqXkVWE`) | 1 (`msg_011Cf5rqQ9UUx3WYkK8W2c9D`) |
| turn 1: first record (thinking, content empty in the transcript) | 20:28:29.100Z (1 min 41 s after the prompt) | 20:28:39.113Z (1 min 21 s after the prompt) | 20:28:58.742Z (1 min 13 s after the prompt) | 20:29:35.563Z (1 min 20 s after the prompt) | 20:31:37.546Z (1 min 33 s after the prompt) | 20:32:00.946Z (1 min 15 s after the prompt) | 20:33:04.790Z (1 min 46 s after the prompt) |
| turn 1: text block | one, **11 699 chars**, title to §9 | one, **10 968 chars**, title to §9 | one, **10 827 chars**, title to §9 | one, **11 172 chars**, title to §9 | one, **12 284 chars**, title to §9 | one, **11 339 chars**, title to §9 | one, **11 204 chars**, title to §9 |
| turn 1: end | 20:29:17.508Z | 20:29:25.508Z | 20:29:44.390Z | 20:30:24.781Z | 20:32:30.166Z | 20:32:48.355Z | 20:33:51.434Z |
| **turn 1: cap in force · stop reason · output tokens** | **128 000 · `end_turn` · 13 778** | **128 000 · `end_turn` · 11 429** | **128 000 · `end_turn` · 10 345** | **128 000 · `end_turn` · 11 480** | **128 000 · `end_turn` · 13 706** | **128 000 · `end_turn` · 10 642** | **128 000 · `end_turn` · 13 162** |
| continuation message injected | **no** ("Output token limit hit" occurs 0 times) | **no** ("Output token limit hit" occurs 0 times) | **no** ("Output token limit hit" occurs 0 times) | **no** ("Output token limit hit" occurs 0 times) | **no** ("Output token limit hit" occurs 0 times) | **no** ("Output token limit hit" occurs 0 times) | **no** ("Output token limit hit" occurs 0 times) |
| turns | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `tool_uses` (notification) · tool_use blocks (transcript) | 0 · 0 | 0 · 0 | 0 · 0 | 0 · 0 | 0 · 0 | 0 · 0 | 0 · 0 |
| duration (notification) | 150 172 ms | 128 361 ms | 119 106 ms | 129 505 ms | 145 953 ms | 123 269 ms | 153 087 ms |
| subagent tokens (notification) | 21 681 | 19 203 | 18 060 | 19 295 | 21 467 | 18 561 | 21 363 |
| models recorded | `claude-opus-5` only | `claude-opus-5` only | `claude-opus-5` only | `claude-opus-5` only | `claude-opus-5` only | `claude-opus-5` only | `claude-opus-5` only |
| `effort` on assistant records | `high` | `high` | `high` | `high` | `high` | `high` | `high` |
| harness attachments | environment, model, instructions, session_context, date, prompt_snapshot ×2 | environment, model, instructions, session_context, date, prompt_snapshot ×2 | environment, model, instructions, session_context, date, prompt_snapshot ×2 | environment, model, instructions, session_context, date, prompt_snapshot ×2 | environment, model, instructions, session_context, date, prompt_snapshot ×2 | environment, model, instructions, session_context, date, prompt_snapshot ×2 | environment, model, instructions, session_context, date, prompt_snapshot ×2 |
| engine stamp printed (§9) | **Engine `Hotyn-W 1.2`.** Partial run, subtree N02 of `HM57-1`, 35 elements. | **Engine `Hotyn-W 1.2`. Partial run: subtrees N06, N07, N10 of `HM57-1`, 30 elements.** | **Engine: `Hotyn-W 1.2`.** Partial run on subtrees N08 and N09 of `HM57-1`: 26 elements, no demanded-work list received. | **Engine `Hotyn-W 1.2`.** Partial run over the N11 and N12 subtrees of `HM57-1`: 26 elements, with the demanded-work list not supplied. | **Engine: `Hotyn-W 1.2`**. Partial run on the subtree rooted at N13 of `HM57-1` (37 elements). | **Engine: `Hotyn-W 1.2`.** Partial run over the subtrees N19 and N20 of `HM57-1`, 31 elements. | **Engine `Hotyn-W 1.2`.** Partial run: subtrees N21 and N22 of `HM57-1`, 25 elements. |

For comparison: run 45's run record states all seven stamped `Hotyn-W 1.1`, `tool_uses: 0`, Opus 5 via `opus`, every
reply complete from §1. It records no cap, stop reasons or output tokens.

## Ambient context the sensors received (by script, from the attachments)

The seven transcripts carry byte-identical `environment`, `model`, `instructions`, `session_context` and `date`
attachments.
- **`session_context`** carried:
  - a `userEmail` line (the user's address, with its use restriction);
  - a git snapshot: `Current branch: main`, `Git user: Gennadiy Serdyuk`, and `Status:`
    - `?? docs/proposal_architecture_declaration.md`
    - `?? examples/SAS/run58_raw/`
    - `?? examples/SAS/run59_raw/`
  - recent commit subjects, newest first:
    - `eb40827 measure: run 57 - the Hotyn-M 2.1 pair on SAS; equal-set leaves kept apart, the remaining spread is the skeleton`
    - `2faaad3 docs: estimate-product skill - the corridor line matches instrument.md §4 (assumed ρ = 0.5, not measured)`
    - `e8f8d07 feat: Hotyn-M 2.1 - identity by coverage set is for comparing models, not for building one; the output cap is a launch coordinate`
    - `8a1f01f measure: run 56 - the first Hotyn-M 2.0 pair on SAS; the output cap reaches subagents`
    - `53a8a4e measure: run 55 - first Hotyn-M 2.0 reading on SAS, n = 1; the smoke test fails on the harness cap`
- **`examples/SAS/run59_raw/`** was not in the status at the pre-launch check. It is in the snapshot of the first sensor
  (A, 20:26:47Z) and was last modified at 20:27:24Z. It was created by something other than this session, between the
  check and the first launch. This session did not open, modify or use it.
- **`instructions`** carried the memory index (`memory/MEMORY.md`).
- **`environment`** carried the working directory, the platform and the scratchpad path.

No attachment names a work-model count, an item figure or an estimate. The subjects name runs 55–57 and the Hotyn-M
changes, not the work crosser. All seven sensors reported the ambient context present and quarantined:
- F named the user email;
- G named "a user identity line";
- B named "commit subjects that mention earlier runs and an estimation skill".

## Transcription

Each raw file was produced by script (`build_raw58.py`): the orchestrator header, a blank line, then the single
assistant text block from the per-agent transcript, verbatim, with no final newline added (HM57's convention, checked
on `HM57-1.md`). The script refuses to overwrite. It refuses a batch whose transit is not one clean `end_turn` turn,
and none was refused. It checked that each file's body equals the extracted text. There is no seam in any file.

| reading | reached the orchestrator | source of the raw file | text blocks | body md5 | file md5 |
|---|---|---|---|---|---|
| HW58-A1 | whole, title to §9 | per-agent transcript | 1 (11 699 chars) | `281eac5b39ffa8f05278dbc90c83dd0e` | `5c8aa947c8026ef2fe97f72a5ff35199` |
| HW58-B1 | whole, title to §9 | per-agent transcript | 1 (10 968 chars) | `d3ea8bd8af991bb58210c04d5e00772f` | `b35f22780b16dd28a20b57b7da40a8b8` |
| HW58-C1 | whole, title to §9 | per-agent transcript | 1 (10 827 chars) | `8ab8039a7c7921889dd1d0763477b792` | `252ff9e058d13af69bfe243eed508b4a` |
| HW58-D1 | whole, title to §9 | per-agent transcript | 1 (11 172 chars) | `db9dddf4daed62d5f39f355e11d68f13` | `79d87c046a6a0dff0b8c01a1c0914570` |
| HW58-E1 | whole, title to §9 | per-agent transcript | 1 (12 284 chars) | `9da6641fd9a071c5778ea062e3738818` | `015d84113ef56fac662258786c5fc28c` |
| HW58-F1 | whole, title to §9 | per-agent transcript | 1 (11 339 chars) | `49d990b30b457e0c33e3ce0ad3140268` | `d6fdd3de5545fc5df7efcc8020dc3972` |
| HW58-G1 | whole, title to §9 | per-agent transcript | 1 (11 204 chars) | `e773eac1dc78deddf3f5a1396b8bb1ca` | `621c22b885f13848705dd28cf759cf97` |

## Deviations from run 45

1. **Engine `Hotyn-W 1.2`** on disk and in the probe; run 45 ran `1.1`. Under 1.2 the class follows position (every
   node `aggregate`, only nodes). **This is part of what the run measures.**
2. **Product model `HM57-1`** (`Hotyn-M 2.1`; 211 rows, 24 nodes, 187 leaves; nodes carry no coverage, derived leaves
   carry `trigger:`), against `HM44-OA1` (`Hotyn-M 1.1`, 246 rows). The batches follow HM57-1's top-level subtrees:
   A N02 · B N06, N07, N10 · C N08, N09 · D N11, N12 · E N13 · F N19, N20 · G N21, N22 (+ demanded-work list).
   Run 45's were S-01…S-14.
3. **Prompts** are generated by `make_prompts58.py`, not run 45's `make_prompts.py`. They add INPUT 1's description of
   leaves-only coverage, triggers and the derived node `CN01`. That paragraph is the same in every batch and names
   `CN01`, which is in batch A only. Six sensors (B–G) remarked that `CN01` is named but not listed, and crossed
   nothing for it.
4. **Demanded-work list** given to batch G only, as in run 45. Batches A–F each reported input 4 missing, as HW45-A1 did,
   and none stopped.
5. **Transcription**: all seven raw files are extracted by script from the per-agent transcript. In run 45, A, B, D
   and E were transcribed from the delivered reply, because the harness transcript was empty, and C, F and G came from
   the transcript.
6. **Output cap 128 000 recorded, with per-turn stop reason and output tokens.** Run 45 recorded neither. Every run 58
   turn is under 14 000 output tokens, so the cap was not approached in either run.
7. **Harness** SDK `0.3.271`; run 57 recorded `0.3.270`, and run 45's version is not recorded.
8. **Repository** at `eb40827`. The sensors' ambient status showed `run58_raw/`, the unrelated untracked
   `docs/proposal_architecture_declaration.md`, and `run59_raw/`, which another process created during this session.
9. **`effort: "high"`** on assistant records; run 45 does not record the field.
10. **Header wording.** The scope field in the seven raw headers reads e.g. `batch A: subtrees N02; 35 elements of
    HM57-1` (the generator joined two fields). It is left as written, because the files are exclusive-create and not
    edited after writing.
11. **Scripts** (session scratchpad, not part of the run's files):
    - `pins58.py`: prompt md5s, environment values, repository state.
    - `tails58.py`: preamble and INPUT 2/3 identity across batches.
    - `struct58.py`: record layout.
    - `audit58.py`: per-record audit, prompt-record equality, reply extraction.
    - `context58.py`: attachment contents and cross-batch identity; HM57 join convention.
    - `sections58.py`: §3 classes against node positions; §4/§5 activity ids against INPUT 2; §5 kinds.
    - `build_raw58.py`: raw files.
    - `make_manifest58.py`: this file.
