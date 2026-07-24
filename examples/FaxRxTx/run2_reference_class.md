# FaxRxTx — Run 2: Reference Class Forecasting (outside view)

**Method:** estimating by the class of similar projects as a whole, without decomposition into subtasks.
**Input:** SYSTEM.md + assumptions.md (A1–A9). FACT.md, REQUIREMENTS.md, and the other project files were not opened; web search was not used.
**Run date:** 2026-07-17.

---

## 1. Reference-class candidates

The object of the estimate (per SYSTEM.md §6 and A1–A8): rewriting from scratch the core functionality of a working distributed messaging/telecom platform of medium scale; a product company; the 2007–2009 era; C#/.NET on our own hardware; a blended team with QA/PM; the domain new to the team; a working v1 exists as a live requirements reference; the Definition of Done — production traffic in prod and the ability to decommission v1 (A2).

### Candidate A. "A full rewrite of a working server product of medium scale" (ground-up rewrite)

A class of projects where a product company decides to replace a working system with a new one, without code reuse. A class well documented in industrial folklore and post-mortems, with stable properties:

- **Systematic underestimation of volume.** A working v1 creates the illusion "the requirements are known, all that's left is to write it cleanly." In reality a significant share of v1's behavior is implicit fixes of edge cases accumulated over years; the new system is forced to rediscover them. This is the classic source of "the second half of the project after everything seemed done."
- **Second-system effect:** the second version is designed "properly," with margin for everything that annoyed in the first (here it is visible directly in SYSTEM.md: they threw out MSMQ, studied DHT, are building their own orchestrator with watchdogs and tokens). This lengthens the architectural phase and makes the system heavier.
- **Typical outcome for the class:** a median rewrite of this scale takes roughly 1.5–2.5 times more effort than the team expects at the start; a noticeable share (by various industrial observations — on the order of 20–40%) of rewrite projects either never reach full decommissioning of the old system or reach it after years of parallel operation.
- A typical successful representative of the class in the mid-to-late 2000s: a team of 6–12 people (blended), 1.5–2.5 years to a production cutover.

**Fit:** high. Almost everything matches: a working v1, zero code reuse, an internal management initiative, a product company, medium scale.

### Candidate B. "Hand-building distributed messaging/integration infrastructure, before the era of ready brokers" (mid-2000s)

The class: teams building their own delivery pipelines for messages/jobs with guarantees (mail gateways, SMS/MMS platforms, telecom billing pipelines, document-flow processing) in an era when "a broker + an orchestrator" were not taken off the shelf but written by hand.

Known properties of the class:

- **The infrastructure part dominates.** The application logic (rendering, parsing, portal) is the visible part; delivery control of every message, recovery from failures, the fight against partial failures and duplicates historically ate from a third to a half of all the effort and almost the entire stabilization "tail."
- **The stabilization tail is long and poorly compressible:** distributed failures reproduce only under real load, so the last 20% of the functionality cost disproportionately much.
- A typical representative: 5–10 engineers, 1–2 years to a stable production, plus a long tuning period.

**Fit:** high in technical nature (home-grown orchestration, watchdogs+tokens, integration tests on live traffic — A5, A6), but the class usually describes greenfield without a v1 reference, i.e. it slightly overstates the requirements risk relative to our case.

### Candidate C. "An average business-software project of the CHAOS-report era" (a generic class)

A broad class of 2000s corporate projects: median overrun in schedule/effort on the order of +50–100% of plan, ~20–30% of projects challenged/failed. It gives a useful base rate for "how much estimates lie in general," but ignores the specifics: distribution, the telecom domain, the rewrite. Within this broad class our project sits in a heavier subgroup.

**Fit:** low as a working class (too broad), but usable as a sanity check on the underestimation coefficient.

### Choice of the working class

**The working class is A (a rewrite of a working server product), with a correction for the systemic properties of B (home-grown distributed delivery before the era of brokers).** Rationale: A matches in organizational nature (a product company, v1 exists, an internal rework — this is exactly what defines the dynamics of the scope and the "second-systemness"), while B supplies the main technical effort driver — hand-written orchestration with delivery guarantees. C is used only as a check on the scale of the overrun coefficient. The final distribution is built on A∩B: "a rewrite of a distributed delivery platform of medium scale by a product team, 2005–2010."

---

## 2. Calibrating the scale within the class

To place the project on the class's scale (without decomposing!), coarse observable features suffice:

- ~8–10 heterogeneous application components/subsystems in the scope (SYSTEM.md §6) + the infrastructure delivery layer;
- the target nominal ~30 msg/s with a burst ×10 (A6) — this is a "medium" scale for the class: not a toy, but not a carrier-grade giant either;
- a cluster of 16–20 nodes, 10–20 PoPs (integration, not development);
- 8–10 rendering formats, each a separate piece of stabilization work (A7);
- a blended team with QA/PM, a "waterfall" planning phase + scrum (A8);
- mitigators: v1 as a requirements reference, ready PoP software and routing, a third-party OCR, no hard deadline under internal approvals.

By these features the project lands in the **middle part of the class** "a rewrite of a distributed delivery platform": typical representatives of this middle part were historically executed by teams of 6–12 people in 1.5–2.5 years, i.e. they fall into a total-effort range on the order of **100–300 person-months**, with a class median around **150–180 pm**.

---

## 3. Effort distribution (person-months, per A9)

| Quantile | Estimate, pm | What scenario within the class this is |
|---|---|---|
| **P10** | **~85 pm** | The upper decile of the class's luck: a small strong team (~5–6 blended), the v1 reference really cuts the requirements risk, the watchdog orchestrator "takes off" on the first architecture, the rendering formats stabilize without surprises; ~14–16 months to cutover. Below 85 pm almost never happens in this class: even an ideal run carries an irreducible minimum — 1–2 months of immersion in the new domain × team, 8–10 components, integration tests on live traffic with comparison to v1. |
| **P50** | **~160 pm** | The class median: a team of ~8 blended, ~20 months. One or two rework cycles in the orchestration layer (the first watchdog/token scheme does not withstand real failures — a typical class event), drawn-out stabilization of 2–3 "capricious" rendering formats, several months of parallel operation with v1 until full trust. Corresponds to the known property of the class: fact ≈ 1.5–2× the naive internal estimate. |
| **P90** | **~320 pm** | The lower decile (without a failure): a second-system sweep of the architecture (DHT ambitions, an over-complicated orchestrator), rediscovery of v1's implicit behaviors in prod, live traffic reveals discrepancies with the old system in waves, the cutover is postponed repeatedly; the team grows to 10–12, the term — 2.5–3 years. For the rewrite class a ×2 overrun from the median is not exotic but exactly P90. |

**The P99 tail (in words).** For the rewrite class the tail is not Gaussian but "failure-shaped": scenarios of 450–600+ pm are projects where the new system lives beside the old for years, unable to displace it (discrepancies on live traffic do not converge, business trust does not arrive), or where after a change of priorities/owner the project is cut and de facto does not reach the DoD of A2. By the class base rates the probability of the outcome "full decommissioning of v1 never happened within a reasonable term" is on the order of 15–30%; in terms of effort to the point of stopping, this is exactly the mass of the P99 tail. A separate tail amplifier specifically for this subgroup of the class: integration testing on the live stream with comparison to v1 is an honest but merciless readiness criterion; it does not allow "declaring victory" prematurely and therefore converts all hidden defects into additional person-months, not into closed eyes.

### Why the points are exactly these (a summary of the justifications through class properties)

1. **The frequency and size of underestimation.** The generic class C gives a median overrun of +50–100%; the "rewrite + distributed" subgroup is stably in the upper half of this range. The median 160 pm already includes this overrun relative to the "naive" ~90–110 pm that a team on such a project usually names at the start.
2. **Second-system effect** (SYSTEM.md directly shows the symptoms: rejecting MSMQ, exploring DHT, its own orchestrator) — shifts both the median and especially P90: the main mechanism of the right tail in class A.
3. **The era without ready brokers (A5).** In class B the "guaranteed delivery + recovery" layer historically costs 30–50% of all the effort and gives a disproportionate contribution to the stabilization tail — this is reflected in the P50→P90 gap (×2), which is wider than the P10→P50 gap (×1.9): the distribution is skewed right.
4. **Live traffic as a test oracle.** A property of the subgroup: comparison with v1 on the real stream lengthens the acceptance phase but lowers the probability of a "silent failure" — so the P99 tail of this project is rather "long and expensive" than "shipped broken."
5. **The mitigators are accounted for in P10/P50:** the v1 requirements reference, reuse of the PoP software/routing/OCR, the absence of an external enterprise client (A8) — these are exactly what keeps the median from drifting to 200+ pm, where the greenfield representatives of class B without a reference sit.

---

## 4. What the method does not see by construction

The outside view deliberately ignores the internal workings of this particular task and this particular team. For the check against the other runs — a list of blind zones:

1. **The team's actual strength and composition.** The class averages over teams of different skill; the real productivity of the specific Venali people (and whether there was a pair of "anchor" strong engineers carrying the orchestrator) can shift the outcome by a quantile in either direction. The assumption log deliberately does not fix the team's headcount (A3) — the method both uses this and is blind because of it.
2. **The real complexity of specific components.** The method does not distinguish what inside the scope is expensive and what is cheap: for example, whether the email parser and CDR are really trivial, and watchdogs+tokens are 40% of the work. This is decomposition's territory; here any such judgments are forbidden and were not made.
3. **The quality of specific third-party components.** How stable exactly the Black Ice-class printer driver, exactly this OCR library, exactly Lustre under Windows load in 2008 are — the class knows only "integrating third-party components sometimes blows up," but does not know whether it will blow up here.
4. **The actual quality of v1 as a reference.** If v1 is well observable and its behavior is easy to capture — the requirements risk is below the class average; if v1 is a black box without logs, above. The document does not report this, the method does not see it.
5. **The organizational dynamics of the specific company.** The patent lawsuit with j2 from 2006 and the subsequent sale of the company (SYSTEM.md §7) — signals of possible pressure on priorities/financing, which could either accelerate ("finish for the deal") or cut off the project. The outside view accounts for such things only as an anonymous mass of the tail, not as a specific factor with dates.
6. **The "scrum after waterfall" effect in this particular team.** The class averages over processes; whether the planning phase was useful or ritual is beyond the method's resolution.
7. **The nonlinearities of the burst requirement.** Designing "to the nominal with burst ×10 resilience" (A6) may be almost free with a lucky architecture or very expensive with an unlucky one; the outside view sees only the class average, not the bifurcation of the specific design.

---

*The file was generated by an isolated reference class forecasting run. It was not checked against FACT.md, findings.md, or the runs of the other methods.*
