Size the elements of the work model batch below by classifying, not pricing. Everything you need is in this message; read no files.

**Scope: the subtrees rooted at N20, N30 of the product model `HM61-1`, as classified and crossed by `Hotyn-W`** — 25 sized elements (aggregates are listed for context and are never sized). Other subtrees and the model root are outside this batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, sections 1 to 7 as your engine definition requires. In the sizing table quote the enumeration verbatim, one row per sized element, grouped by subtree. Every number you output is a count of named things; nothing else.

---

# INPUT 1 — the work model batch: elements with class, parent, declared content, covered obligations (with their texts) and the activities crossed onto them

In this model coverage lives in leaves only: an aggregate's content is its children. A derived leaf has no covered obligation; its declared content is its name read with the trigger that called for it (the elements named after `trigger:`).


**N20 — Outbound fax path** · aggregate (not sized) · parent N00

**N21 — Submission email intake** · aggregate (not sized) · parent N20

**N22 — Renderer set** · aggregate (not sized) · parent N20

**N23 — PoP dispatch** · aggregate (not sized) · parent N20

**N30 — Job orchestration** · aggregate (not sized) · parent N00
- **L03 — Submission address mailbox receiver** · class **interface** · parent N21
  - covered obligations: F03: The user sends outgoing faxes by emailing a special address
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **L13 — Submission email parser** · class **behaviour** · parent N21
  - covered obligations: F12: The email sent to the submission address is parsed
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L14 — Recipient fax number extractor** · class **behaviour** · parent N21
  - covered obligations: F13: The recipient's fax number is extracted from the email
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L15 — Attachment-to-TIFF render path** · class **behaviour** · parent N22
  - covered obligations: F14: The document from the attachment is rendered to TIFF; F18: Renderers for the main document formats: DOC, XLS, PPT, PDF, TXT, GIF, TIFF
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L16 — Black Ice-class printer driver adapter** · class **interface** · parent N22
  - covered obligations: F15: Rendering goes through a printer driver of the Black Ice class *("it seems")*
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **L17 — TIFF archive packager** · class **behaviour** · parent N23
  - covered obligations: F16: The rendered TIFF is sent as an archive to a point of presence
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L18 — PoP outbound handoff** · class **interface** · parent N23
  - covered obligations: F16: The rendered TIFF is sent as an archive to a point of presence; F38: 10–20 points of presence are served
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **L19 — Least-cost routing program exchange** · class **interface** · parent N23
  - covered obligations: F17: Which point of presence receives the TIFF is decided by the ready least-cost routing program
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **L20 — DOC renderer** · class **behaviour** · parent N22
  - covered obligations: F18: Renderers for the main document formats: DOC, XLS, PPT, PDF, TXT, GIF, TIFF; F19: On the order of 8–10 input formats in all; each format is a separate piece of integration and stabilisation work
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L21 — XLS renderer** · class **behaviour** · parent N22
  - covered obligations: F18: Renderers for the main document formats: DOC, XLS, PPT, PDF, TXT, GIF, TIFF; F19: On the order of 8–10 input formats in all; each format is a separate piece of integration and stabilisation work
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L22 — PPT renderer** · class **behaviour** · parent N22
  - covered obligations: F18: Renderers for the main document formats: DOC, XLS, PPT, PDF, TXT, GIF, TIFF; F19: On the order of 8–10 input formats in all; each format is a separate piece of integration and stabilisation work
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L23 — PDF renderer** · class **behaviour** · parent N22
  - covered obligations: F18: Renderers for the main document formats: DOC, XLS, PPT, PDF, TXT, GIF, TIFF; F19: On the order of 8–10 input formats in all; each format is a separate piece of integration and stabilisation work
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L24 — TXT renderer** · class **behaviour** · parent N22
  - covered obligations: F18: Renderers for the main document formats: DOC, XLS, PPT, PDF, TXT, GIF, TIFF; F19: On the order of 8–10 input formats in all; each format is a separate piece of integration and stabilisation work
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L25 — GIF renderer** · class **behaviour** · parent N22
  - covered obligations: F18: Renderers for the main document formats: DOC, XLS, PPT, PDF, TXT, GIF, TIFF; F19: On the order of 8–10 input formats in all; each format is a separate piece of integration and stabilisation work
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L26 — TIFF renderer** · class **behaviour** · parent N22
  - covered obligations: F18: Renderers for the main document formats: DOC, XLS, PPT, PDF, TXT, GIF, TIFF; F19: On the order of 8–10 input formats in all; each format is a separate piece of integration and stabilisation work
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L27 — Further-format renderers, unnamed in source** · class **behaviour** · parent N22
  - covered obligations: F19: On the order of 8–10 input formats in all; each format is a separate piece of integration and stabilisation work
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L32 — Watchdog-and-token store with per-fax status** · class **store** · parent N30
  - covered obligations: F22: No job queue (MQ) is used; MSMQ is deliberately excluded; F23: A home-grown system of watchdogs and tokens (an unordered store) holds the status of each fax; F25: Orchestration of a large number of faxes in flight; F46: Delivery control of every fax is a mandatory property, not an option
  - activities crossed onto it: A2, A3, A4, D4, G1, G2, G3, K1, K2
- **L33 — Watchdog processes** · class **behaviour** · parent N30
  - covered obligations: F23: A home-grown system of watchdogs and tokens (an unordered store) holds the status of each fax; F24: The watchdog-and-token system resumes work if something went wrong; F45: Surviving failures is a mandatory property, not an option
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L34 — Stalled-job resumption** · class **behaviour** · parent N30
  - covered obligations: F24: The watchdog-and-token system resumes work if something went wrong; F45: Surviving failures is a mandatory property, not an option
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L35 — Job dispatcher: token claim and hand-out to workers** · class **behaviour** · parent N30
  - covered obligations: F25: Orchestration of a large number of faxes in flight; F44: Distribution across the cluster is a mandatory property, not an option
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L53 — PoP delivery-result receiver** · class **interface** · parent N23
  - covered obligations: F46: Delivery control of every fax is a mandatory property, not an option
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **L54 — Delivery confirmation and failure notice to sender** · class **behaviour** · parent N23
  - covered obligations: F46: Delivery control of every fax is a mandatory property, not an option
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **D02 — Sender identification and authorisation** · class **behaviour** · parent N21
  - covered obligations: — (derived element, no covered obligation; trigger:L03,L13)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **D08 — Render-failure notice to sender** · class **behaviour** · parent N22
  - covered obligations: — (derived element, no covered obligation; trigger:L15)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **D10 — Outbound retry and reroute on failed delivery** · class **behaviour** · parent N23
  - covered obligations: — (derived element, no covered obligation; trigger:L53)
  - activities crossed onto it: A2, A3, A4, K1, K2

---

# INPUT 2 — the sizing rules (catalogue 1.4 §3a, verbatim where it binds)

**W10.** Every sized element receives one size class — **S / M / L / XL** — by **counting named things**. The
enumeration is the justification; a bare number is not acceptable. Thresholds are pinned here and are not
yours to bend. Drivers count scope, never effort: no driver may reference difficulty, risk, novelty or time.

**One size class per element, assigned once.** The class is a property of the element — a leaf, or an
internal node carrying own content. **A pure aggregate is never sized.** Every per-element activity uses the
element's class by default. **Position-derived sizes are not yours** (per-parent, once-scoped, per-environment
items are tree arithmetic computed outside you) — do not report them.

## Element size classes — counted from the element's declared content plus its own coverage

| element class | what is enumerated | S | M | L | XL |
|---|---|---|---|---|---|
| behaviour | distinct actions (verb on object) the declared content names | 1 | 2–3 | 4–6 | ≥7 |
| interface | operations consumed or exposed; a named protocol/auth concern counts as one | 1 | 2–4 | 5–8 | ≥9 |
| surface | distinct user tasks the surface serves | 1 | 2–3 | 4–6 | ≥7 |
| store | entity kinds the store is responsible for | 1 | 2–3 | 4–6 | ≥7 |
| statement (both kinds) | systems or components the property constrains | 1 | 2–4 | 5–8 | ≥9 |
| aggregate | — never sized | | | | |

**XL is a class and a signal at once:** an XL element is classed XL **and** reported as a probable coarseness
finding about the product model (M10). Neither substitutes for the other.

**`statement` splits into two kinds**, logged with the phrase that justifies the kind: **`compliance`** — the
content names a standard, configuration or policy and no run-time scenario; **`behavioural`** — the content
entails run-time behaviour. **P-4, the kind tie-break: run-time wins** — a statement whose covered obligations
mix kinds is `behavioural` when any covered obligation entails run-time behaviour, `compliance` only when none does.

## Special counts — enumerated the same way, where the element carries the activity

| activity on the element | driver enumerated | S | M | L | XL |
|---|---|---|---|---|---|
| **A9** (performance and availability testing, on a behavioural statement) | measurable targets the statement names (thresholds, service levels) — count from the content **and the covered obligations' texts** | 1 | 2–3 | 4–6 | ≥7 |
| **G2m / G3m / G4m** (field mapping, extraction and transformation, load and reconciliation, on a store) | entity kinds in the store that are loaded from the predecessor applications — say per kind why it must arrive from the predecessor rather than be created at run time | 1 | 2–3 | 4–6 | ≥7 |
| **G1 / G2 / G3** (seed data specification, preparation and load, reconciliation, on a store) | entity kinds in the store that must be pre-loaded before the system is usable — say per kind why it cannot be created at run time | 1 | 2–3 | 4–6 | ≥7 |

The **D4** driver (requirement ids in the element's own coverage) is computed outside you from the coverage
sets; do not report it.

## Enumeration precedents — case law adjudicated once for everybody (catalogue 1.3 and 1.4)

- **P-1 — a named delivery channel is a protocol concern.** An interface whose obligation names a delivery
  channel counts the channel alongside the operation: "notifications via email" = the dispatch operation + the
  email channel = 2.
- **P-2 — a name token counts only when no counted obligation already covers its action.** A token in the
  element's name that an enumerated obligation already covers is not counted again; a token covered by no
  obligation is counted. The test is coverage, not position in name or text.
- **P-3 — slash-separated outcomes are distinct actions.** "Accepted/Rejected" names two transitions, not one;
  stage lists count by outcome.
- **P-4 — the kind tie-break: run-time wins** (above).
- **P-5 — an unnamed catch-all is not a named thing.** "and other details" names no kind and counts nothing.
- **P-6 — a stated cardinality without named members is not an enumeration.** "three amendment origins" is a
  number, not a list; an element whose declaration counts things it never names is **unsizeable — model
  defect (M10)**, never sized on a guessed reading.

An element you cannot count is a finding, not a guess: report it as *unsizeable — model defect (M10)* with what
is missing, and assign no class. You may not add, remove, merge or reshape elements or work items; work you
judge necessary and absent is a **closure violation** — name it, say what it would cover, do not size it.
