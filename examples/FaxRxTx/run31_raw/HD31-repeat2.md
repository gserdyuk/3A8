# Run 31 — `Hotyn-D 2.0` × Opus 5 — FaxRxTx size classification, **repeat 2** (batches A, B, C)

Same three prompts as repeat 1, sent verbatim. Transcribed from the three agents' replies.
`tool_uses: 0` in all three; all three quarantined the harness-injected git status and read no file.
Only the sizing tables and the run's own findings are transcribed here; where a row's enumeration is
identical in substance to repeat 1's it is given in short form and the divergent rows are given in
full, because the divergences are what this repeat measures.

---

## Batch A — 28 elements

**Counting test the run stated once, so the disagreement is visible:** *"I count an action or operation
when the declared content or a covered obligation names a verb on an object, or names a qualifier that
cannot be honoured without a further distinct verb on an object. Installation, configuration, licensing
and error handling are never counted unless named."*

| id | class | n | size | repeat 1 | note where they differ |
|---|---|---|---|---|---|
| HM1-23 | interface | 2 | **M** | M (3) | F11's "carried out by workers" read as naming an executor for an already-counted action, suppressed under P-2 |
| HM1-25 | interface | 2 | **M** | M (2) | — |
| HM1-24 | interface | 2 | **M** | M (2) | — |
| HM1-31 | interface | 1 | **S** | **M (2)** | *"1 operation: invoke the third-party library's recognition operation on the page images. No protocol or auth concern is named — a library is not a delivery channel, so P-1 does not add an item."* Repeat 1 counted the interop binding as a second item under P-2 |
| HM1-38 | interface | 1 | **S** | **M (2)** | *"1 operation: submit a print job to the printer driver of the Black Ice class. The vendor class names a product identity, not a further operation."* Repeat 1 counted the capture of the driver's output as a second operation |
| HM1-39 | interface | 3 | **M** | M (2) | packaging counted as a distinct item here, folded into the channel there — same class either way |
| HM1-90 | interface | 3 | **M** | M (3) | — |
| HM1-26 | behaviour | 3 | **M** | M (3) | — |
| HM1-27 | behaviour | 2 | **M** | M (2) | — |
| HM1-28 | behaviour | 1 | **S** | S (1) | — |
| HM1-86 | behaviour | 2 | **M** | M (2) | — |
| HM1-35 | behaviour | 1 | **S** | **M (2)** | *"1 action: parse the email sent to the submission address."* Repeat 1 placed attachment extraction here; repeat 2 placed it at HM1-37 |
| HM1-36 | behaviour | 1 | **S** | S (1) | — |
| HM1-88 | behaviour | 2 | **M** | M (2) | — |
| HM1-89 | behaviour | 2 | **M** | M (2) | — |
| HM1-29 | behaviour | 1 | **S** | **M (2)** | *"1 action: convert the received fax to PDF. F11's 'carried out by workers' names an executor for an action already counted, suppressed under P-2."* The same reading as its HM1-23 call — the run applied it consistently |
| HM1-30 | behaviour | 2 | **M** | M (2) | reached by a different pair: here *digitise* + *place the recognised text into the PDF*; there *digitise* + *carry out as an OCR-worker job* |
| HM1-37 | behaviour | 2 | **M** | **S (1)** | *"2 actions: take the document out of the attachment ('the document from the attachment'); render that document to TIFF."* The mirror image of the HM1-35 divergence |
| HM1-97 | behaviour | 4 | **L** | L (4) | — |
| HM1-41…47 | behaviour | 1 each | **S** ×7 | S ×7 | — |
| HM1-48 | behaviour | 2 | **M** | M (2) | — |
| HM1-49 | behaviour | 2 | **M** | M (2) | — |

**Unsizeable: none.** Same P-6 near-miss recorded at HM1-48, with the same reasoning and the same
explicit alternative: *"if a reader takes the format count to be this element's driver, the element is
unsizeable — model defect (M10), not M."*

**Doubts: 21, of which 14 class-moving.** The run named its own highest-leverage disagreement, which
repeat 1 did not: **D21 — the boundary between HM1-41…47 and HM1-48.** F18 names the renderers; F19
says each format is a separate piece of integration and stabilisation work; no declaration settles
whether that per-format work sits inside each renderer or inside the harness. *"A reader who folds them
into the renderers reaches 2–3 per renderer — and it moves seven elements at once."*

**Closure violations: 4** — the formats beyond the seven named · determination and receipt of the
outbound transmission outcome · the unattributable inbound fax · the work hand-off to the workers
(*"F11 and F09 name workers carrying out conversion, sending and OCR, and there is no message queue at
all. No element in batch A covers how work reaches a worker or is claimed by one."*)

**Readings.** 28 received · 28 sized · **S 13 · M 14 · L 1 · XL 0** · unsizeable 0 · doubts 21 ·
closure violations 4.

---

## Batch B — 21 elements

| id | class | n | size | repeat 1 | note where they differ |
|---|---|---|---|---|---|
| HM1-32 | behaviour | 1 | **S** | S | — |
| HM1-33 | behaviour | 1 | **S** | S | — |
| HM1-34 | behaviour | 1 | **S** | S | — |
| HM1-50 | behaviour | 2 | **M** | M | — |
| HM1-53 | behaviour | 1 | **S** | S | — |
| HM1-55 | behaviour | 2 | **M** | M | reached by a different pair (sweep + examine, against maintain + sweep) |
| HM1-56 | behaviour | 2 | **M** | M | — |
| HM1-57 | behaviour | — | **unsizeable (M10)** | **S (1)** | *"the size driver of a stage machine is its stages and the transitions between them, and the declaration names zero stages and zero transitions … a list could be reconstructed from sibling elements — that would be an inference about a model I may not reshape, and is refused."* Repeat 1 sized it S on "the only action nameable without guessing" and flagged the same alternative in its doubts |
| HM1-58 | behaviour | 4 | **L** | L | — |
| HM1-82 | behaviour | 2 | **M** | M | — |
| HM1-83 | behaviour | — | **unsizeable (M10)** | unsizeable | identical, and for the same reason: the response is never named |
| HM1-85 | behaviour | 1 | **S** | S | — |
| HM1-92 | behaviour | 1 | **S** | S | — |
| HM1-93 | behaviour | 1 | **S** | S | — |
| HM1-54 | store | 1 | **S** | S | — |
| HM1-59 | store | 1 | **S** | S | — |
| HM1-60 | store | 1 | **S** | S | — |
| HM1-61 | store | — | **unsizeable (M10)** | unsizeable | identical: F28 identifies a platform, not a set of responsibilities |
| HM1-87 | store | 1 | **S** | S | — |
| HM1-75 | statement · **compliance** | 2 | **M** | **unsizeable (M10)** | *"2 components: the render cluster nodes (as a class), the private network segment that joins them. '~16–20' is a cardinality without named members and is not an enumeration (P-6)."* Repeat 1 applied P-6 to the whole element and refused it. **Repeat 1 named this exact alternative in its doubts (D-13) and chose the other side** |
| HM1-94 | statement · **behavioural** | 2 | **M** | M (2) | identical count, identical kind |

**Special count.** HM1-87 pre-load: **1 → S**, identical, and reached by the same argument (*"no default
is stated anywhere in the declared content or the covered obligations"*). HM1-61: **not producible**,
identical.

**Doubts: 22.** The run named a doubt repeat 1 did not: **HM1-60's working-file kinds** — *"the pipeline
in this same batch implies at least three intermediate file kinds (material to digitise, OCR output,
converted output), but F27 names only 'the working files' as one kind."* Both repeats reported the same
two contradictions (F22 against F25; F23's unordered store against the ordering F25 and HM1-57 posit).

**Closure violations: 4** — no outbound transmission interface · no inbound source of the material ·
nothing holds or writes the CDR · nothing holds the user. Three of the four are repeat 1's, worded
differently.

**Readings.** 21 received · 18 sized · **S 11 · M 6 · L 1 · XL 0** · statement kinds: compliance 1,
behavioural 1 · unsizeable 3 · doubts 22 · closure violations 4.

---

## Batch C — 30 elements

| id | class | n | size | repeat 1 | note where they differ |
|---|---|---|---|---|---|
| HM1-65 | surface | 1 | **S** | S | — |
| HM1-66 · HM1-67 · HM1-68 | surface | 1 each | **S** | S | — |
| HM1-51 | surface | 5 | **L** | L (5) | identical enumeration |
| HM1-52 | behaviour | 3 | **M** | M (3) | — |
| HM1-95 | behaviour | 2 | **M** | M (2) | — |
| HM1-69 | surface | 1 | **S** | **M (2)** | *"1 user task: enter and administer one's own service account — the web area itself. The two administration tasks F35 names are the declared content of HM1-70 and HM1-71 and are not recounted here (P-2)."* Repeat 1 counted them at the account area as well |
| HM1-70 | surface | 1 | **S** | **M (2)** | *"1 user task: set the delivery configuration for one's own faxes. 'page-by-page TIFF or converted PDF' are two values of that one setting, not two tasks."* Repeat 1 applied P-3 to the two values |
| HM1-71 | surface | 2 | **M** | M (2) | — |
| HM1-96 | behaviour | 1 | **S** | S | — |
| HM1-74 | behaviour | 2 | **M** | M (2) | — |
| HM1-79 | behaviour | 3 | **M** | M (3) | — |
| HM1-98 | behaviour | 1 | **S** | S | — |
| HM1-62 | behaviour | 1 | **S** | S | — |
| HM1-21 | interface | 2 | **M** | M (2) | — |
| HM1-22 | interface | 2 | **M** | M (3) | archive packaging counted once here, as a separate operation there — same class |
| HM1-91 | interface | 1 | **S** | S | — |
| HM1-40 | interface | 1 | **S** | **M (2)** | *"1 operation consumed: ask the ready least-cost routing program which point of presence receives the TIFF. 'Obeying the answer' names no further operation and no protocol or auth concern."* Repeat 1 counted obeying the answer as a second operation |
| HM1-20 | store | 2 | **M** | M (2) | identical, including the P-6 reasoning on the 10–20 members |
| HM1-63 | store | 1 | **S** | S | — |
| HM1-76 · HM1-77 | store | 1 each | **S** | S | — |
| HM1-64 | statement · **compliance** | 1 | **S** | S (1) | identical kind and count |
| HM1-72 | statement · **behavioural** | 1 | **S** | S (1) | identical |
| HM1-73 | statement · **behavioural** | 2 | **M** | M (2) | identical |
| HM1-80 | statement · **behavioural** | 2 | **M** | M (2) | identical, both by the P-4 tie-break, both saying so |
| HM1-81 | statement · **behavioural** | 3 | **M** | M (3) | identical |
| HM1-78 | interface | — | **unsizeable (M10)** | unsizeable | identical |
| HM1-84 | statement | — | **unsizeable (M10)** | unsizeable | identical; kind withheld in both |

**Special counts.** *Measurable targets* — HM1-72: **1 → S** against repeat 1's **2 → M**. *"One
service-level objective expressed in two units, not two objectives."* Repeat 1 counted the daily volume
and the per-second average as two. Both runs named this exact alternative in their doubts, and chose
opposite sides. HM1-73: **1 → S**, identical, and both refused to count "about ten times nominal"
twice. *Entity kinds needing pre-load* — HM1-20: **2 → M**, identical, same two kinds, same reasons.
HM1-63: **0 kinds, no class assignable** — the substance of repeat 1's "not countable", reached by a
different route: *"the store's single named kind is the unit of work one component hands to another,
and that unit is produced at run time."* Both flagged the same mismatch: the crossing gave this store
seed work and the declaration supports no seeded kind.

**Doubts: 18** (16 enumeration, 2 contradictions). Both repeats independently named the same two
contradictions: the double coverage of F33/F34 across the NOC views and the cluster tool, and the
replacement-against-coexistence tension on identity.

**Closure violations: 3** — end of the coexistence, not just the coexistence · the portal user's own
identity (*"the asymmetry with HM1-95 is the tell: recovery exists without the thing recovered"*) ·
egress of the saved CDR and billing data. All three are repeat 1's, worded differently; repeat 2 did not
raise repeat 1's alerting violation.

**Readings.** 30 received · 28 sized · **S 16 · M 11 · L 1 · XL 0** · statement kinds: compliance 1,
behavioural 4 · unsizeable 2 · doubts 18 · closure violations 3.

---

## Repeat-2 totals

79 elements received · **74 sized** · **S 40 · M 31 · L 3 · XL 0** · unsizeable **5** (HM1-57, HM1-61,
HM1-83, HM1-78, HM1-84) · statement kinds: compliance 2, behavioural 5, withheld 1 · doubts 61 ·
closure violations 11 · **XL elements: zero.**

Note the coincidence that is not one: both repeats size exactly 74 of 79 and refuse exactly 5 — but the
five are not the same five. HM1-75 is unsizeable in repeat 1 and M in repeat 2; HM1-57 is S in repeat 1
and unsizeable in repeat 2. Each run named the other's reading in its own doubts before choosing.
