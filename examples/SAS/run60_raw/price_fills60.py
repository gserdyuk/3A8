"""Run 60 - price the Step C fills of RK60 (H, hole fills; C, closure fills) with rate table v0.1-h, as RK60 §3
instructs: each fill is the Hotyn-W 1.2 element-attached item set of its element class, at size S (low) / M
(central) / L (high); D4 at S (a fill covers about one requirement); NFR verification targets at the A9 cell of the
one carried response-time element (class L); integration at the method's own 20% per ancestor, along the real parent
path for holes and under the named subsystem (depth 2, x1.4) or its matching child node (depth 3, x1.6) for closure
fills. Writes bases60.md (what the diagnostician is given: the priced bases, never the chain's result) and
orchestrator_recomputation.md (the orchestrator's own application of RK60's order, made before the diagnostician
returns, so its arithmetic can be checked rather than trusted). The mapping of RK60's fill lists to parents and
counts is this script's reading of RK60 and is printed so it can be disputed.
Usage: python examples/SAS/run60_raw/price_fills60.py"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.abspath(os.path.join(HERE, '..'))
sys.argv = ['x']
g = {'__file__': os.path.join(CASE, 'run59_raw', 'assemble_sas58.py'), '__name__': 'assembly'}
src = open(g['__file__'], encoding='utf-8').read()
exec(compile(src, g['__file__'], 'exec'), g)          # RATES, rate, cell_for, E, READINGS, assemble, PARENT
rate, cell_for, E, assemble = g['rate'], g['cell_for'], g['E'], g['assemble']
PARENT = g['PARENT']
TOTALS = {rep: assemble(rep)['total'] for rep in (1, 2)}
SIZES = {'low': 'S', 'central': 'M', 'high': 'L'}
LEVELS = ('low', 'central', 'high')


def depth(e):
    d = 0
    while PARENT.get(e) in PARENT:
        e = PARENT[e]
        d += 1
    return d


def item_set(cls):
    if cls == 'interface':
        return ['K1', 'K2', 'A2', 'A3', 'A4', 'A10', 'D4']
    if cls == 'statement':
        return ['K3', 'D4']
    return ['K1', 'K2', 'A2', 'A3', 'A4', 'D4']       # behaviour, surface, store


def price_element(cls, size, acts, kind='compliance'):
    tot = 0.0
    for a in acts:
        sz = 'S' if a == 'D4' else size
        c = cell_for(a, cls, sz, kind)
        assert c is not None, (a, cls, sz)
        tot += E(c)
    return tot


A9_L = E(rate('A9', 'L'))

# ------------------------------------------------------------------ H: hole fills (RK60 §3, table H)
def H_fills(rep, level):
    size = SIZES[level]
    rows = []
    # Access Data REST API: its own six items, real path
    f = 1 + 0.2 * depth('A140')
    h = price_element('interface', size, ['K1', 'K2', 'A2', 'A3', 'A4', 'A10']) * f
    rows.append(('A140 Access Data REST API, 6 items (interface %s), x%.1f' % (size, f), h))
    # migration of stores matching an A16 kind: 1 / 2 / 3 stores, in RK60's order
    stores = {'low': ['A089'], 'central': ['A089', 'A018'], 'high': ['A089', 'A018', 'C01']}[level]
    for e in stores:
        f = 1 + 0.2 * depth(e)
        h = price_element('store', size, ['G2m', 'G3m', 'G4m']) * f
        rows.append(('%s migration items G2m/G3m/G4m (store %s), x%.1f' % (e, size, f), h))
    if rep == 2:
        for e in ('A158', 'A159'):
            f = 1 + 0.2 * depth(e)
            h = E(cell_for('K3', 'statement', size, 'compliance')) * f
            rows.append(('%s K3 (statement-compliance %s), x%.1f' % (e, size, f), h))
    return rows


# ------------------------------------------------------------------ C: closure fills (RK60 §3, table C)
# (label, element class, parent factor, counts low/central/high)
C_SPEC = [
    ('surfaces for screenless behaviours: record entry/edit (and cloning at high) and hierarchy editor, Product and Location, under the module (x1.4); duplicate review and status/reuse-date under the shared-record child nodes (x1.6)',
     'surface', None, {'low': [1.6] * 4, 'central': [1.4] * 4 + [1.6] * 2, 'high': [1.4] * 6 + [1.6] * 2}),
    ('other surfaces: approval review-and-decision (N07), admin assignment (N06), owner publish/share and consumer request/decision (N12), training links (N10), help-desk reset trigger (N06, high only)',
     'surface', 1.4, {'low': 2, 'central': 5, 'high': 6}),
    ('behaviours: deactivate company user (N06), entitlement check before viewing (N21), export-option enforcement (N11), data-challenge follow-up (N07), edit-lock release (N07, high), role seeding (N06, high)',
     'behaviour', 1.4, {'low': 2, 'central': 4, 'high': 6}),
    ('interfaces: 3scale usage collection (N09); import/export through the API (N11, high only)',
     'interface', 1.4, {'low': 1, 'central': 1, 'high': 2}),
    ('stores: report definitions and schedules (N09), groups and members (N12), per-user subscriptions and onscreen notifications (N08, central), pending requests (N12) and page-layout templates (N19) at high',
     'store', 1.4, {'low': 2, 'central': 4, 'high': 6}),
]


def C_fills(level):
    size = SIZES[level]
    rows = []
    for label, cls, f, counts in C_SPEC:
        factors = counts[level] if isinstance(counts[level], list) else [f] * counts[level]
        per = price_element(cls, size, item_set(cls))
        h = sum(per * x for x in factors)
        rows.append(('%s — %d fills (%s %s)' % (label, len(factors), cls, size), h))
    # NFR verification targets: the A9 cell of the carried response-time element (class L), under N22 (x1.4)
    n = {'low': 2, 'central': 3, 'high': 3}[level]
    rows.append(('NFR verification targets: capacity/volume, availability/failover, (central) latency — %d x A9 L cell %.1f h, x1.4' % (n, A9_L), n * A9_L * 1.4))
    # go-live initial load: ETL + load items at store size, under N03 (x1.6)
    n = {'low': 1, 'central': 2, 'high': 2}[level]
    per = E(rate('G3m', size)) + E(rate('G4m', size))
    rows.append(('go-live initial load: read-store population, (central) search-index build — %d x (G3m + G4m store %s) %.1f h, x1.6' % (n, size, per), n * per * 1.6))
    return rows


T2 = {'low': 0.06, 'central': 0.08, 'high': 0.11}
G1 = {'low': 1.09, 'central': 1.18, 'high': 1.30}
G2 = {'low': 1.05, 'central': 1.10, 'high': 1.22}

bases = ["# Precomputed bases for the rate agent's targeted steps (you have no access to the leaf tables or the rate table and may not derive quantities of your own)", '',
         'RK60 prices its fills H and C with the estimate\'s own rate table by element class and size, with the method\'s 20%% integration constant along the parent path. The orchestrator has done that arithmetic; the priced amounts below are the bases you apply in RK60\'s order. Each is stated low / central / high (size S / M / L per RK60\'s fill rule; D4 at S; NFR targets at the carried response-time element\'s A9 cell, class L, %.1f h each; integration x1.4 under a top-level subsystem, x1.6 under its matching child node, and along the real path for holes). Apply low with low, central with central, high with high. Unit: net person-hours of work on the task, integration included where stated.' % A9_L, '']
recomp = ['# Run 60 — the orchestrator\'s own application of RK60, made before the diagnostician returned', '',
          'Net task hours. Fills priced by `price_fills60.py` from rate table v0.1-h under RK60 §3\'s fill rules; this file is not given to the diagnostician.', '']
for rep in (1, 2):
    bases.append('## Repeat %d — estimate total %s h' % (rep, format(round(TOTALS[rep]), ',').replace(',', ' ')))
    bases.append('')
    bases.append('| fill (RK60 §3) | low | central | high |')
    bases.append('|---|---:|---:|---:|')
    Hs, Cs = {}, {}
    hrows = {lv: H_fills(rep, lv) for lv in LEVELS}
    crows = {lv: C_fills(lv) for lv in LEVELS}
    for lv in LEVELS:
        Hs[lv] = sum(h for _, h in hrows[lv])
        Cs[lv] = sum(h for _, h in crows[lv])
    # H rows keyed by element (the label without its size and factor), in order of first appearance
    key = lambda lab: re.sub(r' \(.*?\), x[\d.]+', '', lab)
    hkeys, hval = [], {}
    for lv in LEVELS:
        for lab, h in hrows[lv]:
            k = key(lab)
            if k not in hval:
                hkeys.append(k)
                hval[k] = {}
            hval[k][lv] = h
    for k in hkeys:
        bases.append('| H: %s | %s |' % (k, ' | '.join('%.0f' % hval[k][lv] if lv in hval[k] else '—' for lv in LEVELS)))
    bases.append('| **H, hole fills, integration included** | **%.0f** | **%.0f** | **%.0f** |' % tuple(Hs[lv] for lv in LEVELS))
    for i in range(len(crows['low'])):
        lab = re.sub(r' — \d+ fills.*$| — \d+ x .*$', '', crows['central'][i][0])
        bases.append('| C: %s | %.0f | %.0f | %.0f |' % (lab, crows['low'][i][1], crows['central'][i][1], crows['high'][i][1]))
    bases.append('| **C, closure fills, integration included** | **%.0f** | **%.0f** | **%.0f** |' % tuple(Cs[lv] for lv in LEVELS))
    bases.append('| **B_T2 = estimate total + H + C** | **%.0f** | **%.0f** | **%.0f** |' % tuple(TOTALS[rep] + Hs[lv] + Cs[lv] for lv in LEVELS))
    bases.append('')
    # recomputation
    recomp.append('## Repeat %d' % rep)
    recomp.append('')
    recomp.append('| step | low | central | high |')
    recomp.append('|---|---:|---:|---:|')
    recomp.append('| estimate total | %.0f | %.0f | %.0f |' % ((TOTALS[rep],) * 3))
    recomp.append('| + H | %.0f | %.0f | %.0f |' % tuple(Hs[lv] for lv in LEVELS))
    recomp.append('| + C | %.0f | %.0f | %.0f |' % tuple(Cs[lv] for lv in LEVELS))
    bt2 = {lv: TOTALS[rep] + Hs[lv] + Cs[lv] for lv in LEVELS}
    recomp.append('| B_T2 | %.0f | %.0f | %.0f |' % tuple(bt2[lv] for lv in LEVELS))
    t2 = {lv: bt2[lv] * T2[lv] for lv in LEVELS}
    recomp.append('| + T2 (6 / 8 / 11%%) | %.0f | %.0f | %.0f |' % tuple(t2[lv] for lv in LEVELS))
    s3 = {lv: bt2[lv] + t2[lv] for lv in LEVELS}
    recomp.append('| subtotal | %.0f | %.0f | %.0f |' % tuple(s3[lv] for lv in LEVELS))
    s4 = {lv: s3[lv] * G1[lv] for lv in LEVELS}
    recomp.append('| x G1 (1.09 / 1.18 / 1.30) | %.0f | %.0f | %.0f |' % tuple(s4[lv] for lv in LEVELS))
    s5 = {lv: s4[lv] * G2[lv] for lv in LEVELS}
    recomp.append('| **x G2 (1.05 / 1.10 / 1.22) = calibrated** | **%.0f** | **%.0f** | **%.0f** |' % tuple(s5[lv] for lv in LEVELS))
    recomp.append('| ratio to the raw total | x%.2f | x%.2f | x%.2f |' % tuple(s5[lv] / TOTALS[rep] for lv in LEVELS))
    recomp.append('')
    for lv in LEVELS:
        recomp.append('<details><summary>%s, repeat %d: the fills</summary>' % (lv, rep))
        recomp.append('')
        for lab, h in hrows[lv] + crows[lv]:
            recomp.append('- %.1f h — %s' % (h, lab))
        recomp.append('')
        recomp.append('</details>')
        recomp.append('')

bases.append('- C3 layer (the structure\'s 20%% constant, already inside the totals): %s h (r1), %s h (r2); once-scoped layer 840 h both; element-attached layer %s h (r1), %s h (r2).' % tuple(
    format(round(x), ',').replace(',', ' ') for x in (assemble(1)['c3_total'], assemble(2)['c3_total'], assemble(1)['leaf_total'], assemble(2)['leaf_total'])))
bases.append('- The XL leaves\' own element-attached effort, should you need it: repeat 1 2 085.0 h over 13 leaves, repeat 2 601.7 h over 3 leaves (RK60 names this base and leaves it uncorrected).')
open(os.path.join(HERE, 'bases60.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(bases) + '\n')
open(os.path.join(HERE, 'orchestrator_recomputation.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(recomp) + '\n')
print('\n'.join(bases))
print('\n=== recomputation (not given to the sensor) ===')
print('\n'.join(l for l in recomp if l.startswith('|') or l.startswith('## ')))
