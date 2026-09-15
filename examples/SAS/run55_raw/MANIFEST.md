# Run 55 — manifest (step 1 only: the SAS product model, `Hotyn-M 2.0`, smoke test, n = 1)

**2026-09-15.** The re-baseline of `Hotyn-M 2.0` on the SAS cell (Opus 5 × order A), step 1 only, stopped there. The
engine is the variable: `agents/model-builder.md` is now `Hotyn-M 2.0` (coverage in leaves only). Everything else
reproduces run 53 (`run53_raw/MANIFEST.md`). The run record is `../run55_product_model.md`.

**Smoke test protocol.** One repeat first (HM55-1). The second (HM55-2) was to be launched only if HM55-1's first turn
ended `end_turn` with no continuation message. **It did not, so HM55-2 was not launched.** The run has one reading.

**Where this file is.** Writing into `examples/SAS/` was refused by the permission layer ("sensitive file"), as in
runs 53 and 54. `mkdir examples/SAS/run55_raw` was refused. All run 55 files were written under the session scratchpad
at the same relative paths (`<scratchpad>/examples/SAS/…`), to be copied into place.

## Registered before launch (from the launch instruction, verbatim in substance)

Anchored ≈ 232 at ≈ ×1.02 means the run 53 mechanism was the covered-by-posited-leaf verdict and 2.0 removed it;
≈ 120 again means it was not.

## Launch record

| field | value |
|---|---|
| entry point | `/3a8:estimate-product` (plugin skill), step 1 — as run 53 |
| subagent | `3a8:model-builder` (plugin registration of `agents/model-builder.md`, stamp line `You are engine \`Hotyn-M 2.0\``) |
| model | **claude-opus-5**, launched with the harness's `opus` alias (the launch tool offers `opus`, not a model id) — as run 53. Meta file: `"model":"opus"`, `"requestShape":"background"`, `"requestNonInteractive":true`. The `model` attachment records `claude-opus-5`; both assistant messages record `claude-opus-5` |
| repeats | **n = 1**, `HM55-1`, launched alone, in the background. `HM55-2` **not launched** (smoke test failed, see below) |
| prompt | 29 262 chars, md5 `3fb20734599dfbf7ef1debee4b4c342d`. Saved before launch as `run55_raw/prompt.md` (md5 of the saved file: `3fb20734599dfbf7ef1debee4b4c342d`). The prompt record in HM55-1's transcript equals the saved file byte for byte, final newline included |
| processing order | order A (I → G → P → L → D → NFR) |
| repository state at launch | `main` at `a120b2a`, `git status --porcelain` empty |
| HM55-1 | `tool_uses: 0` · 847 959 ms · 90 742 subagent tokens · sensor stamp `Hotyn-M 2.0` |

## Version gate before the launch

- `3a8:version-probe` answered with 11 lines, `tool_uses: 0`: `calibration-rates Lytin-K 1.1 · diagnostician Lytin-G
  1.1 · estimator-decomposition Lytin-D 5.0 · estimator-reference-class Lytin-R 1.1 · fp-counter Hotyn-P 1.0 ·
  fp-norms-author Hotyn-N 1.0 · model-builder Hotyn-M 2.0 · rate-table-author Hotyn-K 1.1 · rates-step-c Lytin-K 1.1 ·
  work-crosser Hotyn-W 1.2 · work-estimator Hotyn-D 2.0`.
- `PYTHONUTF8=1 py tools/check_probe.py` **ran** (Bash): every agent `ok`, `11 agents, 0 failing`, model-builder
  `Hotyn-M 2.0`, work-crosser `Hotyn-W 1.2`.
- The probe's answer equals the script's on-disk list line for line. **Gate: agree. Launch proceeded.**

## Pinned inputs

Computed as `md5(file bytes with CR removed)` immediately before the launch (by script):

| file | md5 | run 53 manifest | match |
|---|---|---|---|
| `requirements_product.md` (N = 146) | `db9fdc8ff77844f0b9bbb3881d292587` | `db9fdc8ff77844f0b9bbb3881d292587` | yes |
| `assumptions_product.md` v1 | `2540cfb1fca7a90a9f9c5cfb937718f1` | `2540cfb1fca7a90a9f9c5cfb937718f1` | yes |

The same script confirmed that both files, CR stripped, appear whole in the prompt text.

## Prompt composition

This is **run 53's prompt itself, not a rebuild**, as run 54 did. It was recovered by script from run 53's two
per-agent transcripts (session `342e40fd…`, agents `adf49242…` and `a410b03b…`). Both prompt records are identical,
29 262 chars, md5 `3fb20734…`, equal to run 53's manifest. The composition is therefore run 53's exactly:

1. the framing sentence ("Build the product model of the case below, as your engine definition requires.");
2. the input statement (whole input; INPUT 1 and INPUT 2 pasted whole; no file, no tool);
3. **Declared processing order: order A**;
4. the quarantine paragraph, with "a memory index" in the list;
5. the output instruction ("sections 1 to 9, every section the engine definition requires; in §6 give every node its
   parent; do not compact any section");
6. `# INPUT 1 — requirements_product.md`, pasted whole;
7. `# INPUT 2 — assumptions_product.md`, pasted whole.

**Not given:** any prior tree, any run 44 / 53 reading, any work model, rate, estimate, budget, deadline, duration or
team size, `requirements_work.md`, the technology declaration, the case profile.

The output instruction was written for `Hotyn-M 1.1`. It still names sections 1 to 9. `Hotyn-M 2.0` adds §7c and the
terminator lines, and 2.0's §6 asks for a TSV block, not a table. The prompt says nothing that contradicts these, and
"every section the engine definition requires" covers them. The wording was kept unchanged to hold the composition
fixed.

## Per-sensor audit (from `subagents/agent-<id>.jsonl`, by script)

| | HM55-1 |
|---|---|
| prompt record | 2026-09-15T05:12:25.761Z |
| turn 1 | first record 05:24:14.188Z (thinking block, content empty in the transcript), text block begun; **stop `max_tokens`** · **output 64 000** · ended 05:24:23.722Z (11 min 58 s after the prompt). Content: thinking, then **3 200 chars of text** (title, §1, §2 whole, the first 20 chars of the §3 pass-1 table header) |
| continuation message injected | **yes, once**, at 05:24:23.777Z, `isMeta: true`, verbatim: "Output token limit hit. Resume directly — no apology, no recap of what you were doing. Pick up mid-thought if that is where the cut happened. Break remaining work into smaller pieces." |
| turn 2 | thinking block (content empty) then text · **stop `end_turn`** · **output 14 592** · ended 05:26:33.671Z (2 min 10 s). **34 588 chars of text**, from the §3 pass-1 table header to §9 |
| output tokens, total | 78 592 (64 000 + 14 592) |
| text blocks | 2 (3 200 + 34 588 chars) |
| `tool_uses` | 0 |
| models recorded | `claude-opus-5` only |
| harness attachments | environment, model, instructions (`memory/MEMORY.md`), session_context, date, prompt_snapshot — the types run 54 listed for run 53. Their contents were not compared |

For comparison, run 53 and run 54, as audited in `run54_raw/MANIFEST.md`:

| | turn 1 | continuation 1 | turn 2 | continuation 2 | turn 3 |
|---|---|---|---|---|---|
| HM53-1 | thinking · `max_tokens` · 64 000 · 12 min 10 s | yes | text · `end_turn` · 62 073 | — | — |
| HM53-2 | thinking · `max_tokens` · 64 000 · 12 min 30 s | yes | text · `max_tokens` · 64 000 | yes | text · `end_turn` · 14 746 |
| HM54-1 | thinking · `max_tokens` · 64 000 · 12 min 57 s | yes | no record (watchdog abort) | — | — |
| **HM55-1** | **thinking + 3 200 chars text · `max_tokens` · 64 000 · 11 min 58 s** | **yes** | **text · `end_turn` · 14 592** | — | — |

## Smoke-test verdict

**FAILED.** The first turn stopped at `max_tokens` and a continuation message was injected. By the protocol, HM55-2 was
not launched. The failure is the same event as in runs 53 and 54, with one difference. HM55-1 began its text inside
turn 1 and wrote the skeleton (§1–§2) before the limit. The whole accretion log, completion, closure and readings
(§3–§9) were therefore written after the continuation message.

## Transcription

The raw file was produced by script, not by hand: the two assistant text blocks, taken from the per-agent transcript,
joined in order, with the orchestrator header above them. The script checked that the body of `HM55-1.md` equals the
joined text. The completion notification was not used as the source: it carried only the second text block, which
begins at §3's pass-1 table header. The seam at char 3 200 is described in the file's header.

| reading | reached the orchestrator | source of the raw file | text blocks |
|---|---|---|---|
| HM55-1 | **truncated at the head**: began at the §3 pass-1 table header | per-agent transcript | 2 (3 200 + 34 588 chars), joined verbatim |

All sections from §1 to §9, and §7c, are in the raw file. The counts parsed from §6 equal the sensor's own §8.

## Deviations from run 53

1. **Engine `Hotyn-M 2.0`** in place of 1.1. **This is the variable the run measures.** Work-crosser is `Hotyn-W 1.2`
   on disk; it is not used in step 1.
2. **n = 1, not n = 2.** This was the smoke-test protocol: HM55-2 depended on HM55-1's first turn ending clean, and it
   did not. There is no repeat spread and no within-run Jaccard.
3. **Launch shape.** One background launch alone, where run 53 launched two background launches in one message. The
   request shape is the same (`background`).
4. **Prompt replayed from run 53's transcripts**, byte-identical, final newline included. Run 53's own prompt was a
   rebuild of run 44's framing, so run 53's deviation 2 carries over unchanged.
5. **Check script executed** (`tools/check_probe.py`); run 53's was refused and done by hand.
6. **Repository** at `a120b2a`; run 53 at `5971dc1`. Only the commit subjects in the quarantined ambient material
   differ.
7. **Output-limit continuation**: once, as in HM53-1. It was injected after 3 200 chars of reply text (§1–§2), where
   run 53's came before any text. See *Smoke-test verdict*.
8. **Transit**: the notification was truncated at the head, inside §3. The reply was recovered whole from the
   transcript, with the seam inside §3's pass-1 header row.
9. **Files written to the scratchpad**, not `examples/SAS/` (permission refusal).
10. **Comparison relation.** Co-location is computed on the coverage sets of **leaves** as well as of all rows, because
    2.0 nodes carry no coverage. For run 44 and run 53 members the two relations are equal, except HM44-OA2: one
    internal node carries coverage there, giving 153 against 154 pairs.
11. **Comparison script.** A scratchpad script (`compare55.py`) extends run 53's `compare_models.py`. It reads 2.0's
    TSV §6 and computes the leaf relation. Before use it reproduced run 44's and run 53's recorded figures exactly:
    246 / 242 and 117 / 150 rows, J = 0.451 and 0.569, cross-run 0.252 / 0.360 / 0.325 / 0.343.

## Scripts

`recover_prompt53.py` (prompt recovery, pins, input presence), `audit55.py` (per-record audit and reply extraction),
`fmtcheck55.py` (2.0 output format), `logcheck55.py` (log-internal checks: verdicts per pass, leaves added per row,
nodes named in covering columns, identical coverage sets), `compare55.py` (counts and Jaccard). All live in the session
scratchpad and are not part of the run's files.
