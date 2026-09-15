Size the elements of the work model batch below by classifying, not pricing. Everything you need is in this message; read no files.

**Scope: the subtrees rooted at N08, N09 of the product model `HM57-1`, as classified and crossed by `Hotyn-W 1.2`** — 24 sized elements (aggregates are listed for context and are never sized). Other subtrees and the model root are outside this batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, sections 1 to 7 as your engine definition requires. In the sizing table quote the enumeration verbatim, one row per sized element, grouped by subtree. Every number you output is a count of named things; nothing else.

---

# INPUT 1 — the work model batch: elements with class, parent, declared content, covered obligations (with their texts) and the activities crossed onto them

In this model coverage lives in leaves only: an aggregate's content is its children. A derived leaf has no covered obligation; its declared content is its name read with the trigger that called for it (the elements named after `trigger:`).


**N08 — Notifications** · aggregate (not sized) · parent N01

**N09 — Reporting and dashboard** · aggregate (not sized) · parent N01
- **A022 — Approval status change notification** · class **behaviour** · parent N08
  - covered obligations: G-3.2: Editors and Approvers are notified of a change in approval status
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A027 — User dashboard start screen** · class **surface** · parent N09
  - covered obligations: G-6: Display a user dashboard or start screen with notifications, reports, prefix data and other information
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A028 — Prefix capacity counter** · class **behaviour** · parent N09
  - covered obligations: G-6.1: A prefix capacity counter displays how many numeric indicators (GINs or LNs) have been used and how many are available
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A029 — Report engine over read store** · class **behaviour** · parent N09
  - covered obligations: G-7: Allow users to generate reports; G-7.1: Customise, schedule, run and view reports for adds, changes and deletes; G-7.2: View usage reports by hour, day, week, month and year *(current reporting utilises 3scale)*; G-7.3: Run report data history; G-7.4: Run audit reports
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A030 — Adds, changes, deletes report definitions** · class **behaviour** · parent N09
  - covered obligations: G-7.1: Customise, schedule, run and view reports for adds, changes and deletes
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A031 — Report customisation** · class **behaviour** · parent N09
  - covered obligations: G-7.1: Customise, schedule, run and view reports for adds, changes and deletes
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A032 — Report scheduler** · class **behaviour** · parent N09
  - covered obligations: G-7.1: Customise, schedule, run and view reports for adds, changes and deletes
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A033 — Usage reports by hour, day, week, month, year** · class **surface** · parent N09
  - covered obligations: G-7.2: View usage reports by hour, day, week, month and year *(current reporting utilises 3scale)*
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A035 — Report run history** · class **store** · parent N09
  - covered obligations: G-7.3: Run report data history
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A036 — Audit report definitions** · class **surface** · parent N09
  - covered obligations: G-7.4: Run audit reports
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A037 — Notification dispatch service** · class **behaviour** · parent N08
  - covered obligations: G-8: Provide notifications to users in various formats — email, SMS and/or onscreen; G-8.1: Global notifications (e.g. scheduled server downtime); G-8.2: Member-specific notifications (e.g. a user opts to be notified when records are updated or added); G-8.3: Member-to-member and member-to-X-Customer notifications (e.g. a user can challenge record data); P-11.5: If the status of a record within a hierarchy changes, the user is notified if it affects the status of other records in the hierarchy; NFR-17: Near-real-time event notifications when system errors occur
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A038 — Email channel via client SMTP relay** · class **interface** · parent N08
  - covered obligations: G-8: Provide notifications to users in various formats — email, SMS and/or onscreen; G-9: Users can send application feedback to X-Customer, routed to a single X-Customer contact or a feedback tracking system
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A039 — SMS channel via external SMS gateway** · class **interface** · parent N08
  - covered obligations: G-8: Provide notifications to users in various formats — email, SMS and/or onscreen
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **A040 — Onscreen notification inbox** · class **surface** · parent N08
  - covered obligations: G-8: Provide notifications to users in various formats — email, SMS and/or onscreen
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A041 — Global notification broadcast** · class **behaviour** · parent N08
  - covered obligations: G-8.1: Global notifications (e.g. scheduled server downtime)
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A042 — Record add and update notification subscriptions** · class **behaviour** · parent N08
  - covered obligations: G-8.2: Member-specific notifications (e.g. a user opts to be notified when records are updated or added)
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A043 — Directed member and member-to-X-Customer messages incl. record data challenge** · class **behaviour** · parent N08
  - covered obligations: G-8.3: Member-to-member and member-to-X-Customer notifications (e.g. a user can challenge record data)
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A044 — Communication preferences (method, frequency)** · class **store** · parent N08
  - covered obligations: G-8.5: A user can set communication preferences for the method and frequency of notifications received outside the system
  - activities crossed onto it: A2, A3, A4, D4, G2m, G3m, G4m, K1, K2
- **A045 — Notification digest batching by frequency** · class **behaviour** · parent N08
  - covered obligations: G-8.5: A user can set communication preferences for the method and frequency of notifications received outside the system
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A113 — Hierarchy status impact notification** · class **behaviour** · parent N08
  - covered obligations: P-11.5: If the status of a record within a hierarchy changes, the user is notified if it affects the status of other records in the hierarchy; L-10.3: If the status of a record within a hierarchy changes, the user is notified if it affects the status of other records in the hierarchy
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A136 — Access request notification to owner** · class **behaviour** · parent N08
  - covered obligations: D-2.1: The request is sent to the data owner, who must approve before the data becomes available
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **A167 — Administrator alert notification** · class **behaviour** · parent N08
  - covered obligations: NFR-17: Near-real-time event notifications when system errors occur; NFR-18: Near-real-time event notification when critical business functions fail
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **C06 — Notification message templates** · class **store** · parent N08
  - covered obligations: — (derived element, no covered obligation; trigger:A037)
  - activities crossed onto it: A2, A3, A4, G2m, G3m, G4m, K1, K2
- **C07 — SMS contact number capture and verification** · class **behaviour** · parent N08
  - covered obligations: — (derived element, no covered obligation; trigger:A039)
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
