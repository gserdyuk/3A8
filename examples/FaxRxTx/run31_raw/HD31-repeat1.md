# Run 31 — `Hotyn-D 2.0` × Opus 5 — FaxRxTx size classification, **repeat 1** (batches A, B, C)

Transcribed from the three agents' replies. Inputs: the elements of `HM29-OA1` as classified by
`HW30-A1/B1/C1`, plus catalogue 1.4 §3a sizing rules and precedents P-1…P-6. `tool_uses: 0` in all
three. All three quarantined the harness-injected git status and read no file.

---

## Batch A — 28 elements (7 interface, 21 behaviour)

**Contamination check.** Clean. Two numeric expressions checked and cleared: "8–10 input formats" (a
count of things, the engine's own currency) and "C#/.NET of the 2007–2009 generation" (a technology
generation label). Ambient repository information quarantined.

| id | class | enumeration (verbatim) | n | size |
|---|---|---|---|---|
| HM1-23 | interface | 3 operations: dispatch the composed email carrying the fax to the user's address; the outbound email channel itself (gateway contract and message format) — counted per P-1; the worker-facing invocation of the send path, named by F11 and covered by no other obligation | 3 | **M** |
| HM1-25 | interface | 2 operations: accept an incoming TIFF file arriving from a point of presence; the point-of-presence → Miami data-centre transport channel, counted as a delivery channel per P-1 | 2 | **M** |
| HM1-24 | interface | 2 operations: collect mail arriving at the special submission address; the inbound mailbox channel itself (mailbox protocol and message format), per P-1 | 2 | **M** |
| HM1-31 | interface | 2 operations: invoke recognition on the third-party library for a page image (F08); bind and load the third-party library into the process (interop contract) — the name token "binding" is covered by no obligation, counted per P-2 | 2 | **M** |
| HM1-38 | interface | 2 operations: submit a print job to the printer driver; capture the file the driver produces — the two ends of the "path" named in the element | 2 | **M** |
| HM1-39 | interface | 2 operations: send the rendered TIFF to a point of presence; the point-of-presence transport channel, whose own substance includes the archive format (P-1 states formats are the channel's substance, so the archive form is not counted a second time) | 2 | **M** |
| HM1-90 | interface | 3 operations: launch or attach a driven application session; open the office document inside that session; drive the print action from the application through the printer driver | 3 | **M** |
| HM1-26 | behaviour | 3 actions: read the user's delivery-format configuration; route to the page-by-page TIFF outcome; route to the PDF outcome — the two outcomes of "either … or" counted as distinct per P-3 | 3 | **M** |
| HM1-27 | behaviour | 2 actions: split the received fax into its pages; attach each page to the email as a TIFF | 2 | **M** |
| HM1-28 | behaviour | 1 action: attach the converted PDF to the email — the conversion that produces it is covered by HM1-29 (F06), so not counted here per P-2 | 1 | **S** |
| HM1-86 | behaviour | 2 actions: attribute the received fax to an owning user; resolve that user's email address so the message can be addressed | 2 | **M** |
| HM1-35 | behaviour | 2 actions: parse the email sent to the submission address (headers and body); extract the attached document from the parsed message — extraction is covered by no other obligation (P-2) | 2 | **M** |
| HM1-36 | behaviour | 1 action: extract the recipient's fax number from the email | 1 | **S** |
| HM1-88 | behaviour | 2 actions: attribute mail arriving at the public address to an account; gate the submission on that attribution before a fax leaves on the account's behalf | 2 | **M** |
| HM1-89 | behaviour | 2 actions: compose a notification of the determined outcome; deliver it to the submitter by email — the email channel is not counted here, P-1 being scoped to interface elements | 2 | **M** |
| HM1-29 | behaviour | 2 actions: convert the received fax to PDF (F06, and the conversion the PDF branch of F05 needs); carry out that conversion as a worker-pool job (F11), covered by no other obligation | 2 | **M** |
| HM1-30 | behaviour | 2 actions: digitise the page image by OCR (F07); carry out that digitisation as an OCR-worker job (F09) — the library call itself is covered by HM1-31 (P-2) | 2 | **M** |
| HM1-37 | behaviour | 1 action: render the document to TIFF (F14) — obtaining the document from the attachment is counted at HM1-35, and choosing the renderer for the format is counted at HM1-49 (P-2) | 1 | **S** |
| HM1-97 | behaviour | 4 actions: detect a hung driven application session; isolate the session so a hang does not spread past its node (name token, covered by no obligation — P-2); restart the node's session to recover it; preserve and resume the fax so it is not lost across the recovery | 4 | **L** |
| HM1-41…47 | behaviour | 1 action each: render a DOC / XLS / PPT / PDF / TXT / GIF / TIFF input to TIFF | 1 | **S** ×7 |
| HM1-48 | behaviour | 2 actions: integrate a format into the render path; stabilise that format's rendering output — F19 names exactly these two kinds of work per format. The number of formats is multiplicity, not a counted action | 2 | **M** |
| HM1-49 | behaviour | 2 actions: register a renderer for a format; resolve the renderer for an input format at run time so the set stays open beyond the seven named ones | 2 | **M** |

**Unsizeable: none.** One near-miss recorded rather than suppressed: HM1-48 stands close to P-6,
because "on the order of 8–10 input formats in all" is a cardinality whose last one to three members
are never named. It is sized only because the counted thing for a `behaviour` is *actions*, not
formats. Had formats been the counted thing, P-6 would have made this element unsizeable.

**Doubts: 23** (20 element-level, 3 contradictions). Class-changing ones: HM1-25 (channel counted under
P-1; without it S), HM1-31 ("binding" counted under P-2; folded in, S), HM1-38 (output capture counted;
folded in, S), HM1-27 ("page by page" as a split; as a qualifier, S), HM1-28 ("assembly" not counted;
counted, M), HM1-86, HM1-35 (extraction placed here; if in F12 alone, S), HM1-88, HM1-89, HM1-29 and
HM1-30 (F11/F09's "carried out by workers" counted as an action; read as naming only the executor, S),
HM1-97 ("isolation" counted; without it M). Contradictions named and not resolved: **F05 against F06**
(F05 makes the PDF conversion conditional, F06 states it unconditionally) · **F18 against F19** (seven
formats named, "8–10 in all" asserted) · **F11 against the pinned "no message queue at all"** (work is
carried out by workers, and how work reaches a worker is undeclared — which is what makes the
worker-invocation doubts arguable).

**Closure violations: 4.** Disposition of an inbound fax that cannot be attributed to an owning user ·
determination of the outbound send outcome (HM1-89 presupposes "a determined outcome"; nothing in
batch A receives an acknowledgement from a point of presence) · integration of the formats beyond the
seven named · the user configuration HM1-26 reads (no store for it in this batch).

**Readings.** Elements received 28 · sized 28 · **S 10 · M 17 · L 1 · XL 0** · statements 0 ·
unsizeable 0 · doubts 23 · closure violations 4.

---

## Batch B — 21 elements (14 behaviour, 5 store, 2 statement)

**Contamination check.** Clean. "~16–20 nodes" checked and cleared as a count of machines, not a team
size — and flagged as a cardinality without named members, so P-6 bars its use as an enumeration.

| id | class | enumeration (verbatim) | n | size |
|---|---|---|---|---|
| HM1-32 | behaviour | 1 action: digitise the fax image (F09). The name token "OCR" is covered by that same obligation and is not counted again (P-2) | 1 | **S** |
| HM1-33 | behaviour | 1 action: convert a fax document to its delivery form (F11, conversion half). *[Corrected in place by the run: the first draft read M; the two delivery forms belong to HM1-87's declaration, not this one, and were not imported]* | 1 | **S** |
| HM1-34 | behaviour | 1 action: send a fax to its destination (F11, sending half) | 1 | **S** |
| HM1-50 | behaviour | 2 actions: run a node's assigned rendering work on a cluster machine (F20); join a machine to the cluster and hold its membership (F39). "and other tasks" is an unnamed catch-all and is not counted (P-5) | 2 | **M** |
| HM1-53 | behaviour | 1 action: hand a fax over to a worker without a broker (F25). F22 is a prohibition and names no verb on object; claiming is HM1-58's declared content | 1 | **S** |
| HM1-55 | behaviour | 2 actions: maintain (write) each fax's status token as the fax progresses (F23); sweep the token store on a cycle (F24) | 2 | **M** |
| HM1-56 | behaviour | 2 actions: detect that a fax's work has failed or stalled (F24); resume the work by re-dispatching the fax (F24/F45) | 2 | **M** |
| HM1-57 | behaviour | 1 action: move a fax from its current stage to the next one (F25). Arguable: neither the stages nor the transitions are named individually, so this is the only action nameable without guessing | 1 | **S** |
| HM1-58 | behaviour | 4 actions: claim a fax for a node; hold and expire a lease on that claim (P-3, slash-separated, covered by no obligation so P-2 counts them from the name); hold the in-flight population at its concurrency limit (F25); spread claimable work across the cluster nodes (F44) | 4 | **L** |
| HM1-82 | behaviour | 2 actions: determine the outcome of a fax's delivery attempt; confirm and record that outcome against the fax (F46) | 2 | **M** |
| HM1-83 | behaviour | — | — | **unsizeable (M10)** |
| HM1-85 | behaviour | 1 action: issue a per-fax identifier. "token, archive, CDR and coexistence" are named consumers, not actions of this element | 1 | **S** |
| HM1-92 | behaviour | 1 action: suppress a second delivery of a fax that is re-dispatched | 1 | **S** |
| HM1-93 | behaviour | 1 action: reclaim a fax's working files when the fax reaches an outcome | 1 | **S** |
| HM1-54 | store | 1 entity kind: the per-fax status token (F23). F25's "in-flight population materialised" and F46's "every fax's status is held" are the same kind seen as a set and as a guarantee (P-2) | 1 | **S** |
| HM1-59 | store | 1 entity kind: the archived fax (F26). Lustre is used, not built | 1 | **S** |
| HM1-60 | store | 1 entity kind: the working file (F27). F27 differentiates no sub-kinds | 1 | **S** |
| HM1-61 | store | — | — | **unsizeable (M10)** |
| HM1-87 | store | 1 entity kind: the per-user delivery-format setting (the choice between page-by-page TIFF and converted PDF) | 1 | **S** |
| HM1-75 | statement · **compliance** (*"joined by a private network"* — a network configuration, no run-time scenario) | — | — | **unsizeable (M10)** |
| HM1-94 | statement · **behavioural** (*"elapsed-time stall detection … require an agreed clock"* — a run-time scenario; P-4) | 2 components: the elapsed-time stall detection that compares times across machines; the cluster machines that write records | 2 | **M** |

**Special count — entity kinds needing pre-load.** HM1-87: **1 → S** (the per-user delivery-format
setting; the reading side cannot create it on demand, so a user with no setting has no defined delivery
form). HM1-61: **not producible** — F28 names no entity kind at all.

**Unsizeable: 3, all model defects (M10).** **HM1-61** — the driver is entity kinds and the declaration
(*"A database is part of the system (the DBMS is not specified)"*) names zero; the plural "schemas"
counts and names nothing. This is the store analogue of P-6, and it also voids the demanded pre-load
count. **HM1-75** — the driver is the components the property constrains, and F39 states *"~16–20
nodes"*, counting the constrained components without naming one. P-6 is exact on this. **HM1-83** — the
declared content is the parenthetical *"what happens when there is no delivery"*, a question about F46,
not a statement of content: no retry, no notification, no abandonment, no escalation is named.

**Doubts: 14 enumeration doubts (10 class-changing) + 3 contradictions.** The loudest: HM1-58's
claim/lease split (L vs M) · HM1-60's working-file kinds (F27 names one kind; the pipeline implies at
least three) · HM1-75's alternative reading (count *the cluster node* as one kind → S rather than M10).
Contradictions named, not resolved: **F23's unordered store against F25/F44's orchestration and
distribution** (selecting the next fax and capping the in-flight population are ordering questions asked
of a store declared to have no order) · **F22 against F25** (the exclusion of any queue against the
requirement of exactly what a queue provides — resolved by the assumption projection, not by the
obligations) · **HM1-83 against HM1-93** (HM1-93 triggers on "the fax reaching an outcome", and it is
not stated whether a non-delivered fax ever reaches one).

**Closure violations: 5.** User identity (HM1-87 holds a per-user setting; nothing holds a user) ·
CDR production (named as a consumer of the fax identity, produced nowhere in this batch) · coexistence
(same) · node departure and claim release (HM1-50 names joining only) · establishing the agreed clock.

**Readings.** Elements received 21 · sized 18 · **S 12 · M 5 · L 1 · XL 0** · statement kinds:
compliance 1, behavioural 1 · unsizeable 3 · doubts 14 + 3 · closure violations 5.

---

## Batch C — 30 elements (8 surface, 7 behaviour, 5 interface, 4 store, 6 statement)

**Contamination check.** Clean. F36/F37's traffic figures declared and reproduced only inside the
demanded measurable-target count.

| id | class | enumeration (verbatim) | n | size |
|---|---|---|---|---|
| HM1-65 | surface | 1 user task: enter one internal control centre and reach the state views from it (F31). The views are counted on HM1-66/67/68 (P-2) | 1 | **S** |
| HM1-66 | surface | 1 user task: see the state of the remote nodes (PoP) | 1 | **S** |
| HM1-67 | surface | 1 user task: see the state of the cluster | 1 | **S** |
| HM1-68 | surface | 1 user task: see the state of the queues (the system's own pending-work sets) | 1 | **S** |
| HM1-51 | surface | 5 user tasks: see queue lengths (F21 + F34); see the state of the nodes (F21 + F33); take a node out; put a node back; redistribute what a node was doing. P-5: "and so on" adds nothing | 5 | **L** |
| HM1-52 | behaviour | 3 actions: take a node out; put a node back; redistribute what the node was doing | 3 | **M** |
| HM1-95 | behaviour | 2 actions: establish a staff operator's identity; check that operator's access before a console action. *Derived*, so P-2's coverage test leaves both name tokens countable | 2 | **M** |
| HM1-69 | surface | 2 user tasks: administer the delivery configuration that F05 reads; see the status and history of one's own faxes. "administers their own service" is the umbrella over exactly those two (P-2) | 2 | **M** |
| HM1-70 | surface | 2 user tasks: set delivery to page-by-page TIFF; set delivery to converted PDF (two named alternative outcomes, in the spirit of P-3) | 2 | **M** |
| HM1-71 | surface | 2 user tasks: see the status of a fax of one's own; see the history of one's own faxes | 2 | **M** |
| HM1-96 | behaviour | 1 action: recover a lost portal credential | 1 | **S** |
| HM1-21 | interface | 2 operations: take in a fax received at a point of presence (F01 receive leg); carry the received fax to the Miami data centre as a TIFF file (F04) | 2 | **M** |
| HM1-22 | interface | 3 operations: hand a fax off for sending at a point of presence (F01 send leg); send the rendered TIFF to a point of presence (F16); the named "as an archive" packaging, counted once as a transfer/protocol concern under P-1 | 3 | **M** |
| HM1-91 | interface | 1 operation: carry remote-node (PoP) state across the exchange so the NOC can show it | 1 | **S** |
| HM1-40 | interface | 2 operations: ask the ready least-cost routing program which point of presence receives the TIFF; obey the answer by directing the TIFF to the point of presence it names | 2 | **M** |
| HM1-74 | behaviour | 2 actions (P-3): fan in from the whole PoP set concurrently; fan out to the whole PoP set concurrently. F38's "10–20" names no members and is not counted (P-6) | 2 | **M** |
| HM1-79 | behaviour | 3 actions: split traffic between the new and the old system; issue a fax identity that does not collide with the old system's; present a view that is consistent across both systems | 3 | **M** |
| HM1-98 | behaviour | 1 action: correlate a fax identity issued by the new system with the old system's own identity for the same fax | 1 | **S** |
| HM1-62 | behaviour | 1 action: carry a component-to-component call over the API (F29's API half). No individual operation is named; the components are "in the dozens" with no member named, which counts nothing under P-6 | 1 | **S** |
| HM1-20 | store | 2 entity kinds: the served region (F01 names Europe and the USA); the registered point of presence (F38). The *kind* is named even though its members are not, so P-6 bars counting instances, not the kind | 2 | **M** |
| HM1-63 | store | 1 entity kind: the handed-over work item — the row through which one component hands work to another (F29's database half). "Tables", plural, names no further kind (P-6) | 1 | **S** |
| HM1-76 | store | 1 entity kind: the call detail record (F40). "Production" is an act, not an entity kind | 1 | **S** |
| HM1-77 | store | 1 entity kind: the billing-data record (F41; billing itself is out of scope and adds no kind) | 1 | **S** |
| HM1-64 | statement · **compliance** ("The development language is C#": a configuration/policy, no run-time scenario) | 1 system: the artefact's own codebase, the only thing a development-language rule binds — the PoP software, the router and the old system are used, not built | 1 | **S** |
| HM1-72 | statement · **behavioural** ("every stage dimensioned for that sustained volume") | 1 system: the end-to-end fax path, every stage of which F36's sustained volume constrains. No individual stage is named (P-6) | 1 | **S** |
| HM1-73 | statement · **behavioural** ("absorbed as backlog and worked off") | 2 components: the pending-work sets that absorb a burst as backlog; the processing path that works the backlog off afterwards | 2 | **M** |
| HM1-80 | statement · **behavioural** by P-4 ("no stage bound to a single machine") | 2 systems: the render cluster, across which distribution is mandatory; the single machine, to which no stage may be bound. The stages are the constrained plurality and are never named (P-6) | 2 | **M** |
| HM1-81 | statement · **behavioural** ("node loss, link loss and dependency loss do not lose a fax") | 3 systems: the cluster nodes; the links between components; the dependencies the system calls | 3 | **M** |
| HM1-78 | interface | — | — | **unsizeable (M10)** |
| HM1-84 | statement · kind withheld | — | — | **unsizeable (M10)** |

**Special counts.** *Measurable targets* — HM1-72: **2 → M** (F36's nominal daily volume "~1,000,000
faxes per 10-hour day"; F36's average sustained rate "~30/s on average"). HM1-73: **1 → S** ("~300/s";
"about ten times nominal" is the same figure as a ratio, not a second threshold; no threshold is named
for how long a burst lasts or how quickly the backlog must be worked off). *Entity kinds needing
pre-load* — HM1-20: **2 → M** (point of presence — nothing can cross the boundary before the registry is
populated; served region — the footprint decides which destinations the service accepts). HM1-63:
**not countable** — the one named kind is created at run time, and the declaration names nothing
pre-existing; the element's own class (S) stands, only the seed count is withheld.

**Unsizeable: 2.** **HM1-78** — an interface's count is operations consumed or exposed, and the source
"names neither direction nor payload"; F42 gives only the word "Integration". **HM1-84** — the
declaration asserts it *is* the boundary of "which core functions of the first version this artefact
must present" and names not one; F47 names none either. Kind withheld with the class.

**Doubts: 22** (20 enumeration, 2 contradictions). The largest single sensitivity named by the run:
HM1-72, HM1-73 and HM1-80 all quantify over stages the declaration never names — *"if the model named
its stages, each of these counts would rise, and HM1-72 in particular would very likely leave S."*
Contradictions named, not resolved: **replacement against coexistence, on identity** (F47 replaces the
first version; F42/F43 integrate and coexist with it, with "non-colliding identity" and "a consistent
view across both" — nothing states which system's identity is authoritative during the transition) ·
**the availability half has no measurable target anywhere in the batch** (the special count was demanded
because HM1-72/73 drew a performance-*and-availability* item; between them they name only throughput
and burst thresholds, and HM1-81, which carries the survival property, names no availability objective
at all).

**Closure violations: 4.** No element issues or verifies a portal user's credential (recovery exists
without the thing recovered) · no element ends the transition · no element raises an alert on bad state
(the views show; nothing notifies) · no element hands the CDR and billing data to their consumer.

**Readings.** Elements received 30 · sized 28 · **S 13 · M 14 · L 1 · XL 0** · statement kinds:
compliance 1, behavioural 4 (HM1-84 withheld) · unsizeable 2 + 1 uncountable special count · doubts 22
· closure violations 4.

---

## Repeat-1 totals

79 elements received · **74 sized** · **S 35 · M 36 · L 3 · XL 0** · unsizeable **5** (HM1-61, HM1-75,
HM1-83, HM1-78, HM1-84) · statement kinds: compliance 2, behavioural 5, withheld 1 · doubts 59 ·
closure violations 13 · **XL elements: zero, so no XL coarseness finding anywhere in the model.**
