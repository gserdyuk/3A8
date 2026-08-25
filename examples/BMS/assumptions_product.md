# BMS — assumptions a product-model run may see

**Pinned input, version 1, 2026-08-20.** The projection of `assumptions.md` v2 and `open_questions.md`
onto the product: only what constrains **what must exist**.

Why a projection and not the log itself: `assumptions.md` v2 speaks about what a number prices, what
is carried, and which delivery activities absorb which obligation. A product-model run must not see
that vocabulary — a builder shown the language of work starts building work. What is removed is
removed because it is about the doing, never because it is inconvenient.

Removed here, and where it lives: the term of the continuing service and what is priced versus carried
(`assumptions.md` A0, A1) · the team (A3) · the definition of done (A2) · the organisational context
(A6) · units (A7). None of them says anything about what the product is.

---

## P1. Scope of the thing being modelled

The **first release** of the system, covering every obligation in `requirements_product.md` (N = 68).

The system is delivered as a hosted, multi-tenant service — that is R01, a property of the artefact.
**The acts of hosting it and supporting it are not product obligations and are not in your list.** If
your structure seems to need an operations department or a support desk as a component, that is the
signal you have crossed out of the product; say so rather than building it.

## P2. External systems

- The Cost Tracking Center (R06) and UPSA (R07) have working, documented APIs.
- **R15**, "intelligent search across multiple third-party systems", is read as integration with
  **one or two aggregators** — a GDS or Booking-class API. *The reading refused:* direct integrations
  with many individual hotel suppliers.
- **R08**, SSO, is a standard protocol per the client's documentation (SAML or OIDC).
- **R27**, SMS, is delivered through an external gateway of the Twilio class, not through
  infrastructure of our own.

## P3. R13 — the reading taken

"Support for critical instances such as major disruption situations" is read as **technical**:
resilience, disaster recovery, operation in a degraded mode under load. It is a property of the
platform, alongside R12 and R68.

*The reading refused:* mass re-booking and re-routing of travellers during a travel disruption — a
strike, a volcano, a hotel closing. That reading is **not in your list**. Do not build it, and do not
treat its absence as an omission of yours.

## P4. R14 — assumed content

The RFP names "Admin and Support" in its context diagram and gives it no content anywhere. Assumed
content: **an internal support console** — incident intake, diagnostic inspection of bookings and
integrations, inspection of the running configuration. **Not** a ticketing product, **not** a
customer-facing help desk, **not** a knowledge base, **not** an engine for service-level agreements.

## P5. Readings taken where an entry can be read two ways

| ids | reading taken |
|---|---|
| R05 | "Access for the travel department, transport suppliers and employees to manage their confirmed bookings" is the **umbrella** over the three portals, not a separate capability beside them |
| R10 | "Clear business processes" is a **property of the system** — the processes a user meets are clear — not a document to be produced |
| R29 | "Automatic booking" applies where an integration exists (R39 transport; aggregator-backed hotel booking). Elsewhere booking is manual, per R38, R40 and R48. When the automatic path fails, it falls back to the manual one |
| R37 R38 R40 R47 R48 | "Handled manually" means the system **supports** the manual process — forms, uploads, status records — and performs no external automation for those suppliers |
| R67 | No numeric target for report generation is pinned; the obligation is that generation is not excessive, with criteria settled during design |
| R11 R65 R71 | R11 and R65 state one obligation twice — configurability, including for legislative and organisational change. R71, designed to grow, is distinct and architectural. You may not merge entries (M1); cover them jointly and record the overlap |

## Pin

    tr -d '\r' < assumptions_product.md | md5sum

Parents: `assumptions.md` v2, `open_questions.md` v1, `requirements_product.md`
(md5 `0c2dea478b993e4451a66f9468633f1e`, N = 68).
