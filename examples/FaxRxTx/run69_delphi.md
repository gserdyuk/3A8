# Run 69 — a Delphi among ten bare estimators on FaxRxTx: what talking bought (2026-09-17)

Registered before launch in `run69_delphi_registration.md`. Ten general agents with no sensor definition, model
`claude-opus-5`, the pinned no-method prompt of run 41 (md5 `c17b874b…`), launched together. Round 2 continued the
same ten, each with its own context, after one read of `run69_raw/sheet_R2.md` — the ten round-1 replies verbatim,
anonymous, nothing of the moderator's in it. Raw replies `run69_raw/R1_P-*.md`, `R2_P-*.md`; per-round ledger
`ledger.jsonl`; helper `delphi.py`. The run stopped after round 2 by its registered rule (max/min ≤ ×1.10);
`sheet_R3.md` was built and never sent.

## The result

Person-months of the prompt's A9 convention (168 h). The actual effort, 13 745 net task hours = 81.8 pm, was seen by
no participant and is in no sheet.

| | round 1, independent | round 2, after reading each other |
|---|---:|---:|
| totals | 145 · 105 · 120 · 135 · 125 · 130 · 120 · 120 · 130 · 120 | 135 · 125 · 130 · 128 · 125 · 125 · 128 · 125 · 125 · 130 |
| mean / median | 125.0 / 122.5 | 127.6 / **126.5 — the consensus** |
| CV · max/min | 8.6% · ×1.38 | 2.6% · **×1.08** |
| against the actual | mean ×1.53, median ×1.50 | mean ×1.56, median ×1.55 |
| declared high/low, mean | ×2.25 | ×2.24 |
| declared ranges that contain the actual | 4 of 10 | **1 of 10** |

**The answer to the question asked:** the agreed figure is no nearer the actual than the plain mean of the ten
independent answers — it is marginally farther (log distance 0.436 against 0.424). Talking removed four fifths of
the disagreement and none of the error.

## Registered expectations, scored

| # | registered | happened | |
|---|---|---|---|
| 1 | round 1 like batches 1–2: mean 110–150, CV 10–17%, max/min ×1.4–1.9 | mean 125.0; CV 8.6%; ×1.38 | level met, **spread tighter than registered** |
| 2 | max/min ≤ ×1.25 by round 3; the farthest move most, toward the median | ×1.08 after **one** exchange; P-2 +20, P-1 −10, the two outliers, moved most | **met**, faster than expected |
| 3 | consensus ≥ round-1 median, shift 0 … +15% | 126.5 against 122.5, **+3.3%** | **met** |
| 4 | no nearer the actual | ln 0.436 against 0.424 (mean), 0.404 (median) | **met** |
| 5 | declared ranges narrow, fewer contain the actual | width unchanged (×2.25 → ×2.24); containing the actual 4 → 1 | **half met** — see below |

Neither overturning condition occurred.

## How the convergence happened — it was argument, not voting, and it still did not help

Every participant said what moved it and what it rejected. Three mechanisms account for all the movement:

- **A double count found by comparison (down).** P-1, P-4, P-5 and P-9 each saw that a QA/PM uplift had been applied
  on top of lines already sized whole-team (P-3's and P-9's sheets made it visible). P-1 145 → 135, P-4 135 → 128.
- **A missing line found by comparison (up).** Four sheets carried the inbound delivery path — PoP-to-data-centre
  transfer, the per-user TIFF-or-PDF branch, outbound email at a million messages a day — and four did not. P-2,
  P-7, P-8 and P-10 checked it against the source text, found it in §2, and added 5 pm each. P-2 also added the
  DB/API contract line. This is the union-of-work-items effect the registration expected, and it is why the centre
  rose.
- **Regression of one line to the group (both ways).** The delivery-control core was priced 16 to 28 pm; after the
  exchange everyone sat at 18–24. P-6 and P-9 came down from 28, P-3, P-7 and P-8 came up from 16–20, each giving a
  reason, none giving evidence the other side lacked.

All ten rejected both outliers (105 and 145) with the same two arguments, and the low floor of the ranges rose
(70–100 → 80–95) because "having found scope I had missed, the everything-is-thinner case is weaker". That is
expectation 5's real shape: **the ranges did not narrow, they moved up and away from the actual** — four ranges
contained 81.8 pm before the talking, one after.

Two participants wrote the limit of the exercise themselves. P-5: "all ten of us ran the same bottom-up
decomposition over the same component list from the same document, so we share a method bias rather than
triangulating independently." P-10: "Ten applications of one method share that method's bias … the clustering at
120–130 is weak evidence." P-2 noticed that nine of ten had answered "8 people" and called it arithmetic, not
corroboration. They saw it, said it, and converged anyway — nothing in the exchange could tell them which way the
shared bias points.

## What it means

- **For the instrument:** the measurement behind `METHODOLOGY.md` §1 now exists. A Delphi among copies of one model
  produces agreement (CV 8.6% → 2.6%) without accuracy (×1.53 → ×1.56). An agreed figure from such a panel would
  look three times more certain than the independent runs and be exactly as wrong — the false convergence the
  method was built to avoid. Independence has to come from methods that cannot see each other's blind spots, not
  from voices.
- **For the no-method family on the chart:** its width is sampling noise of one model and collapses on contact; its
  level is the model's prior on this text and does not move. The thin ochre curves should keep being drawn as a
  family and never pooled — pooling them is what this run did, and it bought nothing.
- **What the exchange is good for:** finding omissions and double counts in a decomposition. Both corrections here
  were real and checkable against the source. That is a review function, and the chain already has a stronger form
  of it (the crossing reports work no declared activity covers; the diagnosis names each method's blind spot).
- **On `findings.md` §3** (SEEAgent, Bui et al. 2025, cited as confirmation that debating agents estimate well):
  that paper estimates single user stories in story points with agents fine-tuned on the project's own history and
  reports no ablation separating the debate from the fine-tuning. It does not bear on this setting; this run does.

## Protocol notes

- Each participant made exactly one tool use per round, the permitted read (transcripts checked: `Read` of the prompt
  in round 1, of `sheet_R2.md` in round 2). For five participants the harness's usage counter showed 2 tool uses in
  round 2 while the transcript holds one `Read`; the ledger records the transcript.
- The deviation registered in advance (prompt delivered by one file read, not pasted) held for all ten.
- Registered and not done: quarantine notices were to be removed from the sheet. They were left in, because removing
  them is a moderator's edit of a verbatim reply; they name only the injected repository status every participant
  already had (branch, five commit subjects without figures, the memory index, tool listings). Two participants noted
  that the commit subjects mention this very run; none contained a number.
- Batch level: this batch's round-1 mean is 125.0 against 120.5 (run 41) and 138.0 (run 43) — a third batch of the
  same prompt, inside the earlier two. Pooled n = 30: mean 127.8.
- Not drawn on the report: a control, as registered. No figure of the run 61–67 estimate moves.
