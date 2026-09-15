"""Run 59 - SAS whole-model assembly on the 2.1 chain. The only thing in the chain that multiplies anything.

Inputs, all pinned before this script was written:
  product model    run57_raw/HM57-1.md section 6 (Hotyn-M 2.1, 211 rows, 187 leaves, 24 nodes; fenced TSV)
  work model       run58_raw/work_model.tsv, classes.tsv  (Hotyn-W 1.2, seven partial crossings)
  size classes     run59_raw/HD59-[A-G][12].md  (Hotyn-D 2.0, two repeats x seven batches)
  rates            docs/rate_table.md v0.1-h   (net person-hours; first row per (activity, class, size) wins
                   where the table repeats an activity under a second, undeclared technology)
  declaration      technology_declaration.md: environments 4 (dev S, test M, stage M, prod L),
                   test cycles 2, UAT cycles 2, migration rehearsal cycles 2

Conventions, identical to run 47 (run47_raw/assemble_sas.py), BMS and FaxRxTx:
  subtree = rooted (element + descendants)
  C3 base = leaf-item E of the rooted subtree, element-attached items only; once-scoped and per-environment
            items enter no C3 base; rate 20%, never compounding
  E(O,M,P) = (O + 4M + P) / 6
  per-parent / once / per-environment classes are tree arithmetic (catalogue 1.4 section 3a), computed here
  an element the sensors could not size is a named hole: its per-element items are listed, not priced
The two repeats are priced as two variants. Their ratio is the measurement.
Usage: python examples/SAS/run59_raw/assemble_sas58.py
"""
import csv
import os
import re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.abspath(os.path.join(HERE, '..'))
ROOT = os.path.abspath(os.path.join(CASE, '..', '..'))
BATCHES = 'ABCDEFG'
C3_RATE = 0.20
SIZES = ('S', 'M', 'L', 'XL')
ROOT_ID = 'N01'
REQ = re.compile(r'\b(?:I|G|P|L|D|NFR)-\d+(?:\.\d+)?\b')


def E(cell):
    o, m, p = cell
    return (o + 4 * m + p) / 6.0


def band(n, cuts):
    """cuts = (S_max, M_max, L_max); n above L_max is XL."""
    return 'S' if n <= cuts[0] else 'M' if n <= cuts[1] else 'L' if n <= cuts[2] else 'XL'


# ---------------------------------------------------------------- rate table
RATES = {}   # (activity, classkey, size) -> (O, M, P); first occurrence wins
for line in open(os.path.join(ROOT, 'docs', 'rate_table.md'), encoding='utf-8'):
    if not line.startswith('| '):
        continue
    c = [x.strip() for x in line.strip().strip('|').split('|')]
    if len(c) < 6 or not re.fullmatch(r'[A-Z]\d{1,2}[a-z]?d?', c[0]):
        continue
    try:
        cell = (float(c[3]), float(c[4]), float(c[5]))
    except ValueError:
        continue
    act, cls, sz = c[0], c[1], c[2]
    m = re.match(r'(?:\w+ = )?(S|M|L|XL)\b', sz)
    size = m.group(1) if m else sz
    if act == 'E1' and '=' in sz:
        size = sz.split('=')[1].strip()
    RATES.setdefault((act, cls, size), cell)
    RATES.setdefault((act, '*', size), cell)   # activities with one class row


def rate(act, size, cls='*'):
    if (act, cls, size) in RATES:
        return RATES[(act, cls, size)]
    if (act, '*', size) in RATES:
        return RATES[(act, '*', size)]
    return None


K1CLS = {'interface': 'interface'}
K2CLS = {'interface': 'interface', 'store': 'store'}


def cell_for(act, elcls, size, kind=None):
    if act == 'K1':
        return rate('K1', size, K1CLS.get(elcls, 'behaviour, surface, store'))
    if act == 'K2':
        return rate('K2', size, K2CLS.get(elcls, 'behaviour, surface'))
    if act == 'K3':
        return rate('K3', size, 'statement-' + (kind or 'compliance'))
    return rate(act, size)


# ---------------------------------------------------------------- product model (2.x TSV)
txt = open(os.path.join(CASE, 'run57_raw', 'HM57-1.md'), encoding='utf-8').read()
sec6 = txt[txt.index('\n## 6. '):txt.index('\n## 7. ')]
blk = sec6[sec6.index('```tsv') + 6:sec6.rindex('```')]
lines = [l for l in blk.strip('\n').split('\n') if l.strip()]
assert lines[0].split('\t') == ['id', 'parent', 'origin', 'coverage', 'name']
PARENT, COV, ORDER, NAME = {}, {}, [], {}
for l in lines[1:]:
    c = l.split('\t')
    PARENT[c[0]] = c[1]
    NAME[c[0]] = c[4]
    COV[c[0]] = len(REQ.findall(c[3]))
    ORDER.append(c[0])
KIDS = defaultdict(list)
for k, p in PARENT.items():
    if p in PARENT:
        KIDS[p].append(k)


def sub(e):
    out = [e]
    for c in KIDS.get(e, []):
        out += sub(c)
    return out


# ---------------------------------------------------------------- work model
CLS = {}
for row in csv.DictReader(open(os.path.join(CASE, 'run58_raw', 'classes.tsv'), encoding='utf-8'), delimiter='\t'):
    CLS[row['element']] = row['class']
CLS[ROOT_ID] = 'aggregate'
ITEMS = []   # (activity, element)
for row in csv.DictReader(open(os.path.join(CASE, 'run58_raw', 'work_model.tsv'), encoding='utf-8'), delimiter='\t'):
    ITEMS.append((row['activity'], row['element']))
# the root's per-parent items, outside every batch: same set as any surface-bearing parent (run 47 convention)
ITEMS += [('A5', ROOT_ID)] * 2 + [('A6', ROOT_ID)] * 2 + [('A7', ROOT_ID), ('A8', ROOT_ID), ('D2', ROOT_ID),
                                                          ('U1', ROOT_ID), ('O1', ROOT_ID)] + [('U2', ROOT_ID)] * 2 + [('U3', ROOT_ID)] * 2

PER_PARENT = {'A5', 'A6', 'A7', 'A8', 'D2', 'U1', 'U2', 'U3', 'O1'}
SPECIAL_MIG = {'G2m', 'G3m', 'G4m'}

# ---------------------------------------------------------------- size classes from the fourteen readings
ID = re.compile(r'\b(?:A\d{3}|C\d{2})\b')          # leaves of the 2.x model
SIZE_TOKEN = re.compile(r'\*\*(S|M|L|XL)\*\*')


def section(t, n):
    m = re.search(r'^#+ *%s\. .*$' % n, t, re.M)
    if not m:
        return ''
    rest = t[m.end():]
    m2 = re.search(r'^#+ *%d\. ' % (n + 1), rest, re.M)
    return rest[:m2.start()] if m2 else rest


def parse_reading(fn):
    t = open(fn, encoding='utf-8').read()
    sizes, kinds, special = {}, {}, {}
    for line in section(t, 2).split('\n'):
        if not line.startswith('| '):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        eid = re.sub(r'[*`]', '', c[0]).strip()
        if len(c) < 5 or not ID.fullmatch(eid):
            continue
        m = SIZE_TOKEN.search(c[-1]) or SIZE_TOKEN.search(' '.join(c[1:]))
        sizes[eid] = m.group(1) if m else None
        km = re.search(r'statement[^|]*?(compliance|behavioural)', ' '.join(c[1:]))   # the kind, only on a statement's class cell
        if km:
            kinds[eid] = km.group(1)
    s3 = section(t, 3)
    ANCHOR = re.compile(r'^[\s|*\-]*((?:A\d{3}|C\d{2}))(?!\d)', re.M)
    hits = [(m.start(), m.group(1)) for m in ANCHOR.finditer(s3)]
    for i, (pos, eid) in enumerate(hits):
        end = hits[i + 1][0] if i + 1 < len(hits) else len(s3)
        chunk = s3[pos:end]
        m = (re.search(r'(?:→|->)\s*\**\s*(S|M|L|XL)\b', chunk)
             or re.search(r'\|\s*\d+\s*\|\s*\*\*(S|M|L|XL)\*\*', chunk)            # | 3 | **M** |
             or re.search(r'\|\s*\d+\s*\|\s*(S|M|L|XL)\s*\|', chunk)                # | 5 | L |      (run 59 A2)
             or re.search(r'class\s*\*\*(S|M|L|XL)\*\*', chunk)
             or re.search(r'[Cc]ount and class:\*\*\s*\d+,\s*\*\*(S|M|L|XL)\*\*', chunk)   # bullet form (run 59 G1)
             or re.search(r'·\s*\d+ kinds?\s*·\s*\*\*(S|M|L|XL)\*\*', chunk))
        if m:
            special.setdefault(eid, m.group(1))
        elif re.search(r'unsizeable|none assigned|not assigned|not countable|not determinable|no special[- ]count|no count'
                       r'|nothing can be enumerated|\*\*none\*\*|\|\s*none\s*\||\bno class\b|\bno band\b|below the S threshold'
                       r'|\|\s*0(?: evidenced| kinds)?\s*\||\|\s*—\s*\|\s*—\s*\|', chunk, re.I):
            special.setdefault(eid, None)     # the sensor enumerated nothing that reaches the lowest rung: a named hole
    return sizes, kinds, special


READINGS = {1: ({}, {}, {}), 2: ({}, {}, {})}
for b in BATCHES:
    for r in (1, 2):
        fn = os.path.join(HERE, f'HD59-{b}{r}.md')
        if not os.path.exists(fn):
            print('!! missing', fn)
            continue
        s, k, sp = parse_reading(fn)
        READINGS[r][0].update(s)
        READINGS[r][1].update(k)
        READINGS[r][2].update(sp)


def assemble(rep):
    sizes, kinds, special = READINGS[rep]
    leafE = defaultdict(float)
    byact = defaultdict(float)
    sds = []
    holes = []
    for act, el in ITEMS:
        cls = CLS.get(el, '?')
        if act in PER_PARENT:
            st = sub(el)
            leaves = [x for x in st if x not in KIDS]
            if act == 'A8':
                n = sum(1 for x in st if CLS.get(x) in ('store', 'interface'))
                size = band(n, (1, 3, 6))
            elif act in ('U1', 'U2', 'U3', 'O1'):
                n = sum(1 for x in st if CLS.get(x) == 'surface')
                if n == 0:
                    holes.append((el, act, 'no surface in subtree (crosser filter should have refused)'))
                    continue
                size = band(n, (1, 3, 6))
            else:
                size = band(len(leaves), (3, 8, 14))
            cell = cell_for(act, cls, size)
        elif act == 'D4':
            size = band(COV.get(el, 0), (1, 3, 6))
            cell = cell_for(act, cls, size)
        elif act == 'A9' or act in SPECIAL_MIG:
            size = special.get(el, 'MISSING')
            if size in (None, 'MISSING'):
                holes.append((el, act, 'special count unsizeable' if size is None else 'special count not found in reading'))
                continue
            cell = cell_for(act, cls, size)
        else:
            size = sizes.get(el, 'MISSING')
            if size in (None, 'MISSING'):
                holes.append((el, act, 'unsizeable (M10)' if size is None else 'no size in reading'))
                continue
            cell = cell_for(act, cls, size, kinds.get(el))
        if cell is None:
            holes.append((el, act, f'no rate cell for class {cls} size {size}'))
            continue
        leafE[el] += E(cell)
        byact[act] += E(cell)
        sds.append((cell[2] - cell[0]) / 6.0)
    parents = [e for e in ORDER if e in KIDS]
    c3 = {p: C3_RATE * sum(leafE.get(x, 0.0) for x in sub(p)) for p in parents}
    n_model = len(ORDER)                     # 211 -> bracket L
    bracket = band(n_model, (30, 90, 10**9))
    n_si = sum(1 for e in ORDER if CLS.get(e) in ('surface', 'interface'))
    once = [
        ('A1 test strategy [bracket]', rate('A1', bracket)),
        ('U4 acceptance record [bracket]', rate('U4', bracket)),
        ('D1 mobilisation [bracket]', rate('D1', bracket)),
        ('D3 status reporting [bracket]', rate('D3', bracket)),
        ('D6 risk & dependency [bracket]', rate('D6', bracket)),
        ('E2 build/deploy pipeline [bracket]', rate('E2', bracket)),
        ('E3 promotion procedure [4 envs: L]', rate('E3', 'L')),
        ('E4 configuration management [bracket]', rate('E4', bracket)),
        ('E6 production cutover [bracket]', rate('E6', bracket)),
        ('E7 hosting set-up [bracket]', rate('E7', bracket)),
        ('G1m source profiling [bracket]', rate('G1m', bracket)),
        ('G5m migration rehearsal #1 [bracket]', rate('G5m', bracket)),
        ('G5m migration rehearsal #2 [bracket]', rate('G5m', bracket)),
        ('O2 operational runbook [bracket]', rate('O2', bracket)),
        ('O3 support handover pack [bracket]', rate('O3', bracket)),
        ('O4 release notes [single]', rate('O4', 'single')),
        ('S1 security design review [bracket]', rate('S1', bracket)),
        (f'S2 penetration test [{n_si} surf+int: {band(n_si, (5, 12, 25))}]', rate('S2', band(n_si, (5, 12, 25)))),
        (f'S3 remediation [{n_si} surf+int: {band(n_si, (5, 12, 25))}]', rate('S3', band(n_si, (5, 12, 25)))),
        ('E1 environment: dev [S]', rate('E1', 'S')),
        ('E1 environment: test [M, declared]', rate('E1', 'M')),
        ('E1 environment: stage [M]', rate('E1', 'M')),
        ('E1 environment: prod [L]', rate('E1', 'L')),
    ]
    for lab, cell in once:
        assert cell is not None, lab
    once_total = sum(E(c) for _, c in once)
    tl, tc3 = sum(leafE.values()), sum(c3.values())
    once_sd = [(c[2] - c[0]) / 6.0 for _, c in once]
    rho = 0.5
    var_el = (1 - rho) * sum(x * x for x in sds) + rho * sum(sds) ** 2
    var_once = (1 - rho) * sum(x * x for x in once_sd) + rho * sum(once_sd) ** 2
    sd_total = (var_el ** 0.5) * (1 + tc3 / tl) + var_once ** 0.5
    return dict(sd=sd_total, p10=tl + tc3 + once_total - 1.2816 * sd_total, p90=tl + tc3 + once_total + 1.2816 * sd_total,
                leafE=leafE, c3=c3, once=once, once_total=once_total, holes=holes, byact=byact,
                leaf_total=tl, c3_total=tc3, total=tl + tc3 + once_total, bracket=bracket, n_si=n_si)


if __name__ == '__main__':
    res = {}
    for rep in (1, 2):
        sizes, kinds, special = READINGS[rep]
        dist = defaultdict(int)
        for e, s in sizes.items():
            dist[s or 'unsizeable'] += 1
        print(f'=== repeat {rep}: sized elements {len(sizes)} · distribution {dict(dist)} · statement kinds {len(kinds)} · special counts {len(special)}')
        a = assemble(rep)
        res[rep] = a
        print('  element leaf E (incl. root per-parent items): %.1f h' % a['leaf_total'])
        print('  C3 all parents:                               %.1f h   of which root C3: %.1f' % (a['c3_total'], a['c3'][ROOT_ID]))
        print('  once + per-environment layer [%s]:            %.1f h' % (a['bracket'], a['once_total']))
        print('  GRAND TOTAL:                                  %.0f net person-hours  (= %.1f pd at 8 h)' % (a['total'], a['total'] / 8))
        print('  corridor, rho = 0.5:  sd %.0f h · P10 %.0f · P90 %.0f  (x%.2f / x%.2f of the centre)' % (a['sd'], a['p10'], a['p90'], a['p10'] / a['total'], a['p90'] / a['total']))
        print('  named holes (%d):' % len(a['holes']))
        for h in a['holes']:
            print('     ', h)
    a = res[1]
    print('=== composition, repeat 1 - per top-level subtree: element items + C3 inside the subtree')
    for top in KIDS[ROOT_ID]:
        st = sub(top)
        el = sum(a['leafE'].get(x, 0.0) for x in st)
        c3 = sum(a['c3'].get(x, 0.0) for x in st if x in a['c3'])
        print('   %-6s %-40s elements %3d  items %6.0f h  C3 %6.0f h  subtotal %6.0f h' % (top, NAME.get(top, '')[:40], len(st), el, c3, el + c3))
    print('   root own per-parent items %.0f h · root C3 %.0f h · once/per-env %.0f h' % (a['leafE'].get(ROOT_ID, 0.0), a['c3'][ROOT_ID], a['once_total']))
    print('=== composition, repeat 1 - per activity (element-attached items only, hours)')
    for act, v in sorted(a['byact'].items(), key=lambda kv: -kv[1]):
        print('   %-4s %7.0f' % (act, v))
    print('=== once/per-environment items, repeat 1:')
    for lab, cell in a['once']:
        print('   %-48s E = %5.1f' % (lab, E(cell)))
    s1, k1, sp1 = READINGS[1]
    s2, k2, sp2 = READINGS[2]
    common = [e for e in s1 if e in s2]
    diff = [(e, s1[e], s2[e]) for e in common if s1[e] != s2[e]]
    print('=== size-class agreement: %d elements in both, %d differ (%.1f%% agree)' % (len(common), len(diff), 100 * (1 - len(diff) / max(1, len(common)))))
    for d in diff:
        print('     ', d)
    kd = [(e, k1.get(e), k2.get(e)) for e in set(k1) | set(k2) if k1.get(e) != k2.get(e)]
    print('=== statement-kind divergences:', kd)
    spd = [(e, sp1.get(e, '-'), sp2.get(e, '-')) for e in set(sp1) | set(sp2) if sp1.get(e, '-') != sp2.get(e, '-')]
    print('=== special-count divergences:', spd)
    xl = sorted(set(e for e, v in s1.items() if v == 'XL') | set(e for e, v in s2.items() if v == 'XL'))
    print('=== XL elements (either repeat):', xl)
    lo, hi = min(r['total'] for r in res.values()), max(r['total'] for r in res.values())
    print('=== repeat spread: %.0f .. %.0f net person-hours (x%.4f); centre %.0f h' % (lo, hi, hi / lo, (lo + hi) / 2))
    depth = [len([p for p in ORDER if p in KIDS and e in sub(p)]) for e in ORDER if e not in KIDS]
    print('=== tree: %d elements, %d leaves, %d parents; mean leaf depth %.2f (run 47 on HM44-OA1: 2.6)' % (len(ORDER), len(depth), len(KIDS), sum(depth) / len(depth)))
    print('=== unit: net hours of work on the task (docs/instrument.md section 0). Leave, holidays, sickness and')
    print('===       presence are NOT included; the comparison-layer conversion is docs/constants.md section 4a.')
