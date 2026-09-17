# Runs 70 and 71 — the Delphi of run 69 repeated twice: is the consensus stable, and are the work lists alike? Registered before launch (2026-09-17)

**The author's question, after run 69.** That the agreed figure came no nearer the actual means little on one case
— the same can be said of the chain's calibration. Stability is the question: run the whole thing again, and again,
and compare the runs. And: *if the panels arrive at similar lists of work, that would be the valuable result.*

## Design

Runs 70 and 71 are run 69 again, each with ten fresh participants: the same pinned prompt
(`run41_raw/prompt_baseline_faxrxtx.txt`, md5 `c17b874b…`), the same launch message, model `opus`, one permitted read
per round, the same verbatim anonymous sheet, the same stop rule (max/min ≤ ×1.10, at most three rounds), the same
helper (`run69_raw/delphi.py`, given the run's folder). No panel sees another panel's sheet. The two panels are
launched together; each is its own batch in the sense of runs 41/43.

**One change, declared:** the round-2 instruction asks for the participant's **final decomposition table in full**,
not only what changed, so that work lists can be compared across panels. Run 69's ten are asked, after the fact, to
restate their final table with no re-estimation (`R3` in its ledger is a transcription, not a round).

**Protocol finding that shapes the launch.** Participants receive the repository status the harness injects,
including the five most recent commit subjects. The subject of run 69's result commit states how far the bare
estimates sat from the actual. Four ordinary commits with figure-free subjects are made before launch so that it is
no longer among the five; from now on a commit subject on this case carries no figure while a panel may still be
launched. Run 69's own participants were launched before that commit existed.

## What is compared

1. **Totals:** round-1 mean and median, consensus (median of the last round), spread per round — three panels.
2. **Work lists:** each participant's final table mapped by the moderator onto one vocabulary of lines, written down
   from run 69's tables before runs 70–71 are read: immersion · render workers · OCR · delivery-control core ·
   cluster management · NOC · portal · inbound-email parser (Tx) · inbound delivery path (Rx) · CDR capture ·
   DB/API/storage contract · old-system integration and coexistence · real-stream comparison and load testing ·
   rollout and cutover · QA uplift · PM uplift · integration drag / omissions factor. Per panel: which lines at least
   eight of ten carry after the exchange, and the median value of each line. The mapping is the moderator's
   judgement and is published with the tables so it can be checked.

## Registered expectations

1. **Each panel converges as run 69 did:** max/min ≤ ×1.15 after one exchange; consensus within −3 … +8% of its own
   round-1 median.
2. **The three consensus figures agree with each other no better than the three round-1 means do:** the exchange
   removes disagreement inside a panel, not the level a panel starts from. Registered as: max/min of the three
   consensus medians ≥ 0.7 × (max/min of the three round-1 means − 1) + 1. Expected range of all six figures:
   115–140 pm.
3. **The lists:** the lines the source document itself names (§6) are carried by all three panels from round 1. Of
   the lines it does **not** name — Rx path, DB/API contract, integration drag, a separate QA uplift — each panel
   ends with at least three of the four carried by eight of ten, **and they are the same ones across panels**.
4. **Line values:** after the exchange the panel medians of the big lines (delivery-control core, portal, NOC, render
   workers, comparison testing) differ between panels by no more than ×1.25; before the exchange the per-participant
   spread on the delivery-control core is ≥ ×1.5 in every panel.

## What would overturn this reading

- Consensus figures of the three panels much closer to each other than their round-1 means (say within 2% while the
  means differ by 8% or more): the exchange is then an attractor, a stabiliser of level, and worth more than run 69
  suggested.
- Panels that converge on **different** lists or on line values ×1.5 apart: then a panel's agreement is an accident of
  who was in it, and even the review function of the exchange is unreliable.

## What it is not

A control on the no-method family, as run 69. No figure of the run 61–67 estimate moves.
