# Run 52 — manifest

**2026-09-14.** A regression run of the `/3a8:estimate-reference-class` entry point (the plugin skill) against run 46: the
run 46 input conditions reproduced, the sensor launched n = 2 through the plugin-namespaced subagent.

## Inputs

| input | value |
|---|---|
| target run | `examples/SAS/run46_reference_class.md`, whose head is the specification reproduced here |
| input text source | run 46's own prompt was **not preserved**. Rebuilt from `run49_raw/prompt_baseline_sas.txt`, whose record (`run49_raw/MANIFEST.md`) states it carries "the RFP §1–2 verbatim + the assumption log v1 (the sanitised form the class sensors saw)" |
| source file check | `prompt_baseline_sas.txt` LF-form md5 **`9d71b4c7039e5adcd5477c75c7439732`** on 2026-09-14 — identical to run 49's record, so the file is unchanged since the runs it describes |
| slice used | lines **23–701** of that file (LF form): the RFP section header through the end of the log; lines 1–21 (run 49's bare baseline instruction and its imposed unit) **dropped** — run 46 was told no unit (A19 withheld) |
| slice md5 | **`9da9b3331f511d2dd0269c111222772a`** (LF form, lines 23–701 joined with LF, trailing LF) |
| match to run 46's head, point by point | RFP §1–2 verbatim, §3–5 dropped as commercial boilerplate ✓ · log v1 with run-history narration (header, changelog, A20, A21) withheld ✓ · obligation counts (A1's N = 146 / N = 7) withheld ✓ · unit convention (A19 first half) withheld ✓ · A3 carries the case profile's team line (middle/senior, one site, first domain) ✓ · no product model, work model, rate table, total, prior sensor output ✓ |
| transmitted prompt, vs the slice — **not byte-identical, declared** | (a) one preface sentence added: "Produce your reference class forecast for the project below. Two inputs are pasted in full: the project description and the assumption log. There is nothing else." · (b) the two section headers prefixed "INPUT 1 — " and "INPUT 2 — " · (c) runs of whitespace-only lines from the PDF extraction collapsed (page-1 cover block, the Figure 1 gap, the run after G-13.7) · every line carrying text pasted verbatim. The prompt was pasted by the orchestrator; no md5 of the transmitted bytes exists. Run 46's own framing wording is unknown, so (a)–(b) cannot be compared with it |
| engine | `Lytin-R 1.1`, as both sensors printed |
| subagent | **`3a8:estimator-reference-class`** (plugin namespace; run 46 launched `estimator-reference-class` before packaging — this difference is what the regression tests), definition `agents/estimator-reference-class.md`, `tools: Glob` |
| model | the harness's `opus` alias, i.e. **claude-opus-5** (the orchestrator session's own model ID) — the same coordinate as run 46 |
| n | 2, launched simultaneously 2026-09-14, identical prompts, neither seeing the other |
| repository state | HEAD `b5c594b` ("docs: the bottom-up bell is an assumed ρ = 0.5; …"), working tree clean — from the session-start snapshot; git could not be re-queried (commands required approval) |
| not given | FACT.md (does not exist; not opened) · any bottom-up figure · product/work model · rate table · run 46 readings · any target |

## Files

| file | what |
|---|---|
| `RC52-1.md` | reply verbatim, orchestrator header · tool_uses 0 · 202 s · 29 974 subagent tokens |
| `RC52-2.md` | reply verbatim, orchestrator header · tool_uses 0 · 179 s · 28 533 subagent tokens |
| `../run52_reference_class.md` | the run record |

## Deviations, declared

- **File names** follow the request (`RC52-n`), not the skill's `LR<N>-<repeat>` pattern — kept consistent with run 46's `RC46-n`.
- **Where the files were written.** A write into `examples/SAS/run52_raw/` was refused by the harness's permission layer
  (reported as a sensitive path). All four files were written to the session scratchpad instead, byte-for-byte what
  should land at `examples/SAS/run52_raw/` and `examples/SAS/run52_reference_class.md`; they need to be copied there.
- **Transcription.** Both replies were taken from the harness's completion notification, as run 46's were taken from
  the delivered reply. Whether the harness reformats a reply before delivery cannot be checked from here.
- **Ambient context.** Neither reading reports ambient repository material (both run 46 readings reported and
  quarantined a git status). Whether the plugin launch path still injects it is not observable from the orchestrator.
