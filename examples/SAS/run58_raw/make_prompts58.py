"""Run 58 - assemble the work-crosser prompts for HM57-1 (Hotyn-M 2.1), one per batch.
Reads run57_raw/HM57-1.md section 6 (the fenced TSV: id, parent, origin, coverage, name). INPUT 2 (the technology
declaration as the crosser must see it) and INPUT 3 (the demanded-work list) are taken at run time from run 45's
generator (run45_raw/make_prompts.py), so the declaration the sensor sees is byte-identical to run 45's. Batches are
HM57-1's top-level subtrees, grouped to the size of run 45's batches (25-37 elements). Writes prompt_<batch>.md.
Usage: python examples/SAS/run58_raw/make_prompts58.py [OUT dir]"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

BATCHES = {  # batch: top-level subtrees of N01, in the model's own order
    'A': ['N02'], 'B': ['N06', 'N07', 'N10'], 'C': ['N08', 'N09'], 'D': ['N11', 'N12'],
    'E': ['N13'], 'F': ['N19', 'N20'], 'G': ['N21', 'N22'],
}
ROOT = 'N01'

# --- the product model: section 6 of HM57-1, one fenced TSV block
txt = open(os.path.join(HERE, '..', 'run57_raw', 'HM57-1.md'), encoding='utf-8').read()
sec6 = txt[txt.index('\n## 6. '):txt.index('\n## 7. ')]
blk = sec6[sec6.index('```tsv') + 6:sec6.rindex('```')]
lines = [l for l in blk.strip('\n').split('\n') if l.strip()]
hdr = lines[0].split('\t')
assert hdr == ['id', 'parent', 'origin', 'coverage', 'name'], hdr
nodes, order = {}, []
for l in lines[1:]:
    c = l.split('\t')
    nodes[c[0]] = dict(parent=c[1], prov=c[2], cov=c[3].strip(), name=c[4])
    order.append(c[0])
kids = {}
for k, n in nodes.items():
    kids.setdefault(n['parent'], []).append(k)


def subtree(k):
    out = [k]
    for c in kids.get(k, []):
        out += subtree(c)
    return out


# --- INPUT 2 and INPUT 3, verbatim from run 45's generator
src = open(os.path.join(HERE, '..', 'run45_raw', 'make_prompts.py'), encoding='utf-8', newline='').read()
src = src.replace('\r\n', '\n')


def block(marker):
    start = src.index(marker)
    end = src.index('"""', start)
    return src[start:end]


DECLARATION = block('# INPUT 2')
DEMANDED = block('# INPUT 3')


def header(roots, n):
    return f"""Cross the product model subtrees named below with the declared technology. Everything you need is in this message; read no files.

**Partial run.** Scope: the subtrees rooted at **{', '.join(roots)}** of the closed product model `HM57-1` — **{n} elements**, listed in INPUT 1 with their parents and coverage. The model root `{ROOT}` and every other subtree are outside this batch: do not cross them and do not speculate about them. Per the partial-run rule, once-scoped and per-environment activities are **deferred**, not generated, and per-parent activities apply only to parents inside the batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, beginning at section 1 and ending at section 9, with every section the engine definition requires. **Compact §4 at the orchestrator's instruction: one row per activity — activity id, scope, the element ids receiving an item, the count — with item ids of the form `ACTIVITY@ELEMENT`.** The classification log (§3) and the `no` log (§5) are not compacted: every element with its class, every refusal with its kind and reason.

---

# INPUT 1 — the product model subtrees in scope (from `HM57-1`, `Hotyn-M 2.1`, closed and normalised)

This model keeps coverage in leaves only. **A node (an element with children) has an empty coverage column by rule; its content is its children.** A leaf's declared content is its name together with the obligations it covers. A derived leaf has no requirement coverage: its column holds `trigger: <ids>`, the elements whose existence called for it, and its content is its name read with that trigger. One derived node (`CN01`) carries a trigger in its column as well; it is a node — its content is its children — and the trigger is not coverage. Every element listed here has its parent listed here, except the batch roots whose parent is `{ROOT}`. Origin values: posited (skeleton), accreted (added at a requirement), derived (added at completion).

| id | name | parent | origin | coverage |
|---|---|---|---|---|
"""


for batch, roots in BATCHES.items():
    ids = []
    for r in roots:
        ids += subtree(r)
    rows = ''.join(
        f"| {k} | {nodes[k]['name']} | {nodes[k]['parent']} | {nodes[k]['prov']} | {nodes[k]['cov'] or '—'} |\n"
        for k in order if k in ids)
    body = header(roots, len(ids)) + rows + '\n---\n\n' + DECLARATION
    if batch == 'G':
        body += '\n---\n\n' + DEMANDED
    open(os.path.join(OUT, f'prompt_{batch}.md'), 'w', encoding='utf-8', newline='\n').write(body)
    print(batch, roots, len(ids), 'elements', len(body), 'chars')

covered = set()
for roots in BATCHES.values():
    for r in roots:
        covered |= set(subtree(r))
missing = [k for k in order if k not in covered and k != ROOT]
assert not missing, missing
assert set(kids[ROOT]) == {r for roots in BATCHES.values() for r in roots}, kids[ROOT]
print('all', len(covered), 'non-root elements batched; root', ROOT, 'outside every batch')
