# Run 29 — `Hotyn-M 1.1` × Opus 5 — FaxRxTx product model, order A, run 2 of 2

**Transcription note, recorded as a protocol fact.** The agent's first reply reached the orchestrator
**truncated**: it began part-way through §7c, so sections 1–7b were lost in transit. The agent was
resumed with a request to re-emit §6, §7 and §7b **verbatim from what it had already produced**, with
an explicit instruction not to rebuild, re-derive or revise. Sections 6, 7 and 7b below are that
re-emission; sections 7c (tail), 8 and 9 are from the original reply. Sections 2–5 (skeleton log,
accretion log, completion log, convergence trace) **were not recovered** and are absent from this
record. The instrument readings, which are what the pair measurement consumes, are intact.

Inputs: identical to run 1 — `requirements_product.md` (md5 `306046dc6cab35147040224e7a4e9662`,
N = 47) + `assumptions_product.md` v1, pasted in full, order A. `tool_uses: 0`.

---

## 6. Final model (frozen, post-normalisation — 87 nodes)

Provenance: origin label (M4) with its stated/implied reading — `accreted` = stated,
`posited`/`derived` = implied.

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM2-01 | Fax service system (new core version) | — | posited (implied) | — |
| HM2-02 | Inbound fax path | HM2-01 | posited (implied) | F47 (part: the receive-and-deliver-by-email core function of the first version is present in the new artefact) |
| HM2-03 | Outbound fax path | HM2-01 | posited (implied) | F47 (part: the submit-by-email-and-send core function of the first version is present) |
| HM2-04 | Document rendering subsystem | HM2-01 | posited (implied) | — |
| HM2-05 | Fax state, orchestration and recovery mechanism | HM2-01 | posited (implied) | — |
| HM2-06 | Cluster and execution platform | HM2-01 | posited (implied) | — |
| HM2-07 | Storage, data and internal interfaces | HM2-01 | posited (implied) | — |
| HM2-08 | External exchange surfaces | HM2-01 | posited (implied) | — |
| HM2-09 | NOC | HM2-01 | posited (implied) | — |
| HM2-10 | User portal | HM2-01 | posited (implied) | — |
| HM2-11 | Accounting records | HM2-01 | posited (implied) | — |
| HM2-12 | Old-system integration and coexistence | HM2-08 | posited (implied) | — |
| HM2-13 | Access control and identity | HM2-01 | posited (implied) | — |
| HM2-14 | PoP footprint and endpoint registry | HM2-08 | accreted (stated) | F01 (part: the served reach — PoP endpoints in Europe and the USA), F38 (part: the 10–20 PoPs are known and addressable) |
| HM2-15 | Inbound fax intake service (DC-side reception from PoPs) | HM2-02 | accreted (stated) | F01 (part: the receive direction of the service is offered here), F04 (part: faxes from the PoPs are received at the Miami data centre as TIFF), F38 (part: faxes are received from each served PoP) |
| HM2-16 | Fax submission mail endpoint (the special address) | HM2-03 | accreted (stated) | F01 (part: the send direction of the service is offered here), F03 (part: the special address receives the user's mail) |
| HM2-17 | Recipient account and delivery-address resolution | HM2-02 | accreted (stated) | F02 (part: the received fax is directed to the right user's email address) |
| HM2-18 | Delivery email assembly | HM2-02 | accreted (stated) | F02 (part: the fax is packaged as an email to the user), F10 (part: the email carrying the fax is composed) |
| HM2-20 | Outbound job creation from a submission mail | HM2-03 | accreted (stated) | F03 (part: the received mail becomes an outgoing fax job) |
| HM2-21 | Received-fax landing and registration | HM2-02 | accreted (stated) | F04 (part: the received TIFF is landed and registered as an identified fax at the data centre) |
| HM2-22 | Delivery format selection | HM2-02 | accreted (stated) | F05 (part: the branch between page-by-page TIFF and converted PDF is taken from the user's configuration) |
| HM2-23 | Page-by-page TIFF attachment assembly | HM2-18 | accreted (stated) | F05 (part: the TIFF branch — each page attached as TIFF) |
| HM2-24 | PDF attachment assembly | HM2-18 | accreted (stated) | F05 (part: the PDF branch — the converted PDF attached) |
| HM2-25 | User delivery-preference configuration store | HM2-07 | accreted (stated) | F05 (part: the user's configuration is held where the delivery path reads it) |
| HM2-26 | Received-fax conversion to PDF | HM2-02 | accreted (stated) | F06 (whole) |
| HM2-27 | Digitisation step within the conversion | HM2-26 | accreted (stated) | F07 (whole) |
| HM2-28 | Third-party OCR library adapter | HM2-27 | accreted (stated) | F08 (whole) |
| HM2-29 | OCR worker | HM2-27 | accreted (stated) | F09 (whole), F11 (part: the digitisation stage of the conversion is carried out by a worker) |
| HM2-30 | Conversion worker | HM2-26 | accreted (stated) | F11 (part: conversion is carried out by a worker) |
| HM2-31 | Sending worker (delivery email dispatch) | HM2-02 | accreted (stated) | F11 (part: sending is carried out by a worker), F02 (part: the email reaches the user's mailbox), F10 (part: the email is sent to the user) |
| HM2-33 | Submission mail parsing and recipient fax-number extraction | HM2-03 | accreted (stated) | F13 (whole), F12 (whole: the mail sent to the submission address is parsed) |
| HM2-34 | Render service (document in, fax-ready TIFF out) | HM2-04 | accreted (stated) | F14 (part: the attachment document is taken in and a TIFF comes back) |
| HM2-36 | Fax-image production through a Black Ice class print driver | HM2-04 | accreted (stated) | F15 (whole), F14 (part: the document is actually rendered into TIFF pages) |
| HM2-37 | Outbound archive packaging | HM2-03 | accreted (stated) | F16 (part: the rendered TIFF is packed as the archive a PoP takes) |
| HM2-38 | PoP handoff transfer | HM2-08 | accreted (stated) | F16 (part: the archive is delivered to the chosen point of presence), F38 (part: outgoing archives are delivered to each served PoP) |
| HM2-39 | Least-cost-routing integration | HM2-08 | accreted (stated) | F17 (whole) |
| HM2-40 | Format renderer set | HM2-04 | accreted (stated) | — |
| HM2-41 | DOC renderer | HM2-40 | accreted (stated) | F18 (part: DOC), F19 (part: DOC separately integrated and stabilised) |
| HM2-42 | XLS renderer | HM2-40 | accreted (stated) | F18 (part: XLS), F19 (part: XLS separately integrated and stabilised) |
| HM2-43 | PPT renderer | HM2-40 | accreted (stated) | F18 (part: PPT), F19 (part: PPT separately integrated and stabilised) |
| HM2-44 | PDF renderer | HM2-40 | accreted (stated) | F18 (part: PDF), F19 (part: PDF separately integrated and stabilised) |
| HM2-45 | TXT renderer | HM2-40 | accreted (stated) | F18 (part: TXT), F19 (part: TXT separately integrated and stabilised) |
| HM2-46 | GIF renderer | HM2-40 | accreted (stated) | F18 (part: GIF), F19 (part: GIF separately integrated and stabilised) |
| HM2-47 | TIFF renderer | HM2-40 | accreted (stated) | F18 (part: TIFF), F19 (part: TIFF separately integrated and stabilised) |
| HM2-48 | Renderer registry and format extension point | HM2-40 | accreted (stated) | F19 (part: the set reaches the stated ~8–10 input formats, including those the source could not name) |
| HM2-49 | Per-format integration and stabilisation harness | HM2-40 | accreted (stated) | F19 (part: each format carries its own integration and stabilisation fixture) |
| HM2-51 | Cluster management console | HM2-06 | accreted (stated) | — |
| HM2-52 | Node state view and node control actions | HM2-51 | accreted (stated) | F21 (part: node state shown; a node can be taken out, put back, its work redistributed), F33 (part: the state of the cluster's nodes is displayed to operators — joint with F21 per P5) |
| HM2-53 | Queue-length view | HM2-51 | accreted (stated) | F21 (part: queue lengths shown), F34 (part: the state of the queues is displayed to operators — joint with F21 per P5) |
| HM2-54 | Queue-free job dispatch (token claim, no MQ) | HM2-05 | accreted (stated) | F22 (whole), F25 (part: work for many faxes is handed to workers without a broker), F44 (part: any free node claims the next piece of work) |
| HM2-55 | Fax status token store (unordered) | HM2-05 | accreted (stated) | F23 (whole), F46 (part: every fax carries a status record that can be controlled against) |
| HM2-56 | Watchdog over tokens | HM2-05 | accreted (stated) | F24 (part: what went wrong is detected), F45 (part: failures are detected rather than assumed away) |
| HM2-57 | Resume and re-dispatch of interrupted work | HM2-05 | accreted (stated) | F24 (part: work is resumed), F45 (part: interrupted work continues after a failure) |
| HM2-58 | Fax lifecycle progression driver | HM2-05 | accreted (stated) | F25 (part: each of a large number of faxes advances through its stages concurrently) |
| HM2-59 | Fax archive store on Lustre | HM2-07 | accreted (stated) | F26 (whole) |
| HM2-60 | Working file store on Lustre | HM2-07 | accreted (stated) | F27 (whole) |
| HM2-61 | System database schemas | HM2-07 | accreted (stated) | F28 (whole), F29 (part: components hand work over through the database) |
| HM2-62 | Internal component API | HM2-07 | accreted (stated) | F29 (part: components call one another through an API) |
| HM2-64 | NOC shell and operator workspace | HM2-09 | accreted (stated) | F31 (whole) |
| HM2-65 | PoP state view (NOC) | HM2-09 | accreted (stated) | F32 (whole) |
| HM2-66 | Cluster and backlog telemetry feed | HM2-06 | accreted (stated) | F33 (part: the cluster's state is acquired from the nodes), F34 (part: per-stage backlog figures are acquired from the token store) |
| HM2-67 | NOC cluster state panel | HM2-09 | accreted (stated) | F33 (part: the control centre shows the state of the cluster) |
| HM2-68 | NOC queue state panel | HM2-09 | accreted (stated) | F34 (part: the control centre shows the state of the queues) |
| HM2-69 | Portal web application | HM2-10 | accreted (stated) | F35 (part: the customer-facing web area exists and the user reaches it) |
| HM2-70 | Delivery configuration area (portal) | HM2-10 | accreted (stated) | F35 (part: the user administers their own delivery configuration) |
| HM2-71 | Own fax status and history view (portal) | HM2-10 | accreted (stated) | F35 (part: the user sees the status and history of their own faxes) |
| HM2-72 | Pipeline capacity dimensioning and worker allocation | HM2-06 | accreted (stated) | F36 (whole), F37 (part: the sizing frame within which burst headroom is allocated) |
| HM2-73 | Burst absorption and admission control | HM2-05 | accreted (stated) | F37 (part: about ten times nominal is accepted, held and drained with no broker beneath) |
| HM2-74 | Cluster roster and private-network topology (own Windows machines) | HM2-06 | accreted (stated) | F20 (whole), F39 (whole: ~16–20 render nodes, own machines, joined by a private network) |
| HM2-75 | CDR writer and CDR store | HM2-11 | accreted (stated) | F40 (whole) |
| HM2-76 | Billing data extract and store | HM2-11 | accreted (stated) | F41 (whole) |
| HM2-77 | Old-system exchange interface | HM2-12 | accreted (stated) | F42 (whole), F43 (part: the two systems exchange while both run) |
| HM2-78 | Transition coexistence arrangement | HM2-12 | accreted (stated) | F43 (part: which faxes and users each system serves during the transition, and shared access to PoPs and archive) |
| HM2-79 | Work distribution across the cluster | HM2-06 | accreted (stated) | F44 (part: every stage's work spreads over the roster; no stage bound to one node) |
| HM2-80 | Node loss handling and work redistribution | HM2-06 | accreted (stated) | F45 (part: the loss of a cluster node is survived and its work re-dispatched) |
| HM2-81 | Idempotent re-processing safeguards | HM2-05 | accreted (stated) | F45 (part: recovery neither duplicates nor drops a fax) |
| HM2-82 | Delivery confirmation and non-delivery handling | HM2-05 | accreted (stated) | F46 (part: the terminal delivery of each fax is confirmed and an unconfirmed fax is raised) |
| HM2-83 | Portal user authentication and session | HM2-13 | derived (implied) | — |
| HM2-84 | NOC operator authentication and roles | HM2-13 | derived (implied) | — |
| HM2-85 | Non-delivery notification to the user | HM2-05 | derived (implied) | — |
| HM2-86 | Retention and purge of archive and working files | HM2-07 | derived (implied) | — |
| HM2-87 | Component deployment and configuration distribution | HM2-06 | derived (implied) | — |
| HM2-88 | Subscriber and fax-number directory | HM2-07 | derived (implied) | — |
| HM2-89 | Logging and diagnostic trace (host of the shared C#/.NET component framework) | HM2-06 | derived (implied) | F30 (whole — carried across at normalisation from HM2-63) |
| HM2-90 | Cluster clock discipline | HM2-06 | derived (implied) | — |
| HM2-91 | Portal credential recovery | HM2-13 | derived (implied) | — |
| HM2-92 | Component version consistency across nodes | HM2-06 | derived (implied) | — |

Parent check at every aggregate holds: each parent's total coverage equals the union of its children's
totals plus its own residue; the only residues declared at aggregates are F47 at HM2-02 and HM2-03,
and no child of either realises F47.

## 7. Empty skeleton nodes (total coverage empty at accretion convergence)

| node | name | verdict |
|---|---|---|
| HM2-13 | Access control and identity | **genuine infrastructure that no requirement names** — kept. A portal scoped to "their own faxes" and a control centre whose actions take cluster nodes out of service both presuppose identity and authorisation, and the pinned list names neither. It is the only posited node whose whole subtree covered nothing at accretion convergence, and its subtree is entirely derived (HM2-83, HM2-84, HM2-91) |

All other posited nodes ended with non-empty *total* coverage. The test was not applied to own
coverage: eleven of the thirteen posited nodes hold no own coverage by rule, and two accreted
aggregates (HM2-40 format renderer set, HM2-51 cluster management console) likewise hold none — none
of these are findings.

## 7b. Normalisation log (closure step 2)

| collapsed node | name (retired label) | merged into | coverage carried across | new parent of the surviving leaf |
|---|---|---|---|---|
| HM2-19 | Delivery email dispatch | HM2-31 (Sending worker) | F02 (part: the email reaches the user's mailbox), F10 (part: the email is sent) | HM2-02 |
| HM2-32 | Submission mail parsing | HM2-33 (Recipient fax-number extraction) | F12 (whole) | HM2-03 |
| HM2-35 | Fax-image production | HM2-36 (Black Ice class print-driver integration) | F14 (part: the document is actually rendered into TIFF pages) | HM2-04 |
| HM2-50 | Windows cluster estate | HM2-74 (Cluster roster and private-network topology) | F20 (whole), F39 (part: the render machines are our own) — merging with HM2-74's F39 part, so F39 now sits whole on one node and the assignment count drops by one | HM2-06 |
| HM2-63 | Shared C#/.NET component framework and service host | HM2-89 (Logging and diagnostic trace) | F30 (whole) | HM2-06 |

Five collapses. The last is the case the instrument section anticipates: a **stated** node merged into
a **derived** leaf, so the post-normalisation provenance counts no longer coincide with the
pre-normalisation ones and the counts in §8 are taken before normalisation.

## 7c. Coverage completeness — tail of the table as received

| req | covering nodes and the part each realises | verdict |
|---|---|---|
| F45 | … survived and work redistributed · HM2-81 recovery neither duplicates nor drops | **whole** |
| F46 | HM2-55 every fax carries a controllable status record · HM2-82 terminal delivery confirmed, unconfirmed faxes raised | **whole** |
| F47 | HM2-02 the receive-and-deliver-by-email core of the first version present in the artefact · HM2-03 the submit-by-email-and-send core present | **whole** (under the reading recorded in §9) |

47 of 47 obligations asserted **whole**. No id is held by no node; no residue was left unclosed; there
is no list of unplaceable requirements because there are none.

*(Rows F01–F44 of this table were lost to the truncation and were not re-requested; the summary line
above is the run's own.)*

## 8. Instrument readings

**Engine: `Hotyn-M 1.1`.**

| reading | value |
|---|---|
| node count before normalisation | 92 |
| node count after normalisation | 87 |
| provenance counts, taken **before** normalisation | posited 13 · accreted 69 · derived 10 |
| derived fraction (before normalisation) | 10 of 92 |
| skeleton size | 13 |
| skeleton nodes ending with empty **total** coverage at accretion convergence | 1 (HM2-13) |
| accreted nodes holding no own coverage (not a finding; recorded for contrast) | 2 (HM2-40, HM2-51) |
| nodes collapsed at closure | 5 |
| passes to convergence — skeleton | 1 |
| passes to convergence — accretion | 2 (pass 2 added nothing, deferred nothing) |
| passes to convergence — completion | 3 (8 + 2 + 0) |
| deferrals, all passes | 0 |
| coverage assignments (id-at-node pairs), before normalisation | 96 |
| coverage assignments, after normalisation | 95 (the HM2-50→HM2-74 collapse merged F39's two parts onto one node) |
| nodes carrying at least one id (before normalisation) | 69 of 92 |
| nodes per requirement | min 1 · max 9 (F19) · 96 assignments over 47 obligations |
| requirements per node (of the 69 carrying nodes) | 1 id: 44 nodes · 2 ids: 23 nodes · 3 ids: 2 nodes (HM2-15, HM2-54) |
| ambiguity flags — entry holding two obligations | 1 (F19) |
| ambiguity flags — overlap between entries, covered jointly, not merged | 3 ids in one trio (F21 ↔ F33, F21 ↔ F34) |
| ambiguity flags — source hedges recorded without structural effect | 3 (F01 Australia, F15 "it seems", F28 DBMS unnamed) |
| ambiguity flags — contentless entries carrying assumed content from P4 | 2 (F21, F35) |
| completion-covers-a-requirement defects | 0 |
| partial marks standing at closure | **0** |
| numbers of effort, size, duration or cost emitted | 0 |

## 9. Assumption log

**Nothing was left unplaced.** There is no unplaceable-requirement list.

**Entries flagged ambiguous, verbatim:** F19 (a count of the format set and a property of how each
format is built; covered as two parts at HM2-48 and at HM2-49 plus each of HM2-41…HM2-47; the entry
was not split) · F21 and F35 (contentless; content taken from P4 only) · the F21 / F33 / F34 overlap
(covered jointly per P5: HM2-52 carries F21 and F33, HM2-53 carries F21 and F34, and the acquisition
of the underlying state is a single node, HM2-66, feeding both surfaces; no entry merged) · F01's
Australia hedge (read as reach; no per-region structure, and the hedge produced no missing branch) ·
F15's "it seems" (the hedge is on the driver's class, not on whether rendering goes through a driver)
· F28's unnamed DBMS (modelled as schemas the system owns; no DBMS is a node).

**Where the run interpreted rather than read:**

1. **F47 declared as residue on two aggregates.** No child node realises "being the replacement", so
   it could not be declared at a leaf; declared as own residue at HM2-02 and HM2-03, reading "core
   functionality" as the two fax paths. **The only place in this model where an aggregate holds own
   coverage.** If a reader takes "core functionality" to include the portal or the NOC, F47's parts
   would have to be extended — a reading of the source, not a defect of the structure.
2. **F01 split across three nodes** — reach at the PoP footprint, each direction at the point where
   that direction is offered to the user.
3. **F36, F37, F44, F45, F46 are properties, and each was given a realising node rather than a note**
   (HM2-72, HM2-73, HM2-79, HM2-80, HM2-81, HM2-82), on P3's instruction that nothing underneath
   provides these for free. F36/F37/F39's numbers stay in the requirement text, never in a node.
4. **"Queues" means per-stage backlog in the token store**, since F22 excludes any broker. Nothing in
   the model is an MQ.
5. **"Workers" read as components, per P5** — HM2-29, HM2-30, HM2-31 are processes.
6. **Renderers modelled one node per named format**, because A7 makes per-format integration
   structural. The seven named formats only; the unnamed remainder is held by an extension point
   (HM2-48), not by invented format nodes.
7. **P1 boundary respected and checked.** No fax-board driver, no routing algorithm, no billing engine
   exists as a node.
8. **A cost of normalisation, recorded rather than avoided.** The collapse of HM2-63 into HM2-89
   retires the label "Shared C#/.NET component framework and service host" and leaves F30 sitting on a
   node named for logging. Names are labels and never identity (M2), and the retired label survives in
   §7b — but a reader of the final tree alone would lose it. Structure was not added to prevent the
   collapse, as M7 forbids exactly that.
9. **Derived nodes are conservative but not minimal.** Ten completion nodes, two of them second-pass.
   HM2-88 (subscriber and fax-number directory) and HM2-85 (non-delivery notification) are the two
   judged closest to the accretion boundary; both cover nothing, so neither is a
   completion-covers-a-requirement defect.
