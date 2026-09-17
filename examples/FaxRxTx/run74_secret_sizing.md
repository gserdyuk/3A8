# Run 74 — a fixed list sized in secret by forty: averaging buys stability, and the list's wording sets the level (2026-09-17)

Registered before launch in `run74_secret_sizing_registration.md`. The seventeen lines panel D (run 72) ended with,
worded without any figure, fixed in the prompt (`run74_raw/prompt_fixed_list.txt`, built by `make_prompt.py` from the
rules prompt of runs 72–73; the three rules stay in force). Forty fresh bare agents, model `opus`, the launch message
of runs 69–73; **one round, no sheet, no exchange**: nobody ever saw anybody's figure. Replies verbatim
`run74_raw/R1_P-*.md`, ledger `ledger.jsonl`, per-line table `lines.tsv`, helper `secret.py`, its printout
`stats_output.txt`. Chart: `reports/report_2026-09-17T1325.html` (dotted ochre curve).

All forty replies are complete: seventeen rows, no row added, the stated TOTAL equal to the sum of the rows in every
one; one tool use each, the permitted read. Every participant reported the out-of-message material (repository
status, commit subjects, memory index) and none found a figure in it.

## 1. Stability — what the author asked for, and it is there

A group's estimate is the sum over the lines of the group's median for the line. Person-months of the prompt's
convention; the actual, 81.8 pm, was seen by no one.

| | max/min between groups |
|---|---:|
| the four registered groups of ten (P-1…10, 11…20, 21…30, 31…40): 175.5 / 177.0 / 171.5 / 176.0 | **×1.03** |
| the two registered halves of twenty: 178.0 / 175.0 | ×1.02 |
| for comparison — two debating panels under rules (runs 72–73) | ×1.10 |
| for comparison — three free debating panels (runs 69–71) | ×1.17 |

Random partitions (2000, seeded), so the result does not hang on one grouping — max/min of the group estimates:

| group size | groups | median | 90th percentile |
|---:|---:|---:|---:|
| 5 | 8 | ×1.21 | ×1.32 |
| 10 | 4 | ×1.09 | ×1.15 |
| 20 | 2 | ×1.03 | ×1.06 |
| a random **pair** of groups of ten (the like-for-like of two panels) | | **×1.04** | ×1.10 |

Two groups of ten that never talk stand ×1.04 apart; two panels of ten that talk stand ×1.10–1.17 apart. The
per-line picture is the same: the four group medians coincide exactly on seven of seventeen lines and differ by more
than ×1.10 on three (render host ×1.17, integration tests ×1.18, format renderers ×1.22). Agreement improves with
the number of estimators roughly as one over its square root, as registered.

**No line-level anchoring.** The most frequent figure on any line is given by 24 of 40 (CDR capture = 4); on the big
lines by 12–18 of 40. In panel D all ten ended with the same integer on seven lines. The replies are heavily
quantised — even numbers, 4–10 distinct values per line — which is the model's own habit, not copying.

## 2. Individuals still disagree — as one scale factor, not line by line

Own totals run 130 … 237, max/min ×1.82, CV 14%. Per line the 90th/10th percentile ratio is ×1.4–1.8. And the
disagreement is not independent noise on each line: across the forty, the pairwise correlation between lines is
**0.80 on average** (0.48–0.93). An estimator who is high on the delivery core is high on the portal and on the
rollout. Each participant carries its own scale — what a person-month buys — and applies it to every line. This is
why a single estimator's total does not average its own line errors out, why the median of ten does, and why the
spread of the ballot is an honest width for the number: not one of the forty declared ranges contains the actual
(lowest low: 95).

## 3. The level — the surprise, and the overturning condition that fired

**All forty: 174 pm (sum of line medians; 177.6 by means) — ×2.13 of the actual.** Registered: 125–150. The
registration named this as overturning: *"the level moves by more than ×1.15 from the rule-bound panels' … then the
wording of a fixed list, not the estimators, sets the level."* It moved ×1.18 above panel D's own consensus (148) on
panel D's own list.

Where the 26 pm came from — panel D's final line medians beside the secret medians:

| line | panel D | secret | | line | panel D | secret |
|---|---:|---:|---|---|---:|---:|
| **render worker host** | **4** | **14** | | Tx path | 8 | 10 |
| load / failure rig | 5 | 8 | | data layer | 9 | 12 |
| integration with reused + coexistence | 6 | 9 | | Rx path | 9 | 12 |
| cluster management tool | 6 | 8 | | PM | 14 | 18 |
| CDR capture | 3 | 4 | | format renderers | 10 | 12 |
| delivery-control core | 22 | 18 | | immersion | 12 | 10 |
| NOC | 9 | 8 | | integration tests | 10 | 9 |

Down: the two lines everyone sizes first and largest (core, immersion). Up: almost everything else, and most of all
**the lines that panel D had carved out of other lines**. "Render worker host" was split from the renderers during
the debate; its authors knew it was a 4-pm remainder of something already counted. Handed over as a standing line
with a full description — job model, node-side execution, restart and isolation, printer-driver harness — it reads
as a subsystem and is sized at 14. The same for the rig, the integration line, the management tool. A fresh reader
gives every named line a subsystem's floor; the authors of a decomposition know which lines are slivers. (Many
participants saw it and said so — "the L2/L3 boundary invites double counting" — and, the list being fixed, sized
both.) PM then follows at its usual ~12% of a larger sum.

So the instability that the secret ballot removed from the *numbers* has a twin in the *list*: the level of the
estimate depends on how finely the list is cut and how richly each line is described, and a second panel's list,
cut differently, would give a different level — stable to ×1.03, and different.

## 4. Registered expectations, scored

| # | registered | happened | |
|---|---|---|---|
| 1 | four groups of ten ≤ ×1.10; random pair of tens, median ≤ ×1.05 | ×1.03; ×1.04 | **met** |
| 2 | agreement improves with group size roughly as 1/√n; two halves of twenty within ×1.04 | ×1.21 → ×1.09 → ×1.03; halves ×1.02 | **met** |
| 3 | own totals max/min ≥ ×1.4; p90/p10 ≥ ×1.6 on at least half of the lines, widest where the source says least | ×1.82; ≥ ×1.6 on 5 of 17 lines, widest on the render host, not on Rx/Tx | first part **met**, second **missed** — the spread is one scale factor per estimator, not line-specific doubt |
| 4 | level 125–150, ≥ ×1.5 of the actual | 174; ×2.13 | band **missed** (too high); distance **met** |
| 5 | no line with ≥ 30 of 40 on one figure, immersion excepted | the most is 24 of 40 | **met** |

Overturning conditions: groups ≥ ×1.13 apart — no. Spread of own totals collapsing — no. **Level more than ×1.15 off
the rule-bound panels — yes.**

## 5. What it means for the method of debates

- **The division of labour holds for stability.** List by debate under rules, numbers by secret ballot and median:
  ten estimators give a figure that another ten reproduce within ×1.04, twenty within ×1.03, with no rounds at all
  for the numbers. The author's proposal does what it was proposed for. It is also the cheapest step of the whole
  series — one message per estimator.
- **The ballot's width is the honest uncertainty** — ×1.8 between individuals, one scale factor each — where a
  debating panel reports ×1.06 and is wrong about it.
- **The freedom has moved to the list.** A fixed list is sized ×1.18 dearer by strangers than by its authors, the
  carved-out lines ×1.5–3.5 dearer. Two things follow. (a) The list that goes to a ballot must be written for a
  stranger: a line carved from another says so ("the remainder of X after Y; X is priced separately"), or carved
  lines are merged back before the ballot. (b) The level cannot be read off one list. The next measurement is the
  obvious one: panel E's list (run 73) under the same secret ballot — if two lists of one project, each stable to
  ×1.03, stand ×1.1–1.2 apart, the list is the remaining instrument error and the way to pin it is the way the chain
  pins it (a closed vocabulary of what a line may be), not more estimators.
- **Level against the actual: ×2.13, worse than any panel.** Averaging removes scatter and leaves the model's prior
  on the text; finer, richer lists raise it. None of this is calibration; whether a stable ×2 is a usable constant is
  a question for other cases, not this one.
- The variant with a norm table was not run. After this result its place is clearer: a table fixes the scale factor
  that each estimator otherwise brings with it (§2) — the one thing averaging needs ten estimators to cancel — and
  its reasonableness can be checked against exactly this ballot.

## 6. Protocol notes

- The harness allows twenty concurrent subagents: P-27's first launch was refused, and it was launched alone after
  the first twenty had finished; same message, same file. P-21…P-40 otherwise started while P-1…P-20 were finishing.
  Nothing passed between participants at any point.
- The commit subject of the registration carried no figure; participants quoted what they saw of it ("run 74",
  "a fixed list of lines sized in secret") and nothing numeric.
- A method, not the no-method control: rules, a given list and a moderator's median. No figure of the run 61–67
  estimate moves.
