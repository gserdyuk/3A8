# Run 72 — the moderator's tally of the round-3 votes

Rule (registered): a contested item falls if at least half of the ten reject it. The grouping of differently worded
items into one item, and the reading of qualified votes, are the moderator's; the votes themselves are in
`R3_P-*.md` under the heading VOTES.

| item | REJECT | KEEP | outcome |
|---|---|---|---|
| Data layer: DB schema, inter-component API, Lustre integration (P-1) | — | all ten | stands |
| Load-generation and failure-injection rig for the burst mode, with the end-to-end campaign run on it (P-1; the rig half of P-9; P-4's and P-7's narrowed form) | — | all ten | stands |
| Render worker host, split from the per-format work (P-4, P-10) | — | all ten | stands |
| Production rollout and cutover to the point v1 can be decommissioned (P-4, P-8, P-9, P-10) | — | all ten | stands |
| Coexistence with v1 through the transition (P-6, P-9, P-10) | — | all ten | stands |
| Interface work with the reused PoP software and routing as a line of its own (P-9) | P-2, P-7, P-8, P-9 (its author) | P-1, P-3, P-4, P-5, P-6, P-10 — most of them "only where no Rx/Tx line already carries the hand-off" | stands (4 of 10); withdrawn by its author |
| **Scale and burst hardening in its broad wording — "distribution, failure survival and delivery control", hardening of the blocks to target scale (P-3, P-7; the same wording in P-4's, P-8's and P-10's round-2 tables; the tuning half of P-9)** | P-1, P-3 (its author), P-5, P-9, P-10 | P-2, P-6, P-8; P-4 and P-7 voted KEEP "only in the narrow form of the rig and the campaign", which is the item above | **falls (5 of 10)** |
| **Cluster runtime and burst hardening, 10 pm (P-6)** | P-1, P-2, P-3, P-4, P-6 (its author), P-7, P-9, P-10 | P-5, P-8 | **falls (8 of 10)** |

Not contested but named inadmissible by several: the "TOTAL (sum)" row inside P-8's table (P-2, P-4, P-10) — arithmetic, not
a line; it changes no figure.

Reasons given for the two falls, in the panel's words: A6 calls distribution, failure survival and delivery control
mandatory properties of the blocks; hardening a block to its target scale is that block's stabilisation, which rule 1
puts inside its line; carried on top it is "an uplift wearing a line's clothes". What survives of it is the thing
built: the rig and the campaign run on it.
