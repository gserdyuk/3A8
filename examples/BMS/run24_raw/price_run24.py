# run 24 - price batches A and C from sensor size classes x rate table v0.1
# Data transcribed from docs/rate_table.md, run21_raw/HW21-A1.md, HW21-C1.md, run19_raw/HM19-OA1.md.
# Sensor inputs: the four SIZES_* dicts below, from run24_raw/HD24-{A1,A2,C1,C2}.md.
# Conventions, stated: subtree = the element itself plus all descendants (rooted); C3 base = leaf-item
# E of the rooted subtree (own items included), rate 20%, never compounding on other C3 items.

STD6 = [("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("D4",1)]
P7 = [("A5",2),("A6",2),("A7",1),("A8",1),("D2",1)]
PUAT = [("U1",1),("U2",2),("U3",2),("O1",1)]

# ---------------- batch A ----------------
EL_A = {
 "N02":("aggregate","root",[]), "N69":("statement","N02",["R01"]), "N04":("statement","N02",["R12","R66"]),
 "N05":("statement","N02",["R13","R68"]), "N06":("statement","N02",["R63"]), "N70":("statement","N02",["R72","R73"]),
 "N08":("statement","N02",["R71"]), "N09":("aggregate","root",[]), "N86":("store","N09",["R11","R54","R65"]),
 "N11":("behaviour","N09",["R11","R19"]), "N12":("behaviour","N09",["R11","R28","R65"]),
 "N13":("aggregate","root",[]), "N14":("interface","N13",["R08","R52"]), "N15":("behaviour","N13",["R65"]),
 "N79":("behaviour","N13",[]), "N26":("aggregate","root",[]), "N27":("store","N26",["R04"]),
 "N28":("store","N26",["R21"]), "N74":("interface","N28",["R31","R32"]), "N75":("behaviour","N74",["R32"]),
 "N77":("behaviour","N74",["R33","R34","R44"]), "N29":("store","N26",["R37","R47"]),
 "N80":("store","N26",[]), "N81":("store","N26",[]), "N82":("store","N26",[]),
}
OWN_A = {
 "N69":[("K3",1),("D4",1)], "N04":[("K3",1),("A9",1),("D4",1)], "N05":[("K3",1),("A9",1),("D4",1)],
 "N06":[("K3",1),("A9",1),("D4",1)], "N70":[("K3",1),("D4",1)], "N08":[("K3",1),("D4",1)],
 "N86":STD6+[("G1",1),("G2",1),("G3",1)], "N11":STD6, "N12":STD6,
 "N14":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("A10",1),("D4",1)], "N15":STD6,
 "N79":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1)], "N27":STD6, "N28":STD6,
 "N74":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("A10",1),("D4",1)], "N75":STD6, "N77":STD6,
 "N29":STD6, "N80":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("G1",1),("G2",1),("G3",1)],
 "N81":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("G1",1),("G2",1),("G3",1)],
 "N82":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1)],
}
PARENT_A = {p: list(P7) for p in ["N02","N09","N13","N26","N28","N74"]}

SIZES_A1 = {"N69":"M","N04":"M","N05":"M","N06":"S","N70":"M","N08":"S","N86":"XL","N11":"M","N12":"M",
 "N14":"M","N15":"M","N79":"M","N27":"M","N28":"S","N74":"M","N75":"L","N77":"L","N29":"L","N80":"S","N81":"S",
 # N82 unsizeable (M10) -> holes
 "kind":{"N69":"behavioural","N04":"behavioural","N05":"behavioural","N06":"behavioural","N70":"compliance","N08":"compliance"},
 "A9":{"N04":"S","N05":None,"N06":None},  # None = zero stated targets, below band -> named hole
 "G":{"N86":"L","N80":"S","N81":"S"}}
SIZES_A2 = {"N69":"M","N04":"M","N05":"M","N06":"S","N70":"M","N08":"S","N86":"L","N11":"M","N12":"M",
 "N14":"M","N15":"M","N79":"M","N27":"M","N28":"S","N74":"M","N75":"L","N77":"L","N29":"M","N80":"S","N81":"S",
 "N82":"M",
 "kind":{"N69":"compliance","N04":"behavioural","N05":"behavioural","N06":"compliance","N70":"compliance","N08":"compliance"},
 "A9":{"N04":"S","N05":None,"N06":None},
 "G":{"N86":"L","N80":"S","N81":"S"}}

# ---------------- batch C ----------------
EL_C = {
 "N45":("aggregate","root",[]), "N46":("behaviour","N45",["R36","R46"]), "N47":("surface","N45",["R37","R47"]),
 "N48":("surface","N45",["R05","R38","R48"]), "N49":("aggregate","root",[]), "N50":("surface","N49",["R05","R49"]),
 "N51":("behaviour","N49",["R50"]), "N52":("surface","N49",["R51"]), "N53":("behaviour","N49",["R22","R42"]),
 "N54":("behaviour","N49",["R53"]), "N55":("surface","root",["R57"]), "N56":("surface","N55",["R54","R57"]),
 "N57":("behaviour","N55",["R20"]), "N58":("behaviour","N55",["R23","R43"]), "N59":("surface","N55",["R05","R55"]),
 "N60":("surface","root",["R56","R67"]), "N61":("surface","N60",["R58"]), "N62":("surface","N60",["R59"]),
 "N63":("surface","N60",["R60"]), "N87":("store","N60",[]), "N64":("aggregate","root",[]),
 "N65":("surface","N64",["R14"]), "N66":("surface","N64",["R14"]), "N67":("surface","N64",["R14"]),
 "N68":("statement","root",["R10"]),
}
OWN_C = {n:list(STD6) for n in ["N46","N47","N48","N50","N51","N52","N53","N54","N55","N56","N57","N58",
                                "N59","N60","N61","N62","N63","N65","N66","N67"]}
OWN_C["N87"] = [("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("G1",1),("G2",1),("G3",1)]
OWN_C["N68"] = [("K3",1),("D4",1)]
PARENT_C = {p: P7+PUAT for p in ["N45","N49","N55","N60","N64"]}

_SC = {"N46":"M","N47":"M","N48":"M","N50":"M","N51":"M","N52":"M","N53":"M","N54":"M","N55":"M","N56":"M",
 "N57":"S","N58":"M","N59":"M","N60":"S","N61":"S","N62":"S","N63":"S","N87":"M","N65":"S","N66":"S","N67":"S",
 # N68 unsizeable (M10) -> K3 hole; its D4 is computed
 "kind":{"N68":"compliance"}, "A9":{}, "G":{"N87":"S"}}
SIZES_C1 = dict(_SC); SIZES_C2 = dict(_SC)  # identical outcomes, both repeats

# ---------------- rate table v0.1 (E-relevant cells) ----------------
T = {
 ("K1","bss"):{"S":(0.25,0.5,1),"M":(0.5,1,2),"L":(1,2,3.5),"XL":(2,3.5,6)},
 ("K1","int"):{"S":(0.5,1,2),"M":(1,2,4),"L":(2,3.5,6),"XL":(3,5,9)},
 ("K2","bs"):{"S":(0.5,1,2),"M":(1,2.5,5),"L":(2.5,5,9),"XL":(5,8,14)},
 ("K2","int"):{"S":(1,2,4),"M":(2,3.5,7),"L":(3,6,10),"XL":(5,9,15)},
 ("K2","sto"):{"S":(0.5,1,2),"M":(1,2,3.5),"L":(2,4,7),"XL":(3.5,6.5,11)},
 ("K3","compliance"):{"S":(0.25,0.5,1.5),"M":(0.5,1.5,3),"L":(1,2.5,5),"XL":(2,4,8)},
 ("K3","behavioural"):{"S":(1,2,4),"M":(2,4,8),"L":(3,6,12),"XL":None},
 ("A2","*"):{"S":(0.25,0.5,1),"M":(0.5,1,2),"L":(1,2,3.5),"XL":(1.5,3,5)},
 ("A3","*"):{"S":(0.5,1,2),"M":(1,2,4),"L":(2,3.5,6),"XL":(3,5.5,9)},
 ("A4","*"):{"S":(0.1,0.25,0.5),"M":(0.25,0.5,1),"L":(0.5,1,2),"XL":(0.75,1.5,3)},
 ("A9","*"):{"S":(1,2,4),"M":(2,3.5,7),"L":(3,5.5,10),"XL":(4,8,14)},
 ("A10","*"):{"S":(0.5,1,2.5),"M":(1,2,4),"L":(2,3.5,7),"XL":(3,5,10)},
 ("A5","*"):{"S":(0.5,1,2),"M":(1,2,4),"L":(2,3.5,6),"XL":(3,5,9)},
 ("A6","*"):{"S":(0.5,1.5,4),"M":(1,3,7),"L":(2,5,10),"XL":(3,7,14)},
 ("A7","*"):{"S":(1,2,4),"M":(2,4,7),"L":(3,6,10),"XL":(4,8,14)},
 ("A8","*"):{"S":(0.25,0.5,1.5),"M":(0.5,1.5,3),"L":(1,2.5,5),"XL":(2,4,8)},
 ("D2","*"):{"S":(0.5,1,2),"M":(1,2,4),"L":(2,3.5,6),"XL":(3,5,8)},
 ("D4","*"):{"S":(0.25,0.5,1),"M":(0.5,1,2),"L":(1,2,4),"XL":(1.5,3,6)},
 ("U1","*"):{"S":(0.5,1,2),"M":(1,2,4),"L":(2,3.5,6),"XL":(3,5,9)},
 ("U2","*"):{"S":(0.5,1,2.5),"M":(1,2,4),"L":(1.5,3,6),"XL":(2.5,4.5,8)},
 ("U3","*"):{"S":(0.5,1.5,4),"M":(1,2.5,6),"L":(1.5,4,8),"XL":(2.5,6,12)},
 ("O1","*"):{"S":(0.5,1,2),"M":(1,2,4),"L":(2,3.5,6),"XL":(3,5,9)},
 ("G1","*"):{"S":(0.25,0.5,1),"M":(0.5,1,2),"L":(1,2,3.5),"XL":(1.5,3,5)},
 ("G2","*"):{"S":(0.25,0.5,1.5),"M":(0.5,1.5,3),"L":(1,2.5,5),"XL":(2,4,7)},
 ("G3","*"):{"S":(0.1,0.25,0.5),"M":(0.25,0.5,1),"L":(0.5,1,2),"XL":(1,1.5,3)},
}
C3_RATE = 0.20

def band(n, cuts): return "S" if n<=cuts[0] else "M" if n<=cuts[1] else "L" if n<=cuts[2] else "XL"

def build(EL):
    kids = {e:[] for e in EL}
    for e,(_,p,_) in EL.items():
        if p in kids: kids[p].append(e)
    def sub(e):  # rooted subtree
        out=[e]
        for c in kids[e]: out+=sub(c)
        return out
    return kids, sub

def key(act, cls, kind):
    if act=="K1": return ("K1","int") if cls=="interface" else ("K1","bss")
    if act=="K2": return ("K2","int") if cls=="interface" else ("K2","sto") if cls=="store" else ("K2","bs")
    if act=="K3": return ("K3",kind)
    return (act,"*")

def price(EL, OWN, PARENT, sizes):
    kids, sub = build(EL)
    leafE, holes, rows = {}, [], []
    for e, items in OWN.items():
        cls, _, cov = EL[e]
        for act, cnt in items:
            if act=="D4": s = band(len(cov),(1,3,6))
            elif act=="A9":
                s = sizes["A9"].get(e)
                if s is None: holes.append((e,"A9","zero targets, below band")); continue
            elif act in ("G1","G2","G3"): s = sizes["G"][e]
            else:
                s = sizes.get(e)
                if s is None: holes.append((e,act,"unsizeable")); continue
            cell = T[key(act,cls,sizes["kind"].get(e))].get(s)
            if cell is None: holes.append((e,act,f"refused cell {s}")); continue
            o,m,p = cell; ev=(o+4*m+p)/6.0
            leafE[e]=leafE.get(e,0.0)+ev*cnt; rows.append((e,act,s,ev,cnt))
    for par, items in PARENT.items():
        st = sub(par)
        leaves=[x for x in st if not kids[x]]
        si=sum(1 for x in st if EL[x][0] in ("store","interface"))
        surf=sum(1 for x in st if EL[x][0]=="surface")
        for act,cnt in items:
            if act=="A8": s=band(si,(1,3,6))
            elif act in ("U1","U2","U3","O1"): s=band(surf,(1,3,6))
            else: s=band(len(leaves),(3,8,14))
            o,m,p = T[(act,"*")][s]; ev=(o+4*m+p)/6.0
            leafE[par]=leafE.get(par,0.0)+ev*cnt; rows.append((par,act,s,ev,cnt))
    c3 = {p: C3_RATE*sum(leafE.get(x,0.0) for x in sub(p)) for p in PARENT}
    proj={}
    for e,(_,_,cov) in EL.items():
        for r in cov: proj[r]=proj.get(r,0.0)+leafE.get(e,0.0)
    return {"leafE":leafE,"c3":c3,"holes":holes,
            "tot_leaf":sum(leafE.values()),"tot_c3":sum(c3.values()),
            "total":sum(leafE.values())+sum(c3.values()),"proj":proj}

def report(name, EL, OWN, PARENT, s1, s2):
    n_items = sum(c for it in OWN.values() for _,c in it)+sum(c for it in PARENT.values() for _,c in it)
    r1, r2 = price(EL,OWN,PARENT,s1), price(EL,OWN,PARENT,s2)
    print(f"=== batch {name}: {n_items} items ===")
    for lbl,r in (("r1",r1),("r2",r2)):
        print(f" {lbl}: leaf {r['tot_leaf']:.2f}  C3 {r['tot_c3']:.2f}  TOTAL {r['total']:.2f}  holes {len(r['holes'])}: {r['holes']}")
    hi,lo=max(r1["total"],r2["total"]),min(r1["total"],r2["total"])
    print(f" Sigma-E ratio: x{hi/lo:.4f}")
    diffs=[e for e in EL if EL[e][0]!="aggregate" and (s1.get(e),s1["kind"].get(e))!=(s2.get(e),s2["kind"].get(e))]
    print(f" element outcome differences: {diffs}")
    per=[]
    for r in sorted(set(r1["proj"])|set(r2["proj"])):
        a,b=r1["proj"].get(r,0.0),r2["proj"].get(r,0.0)
        rat=max(a,b)/min(a,b) if min(a,b)>0 else float("inf")
        per.append((r,a,b,rat))
    moved=[(r,a,b,rat) for r,a,b,rat in per if abs(rat-1)>1e-9]
    print(f" projection rows: {len(per)}, identical {len(per)-len(moved)}, moved: ")
    for r,a,b,rat in moved: print(f"   {r}: {a:8.2f} {b:8.2f}  x{rat:.3f}")
    return r1,r2

if __name__=="__main__":
    ra1,ra2 = report("A", EL_A, OWN_A, PARENT_A, SIZES_A1, SIZES_A2)
    rc1,rc2 = report("C", EL_C, OWN_C, PARENT_C, SIZES_C1, SIZES_C2)
    print("=== all three batches, run/run totals (batch B from run 23: 347.70 / 353.31) ===")
    t1 = ra1["total"]+rc1["total"]+347.70
    t2 = ra2["total"]+rc2["total"]+353.31
    print(f" r1 {t1:.2f}   r2 {t2:.2f}   ratio x{max(t1,t2)/min(t1,t2):.4f}")
