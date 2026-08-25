# FaxRxTx — assumptions a product-model run may see

**Pinned input, version 1, 2026-08-22.** The projection of `assumptions.md` (A1–A9) onto the product:
only what constrains **what must exist**. The FaxRxTx analogue of `examples/BMS/assumptions_product.md`.

Why a projection and not the log itself: the log speaks about scope of effort, the definition of done,
the team, the organisation and the unit of estimation. A product-model run must not see that
vocabulary — a builder shown the language of work starts building work, and a builder shown a
duration starts estimating. What is removed is removed because it is about the doing, never because
it is inconvenient.

**Removed here, and where it lives:** the effort scope and the ~1–2 month figure attached to the
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
