# SAS - the calibrated centre (57 600 net task hours, run 48) laid over the author's phase table.
# Every allocation rule is declared here; nothing is re-estimated. Run: python examples/SAS/phase_breakdown.py
import sys, os
from collections import defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'run47_raw'))
import assemble_sas as a

# ------------------------------------------------------------ price every item again, keeping (activity, element, E)
sizes, kinds, special = a.READINGS[1]          # repeat 1 (38 069 h); repeat 2 differs by 0.26 %
priced = []
for act, el in a.ITEMS:
    cls = a.CLS.get(el, '?')
    if act in a.PER_PARENT:
        st = a.sub(el); leaves = [x for x in st if x not in a.KIDS]
        if act == 'A8':
            size = a.band(sum(1 for x in st if a.CLS.get(x) in ('store', 'interface')), (1, 3, 6))
        elif act in ('U1', 'U2', 'U3', 'O1'):
            n = sum(1 for x in st if a.CLS.get(x) == 'surface')
            if n == 0:
                continue
            size = a.band(n, (1, 3, 6))
        else:
            size = a.band(len(leaves), (3, 8, 14))
        cell = a.cell_for(act, cls, size)
    elif act == 'D4':
        cell = a.cell_for(act, cls, a.band(a.COV.get(el, 0), (1, 3, 6)))
    elif act == 'A9' or act in a.SPECIAL_MIG:
        size = special.get(el, 'MISSING')
        if size in (None, 'MISSING'):
            continue
        cell = a.cell_for(act, cls, size)
    else:
        size = sizes.get(el, 'MISSING')
        if size in (None, 'MISSING'):
            continue
        cell = a.cell_for(act, cls, size, kinds.get(el))
    if cell is None:
        continue
    priced.append((act, el, a.E(cell)))


def top(el):                                   # the top-level subtree an element sits under
    if el == a.ROOT_ID:
        return 'root'
    while a.PARENT.get(el) in a.PARENT and a.PARENT.get(el) != a.ROOT_ID:
        el = a.PARENT[el]
    return el


# ------------------------------------------------------------ declared rules
BUCKET = {'S-01': 'platform', 'S-02': 'platform', 'S-03': 'platform', 'S-13': 'platform', 'S-14': 'platform',
          'S-05': 'product', 'S-06': 'location', 'S-08': 'data access',
          'S-04': 'cross-cutting', 'S-07': 'cross-cutting', 'S-09': 'cross-cutting', 'S-10': 'cross-cutting',
          'S-11': 'cross-cutting', 'S-12': 'cross-cutting', 'root': 'root'}
PHASE0_ACTS = {'D4'}                           # requirement elaboration: all of it is discovery/design
PHASE0_HALF = {'K1'}                           # element design: half before build, half during
PHASE3_ACTS = {'G2m', 'G3m', 'G4m', 'A9', 'U2', 'U3', 'U4', 'O1', 'O2', 'O3', 'O4'}   # migration, UAT, docs, perf test
CROSS_SPLIT = (0.6, 0.4)                       # cross-cutting mechanisms: 60 % built in phase 1, 40 % in phase 2
PLATFORM_P0 = 0.5                              # S-01 platform foundation: half is phase 0 (walking skeleton, envs, pipeline)

ph = defaultdict(float)          # (phase, bucket) -> hours, element items only
for act, el, e in priced:
    b = BUCKET[top(el)]
    if act in PHASE0_ACTS:
        ph[('P0', b)] += e
        continue
    if act in PHASE0_HALF:
        ph[('P0', b)] += e / 2
        e /= 2
    if act in PHASE3_ACTS:
        ph[('P3', b)] += e
        continue
    if b == 'platform' and top(el) == 'S-01':
        ph[('P0', b)] += e * PLATFORM_P0
        ph[('P1', b)] += e * (1 - PLATFORM_P0)
        continue
    if b in ('platform', 'product', 'root'):
        ph[('P1', b)] += e
    elif b in ('location', 'data access'):
        ph[('P2', b)] += e
    else:
        ph[('P1', b)] += e * CROSS_SPLIT[0]
        ph[('P2', b)] += e * CROSS_SPLIT[1]

# C3 (20 % at every parent incl. the root) follows the items it sits on: scale every cell by the run's C3 ratio
tot_items = sum(v for v in ph.values())
r = a.assemble(1)
c3_ratio = sum(r['c3'].values()) / tot_items
for k in list(ph):
    ph[k] *= (1 + c3_ratio)

# once-scoped layer, by name
ONCE_PHASE = {'A1': 'P0', 'D1': 'P0', 'E2': 'P0', 'E4': 'P0', 'E7': 'P0', 'G1m': 'P0', 'S1': 'P0',
              'E1 environment: dev': 'P0', 'E1 environment: test': 'P0',
              'D3': 'P1', 'D6': 'P1', 'E3': 'P2', 'E1 environment: stage': 'P2',
              'U4': 'P3', 'E6': 'P3', 'G5m': 'P3', 'O2': 'P3', 'O3': 'P3', 'O4': 'P3', 'S2': 'P3', 'S3': 'P3',
              'E1 environment: prod': 'P3'}
for name, cell in r['once']:
    key = next(k for k in sorted(ONCE_PHASE, key=len, reverse=True) if name.startswith(k))
    ph[(ONCE_PHASE[key], 'once')] += a.E(cell)

raw = sum(ph.values())
# ------------------------------------------------------------ the Step C chain (run 48), repeat 1, central
T = 24163.5 * (0.025 + 0.09) + 593.0 * 0.30          # T1 + T2 + T3 increments
T *= 1.20                                               # the structure's 20 % on the increments
ADD = {'P3': 320 + 160 + 200 + 130 + 160}               # A-1..A-5: load test, failover/DR, WCAG, browsers, help content
G = 1.15 * 1.18
build = sum(v for (p, b), v in ph.items() if p in ('P1', 'P2'))
for (p, b) in list(ph):
    if p in ('P1', 'P2'):
        ph[(p, b)] += T * ph[(p, b)] / build      # holes and closure gaps sit in the build phases
for p, v in ADD.items():
    ph[(p, 'once')] += v
for k in list(ph):
    ph[k] *= G
cal = sum(ph.values())

# ------------------------------------------------------------ print
H8, H6, LEAVE, DAYS = 8.0, 6.0, 1.10, 21


def fmt(h):
    return "%8.0f h  %7.0f pd@8  %7.0f present d@6  %6.1f staffed pm" % (h, h / H8, h / H6, h / H6 / DAYS * LEAVE)


print("raw chain (repeat 1)   " + fmt(raw))
print("calibrated centre      " + fmt(cal) + "   (x%.3f)\n" % (cal / raw))
PH = {'P0': 'Phase 0 Discovery, Design & Foundation (M1-3)', 'P1': 'Phase 1 Platform + Product (M3-8)',
      'P2': 'Phase 2 Location + Data Access (M7-11)', 'P3': 'Phase 3 Implementation (M11-14)'}
MONTHS = {'P0': 3, 'P1': 5, 'P2': 4, 'P3': 3}
for p, label in PH.items():
    h = sum(v for (pp, b), v in ph.items() if pp == p)
    print("%-48s %s   share %4.1f %%   avg heads over %d mo: %4.1f" % (label, fmt(h), 100 * h / cal, MONTHS[p], h / H6 / DAYS * LEAVE / MONTHS[p]))
print("%-48s %s\n" % ('delivery subtotal', fmt(cal)))
print("inside phases 1-2, calibrated, by bucket:")
for b in ('platform', 'product', 'location', 'data access', 'cross-cutting', 'root', 'once'):
    h = sum(v for (p, bb), v in ph.items() if bb == b and p in ('P1', 'P2'))
    print("   %-14s %s" % (b, fmt(h)))
prod = sum(v for (p, bb), v in ph.items() if bb == 'product' and p in ('P1', 'P2'))
loc = sum(v for (p, bb), v in ph.items() if bb == 'location' and p in ('P1', 'P2'))
print("   location = %.0f %% of product (module subtrees S-06 vs S-05; the shared record core S-03 sits in platform)" % (100 * loc / prod))
print("\nphase 0 by bucket:")
for b in ('platform', 'product', 'location', 'data access', 'cross-cutting', 'root', 'once'):
    h = ph.get(('P0', b), 0)
    if h:
        print("   %-14s %s" % (b, fmt(h)))
print("\nphase 3 by bucket:")
for b in ('platform', 'product', 'location', 'data access', 'cross-cutting', 'root', 'once'):
    h = ph.get(('P3', b), 0)
    if h:
        print("   %-14s %s" % (b, fmt(h)))
