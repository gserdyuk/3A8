Size the elements of the work model batch below by classifying, not pricing. Everything you need is in this message; read no files.

**Scope: the subtrees rooted at N40, N50, N60, N70, N80, N90 of the product model `HM61-1`, as classified and crossed by `Hotyn-W`** — 29 sized elements (aggregates are listed for context and are never sized). Other subtrees and the model root are outside this batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, sections 1 to 7 as your engine definition requires. In the sizing table quote the enumeration verbatim, one row per sized element, grouped by subtree. Every number you output is a count of named things; nothing else.

---

# INPUT 1 — the work model batch: elements with class, parent, declared content, covered obligations (with their texts) and the activities crossed onto them

In this model coverage lives in leaves only: an aggregate's content is its children. A derived leaf has no covered obligation; its declared content is its name read with the trigger that called for it (the elements named after `trigger:`).


**N40 — Processing cluster** · aggregate (not sized) · parent N00

**N41 — Cluster management tool** · aggregate (not sized) · parent N40

**N50 — Storage and records** · aggregate (not sized) · parent N00

**N60 — NOC** · aggregate (not sized) · parent N00

**N70 — User portal** · aggregate (not sized) · parent N00

**N80 — Old system coexistence** · aggregate (not sized) · parent N00

**N90 — System-wide properties** · aggregate (not sized) · parent N00
- **L01 — PoP registry: served PoPs and their reach** · class **store** · parent N90
  - covered obligations: F01: A worldwide fax send-and-receive service covering at least Europe and the USA *(the participant does not remember whether Australia was included)*; F38: 10–20 points of presence are served
  - activities crossed onto it: A2, A3, A4, D4, G1, G2, G3, K1, K2
- **L28 — Windows cluster node host** · class **behaviour** · parent N40
  - covered obligations: F20: An own cluster of Windows computers for rendering and other tasks; F39: A render cluster of ~16–20 nodes joined by a private network
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L29 — Queue-length view** · class **surface** · parent N41
  - covered obligations: F21: A cluster management tool — queue lengths and so on *(no further detail given anywhere in the source)*; F34: The NOC shows the state of the queues
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L30 — Node state view** · class **surface** · parent N41
  - covered obligations: F21: A cluster management tool — queue lengths and so on *(no further detail given anywhere in the source)*; F33: The NOC shows the state of the cluster
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L31 — Node control: take out, put back, redistribute** · class **behaviour** · parent N41
  - covered obligations: F21: A cluster management tool — queue lengths and so on *(no further detail given anywhere in the source)*
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L36 — Fax archive store on Lustre** · class **store** · parent N50
  - covered obligations: F26: The fax archive is stored on the Lustre file system
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L37 — Working-file area on Lustre** · class **store** · parent N50
  - covered obligations: F27: The working files are stored on the Lustre file system
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L38 — System database schema** · class **store** · parent N50
  - covered obligations: F28: A database is part of the system *(the DBMS is not specified)*; F29: The components communicate through the database and an API
  - activities crossed onto it: A2, A3, A4, D4, G1, G2, G3, K1, K2
- **L40 — Common C#/.NET codebase and shared libraries** · class **statement** · parent N90
  - covered obligations: F30: The development language is C#
  - activities crossed onto it: D4, K3
- **L41 — NOC console** · class **surface** · parent N60
  - covered obligations: F31: NOC — an internal control centre; F33: The NOC shows the state of the cluster; F34: The NOC shows the state of the queues
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L42 — PoP state view** · class **surface** · parent N60
  - covered obligations: F32: The NOC shows the state of the remote nodes (PoP)
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L43 — Portal site and user sign-in** · class **surface** · parent N70
  - covered obligations: F35: User portal — the users' website *(named in the source; no functional detail given anywhere)*
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L44 — Delivery configuration page** · class **surface** · parent N70
  - covered obligations: F35: User portal — the users' website *(named in the source; no functional detail given anywhere)*
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L45 — Fax status and history page** · class **surface** · parent N70
  - covered obligations: F35: User portal — the users' website *(named in the source; no functional detail given anywhere)*
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L46 — Capacity provision for nominal volume** · class **statement** · parent N90
  - covered obligations: F36: Nominal target volume ~1,000,000 faxes per 10-hour day (~30/s on average)
  - activities crossed onto it: D4, K3
- **L47 — Burst absorption: backlog and admission control** · class **behaviour** · parent N90
  - covered obligations: F37: Burst mode of about ten times nominal (~300/s)
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L48 — Cluster membership and private-network addressing** · class **behaviour** · parent N40
  - covered obligations: F39: A render cluster of ~16–20 nodes joined by a private network; F44: Distribution across the cluster is a mandatory property, not an option
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L49 — CDR writer and store** · class **store** · parent N50
  - covered obligations: F40: CDR data is saved
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L50 — Billing data writer and store** · class **store** · parent N50
  - covered obligations: F41: Billing data is saved *(billing itself is out of scope)*
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **L51 — Old-system exchange interface** · class **interface** · parent N80
  - covered obligations: F42: Integration with the old system; F43: Coexistence with the old system for the duration of the transition
  - activities crossed onto it: A2, A3, A4, A10, D4, K1, K2
- **L52 — Traffic assignment between old and new system** · class **behaviour** · parent N80
  - covered obligations: F43: Coexistence with the old system for the duration of the transition
  - activities crossed onto it: A2, A3, A4, D4, K1, K2
- **D03 — User account and service settings records** · class **store** · parent N50
  - covered obligations: — (derived element, no covered obligation; trigger:L43,L05,D01,D02)
  - activities crossed onto it: A2, A3, A4, G1, G2, G3, K1, K2
- **D04 — PoP status collector** · class **behaviour** · parent N60
  - covered obligations: — (derived element, no covered obligation; trigger:L42)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **D05 — Node and queue state collector** · class **behaviour** · parent N41
  - covered obligations: — (derived element, no covered obligation; trigger:L29,L30)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **D06 — Archive retrieval index by fax identity** · class **store** · parent N50
  - covered obligations: — (derived element, no covered obligation; trigger:L36,L45)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **D07 — Working-file cleanup** · class **behaviour** · parent N50
  - covered obligations: — (derived element, no covered obligation; trigger:L37)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **D09 — Portal password recovery** · class **behaviour** · parent N70
  - covered obligations: — (derived element, no covered obligation; trigger:L43)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **D11 — System event and alarm log** · class **store** · parent N60
  - covered obligations: — (derived element, no covered obligation; trigger:L41,L33)
  - activities crossed onto it: A2, A3, A4, K1, K2
- **D12 — Account data synchronisation with old system** · class **interface** · parent N80
  - covered obligations: — (derived element, no covered obligation; trigger:D03,L51)
  - activities crossed onto it: A2, A3, A4, A10, K1, K2

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
