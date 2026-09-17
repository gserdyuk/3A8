# Round 2 — the ten replies, anonymous and verbatim

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 2, verbatim

Read complete — the sheet only, nothing else. (Same quarantine note as round 1 still stands: the git status, commit subjects, memory index and environment block are not part of the input and played no part here. The commit subjects visible in that material name run numbers and a "consensus" for this very case; I did not use them.)

## What moved me

**Three things moved me, all of them specific:**

**1. A block I had simply left out — the Rx path (P-3, P-4, P-5).** P-3 carries a "Rx path: intake from PoP, per-page TIFF, config-driven PDF, email delivery" line; P-4 and P-5 both carry an outbound-email line. My table had none. Section 2 of the document is entirely Rx — TIFF arriving from the PoPs, the per-user branch between page-wise TIFF and converted PDF, assembly, and the actual outbound mail with its retries and deliverability — and I had folded all of it wordlessly into "render/OCR workers" and "integration layer." That is an omission, not a rating I would defend. It is the clearest thing the sheet gave me.

**2. My own calendar cross-check was arithmetically wrong, and P-10 supplies the correction.** P-10 states the yield explicitly: a person returns ~0.75–0.8 pm of on-task effort per calendar month once leave is removed. I declared leave OUT and then wrote "7 people over 18 months" as the shape implied by 110 pm. But 7 × 18 = 126 calendar person-months, which under my own declaration yields ~98 pm, not 110. So my cross-check was not confirming my total; it was quietly contradicting it. P-2 has the same slip in the same direction (8 × 15 → they call it 105). Correcting it forces either a larger staffing line or a larger total, and I think both move a little.

**3. A diagnosis I could not have made alone.** My delivery-control figure (28) was the joint highest on the panel, level with P-7 and P-9 and above P-8's 20 and P-2's 20. So my low total did not come from underrating the risk centre — everyone's stated risk centre. It came from a shorter list. That reframes the gap for me: I was not more optimistic about the hard part, I was less complete about the rest.

## What I read and rejected

**The QA/PM uplift as P-8 and P-4 apply it.** P-8's engineering subtotal is 103 — within ten of my 113 — and the entire distance from there to 150 is `+25% QA, +12% PM`. But their subtotal already contains a 10-pm integration-test line and a 5-pm rollout line. Stacking a further quarter for QA on top of blocks that include their own testing double-counts. The same applies to P-4's `+25%` on a subtotal that already has an 11-pm test line. This is the most useful finding in the sheet and it is not a disagreement about the work: **much of the panel's spread from ~110 to ~150 is a convention difference about whether QA and PM sit inside the block figures or on top of them, not a difference about what has to be built.** I reject the uplift as applied — but I concede the honest half of it, that my per-block figures were priced dev-flavoured, so I add one *named* line for QA capacity that is genuinely outside both the blocks and the harness, rather than a blind percentage.

**P-7's rounding from 128 to 140** for "the parts an inventory always misses." I reject an unexplained +12 in a point estimate; the named content behind it (a second pass on the token store after real traffic) belongs in the upper range, where I have put it.

**P-3's 150.** Their portal at 14 and NOC at 12 overlook that v1's equivalents exist as working visual specifications — A3's oracle argument, which P-3 themselves credit for analysis but not here. I hold 12 and 10.

## Final decomposition

| Block | pm | Status |
|---|---|---|
| Immersion, architecture, technology selection | 10 | hold |
| Rx path: PoP intake, per-page TIFF assembly, config-driven PDF branch, outbound email with retries | 6 | **new** (P-3, P-4, P-5) |
| Render workers, framework + 8–10 formats | 12 | hold |
| OCR workers on the third-party library | 4 | hold |
| Delivery-control core: watchdogs, tokens, unordered status store, resume, per-fax accounting | 23 | split out of my old 28 |
| Cluster management tool: queue depth, node lifecycle, deployment across 16–20 nodes | 5 | split out of my old 28 (8 of 9 panellists itemise it; §4 lists it separately) |
| NOC: collectors over 10–20 PoPs, cluster and queue state, alerting, console | 10 | hold |
| User portal: accounts, per-user TIFF/PDF config, archive and history, admin | 12 | hold |
| Inbound email parser, Tx entry: MIME, attachments, number extraction, bounces, abuse | 6 | hold |
| CDR and billing-data capture | 3 | hold |
| Integration fabric: DB and inter-component API, Lustre, PoP protocol, routing reuse, coexistence with v1 | 8 | hold |
| Integration tests on the real stream with v1 comparison, load work to nominal and burst | 10 | hold |
| Dedicated QA outside the blocks and the harness: test design, regression suites, defect cycles | 10 | **new** (the defensible part of P-8 / P-10) |
| PM, release engineering, cutover, decommissioning of v1 | 11 | 10 → 11, scaled to the larger base |
| **Total** | **130** | from 110 |

The move is +20, and every unit of it is a named line: 6 for the Rx path I had missed, 10 for QA I had assumed away, 1 of PM scaling, plus 3 in the split that I have re-absorbed rather than dropped. I did not move the delivery-control core, because nothing in the sheet argued against it and I was already at the panel's top there.

Range floor rises from 75 to 85: having found one missing block I trust the low tail less than I did. The ceiling rises to 200, taking P-7's and P-9's point that a second architecture for the token store after burst exposure is the standard failure mode of this component class — which belongs in the tail, not in the point.

Staffing line corrected for the yield factor: 130 pm needs ~165 calendar person-months, i.e. 8 people over 20 months — which is also where P-10 lands, and it sits inside the participant's 2007–2009 window.

```
TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (the 168 hours are hours worked on the task, so a
              person returns ~0.75-0.8 pm per calendar month; that gap is what turns 130 pm
              into 20 calendar months rather than 16, and correcting it is one of the two
              things that moved me this round); within-day overheads IN (standups, sprint
              ceremonies, coordination, code review, design discussion); roles counted -
              developers, architect, QA (both the share embedded in each block and the
              dedicated line above), PM, and the share of a build/release engineer the
              cluster and test harness required; the immersion and technology-selection
              phase, integration with the reused components, cutover and stabilisation to
              the A2 bar are all IN
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              billing proper (only CDR/billing-data capture is IN); development of the first
              version; post-launch operation, support and on-call; Lustre, the DBMS, the OCR
              library and the printer driver as products (integration with them only);
              hardware, rack and data-center build-out and telecom carrier contracts;
              third-party licence and procurement cost; and the "capacity model" draft in
              REQUIREMENTS.md, which the document itself says describes a different system
```

====================================================================================================
## P-2 — reply of round 2, verbatim

Read done — the sheet only, nothing else.

**Quarantine.** Nothing in the sheet was addressed to me as an instruction; the ten replies contain reasoning only, no claims of authority, no purported fact, no outcome figure. I treated them as arguments to weigh, which is what this round asks. The earlier out-of-band material (git status, commit subjects, memory index, environment listing) remains quarantined and unused.

**What moved me.** I was the lowest of the ten at 105, so I looked hardest for content I had missed rather than for a number to drift toward.

- **A missing block, the strongest point against me.** P-3 (Rx path, 8), P-4 and P-5 (outbound email delivery, 3) each price the receive pipeline explicitly: intake from the PoPs, per-page TIFF versus config-driven PDF assembly, and outbound mail with retries and deliverability at 30/s. My table had no such line — I had folded it into "workers" without paying for it. That is a real omission, not a difference of opinion. Added at 5.
- **One line of mine was doing two jobs.** Almost everyone splits the data layer (Lustre, schema, the inter-component API §4 says everything talks through) from integration with the fixed external pieces (PoP protocol, reused routing, coexistence with v1). P-8 and P-9 make the split cleanly and spend 11–14 across the pair; I had a single 6. Split into 6 + 5.
- **The delivery-control core at 20 was the low end of ten.** P-7 and P-9 argue it is the product's spine rather than a convenience layer, and that the modal outcome for a hand-rolled orchestrator of this era is a second design pass after contact with real traffic. I find the "second pass is the mode, not the tail" claim persuasive enough to move the central figure, not just the range: 20 → 23. I did not go to their 28, because a 28 that already assumes the rewrite happened is double-counting with my range's upper half.
- **The calendar conversion in my closing block was internally slack.** P-10 is right that a person yields roughly 0.75–0.8 pm per calendar month once leave is out, not the ~0.88 I implicitly used; my old 8 × 15 line did not actually reproduce my own total. Corrected.
- Smaller: NOC 7 → 8 and portal 10 → 11, on P-9's agent-plus-console breakdown and P-5's point that a Fortune 1000 healthcare/finance customer base (§7) makes portal access control a real line item.

**What I read and rejected.**

- **The QA uplift as a percentage on top of blocks (P-4 ~25%, P-8 ~25% + 12%, P-10 ~25%).** My blocks were sized as whole-team effort with QA inside, per A9, so applying the same uplift would double-count. I raised the dedicated test line by 1 instead. P-8 in particular adds the uplift to reach 140, then settles on 150 on qualitative grounds — an unexplained increment I will not copy.
- **P-3's NOC at 12 and portal at 14, and P-9's identical pair.** Both are internal or web surfaces with a live v1 sitting there as a working template; that is exactly where the v1-as-oracle discount should bite hardest, and neither reply applies it there.
- **The calendar cross-check as corroboration, which nine of ten used.** The 2007–2009 window plus a 6–10 person blended team admits roughly 75 to 240 pm — it is consistent with every number on this sheet, including the ones two-and-a-half times apart. P-1 concedes this ("weak evidence") and P-9's own arithmetic shows the band. I keep my cross-check but claim nothing from it.
- **P-1's parity-tail warning** (discrepancy investigation against v1 could absorb another 30–40 pm) I accept as a range argument only; A2 makes agreement the Definition of Done, but there is nothing in the document saying the diff went badly.

**Final decomposition.**

| Block | pm |
|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), ~1.5 calendar months with a largely assembled team | 10 |
| Render workers: worker harness plus 8–10 format integrations, each its own stabilization job (A7); unattended printer-driver automation is the cost | 13 |
| OCR workers on the third-party library: integration, PDF assembly, throughput tuning | 4 |
| Rx path: intake from the PoPs, per-page TIFF vs config-driven PDF, outbound email delivery with retries at 30/s | 5 |
| Delivery-control core: watchdogs, tokens, the unordered status store, per-fax resume and idempotency, burst behaviour — MSMQ excluded by A5 | 23 |
| Cluster management tool: queue depth, node lifecycle, deployment across 16–20 nodes | 5 |
| NOC: collectors on 10–20 remote PoPs plus cluster and queue state, alerting, operator console | 8 |
| User portal: accounts, per-user TIFF/PDF configuration, archive and search, admin, enterprise access control | 11 |
| Inbound email parser (Tx): MIME, attachments, number extraction, sender auth, bounces, abuse | 5 |
| CDR and billing-data capture (billing engine excluded) | 3 |
| Data layer: Lustre integration, DB schema, the inter-component API everything talks through | 6 |
| Integration with the fixed external pieces: PoP protocol, reused least-cost routing, coexistence with v1 through the transition | 5 |
| Integration and load testing on the real stream, diff against the old system, burst rig to ~300/s | 11 |
| Production rollout, traffic migration, stabilization to the A2 bar | 5 |
| PM, tech lead and release coordination not already inside the blocks | 12 |
| **Total** | **126 → carried as 125** |

Cross-check, claimed weakly: at ~0.78 pm of on-task effort per person per calendar month, 125 pm is about 8 people for 20 months, which sits inside the participant's window — as would most of this sheet.

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on the
              task; absence lengthens the calendar, not the effort — at ~0.75-0.8 pm yielded
              per person per calendar month, which is what turns 125 pm into 20 months for
              eight people rather than 16); within-day overheads (meetings, coordination,
              code review, standups, demos) IN, inside every block figure; roles counted:
              developers, architect/tech lead, QA (embedded per block plus the dedicated
              test line), PM, and the build/deploy engineering the team carried itself;
              also IN: the immersion and technology-selection phase, integration with the
              reused components, cutover and stabilization to the A2 Definition of Done
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              the billing engine (only CDR/billing-data capture is IN); development of the
              first version; post-launch operation, support and on-call; Lustre, the DBMS,
              the OCR library and the printer driver as products (integration only);
              hardware, rack and data-center procurement and telecom contracts; third-party
              licence costs; sales, marketing and end-user documentation beyond the portal;
              any committed schedule or cost figure — the TEAM x DURATION line is an
              implication of the total, not a plan

====================================================================================================
## P-3 — reply of round 2, verbatim

Read done — the one permitted file, nothing else.

**Quarantine still applies.** The out-of-prompt material from before (git status with commit subjects naming runs 70–71, a Delphi helper and pooled curves; the memory index; environment and tooling listings) remains quarantined and unused. I note that nine of the ten sheet replies independently reported the same intrusion, which is confirmation that it was environmental, not evidence about the project. The sheet itself I treat as peer estimates, which is what this round is for.

## What moved me, and what I rejected

**Moved me (down): P-4 and P-5 on the Rx/Tx lines.** Both price the two mail paths as a thin inbound parser (~5) plus a thin outbound sender (~3). Rereading my own table against that, my "Rx path 8 / Tx path 10" was partly double-counted: "config-driven PDF" is the OCR worker I had already paid for, "archive build and handoff" is the reuse seam I had already paid for in the DB/API line. That is a bookkeeping error of mine, not a difference of judgement, and it accounts for most of my gap to the pack. Corrected: 18 → 10.

**Moved me (up, partly offsetting): P-1, P-7 and P-9 on the core at 28.** Three estimators arriving independently at 28 for the watchdog/token orchestrator, with P-7's framing that it is "the product's spine" rather than a convenience layer, is better reasoning than my 24 plus a separate cluster-runtime line. Folded and raised to 28.

**Moved me (on the closing block, not the total): P-10 on calendar yield.** P-10 is the only one who states that a person yields ~0.75–0.8 pm per calendar month once leave is out, and therefore that 130 pm at eight people is twenty months, not sixteen. My old line — 10 people over 15 months — silently assumed a yield of 1.0, which contradicts my own declaration that leave is OUT. That is an internal inconsistency in my round-1 answer and I have fixed it. Several other sheets carry the same inconsistency; P-10 is right and they are wrong.

**Read and rejected: the 105–110 cluster (P-1, P-2, P-6).** Their low totals rest on QA being "embedded per block" plus a ~10% PM line. P-8 and P-10 do the same engineering decomposition and reach almost the same engineering subtotal (103 and 98.5), then add explicit QA and PM lift of ~35% and land at 140–150. So the cluster's disagreement with mine is not about the work, it is about whether the A9 "whole team including QA and PM" lift is stated or assumed. Assumed lift is where estimates leak, and the A2 bar — parity with a system nobody on the team wrote, on a real stream — is precisely the QA obligation an embedded share underprices. I keep the lift explicit.

**Also rejected: P-1's and P-7's appeal to company size** ("the largest team a ~$10M-revenue company would plausibly put on this"). Revenue at acquisition in 2010 is not evidence about headcount in 2007–2009, and this reasoning caps the estimate from outside the scope rather than from the work. It is a ceiling with no mechanism behind it.

Net: 150 → **140**. I moved for the double-count, which is a real defect; I did not move for the pack's centre of gravity, and I remain at the top of the distribution deliberately.

## Full decomposition

| Block | pm |
|---|---|
| Domain immersion + architecture/technology selection (DHT and alternatives, A1/A3) | 12 |
| Render worker framework + 8–10 format integrations (A7, each its own stabilization) | 15 |
| OCR workers on the third-party library (TIFF→PDF, throughput tuning) | 5 |
| Delivery-control core + cluster runtime: watchdogs, tokens, unordered status store, per-fax resume, idempotency, burst behaviour | 28 |
| Cluster management tool (queue depth, node lifecycle, deployment across 16–20 nodes) | 6 |
| Rx path: intake from PoP, outbound email delivery of received faxes, retries | 4 |
| Tx path: inbound-email parser, MIME/attachments, number extraction, sender auth, NDRs | 6 |
| NOC: agents and console over 10–20 remote PoPs, cluster, queues, alerting | 10 |
| User portal: accounts, per-user TIFF/PDF configuration, archive, history, admin | 12 |
| CDR / billing-data capture (billing engine excluded) | 3 |
| DB schema + inter-component API + Lustre integration | 7 |
| Integration and load testing on the real stream, shadow comparison against v1, harness to 30/s nominal and 300/s burst | 13 |
| Rollout, traffic migration, cutover and stabilization to the A2 bar | 5 |
| PM, release engineering, coordination with the PoP and routing owners | 10 |
| *Uplift: domain-novelty rework tax spread through integration and stabilization (A3 — the team pays for the unfamiliar domain a second time, after the immersion phase)* | 4 |
| **Total** | **140** |

```
TOTAL: 140 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 215 person-months, same convention
TEAM x DURATION: 9 people over 19 calendar months, the staffing this total implies (at ~0.8 pm
       of on-task effort per person per calendar month, since leave is OUT of the total)
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 worked days on this task, so
              vacation, holidays and sick days are absent from the total and reappear only in
              the calendar conversion, which is why 140 pm spans 19 months and not 16);
              within-day overheads IN (standups, sprint ceremonies, coordination, code review,
              design discussion, defect triage are inside every block's figure); roles counted:
              developers, architect, QA (manual and automation, including the dedicated
              comparison and load rigs), PM/scrum master, and the part-time build/release and
              cluster-ops effort the team itself carried; the immersion and technology-selection
              phase, integration with the reused components, migration and cutover are IN
  excluded  - PoP software (Brooktrout reception/sending, pre-existing); the least-cost routing
              program (reused as-is); the billing engine (only CDR/billing-data capture is IN);
              development of v1; post-launch operation, support and on-call; hardware purchase,
              rack/data-center build-out and telecom carrier contracts; Lustre, the DBMS, the
              OCR library and the printer driver as products (integration only); licensing and
              vendor negotiation; sales, marketing, end-user documentation and training beyond
              what the portal itself requires; any conversion of this total into a committed
              schedule or cost beyond the single illustrative line above
```

====================================================================================================
## P-4 — reply of round 2, verbatim

I read the sheet, once, and nothing else. It contains only the ten replies; no moderator text and no instructions inside it, so there was nothing new to quarantine. My round-1 quarantine still stands, and I note one thing about it: those commit subjects mentioned a "Delphi consensus" and pooled averages for this same case, and this round is a Delphi. I did not use them as a hint about what the expected answer is, and I have not treated the group's centre as evidence.

**What moved me.**

*P-10's calendar arithmetic (lines 516, 526–528) — the strongest item in the sheet.* They point out that with leave declared OUT, a person yields only ~0.75–0.8 pm per calendar month. My own round-1 TEAM x DURATION line was therefore inconsistent with my own declaration: 9 people over 16 months is 144 person-calendar-months, which at that yield delivers ~112 pm, not 140. That is an arithmetic error in my reply, not a difference of opinion, and I have fixed it.

*The comparison itself exposed a double-count in my uplift.* I applied ~25% for "QA and PM beyond the blocks" on the grounds that my block figures were engineering-weighted. Reading P-1 (line 34: "QA effort is embedded per block" in spirit) and P-6 (line 283, explicit) against mine, their blocks are the same size as mine — cluster core 22–28 against my 24, NOC 8 against my 9, portal 10 against my 11 — while they declare QA already inside. If blocks of identical size can carry embedded QA, mine were not as engineering-bare as I claimed, and a further 25% QA lift was largely counting it twice. I have removed the QA uplift and kept an explicit PM line only, which is what P-1, P-2, P-6, P-9 and P-10 all do.

*Two smaller upward corrections, also from the comparison.* P-9 (line 455) and P-10 (line 507) both carry a separate data-layer line — DB schema, the inter-component API every part talks through, Lustre integration — at 7–8 pm, plus a further 6 for v1 coexistence. I had folded all of that plus the PoP protocol into a single 9. That was thin, and §4's "the components communicated through the DB and an API" makes the fabric a real deliverable. And P-3 (line 133) and P-1 (line 42) both argue that parity against v1 on a real stream is an open-ended diff-investigation job; I found that persuasive enough to lift my test line from 11 to 13.

*On the floor.* P-1 (line 40) and P-6 (line 289) build their low end partly on §5's clarification that actual traffic ran below nominal, so the burst hardening may never have been engineered to the stated 300/s. I had A6 in mind and ignored §5 on this point. My floor drops from 100 to 90. I do not follow them to 70–80, because A6 makes burst resilience a mandatory property, not an option.

**What I read and rejected.**

I reject the per-format price of 1–1.5 pm used by P-2 (line 73), P-6, P-7 (line 331) and P-8 — a majority. A4 states the printer driver is reused; what the team pays per format is integration and fidelity stabilisation, not building a renderer. I keep ~0.7 per format and price the crash-isolation harness higher instead, landing at the same 12, so this changes my reasoning rather than my number.

I reject P-3's 150 and P-8's 150. P-3's portal at 14 and NOC at 12 outrun what a v1 already sets a bar for. P-8's route to 150 is the same QA-plus-PM uplift I have just concluded was double-counting in my own sheet, followed by a discretionary bump above their own arithmetic (line 401: 140 computed, 150 declared) that I could not find a reason for.

I reject the 20 pm orchestrator core of P-2 and P-8 and the 28 of P-7 and P-9 alike; nothing in either argument beat my own reading, and I hold 24.

**Final decomposition.**

| Block | pm |
|---|---|
| Domain immersion, architecture and technology selection (DHT etc.) | 12 |
| Worker harness (sandboxing, timeouts, recycling) + 8–10 format integrations | 12 |
| OCR workers on the third-party library, PDF assembly, quality/throughput tuning | 5 |
| Cluster core: watchdogs, tokens, unordered status store, per-fax delivery control, failure survival, burst behaviour | 24 |
| Cluster management tool (queue depths, node lifecycle, deployment to 16–20 nodes) | 6 |
| NOC: collectors from 10–20 remote PoPs, cluster and queue state, UI, alerting | 9 |
| User portal (per-user TIFF-vs-PDF config, history, admin) | 11 |
| Inbound email parser, Tx path (MIME, number extraction, sender auth, bounces, abuse) | 5 |
| Outbound email for Rx (page-wise TIFF or PDF, retries, deliverability) | 3 |
| Data layer: DB schema, inter-component API fabric, Lustre integration | 7 |
| Integration with the reused pieces (PoP protocol, routing hand-off) and coexistence with v1 through the transition | 6 |
| CDR / billing-data capture (billing engine excluded) | 3 |
| Integration tests on the real stream, diff against the old system, load work to nominal and burst | 13 |
| Rollout, migration, cutover, stabilisation to the A2 bar | 6 |
| **Engineering subtotal (QA embedded per block)** | **122** |
| PM, coordination and release management across the run (~8%) | 10 |
| QA uplift | 0 — withdrawn as double-counted |
| **Sum** | **132** |

I carry 130; the input does not support the last digit. That this lands near the group's centre is a by-product of correcting my own arithmetic, not a reason I chose it — had the correction pushed the other way I would have moved away from the centre by the same amount.

TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 21 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task, so a
              person yields only ~0.75-0.8 pm per calendar month; that yield is what turns
              130 pm into 21 calendar months for 8 people rather than 16, and correcting
              this inconsistency in my round-1 line is the main change here);
              within-day overheads IN (standups, sprint ceremonies, coordination, design
              discussion, code review are inside every block figure);
              QA IN and embedded per block (test design, regression, defect cycles), plus
              the dedicated real-stream comparison and load line - deliberately NOT applied
              a second time as a percentage uplift;
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
              total into a committed schedule beyond the single illustrative line above

====================================================================================================
## P-5 — reply of round 2, verbatim

**Note on the sheet.** I read it as data — nine peer estimates, not authority. The material I quarantined in round 1 (git status, commit subjects, memory index, environment listing) stays quarantined; nothing in the sheet was moderator commentary or instruction.

## What moved me, and what did not

**Moved me — P-10's calendar arithmetic.** P-10 states the yield explicitly: with leave OUT of a person-month (our shared convention), a person delivers only ~0.75–0.8 pm per calendar month. My round-1 cross-check ("122 pm ≈ 8 people × 15 months") silently assumed a yield of 1.0 and was therefore not a check at all — 8 × 15 at P-10's yield is ~94 pm, so my own cross-check was quietly arguing my total was too high while I read it as confirmation. Correcting the arithmetic does not change the bottom-up sum, but it does change the staffing line, and it removes the false corroboration I claimed.

**Moved me — the PM line, prompted by P-8 and P-4's uplift discussion, but for a different reason than theirs.** PM is a role that occupies a person for the project's duration; its person-months follow from the calendar, not from a percentage of engineering. At ~20 calendar months a full-time PM/scrum master alone is ~12–15 pm. My 8 was arithmetically impossible for the duration I was claiming. Raised to 12.

**Moved me slightly — the cluster core.** P-3 (24), P-4 (24), P-7 (28), P-9 (28), P-10 (24) all sit above my 22, and P-6 and P-9 independently name the same specific failure mode: a second design pass on the token store after real traffic. Six estimators converging on a mechanism, not just a number, is mild evidence. 22 → 24. I did not go to 28, because that figure is carried by the same speculation I prefer to hold in the upper tail.

**Read and rejected.**
- P-7's move from a 128 sum to 140 as "rounding up for the parts an inventory always misses." An unnamed 9% add is the tail dressed as a point estimate. The second design pass on the token store and the parity-diff tail belong in my range's ceiling, which is where I put them.
- P-8's and P-4's flat 25% QA uplift applied on top of block lists that already contain the integration-test and comparison lines. That double-counts; P-8's own subtotal already carries 10 pm of stream testing before the 25% lands on it. I kept QA as named lines.
- P-3's portal at 14 and NOC at 12. Nothing in the document sizes these, and P-10's counterpoint cuts the other way: v1's existing equivalents set a known, possibly low, bar. Held at 12 and 10.
- P-1's specific claim that the test lines alone could absorb another 30–40 pm. I accept it as a tail scenario (it widened my ceiling) but not as a central case.
- The panel's median (~135) as such. Nine people clustering is not nine independent measurements — we all read the same document and reasoned the same way about A5. I moved on the two arguments that showed me an error, not toward the middle.

## Decomposition

| Block | pm |
|---|---|
| Domain immersion, architecture and technology selection (~1.5 cal. months, blended team) | 10 |
| Render worker framework + 8–10 formats (each a separate integration/stabilization job, A7) | 13 |
| OCR workers on a third-party library (pipeline, TIFF→PDF, quality tuning) | 4 |
| Cluster core: watchdogs + tokens, unordered status store, per-fax delivery control, failure resume — the hand-built substitute for a broker (A5) — **raised from 22** | 24 |
| Cluster management tool (queue depth, node/job control over 16–20 nodes, deployment) | 6 |
| NOC: collectors and console for 10–20 PoPs, cluster, queues | 10 |
| User portal (config TIFF vs PDF, history, search, retrieval, enterprise-grade access control) | 12 |
| Inbound-email parser, Tx path (MIME, attachments, number extraction, sender auth, error mail) | 5 |
| Outbound email delivery of received faxes | 3 |
| CDR / billing data capture (billing itself excluded) | 3 |
| Lustre + DB schema + the inter-component API the parts talk through | 6 |
| Integration with the old system, coexistence during transition, real-stream comparison tests, rollout | 12 |
| QA beyond the above: test infrastructure, load to ~300/s burst, soak | 8 |
| PM / coordination — **raised from 8**, now derived from duration (a full-time PM/scrum master across ~20 calendar months) rather than as a share of engineering | 12 |
| Rounding to the resolution the input supports | +2 |
| **Total** | **130** |

Staffing now follows the corrected yield: 130 pm at ~0.8 pm per person per calendar month is 8 people over ~20 calendar months, which fits the participant's 2007–2009 window under either of the two datings they gave — this time as an actual check rather than an arithmetic slip.

TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h are hours actually worked on the task; a
              person therefore yields only ~0.75-0.8 pm per calendar month, and that gap is
              what turns 130 pm into 20 calendar months rather than 16);
              within-day overheads (meetings, coordination, code review, standups) IN;
              roles counted: developers, architect/tech lead, QA, PM, UI/web work
  excluded  - PoP software (Brooktrout send/receive), least-cost routing, the billing engine,
              development of v1, post-launch operation and support, hardware/rack/datacenter
              procurement and telecom contracts, third-party license costs, and any calendar
              conversion beyond the illustrative team x duration line above

====================================================================================================
## P-6 — reply of round 2, verbatim

**Read:** the Round 2 sheet, once. No other tool used. (The sheet's header calls these "round 1" replies; I read it as the same set the coordinator described.)

---

## What moved me, and what I rejected

**Moved me — three things, all of them defects in my own round-1 answer rather than differences of taste.**

1. **P-10's calendar arithmetic.** P-10 is the only one who noticed that if leave is OUT of a person-month (as every declaration on this panel says, mine included), then a person yields roughly 0.8 pm per calendar month, not 1.0. My cross-check — "6 over 18 is 108, 7 over 16 is 112" — silently used 1.0 and so contradicted my own DECLARATION. Repaired, that cross-check no longer confirms 110; for the remembered shape (a blended team of ~8 across a 2007–2009 window) it points at 130–160. This is the argument that did the most work on me, because it exposed an inconsistency rather than asking me to feel differently about a block.

2. **P-8 and P-10 on the QA lift.** I wrote "QA effort is embedded per block" and then never priced it — my block figures read as engineering figures, and my only dedicated QA was the 10 pm test line. P-5 carries a separate 8, P-10 adds ~25%, P-8 ~25%. Test design, regression suites and defect cycles across an eighteen-month rewrite are not inside a developer's estimate of "the NOC." I now carry an explicit line, though a smaller one than P-8/P-10 — see rejections.

3. **P-4 and P-5 on coverage.** Both carry an Rx outbound-delivery line (~3) that I had nowhere: §2.4 is a real deliverable — page-wise TIFF or PDF attachment, retries, deliverability. And five participants (P-2, P-4, P-7, P-8, P-9) split rollout/migration/cutover out of the test line; I had bundled it and thereby under-drew it. Both are genuine gaps, not re-labelling.

I also moved the orchestration core from 22 to 24. P-1, P-7 and P-9 all put it at 28 on the argument that this class of hand-built system needs a second design pass after production exposure. I find the pattern real but decline to price the tail into the mode — that scenario is what my upper bound is for. Two points is what I think the argument is worth at the centre.

**Read and rejected.**

- **P-8's final step.** 103 subtotal, +25% QA, +12% PM gives 140; P-8 then writes 150 because the burst requirement "justifies sitting slightly above." That last ten has no content — it is a rounding in the direction of the scariest risk, which the range already carries. Also, a flat 25% dedicated QA on a subtotal that P-8 says already contains embedded testing double-counts; that is why my own lift is ~12%, not 25%.
- **P-4's and P-7's unnamed uplift** (116→145, 128→140, "the parts an inventory always misses"). I accept that inventories miss things; I do not accept an uplift that cannot be pointed at. Where I agreed something was missing I added a named line instead.
- **P-3's block levels** — portal 14, NOC 12, render 17, sum 153. P-3 credits the live v1 as a reduction "in analysis and rework, not in build," which I think under-uses it: for a portal and a NOC, a running predecessor fixes the feature set and the screens, which *is* a build discount. P-3's 150 is the panel's top and it gets there by being the highest on nearly every line at once, which reads as a systematic level shift rather than a set of independent judgements.
- **The one downward argument nobody pressed** — §5's "actual traffic was even below the nominal." I considered cutting the burst-engineering share and rejected it: A6 makes burst resilience a mandatory design property, and the estimate is of work done, not of work that turned out to be needed.

I am not moving to the panel median (~137) because it is the median. I am moving because fixing my calendar cross-check, pricing the QA I claimed was already there, and adding two deliverables I had omitted lands me at 135 on my own arithmetic. That it sits near the others is a consequence, not the reason.

---

## Final decomposition (every line)

| Block | pm | Change from R1 |
|---|---|---|
| Domain immersion, architecture, technology selection (DHT etc.) | 10 | hold |
| Cluster + delivery control: watchdogs, tokens, unordered status store, resume, per-fax accounting | 24 | 22 → 24 |
| Cluster management / node lifecycle, queue-depth control, deployment to 16–20 nodes | 5 | hold |
| Rendering workers: harness + 8–10 formats via printer driver | 13 | hold |
| OCR workers on the third-party library, PDF assembly, throughput tuning | 4 | hold |
| Rx outbound path: page-wise TIFF or converted PDF to email, retries, deliverability | 3 | **new line** |
| Inbound-email parser (Tx): MIME, attachments, number extraction, sender auth, bounces | 5 | hold |
| User portal: accounts, per-user TIFF/PDF config, archive and history, admin | 10 | hold |
| NOC: collectors over 10–20 PoPs, cluster and queue state, alerting, console | 8 | hold |
| DB schema + inter-component API fabric + Lustre integration | 6 | hold |
| CDR / billing-data capture (engine excluded) | 3 | hold |
| Integration with the reused pieces (PoP protocol, routing hand-off) and coexistence with v1 through the transition | 5 | **split out of the old test line** |
| Integration testing on the real stream, diff against the old system, load rig to nominal and burst | 11 | 10 → 11, cutover removed |
| Production rollout, traffic migration, cutover, stabilisation to the A2 bar | 5 | **split out** |
| **Engineering subtotal** | **112** | was 96 |
| Dedicated QA beyond the embedded share and the test line: test design, regression suites, defect cycles across the run (~12%) | 14 | **new uplift line** |
| PM, coordination, release management (~10%) | 12 | hold |
| **Total** | **138 → carried as 135** | was 110 |

---

TOTAL: 135 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies
       (at ~0.85 pm of on-task effort per person per calendar month once leave is removed —
       the conversion my round-1 line got wrong)
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, so a person
              yields roughly 0.85 pm per calendar month and the shortfall lands in the
              calendar, not in the effort); within-day overheads IN (standups, sprint
              ceremonies, planning, coordination, code review, design discussion);
              roles counted: architect, developers, QA (embedded, plus the dedicated line
              above), PM/scrum master, and the part-time build/release and cluster-ops
              share the team carried itself. Also IN: the domain-immersion and
              technology-selection phase, integration with the reused components,
              real-stream testing against the old system, and the production cutover.
  excluded  - PoP software and Brooktrout work; the least-cost routing program; the billing
              engine (only CDR/billing-data capture is in); development of the first version;
              post-launch operation, support and on-call; Lustre, the DBMS, the OCR library
              and the printer driver as products (integration only); hardware, rack,
              data-center and telecom procurement; third-party licence cost; the
              REQUIREMENTS.md capacity model, which the document itself says describes a
              different system; any calendar commitment (the TEAM x DURATION line is an
              implication of the total, not a schedule).

====================================================================================================
## P-7 — reply of round 2, verbatim

I read the sheet. I am P-7; the panel runs 105, 110, 110, 120, 130, 140, 140, 140, 150, 150.

**What moved me.**

P-10's calendar arithmetic. They are the only one who converts properly: a person yields ~0.75–0.8 pm of on-task effort per calendar month once leave is stripped out, because A9 defines a pm as 168 hours *worked*. My round-1 cross-check ("140 pm is roughly eight people for a year and a half") silently used 1.0, and that cross-check was the stated reason I did not push higher. Corrected, 140 pm at eight people is about 22 calendar months — still inside 2007–2009, so the check no longer pulls down on my number. I have fixed the TEAM x DURATION line accordingly.

P-9's pricing of v1-as-oracle as an explicit 15–20% discount, and P-4's related point that the reused pieces are genuinely large parts of a fax system the team never pays for. I had this in my prose and nowhere in my table — a 12 pm round-up "for parts an inventory always misses" with no offsetting line is one-sided bookkeeping. I have now split that into a named uplift and a named discount, which is why my total is unchanged but the table is not.

**What I read and rejected.**

The low cluster — P-2 at 105, P-1 and P-6 at 110 — because their top-down confirmations reproduce exactly the error P-10 identified. P-6 writes "a team of 6 over 18 months is 108 pm"; at 0.75–0.8 that shape yields 81–86 pm. P-2 writes "~8 people for ~15 calendar months is ~105 pm"; it is nearer 90–96. Their bottom-up figures may stand on their own, but the cross-checks that ratify them are too generous by a fifth, so I give the convergence of three participants near 108 much less weight than its apparent unanimity deserves.

P-8's 150, as constructed rather than as a level: a 103 subtotal that already contains a 10 pm integration-test line, then +25% for "dedicated QA beyond the integration harness", then an unexplained bump from 140 to 150. The QA uplift partly re-counts the line beneath it.

I also checked whether my 28 for the delivery-control core is the outlier it looks like next to P-2's and P-8's 20. It is not: on a combined cluster-core-plus-management basis the panel sits at 25–34 (P-1 28, P-3 34, me 33), and the single-line spread is mostly where each participant drew the boundary. So I saw no reason to cut it.

I hold at 140.

| Line | pm |
|---|---|
| Domain immersion, architecture and technology selection (DHT etc.) | 12 |
| Cluster + delivery control: watchdogs, tokens, unordered status store, recovery, the orchestrator proper | 28 |
| Cluster management (queue depth, node health, work distribution) | 5 |
| Rendering workers: harness plus 8–10 formats, each its own integration and stabilization job | 15 |
| OCR workers, third-party library integration, PDF assembly and tuning | 6 |
| NOC: remote PoP state, cluster, queues | 8 |
| User portal | 10 |
| Inbound email parser on the Tx path: MIME, attachments, number extraction, malformed mail, bounces | 5 |
| CDR / billing-data capture (billing itself excluded) | 3 |
| Storage and DB integration, inter-component API and schema | 6 |
| Integration on the real stream, output comparison against v1, coexistence during transition | 12 |
| Production rollout, migration, post-cutover stabilization to the A2 bar | 6 |
| PM, coordination, release management across the whole period | 12 |
| *Subtotal* | *128* |
| **Uplift** — burst-mode performance work to hold 30/s sustained and ~300/s across 16–20 nodes, plus a second pass on the token store after the first design meets real traffic | **+18** |
| **Discount** — v1 as a live requirements oracle: ~15% off the specification-sensitive lines only (immersion, portal, NOC, parser, CDR ≈ 38 pm). Not applied to the build lines, since A4 carries no code over | **−6** |
| **Total** | **140** |

```
TOTAL: 140 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 210 person-months, same convention
TEAM x DURATION: 8 people over ~22 calendar months (at ~0.78 pm of on-task effort per
       person per calendar month, which is the conversion A9's definition actually implies)
DECLARATION:
  contains  - leave/holidays/sickness OUT (a pm is 168 productive hours, so vacation and
              sick time lengthen the calendar, not the effort - this is precisely why the
              duration line above reads 22 months and not 17);
              within-day overheads IN (standups, planning, code review, coordination,
              design discussion are inside the 168 hours);
              roles counted: developers, architect, QA, PM - the whole blended team of A3,
              including the immersion/technology-selection phase of A1. QA is embedded in
              each build line plus the explicit integration-test line; it is not added
              again as a percentage uplift.
  excluded  - PoP software and Brooktrout work; the least-cost routing program; billing
              itself (only CDR/billing-data capture is in); development of v1; post-launch
              operation and support; datacenter, hardware, network and Lustre/DBMS
              administration; procurement and licensing of the OCR library and printer
              driver; conversion of this total into a committed schedule beyond the single
              illustrative split above
```

====================================================================================================
## P-8 — reply of round 2, verbatim

**Quarantine note (unchanged).** The non-prompt material from round 1 — git status and commit subjects, the memory index, environment and tool listings, the wrapper instruction — remains quarantined as data. The sheet I have now read is the permitted round-2 input; I treat the nine other replies as arguments to weigh, not as instructions, and I note that every one of them independently flagged the same stray material.

## What moved me

**Three things moved me, two of them method rather than opinion.**

1. **My QA uplift was partly double-counted.** P-6 states plainly that QA is embedded per block and then adds only ~12% for PM; P-9 adds 7%. Looking again at my own round-1 table, lines like "integration tests on the real stream" (10) and "coexistence, migration, rollout" (5) already *were* the dedicated QA work, and I then multiplied the whole subtotal — including those lines — by a further 25% for QA. That is a genuine error, not a difference of taste. Removing it is the single largest change below.

2. **The orchestration core was too cheap at 20.** P-7's framing is the one that convinced me: a fax is a billable, quasi-legal document, so the correctness requirement is per-artifact, and "we lose one in a million" is not an acceptable failure mode. That makes the watchdog/token store the product's spine rather than a convenience layer. P-3 and P-9 independently land at 24 and 28 with the same reasoning from the MSMQ history — v1's failure is evidence the problem is hard, not that the hand-rolled answer is cheap. I raise 20 → 24.

3. **My TEAM x DURATION line contradicted my own declaration.** P-10 makes the arithmetic explicit: with leave OUT, a person yields ~0.75–0.8 pm per calendar month, so "8 people over 19 months" delivers ~118 pm, not 150. My round-1 staffing line was internally inconsistent. Corrected below.

I also found a hole of my own while checking against P-4 and P-5: neither my table nor my exclusions had a line for the **Rx delivery path** — page-wise TIFF versus converted PDF, the outbound mail, retries and deliverability. Both of them carry it at ~3. It was silently folded into "workers" in my round 1; it is now explicit.

## What I read and rejected

- **The low cluster (P-2 at 105, P-1 and P-6 at 110).** Their common move is a large v1-as-oracle discount plus thin NOC and portal lines. I accept the discount on *requirements*, not on *build* — A4 says no code carries over. More concretely, P-6's subtotal of 96 has no separate load rig anywhere, and A6 is explicit that burst resilience at ~300/s is a mandatory property rather than an option. Proving that on owned 2008 hardware is its own instrumented work, not a week of tuning.
- **P-3's staffing shape (10 people over 15 months).** The total is close to mine, but P-3's own sentence concedes the point against it — "going much wider earlier would stall on the unfinished delivery-control core." Everything downstream waits on the core's interfaces, so this scope cannot absorb ten people early.
- **My own 240 ceiling.** It was the highest of the ten and I cannot defend the gap between it and the next (P-3's 230) with anything the document says. Pulled to 220, keeping the right skew.
- **Simple convergence on the median.** I note that 140 is the modal answer here (P-4, P-7, P-9) and that this is weak evidence at best — the ten of us share a training distribution and an anchor in the same document, so agreement is not independence. I move because the QA double-count is a real defect in my arithmetic; the destination being popular is a coincidence I am declining to treat as confirmation.

## Full decomposition

QA is now embedded inside every line, not applied as a multiplier on top.

| Line | pm | Change from R1 |
|---|---|---|
| Domain immersion + architecture/tech selection | 10 | — |
| Render worker framework + 8–10 format integrations | 13 | 12 → 13 (absorbs embedded QA) |
| OCR workers (library integration, TIFF→PDF, throughput) | 5 | 4 → 5 |
| Cluster + delivery control core (watchdogs, tokens, unordered store, resume, idempotency) | 24 | 20 → 24 (P-7, P-3, P-9) |
| Cluster management tool (queue depth, node lifecycle) | 5 | — |
| Rx delivery path (page-wise TIFF vs PDF, outbound mail, retries, deliverability) | 3 | **new line** (P-4, P-5) |
| NOC (agents on 10–20 PoPs, cluster and queue state, alerting, UI) | 9 | 8 → 9 |
| User portal (accounts, per-user delivery config, archive, admin) | 11 | 10 → 11 |
| Inbound email parser, Tx entry (MIME, attachments, number extraction, sender auth, bounces) | 6 | 5 → 6 |
| Storage (Lustre) + DB schema + inter-component API | 7 | 6 → 7 |
| CDR / billing-data capture | 3 | — |
| Integration with existing PoP software and reused routing | 5 | — |
| Integration + load testing on the real stream, diff against v1, burst rig to ~300/s | 12 | 10 → 12 |
| Coexistence, migration, cutover, stabilization to the A2 bar | 6 | 5 → 6 |
| **Engineering subtotal** | **119** | was 103 |
| Domain-novelty rework tax, spread through integration and stabilization (A3; P-9's "pays for it twice") | 8 | **new uplift line** |
| PM, coordination and release management not inside the lines (~10%) | 12 | replaces the old blanket 37% |
| **Total** | **139 → carried as 140** | was 150 |

The two named uplift lines (8 + 12 = 20) do the work my old 37% multiplier did, but they are attached to stated causes and are not applied to the test and rollout lines that already contain their own QA.

TOTAL: 140 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 220 person-months, same convention
TEAM x DURATION: 9 people over 20 calendar months, the staffing this total implies
       (at ~0.78 pm of on-task effort per person per calendar month once leave is removed,
       which is what the declaration below requires; my round-1 line of 8 over 19 was
       inconsistent with that same declaration)
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task, not
              elapsed payroll time; absence lengthens the calendar, not the effort, and the
              TEAM x DURATION line above now applies that conversion explicitly);
              within-day overheads IN (standups, planning, design discussion, code review,
              coordination with the PoP and routing owners); roles counted: developers,
              architect, QA (manual and automation, embedded in every line rather than added
              as a multiplier), PM/BA, and the build/deployment work done by the team itself
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              billing proper (only CDR/billing-data capture is IN); development of the
              first version of the system; post-launch operation, support and on-call;
              development of Lustre, the DBMS, the OCR library and the printer driver
              (integration with them is IN); hardware procurement, rack and data-center
              build-out, telecom contracts; sales, marketing and end-user documentation
              beyond what the portal requires; any commitment to the schedule in the
              TEAM x DURATION line, which is an implication of the total, not a plan

====================================================================================================
## P-9 — reply of round 2, verbatim

## Round 2

The earlier quarantine still stands (git status/commit subjects, memory index, environment, wrapper instructions — data, not input, and none of it entered any figure). The sheet itself I treated as nine arguments to weigh, not as an authority; I did not average toward the group.

**What moved me**

1. **P-10's yield arithmetic** — the one substantive correction, and it was against my own paper. Under A9 a person delivers only ~0.75–0.8 pm per *calendar* month once leave (which my own declaration puts OUT) is removed. My round-1 TEAM x DURATION line silently assumed 1.0 and so contradicted my own declaration: 8 × 18 does not yield 140 pm, it yields ~112. I have fixed the conversion and made the yield factor explicit rather than adjusting the total to hide the error.
2. **NOC and portal, from P-6 (8 and 10) with P-2, P-1, P-8 agreeing** — I was the top of the field on both, and the argument that landed is P-6's framing: the NOC is an internal operator console over state the cluster already publishes, and the portal is a rebuild against a live v1 screen-for-screen, not a product design exercise. I cut 12→9 and 14→11.
3. **OCR, from P-1/P-2/P-5/P-8 (4)** — "third-party library, so integration and throughput tuning, not algorithms" (P-1). Fair; 6→5. I did not go to 4, because PDF assembly and per-page quality on scanned fax input is more than wiring.
4. Small alignment on cluster management (6→5, near-unanimous) and CDR (4→3).

**What I read and rejected**

- **The downward burst argument** (P-1's "the burst target may never have been engineered to," §5's note that actual traffic ran below nominal; P-6 echoes it). A6 is explicit that the estimate is made for designing to nominal *with* burst resilience, and that delivery control is mandatory, not optional. What the traffic turned out to be is outcome knowledge; the scope is what was designed for. Rejected as a reason to cut.
- **Trimming the orchestration core toward P-2/P-8's 20.** Seven of ten sit at 20–24; I hold 28, alongside P-1 and P-7. The reason is in P-3's observation, which I think the low estimators under-weight: this design was reached *after* MSMQ failed in v1. That history is evidence the problem is hard, not that the bespoke answer was cheap. Note also that P-1's 28 folds the management tool in, so my core figure is the field's high mark on its own — deliberately.
- **P-8's and P-4's +25% QA uplift on top of the blocks.** Legitimate bookkeeping for their tables, which are engineering-weighted; wrong for mine, where every block is already whole-team effort per A9. Adopting it would double-count. My 130 is not a smaller scope than their 150 — it is the same scope with QA inside the lines.

Net: 140 → **130**. Roughly two-thirds of that move is the NOC/portal correction, one-third is OCR and the small trims; the yield fix changed the duration line, not the total.

## Final decomposition

| Block | pm |
|---|---|
| Domain immersion, architecture & technology selection (DHT etc.) | 10 |
| Render workers: framework + 8–10 format integrations, crash isolation | 13 |
| OCR workers + PDF assembly (third-party library integration, tuning) | 5 |
| Cluster orchestration core: watchdogs, tokens, unordered status store, resume, per-fax delivery control | 28 |
| Cluster management tool (queues, node health, control) | 5 |
| NOC: state of 10–20 remote PoPs, cluster, queues; agents + UI + alerting | 9 |
| User portal: accounts, per-user delivery config, archive/search, admin | 11 |
| Inbound-email parser for Tx: MIME, attachments, addressing, sender auth, bounces | 6 |
| CDR / billing-data capture (billing itself excluded) | 3 |
| Data layer: DB schema, inter-component API, Lustre integration | 7 |
| Integration with v1 and coexistence through the transition | 6 |
| Integration testing on the real stream + diff against the old system, load/burst testing | 12 |
| Production rollout, migration, stabilization to A2's Done | 6 |
| **Subtotal (QA embedded in every line)** | **121** |
| PM / coordination not already inside the blocks (~8%) | 9 |
| **Total** | **130** |

---

TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 195 person-months, same convention
TEAM x DURATION: 9 people over 18 calendar months, the staffing this total implies, at a yield
       of ~0.8 pm per person per calendar month (9 x 18 x 0.8 = 130)
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task; a person
              therefore yields ~0.75-0.8 pm per calendar month, and that factor - not 1.0 - is
              what the TEAM x DURATION line above uses); within-day overheads IN (standups,
              planning, coordination, code review, defect triage are inside every block figure);
              roles counted: developers, architect, QA, PM, plus DBA/ops time drawn into the
              project work itself. QA is embedded per block, not added as a separate uplift.
  excluded  - PoP software (Brooktrout send/receive); the least-cost routing program;
              billing proper (only CDR/billing-data capture is in); development of v1;
              post-launch operation and support; hardware, rack, carrier and third-party
              licence procurement; data-center and network administration as a standing
              function; conversion of this total into a committed schedule

====================================================================================================
## P-10 — reply of round 2, verbatim

Read done: the one permitted file, nothing else.

**What moved me, and whose argument it was.**

Three specific things, all of them gaps in my own inventory rather than disagreements about difficulty:

- **A missing line: outbound email delivery on the Rx path.** P-4 and P-5 both carry it (~3 pm) and I did not. Section 2.4 says plainly that conversion *and sending* are the workers' job; SMTP delivery at 30/s with retries, deliverability and per-user TIFF-vs-PDF application is work I simply had not written down. **+3.**
- **A missing line: rollout and post-cutover stabilization.** P-7, P-8 and P-9 keep "integration with v1 / coexistence" and "rollout, migration, stabilization to the A2 bar" as two lines. I had one line of 6 doing both jobs. A2's Done is production traffic plus decommission readiness, which is not free once the diffing stops. **+4.**
- **The render-worker harness is a separate cost from the formats.** P-4 makes the cleanest case: Office automation on Windows is crash-prone, so the per-node job harness needs sandboxing, timeouts and process recycling before any format is priced. My single 11 was implicitly charging the harness to the formats. Split into 4 + 9. **+2.**

I also now make the real-stream parity test an explicit line instead of burying it inside a QA percentage — P-1, P-3, P-7 and P-9 all give it its own number, and A1 names it as scope, so it should be visible.

**What I read and rejected.**

- **The low cluster (P-2 at 105, P-1 and P-6 at 110).** The mechanism producing it is visible: they embed QA inside each block and then add only 10–12% for PM. Against a Definition of Done that is *results agree with the old system on a real production stream*, dedicated QA is a first-class cost line, not an embedded rounding. I keep QA as an explicit uplift.
- **P-8's final step.** Its own arithmetic gives ≈140 and it then writes 150 because of burst resilience — but the blocks it just summed already price burst resilience. An uplift for a factor already inside the blocks is a double charge, and I did not follow it.
- **P-3's 150 by a different route.** Internally consistent, but its portal (14), NOC (12) and test (16) lines all sit at the crowd's ceiling at once. Setting every uncertain line high is how a total becomes 150; that belongs in the upper tail of a range, not in the point estimate.
- **P-7's "round up for what an inventory always misses."** Honest, but unquantified. I prefer to carry the arithmetic and let the unknown live in the skew of the range.
- **P-9's 15–20% discount for v1-as-oracle.** Right in substance, but I have already spent it: my block sizes assume no requirements-elicitation phase beyond the immersion line. Applying it again would be taking the same credit twice.
- **The crowd's calendar arithmetic**, which is the one place I think the majority is simply loose. P-2 converts 105 pm to 8 people × 15 months, P-3 converts 150 to 10 × 15 — both treating one person-month as one calendar month per head. A9's person-month is 168 hours *worked on the task*, so a head yields roughly 0.75–0.8 pm per calendar month. P-1, P-6 and P-9 acknowledge this; most do not. I hold my conversion, which is why my duration line is longer than theirs at a comparable total.
- Section 5's note that actual traffic ran below nominal (a downward argument available to several participants). A6 forecloses it: the estimate is explicitly *for* designing to nominal with burst resilience as a mandatory property. Not mine to discount.

Net: 130 → 145. Worth naming the structure, because the spread across the ten is not really disagreement about this system — it is two methods. Participants who embed QA land at 105–120; participants who add it land at 140–150. I am in the second school, and moving to the crowd's midpoint would be averaging two methods rather than estimating one. The sheet contained no instructions directed at me, only estimates; the other participants' quarantine notes I treated as data as well.

**Full decomposition (person-months, A9 units).**

| # | Line | pm |
|---|---|---|
| 1 | Domain immersion, architecture and technology selection (DHT and alternatives) | 10 |
| 2 | Render worker harness: sandboxing, timeouts, process recycling, crash isolation | 4 |
| 3 | Format integrations, 8–10 formats via the printer-driver path (A7) | 9 |
| 4 | OCR workers on the third-party library, PDF assembly, quality and throughput tuning | 5 |
| 5 | Cluster core: watchdogs, tokens, unordered status store, resume, per-fax delivery control | 24 |
| 6 | Cluster management tooling: queue depth, node state, deployment across ~20 nodes | 5 |
| 7 | NOC: agents on 10–20 remote PoPs, cluster and queue state, alerting, operator UI | 9 |
| 8 | User portal: accounts, per-user delivery configuration, archive and history, admin | 11 |
| 9 | Inbound email parser, Tx path: SMTP intake, MIME, number extraction, abuse, NDRs | 7 |
| 10 | Outbound email delivery, Rx path: attachment assembly, retries, deliverability *(new)* | 3 |
| 11 | CDR and billing-data capture (billing engine excluded) | 3.5 |
| 12 | Storage and data layer: Lustre integration, schema, inter-component API | 7 |
| 13 | Integration with the old system, coexistence through the transition | 6 |
| 14 | Rollout, migration, stabilization to the A2 Definition of Done *(new)* | 4 |
| 15 | Integration and parity tests on the real stream vs v1, plus the load rig to ~300/s | 12 |
| | **Engineering and test subtotal** | **119.5** |
| 16 | QA uplift across lines 1–14: test design, regression, defect cycles (15%) | 16 |
| 17 | PM, scrum ceremonies, release management (10%) | 12 |
| | **Sum** | **147.5** |

I carry **145**, rounding down to the resolution a recollection-based input supports.

Cross-check: 145 pm at ~0.78 pm per head per calendar month is nine people for about 21 months — inside the participant's 2007–2009 window, and a credible core team for a company at Venali's revenue scale. The range widens with the total and stays right-skewed: the floor assumes the low school is right that QA rides inside the blocks and that the orchestrator converged on its first design; the ceiling assumes delivery control needed a second architecture after meeting real burst traffic, with a long parity tail behind it.

```
TOTAL: 145 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 220 person-months, same convention
TEAM x DURATION: 9 people over 21 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 168 hours worked on the task, so a
              head yields ~0.75-0.8 pm per calendar month; that gap is what turns 145 pm into
              21 calendar months rather than 16); within-day overheads IN (standups, planning,
              design discussion, code review, defect triage, internal coordination are counted
              as work on the task); roles counted - developers, architect, QA (test design,
              automation, regression), PM/scrum master, and the build and release work the team
              carried itself; the immersion and technology-selection phase, the parity testing,
              and the cutover are all IN
  excluded  - PoP software and Brooktrout work; the least-cost routing program; billing itself
              (only CDR/billing-data capture is in); development of the first version;
              post-launch operation, support and on-call; hardware, rack, data-center and
              telecom-carrier procurement; Lustre, the DBMS, the OCR library and the printer
              driver as products (integration with them only), including their licensing;
              end-user documentation, training and sales; and any commitment of this total to a
              schedule beyond the single illustrative TEAM x DURATION line above
```
