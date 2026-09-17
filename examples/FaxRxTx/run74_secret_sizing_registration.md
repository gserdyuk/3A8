# Run 74 — a fixed list sized in secret: does averaging do what debating could not? Registered before launch (2026-09-17)

**Where this comes from.** Runs 69–73: five panels of ten identical bare estimators. Talking gives one list of
deliverables, and under three rules with a contest a clean one; it does not give one number. Two rule-bound panels
ended ×1.10 apart with every structural difference gone, each internally unanimous on integers the other panel does
not share: a line's size, which nobody can cite, is settled by copying the first defensible figure on the sheet. A
look back at the same data (no new run): the per-line means of the ten *secret* round-1 tables of panels D and E
already stand as close as the debated figures do, and on most lines closer. The author's proposal, 2026-09-17:
**have the agents size the work in secret and let the moderator average** — and the author's argument for it against
a table of norms: a norm table is only as good as its reasonableness, whereas an average is grounded in the
estimators' own judgement of this text.

**The method under test, as a division of labour.** The list comes from the debate under rules (that is what debate
does well). The numbers come from a secret ballot: nobody ever sees anybody's figure, so there is nothing to anchor
on; the moderator takes the median per line; the spread of the ballot is published as the uncertainty instead of
being talked away; stability is bought with the number of estimators, not with rounds.

## Design

- **The list:** the seventeen lines panel D (run 72) ended with after its contest, carried by all ten of its final
  tables; wording from those tables with every figure and staffing hint removed (`run74_raw/make_prompt.py` →
  `prompt_fixed_list.txt`, built from `run72_raw/prompt_rules.txt`; the three rules stay in force). No figure of any
  participant of any run is in the prompt. The participant is told the list is fixed and its estimate secret.
- **Participants:** forty fresh bare agents, model `opus`, launched together, the launch message of runs 69–73 with
  the file name changed; one permitted tool use (the read of the prompt). **One round, no sheet, no exchange.**
- **Groups, fixed now by launch label:** G1 = P-1…P-10, G2 = P-11…P-20, G3 = P-21…P-30, G4 = P-31…P-40. A group's
  estimate is the sum over the lines of the group's median for the line. Alongside, 2000 seeded random partitions
  into groups of 5, 10 and 20, so the result does not hang on one partition (`run74_raw/secret.py`).
- A reply with a line missing or a row added is reported and left out of the line statistics, not repaired.
- Commit subjects carry no figure until the series is over (they reach participants through the harness).

## Registered expectations

1. **Groups of ten agree better than debating panels.** max/min of the four registered group estimates ≤ ×1.10
   (four groups, so a stricter test than the two-panel ×1.10 of runs 72–73 and ×1.17 of runs 69–71); for a random
   pair of groups of ten, the median max/min ≤ ×1.05.
2. **Agreement is bought by numbers.** The median max/min over random partitions falls from groups of 5 to 10 to 20,
   roughly as one over the square root of the group size; two halves of twenty within ×1.04.
3. **Individuals still disagree, and that is now visible.** Own totals spread max/min ≥ ×1.4 across the forty; on at
   least half of the lines the 90th/10th percentile ratio is ≥ ×1.6. Expected to be widest on the lines the source
   says least about (Rx path, Tx path, rig, rollout), narrowest on the ones it pins (immersion, formats).
4. **The level** is that of the rule-bound panels: the estimate of all forty lands in 125–150 pm, i.e. ≥ ×1.5 of the
   actual (81.8 pm). Averaging removes scatter, not the model's prior on this text.
5. **No line-level anchoring.** No line on which thirty or more of the forty give the same figure, except where the
   source itself gives the figure (immersion, "about 1–2 months" of a team).

## What would overturn this reading

- The four groups stand ≥ ×1.13 apart: then the between-panel difference of runs 69–73 was never anchoring or
  sampling alone, and there is a source of variation that neither rules nor secrecy nor ten-fold averaging reaches.
- The spread of own totals collapses (max/min < ×1.2): then a fixed list already pins the number, the debate's list
  was the whole of the instability, and the secret ballot adds nothing to it.
- The level moves by more than ×1.15 from the rule-bound panels' (below 118 or above 165): then the wording of a
  fixed list, not the estimators, sets the level, and the list's wording becomes the thing to pin and test.

## What it is, and is not

A measurement on the debate line of work opened 2026-09-17, beside the instrument: it prices nothing for the run
61–67 estimate and no figure of that estimate moves. It says nothing yet about calibration — a stable figure that
stands ×1.5 above the actual is a candidate for a calibration constant only once the same is measured on other cases.
The variant with a norm table (classify each line, price from a pinned table) is not run here; if wanted, it runs
next on the same list, so the two ways of fixing a line's size are compared like for like.
