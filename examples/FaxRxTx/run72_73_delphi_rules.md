# Runs 72 and 73 — the Delphi under three rules: what rules can reach, and what they cannot (2026-09-17)

Registered before launch in `run72_delphi_rules_registration.md`. Two fresh panels of ten bare agents, the pinned
prompt of run 41 with three rules added (`run72_raw/prompt_rules.txt`, built by `make_prompt.py`); round instructions
`run72_raw/round_instructions.md`; helper `run72_raw/delphi_rules.py` (two-part sheets, contested additions copied
verbatim); raw replies, ledgers, sheets in `run72_raw/`, `run73_raw/`; the moderator's vote tally
`run72_raw/tally_R3.md`; line mapping `run72_raw/lines_output.txt` (by `run70_raw/lines.py`). Chart:
`reports/report_2026-09-17T1152.html`.

**The rules.** (1) A line includes its testing — whole-team effort, no QA line, no uplift. (2) A line is a thing
built or work done and cites the text — no lines for risk, novelty, glue, discounts, rounding; those go to RANGE.
(3) One line on top, PM, with its basis. **The contest.** Round 2: list every added line under ADDED. Round 3: vote
KEEP or REJECT on every contested addition; an item falls if at least half reject it. Round 4, only if something fell:
restate the table without it.

## 1. The totals

Person-months of the prompt's convention. The actual, 81.8 pm, was seen by no participant.

| | panel D, run 72 | panel E, run 73 |
|---|---:|---:|
| round 1: mean / median · max/min | 143.2 / 146.5 · ×1.58 | 126.7 / 115.5 · ×1.90 |
| round 2: median · max/min | 150.0 · ×1.13 | 130.5 · ×1.27 |
| round 3 (votes): median · max/min | 149.0 · ×1.06 | 134.0 · ×1.19 — nothing fell, final |
| round 4 (after the tally): median · max/min | **148.0 · ×1.06** — final | — |
| against the actual, round-1 mean → consensus | ×1.75 → ×1.81 | ×1.55 → ×1.64 |
| declared ranges containing the actual, first → last | 1 → 0 | 5 → 0 |

Between the two panels: round-1 means ×1.13 apart, consensus **×1.10** apart. For comparison, the three free panels
of runs 69–71: means ×1.08, consensus ×1.17.

## 2. What the rules did

**They cleaned the tables completely.** In the twenty final tables there is not one line for risk, novelty, glue,
discount or rounding, and not one separate QA line (free panels: 4–7 of 10 and 6–8 of 10). Every line cites a
section or an assumption. All twenty tables sum exactly to their stated totals.

**They made removal ordinary.** In the free panels almost every move was an addition. Here the high estimators came
down as far as the low ones went up — panel D 165 → 151, 167 → 147, 168 → 148 and 106 → 147, 118 → 150; panel E
175 → 135, 163 → 149 and 92 → 125, 96 → 132 — and the arguments for coming down were the rules themselves, quoted:
*"that is the fear of overrun entering TOTAL, which Rule 2 sends to RANGE"*; *"carried separately it is an uplift
wearing a line's clothes"*; *"I cannot cite text for the excess"*; *"my own declaration puts coordination inside every
line, so a full-time PM on top charges the same hours twice"*.

**The contest worked, in both directions, and participants voted against themselves.**

| panel D, contested item | rejected by | outcome |
|---|---:|---|
| data layer: schema, inter-component API, Lustre | 0 | stands |
| load-generation and failure-injection rig, with the campaign run on it | 0 | stands |
| render worker host, split from per-format work | 0 | stands |
| production rollout and cutover to v1's decommissioning | 0 | stands |
| coexistence with v1 through the transition | 0 | stands |
| interface work with the reused components, as its own line | 4 | stands; withdrawn by its author |
| **"scale and burst hardening": distribution, failure survival, hardening of blocks to target scale** | **5**, its author among them | **falls** |
| **"cluster runtime and burst hardening", 10 pm** | **8**, its author among them | **falls** |

Panel E contested one item in earnest, the load and burst rig: 4 rejected it (two of them its own authors), 6 kept
it; it stands. The distinction both panels drew is exactly the one the criterion was meant to produce: **a rig is a
thing built and stays; "hardening" is a property of the blocks, its stabilisation is already inside their lines under
rule 1, and it goes.** In round 4 the one participant still carrying the fallen wording removed it and wrote that 3
of its 7 pm "goes nowhere — the total falls by 3", because he could not name the work that stayed. Real work was
never voted out: the Rx path, missing from two of panel E's round-1 tables, was added, contested and kept by all ten;
in panel D the citation rule had already put it in every round-1 table.

## 3. What the rules did not do

**They did not bring the panels together.** Consensus 148 against 134, ×1.10 — better than the free panels' ×1.17,
and the gap no longer grows with talking (×1.13 before, ×1.10 after), but it does not close. And it is no longer made
of invented lines or bookkeeping: the boundary-free sums now agree (delivery stack 33 vs 30, ×1.10 — free panels
×1.35; verification ×1.11 — was ×1.78; PM 14 vs 14 — overhead was ×1.50). What is left is **the ordinary lines
themselves**:

| line | D | E | | line | D | E |
|---|---:|---:|---|---|---:|---:|
| immersion | 12 | 10 | | Tx parser and hand-off | 8 | 6 |
| delivery-control core | 22 | 20 | | data layer / API | 9 | 7.5 |
| Rx path | 9 | 6 | | NOC | 9 | 8 |
| portal | 10 | 8 | | OCR | 6 | 5 |

A point or two per line, the same sign on almost every line, fourteen person-months in all. Inside a panel these
figures are not merely close, they are **identical**: in panel D all ten participants end with NOC 9, portal 10, OCR 6,
data layer 9, management tool 6, real-stream testing 10, immersion 12. Ten estimators do not independently arrive at
the same integer on seven lines; they copy the first defensible number on the sheet. The other panel copies a
different one. **Agreement inside, disagreement between — reproduced one level down, at the line.** This is the
overturning condition the registration named: the instability is in the line sizes themselves, and rules about what
a line *is* cannot reach what a line *costs*.

**They did not lower the level — they raised it.** Registered expectation: 115–140, the "testing inside the line"
school. Observed: 148 and 134, the level of the free panels' "QA on top" school. Folding testing into the lines does
not select the cheaper bookkeeping, it renames the dearer one: every line grew by the testing it now openly carries
(OCR 5 → 6, Rx 5 → 9, Tx 5 → 8, data layer 6 → 9, render 11.5 → 14 between free panel A and ruled panel D), and the
citation rule makes participants walk the text section by section, so tables run to 17–19 lines where the free ones
had 13–16, each with its own floor of a few person-months.

## 4. Registered expectations, scored

| # | registered | happened | |
|---|---|---|---|
| 1 | invented lines ≤ 1 of 10; separate QA lines ≤ 1 of 10 | 0 of 10 and 0 of 10 in both panels | **met** |
| 2 | consensus figures ≤ ×1.08 apart, and no further apart than the round-1 means | ×1.10; round-1 means ×1.13 | first half **missed** narrowly, second **met** — the panels no longer move apart, and do not meet |
| 3 | consensus within −5 … +3% of the panel's round-1 median | D +1.0%; E +16% (against its round-1 mean +5.8%; its round 1 ran 92–175) | **met in D, missed in E** |
| 4 | level 115–140 for round-1 means and consensus; consensus ≥ ×1.4 of the actual | means 143 and 127, consensus 148 and 134; ×1.81 and ×1.64 of the actual | band **missed** for D (too high); distance from the actual **met** |
| 5 | at least one addition rejected by majority; the Rx path present from round 1 or surviving the contest | two fell in D; Rx in all of D's round-1 tables, kept 10–0 in E | **met** |
| 6 | the eleven source-named lines carried by ≥ 9 of 10; medians within ×1.25 of runs 69–71 | all carried 10 of 10; six of eleven medians within ×1.25, the rest higher (testing folded in, finer partition) | list **met**, values **half met** |

Overturning conditions: (a) *panels still apart with no invented lines left* — **this is what happened**, at the
registered threshold (×1.10); (b) the contest rejecting real work — did not happen; (c) totals below 115 — the
opposite.

## 5. What it means

- **Rules fix what they name.** Admissibility, bookkeeping, where risk lives, the burden of proof on additions:
  all four were obeyed by every participant, argued with in the rules' own words, and enforced by vote against the
  voters' own lines. As a way to get a clean, comparable, fully cited decomposition out of a panel, this works and is
  cheap. It is the review function of runs 69–71 made reliable.
- **Rules do not fix magnitude.** With every structural source of disagreement removed, two panels still differ by
  ×1.10, all of it in line sizes, each panel internally unanimous on integers the other panel does not share. A
  number nobody can cite is settled by anchoring, and anchoring differs by panel. This is the project's founding
  finding — the model may choose rows, it must not choose numbers — measured again, from the other side: take away
  everything but the numbers and the numbers are what still moves.
- **Which is the argument for the chain, not against the experiment.** The chain closes this last freedom the only
  way it can be closed: the size of a line is not estimated, it is *classified* (count named things, read the class
  off thresholds) and *priced from a pinned table*. Runs 69–73 show how far a panel gets without that — a good
  list, clean tables, a confident number — and exactly where it stops.
- **Level.** Five panels, fifty estimators: consensus 126.5, 135, 147.5, 148, 134 against an actual of 81.8. None
  below ×1.55. Nothing done to the panels moved the level toward the actual; the level is the model's prior on this
  text.

## 6. Protocol notes

- Sheets in two parts, two reads per round: every participant read both parts in full; no truncation (run 70's
  defect did not recur). The harness's tool-use counter again showed more uses than the transcripts hold for a few
  participants (one at 4, one at 5 in round 3); the transcripts show the two permitted reads in every case, and the
  ledger records the transcripts. Round 4 used no tool.
- The moderator's only words to the panels, beyond the instructions, are the round-4 tally (`tally_R3.md`); the
  grouping of differently worded items and the reading of qualified votes ("KEEP only in the narrow form") are the
  moderator's judgement and are published with the votes.
- Commit subjects carried no figure before launch; participants again listed what they saw (run numbers, the words
  "Delphi", "panels", "three rules") and confirmed no figure.
- No longer a no-method control: three rules and a contest are a method. Recorded as such. No figure of the
  run 61–67 estimate moves.
