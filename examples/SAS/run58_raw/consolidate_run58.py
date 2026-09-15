"""Run 58 - consolidate the seven partial crossings of HM57-1 into one work model.
Same role as run45_raw/consolidate_run45.py, with the element-id pattern of the 2.x model (N02, CN01, A001, C01) and
a wider reader for the compacted section 4: the seven sensors compacted differently (named groups such as `L27`,
`Leaves31`, `Parents6`, "the 14 build leaves", "build set (24)"; `except` clauses; cycle suffixes `·c1`, `/c1`,
`#c1`, "(c1, c2 each)"; parenthesised justifications). Every row's parsed count is checked against the count the
sensor printed; a mismatch is printed, never silently accepted. Parses section 3 (classification log), section 4
(the crossing) and section 5 (refusals, filter / judgement). Writes work_model.tsv (one row per work item, cycles
expanded) and classes.tsv (one row per element), and prints the readings quoted in run58_work_model.md.
Usage: python examples/SAS/run58_raw/consolidate_run58.py"""
import os
import re
import sys
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.abspath(os.path.join(HERE, '..'))
BATCHES = {'A': ['N02'], 'B': ['N06', 'N07', 'N10'], 'C': ['N08', 'N09'], 'D': ['N11', 'N12'],
           'E': ['N13'], 'F': ['N19', 'N20'], 'G': ['N21', 'N22']}
CYCLED = {'A5': 2, 'A6': 2, 'U2': 2, 'U3': 2}     # declaration parameters: test cycles 2, UAT cycles 2
ELEMENT = re.compile(r'\b(?:CN\d{2}|N\d{2}|A\d{3}|C\d{2})\b')
ACT = re.compile(r'^\*{0,2}([A-Z]\d{1,2}m?)\*{0,2}\b')
CLASSES = {'aggregate', 'behaviour', 'surface', 'interface', 'store', 'statement'}
BUILD = {'behaviour', 'surface', 'interface', 'store'}

# --- the product model, for the batch scopes (leaves and nodes per batch)
txt = open(os.path.join(CASE, 'run57_raw', 'HM57-1.md'), encoding='utf-8').read()
sec6 = txt[txt.index('\n## 6. '):txt.index('\n## 7. ')]
blk = sec6[sec6.index('```tsv') + 6:sec6.rindex('```')]
lines = [l for l in blk.strip('\n').split('\n') if l.strip()]
PARENT = {}
ORDER = []
for l in lines[1:]:
    c = l.split('\t')
    PARENT[c[0]] = c[1]
    ORDER.append(c[0])
KIDS = {}
for k, p in PARENT.items():
    KIDS.setdefault(p, []).append(k)


def subtree(k):
    out = [k]
    for c in KIDS.get(k, []):
        out += subtree(c)
    return out


def section(t, n):
    """Text of markdown section '## n.' up to the next '## '."""
    m = re.search(r'^#{2,3} *%s\. .*$' % re.escape(str(n)), t, re.M)
    if not m:
        return ''
    rest = t[m.end():]
    m2 = re.search(r'^#{2,3} ', rest, re.M)
    return rest[:m2.start()] if m2 else rest


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def strip_md(s):
    return re.sub(r'[*`]', '', s).strip()


classes = OrderedDict()   # element -> class
items = []                # (batch, activity, element, cycle)
judgements = []           # (batch, element, activity, reason)
filters = []
batch_totals = {}
mismatches = 0
for b, roots in BATCHES.items():
    fn = os.path.join(HERE, f'HW58-{b}1.md')
    if not os.path.exists(fn):
        print(f'!! missing {fn}', file=sys.stderr)
        continue
    scope = []
    for r in roots:
        scope += subtree(r)
    scope_leaves = [e for e in scope if e not in KIDS]
    scope_nodes = [e for e in scope if e in KIDS]
    t = open(fn, encoding='utf-8').read()
    # --- section 3: classification
    for line in section(t, 3).split('\n'):
        if not line.startswith('| '):
            continue
        c = cells(line)
        eid = strip_md(c[0])
        if len(c) < 3 or not ELEMENT.fullmatch(eid):
            continue
        found = [strip_md(x).lower() for x in c[1:] if strip_md(x).lower() in CLASSES]
        if not found:
            print(f'!! batch {b}: unparsed class for {eid}: {c[1:]!r}', file=sys.stderr)
            continue
        if eid in classes:
            print(f'!! duplicate element {eid} in batch {b}', file=sys.stderr)
        classes[eid] = found[0]
    build_leaves = [e for e in scope_leaves if classes.get(e) in BUILD]
    # --- section 4: named groups defined before (or after) the table
    s4 = section(t, 4)
    groups = {}
    for line in s4.split('\n'):
        if line.startswith('|'):
            continue
        ids = ELEMENT.findall(line)
        if len(ids) < 3:
            continue
        keys = re.findall(r'"([^"]+)"', line)                  # "build set", "The 14 build leaves"
        keys += re.findall(r'\*\*([^*]+)\*\*\s*=', line)         # **Leaves31** =
        keys += re.findall(r'^\s*-?\s*\**(\w+)\**\s*(?:=|below means)', line)   # L27 below means
        for k in keys:
            groups[k.strip().lower()] = ids
    # --- section 4: the table
    k1 = None
    prev = []
    declared = 0
    for line in s4.split('\n'):
        if not line.startswith('| '):
            continue
        c = cells(line)
        if len(c) < 4:
            continue
        head = strip_md(c[0])
        m = ACT.match(head)
        if not m:
            continue
        act = m.group(1)
        if ',' in head.split(' ')[0] or '/' in head.split(' ')[0]:
            continue  # grouped deferred rows like "E2, E3, E4, E6, E7"
        target = strip_md(c[2])
        low = target.lower()
        if 'deferred' in low or low.startswith('none') or low.startswith('(none') or low in ('—', '-', ''):
            elems = []
        else:
            excluded = []
            if ' except ' in low:
                left, right = re.split(r'\s+except\s+', target, maxsplit=1, flags=re.I)
                excluded = ELEMENT.findall(right)
                target, low = left, left.lower()
            core = re.sub(r'\([^)]*\)', ' ', target)           # drop justifications like "(A016)", "(c1, c2 each)"
            found = ELEMENT.findall(core)
            if found:
                elems = list(OrderedDict.fromkeys(found))
            else:
                elems = None
                for key, ids in groups.items():
                    if key in low:
                        elems = list(ids)
                        break
                if elems is None:
                    if 'same' in low and ('k1' in low or 'leaves' in low or 'leaf' in low):
                        elems = list(k1 or [])      # "same 23 as K1", "same 28 leaves": the K1 list is the leaf list
                    elif 'same' in low:
                        elems = list(prev)
                    elif 'build' in low:
                        elems = list(build_leaves)
                    elif 'leaves' in low or 'leaf' in low:
                        elems = list(scope_leaves)
                    elif 'parent' in low:
                        elems = list(scope_nodes)
                    else:
                        print(f'!! batch {b} {act}: cannot read target {target!r}', file=sys.stderr)
                        elems = []
            elems = [e for e in elems if e not in excluded]
        if act == 'K1':
            k1 = elems
        if elems:
            prev = elems
        try:
            cnt = int(strip_md(c[3]))
        except ValueError:
            cnt = None
        mult = CYCLED.get(act, 1)
        if cnt is not None and cnt != len(elems) * mult:
            print(f'!! batch {b} {act}: table count {cnt} vs parsed {len(elems)}x{mult}  ({target[:60]!r})', file=sys.stderr)
            mismatches += 1
        for e in elems:
            if e not in scope:
                print(f'!! batch {b} {act}: element {e} outside the batch scope', file=sys.stderr)
            for cyc in range(1, mult + 1):
                items.append((b, act, e, cyc))
        if cnt:
            declared += cnt
    total_line = re.search(r'\*\*\s*Total[^*]*?(\d+)\s*items?[^*]*\*\*|\*\*\s*Total:\s*(\d+)|\*\*total\*\*\s*\|\s*\|\s*\|\s*\*\*(\d+)\*\*', s4, re.I)
    printed = next((int(g) for g in (total_line.groups() if total_line else ()) if g), None)
    batch_totals[b] = (printed, declared, sum(1 for i in items if i[0] == b))
    # --- section 5: refusals
    for line in section(t, 5).split('\n'):
        if not line.startswith('| '):
            continue
        c = cells(line)
        if not ELEMENT.search(strip_md(c[0])):
            continue
        low = ' '.join(c).lower()
        if 'judgement' in low or 'judgment' in low:
            judgements.append((b, strip_md(c[0]), strip_md(c[1]), strip_md(c[-1])[:90]))
        elif 'filter' in low:
            filters.append((b, strip_md(c[0]), strip_md(c[1])))

# --- write
with open(os.path.join(HERE, 'classes.tsv'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('element\tclass\n')
    for e in ORDER:
        if e in classes:
            f.write(f'{e}\t{classes[e]}\n')
with open(os.path.join(HERE, 'work_model.tsv'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('batch\tactivity\telement\tcycle\tclass\n')
    for b, a, e, cyc in items:
        f.write(f'{b}\t{a}\t{e}\t{cyc}\t{classes.get(e, "?")}\n')

# --- readings
print('elements classified:', len(classes), dict(Counter(classes.values())))
print('leaves classed aggregate:', [e for e, c in classes.items() if c == 'aggregate' and e not in KIDS])
print('nodes not classed aggregate:', [e for e, c in classes.items() if c != 'aggregate' and e in KIDS])
print('batch totals (printed, sum of rows, parsed):', batch_totals)
print('row-count mismatches:', mismatches)
print('crossing items total:', len(items))
by_act = Counter(a for _, a, _, _ in items)
print('items by activity:', dict(sorted(by_act.items())))
per_el = Counter(e for _, _, e, _ in items)
untouched = [e for e in classes if e not in per_el]
print('elements untouched:', untouched)
print('elements crossed: %d · items per crossed element: %.2f' % (len(per_el), len(items) / max(1, len(per_el))))
print('refusals: filter %d · judgement %d' % (len(filters), len(judgements)))
print('filters by activity:', dict(sorted(Counter(a for _, _, a in filters).items())))
for j in judgements:
    print('   judgement', j)
