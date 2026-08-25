# What unit is the rate table actually in? — the question nobody checked

**2026-08-24.** The author asks: *when the rate table was compiled, was a 6-hour or an 8-hour working
day taken into account?*

The answer is on the record, it is not the one I have been computing with, and it is worth **×1.33** —
larger than every correction discussed in the last three days put together.

---

## 1. What the table says

Two lines, both written by `Hotyn-K 1.0` **alongside the values**, in the same run:

- `docs/rate_table.md` §2, line 37: *"Units: person-days (pd), **1 pd = 8 h net**. Team assumed
  throughout: competent engineers, senior/middle mix, enterprise delivery."*
- §5 Notes on use, line 442: *"**Units:** person-days; **1 pd = 8 hours of net working time.** O ≤ M ≤ P
  holds in every row."*

**The table was written under 8 net hours to the person-day.** That is what the author of the values
had in mind while writing them, and it is stated twice.

## 2. Where the 6 came from

From the author's adjudication of 2026-08-22, now the banner at the top of the same file:

> *"one person-day = one assigned working day — the convention the table's external sources natively
> record. The '8 hours of net working time' wording below is v0.1's original text, superseded…
> **values are unchanged**, since they were compiled from assigned-day norms in the first place."*

**A relabelling, with no value re-derived.** If the values were budgeted as 8 net hours and are then
declared to mean 6, every number in the table quietly falls by a third.

## 3. And the table's own author refused to certify it

This was not missed. `Hotyn-K` raised it **unprompted**, in addendum A3, before anyone asked:

> *"My instruction for these rows says one person-day is one assigned working day… My base table's
> stated convention is 8 hours of net working time. **Those are not the same unit**: an assigned working
> day contains meetings, correspondence, context switching and interruption, and typically yields well
> under 8 net hours. … If base-table cells are in net-hour days, **the two sets of rows may not be
> summed without a declared conversion, and one of the two labels is wrong.** I am raising this rather
> than resolving it."*

When told the author had adjudicated, it accepted — and marked exactly what kind of acceptance it was:

> *"I cannot verify the compilation claim, because verifying it would mean reading the base table, which
> I may not do. I accept it on the owner's statement and mark it as **accepted-on-statement, not as
> checked**."*

**The one party that could have known declined to confirm it, and said why.**

## 4. What I then did, which was worse

`A2` and `A3` — the eleven FaxRxTx demanded-work rows — were written **in assigned working days**, on my
instruction, and `Hotyn-K` warned in the same breath that they may not be summed with base-table rows
without a declared conversion.

**I overrode that warning with the author's statement and summed them anyway.** The assembly in
`run31_raw/assemble_faxrxtx.py` adds 1 335 pd of base-table rows to 117 pd of addendum rows as though
they were the same unit. By the two documents' own declarations, they are not.

## 5. The arithmetic, all three readings

The **fact** is unambiguous: 2 520 nominal staffed days × presence `L` × 6 delivered hours =
**13 306 person-hours** at `L` = 0.88. The ambiguity is entirely on the estimate's side.

| reading | chain as it stands | + two adjudications | + W-F48 at the real headcount | + both |
|---|---|---|---|---|
| **6 h/pd** — what I have been computing | 8 715 h · ×1.53 **low** · fail | 10 713 h · ×1.24 low | 10 672 h · ×1.25 low | 12 670 h · ×1.05 low |
| **8 h/pd** — what the table's text says | 11 620 h · ×1.15 low | 14 284 h · ×1.07 **high** | 13 490 h · ×1.01 high | 16 154 h · ×1.21 high |
| **mixed** — each document's own label | 11 385 h · ×1.17 low | 14 049 h · ×1.06 high | 13 342 h · **×1.003** | 16 006 h · ×1.20 high |

**The estimate spans ×1.53 low to ×1.21 high across readings of its own unit — a range of ×1.85.** No
score computed over that range means anything.

## 6. The reading the evidence supports is the favourable one, and that is why it is not being adopted

Under 8 h/pd the chain passes as it stands; with the concept stage corrected it lands **within 0.3% of
the fact**; and the two pending adjudications would push it **20% over**. Every number moves the right
way.

The evidence — two explicit statements by the party that wrote the values, plus that party's later
refusal to certify the relabelling — does point at 8. **And "the evidence supports the favourable
reading" is precisely the sentence that should stop a scoring act, not complete one.** It has the same
shape as everything the last three days killed.

**So: no reading is adopted, and no score stands.** The unit of the estimate is now the largest open
parameter in the comparison, and it must be settled by **re-derivation, not by anyone's statement —
neither the author's nor mine.**

## 7. The test, and it is cheap and needs nobody's word

Ask `Hotyn-K`, gap-blind — no total, no gap, no project, no mention of this question's existence — to
price a **sample of the same activities directly in person-hours**: *for this activity, at this size,
for this team grade, how many person-hours of work?* Then compare against the person-day values already
in the table.

- If `K2 · behaviour · S` comes back near **8 hours**, the table is in net-hour days and the banner is
  wrong.
- If it comes back near **6**, the banner is right and the original §2/§5 wording was the error.
- If it comes back at neither, the table has no consistent unit and v0.2 is a re-derivation, not an
  edit.

Ten to fifteen rows spanning the classes and sizes is enough, and the run costs one agent.

**And then write the table in hours in the first place** — which is exactly the author's own instruction
of two turns ago, *"move to person-hours, then there is nothing to manipulate."* It removes this failure
mode permanently, on both sides, because an hour has no convention inside it.

## 8. The pattern: three unit failures in three days, all the same shape

| # | where | what happened |
|---|---|---|
| 1 | the **fact** | recorded as headcount × calendar and never interrogated — staffed presence read as delivered work |
| 2 | **my arithmetic** | applied the 6/8 to one side of the comparison only — a double count worth ×1.33, in my own favour |
| 3 | the **rate table** | its hour content asserted by relabelling, never re-derived; certification explicitly refused by the party that wrote the values |

**The method has been carrying an unverified unit on both sides of the comparison at the same time.**
Every accuracy claim made in the last three days — including the ones in `run34` and `run35` that read
as findings — rests on two conventions of which neither has been checked.

That is the finding. It is not about FaxRxTx and it does not go away with a second case: **until the
estimate's unit is re-derived and the fact's unit is declared, this method cannot score anything at
all.** Everything else in the backlog is downstream of it, and it moves to the top.
