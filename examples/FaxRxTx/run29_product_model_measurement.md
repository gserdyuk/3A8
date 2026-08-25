# Run 29 — the FaxRxTx product model, `Hotyn-M 1.1`, n = 2

**2026-08-22.** Stage 3 step (c), first sensor. One cell: **Opus 5 × order A × n = 2** — deliberately
the same cell as BMS run 19, so the two cases are comparable and the only difference is the project.

Raw: `run29_raw/HM29-OA1.md`, `run29_raw/HM29-OA2.md`.
Inputs: `requirements_product.md` (md5 `306046dc6cab35147040224e7a4e9662`, N = 47) +
`assumptions_product.md` v1, both pasted whole into each prompt. No file was read by either sensor;
`tool_uses: 0` in both. Both printed the stamp `Hotyn-M 1.1`, and the pre-batch probe returned
`Lytin-F 5.0` — the definitions in force are the edited ones.

---

## 1. What is being scored

No new predictions were registered before this pair. Scoring uses **run 19's registered predictions**,
which predate this run by three days and were written for the instrument rather than for BMS. That is
the honest available test: an expectation formed on one case, applied unchanged to a second.

---

## 2. The readings

| reading | OA1 | OA2 | ratio |
|---|---:|---:|---|
| skeleton (posited) | 19 | 13 | ×1.46 |
| accretion (accreted) | 65 | 69 | ×1.06 |
| **anchored (posited + accreted)** | **84** | **82** | **×1.024** |
| completion (derived) | 14 | 10 | ×1.40 |
| nodes before normalisation | 98 | 92 | ×1.065 |
| nodes after normalisation | 97 | 87 | ×1.115 |
| nodes collapsed at closure | 1 | 5 | ×5.0 |
| coverage assignments (requirement, node) | 82 | 96 | ×1.171 |
| nodes per requirement, mean | 1.74 | 2.04 | ×1.17 |
| co-located requirement pairs | 21 | 24 | **×1.14** |
| skeleton nodes ending with empty **total** coverage | 0 of 19 | 1 of 13 | — |
| partial marks standing at closure | 0 | 0 | — |
| completion-covers-a-requirement defects | 0 | 0 | — |
| unplaceable requirements | 0 | 0 | — |

**Jaccard of the co-location relations: 13 shared pairs, 32 in the union → 0.406.**

---

## 3. Scoring run 19's predictions on a second case

| # | prediction | BMS run 19 | FaxRxTx run 29 |
|---|---|---|---|
| 1 | executability: all nine sections, a parent for every node | held | **held in content, broken in transit** — see §6 |
| 2 | anchored total agrees within ±5% | **REFUTED**, ×1.56 | **CONFIRMED**, ×1.024 |
| 3 | derived spread exceeds anchored spread | **REFUTED and inverted** (derived ×1.10 < anchored ×1.56) | **CONFIRMED**, derived ×1.40 > anchored ×1.024 |
| 4 | relations within ×2 in size **and** Jaccard above 0.5 | **SPLIT**: ×1.07, J = 0.308 | **SPLIT**: ×1.14, J = 0.406 |
| 6 | fewer than 20% of skeleton nodes end with empty total coverage | not scoreable | **CONFIRMED**: 0% and 7.7% |

Three of the four scoreable predictions, refuted on BMS, are confirmed here. Prediction 4 splits the
same way on both cases and its Jaccard is the one reading that improved without crossing its
threshold.

---

## 4. The reading that matters, and what would overturn it

**R5 — the ×1.56 anchored spread of run 19 was a property of the BMS input, not of `Hotyn-M 1.1`.**

Run 19's conclusion was that version 1.1 "removed the freedom of declaration depth and exposed a
partition freedom underneath it": M2 forces coverage down to the node that realises the obligation, so
a run must decide how many *parts* an obligation has, and nothing bounds that judgement. OA1 read BMS
requirements as mostly single-part (1.41 nodes per requirement), OA2 as compound (2.00), and that
single ratio carried nearly the whole ×1.56.

On FaxRxTx the same freedom exists — 1.74 against 2.04 nodes per requirement, a ratio of ×1.17 — but
it moves the anchored node count by ×1.024, not by ×1.56. The freedom did not disappear; **it stopped
propagating.**

Two candidate mechanisms, and they are separable by experiment:

- **The input describes structure.** An RFP states obligations and leaves the architecture open; a
  participant's recollection of a system states the architecture and leaves the obligations sparse.
  Where the source names the parts — workers, cluster, token store, NOC, portal, renderers — two runs
  cannot partition them very differently, because the partition is in the document.
- **The projection pinned more readings.** `assumptions_product.md` P5 fixes ten readings against
  BMS's six, and P4 supplies content for both contentless entries. Every pinned reading is one
  partition judgement removed from the run.

*Overturned by:* a third FaxRxTx pair run **without** P4/P5 that reproduces run 19's spread — which
would put the cause in the projection, not in the document; or a BMS pair rerun with a P5 as dense as
this one that comes down near ×1.0 — same conclusion, from the other side. Neither experiment is run
here, and until one is, the two mechanisms are not distinguished. **What is settled is the negative:
×1.56 is not the instrument's number.**

---

## 5. What the two models actually disagree about

The disagreements are visible and few. Both models contain the same system; they place four things
differently.

| the thing | OA1 | OA2 |
|---|---|---|
| **F47** ("replaces the core functionality of the first version") | an enumerated **parity-boundary node** under system-wide properties (HM1-84) | **own residue declared on two aggregates** (HM2-02, HM2-03) — the only aggregate-held coverage in either model |
| **identity and access** | two nodes, placed where they are used (HM1-95 operator access, HM1-96 portal recovery) | a **posited subsystem** (HM2-13) with three derived children — and the only empty skeleton node in either run |
| **F19 (the ~8–10 formats)** | 2 nodes: a stabilisation harness and an open registration point | **9 nodes**: the harness, the registry, **and F19 carried on each of the seven format renderers** |
| **the C#/.NET baseline (F30)** | a standing node under system-wide properties (HM1-64) | collapsed at closure into a **derived logging node** (HM2-89), which the run flagged itself as a cost of normalisation |

The F19 difference is the whole of the coverage-assignment gap: OA2's seven extra assignments on the
renderers are 7 of the 14 assignments by which the two models differ. It is a genuine reading
difference about what "each format is a separate piece of integration work" attaches to — the set, or
each member — and it is exactly the kind of thing the enumeration precedents (catalogue §3a) exist to
adjudicate. **It is not adjudicated here**, because it is a coverage question and the precedents so
far are sizing questions.

---

## 6. Protocol facts from this run

1. **A subagent reply can arrive truncated.** OA2's first reply reached the orchestrator beginning
   part-way through §7c; sections 1–7b were lost in transit. Resuming the agent and asking it to
   **re-emit verbatim, explicitly forbidding re-derivation**, recovered §6, §7 and §7b. Sections 2–5
   of OA2 are permanently absent from the record. **Standing practice from now on: check a sensor's
   reply begins at section 1 before transcribing it**, and recover by re-emission, never by re-running
   — a re-run is a different sample and quietly turns n = 2 into n = 3 with one member discarded.
2. **The `gitStatus` injection is still happening, and the sensors still catch it.** OA1's
   contamination check names it explicitly: *"my context was injected with ambient repository
   information (a git status listing prior runs, raw-run directories and prior model documents)"*, and
   quarantines it. Both runs proceeded on the pasted input alone. This is the third independent catch
   (runs 27, 28, 29) and the fix — launching sensors from a cwd outside the repository, or a harness
   setting — remains open as debt 3 of the session record.
3. **The explicit quarantine instruction works.** Both prompts carried a paragraph telling the sensor
   that ambient repository information is not its input and must be reported and ignored rather than
   treated as contamination that stops the run. Neither run stopped; both reported. Before this
   instruction existed, run 28's sensor refused to certify validity until the orchestrator supplied a
   missing stamp — the same reflex, costing a round trip.

---

## 7. The model carried forward

**`HM29-OA1` — 97 nodes after normalisation — is crossed with the declared technology in the next
step.** Chosen as the first of the pair, the same rule BMS used when it crossed `HM19-OA1`, and not on
any property of the model.

`HM29-OA2` stands as the **declared structural sensitivity** of everything downstream: 87 nodes
against 97, and the differences enumerated in §5. What that costs in person-days is not knowable until
the work models are priced, and it is not guessed here. BMS carried the same sensitivity unquantified
(session record, debt 4, the OA2 structure axis); this case will carry it the same way unless the
crossing turns out cheap enough to run twice.
