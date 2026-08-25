# Run 35 — the concept stage, and the point at which this case stopped being able to score anything

**2026-08-24.** The author, answering a question about a parameter the rate row itself declared:

> *How many of the ten were in the two-month concept discussion, and were they doing anything else?*
> — **All of them. And no, nothing else.**

---

> **§6 superseded by the author's decision, 2026-08-25.** Asked whether a comparison whose unit
> conventions arrived after the estimate can count as a score, the author ruled **yes** — *"an
> explanation after the fact is a poor explanation, but it is still an explanation."* FaxRxTx is
> therefore case 1 of the exit criterion's four and **passes on the centre at ×1.21**. The reasoning
> in §6 stands as reasoning. Note what the decision does *not* cover: the stage headcount this
> document is about was supplied and **has not been applied** — the scored number still prices the
> concept stage at 2% where the fact puts it at 17%.


## 1. The arithmetic

`W-F48` was priced by the gap-blind rate author at **43.5 pd = 261 person-hours**, on an assumption it
stated inside the row: *"the row aggregates the effort of everyone who must actually hold the domain —
assumed two people… that headcount is stated here because it is not derivable from the row's
description and it scales the row linearly."*

The actual parameter: **10 people × 2 months, nothing else** = 10 × 42 nominal days × 0.88 × 6 h =
**2 218 person-hours**.

**The row was low by ×8.5.**

## 2. Why this is a parameter update and not an excuse — the three-question test applied to itself

| question | answer |
|---|---|
| is the thing in a pinned input? | **yes** — §6 and A1 state the stage and its duration |
| is it already counted? | the **stage** is counted once, in `W-F48`. The **headcount** was a declared assumption inside the row, written gap-blind before any total existed |
| was it recorded before the comparison? | the stage yes; **the headcount value, no — it arrived now** |

So the legitimate act is to **update a declared parameter**, which is exactly what declaring it was
for. That is a different species from mining a new true fact until the gap closes.

## 3. It flips the verdict, so it gets maximum scepticism, not minimum

**Check (a) — overlap with element design.** `Hotyn-K` bounded `W-F48.3` explicitly: *"this row is the
act of choosing and recording it. It does not include producing a design (component decomposition,
interface definition)."* If part of those two months was design, the chain prices it a second time in
`K1`.

Measured: **the whole `K1` element-design layer is 68 items, 421 person-hours, 4.8% of the chain.**
Even total overlap cannot account for a delta of 1 957 h. And §6's own wording — *"discussions,
immersion in the subject area, and technology selection"* — is `W-F48`'s scope, not design. **The check
passes, and it is small either way.**

**Check (b) — and this one does not pass.** Ten people for two of twelve months **is one sixth of the
fact, by arithmetic**. The "correction" is therefore not an estimate at all: it is a slice of the answer
handed over. That is simultaneously the strongest argument for its legitimacy — it cannot have been
fitted — and the reason it proves nothing about the instrument.

## 4. So split the comparison, and look at what is still being tested

| | chain | fact | ratio |
|---|---:|---:|---|
| concept stage | *taken from the fact* | 2 218 h | **not a test** |
| **everything else, chain as it stands** | 8 454 h | 11 088 h | **×1.312** |
| **everything else, + the two pending adjudications** | 10 452 h | 11 088 h | **×1.061** |

Blended totals, for the record only: 10 672 h (×1.247, inside the gate) and 12 670 h (×1.050, inside).
**Those two figures should not be quoted as a score.** A sixth of the numerator now comes from the
denominator.

## 5. The finding that is worth more than the verdict

**This is not a level error. It is one rate row, for a stage that is 17% of the project, written at
2% of it.** A defect of that shape is invisible in a total and lethal inside it, and it is exactly what
a rate card is supposed to make findable.

Its cause is on the record and is not a mistake by the rate author. `Hotyn-K` **refused** to price the
stage from the calendar duration the client stated — correctly, because a duration may not enter a rate
table — and then had to invent a headcount in order to convert calendar into effort. **The refusal was
right and the substitute was wrong by ×8.5.**

**The fix is structural, not numeric: stage headcount is a declaration parameter**, of the same kind as
environment count and cycle count — supplied by whoever knows the case, before pricing, in the
technology declaration. It is not a rate author's assumption to make, because the rate author is
gap-blind by design and therefore has nothing to make it from.

Proposed: `docs/technology_catalogue.md` gains a parameter class for **staffing of once-scoped stages**,
and any rate row that scales linearly in a headcount refuses to be priced until that parameter is
declared — the same discipline as A9's "≥1 stated target".

## 6. What this case can and cannot do any more

**Three parameters have now come from the fact's owner after the estimate existed:** staffed-versus-
delivered time, the presence fraction `L`, and the concept-stage headcount. Every one of them was
legitimate — each was a genuine input the case had never been asked for. Cumulatively they mean
something that has to be said plainly:

> **FaxRxTx can no longer score the instrument.** Not because a factor was fitted — none was — but by
> information transfer. The residue is now ×1.05–1.06, and beneath it sit the fact's own ±20% band, an
> `L` that is still undeclared and worth ±5% across its plausible range, two adjudications not yet
> made, and one parameter taken directly from the fact. **The comparison has run out of resolving
> power.** A gate cleared by being handed a sixth of the answer is not a gate.

Run 32 said this case was spent because `L-1` had been fitted on it; run 33 gave it back when `L-1` was
withdrawn. It is spent again, for a better reason, and this time it does not come back.

**What the case can still be used for**, and these are not small:

- the **five unsizeable elements and thirteen closure violations** still want adjudicating on their
  merits, and their +182 pd is now measurable against something;
- the **four scope decisions** still want ruling;
- the **`W-F48` defect** (§5) is a transferable finding about the rate card's design and owes nothing to
  the fact;
- and the **catalogue defects** run 30 found — `A10` blind to internal APIs, `A9` unreachable from a
  behaviour-carried availability obligation — are untouched by any of this.

## 7. The rule this whole episode produces

Everything asked for over three days — staffed versus delivered, the presence fraction, the concept
stage's headcount, the team's grade, the training load — is a **case condition**. None of it is a
requirement. **All of it was obtainable on day one**, from the same person, before any number existed.

> **A case profile is pinned with the requirements, before any estimate: the conditions under which the
> work was or will be done — team grade and domain experience, declared overheads, the process, and the
> staffing of every stage the method prices separately. A case whose conditions arrive after its number
> can be learned from. It cannot score.**

That is the finding of `run33` §9 in its final form, and it has now cost three days and one validation
case to arrive at, which is roughly what such findings cost.
