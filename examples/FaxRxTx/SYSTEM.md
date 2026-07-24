# FaxRxTx (Venali) — system and task description

**Source:** the recollections of a project participant, recorded 2026-07-17 from their
account. A real commercial project (the company Venali, a data center in Miami).
Markers of uncertainty ("it seems," "I think," "I don't remember") are kept deliberately —
they are part of the input data, not editorial defects.

**Document status:** a fixed input for the 3A8 pipeline (the analog of
BMS_extracted.md in the BMS example). The estimate must rely only on this
document + the assumption log, with no access to the actual outcome.

---

## 1. What the system does

A worldwide fax send-and-receive service: at least Europe and the USA
(possibly Australia too — the participant does not remember exactly). The user receives
incoming faxes by email and sends outgoing faxes by emailing a special address.

## 2. Fax reception (Rx)

1. Geographically distributed points of presence (PoP) are placed at
   telecom providers: they worked with BT and with others too.
   Rack space is rented at the provider, a computer with **Brooktrout**
   boards is installed to receive faxes.
2. Received faxes, as TIFF files, are sent to the company's own data center
   in Miami.
3. In the data center, depending on the user's configuration, the fax is either
   attached to the email page by page (TIFF) or converted to PDF
   and attached to the email. Conversion to PDF included digitization (OCR) —
   this was handled by OCR workers.
4. The email is sent to the user. Conversion and sending are handled by
   **workers**.

## 3. Fax transmission (Tx)

1. The user sends an email to a specific address. The email is parsed,
   the recipient's fax number is extracted from it.
2. The document from the attachment is rendered to TIFF (via, it seems, the **Black Ice**
   printer driver) and sent as an archive to a point of presence, where it
   goes into the PSTN through the Brooktrout boards.
3. A **routing** program (least-cost routing) works: it decides which
   point of presence to send the TIFF files to, so that delivery is cheaper.
4. **Renderers** — for the main document formats: DOC, XLS, PPT, PDF,
   TXT, GIF, TIFF (the list is from memory; the participant may have forgotten
   something; on the order of 8–10 formats in all).

## 4. Infrastructure and key technical decisions

- **Its own cluster of Windows 7 computers** — for rendering and other
  tasks.
- **A cluster management tool** — queue lengths and so on.
- **A job queue (MQ) was not used**: using MSMQ in the previous version of the
  system broke everything. Instead — a home-grown system of
  **watchdogs and tokens** (an unordered store) that kept the status
  of each fax and resumed work if something went wrong. Essentially — an
  orchestrator of a large number of faxes.
- **Storage:** the **Lustre** file system (from HP, it seems) — it stored both the
  fax archive and the working files. There was also a database (the DBMS is not
  specified) — the components communicated through the DB and an API.
- **Development language:** C#.
- **NOC** — an internal control center: the state of the remote nodes (PoP),
  the cluster, and the queues (where there were any).
- **User portal** — the users' website.

## 5. Scale

- The nominal target volume — **~1,000,000 faxes per 10-hour day**
  (~30/s on average). The figure 10,000,000/day (~300/s) is a **burst estimate**,
  the peak mode ~10× the nominal. Actual traffic was even below the
  nominal (the participant's clarification, 2026-07-17).
- Points of presence (PoP): **10–20**.
- Nodes in the render cluster: **~16–20** (from memory: "probably 20," "maybe 16"),
  joined by a private network.

## 6. The team's scope (the object of the estimate)

Context: by the start of the work **a working first version of the system already
existed**. The task was to redo what management did not like in the
original version. The team, meanwhile, **did not know the domain**: about
a month (possibly two) went into discussions, immersion in the subject
area, and technology selection (they studied DHT and other mechanisms).
There was no code reuse ("no reference base classes") —
only integration with the old system and coexistence for the duration
of the transition.

**What the team did (included in the estimate):**

- the stage of domain immersion and architecture/technology selection
  (they considered DHT and the like) — about 1–2 months;
- the printing (rendering) and OCR workers — OCR on a third-party library;
- the cluster itself with the delivery-control mechanism (watchdogs + tokens, §4);
- the NOC;
- the user portal;
- the inbound-email parser (the Tx path);
- saving CDR and billing data (billing itself is out of scope);
- integration tests on the real message stream with comparison of the
  results to the "old system."

**What the team did not do (out of the estimate):**

- the software on the PoPs (reception/sending via Brooktrout) — already existed;
- the routing program (least-cost) — was ready, reused;
- billing — was separate.

The components communicated through the database and an API.

**Process:** "scrum after waterfall" — first a planning phase, then
scrum. There was no hard deadline, but there was pressure. The team included
QA/PM, not just developers. The work period — roughly 2007–2009
(the participant named both "2007–2008" and "2008–2009").

## 7. Public context (open sources, 2026-07-17)

- Venali, Inc. — Miami, hosted enterprise internet fax for Fortune 1000
  (healthcare, retail, finance/insurance).
- Acquired by j2 Global in September 2010 for ~$17M; revenue ~$10M over
  the preceding 12 months. Since 2006 there was a patent lawsuit by Venali against j2,
  closed by the deal.
- A cluster on Windows 7 (released in October 2009) + the sale of the company in 2010
  constrain the dating of the development described to roughly 2005–2010;
  the exact period — to be clarified with the participant.

## 8. The estimation task

Estimate the **effort in person-months** for the scope from §6 — blind,
from this document and the assumption log only.

The project's actual outcome (team size, duration, final
person-months) is recorded separately in **FACT.md** and must not enter
the context of the estimator agents. The check against fact — only at the final
Step D of the pipeline.

---

## A note on REQUIREMENTS.md

The REQUIREMENTS.md next to it is an earlier synthetic statement of
a "capacity model for fax reception." It diverges from the real system:
reception only (no Tx), 100k faxes/day instead of the 10M design target,
invented SLAs. Treat it as a draft of a different task, not a description of this
system; the file's fate is up to the project's author.
