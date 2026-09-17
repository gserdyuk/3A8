# Runs 72 and 73 — the Delphi under three rules: do the panels stop inventing lines and stop drifting apart? Registered before launch (2026-09-17)

**Where this comes from.** Runs 69–71: three panels of identical bare estimators agree on the list of deliverables
and on the size of each line, and still end ×1.17 apart, because (a) each panel breeds its own cross-cutting lines —
a novelty tax, a glue factor, discounts, a burst line — that one participant invents and the rest adopt, adding being
free and removing being rare, and (b) QA is booked inside the lines by some and on top of them by others. The author's
two proposals, 2026-09-17: **forbid invented lines by a criterion of admissibility, and push the panel to remove lines,
not only add them, by making additions contestable; and settle QA by rule — every line includes its testing.**
The author's remark on what this is: "so we are implementing another method — I will survive that."

## The three rules (in the prompt, `run72_raw/prompt_rules.txt`, built by `make_prompt.py` from run 41's pinned prompt)

1. **A line includes its testing.** Whole-team effort per block: designed, built, tested, stabilised. No QA line, no
   uplift, no percentage on top.
2. **A line is a thing built or work done, and cites the text** (a section of the description or an assumption). No
   lines for risk, novelty, friction, glue, omissions, discounts or rounding — those go to RANGE, never to TOTAL.
3. **One line on top:** PM/coordination, in person-months, with its basis. TOTAL is the sum of the lines.

## The contest (in the round instructions)

- **Round 2:** read both parts of the sheet; revise or hold; give the full table; list under the heading **ADDED**
  every line not in your round-1 table, with its citation and person-months (or "none").
- **Round 3:** the sheet carries every ADDED block verbatim as CONTESTED ADDITIONS. Each participant votes **KEEP** or
  **REJECT**, with a reason, on each distinct contested item, and may also name any other line on the sheet it holds
  inadmissible under rule 2. Then its full table.
- **Round 4, only if something is rejected:** the moderator tallies the votes (a contested item falls if at least
  half of the ten reject it; the tally and the mapping of differently-worded items to one item are the moderator's,
  published with the votes) and tells the panel which items fell; each participant restates its table without them.
- The burden is on the addition: a line enters a table freely, and stays only if its author cited the text and the
  panel did not throw it out.

Everything else as runs 69–71: ten fresh bare agents per panel, model `opus`, two panels launched together and blind
to each other, verbatim anonymous sheets with nothing of the moderator's except the mechanically copied ADDED blocks
and, in round 4, the tally. **One change of plumbing:** the sheet comes in two files and two reads are permitted per
round, one of each, because run 70's single round-3 sheet was cut off by the read limit.

## Registered expectations

1. **No invented lines survive.** In the final tables, lines that are not work (tax, glue, friction, discount,
   rounding, blanket uplift) are carried by no more than 1 of 10 in each panel; separate QA lines by no more than 1 of
   10. (Runs 69–71: 4–7 of 10 and 6–8 of 10.)
2. **The panels stop moving apart.** max/min of the two consensus figures ≤ ×1.08, and no larger than the max/min of
   the two round-1 means plus 0.02. (Runs 69–71: means ×1.08 → consensus ×1.17.)
3. **The upward drift stops.** Consensus within −5 … +3% of the panel's own round-1 median. (Runs 69–71: +3.3%, 0%,
   +5.4%, never down.)
4. **The level** lands in 115–140 pm for round-1 means and for consensus figures alike — the "testing inside the line"
   school of runs 69–71. It will not come nearer the actual (81.8 pm): every line is still sized from the model's
   own prior. Registered as: consensus ≥ ×1.4 of the actual in both panels.
5. **The contest bites both ways.** At least one contested addition is rejected by a majority in at least one panel,
   and the Rx delivery path — the one real omission of runs 69–71 — is either present from round 1 (the citation rule
   makes participants walk the text) or survives the contest in both panels.
6. **Same list as before.** The eleven source-named lines of runs 69–71 are carried by at least 9 of 10 in both
   panels, with panel medians within ×1.25 of the run 69–71 medians.

## What would overturn this reading

- The panels still end more than ×1.10 apart with no invented lines left: then the between-panel instability is not
  made of memes and bookkeeping, it is in the line sizes themselves, and rules cannot reach it.
- The contest rejects real work (the Rx path, or another line the source plainly asks for): then majority voting
  among copies of one model is as unreliable for removal as free adoption is for addition.
- Totals fall well below 115: then rule 1 is being read as "drop the testing", not "fold it in", and the rule's
  wording, not the estimators, is what was measured.

## What it is, and is not

No longer the no-method control: three rules and a contest are a method, a light one, and the runs are recorded as
such. It is a measurement of how much of the chain's stability comes from rules alone — a closed notion of what a
line is, a pinned bookkeeping convention, risk kept out of the centre. It prices nothing for the run 61–67
estimate, and no figure of that estimate moves.
