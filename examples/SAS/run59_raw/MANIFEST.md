# Run 59 — manifest (step 3 only: size classes of the run 58 work model, `Hotyn-D 2.0`, seven batches × 2 repeats)

**2026-09-15.** The run 58 work model (`Hotyn-W 1.2` × `HM57-1`; 210 elements, 187 sizeable leaves, 23 aggregates never
sized) sized by engine `Hotyn-D 2.0`, in the same seven batches as the crossing, two independent repeats per batch —
fourteen launches. Step 3 only, stopped there: nothing priced, no assembly script run. This is the regression of stages
2–3 through the plugin entry point on a 2.x model; the comparison is run 47 (`../run47_sizing_and_assembly.md`,
`../run47_raw/`). **No run record is written here**: the orchestrating session assembles and writes
`run59_sizing_and_assembly.md`.

**Where the files are.** All in place in `examples/SAS/run59_raw/`:
- **Before this session:** `make_sizing_prompts58.py`, `prompt_size_A.md` … `prompt_size_G.md` and `assemble_sas58.py`,
  generated and pinned by the orchestrating session. `assemble_sas58.py` was not opened or run.
- **Written by this session, by Python scripts with exclusive create:** `HD59-A1.md`, `HD59-A2.md` … `HD59-G1.md`,
  `HD59-G2.md` and this `MANIFEST.md`. Nothing was refused and nothing went to the scratchpad.

## Registered before launch (from the launch instruction, verbatim in substance)

- (a) Each repeat sizes the 187 leaves and no aggregate, with at most 5 unsizeable (M10) per repeat.
- (b) Class agreement between the two repeats of every batch in the region 80–90% overall (run 47: 85.0%).
- (c) XL elements few (≤ 5 per repeat) and the same set in both repeats.
- (d) Every sensor prints the stamp `Hotyn-D 2.0` and finishes in one turn without a continuation message under the
  raised cap.
- (e) Every number a sensor prints is a count of named things — a person-day, hour, cost or duration anywhere in a reply
  overturns that reading and is reported, not repaired.

**Outcome (by script from the replies as printed; the consolidated reading belongs to the run record):**
- **(a) met.** No aggregate id appears in any sizing table.
  - Repeat 1: 186 sized + 1 unsizeable (`A140`) = 187.
  - Repeat 2: 184 sized + 3 unsizeable (`A140`, `A158`, `A159`) = 187.
  - Separately from element classes, sensors reported special counts (G2m–G4m) with no class; these are not
    unsizeable elements and are listed per launch below.
- **(b) not met.** Same class in both repeats: **142 of 187 (75.9%)**, below the region 80–90% (run 47: 159 of 187).
  `A140` (unsizeable in both repeats) is counted as not agreeing; counting it as agreeing gives 143 of 187 (76.5%).
  By batch: A 27/30 · B 15/27 · C 19/24 · D 23/24 · E 16/31 · F 26/28 · G 16/23. The 45 differing elements are listed
  below.
- **(c) not met.**
  - Repeat 1 has **13 XL**: `A008`, `A020` (B) · `A029`, `A037` (C) · `A051` (D) · `A081`, `A099`, `A100` (E) ·
    `A078`, `A123` (F) · `A160`, `A161`, `A162` (G).
  - Repeat 2 has **3 XL**: `A029`, `A037` (C) · `A051` (D).
  - The sets agree in C and D only; repeat 1 exceeds 5.
- **(d) met.** Fourteen of fourteen print `Hotyn-D 2.0` in the title line and in §7. Each ran one turn ending
  `end_turn`, with output tokens 17 637–28 131, and no continuation message.
- **(e) met: no reading overturned.** The unit grep (person-day, pd, hour, h, day, week, month, cost, price, €, $) hits
  in three places only, none a figure of effort, time or money (detail under the audit).
- Size-class distribution, repeat 1 / repeat 2 (sum of the §7 lines): S 35 / 45 · M 94 / 101 · L 44 / 35 · XL 13 / 3.
  Run 47: 52/105/23/3 and 55/101/25/3.
- Doubts 172 / 183 (run 47: 126 / 143). Closure violations 35 / 35 (run 47: 33 / 28).

## Launch record

| field | value |
|---|---|
| entry point | `/3a8:estimate-product` (plugin skill), step 3 only |
| subagent | `3a8:work-estimator` (plugin registration of `agents/work-estimator.md`, stamp line ``You are engine `Hotyn-D 2.0` ``) |
| model | **claude-opus-5**, launched with the harness's `opus` alias (the launch tool offers `sonnet`, `opus`, `haiku`, `fable`, not a model id). Meta files: `"model":"opus"`, `"requestShape":"background"`, `"requestNonInteractive":true`. The `model` attachment records `claude-opus-5` ("Opus 5"); every assistant record records `claude-opus-5`, with `effort: "high"` |
| **output cap** | **`CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`**, read from this orchestrating process's environment (by script, `os.environ`) before launch. Not separately observable per subagent; no turn came near 64 000 (largest 28 131) |
| harness | Claude Agent SDK `0.3.271` (`CLAUDE_AGENT_SDK_VERSION`), entry point `claude-desktop` |
| repeats | **n = 2 per batch**, seven batches, fourteen launches, each in its own context. Prompt text = the batch file's content, verbatim and entire, nothing added before or after; both repeats of a batch received the same file |
| concurrency | at most four at once. A1, A2, B1, B2 launched in one orchestrator message (prompt records 20:45:43Z–20:48:08Z). Each later launch followed a completion notification: C1 after A1 (20:52:06Z), C2 after A2 (20:53:16Z), D1 and D2 in one message after B2 and B1 (20:54:21Z, 20:55:14Z), E1 after C1 (20:57:17Z), E2 after C2 (20:58:38Z), F1 after D1 (21:00:39Z), F2 after D2 (21:01:32Z), G1 after E1 (21:02:22Z), G2 after E2 (21:04:31Z). Largest overlap by the transcript timestamps (prompt record to last assistant record): 4, reached seven times, first at 20:48:08Z; never 5. Last reply 21:09:07Z |
| repository state at launch | `main` at `eb40827`. `git status --porcelain` at the pre-launch check (after the probe, before A1): `?? docs/proposal_architecture_declaration.md`, `?? examples/SAS/run58_raw/`, `?? examples/SAS/run59_raw/` |
| inputs | `prompt_size_A.md` … `prompt_size_G.md` (below). The launch instruction states INPUT 2 (the sizing rules) is byte-identical to run 47's. This session verified by script (`tails59.py`) that the text from `# INPUT 2` to the end (4 456 chars) is identical across A–G, and that the preamble before `# INPUT 1`, scope line masked, is identical across A–G. It did not re-derive run 47's prompts |

## Version gate before the launch

- `3a8:version-probe` was launched in the foreground with the prompt `Print the manifest.`. It answered with 11 lines,
  `tool_uses: 0`, 3 536 ms, 3 665 subagent tokens: `calibration-rates Lytin-K 1.1 · diagnostician Lytin-G 1.1 ·
  estimator-decomposition Lytin-D 5.0 · estimator-reference-class Lytin-R 1.1 · fp-counter Hotyn-P 1.0 ·
  fp-norms-author Hotyn-N 1.0 · model-builder Hotyn-M 2.1 · rate-table-author Hotyn-K 1.1 · rates-step-c Lytin-K 1.1 ·
  work-crosser Hotyn-W 1.2 · work-estimator Hotyn-D 2.0`.
- `PYTHONUTF8=1 py tools/check_probe.py` **ran** (Bash): every agent `ok`, `11 agents, 0 failing`,
  `work-estimator Hotyn-D 2.0`, `work-crosser Hotyn-W 1.2`, `model-builder Hotyn-M 2.1`.
- The probe's answer equals the script's on-disk list line for line. **Gate: agree. Launch proceeded.**
- The seven prompt files were then checked by script (`pins59.py`) against the md5 values in the launch instruction:
  seven of seven equal, no CR, final newline present. `CLAUDE_CODE_MAX_OUTPUT_TOKENS` read from this process's
  environment: `128000`.

## Prompt pins

md5 of the file bytes as on disk (no CR, final newline), computed by script before launch and again at manifest time.
Both repeats of a batch received the same file.

| batch | subtrees · sized elements | chars | md5 on disk | expected (launch instruction) | transcript prompt records (repeat 1 · repeat 2) |
|---|---|---|---|---|---|
| A | N02 · 30 | 18 619 | `6b68546221905104e660b48b5f26470c` | `6b68546221905104e660b48b5f26470c` | both equal to the file, byte for byte, final newline included |
| B | N06, N07, N10 · 27 | 15 920 | `c1f1abe1ef02f3aa8f190aa37765558c` | `c1f1abe1ef02f3aa8f190aa37765558c` | both equal to the file, byte for byte, final newline included |
| C | N08, N09 · 24 | 13 082 | `486e0e9064fad8ef78124f7036276cbf` | `486e0e9064fad8ef78124f7036276cbf` | both equal to the file, byte for byte, final newline included |
| D | N11, N12 · 24 | 18 790 | `be5ce765dfbf45248960baaf7b45c2d5` | `be5ce765dfbf45248960baaf7b45c2d5` | both equal to the file, byte for byte, final newline included |
| E | N13 · 31 | 20 993 | `89a3f5c00330d1ec318c70b58fda2479` | `89a3f5c00330d1ec318c70b58fda2479` | both equal to the file, byte for byte, final newline included |
| F | N19, N20 · 28 | 14 578 | `110a3a2a12db1b057edfe9f7756d7437` | `110a3a2a12db1b057edfe9f7756d7437` | both equal to the file, byte for byte, final newline included |
| G | N21, N22 · 23 | 13 712 | `a616f912180e357a548a7d42e2fe26e5` | `a616f912180e357a548a7d42e2fe26e5` | both equal to the file, byte for byte, final newline included |

## Per-sensor audit (from `subagents/agent-<id>.jsonl`, by script)

One row per launch. Every turn ran under the cap 128 000 (the orchestrating process's value; not separately observable per
subagent). "Continuation" is the count of "Output token limit hit" in the whole transcript.

| reading | prompt record | user records after the prompt | API messages | first assistant record · last | text blocks (chars) | **stop reason · output tokens** | continuation | turns | `tool_uses` (notification) · tool_use blocks | duration (notification) | subagent tokens (notification) | models recorded · `effort` | `date` attachment |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HD59-A1 | 20:45:43.354Z | none | 1 (`msg_011Cf5swAp4mSBeavvWxJerB`) | 20:50:11.364Z · 20:51:16.125Z | 1 (17 329) | **end_turn · 27 181** | no | 1 | 0 · 0 | 332 797 ms | 36 121 | `claude-opus-5` only · `high` | 2026-09-15 |
| HD59-A2 | 20:46:36.040Z | none | 1 (`msg_011Cf5t14BKiLHatA2HDRLu2`) | 20:51:13.995Z · 20:52:21.330Z | 1 (17 797) | **end_turn · 28 131** | no | 1 | 0 · 0 | 345 312 ms | 36 944 | `claude-opus-5` only · `high` | 2026-09-15 |
| HD59-B1 | 20:47:22.287Z | none | 1 (`msg_011Cf5t4Tg2f1V8SqQVwEnvR`) | 20:51:56.974Z · 20:52:58.805Z | 1 (16 484) | **end_turn · 27 822** | no | 1 | 0 · 0 | 336 538 ms | 35 884 | `claude-opus-5` only · `high` | 2026-09-15 |
| HD59-B2 | 20:48:08.163Z | none | 1 (`msg_011Cf5t7rXnUFDSip2tyacoG`) | 20:52:02.052Z · 20:52:57.492Z | 1 (14 835) | **end_turn · 23 528** | no | 1 | 0 · 0 | 289 347 ms | 31 977 | `claude-opus-5` only · `high` | 2026-09-15 |
| HD59-C1 | 20:52:06.226Z | none | 1 (`msg_011Cf5tRPd2zZGJCyfsS3P24`) | 20:55:09.204Z · 20:56:05.021Z | 1 (14 422) | **end_turn · 18 976** | no | 1 | 0 · 0 | 238 813 ms | 26 463 | `claude-opus-5` only · `high` | 2026-09-15 |
| HD59-C2 | 20:53:16.620Z | none | 1 (`msg_011Cf5tWahRJUyaTf1AXReUz`) | 20:56:33.595Z · 20:57:22.113Z | 1 (13 338) | **end_turn · 19 792** | no | 1 | 0 · 0 | 245 619 ms | 27 592 | `claude-opus-5` only · `high` | 2026-09-15 |
| HD59-D1 | 20:54:21.496Z | none | 1 (`msg_011Cf5tbNAkkWTErZg2KXcnP`) | 20:58:41.833Z · 20:59:47.375Z | 1 (17 367) | **end_turn · 26 891** | no | 1 | 0 · 0 | 325 901 ms | 35 696 | `claude-opus-5` only · `high` | 2026-09-15 |
| HD59-D2 | 20:55:14.431Z | none | 1 (`msg_011Cf5tfFxK2CtBAwXPmL3mS`) | 20:59:24.430Z · 21:00:29.963Z | 1 (16 913) | **end_turn · 25 967** | no | 1 | 0 · 0 | 315 546 ms | 34 783 | `claude-opus-5` only · `high` | 2026-09-15 |
| HD59-E1 | 20:57:17.418Z | none | 1 (`msg_011Cf5tpKnk6JDnSQsKsv211`) | 21:00:27.873Z · 21:01:34.756Z | 1 (17 377) | **end_turn · 21 920** | no | 1 | 0 · 0 | 257 366 ms | 31 418 | `claude-opus-5` only · `high` | 2026-09-15 |
| HD59-E2 | 20:58:38.839Z | none | 1 (`msg_011Cf5tvLX4gJABNB4Vvnrnf`) | 21:02:36.660Z · 21:03:34.020Z | 1 (14 740) | **end_turn · 24 260** | no | 1 | 0 · 0 | 295 200 ms | 33 909 | `claude-opus-5` only · `high` | 2026-09-15 |
| HD59-F1 | 21:00:39.125Z | none | 1 (`msg_011Cf5u5CPQyuXH4n2HYinqW`) | 21:03:21.523Z · 21:04:15.737Z | 1 (14 472) | **end_turn · 17 637** | no | 1 | 0 · 0 | 216 631 ms | 25 611 | `claude-opus-5` only · `high` | 2026-09-16 |
| HD59-F2 | 21:01:32.853Z | none | 1 (`msg_011Cf5u9A4sfnUSBpRc4gZ5S`) | 21:04:46.969Z · 21:05:45.405Z | 1 (14 989) | **end_turn · 20 879** | no | 1 | 0 · 0 | 252 578 ms | 28 696 | `claude-opus-5` only · `high` | 2026-09-16 |
| HD59-G1 | 21:02:22.642Z | none | 1 (`msg_011Cf5uCqACCy6pKAs9rL7Rx`) | 21:06:24.158Z · 21:07:14.393Z | 1 (13 549) | **end_turn · 22 878** | no | 1 | 0 · 0 | 291 766 ms | 30 587 | `claude-opus-5` only · `high` | 2026-09-16 |
| HD59-G2 | 21:04:31.694Z | none | 1 (`msg_011Cf5uNLhx9xDmy8KoQs1hn`) | 21:08:18.821Z · 21:09:07.017Z | 1 (12 507) | **end_turn · 21 816** | no | 1 | 0 · 0 | 275 347 ms | 29 626 | `claude-opus-5` only · `high` | 2026-09-16 |

Harness attachments, identical list in all fourteen: environment, model, instructions, session_context, date, prompt_snapshot ×2.

**Engine stamp as printed** (title line · §7 line):

| reading | title line | §7 line |
|---|---|---|
| HD59-A1 | Hotyn-D 2.0: size classification, subtrees under N02 of `HM57-1` (crossed by `Hotyn-W 1.2`) | - **Engine:** Hotyn-D 2.0 |
| HD59-A2 | Hotyn-D 2.0: size classes for the N02 subtrees of HM57-1 (as crossed by Hotyn-W 1.2) | **Engine: Hotyn-D 2.0** |
| HD59-B1 | Hotyn-D 2.0: size classification of subtrees N06, N07, N10 of `HM57-1` | - **Engine:** `Hotyn-D 2.0` |
| HD59-B2 | Hotyn-D 2.0: size classes for subtrees N06, N07 and N10 of work model HM57-1 | - **Engine:** Hotyn-D 2.0 |
| HD59-C1 | Hotyn-D 2.0: size classification, subtrees N08 and N09 of `HM57-1` (as crossed by `Hotyn-W 1.2`) | - **Engine:** Hotyn-D 2.0 |
| HD59-C2 | Hotyn-D 2.0: size classification of HM57-1, subtrees N08 and N09 (crossed by Hotyn-W 1.2) | **Engine: Hotyn-D 2.0** |
| HD59-D1 | Hotyn-D 2.0 sizing: batch N11, N12 of HM57-1 (as crossed by Hotyn-W 1.2) | - Engine: **Hotyn-D 2.0** |
| HD59-D2 | Hotyn-D 2.0: size classes for the N11 and N12 subtrees of HM57-1 (as classified and crossed by Hotyn-W 1.2) | - **Engine:** Hotyn-D 2.0 |
| HD59-E1 | Hotyn-D 2.0 — size classification of the N13 subtrees in product model HM57-1 (as crossed by Hotyn-W 1.2) | **Engine: Hotyn-D 2.0** |
| HD59-E2 | Hotyn-D 2.0: size classification of the N13 subtrees, model HM57-1 (crossed by Hotyn-W 1.2) | - **Engine:** Hotyn-D 2.0 |
| HD59-F1 | Hotyn-D 2.0: size classification of the N19 / N20 subtrees of `HM57-1` | - **Engine:** Hotyn-D 2.0 |
| HD59-F2 | Hotyn-D 2.0: sizing of the N19 and N20 subtrees of HM57-1 (crossed by Hotyn-W 1.2) | **Engine: Hotyn-D 2.0** |
| HD59-G1 | Hotyn-D 2.0 sizing: subtrees N21, N22 of HM57-1 (as crossed by Hotyn-W 1.2) | **Engine: Hotyn-D 2.0** |
| HD59-G2 | Hotyn-D 2.0: size classes for HM57-1, subtrees N21 and N22 | **Engine: Hotyn-D 2.0** |

**Unit grep** (person-day, pd, hour, h, day, week, month, cost, price, €, $; case-insensitive, word-bounded), every hit
by line of the reply body:
- **Contamination checks naming the forbidden categories** ("no effort figure, person-day value, rate, price, budget,
  duration …"): A1 L7, A2 L7, B1 L5, B2 L5, C1 L5, C2 L7, D1 L5, D2 L6, E1 L9, E2 L5, F1 L5, F2 L7, G1 L8–9, G2 L8–9.
  A1 L9 and A2 L7 also quote NFR-5's "at no cost to X-Customer"; C1 L8 and G2 L9 say "3scale" / D-8 carry no price.
- **The report periods of G-7.2** ("hour, day, week, month and year"), quoted or enumerated as report periods:
  A1 L32 and A2 L41 (A034); C1 L6, L48 (A033), L143 (closure violation 1); C2 L45 (A033), L112 (closure violation 1).
- **An idiom:** A2 L74, special count on A001: "existing members must be able to work on day one".
- None states a figure of effort, time or money. **No reading is overturned.**

**Instrument readings as printed (§7; unsizeable and XL ids from §4 and the §2 table; special counts from §7, or from
§3 where §7 does not list them).**

| reading | stamp | stop · output tokens | continuation | sized | S / M / L / XL | unsizeable (ids) | XL (ids) | statements compliance / behavioural | special counts assigned (A9, G2m–G4m) | doubts | closure violations |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HD59-A1 | Hotyn-D 2.0 | end_turn · 27 181 | none | 29 | 9 / 15 / 5 / 0 | 1 (A140) | — | 6 / 4 | G: A001 L, A012 M, A076 M; A089 no class. A9: none in batch | 32 | 2 |
| HD59-A2 | Hotyn-D 2.0 | end_turn · 28 131 | none | 29 | 8 / 15 / 6 / 0 | 1 (A140) | — | 7 / 3 | G: A001 L, A012 S (§3); A076, A089 no class. A9: none | 33 | 3 |
| HD59-B1 | Hotyn-D 2.0 | end_turn · 27 822 | none | 27 | 4 / 14 / 7 / 2 | 0 | A008, A020 | 0 / 0 | G: none assigned; A009, A018, A021, A048, A050, C01 no class. A9: none | 29 | 7 |
| HD59-B2 | Hotyn-D 2.0 | end_turn · 23 528 | none | 27 | 5 / 21 / 1 / 0 | 0 | — | 0 / 0 | G: none assigned; A009, A018, A021, A048, A050, C01 no class. A9: none | 24 | 7 |
| HD59-C1 | Hotyn-D 2.0 | end_turn · 18 976 | none | 24 | 4 / 14 / 4 / 2 | 0 | A029, A037 | 0 / 0 | G: none assigned; A035, A044, C06 count 0, no class. A9: none | 26 | 6 |
| HD59-C2 | Hotyn-D 2.0 | end_turn · 19 792 | none | 24 | 6 / 11 / 5 / 2 | 0 | A029, A037 | 0 / 0 | G: C06 S; A035, A044 count 0, no class. A9: none | 31 | 2 |
| HD59-D1 | Hotyn-D 2.0 | end_turn · 26 891 | none | 24 | 3 / 16 / 4 / 1 | 0 | A051 | 0 / 1 | G: A010 S, A062 M. A9: none | 21 | 5 |
| HD59-D2 | Hotyn-D 2.0 | end_turn · 25 967 | none | 24 | 3 / 17 / 3 / 1 | 0 | A051 | 0 / 1 | G: A062 M; A010 unsupported. A9: none | 24 | 4 |
| HD59-E1 | Hotyn-D 2.0 | end_turn · 21 920 | none | 31 | 4 / 12 / 12 / 3 | 0 | A081, A099, A100 | 0 / 0 | G: A080 M, A087 S; A083 no band. A9: none | 25 | 7 |
| HD59-E2 | Hotyn-D 2.0 | end_turn · 24 260 | none | 31 | 12 / 14 / 5 / 0 | 0 | — | 0 / 0 | G: A080 M, A087 S (§3); A083 count 0, no class. A9: none | 26 | 5 |
| HD59-F1 | Hotyn-D 2.0 | end_turn · 17 637 | none | 28 | 7 / 14 / 5 / 2 | 0 | A078, A123 | 0 / 0 | G: 5 (S 1 / M 4) — A077 M, A109 M, A122 M, A129 M, A131 S (§3). A9: none | 22 | 4 |
| HD59-F2 | Hotyn-D 2.0 | end_turn · 20 879 | none | 28 | 7 / 14 / 7 / 0 | 0 | — | 0 / 0 | G: 5 — A077 M, A109 M, A122 M, A129 M, A131 S (§3). A9: none | 27 | 11 |
| HD59-G1 | Hotyn-D 2.0 | end_turn · 22 878 | none | 23 | 4 / 9 / 7 / 3 | 0 | A160, A161, A162 | 5 / 4 | A9: A164 L (§3). G: A170 unsupported | 17 | 4 |
| HD59-G2 | Hotyn-D 2.0 | end_turn · 21 816 | none | 21 | 4 / 9 / 8 / 0 | 2 (A158, A159) | — | 3 / 4 | A9: A164 L (§3). G: A170 no class | 18 | 3 |

**Elements whose class differs between the repeats** (repeat 1 → repeat 2; `—` = no class), from the §2 tables by
script (`readings59.py`):
- A: A034 M→L · C14 S→M · A140 —/— (unsizeable in both).
- B: A007 L→M · A008 XL→M · A015 L→M · A017 M→S · A020 XL→L · A021 M→S · A025 L→M · A026 S→M · A046 L→M · A146 L→M ·
  A147 L→M · A165 L→M.
- C: A022 M→S · A035 M→S · A036 S→M · A038 M→L · A044 M→S.
- D: A071 L→M.
- E: A004 L→S · A073 L→S · A074 L→S · A075 L→S · A081 XL→L · A082 M→S · A084 L→M · A094 L→M · A097 M→S · A098 M→S ·
  A099 XL→M · A100 XL→L · A102 L→S · A107 L→M · A108 L→M.
- F: A078 XL→L · A123 XL→L.
- G: A011 L→M · A158 M→— · A159 M→— · A160 XL→L · A161 XL→L · A162 XL→L · C11 L→M.

Several sensors stated a batch-wide reading rule at the head of §2. In B and E the two repeats chose opposite rules for
obligations shared between siblings: B1 and E1 counted every covered obligation in full on every element, B2 and E2
counted only the clauses the element's own name claims. In G both repeats counted coverage in full; G2 added that one
verb over a list of same-kind objects counts once and that a statement counts only named systems or components, and
the G differences (A011, A160–A162, C11, A158/A159) fall where those rules act. This is noted, not adjudicated.

## Ambient context the sensors received (by script, from the attachments)

The fourteen transcripts carry byte-identical `environment`, `model`, `instructions` and `session_context` attachments
(`context59.py`: one distinct value each). The `date` attachment has two values: `2026-09-15` for A1–E2 and `2026-09-16`
for F1, F2, G1, G2 (local midnight fell between the E2 and F1 launches; F1's prompt record is 21:00:39Z).
- **`session_context`** carried:
  - a `userEmail` line (the user's address, with its use restriction);
  - a git snapshot: `Current branch: main`, `Git user: Gennadiy Serdyuk`, and `Status:`
    - `?? docs/proposal_architecture_declaration.md`
    - `?? examples/SAS/run58_raw/`
    - `?? examples/SAS/run58_work_model.md`
    - `?? examples/SAS/run59_raw/`
  - recent commit subjects, newest first:
    - `eb40827 measure: run 57 - the Hotyn-M 2.1 pair on SAS; equal-set leaves kept apart, the remaining spread is the skeleton`
    - `2faaad3 docs: estimate-product skill - the corridor line matches instrument.md §4 (assumed ρ = 0.5, not measured)`
    - `e8f8d07 feat: Hotyn-M 2.1 - identity by coverage set is for comparing models, not for building one; the output cap is a launch coordinate`
    - `8a1f01f measure: run 56 - the first Hotyn-M 2.0 pair on SAS; the output cap reaches subagents`
    - `53a8a4e measure: run 55 - first Hotyn-M 2.0 reading on SAS, n = 1; the smoke test fails on the harness cap`
- **`examples/SAS/run58_work_model.md`** was not in the status at this session's pre-launch check (`git status
  --porcelain` after the probe). By file time it was created at 20:44:48Z and last written at 20:45:25Z, between that
  check and the first launch (A1, 20:45:43Z). It was created by something other than this session; this session did not
  open, modify or use it.
- **`instructions`** carried the memory index (`memory/MEMORY.md`). One of its lines speaks of a rate table as a
  direction ("числа из тарифной таблицы") without rows or figures.
- **`environment`** carried the working directory, the platform and the scratchpad path.

No attachment names a work-model count, a size class, a rate or an estimate. The commit subjects name runs 55–57, the
Hotyn-M changes and the skill's corridor line, not the work estimator.

## Transcription

Each raw file was produced by script (`build_raw59.py`): the orchestrator header, a blank line, then the single
assistant text block from the per-agent transcript, verbatim, with no final newline added (the HW58 convention). The
script opens with exclusive create and refuses to overwrite; it refuses a reading whose transit is not one clean
`end_turn` turn with one text block, no user record after the prompt, no continuation message, no tool_use block, a
prompt record equal to the file and `claude-opus-5` only. None was refused. It checked after writing that each file's
bytes equal header plus body. There is no seam in any file.

| reading | reached the orchestrator | source of the raw file | text blocks | body md5 | file md5 |
|---|---|---|---|---|---|
| HD59-A1 | whole, title to §7 | per-agent transcript | 1 (17 329 chars) | `dd6f6286e608facc7849c004abf3e538` | `e438d50adc7754609fb850a5d005c028` |
| HD59-A2 | whole, title to §7 | per-agent transcript | 1 (17 797 chars) | `45347da582620ef8db7015a08068844c` | `7538969057ec41ffed43d7babaa18afc` |
| HD59-B1 | whole, title to §7 | per-agent transcript | 1 (16 484 chars) | `e2a8e669befd7665990301ba37c3b94a` | `bf77adb1661b68f5fbe4320c0a76a01e` |
| HD59-B2 | whole, title to §7 | per-agent transcript | 1 (14 835 chars) | `e278190ee575b93a39cd16d94eb7e94f` | `f2f0093158c1d5b54f68c43da8f59c44` |
| HD59-C1 | whole, title to §7 | per-agent transcript | 1 (14 422 chars) | `b16213fb4cfba2c514229017f73a6f01` | `5431d476de8059d35195f524714816d8` |
| HD59-C2 | whole, title to §7 | per-agent transcript | 1 (13 338 chars) | `3066a1383bc35ccbda8d5470f2182eda` | `12bd9d2a79e633e5aae8682a38fc45e5` |
| HD59-D1 | whole, title to §7 | per-agent transcript | 1 (17 367 chars) | `b6431552c6c059a2f271532b9c1964b1` | `829b194bb1818fdf3aed72ddfddc8273` |
| HD59-D2 | whole, title to §7 | per-agent transcript | 1 (16 913 chars) | `2b299240400b1cb5876bf14817c0101f` | `a72d2600c278612fe27fe5b269906819` |
| HD59-E1 | whole, title to §7 | per-agent transcript | 1 (17 377 chars) | `a115de4eea5178feebb9d7fba76c1dc0` | `b1ec97597a684cf848a0eaebd5563d46` |
| HD59-E2 | whole, title to §7 | per-agent transcript | 1 (14 740 chars) | `42eae4d389e5806758aed3af1faa32a1` | `8aec39272ad8aceb3ce4db01ef7f0670` |
| HD59-F1 | whole, title to §7 | per-agent transcript | 1 (14 472 chars) | `c5eb6ee677eb6fcc2188cd5eaa70e8aa` | `ce3982e21d55a227b92b68b3437c0ffd` |
| HD59-F2 | whole, title to §7 | per-agent transcript | 1 (14 989 chars) | `4d00ca39048575d989498dd78482e9a1` | `d2b8ce30682fa27381598769c2f2f15e` |
| HD59-G1 | whole, title to §7 | per-agent transcript | 1 (13 549 chars) | `6d28f0ea9c6886056a0977811e59c689` | `1d806c0b36796371a1b875390943bfea` |
| HD59-G2 | whole, title to §7 | per-agent transcript | 1 (12 507 chars) | `f71203eb5eb723e0c3e246c4889d5c1e` | `936261454c041727af35b3d05f97d973` |

## Deviations from run 47

1. **Work model:** the run 58 work model (`Hotyn-W 1.2` × `HM57-1`; 210 elements, 187 sizeable leaves, 23 aggregates),
   against run 47's run 45 work model (`Hotyn-W 1.1` × `HM44-OA1`). **This is what the run measures.** Under `HM57-1`
   coverage lives in leaves only and derived leaves (`C01`…`C16`) carry no covered obligation, only a `trigger:` list;
   INPUT 1 of every prompt says so in one paragraph.
2. **Batches** follow `HM57-1`'s top-level subtrees, the same seven as the run 58 crossing: A N02 (with CN01) · B N06,
   N07, N10 · C N08, N09 · D N11, N12 · E N13 · F N19, N20 · G N21, N22. Run 47's were cut from `HM44-OA1`'s S-01…S-14.
   The engine (`Hotyn-D 2.0`), the model (`claude-opus-5` via `opus`), n = 2 per batch and seven batches are the same.
3. **Prompts** are generated by `make_sizing_prompts58.py`, not run 47's `make_sizing_prompts.py`. The launch
   instruction states INPUT 2 (the sizing rules) is byte-identical to run 47's; this session verified by script that
   INPUT 2 is identical across A–G and did not re-derive run 47's prompts (none is kept on disk in `run47_raw/`).
4. **Derived leaves read from their triggers.** Several triggers name elements outside the batch (e.g. C05's A032,
   A045, A104; C01's A041, A069, A137; C15's A129). A1 (C05), B1 and B2 (C01), E1 and E2 (C15) said so in their
   doubts and sized from the name.
5. **Transcription:** all fourteen raw files are extracted by script from the per-agent transcript. Run 47's HD47
   headers record the text "taken from the harness transcript of the agent, identical to the reply as received".
6. **Output cap 128 000 recorded, with per-turn stop reason and output tokens.** Run 47 recorded neither. Every run 59
   turn is under 29 000 output tokens, so the cap of 64 000 would not have been reached either.
7. **Harness** SDK `0.3.271` (`CLAUDE_AGENT_SDK_VERSION`), entry point `claude-desktop`; run 47's version is not recorded.
8. **Repository** at `eb40827`. The sensors' ambient status showed `run58_raw/`, `run58_work_model.md` (created by
   another process after this session's pre-launch check), `run59_raw/` and the unrelated untracked
   `docs/proposal_architecture_declaration.md`.
9. **`effort: "high"`** on every assistant record; run 47 does not record the field.
10. **`date` attachment** differs within the run (2026-09-15 for A1–E2, 2026-09-16 for F1–G2); the run started and
    ended on 2026-09-15 UTC.
11. **Scripts** (session scratchpad, not part of the run's files):
    - `pins59.py`: prompt md5s against the instruction, environment values.
    - `promptcheck59.py`: transcript prompt record against the file, per launch, run after each group of launches.
    - `tails59.py`: preamble (scope line masked) and INPUT 2 identity across the seven prompt files.
    - `struct59.py`: record layout.
    - `audit59.py`: per-record audit, continuation count, stamps, unit grep.
    - `context59.py`: attachment identity across transcripts and contents.
    - `stat59.py`: file times of `run58_work_model.md` and `run59_raw/`.
    - `readings59.py`: §2 table classes, §4 and §7 verbatim, class agreement between repeats.
    - `overlap59.py`: concurrency by transcript timestamps.
    - `build_raw59.py`: raw files.
    - `make_manifest59.py`: this file.
