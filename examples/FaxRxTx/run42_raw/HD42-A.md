# Run 42 — `Hotyn-D 2.0` × Opus 5 — sizing of HM29-OA2, batch A (30 elements)

`tool_uses: 0`. Clean contamination check; harness injection quarantined (branch, commit subjects
naming runs 38-40, `Hotyn-P`, "UFP 78 vs 82"). **Tenth independent catch.**

## Sizes

| class | n | elements |
|---|---:|---|
| S | 12 | HM2-20, 24, 26, 27, 37, 41, 42, 43, 44, 45, 46, 47 |
| M | 17 | HM2-03, 15, 16, 17, 18, 21, 22, 23, 28, 29, 30, 31, 33, 34, 36, 48, 49 |
| L | 1 | HM2-02 |
| XL | 0 | — |

**Statement kinds:** HM2-02 **behavioural** ("the receive-and-deliver-by-email core function … is
present in the new artefact" — a run-time scenario, not a policy) · HM2-03 **behavioural**.

**Unsizeable: 0.** All thirty enumerations were supported.

## The two judgements that move the most

1. **HM2-02 sized L on 7 direct components.** Counting the whole transitive inbound subtree gives 13
   (plainly XL); reading the parity property narrowly as two components ("receive", "deliver by
   email") gives M. The run took direct components — "sub-components are constrained through their
   parents, and counting both would count the same named thing twice."
2. **The seven renderers held at S, systematically.** F19's clause *"separately integrated and
   stabilised"* was deliberately **not** counted as a second action per renderer, because HM2-49 is
   the element the model declares as carrying the per-format fixture. Counting it would move all
   seven S→M in one stroke. The run names this as its single largest judgement call.

## Six closure violations named (none priced)

1. **F17 is covered by no element in this batch** — nothing integrates with the ready least-cost
   routing program. *(Closed in batch C: HM2-39.)*
2. **The send half of F16 is unclaimed** — HM2-37 stops at "packed as the archive a PoP takes".
   *(Closed in batch C: HM2-38.)*
3. **F05's user configuration has no owner here.** *(Closed in batch B: HM2-25.)*
4. **The recipient directory HM2-17 resolves against has no owner here.** *(Closed in batch B: HM2-88.)*
5. **The PoP-side counterparts of F01/F04/F38 are absent** — correctly: `assumptions.md` A1 puts PoP
   software out of scope. **Not a defect.**
6. **Failure paths for F12/F13 are absent** — a submission mail that will not parse, carries no usable
   fax number, or carries an unsupported format. **Genuinely open across the whole model.**

## Doubts: 25, of which 15 class-flipping

Named individually in the transcript. The systematic one is item 14 (the seven renderers). Two source
hedges were carried, not resolved: F01's "does not remember whether Australia was included" and F15's
"it seems" on the Black Ice driver class. One tension named and left: **F18 names seven formats while
F19 states 8–10 in all**, so the named set does not reach the stated total; HM2-48's extension point
is read as covering the remainder.
