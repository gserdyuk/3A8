#!/usr/bin/env python3
"""Run 66: build the Step C (Lytin-K) prompt from the pinned inputs and the bottom-up chain's own outputs.

Contents: the project description as the outside-view sensor received it (run 65 INPUT 1, same struck lines),
the assumption log verbatim, and the bottom-up reading of runs 61-64: structure (element tree with classes and
size classes), totals, composition, coverage report. It contains nothing from run 65 and no target of any kind.
The script asserts that no run-65 file is read and that no quantile word appears in the result.
"""
import csv, hashlib, json, os, re, sys
sys.path.insert(0, r'C:\home\OhmNova\3A8\tools\chain')
from chainlib import Model

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.dirname(HERE)
QUAR = ("**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — "
        "a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, "
        "do not treat it as contamination that stops the run: report in your contamination check that it was present and "
        "that you quarantined it, and proceed on the pasted input alone.")

sys.path.insert(0, os.path.join(CASE, 'run61_raw'))
import make_prompts_61_65 as mp  # the same description() as the outside view received
desc, _ = mp.description()
alog = mp.read('assumptions.md')

model = Model(os.path.join(CASE, 'run61_raw', 'HM61-1.md'))
cls = {r['element']: r['class'] for r in csv.DictReader(open(os.path.join(CASE, 'run62_raw', 'classes.tsv'), encoding='utf-8'), delimiter='\t')}
acts = {}
for r in csv.DictReader(open(os.path.join(CASE, 'run62_raw', 'work_model.tsv'), encoding='utf-8'), delimiter='\t'):
    acts.setdefault(r['element'], set()).add(r['activity'])
asm = json.load(open(os.path.join(CASE, 'run63_raw', 'assembly_summary.json'), encoding='utf-8'))
add = json.load(open(os.path.join(CASE, 'run64_raw', 'addendum_summary.json'), encoding='utf-8'))
out_txt = open(os.path.join(CASE, 'run63_raw', 'assembly_output.txt'), encoding='utf-8').read()

# sizes per repeat, as the assembler read them (re-run its parser through the run-63 overlay)
import assemble as A
leaf_re = re.compile(r'\b(?:%s)\b' % '|'.join(sorted(map(re.escape, model.leaves()), key=len, reverse=True)))
sizes = {}
for rep in (1, 2):
    S = {}
    for b in 'ABCD':
        fn = os.path.join(CASE, 'run63_raw', 'HD63-%s%d.md' % (b, rep))
        s, k, sp = A.parse_reading(fn, leaf_re)
        S.update(s)
    sizes[rep] = S

rows = []
for e in model.order:
    r = model.rows[e]
    s1, s2 = sizes[1].get(e, ''), sizes[2].get(e, '')
    sz = '—' if model.parents().__contains__(e) else '%s / %s' % (s1 or 'unsizeable', s2 or 'unsizeable')
    rows.append('| %s | %s | %s | %s | %s | %s | %s |' % (e, r['name'], r['parent'], r['origin'], r['coverage'] or '—', cls.get(e, 'aggregate'), sz))

r1, r2 = asm['repeats']['1'], asm['repeats']['2']
comp = out_txt[out_txt.index('=== composition, repeat 1 - per top-level'):out_txt.index('=== demanded ids')]

body = f"""Propose the Step C calibration corrections for the bottom-up estimate below. Everything you need is in this message; read no files.

{QUAR}

**Output.** Your engine definition's output format, sections 1–5, with the declaration before any addition. Record the engine stamps of the bottom-up chain you are calibrating (given in INPUT 3).

---

# INPUT 1 — the project description (`SYSTEM.md`, with the struck lines marked in place)

{desc}
---

# INPUT 2 — the assumption log (`assumptions.md`), verbatim

{alog}
---

# INPUT 3 — the bottom-up estimate: structure, totals, composition, coverage report

**Chain and engines.** Product model `HM61-1` by `Hotyn-M 2.1` (one of two repeats; the other, `HM61-2`, built 91 elements / 75 leaves against this one's 84 / 68 — ×1.10 on leaves); work model by `Hotyn-W 1.2` (4 batches, one crossing each); size classes by `Hotyn-D 2.0` (two repeats per batch); prices from a pinned rate table of **external industry norms in net task hours, uncalibrated against any outcome** (rate table v0.1-h), joined by a script; four demanded-work rows priced or refused by a gap-blind `Hotyn-K 1.1` addendum. All sensors ran on Claude Opus 5.

**Unit of every figure below: net hours of work on the task.** Leave, public holidays and sickness are outside; so are within-day overheads (meetings, coordination, interruptions) except where an activity row names them (planning and tracking, status reporting, risk management). Roles: the delivery team's hours on each activity.

**Scope and declaration the chain was built under** (a pinned technology declaration, chosen once for everybody): bespoke construction on a mainstream stack · test-based assurance, 2 test execution cycles · direct to production, **no acceptance stage** · one team with planning and reporting ceremonies · environments dev, stage, production · **reference data seeded, no legacy data migration** · operational and user documentation · **no security or compliance assurance activities**. The declared sensitivities, not priced: acceptance with UAT; migration of legacy data; no documentation; penetration testing.

**The rate table's era.** Its values are modern external norms; the project ran on the era described in A5. No era adjustment has been applied anywhere in the chain.

## Totals

| reading | element items | integration (C3: 20% of the leaf effort beneath every parent, root included) | once and per-environment items | demanded-work addendum | **total** |
|---|---:|---:|---:|---:|---:|
| sizing repeat 1 | {r1['leaf_total']:.0f} | {r1['c3_total']:.0f} | {r1['once_total']:.0f} | {add['addendum_E_h']:.0f} | **{add['repeats']['1']['chain_total_h']:.0f}** |
| sizing repeat 2 | {r2['leaf_total']:.0f} | {r2['c3_total']:.0f} | {r2['once_total']:.0f} | {add['addendum_E_h']:.0f} | **{add['repeats']['2']['chain_total_h']:.0f}** |

Repeat spread ×{add['spread']:.3f}; centre {add['centre_h']} h. Every figure is E = (O + 4M + P) / 6 of the table's cells.

## Composition (repeat 1), as printed by the assembly script

```
{comp.rstrip()}
```

Demanded-work addendum (once, enters no integration base): W-F49 integration tests on the real message stream, E {add['rows_priced']['W-F49']['E_h']} h · W-F52 establishing that the old version can be decommissioned, E {add['rows_priced']['W-F52']['E_h']} h.

## Structure — the closed product model with the crossing's element classes and the two sizing repeats

84 elements: 16 parents (never sized), 68 leaves. Coverage lists obligation ids of the pinned list (F01–F47 product obligations; F48–F52 demanded work, carried in the work model, not in the product model). Size classes S / M / L / XL are counts of named things (actions, operations, user tasks, entity kinds), not effort.

| id | name | parent | origin | coverage | class | size (repeat 1 / 2) |
|---|---|---|---|---|---|---|
{chr(10).join(rows)}

Work items: 521 element-attached items from the crossing (per element: design, implementation, test design, unit tests, code review, requirement elaboration, interface contract tests, seed-data items on stores, statement realisation; per parent: test execution ×2 cycles, defect resolution ×2 cycles, regression suite, test data, planning and tracking, user documentation where a surface is beneath), plus the root's per-parent items, plus 16 once/per-environment items, plus the two priced addendum rows.

## Coverage report

**Categories of work the estimate carries** (each is a priced activity): element design and implementation; test design, unit and component tests, code review; test execution and defect resolution (2 cycles per subsystem); automated regression suite; test data preparation; interface contract testing; requirement elaboration per element; planning and tracking per subsystem; integration at every aggregation node (C3); test strategy; production verification checklist; mobilisation and set-up; status reporting; risk and dependency management; provisioning of three environments; build and deployment pipeline; promotion procedure; configuration management and version control set-up; **production cutover**; hosting set-up; operational runbook; support handover pack; release notes; user documentation; seed data specification, load and reconciliation on stores that need it; integration tests on the real message stream (one pass); establishing that the old version can be decommissioned.

**Carried, NOT priced — awaiting a parameter** (refused by the gap-blind rate author):
- **W-F48, domain immersion and architecture/technology selection** — its effort is headcount × stage length; the stage's headcount is undeclared (the case profile records it as unknown; A3 excludes headcount by design).
- **W-F50, comparison of the new system's outputs with the old system's until they agree** — scales with the parallel-run period, which is undeclared; the rate author also judged its honest most-likely above the table's per-row ceiling and asked for a catalogue split (comparator build · per class of discrepancy · per week of monitoring).
- Also named by the rate author: W-F49 prices one pass, **not a sustained soak window** on live traffic.

**Named holes — elements the sizing sensors could not size, priced at nothing** (per-element items on them are absent from the totals):
- L27 further-format renderers (the source says 8–10 formats and names 7) — both repeats.
- L38 system database schema (no entity kinds named) — both repeats.
- L51 old-system exchange interface (no operations named) — both repeats.
- L56 first-version core function set, as replaced (the functions are never listed) — both repeats.
- L46 capacity provision for nominal volume — repeat 2 only.
- Seed-data items on L32 (both) and on D03 (repeat 2) — the sensors found nothing to pre-load.

**Not in the declaration, therefore in no item**: acceptance testing by a separate party; legacy data migration (accounts, configurations, archive); security or compliance assurance; performance, capacity and burst testing (the performance-testing activity applies only to statements with a measurable target, and the crossing refused it on both candidate statements); hyper-care after cutover; operating the old system during coexistence; hardware procurement and cluster installation.

**Closure findings the sizing sensors named** (work they judged necessary and absent; not priced): hand-off of jobs to the workers on the inbound path; handling of faxes for unknown numbers; submission-rejection notices; fallback when the routing program gives no answer; recording outbound status changes in the token store; clean-up of finished status entries; a registry of points of presence maintained after its seed load; account creation / provisioning; an inventory of the first version's core functions; initial migration of user accounts from the old system; ending coexistence.
"""
for bad in ('P10', 'P50', 'P80', 'P90', 'quantile', 'reference class', 'RC65'):
    assert bad not in body.replace(alog, ''), bad   # A8 of the pinned log names the method, carries no result
p = os.path.join(HERE, 'prompt_C.md')
open(p, 'w', encoding='utf-8', newline='\n').write(body)
print(len(body), hashlib.md5(open(p, 'rb').read()).hexdigest())
