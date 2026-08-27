# run 42 - FaxRxTx whole-model assembly on the SECOND product model of the run-29 pair
#
# Purpose: the chain's first END-TO-END repeatability figure. HM29-OA1 (97 nodes) was carried to
# 1423.2 table pd by run 31; HM29-OA2 (87 nodes) had never been crossed or sized. Nothing here is
# a new rate: every constant is copied from run31_raw/assemble_faxrxtx.py, and the ONLY differences
# are those the second model forces.
#
#   product model    HM29-OA2  (Hotyn-M 1.1, 87 nodes, 18 parents, 69 leaves)
#   work model       HW42-A/B/C  (Hotyn-W 1.1, 584 crossing items + 4 demanded branches)
#   size classes     HD42-A/B/C  (Hotyn-D 2.0)
#   rates            docs/rate_table.md v0.1 + addendum A1; FaxRxTx addenda A2/A3 - UNCHANGED
#   declaration      examples/FaxRxTx/technology_declaration.md - UNCHANGED
#
# Conventions identical to run 31: subtree = rooted; C3 base = leaf-item E of the rooted subtree,
# element-attached only; once/per-environment/demanded enter no C3 base; rate 20%, never compounding;
# E(O,M,P) = (O + 4M + P)/6.
#
# THE MODEL BRACKET STEPS. 97 elements -> L (>=91); 87 elements -> M (31-90). The once-layer
# therefore takes its M rows here where run 31 took L. That is tree arithmetic, not a judgement.

import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

KIDS = {
 "HM2-01": ["HM2-02","HM2-03","HM2-04","HM2-05","HM2-06","HM2-07","HM2-08","HM2-09","HM2-10","HM2-11","HM2-13"],
 "HM2-02": ["HM2-15","HM2-17","HM2-18","HM2-21","HM2-22","HM2-26","HM2-31"],
 "HM2-03": ["HM2-16","HM2-20","HM2-33","HM2-37"],
 "HM2-04": ["HM2-34","HM2-36","HM2-40"],
 "HM2-05": ["HM2-54","HM2-55","HM2-56","HM2-57","HM2-58","HM2-73","HM2-81","HM2-82","HM2-85"],
 "HM2-06": ["HM2-51","HM2-66","HM2-72","HM2-74","HM2-79","HM2-80","HM2-87","HM2-89","HM2-90","HM2-92"],
 "HM2-07": ["HM2-25","HM2-59","HM2-60","HM2-61","HM2-62","HM2-86","HM2-88"],
 "HM2-08": ["HM2-12","HM2-14","HM2-38","HM2-39"],
 "HM2-09": ["HM2-64","HM2-65","HM2-67","HM2-68"],
 "HM2-10": ["HM2-69","HM2-70","HM2-71"],
 "HM2-11": ["HM2-75","HM2-76"],
 "HM2-12": ["HM2-77","HM2-78"],
 "HM2-13": ["HM2-83","HM2-84","HM2-91"],
 "HM2-18": ["HM2-23","HM2-24"],
 "HM2-26": ["HM2-27","HM2-30"],
 "HM2-27": ["HM2-28","HM2-29"],
 "HM2-40": ["HM2-41","HM2-42","HM2-43","HM2-44","HM2-45","HM2-46","HM2-47","HM2-48","HM2-49"],
 "HM2-51": ["HM2-52","HM2-53"],
}

# ---- element classes, from the three HW42 crossings verbatim -------------------------------
# NOTE vs run 31: OA1 forced CLS[parent]="aggregate" because all 18 of its parents had EMPTY own
# coverage. OA2 places obligations on five parents (HM2-02, 03, 18, 26, 27), which the crossing
# therefore classified as priced elements AND parents. That difference is the model's, not ours.
CLS = {}
for e in ["HM2-17","HM2-18","HM2-20","HM2-21","HM2-22","HM2-23","HM2-24","HM2-26","HM2-27",
          "HM2-29","HM2-30","HM2-33","HM2-34","HM2-36","HM2-37","HM2-41","HM2-42","HM2-43",
          "HM2-44","HM2-45","HM2-46","HM2-47","HM2-48","HM2-49",
          "HM2-54","HM2-56","HM2-57","HM2-58","HM2-73","HM2-81","HM2-82","HM2-85","HM2-66",
          "HM2-72","HM2-79","HM2-80","HM2-87","HM2-89","HM2-62","HM2-86",
          "HM2-83","HM2-84","HM2-91"]:
    CLS[e] = "behaviour"
for e in ["HM2-15","HM2-16","HM2-28","HM2-31","HM2-38","HM2-39","HM2-77"]:
    CLS[e] = "interface"
for e in ["HM2-55","HM2-74","HM2-25","HM2-59","HM2-60","HM2-61","HM2-88","HM2-14","HM2-75","HM2-76"]:
    CLS[e] = "store"
for e in ["HM2-52","HM2-53","HM2-64","HM2-65","HM2-67","HM2-68","HM2-69","HM2-70","HM2-71"]:
    CLS[e] = "surface"
for e in ["HM2-02","HM2-03","HM2-90","HM2-92","HM2-78"]:
    CLS[e] = "statement"
for e in ["HM2-01","HM2-04","HM2-40","HM2-05","HM2-06","HM2-07","HM2-51",
          "HM2-08","HM2-09","HM2-10","HM2-11","HM2-12","HM2-13"]:
    CLS[e] = "aggregate"

# ---- own coverage counts, for D4 sizing (computed from the model table) --------------------
COV = json.load(open(os.path.join(HERE, "oa2_tree.json")))["cov"]

# ---- own item sets, from the three HW42 crossings ------------------------------------------
STD = ["K1","K2","A2","A3","A4"]
OWN = {}
def own(els, items):
    for e in els:
        OWN[e] = list(items)

# batch A
own(["HM2-15","HM2-16","HM2-28","HM2-31"], STD+["A10","D4"])
own(["HM2-17","HM2-18","HM2-20","HM2-21","HM2-22","HM2-23","HM2-24","HM2-26","HM2-27","HM2-29",
     "HM2-30","HM2-33","HM2-34","HM2-36","HM2-37","HM2-41","HM2-42","HM2-43","HM2-44","HM2-45",
     "HM2-46","HM2-47","HM2-48","HM2-49"], STD+["D4"])
own(["HM2-02","HM2-03"], ["K3","D4"])
# batch B
own(["HM2-54","HM2-56","HM2-57","HM2-58","HM2-73","HM2-81","HM2-82","HM2-52","HM2-53","HM2-66",
     "HM2-72","HM2-79","HM2-80","HM2-89","HM2-59","HM2-60","HM2-62"], STD+["D4"])
own(["HM2-55"], STD+["D4"])                    # store, but no G-triple: fills at run time
own(["HM2-85","HM2-87","HM2-86"], STD)         # derived, no coverage -> no D4
own(["HM2-74","HM2-25","HM2-61"], STD+["D4","G1","G2","G3"])
own(["HM2-88"], STD+["G1","G2","G3"])          # derived, no coverage -> no D4
own(["HM2-90","HM2-92"], ["K3"])               # derived statements, K3 alone
# batch C
own(["HM2-38","HM2-39","HM2-77"], STD+["A10","D4"])
own(["HM2-64","HM2-65","HM2-67","HM2-68","HM2-69","HM2-70","HM2-71","HM2-75","HM2-76"], STD+["D4"])
own(["HM2-83","HM2-84","HM2-91"], STD)         # derived, no coverage -> no D4
own(["HM2-14"], STD+["D4","G1","G2","G3"])
own(["HM2-78"], ["K3","D4"])

# ---- per-parent item sets -------------------------------------------------------------------
P7 = [("A5",2),("A6",2),("A7",1),("A8",1),("D2",1)]
PARENT = {p: list(P7) for p in KIDS}            # all 18 parents, root included
for p in ["HM2-06","HM2-51","HM2-09","HM2-10","HM2-01"]:   # O1 gated on a surface in the subtree
    PARENT[p].append(("O1",1))

# ---- rate table v0.1 (+A1) -- copied verbatim from run31_raw/assemble_faxrxtx.py ------------
T = {
 ("K1","bss"):{"S":(2,4,8),"M":(4,8,16),"L":(8,16,28),"XL":(16,28,48)},
 ("K1","int"):{"S":(4,8,16),"M":(8,16,32),"L":(16,28,48),"XL":(24,40,72)},
 ("K2","bs"):{"S":(4,8,16),"M":(8,20,40),"L":(20,40,72),"XL":(40,64,112)},
 ("K2","int"):{"S":(8,16,32),"M":(16,28,56),"L":(24,48,80),"XL":(40,72,120)},
 ("K2","sto"):{"S":(4,8,16),"M":(8,16,28),"L":(16,32,56),"XL":(28,52,88)},
 ("K3","compliance"):{"S":(2,4,12),"M":(4,12,24),"L":(8,20,40),"XL":(16,32,64)},
 ("K3","behavioural"):{"S":(8,16,32),"M":(16,32,64),"L":(24,48,96),"XL":None},
 ("A2","*"):{"S":(2,4,8),"M":(4,8,16),"L":(8,16,28),"XL":(12,24,40)},
 ("A3","*"):{"S":(4,8,16),"M":(8,16,32),"L":(16,28,48),"XL":(24,44,72)},
 ("A4","*"):{"S":(0.8,2,4),"M":(2,4,8),"L":(4,8,16),"XL":(6,12,24)},
 ("A9","*"):{"S":(8,16,32),"M":(16,28,56),"L":(24,44,80),"XL":(32,64,112)},
 ("A10","*"):{"S":(4,8,20),"M":(8,16,32),"L":(16,28,56),"XL":(24,40,80)},
 ("A5","*"):{"S":(4,8,16),"M":(8,16,32),"L":(16,28,48),"XL":(24,40,72)},
 ("A6","*"):{"S":(4,12,32),"M":(8,24,56),"L":(16,40,80),"XL":(24,56,112)},
 ("A7","*"):{"S":(8,16,32),"M":(16,32,56),"L":(24,48,80),"XL":(32,64,112)},
 ("A8","*"):{"S":(2,4,12),"M":(4,12,24),"L":(8,20,40),"XL":(16,32,64)},
 ("D2","*"):{"S":(4,8,16),"M":(8,16,32),"L":(16,28,48),"XL":(24,40,64)},
 ("D4","*"):{"S":(2,4,8),"M":(4,8,16),"L":(8,16,32),"XL":(12,24,48)},
 ("O1","*"):{"S":(4,8,16),"M":(8,16,32),"L":(16,28,48),"XL":(24,40,72)},
 ("G1","*"):{"S":(2,4,8),"M":(4,8,16),"L":(8,16,28),"XL":(12,24,40)},
 ("G2","*"):{"S":(2,4,12),"M":(4,12,24),"L":(8,20,40),"XL":(16,32,56)},
 ("G3","*"):{"S":(0.8,2,4),"M":(2,4,8),"L":(4,8,16),"XL":(8,12,24)},
}

# once / per-environment layer. MODEL BRACKET = 87 elements -> M (31-90), where run 31 had L.
# Environment count = 3, unchanged -> E3 and E7 keep their environment-driven rows.
ONCE = [
 ("A1  test strategy            [bracket M]", (16,28,48)),
 ("U1d production verification  [single]",    (4,8,16)),
 ("D1  mobilisation             [bracket M]", (16,32,56)),
 ("D3  status reporting         [bracket M]", (16,32,64)),
 ("D6  risk & dependency mgmt   [bracket M]", (8,20,40)),
 ("E2  build/deploy pipeline    [bracket M]", (16,28,56)),
 ("E3  promotion procedure      [3 envs: L]", (8,16,32)),
 ("E4  configuration management [bracket M]", (8,12,24)),
 ("E6  production cutover       [bracket M]", (16,28,56)),
 ("E7  hosting set-up           [3 envs: L]", (24,44,80)),
 ("O2  operational runbook      [bracket M]", (12,24,40)),
 ("O3  support handover pack    [bracket M]", (8,20,36)),
 ("O4  release notes            [single]",    (2,4,8)),
 ("E1  environment: dev         [S]",         (4,8,20)),
 ("E1  environment: stage       [M]",         (8,16,32)),
 ("E1  environment: prod        [L]",         (16,28,56)),
]

# demanded-work branches - IDENTICAL to run 31. Same four obligations stand alone (F48, F49, F50,
# F52), F51 absorbed at E6. The addendum rows are rate rows, independent of which model was built,
# so not one of them changes.
DEMANDED = [
 ("W-F48.1 domain immersion, per area       x4", (18,30,72),  4),
 ("W-F48.2 candidate mechanism spike        x2", (18,42,96),  2),
 ("W-F48.3 architecture selection & record  x1", (12,24,54),  1),
 ("W-F49.1 live-stream tap facility         x2", (18,42,96),  2),
 ("W-F49.2 parallel-run env + isolation     x1", (18,42,90),  1),
 ("W-F49.3a first execution cycle           x1", (24,48,108), 1),
 ("W-F49.3b regression cycle                x1", (12,24,54),  1),
 ("W-F50.1 build the comparator             x1", (24,48,108), 1),
 ("W-F50.2 comparison run                   x4", (3,6,18),    4),
 ("W-F50.3 adjudicate differences, per type x2", (12,36,120), 2),
 ("W-F52   decommission-readiness           x1", (18,42,90),  1),
]

C3_RATE = 0.20

def E(c):
    o, m, p = c
    return (o + 4*m + p) / 6.0

def band(n, c):
    return "S" if n <= c[0] else "M" if n <= c[1] else "L" if n <= c[2] else "XL"

def sub(e):
    out = [e]
    for c in KIDS.get(e, []):
        out += sub(c)
    return out

def key(act, cls, kind):
    if act == "K1":
        return ("K1", "int") if cls == "interface" else ("K1", "bss")
    if act == "K2":
        if cls == "interface": return ("K2", "int")
        if cls == "store":     return ("K2", "sto")
        return ("K2", "bs")
    if act == "K3":
        return ("K3", kind)
    return (act, "*")

def assemble(sizes, kind, gs):
    leafE, holes = {}, []
    for e, items in OWN.items():
        cls = CLS[e]
        for act in items:
            if act == "D4":
                s = band(COV.get(e, 0), (1, 3, 6))
            elif act in ("G1", "G2", "G3"):
                s = gs.get(e)
            else:
                s = sizes.get(e)
            if s is None:
                holes.append((e, act, "unsizeable - model defect (M10)")); continue
            cell = T[key(act, cls, kind.get(e))].get(s)
            if cell is None:
                holes.append((e, act, "refused cell %s" % s)); continue
            leafE[e] = leafE.get(e, 0.0) + E(cell)
    for par, items in PARENT.items():
        st = sub(par)
        leaves = [x for x in st if x not in KIDS]
        si   = sum(1 for x in st if CLS[x] in ("store", "interface"))
        surf = sum(1 for x in st if CLS[x] == "surface")
        for act, cnt in items:
            if act == "A8":
                s = band(si, (1, 3, 6))
            elif act == "O1":
                if surf == 0: continue
                s = band(surf, (1, 3, 6))
            else:
                s = band(len(leaves), (3, 8, 14))
            leafE[par] = leafE.get(par, 0.0) + E(T[(act, "*")][s]) * cnt
    c3   = {p: C3_RATE * sum(leafE.get(x, 0.0) for x in sub(p)) for p in PARENT}
    once = sum(E(c) for _, c in ONCE)
    dem  = sum(E(c) * n for _, c, n in DEMANDED)
    tl, tc3 = sum(leafE.values()), sum(c3.values())
    return leafE, c3, once, dem, holes, tl, tc3, tl + tc3 + once + dem


if __name__ == "__main__":
    d = json.load(open(os.path.join(HERE, "hd42_sizes.json")))
    sizes, kind, gs = d["sizes"], d["kind"], d["gs"]
    leafE, c3, once, dem, holes, tl, tc3, total = assemble(sizes, kind, gs)
    print("=== HM29-OA2, priced with the run-31 rate table, nothing changed ===")
    print("  element leaf E (incl. root own items): %.2f" % tl)
    print("  C3 all parents:                        %.2f   of which root C3: %.2f" % (tc3, c3["HM2-01"]))
    print("  once + per-environment layer:          %.2f   [model bracket M, 87 elements]" % once)
    print("  demanded-work branches:                %.2f" % dem)
    print("  GRAND TOTAL:                           %.0f net person-hours  (= %.1f table pd at 8 h)"
          % (total, total / 8.0))
    print("  named holes (%d items on %d elements): %s"
          % (len(holes), len(set(h[0] for h in holes)), sorted(set(h[0] for h in holes))))
    print("  root own per-parent items: %.2f | once layer as %% of element leaf: %.1f%%"
          % (leafE.get("HM2-01", 0.0), once / tl * 100))
    OA1_LO, OA1_HI, OA1_MID = 1400.4, 1446.0, 1423.2
    pd = total / 8.0
    print()
    print("=== END-TO-END REPEATABILITY, the measurement run 42 exists for ===")
    print("  HM29-OA1 (97 nodes), run 31 repeats : %.1f / %.1f table pd, centre %.1f" % (OA1_HI, OA1_LO, OA1_MID))
    print("  HM29-OA2 (87 nodes), this run       : %.1f table pd" % pd)
    hi, lo = max(pd, OA1_MID), min(pd, OA1_MID)
    print("  ratio against the OA1 centre        : x%.4f" % (hi / lo))
    print("  against the whole OA1 range         : x%.4f .. x%.4f"
          % (min(pd, OA1_LO) and max(pd, OA1_LO) / min(pd, OA1_LO), max(pd, OA1_HI) / min(pd, OA1_HI)))
    print()
    print("  pre-registered comparators (BACKLOG.md, set before this ran):")
    print("    beat the no-method baseline on equal terms : under x1.168")
    print("    pass gate v2.0 test 1                      : under x1.30")
