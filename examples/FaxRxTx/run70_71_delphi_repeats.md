# Runs 70 and 71 — the Delphi repeated twice: is the consensus stable, and are the work lists alike? (2026-09-17)

Registered before launch in `run70_delphi_repeats_registration.md`. Two fresh panels of ten bare agents, the pinned
prompt of run 41, the launch message, sheets and stop rule of run 69, launched together; the same helper
(`run69_raw/delphi.py`). Raw replies and ledgers: `run70_raw/`, `run71_raw/`; run 69's final tables, transcribed
after the fact with no re-estimation: `run69_raw/final_table_P-*.md`. Line mapping: `run70_raw/lines.py` →
`lines.tsv`, `lines_output.txt`. Chart: `reports/report_2026-09-17T1118.html`.

## 1. The totals — three panels

Person-months of the prompt's convention (168 h). The actual, 81.8 pm, was seen by no participant and is in no sheet.

| | panel A, run 69 | panel B, run 70 | panel C, run 71 |
|---|---:|---:|---:|
| round 1: mean / median | 125.0 / 122.5 | 129.5 / 135.0 | 135.5 / 140.0 |
| round 1: max/min | ×1.38 | ×1.43 | ×1.45 |
| round 2: median · max/min | 126.5 · ×1.08 — stop | 132.5 · ×1.16 | 145.0 · ×1.32 |
| round 3: median · max/min | — | 135.0 · ×1.08 | 147.5 · ×1.23 — not under ×1.10 |
| **consensus** | **126.5** | **135.0** | **147.5** |
| against the actual: round-1 mean → consensus | ×1.53 → ×1.55 | ×1.58 → ×1.65 | ×1.66 → ×1.80 |
| declared ranges containing the actual: first → last round | 4 → 1 | 4 → 0 | 3 → 0 |

**Stability, the author's question:** the consensus is **not stable across panels**. Three panels of identical
estimators on one text agreed on 126.5, 135 and 147.5 — ×1.17 between the outer two — while inside each panel the
participants ended ×1.08–1.23 apart. A panel looks far more certain than the next identical panel allows. And the
exchange **widened** the gap between panels: the round-1 means lay within ×1.08 of each other, the consensus figures
within ×1.17. Each panel settles near where it happened to start and then drifts upward; none moved toward the
actual, and after the talking not one of the twenty declared ranges in panels B and C still contained it (one of ten in A).

## 2. The work lists — what the author hoped for, and it is mostly there

Each participant's final table mapped onto the vocabulary registered before launch (keyword rules in `lines.py`, the
moderator's judgement written as code; 27 of 30 tables sum to their stated total within 3 pm, the other three carry
"implied" residuals). "n/10" = how many of the ten carry the line; the figure is the panel median in pm.

**Lines the source document names — every panel, every participant, nearly the same value:**

| line | A | B | C | between panels |
|---|---:|---:|---:|---:|
| immersion and technology selection | 10/10 · 10 | 10/10 · 10 | 10/10 · 10 | ×1.00 |
| OCR workers | 10/10 · 5 | 10/10 · 5 | 10/10 · 5 | ×1.00 |
| CDR capture | 10/10 · 3 | 10/10 · 3 | 10/10 · 3.2 | ×1.08 |
| real-stream / load testing | 8/10 · 11 | 9/10 · 12 | 9/10 · 12 | ×1.09 |
| user portal | 10/10 · 10 | 10/10 · 11 | 10/10 · 11 | ×1.10 |
| render workers | 10/10 · 11.5 | 10/10 · 13 | 10/10 · 13 | ×1.13 |
| delivery-control core | 10/10 · 21 | 10/10 · 24 | 10/10 · 22 | ×1.14 |
| data layer / API | 10/10 · 6 | 10/10 · 6.5 | 10/10 · 7 | ×1.17 |
| NOC | 10/10 · 8 | 10/10 · 9 | 10/10 · 9.5 | ×1.19 |
| Tx inbound-mail parser | 10/10 · 5 | 10/10 · 5.5 | 10/10 · 6 | ×1.20 |
| cluster management tool | 9/10 · 4 | 10/10 · 5 | 10/10 · 5 | ×1.25 |

**A line the source does not name as a deliverable, found by all three panels on their own:** the inbound delivery
path (Rx: PoP intake, the per-user TIFF-or-PDF branch, outbound mail at volume) — 8/10, 10/10, 10/10. In every
panel it was missing from most round-1 tables, present in a few, and adopted after the participants checked it
against §2 of the source. Its **value** did not converge between panels: 5, 4 and 7.5 pm (×1.88).

**Where the panels differ — each grew its own extra lines:**

| line | A | B | C |
|---|---|---|---|
| burst / scale hardening as its own line | 0/10 | 1/10 | **10/10 · 6.5** |
| "domain-novelty rework tax" | 0/10 | **6/10 · 5** | 0/10 |
| glue / omissions factor | **4/10 · 6** | 0/10 | 1/10 (set to 0) |
| discounts, round-downs (v1 as oracle, double-count cuts) | **7/10 · −5** | 3/10 · −6 | 0/10 |
| QA as a separate line | 8/10 · **19.7** | 6/10 · 8 | 7/10 · 8 |
| PM derived from duration rather than a percentage | — | adopted by most | — |

Boundary-free sums say the same: delivery stack (core + management tool + burst) 25 → 30 → 34 pm (×1.35);
verification (testing + separate QA) 26 / 14.5 / 18.5 (×1.78); overhead (PM, glue, tax, discounts) 9 / 13.5 / 13.

So the answer to "will the lists be alike": **the list of deliverables is alike to the point of being one list, and
the panel medians of its lines agree within ×1.25.** What is not alike is (a) the handful of cross-cutting lines each
panel invented for itself — an argument that one participant happens to make in round 1 becomes that panel's
convention by round 3 (the calendar-yield correction and the novelty tax in B, the burst-hardening line in C, the
double-count cuts in A) — and (b) the bookkeeping of QA. Several participants said so in as many words: the spread
"is a convention difference about whether QA and PM sit inside the block figures or on top of them, not a difference
about what has to be built"; "two methods … moving to the crowd's midpoint would be averaging two methods rather than
estimating one." The level a panel ends at is decided by which of these memes it happened to breed.

## 3. Registered expectations, scored

| # | registered | happened | |
|---|---|---|---|
| 1 | each panel ≤ ×1.15 after one exchange; consensus within −3 … +8% of its own round-1 median | A ×1.08, B ×1.16, C ×1.32 after one exchange (C ×1.23 after three); consensus vs round-1 median +3.3%, 0%, +5.4% | convergence **half met** — slower than run 69 suggested; shift **met** |
| 2 | consensus figures agree no better than the round-1 means; all six figures inside 115–140 | means ×1.08 apart, consensus ×1.17 apart — **worse**, not merely no better; 147.5 outside the expected band | **met**, and stronger than registered |
| 3 | source-named lines carried by all; of the four lines the source does not name, each panel ends with ≥ 3 carried by 8/10, the same ones | source-named: all. Rx path and data layer: all three panels. Integration drag: none at 8/10. Separate QA: 8/10 in A only | **partly met** — two of four, the same two |
| 4 | big lines' panel medians within ×1.25 between panels; pre-exchange spread on the core ≥ ×1.5 in every panel | core ×1.14, portal ×1.10, NOC ×1.19, render ×1.13, testing ×1.09; pre-exchange core spread ×1.75, ×1.40, ×1.50 | **met** on values; pre-exchange spread met in two of three |

Overturning conditions: neither. The consensus is not an attractor (the panels moved apart), and the panels did not
converge on different lists (the deliverables are one list; only the cross-cutting lines differ).

## 4. What it means

- **A Delphi among copies of one model manufactures confidence, not stability.** Inside a panel CV falls to
  2.5–5.6%; between panels the consensus moves ×1.17. Reported alone, any one panel would overstate what is known by
  a factor of several. This is the no-method family's batch shift (runs 41/43) again, now shown to survive — and
  grow under — deliberation.
- **Every panel drifted up, none down.** The exchange finds omissions (checkable against the source, so adopted) and
  double counts (adopted where a participant can see them in its own table); omissions outnumber them, and new
  cross-cutting lines are cheap to add. 125 → 126.5, 129.5 → 135, 135.5 → 147.5; the actual is 81.8.
- **The useful product is the list, not the number.** Thirty tables, three panels, one list of deliverables with
  line medians inside ×1.25 — and one genuinely missing block (the Rx path) found independently three times. As a
  *review of a decomposition* the exchange is reliable; as a way to fix a level it is not. For the instrument this
  supports the existing design rather than changing it: structure may come from a model (and may be cross-checked
  by several), magnitude must come from somewhere a panel cannot talk itself into — the rate table and the
  calibration round.
- **The participants saw the limit and said it**, in all three panels: "ten agents reading one document are not ten
  independent samples"; "in a third Delphi round, movement toward the centre is the outcome the format manufactures";
  "nobody learned anything new about Venali". They converged anyway.

## 5. Protocol notes

- **Round-3 sheet of panel B exceeded one read.** The harness returned lines 1–602 of 711, so no participant of
  panel B saw P-10's round-2 reply (the panel's highest, 145, and the one that named the "two schools" of QA
  bookkeeping) or the lower half of P-9's table. Nine of ten declared the gap and did not read again; one (P-1)
  read a second time, got the same page, and reported the breach itself. Panel C's sheet (66 566 characters against
  70 796) came through whole. Panel B's round 3 therefore converged without its top voice; its ×1.08 is partly an
  artefact. For any further round: split the sheet or allow two reads.
- **Commit subjects reach participants.** Four figure-free commits were made before launch so that run 69's result
  subject was no longer among the five injected; participants listed what they saw (run numbers, the words "Delphi
  consensus", "no-method control") and confirmed no figure. The design of the experiment was therefore visible to
  them; one noted it and declined to treat it as a hint about the expected answer.
- One permitted read per round held in 78 of 80 participant-rounds by the transcripts: panel B P-1 in round 3 (above)
  and panel C P-9 in round 3 read twice. Every reply ended `end_turn`, model `claude-opus-5` throughout (two
  streaming fragments of panel C P-7 carry no stop reason in the transcript; its replies are complete).
- Sheet headers name the round the replies came **from** ("Round 2 — the ten replies") while the instruction names
  the round being run ("round 3"); several participants flagged the off-by-one. Harmless here; fix the header text
  before the files are pooled with anything else.
- Deviation from run 69, as registered: rounds 2 and 3 asked for the full final table. Run 69's tables were
  transcribed afterwards; rows its participants had never stated as numbers are marked "implied" by them.
- A control beside the no-method family. No figure of the run 61–67 estimate moves.
