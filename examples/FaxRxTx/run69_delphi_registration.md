# Run 69 — a Delphi among ten bare estimators on FaxRxTx, registered before launch (2026-09-17)

**The question (the author's, 2026-09-17):** the no-method control is ten bare runs whose curves differ, but not
much. What happens if the ten talk to each other and agree on a figure — does the agreed figure land nearer the
actual effort than the plain mean of the ten independent answers? One question, one run.

**Why it is worth a run.** `findings.md` §3 cites SEEAgent (Bui, Dam, Hoda 2025) as evidence that debating agents
estimate well. Read closely, that paper estimates single user stories in story points with agents fine-tuned on the
project's own history, and has no ablation separating the debate from the fine-tuning. Whether talking helps
identical estimators with no history, at RFP stage, is not measured there. This run measures it on the one case
with a known actual.

## Design, declared once

- **Participants:** ten general agents, no sensor definition, model `opus` (`claude-opus-5`), launched together,
  none seeing another. The same participants carry through all rounds (each is continued with its context intact),
  so the comparison is inside one batch — runs 41 and 43 showed the level moves ×1.145 between batches of the
  identical prompt a day apart, which would swamp the effect if round 1 were borrowed from them.
- **Round 1:** the pinned prompt of run 41, `run41_raw/prompt_baseline_faxrxtx.txt` (md5 of the LF form
  `c17b874b1101f32f6d8c1ff7a151e7df`), unchanged. **Deviation from runs 41/43, declared:** the text is not pasted
  into the launch message; each participant is told to read that one file and nothing else (one permitted tool
  use, checked in the transcript). Reason: byte-exactness of the input over ten launches.
- **Rounds 2 and 3:** the moderator (the orchestrating session) writes one sheet per round: the ten replies of the
  previous round **verbatim**, anonymised P-1 … P-10, quarantine notices removed, **no moderator commentary, no
  statistic, no outside number**. Each participant is told which P it is, reads that one file, may revise or hold,
  says what moved it, and closes with the same `TOTAL / RANGE / TEAM x DURATION / DECLARATION` block. Classic
  Delphi by rounds with full anonymous feedback; numbers are visible, as in Delphi, not hidden as in the wideband
  variant.
- **Stop:** after round 3, or earlier if max/min of the ten totals ≤ ×1.10.
- **The consensus** is the median of the last round's ten totals. **The comparison:** round-1 mean and median
  against the consensus, each against the actual 13 745 net task hours = 81.8 person-months of the prompt's A9
  convention (168 h), which no participant and no sheet ever sees.
- The moderator knows the actual; that is why the sheets are verbatim and carry nothing of the moderator's.

## Registered expectations

1. **Round 1 looks like batches 1–2:** mean 110–150 pm, CV 10–17%, max/min ×1.4–1.9.
2. **The spread collapses:** max/min ≤ ×1.25 by round 3; the participants farthest from the round-1 median move
   most, toward it.
3. **The centre does not come down:** consensus ≥ round-1 median (−3% tolerance). Union of work items pushes up;
   nothing in the exchange pushes down. Expected shift 0 … +15%.
4. **No nearer the actual:** |ln(consensus / 81.8)| ≥ |ln(round-1 mean / 81.8)| − 0.03. Round 1 is expected
   ×1.4–1.8 above the actual, the consensus the same or higher.
5. **Declared ranges narrow while the miss stays:** the mean declared high/low ratio falls from round 1 to round 3,
   and fewer of the ten ranges contain 81.8 pm after the talking than before it.

## What would overturn this reading

- The consensus lands materially nearer the actual than the round-1 mean (log distance smaller by more than 0.1):
  then the exchange carries information the independent runs lack, and the next question is which — it would be
  visible in what the participants say moved them.
- The spread does not collapse: then the ten are less alike than "one model, one text" predicts, and the
  no-method family's width means something else than sampling noise.

## What it is not

Not a reading of the instrument and never drawn as one: a control beside the no-method family. Whatever comes out,
no figure of the run 61–67 estimate moves.
