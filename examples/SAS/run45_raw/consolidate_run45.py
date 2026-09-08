"""Run 45 - consolidate the seven partial crossings of HM44-OA1 into one work model.
Parses each HW45-*.md: section 3 (classification log) and section 4 (the compacted crossing), plus the
judgement refusals of section 5. Writes work_model.tsv (one row per work item, cycles expanded) and
classes.tsv (one row per element), and prints the readings quoted in run45_work_model.md.
Usage: python examples/SAS/run45_raw/consolidate_run45.py"""
import os
import re
import sys
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
BATCHES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
CYCLED = {'A5': 2, 'A6': 2, 'U2': 2, 'U3': 2}     # declaration parameters: test cycles 2, UAT cycles 2
ELEMENT = re.compile(r'\b[SAC]-\d{2,3}(?:\.\d)?\b')
ACT = re.compile(r'^\*{0,2}([A-Z]\d{1,2}m?)\*{0,2}\b')
CLASSES = {'aggregate', 'behaviour', 'surface', 'interface', 'store', 'statement'}


def section(txt, n):
    """Text of markdown section '## n.' up to the next '## '."""
    m = re.search(r'^## %s\. .*$' % re.escape(str(n)), txt, re.M)
    if not m:
        return ''
    rest = txt[m.end():]
    m2 = re.search(r'^## ', rest, re.M)
    return rest[:m2.start()] if m2 else rest


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


classes = OrderedDict()   # element -> class
items = []                # (batch, activity, element, cycle)
judgements = []           # (batch, element, activity, reason)
batch_totals = {}
for b in BATCHES:
    txt = open(os.path.join(HERE, f'HW45-{b}1.md'), encoding='utf-8').read()
    # --- section 3: classification
    for line in section(txt, 3).split('\n'):
        if not line.startswith('| '):
            continue
        c = cells(line)
        if len(c) < 3 or not ELEMENT.fullmatch(c[0]):
            continue
        cls = re.sub(r'[*`]', '', c[2]).strip().lower()
        if cls not in CLASSES:
            print(f'!! batch {b}: unparsed class for {c[0]}: {c[2]!r}', file=sys.stderr)
            continue
        if c[0] in classes:
            print(f'!! duplicate element {c[0]} in batch {b}', file=sys.stderr)
        classes[c[0]] = cls
    # --- section 4: the crossing
    k1 = None
    prev = []
    parents_all = []
    declared = 0
    for line in section(txt, 4).split('\n'):
        if not line.startswith('| '):
            continue
        c = cells(line)
        if len(c) < 4:
            continue
        m = ACT.match(c[0])
        if not m:
            continue
        act = m.group(1)
        if act in ('E2', 'O2', 'S1') and '/' in c[0] or ',' in c[0].split(' ')[0]:
            continue  # grouped deferred rows like "E2, E3, E4, E6, E7"
        target = c[2]
        low = target.lower()
        found = ELEMENT.findall(target)
        if 'deferred' in low or low.strip('— -') == '' or 'none' in low:
            elems = []
        elif 'same' in low and 'k1' in low:
            elems = list(k1)
        elif found:
            elems = found
        elif 'same' in low:
            elems = list(prev)          # "same 8 parents (each x2)" - the previous row's list
        elif 'parent' in low:
            elems = list(parents_all)   # "8 parents", "all 11 parents"
        else:
            elems = []
        if act == 'K1':
            k1 = elems
        if act == 'A5':
            parents_all = elems
        if elems:
            prev = elems
        try:
            cnt = int(re.sub(r'[*]', '', c[3]))
        except ValueError:
            cnt = None
        mult = CYCLED.get(act, 1)
        if cnt is not None and elems and cnt != len(elems) * mult:
            print(f'!! batch {b} {act}: table count {cnt} vs parsed {len(elems)}x{mult}', file=sys.stderr)
        for e in elems:
            for cyc in range(1, mult + 1):
                items.append((b, act, e, cyc))
        if cnt:
            declared += cnt
    batch_totals[b] = (declared, sum(1 for i in items if i[0] == b))
    # --- section 5: judgement refusals
    for line in section(txt, 5).split('\n'):
        if not line.startswith('| ') or 'judgement' not in line.lower():
            continue
        c = cells(line)
        if len(c) >= 4 and 'judgement' in c[2].lower():
            judgements.append((b, c[0], c[1], c[3][:80]))

# --- write
with open(os.path.join(HERE, 'classes.tsv'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('element\tclass\n')
    for e, cls in classes.items():
        f.write(f'{e}\t{cls}\n')
with open(os.path.join(HERE, 'work_model.tsv'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('batch\tactivity\telement\tcycle\tclass\n')
    for b, a, e, cyc in items:
        f.write(f'{b}\t{a}\t{e}\t{cyc}\t{classes.get(e, "?")}\n')

# --- readings
print('elements classified:', len(classes), Counter(classes.values()))
print('batch totals (declared, parsed):', batch_totals)
print('crossing items total:', len(items))
by_act = Counter(a for _, a, _, _ in items)
print('items by activity:', dict(sorted(by_act.items())))
per_el = Counter(e for _, _, e, _ in items)
untouched = [e for e in classes if e not in per_el]
print('elements untouched:', untouched)
print('judgement refusals:', len(judgements))
for j in judgements:
    print('   ', j)
