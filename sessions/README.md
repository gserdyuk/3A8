# Session records

One file per working session, written to be read **without the conversation that produced it** and
alongside the others. The intended use is a later analysis session that reads two or three of these
together and looks for what a single session cannot see.

The shape each record keeps, so they can be read in parallel:

| section | holds |
|---|---|
| instrument state | engine versions before and after, and what changed — readings from different versions are not one instrument |
| pinned inputs | md5s and versions, so a number can be tied to the input that produced it |
| **facts** | measurements with provenance, no interpretation |
| rule defects | what broke, which run found it, what the fix was |
| **readings** | interpretation, separated on purpose, each with what would overturn it |
| method decisions | the author's calls, which are not derivable from the numbers |
| debts | what is unfinished, cheapest first |
| open cross-session questions | what this session could not settle alone |
| reproduction | the scripts that regenerate every number |

- [2026-08-20 — the Hotyn chain run end to end](2026-08-20_hotyn_chain_end_to_end.md)
- [2026-08-21…22 — the course correction, the rate card, and the first deliverable](2026-08-22_course_correction_and_first_deliverable.md)
- [2026-08-22…23 — the chain against a fact](2026-08-22_faxrxtx_validation.md)
- [2026-08-23…25 — the units, the discipline, and the table fixed](2026-08-25_units_discipline_and_the_fixed_table.md)
- [2026-08-25…26 — the constants counted, the report made a format, and the class returns](2026-08-26_the_report_becomes_a_format.md)
