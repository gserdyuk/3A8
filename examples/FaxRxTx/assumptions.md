# FaxRxTx — Assumption Log (fixed before the runs, 2026-07-17)

Assumptions that close the gaps in SYSTEM.md. Agreed before estimation begins; all
runs (decomposition, reference class, …) must use the same assumptions — otherwise
their ranges are not comparable. Run input: SYSTEM.md + this file. FACT.md is not
passed into the runs.

## A1. Estimation scope
The full cycle for the "the team did" list from SYSTEM.md §6: the phase of domain
immersion and architecture/technology selection (~1–2 months) + design + development +
testing + rollout to production of the new version of the core functionality replacing
the first version.
- Included: rendering and OCR workers, the cluster with the delivery-control
  mechanism (watchdogs + tokens), NOC, the user portal, the inbound-email parser,
  saving CDR/billing data, integration tests on the real stream with comparison to the
  old system.
- **Not included:** the PoP software, the routing program, billing, post-launch
  operation, development of the first version of the system.

## A2. Definition of Done
The new system takes production traffic in prod; the integration tests on the real
stream have passed, the results agree with the old system; the old version can be
decommissioned.

## A3. Team and starting conditions
The team **did not know the domain** — immersion in the subject area, discussions,
and technology selection took ~1–2 months (included in A1). Mitigating factor: a
working v1 exists as a live reference of requirements ("like v1, but fix what we don't
like") — there is no full-scale requirements gathering from scratch, but the domain
(fax protocols, telecom, distributed delivery) is new to the team. Blended composition,
including QA and PM. The team's headcount is **not** part of the assumptions
(the volume of work is estimated, not the calendar).

## A4. Reuse
No first-version code in the new one ("no reference base classes"). Reused: the
ready PoP software, the ready routing, a third-party OCR library, rendering via a
printer driver (Black Ice-class), the existing storage infrastructure (Lustre) and the
DB as technologies — we do not develop these, only integrate with them.

## A5. Technological era
2007–2009: C#/.NET ~3.x, a Windows cluster on our own hardware, no clouds and no
ready orchestrators (what a message broker/Kubernetes would give today is written by
hand — watchdogs, tokens, delivery control). MSMQ deliberately excluded from the
negative experience of v1.

## A6. Target scale
The engineering target — **~1 million faxes / 10-hour day (~30/s on average)**,
with bursts up to ~10× (**~300/s**, "10 million/day" — an estimate of the peak mode).
A cluster of ~16–20 nodes, 10–20 PoPs. The estimate is made for designing to the
nominal with burst resilience: distribution, surviving failures, and delivery control
of every fax are mandatory properties, not options.

## A7. Rendering formats
8–10 input formats (DOC, XLS, PPT, PDF, TXT, GIF, TIFF + possibly 1–3 forgotten
ones). Each format is a separate piece of integration and stabilization work, not a
"free" extension of the list.

## A8. Organizational context
A product company (Venali), an internal rework by management decision. There is no
hard deadline, but there is pressure. The process — a planning phase, then scrum.
Approvals are internal, faster than the enterprise client of the BMS example.
Accounted for in reference class (decomposition, by construction, does not see it).

## A9. Units
Estimation in **person-months** (1 pm ≈ 21 pd ≈ 168 hours), the total effort of the
whole team, including QA/PM and the architecture-selection phase. Conversion to a
calendar duration is a separate step, not part of the runs.
