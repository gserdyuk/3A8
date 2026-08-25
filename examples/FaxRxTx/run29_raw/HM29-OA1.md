# Run 29 — `Hotyn-M 1.1` × Opus 5 — FaxRxTx product model, order A, run 1 of 2

**Transcribed verbatim from the agent's reply.** The harness does not persist subagent output; this
file is the durable record. Inputs: `requirements_product.md` (md5 `306046dc6cab35147040224e7a4e9662`,
N = 47) + `assumptions_product.md` v1, pasted into the prompt in full. `tool_uses: 0`.

---

# Product model — run 1 of a pair · engine `Hotyn-M 1.1`

## 1. Contamination check

**Clean — build proceeds.** The pinned input contains no effort figure, no budget, no deadline, no
project duration, no team size and no pre-existing tree. The figures in F19, F36–F39 (format count,
daily volume, burst multiple, PoP count, cluster node count) are stated *properties of the product*
and are treated as such; they are never converted into size, effort or schedule here, and I do not
restate them in my own text — I refer to them by requirement id. **Quarantine note:** my context was
injected with ambient repository information (a git status listing prior runs, raw-run directories and
prior model documents). It is not part of my input; I have read none of it and acted on none of it.

## 2. Skeleton log

Read the 47 obligations as a set. Nineteen nodes posited; **no requirement attached, no coverage
assigned.** Stopped when every id had at least one plausible attachment point.

| id | name | parent | intended scope |
|---|---|---|---|
| HM1-01 | Fax service core system | — | root: the new core of the send-and-receive fax service |
| HM1-02 | Inbound fax path | HM1-01 | from a fax arriving out of a PoP to the user holding it in email |
| HM1-03 | Outbound fax path | HM1-01 | from a user's email arriving to a TIFF handed to a PoP |
| HM1-04 | Document conversion services | HM1-01 | conversion and rendering capabilities shared by both paths |
| HM1-05 | Execution platform | HM1-01 | the system's own Windows cluster and the worker components that run on it |
| HM1-06 | Fax lifecycle control | HM1-01 | the home-grown status/resumption/orchestration mechanism that stands in for a broker |
| HM1-07 | Storage and data | HM1-01 | archive, working files, database schemas |
| HM1-08 | Operations surfaces | HM1-01 | staff-facing observation and control |
| HM1-09 | User portal | HM1-01 | the customer-facing self-service area |
| HM1-10 | External exchanges | HM1-01 | boundaries with things used but not built |
| HM1-11 | Accounting records | HM1-01 | records this system writes and keeps for others to consume |
| HM1-12 | System-wide design properties | HM1-01 | obligations that bind every part rather than sitting in one |
| HM1-13 | Inter-component interfaces | HM1-01 | how the system's own components reach one another |
| HM1-14 | Point-of-presence exchange | HM1-10 | the exchange with the distributed PoPs |
| HM1-15 | Old-system coexistence | HM1-10 | the exchange with, and the running alongside, the first version |
| HM1-16 | Routing exchange | HM1-10 | the exchange with the existing least-cost routing program |
| HM1-17 | Renderer set | HM1-04 | the per-format renderers and how the set is built |
| HM1-18 | NOC | HM1-08 | the internal control centre |
| HM1-19 | Cluster management tool | HM1-08 | operator view and control of the render cluster |

## 3. Accretion log

### Pass 1 — order A, one requirement at a time

| req | pass | verdict | covering node(s) | nodes added (parent) | what was missing | reason | flag |
|---|---|---|---|---|---|---|---|
| F01 | 1 | not covered | HM1-20, HM1-21, HM1-22 | HM1-20 Service footprint & PoP region registry (HM1-14); HM1-21 PoP inbound intake (HM1-14); HM1-22 PoP outbound handoff (HM1-14) | everything: skeleton held no coverage | reach is a property of the served PoP set (P5); the send-and-receive obligation needs both legs to exist at the PoP boundary | **ambiguous** — one entry, two obligations (a receive service and a send service); the Australia hedge read per P5 as reach, not a branch |
| F02 | 1 | not covered | HM1-23 | HM1-23 Inbound email delivery to the user (HM1-02) | the email leg to the user | intake exists (HM1-21), delivery to the user does not | |
| F03 | 1 | not covered | HM1-24 | HM1-24 Submission-address mailbox intake (HM1-03) | the special address and the acceptance of mail at it | the PoP-side send leg is not the user-side submission leg | |
| F04 | 1 | **partially covered** | HM1-21 (part), HM1-25 (part) | HM1-25 Received-TIFF landing (HM1-02) | acceptance of the arriving TIFF at the data centre and its placement in working storage | HM1-21 already realises the PoP→data-centre delivery; the landing did not exist. Debt discharged in this pass | |
| F05 | 1 | not covered | HM1-26, HM1-27, HM1-28, HM1-29 | HM1-26 Delivery-format selection (HM1-02); HM1-27 Page-by-page TIFF attachment (HM1-02); HM1-28 PDF attachment assembly (HM1-02); HM1-29 Received-fax PDF conversion (HM1-04) | both branches, the choice between them, and the conversion the second branch needs | added the conversion in the same pass so no part of F05 waits on a later id | |
| F06 | 1 | **covered** | HM1-29 | none | — | HM1-29, added for F05's PDF branch, *is* conversion of a received fax to PDF. Judgement recorded rather than a duplicate node | |
| F07 | 1 | not covered | HM1-30 | HM1-30 OCR digitisation stage (HM1-04) | digitisation inside the PDF conversion | conversion existed; digitisation did not | |
| F08 | 1 | not covered | HM1-31 | HM1-31 Third-party OCR library binding (HM1-04) | the binding to the bought library | the library is used, not built (P2); the system owes the adapter and its deployment on the workers | |
| F09 | 1 | **partially covered** | HM1-30 (part), HM1-32 (part) | HM1-32 OCR worker (HM1-05) | the worker component that carries the digitisation out | "workers" are components, not people (P5); the stage existed, the carrier did not | |
| F10 | 1 | **covered** | HM1-23 | none | — | HM1-23 already sends the email carrying the fax to the user | **ambiguous** — restates F02 almost exactly; covered jointly, not merged (M1) |
| F11 | 1 | **partially covered** | HM1-29 (part), HM1-23 (part), HM1-33, HM1-34 | HM1-33 Conversion worker (HM1-05); HM1-34 Sending worker (HM1-05) | the worker components behind conversion and sending | same reading of "workers" as F09 | |
| F12 | 1 | not covered | HM1-35 | HM1-35 Submission email parser (HM1-03) | parsing of the accepted mail | acceptance (HM1-24) is not parsing | |
| F13 | 1 | not covered | HM1-36 | HM1-36 Destination fax-number extraction (HM1-03) | the extraction rule | the parser exposes fields; nothing derived the destination number from them | |
| F14 | 1 | not covered | HM1-37 | HM1-37 Attachment-to-TIFF rendering stage (HM1-04) | rendering of the submitted document | inbound conversion is the other direction | |
| F15 | 1 | not covered | HM1-38 | HM1-38 Print-driver rendering path (HM1-04) | the route through the bought printer driver | driver is used, not built (P2); the system owes the binding and the print path | **hedge** — source says "it seems" of the driver class; taken as stated |
| F16 | 1 | **partially covered** | HM1-39 (part), HM1-22 (part) | HM1-39 Outbound archive packaging (HM1-03) | packaging of the rendered TIFF as the transferred archive | the handoff to a PoP existed; the archive form did not | |
| F17 | 1 | not covered | HM1-40 | HM1-40 Least-cost-routing invocation (HM1-16) | the exchange with the ready router | the router is not built (P1); the system owes asking it and obeying the answer | |
| F18 | 1 | not covered | HM1-41 … HM1-47 | HM1-41 DOC, HM1-42 XLS, HM1-43 PPT, HM1-44 PDF, HM1-45 TXT, HM1-46 GIF, HM1-47 TIFF renderer (all HM1-17) | a renderer per named format | generic rendering is not a renderer set; the seven named formats each get a node, none invented (P5) | |
| F19 | 1 | **partially covered** | HM1-48, HM1-49 | HM1-48 Per-format integration & stabilisation harness (HM1-17); HM1-49 Renderer registration / open format set (HM1-17) | the separateness of each format's integration, and the openness of the set beyond the named formats | per P5 the separateness belongs in the structure; the unnamed remainder is admitted structurally, never enumerated | **ambiguous** — one entry holds a count statement and a work-property statement |
| F20 | 1 | not covered | HM1-50 | HM1-50 Cluster node agent & membership (HM1-05) | the cluster the workers run on | workers existed; the machine fabric they run on did not | |
| F21 | 1 | not covered | HM1-51, HM1-52 | HM1-51 Cluster queue-length & node-state view (HM1-19); HM1-52 Node control actions (HM1-19) | the operator view and the ability to act on a node | content taken from P4: view plus act (out / back / redistribute); explicitly not a monitoring suite, not a deployment tool | **ambiguous** — contentless in the source; overlaps F33/F34 |
| F22 | 1 | not covered | HM1-53 | HM1-53 Broker-free dispatch mechanism (HM1-06) | the thing that carries work between components without a broker | a prohibition is realised by the mechanism that makes the prohibited thing unnecessary (P3) | |
| F23 | 1 | not covered | HM1-54, HM1-55 | HM1-54 Token store (HM1-06); HM1-55 Watchdog (HM1-06) | both halves of the named mechanism | P5: one mechanism, three obligations; F23 supplies its two components | |
| F24 | 1 | **partially covered** | HM1-55 (part), HM1-56 (part) | HM1-56 Stall detection & re-dispatch (HM1-06) | detection that something went wrong, and the resumption itself | the watchdog component existed; its act did not | |
| F25 | 1 | **partially covered** | HM1-53 (part), HM1-54 (part), HM1-57, HM1-58 | HM1-57 Fax lifecycle stage machine (HM1-06); HM1-58 In-flight concurrency & claim/lease control (HM1-06) | the stages a fax moves through, and keeping a large in-flight population moving | handoff and status existed; orchestration proper did not | |
| F26 | 1 | not covered | HM1-59 | HM1-59 Fax archive store on Lustre (HM1-07) | the long-lived archive | Lustre is used, not built (P2); the system owes the archive's layout and access | |
| F27 | 1 | not covered | HM1-60 | HM1-60 Working-file store on Lustre (HM1-07) | the short-lived per-job files | P5: two responsibilities on one infrastructure, not one | |
| F28 | 1 | not covered | HM1-61 | HM1-61 System database schemas (HM1-07) | the schemas the system owns | the DBMS is not modelled and not guessed (P2) | **ambiguous** — DBMS unspecified in the source |
| F29 | 1 | not covered | HM1-62, HM1-63 | HM1-62 Inter-component API (HM1-13); HM1-63 Database-mediated exchange tables (HM1-13) | both stated media of communication | the database existed as a store, not as an exchange medium | |
| F30 | 1 | not covered | HM1-64 | HM1-64 C#/.NET implementation baseline (HM1-12) | the language obligation on the system's own parts | binds every own component; bought parts are bound to from it | |
| F31 | 1 | not covered | HM1-65 | HM1-65 NOC console shell (HM1-18) | the control-centre application itself | the skeleton NOC node held nothing | |
| F32 | 1 | not covered | HM1-66 | HM1-66 PoP state view (HM1-18) | the remote-node state surface | | |
| F33 | 1 | **partially covered** | HM1-51 (part), HM1-67 (part) | HM1-67 Cluster state view in the NOC (HM1-18) | the NOC's own presentation of cluster state | P5: cover F21 and F33 jointly where they genuinely coincide — the state content is one thing, its two surfaces are two | **ambiguous** — overlaps F21 |
| F34 | 1 | **partially covered** | HM1-51 (part), HM1-68 (part) | HM1-68 Queue state view in the NOC (HM1-18) | the NOC's own presentation of queue state | same joint treatment; "queues" read as the system's own pending-work sets, since F22 excludes a broker | **ambiguous** — overlaps F21 |
| F35 | 1 | not covered | HM1-69, HM1-70, HM1-71 | HM1-69 Portal account area (HM1-09); HM1-70 Delivery-configuration editing (HM1-09); HM1-71 User fax status & history (HM1-09) | the whole portal | content taken from P4: own-service administration, the configuration F05 reads, own status and history; explicitly not marketing, billing or staff console | **ambiguous** — contentless in the source |
| F36 | 1 | not covered | HM1-72 | HM1-72 Sustained-throughput capacity design (HM1-12) | the sustained-volume obligation on every stage | P5: a property the design must meet, not a component; figure referenced by id only | |
| F37 | 1 | **partially covered** | HM1-73 | HM1-73 Burst absorption (HM1-12) | absorbing the burst multiple without loss (backlog held and worked off) | sustained capacity is not burst tolerance | |
| F38 | 1 | **partially covered** | HM1-20 (part), HM1-74 (part) | HM1-74 Multi-PoP fan-in/fan-out (HM1-14) | operating against the whole PoP set concurrently, both directions | the registry existed; the concurrency of the exchanges did not | |
| F39 | 1 | **partially covered** | HM1-50 (part), HM1-75 (part) | HM1-75 Private cluster network topology (HM1-05) | the private network joining the nodes | membership existed; the medium did not | |
| F40 | 1 | not covered | HM1-76 | HM1-76 CDR production & store (HM1-11) | the record per fax transaction | | |
| F41 | 1 | not covered | HM1-77 | HM1-77 Billing-data production & store (HM1-11) | the data billing consumes | written and kept here; the consumer is not built (P1/P5) | |
| F42 | 1 | not covered | HM1-78 | HM1-78 Old-system integration interface (HM1-15) | the defined exchange with the first version | | **ambiguous** — the source names no direction or payload |
| F43 | 1 | **partially covered** | HM1-79 | HM1-79 Transitional coexistence controls (HM1-15) | running at the same time: traffic split, non-colliding identity, a consistent view across both | an interface is not coexistence | |
| F44 | 1 | **partially covered** | HM1-58 (part), HM1-80 (part) | HM1-80 Distributed-by-construction stage placement (HM1-12) | the mandatory character: no stage bound to a single machine | the dispatcher spreads work; nothing forbade a single-node-only stage | |
| F45 | 1 | **partially covered** | HM1-56 (part), HM1-81 (part) | HM1-81 Failure-survival design across components (HM1-12) | survival beyond worker stalls: node loss, link loss, dependency loss | re-dispatch covers one failure kind only | |
| F46 | 1 | **partially covered** | HM1-54 (part), HM1-82, HM1-83 | HM1-82 Per-fax delivery-outcome tracking (HM1-06); HM1-83 Non-delivery handling (HM1-06) | a determined, confirmed outcome per fax, and what happens when there is none | holding status is not controlling delivery | |
| F47 | 1 | not covered | HM1-84 | HM1-84 Core-parity scope baseline (HM1-12) | the declared boundary: which core functions of the first version this artefact must present | P5: a scope statement on the artefact, not a migration and not a goal; realised as an enumerated parity boundary the coexistence controls read | |

**Pass 1: 65 nodes added, 0 deferrals.**

### Pass 2 — required to demonstrate the fixpoint

Structure unchanged since pass 1 closed; every id re-tested against it. All 47 verdicts `covered`,
0 added, 0 deferred — **accretion fixpoint reached.** (Covering nodes as listed in §7c.)

## 4. Completion log

Derived nodes only. **None covers a requirement** — each is structure the model requires and no
obligation names.

| node | name | parent | trigger | justification | pass |
|---|---|---|---|---|---|
| HM1-85 | Fax identifier issuance | HM1-06 | HM1-54, HM1-59, HM1-76, HM1-79 | token, archive, CDR and coexistence all key on a per-fax identity that nothing states | 1 |
| HM1-86 | Inbound recipient resolution | HM1-02 | HM1-23 | a received fax must be attributed to an owning user before an email can be addressed | 1 |
| HM1-87 | Per-user delivery configuration store | HM1-07 | HM1-26, HM1-70 | the configuration one node reads and another sets must be held somewhere | 1 |
| HM1-88 | Submission sender attribution | HM1-03 | HM1-24, HM1-35 | mail arriving at a public address must be attributed to an account before a fax leaves on its behalf | 1 |
| HM1-89 | Submission outcome notification to the sender | HM1-03 | HM1-83, HM1-24 | the submitter's only channel is email; a determined outcome has to reach them | 1 |
| HM1-90 | Render host application automation | HM1-04 | HM1-38, HM1-41, HM1-42, HM1-43 | printing office documents through a printer driver needs a driven application session per node | 1 |
| HM1-91 | PoP state feed | HM1-14 | HM1-66 | the NOC can only show remote-node state if state crosses the exchange | 1 |
| HM1-92 | Duplicate suppression on re-dispatch | HM1-06 | HM1-56, HM1-82 | re-dispatch after a stall can produce a second delivery unless the unit is idempotent | 1 |
| HM1-93 | Working-file reclamation | HM1-07 | HM1-60, HM1-82 | short-lived files need a defined end, tied to the fax reaching an outcome | 1 |
| HM1-94 | Cluster-wide time alignment | HM1-05 | HM1-56, HM1-76 | elapsed-time stall detection and records written on many machines require an agreed clock | 1 |
| HM1-95 | Operator identity and access for the staff surfaces | HM1-08 | HM1-65, HM1-52 | a console that can take a cluster node out needs staff identity behind it | 1 |
| HM1-96 | Portal credential recovery | HM1-09 | HM1-69 | a customer-facing account area implies recovery of lost credentials; stated nowhere | 1 |
| HM1-97 | Render session isolation and recovery | HM1-04 | **HM1-90** (derived) | a driven application session hangs; a node must be recoverable without losing the fax | 2 |
| HM1-98 | Identifier correlation with the old system | HM1-15 | **HM1-85** (derived), HM1-79 | if the new system issues its own fax identity while the old one keeps its own, coexistence needs a correlation | 2 |

**Pass 3: 0 added — completion fixpoint reached.**

## 5. Convergence trace

| phase | pass | nodes added | deferrals |
|---|---|---|---|
| skeleton | 1 | 19 posited | n/a (no attachment permitted) |
| accretion | 1 | 65 | 0 |
| accretion | 2 | **0** | **0** — fixpoint |
| completion | 1 | 12 | n/a |
| completion | 2 | 2 | n/a |
| completion | 3 | **0** | fixpoint |
| closure | — | 0 (1 collapse) | — |

Both fixpoints reach zero. No deferral arose in either phase; accretion therefore needed a second
pass only to demonstrate the fixpoint, not to discharge one.

## 6. Final model (frozen, post-normalisation — 97 nodes)

Provenance is given as origin (`posited` / `accreted` / `derived`) with the `stated` / `implied`
reading: **accreted = stated**, **posited and derived = implied**.

### Spine

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM1-01 | Fax service core system | — | posited (implied) | ∅ |
| HM1-02 | Inbound fax path | HM1-01 | posited (implied) | ∅ |
| HM1-03 | Outbound fax path | HM1-01 | posited (implied) | ∅ |
| HM1-04 | Document conversion services | HM1-01 | posited (implied) | ∅ |
| HM1-05 | Execution platform | HM1-01 | posited (implied) | ∅ |
| HM1-06 | Fax lifecycle control | HM1-01 | posited (implied) | ∅ |
| HM1-07 | Storage and data | HM1-01 | posited (implied) | ∅ |
| HM1-08 | Operations surfaces | HM1-01 | posited (implied) | ∅ |
| HM1-09 | User portal | HM1-01 | posited (implied) | ∅ |
| HM1-10 | External exchanges | HM1-01 | posited (implied) | ∅ |
| HM1-11 | Accounting records | HM1-01 | posited (implied) | ∅ |
| HM1-12 | System-wide design properties | HM1-01 | posited (implied) | ∅ |
| HM1-13 | Inter-component interfaces | HM1-01 | posited (implied) | ∅ |
| HM1-14 | Point-of-presence exchange | HM1-10 | posited (implied) | ∅ |
| HM1-15 | Old-system coexistence | HM1-10 | posited (implied) | ∅ |
| HM1-17 | Renderer set | HM1-04 | posited (implied) | ∅ |
| HM1-18 | NOC | HM1-08 | posited (implied) | ∅ |
| HM1-19 | Cluster management tool | HM1-08 | posited (implied) | ∅ |

*(HM1-16 collapsed at closure — see §7b.)*

### Inbound fax path

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM1-23 | Inbound email delivery to the user | HM1-02 | accreted (stated) | F02, F10, F11 |
| HM1-25 | Received-TIFF landing | HM1-02 | accreted (stated) | F04 |
| HM1-26 | Delivery-format selection | HM1-02 | accreted (stated) | F05 |
| HM1-27 | Page-by-page TIFF attachment | HM1-02 | accreted (stated) | F05 |
| HM1-28 | PDF attachment assembly | HM1-02 | accreted (stated) | F05 |
| HM1-86 | Inbound recipient resolution | HM1-02 | derived (implied) | ∅ |

### Outbound fax path

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM1-24 | Submission-address mailbox intake | HM1-03 | accreted (stated) | F03 |
| HM1-35 | Submission email parser | HM1-03 | accreted (stated) | F12 |
| HM1-36 | Destination fax-number extraction | HM1-03 | accreted (stated) | F13 |
| HM1-39 | Outbound archive packaging | HM1-03 | accreted (stated) | F16 |
| HM1-88 | Submission sender attribution | HM1-03 | derived (implied) | ∅ |
| HM1-89 | Submission outcome notification to sender | HM1-03 | derived (implied) | ∅ |

### Document conversion services

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM1-29 | Received-fax PDF conversion | HM1-04 | accreted (stated) | F05, F06, F11 |
| HM1-30 | OCR digitisation stage | HM1-04 | accreted (stated) | F07, F09 |
| HM1-31 | Third-party OCR library binding | HM1-04 | accreted (stated) | F08 |
| HM1-37 | Attachment-to-TIFF rendering stage | HM1-04 | accreted (stated) | F14 |
| HM1-38 | Print-driver rendering path (Black Ice class) | HM1-04 | accreted (stated) | F15 |
| HM1-90 | Render host application automation | HM1-04 | derived (implied) | ∅ |
| HM1-97 | Render session isolation and recovery | HM1-04 | derived (implied) | ∅ |

### Renderer set

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM1-41 | DOC renderer | HM1-17 | accreted (stated) | F18 |
| HM1-42 | XLS renderer | HM1-17 | accreted (stated) | F18 |
| HM1-43 | PPT renderer | HM1-17 | accreted (stated) | F18 |
| HM1-44 | PDF renderer | HM1-17 | accreted (stated) | F18 |
| HM1-45 | TXT renderer | HM1-17 | accreted (stated) | F18 |
| HM1-46 | GIF renderer | HM1-17 | accreted (stated) | F18 |
| HM1-47 | TIFF renderer | HM1-17 | accreted (stated) | F18 |
| HM1-48 | Per-format integration & stabilisation harness | HM1-17 | accreted (stated) | F19 |
| HM1-49 | Renderer registration / open format set | HM1-17 | accreted (stated) | F19 |

### Execution platform

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM1-32 | OCR worker | HM1-05 | accreted (stated) | F09 |
| HM1-33 | Conversion worker | HM1-05 | accreted (stated) | F11 |
| HM1-34 | Sending worker | HM1-05 | accreted (stated) | F11 |
| HM1-50 | Cluster node agent & membership | HM1-05 | accreted (stated) | F20, F39 |
| HM1-75 | Private cluster network topology | HM1-05 | accreted (stated) | F39 |
| HM1-94 | Cluster-wide time alignment | HM1-05 | derived (implied) | ∅ |

### Fax lifecycle control

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM1-53 | Broker-free dispatch mechanism | HM1-06 | accreted (stated) | F22, F25 |
| HM1-54 | Token store (unordered, per-fax status) | HM1-06 | accreted (stated) | F23, F25, F46 |
| HM1-55 | Watchdog | HM1-06 | accreted (stated) | F23, F24 |
| HM1-56 | Stall detection & re-dispatch | HM1-06 | accreted (stated) | F24, F45 |
| HM1-57 | Fax lifecycle stage machine | HM1-06 | accreted (stated) | F25 |
| HM1-58 | In-flight concurrency & claim/lease control | HM1-06 | accreted (stated) | F25, F44 |
| HM1-82 | Per-fax delivery-outcome tracking | HM1-06 | accreted (stated) | F46 |
| HM1-83 | Non-delivery handling | HM1-06 | accreted (stated) | F46 |
| HM1-85 | Fax identifier issuance | HM1-06 | derived (implied) | ∅ |
| HM1-92 | Duplicate suppression on re-dispatch | HM1-06 | derived (implied) | ∅ |

### Storage and data

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM1-59 | Fax archive store on Lustre | HM1-07 | accreted (stated) | F26 |
| HM1-60 | Working-file store on Lustre | HM1-07 | accreted (stated) | F27 |
| HM1-61 | System database schemas | HM1-07 | accreted (stated) | F28 |
| HM1-87 | Per-user delivery configuration store | HM1-07 | derived (implied) | ∅ |
| HM1-93 | Working-file reclamation | HM1-07 | derived (implied) | ∅ |

### Operations surfaces

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM1-65 | NOC console shell | HM1-18 | accreted (stated) | F31 |
| HM1-66 | PoP state view | HM1-18 | accreted (stated) | F32 |
| HM1-67 | Cluster state view in the NOC | HM1-18 | accreted (stated) | F33 |
| HM1-68 | Queue state view in the NOC | HM1-18 | accreted (stated) | F34 |
| HM1-51 | Cluster queue-length & node-state view | HM1-19 | accreted (stated) | F21, F33, F34 |
| HM1-52 | Node control actions | HM1-19 | accreted (stated) | F21 |
| HM1-95 | Operator identity and access | HM1-08 | derived (implied) | ∅ |

### User portal

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM1-69 | Portal account area | HM1-09 | accreted (stated) | F35 |
| HM1-70 | Delivery-configuration editing | HM1-09 | accreted (stated) | F35 |
| HM1-71 | User fax status & history | HM1-09 | accreted (stated) | F35 |
| HM1-96 | Portal credential recovery | HM1-09 | derived (implied) | ∅ |

### External exchanges

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM1-20 | Service footprint & PoP region registry | HM1-14 | accreted (stated) | F01, F38 |
| HM1-21 | PoP inbound intake | HM1-14 | accreted (stated) | F01, F04 |
| HM1-22 | PoP outbound handoff | HM1-14 | accreted (stated) | F01, F16 |
| HM1-74 | Multi-PoP fan-in/fan-out | HM1-14 | accreted (stated) | F38 |
| HM1-91 | PoP state feed | HM1-14 | derived (implied) | ∅ |
| HM1-78 | Old-system integration interface | HM1-15 | accreted (stated) | F42 |
| HM1-79 | Transitional coexistence controls | HM1-15 | accreted (stated) | F43 |
| HM1-98 | Identifier correlation with the old system | HM1-15 | derived (implied) | ∅ |
| HM1-40 | Least-cost-routing invocation | **HM1-10** (was HM1-16) | accreted (stated) | F17 |

### Accounting records · interfaces · design properties

| id | name | parent | provenance | own coverage |
|---|---|---|---|---|
| HM1-76 | CDR production & store | HM1-11 | accreted (stated) | F40 |
| HM1-77 | Billing-data production & store | HM1-11 | accreted (stated) | F41 |
| HM1-62 | Inter-component API | HM1-13 | accreted (stated) | F29 |
| HM1-63 | Database-mediated exchange tables | HM1-13 | accreted (stated) | F29 |
| HM1-64 | C#/.NET implementation baseline | HM1-12 | accreted (stated) | F30 |
| HM1-72 | Sustained-throughput capacity design | HM1-12 | accreted (stated) | F36 |
| HM1-73 | Burst absorption | HM1-12 | accreted (stated) | F37 |
| HM1-80 | Distributed-by-construction stage placement | HM1-12 | accreted (stated) | F44 |
| HM1-81 | Failure-survival design across components | HM1-12 | accreted (stated) | F45 |
| HM1-84 | Core-parity scope baseline | HM1-12 | accreted (stated) | F47 |

**Parent check (M2), every aggregate:** total coverage = union of children's totals + own residue.
Every aggregate's own residue is empty; every coverage assignment sits on a leaf. No id appears at a
parent that is absent from all its children, and none disappears going up. Verified at all 18
surviving aggregates.

## 7. Empty skeleton nodes

**None.** All 19 posited nodes ended with non-empty *total* coverage.

Reading, stated rather than left implicit: zero empty skeleton nodes is itself a measurement, and a
partly self-confirming one — the skeleton was posited after reading the whole list as a set, which
biases the guess toward finding matter under every branch. The nearest thing to a wrong guess was
**HM1-16 (Routing exchange)**, which attracted exactly one leaf and did not survive normalisation; it
was a correct guess about the product with too much structure around it. The *own*-coverage test was
not applied, per M4.

## 7b. Normalisation log

| collapsed node | merged into | new parent of the leaf | coverage carried across |
|---|---|---|---|
| HM1-16 Routing exchange | HM1-40 Least-cost-routing invocation | HM1-10 External exchanges | ∅ (HM1-16 held no own coverage; HM1-40 retains {F17}) |

One collapse. No cascade: HM1-10 has three children afterwards.

## 7c. Coverage completeness

Every id asserted explicitly. "Whole" is claimed, never inferred.

| req | covering nodes and the part each realises | verdict |
|---|---|---|
| F01 | HM1-21 the receive leg exists at the PoP boundary · HM1-22 the send leg exists · HM1-20 the served regions include Europe and the USA | **whole** |
| F02 | HM1-23 the received fax reaches the user as email | **whole** |
| F03 | HM1-24 the special address is served and users' mail accepted at it | **whole** |
| F04 | HM1-21 faxes received at PoPs are delivered to the data centre · HM1-25 the arriving TIFF is accepted there and placed in working storage | **whole** |
| F05 | HM1-26 the user's configuration is read and the branch chosen · HM1-27 the TIFF-page-by-page branch · HM1-29 the conversion for the other branch · HM1-28 the converted PDF attached | **whole** |
| F06 | HM1-29 conversion of a received fax to PDF | **whole** |
| F07 | HM1-30 digitisation performed inside that conversion | **whole** |
| F08 | HM1-31 the digitisation is obtained from the bought library, not written | **whole** |
| F09 | HM1-30 the digitisation carried out · HM1-32 the worker component carrying it out | **whole** |
| F10 | HM1-23 the email carrying the fax is sent to the user | **whole** |
| F11 | HM1-29 the conversion performed · HM1-23 the sending performed · HM1-33 conversion runs in a worker · HM1-34 sending runs in a worker | **whole** |
| F12 | HM1-35 the submission email is parsed | **whole** |
| F13 | HM1-36 the recipient fax number is derived from it | **whole** |
| F14 | HM1-37 the attached document is rendered to a fax-ready TIFF | **whole** |
| F15 | HM1-38 rendering goes through the bought printer driver | **whole** |
| F16 | HM1-39 the rendered TIFF is packaged as the archive · HM1-22 the archive is sent to a PoP | **whole** |
| F17 | HM1-40 the destination PoP is decided by the existing router and obeyed | **whole** |
| F18 | HM1-41 DOC · HM1-42 XLS · HM1-43 PPT · HM1-44 PDF · HM1-45 TXT · HM1-46 GIF · HM1-47 TIFF | **whole** (the seven named formats; none invented) |
| F19 | HM1-48 each format separately integrated and stabilised · HM1-49 the set is open beyond the named formats, to the order stated in F19 | **whole** — the unnamed remainder is structurally admitted, not enumerated (P5 forbids inventing names) |
| F20 | HM1-50 the system's own Windows cluster carries rendering and the other tasks | **whole** |
| F21 | HM1-51 operator view of queue lengths and node state · HM1-52 acting on a node | **whole** (against P4's assumed content) |
| F22 | HM1-53 work is handed between components with no queue product; MSMQ excluded | **whole** |
| F23 | HM1-54 the unordered store holding each fax's status · HM1-55 the watchdog half of the mechanism | **whole** |
| F24 | HM1-55 the watchdog that sweeps · HM1-56 detection of the stall and resumption of the work | **whole** |
| F25 | HM1-57 the stages and transitions · HM1-58 a large in-flight population kept moving · HM1-54 that population materialised · HM1-53 the handoff itself | **whole** |
| F26 | HM1-59 the long-lived fax archive on Lustre | **whole** |
| F27 | HM1-60 the short-lived per-job working files on Lustre | **whole** |
| F28 | HM1-61 the schemas the system owns in a database platform | **whole** (the DBMS is out of the product, P2) |
| F29 | HM1-62 the API · HM1-63 the database as exchange medium | **whole** |
| F30 | HM1-64 the system's own components are C#/.NET | **whole** |
| F31 | HM1-65 the internal control-centre application | **whole** |
| F32 | HM1-66 remote PoP state shown in the NOC | **whole** |
| F33 | HM1-51 the cluster-state content and its operator presentation · HM1-67 that state shown in the NOC | **whole** |
| F34 | HM1-51 the queue-state content · HM1-68 that state shown in the NOC | **whole** |
| F35 | HM1-69 the customer-facing area · HM1-70 the delivery configuration set by the user · HM1-71 own status and history | **whole** (against P4's assumed content) |
| F36 | HM1-72 every stage dimensioned for the sustained volume stated in F36 | **whole** |
| F37 | HM1-73 the burst multiple stated in F37 absorbed as backlog and worked off | **whole** |
| F38 | HM1-20 the served PoPs are registered · HM1-74 both exchanges operate against the whole set concurrently | **whole** |
| F39 | HM1-50 cluster membership at the size stated in F39 · HM1-75 the nodes joined by a private network | **whole** |
| F40 | HM1-76 a CDR is written per fax transaction and kept | **whole** |
| F41 | HM1-77 the data billing consumes is written and kept | **whole** |
| F42 | HM1-78 the defined exchange with the running first version | **whole** |
| F43 | HM1-79 both systems run at once: traffic split, non-colliding identity, consistent view for the transition | **whole** |
| F44 | HM1-58 work is spread across nodes · HM1-80 no stage is bound to one machine | **whole** |
| F45 | HM1-56 failed work is resumed · HM1-81 node, link and dependency loss do not lose a fax | **whole** |
| F46 | HM1-54 every fax's status is held · HM1-82 its delivery outcome is determined and confirmed · HM1-83 non-delivery ends in a declared outcome | **whole** |
| F47 | HM1-84 the enumerated core functions of the first version that this artefact must present | **whole** |

**Residues: none. Partial marks standing at closure: zero.** Every partial verdict raised during
accretion was discharged in the same pass by adding structure.

## 8. Instrument readings

**Engine: `Hotyn-M 1.1`.**

| reading | value |
|---|---|
| node count before normalisation | 98 |
| node count after normalisation | 97 |
| provenance, before normalisation — posited | 19 |
| provenance, before normalisation — accreted | 65 |
| provenance, before normalisation — derived | 14 |
| derived fraction (primary reading of this engine) | 14 of 98 before normalisation; 14 of 97 after |
| skeleton size | 19 |
| skeleton nodes ending with empty **total** coverage | 0 |
| nodes collapsed at closure | 1 (HM1-16 → HM1-40) |
| passes to convergence — skeleton | 1 |
| passes to convergence — accretion | 2 (65 added, then 0/0) |
| passes to convergence — completion | 3 (12, then 2, then 0) |
| requirements in the pinned list | 47 |
| requirements appearing in some node's own coverage | 47 |
| requirements unplaceable | 0 |
| coverage assignments (node–requirement pairs) | 82 |
| nodes per requirement — min / max | 1 / 7 |
| nodes per requirement — the spread | 1 node: 26 ids · 2 nodes: 14 ids · 3 nodes: F01 F35 F46 · 4 nodes: F05 F11 F25 · 7 nodes: F18 |
| requirements per node — nodes carrying coverage | 65 of 98 |
| requirements per node — the spread | 1 id: 52 nodes · 2 ids: 9 nodes (HM1-20, 21, 22, 30, 50, 53, 55, 56, 58) · 3 ids: 4 nodes (HM1-23, 29, 51, 54) |
| nodes with empty own coverage | 33 (19 posited aggregates + 14 derived) |
| ambiguity flags | 10 — F01, F10, F15, F19, F21, F28, F33, F34, F35, F42 |
| completion-covers-a-requirement defects | 0 |
| partial marks standing at closure | **0** |
| numbers produced by this run | none — only the counts above |

## 9. Assumption log

**Entries flagged ambiguous, verbatim from the pinned list:** F01 (two obligations in one entry — a
receive service and a send service; not split per M1; Australia read as reach) · F10 (restates F02 to
the point where one node realises both; not merged, HM1-23 carries both ids) · F15 (hedged "it seems";
taken as stated) · F19 (a count and a property of how the set is built; both covered without
splitting) · F21 (contentless; content from P4 only; overlaps F33/F34) · F28 (DBMS unspecified;
modelled as schemas the system owns) · F33/F34 (overlap with F21 recorded, not resolved: HM1-51
realises the state content once and carries F21, F33, F34; HM1-67 and HM1-68 realise the NOC's own
surfaces — a coverage decision, not a merge) · F35 (contentless; content from P4 only) · F42 (neither
direction nor payload stated; modelled as a defined interface whose content is undetermined).

**Places where the run interpreted rather than read:**

1. **F22 is a prohibition and prohibitions have no natural node.** Realised positively: HM1-53 is the
   mechanism that makes a broker unnecessary. Reading a negative obligation as its positive
   replacement (P3) is an interpretation, not a reading.
2. **F36, F37, F39, F44, F45, F46 are properties, not components,** and were given nodes under HM1-12
   and HM1-06 so the obligations have somewhere to be realised. A different run may distribute the
   same obligations onto the stages instead, and the two models would then differ in structure while
   agreeing on coverage.
3. **F47 names no function.** Realised as an enumerated parity boundary (HM1-84). The alternative was
   to leave a residue, which M2 forbids at closure.
4. **F19's unnamed formats** realised as an *open registration mechanism* (HM1-49) rather than as
   nodes — the only place in the model where an obligation is realised by an extension point instead
   of by content.
5. **"Queues" in F21 and F34** read as the system's own pending-work sets held in the token store,
   since F22 excludes any broker. The source does not say this.
6. **HM1-87 (per-user delivery configuration store) is derived and covers nothing.** Had the run ruled
   the other way, this would have been a completion-covers-a-requirement defect. Recorded because the
   ruling is contestable.
7. **A deployment/rollout subsystem was considered at completion and deliberately not added.**
   Installing worker software on cluster nodes is plausibly implied by HM1-50 and HM1-52 but is close
   to the product boundary (P1). The omission is recorded so the next run can rule differently and
   know it is disagreeing.
8. **F40 and F41 were kept as two nodes.** CDR and billing data may well be one record set; the source
   distinguishes them.

**Requirements that could not be placed: none.** All 47 ids appear in some node's own coverage.

**Boundary checks (P1) that came up and were refused:** no fax-board driver, no routing algorithm and
no billing engine appears anywhere in this model. HM1-40, HM1-21/HM1-22 and HM1-77 are exchanges with
those things, not the things.

**Files:** none read, none written.
