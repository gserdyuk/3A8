Write addendum rows for the rate table: four activities that the technology catalogue does not contain, each performed once for a whole work model. Everything you need is in this message; read no files.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Your engine definition's format, restricted to what an addendum needs: contamination check, the declaration, the rows, findings, notes on use. State values in **hours of work on the task** (the table these rows join is kept in that unit); if your base rates are natively in another unit, say so and give the conversion rather than restating silently.

---

# INPUT 1 — the activities, as worded by the work model

Each is a **demanded-work branch**: an obligation on the doing that the client stated and that no catalogue activity absorbs. Each occurs **once** for the whole system (scope `once`, size `single`); there is no element class and no size class to count.

| row id | activity, as worded | what it is, in the work model's words |
|---|---|---|
| W-F48 | a stage of domain immersion and architecture/technology selection (distributed-hash-table approaches and the like were studied) | a period of the team learning an unfamiliar domain and deciding the architecture and technologies; no property of the delivered system satisfies it |
| W-F49 | integration tests on the real message stream | integration testing performed against live production traffic, not against prepared test data |
| W-F50 | the integration-test results are compared with the old system and must agree | an act of comparison and adjudication of the new system's outputs against a running predecessor's outputs on the same stream, until they agree |
| W-F52 | the old version can be decommissioned | establishing that the predecessor can be switched off: traffic cut over, the parallel period ended, no obligation left on the predecessor |

The production cutover itself (the new system taking production traffic) is **not** among these: it is already priced by a catalogue activity.

# INPUT 2 — the sizing rule for these rows

Scope `once`, size `single`: one row per activity, O / M / P for performing it once for the whole system.

**Staffing rule, pinned in the case profile before any estimate:** the headcount of any separately-priced stage is a declaration parameter, and **for these four stages it is not declared (unknown)**. A row whose effort scales with the number of people taking part, or with the length of a calendar period, **must not be priced on a guessed headcount or a guessed period**: refuse it and name the missing parameter. A row whose effort does not depend on either may be priced; say which kind each row is.

# INPUT 3 — the assumed team grade

Competent engineers, senior/middle mix, enterprise delivery.
