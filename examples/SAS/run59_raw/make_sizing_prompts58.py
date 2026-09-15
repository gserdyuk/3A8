"""Run 59 - assemble the work-estimator (Hotyn-D 2.0) prompts for the run 58 work model, one per crossing batch.
Inputs: run58_raw/classes.tsv and work_model.tsv (the crossing of HM57-1), run57_raw/HM57-1.md section 6 (names,
parents, coverage; the 2.x fenced TSV), requirements_product.md (obligation texts). INPUT 2, the sizing rules, is
taken at run time from run 47's generator (run47_raw/make_sizing_prompts.py) so that it is byte-identical to run 47's.
Writes prompt_size_<batch>.md into OUT. Contains no rate, price, effort or duration.
Usage: python examples/SAS/run59_raw/make_sizing_prompts58.py [OUT dir]"""
import csv
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.abspath(os.path.join(HERE, '..'))
OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
BATCHES = {'A': ['N02'], 'B': ['N06', 'N07', 'N10'], 'C': ['N08', 'N09'], 'D': ['N11', 'N12'],
           'E': ['N13'], 'F': ['N19', 'N20'], 'G': ['N21', 'N22']}
REQ = re.compile(r'\b(?:I|G|P|L|D|NFR)-\d+(?:\.\d+)?\b')

# --- product model (HM57-1, section 6 TSV)
txt = open(os.path.join(CASE, 'run57_raw', 'HM57-1.md'), encoding='utf-8').read()
sec6 = txt[txt.index('\n## 6. '):txt.index('\n## 7. ')]
blk = sec6[sec6.index('```tsv') + 6:sec6.rindex('```')]
lines = [l for l in blk.strip('\n').split('\n') if l.strip()]
assert lines[0].split('\t') == ['id', 'parent', 'origin', 'coverage', 'name']
nodes, order = {}, []
for l in lines[1:]:
    c = l.split('\t')
    nodes[c[0]] = dict(name=c[4], parent=c[1], origin=c[2], raw=c[3].strip(), cov=REQ.findall(c[3]))
    order.append(c[0])
kids = defaultdict(list)
for k, n in nodes.items():
    kids[n['parent']].append(k)


def subtree(k):
    out = [k]
    for c in kids.get(k, []):
        out += subtree(c)
    return out


# --- obligations
req = {}
for line in open(os.path.join(CASE, 'requirements_product.md'), encoding='utf-8'):
    m = re.match(r'^\| ((?:I|G|P|L|D|NFR)-[0-9.]+) \| (.*) \| (.*) \|\s*$', line)
    if m:
        req[m.group(1)] = m.group(2)

# --- crossing
classes = {}
for row in csv.DictReader(open(os.path.join(CASE, 'run58_raw', 'classes.tsv'), encoding='utf-8'), delimiter='\t'):
    classes[row['element']] = row['class']
acts = defaultdict(set)
for row in csv.DictReader(open(os.path.join(CASE, 'run58_raw', 'work_model.tsv'), encoding='utf-8'), delimiter='\t'):
    acts[row['element']].add(row['activity'])

# --- INPUT 2 verbatim from run 47's generator
src = open(os.path.join(CASE, 'run47_raw', 'make_sizing_prompts.py'), encoding='utf-8', newline='').read()
src = src.replace('\r\n', '\n')
start = src.index('# INPUT 2')
RULES = src[start:src.index('"""', start)]


def header(roots, n):
    return f"""Size the elements of the work model batch below by classifying, not pricing. Everything you need is in this message; read no files.

**Scope: the subtrees rooted at {', '.join(roots)} of the product model `HM57-1`, as classified and crossed by `Hotyn-W 1.2`** — {n} sized elements (aggregates are listed for context and are never sized). Other subtrees and the model root are outside this batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, sections 1 to 7 as your engine definition requires. In the sizing table quote the enumeration verbatim, one row per sized element, grouped by subtree. Every number you output is a count of named things; nothing else.

---

# INPUT 1 — the work model batch: elements with class, parent, declared content, covered obligations (with their texts) and the activities crossed onto them

In this model coverage lives in leaves only: an aggregate's content is its children. A derived leaf has no covered obligation; its declared content is its name read with the trigger that called for it (the elements named after `trigger:`).

"""


for batch, roots in BATCHES.items():
    ids = []
    for r in roots:
        ids += subtree(r)
    rows = []
    sized = 0
    for e in order:
        if e not in ids:
            continue
        n = nodes[e]
        cls = classes.get(e, '?')
        if cls == 'aggregate':
            rows.append(f"\n**{e} — {n['name']}** · aggregate (not sized) · parent {n['parent']}\n")
            continue
        sized += 1
        if n['cov']:
            cov = '; '.join(f"{r}: {req.get(r, '?')}" for r in n['cov'])
        else:
            cov = f"— (derived element, no covered obligation; {n['raw']})"
        a = ', '.join(sorted(acts.get(e, []), key=lambda x: (x[0], len(x), x)))
        rows.append(f"- **{e} — {n['name']}** · class **{cls}** · parent {n['parent']}\n"
                    f"  - covered obligations: {cov}\n"
                    f"  - activities crossed onto it: {a}\n")
    body = header(roots, sized) + ''.join(rows) + '\n---\n\n' + RULES
    open(os.path.join(OUT, f'prompt_size_{batch}.md'), 'w', encoding='utf-8', newline='\n').write(body)
    print(batch, roots, 'sized', sized, 'chars', len(body))
