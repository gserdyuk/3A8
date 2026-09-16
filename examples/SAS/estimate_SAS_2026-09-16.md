# SAS — the estimate, v2 — 2026-09-16 — the first produced through the plugin

**The same case, the same requirements, the same outside view, the same rate table — estimated
again through the packaged instrument** (`3a8`, a Claude Code plugin: skills `/3a8:estimate-product`
and `/3a8:estimate`, twelve sensors in `agents/`) with the current product-model engine. This is the
answer the instrument gives today; the answer of 2026-09-08 (`estimate_SAS_2026-09-08.md`, the 1.1
chain, launched by hand from `.claude/agents/`) remains on record beside it. Written to be read
without the conversation behind it.

**Read this box before any number.**
- Every bottom-up figure rests on **rate table v0.1-h — external industry norms in net task hours,
  uncalibrated against any outcome**. The centre is "norms passed through a measured size vector",
  not a validated cost. Both diagnoses on this case say to read it as "the table's level ×1.5" until
  the table's level is checked gap-blind. That check has not run.
- The bottom-up stands on **one** product model (HM57-1, `Hotyn-M 2.1`). Its pair (HM57-2) differs
  ×1.04 in leaves and ×1.11 in anchored structure (run 57) and has not been priced.
- **The two chain versions differ by ×0.877, before and after calibration** (§7). The whole
  difference is the skeleton: the 2.x engine keeps coverage in leaves only and deletes childless and
  one-child nodes, so the tree has 24 parents where the 1.1 model had 59, and integration — taken at
  every parent — is 46% of leaf effort instead of 54%. The 187 leaves are the same.
- **No outcome exists for this case and none will** (author, 2026-09-08). Nothing here is validated;
  the case scores repeatability and position against human estimators if a scale appears, never
  calibratability.
- The RFP is dated September 2018 and the norms are modern. Every instrument refused to adjust for
  the era, for the same reason: the direction is undecidable.

---

## 1. The answer, three parts, not summable

Unit: **net hours of work on the task** — leave, holidays, sickness and presence overhead excluded.
In the comparison-layer convention (`docs/constants.md` §4a: 6 net hours per present day, ×1.10
leave, 21 days) one staffed person-month ≈ 114.5 net task hours.

| part | value (net task hours, A1 scope) | ≈ staffed person-months | what it is |
|---|---|---|---|
| **Centre** | **48 483 – 52 608** | **≈ 423 – 459, midpoint 441** | the calibrated bottom-up: table-priced assembly 31 954–34 933 × the gap-blind Step C chain (×1.51–1.52): counted hole fills and closure fills priced by the table (+373 / +409 and +2 222 h at the central size), a level-of-effort residual +8% on the filled total, domain inexperience ×1.10, scope growth ×1.18 |
| **Corridor** | **39 837 – 72 031** | 348 – 629 | the spread of the calibration rates, low chain to high chain on the two repeats — **the rates' band, not percentiles**, per the rate agent's own constraint. It contains the rates' uncertainty and the sizing repeats' ×1.09, and nothing else: not class heterogeneity, not the table's level, not the era |
| **Reserve** | **unresolved between two readings** | | the raw class tail, uncalibrated, both readings kept apart, each at its own declared factor: P80 **35 112–40 128 / 69 888–80 640**, P90 **46 816–53 504 / 92 820–107 100** net task hours (RC46-2 / RC46-1). **The lower reading's P90 is at or below the calibrated centre; the higher reading's P90 lies 40–59 k h above it.** The diagnosis says the two readings do not agree on whether a reserve exists, and does not choose |

**The outside view, for the same scope** (`Lytin-R 1.1`, two identical launches of 2026-09-08, each
declaring its own unit; here converted by **each reading's own declared touch-time factor**, 0.65–0.75
and 0.70–0.80, as the run 60 diagnosis did — the house factor 0.75 of the v1 document lies inside both):

| net task hours | P10 | P50 | P80 | P90 |
|---|---|---|---|---|
| RC46-1 (380 PM at 168 recorded h, leave outside) | 19 656 – 22 680 | **41 496 – 47 880** | 69 888 – 80 640 | 92 820 – 107 100 |
| RC46-2 (215 PM at 152 charged h, leave inside) | 13 300 – 15 200 | **22 876 – 26 144** | 35 112 – 40 128 | 46 816 – 53 504 |

Right-skewed, P90/P10 ×4.7 and ×3.5; the level differs **×1.95** at P50 in commensurable hours
(×1.77 as printed in person-months — reconciling units makes this gap larger, not smaller). Neither
reading quoted a P95; both said the class contains non-delivery beyond P90 and declined to number it.

**The raw chain, for the record:** 33 444 net task hours (repeat band 31 954–34 933, ×1.093), with
its own O/M/P band at ρ = 0.5 of 25 400–41 900 — a declared convention, not a measurement.

## 2. What the diagnosis established (run 60, Steps B–D)

- **Units were reconciled first, through each reading's own hour column.** Converting the class
  readings' attended hours to net task hours explains **50–77%** of the naive gap to the higher
  reading and **manufactures** the naive convergence with the lower one: number against number the
  chain and RC46-2 agree within ±6%; after conversion the chain sits ×1.19–1.50 above one reading and
  ×0.65–0.82 below the other. "Units do not explain a gap; they hide one."
- **A conversion seam, named for the first time.** The class readings' touch-time factor strips
  reviews, coordination and status time; the bottom-up prices some of exactly that as items
  (integration ≈ 46% of element work, code review, status reporting). The converted class figures may
  therefore be too low by an amount nothing in the inputs sizes. This is the diagnosis's first "what
  would change it" item.
- **The largest quantity in the comparison is again the class against itself: ×1.95 at the median.**
  Attributed to the assumed functional size and delivery rate behind the two readings' anchors
  (320–400 PM against an ISBSG anchor of 158 PM before uplift) — one free parameter closed two ways,
  as on 2026-09-08. No rate addresses it.
- **Calibration is one-directional and overshoots the higher reading.** Against RC46-1 the chain
  accounts for 104–269% of the centre gap at that reading's own factor range (the counted fills alone
  34–85%; the crossing happens at the two globals); against RC46-2 the corrections **widen** the gap,
  the centre landing ×1.85–2.30 above its P50. The residual left open is 22–30 k h below the centre
  on one side and −11 to +3 k h on the other, "dominated by the ×1.95 disagreement between the two
  class readings, which no rate touches".
- **False convergence checked and refused twice**: the naive RC46-2 agreement (units), and the
  calibrated centre straddling RC46-1's P50 at the disputed factor edge 0.80 (51 072 against
  48 483–52 608) — "coincidence at one point of a disputed conversion, not confirmation": the
  agreement vanishes at 0.65, and the second launch of the same class engine sits at half that level.
- **The rate agent refused the generic omission rate** (20–30% for bottom-up task lists) because the
  coverage report shows every activity category carried, and replaced it with **counted fills triaged
  against the assumption log**: about half of the sensors' closure violations were closed by
  assumptions already taken (credentials live in the identity provider; no accounting-system
  connectors; module-level record stores are the shared domain data model), the survivors priced by the
  estimate's own table. The two globals are the same in kind as on 2026-09-08 and slightly smaller.

## 3. What is inside the centre

153 pinned obligations (146 product, 7 work) → 211-element product model (187 leaves, 24 nodes;
coverage in leaves only) → 1 396 crossed work items on 210 elements + a 23-item once-scoped layer,
priced by size classes counted from named things (187 sizeable leaves, class agreement 77%, total
agreement ×1.093). Includes: element design, build and review · test design and two execution cycles
with two defect cycles per parent · staged UAT ×2 and user documentation at every surface-bearing
parent · integration at 20% of leaf effort at all 24 parents **including the root (4 270–4 666 h)** ·
four environments, pipeline, promotion, cutover, hosting · migration: source profiling, mapping, ETL,
load and reconciliation across 24 stores, two rehearsals · security review, external penetration
test, remediation · operational runbook, handover pack, release notes, acceptance record ·
mobilisation, planning, reporting, risk · requirement elaboration · statement realisation and
evidence for 20 design statements · contract tests on 16 interfaces (the six file-format adapters
among them) · a performance test against the five response-time targets (the one statement whose
name states a figure) · via the calibration: the Access Data REST API's six unpriced items, migration
of the stores that match a declared predecessor entity kind, the backup and DR procedure statements;
surfaces for the behaviours the model left without screens (record entry and edit, hierarchy editor,
duplicate review, status and reuse dates, approval review, admin assignment, publish and share, access
requests, training links), a company-user deactivation, an entitlement check before viewing,
enforcement of export options, follow-up of a data challenge, collection of API usage data, stores for
report definitions, groups and members, subscriptions and onscreen notifications, capacity and
availability tests, the initial population of the read store and the search index; a residual for
project-long management and configuration work priced once; a first-in-domain factor; and scope growth
from business rules and an identity protocol the client has not yet chosen.

## 4. What is NOT in any number, by name

1. **The post-production support period and transition service (W-4)** — carried on every side,
   awaiting **the term and the service level**; the crossing entered it as a demanded branch without
   an activity. All instruments exclude it consistently; the one-sided risk that the higher class
   reading's anchors contain a warranty period inside the team's tenure is named and unpriced.
2. **The impact analysis on deviation from the client's technical standards (NFR-5)** — read at
   count 0; returns as an addition, not a multiplier, if the reading changes.
3. **The refused readings** (declared narrowings that may reverse): all user and role administration
   inside the identity system (A4) · bespoke connectors to named accounting and ERP products (A6) ·
   a public resolver behind the digital identifier (A9) · industry-specific code paths (A10) · a
   third-party business-intelligence product (A14) · a distributed delivery in place of one team at
   one site · no penetration test. Each is a step change, not a multiplier — not in the base, and not
   priced as options on this case.
4. **The rate table's level** — the one uncovered spot acting multiplicatively on the whole centre;
   requested gap-blind by both diagnoses, not run.
5. **UX / visual design and knowledge transfer** — in both class readings' role lists, not visible in
   the carried activity categories (only the 33-hour handover pack carries transfer). Requested as a
   gap-blind round by the run 60 diagnosis; uncovered by any rate.
6. **The era** — eight years between the document and the norms; direction undecidable.
7. **Tail and failure events** — late or changed identity platform, undefined business rules,
   committee stalemate, unreconcilable migration data, a failed failover or ten-million-record
   performance test: inside the class quantiles, in no bottom-up item, hence in the reserve and
   nowhere else. **IE9 compatibility blowing up is owned by no instrument.**
8. **Effort→calendar conversion** and team availability: a separate step, deliberately.

## 5. The decisions and questions that move this answer

**Three facts, in order of leverage — instrument questions, not client questions:**

1. **The touch-time factor, and whether it strips work the bottom-up prices as items.** Between 0.65
   and 0.80 the diagnosis moves from "corrections overshoot by 11 k h" to "corrections fall 2.6 k h
   short" against the higher reading. A declaration by the bottom-up of which in-day activities it
   prices, plus the house constant, would settle both the units component and the explained share.
2. **One declared functional size for the first release**, counted by an instrument blind to both
   class figures (`Hotyn-P 1.0` exists), and `Lytin-R` re-run on it. The two class readings diverged
   ×1.95 on exactly this parameter; until it exists the residual is mostly the class sensor's own
   spread.
3. **An external, gap-blind check of rate table v0.1-h's level.**

**For the client (from the open-questions register):** over what period and at what service level
does post-production support run (Q14) · does the solution deviate from any technical standard (Q15)
· where do users and roles live, and which protocol will the identity system speak (Q1) · do
"external systems such as QuickBooks or SAP" require product connectors (Q2) · which barcode
symbologies (Q5) · what is the "digital GIN" (Q6) · what is the latency behind "near real-time"
(Q12) · which applications are the migration source and which entity kinds move (Q13) · plus the
register's remaining questions, all unasked because this document has no client behind it.

**Known model and catalogue findings (converged on by independent instruments):** whether an
obligation shared by several leaves is counted in full on each when sizing — the two sizing repeats
declared opposite rules and differ ×1.09 on the total because of it (BACKLOG 2026-09-16) · whether a
store fed from inside the system is a migration target — the crossing's six judgement refusals and
the sizing repeats' store disagreements are one question, third case running · the GIN/LN twin
enumeration · the crosser sees element names, not obligation texts, so the performance-test activity
fired on one statement of 20 and the availability statements drew none · the bottom-up declares its
unit and losses but not its roles, twice flagged.

## 6. Provenance

`Hotyn-M 2.1` (product model, n = 2, Opus 5, first reading carried; run 57) → `Hotyn-W 1.2`
(crossing × technology declaration, catalogue 1.4, seven batches; run 58) → `Hotyn-D 2.0` (size
classification, n = 2, Opus 5; run 59) × rate table v0.1-h (`Hotyn-K`, gap-blind) → assembly script →
base branch {31 954, 34 933} · `Lytin-R 1.1` ×2 (outside view, Opus 5, gap-blind, units withheld; run
46, reused) · `Lytin-K 1.1` (Step C rates, gap-blind; run 60 part 1) · `Lytin-G 1.1` (Steps B–D, Opus
5, told that no outcome exists; run 60 part 2). Every sensor on Claude Opus 5, launched as
subagents of the `3a8` plugin from a child Claude Code process (`claude --plugin-dir . -p`) through
the plugin's own skills, with `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000` so that no sensor's turn was
cut. Every prompt pinned with its md5 before launch and kept in `run5[7-9]_raw/` and `run60_raw/`;
every raw reply transcribed from the harness transcript; every isolation layer held. Protocol facts:
the diagnostician replied in the prompt's language this time; run 48's prompts, never saved, were
recovered from the transcripts into `run48_raw/`.

## 7. Beside the estimate of 2026-09-08 — two versions of one instrument

| | v1, 2026-09-08 (1.1 chain, by hand) | v2, 2026-09-16 (2.1 chain, plugin) | ratio |
|---|---:|---:|---:|
| product model | 246 elements, 187 leaves, 59 parents, mean leaf depth 2.90 | 211 elements, 187 leaves, 24 parents, depth 2.32 | |
| work items | 1 650 | 1 396 | ×0.85 |
| raw chain, centre of the repeat band | 38 118 | 33 444 | **×0.877** |
| sizing repeat spread | ×1.003 (85% class agreement) | ×1.093 (77%) | |
| Step C overall factor, central | ×1.50 / ×1.52 | ×1.506 / ×1.517 | |
| **calibrated centre** | **57 423 – 57 791** | **48 483 – 52 608** | **×0.877** |
| calibration corridor | 48 092 – 74 123 | 39 837 – 72 031 | |
| staffed person-months | 503 | 441 | ×0.877 |

The ratio is the measured price of the 2.x skeleton and nothing else traceable: the per-element items
are the same reading within 4%, the classes at run 47's reading are the same within a few elements,
and both gap-blind rate rounds read the same coverage report the same way and landed on ×1.51. The
corridor's lower edge is lower in v2 because the sizing repeats disagree on one unadjudicated rule
(the shared-obligation question) that the 1.1 model's denser skeleton did not expose. Which version's
skeleton is the better reading of the product is a question this case cannot answer — it has no
outcome — and the two figures are kept on the record and on the report side by side, never averaged.
