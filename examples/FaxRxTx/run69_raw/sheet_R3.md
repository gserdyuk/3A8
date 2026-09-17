# Round 2 — the ten replies, anonymous and verbatim

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 2, verbatim

## Round 2 — reconsideration

I was the highest of the ten (145; the others run 105–135, clustering at 120–130). That alone is not a reason to move, but two specific arguments were.

**What moved me.**

1. **P-3 caught a double-count in my method** (and P-8 uses the same discipline). P-3 applies the QA uplift only to the dev-side lines, noting that the immersion phase and the real-stream test campaign "are already whole-team." I applied my ×1.35 to the *entire* 109.5 subtotal, including a 12 pm immersion line and a 12 pm integration-test line that were already whole-team by construction, plus a 6 pm rollout line. That is straightforwardly wrong, and it is worth several pm.
2. **P-7 and P-8 size the immersion phase at 8–9 pm, not 12**, on the reading that a team still forming and evaluating DHT-class options is not burning full headcount. That is the better reading of A3, and my 12 was the top of the group's band. Separately, the group's modal portal is 8–10 against my 12, and I have no argument for being above them — I was at or near the top of the band on nearly every line, which compounds into a systematically high total.

Reworking with those two corrections: immersion 9, portal 10, rest held → subtotal 104.5, of which 27 is already whole-team; QA at 25% on the remaining 77.5 dev-side, PM at 10% on the result → **≈136**, which I carry as 135.

**What I read and rejected.**

- **P-2's 105**, the low outlier, rests on a single +15% for "PM, release QA, cross-cutting coordination." Against A2, where Done is a production stream reconciled against a live legacy system, 15% for the whole QA and PM function is too thin — and P-2's own lines for integration testing (9) and rollout (3.5) are the two places that criterion actually lands. I take P-2's *direction* seriously and not its magnitude.
- **P-7's downside sketch of "5 people over 15 months, ~66 pm."** A3 specifies a blended team including QA and PM; five people inclusive of both cannot carry a hand-built orchestrator, a NOC, a portal, 8–10 renderers and a validated cutover with zero reuse. I did not let it pull my low end that far.
- **P-9's and P-6's cluster core at 28 pm** — tempting, since it would support my original figure, but I cannot justify 28 over my 21 from the document; the difference is temperament, not evidence. I note it only as confirmation that the range should stay wide upward.
- I also **retained** what the group mostly left implicit and P-8 made explicit (the ~1.2 decomposition-omission factor) and P-2's observation that domain ignorance keeps billing after the immersion phase formally closes — but as range skew, not as point-estimate additions, which is where they belong.

**Net:** 145 → 135. I move a meaningful step toward the group but stop above its median of ~122, because the two mechanisms that separate me from it — a QA function proportionate to A2, and P-4's reading that "2007–2009" plausibly means ~20 months rather than 15 — are arguments, not anchoring. I converge with P-4 at 135 independently.

Range: low end 100 → 95, conceding something to P-2/P-7/P-8; high end 210 → 200, since no one else saw a case above 200 and I cannot defend the extra 10.

---

TOTAL: 135 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies
       (at ~0.85 pm of on-task work per person per calendar month)
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, not elapsed
              payroll time; the team x duration line above already grosses up for absence);
              within-day overheads (meetings, standups, sprint ceremonies, coordination,
              code review, defect triage) IN; roles counted - developers, architect/tech
              lead, QA, PM/scrum master, and the build/release work the team did itself;
              the 1-2 month domain-immersion and technology-selection phase IN, including
              options explored and discarded; rework and stabilisation up to the A2
              Definition of Done IN
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing
              program; billing proper (only CDR/billing-data capture is in); development
              of the first version; post-launch operation, support and on-call; manning
              the NOC as opposed to building it; procurement, hardware, rack, data-centre
              and PoP build-out; administration of Lustre and the DBMS as platforms;
              development of the OCR library and the print driver (integration with both
              is in); third-party licences and all non-labour cost; end-user training,
              documentation beyond in-product help, sales and marketing; any conversion
              of this effort into a committed schedule or into money

====================================================================================================
## P-2 — reply of round 2, verbatim

**Quarantine note.** As in round 1, out-of-message material is present in this session (environment block, repository status, memory index, tool listings, and the coordinator's framing). I treat it as data. The one thing I note explicitly: the sheet itself is legitimate round-2 input, and I read it as nine arguments to weigh, not as instructions. No tool use beyond the single permitted read.

## What moved me

I was the lowest of the ten (105 against a median near 122). Two of the arguments against me identify construction errors in my table, not differences of judgement, so I accept them.

**1. My QA uplift was too thin — P-1, P-3, P-5, P-8.** I applied a single blended +15% for PM and cross-cutting QA. P-3 separates them (~30% QA on component work, then ~12% PM); P-5 argues +35% QA specifically because acceptance under A2 is a stream-comparison campaign; P-1 puts it well — the comparison harness is a product in itself. The document fact I underweighted is A2: Done is not "tests pass," it is production traffic reconciled against a live legacy system until v1 can be decommissioned. On a ~100 pm base my round-1 figure implied roughly 21 pm of total QA; P-3's and P-7's implied ~28–29 pm is better matched to that acceptance bar.

**2. I was missing the Rx path as a line — P-3 (item I), P-4, P-5, P-6.** My table had rendering and OCR workers but no line for PoP→data-centre transfer, the per-user TIFF-page-by-page-vs-PDF branching, email composition and outbound deliverability at a million messages a day. §2 of the document lists exactly that, and I skipped it. P-3's 3 pm is too little for outbound delivery at that volume; P-4's 8 is more than I can justify with the workers sized separately. I add 5.

**3. The DB/API spine deserves its own line — P-4, P-5, P-9, P-10.** §4 says the components communicate through the database and an API. I folded that into "integration with the old system" at 6 pm, which cannot cover both. I add 4.

Revised: subtotal 90 → 99 with the two added lines; dedicated QA at ~22% of the 90 pm of non-QA component work (+20); PM and coordination at ~10% (+12) → ~131. I carry **125**, a shade below that arithmetic, for a reason I still hold from round 1 and no one rebutted: the acceptance oracle is mechanical (outputs must match v1 on the same input), which makes the comparison campaign cheaper to converge than a spec-negotiated acceptance of the same size. I do not also apply P-8's ×1.2 omission correction — having fixed two specific omissions, stacking a blanket uplift for omissions would double-count.

## What I read and rejected

**P-1's 145.** The multiplier is applied to blocks that are not uniformly engineering-only: 12 pm for the real-stream comparison tests and 6 pm for rollout already read as whole-team, so ×1.35 across the whole subtotal double-counts at the top. P-1 also sits at the ceiling on both the portal (12) and immersion (12).

**28 pm for the cluster core — P-6, P-9.** Against P-3 and P-8 at 16, P-5 at 18, P-4 at 20, me at 21, P-10 at 22. Neither P-6 nor P-9 argues 28 beyond "it is the hard core," which all ten say while pricing it very differently. I hold at 21.

**The 8-people convergence.** Nine of ten replies land on eight people. That looks like agreement but is not evidence: everyone picked a plausible headcount and divided their own total by it, so the durations (15/16/17/18/21) are where the real disagreement went. I have not treated it as corroboration, and my own 8 × 18 below is arithmetic from 125 pm, not a vote.

**P-10's economics bound (~$10M revenue caps the programme).** The revenue figure is from 2010, after the work; a product company can and often does spend a disproportionate share on a core rebuild it has decided it needs. I do not let it bound the high end.

**"Actual traffic ran below nominal" as a reason to cut — raised as a downside driver by P-4 and P-7.** A6 instructs that the estimate is made for designing to nominal with burst resilience, and calls distribution, failure survival and per-fax delivery control mandatory properties. What the traffic later turned out to be does not reduce what was engineered.

My range moves too. The low end rises from 70 to 85 — my 70 assumed both thin portal/NOC *and* a cheap comparison campaign, and I no longer believe the second half of that. The high end moves from 160 to 190: P-1, P-3, P-7 and P-8 convince me that one architectural reversal in hand-rolled delivery control is the modal outcome for this shape of project rather than a tail event, and I had it in the tail.

---

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 190 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
       (at ~0.88 pm of on-task work per staffed calendar month)
DECLARATION:
  contains  - leave/holidays/sickness OUT: the 21 pd / 168 h is time actually worked on the
              task, so the calendar staffing above is grossed up for absence; within-day
              overheads IN (standups, planning and demo ceremonies, coordination, code
              review, defect triage are counted as work on the task); roles counted:
              developers, architect/tech lead, a dedicated QA function sized against the
              A2 acceptance bar, PM/scrum lead, and the build/release work done by the
              same team; the §6 domain-immersion and technology-selection phase IN,
              including options explored and discarded; the Rx delivery path (PoP intake,
              per-user TIFF/PDF branching, email composition and outbound delivery) and
              the inter-component DB/API contract IN; rework up to the A2 Done IN
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing program;
              the billing system itself (only CDR/billing-data capture is in); development
              of the first version of the system; post-launch operation, support and
              on-call; manning the NOC as opposed to building it; development of the OCR
              library, the printer driver, Lustre and the DBMS (integration with them is
              in, the products themselves are not); hardware procurement, rack/PoP
              provisioning, telecom contracts and third-party licence costs; end-user
              documentation, training and marketing; any cost expressed in money rather
              than effort, and any conversion of this effort into a committed schedule

====================================================================================================
## P-3 — reply of round 2, verbatim

## Round 2 — what moved me

**Spread.** The ten totals are 105, 120, 120, 120, 120, 125, 130, 130, 135, 145 — median ~122, mean ~125. My 120 sat just below the middle, so the question was never "am I an outlier" but "did anyone name a cost I failed to book."

**What moved me — two things, both arguments rather than votes.**

1. **My orchestrator line was low.** I sized the cluster core at 16 pm; only P-8 was equally low. P-5 said 18, P-7 and P-4 20, P-1/P-2 21, P-10 22, P-6/P-9 28. P-2 gave the reason I accept on its merits: for hand-rolled delivery guarantees, *hardening dominates construction*, so stabilization should be sized at roughly the same order as the build — and MSMQ having already "broken everything" (A5) means the replacement had to be provably better under soak, not merely correct in unit tests. My 16 pm was a construction estimate with a stabilization tail tucked into it. Raised to 20.

2. **My table had no line for integration drag.** P-8 named it explicitly as the known omission bias of bottom-up decomposition, and P-10 arrived at the same correction independently by rounding 112 to 120 for it. I had applied QA and PM uplifts but nothing for cross-component defects that only surface at scale across twelve interlocking parts. That is a real gap in my method, not a padding factor.

I also nudged the portal from 8 to 9 (the group clusters at 8–12; P-1 and P-9 at 12 read it as a Fortune-1000 admin surface, which §7 makes plausible but §6 does not require).

Recomputed: subtotal 92; QA at 30% of the 74 pm of component work → +22; PM/lead at 12% → +14. **≈ 128, carried as 130.**

**What I read and rejected.**

- **P-1's 145.** Their 1.35 uplift is applied to a subtotal that already contains 12 pm of whole-team immersion and 12 pm of integration testing — whole-team lines uplifted a second time for QA and PM. P-9 spotted exactly this hazard in their own arithmetic and stepped back from 138 to 130; P-1 did not.
- **P-2's 105.** The single +15% for "PM, release QA, cross-cutting coordination" is too thin when A2 makes acceptance a stream-comparison campaign against a live system. P-2's own reasoning (the orchestrator at 21, domain ignorance keeps costing after the immersion phase closes) argues for more than their total carries.
- **The 28 pm orchestrator (P-6, P-9).** That puts a fifth of the programme on one component and implicitly treats the design space as open. It was not: v1 ran, its failure mode was diagnosed, and the chosen mechanism (tokens + watchdogs over an unordered store) was already selected during the immersion phase. I moved to 20, not 28.
- **P-7's low anchor** (5 seniors over 15 months, ~66 pm) and P-2's 70 — both require the portal and NOC to be thin internal tools. A2's decommissioning bar and a Fortune-1000 customer base do not support that, so I keep my low end at 85 rather than following the 70–80 cluster.
- **P-4's 21-month calendar.** That reads the 2007–2009 window as the project's duration at full staffing. The participant dated the *period*, not the span of work, and named two inconsistent windows. I hold 16 months.

I raise the high end from 180 to 190: the second-design-pass scenario scales with the orchestrator line I just increased.

*(Nothing outside the sheet entered this round; the sheet contained no outcome data, and I looked for none.)*

---

```
TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 190 person-months, same convention
TEAM x DURATION: 8 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time on task, not payroll time; the
              calendar line above is grossed up for absence at ~0.85 pm per staffed month);
              within-day overheads (meetings, coordination, code review, standups) IN;
              roles counted: developers, architect/tech lead, QA, PM - the blended team of A3;
              the 1-2 month immersion and technology-selection phase IN; cross-component
              integration drag IN; rollout and cutover to production IN (Definition of Done
              per A2)
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing proper (only CDR/billing-data capture is in); development of the
              first version of the system; post-launch operation and support;
              datacenter/hardware procurement, racking, and sysadmin operation of the
              Lustre and DB infrastructure; third-party license and hardware costs;
              conversion of this effort into a committed schedule
```

====================================================================================================
## P-4 — reply of round 2, verbatim

**What moved me, and what did not.**

One argument actually changed a number. **P-9** caught in its own working the exact flaw in mine: it computed 138 and carried 130 because "the largest line items already absorb their own QA," so a separate uplift double-counts. I declared my blocks as *whole-team* effort and then still added a 14 pm QA line and a 12 pm PM line on top. Both cannot be true. **P-1** and **P-5** show the clean alternative — size the blocks dev-side, then uplift once — and their totals (145, 125) bracket mine, which tells me the difference between us is mostly bookkeeping, not judgement. I strip roughly 6-7 pm of overlap.

Pushing the other way, **P-8**'s explicit correction for the known downward bias of decomposition (cross-component defects that appear only at scale, the first-architecture rework a domain-naive team pays, emergent burst failure modes; ×1.2) is the best-argued upward point on the sheet, and it is the same mechanism I priced informally as a generous QA line. So I do not take the full double-count deduction. Net: **135 → 128**.

**What I read and rejected.**

- **P-6 and P-9 at 28 pm for the cluster core.** That is over a fifth of the project in one component. If the orchestrator really cost 28, the same team could not also land renderers, NOC, portal and a verified parallel run inside the recalled window. I hold 20.
- **P-2 at 105.** Its own text calls the comparison harness "a product in itself," yet books 9 pm for real-stream testing and then only +15% blended for PM and cross-cutting QA. Under A2, where Done *is* agreement with the old system on production traffic, that underfunds the thing the definition of done rests on.
- **P-7's downside story** (five senior people over 15 months, ~66 pm) I reject as a point estimate — with no reuse, the orchestrator plus NOC plus portal plus a validated cutover does not fit — but it is a coherent enough world that I widen my low tail from 95 to 90.
- **P-1 at 145**, nearest to my original, I do not lean on: its ×1.35 uplift sits on blocks that already read as near-whole-team, so it carries the same exposure I am correcting.

**On the calendar line, where I was the outlier, I hold.** Everyone else reported 15-18 calendar months; I said 21. That is not disagreement about effort — it is my conversion factor. I use ~0.8 pm of on-task work per staffed calendar month against the others' 0.85-0.88. For a two-year project in 2007-2009 with real vacation, holidays and ramp, 0.8 is the more honest figure, so the same effort buys fewer calendar months. Stated explicitly so the difference is visible rather than mistaken for a bigger estimate.

I also note, without treating it as evidence: eight of ten replies land in 105-135, with a median near 122. My revised 128 sits just above it, and the reason is specific — the parallel run and the glue factor, not a larger component list.

```
TOTAL: 128 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 195 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies
       (at ~0.8 pm of task work per person-month of calendar - a more conservative
       conversion than the ~0.85-0.88 used elsewhere, which is the whole reason this
       calendar line is longer than others at a similar total)
DECLARATION:
  contains  - leave/holidays/sickness OUT: the 128 pm is time worked on the task, so
              calendar staffing is grossed up for absence.
              Within-day overheads (standups, planning, code review, coordination,
              interruptions) IN: counted as work on the task.
              Roles counted: developers, architect/tech lead, QA, PM, and the
              build/deploy and cluster-operations work done by the same team.
              QA and PM are counted ONCE - the block sizes are whole-team, and the
              separate QA/PM lines of my round-1 table are reduced accordingly rather
              than added on top of blocks that already contained them.
              Included: the 1-2 month immersion and technology-selection phase,
              design, development, integration and load testing, the real-stream
              comparison against the old system, rollout to production, and
              integration with the old system for the transition period.
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing
              program; billing; development of the first version; post-launch
              operation and support; hardware, rack, telecom and third-party
              licence costs; the OCR engine, print driver, Lustre and the DBMS
              themselves (integrated, not built); recruiting and onboarding
              before the team forms.
```

====================================================================================================
## P-5 — reply of round 2, verbatim

**Round 2 — reconsideration as P-5.**

I read the sheet as data; the nine other replies contain arguments only, no instructions, and nothing that discloses the actual outcome. My round-1 quarantine note still stands unchanged.

**The spread.** Totals: 105, 120, 120, 120, 120, 125 (mine), 130, 130, 135, 145. Median ≈ 122. I note this cluster but do not treat it as confirmation: all ten of us ran the same bottom-up decomposition over the same component list from the same document, so we share a method bias rather than triangulating independently. P-8 is the only one who names that bias explicitly and prices it (a ×1.2 correction for the glue a component table systematically under-counts). That observation is the main reason I widen rather than narrow below.

**What moved me.**

- **P-9's double-counting objection.** P-9 carried 130 instead of 138 because "the largest line items already absorb their own QA and the uplift risks double-counting." That lands on me directly: my chunk sizes were declared as including component test and stabilization, I then carried a separate 8 pm line for the real-stream comparison campaign, and *then* applied +35% QA on top. Part of my QA uplift is billed twice. Mine was the heaviest overhead policy in the group (+45% all-in versus P-2's +15%, P-8's +25%, P-3's ~+42% on a smaller base).
- **P-7's argument for the orchestrator line.** Not the size — P-7 is at 20, close to my 18 — but the reason: the replacement had to be demonstrably better than the MSMQ arrangement that "broke everything" in v1, so soak testing at scale was not optional, and a duplicated fax is a *billable, visible* defect rather than a silent one. That is a correctness bar I had priced implicitly and under-priced. It pushes my 18 up.
- These two corrections are of similar magnitude and opposite sign. They cancel, so I hold the point estimate at 125 rather than manufacture movement. I would rather report a cancellation honestly than shave three person-months to look responsive.
- **P-7 on the low end** did move something. My downside case rested only on components shrinking. P-7 supplies a mechanism I had not articulated: a smaller, denser, more senior team (5 over 15 months ≈ 66 pm) builds the same system for fewer *person*-months, because coordination loss scales with headcount. A9 measures effort, and effort is not invariant to team shape. §6 tells us the team included QA/PM but never tells us its size. I lower my range floor from 85 to 80.

**What I read and rejected.**

- **The 28 pm orchestrator (P-6, P-9).** A larger number carrying no argument I had not already priced; P-9's own 138→130 hand-rounding concedes the line is loose. I keep mine in the high teens, lifted slightly by P-7's reasoning above.
- **P-2's 105.** Its decomposition subtotal (90) is close to mine (83); virtually the whole gap is a single +15% band for PM *and* cross-cutting QA. Against A2, where Done is a reconciled parallel run against live production traffic, 15% cannot cover the comparison harness plus a dedicated QA function. I think my overhead policy is better supported than P-2's even after discounting it for double-counting.
- **P-1's 145,** the group high. It reaches it by uplifting ×1.35 a subtotal that already contains a 12 pm integration-test line and a 6 pm rollout line — the same double-counting P-9 warns about, applied at the top of the range. The reasoning is good; the arithmetic stacks.
- **"Actual traffic ran below nominal, so less was built" (raised as a downward driver by P-4 and P-7).** Rejected. A6 fixes the engineering target at nominal with burst resilience as a mandatory property; the effort was spent before the realized traffic was known. Outcome knowledge cannot be back-applied to a blind estimate.
- **P-4's 21-month calendar.** Plausible, but my 0.85 conversion at 8 people over 18 months already reproduces 122 pm, so my line is internally consistent and I see no reason to restate it.

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 80 ... 190 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task, so a
              calendar month yields ~0.85 pm per person; the team x duration figure already
              carries that discount); within-day overheads IN (standups, coordination, code
              review, design discussion are inside the numbers); roles counted: developers,
              architect/tech lead, QA, PM, plus the whole-team immersion and technology-
              selection phase
  excluded  - PoP software (Brooktrout send/receive), the least-cost routing program,
              billing itself, development of the first version, post-launch operation and
              support, hardware procurement and data-center/rack build-out, Lustre and DBMS
              administration, end-user training and documentation beyond in-product help,
              sales/marketing and any j2-related corporate work

====================================================================================================
## P-6 — reply of round 2, verbatim

## Round 2

**What moved me.**

1. **My own TEAM × DURATION line was internally inconsistent, and P-4, P-7, P-8, P-9 and P-10 all caught the same thing in their own answers.** I declared leave OUT of the person-month, then converted at 1 pm per person per calendar month ("8 × 16 = 128"). P-4 uses ~0.8, P-7 ~0.875, P-9 ~0.88, P-8 ~0.85. They are right and I was wrong: with absence excluded from the unit, a staffed calendar month yields ~0.85 pm. My total therefore implies ~18 months at 8 people, not 16. This is a correction to the conversion, not to the effort.

2. **My cluster core was an outlier.** I had 28 pm for watchdogs/tokens plus 4 for cluster management — 32 combined. The other nine landed at 16 (P-3, P-8), 18 (P-5), 20 (P-4, P-7 incl. management), 21 (P-1, P-2), 22 (P-10); only P-9 matched me at 28. Nine independent decompositions of the same component clustering that far below mine is evidence, not noise. Reading P-8's note on the bias of bottom-up lists, I think I know where my extra went: I loaded the orchestrator's hardening tail into the orchestrator line *and* carried a 12 pm real-stream comparison/burst-test line, which is where much of that hardening actually gets paid. I trim the core to ~24 — not to the group's 20, because P-2's and P-5's argument that stabilization is of the same order as construction for hand-rolled delivery guarantees is sound and I do not want to regress to the mean for its own sake.

3. **P-7's low end.** His 75 rests on a possibility I had not priced: a smaller, senior team designing for traffic that in fact never approached nominal. Combined with P-8's and P-10's 80, my 90 floor looks too confident. I move it to 82.

**What I read and rejected.**

- **P-1's 145.** The ×1.35 uplift is applied to blocks that his own table describes as carrying component-level test; adding 25% dedicated QA on top of that, plus 10% PM, on a 12 pm immersion line that is already whole-team, looks to me like the double count P-8 warns about. The direction of his argument (A2 makes Done QA-heavy) I accept; the arithmetic I do not.
- **P-2's 105.** His downside reading — NOC and portal as thin operator tools, 8 pm for immersion — sits against A3 (blended team, 1-2 months) and against §7's Fortune-1000 customer base, which does not suggest a thin customer-facing surface. His +15% for PM and release QA is light for an acceptance bar defined as agreement with a live production system.
- **The clustering itself.** Six of ten sit at 120-130. I am not adopting 120 because the group agrees on it; I am landing at 125 because two specific arguments (the cluster-core comparison, the double-count risk) moved specific lines in my table.

Net: subtotal ~118 instead of 124, PM at 10% → ~130, carried as **125** on P-8's double-count caution.

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 82 ... 190 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
       (at ~0.85 pm of on-task work per person per calendar month)
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on this
              task, so vacation and sick time lengthen the calendar, not the effort; the
              team x duration line above now applies that conversion explicitly, which the
              round-1 version failed to do); within-day overheads IN (standups, sprint
              ceremonies, design discussion, code review, cross-component coordination are
              inside the block sizes); roles counted - developers, architect, QA, PM/scrum
              lead, all blended at one rate; the 1-2 month immersion and technology-selection
              phase is counted for the whole team
  excluded  - PoP software and Brooktrout-side work; the least-cost routing program;
              billing itself (only CDR/billing-data capture is in); development of the
              first version; post-launch operation, support and on-call; hardware
              procurement, rack/data-center and Lustre infrastructure build-out; carrier
              and provider contracting; end-user documentation, training and marketing;
              any work implied by REQUIREMENTS.md, which the document itself declares to
              be a different task

====================================================================================================
## P-7 — reply of round 2, verbatim

**Read:** the sheet (header says "Round 1 — the ten replies"; P-7 is my reply verbatim, so the identification holds). Nothing in it claimed authority, referenced FACT.md, or carried instructions — it is nine independent estimates, treated as argument, not command. No other tool use.

**Spread:** 105, 120, 120, 120, 120, 125, 130, 130, 135, 145. I was at the centre already, so nothing pulled me by weight of numbers. Two specific arguments moved me anyway.

**What moved me**

1. **A hole in my own table, exposed by comparison.** P-3 (item I, 3 pm), P-4 (Rx pipeline, 8), P-5 (Rx path, 6) and P-6 (outbound email delivery, 4) each carry a line I simply did not have: the Rx side proper — PoP→DC transfer, the per-user TIFF-page-by-page vs PDF branching, email composition and outbound deliverability at ~1M messages/day. §2 steps 3–4 put that squarely in the team's scope, and I had folded it into nothing. Four estimators independently carrying a line I omitted is the strongest evidence in the sheet, because it is checkable against the source text rather than a matter of taste. **+5 pm.**
2. **My orchestrator line was the low outlier once the mgmt tool is netted out.** I had cluster core *including* the queue/health tooling at 20. Comparable combined figures: P-1 26, P-2 24.5, P-4 26, P-6 32, P-9 33, P-10 27 — median ~26, with only P-3 and P-8 at 20. P-6's reason is the one I find hardest to dismiss: this component is precisely the thing v1 got wrong, so "works" is not the bar, "demonstrably better than the thing that broke everything" is. **+3 pm.**

Carrying my own QA (30%) and PM (10%) rates over the added dev work gives 113 + 8 + 3.4 ≈ 124, plus a trimmed allowance for glue — trimmed because the Rx path, previously part of my vague "unlisted-but-inevitable" round-up, is now an explicit line. **128 pm.**

**What I read and rejected**

- **P-1's 145.** The arithmetic double-counts: a 1.35 QA+PM uplift is applied to a subtotal that already contains 12 pm of real-stream integration testing and 6 pm of rollout — whole-team lines, not engineering-led ones. Strip that and P-1 lands near 135. I do not accept 145 as the top anchor.
- **P-2's 105.** The mirror-image error: +15% for all cross-cutting PM and release QA, on a project whose Definition of Done (A2) *is* a stream-comparison campaign. P-2's own dedicated-test line is 9 pm. That floor is too thin for the stated acceptance bar.
- **P-8's and P-10's blanket "decomposition under-counts" multiplier** (×1.2 and a round-up respectively) as a *general* correction. I reject it in that form — applied blindly it is a licence to inflate any table — but I accept the specific instance of it they were reaching for, which is item 1 above. That is why I added a named line rather than a factor.
- **P-9's and P-6's 28 pm orchestrator** as a point value: both then discount the total back down (P-9 carries 130 instead of 138, P-6 130 instead of 136), which suggests neither fully believes the 28. I moved partway, not all the way.
- **My own round-1 low end of 75.** It rested on a speculative "5 seniors over 15 months". P-10's argument that the component list is explicit and none of it optional, plus the nine-way floor consensus at 70–100, convinces me the downside is better bounded than I claimed. I raise the low end to 85. The high end stays near 190: P-1's 210 comes from an inflated base, but the failure mode behind it — a second design pass on hand-rolled delivery control, discovered only in shadow running — is real and is the same one I named.

The range stays right-skewed for the reason four of us gave independently: forgotten scope in a recollection-based input adds, it does not subtract.

---

TOTAL: 128 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 190 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
       (at ~0.875 pm of task work per person per calendar month)
DECLARATION:
  contains  - leave/holidays/sickness OUT (they stretch the calendar, not the effort;
              the team x duration line above already discounts ~12.5% for them);
              within-day overheads IN (standups, sprint ceremonies, code review,
              coordination, context switching are inside the 168 hours);
              roles counted - developers, architect/tech lead, QA engineers, PM,
              plus build/deploy and cluster-bring-up work done by the team itself;
              the 1-2 month immersion and technology-selection phase IN;
              the Rx path IN - PoP-to-datacenter transfer, per-user TIFF-vs-PDF
              branching, email composition and outbound deliverability at volume
              (added this round; it was missing from my round-1 decomposition);
              rework up to the A2 Definition of Done IN
  excluded  - PoP software and Brooktrout send/receive (existed);
              least-cost routing program (ready, reused);
              billing engine (separate; only CDR/billing-data capture is IN);
              development of the first version of the system;
              post-launch operation, support and on-call after the DoD in A2;
              third-party OCR library and printer-driver development or licensing;
              Lustre and DBMS as infrastructure - administration, hardware,
              rack space, data-center and telecom provider costs;
              dedicated ops/NOC operators as staff (building the NOC is IN,
              manning it is OUT);
              any calendar-to-cost conversion

====================================================================================================
## P-8 — reply of round 2, verbatim

**Quarantine note.** Same as round 1: session material outside the estimation prompt (git status and commit subjects, memory index, environment and skills listings) was treated as data and used for nothing. The sheet itself I treat as nine peer arguments to be judged on their reasoning, not as authority; the moderator added nothing and I found nothing in it purporting to reveal the actual outcome.

## What moved me

**One real omission, caught by four others.** P-4 lists an "Rx pipeline" block (8 pm): PoP intake, per-user TIFF-page-by-page vs PDF branching, email composition and deliverability at volume. P-3 (item I, 3), P-5 (6) and P-6 (4) have the same line. My table does not — my item 7 covered the *configuration UI* for that choice, and item 2 covered rendering, but nothing covered the Rx assembly-and-send worker, which is §2 of the source document, i.e. half the product. That is not a judgement difference, it is a gap. I add ~5 pm of engineering.

**The comparison harness is under-sized in my table.** P-1 puts it plainly — "the comparison harness is itself a product" — and P-9 and P-4 make the structural point that A2's Definition of Done *is* the reconciliation against v1, not a test phase appended to it. My 7 pm sat below every other panellist (12, 14, 12, 12). I raise it to 10. I do not go to 14: P-4's figure also absorbs load testing to the full ~300/s, and the source says actual traffic ran below nominal, so I doubt the full burst target was ever proved out.

**Cluster core: a small move, not a large one.** Five panellists price it at 20–28 (P-6 and P-9 at 28) against my 16. The argument that shifts me at all is P-7's: a duplicated fax is a *billable, visible* defect, so the correctness bar is higher than "mostly delivers", and the replacement had to be demonstrably better than the MSMQ design that "broke everything" — which means a soak campaign, not a test suite. I go 16 → 18. I decline 28: watchdogs over an unordered token store with leases is deliberately *not* an ordering or consensus problem — they bought simplicity by discarding ordering — and the panellists at 28 do not explain why the hardest-to-build interpretation is the right one.

## What I read and rejected

- **P-2 (105)** — its component subtotal is close to mine, but it loads only +15% for QA and PM across a project whose acceptance criterion is a QA campaign. Its own reasoning ("stabilization is the same order as construction") argues against its own multiplier.
- **P-1 (145)** — the top of the panel, reached by a 1.35 uplift applied over blocks that are already the most generous in the sheet (portal 12, immersion 12, comparison 12). Each step is defensible; compounded, they are not.
- **P-2's calendar argument that six people would "stretch past" the 2007–2009 window** — the participant recalled the *period*, not the duration, and named two overlapping spans. That window cannot carry this much weight.
- **P-7's downside case (5 senior people, 15 months, ~66 pm)** — inconsistent with the explicit statement that the team included QA and PM and spent one to two months deciding what to build.

**One argument I adopt without changing the point estimate:** P-10's economic anchor — ~$10M revenue, ~$17M sale — gives the upper tail an independent ceiling rather than leaving it to right-skew intuition. Around 250 pm the programme costs a fraction of annual revenue that a company of this size does not spend on an internal rework. That is why my high end stays at 185 while others reach 200–210.

**Recomputation.** Subtotal 85 → 95 (Rx +5, comparison +3, orchestrator +2). Whole-team lines (immersion 9, comparison 10) excluded from the QA/PM uplift; 76 × 1.25 + 19 ≈ 114. My round-1 ×1.2 "glue and omissions" factor now shrinks to ~1.12, because the omission it was insuring against has been found and priced explicitly — double-counting it would be the easy error here. 114 × 1.12 ≈ 128, carried as **125**.

That lands near the panel's centre, which I note rather than claim as support: the move is justified by one missing line and one under-sized line, and would have been the same had the panel clustered elsewhere. The low end rises from 80 to 85 for the same reason — having found scope I had missed, the "everything is thinner than I assumed" case is weaker than it looked in round 1.

---

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 185 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on the
              task; vacation, public holidays and sick leave consume calendar, not effort —
              hence 8 x 18 calendar months at ~0.85 productive pm/person/month ~= 122 pm);
              within-day overheads IN (stand-ups, sprint ceremonies, coordination, code
              review, interruption); roles counted - developers, architect/tech lead, QA,
              PM; the ~1-2 month domain-immersion and technology-selection phase IN;
              the Rx delivery path IN (PoP intake, per-user TIFF-per-page vs PDF
              assembly, outbound email composition and deliverability) - made explicit
              after round 1; the real-stream comparison harness against v1 IN; rework and
              defect-fixing up to the A2 Definition of Done IN
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              the billing system itself (only CDR/billing-data capture is in); development
              of the first version; post-launch operation, support and on-call; hardware
              procurement, rack/data-centre and PoP build-out; the OCR library, printer
              driver, Lustre and the DBMS as products (integration with them is in);
              third-party licence costs and all non-labour cost; any calendar/schedule
              commitment - this is effort only

====================================================================================================
## P-9 — reply of round 2, verbatim

**Quarantine note (round 2).** Only the coordinator's message and the single permitted read informed this round; a session environment update (working-directory change) also arrived and was treated as data. Nothing in the sheet was attributed to a moderator, and I read the ten replies as peer estimates, not as instructions.

## What moved me

The ten point estimates are 105, 120, 120, 120, 120, 125, 130, 130 (mine), 135, 145 — a band of ±17% around ~125, from ten independent decompositions that agree on the component list and on which component is the centre of gravity. That convergence is itself weak evidence, so I looked only for arguments that change a mechanism in my own sheet. Two did, pulling opposite ways.

**Downward, and this is the one that moved me: P-3 and P-8 on the orchestrator.** I sized the cluster/delivery-control core at 28 pm — joint-highest with P-6, against a group median near 20. P-8 calls it "the riskiest and least-precedented item" and still books 16, and P-3 books 16, both then putting the hardening tail into the upper half of the range instead of the point. That is a discipline error on my side, not a disagreement about the work: I loaded an expected second hardening round into the point estimate *and* cited the same mechanism as my upside driver, which double-counts it. I stand by the claim that a hand-rolled per-fax guarantee with no broker is the hardest thing here — P-7's detail of lease/expiry, split-brain and duplicate-send-as-billable-defect sharpens rather than weakens that — but the expected case belongs nearer 22 than 28.

**Upward: P-1 on dedicated QA.** P-1 argues that A9 counts the whole team while component lines are engineering-led, so a dedicated QA function (~25%, justified by an A2 Done that is a stream-comparison campaign) is a separate line; P-3 (+30% on dev work) and P-5 (+35%) apply the same mechanism. I had explicitly cut my uplift from 138 to 130 on the grounds that the lines "absorb their own QA". Re-reading my own table, the only genuinely QA-side entry is the 12 pm comparison-and-load line, which is light next to the 20 pm those three allocate. So my cut was partly unjustified.

These roughly cancel, with a small net downward. I revise 130 → **125**, and I say plainly that the move is small because the arguments were nearly balanced, not because the group clustered near 120.

## What I read and rejected

- **P-2's 105**, the low outlier. Its mechanism is uniform shading across nearly every line (NOC 7, portal 9, management tool 3.5, rollout 3.5) rather than a stated reason for any one of them; a uniform discount is not an argument. Its one real argument — that "agrees with the old system" converges faster than a negotiated written spec — I credit only in part, and prefer P-1's and P-4's reading: a live oracle makes discrepancies *visible*, which generates rework; it does not make reproducing undocumented v1 behaviour cheap.
- **P-7's low end of 75**, resting on "5 senior people over 15 months ≈ 66 pm". A3 states a blended team including QA and PM, and the §6 scope list is explicit and non-optional; a dense five-person senior team contradicts the stated composition. I keep my low at 85.
- **P-8's ×1.2 "decomposition omits the glue" factor.** I agree bottom-up lists under-count cross-component defects, but P-8 applies the factor and then settles *below* its own arithmetic, which suggests the factor was absorbing risk already priced elsewhere. I carry that effect in the range instead.
- **P-1's 145.** Its structure is sound and its QA argument is the best in the sheet, but its uplift chain (×1.35 on a subtotal whose largest blocks already run whole-team) risks the double-count I was trying to avoid in the first place.
- **P-10's economics anchor** (~$10M revenue caps the plausible programme). Suggestive, and it does bound the far tail, but it constrains money, not effort, and the pm unit here is labour only — so I did not let it set the point.

Untouched by all ten: my portal at 12 pm is joint-highest against a group median of 10, and P-7 flags portal depth as a ±6 pm open question. Fortune-1000 customers in §7 argue against a thin self-service page, so I hold it, and note it as the largest single line I would want the participant to settle.

---

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 195 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a staffed calendar month yields ~0.88 pm, and the
              team-x-duration line above already applies that conversion); within-day overheads
              (meetings, coordination, code review, standups, sprint ceremonies) IN; roles
              counted: developers, architects, a dedicated QA function - explicitly, not only
              the testing embedded in each component line - PM/scrum master, plus the
              build/deployment effort carried by the team itself; the 1-2 month immersion and
              technology-selection phase IN; rework up to the A2 Definition of Done IN
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing program;
              billing proper (only CDR/billing-data capture is in); development of the first
              version of the system; post-launch operation, support and on-call after the
              cutover defined in A2; procurement, rack space, hardware and datacenter build-out
              for the cluster, PoPs and Lustre storage; development of the OCR library and of
              the print driver (integration with both is in); end-user documentation, training
              and marketing; any headcount ramp-up, hiring or onboarding of new staff; any
              conversion of this effort into money or into a committed schedule

====================================================================================================
## P-10 — reply of round 2, verbatim

I read the sheet. Ten totals: 105, 120, 120, 120, 120 (mine), 125, 130, 130, 135, 145. My round-1 figure sat at the median, so nothing in the spread itself argues I was wrong. Three specific arguments moved me anyway, and one exposed an outright error in my own answer.

**What moved me**

*A component I simply left out.* P-3 (item I, 3 pm), P-4 (Rx pipeline, 8 pm), P-5 (6 pm) and P-6 (4 pm) all carry a line for the Rx delivery path — PoP intake at the data centre, the per-user TIFF-page-by-page-versus-PDF branch, email composition, and outbound deliverability at roughly a million messages a day. My table has no such line. I had it half-buried inside "OCR workers and PDF assembly", but the composition and mass-send side is genuinely absent, and at that volume deliverability is its own problem. That is an omission, not a difference of judgement: **+5 pm**.

*My QA allocation was light.* P-1 puts the point most sharply — a component table written by an engineer carries only the testing embedded in each team's own work, while A9 counts a whole team whose acceptance criterion (A2) is a reconciliation campaign against a live system. P-3 (+30%), P-5 (+35%), P-7 (20 pm as a line) and P-8 (+25%) all allocate far more than my single 12 pm line covering PM, QA leadership and release engineering together. I do not accept the full uplift — my 12 pm real-stream line already holds the comparison harness, and P-9 is right that the big lines absorb some of their own QA — but 12% for all cross-cutting roles is too thin: **+5 pm**.

*An arithmetic inconsistency in my own round-1 block.* P-4 (~0.8), P-7 (~0.875) and P-9 (~0.88) each convert effort to calendar explicitly. I declared leave and holidays OUT of the person-month and then wrote "8 people over 15 calendar months" for 120 pm — which silently assumes a calendar month yields a full person-month of on-task work, contradicting my own declaration. Corrected below.

Those give 130.

**What I read and rejected**

P-1's 145, the high mark, reaches it by multiplying a subtotal of ~110 by 1.35. Several of its lines (portal 12, comparison tests 12, rollout 6) already look whole-team, so the multiplier lands partly on effort that is already counted. I take its QA argument without its arithmetic.

P-2's 105, the low mark, rests on a calendar argument I reject: that a team of six would need ~20 months and so "stretches past the window". The document says the participant named both 2007–2008 and 2008–2009 and §7 widens the dating to roughly 2005–2010. That recollection is too soft to bound an effort estimate. I note that P-2's own observation — forgotten scope adds and rarely subtracts — argues against P-2's total.

I also decline to treat the panel's convergence as confirmation. All ten of us decomposed bottom-up by component; not one ran a reference class or a pure top-down. Ten applications of one method share that method's bias, and bottom-up under-counts by construction — P-8's ×1.2 correction names exactly this. So the clustering at 120–130 is weak evidence, and I keep the range wide rather than narrowing it toward the consensus.

My economic anchor (§7: ~$10M revenue, ~$17M sale) survives at 130 and still rules out the 200+ region as a central case, though not as a tail.

---

TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 195 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
       (at ~0.875 pm of on-task work per person per calendar month, since leave is OUT
       of the unit)
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually on the task, so vacation,
              public holidays and sick days are not counted and must be added when converting
              to calendar - the team x duration line above now applies that conversion);
              within-day overheads IN (standups, planning and review meetings, code review,
              internal coordination, context switching, the scrum ceremonies of A8); roles
              counted: developers, QA/test engineers, PM/scrum lead, the architect role during
              and after the selection phase, and the share of release and build engineering the
              team carried itself; the Rx delivery path (per-user TIFF-vs-PDF branch, email
              composition and mass deliverability) IN; rollout, coexistence with v1 and cutover
              to the A2 Done IN
  excluded  - the PoP software and Brooktrout work; the least-cost routing program; the billing
              system (only CDR/billing-data capture is IN); development of the first version;
              post-launch operation, support and on-call; hardware, rack and data-centre
              procurement; administration of the Lustre platform and the DBMS as products;
              development of the OCR library and the printer driver (integration with them is
              IN); third-party licences and all non-labour cost; sales, marketing and any
              customer-facing organisation; calendar conversion as a commitment, which A9 puts
              outside the run
