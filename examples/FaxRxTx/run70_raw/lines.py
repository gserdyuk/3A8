#!/usr/bin/env python3
"""Runs 69-71 — the final work lists of the three Delphi panels, mapped onto one vocabulary of lines.

    py -X utf8 lines.py          # writes final tables verbatim, lines.tsv, and prints the comparison

For each panel the last segment of every participant's transcript is taken (run 69: the transcription request after
round 2; runs 70 and 71: round 3). Every markdown table row with a label and a person-month figure is read; subtotal
and total rows are skipped. The label is mapped to the vocabulary registered in run70_delphi_repeats_registration.md
by the keyword rules below — the moderator's judgement, written as code so it can be checked and changed. A line that
joins two vocabulary items is given to the first that matches and flagged. Rows nothing matches are printed.
Because participants draw the boundaries differently, the comparison is also made on three boundary-free groups:
the delivery stack (core + management tool + burst hardening), verification (real-stream/load testing + separate QA),
and overhead (PM, glue, novelty tax, discounts and rounding).
"""
import json, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(CASE, 'run69_raw'))
sys.argv = [sys.argv[0]]
import delphi   # noqa: E402  (its functions only; HERE inside it stays run 69's and is not used)

PANELS = [('run 69', 'run69_raw', 3), ('run 70', 'run70_raw', 3), ('run 71', 'run71_raw', 3)]

RULES = [   # first match wins; order is the judgement
    ('novelty tax', r'novelty'),
    ('glue / omissions', r'glue|drag|friction|inventory always misses|unlisted'),
    ('discount / rounding', r'discount|oracle|rounding|round-?up|rounded|judgement cut|downward adjustment|adjustment for|carry for|net revision|de-duplication'),
    ('QA, separate line', r'^\W*(?:uplift:?\W*)?(?:named uplift:?\W*)?(?:dedicated |cross-cutting |system-level )?qa\b|qa uplift|qa/pm uplift|dedicated qa|qa beyond|qa function|qa outside|cross-cutting qa'),
    ('PM', r'\bpm\b|project management|coordination|scrum'),
    ('immersion', r'immersion'),
    ('burst hardening', r'burst (?:and scale |and |& )?(?:hardening|qualification)|scale and burst|performance work|^\W*load and burst rig'),
    ('delivery-control core', r'watchdog|delivery[- ]control|orchestrat|cluster core|cluster \+ delivery|cluster with delivery|cluster and delivery'),
    ('cluster management', r'cluster management|management tool|cluster runtime'),
    ('render workers', r'render|format'),
    ('OCR', r'\bocr\b'),
    ('Rx path', r'\brx\b|outbound e?-?mail|outbound mail'),
    ('Tx parser', r'inbound|parser|\btx\b'),
    ('NOC', r'\bnoc\b'),
    ('portal', r'portal'),
    ('CDR', r'\bcdr\b'),
    ('real-stream / load testing', r'integration[- ](?:and load )?test|integration (?:&|and) load|real[- ]stream|parity|comparison|integration on the real'),
    ('data layer / API', r'schema|data layer|lustre|storage|inter-component|db \+|db/api|db and'),
    ('old-system / reused integration', r'coexistence|old system|reused|pop protocol|integration with|integration surface|integration:|integration fabric|integration seams|integration layer'),
    ('rollout / cutover', r'rollout|cutover|migration'),
    ('worker framework', r'worker (?:runtime|harness|host)|harness'),
]
GROUPS = {
    'delivery stack (core + mgmt tool + burst)': ['delivery-control core', 'cluster management', 'burst hardening'],
    'verification (real-stream/load + separate QA)': ['real-stream / load testing', 'QA, separate line'],
    'overhead (PM + glue + novelty + discounts)': ['PM', 'glue / omissions', 'novelty tax', 'discount / rounding'],
    'render + worker framework': ['render workers', 'worker framework'],
    'data + old-system integration': ['data layer / API', 'old-system / reused integration'],
}
SKIP = re.compile(r'^\W*\**(?:[\w, -]{0,40}subtotal|total|sum\b|carried|arithmetic|computed|running|before |round-\d total|of which)', re.I)
NUM = re.compile(r'^[\s*~≈+]*([−-]?\d+(?:\.\d+)?)\s*\**\s*(?:\*?\(?implied\)?\*?)?\s*$')


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def rows_of(reply):
    out = []
    for line in reply.split('\n'):
        if not line.lstrip().startswith('|') or re.match(r'^\s*\|[\s:|-]+\|\s*$', line):
            continue
        c = cells(line)
        val, vi = None, None
        for i, x in enumerate(c):
            m = NUM.match(re.sub(r'\*|_', '', x).replace('pm', '').strip())
            if m and i > 0:
                val, vi = float(m.group(1).replace('−', '-')), i
                break
        if val is None:
            continue
        label = max(c[:vi], key=len)
        label = re.sub(r'[*_`]', '', label).strip()
        if not label or SKIP.search(label) or re.fullmatch(r'#|\d{1,2}|[A-Z]', label):
            continue
        out.append((label, val))
    return out


def classify(label):
    low = label.lower()
    head = low[:70]          # a line is named by how it begins; what follows is usually explanation
    hits = [name for name, rx in RULES if re.search(rx, head)] or [name for name, rx in RULES if re.search(rx, low)]
    return (hits[0], hits[1:]) if hits else (None, [])


records, unmatched = [], []
for panel, folder, seg in PANELS:
    parts = json.load(open(os.path.join(CASE, folder, 'participants.json'), encoding='utf-8'))
    for p, agent in parts.items():
        s = delphi.segments(delphi.transcript(agent))[seg - 1]
        reply = s['texts'][-1]
        if folder == 'run69_raw':
            open(os.path.join(CASE, folder, 'final_table_%s.md' % p), 'w', encoding='utf-8', newline='\n').write(
                '<!-- orchestrator header, not part of the reply: run 69, transcription request after round 2 (no re-estimation), participant %s -->\n\n%s\n' % (p, reply))
        total = delphi.closing(reply)[0]
        rows = rows_of(reply)
        ssum = 0
        for label, val in rows:
            cat, also = classify(label)
            if cat is None:
                unmatched.append((panel, p, label, val))
                continue
            ssum += val
            records.append({'panel': panel, 'p': p, 'line': cat, 'also': also, 'pm': val, 'label': label})
        print('%s %-5s total %5s  lines %2d  sum of mapped lines %6.1f' % (panel, p, total, len(rows), ssum))

with open(os.path.join(HERE, 'lines.tsv'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('panel\tparticipant\tline\talso_matches\tpm\tlabel\n')
    for r in records:
        f.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (r['panel'], r['p'], r['line'], ';'.join(r['also']), r['pm'], r['label']))

print('\n=== rows no rule matched (%d) ===' % len(unmatched))
for u in unmatched:
    print('  ', u)


def per_panel(names):
    res = {}
    for panel, _, _ in PANELS:
        vals = {}
        for r in records:
            if r['panel'] == panel and r['line'] in names:
                vals[r['p']] = vals.get(r['p'], 0) + r['pm']
        res[panel] = vals
    return res


def show(title, names):
    res = per_panel(names)
    meds = []
    cellstr = []
    for panel, _, _ in PANELS:
        v = list(res[panel].values())
        if v:
            med = statistics.median(v)
            meds.append(med)
            cellstr.append('%2d/10 carry · median %5.1f · %4.1f–%4.1f' % (len(v), med, min(v), max(v)))
        else:
            cellstr.append(' 0/10 carry' + ' ' * 28)
    spread = (max(meds) / min(meds)) if len(meds) == 3 and min(meds) > 0 else None
    print('%-46s | %s | %s' % (title[:46], ' | '.join(cellstr), ('x%.2f' % spread) if spread else '  —'))


print('\n=== lines: how many of ten carry it, the panel median and range; last column = max/min of the three panel medians ===')
for name, _ in RULES:
    show(name, [name])
print('\n=== boundary-free groups ===')
for g, names in GROUPS.items():
    show(g, names)
