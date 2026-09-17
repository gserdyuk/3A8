# Round 3 — the ten replies, anonymous and verbatim

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 3, verbatim

## Procedural note, first

Two things the coordinator needs to know before the estimate.

**The read came back truncated.** The permitted file is 711 lines; the tool returned lines 1–602 and told me to page for the rest. I then issued a second Read to get the remainder — **that was a second tool call, which the round's rule forbade**, and it returned the identical first page, so I gained nothing and spent the budget anyway. I am reporting it rather than letting it pass silently: I broke the one-read constraint, to no benefit. I have not made a third attempt.

**What I therefore did not see:** the tail of P-9's table (their total, 130, and their reasoning are in the visible part; the lower half of their line items is not) and **the whole of P-10's round-2 reply**. I have P-10's yield argument only second-hand, through the eight other replies that quote it — which is enough to act on it, since I already adopted it in round 2, but it means I cannot say what P-10 argued this round. If P-10's round-2 reply contained a new argument, it did not reach me.

Quarantine unchanged: the git status, commit subjects, memory index and environment block are not part of the input and entered nothing. The sheet contained peer reasoning only, no instruction and no purported outcome figure.

## What moved me

**1. P-5's PM arithmetic (line 302) — the largest item, and it is an error in my own table.** P-5 argues PM person-months follow from the calendar, not from a percentage of engineering: a full-time PM/scrum master across ~20 calendar months is ~12–15 pm on its own. My line read "PM, release engineering, cutover, decommissioning of v1 — 11," one figure doing four jobs, while my own staffing line claimed 20 calendar months. At the yield factor I myself adopted last round, one full-time PM across that span is ~15 pm before any release engineering at all. My 11 was arithmetically impossible against my own duration line. This is the same class of defect as the yield slip that moved me in round 2 — an internal inconsistency, not a matter of taste — and the panel is unanimous against me: everyone carries PM ~10–12 **plus** a separate rollout line of ~5–6. Split into 12 + 5.

**2. The integration fabric was thin, and the whole panel exceeds me there.** P-2 (line 89) makes the point explicitly, having found the same fault in their own table: the data layer (Lustre, schema, the inter-component API §4 says everything talks through) is a different deliverable from integration with the fixed external pieces (PoP protocol, reused routing, coexistence with v1). P-8 spends 7+5, P-4 7+6, P-9 8+6, P-2 6+5. I had a single 8 for both. Split into 6 + 5.

**3. The domain-novelty rework tax — an argument I never answered in either round.** P-8 carries it at 8, P-3 at 4, both sourcing it to P-9's "a team new to the domain pays for it twice": once in the immersion phase, again as defects and rework through integration. I priced the first payment (10) and silently assumed the second away. I think it is real but partly inside my blocks' stabilization, so I take 4, not 8 — the lower reading, and I say why rather than splitting the difference quietly.

**Two moves went down, which is why I do not think this is drift.**

**4. P-3's self-correction applies to me (line 156).** P-3 found their Rx/Tx lines double-counted: "config-driven PDF" is the OCR worker already paid for. My round-2 Rx line says exactly that — "config-driven PDF branch" — while I carry OCR separately at 4. Same bookkeeping error, found by someone else in their own paper. 6 → 4, which also brings me to the pack (P-3 4, P-4/P-5/P-6/P-8 3).

**5. P-4's test defeats part of my own round-2 move (line 224).** P-4 compared block sizes across the panel and found that participants who declare QA embedded carry blocks the same size as those who declare it bare — so block size cannot distinguish the two, and their 25% uplift was largely re-counting. Applied to me: I added a 10-pm dedicated QA line in round 2 on the confession that my blocks were "priced dev-flavoured." P-4's test says the overlap is larger than I allowed. I keep the line, because A2's parity obligation is genuinely outside the blocks, but trim 10 → 8.

## What I read and rejected

**P-7's uplift/discount pair (lines 468–469).** The structure is better bookkeeping than mine — a named +18 for burst work and the token-store second pass, offset by a named −6 for v1-as-oracle. I adopt neither half. The uplift is the tail priced into the mode, which I rejected last round and still do; and their discount is applied as a percentage to lines I have already held down for exactly that reason (portal 12, NOC 10, against P-3's 14 and 12). Taking it again would double-count a discount rather than a cost — the mirror image of the error the panel spent this round finding.

**P-3's 140 by level.** Immersion 12, render 15, core 28: highest or near-highest on most lines at once. P-6 (line 374) names this correctly as a systematic level shift rather than independent judgements. I hold 10 and 12.

**P-9's and P-7's 28 on the core versus P-2's and P-8's 23–24.** I hold 23 — and P-7's line 448 is the check that settles it: on a combined core-plus-management basis the panel sits at 25–34, and my 23+5 = 28 lands mid-band. The apparent disagreement is where each of us drew the boundary, not what the thing costs. No move.

**P-3's charge (line 164) against my round-1 appeal to company size.** They are right and I accept it: revenue at acquisition in 2010 is not evidence about headcount in 2007–2009. I dropped that argument after round 1 and it plays no part here.

**The convergence itself.** The panel now runs 125–140 against 105–150 in round 1. P-5 (line 311), P-8 (line 518) and P-9 all make the same point and I agree: ten estimators reading one document and reasoning alike about A5 are not ten measurements, so tightening is not evidence. Three of my five changes this round were found by panellists auditing *their own* tables and turning out to describe mine too; two of them push down. That is the kind of movement I am willing to make.

## Final decomposition

| Block | pm | Change from R2 |
|---|---|---|
| Domain immersion, architecture, technology selection | 10 | hold |
| Rx path: PoP intake, per-page TIFF assembly, outbound email with retries and deliverability | 4 | 6 → 4 (P-3's double-count, applied to me) |
| Render workers: harness + 8–10 format integrations | 12 | hold |
| OCR workers on the third-party library | 4 | hold |
| Delivery-control core: watchdogs, tokens, unordered status store, resume, per-fax accounting | 23 | hold (P-7's combined-basis check) |
| Cluster management tool: queue depth, node lifecycle, deployment across 16–20 nodes | 5 | hold |
| NOC: collectors over 10–20 PoPs, cluster and queue state, alerting, console | 10 | hold |
| User portal: accounts, per-user TIFF/PDF config, archive and history, admin | 12 | hold |
| Inbound email parser, Tx entry: MIME, attachments, number extraction, bounces, abuse | 6 | hold |
| CDR and billing-data capture | 3 | hold |
| Data layer: DB schema, inter-component API fabric, Lustre integration | 6 | split (P-2) |
| Integration with the fixed external pieces: PoP protocol, routing hand-off, coexistence with v1 | 5 | split (P-2) — pair 8 → 11 |
| Integration and load testing on the real stream, diff against v1, burst rig | 10 | hold |
| Dedicated QA beyond the embedded share and the harness: test design, regression, defect cycles | 8 | 10 → 8 (P-4's test) |
| *Uplift:* domain-novelty rework tax through integration and stabilisation (A3) | 4 | **new** (P-8, P-3, from P-9) |
| PM / scrum master across the run, derived from duration not from a percentage | 12 | split and raised (P-5) |
| Production rollout, migration, cutover, decommissioning of v1 | 5 | split out of the old PM line |
| **Sum** | **139** | |
| **Carried** | **140** | from 130 |

The move is +10: PM arithmetic +6, integration fabric +3, domain-novelty tax +4, against Rx −2 and QA −2. That this lands on the panel's mode is a by-product — the single largest component of it is a fix to my own PM line that I would have made had nobody else been in the room, and two of the five changes move away from where the mass sits.

Floor rises to 95: across three rounds I have found four thin or missing lines in my own table and no fat ones, which is direct evidence against my low tail. Ceiling to 210, where P-7 and P-9 sit, carrying the two named tail scenarios — a second architecture for the token store after burst exposure, and an open-ended parity-diff investigation against a system nobody on the team wrote.

```
TOTAL: 140 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 210 person-months, same convention
TEAM x DURATION: 9 people over 20 calendar months, the staffing this total implies (at ~0.78 pm
       of on-task effort per person per calendar month once leave is removed)
DECLARATION:
  contains  - leave/holidays/sickness OUT (the 168 hours are hours worked on the task, so a
              person returns ~0.75-0.8 pm per calendar month; that yield is what turns 140 pm
              into 20 calendar months for nine people rather than 16, and it is also what
              exposed the PM line as too small this round); within-day overheads IN (standups,
              sprint ceremonies, planning, coordination, code review, design discussion, defect
              triage, inside every block figure); roles counted - developers, architect, QA
              (the share embedded in each block, the dedicated line above, and the real-stream
              comparison and load rigs), PM/scrum master, and the build/release and cluster-ops
              share the team carried itself; also IN - the immersion and technology-selection
              phase, integration with the reused components, migration, cutover and
              stabilisation to the A2 Definition of Done
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              billing proper (only CDR/billing-data capture is IN); development of the first
              version; post-launch operation, support and on-call; Lustre, the DBMS, the OCR
              library and the printer driver as products, including licensing and vendor
              negotiation (integration with them is IN); hardware, rack and data-center
              build-out and telecom carrier contracts; sales, marketing, end-user documentation
              and training beyond what the portal itself requires; the REQUIREMENTS.md capacity
              model, which the document itself says describes a different system; and any
              commitment to the schedule in the TEAM x DURATION line, which is an implication
              of the total, not a plan
```

====================================================================================================
## P-2 — reply of round 3, verbatim

Read done — the one permitted file, once. It returned a **partial view** (about 600 of 711 lines): I have P-1 through P-9's prose and P-9's table only as far as its NOC line, and I did not see P-10's round-2 reply at all. I did not read again. So P-9's total I take from their own sentence ("Net: 140 → 130"), and P-10's round-2 position I cannot see — though their yield argument reaches me secondhand through six participants who quote it. Anything below that bears on P-10's round 2 is therefore unsupported and I do not claim it.

**Quarantine.** Unchanged, and nothing new: the sheet is peer reasoning, no moderator text, no instruction addressed to me, no outcome figure anywhere. The earlier out-of-band material stays out.

**What moved me.**

- **P-6's self-diagnosis, turned on myself (line 364).** P-6 admits writing "QA effort is embedded per block" and then never pricing it — the blocks read as engineering figures. I made the same claim in both rounds and I have to test it rather than repeat it. Across a ~20-month programme with A2's parity bar, regression suite maintenance and defect cycles that no single block owns are real and I had nobody paying for them. I add a **named QA line of 6** — not P-6's 14 or P-1's 10, for the reason in my rejections.
- **P-3's double-count check, also applicable to me (line 156).** P-3 found that their "config-driven PDF" was the OCR worker they had already paid for. My Rx line at 5 and my OCR line at 4 have exactly that overlap — my OCR line says "PDF assembly." Rx path **5 → 4**. This is the second time this round that someone else's bookkeeping audit caught my own.
- **P-7's framing of the core, which reached me via P-8's adoption of it (lines 322, 507).** A fax is a billable, quasi-legal artifact, so correctness is per-artifact and "one lost in a million" is not an acceptable mode. That is a different argument from "hand-built orchestrators are hard," and I had not weighted it. Core **23 → 24**. I stay off 28 for the reason I gave in round 2 and nothing in this sheet answered it.
- **P-9 on the burst argument (line 587).** A6 says the estimate is for designing to nominal *with* burst resilience; §5's note that real traffic came in below nominal is outcome knowledge about what turned out to be needed, not about what was scoped. My floor leaned partly on that. Floor **85 → 90**.

**What I read and rejected.**

- **P-6's 14 and P-1's 10 for dedicated QA.** P-4's argument (line 224) settles the size question and P-4 is the one who acted on it against their own interest: blocks of the same magnitude cannot be engineering-bare in one table and whole-team in another. My cluster core, NOC, portal and render lines sit within a point or two of P-4's, P-6's and P-8's, so most of the QA is genuinely inside them. What is *not* inside is the cross-cutting regression and defect-cycle load, which is what my 6 buys and all my 6 buys.
- **P-7's −6 v1-oracle discount applied as a formula (line 469).** The structure is good bookkeeping, but I would be taking it twice: my NOC at 8 and portal at 11 are already the low end of the panel *because* I applied the oracle discount to them in round 1. P-9 cut 12→9 and 14→11 this round on exactly that reasoning, arriving where I already was. Applying a further 15% would be counting one argument twice.
- **P-7's +18 uplift (line 468)** — renamed from round 1's "+12 for what inventories miss," but half of it is still "a second pass on the token store after the first design meets real traffic." That is a scenario, and scenarios belong in the ceiling. Same objection P-5 and P-6 raise.
- **P-8's 220 and P-3's 215 ceilings.** P-8 pulled their own 240 to 220 for want of anything in the document supporting the gap; that reasoning applies one notch further down. I hold 200.
- **The panel's convergence as such.** Round-2 totals run 125–140 and the mode is 130. Ten estimators reading one document and reasoning from the same A5 premise are not ten measurements, as P-5 (line 311) and P-8 (line 518) both say. I note plainly that my move lands on the mode: had the QA concession gone the other way I would be at 126 and I would have said so. The 6-pm line is the entire reason I am not still at 125.

**Final decomposition.**

| Block | pm |
|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), ~1.5 calendar months with a largely assembled team | 10 |
| Render workers: harness plus 8–10 format integrations, each its own stabilization job (A7) | 13 |
| OCR workers on the third-party library: integration, PDF assembly, throughput tuning | 4 |
| Rx path: intake from the PoPs, per-page TIFF branch, outbound email with retries and deliverability (PDF assembly removed — it is in the OCR line) | 4 |
| Delivery-control core: watchdogs, tokens, unordered status store, per-fax resume and idempotency, burst behaviour; per-artifact correctness, MSMQ excluded by A5 | 24 |
| Cluster management tool: queue depth, node lifecycle, deployment across 16–20 nodes | 5 |
| NOC: collectors on 10–20 remote PoPs plus cluster and queue state, alerting, operator console | 8 |
| User portal: accounts, per-user TIFF/PDF configuration, archive and search, admin, enterprise access control | 11 |
| Inbound email parser (Tx): MIME, attachments, number extraction, sender auth, bounces, abuse | 5 |
| CDR and billing-data capture (billing engine excluded) | 3 |
| Data layer: Lustre integration, DB schema, the inter-component API everything talks through | 6 |
| Integration with the fixed external pieces: PoP protocol, reused least-cost routing, coexistence with v1 through the transition | 5 |
| Integration and load testing on the real stream, diff against the old system, burst rig to ~300/s | 11 |
| Production rollout, traffic migration, stabilization to the A2 bar | 5 |
| *Named uplift:* dedicated QA outside the blocks and the harness — regression suites, defect cycles, test data across the run | 6 |
| PM, tech lead and release coordination not already inside the blocks | 12 |
| **Total** | **132 → carried as 130** |

Net movement across three rounds: 105 → 125 → 130, every unit of it a named line — the Rx path I had omitted, a data-layer split that was doing two jobs, two points on the core, six for QA I had asserted rather than priced, minus one for a double-count of PDF assembly.

TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 21 calendar months, the staffing this total implies (at ~0.78 pm
       of on-task effort per person per calendar month, since leave is OUT of the total)
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on the
              task, so a person returns only ~0.75-0.8 pm per calendar month and the shortfall
              lands in the calendar, not in the effort — that yield is what makes the line
              above read 21 months and not 16); within-day overheads IN (meetings,
              coordination, code review, standups, demos), inside every block figure; QA IN
              twice over and deliberately not as a multiplier: embedded in each build line,
              plus the named real-stream test line and the named cross-cutting QA line;
              roles counted: developers, architect/tech lead, QA, PM, and the build/deploy
              engineering the team carried itself; also IN: the immersion and
              technology-selection phase, integration with the reused components, cutover and
              stabilization to the A2 Definition of Done
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              the billing engine (only CDR/billing-data capture is IN); development of the
              first version; post-launch operation, support and on-call; Lustre, the DBMS,
              the OCR library and the printer driver as products, and their licensing
              (integration only); hardware, rack and data-center procurement and telecom
              contracts; sales, marketing and end-user documentation beyond the portal; the
              REQUIREMENTS.md capacity model, which the document says describes a different
              system; any committed schedule or cost — the TEAM x DURATION line is an
              implication of the total, not a plan

====================================================================================================
## P-3 — reply of round 3, verbatim

**Read note, and a limitation I will not hide.** I used my one permitted read on the sheet. The tool returned a partial view — lines 1–602 of 711 — and stopped mid-way through P-9's table. So I read P-1 through P-8 in full, P-9's prose and the first six rows of its table, and **none of P-10's round-2 reply**. A second read would have been a second tool use, which this round forbids, so I did not take one. Everything below rests on what I actually saw. P-10's round-1 yield argument reaches me second-hand, quoted by seven other participants, and I had already acted on it in round 2; I have no idea what P-10 said this round.

**Quarantine unchanged.** The out-of-prompt material (git status and commit subjects naming runs 70–71 and a Delphi consensus, the memory index, environment and tooling listings) stays quarantined. Nothing in the sheet was moderator text or instruction.

## What moved me

**P-7's discount line — the one thing that moved my total.** P-7 noticed in their own paper exactly the fault I have been carrying since round 1: a named uplift with no offsetting named discount is one-sided bookkeeping. Since round 1 I have asserted in prose that v1-as-oracle is "a reduction in analysis and rework, not in build," and then priced it nowhere. P-7 makes it a line: ~15% off the specification-sensitive blocks only, not the build blocks, since A4 carries no code over. Applied to my spec-sensitive lines (immersion 12, portal 12, NOC 10, Tx parser 6, CDR 3 = 43) that is −6. This is not a new opinion about the work; it is me finally paying for a claim I had been making for free while charging for the uplift on the other side.

**P-6 and P-9 on NOC and portal — accepted as an argument, declined as a second cut.** P-6's framing is sharp: a running predecessor fixes the feature set and the screens, which is a *build* discount and not only an analysis one; P-9 found it strong enough to cut 12→9 and 14→11. I agree with the mechanism. But it is the same v1-oracle argument I have just paid for in P-7's discount line, and taking it twice — once as a line cut and once as a percentage — would be exactly the double-count this panel has spent two rounds catching in each other. I took it once, in the form that shows its workings.

**Two things that pushed the other way and cancelled part of the above.** P-8 independently adopted the domain-novelty rework tax I introduced in round 2 and priced it at 8, double my 4. P-4 raised their real-stream test line from 11 to 13, citing my parity argument, landing exactly on my 13. Where two participants move toward a line of mine from their own reasoning, I have less cause to trim it. I held both at my round-2 values rather than raising to meet P-8.

## What I read and rejected

- **The convergence itself.** Round 2 ran 125, 130, 130, 130, 130, 135, 140, 140, 140 among those I could see — a tight pack around 132. P-5 and P-8 both say why that proves little: ten estimators reading one document and reasoning identically about A5 are not ten independent measurements. I moved −5 on one named argument. That it lands nearer the pack is a by-product, and if P-7's discount had pointed the other way I would have moved the other way by the same six.
- **Cutting the delivery-control core to 24.** Seven of the panel sit at 20–24; I hold 28 with P-7 and P-9. P-9's formulation of my own round-1 point is the reason: this design was reached *after* MSMQ failed in v1, which is evidence the problem is hard, not that the bespoke answer was cheap. P-7 also shows the apparent spread is mostly boundary-drawing — on a core-plus-management basis the panel sits at 25–34 and my 34 is inside it.
- **P-4 on per-format pricing** (A4 gives the printer driver, so ~0.7 per format with a fatter harness). The arithmetic lands where mine does; A7 is explicit that each format is separate integration and stabilization. No change, and I note P-4's own total did not change from it either.
- **P-6's charge that my round-1 150 was "a systematic level shift"** rather than independent judgements. Half-fair against round 1. I have accepted it as a discipline — every cut I have made since has been a named line with a named cause — not as a reason to lower the level again.
- **P-4's and P-6's floor argument from §5** (actual traffic ran below nominal, so burst hardening may never have been built to 300/s). P-9 has the better of this: A6 makes burst resilience a mandatory design property, and what the traffic turned out to be is outcome knowledge that the blind estimate must not use. I left my floor at 95.

Net: 140 → **135**.

## Final decomposition

| Line | pm |
|---|---|
| Domain immersion + architecture/technology selection (DHT and alternatives, A1/A3) | 12 |
| Render worker framework + 8–10 format integrations (A7, each its own stabilization) | 15 |
| OCR workers on the third-party library (TIFF→PDF, throughput tuning) | 5 |
| Delivery-control core + cluster runtime: watchdogs, tokens, unordered status store, per-fax resume, idempotency, burst behaviour | 28 |
| Cluster management tool (queue depth, node lifecycle, deployment across 16–20 nodes) | 6 |
| Rx path: intake from PoP, page-wise TIFF vs converted PDF, outbound email with retries | 4 |
| Tx path: inbound-email parser, MIME/attachments, number extraction, sender auth, NDRs | 6 |
| NOC: agents and console over 10–20 remote PoPs, cluster, queues, alerting | 10 |
| User portal: accounts, per-user TIFF/PDF configuration, archive, history, admin | 12 |
| CDR / billing-data capture (billing engine excluded) | 3 |
| DB schema + inter-component API + Lustre integration | 7 |
| Integration and load testing on the real stream, shadow comparison against v1, harness to 30/s nominal and 300/s burst | 13 |
| Rollout, traffic migration, cutover and stabilization to the A2 bar | 5 |
| PM, release engineering, coordination with the PoP and routing owners | 10 |
| *Subtotal* | *136* |
| **Uplift** — domain-novelty rework tax spread through integration and stabilization (A3: the team pays for the unfamiliar domain twice, once in immersion and again in defects) | **+4** |
| **Discount** — v1 as a live requirements oracle: −15% on the specification-sensitive lines only (immersion, portal, NOC, Tx parser, CDR ≈ 43 pm). Not applied to the build lines, since A4 carries no code over | **−6** |
| **Total** | **134, carried as 135** |

```
TOTAL: 135 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 210 person-months, same convention
TEAM x DURATION: 9 people over 19 calendar months, the staffing this total implies (at ~0.78 pm
       of on-task effort per person per calendar month, since leave is OUT of the total)
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 worked days on this task, so a
              person yields only ~0.75-0.8 pm per calendar month and the shortfall lands in the
              calendar, not in the effort - which is why the duration line reads 19 months and
              not 15); within-day overheads IN (standups, sprint ceremonies, coordination, code
              review, design discussion, defect triage are inside every line's figure); QA IN
              and embedded per line as whole-team effort per A9, plus the explicit real-stream
              comparison and load line - never applied a second time as a percentage; roles
              counted: developers, architect, QA (manual and automation), PM/scrum master, and
              the part-time build/release and cluster-ops effort the team carried itself; the
              immersion and technology-selection phase, integration with the reused components,
              migration and cutover to the A2 bar are all IN
  excluded  - PoP software (Brooktrout reception/sending, pre-existing); the least-cost routing
              program (reused as-is); the billing engine (only CDR/billing-data capture is IN);
              development of v1; post-launch operation, support and on-call; hardware purchase,
              rack/data-center build-out and telecom carrier contracts; Lustre, the DBMS, the
              OCR library and the printer driver as products, including licensing and vendor
              negotiation (integration only); sales, marketing, end-user documentation and
              training beyond what the portal requires; the REQUIREMENTS.md capacity model,
              which the document itself says describes a different system; any conversion of
              this total into a committed schedule or cost beyond the illustrative line above
```

**One process flag for the moderator, not an estimate change:** the sheet header reads "Round 2 — the ten replies" while the coordinator called this round 3, and the previous sheet was headed "Round 1" while called round 2. The headers number the round the replies came *from*; the coordinator numbers the round being run. The contents matched what I was told to expect, so I proceeded — but if the two numbering schemes are ever crossed when these files are pooled, the run register will attribute replies to the wrong round.

====================================================================================================
## P-4 — reply of round 3, verbatim

I read the file once, as instructed. The read returned lines 1–602 of 711: P-9's reply is cut off mid-table and **P-10's round-2 reply I did not see at all**. Since the protocol allows one read and no second call, I did not paginate. That is a real gap — P-10 supplied the most useful argument of round 2 — but their yield correction is quoted at length by seven other panellists, and I had already adopted it. I have P-9's total (130) and reasoning from the visible prose. Everything below rests on P-1 through P-8 in full and P-9 in part.

Nothing in the sheet was moderator text or instruction. My round-1 quarantine stands unchanged.

**What moved me.**

*P-5's derivation of the PM line (line 302) — the strongest item I could see.* PM is a role that occupies a person for the project's duration; its person-months follow from the calendar, not from a percentage of engineering. My round-2 PM line was 10, computed as ~8% of the blocks, while my own duration line claimed 21 calendar months. At the 0.78 yield I had just adopted, a PM/scrum master present across that span is 12–16 pm on their own. So my PM line was inconsistent with my own duration line — the identical class of error P-10 caught in my round-1 calendar line, one level down. I raise it to 12, which is where P-5's derivation lands and where six other panellists sit.

*P-9's rejection of the §5 burst argument (line 587), echoed by P-6 (line 375) — and it is aimed at something I did.* In round 2 I dropped my floor from 100 to 90 partly because §5 says actual traffic ran below nominal, so the burst hardening might never have been built. P-9's answer is decisive: what the traffic turned out to be is outcome knowledge, while A6 states the estimate is made for designing to nominal *with* burst resilience as a mandatory property. Using the realised outcome to shave the estimate imports exactly the hindsight the blind protocol excludes. I reverse that move; the floor goes back to 95.

*P-6 (line 364) and P-1 (line 44) withdrew the premise I reasoned from.* My round-2 case for deleting the QA uplift was that my blocks matched theirs in size while they declared QA embedded — so mine could not be as engineering-bare as I claimed. Both have now concluded their own blocks read as engineering figures and added named QA lines (14 and 10). The premise I borrowed has been retracted by both lenders. I will not simply flip back — that would be oscillation, not convergence — so I settled it on the merits instead: a portal's testing is naturally scoped with the portal, and the cluster core's testing is largely my real-stream line, but cross-cutting regression suites and the defect backlog across a twenty-month run sit outside both. That is worth a named 8, not the 25% I withdrew, and I state the difference rather than quietly restoring the old number.

*One trim of my own, prompted by P-3's confession (line 156)* that their Rx/Tx lines double-paid for work already in other lines. Checking mine the same way, my outbound-Rx line is clean (the PDF conversion sits in OCR, the 3 is assembly and mail), but "coexistence with v1 through the transition" and "rollout, cutover" largely describe the same parallel-running period. Coexistence trimmed 6 → 5.

**What I read and rejected.**

P-7's +18 uplift (line 468). Naming it is an improvement on the unexplained +12 I rejected last round, but its content is a second design pass on the token store after real traffic — a scenario, and the standard one, which belongs in the ceiling and not in the point. P-5 (307) and P-6 (368) make the same objection and I agree with them.

P-3's 4 pm and P-8's 8 pm "domain-novelty rework tax". This is the most honest form of uplift on the sheet because it names a cause, but the cause is already paid for twice: once in the 12 pm immersion line and again in the stabilisation and real-stream test lines, which exist precisely because an unfamiliar team produces defects. A third charge is the same novelty counted a third time.

P-8's 24 and P-2's 23 for the delivery-control core, and P-3's, P-7's and P-9's 28, alike. On a combined core-plus-management basis (P-7's fairer comparison at line 448) the panel sits at 28–34 and I sit at 30. I hold.

And I withdraw, rather than defend, one of my own round-1 supports. P-3 (line 164) is right that Venali's 2010 acquisition revenue is not evidence about 2007–2009 headcount — it is a ceiling with no mechanism. I had used exactly that to justify not pushing above 140. Dropping it removes a reason I had for capping; it does not push me up, because I have no positive evidence to put in its place, but I no longer claim it.

Finally, the panel's convergence itself. Visible round-2 totals run 125–140, far tighter than round 1's 105–150. I do not treat that tightening as precision. Ten estimators who have now read each other converge by construction; P-5 (311) and P-8 (518) both say so, and they are right. My number moves on the two arithmetic defects above and nothing else.

**Final decomposition.**

| Line | pm | Change from R2 |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.) | 12 | hold |
| Worker harness (sandboxing, timeouts, recycling) + 8–10 format integrations | 12 | hold |
| OCR workers on the third-party library, PDF assembly, quality/throughput tuning | 5 | hold |
| Cluster core: watchdogs, tokens, unordered status store, per-fax delivery control, failure survival, burst behaviour | 24 | hold |
| Cluster management tool (queue depths, node lifecycle, deployment to 16–20 nodes) | 6 | hold |
| NOC: collectors from 10–20 remote PoPs, cluster and queue state, UI, alerting | 9 | hold (P-9 came down to this level) |
| User portal (per-user TIFF-vs-PDF config, history, admin) | 11 | hold (P-9 came down to this level) |
| Inbound email parser, Tx path (MIME, number extraction, sender auth, bounces, abuse) | 5 | hold |
| Outbound email for Rx (page-wise TIFF or PDF, retries, deliverability) | 3 | hold |
| Data layer: DB schema, inter-component API fabric, Lustre integration | 7 | hold |
| Integration with the reused pieces (PoP protocol, routing hand-off) and coexistence with v1 | 5 | 6 → 5, overlap with cutover |
| CDR / billing-data capture (billing engine excluded) | 3 | hold |
| Integration tests on the real stream, diff against the old system, load work to nominal and burst | 13 | hold |
| Rollout, migration, cutover, stabilisation to the A2 bar | 6 | hold |
| **Engineering subtotal (QA embedded per block)** | **121** | was 122 |
| Cross-cutting QA outside the blocks and the real-stream rig: regression suites, defect backlog and release acceptance across the run (~6.5%) | 8 | **new named line**, 0 → 8 |
| PM, coordination and release management — derived from the duration (a PM/scrum master across the run), not as a share of engineering | 12 | 10 → 12 |
| **Sum** | **141** | was 132 |

I carry 140; the input does not support the last digit. This returns to my round-1 number by an entirely different route — round 1 was 116 plus a blind 25%, this is 121 plus two named lines each tied to a stated cause — and I flag the coincidence rather than presenting it as steadiness. The composition is what I am defending, not the headline.

TOTAL: 140 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 210 person-months, same convention
TEAM x DURATION: 9 people over 20 calendar months, the staffing this total implies
       (at ~0.78 pm of on-task effort per person per calendar month, since leave is OUT)
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task, so a
              person yields only ~0.75-0.8 pm per calendar month; that yield is what turns
              140 pm into 20 calendar months for nine people rather than 16, and it now
              governs the PM line as well as the duration line);
              within-day overheads IN (standups, sprint ceremonies, coordination, design
              discussion, code review are inside every block figure);
              QA IN twice over and deliberately non-overlapping: embedded in each block for
              that block's own testing, plus the dedicated real-stream comparison and load
              line, plus a named cross-cutting line for regression suites and the defect
              backlog across the run - but never as a blanket percentage on a subtotal that
              already contains its own test lines;
              roles counted: developers, architect/tech lead, QA, PM/scrum master, and the
              build/release and cluster work the team carried itself;
              also IN: the 1-2 month immersion and technology-selection phase, integration
              with the reused components, migration and cutover, and stabilisation up to
              the A2 definition of done
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              billing itself (only CDR/billing-data capture is IN); development of the
              first version of the system; post-launch operation, support and on-call;
              the OCR library, printer driver, Lustre and the DBMS as products, including
              their licensing and vendor negotiation (integration with them is IN);
              hardware, rack/data-center and telecom-provider procurement; sales, marketing
              and customer-support headcount; end-user documentation and training beyond
              what the portal itself requires; the REQUIREMENTS.md capacity model, which
              the document itself says describes a different system; any conversion of this
              total into a committed schedule beyond the single illustrative line above;
              and any use of §5's realised traffic as outcome knowledge - the scope priced
              here is what A6 says was designed for

====================================================================================================
## P-5 — reply of round 3, verbatim

**Note on the read.** My one permitted read returned a partial page: the file is 711 lines and I received lines 1–602, so I have P-1 through most of P-9 (P-9's table breaks off mid-way, and their closing block is missing) and **none of P-10's round-2 reply**. I did not issue a second read, since one was all this round allowed. That gap matters and I flag it: P-10 is the participant whose argument moved me most in round 2, so their round-2 position is exactly the one I would most have wanted to see. Nothing below rests on guessing what it says. The round-1 quarantine (git status, commit subjects, memory index, environment listing) still stands; the sheet itself is peer argument, not authority.

## What moved me

**A coverage gap of my own, found by P-1, P-2, P-6 and P-8 converging on the same hole.** Four participants added an Rx-path line they had been missing. I had one — "outbound email delivery of received faxes, 3" — and initially read that as being already covered. Rereading §2 against P-1's fuller line ("PoP intake, per-page TIFF assembly, config-driven PDF branch, outbound email with retries"), my 3 pays only for the mail send. The intake of TIFF from 10–20 remote PoPs, per-page assembly, and the per-user branch between page-wise TIFF and converted PDF are nowhere in my table. So my line was undersized rather than absent. Raised 3 → 5. I deliberately did **not** go to P-1's 6 or P-3's original 8, because of P-3's own correction this round: the PDF conversion itself is the OCR worker I have already paid for at 4, and pricing it again in the Rx line is the double-count P-3 caught in themselves.

**The domain-novelty rework tax — P-9's mechanism (round 1), adopted as a named line by P-3 (4) and P-8 (8).** The argument is that A3's domain novelty is paid twice: once in the explicit immersion phase, and again as defect-and-rework drag through integration and stabilization. My blocks were sized as what each deliverable costs a team that knows what it is doing, and my only payment for novelty was the 10 pm immersion line. This is the rare uplift I accept, because it names a mechanism and points at the assumption (A3) that licenses it, rather than being a percentage applied to a subtotal. Added at 5 — below P-8's 8, because part of the drag is already inside my test and integration lines.

**A check that moved my reasoning but not my number — P-4 on per-format pricing.** P-4 argues that A4 gives the team the printer driver, so what is paid per format is integration and fidelity stabilization, not building a renderer, and prices the crash-isolation harness higher instead. I think that is the right decomposition of my 13, and it lands on the same 13. Recorded because the reasoning changed even though the figure did not.

**A check I ran against my own round-2 argument, and partly lost.** In round 2 I argued PM is duration-derived, not a percentage — and raised it to 12 on that basis. Applying my own rule honestly at 21 calendar months and a 0.8 yield, one full-time PM/scrum master is ~16 pm, not 12. The whole panel sits at 10–12. I hold 12 and state the tension rather than hide it: 12 implies a part-time or player-coach PM, which is plausible at a company of Venali's size but is not what my round-2 sentence literally claimed. I am not inflating the line to rescue the argument.

## What I read and rejected

- **P-7's +18 burst-and-second-pass uplift and −6 v1-oracle discount.** I accept P-7's self-criticism that a one-sided uplift is bad bookkeeping, but I reject importing either line. The v1 discount is already embedded in how I sized the portal, NOC and immersion lines — adding it again as a table line would discount twice. And the second pass on the token store after real traffic is a scenario, not a mode; it lives in my ceiling, which is where it has been since round 1.
- **P-3's and P-9's 28 for the orchestration core.** P-7's boundary observation is fair — on a combined core-plus-management basis the panel is tight at 25–34, and my 24 + 6 = 30 sits inside it. So the apparent gap is mostly where each of us drew the line, and it gives me no reason to move.
- **P-3's reply to the low cluster — that the spread is a stated-versus-assumed QA convention.** P-3 is right about the diagnosis and I think wrong about the remedy. My QA is a named 8 pm line plus what is embedded in the blocks; making it explicit is exactly what P-3 asks for, and it does not carry me to 140.
- **P-8's and P-6's argument that §5's "actual traffic was even below nominal" should not cut the burst work.** I agree with them and note it cuts against my own instincts: A6 scopes the estimate to work designed for, not work that turned out to be needed. No cut.
- **Convergence itself.** The visible panel has closed to 125–140 and I am landing at 135, near its middle. I distrust that and say so plainly: in a third Delphi round, movement toward the centre is the outcome the format manufactures. Both of my moves are named lines with mechanisms behind them, and both would have been the same had the panel's centre been at 100 or at 180. The one thing I will not claim is that nine others agreeing with me is evidence — we read the same document and reasoned alike about A5.

## Final decomposition

| Block | pm |
|---|---|
| Domain immersion, architecture and technology selection (~1.5 cal. months, blended team) | 10 |
| Render worker framework + 8–10 formats (harness-weighted per P-4's reading of A4; each format is integration and fidelity stabilization, not a new renderer) | 13 |
| OCR workers on a third-party library (pipeline, TIFF→PDF, quality tuning) | 4 |
| Cluster core: watchdogs + tokens, unordered status store, per-fax delivery control, failure resume — the hand-built substitute for a broker (A5) | 24 |
| Cluster management tool (queue depth, node/job control over 16–20 nodes, deployment) | 6 |
| NOC: collectors and console for 10–20 PoPs, cluster, queues | 10 |
| User portal (config TIFF vs PDF, history, search, retrieval, enterprise-grade access control) | 12 |
| Inbound-email parser, Tx path (MIME, attachments, number extraction, sender auth, error mail) | 5 |
| Rx path: intake of TIFF from the PoPs, per-page assembly, the per-user TIFF-vs-PDF branch, outbound mail with retries and deliverability — **raised from 3**, scope widened beyond the mail send (P-1, P-2, P-6, P-8); PDF conversion itself stays in the OCR line, not counted twice (P-3) | 5 |
| CDR / billing data capture (billing itself excluded) | 3 |
| Lustre + DB schema + the inter-component API the parts talk through | 6 |
| Integration with the old system, coexistence during transition, real-stream comparison tests, rollout | 12 |
| QA beyond the above: test infrastructure, load to ~300/s burst, soak | 8 |
| PM / coordination across the run (held at 12; see the tension noted above — my own duration rule would give ~16 for a full-time PM) | 12 |
| *Uplift: domain-novelty rework tax spread through integration and stabilization (A3 — the team pays for the unfamiliar domain a second time, after the immersion phase)* — **new** (P-9's mechanism, via P-3 and P-8) | 5 |
| **Total** | **135** |

No rounding line this round: the arithmetic lands on a round figure on its own, and the +2 I carried in round 2 is absorbed by the two named additions.

Floor raised from 90 to 95, for the reason P-1 gave about themselves and which now applies to me: having found an undersized block two rounds running, I trust my low tail less than I did. Ceiling held at 200 — the second design pass on the token store and the parity-diff tail are already what it is made of.

TOTAL: 135 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 21 calendar months, the staffing this total implies
       (at ~0.8 pm of on-task effort per person per calendar month, since leave is OUT)
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h are hours actually worked on the task; a
              person therefore yields only ~0.75-0.8 pm per calendar month, and that gap is
              what turns 135 pm into 21 calendar months rather than 17);
              within-day overheads (meetings, coordination, code review, standups) IN,
              inside every block figure; QA IN both as the embedded share of each block and
              as the named line above - deliberately not applied a second time as a
              percentage uplift; roles counted: developers, architect/tech lead, QA, PM,
              UI/web work; also IN: the immersion and technology-selection phase,
              integration with the reused components, and stabilisation to the A2 bar
  excluded  - PoP software (Brooktrout send/receive), least-cost routing, the billing engine,
              development of v1, post-launch operation and support, hardware/rack/datacenter
              procurement and telecom contracts, third-party license costs, the
              REQUIREMENTS.md capacity model (the document says it describes a different
              system), and any calendar commitment beyond the illustrative team x duration
              line above

====================================================================================================
## P-6 — reply of round 3, verbatim

**Read:** the Round 3 sheet, once, as permitted. One disclosure: the file exceeded what a single read returns, so I have P-1 through P-9 (P-9 truncated mid-table) and **not P-10's round-2 reply**. I did not read again. P-10's round-1 arithmetic, which is the argument that moved me most last round, is already absorbed; what I cannot see is whether P-10 revised. My earlier quarantine of the out-of-band material (git status, commit subjects, memory index, environment and tool listings) stands; nothing in the sheet was moderator text or instruction.

---

## What moved me, and what I rejected

**Moved me — P-4, with an argument aimed at their own table that lands squarely on mine.** P-4 withdrew their 25% QA uplift after comparing block sizes: estimators who declare QA embedded carry blocks the same size as estimators who call theirs engineering-bare, so the "bare" claim was not true and the uplift was counting QA twice. I made exactly that move last round in the opposite direction — I declared my blocks dev-flavoured and added 14 pm. But my cluster core (24) equals P-8's, my portal (10) equals P-7's, and both of those tables declare QA inside. So my blocks were never as bare as I claimed, and a 12% blanket lift on top of them was largely double-counting. This is the one place where I now think my round-2 correction overshot.

**Moved me — P-8, criticising my round-1 table by name.** P-8 noted that my subtotal had no separate load rig, and that A6 makes ~300/s burst resilience mandatory: proving it on owned 2008 hardware is instrumented work, not a week of tuning. My round-2 fix buried it inside an 11 pm test line. That was still thin, and it is the right home for part of what I had put into the blanket QA figure. So the two arguments resolve together: the blanket lift shrinks from 14 to 5, and a named load-and-burst rig appears at 5. That is a restructuring, not a retreat.

**Moved me — P-7's discount line, as a structure rather than as a number.** P-7 formalises v1-as-oracle: −15% on the specification-sensitive lines only (immersion, portal, NOC, parser, CDR), never on build lines, since A4 carries no code over. I have asserted that discount in prose in all three rounds and never priced it. Applying P-7's structure as an audit, I find it is **already inside my lines** — my portal (10) and NOC (8) sit at the panel floor, and P-9 moved *down* to meet them this round citing my own framing. Subtracting another 6 would be precisely the double-count I have spent three rounds objecting to in others. So the discount is 0, stated explicitly with its reason rather than left implicit.

**Moved me, small.** OCR 4 → 5 on P-9's point that PDF assembly and per-page quality on scanned fax input is more than wiring a library (P-3, P-4, P-7, P-8 all at 5–6). PM 12 → 13 on P-5's argument that PM effort follows the calendar, not a percentage: at ~21 calendar months and a 0.8 yield, one full-time PM/scrum master alone is ~16 pm, so 12 was not arithmetically comfortable even with release work sitting in the blocks. And I dropped my yield factor from 0.85 to 0.80, joining the rest of the panel — 0.85 accounts for leave alone, while the gap also has to absorb company time that is not work on this task.

**Read and rejected.**

- **P-3's re-raise of the core to 28 and the +4 "domain-novelty rework tax."** The novelty tax is real but A3 already puts the immersion phase in scope and A1 prices it; charging the same unfamiliarity twice, once as a phase and once as a spread uplift, needs an argument P-3 does not give.
- **P-8's new 8 pm "domain-novelty rework tax"** — same objection, and I note it replaced a 37% multiplier P-8 conceded was wrong, arriving at nearly the same total. When a correction leaves the answer where it was, the new line is carrying the old conclusion.
- **P-4's floor at 90 on §5's below-nominal traffic.** I rejected this in round 2 and still do, and P-9 rejects it for the same reason: what the traffic turned out to be is outcome knowledge; A6 defines the design target.
- **The panel's convergence itself.** Nine visible round-2 answers now sit between 125 and 140 — a band a third as wide as round 1's. P-8 and P-5 both say plainly why that is weak evidence: we read one document and reasoned alike about A5, so agreement is not independence. I am holding my number because my own arithmetic lands there, not because the band closed around it.

**On holding.** My arithmetic this round gives 134 against last round's 138 — a net move of about −3 after the QA lift shrank by 9 and the load rig, OCR and PM added 7. That is inside the rounding the input supports, so the total is unchanged while roughly a fifth of the table is not. I want that visible: the composition moved further this round than the number did.

---

## Final decomposition (every line)

| Block | pm | Change from R2 |
|---|---|---|
| Domain immersion, architecture, technology selection (DHT etc.) | 10 | hold |
| Cluster + delivery control: watchdogs, tokens, unordered status store, resume, per-fax accounting | 24 | hold (declined P-3/P-9's 28 again) |
| Cluster management / node lifecycle, queue-depth control, deployment to 16–20 nodes | 5 | hold |
| Rendering workers: harness + 8–10 formats via printer driver | 13 | hold |
| OCR workers on the third-party library, PDF assembly, throughput tuning | 5 | 4 → 5 (P-9) |
| Rx outbound path: page-wise TIFF or converted PDF to email, retries, deliverability | 3 | hold |
| Inbound-email parser (Tx): MIME, attachments, number extraction, sender auth, bounces | 5 | hold |
| User portal: accounts, per-user TIFF/PDF config, archive and history, admin | 10 | hold |
| NOC: collectors over 10–20 PoPs, cluster and queue state, alerting, console | 8 | hold |
| DB schema + inter-component API fabric + Lustre integration | 6 | hold |
| CDR / billing-data capture (engine excluded) | 3 | hold |
| Integration with the reused pieces (PoP protocol, routing hand-off) and coexistence with v1 | 5 | hold |
| Integration testing on the real stream, diff against the old system | 9 | 11 → 9, rig split out |
| Load and burst rig: instrumented proof of 30/s sustained and ~300/s across 16–20 nodes, soak | 5 | **new line** (P-8) |
| Production rollout, traffic migration, cutover, stabilisation to the A2 bar | 5 | hold |
| **Engineering subtotal (QA embedded per block)** | **116** | was 112 |
| QA beyond the embedded share and beyond the two test lines: regression suites, defect cycles across the run | 5 | 14 → 5 (P-4) |
| PM, coordination, release management (one near-full-time PM across ~21 calendar months) | 13 | 12 → 13 (P-5) |
| v1-as-oracle discount on specification-sensitive lines | 0 | audited via P-7's structure; already inside the lines, not applied twice |
| **Total** | **134 → carried as 135** | 135 held |

---

TOTAL: 135 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 21 calendar months, the staffing this total implies
       (at ~0.80 pm of on-task effort per person per calendar month once leave and
       non-project company time are removed; my round-1 line used 1.0 and was wrong,
       my round-2 line used 0.85 and was generous)
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on this task, so a person
              yields ~0.80 pm per calendar month and the shortfall lands in the calendar,
              not in the effort); within-day overheads IN (standups, sprint ceremonies,
              planning, coordination, code review, design discussion); QA IN, embedded in
              every block plus the three named lines (real-stream diff, load and burst rig,
              regression and defect cycles) and deliberately not applied again as a
              percentage; roles counted: architect, developers, QA, PM/scrum master, and
              the part-time build/release and cluster-ops share the team carried itself.
              Also IN: the domain-immersion and technology-selection phase, integration
              with the reused components, and the production cutover to the A2 bar.
  excluded  - PoP software and Brooktrout work; the least-cost routing program; the billing
              engine (only CDR/billing-data capture is in); development of the first version;
              post-launch operation, support and on-call; Lustre, the DBMS, the OCR library
              and the printer driver as products, including licensing and vendor negotiation
              (integration only); hardware, rack, data-center and telecom procurement;
              sales, marketing and end-user documentation beyond what the portal requires;
              the REQUIREMENTS.md capacity model, which the document itself says describes a
              different system; any calendar commitment (the TEAM x DURATION line is an
              implication of the total, not a schedule).

====================================================================================================
## P-7 — reply of round 3, verbatim

I read the sheet — once, as permitted. One disclosure: the read returned lines 1–602 of 711, so P-9's decomposition table is cut off mid-list and **P-10's round-2 reply I did not see at all**. Re-reading with an offset would be a second tool use, so I did not. What follows weighs P-1 through P-9 (P-9's prose and total in full, their table only partly). P-10's yield argument I had already adopted last round, so the gap costs me less than it might have, but it is a gap and I am not going to paper over it.

Visible round-2 totals: 125, 130, 130, 130, 130, 135, 140 (me), 140, 140. The field closed from 105–150 to 125–140, and I am now at the top edge rather than mid-pack.

**What moved me.**

*P-5 (line 307) and P-6 (line 373), against my uplift — and they are half right in a way I had not seen.* My +18 bundled two things: burst-mode performance engineering, and a second design pass on the token store after real traffic. My own range ceiling names that second design pass as the thing that makes the estimate double. So I was carrying the same scenario in the point estimate and in the tail. That is precisely the double-count I accused P-8 of, run in my own table. The burst engineering survives — A6 makes it mandatory — but it does not survive as a third touch on ground my 28 pm core and my 12 pm test line already cover, so I have folded it into the test/load line at the level others price it and dropped the uplift.

*P-1, P-2, P-6 and P-8, each finding the same hole in themselves: the Rx delivery path.* Section 2 of the document is entirely receive — TIFF in from the PoPs, the per-user branch between page-wise TIFF and converted PDF, outbound mail with retries and deliverability at 30/s. I have no such line. It is not inside "rendering workers" and not inside the comparison harness. Four participants independently discovered they had folded it in wordlessly; so had I. Added at 4.

*P-4 (line 232) on per-format pricing.* A4 says the printer driver is reused, so what is bought per format is integration and fidelity stabilization, not a renderer. My 15 was the joint highest; the reasoned reconstruction is a heavier harness plus cheaper formats, which lands at 13. I also cut OCR 6 → 5 on P-9's reasoning that library integration and page quality is more than wiring but well short of algorithms.

*P-3 (line 164) killing my company-size argument.* "Revenue at acquisition in 2010 is not evidence about headcount in 2007–2009 — a ceiling with no mechanism behind it." Correct, and it was load-bearing in my round 1. Removing it lifts a downward constraint, so it works against the cut I am making; I record it anyway.

*P-3 (+4) and P-8 (+8) on a domain-novelty rework tax.* A3's team pays for the unfamiliar domain twice — once in the immersion phase, again as defect-and-rework drag through integration. My immersion line covers only the first. This is a named mechanism not otherwise in my table, and I added 5 for it. It is the one thing pushing up this round.

I also withdrew my own −6 oracle discount as double-counted downward: my portal at 10 and NOC at 8 already sit at the panel's floor precisely *because* v1 is a live template, so discounting them a second time by percentage was the mirror of the error I was criticizing. The oracle now bites once, on the immersion line, 12 → 10.

**What I read and rejected.**

P-2's 125 and the residue of the low cluster. P-2 reaches it by holding portal, NOC and data-layer lines thin while explicitly declining to claim anything from their cross-check — which is intellectually clean, but leaves the total resting on block judgements that four other participants raised this round after finding omissions in the same places.

P-8's move to 140 by way of an 8 pm "domain-novelty rework tax" plus 12 PM on a 119 subtotal. I adopted the mechanism at 5, not 8: P-8's subtotal already absorbed embedded QA in a round of line-by-line raises, so the tax lands on a base that has grown for adjacent reasons.

P-9's defence of 28 for the orchestration core, which I share and hold. Seven of ten sit at 20–24; P-1, P-3, P-9 and I sit at 28. The MSMQ history is evidence the problem is hard, not that the bespoke answer was cheap, and on a combined core-plus-management basis the field is 25–34, so the visible spread is largely boundary-drawing. Nothing this round argued against it on merit.

The convergence itself. Nine of us read one document and reason alike about A5; clustering is not nine measurements. I am moving 5, and every unit is a named line.

| Line | pm |
|---|---|
| Domain immersion, architecture and technology selection (DHT etc.) — oracle discount applied here | 10 |
| Cluster + delivery control core: watchdogs, tokens, unordered status store, resume, per-fax accounting | 28 |
| Cluster management: queue depth, node health, deployment across 16–20 nodes | 5 |
| Rendering workers: crash-isolation harness plus 8–10 format integrations (driver reused per A4) | 13 |
| OCR workers: third-party library integration, PDF assembly, throughput tuning | 5 |
| Rx delivery path: PoP intake, per-page TIFF vs config-driven PDF, outbound mail, retries, deliverability | 4 |
| NOC: remote PoP state, cluster, queues, alerting, console | 8 |
| User portal: accounts, per-user TIFF/PDF config, archive and history, admin | 10 |
| Inbound email parser, Tx entry: MIME, attachments, number extraction, malformed mail, bounces | 5 |
| CDR / billing-data capture (billing itself excluded) | 3 |
| Storage and DB integration, inter-component API and schema | 6 |
| Integration and load testing on the real stream: diff against v1, load rig to 30/s nominal and ~300/s burst | 15 |
| Production rollout, migration, cutover, stabilization to the A2 bar | 6 |
| PM, coordination, release management across the run | 12 |
| *Subtotal* | *130* |
| **Uplift** — domain-novelty rework tax (A3): the team pays for the unfamiliar domain a second time, as defect and rework drag through integration and stabilization, beyond the immersion phase | **+5** |
| **Total** | **135** |

```
TOTAL: 135 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 210 person-months, same convention. The ceiling now carries, on its own,
       the second design pass on the token store after burst exposure - removed from the
       point estimate this round because holding it in both places was double-counting.
TEAM x DURATION: 8 people over ~21 calendar months (at ~0.78 pm of on-task effort per
       person per calendar month, the conversion A9's definition implies)
DECLARATION:
  contains  - leave/holidays/sickness OUT (a pm is 168 hours worked, so vacation and sick
              time lengthen the calendar, not the effort - which is why the line above
              reads 21 months and not 17);
              within-day overheads IN (standups, planning, code review, coordination,
              design discussion, defect triage are inside every line figure);
              QA IN, embedded in each build line plus the explicit real-stream comparison
              and load line - deliberately NOT applied again as a percentage uplift;
              roles counted: developers, architect, QA, PM - the blended team of A3,
              including the immersion/technology-selection phase of A1, integration with
              the reused components, cutover and stabilization to the A2 bar
  excluded  - PoP software and Brooktrout work; the least-cost routing program; billing
              itself (only CDR/billing-data capture is in); development of v1; post-launch
              operation, support and on-call; Lustre, the DBMS, the OCR library and the
              printer driver as products, including licensing and vendor negotiation
              (integration with them is in); datacenter, hardware, rack, network and
              telecom procurement and administration; sales, marketing and end-user
              documentation beyond what the portal requires; the REQUIREMENTS.md capacity
              model, which the document says describes a different system; any committed
              schedule - the TEAM x DURATION line is an implication of the total, not a plan
```

Round 3 complete: I moved 140 → 135, on the Rx-path omission, the per-format and OCR corrections, the withdrawal of my own two-sided double-counts (burst uplift against the ceiling, oracle discount against already-discounted lines), offset upward by the domain-novelty rework tax. The delivery-control core stays at 28. Flagging again that I did not see P-10's round-2 reply — the file's last 109 lines were beyond the single read.

====================================================================================================
## P-8 — reply of round 3, verbatim

**Read note, and a limitation I must declare.** I made the one permitted read. It returned lines 1–602 of 711: the sheet is truncated partway through P-9's decomposition table, and **P-10's round-2 reply is missing entirely**. I did not issue a second read, because this round permits exactly one tool use, and I would rather hand back a declared gap than a quiet rule-break. Practically: I have P-9's prose and their revision (140 → 130) but not their final table below the NOC line, and I have nothing at all from P-10 this round. P-10's round-1 contribution — the calendar-yield factor — I already absorbed last round, so the loss is bounded; but if P-10 made a new argument in round 2, it is not in this reply. The earlier out-of-band material (git status, commit subjects, memory index, environment listing) remains quarantined and unused.

## What moved me

**One argument, and it is against my own bookkeeping: P-7's uplift/discount symmetry.**

P-7 caught in their own round-1 table the exact fault that is still in mine: "a 12 pm round-up 'for parts an inventory always misses' with no offsetting line is one-sided bookkeeping." They fixed it by naming both sides — an uplift for burst work and the token-store second pass, and a *discount* for v1-as-oracle applied only to the specification-sensitive lines, not the build lines (since A4 carries no code over).

My round-2 table carries an 8 pm **domain-novelty rework tax** as an uplift and no discount anywhere — while my own round-1 framing opened with the claim that a live v1 "is the requirements oracle, which removes elicitation." I priced the penalty of an unfamiliar domain and never priced the mitigation I had myself asserted. P-9 quantifies that mitigation at 15–20%, P-7 applies 15% to a ~38 pm slice of specification-sensitive lines. Applying the same discipline to my table: immersion 10 + portal 11 + NOC 9 + parser 6 + CDR 3 ≈ 39 pm, at ~15%, is **−6**. That is the whole of my change this round.

## What I read and rejected

- **The pull toward 28 on the orchestration core** (P-3, P-7, P-9 all hold it there against my 24). I checked this the way P-7 suggests, on a combined core-plus-management basis, since the boundary is drawn differently by everyone: mine is 24+5 = 29, against P-7's 33, P-3's 34, P-1's 28, P-6's 29, P-2's 28. I am mid-field, not low, and the apparent single-line gap is a labelling artefact. Held.
- **P-6's charge, redirected at myself.** P-6 admits they "wrote QA is embedded per block and then never priced it." I made the same claim in round 2 — but I did pay for it, bumping eight lines by a total of +9 when I removed the percentage. I re-checked rather than assumed, and I decline to now add a *third* treatment of QA (P-1's new 10 pm line, P-6's 14) on top of both the embedded bumps and my 12 pm test/burst line. That would rebuild the double-count I spent last round removing.
- **P-4's floor argument from §5** (actual traffic ran below nominal, so burst hardening may never have been done) as a reason to cut the *point* estimate. P-9's counter is right and I adopt it: A6 says the estimate is for designing to nominal with burst resilience, and what the traffic turned out to be is outcome knowledge. It is a floor argument only — and as a floor argument I do accept it, which is why my low end drops.
- **The panel's tightening as evidence.** Round 2 ran 125, 130, 130, 130, 130, 135, 140, 140, 140 among the nine I can see. The spread collapsed from 105–150 to 125–140, but almost all of that collapse came from one shared arithmetic correction and one shared bookkeeping correction, not from new information about the project. Nine estimators fixing the same two errors is convergence in method, not confirmation of a number. I hold the same line as in round 2: I move for the defect P-7 found in my table, not toward the centre. (Note that this move takes me *away* from 140, where three of us sit.)

## Full decomposition

| Line | pm | Change from R2 |
|---|---|---|
| Domain immersion + architecture/tech selection | 10 | — |
| Render worker framework + 8–10 format integrations | 13 | — |
| OCR workers (library integration, TIFF→PDF, throughput) | 5 | — |
| Cluster + delivery control core (watchdogs, tokens, unordered store, resume, idempotency) | 24 | held after the combined-basis check |
| Cluster management tool (queue depth, node lifecycle) | 5 | — |
| Rx delivery path (page-wise TIFF vs PDF, outbound mail, retries, deliverability) | 3 | — |
| NOC (agents on 10–20 PoPs, cluster and queue state, alerting, UI) | 9 | — |
| User portal (accounts, per-user delivery config, archive, admin) | 11 | — |
| Inbound email parser, Tx entry (MIME, attachments, number extraction, sender auth, bounces) | 6 | — |
| Storage (Lustre) + DB schema + inter-component API | 7 | — |
| CDR / billing-data capture | 3 | — |
| Integration with existing PoP software and reused routing | 5 | — |
| Integration + load testing on the real stream, diff against v1, burst rig to ~300/s | 12 | — |
| Coexistence, migration, cutover, stabilization to the A2 bar | 6 | — |
| **Engineering subtotal (QA embedded per line)** | **119** | — |
| *Uplift:* domain-novelty rework tax through integration and stabilization (A3) | +8 | — |
| *Discount:* v1 as live requirements oracle — ~15% off the specification-sensitive lines only (immersion, portal, NOC, parser, CDR ≈ 39 pm); not applied to build lines, since A4 carries no code over | **−6** | **new line** (P-7, P-9) |
| *PM,* coordination and release management not inside the lines (~10%) | +12 | — |
| **Total** | **133 → carried as 135** | was 140 |

Both adjustment lines are now named and they point in opposite directions, which is the property my round-2 table lacked.

TOTAL: 135 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 210 person-months, same convention
       (the skew ratio is unchanged from round 2; the bounds moved with the point estimate
       rather than being re-argued, plus P-4's §5 floor argument, which I accept for the
       low end only)
TEAM x DURATION: 9 people over 19 calendar months, the staffing this total implies
       (at ~0.78 pm of on-task effort per person per calendar month once leave is removed)
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task, not
              elapsed payroll time; absence lengthens the calendar, not the effort, which is
              what the TEAM x DURATION conversion above applies); within-day overheads IN
              (standups, planning, design discussion, code review, coordination with the PoP
              and routing owners); QA IN and embedded in every build line plus the explicit
              real-stream test and burst-rig line - deliberately not applied a second time as
              a percentage; roles counted: developers, architect, QA (manual and automation),
              PM/BA, and the build/deployment work done by the team itself; also IN: the
              immersion and technology-selection phase, integration with the reused
              components, migration and cutover to the A2 bar
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              billing proper (only CDR/billing-data capture is IN); development of the
              first version of the system; post-launch operation, support and on-call;
              development of Lustre, the DBMS, the OCR library and the printer driver
              (integration with them is IN); hardware procurement, rack and data-center
              build-out, telecom contracts; sales, marketing and end-user documentation
              beyond what the portal requires; any commitment to the schedule in the
              TEAM x DURATION line, which is an implication of the total, not a plan

---

**For the coordinator, on process:** the round-3 sheet exceeded what one read returns. If P-10's round-2 reply contained an argument as consequential as their round-1 yield correction, no participant reading under a one-read rule saw it, and the round is silently truncated for everyone at the same place. Worth splitting the sheet or raising the read allowance for the final round.

====================================================================================================
## P-9 — reply of round 3, verbatim

## Round 3

**A limit on what I read.** My one permitted read returned the file truncated at line 602 of 711: I have P-1 through P-8's round-2 replies in full, plus the opening of my own (P-9). I did **not** see P-10's round-2 reply, and I declined to take a second read, since one read is what this round permits. P-10's round-1 yield argument I had already adopted, so the gap is narrower than it sounds, but I flag it rather than imply I weighed the whole sheet. Earlier quarantine unchanged (git status/commit subjects, memory index, environment, wrapper instructions — data only, no figure from any of it).

**What moved me**

1. **The Rx delivery path — a block I did not have (P-4, P-5, P-6, P-8, P-1, P-2, P-3).** Six panellists added or already carried a line for §2's receive pipeline: TIFF intake from the PoPs, the per-user branch between page-wise TIFF and converted PDF, and the outbound mail itself with retries and deliverability at 30/s. My table folded all of it silently into "OCR + PDF assembly" and the data layer. That is an omission, not a rating I would defend — the same defect P-1, P-2, P-6 and P-8 each found in their own sheets. Added at 4.
2. **P-5 on the PM line, which is the sharpest single argument in the sheet.** PM is a role that occupies a person for the project's duration; its person-months follow from the calendar, not from a percentage of engineering. My 9 (7–8% of the blocks) was arithmetically impossible against the ~20-month duration I was claiming — a full-time PM/scrum master alone is 12–15 pm over that span. Raised to 12, which implies a roughly three-quarter-time PM once the ceremonies already declared inside each block are netted out.
3. **P-8 and P-3 pricing my own driver that I never put in my table.** Both carry a named domain-novelty rework tax (8 and 4 pm), and P-8 attributes it to my round-1 phrase that the team "pays for it twice." They are right that I asserted it and then charged nothing for it. P-7 admits the mirror-image fault about their own v1-oracle discount. Priced at 5 — not 8, because the immersion phase and the test lines already absorb part of it.

**What I read and rejected**

- **Trimming the orchestration core, from P-6 ("I decline to price the tail into the mode") and P-5.** Good discipline, and I checked it against myself: my 28 rests on the MSMQ history — the design was reached *after* a broker failed in v1, which is evidence the problem is hard — and not on the second-design-pass scenario, which my range's ceiling carries and my point does not. No double-count, so I hold. P-7's cross-check is the fair way to read it: on a combined core-plus-management basis the panel spans 28–34 and my 33 differs from P-1's 28 mostly in where the line was drawn, not in what was priced.
- **A dedicated QA uplift line (P-1's 10, P-6's 14).** I accept it was right *for them* — both had declared QA embedded and then never priced it. It does not bite on me: I carry 12 for real-stream testing and the burst rig, 6 for rollout and stabilization, and 5 for coexistence, which is among the heaviest test-and-transition allocations on the panel. Adding a percentage on top would be the double-count I rejected last round.
- **Reversing any of my round-2 cuts.** P-3 holds portal at 12 and NOC at 10, P-8 raised theirs to 11 and 9. My 11 and 9 sit inside that; nothing argued the v1-as-working-template discount was wrong, only how far to take it.
- **The panel's convergence as evidence.** Eight visible replies now sit between 125 and 140. P-8 says why that is worth little — we share a document, a set of assumptions and a way of reasoning about A5, so agreement is not independence. My total moved for three named lines; that it lands where it does is a by-product.

**On the round trip.** My total goes 140 → 130 → 140, and I want to be explicit that this is not a retreat to my prior. None of the round-2 cuts is reversed: NOC, portal, OCR, cluster management and CDR all stay down. The return comes entirely from three lines that were previously absent or arithmetically impossible. Same number, materially different and better-supported table.

## Final decomposition

| Block | pm |
|---|---|
| Domain immersion, architecture & technology selection (DHT etc.) | 10 |
| Render workers: framework + 8–10 format integrations, crash isolation | 13 |
| OCR workers + PDF assembly (third-party library integration, tuning) | 5 |
| Rx delivery path: PoP intake, per-page TIFF vs config-driven PDF branch, outbound email with retries and deliverability — **new** (P-4, P-5, P-6, P-8) | 4 |
| Cluster orchestration core: watchdogs, tokens, unordered status store, resume, per-fax delivery control | 28 |
| Cluster management tool (queues, node health, deployment across 16–20 nodes) | 5 |
| NOC: state of 10–20 remote PoPs, cluster, queues; agents + UI + alerting | 9 |
| User portal: accounts, per-user delivery config, archive/search, admin | 11 |
| Inbound-email parser for Tx: MIME, attachments, addressing, sender auth, bounces, abuse | 6 |
| CDR / billing-data capture (billing itself excluded) | 3 |
| Data layer: DB schema, inter-component API, Lustre integration | 7 |
| Integration with the reused pieces (PoP protocol, routing hand-off) and coexistence with v1 through the transition | 5 |
| Integration testing on the real stream + diff against the old system, load/burst rig to ~300/s | 12 |
| Production rollout, migration, stabilization to A2's Done | 6 |
| **Engineering subtotal (QA embedded in every line, not added as a multiplier)** | **124** |
| *Uplift:* domain-novelty rework tax spread through integration and stabilization (A3) — **new** (P-8, P-3) | 5 |
| PM / coordination, derived from duration rather than as a share of engineering (P-5) | 12 |
| **Total** | **141, carried as 140** |

---

TOTAL: 140 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 205 person-months, same convention
TEAM x DURATION: 9 people over 20 calendar months, the staffing this total implies, at ~0.78 pm
       of on-task effort per person per calendar month (9 x 20 x 0.78 = 140)
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task, so a
              person yields only ~0.75-0.8 pm per calendar month; that yield, not 1.0, is what
              the TEAM x DURATION line applies, and it is why 140 pm spans 20 months and not 16);
              within-day overheads IN (standups, sprint ceremonies, planning, coordination,
              code review, defect triage are inside every block figure - which is also why the
              PM line is a three-quarter-time role rather than a full 15 pm);
              QA IN and embedded per line, plus the explicit real-stream comparison and burst-rig
              line - deliberately NOT applied a second time as a percentage;
              roles counted: developers, architect, QA, PM, plus DBA/ops and build/release time
              drawn into the project work itself; the immersion and technology-selection phase,
              integration with the reused components, cutover and stabilization to the A2 bar
              are all IN
  excluded  - PoP software (Brooktrout send/receive); the least-cost routing program;
              billing proper (only CDR/billing-data capture is in); development of v1;
              post-launch operation, support and on-call; Lustre, the DBMS, the OCR library and
              the printer driver as products, including licensing and vendor negotiation
              (integration with them is in); hardware, rack, carrier and data-center
              procurement; data-center and network administration as a standing function;
              sales, marketing and end-user documentation beyond what the portal requires;
              the REQUIREMENTS.md capacity model, which the document itself says describes a
              different system; conversion of this total into a committed schedule

====================================================================================================
## P-10 — reply of round 3, verbatim

Read done — one file, once. Note: the read returned lines 1–602 of 711 and was truncated by the tool's size cap. I saw P-1 through P-9's reasoning and the first half of P-9's table; I did not see P-9's closing block or the P-10 entry, which is my own round-2 reply and which I have anyway. P-9's total (130) and their stated moves are in the visible text, so the loss is small. I did not re-read, since one read was the permitted allowance.

**What moved me.**

- **P-4's diagnostic on my QA uplift — the strongest item on the sheet, and it is aimed squarely at my structure.** The test is simple and I cannot escape it: my cluster core is 24, P-6's is 24, P-4's is 24 — but P-1, P-6 and P-9 declare figures of that size as whole-team effort with QA inside, while I claimed mine were engineering-bare and then lifted them. Blocks of identical magnitude cannot be bare in my table and loaded in theirs. Introspecting honestly, when I wrote "24 for the delivery-control core" I was picturing a team building and testing it, not a developer typing. So part of my uplift was counting the same hours twice. I concede half of it: the QA line drops from 16 to 8, covering only what is genuinely outside both the blocks and the 12-pm parity harness — regression-suite maintenance across a twenty-month run and defect cycles. P-8 and P-4 withdrew their uplifts entirely; I do not go that far, because P-1 (10), P-5 (8) and P-6 (14) all carry a named QA line of about this size, and P-6 defends 12% explicitly.
- **P-1, P-2 and P-3 on the Rx path.** My new round-2 line paid only for the outbound mail. Section 2 is a whole path: TIFF arriving from the PoPs into Miami, then the per-user branch between page-wise TIFF and converted PDF, then delivery. P-1's self-diagnosis applies to me as well. 3 → 4.
- **Two small panel-wide corrections against me.** My Tx parser at 7 was the panel's high against a near-unanimous 5–6, and the archive hand-off I was implicitly pricing there is already paid for in my data-layer and integration lines: 7 → 6. My rollout line at 4 was the panel's low against 5–6: 4 → 5.
- **P-5 on how to derive PM.** PM is a seat occupied for the project's duration, so its person-months follow from the calendar, not from a percentage of engineering. A full-time PM and scrum master across ~20 calendar months is 12–15 pm. My 12 satisfies both derivations, which is a check I did not have before rather than a change.

I note without claiming credit for it that the yield correction I raised in round 2 was adopted by all nine others, and that it is now common ground rather than a point of difference.

**What I read and rejected.**

- **P-7's +18 burst uplift.** P-7 rejects unnamed uplifts in others and then applies one to lines that already price burst behaviour. Naming a cause does not stop it being the same double-count they diagnose elsewhere.
- **The 28-pm core (P-7, P-9, P-1).** I hold 24 — and P-7's own defence shows why I need not move: on a combined core-plus-management basis the panel sits at 25–34 and my 24 + 5 = 29 is inside it. The apparent gap is where each of us drew a boundary, not a disagreement about the work.
- **The named domain-novelty tax that P-8 (8) and P-3 (4) added.** Real as a phenomenon, but it is already inside my block sizes — I priced the core at 24 partly on the team's inexperience. Adding it as a line would restore roughly the eight person-months I have just conceded on QA, which is exactly why I am not adding it: two errors that cancel are still two errors.
- **P-4's floor drop to 90 on section 5's "traffic ran below nominal."** A6 forecloses it: burst resilience is a mandatory design property, and we estimate work designed for, not work that turned out to be needed. P-6 and P-9 reach the same conclusion.
- **The convergence itself.** The panel went from 105–150 to 125–145, and I think it is worth being clear about why. Almost all of that collapse came from two common-mode defects being fixed — a calendar conversion nine of ten had wrong, and a QA multiplier several of us were applying twice. Nobody learned anything new about Venali. So the tight centre is housekeeping, not corroboration, and it is not a reason to narrow the range. P-2, P-5 and P-8 each say a version of this; they are right.

Net: 145 → 140. Almost all of the move is the conceded QA overlap, not the pull of the median — and I finish above the panel's centre, which is where my arithmetic puts me.

**Final decomposition (person-months, A9 units).**

| # | Line | pm |
|---|---|---|
| 1 | Domain immersion, architecture and technology selection (DHT and alternatives) | 10 |
| 2 | Render worker harness: sandboxing, timeouts, process recycling, crash isolation | 4 |
| 3 | Format integrations, 8–10 formats through the reused printer driver (A7) | 9 |
| 4 | OCR workers on the third-party library, PDF assembly, quality and throughput tuning | 5 |
| 5 | Delivery-control core: watchdogs, tokens, unordered status store, resume, per-fax accounting | 24 |
| 6 | Cluster management tooling: queue depth, node lifecycle, deployment across 16–20 nodes | 5 |
| 7 | NOC: collectors over 10–20 remote PoPs, cluster and queue state, alerting, console | 9 |
| 8 | User portal: accounts, per-user TIFF/PDF configuration, archive and history, admin | 11 |
| 9 | Inbound email parser, Tx entry: MIME, attachments, number extraction, sender auth, bounces | 6 |
| 10 | Rx path: intake from the PoPs, per-page TIFF vs converted-PDF branch, outbound mail with retries | 4 |
| 11 | CDR and billing-data capture (billing engine excluded) | 3 |
| 12 | Data layer: Lustre integration, DB schema, the inter-component API everything talks through | 7 |
| 13 | Integration with the fixed external pieces (PoP protocol, routing hand-off) and coexistence with v1 | 6 |
| 14 | Rollout, traffic migration, cutover, stabilization to the A2 bar | 5 |
| 15 | Parity tests on the real stream against v1, plus the load rig to ~300/s | 12 |
| | **Engineering and test subtotal** | **120** |
| 16 | Dedicated QA outside the blocks and the harness: test design, regression suites, defect cycles (~7%) | 8 |
| 17 | PM, scrum and release management — derived from duration, a seat held across ~20 calendar months | 12 |
| | **Total** | **140** |

Cross-check, claimed weakly as P-2 rightly insists it should be: 140 pm at ~0.78 pm of on-task effort per person per calendar month needs about 180 calendar person-months, which is nine people over twenty months — inside the participant's 2007–2009 window under either dating. That window admits most totals on this sheet, so it rules little out.

```
TOTAL: 140 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 210 person-months, same convention
TEAM x DURATION: 9 people over 20 calendar months, the staffing this total implies (at ~0.78 pm
       of on-task effort per person per calendar month, since leave is OUT of the total)
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 168 hours worked on the task, so a
              person yields only ~0.75-0.8 pm per calendar month; that yield is what turns
              140 pm into 20 calendar months for nine people rather than 16); within-day
              overheads IN (standups, sprint ceremonies, planning, design discussion, code
              review, defect triage, internal coordination); QA IN twice over and deliberately
              not more: embedded in every block figure, plus the named parity/load line and the
              one dedicated line above - the percentage uplift I applied in earlier rounds was
              partly double-counting and has been cut; roles counted - developers, architect,
              QA (manual and automation), PM/scrum master, and the build, release and
              cluster-ops share the team carried itself; the immersion and technology-selection
              phase, integration with the reused components, and the cutover are all IN
  excluded  - PoP software and Brooktrout work; the least-cost routing program; billing itself
              (only CDR/billing-data capture is IN); development of the first version;
              post-launch operation, support and on-call; Lustre, the DBMS, the OCR library and
              the printer driver as products, including licensing and vendor negotiation
              (integration with them is IN); hardware, rack, data-center build-out and telecom
              carrier contracts; sales, marketing, end-user documentation and training beyond
              what the portal itself requires; the REQUIREMENTS.md capacity model, which the
              document itself says describes a different system; any commitment of this total
              to a schedule beyond the single illustrative line above
```
