#!/usr/bin/env python3
"""Step 2, the consolidation: the partial crossings of one run into one work model.

    python tools/chain/consolidate_crossing.py examples/<case> --run <N>

Reads examples/<case>/run<N>_raw/batches.json (written by make_crossing_prompts.py), the model it names, and
HW<N>-<batch>1.md for every batch. Parses section 3 (classification), the compacted section 4 (the crossing) and
section 5 (refusals). Every §4 row's parsed count is checked against the count the sensor printed; a mismatch is
printed and counted, never silently accepted. Writes classes.tsv and work_model.tsv into the run folder and
prints the readings the run record quotes. Cycle counts come from the declaration's parameters.
"""
import argparse, json, os, re, sys
from collections import Counter, OrderedDict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chainlib import Model, md_section

CLASSES = {'aggregate', 'behaviour', 'surface', 'interface', 'store', 'statement'}
BUILD = {'behaviour', 'surface', 'interface', 'store'}
ACT = re.compile(r'^\*{0,2}([A-Z]\d{1,2}[a-z]?)\*{0,2}\b')


def strip_md(s):
    return re.sub(r'[*`]', '', s).strip()


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('case')
    ap.add_argument('--run', required=True, type=int)
    a = ap.parse_args()
    case = a.case.rstrip('/\\')
    run_dir = os.path.join(case, 'run%d_raw' % a.run)
    rec = json.load(open(os.path.join(run_dir, 'batches.json'), encoding='utf-8'))
    model = Model(os.path.join(case, rec['model']))
    P = rec['parameters']
    CYCLED = {'A5': P.get('test_cycles', 1), 'A6': P.get('test_cycles', 1), 'U2': P.get('uat_cycles', 1) or 1, 'U3': P.get('uat_cycles', 1) or 1}
    ELEMENT = re.compile(r'\b(?:%s)\b' % '|'.join(sorted((re.escape(k) for k in model.order), key=len, reverse=True)))

    classes, items, judgements, filters = OrderedDict(), [], [], []
    batch_totals, mismatches = {}, 0
    for b, roots in rec['batches'].items():
        fn = os.path.join(run_dir, 'HW%d-%s1.md' % (a.run, b))
        if not os.path.exists(fn):
            print('!! missing', fn, file=sys.stderr)
            continue
        scope = []
        for r in roots:
            scope += model.subtree(r)
        scope_leaves = [e for e in scope if model.is_leaf(e)]
        scope_nodes = [e for e in scope if not model.is_leaf(e)]
        t = open(fn, encoding='utf-8').read()
        for line in md_section(t, 3).split('\n'):
            if not line.startswith('| '):
                continue
            c = cells(line)
            eid = strip_md(c[0])
            if len(c) < 3 or not ELEMENT.fullmatch(eid):
                continue
            found = [strip_md(x).lower() for x in c[1:] if strip_md(x).lower() in CLASSES]
            if not found:
                print('!! batch %s: unparsed class for %s: %r' % (b, eid, c[1:]), file=sys.stderr)
                continue
            if eid in classes:
                print('!! duplicate element %s in batch %s' % (eid, b), file=sys.stderr)
            classes[eid] = found[0]
        build_leaves = [e for e in scope_leaves if classes.get(e) in BUILD]
        s4 = md_section(t, 4)
        groups = {}
        for line in s4.split('\n'):
            if line.startswith('|'):
                continue
            ids = ELEMENT.findall(line)
            if len(ids) < 3:
                continue
            keys = re.findall(r'"([^"]+)"', line) + re.findall(r'\*\*([^*]+)\*\*\s*=', line) + re.findall(r'^\s*-?\s*\**(\w+)\**\s*(?:=|below means)', line)
            for k in keys:
                groups[k.strip().lower()] = ids
        k1, prev, declared = None, [], 0
        for line in s4.split('\n'):
            if not line.startswith('| '):
                continue
            c = cells(line)
            if len(c) < 4:
                continue
            head = strip_md(c[0])
            m = ACT.match(head)
            if not m or ',' in head.split(' ')[0] or '/' in head.split(' ')[0]:
                continue
            act = m.group(1)
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
                core = re.sub(r'\([^)]*\)', ' ', target)
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
                            elems = list(k1 or [])
                        elif 'same' in low:
                            elems = list(prev)
                        elif 'build' in low:
                            elems = list(build_leaves)
                        elif 'leaves' in low or 'leaf' in low:
                            elems = list(scope_leaves)
                        elif 'parent' in low:
                            elems = list(scope_nodes)
                        else:
                            print('!! batch %s %s: cannot read target %r' % (b, act, target), file=sys.stderr)
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
                print('!! batch %s %s: table count %s vs parsed %dx%d  (%r)' % (b, act, cnt, len(elems), mult, target[:60]), file=sys.stderr)
                mismatches += 1
            for e in elems:
                if e not in scope:
                    print('!! batch %s %s: element %s outside the batch scope' % (b, act, e), file=sys.stderr)
                for cyc in range(1, mult + 1):
                    items.append((b, act, e, cyc))
            if cnt:
                declared += cnt
        batch_totals[b] = (declared, sum(1 for i in items if i[0] == b))
        for line in md_section(t, 5).split('\n'):
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

    with open(os.path.join(run_dir, 'classes.tsv'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('element\tclass\n')
        for e in model.order:
            if e in classes:
                f.write('%s\t%s\n' % (e, classes[e]))
    with open(os.path.join(run_dir, 'work_model.tsv'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('batch\tactivity\telement\tcycle\tclass\n')
        for b, act, e, cyc in items:
            f.write('%s\t%s\t%s\t%d\t%s\n' % (b, act, e, cyc, classes.get(e, '?')))

    per_el = Counter(e for _, _, e, _ in items)
    summary = {
        'elements_classified': len(classes), 'classes': dict(Counter(classes.values())),
        'leaves_classed_aggregate': [e for e, c in classes.items() if c == 'aggregate' and model.is_leaf(e)],
        'nodes_not_aggregate': [e for e, c in classes.items() if c != 'aggregate' and not model.is_leaf(e)],
        'batch_totals_printed_vs_parsed': batch_totals, 'row_count_mismatches': mismatches,
        'items': len(items), 'items_by_activity': dict(sorted(Counter(a for _, a, _, _ in items).items())),
        'elements_crossed': len(per_el), 'items_per_crossed_element': round(len(items) / max(1, len(per_el)), 2),
        'elements_untouched': [e for e in classes if e not in per_el],
        'refusals_filter': len(filters), 'refusals_judgement': len(judgements),
        'filters_by_activity': dict(sorted(Counter(a for _, _, a in filters).items())),
        'judgements': judgements,
    }
    json.dump(summary, open(os.path.join(run_dir, 'crossing_summary.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for k, v in summary.items():
        print('%s: %s' % (k, v if not isinstance(v, list) or len(v) < 12 else '%d entries' % len(v)))


if __name__ == '__main__':
    main()
