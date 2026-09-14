# Run 53 — manifest (step 1 only: the SAS product model, `Hotyn-M`, n = 2)

**2026-09-15.** Stage 1 of a regression run of the `/3a8:estimate-product` plugin entry point against runs 44–47.
This launch does step 1 and stops; steps 2–4 are launched separately later. The comparison target is run 44
(`run44_product_model_measurement.md`, `run44_raw/`). The run record is `../run53_product_model.md`.

This is the **relaunch**. A previous attempt the same day was cut off before its replies arrived. It wrote only a
manifest, and no replies from it exist. Nothing from it is counted; its prompt composition and md5 check are reused
here verbatim.

**Where this file is.** Writing into `examples/SAS/` was refused by the permission layer in this session too
("sensitive file"). All run 53 files were written under the session scratchpad at the same relative paths
(`<scratchpad>/examples/SAS/…`), to be copied into place.

## Launch record (the orchestrator's half of the stamp)

| field | value |
|---|---|
| entry point | `/3a8:estimate-product` (plugin skill), step 1 |
| subagent | `3a8:model-builder` (plugin registration of `agents/model-builder.md`, stamp line `You are engine \`Hotyn-M 1.1\``) |
| model | **claude-opus-5**, launched with the harness's `opus` alias — the run 44 coordinate. Both transcripts record `claude-opus-5` on every assistant turn; the agents' meta files record `"model":"opus"`, `"requestShape":"background"` |
| repeats | n = 2, `HM53-1` and `HM53-2`, launched in one message, in the background, independent contexts |
| prompt | identical for both: 29 262 chars, md5 `3fb20734599dfbf7ef1debee4b4c342d`, computed from each agent's transcript |
| processing order | order A (I → G → P → L → D → NFR) |
| repository state at launch | `main` at `5971dc1`, working tree clean (`git status --porcelain` empty) |
| HM53-1 | `tool_uses: 0` · 1 399 474 ms · 70 183 subagent tokens · sensor stamp `Hotyn-M 1.1` |
| HM53-2 | `tool_uses: 0` · 1 573 128 ms · 89 078 subagent tokens · sensor stamp `Hotyn-M 1.1` |

## Pinned inputs

Computed as the pins say, `tr -d '\r' < FILE | md5sum`, immediately before the launch:

| file | md5 | run 44 | match |
|---|---|---|---|
| `requirements_product.md` (N = 146) | `db9fdc8ff77844f0b9bbb3881d292587` | `db9fdc8ff77844f0b9bbb3881d292587` | yes |
| `assumptions_product.md` v1 | `2540cfb1fca7a90a9f9c5cfb937718f1` | `2540cfb1fca7a90a9f9c5cfb937718f1` | yes |

## Prompt composition (identical for both repeats)

In this order:

1. One framing sentence: build the product model of the case below, as the engine definition requires.
2. **Input statement**: the message is the whole input; INPUT 1 and INPUT 2 pasted whole; do not read, open, list or
   search any file, use no tool.
3. **Declared processing order: order A**, the table order of INPUT 1, top to bottom (I → G → P → L → D → NFR).
4. **Quarantine instruction**, the standing paragraph in the wording of `run45_raw/make_prompts.py` line 152, with
   "a memory index" added to the list of ambient material.
5. **Output instruction**: the complete deliverable in one reply, sections 1 to 9, every section the engine
   definition requires. §6 must give every node its parent. No compaction of any section.
6. `# INPUT 1 — requirements_product.md`: the file pasted whole, heading to pin section.
7. `# INPUT 2 — assumptions_product.md`: the file pasted whole, heading to pin section.

**Not given:** any prior tree, any run 44 reading, any work model, rate, estimate, budget, deadline, duration or team
size, `requirements_work.md`, the technology declaration, the case profile.

The inputs were pasted as read from disk. Two things differ from the bytes on disk: CRLF became LF, and a file
heading was added above each input. The md5 in the table above is the pinned (CR-stripped) md5 of the files the
pasted text was taken from.

## Version gate before the first launch

- `3a8:version-probe` answered with an 11-line manifest, `tool_uses: 0`:
  `calibration-rates Lytin-K 1.1 · diagnostician Lytin-G 1.1 · estimator-decomposition Lytin-D 5.0 ·
  estimator-reference-class Lytin-R 1.1 · fp-counter Hotyn-P 1.0 · fp-norms-author Hotyn-N 1.0 · model-builder
  Hotyn-M 1.1 · rate-table-author Hotyn-K 1.1 · rates-step-c Lytin-K 1.1 · work-crosser Hotyn-W 1.1 ·
  work-estimator Hotyn-D 2.0`.
- `PYTHONUTF8=1 py tools/check_probe.py` **could not be executed in this session either**. The permission layer refused
  it in every form tried: `PYTHONUTF8=1 py tools/check_probe.py` (Bash, twice), `$env:PYTHONUTF8='1'; py
  tools/check_probe.py` (PowerShell) and `py -X utf8 tools/check_probe.py` (PowerShell). `py` itself did run later
  in the session for scripts under the scratchpad.
- The script's comparison was therefore reproduced with read-only tools on the same files the script reads. For every
  `agents/*.md` except `version-probe.md`, the line `You are engine \`…\``; for `agents/version-probe.md`, the fenced
  block after "Reply with exactly these lines".
- Result: 11 agent files, 11 stamps, 11 manifest lines, **0 disagreeing**. No agent file lacks a stamp line.
- The probe agent's answer equals both, line for line. **Gate: agree. Launch proceeded.**

## Transcription

Both raw files were produced by script, not by hand. The script copies the assistant text from the harness's
per-agent transcript (`~/.claude/projects/<project>/<session>/subagents/agent-<id>.jsonl`) and adds the orchestrator
header above it. The scripts (`extract_reply.py`, `extract_all.py`, `audit_transcript.py`) live in the session
scratchpad and are not part of the run's files. The completion notifications were not used as the source: they escape
`&` as `&amp;`. The task output files named in the notifications were empty (0 chars). The same happened to
HM44-OA1 in run 44.

| reading | reached the orchestrator | source of the raw file | text blocks |
|---|---|---|---|
| HM53-1 | whole, §1 to §9 | per-agent transcript | 1 (46 532 chars) |
| HM53-2 | **truncated at the head**: began inside §5, at the separator row of the convergence table | per-agent transcript | 2 (22 230 + 30 910 chars), joined verbatim; the seam is described in the file's header |

Both raw files carry all nine sections, and their counts parsed from §6 equal each sensor's own §8.

## Deviations from run 44

1. **Entry point and registration.** Run 44 launched the repository agent `model-builder` from the main session,
   before the repository was packaged as a plugin (`6543df6`). Run 53 launches the plugin subagent
   `3a8:model-builder` through `/3a8:estimate-product`. The definition file carries the same engine stamp,
   `Hotyn-M 1.1`. **This is the variable the regression measures.**
2. **Prompt text rebuilt, not replayed.** Run 44's prompt text was not kept: `run44_raw/` holds the two replies and
   the compare script only. The framing (items 1–5 above) is rebuilt from what run 44's record and raw headers
   state: inputs pasted whole, order A declared, the standing quarantine paragraph, no file read. The two pasted
   inputs are md5-identical to run 44's. The framing wording cannot be checked against run 44; read it as a
   difference of unknown size. **It is confounded with deviation 1**: this run cannot separate the two.
3. **Explicit tool ban in the prompt.** Run 44's record says "no file was read" and `tool_uses: 0`, but not whether
   the prompt said so. Run 53's prompt says it explicitly. The agent's own definition already forbids reading files.
4. **Quarantine list** names "a memory index". Run 44's OA2 reported a memory index among the quarantined ambient
   material, so the material existed then too; only the prompt's list is longer.
5. **Version gate.** Run 44's pre-batch probe returned `Lytin-F 5.0`, the old single-sensor mirror, which confirms
   nothing about `Hotyn-M` (PIPELINE.md, probe note). Run 53 used the manifest probe plus an on-disk comparison, done
   by hand with read-only tools because the script was refused (see above).
6. **Repository state.** Run 44 launched at `73357e9`; run 53 at `5971dc1`. The commit subjects the harness prepends
   differ; they are part of the quarantined ambient material only.
7. **Relaunch.** A previous attempt at run 53 was cut off before any reply arrived (see the head of this file).
8. **Files written to the scratchpad**, not `examples/SAS/` (permission refusal, see the head of this file).
9. **Output-limit continuations inside the sensors.** Both agents' first turn was thinking only and stopped at
   `max_tokens` (64 000 output tokens). HM53-2 then stopped at `max_tokens` a second time, partway through its reply
   text. After each stop the harness injected a meta message into the agent's context, verbatim: "Output token limit
   hit. Resume directly — no apology, no recap of what you were doing. Pick up mid-thought if that is where the cut
   happened. Break remaining work into smaller pieces." HM53-1 received it once and HM53-2 twice. It is not
   case material and carries no estimate. It is still text that reached the sensor, and the prompt did not contain
   it. Its last sentence, "Break remaining work into smaller pieces", is an instruction about how to proceed. Whether run
   44's sensors met the same limit is not recorded: its transcripts were not audited this way, and OA1's is empty.
10. **Transcription source.** Run 44 took OA1 from the relayed reply (sections 1–3 lost) and OA2 from the task output
    file. Run 53 took both from the per-agent `subagents/` transcripts, so neither has a lost section (see
    *Transcription*).
