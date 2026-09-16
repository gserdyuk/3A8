Build the product model of the system whose obligations are listed below. Everything you need is in this message; read no files.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Declared processing order: Order A** — the order of INPUT 1 as given, F01 first, F47 last.

**Output.** Emit the complete deliverable in one reply, beginning at section 1 and ending at section 9, with every section your engine definition requires.

---

# INPUT 1 — the pinned product obligation list (`requirements_product.md`, N = 47), verbatim

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

---

# INPUT 2 — the assumption log a product-model run may see (`assumptions_product.md`), verbatim

# FaxRxTx — assumptions a product-model run may see

**Pinned input, version 1, 2026-08-22.** The projection of `assumptions.md` (A1–A9) onto the product:
only what constrains **what must exist**. The FaxRxTx analogue of `examples/BMS/assumptions_product.md`.

Why a projection and not the log itself: the log speaks about scope of effort, the definition of done,
the team, the organisation and the unit of estimation. A product-model run must not see that
vocabulary — a builder shown the language of work starts building work, and a builder shown a
duration starts estimating. What is removed is removed because it is about the doing, never because
it is inconvenient.

**Removed here, and where it lives:** the effort scope and [struck by the orchestrator: a figure] attached to the
immersion stage (A1 — the stage is an obligation on the **work**, F48, and is not in your list) · the
definition of done (A2) · the team and its composition (A3) · the organisational context (A8) · the
unit of estimation and its conversions (A9). None of them says anything about what the product is.

---

## P1. Scope of the thing being modelled

The **new version** of the core system, covering every obligation in `requirements_product.md`
(N = 47). A first version of the system already runs; what is modelled is the replacement of its core
functionality (F47), not the first version.

**The following are not part of the product and are not in your list:** the software on the points of
presence (reception and sending through the fax boards), the least-cost routing program, and billing.
They are existing, working things. The system's obligations *towards* them — receiving from a PoP
(F04), handing a TIFF to a PoP (F16), being routed by the router (F17), saving the data billing
consumes (F41) — are in the list and are exchanges, not components.

If your structure seems to need a fax board driver, a routing algorithm or a billing engine as a
component, that is the signal you have crossed out of the product; say so rather than building it.

## P2. External and pre-existing things the system integrates with

Each is **used, not built**. Model the exchange, never the thing.

- **The points of presence** — geographically distributed nodes at telecom providers, 10–20 of them
  (F38), with working software already installed. They deliver received faxes to the data centre and
  accept outgoing ones.
- **The least-cost routing program** (F17) — ready and reused; it decides which PoP receives an
  outgoing TIFF.
- **A third-party OCR library** (F08) — digitisation is obtained from it, not written.
- **A printer driver of the Black Ice class** (F15) — rendering to TIFF is obtained through it.
- **The Lustre file system** (F26, F27) — existing storage infrastructure. The system stores the fax
  archive and its working files on it; it does not build a file system.
- **A database platform** (F28) — the DBMS is not named in the source and is not to be guessed. Read
  it as *a database the system owns schemas in*; do not model the DBMS itself.
- **The old system** (F42, F43) — the running first version. The new system exchanges with it and
  runs alongside it for the transition.

## P3. The era, as it bears on structure

The stack is C#/.NET of the 2007–2009 generation on the company's own hardware. There is **no cloud
and no ready orchestrator**, and by an explicit decision **no message queue at all** (F22): what a
broker would provide is built by hand as the watchdog-and-token mechanism (F23, F24, F25). Read this
as structural, not as a background note — distribution across the cluster (F44), surviving failures
(F45) and delivery control of every fax (F46) are mandatory properties of the thing, and nothing
underneath provides them for free.

## P4. F21 and F35 — the two contentless entries, and their assumed content

The source names both and gives neither any detail. Assumed content, so that the model has something
to be a model *of*:

- **F21, the cluster management tool:** an operator-facing view and control of the render cluster —
  queue lengths, the state of the nodes, and the ability to act on a node (take it out, put it back,
  redistribute what it was doing). **Not** a general infrastructure product, **not** a monitoring
  suite, **not** a deployment tool.
- **F35, the user portal:** the customer-facing web area where a user administers their own service —
  the delivery configuration that F05 reads (TIFF page-by-page or converted PDF), and the status and
  history of their own faxes. **Not** a marketing site, **not** a billing or payment area (billing is
  out of scope), **not** a staff console — the staff-facing view is the NOC, F31–F34.

## P5. Readings taken where an entry can be read two ways

| ids | reading taken |
|---|---|
| F01 | "at least Europe and the USA (possibly Australia)" is a statement about **reach**, not a structural axis. Do not build a per-region variant of anything, and do not treat the Australian hedge as a missing branch |
| F09 F11 | "workers" names **components of the system** — processes doing conversion, OCR and sending on the cluster — not people and not job titles |
| F18 F19 | the renderer set covers the **seven named formats** (DOC, XLS, PPT, PDF, TXT, GIF, TIFF); the source says the true count is on the order of 8–10 and that it may have forgotten some. **Do not invent named formats.** Per A7, each format is separately integrated and separately stabilised — that is a property of how the renderer set is built, and it belongs in the structure |
| F21 F33 F34 | these overlap: the cluster management tool shows queue lengths, and the NOC is stated to show the state of the cluster and of the queues. The source says both and distinguishes neither. **You may not merge entries** (M1) — cover them jointly where they genuinely coincide and record the overlap as an ambiguity |
| F23 F24 F25 | the watchdog-and-token mechanism is **one mechanism with three stated obligations** — holding the status of every fax, resuming what failed, and orchestrating a large number in flight. It is the system's own replacement for a message queue |
| F26 F27 | two distinct responsibilities on one piece of infrastructure: the long-lived fax archive, and the short-lived working files of jobs in flight |
| F40 F41 | CDR and billing data are **written and kept** by this system; what consumes them is not |
| F36 F37 F38 F39 | the scale figures are **properties the design must meet**, not components. ~1M faxes per 10-hour day nominal, about ten times that in burst, 10–20 PoPs, a private-network cluster of ~16–20 nodes |
| F47 | "replaces the core functionality of the first version" is a **scope statement on the artefact** — what must be in it — not a project goal and not a migration |

## Pin

    tr -d '\r' < assumptions_product.md | md5sum

Parents: `assumptions.md` (A1–A9), `requirements_product.md`
(md5 `306046dc6cab35147040224e7a4e9662`, N = 47).
