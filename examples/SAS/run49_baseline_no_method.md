# SAS — Run 49: the no-method baseline, n = 10 — the same text with no method at all, and no fact

Date: 2026-09-08, after the deliverable was closed. The run 41/43 experiment (FaxRxTx) repeated on
case 3 at the author's request, to put a fast, unstructured answer on the same axis as the chain and
the two class readings. Ten runs of the pinned prompt `run49_raw/prompt_baseline_sas.txt` (md5 of the
LF form `9d71b4c7039e5adcd5477c75c7439732`, 40 286 bytes) sent to a general agent with **no method
definition**, on Claude Opus 5 — the same model coordinate as runs 44–48.

The prompt is a bare instruction plus the RFP §1–2 verbatim and the assumption log v1 in the
sanitised form the class sensors saw. Not `requirements_pinned.md`: extracting that list of 153
obligations **is the method's first act**, and handing it to the baseline would credit the baseline
with work the chain performs. The unit imposed is run 41's — 1 pm = 21 person-days = 168 hours of
work on the task, leave outside — so the three baselines on record compare without conversion.

**Deviation from run 41, declared before launch** (`run49_raw/MANIFEST.md`): the prompt is 40 KB,
too long to paste ten times, so each run was told to read exactly this one file and use no other
tool. **Every run reported `tool_uses: 1`** — the one permitted Read — and every run quarantined the
ambient repository status, commit subjects and memory index unprompted; two also noted that the log
cites files they did not open. Raw replies: `run49_raw/B-1.md` … `B-10.md` (six from the harness
transcript, four transcribed from the delivered reply, headers say which); arithmetic:
`run49_raw/readout.py`; the fitted curves: `run49_raw/curves_pd.json`.

## Raw data

| Run | TOTAL, pm (168 h) | own P10 … P90 | team × months | net task hours |
|---|---:|---|---|---:|
| B-1 | 170 | 120 … 270 | 14 × 14 | 28 560 |
| B-2 | 250 | 165 … 390 | 18 × 16 | 42 000 |
| B-3 | 150 | 105 … 230 | 12 × 14 | 25 200 |
| B-4 | 185 | 125 … 290 | 13 × 16 | 31 080 |
| B-5 | 240 | 165 … 380 | 18 × 16 | 40 320 |
| B-6 | 130 | 95 … 195 | 12 × 12 | 21 840 |
| B-7 | 147 | 110 … 240 | 13 × 13 | 24 696 |
| B-8 | 145 | 105 … 215 | 11 × 14 | 24 360 |
| B-9 | 140 | 95 … 225 | 11 × 15 | 23 520 |
| B-10 | 135 | 95 … 210 | 11 × 14 | 22 680 |

Every run built a bottom-up table of its own (blocks of person-days or person-months), most added a
function-point or reference-class cross-check, and all ten carried W-4 and NFR-5 as "carried, not
priced" in the log's own words. The two high runs (B-2, B-5) both reconciled *upward* from their own
bottom-up toward a reference class of 15–20 people over 16–20 months; the eight low ones reconciled
downward or not at all.

## 1. The batch

| | n | mean | median | sd | CV | min … max | max/min |
|---|---:|---:|---:|---:|---:|---|---:|
| BMS run 14 | 10 | — | — | — | 8.55% | — | ×1.26 |
| FaxRxTx run 41 | 10 | 120.5 | 120.0 | 16.6 | 13.75% | 90 … 155 | ×1.72 |
| FaxRxTx run 43 | 10 | 138.0 | 137.5 | 18.6 | 13.47% | 110 … 165 | ×1.50 |
| **SAS run 49** | 10 | **169.2** | **148.5** | 43.2 | **25.53%** | 130 … 250 | **×1.92** |

The spread is **twice** either FaxRxTx batch and three times BMS's, on a document that is longer and
more structured than either. Mean pairwise ratio between runs 1.327 (median 1.259) — against the
chain's whole-chain repeat spread of ×1.0026 on this case and ×1.05 across two product models on
FaxRxTx. On repeatability, the one axis that needs no fact, the gap between the two instruments is
wider here than on any earlier case.

**Each run's declared P10–P90 corridor is ×2.23 wide on average (×2.05 … ×2.37), wider than the
×1.92 spread of the ten medians.** That is the opposite of run 43's finding on FaxRxTx, where every
run declared a corridor (×1.51) narrower than the distance to its neighbours (×1.85). On SAS the bare
instrument is *not* over-confident about its own precision — it is wide and it says so; the ten
corridors overlap heavily. What the batch does not know is its level.

## 2. On the chain's axis — the sign is the inverse of FaxRxTx

Net task hours, no conversion on either side (both instruments emit them):

| | net task hours | ratio |
|---|---:|---|
| baseline, mean of 10 | **28 426** | — |
| raw chain (run 47) | 38 118 | baseline = **×0.75** |
| calibrated centre (run 48) | 57 600 | baseline = **×0.49** |
| RC46-1 median, house 0.75 | 47 880 | baseline = ×0.59 |
| RC46-2 median, house 0.75 | 24 510 | baseline = ×1.16 |

On FaxRxTx the no-method baseline sat **×1.78 above** the chain (run 41) and above the fact; here it
sits **×0.75 below** the raw chain and inside the lower class reading. Six of ten runs' own corridors
cover the raw chain; two of ten cover the calibrated centre. There is no fact to say which side is
right, so this is a distance and a sign, not a score. Two readings of it, both kept:

- **The chain scales with the document; the bare instrument does not.** SAS carries 153 obligations
  to FaxRxTx's 52 (×2.9) and the chain priced it at ×3.35; the bare instrument's mean moved ×1.40
  (169 against 120.5). An instrument that reads a requirement list and answers "about 150 person-
  months" for both a fax platform and a three-module member application is anchored on something
  other than the text.
- **Or the chain over-prices dense enumeration.** The C3 constant delivers 54% of leaf effort on
  this deep tree (34% of the total), and every Step C correction pointed up. The lower class reading
  (RC46-2) and the ten bare runs agree with each other within ×1.16 and disagree with the chain.
  The diagnosis (run 48) already named the two facts that would settle this — a declared functional
  size, and the level of table v0.1-h — and this batch does not add a third.

## 3. On the report

The ten curves are drawn as a **family, never pooled**, in ochre and thin, on both panels and in the
cursor readout ("median % over · k of 10 put it above"). The builder gained a `nomethod` family and
an ochre pen; nothing about the standing instruments' scale changed. Per run 43's finding, a pooled
curve would assert a stability the instrument does not have.

## 4. What this does not settle

- **One batch is one draw of the level.** Run 43 moved ×1.145 in a day on FaxRxTx. A second batch
  (run 50) is scheduled for 2026-09-09 with the same pinned prompt; until it runs, 169 pm is a sample,
  not the instrument's level.
- **The `tool_uses: 1` deviation.** Every run read the one file and nothing else, and said so; the
  transcripts confirm one tool call each. But the run 41 control (`tool_uses: 0`) was cleaner, and a
  harness that could carry a 40 KB prompt inline would restore it.
- **No fact.** The sign of the gap between the bare instrument and the chain flipped between two
  cases, and only an outcome could say which instrument moved.
