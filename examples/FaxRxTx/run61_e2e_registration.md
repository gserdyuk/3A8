# Run 61 — the end-to-end test of the instrument on FaxRxTx, registered before launch

**2026-09-16.** The first time the packaged instrument (`3a8` plugin 0.2.0, `/3a8:estimate`) is given a case
and left alone from the pinned inputs to the estimate document and the report. One child Claude Code process
(`claude --plugin-dir . -p`, `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`), one instruction: estimate
`examples/FaxRxTx` as the skill prescribes. The orchestrating session launches, watches the transcripts, and
touches nothing until the process ends. Run numbers from 61 upward are the child's to assign.

FaxRxTx is the one case with an outcome (`FACT.md`, 120 staffed person-months ≈ 13 304 net task hours by the
case's own conversion, run 33). The earlier estimate on it is the 1.1 chain's (run 31, 2026-08-22): raw
11 386 h, ×0.86 of the outcome, uncalibrated. The child is told not to consult earlier run records or reports;
its sensors never see them by construction.

## Registered outcomes

1. **Process.** The child completes Step 0 (writes `case_profile.md`, which this case never had), Steps 1–4
   through the plugin's sensors and `tools/chain/`, the outside view (n = 2), Steps C, B and D, and Step 7
   (`report_numbers.json`, `report_text.json`, the report, the estimate document) in one process, without the
   orchestrating session intervening. A process that stops or asks for help is the finding.
2. **Sensors.** Every sensor turn ends `end_turn` with no continuation message; every stamp is the current
   version (`Hotyn-M 2.1`, `Hotyn-W 1.2`, `Hotyn-D 2.0`, `Lytin-R 1.1`, `Lytin-K 1.1`, `Lytin-G 1.1`).
3. **The chain.** The 2.x skeleton is shallower than the 1.1 model's, so the raw chain should land **below**
   run 31's 11 386 h: registered region **×0.70–0.95 of the outcome** (9 300–12 600 h). Sizing repeat spread
   ≤ ×1.10; class agreement ≥ 75%.
4. **Calibrated.** Both gap-blind rounds so far landed on ×1.5; if this one does too, the calibrated centre
   sits at **×1.05–1.4 of the outcome**. Inside the ×1.3 gate of `docs/exit_criterion.md` on at least one
   side of the band is the registered expectation; outside both sides is the finding.
5. **Artefacts.** `estimate_FaxRxTx_<date>.md` in the template's form; a report in `reports/` with the chain
   bell, the class curves, the outcome line (Step 6 after the document is fixed), and the tiles; both input
   files of the report present and every number in them traceable to a run.
6. **Not registered, to be read afterwards:** how the crossing handles `C-DIRECT`, `G-SEED` and `SA-NONE`
   (the first 2.x run on a declaration other than SAS's); what the sizing does with the seed counts; whether
   the four standing demanded items (F48, F49, F50, F52) reach the assembly as carried, as run 31 had them.

## What would overturn the test's reading

- The process finishing but the report or the document missing: the skill's Step 7 is not executable as
  written.
- The chain outside ×0.70–0.95 of the outcome: either the 2.x skeleton's price is not what SAS measured, or
  the declaration (`C-DIRECT`, `G-SEED`) moves more than the skeleton.
- A sensor cut by the cap or resumed with an injected message: the launch coordinate is not honoured by the
  skill's instructions.
