# Run 41 — the ten baseline replies

**Record status.** The harness does not persist subagent output, so this file is the durable record.
Each run's **instrument readings are verbatim**: the closing `TOTAL / RANGE / TEAM x DURATION /
DECLARATION` block and the decomposition totals. The surrounding prose reasoning is **condensed** —
stated here so no reader mistakes this for a full transcript. Every run: `tool_uses: 0`,
`claude-opus-5`, identical prompt (md5 `c17b874b1101f32f6d8c1ff7a151e7df`).

Every run opened with an unprompted quarantine notice naming injected repository material (git
branch/status, commit subjects referencing runs 38-40, "Hotyn-P counts FaxRxTx twice", "UFP 78 vs 82",
the memory index, tool listings). Several stated explicitly that these looked like leaked prior
results for the object under estimate. None used them. Not repeated per run below.

---

## B-1 — TOTAL 130, range 90...190, 9 x 18

Two passes: 15-line component decomposition (subtotal 112 pm) + QA ~10% + PM ~8% -> ~131; then a
COCOMO II cross-check at ~60 KSLOC with multipliers ~0.5 giving ~130 pm. Largest line: orchestrator
(watchdogs + tokens) 18. Declared: leave OUT, within-day overheads IN, roles = devs, architect/lead,
QA, PM/scrum. Calendar conversion at ~0.8 pm per head per calendar month.

## B-2 — TOTAL 90, range 60...140, 7 x 13

13-line build decomposition in **developer**-months (subtotal 54 dm), then loads: immersion ~10,
QA ~30% of dev = 16, PM ~12% = 8.5, cutover 4 -> ~92, carried at 90. Largest line: cluster + delivery
control 12.0. Cross-checks: calendar (7 FTE over ~13 productive months) and ~1200 blended LOC/pm
implying ~110 KLOC. Declared: leave OUT (calendar stretch ~10-15%), overheads IN. **The lowest of
the ten, and the only one under 100.**

## B-3 — TOTAL 120, range 85...175, 7 x 19

14-line decomposition summing ~118, rounded to 120. Largest line: cluster + delivery control 20.
Separate lines for a load/burst/failure-injection programme (8) and the real-stream comparison
harness (8). PM/release/cutover 15 (~12-13% of engineering). Cross-check: ~7 people over ~19 months
at ~0.88 pm per head-month. Range skewed upward, explicitly: "the downside is bounded, the upside
is not."

## B-4 — TOTAL 120, range 85...180, 8 x 15

12-line decomposition (subtotal 94.5) + dedicated QA 15 + architect/lead/PM ~10% = 11 -> ~120.
Largest line: cluster + delivery control + management tool 22. Cross-check at ~1 KLOC per all-in
person-month implying ~120 KLOC. Declared: leave OUT, wall clock therefore ~17-18 months rather
than 15.

## B-5 — TOTAL 120, range 80...190, 8 x 17

12-line decomposition (engineering subtotal 82) + QA 20 + PM/release/cutover 10 + an explicit
**"decomposition-blindness uplift ~7%"** of 8 -> 120. Largest line: orchestration core 20.
Cross-checks: 150-250 KLOC at 1.5-2.5 KLOC/pm -> 80-150 pm; team shape 8 x 17.

## B-6 — TOTAL 105, range 70...160, 7 x 18

10-line build decomposition (subtotal ~50 pm), then explicit overlays: ceremonies/review/coordination
+15%, system-level defect backlog +15%, QA 32%, immersion ~10, PM ~10% -> ~105. Largest line:
cluster core 15. **Rejected basic COCOMO (300-500 pm) as a known overestimate for commercial product
teams**, kept only as an argument against the low end.

## B-7 — TOTAL 155, range 110...225, 8 x 22

14-line decomposition, build subtotal 118, + dedicated QA 20 + PM/lead 15 -> ~153, carried at 155.
Largest line: cluster + delivery control 24, with an explicit note that this item alone could run
35+ pm. Cross-checks: ~150-200 KLOC at ~1000-1300 LOC/pm -> 130-180 pm; COCOMO II 400+ treated as a
loose upper anchor only. **The highest of the ten.**

## B-8 — TOTAL 120, range 85...175, 8 x 18

Two passes reconciled. Pass 1: 14-line decomposition, engineering subtotal 77.5 developer-months,
+ QA 25% = 18 + PM 0.7 FTE = 12 -> ~115. Pass 2: team shape, centre 7 x 18 ~ 126, box 75...220.
Taken at 120. Largest line: cluster orchestration 15. **Explicitly ran and discarded COCOMO II**
(300-700 pm) as miscalibrated for this organisational shape, letting it widen only the upper tail.

## B-9 — TOTAL 125, range 80...200, 8 x 18

12-line decomposition (subtotal 75.5) + QA and PM ~30% -> ~98 + immersion 11 -> ~109 + an explicit
**+15% correction for decomposition's structural blind spots** -> ~125. Largest line: cluster +
delivery control 18. Cross-checks: 200-300 KLOC at ~2.5 KLOC/pm -> 80-120 pm; 8 heads x 18 months at
~88% availability -> ~127.

## B-10 — TOTAL 120, range 80...190, 7 x 19

13-line decomposition, dev subtotal 97, + QA 22 + PM 10 -> ~129, **carried down to 120** for a stated
overlap between the orchestration and comparison-harness fixtures. Largest line: orchestration core
22 (of which cluster manager 6). Cross-checks: 7 x 19 at ~0.87-0.9 -> ~116; 130-180 KLOC at
1.3-1.7 KLOC/pm -> 90-135. COCOMO II 350-700+ rejected as miscalibrated, used only as tail evidence.

---

## What is common across all ten

1. **Every run decomposed.** 10-15 named components, then a role loading for QA and PM, then a
   contingency or bias correction. Nobody guessed; nobody used a bare analogy; nobody asked for more
   information. This reproduces `run14`'s finding on a second case.
2. **Nine of ten volunteered a second, independent cross-check** (KLOC per person-month, or team
   shape against the stated calendar window) without being asked for one.
3. **Four named COCOMO II and all four rejected its number**, each giving the same reason: calibrated
   on a development world that does not include a small product company's internal rework. This is
   the corpus's own consensus reproducing itself, not four independent judgements.
4. **Every run named the same largest cost driver** — the hand-rolled watchdog/token orchestrator,
   at 15-24 pm — and every run named the same mitigating factor, v1 as a live executable
   specification.
5. **Every run declared leave OUT and within-day overheads IN**, and every run put a working day's
   yield at roughly 0.85-0.9 A9 pm per head-month — against this project's gap-blind measurement of
   5-6 net task hours in 8, which is ~0.68. See `run41_baseline_no_method.md` §3.
