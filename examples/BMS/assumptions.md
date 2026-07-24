# BMS — Assumption Log (fixed before the runs, 2026-07-17)

Assumptions that close the RFP's gaps. Agreed before estimation begins; all runs (decomposition, reference class) must use the same assumptions — otherwise their ranges are not comparable.

## A1. Estimation scope
Design + development + testing + production deployment of the **first release** covering all functional requirements of the RFP.
- Included: hosting / DevOps / environment setup (dev/stage/prod), UAT support.
- **Not included:** subsequent operation (hosting & support), user training, the warranty period.

## A2. Definition of Done
The functionality works in production, UAT has passed, basic documentation (operational + user) exists.

## A3. Assumed team
1 PM/BA, 1 architect (part-time), 3–4 developers, 1 QA, 1 DevOps (part-time). Blended, predominantly senior/middle. A typical team that has not worked together before (conservatively).

## A4. External integrations
- CTC and UPSA have working, documented APIs.
- "Intelligent search across multiple third-party systems" = integration with **1–2 aggregators** (a GDS/Booking-class API), not dozens of direct integrations with hotels.
- SSO — per the client's documentation, a standard protocol (SAML/OIDC).

## A5. SMS
Via a ready external gateway (Twilio-class), not our own infrastructure.

## A6. Organizational context
The client is a large enterprise; the speed of approvals and the availability of the client's specialists are typical for an enterprise. Accounted for only in reference class (decomposition, by construction, does not see it).

## A7. Units
Estimation in **person-days** (1 pd = 8 hours of net work). Conversion to a calendar is a separate step, not part of the method runs.
