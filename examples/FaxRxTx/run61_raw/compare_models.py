#!/usr/bin/env python3
"""Run 61: compare the two product-model repeats as structures (identity by coverage set, M2).
Reads HM61-1.md and HM61-2.md through tools/chain/chainlib.Model. Prints counts and the Jaccard of the
accreted leaves' coverage sets (as sets of distinct coverage sets, and as multisets)."""
import os, sys
from collections import Counter
sys.path.insert(0, r'C:\home\OhmNova\3A8\tools\chain')
from chainlib import Model

here = os.path.dirname(os.path.abspath(__file__))
ms = [Model(os.path.join(here, 'HM61-%d.md' % i)) for i in (1, 2)]
cov = []
for m in ms:
    leaves = m.leaves()
    acc = [frozenset(m.coverage_ids(k)) for k in leaves if m.rows[k]['origin'] == 'accreted']
    der = [k for k in leaves if m.rows[k]['origin'] == 'derived']
    placed = set().union(*acc)
    depth = [m.depth(k) for k in leaves]
    print('%s %s: elements %d · leaves %d (accreted %d, derived %d) · parents %d · root children %d · mean leaf depth %.2f · ids placed %d · derived share %.1f%%'
          % (m.id, m.engine, len(m.order), len(leaves), len(acc), len(der), len(m.parents()), len(m.kids[m.root]),
             sum(depth) / len(depth), len(placed), 100 * len(der) / len(leaves)))
    cov.append(acc)
a, b = cov
sa, sb = set(a), set(b)
print('distinct coverage sets: %d / %d · shared %d · Jaccard %.3f' % (len(sa), len(sb), len(sa & sb), len(sa & sb) / len(sa | sb)))
ca, cb = Counter(a), Counter(b)
inter, union = sum((ca & cb).values()), sum((ca | cb).values())
print('multiset of accreted leaves: shared %d of union %d · Jaccard %.3f' % (inter, union, inter / union))
print('leaf-count ratio x%.3f · element-count ratio x%.3f' % (len(ms[1].leaves()) / len(ms[0].leaves()), len(ms[1].order) / len(ms[0].order)))
