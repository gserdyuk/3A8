# run 31 - FaxRxTx whole-model assembly
#
# Inputs, all pinned before this script was written:
#   product model    HM29-OA1  (Hotyn-M 1.1, 97 nodes, 18 aggregates, 79 leaves)
#   work model       HW30-A1/B1/C1  (Hotyn-W 1.1, three partial crossings, 570 crossing items
#                                    + 4 demanded-work branches)
#   size classes     HD31-A1/B1/C1 (repeat 1) and HD31-A2/B2/C2 (repeat 2), Hotyn-D 2.0
#   rates            docs/rate_table.md v0.1 + addendum A1; FaxRxTx addenda A2/A3 for the
#                    demanded-work branches (gap-blind Hotyn-K 1.0)
#   declaration      examples/FaxRxTx/technology_declaration.md
#
# Conventions, identical to the BMS assembly of 2026-08-22 (examples/BMS/run25_raw/assemble.py):
#   subtree = rooted (element + descendants)
#   C3 base = leaf-item E of the rooted subtree, element-attached items only; once-scoped,
#             per-environment and demanded items enter no C3 base; rate 20%, never compounding
#   E(O,M,P) = (O + 4M + P) / 6
#
# The two repeats are priced as two variants. Their ratio is the measurement.

# ---------------------------------------------------------------- tree
KIDS = {
 "HM1-01": ["HM1-02","HM1-03","HM1-04","HM1-05","HM1-06","HM1-07","HM1-08","HM1-09","HM1-10","HM1-11","HM1-12","HM1-13"],
 "HM1-02": ["HM1-23","HM1-25","HM1-26","HM1-27","HM1-28","HM1-86"],
 "HM1-03": ["HM1-24","HM1-35","HM1-36","HM1-39","HM1-88","HM1-89"],
 "HM1-04": ["HM1-29","HM1-30","HM1-31","HM1-37","HM1-38","HM1-90","HM1-97","HM1-17"],
 "HM1-17": ["HM1-41","HM1-42","HM1-43","HM1-44","HM1-45","HM1-46","HM1-47","HM1-48","HM1-49"],
 "HM1-05": ["HM1-32","HM1-33","HM1-34","HM1-50","HM1-75","HM1-94"],
 "HM1-06": ["HM1-53","HM1-54","HM1-55","HM1-56","HM1-57","HM1-58","HM1-82","HM1-83","HM1-85","HM1-92"],
 "HM1-07": ["HM1-59","HM1-60","HM1-61","HM1-87","HM1-93"],
 "HM1-08": ["HM1-18","HM1-19","HM1-95"],
 "HM1-18": ["HM1-65","HM1-66","HM1-67","HM1-68"],
 "HM1-19": ["HM1-51","HM1-52"],
 "HM1-09": ["HM1-69","HM1-70","HM1-71","HM1-96"],
 "HM1-10": ["HM1-14","HM1-15","HM1-40"],
 "HM1-14": ["HM1-20","HM1-21","HM1-22","HM1-74","HM1-91"],
 "HM1-15": ["HM1-78","HM1-79","HM1-98"],
 "HM1-11": ["HM1-76","HM1-77"],
 "HM1-12": ["HM1-64","HM1-72","HM1-73","HM1-80","HM1-81","HM1-84"],
 "HM1-13": ["HM1-62","HM1-63"],
}

# ---------------------------------------------------------------- classes (Hotyn-W 1.1)
CLS = {}
for e in ["HM1-23","HM1-24","HM1-25","HM1-31","HM1-38","HM1-39","HM1-90",
          "HM1-21","HM1-22","HM1-91","HM1-78","HM1-40"]:
    CLS[e] = "interface"
for e in ["HM1-26","HM1-27","HM1-28","HM1-86","HM1-35","HM1-36","HM1-88","HM1-89","HM1-29",
          "HM1-30","HM1-37","HM1-97","HM1-41","HM1-42","HM1-43","HM1-44","HM1-45","HM1-46",
          "HM1-47","HM1-48","HM1-49",
          "HM1-32","HM1-33","HM1-34","HM1-50","HM1-53","HM1-55","HM1-56","HM1-57","HM1-58",
          "HM1-82","HM1-83","HM1-85","HM1-92","HM1-93",
          "HM1-52","HM1-95","HM1-96","HM1-74","HM1-79","HM1-98","HM1-62"]:
    CLS[e] = "behaviour"
for e in ["HM1-54","HM1-59","HM1-60","HM1-61","HM1-87","HM1-20","HM1-76","HM1-77","HM1-63"]:
    CLS[e] = "store"
for e in ["HM1-75","HM1-94","HM1-64","HM1-72","HM1-73","HM1-80","HM1-81","HM1-84"]:
    CLS[e] = "statement"
for e in ["HM1-65","HM1-66","HM1-67","HM1-68","HM1-51","HM1-69","HM1-70","HM1-71"]:
    CLS[e] = "surface"
for a in KIDS:
    CLS[a] = "aggregate"

# ---------------------------------------------------------------- own coverage (for D4 sizing)
COV = {
 "HM1-23":3,"HM1-25":1,"HM1-26":1,"HM1-27":1,"HM1-28":1,
 "HM1-24":1,"HM1-35":1,"HM1-36":1,"HM1-39":1,
 "HM1-29":3,"HM1-30":2,"HM1-31":1,"HM1-37":1,"HM1-38":1,
 "HM1-41":1,"HM1-42":1,"HM1-43":1,"HM1-44":1,"HM1-45":1,"HM1-46":1,"HM1-47":1,
 "HM1-48":1,"HM1-49":1,
 "HM1-32":1,"HM1-33":1,"HM1-34":1,"HM1-50":2,"HM1-75":1,
 "HM1-53":2,"HM1-54":3,"HM1-55":2,"HM1-56":2,"HM1-57":1,"HM1-58":2,"HM1-82":1,"HM1-83":1,
 "HM1-59":1,"HM1-60":1,"HM1-61":1,
 "HM1-65":1,"HM1-66":1,"HM1-67":1,"HM1-68":1,"HM1-51":3,"HM1-52":1,
 "HM1-69":1,"HM1-70":1,"HM1-71":1,
 "HM1-20":2,"HM1-21":2,"HM1-22":2,"HM1-74":1,"HM1-78":1,"HM1-79":1,"HM1-40":1,
 "HM1-76":1,"HM1-77":1,
 "HM1-64":1,"HM1-72":1,"HM1-73":1,"HM1-80":1,"HM1-81":1,"HM1-84":1,
 "HM1-62":1,"HM1-63":1,
}

# ---------------------------------------------------------------- own item sets (HW30 crossings)
STD_BEH = ["K1","K2","A2","A3","A4"]            # behaviour/surface/store construction+assurance
OWN = {}
def own(els, items):
    for e in els: OWN[e] = list(items)

# batch A
own(["HM1-23","HM1-24","HM1-25","HM1-31","HM1-38","HM1-39"], STD_BEH+["A10","D4"])
own(["HM1-90"], STD_BEH+["A10"])
own(["HM1-26","HM1-27","HM1-28","HM1-35","HM1-36","HM1-29","HM1-30","HM1-37",
     "HM1-41","HM1-42","HM1-43","HM1-44","HM1-45","HM1-46","HM1-47","HM1-48","HM1-49"], STD_BEH+["D4"])
own(["HM1-86","HM1-88","HM1-89","HM1-97"], STD_BEH)
# batch B
own(["HM1-32","HM1-33","HM1-34","HM1-50","HM1-53","HM1-55","HM1-56","HM1-57","HM1-58",
     "HM1-82","HM1-83","HM1-54","HM1-59","HM1-60"], STD_BEH+["D4"])
own(["HM1-85","HM1-92","HM1-93"], STD_BEH)
own(["HM1-61"], STD_BEH+["D4","G1","G2","G3"])
own(["HM1-87"], STD_BEH+["G1","G2","G3"])
own(["HM1-75"], ["K3","D4"])
own(["HM1-94"], ["K3"])
# batch C
own(["HM1-65","HM1-66","HM1-67","HM1-68","HM1-51","HM1-69","HM1-70","HM1-71",
     "HM1-52","HM1-74","HM1-79","HM1-62","HM1-76","HM1-77"], STD_BEH+["D4"])
own(["HM1-95","HM1-96","HM1-98"], STD_BEH)
own(["HM1-21","HM1-22","HM1-78","HM1-40"], STD_BEH+["A10","D4"])
own(["HM1-91"], STD_BEH+["A10"])
own(["HM1-20","HM1-63"], STD_BEH+["D4","G1","G2","G3"])
own(["HM1-64"], ["K3"])                       # D4 refused by judgement in HW30-C1
own(["HM1-80","HM1-81","HM1-84"], ["K3","D4"])
own(["HM1-72","HM1-73"], ["K3","D4","A9"])

# ---------------------------------------------------------------- per-parent item sets
P7   = [("A5",2),("A6",2),("A7",1),("A8",1),("D2",1)]
PARENT = {p: list(P7) for p in ["HM1-02","HM1-03","HM1-04","HM1-17",
                                "HM1-05","HM1-06","HM1-07",
                                "HM1-08","HM1-18","HM1-19","HM1-09","HM1-10","HM1-14",
                                "HM1-15","HM1-11","HM1-13"]}
PARENT["HM1-12"] = [("D2",1)]                     # A5/A6/A7/A8 refused by judgement (HW30-C1)
for p in ["HM1-08","HM1-18","HM1-19","HM1-09"]:   # O1 gated on a surface in the subtree
    PARENT[p].append(("O1",1))
PARENT["HM1-01"] = P7 + [("O1",1)]                # the root, computed here: not in any batch

# ---------------------------------------------------------------- sizes, two repeats
V1 = {
 "HM1-23":"M","HM1-25":"M","HM1-24":"M","HM1-31":"M","HM1-38":"M","HM1-39":"M","HM1-90":"M",
 "HM1-26":"M","HM1-27":"M","HM1-28":"S","HM1-86":"M","HM1-35":"M","HM1-36":"S","HM1-88":"M",
 "HM1-89":"M","HM1-29":"M","HM1-30":"M","HM1-37":"S","HM1-97":"L",
 "HM1-41":"S","HM1-42":"S","HM1-43":"S","HM1-44":"S","HM1-45":"S","HM1-46":"S","HM1-47":"S",
 "HM1-48":"M","HM1-49":"M",
 "HM1-32":"S","HM1-33":"S","HM1-34":"S","HM1-50":"M","HM1-53":"S","HM1-55":"M","HM1-56":"M",
 "HM1-57":"S","HM1-58":"L","HM1-82":"M","HM1-83":None,"HM1-85":"S","HM1-92":"S","HM1-93":"S",
 "HM1-54":"S","HM1-59":"S","HM1-60":"S","HM1-61":None,"HM1-87":"S","HM1-75":None,"HM1-94":"M",
 "HM1-65":"S","HM1-66":"S","HM1-67":"S","HM1-68":"S","HM1-51":"L","HM1-52":"M","HM1-95":"M",
 "HM1-69":"M","HM1-70":"M","HM1-71":"M","HM1-96":"S","HM1-21":"M","HM1-22":"M","HM1-91":"S",
 "HM1-40":"M","HM1-74":"M","HM1-79":"M","HM1-98":"S","HM1-62":"S","HM1-20":"M","HM1-76":"S",
 "HM1-77":"S","HM1-63":"S","HM1-64":"S","HM1-72":"S","HM1-73":"M","HM1-80":"M","HM1-81":"M",
 "HM1-84":None,"HM1-78":None,
}
V2 = dict(V1)
V2.update({"HM1-31":"S","HM1-38":"S","HM1-35":"S","HM1-29":"S","HM1-37":"M",     # batch A
           "HM1-57":None,"HM1-75":"M",                                            # batch B
           "HM1-69":"S","HM1-70":"S","HM1-40":"S"})                               # batch C

KIND = {"HM1-75":"compliance","HM1-94":"behavioural","HM1-64":"compliance",
        "HM1-72":"behavioural","HM1-73":"behavioural","HM1-80":"behavioural",
        "HM1-81":"behavioural","HM1-84":None}

A9S = {"v1":{"HM1-72":"M","HM1-73":"S"}, "v2":{"HM1-72":"S","HM1-73":"S"}}
GS  = {"HM1-61":None,"HM1-87":"S","HM1-20":"M","HM1-63":None}   # identical in both repeats

# ---------------------------------------------------------------- rate table v0.1 (+A1)
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

# once / per-environment layer. Model bracket = 97 elements -> L (>=91).
# Environment count = 3 -> E3 and E7 take their L rows. SA-NONE contributes nothing;
# C-DIRECT contributes U1d only. No U1/U2/U3/U4 (no acceptance stage is declared).
ONCE = [
 ("A1  test strategy            [bracket L]", (24,40,72)),
 ("U1d production verification  [single]",    (4,8,16)),
 ("D1  mobilisation             [bracket L]", (24,48,80)),
 ("D3  status reporting         [bracket L]", (32,64,112)),
 ("D6  risk & dependency mgmt   [bracket L]", (16,32,64)),
 ("E2  build/deploy pipeline    [bracket L]", (24,44,80)),
 ("E3  promotion procedure      [3 envs: L]", (8,16,32)),
 ("E4  configuration management [bracket L]", (12,20,40)),
 ("E6  production cutover       [bracket L]", (24,40,80)),
 ("E7  hosting set-up           [3 envs: L]", (24,44,80)),
 ("O2  operational runbook      [bracket L]", (20,36,64)),
 ("O3  support handover pack    [bracket L]", (16,32,56)),
 ("O4  release notes            [single]",    (2,4,8)),
 ("E1  environment: dev         [S]",         (4,8,20)),
 ("E1  environment: stage       [M]",         (8,16,32)),
 ("E1  environment: prod        [L]",         (16,28,56)),
]

# demanded-work branches standing alone (FaxRxTx addenda A2/A3, gap-blind Hotyn-K 1.0).
# F51 is absorbed at E6 and is NOT listed here - it would be the same work twice.
# Each row prices ONE unit; the multiplicand is an orchestrator-declared parameter derived from
# the client's pinned statement, in the same class as "environment count = 3". Hotyn-K applied
# none of them and computed no total.
#   domain areas 4 · candidate mechanisms 2 · tap points 2 · test cycles 2 (= one 3a + one 3b)
#   message types 2 · comparison runs 4 (declared here: one run per cycle plus one re-run each
#   after a normalisation-rule change - Hotyn-K F-3 requires this be its own parameter)
# UNIT CONVERSION, applied 2026-08-25 (author's decision).
# Hotyn-K wrote the A2/A3 rows below in ASSIGNED WORKING DAYS (a day a person is present, ~6 net
# hours), on the orchestrator's instruction, and warned in A3 that they "may not be summed without a
# declared conversion" with base-table rows. The base table's unit is 1 pd = 8 NET HOURS.
# The eleven A2/A3 rows were authored in ASSIGNED WORKING DAYS and are stated below in net hours
# at the declared 6 net hours per assigned day (117.33 assigned-days = 704 net person-hours).
# RECORDED DEFECT: a converted value, not one derived in the operative unit. Re-derivation is
# owed and is parked with the outcome-comparison work; see docs/constants.md section 4.
DEMANDED = [
 ("W-F48.1 domain immersion, per area      x4", (18,30,72),  4),
 ("W-F48.2 candidate mechanism spike       x2", (18,42,96),  2),
 ("W-F48.3 architecture selection & record x1", (12,24,54),   1),
 ("W-F49.1 live-stream tap facility        x2", (18,42,96),  2),
 ("W-F49.2 parallel-run env + isolation    x1", (18,42,90),  1),
 ("W-F49.3a first execution cycle          x1", (24,48,108),  1),
 ("W-F49.3b regression cycle               x1", (12,24,54),   1),
 ("W-F50.1 build the comparator            x1", (24,48,108),  1),
 ("W-F50.2 comparison run                  x4", (3,6,18), 4),
 ("W-F50.3 adjudicate differences, per type x2",(12,36,120),  2),
 ("W-F52   decommission-readiness          x1", (18,42,90),  1),
]

C3_RATE = 0.20
def E(c): o,m,p = c; return (o + 4*m + p) / 6.0
def band(n, c): return "S" if n<=c[0] else "M" if n<=c[1] else "L" if n<=c[2] else "XL"

def sub(e):
    out = [e]
    for c in KIDS.get(e, []): out += sub(c)
    return out

def key(act, cls, kind):
    if act == "K1": return ("K1","int") if cls=="interface" else ("K1","bss")
    if act == "K2":
        return ("K2","int") if cls=="interface" else ("K2","sto") if cls=="store" else ("K2","bs")
    if act == "K3": return ("K3", kind)
    return (act, "*")

def assemble(vname, sizes):
    leafE, holes = {}, []
    for e, items in OWN.items():
        cls = CLS[e]
        for act in items:
            if act == "D4":       s = band(COV[e], (1,3,6))
            elif act == "A9":     s = A9S[vname].get(e)
            elif act in ("G1","G2","G3"): s = GS[e]
            else:                 s = sizes.get(e)
            if s is None:
                holes.append((e, act, "unsizeable - model defect (M10)")); continue
            k = key(act, cls, KIND.get(e))
            cell = T[k].get(s)
            if cell is None:
                holes.append((e, act, "refused cell %s" % s)); continue
            leafE[e] = leafE.get(e, 0.0) + E(cell)
    for par, items in PARENT.items():
        st = sub(par)
        leaves = [x for x in st if x not in KIDS]
        si   = sum(1 for x in st if CLS[x] in ("store","interface"))
        surf = sum(1 for x in st if CLS[x] == "surface")
        for act, cnt in items:
            if act == "A8":  s = band(si, (1,3,6))
            elif act == "O1":
                if surf == 0: continue
                s = band(surf, (1,3,6))
            else:            s = band(len(leaves), (3,8,14))
            leafE[par] = leafE.get(par, 0.0) + E(T[(act,"*")][s]) * cnt
    c3 = {p: C3_RATE * sum(leafE.get(x,0.0) for x in sub(p)) for p in PARENT}
    once = sum(E(c) for _,c in ONCE)
    dem  = sum(E(c)*n for _,c,n in DEMANDED)
    tl, tc3 = sum(leafE.values()), sum(c3.values())
    return leafE, c3, once, dem, holes, tl, tc3, tl + tc3 + once + dem

if __name__ == "__main__":
    res = {}
    for name, sizes in (("v1", V1), ("v2", V2)):
        leafE, c3, once, dem, holes, tl, tc3, total = assemble(name, sizes)
        res[name] = total
        print("=== variant %s (Hotyn-D repeat %s) ===" % (name, name[-1]))
        print("  element leaf E (incl. root own items): %.2f" % tl)
        print("  C3 all parents:                        %.2f   of which root C3: %.2f" % (tc3, c3["HM1-01"]))
        print("  once + per-environment layer:          %.2f" % once)
        print("  demanded-work branches:                %.2f" % dem)
        for lab,c,n in DEMANDED:
            print("       %-44s %6.2f" % (lab, E(c)*n))
        print("  GRAND TOTAL:                           %.0f net person-hours  (= %.1f person-days at 8 h)" % (total, total/8.0))
        print("  named holes (%d): %s" % (len(holes), sorted(set(h[0] for h in holes))))
        print("  root own per-parent items: %.2f · once layer as %% of element leaf: %.1f%%"
              % (leafE.get("HM1-01",0.0), once/tl*100))
    lo, hi = min(res.values()), max(res.values())
    print("=== repeat spread: %.0f .. %.0f net person-hours  (x%.4f) ===" % (lo, hi, hi/lo))
    print("=== unit: net hours of work on the task. Leave, holidays, sickness and presence are NOT")
    print("===       included and are not parameters of this method (docs/constants.md).")
