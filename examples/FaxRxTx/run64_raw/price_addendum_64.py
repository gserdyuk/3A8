#!/usr/bin/env python3
"""Run 64: price the demanded-work addendum rows of HK64-1 and add them to the run 63 assembly.

Rows are read from HK64-1.md (the hours columns O h / M h / P h, bold); refused rows carry no values and stay
carried, not priced. E = (O + 4M + P) / 6. The addendum is a once-scoped layer: it enters no C3 base (tools/chain
README). Its sd is the rows' (P - O) / 6 combined at rho = 0.5, added to the assembly's sd linearly, the same way
assemble.py adds its once layer. Writes addendum_summary.json and prints the chain total per repeat.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.dirname(HERE)
text = open(os.path.join(HERE, 'HK64-1.md'), encoding='utf-8').read()
rows, refused = {}, []
for line in text.split('\n'):
    m = re.match(r'\|\s*(W-F\d+)\s*\|', line)
    if not m:
        continue
    c = [x.strip() for x in line.strip().strip('|').split('|')]
    if 'refused' in line.lower() and '**' not in ''.join(c[6:9]):
        refused.append(m.group(1))
        continue
    o, mm, p = (float(re.sub(r'[*\s]', '', x)) for x in c[6:9])
    rows[m.group(1)] = (o, mm, p)
E = {k: (o + 4 * m + p) / 6 for k, (o, m, p) in rows.items()}
sds = [(p - o) / 6 for (o, m, p) in rows.values()]
rho = 0.5
sd_add = ((1 - rho) * sum(s * s for s in sds) + rho * sum(sds) ** 2) ** 0.5
asm = json.load(open(os.path.join(CASE, 'run63_raw', 'assembly_summary.json'), encoding='utf-8'))
out = {'rows_priced': {k: {'OMP_h': rows[k], 'E_h': round(E[k], 1)} for k in rows}, 'rows_refused': refused,
       'addendum_E_h': round(sum(E.values()), 1), 'addendum_sd_h': round(sd_add, 1), 'repeats': {}}
for rep, r in asm['repeats'].items():
    tot = r['total'] + sum(E.values())
    sd = r['sd'] + sd_add
    out['repeats'][rep] = {'assembly_h': r['total'], 'chain_total_h': round(tot, 1), 'sd_h': round(sd, 1),
                           'p10_h': round(tot - 1.2816 * sd), 'p90_h': round(tot + 1.2816 * sd)}
tots = [v['chain_total_h'] for v in out['repeats'].values()]
out.update(lo_h=round(min(tots)), hi_h=round(max(tots)), centre_h=round((min(tots) + max(tots)) / 2),
           spread=round(max(tots) / min(tots), 4),
           sd_rho05_h=round(sum(v['sd_h'] for v in out['repeats'].values()) / len(out['repeats'])))
json.dump(out, open(os.path.join(HERE, 'addendum_summary.json'), 'w', encoding='utf-8'), indent=1)
print(json.dumps(out, indent=1))
