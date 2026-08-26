# Run 40 — `Hotyn-P 1.0` on BMS, n=2 — raw transcripts

**2026-08-27.** The parametric counter's second case: the specification-density input. Two
independent launches, identical prompts, parallel, model **`claude-fable-5`** (session model,
recorded by the orchestrator).

Registered question, written before launch: *what is the data-function inventory and the
transaction inventory of the pinned BMS requirement list — each item classified with its complexity
class justified by enumeration — and which requirements lie outside the instrument's scope?* The
run this exists to inform: does the count leave the enumeration floor on an RFP, where the FaxRxTx
count (run 39) sat on it?

## Inputs

- `requirements.md`, N = 73, md5 `554ea3608dd0602f0ddf2f7e7b82178c`, verified before launch,
  pasted verbatim (list + granularity preamble + known weaknesses; processing orders omitted —
  they are `Hotyn-M`'s concern).
- Assumption log v3 with **A3 (team) and A7 (units) withheld by the orchestrator** — team
  composition and unit conventions are not inputs to a functional count, and both are
  contamination triggers for this sensor.
- The pinned component definitions and threshold matrices (run 38). Weights never in the prompt.
- Quarantine declared: harness block; the log's structural references (activity ids E7/O3).

Both runs reported the quarantine items and proceeded clean. `tool_uses: 0` both. Protocol note:
both placed the engine stamp in the instrument readings rather than at the top — recorded.

## Result, in three lines

**The data-function inventory is identical between runs — 14 of 14 groups, same identities, same
9 ILF / 5 EIF split.** The transaction inventories (33 vs 38) differ only by split/merge and
EO-vs-EQ type calls, every one of which the runs themselves named in their doubts (CTC feed 1↔3,
email/SMS 1↔2, auto-booking 1↔2, reports EQ↔EO). Priced by the script: **UFP 195 vs 213 = ×1.092**.

**The floor holds even on the RFP.** 92 of 99 classified items are Low; both runs, unprompted, in
almost the same words: *"the RFP names workflows and sources far more richly than it names
fields."* The transaction axis follows the document's density (items ×2.5 against run 39); the
complexity axis does not move, because no pre-contract document enumerates fields.

| | HP40-1 | HP40-2 |
|---|---|---|
| items classified | 47 | 52 |
| data functions | 14 (9 ILF + 5 EIF) | 14 (9 ILF + 5 EIF) — same identities |
| transactions | 33 (EI 22 · EO 6 · EQ 5) | 38 (EI 23 · EO 8 · EQ 7) |
| non-Low classes | 2 Average | 1 High |
| outside scope | 21 of 73 | 22 of 73 |
| under-enumerated | 28 | 32 |
| doubts | 17 | 16 |
| **UFP (script)** | **195** | **213** |

Parametric level (script, `parametric_readout.txt`): P50 **120–163 table pd** across the two
curves and two counts — against the chain's raw 1342–1353 pd (×8–11) and the class's 600–1275 pd
(×4–8). BMS has no outcome; this is a cross-instrument distance, not a score.

| file | holds |
|---|---|
| `HP40-1.md` / `HP40-2.md` | verbatim transcripts |
| `HP40-1_components.tsv` / `HP40-2_components.tsv` | readouts for the script |
| `parametric_readout.txt` | script output on both counts, verbatim |
