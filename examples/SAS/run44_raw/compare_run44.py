"""Run 44 - compare the two HM44 product models (SAS). Reads the two raw transcripts, parses section 6
(the final model), and prints the readings quoted in run44_product_model_measurement.md.
Usage: python examples/SAS/run44_raw/compare_run44.py"""
import re, itertools, os
HERE = os.path.dirname(os.path.abspath(__file__))
ID = r'\b(?:I|G|P|L|D|NFR)-\d+(?:\.\d+)?\b'

def parse(fn, ncols):
    txt = open(os.path.join(HERE, fn), encoding='utf-8').read()
    sec6 = txt[txt.index('\n## 6. '):txt.index('\n## 7. ')]
    nodes = {}
    for line in sec6.split('\n'):
        if not line.startswith('| '):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) != ncols or cells[0] == 'id' or set(cells[0]) <= set('-'):
            continue
        nodes[cells[0]] = dict(parent=cells[2], prov=cells[3], cov=set(re.findall(ID, cells[-1])))
    return nodes

def pairs(nodes):
    s = set()
    for n in nodes.values():
        s.update(itertools.combinations(sorted(n['cov']), 2))
    return s

def readings(tag, nodes, req):
    prov = {}
    for n in nodes.values():
        prov[n['prov']] = prov.get(n['prov'], 0) + 1
    covered = set().union(*[n['cov'] for n in nodes.values()])
    twins = sum(1 for n in nodes.values()
                if any(i.startswith('P-') for i in n['cov']) and any(i.startswith('L-') for i in n['cov']))
    print(f"{tag}: nodes after normalisation {len(nodes)} · provenance {prov} · "
          f"assignments {sum(len(n['cov']) for n in nodes.values())} · ids covered {len(covered)}/{len(req)} · "
          f"missing {sorted(req - covered)} · co-located pairs {len(pairs(nodes))} · nodes covering a P- and an L- id {twins}")

req = set(re.findall(r'^\| (' + ID[2:-2] + r') \|',
          open(os.path.join(HERE, '..', 'requirements_product.md'), encoding='utf-8').read(), re.M))
a = parse('HM44-OA1.md', 6)
b = parse('HM44-OA2.md', 5)
readings('OA1', a, req)
readings('OA2', b, req)
pa, pb = pairs(a), pairs(b)
print(f"co-location Jaccard: shared {len(pa & pb)} · union {len(pa | pb)} · J = {len(pa & pb) / len(pa | pb):.3f}")
