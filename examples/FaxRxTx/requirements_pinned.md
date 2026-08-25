# FaxRxTx — pinned obligation list

Extracted 2026-08-22 from `SYSTEM.md` (a participant's recollection, fixed as the pipeline's input)
and `assumptions.md` (A1–A9). This list is the **external anchor** for `Hotyn-M` per
`docs/proposal_product_model.md` §3 and M1. It is the FaxRxTx analogue of the BMS act of 2026-08-19.

**A run may not add, remove, split or merge entries.** Where an entry looks like it contains two
obligations, the run flags it as ambiguous and proceeds. Revising this list is a separate, deliberate
act performed once for everybody.

---

## Granularity rule used in extraction, stated so it can be criticised

**One entry per obligation as the source words it.** Where the source states one obligation over two
objects, that is two entries only where the two objects are separately named things the system is
responsible for; where it states two obligations in one sentence ("the email is parsed, the
recipient's fax number is extracted from it"), those are two entries.

Four exclusion rules, each with its reason:

1. **Rationale and history are not obligations.** "MSMQ in the previous version broke everything",
   "the team did not know the domain", "no reference base classes", "management did not like the
   original version" are causes, not things anyone must build or do. Where such a sentence also states
   a binding constraint on the artefact ("a job queue was **not** used"), the constraint is listed and
   the history is not.
2. **Out-of-scope components are not listed as obligations, but the exchanges with them are.** The PoP
   software, the least-cost routing program and billing are excluded by `assumptions.md` A1/A4. The
   system must still receive from the PoPs (F04), hand TIFF to a PoP (F16), be routed by the ready
   router (F17) and save billing data (F41) — those are obligations on the thing being built.
3. **Uncertainty markers are kept inside the entry, not resolved.** "possibly Australia too",
   "it seems, the Black Ice driver", "the DBMS is not specified", "probably 20, maybe 16" are part of
   the input; an entry carries the hedge as the source wrote it.
4. **`REQUIREMENTS.md` is not a source.** SYSTEM.md's closing note declares it a draft of a different
   task (reception only, 100k/day, invented SLAs). Nothing in this list comes from it.

**Two entries are contentless by construction and are listed anyway**, because the source names them
and gives them no detail: **F35** (user portal) and **F21** (cluster management tool, detailed only as
"queue lengths and so on"). This is the same act as BMS R14, and it is a defect report on the input
rather than on the list.

---

## Declared processing orders

**Order A** — the order below: the source's own order, §1 → §6 → assumption log.
**Order B** — the exact reverse of A, the adversarial case.

---

## The list

| id | obligation | source |
|---|---|---|
| F01 | A worldwide fax send-and-receive service covering at least Europe and the USA *(the participant does not remember whether Australia was included)* | §1 |
| F02 | The user receives incoming faxes by email | §1 |
| F03 | The user sends outgoing faxes by emailing a special address | §1 |
| F04 | Faxes received at the points of presence arrive at the Miami data centre as TIFF files | §2.2 |
| F05 | Depending on the user's configuration, the fax is either attached to the email page by page as TIFF or converted to PDF and attached | §2.3 |
| F06 | Conversion of a received fax to PDF | §2.3 |
| F07 | Digitisation (OCR) as part of the conversion to PDF | §2.3 |
| F08 | OCR is performed on a third-party library | §2.3 / A4 |
| F09 | OCR workers carry out the digitisation | §2.3 |
| F10 | The email carrying the fax is sent to the user | §2.4 |
| F11 | Conversion and sending are carried out by workers | §2.4 |
| F12 | The email sent to the submission address is parsed | §3.1 |
| F13 | The recipient's fax number is extracted from the email | §3.1 |
| F14 | The document from the attachment is rendered to TIFF | §3.2 |
| F15 | Rendering goes through a printer driver of the Black Ice class *("it seems")* | §3.2 / A4 |
| F16 | The rendered TIFF is sent as an archive to a point of presence | §3.2 |
| F17 | Which point of presence receives the TIFF is decided by the ready least-cost routing program | §3.3 / §6 |
| F18 | Renderers for the main document formats: DOC, XLS, PPT, PDF, TXT, GIF, TIFF | §3.4 |
| F19 | On the order of 8–10 input formats in all; each format is a separate piece of integration and stabilisation work | §3.4 / A7 |
| F20 | An own cluster of Windows computers for rendering and other tasks | §4 |
| F21 | A cluster management tool — queue lengths and so on *(no further detail given anywhere in the source)* | §4 |
| F22 | No job queue (MQ) is used; MSMQ is deliberately excluded | §4 / A5 |
| F23 | A home-grown system of watchdogs and tokens (an unordered store) holds the status of each fax | §4 |
| F24 | The watchdog-and-token system resumes work if something went wrong | §4 |
| F25 | Orchestration of a large number of faxes in flight | §4 |
| F26 | The fax archive is stored on the Lustre file system | §4 |
| F27 | The working files are stored on the Lustre file system | §4 |
| F28 | A database is part of the system *(the DBMS is not specified)* | §4 |
| F29 | The components communicate through the database and an API | §4 / §6 |
| F30 | The development language is C# | §4 / A5 |
| F31 | NOC — an internal control centre | §4 |
| F32 | The NOC shows the state of the remote nodes (PoP) | §4 |
| F33 | The NOC shows the state of the cluster | §4 |
| F34 | The NOC shows the state of the queues | §4 |
| F35 | User portal — the users' website *(named in the source; no functional detail given anywhere)* | §4 |
| F36 | Nominal target volume ~1,000,000 faxes per 10-hour day (~30/s on average) | §5 / A6 |
| F37 | Burst mode of about ten times nominal (~300/s) | §5 / A6 |
| F38 | 10–20 points of presence are served | §5 |
| F39 | A render cluster of ~16–20 nodes joined by a private network | §5 |
| F40 | CDR data is saved | §6 |
| F41 | Billing data is saved *(billing itself is out of scope)* | §6 |
| F42 | Integration with the old system | §6 |
| F43 | Coexistence with the old system for the duration of the transition | §6 |
| F44 | Distribution across the cluster is a mandatory property, not an option | A6 |
| F45 | Surviving failures is a mandatory property, not an option | A6 |
| F46 | Delivery control of every fax is a mandatory property, not an option | A6 |
| F47 | The new system replaces the core functionality of the existing first version | §6 / A1 |
| F48 | A stage of domain immersion and architecture/technology selection, about 1–2 months (DHT and the like were studied) | §6 / A1 |
| F49 | Integration tests on the real message stream | §6 / A2 |
| F50 | The integration-test results are compared with the "old system" and must agree | §6 / A2 |
| F51 | Rollout to production: the new system takes production traffic in prod | A1 / A2 |
| F52 | The old version can be decommissioned | A2 |

**N = 52.**

---

## What the source states and this list deliberately does not contain

- **The PoP software** (reception and sending through the Brooktrout boards) — excluded by A1/A4;
  only F04 and F16, the exchanges with it, are listed.
- **The least-cost routing program** — excluded by A1/A4; only F17, being routed by it, is listed.
- **Billing** — excluded by A1; only F41, saving the data it consumes, is listed.
- **The first version of the system** — excluded by A1; F42, F43, F47 and F52 are the obligations the
  existing version places on the new one.
- **Post-launch operation** — excluded by A1. No entry demands hosting, support or an SLA, and none is
  invented. Note the contrast with BMS, where R02, R03 and R64 demanded exactly that: here the client
  is the same company as the team, and the source states no operating obligation at all.
- **Team composition and process** ("scrum after waterfall", QA/PM in the team, the 1–2 months of
  immersion for a team that did not know the domain) — inputs to the **technology declaration**
  (delivery-process dimension) and to the reference class, not obligations. The one exception is F48:
  the immersion **stage** is named by §6 as part of what the team did, so it is an obligation on the
  work and it is listed.
- **Calendar and headcount** — A3 removes them from the assumptions by design, and A9 makes the unit
  person-months of total effort.

---

## Pin

Recompute with:

    tr -d '\r' < examples/FaxRxTx/requirements_pinned.md | md5sum

The value is recorded in `requirements.pin.txt`, computed after this file was closed.
