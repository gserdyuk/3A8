# FaxRxTx — the estimate, v1 of the 2.1 chain — 2026-09-16

**Case FaxRxTx (Venali, 2007–2009): the rework of a worldwide fax send-and-receive back-end — inbound and outbound
fax paths, a hand-built watchdog-and-token orchestration layer, a Windows render cluster, NOC, user portal,
coexistence with and cutover from the first version.** A fresh end-to-end estimate through `/3a8:estimate` on the
current chain (`Hotyn-M 2.1` / `Hotyn-W 1.2` / `Hotyn-D 2.0` × rate table v0.1-h, runs 61–64), the outside view
(`Lytin-R 1.1` ×2, run 65), gap-blind Step C rates (`Lytin-K 1.1`, run 66) and the diagnosis (`Lytin-G 1.1`,
run 67). No number from the earlier FaxRxTx runs (1–43) or their reports was read or used. **This document was
written and fixed before `FACT.md` was opened**; the comparison with the outcome is a separate run record
(`run68_fact_comparison.md`) and does not enter anything below. Written to be read without the conversation behind it.

**Read this box before any number.**
- Every bottom-up figure rests on **rate table v0.1-h — external industry norms in net task hours, uncalibrated
  against any outcome**. The centre is "norms passed through a measured size vector, then corrected by gap-blind
  external rates", not a validated cost.
- The bottom-up stands on **one** product model (`HM61-1`). The pair (run 61) showed leaves ×1.10 (68 vs 75) and
  coverage-set Jaccard 0.51; the other model was not priced, so that spread is **in no number here**.
- **Outcome: one exists** (`FACT.md`, a participant's recollection). It was sealed through every step and opened only
  after this document was fixed. Case 1 of the exit criterion was already admitted on conventions supplied after an
  earlier estimate; this re-estimate pinned its case profile first but is not an independent validation case.
- **Era:** the table is modern; the project ran on C#/.NET 3.x on own hardware. The only era term is Step C's G2
  (×1.00–1.27), the lowest-confidence factor in the chain.

---

## 1. The answer, three parts, not summable

Unit: **net hours of work on the task** — leave, holidays, sickness and presence overhead excluded. In the
comparison-layer convention (`docs/constants.md` §4a) one staffed person-month ≈ 114.5 net task hours.

| part | value (net task hours, A1 scope) | ≈ staffed person-months | what it is |
|---|---|---|---|
| **Centre** | **17 100 – 17 597** (17 350) | **≈ 149 – 154** (152) | the calibrated bottom-up: table-priced chain 9 846–10 194 × the gap-blind Step C chain (×1.73): priced holes and closure findings, performance testing, account migration (A1–A4, +1 000 h); distributed-delivery complexity on the orchestration and cluster subtrees (T1 ×1.17); unnamed requirement growth (T2 ×1.12); immersion phase, parallel run, PM residual as shares (T3–T5, +20%); era tooling and learning curve (G2 ×1.15) |
| **Corridor** | **11 795 – 26 330** | ≈ 103 – 230 | the spread of the calibration rates — **all lows together and all highs together, not percentiles**. It contains the rates' own uncertainty and the two sizing repeats, and nothing else: not the product-model spread, not the unit-factor dispute, not the tail |
| **Reserve** | **unresolved** | | the raw class tail, uncalibrated: RC65-1 P80 30 240 / P90 39 060; RC65-2 P80 20 038 / P90 27 480. The centre sits below RC65-1's P50 (18 900) and between RC65-2's P50 (12 023) and P80; the two readings' P90s differ ×1.42 |

**The outside view, for the same scope** (`Lytin-R 1.1`, 2 launches, each declaring its own unit; converted by the
pinned convention of `docs/instrument.md` §0 as the diagnosis applied it — RC65-1's recorded 168-h month holds 21
present days × 6 net h = 126 h, leave already outside; RC65-2's staffed month = 114.5 h):

| net task hours | P10 | P50 | P80 | P90 |
|---|---:|---:|---:|---:|
| RC65-1 (recorded pm, 168 attended h, leave out; 80 / 150 / 240 / 310) | 10 080 | 18 900 | 30 240 | 39 060 |
| RC65-2 (staffed pm, leave in; 55 / 105 / 175 / 240) | 6 298 | 12 023 | 20 038 | 27 480 |

Both chose one class — an in-house second-generation rewrite of a distributed high-throughput back-end with a
parallel-run cutover — at 55% confidence, and both are right-skewed (P90/P50 ×2.07 and ×2.29). They differ in level
(×1.57 at P50 in net hours) through their anchor weighting (COCOMO II vs team × duration), not through units; the
conversion factor itself is disputed (100–146 and 101–133 net h per unit across the sensors' own declarations).

**The raw chain, for the record:** 10 020 net task hours (repeat band 9 846–10 194, ×1.035), with its own O/M/P
band at ρ = 0.5 of about 7 764–12 337 — a declared convention, not a measurement.

## 2. What the diagnosis established (run 67, Steps B–D)

- **Units first.** Unit-blind, the outside view looks ×2.5 and ×1.8 above the chain; the units component is 6 300 h
  (31%) and 5 618 h (68%) of those gaps. After conversion: RC65-1 ×1.89, RC65-2 ×1.20 above the raw chain.
- **Step C's G1 (within-day overhead ×1.25) is the same quantity as the pinned 6-net-hours-a-day convention**;
  applying both counts overhead twice. The chain is taken to G2 in net task hours; the conversion to months replaces
  G1. The diagnosis asked the rate role to restate G1 as a unit step.
- **Corrections add +7 328 h at central** (×1.73): G2 +2 263 (31%), T3–T5 +2 497 (34%), T2 +1 294, fills +1 012,
  T1 +262. The largest contributions carry the lowest confidence; the itemised, table-priced fills are 14%.
- **Explained share:** against RC65-1, 83% with a residual of +1 552 h whose sign flips across the unit-factor band;
  against RC65-2, an overshoot — the calibrated centre is ×1.44 above its P50. The residual is not closed.
- **False convergence checked:** the calibrated centre's closeness to RC65-1 (×0.92) is partly one source seen twice
  (COCOMO II behind both RK66's phase and complexity factors and RC65-1's anchor A-3). The raw chain's closeness to
  RC65-2 was coincidence.
- **The coverage report moved the rates down:** no generic testing, integration or rework uplift; PM and transition
  as residuals; omissions itemised instead of a blanket percentage (T2 central ×1.12 instead of ~×1.25).

## 3. What is inside the centre

47 product obligations → 84 elements (68 leaves, 16 parents; `HM61-1`) → 521 element-attached work items + the
root's per-parent items + 16 once/per-environment items → 64 / 63 sized leaves (95.6% class agreement; S/M/L/XL
33/26/4/1 and 34/25/4/0) → 10 094 / 9 747 h, plus two demanded-work rows (100 h). The structure carries design,
implementation, test design, unit tests, code review, requirement elaboration and contract tests per element; test
execution and defect resolution in two cycles, regression, test data and planning per subsystem; integration at 20%
of the leaf effort at every parent (3 144 h, of which 1 315 h at the root); test strategy, mobilisation, reporting,
risk, three environments, build pipeline, promotion, configuration management, **production cutover**, hosting
set-up, runbook, handover pack, release notes, user documentation; seed-data work on three stores; one pass of
integration tests on live traffic and the decommissioning check. The calibration added, by name: the renderers for
the 1–3 unnamed formats, the database schema and the old-system interface (holes), ten closure findings (inbound
hand-off, unknown numbers, rejection notices, routing fallback, status recording, clean-up, PoP-registry
maintenance, account provisioning, v1 function inventory, ending coexistence), the initial account load, performance
and burst testing with a load generator; a complexity premium on orchestration and cluster; requirement growth; the
immersion phase (8%), the parallel run and stabilisation (7%) and a PM residual (5%) as shares; era tooling and a
domain learning curve (×1.15).

## 4. What is NOT in any number, by name

1. **Carried unpriced, awaiting a parameter:** W-F48 (immersion) and W-F50 (parallel-run comparison) as rows — the
   rate author refused both for undeclared headcount and period; they enter only as Step C shares T3 and T4.
   A5 (production cluster build-out beyond size L) — the table has no row.
2. **The refused and narrowed readings:** `HM61-2` (75 leaves, ×1.10) was not priced; L56 "first-version core function
   set" is unsizeable in both repeats and priced at nothing (its content is an inventory nobody has); L15's XL/S split
   is inside the repeat band.
3. **The rate table's level** — external norms, uncalibrated; and the open question whether its day-based sources
   meant net or assigned days (the addendum's author declared ×1.23–1.45 for its own rows; the table has not said).
4. **Uncovered by any rate:** archive and configuration migration, keeping v1 alive during coexistence, hyper-care
   after cutover (both outside readings count them partly inside); security and compliance assurance; the team's
   grade; the reverse audit that would check the chain's one-way (additive) design.
5. **The era** beyond G2's merged tooling and learning-curve factor.
6. **Tail and failure events** — a repeat of the MSMQ-style collapse, driver or OCR instability, Lustre problems, a
   failed parallel run forcing redesign: in the class quantiles only, in no bottom-up item.
7. **Effort → calendar and team availability**: not estimated. The conversion to staffed months uses the pinned
   defaults (6 net h per present day, ×1.10 leave) because the case profile has no values of its own.

## 5. The decisions and questions that move this answer

**1. How many net task hours this organisation's month yields.** The diagnosis's first lever: across the sensors'
own declarations the factor runs 100–146 h, which alone flips the sign of the residual against RC65-1 and decides
the staffed-month figure (at 100 h/pm the centre would read ≈ 174 pm instead of 152).

**2. Whether rate table v0.1-h's day was a net or an assigned day** — a units correction to the instrument that could
be larger than any single Step C factor (up to ×1.23–1.45 downward).

**3. Scope rulings on migration, v1 upkeep and hyper-care; and the headcount and length of the immersion and
parallel-run stages** — they turn Step C shares T3/T4 into priced rows and settle whether items in §4.4 are gaps of
the chain or scope differences of the outside view.

**For the client (from the open-questions register):** the case has no `open_questions.md`; the questions above and
the sensors' doubts stand in for it — the unnamed input formats (F19), the functions of the first version that must
be replaced (F47), the content of the old-system integration (F42), and the performance targets as testable limits
(F36, F37).

**Known model and catalogue findings:** a pinned product projection that quotes a figure it claims to remove (both
model sensors refused on it); the crossing cannot see obligation texts, so it refused performance testing on a
statement whose obligation states a target; the demanded-work rows W-F48 and W-F50 need an output-bounded restatement
or a catalogue split; the chain tools' parsers miss two common reply phrasings (group definitions in the crossing,
special counts in the sizing).

## 6. Provenance

| step | run | engine × model | n | readings |
|---|---|---|---|---|
| product model | 61 | `Hotyn-M 2.1` × Claude Opus 5 | 2 (+2 contamination refusals) | HM61-1 (closed), HM61-2 |
| work model | 62 | `Hotyn-W 1.2` × Claude Opus 5 | 1 per batch, 4 batches | HW62-A1…D1 |
| size classes + assembly | 63 | `Hotyn-D 2.0` × Claude Opus 5; `tools/chain/assemble.py` | 2 per batch | HD63-A1…D2 |
| demanded-work rows | 64 | `Hotyn-K 1.1` × Claude Opus 5 | 1 | HK64-1 |
| outside view | 65 | `Lytin-R 1.1` × Claude Opus 5 | 2 | RC65-1, RC65-2 |
| Step C rates | 66 | `Lytin-K 1.1` × Claude Opus 5 | 1 | RK66-1 |
| Steps B, D | 67 | `Lytin-G 1.1` × Claude Opus 5 | 1 | RG67-1 |

Version probe before the first launch: manifest equal to disk, `tools/check_probe.py` 11 agents / 0 failing. All
sensors ran as `Glob`-only subagents of one orchestrating session (Claude Code 2.1.270, model alias `opus` →
`claude-opus-5` in every turn); every prompt was saved with its md5 before launch (except the one-word probe prompt),
and **every sensor received its prompt byte-identical** (md5 of the transcript's first message = saved file). Every
turn ended `end_turn`, largest turn 23 537 output tokens, no continuation message; `CLAUDE_CODE_MAX_OUTPUT_TOKENS` was
raised by the launcher, its value not readable from inside the session. Raw replies were transcribed from the
harness transcripts by `run61_raw/extract_reply.py`; one `MANIFEST.md` per run lists prompts, md5s, stop reasons and
tokens. Three read-time wrappers around unchanged tools (`consolidate_62.py`, `assemble_63.py`, and the pricing script
`price_fills66.py`) are described in the manifests. Protocol facts: writing into `examples/FaxRxTx/` was refused by the
harness, so the whole run lives in the session scratchpad at the same relative paths; the case profile was not
committed; every sensor reported and quarantined the harness's git status, commit subjects and memory index.
