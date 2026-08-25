# FaxRxTx — product obligation list (`Hotyn-M` input)

Derived from `requirements_pinned.md` (N = 52) by the split recorded in `requirements_split.md`. Five
entries — F48, F49, F50, F51, F52 — are obligations on the **work** and live in
`requirements_work.md`. **Ids are unchanged**, so the two lists together are exactly the pinned list
and every id still means what it meant.

This is the **external anchor** for `Hotyn-M` per `docs/proposal_product_model.md` §3 and M1.

**A run may not add, remove, split or merge entries.** Where an entry looks like it contains two
obligations, the run flags it as ambiguous and proceeds. Revising this list is a separate, deliberate
act performed once for everybody.

Granularity rule inherited from `requirements_pinned.md`: **one entry per obligation as the source words it.**

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

**N = 47.**

## Order

**Order A** — the order above (the source's own order). **Order B** — its exact reverse.
