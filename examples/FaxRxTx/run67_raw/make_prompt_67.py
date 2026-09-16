#!/usr/bin/env python3
"""Run 67: build the Steps B/D (Lytin-G) prompt. Everything the diagnosis may see, nothing about the outcome.

Pasted: the description and the assumption log (as the other sensors saw them); the case profile §1-§4 only (its
header disclosure and §5 concern the outcome and are withheld); the pinned presence convention
(docs/instrument.md §0, verbatim); the bottom-up reading (runs 61-64) with its declaration and its static
blind-spot list (docs/instrument.md §4, verbatim); the two outside-view replies verbatim (run 65); the Step C
reply verbatim (run 66); the orchestrator's pricing of the Step C fills (calibration_66.json) with its choices.
Asserts that FACT is not mentioned outside the pinned texts that already name it.
"""
import hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.dirname(HERE)
REPO = r'C:\home\OhmNova\3A8'
sys.path.insert(0, os.path.join(CASE, 'run61_raw'))
import make_prompts_61_65 as mp

QUAR = mp.QUARANTINE
desc, _ = mp.description()
alog = mp.read('assumptions.md')


def reply(path):
    t = open(path, encoding='utf-8').read()
    return t[t.index('-->') + 3:].strip() + '\n'


prof = open(os.path.join(CASE, 'case_profile.md'), encoding='utf-8').read()
prof = prof[prof.index('### 1. Team'):prof.index('### 5.')].strip() + '\n'
inst = open(os.path.join(REPO, 'docs', 'instrument.md'), encoding='utf-8').read()
unit0 = inst[inst.index('## 0. The unit'):inst.index('In the WBS part, time appears')].strip()
blind4 = inst[inst.index('## 4. What the chain does not have'):inst.index('## 5. Standing')].strip().rstrip('-').strip()
_clause = '; it was not derived from the FaxRxTx outcome'
assert blind4.count(_clause) == 1
blind4 = blind4.replace(_clause, ' [a clause struck by the orchestrator]')
asm_out = open(os.path.join(CASE, 'run63_raw', 'assembly_output.txt'), encoding='utf-8').read()
asm_out = asm_out[:asm_out.index('=== composition, repeat 1 - per activity')].strip()
add = json.load(open(os.path.join(CASE, 'run64_raw', 'addendum_summary.json'), encoding='utf-8'))
cal = json.load(open(os.path.join(CASE, 'run66_raw', 'calibration_66.json'), encoding='utf-8'))
rc1 = reply(os.path.join(CASE, 'run65_raw', 'RC65-1.md'))
rc2 = reply(os.path.join(CASE, 'run65_raw', 'RC65-2.md'))
rk = reply(os.path.join(CASE, 'run66_raw', 'RK66-1.md'))
hk = reply(os.path.join(CASE, 'run64_raw', 'HK64-1.md'))

rows = []
for rep, row in cal['repeats'].items():
    for lv in ('low', 'central', 'high'):
        v = row[lv]
        rows.append('| %s | %s | %.0f | %.1f | %.1f | %.1f | %.1f | %.1f | %.1f | %.1f | %.1f | ×%.3f | ×%.3f |' % (
            rep, lv, row['raw_total_h'], v['additions_elements_h'], v['additions_once_h'], v['after_T1_h'], v['after_T2_product_h'],
            v['B_h'], v['after_T3_T5_h'], v['after_G2_h'], v['after_G1_h'], v['factor_to_after_G2'], v['factor_to_after_G1']))
fills = '\n'.join('| %s | %s | %s | %.1f | %.1f |' % tuple(f) for f in cal['repeats']['2']['central']['fills'])
r1, r2 = cal['repeats']['1'], cal['repeats']['2']

body = f"""Perform Steps B and D for the case below: reconcile the declarations, diagnose the divergence between the bottom-up reading and the two outside-view readings, apply the supplied Step C corrections mechanically, and report the final answer in three parts. Everything you need is in this message; read no files.

{QUAR}

**Output.** Your engine definition's output format, sections 1–7. **State the final answer in net hours of work on the task** (the bottom-up's unit, INPUT 3b), and give, beside it, whatever conversion you apply to put the outside view in that unit, with its source. The orchestrator will convert to staffed person-months afterwards by the pinned convention in INPUT 3b; do not do that conversion for the final answer yourself.

---

# INPUT 1 — the project description (`SYSTEM.md`, with the struck lines marked in place)

{desc}
---

# INPUT 2 — the assumption log (`assumptions.md`), verbatim

{alog}
---

# INPUT 3a — the case profile, pinned before any number (§1–§4; the rest of the form concerns the outcome and is withheld)

{prof}
# INPUT 3b — the pinned unit and presence convention of this instrument (`docs/instrument.md` §0, verbatim)

{unit0}

---

# INPUT 4 — the bottom-up reading (runs 61–64, `Hotyn` chain × Claude Opus 5)

**Declaration.** Unit: **net hours of work on the task** (INPUT 3b). Losses (leave, holidays, sickness): **outside**. Within-day overhead: outside, except the activity rows that name it (planning and tracking per subsystem, status reporting, risk management, mobilisation). Roles: the delivery team's hours on each activity (design, build, test, review, requirement elaboration, planning, documentation, environments). Source of every value: rate table v0.1-h — external industry norms, one sample, **uncalibrated against any outcome**, modern (no era adjustment). Scope: the pinned technology declaration — bespoke construction · test-based assurance, 2 test cycles · direct to production, no acceptance stage · one team · dev/stage/prod · seeded data, **no legacy migration** · operational and user documentation · **no security/compliance assurance**.

**Chain.** Product model `HM61-1` (`Hotyn-M 2.1`; the second repeat `HM61-2` built 91 elements / 75 leaves against 84 / 68, leaf ratio ×1.10; accreted coverage-set Jaccard 0.51; `HM61-1` was closed because it was the repeat that closed without a defect report) → work model (`Hotyn-W 1.2`, 521 element-attached items, 4 batches) → size classes (`Hotyn-D 2.0`, two repeats per batch, 95.6% class agreement) → assembly script (E = (O+4M+P)/6; integration C3 = 20% of the leaf effort beneath every parent incl. the root) → demanded-work addendum (`Hotyn-K 1.1`, gap-blind).

**Readings.**

| sizing repeat | assembly (product + once layer) | demanded-work addendum | **raw chain total** | sd at ρ = 0.5 (convention, not measured) |
|---|---:|---:|---:|---:|
| 1 | {add['repeats']['1']['assembly_h']:.0f} | {add['addendum_E_h']:.0f} | **{add['repeats']['1']['chain_total_h']:.0f}** | {add['repeats']['1']['sd_h']:.0f} |
| 2 | {add['repeats']['2']['assembly_h']:.0f} | {add['addendum_E_h']:.0f} | **{add['repeats']['2']['chain_total_h']:.0f}** | {add['repeats']['2']['sd_h']:.0f} |

Repeat band {add['lo_h']}–{add['hi_h']} (×{add['spread']:.3f}), centre {add['centre_h']} net task hours.

The assembly's own printout (both repeats, named holes, composition by subtree):

```
{asm_out}
```

**Demanded-work addendum (`Hotyn-K 1.1`, verbatim below):** W-F49 (one pass of integration tests on live traffic) and W-F52 (establishing the old version can be decommissioned) priced; **W-F48 (domain immersion and architecture/technology selection) and W-F50 (comparison with the old system until outputs agree) refused** — headcount and parallel-run period undeclared.

<details><summary>HK64-1, verbatim</summary>

{hk}
</details>

**The bottom-up's static blind-spot list** (`docs/instrument.md` §4, verbatim):

{blind4}

---

# INPUT 5 — the outside view, two independent launches of `Lytin-R 1.1` × Claude Opus 5 (run 65), verbatim

Both received INPUT 1 and INPUT 2 and nothing else. Do not average them; each declared its own unit.

## RC65-1

{rc1}
## RC65-2

{rc2}
---

# INPUT 6 — the Step C corrections, `Lytin-K 1.1` × Claude Opus 5 (run 66), verbatim

It saw INPUT 1, INPUT 2 and the bottom-up reading (structure, totals, composition, coverage report). It never saw INPUT 5.

{rk}
---

# INPUT 7 — the orchestrator's pricing of the Step C structural additions, and the chain applied in RK66's order

RK66 states additions A1–A5 as element fills to be priced "by the same chain". The orchestrator priced them with the pinned rate table (a script, `price_fills66.py`) and applied T1–T5, G2, G1 in RK66's §5 order to each repeat. **These are arithmetic, not new rates; you may recompute them, and you may reject a pricing choice below if it contradicts RK66 — say so; you may not change any rate.**

Pricing choices the orchestrator made where RK66 left them open:
- an added element gets the per-element activities its class receives in the crossing (behaviour / store: design, implementation, test design, unit tests, code review; interface: + contract testing; statement: statement realisation), and integration C3 = 20% × its number of ancestors (root included); no requirement elaboration, no change to per-parent items;
- classes and parents: L27 behaviour under N22; L38 store under N50; L51 interface under N80; L46 statement under N90 (repeat 2 only); A2 findings as behaviour under N10, N10, N21, N23, N30, N30, N90, N70, N00, N80 (in RK66's row order); A3 interface under N80; A4 load generator behaviour under N90, and A4's performance-testing rows as once items without C3 (size S: one measurable target each);
- **A5 is not priceable**: the table has no XL row for environment provisioning or hosting set-up (both already at L) — carried at zero, named;
- T1 base = items + C3 inside subtrees N30 and N40 + own items of L46, L47 (repeat 1: {r1['T1_base_h']:.0f} h; repeat 2: {r2['T1_base_h']:.0f} h) + additions placed there.

Central fills (repeat 2), net task hours — items, and items with C3:

| fill | class | size | items | with C3 |
|---|---|---|---:|---:|
{fills}

The chain (net task hours; "product" excludes the once layer and the addendum; B = after T2 + once layer + A4 rows; T3–T5 each on the same B; then + addendum; then × G2; then × G1):

| repeat | level | raw total | + element fills | + once fills | product after T1 | product after T2 | B | after T3–T5 (addendum not yet added) | after G2 | after G1 | ×raw to G2 | ×raw to G1 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
{chr(10).join(rows)}

Note for the units reconciliation: RK66 labels G1 as "net task hours vs working hours" — a multiplier that moves the figure out of the bottom-up's declared unit. INPUT 3b's convention also contains a net-hours-per-present-day figure. Whether G1 and that convention overlap is yours to reconcile before anything is attributed.
"""
for w in ('FACT.md', 'actual outcome'):
    stripped = body.replace(desc, '').replace(alog, '').replace(rc1, '').replace(rc2, '').replace(rk, '').replace(unit0, '').replace(QUAR, '')
    assert w not in stripped, w
p = os.path.join(HERE, 'prompt_G.md')
open(p, 'w', encoding='utf-8', newline='\n').write(body)
print(len(body), hashlib.md5(open(p, 'rb').read()).hexdigest())
