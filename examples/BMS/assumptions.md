# BMS — Assumption Log

**Version 2, 2026-08-20.** Version 1 (2026-07-17) governed runs 1–18. What changed and why is in §
*Changelog* at the foot. No number produced under version 1 changes under version 2.

Assumptions that close the RFP's gaps. Agreed before estimation begins; all runs must use the same
assumptions — otherwise their ranges are not comparable.

---

## A0. The imperative: what the client explicitly requires cannot be struck out *(new in v2)*

**An obligation the client stated cannot be removed by an assumption.** The requirement list is the
external anchor; a log that deletes an entry makes the anchor internal, and whoever writes the log can
shrink the project invisibly. That is the defect this framework exists to remove, arriving through a
side door.

A log *may* bound what a given number prices. So every obligation has exactly three permitted
outcomes, and each is visible in the output:

| # | outcome | what the output must show |
|---|---|---|
| 1 | **priced here** | the work items it produced |
| 2 | **priced by another instrument** | the obligation, and which instrument prices it — a service rate per unit time is not this instrument |
| 3 | **not priceable without a parameter the client has not given** | the obligation, the missing parameter, and the question to be asked |

### The failure mode is an exception, not a footnote

**If an id from either pinned list appears neither in the priced work nor on the carried list, the run
raises an exception: it emits a defect report and no estimate.** A number produced over a struck-out
obligation is not a worse estimate, it is an estimate of a different project, and there is no way to
tell from the number which project it was.

Three places the check fires:

1. **Before the run** — the log against the lists (the table in A10). A contradiction is an input
   defect and the run does not start. Run 18's R03 collision is exactly this case: one run of four
   flagged it, three priced over it, and none of them stopped.
2. **At the end of the run** — every id accounted for, or defect report instead of an estimate.
3. **Outside the run** — the same check is mechanical and can be run over the output by anybody.

**What the imperative outlaws is silence, not scope.** The run always has a legal path: carry the
obligation with its reason. That distinction matters, because run 18's single most informative output
— the list of work the decomposer judged necessary and refused to invent — came from a run that
proceeded and reported. An exception on every scope boundary would have destroyed that signal; an
exception on silence produces more of it.

**Narrowing is allowed and is not deletion, but it must be declared.** Where an assumption reads an
obligation in the smaller of two available ways — A4, A5 and A8 all do — the reading taken and the
reading refused are both written down, and the refused one is named as a risk rather than left
implied.

---

## A1. What this estimate prices

Design + development + testing + production deployment of the **first release**, covering all product
obligations of `requirements_product.md` (N=68) and the demanded work of `requirements_work.md` (N=5)
to the extent A0 permits.

- **Included:** hosting / DevOps / environment set-up (dev/stage/prod), UAT support.
- **Included, and now stated rather than implied** — the hand-over residue of the three continuing
  obligations:

  | id | what is priced | where |
  |---|---|---|
  | R02 | making the hosted service exist at hand-over: tenancy, capacity, runtime | activity `E7` |
  | R03 | making support possible at hand-over: the handover pack, diagnostic access | activity `O3` |
  | R64 | agreeing and recording the technology-currency and upgrade policy | one demanded item; no catalogue activity covers it |

- **Carried, not priced** (A0, outcome 3) — the continuing service itself: running the hosted system
  (R02), operating the support function (R03), performing the periodic reviews and upgrades (R64).
  **Missing parameter: the term.** An open-ended obligation has no effort figure until somebody says
  for how long, and the instrument that prices it is a rate per unit time, not a project estimate.
  **The question for the client: over what period do R02, R03 and R64 run?**
- **Not applicable:** user training and the warranty period. Neither list contains an entry demanding
  them, so nothing is being removed — this is the one place where the old wording's "not included" was
  accurate.

Every output produced under this log must show the carried-not-priced list above. A number offered
without it silently claims to cover a running service — and under A0 that is an exception, not a
presentation flaw: no estimate is emitted until R02, R03 and R64 each appear as priced work, as
carried work, or as a stated defect.

## A2. Definition of Done
The functionality works in production, UAT has passed, basic documentation (operational + user)
exists. Matches the declared documentation technology `U-OPS-USER` and acceptance `C-UAT`.

## A3. Assumed team
1 PM/BA, 1 architect (part-time), 3–4 developers, 1 QA, 1 DevOps (part-time). Blended, predominantly
senior/middle. A typical team that has not worked together before (conservatively). Matches the
declared delivery process `D-TEAM`.

## A4. External integrations
- CTC and UPSA have working, documented APIs.
- **Narrowing, declared (A0):** "intelligent search across multiple third-party systems" (R15) is read
  as integration with **1–2 aggregators** (a GDS/Booking-class API). *The reading refused:* dozens of
  direct hotel integrations. If the client means the wider reading, R15 alone changes the size of the
  integration subsystem by an order of magnitude and this estimate does not cover it.
- SSO — per the client's documentation, a standard protocol (SAML/OIDC).

## A5. SMS
Via a ready external gateway (Twilio-class), not our own infrastructure. **Narrowing, declared (A0):**
R27 is read as gateway integration. *The reading refused:* own SMS infrastructure, carrier agreements.

## A6. Organizational context
The client is a large enterprise; the speed of approvals and the availability of the client's
specialists are typical for an enterprise. Accounted for only in reference class (decomposition, by
construction, does not see it).

## A7. Units *(reworded in v3)*
Estimation in **person-days**, where one person-day is **one assigned working day** of a team
member — the industry convention in which effort norms, benchmarks and timesheets are recorded. It
is *not* eight hours of pure productive output; meetings, coordination and ordinary overhead are
inside the day, as they are inside every external source. Conversion to a calendar (leave, holidays,
part-time allocations) is a separate step, not part of the method runs.

*(v3, adjudicated by the author 2026-08-22: the earlier wording "8 hours of net work" could be read
as strict productive time, which would put the unit ×≈0.8 below every external norm and benchmark —
both reference-class runs and the diagnosis flagged the fork independently. The adjudication closes
it: all pipeline figures, the rate table's values included, are assigned-day figures, and no ×0.8
conversion exists anywhere.)*

## A8. R13 — the reading taken *(new in v2)*

R13 "support for critical instances such as major disruption situations" reads two ways, and run 18
(HM-OA) flagged it without resolving it, which was correct behaviour.

- **The reading taken:** technical — resilience, disaster recovery, degraded-mode operation under load.
  It joins R68 and R12 as a property of the platform.
- **The reading refused:** business — mass re-booking and rerouting of travellers during a disruption
  event (a strike, a volcano, a hotel closure).

The refused reading is **not in the product list and is not priced.** HM-OA judged that if it is what
the client means, it is "the largest single omission in this model", and that judgement stands. Under
A0 this is a narrowing, not a deletion: R13 is priced under the technical reading, and the business
reading is named here as an obligation that would enter as a **new requirement** — it is not a
different way of building R13, it is a different system.

## A9. R14 — assumed content *(new in v2)*

R14 "Admin and Support component" is named in the RFP's context diagram and given no content anywhere
in the document. Every run that met it invented content, and the invention was invisible.

**Assumed content:** an internal support console — incident intake, diagnostic inspection of bookings
and integrations, inspection of the running configuration. **Not assumed:** a ticketing product, a
customer-facing help desk, a knowledge base, or an SLA engine.

This is an assumption of the log and not a reading of the RFP, because the RFP says nothing to read.
It is here so that runs stop differing on an invention and start differing on a stated scope.

## A10. This log is checked against the pinned lists before any run *(new in v2)*

The R03 defect existed because the log and the requirement list were written in different eras and
never compared: the log bounded an *estimate*, the list states what the *product* must be. The check
is now standing, and it is this table.

| assumption | touches | relation |
|---|---|---|
| A1 | R02, R03, R64 | bounds what is priced; carries the remainder under A0 |
| A1 | environments | matches `E-DSP`: dev, stage, prod |
| A2 | — | matches `U-OPS-USER`, `C-UAT` in the declaration |
| A3 | — | matches `D-TEAM` |
| A4 | R06, R07, R08, R15 | narrowing of R15, declared |
| A5 | R27 | narrowing, declared |
| A8 | R13 | narrowing, declared |
| A9 | R14 | supplies content the RFP omits |
| A11 | R05, R10, R11, R13, R14, R15, R29, R65, R67, R71, and R02/R03/R64 | points at `open_questions.md`; declares the reading taken for each |

Nothing in this log now contradicts an entry of either list. Any future edit to the log, the lists or
the declaration re-runs this table.

## A11. Open questions stand behind several of these assumptions *(new in v2)*

Where the RFP reads two ways, the procedure is: **ask the client; if no answer, assume; declare the
assumption; and when runs are compared afterwards, exclude the differences the open question causes.**

The register is `open_questions.md`, pinned like the lists. Ten questions, all of them `not asked` —
this RFP is a training document with no client behind it, which is precisely why the assumptions must
be visible: they are what the estimate rests on.

A8 and A9 are the two entries promoted into this log, because run 18 named them as defects. The other
eight live in the register with their readings declared.

**The comparison rule.** Two runs are compared twice — over all requirements, and excluding those the
register names. The gap is the *input-ambiguity component*, a reading on the RFP rather than on the
method. The filter is the register and never the runs' own ambiguity flags: a run that flagged more
would otherwise improve its own agreement score.

---

## Changelog

**v3, 2026-08-22** — A7 reworded: a person-day is an assigned working day, not "8 hours of net
work". Adjudicated by the author after run 27's diagnosis carried the unit question as its
top-ranked open fork (D6, a ×1.25 lever on the whole cross-sensor comparison). No number changes:
every value in the pipeline was already an assigned-day figure by provenance; only the declared
reading was wrong.

**v2, 2026-08-20** — A0 added: an assumption may not remove an obligation, only bound what a number
prices, and must name the instrument or the missing parameter for the rest. A1 rewritten under A0:
R02, R03 and R64 keep their hand-over residue as priced work and their continuing part as carried
work with the term named as the missing parameter — previously they were simply excluded, which run 18
caught as a contradiction with the requirement list. A4 and A5 marked as declared narrowings with the
refused reading named. A8 (R13), A9 (R14), A10 (the standing cross-check) and A11 (the open-questions register and the
comparison rule that goes with it) added.

**v1, 2026-07-17** — governed runs 1–18. Its numbers are unaffected by v2: none of those runs priced
ongoing operation, and v2 does not add it to the priced scope — it makes the exclusion visible and
attaches the question the client has to answer.
