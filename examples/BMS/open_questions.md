# BMS — open questions to the client, and the assumptions standing in for the answers

**Pinned input, version 1, 2026-08-20.** Consumed by every run alongside the requirement lists.

The procedure this file implements, stated by the author 2026-08-20:

> Where the RFP can be read two ways: **ask the client**; if there is no answer, **make an assumption**;
> **declare it explicitly**; and when comparing runs afterwards, **exclude the differences that come
> from it**.

An unanswered question is not a defect of the method and the disagreement it causes is not method
variance. But it is only excludable if the set of affected requirements is **fixed in advance and
shared by everybody**. Taking it from each run's own ambiguity flags does not work: a run that flags
more requirements would improve its own agreement score. So this register is an input, pinned like the
lists, and the runs' flags are evidence that it needs revising — never the filter itself.

**Status values:** `asked` — put to the client, no answer yet · `answered` — the answer is in, and the
assumption is retired · `not asked` — nobody has put it yet, and until they do the assumption stands
in for an answer nobody sought.

The RFP here is a training document with no client to ask, so every question below is `not asked` and
the assumptions are what the estimate actually rests on. In a live engagement the first move is to send
this file.

---

## The register

| # | ids | the question | reading taken | status | where declared |
|---|---|---|---|---|---|
| Q1 | R13 | Do "major disruption situations" mean IT disruption, or a travel disruption — a strike, a volcano, a hotel closing — with mass re-booking and re-routing? | technical: resilience, disaster recovery, degraded operation | not asked | `assumptions.md` A8 |
| Q2 | R14 | What is the "Admin and Support" component? The RFP names it in a diagram and gives it no content anywhere | an internal support console: incident intake, diagnostic inspection, configuration inspection | not asked | A9 |
| Q3 | R15 | "Intelligent search across multiple third-party systems" — one or two aggregator APIs, or direct integrations with many suppliers? | 1–2 aggregators | not asked | A4 |
| Q4 | R02, R03, R64 | Over what period do hosting, support and the technology-currency programme run? | none available — the term is the missing parameter, and the obligations are carried, not priced | not asked | A0, A1 |
| Q5 | R29 | "Automatic booking" — for which suppliers, and what happens when the automatic path fails? | automatic where an integration exists (R39 transport, aggregator-backed hotel); manual elsewhere per R38, R40, R48; failure falls back to the manual path | not asked | this file |
| Q6 | R05 | Is "access for the travel department, transport suppliers and employees" a capability of its own, or the umbrella over the three portals? | the umbrella; the portals realise it | not asked | this file |
| Q7 | R10 | "Clear business processes" — a property of the system, or a documentation deliverable? | a property of the system; documentation is covered by the declared documentation technology | not asked | this file, and `requirements_split.md` §3 |
| Q8 | R67 | Report generation "not excessive; criteria defined at design stage" — what are the criteria? | none pinned; the obligation is to agree them during design, and the agreeing is work | not asked | this file |
| Q9 | R11, R65, R71 | Are configurability (R11), configurability for legislative and organisational change (R65) and designed-to-grow (R71) three obligations or one stated three times? | R11 and R65 are one obligation stated twice; R71 is architectural growth and is distinct. M1 forbids merging them, so they are covered jointly and the overlap is recorded | not asked | this file |
| Q10 | R37, R38, R40, R47, R48 | "Handled manually" — must the system support the manual process with screens and records, or merely not automate it? | it supports it: forms, uploads, status records. It performs no external automation for those suppliers | not asked | this file |
| Q11 | R29, R38 | Does automatic booking (R29) reach hotels at all? R38 says hotel supplier booking is handled manually and the system performs no external automation, and the declared aggregator integration covers search only | automatic booking reaches transport (the integrated supplier) and, if the aggregator supports it, hotels; the manual path is the fallback | not asked | `assumptions_product.md` P5, and this row |

---

## How this register is used in a comparison

Every comparison of two runs is reported **twice**: over all requirements, and excluding the
requirements named in this register. The difference between the two readings is the **input-ambiguity
component** of the disagreement — a reading on the RFP, not on the method.

Measured retroactively on run 18 (`run18_product_model_pilot.md` §3d), with the runs' own flags
standing in for a register that did not exist: excluding the 19 requirements at least one run flagged
raises coverage agreement on three pairings of four — Jaccard from 0.277 to 0.362 on the closest pair
— and leaves it well below the registered 90%. **Input ambiguity is a component of the disagreement
and not the explanation of it.**

---

## What this file is not

It is not a licence to reshape the requirement list. A question here never edits an entry, never
merges two, and never removes one. If an answer arrives that changes what must be built — Q1 is the
candidate — it enters as a **new requirement**, through a deliberate revision of the list, with a new
md5 and a new N.
