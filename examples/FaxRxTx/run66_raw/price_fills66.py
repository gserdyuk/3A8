#!/usr/bin/env python3
"""Run 66: price RK66-1's structural additions (A1-A5) through rate table v0.1-h and apply its correction chain
(T1-T5, G2, G1) in the order its §5 fixes, to each repeat of the run 63/64 chain, at low / central / high.

What the orchestrator decided here, because RK66-1 left it open (each listed in PRICING_CHOICES and printed):
  - class and parent of every added element; per-element activity set by class as the crossing assigned it
    (behaviour/surface/store: K1 K2 A2 A3 A4; interface: + A10; statement: K3); D4 and per-parent items not added;
  - C3 on an added element = 20% × number of its ancestors (root included), never compounding;
  - A4's performance-testing rows (A9) are once items, no C3 (RK66-1 §5 step 1); the load generator is an element;
  - A5 cannot be priced: the table has no XL row for E1 or E7 ("one class up" from L); carried, named, zero;
  - T1 base = the composition subtotals of N30 and N40 (items + C3 inside) + own item effort of L46 and L47,
    plus the added elements placed under N30 or N40 or on L46; RK66-1 names "items + C3" and nothing finer.
The raw chain numbers come from the assembler itself (its res, read from the frame that writes the summary).
Writes calibration_66.json and prints the table the diagnosis receives.
"""
import inspect, json, os, sys
sys.path.insert(0, r'C:\home\OhmNova\3A8\tools\chain')
import assemble as A
from chainlib import load_rates, make_rate_lookup, E

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.dirname(HERE)

# ---- rerun the run-63 assembly (with its overlay) and capture the assembler's per-element results
captured = {}
_dump = A.json.dump


def grab(obj, fp, **kw):
    fr = inspect.currentframe().f_back
    captured['res'] = fr.f_locals['res']
    captured['model'] = fr.f_locals['model']
    return _dump(obj, fp, **kw)


A.json.dump = grab
ov_src = open(os.path.join(CASE, 'run63_raw', 'assemble_63.py'), encoding='utf-8').read()
ov_globals = {'__file__': os.path.join(CASE, 'run63_raw', 'assemble_63.py'), '__name__': 'ov'}
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(ov_src, 'assemble_63.py', 'exec'), ov_globals)
res, model = captured['res'], captured['model']
add = json.load(open(os.path.join(CASE, 'run64_raw', 'addendum_summary.json'), encoding='utf-8'))
ADDENDUM = add['addendum_E_h']

R = load_rates()
rate, cell_for = make_rate_lookup(R)
ACTS = {'behaviour': ['K1', 'K2', 'A2', 'A3', 'A4'], 'surface': ['K1', 'K2', 'A2', 'A3', 'A4'],
        'store': ['K1', 'K2', 'A2', 'A3', 'A4'], 'interface': ['K1', 'K2', 'A2', 'A3', 'A4', 'A10'],
        'statement': ['K3']}


def ancestors(p):
    n = 0
    while p in model.rows:
        n += 1
        p = model.rows[p]['parent']
    return n


def price_element(cls, size, parent, kind='behavioural'):
    items = sum(E(cell_for(a, cls, size, kind)) for a in ACTS[cls])
    return items, items * (1 + 0.2 * ancestors(parent))


# element fills: (label, class, parent, {level: [sizes]}) ; level in low/central/high
FILLS = [
    ('A1 L27 further-format renderers', 'behaviour', 'N22', {'low': ['S'], 'central': ['S', 'S'], 'high': ['S', 'S', 'S']}),
    ('A1 L38 database schema', 'store', 'N50', {'low': ['S'], 'central': ['M'], 'high': ['L']}),
    ('A1 L51 old-system interface', 'interface', 'N80', {'low': ['S'], 'central': ['M'], 'high': ['L']}),
    ('A2 inbound job hand-off', 'behaviour', 'N10', {'low': [], 'central': ['S'], 'high': ['S']}),
    ('A2 faxes for unknown numbers', 'behaviour', 'N10', {'low': ['S'], 'central': ['S'], 'high': ['S']}),
    ('A2 submission-rejection notices', 'behaviour', 'N21', {'low': ['S'], 'central': ['S'], 'high': ['S']}),
    ('A2 routing-program fallback', 'behaviour', 'N23', {'low': ['S'], 'central': ['S'], 'high': ['M']}),
    ('A2 outbound status recording', 'behaviour', 'N30', {'low': ['S'], 'central': ['S'], 'high': ['S']}),
    ('A2 clean-up of finished status', 'behaviour', 'N30', {'low': ['S'], 'central': ['S'], 'high': ['S']}),
    ('A2 PoP registry maintenance', 'behaviour', 'N90', {'low': [], 'central': ['S'], 'high': ['S']}),
    ('A2 account creation and provisioning', 'behaviour', 'N70', {'low': ['S'], 'central': ['M'], 'high': ['M']}),
    ('A2 inventory of v1 core functions', 'behaviour', 'N00', {'low': [], 'central': ['S'], 'high': ['M']}),
    ('A2 ending coexistence', 'behaviour', 'N80', {'low': [], 'central': ['S'], 'high': ['M']}),
    ('A3 initial load of user accounts', 'interface', 'N80', {'low': ['S'], 'central': ['M'], 'high': ['L']}),
    ('A4 load generator (PoP and mail stream)', 'behaviour', 'N90', {'low': [], 'central': ['M'], 'high': ['L']}),
]
L46_FILL = {'low': [], 'central': ['S'], 'high': ['M']}          # repeat 2 only, statement under N90
A4_ROWS = {'low': [('A9 on L47', 'S')], 'central': [('A9 on L46', 'S'), ('A9 on L47', 'S')],
           'high': [('A9 on L46', 'S'), ('A9 on L47', 'S')]}   # one measurable target each (A6: 30/s; 300/s)
T = {'T1': (1.00, 1.17, 1.34), 'T2': (1.05, 1.12, 1.25), 'T3': (0.04, 0.08, 0.15), 'T4': (0.03, 0.07, 0.14),
     'T5': (0.02, 0.05, 0.08), 'G2': (1.00, 1.15, 1.27), 'G1': (1.15, 1.25, 1.40)}
LEVELS = ('low', 'central', 'high')

out = {'pricing_choices': __doc__, 'repeats': {}}
for rep, r in res.items():
    leafE, c3 = r['leafE'], r['c3']
    sub = lambda top: sum(leafE.get(x, 0.0) for x in model.subtree(top)) + sum(c3.get(x, 0.0) for x in model.subtree(top) if x in c3)
    t1_base0 = sub('N30') + sub('N40') + leafE.get('L46', 0.0) + leafE.get('L47', 0.0)
    P0 = r['leaf_total'] + r['c3_total']
    once0 = r['once_total']
    row = {'P0_product_base_h': round(P0, 1), 'once_h': round(once0, 1), 'addendum_h': ADDENDUM,
           'raw_total_h': round(P0 + once0 + ADDENDUM, 1), 'T1_base_h': round(t1_base0, 1)}
    for i, lv in enumerate(LEVELS):
        lines, add_elem, t1_extra = [], 0.0, 0.0
        for lab, cls, parent, lvls in FILLS:
            for s in lvls[lv]:
                it, tot = price_element(cls, s, parent)
                add_elem += tot
                lines.append((lab, cls, s, round(it, 1), round(tot, 1)))
                if parent in ('N30', 'N40'):
                    t1_extra += tot
        if str(rep) == '2':
            for s in L46_FILL[lv]:
                it, tot = price_element('statement', s, 'N90')
                add_elem += tot
                t1_extra += tot
                lines.append(('A1 L46 capacity statement (repeat 2)', 'statement', s, round(it, 1), round(tot, 1)))
        add_once = sum(E(cell_for('A9', 'statement', s)) for _, s in A4_ROWS[lv])
        a5 = 0.0
        P1 = P0 + add_elem
        P1t = P1 + (T['T1'][i] - 1) * (t1_base0 + t1_extra)
        P2 = P1t * T['T2'][i]
        B = P2 + once0 + add_once + a5
        s5 = B * (1 + T['T3'][i] + T['T4'][i] + T['T5'][i])
        s6 = s5 + ADDENDUM
        s7 = s6 * T['G2'][i]
        s8 = s7 * T['G1'][i]
        row[lv] = {'additions_elements_h': round(add_elem, 1), 'additions_once_h': round(add_once, 1), 'A5_h': 'not priceable (no XL row for E1/E7)',
                   'after_1_h': round(P1 + once0, 1), 'after_T1_h': round(P1t, 1), 'after_T2_product_h': round(P2, 1), 'B_h': round(B, 1),
                   'after_T3_T5_h': round(s5, 1), 'after_addendum_h': round(s6, 1), 'after_G2_h': round(s7, 1), 'after_G1_h': round(s8, 1),
                   'factor_to_after_G2': round(s7 / row['raw_total_h'], 3), 'factor_to_after_G1': round(s8 / row['raw_total_h'], 3),
                   'fills': lines}
    out['repeats'][str(rep)] = row
json.dump(out, open(os.path.join(HERE, 'calibration_66.json'), 'w', encoding='utf-8'), indent=1)
print('%-8s %-8s %9s %9s %9s %9s %9s %9s %9s %7s %7s' % ('repeat', 'level', 'raw', '+adds', 'T1', 'T2+once', 'T3-T5', 'G2', 'G1', 'xG2', 'xG1'))
for rep, row in out['repeats'].items():
    for lv in LEVELS:
        v = row[lv]
        print('%-8s %-8s %9.0f %9.0f %9.0f %9.0f %9.0f %9.0f %9.0f %7.3f %7.3f' % (rep, lv, row['raw_total_h'], v['additions_elements_h'] + v['additions_once_h'],
              v['after_T1_h'], v['B_h'], v['after_addendum_h'], v['after_G2_h'], v['after_G1_h'], v['factor_to_after_G2'], v['factor_to_after_G1']))
print('T1 base per repeat:', {k: v['T1_base_h'] for k, v in out['repeats'].items()})
for lab, cls, s, it, tot in out['repeats']['1']['central']['fills']:
    print('   central fill: %-42s %-9s %-2s items %5.1f  with C3 %5.1f' % (lab, cls, s, it, tot))
