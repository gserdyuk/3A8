# Run 18 — the coverage-agreement metric, recomputed on normalised models (2026-08-20).
#
# Reads run18_raw/models.md, extracts every node's declared coverage set, and compares the four
# models by the registered test of proposal_product_model.md M2: over all C(73,2)=2628 requirement
# pairs, do both models place the pair under a common node?
#
# Conventions, fixed by reproducing run 18 §3a exactly (0.161 / 0.270 / 0.220 / 0.195):
#   - a partial-coverage mark (R65p) counts as coverage. Excluding partials collapses Sonnet's
#     relation from 44 pairs to 3 and the comparison with it, so the published figures are the
#     partials-counted convention.
#   - co-location is judged on a node's DECLARED coverage set, never on the union of its subtree:
#     under subtree union the root covers everything and every pair agrees trivially.
#
# M7 normalisation (collapse a node whose content resolves to a single leaf into that leaf, merging
# the coverage sets) is applied through the `merges` table below. Those collapses were read off
# models.md by hand because the file records parent structure only where the node ids or the arrows
# carry it. HM-OA records no parent pointers at all and therefore cannot be normalised from the
# record — see run18_product_model_pilot.md §3c.
#
# Columns: J = Jaccard. max-J = |smaller| / |larger|, the largest Jaccard these two relations could
# reach at their sizes. overlap = |A and B| / |smaller|, the share of the smaller relation contained
# in the larger. agree% = raw pair agreement, inflated by sparsity, never to be quoted alone.

import re, itertools
src=open("C:/home/OhmNova/3A8/examples/BMS/run18_raw/models.md",encoding="utf-8").read()
secs={}
for m in re.finditer(r'^## (HM-\w+).*?$(.*?)(?=^## |\Z)', src, re.S|re.M):
    body=m.group(2)
    for stop in ["**Empty skeleton nodes","**Verdicts:","**Ambiguity flags"]:
        i=body.find(stop)
        if i>=0: body=body[:i]
    secs[m.group(1)]=body

def sets(body):
    out=[]
    for g in re.findall(r'\{([^}]*)\}', body):
        ids={t[:-1] if t.endswith('p') else t for t in re.findall(r'R\d{2}p?', g)}
        out.append(frozenset(ids))
    return out

# collapses recorded by reading the raw file: parent -> single child chain, coverage merged (M7 step 2)
merges={
 "HM-SA":[({"R11","R65"},{"R65"}),({"R57","R54","R20"},{"R20"}),({"R36","R37"},{"R37"}),({"R46","R47"},{"R47"})],
 "HM-SB":[({"R05"},set()),({"R10"},set())],
 "HM-OA":[],   # parent structure not recorded in the raw file
 "HM-OB":[({"R25","R50"},{"R29"}),({"R29","R48"},{"R45"}),({"R15"},{"R15"}),({"R19","R24"},{"R24"}),
          ({"R06","R21","R31","R32","R41"},{"R31"}),({"R52"},set()),({"R05","R36","R46"},set()),
          ({"R13","R68"},set()),({"R63"},set()),({"R11","R54","R65"},set()),({"R03","R14"},set()),
          ({"R01","R02"},set())],
}
def pairs(setlist, cap=None):
    P=set()
    for s in setlist:
        if cap and len(s)>cap: continue
        for a,b in itertools.combinations(sorted(s),2): P.add((a,b))
    return P

def table(name, P):
    print(f"\n--- {name}")
    print("pairing            |A|   |B|  inter  union      J    max-J  J/maxJ  overlap  agree%")
    for a,b in [("HM-SA","HM-SB"),("HM-OA","HM-OB"),("HM-SA","HM-OA"),("HM-SB","HM-OB")]:
        A,B=P[a],P[b]; i=len(A&B); u=len(A|B); mn=min(len(A),len(B))
        J=i/u; mx=mn/max(len(A),len(B)); ov=i/mn; ag=(2628-len(A^B))/2628*100
        print(f"{a} vs {b}  {len(A):4d} {len(B):5d} {i:5d} {u:6d}  {J:.3f}  {mx:.3f}   {J/mx:.2f}   {ov:.3f}   {ag:.1f}")

raw={k:sets(v) for k,v in secs.items()}
P0={k:pairs(v) for k,v in raw.items()}
table("as recorded (reproduces run 18 §3a)", P0)

norm={k:raw[k]+[frozenset(p|c) for p,c in merges[k]] for k in raw}
P1={k:pairs(v) for k,v in norm.items()}
table("after M7 normalisation (HM-OA unchanged: structure not recorded)", P1)

print("\npairs added by normalisation:")
for k in raw: print(f"  {k}: {len(P0[k])} -> {len(P1[k])}   new: {sorted(P1[k]-P0[k])}")

P2={k:pairs(v,cap=3) for k,v in norm.items()}
table("normalised, restricted to nodes covering <=3 requirements", P2)

print("\ncoverage-set profile (nodes declaring 2+ requirements, by size):")
for k in raw:
    sz=[len(s) for s in raw[k] if len(s)>1]
    print(f"  {k}: n={len(sz)}  max={max(sz)}  mean={sum(sz)/len(sz):.2f}  pairs={len(P0[k])}")


# ---------------------------------------------------------------------------
# The input-ambiguity component (assumptions.md A11, added 2026-08-20).
#
# A comparison is reported twice: over all requirements, and excluding those under an open question.
# The filter should be the pinned register (open_questions.md). Run 18 predates the register, so the
# retroactive stand-in below is the union of the runs own ambiguity flags — which is exactly the
# weakness A11 names, since a run that flags more shrinks what it is scored on. Exploratory, not a
# registered test.

flags = {"HM-SA": "R05 R10",
         "HM-SB": "R56 R49 R40 R37 R29 R25 R57 R11 R05",
         "HM-OA": "R01 R03 R10 R13 R14 R29 R44 R67 R71",
         "HM-OB": "R25 R37 R15 R14 R07 R10 R71 R67 R13 R11 R05 R03"}
flags = {k: set(v.split()) for k, v in flags.items()}
allflags = set().union(*flags.values())

def pairs_ex(setlist, drop):
    P = set()
    for s in setlist:
        s = s - drop
        for a, b in itertools.combinations(sorted(s), 2): P.add((a, b))
    return P

print()
print("--- input-ambiguity component: flagged by at least one run =", len(allflags), "of 73")
print("pairing            |A|   |B|      J   overlap   basis")
for a, b in [("HM-SA","HM-SB"),("HM-OA","HM-OB"),("HM-SA","HM-OA"),("HM-SB","HM-OB")]:
    for drop, label in [(frozenset(), "all 73"),
                        (frozenset(flags[a] | flags[b]), "excl. this pair's flags"),
                        (frozenset(allflags), "excl. all 19 flagged")]:
        A, B = pairs_ex(norm[a], drop), pairs_ex(norm[b], drop)
        i, u = len(A & B), len(A | B)
        mn = min(len(A), len(B))
        j = i / u if u else 0.0
        ov = i / mn if mn else 0.0
        print(f"{a} vs {b}  {len(A):4d} {len(B):5d}  {j:.3f}   {ov:.3f}   {label}")
