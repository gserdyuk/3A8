"""Run 47 - assemble the work-estimator (Hotyn-D 2.0) prompts, one per crossing batch.
Inputs: run45_raw/classes.tsv and work_model.tsv (the crossing), run44_raw/HM44-OA1.md section 6 (names,
parents, coverage), requirements_product.md (obligation texts). The sizing rules are transcribed below from
catalogue 1.4 section 3a. Writes prompt_<batch>.md into OUT. Contains no rate, price, effort or duration.
Usage: python make_sizing_prompts.py <OUT dir>"""
import csv
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.abspath(os.path.join(HERE, '..'))
OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
BATCHES = {'A': ['S-01', 'S-02'], 'B': ['S-03'], 'C': ['S-04', 'S-05', 'S-06'], 'D': ['S-07', 'S-08'],
           'E': ['S-10', 'S-11'], 'F': ['S-12', 'S-13'], 'G': ['S-09', 'S-14']}

# --- product model
txt = open(os.path.join(CASE, 'run44_raw', 'HM44-OA1.md'), encoding='utf-8').read()
sec6 = txt[txt.index('\n## 6. '):txt.index('\n## 7. ')]
nodes, order = {}, []
for line in sec6.split('\n'):
    if not line.startswith('| '):
        continue
    c = [x.strip() for x in line.strip().strip('|').split('|')]
    if len(c) != 6 or c[0] == 'id' or set(c[0]) <= set('-'):
        continue
    nodes[c[0]] = dict(name=c[1], parent=c[2], cov=re.findall(r'\b(?:I|G|P|L|D|NFR)-\d+(?:\.\d+)?\b', c[5]))
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
for row in csv.DictReader(open(os.path.join(CASE, 'run45_raw', 'classes.tsv'), encoding='utf-8'), delimiter='\t'):
    classes[row['element']] = row['class']
acts = defaultdict(set)
for row in csv.DictReader(open(os.path.join(CASE, 'run45_raw', 'work_model.tsv'), encoding='utf-8'), delimiter='\t'):
    acts[row['element']].add(row['activity'])

RULES = """# INPUT 2 — the sizing rules (catalogue 1.4 §3a, verbatim where it binds)

**W10.** Every sized element receives one size class — **S / M / L / XL** — by **counting named things**. The
enumeration is the justification; a bare number is not acceptable. Thresholds are pinned here and are not
yours to bend. Drivers count scope, never effort: no driver may reference difficulty, risk, novelty or time.

**One size class per element, assigned once.** The class is a property of the element — a leaf, or an
internal node carrying own content. **A pure aggregate is never sized.** Every per-element activity uses the
element's class by default. **Position-derived sizes are not yours** (per-parent, once-scoped, per-environment
items are tree arithmetic computed outside you) — do not report them.

## Element size classes — counted from the element's declared content plus its own coverage

| element class | what is enumerated | S | M | L | XL |
|---|---|---|---|---|---|
| behaviour | distinct actions (verb on object) the declared content names | 1 | 2–3 | 4–6 | ≥7 |
| interface | operations consumed or exposed; a named protocol/auth concern counts as one | 1 | 2–4 | 5–8 | ≥9 |
| surface | distinct user tasks the surface serves | 1 | 2–3 | 4–6 | ≥7 |
| store | entity kinds the store is responsible for | 1 | 2–3 | 4–6 | ≥7 |
| statement (both kinds) | systems or components the property constrains | 1 | 2–4 | 5–8 | ≥9 |
| aggregate | — never sized | | | | |

**XL is a class and a signal at once:** an XL element is classed XL **and** reported as a probable coarseness
finding about the product model (M10). Neither substitutes for the other.

**`statement` splits into two kinds**, logged with the phrase that justifies the kind: **`compliance`** — the
content names a standard, configuration or policy and no run-time scenario; **`behavioural`** — the content
entails run-time behaviour. **P-4, the kind tie-break: run-time wins** — a statement whose covered obligations
mix kinds is `behavioural` when any covered obligation entails run-time behaviour, `compliance` only when none does.

## Special counts — enumerated the same way, where the element carries the activity

| activity on the element | driver enumerated | S | M | L | XL |
|---|---|---|---|---|---|
| **A9** (performance and availability testing, on a behavioural statement) | measurable targets the statement names (thresholds, service levels) — count from the content **and the covered obligations' texts** | 1 | 2–3 | 4–6 | ≥7 |
| **G2m / G3m / G4m** (field mapping, extraction and transformation, load and reconciliation, on a store) | entity kinds in the store that are loaded from the predecessor applications — say per kind why it must arrive from the predecessor rather than be created at run time | 1 | 2–3 | 4–6 | ≥7 |

The **D4** driver (requirement ids in the element's own coverage) is computed outside you from the coverage
sets; do not report it.

## Enumeration precedents — case law adjudicated once for everybody (catalogue 1.3 and 1.4)

- **P-1 — a named delivery channel is a protocol concern.** An interface whose obligation names a delivery
  channel counts the channel alongside the operation: "notifications via email" = the dispatch operation + the
  email channel = 2.
- **P-2 — a name token counts only when no counted obligation already covers its action.** A token in the
  element's name that an enumerated obligation already covers is not counted again; a token covered by no
  obligation is counted. The test is coverage, not position in name or text.
- **P-3 — slash-separated outcomes are distinct actions.** "Accepted/Rejected" names two transitions, not one;
  stage lists count by outcome.
- **P-4 — the kind tie-break: run-time wins** (above).
- **P-5 — an unnamed catch-all is not a named thing.** "and other details" names no kind and counts nothing.
- **P-6 — a stated cardinality without named members is not an enumeration.** "three amendment origins" is a
  number, not a list; an element whose declaration counts things it never names is **unsizeable — model
  defect (M10)**, never sized on a guessed reading.

An element you cannot count is a finding, not a guess: report it as *unsizeable — model defect (M10)* with what
is missing, and assign no class. You may not add, remove, merge or reshape elements or work items; work you
judge necessary and absent is a **closure violation** — name it, say what it would cover, do not size it.
"""


def header(roots, n):
    return f"""Size the elements of the work model batch below by classifying, not pricing. Everything you need is in this message; read no files.

**Scope: the subtrees rooted at {', '.join(roots)} of the product model `HM44-OA1`, as classified and crossed by `Hotyn-W 1.1`** — {n} sized elements (aggregates are listed for context and are never sized). Other subtrees and the model root are outside this batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, sections 1 to 7 as your engine definition requires. In the sizing table quote the enumeration verbatim, one row per sized element, grouped by subtree. Every number you output is a count of named things; nothing else.

---

# INPUT 1 — the work model batch: elements with class, parent, declared content, covered obligations (with their texts) and the activities crossed onto them

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
        cov = '; '.join(f"{r}: {req.get(r, '?')}" for r in n['cov']) or '— (derived element, empty own coverage)'
        a = ', '.join(sorted(acts.get(e, []), key=lambda x: (x[0], len(x), x)))
        rows.append(f"- **{e} — {n['name']}** · class **{cls}** · parent {n['parent']}\n"
                    f"  - covered obligations: {cov}\n"
                    f"  - activities crossed onto it: {a}\n")
    body = header(roots, sized) + ''.join(rows) + '\n---\n\n' + RULES
    open(os.path.join(OUT, f'prompt_size_{batch}.md'), 'w', encoding='utf-8', newline='\n').write(body)
    print(batch, roots, 'sized', sized, 'chars', len(body))
