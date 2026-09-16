# Review — 2026-09-15 — the three chain sensors and the estimate-product run order

**Requested by the author** after run 53 (the SAS product model through the plugin entry point came out
at half of run 44's anchored structure) and the void run 54 (a thinking-budget setting that did not take
effect). **Written from the record only** by a read-only review agent launched from the orchestrating
session; nothing was modified. Scope: `agents/model-builder.md` (13 820 chars), `agents/work-crosser.md`
(10 867), `agents/work-estimator.md` (5 626), `skills/estimate-product/SKILL.md` (5 349), read against
`README.md`, `PIPELINE.md`, `docs/instrument.md` §3, the run 44 / run 53 records and raw replies, and
the run 45 / 47 prompt generators.

One correction to the premise first. The model-builder definition on disk is **13.8 k characters, not
~30 k**. If the harness transcript shows ~30 k of system-side text before the 29 k prompt, the other
~16 k is harness preamble (environment block, tool description, the `gitStatus` injection every sensor
already quarantines), not sensor text. That preamble is outside the repository's control and is not
recorded in either MANIFEST; if runs are to be compared, its size belongs in the launch record next to
the model alias.

Measured composition of the replies, which the advice below rests on (chars per section):

| section | HM44-OA2 (79.6 k) | HM53-1 (48.0 k) | HM53-2 (55.4 k) |
|---|---:|---:|---:|
| §2 skeleton | 5.5 k | 5.3 k | 5.4 k |
| §3 accretion log | **26.1 k** | 13.8 k | 14.7 k |
| §6 final model | **18.9 k** | 9.5 k | 12.1 k |
| §7c coverage completeness | **12.1 k** | 9.8 k | 11.4 k |
| §9 assumption log | 7.6 k | 3.7 k | 5.4 k |
| §4, §5, §7, §7b, §8, §1 together | 8.5 k | 4.5 k | 4.1 k |

Three sections carry 70 % of the reply, and two of them (§6, §7c) are restatements of the third.

---

## 1. The three sensor texts

### 1a. `agents/model-builder.md` (Hotyn-M 1.1)

**What invites open-ended deliberation or very long output**

- *M4 — Skeleton*: "Read the requirement list **as a set, not as a sequence**. Posit a tree … **Stop**
  when every requirement has at least one plausible attachment point". This is a think-first
  instruction by construction: nothing can be written until all 146 obligations have been held against
  a posited tree in the head. It is the method, so it must stay, but it is where the first 64 000
  thinking tokens went (see §3 below).
- *M5*: "**Repeat passes until a pass adds nothing and defers nothing.**" and *M6*: "Completion has its
  own fixpoint with the same only-adds rule". Two fixpoints described in prose, each a full walk.
  Combined with "**Only additions.** Nodes are never removed and never moved" and "**Resolution is
  final**", an error once written cannot be repaired in the output — so a careful model computes the
  whole tree before committing the first row. Monotonicity is the method; the *consequence* (plan
  everything, then transcribe) is not, and the text nowhere says the walk should be written as it
  happens.
- *M5*: "**Log every verdict, including `covered`.**" — 146 rows × 8 columns per pass. This is the
  measurement and must stay, but the row format (Output §3) demands "requirement id · pass · verdict ·
  covering node(s) · nodes added and their parent · what was missing (for partial) · one-line reason ·
  ambiguity flag" — the `pass` column is redundant under a per-pass heading, and "nodes added and their
  parent" repeats what §6 will carry.
- *Output §7c*: "one row per requirement of the pinned list: the nodes covering it, the part each
  realises, and your verdict **whole / residue** … 'Whole' is asserted explicitly per requirement; it
  is never inferred from the absence of a complaint." This sentence forces 146 rows (12 k chars in OA2)
  that repeat §3's covering nodes and §3's "missing part" column. Under M5 "Resolution is final", the
  whole/residue verdict is already determined at the end of the requirement's accretion row; §7c adds
  no information except the residue list.
- *Output §8*: fifteen readings including "coverage assignments, and nodes per requirement ·
  requirements per node" — HM53-1 read this as two histograms. Every one of these counts is derivable
  from §6 by the assembly script (the run 53 record did exactly that and checked it against §8).
- *Output §9*: "entries you found ambiguous, **verbatim**" — the sensor re-quotes requirement texts the
  orchestrator already holds pinned (5–7 k chars); HM53-2 even had to redact figures inside the quotes
  to honour M8.
- *M2*: "**the check at every parent**: total coverage equals the union of the children's totals plus
  the parent's own residue" — an all-parents check to be done but never printed, i.e. pure thinking
  load.

**Redundant or restated**

- "A requirement is never silently absent" is stated four times: M2 ("A part is not an answer … it is
  how work disappears without anybody deciding to drop it"), *The imperative* (whole section), M7 1a,
  Output §7c. One statement plus one output section suffices.
- Provenance vocabulary is stated twice and inconsistently: M4 fixes `posited / accreted / derived`;
  Output §2 says "All `implied` at this stage" and Output §6 says "provenance (`stated` / `implied`)".
  Both run 53 sensors flagged this and invented **different** mappings — HM53-1 §9: "`stated` means
  the node's total coverage is non-empty"; OA2 §6: "`accreted` = stated, `posited` and `derived` =
  implied". A free choice created by the definition's own inconsistency.
- Engine identity, paragraph 2 (city/letter scheme, "Hotyn is a new generation, not a newer Lytin") —
  repeated in all three sensors, of no use to the run.
- Rationale paragraphs that are documentation, not instruction: M8 ¶2 ("This is what keeps the model
  reusable — for additive costing, for simulation …"), M2 last ¶ ("A model that declares nine
  requirements on a portal aggregate …"), M4 ¶¶4–5 (why the empty-total test is not applied to own
  coverage — the rule is one sentence, the defence is two paragraphs), M7 ¶¶5–6 ("This removes one
  specific obstacle to comparing two models …"), Output §6 ("which is exactly what happened to one of
  run 18's four raw records").

**Ambiguity that flips "covered" vs "new leaf" — the run 53 mechanism**

The text never says whether a posited node may hold own coverage. Read together:

- M4: "Posit a tree of nodes with names and **intended scope**. Attach no requirements. Assign no
  coverage." — the *intended scope* column has no length or content limit, so a skeleton row can be
  "create one record at a time; save as draft" (HM53-1 N22), which is a leaf that already "realises"
  P-1/L-1 before accretion starts.
- M4: "Stop when every requirement has at least one plausible **attachment point**" — an attachment
  point can be read as *a parent to hang a new leaf under* (run 44: skeletons of 69–72 aggregates,
  160–167 accreted leaves) or as *a node that itself realises the obligation* (run 53: skeletons of
  64–74 leaves, 43–64 accreted).
- M5's `covered` verdict: "the existing structure already realises this" — "existing structure"
  includes posited leaves with rich intended scope. Both run 53 sensors say so in their own words:
  HM53-1 §9 "**Posited leaves count as existing structure.** A requirement that an already-posited
  leaf realises got the verdict `covered`"; HM53-2 §9 "89 requirements were judged covered, mostly by
  skeleton leaves whose intended scope already realised them … A finer or coarser skeleton would move
  requirements between covered and not covered."
- M4 ¶5 implies the opposite reading without stating it: "Every aggregate has empty own coverage by
  rule, and testing that would report **the whole spine** as findings" — i.e. the author pictures the
  skeleton as a spine of aggregates. M2 says "A derived node covers nothing" but is silent on posited
  nodes.
- M7 step 2 then quietly rewards the leaf-skeleton reading: with no accreted single children there is
  nothing to collapse (run 53: 0 collapses vs 13–14 in run 44), and "Resolution is final" locks the
  coarse verdicts in.

This is the one sentence-level fix that would have changed the run 53 level, and it is a method change
(see §5).

**Share of the text**: method rules ≈ 55 % (M1–M8, the imperative, the four phases); output format
≈ 18 %; commentary/rationale/history ≈ 22 % (the paragraphs listed above, ≈ 3 k chars); frontmatter
and prohibitions ≈ 5 %.

### 1b. `agents/work-crosser.md` (Hotyn-W 1.1)

**Long output / deliberation**

- Output §4: "one table per activity: … the items it generated (item id · element id · element
  class), and the count". Run 45's orchestrator had to override this in every prompt: "**Compact §4 at
  the orchestrator's instruction: one row per activity … with item ids of the form
  `ACTIVITY@ELEMENT`**" (`run45_raw/make_prompts.py` of the SAS case, `examples/ignored/SAS`). The definition's format was found
  too long in practice and the fix lives in a prompt, not in the definition — which also means the run
  45 readings were taken under a format the definition does not describe.
- Output §8 "Projection onto the requirement anchor — one row per requirement id … the elements that
  cover it, and how many work items trace to those elements. … it is not optional." This is a join of
  the product model's §6 with §4 and is exactly what a script does better; it is declared non-optional
  for a comparability purpose that the orchestrator's script (`consolidate_run45.py`) serves anyway.
- W3/W9: "Every `no` is logged" with a one-line reason and a kind — bounded (elements × activities)
  and it is the measurement; keep. But "A per-cycle activity is logged once per element" is stated
  only in the output section, not in W9 where the rule lives.

**Redundant / stale**

- *Partial runs*: "**Per-aggregate** activities apply only to aggregates inside the named subtree" —
  the 1.0 vocabulary that Engine identity says 1.1 replaced ("the scope formerly called *per
  aggregate* is now **per parent**"). An element with own coverage and children is a parent but not an
  aggregate; the stale sentence excludes it in partial runs.
- W7: "reading its **declared content** — what the element is said to be — and never its name" — but
  the product model's §6 carries only id, name, parent, own coverage; for a derived node (empty
  coverage) the name *is* the only content. The run 45 prompt had to define content as "its name
  together with the obligations it covers", contradicting "never its name".
- Rationale paragraphs: W3 ¶1 ("That question has no bounded answer and it is the question that let
  work run free in earlier generations"), W3 last ¶ ("The negatives are the measurement of this
  step…"), W7 ¶ "The classification is where this step's freedom lives", Engine identity ¶2.

**Ambiguity**: "The class match is necessary, and you may still answer `no` — but only for a reason
specific to that element" leaves the boundary between a W9 *filter* ("the declaration's own further
condition excluded the element — no surface in the subtree, no requirement coverage") and a
*judgement* to the examples in one parenthesis; the catalogue's conditions are not restated, so whether
"no measurable target" for A9 is a filter or a judgement is the sensor's call. Measured Jaccard 0.969
says this rarely bites.

**Share**: method ≈ 60 %, output ≈ 15 %, commentary ≈ 20 %, frontmatter/prohibitions ≈ 5 %.

### 1c. `agents/work-estimator.md` (Hotyn-D 2.0)

The tightest of the three. Two things still inflate the reply:

- The same doubt is asked for twice: step 2 "if an item of your enumeration is arguable, say so in
  one clause" (in the row) and Output §5 "**Doubts** — enumerations that could honestly be read one
  item longer or shorter, each with the arguable item named". HD47-A1 §5 is 6.3 k of 23.7 k (27 %),
  mostly restating rows.
- The contamination rule "any effort figure, any person-day value … any duration, any team size" makes
  the sensor argue its way past the product figures the obligations legitimately contain: HD47-A1 §1
  spends 1.4 k clearing NFR-2 volumes, NFR-7 users and "at no cost to X-Customer". One sentence —
  *figures that describe the product (volumes, users, response times, dates) are input, not
  contamination* — removes that paragraph from every batch.

No covered-vs-new ambiguity lives here, but note the downstream consequence of the run 53 model: with
11 obligations on one node (HM53-1 N42), "Enumerate the counted things from the element's declared
content **and covered obligations**" drives classes to L/XL, so the total will not halve with the node
count — and every XL also "fires the standing rule … reported as a probable M10 coarseness finding"
(catalogue §3a). The chain will report the coarse model as a defect rather than price it silently,
which is correct, but the run record should expect it.

**Share**: method ≈ 65 %, output ≈ 20 %, commentary ≈ 15 % (Engine identity ¶¶2–3, "Your value is
that your classes cannot have been steered").

---

## 2. Output format

### (a) Shorter without losing pinned content

| change | where | saves (OA2 basis) | pinned content lost |
|---|---|---|---|
| §6 becomes the **canonical machine block**: one fenced TSV, `id  parent  origin  own-coverage  name`, no per-subtree sub-headings or prose | model-builder Output §6 | ~5 k of 19 k | none — this is what `make_prompts.py` parses today |
| §7c reduced to **residues only** + one line "146 of 146 whole; residues: NFR-5"; the script checks id presence from §6 | Output §7c | ~11 k | the per-requirement "whole" assertion moves into the last column of the §3 row, where the parts are already named |
| §9 ambiguity entries by **id + ≤ 10-word reason**, no verbatim quote | Output §9 | ~4 k | nothing (the orchestrator holds the pinned text) |
| §8 = stamp + eight counts (nodes before/after, posited/accreted/derived, passes, verdict totals, ambiguity flags, partial-at-closure, collapses); no histograms | Output §8 | ~1 k, and thinking | histograms are one `awk` over §6 |
| §3 drop the `pass` column (rows are under a per-pass heading) and the "nodes added" names (ids only; names live in §6) | Output §3 | ~5 k of 26 k | none |
| Crosser: put run 45's compaction into the definition (`ACTIVITY@ELEMENT` ids, one row per activity); drop §8 projection (script join) | work-crosser Output §4, §8 | ~30 % per batch | none; the projection is reproduced by `consolidate_run45.py` |
| Estimator: doubts live in the row only; §5 lists ids of rows carrying a doubt | work-estimator Output §5 | ~25 % per batch | none |

All of these are reporting changes: **minor** by PIPELINE's rule ("Minor changes when only wording,
reporting or output format changes"). The same file records that a format change alone once moved
Lytin-D by +33.5 % and that "a batch under a changed §6 is treated as a new baseline" — so minor bump,
but re-baseline (one n = 2 pair on SAS) before comparing to run 44.

### (b) Partial output usable, progress observable

Within one subagent turn nothing is observable in this harness: the per-agent transcript receives the
assistant text only at `end_turn`, and a `max_tokens` stop delivers the text so far plus the injected
continuation. So the honest options are:

1. **Fixed emission order = order of work, with a terminator per section.** Sections are emitted in
   the order the phases run (§1, §2, §3 pass 1, §3 pass 2…, §4, §6, §7/7b, residues, §8, §9) and each
   ends with a fixed line, e.g. `-- end §3 pass 1: 146 rows, 43 added, 0 deferred --`. A
   tail-truncated reply is then self-describing: the orchestrator knows which phase it stopped in, and
   "Resume directly" continues from a known state. Requires a rule that **§3 rows are written as the
   verdict is taken**, not after. Minor (reporting), but it changes where thinking happens — see §3.
2. **Two turns of the same instance at a phase boundary.** Turn 1: §1, §2 (skeleton), §3 pass 1.
   Turn 2, triggered by a fixed string from the orchestrator ("Continue: remaining passes, completion,
   closure, §4–§9"): everything else. M3 already forbids one phase doing another's work, so the
   boundary is where the method already stops; the instance keeps its context, so isolation is intact.
   The orchestrator's message must be a **pinned constant** (no comment on the skeleton — a comment is
   contamination in the matrix's sense) and it must be recorded like the harness continuation was in
   run 53 deviation 9. This gives one visible progress point at ~40 % and halves the per-turn output.
   **Minor**, provided the turn-2 text is pinned and identical for every run; it needs `SendMessage`,
   which run 44 found disabled — the skill must check it before launch (§4). Further segmentation of
   accretion by processing-order block (I, G, P, L, D, NFR — six turns) is the same protocol with more
   boundaries.
3. **Two separate agents (A posits the skeleton, B accretes).** The Input section already admits
   "optionally an existing structure to start from", but M4's "read the whole list at once, posit
   structure" and the `covered` verdict are then taken by different judges; the freedom that run 53
   measured moves to the boundary between them. This changes what is measured — **major**
   (Hotyn-M 2.0), and it should be run as a new instrument, not a reporting change.
4. **A sensor that writes to a file** (BACKLOG option): needs `Write`, breaks the Glob-only isolation
   PIPELINE spent a section proving; not recommended.

Which is major and which minor, in one line: anything that changes **who takes the `covered` verdict,
against what structure, with what intended-scope text** is major; anything that changes **which
sections are printed, in what order, in how many turns of the same instance** is minor with a
re-baseline.

---

## 3. Thinking budget

What pushes thought ahead of writing, in order of weight:

1. **The only-adds / never-move / resolution-is-final triad** (M5) plus **logs that must agree with
   each other** (§5 must match §3, §8 must match §6, §7c must match both). Writing a row you cannot
   retract, in a document whose sections must reconcile, makes planning the whole model first the
   rational strategy. Run 53 shows the cost: 64 000 tokens of planning, then a 46 k transcription.
2. **M4's "as a set, not as a sequence"** — inherent; keep but bound it: the skeleton is the *only*
   thing posited before writing.
3. **M2's per-parent union check and M7 1a's per-requirement completeness check**, both "do and say
   so", both requiring the whole model.
4. §8 histograms and §7c per-requirement assertions, both requiring global recomputation.

How to phrase the same discipline so the work happens in the output, with isolation and M8 intact:

- Add to M3 (one paragraph): *"The phases are written, not planned. Deliberate the skeleton once, then
  write it. From then on deliberate one requirement at a time and write its row before taking the next
  verdict; do not hold the rest of the model in reserve. A verdict you would take differently after
  seeing later requirements is not an error to prevent by planning — it is a deferral (M5), and
  deferral is what the second pass is for."* This keeps monotonicity (the deferred verdict is the
  method's own escape hatch) and moves the deliberation into the row.
- Replace "Log every verdict" with "**The log is the walk.** Each row is written at the moment the
  verdict is taken." Same rule, stated as an emission order.
- Replace M7 1a "Say so per requirement" with "report residues"; replace §8's list with counts the
  script cannot compute (passes, verdict totals, ambiguity flags) and let the script compute the rest
  — the sensor stops computing global statistics in its head.
- State the reconciliation rule the other way round: "§6 is assembled from §2–§4 by transcription,
  after they are written. If they disagree, the log is right and §6 is a transcription error" — so
  the model stops pre-reconciling.
- Keep M8 verbatim; nothing above touches numbers, and the "no reading of files" and contamination
  paragraphs are unaffected.
- Orchestrator side: the launch record carries model alias and `requestShape` but **not the
  reasoning-effort setting**, which is exactly the parameter that decides how much of the 64 k budget
  goes to thinking. It belongs in the (project × engine × model) stamp as a fourth coordinate,
  recorded not chosen by the sensor. Whether run 44 and run 53 ran at the same effort is not known
  from either record.

---

## 4. `skills/estimate-product/SKILL.md` — is the run order complete?

For an orchestrator that has never seen the repo, no. What a first-time reader cannot do from this text:

- **Batching.** "Large models are crossed and sized in batches by parent (SAS: seven batches)" — no
  rule for batch composition (must be complete subtrees, or subtree-conditioned activities U1–U3/O1
  are undecidable — HW45-A1 §2 had to reason this out), no batch size, no statement that once-scoped
  and per-environment activities are deferred in a partial run and generated once at consolidation, no
  pointer to the SAS case's `run45_raw/consolidate_run45.py` (`examples/ignored/SAS`) or `classes.tsv`/`work_model.tsv` as the
  batch-join format. The step-1 input cannot be batched (skeleton reads the list as a set) — said in
  BACKLOG, not here.
- **Repeats.** "Launch **n = 2 repeats** per step" contradicts run 45 (crosser n = 1 per batch) and
  PIPELINE step 3 (no ≥ 2 for the crosser). Say which steps repeat and why (M and D measure freedom;
  W is "very nearly a function").
- **Transit and continuation.** Nothing on head-truncated replies (PIPELINE step 2 has it), nothing on
  `max_tokens` stops. Should specify: take every reply from
  `~/.claude/projects/<project>/<session>/subagents/agent-<id>.jsonl`, never from the completion
  notification (`&` → `&amp;`, empty task files); count text blocks and `max_tokens` stops per agent;
  record the injected continuation text verbatim as a transit event in `MANIFEST.md` and in the raw
  file header (run 53 invented deviation 9 for itself); a reply cut mid-text is joined verbatim with
  the seam marked; a re-run is never a recovery.
- **Contamination.** "A sensor that reports contamination has done its job — fix the prompt, relaunch"
  omits PIPELINE's own finding: "the fix is a fresh instance, not a fresh prompt". Add: the
  contaminated reply is kept under `run<N>_raw/` with a `CONTAMINATED` header, does not count toward
  n, and the relaunch is a new agent.
- **The quarantine paragraph** is required by PIPELINE ("Every sensor prompt carries an explicit
  quarantine paragraph") but its text lives in `run45_raw/make_prompts.py` line 152; run 53 rebuilt it
  and added "a memory index". Pin it in one file the skill names.
- **Prompt preservation.** Run 44's prompt text was not kept, which is the confound run 53 cannot
  resolve. Rule: every prompt is written to `run<N>_raw/prompt_<batch>.md` with its md5 *before*
  launch, and the MANIFEST cites the md5.
- **Run numbering.** None. Run 53 took the next number after 52 and declared an aborted attempt "not
  counted". Say: one sequence across the repository, one number per launch attempt, an aborted attempt
  keeps its number and its manifest says `aborted`.
- **Processing order.** "the declared processing order" — not what it is (order A = table order) or
  that the order is part of the cell.
- **Carry-forward rule.** "the first of the pair, on no property of the model" — used in three run
  records, absent here.
- **Version gate.** PIPELINE step 0's probe is not in the skill; run 53 ran it and
  `tools/check_probe.py` was refused by the permission layer — say what to do when it is (hand
  comparison of stamp lines, recorded).
- **Recovery prerequisites.** Check `SendMessage` is available before launching a long-reply sensor;
  without it the verbatim re-emission recovery does not exist (run 44).
- **The step-3 rules paste.** "`docs/technology_catalogue.md` §3a verbatim" — §3a's first paragraph
  says "person-day values per (activity × element class × size class) live in `rate_table.md`", i.e.
  it names person-days; `make_sizing_prompts.py` pastes it "verbatim where it binds", which is the
  right thing and the skill should say so and point at the sanitised text.
- **Launch record fields.** Model alias, resolved model id, reasoning effort, `max_tokens`, harness
  preamble size, `tool_uses`, duration, stop reasons — enumerate them.
- **Where files go when the permission layer refuses `examples/<case>/`** (both run 53 attempts) — at
  least "record the refusal and the substitute path in the manifest".

What is complete and clear: Step 0's file table, the visibility table, Step 4's formula and script
pattern, the raw-file naming scheme.

---

## 5. Prioritised changes (at most eight)

| # | file | change | expected effect | bump |
|---|---|---|---|---|
| 1 | `agents/model-builder.md` M4/M5 | Pin whether a posited node may hold own coverage. Either (a) "A posited node is an aggregate; it takes no own coverage; `covered` may name only accreted or derived nodes" (the run 44 reading), or (b) the opposite, but stated. Bound the skeleton row: "intended scope ≤ 8 words; a scope that reads as a realisation is a leaf and belongs to accretion". Delete "at least one plausible attachment point" in favour of "a parent for every requirement" | Repeatability: removes the verdict that moved anchored nodes ×0.52 and spread ×1.017 → ×1.29 | **major** (Hotyn-M 2.0); re-run the SAS cell |
| 2 | `agents/model-builder.md` M3, M5 | Write-as-you-go: "the log is the walk", one requirement deliberated per row, §6 transcribed from §2–§4, disagreements resolved in favour of the log | Thinking moves into the visible output; removes the plan-then-transcribe pattern that hit 64 k | minor, re-baseline |
| 3 | `agents/model-builder.md` Output §3, §6, §7c, §8, §9 | §6 as one fenced TSV; §7c residues only; §9 ids not quotes; §8 eight counts, no histograms; drop `pass` column and node names from §3; fixed terminator line per section with counts | Reply −40 % (OA2 79 k → ~45 k) with every pinned datum kept; partial replies self-describing | minor, re-baseline |
| 4 | `agents/model-builder.md` Output §2/§6, M4 | One provenance vocabulary: `posited / accreted / derived` everywhere; delete `stated / implied` | Removes a free choice both run 53 sensors had to invent a mapping for | minor |
| 5 | `skills/estimate-product/SKILL.md` | Add: transcript-extraction rule and `max_tokens` audit; contamination = fresh instance, reply kept and not counted; prompt saved with md5 before launch; pinned quarantine text; run-numbering rule; repeat counts per step; batch rule (complete subtrees, once/per-env deferred, consolidation script); launch-record fields incl. reasoning effort; `SendMessage` check; carry-forward rule | Visibility and provenance: the next regression can separate framing from entry point, which run 53 could not | none (skill, not sensor) |
| 6 | `agents/model-builder.md` (protocol paragraph) + skill | Two-turn emission of the same instance at the skeleton→accretion boundary, turn-2 message a pinned constant, recorded in the manifest | One progress point at ~40 %, per-turn output halved, isolation unchanged | minor, re-baseline |
| 7 | `agents/work-crosser.md` Output §4, §8, *Partial runs*, W7 | Adopt run 45's compact §4 as the definition; drop §8 projection (script join); "per-aggregate" → "per parent"; define declared content as name + covered obligations (delete "never its name") | Batch reply −30 %; definition matches what run 45 actually ran under | minor |
| 8 | `agents/work-estimator.md` Input, Output §5 | "Figures describing the product are input, not contamination"; doubts in the row only, §5 = list of ids | Batch reply −25 %; §1 stops arguing with NFR-2 in every batch | minor |

Two things deliberately not on the list: splitting the model builder into two agents (major, and the
freedom it measures would move rather than shrink), and giving any sensor `Write` (breaks the verified
isolation for a visibility gain the two-turn protocol gives for free). Change 1 is the only one that
touches the level; changes 2–4 and 6–8 are reporting by PIPELINE's rule but each needs one n = 2
re-baseline before its readings are compared with run 44, because the same file records a +33.5 % move
from format alone.
