# run 25 - the whole-model assembly under case law 1.4, rate table v0.1 + addendum A1
# Canonical sizes: run 23/24 outcomes with precedents P-1..P-6 applied (see run25 write-up).
# The one un-adjudicated divergence, N86 XL vs L, is carried as the assembly's declared spread.
# Conventions: subtree = rooted (element + descendants); C3 base = leaf-item E of the rooted
# subtree, element-attached items only (once / per-environment / demanded items enter no C3 base);
# rate 20%, never compounding on C3 items.

STD6 = [("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("D4",1)]
P7   = [("A5",2),("A6",2),("A7",1),("A8",1),("D2",1)]
PUAT = [("U1",1),("U2",2),("U3",2),("O1",1)]

EL = {}  # id -> (class, parent, coverage)
OWN = {}; PARENT = {}

def add(el, own=None, parent_items=None):
    for k,v in el.items(): EL[k]=v
    if own:
        for k,v in own.items(): OWN[k]=v
    if parent_items:
        for k,v in parent_items.items(): PARENT[k]=v

# ---- batch B (N17/N18 reclassified to statement-behavioural; N16 loses its UAT/doc items) ----
add({
 "N16":("statement","N01",["R61","R66"]), "N17":("statement","N16",["R09","R61"]),
 "N18":("statement","N16",["R62"]), "N19":("aggregate","N01",[]),
 "N20":("interface","N19",["R06","R21","R31","R41"]), "N21":("interface","N19",["R07"]),
 "N22":("interface","N19",["R15"]), "N23":("interface","N19",["R39"]),
 "N24":("interface","N19",["R26"]), "N25":("interface","N19",["R27"]),
 "N84":("behaviour","N19",[]), "N30":("aggregate","N01",[]),
 "N85":("behaviour","N30",["R15","R16","R17"]), "N72":("behaviour","N30",["R18","R19","R24"]),
 "N33":("aggregate","N01",[]), "N34":("behaviour","N33",["R25"]),
 "N83":("behaviour","N33",["R26","R27"]), "N73":("behaviour","N33",["R29"]),
 "N36":("aggregate","N01",[]), "N37":("behaviour","N36",["R29"]),
 "N38":("surface","N36",["R30","R38"]), "N39":("behaviour","N36",["R35"]),
 "N40":("aggregate","N01",[]), "N41":("behaviour","N40",["R29","R39"]),
 "N42":("surface","N40",["R40","R48"]), "N43":("store","N40",["R41","R44"]),
 "N44":("behaviour","N40",["R45"]),
},
 own={"N16":[("K3",1),("A9",1),("D4",1)], "N17":[("K3",1),("D4",1)], "N18":[("K3",1),("D4",1)],
      "N84":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1)],
      "N43":STD6+[("G1",1),("G2",1),("G3",1)]},
 parent_items={"N16":list(P7), "N19":list(P7), "N30":list(P7), "N33":list(P7),
               "N36":P7+PUAT, "N40":P7+PUAT})
for n in ["N20","N21","N22","N23","N24","N25"]:
    OWN[n]=[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("A10",1),("D4",1)]
for n in ["N85","N72","N34","N83","N73","N37","N39","N41","N44","N38","N42"]:
    OWN[n]=list(STD6)

# ---- batch A ----
add({
 "N02":("aggregate","N01",[]), "N69":("statement","N02",["R01"]), "N04":("statement","N02",["R12","R66"]),
 "N05":("statement","N02",["R13","R68"]), "N06":("statement","N02",["R63"]),
 "N70":("statement","N02",["R72","R73"]), "N08":("statement","N02",["R71"]),
 "N09":("aggregate","N01",[]), "N86":("store","N09",["R11","R54","R65"]),
 "N11":("behaviour","N09",["R11","R19"]), "N12":("behaviour","N09",["R11","R28","R65"]),
 "N13":("aggregate","N01",[]), "N14":("interface","N13",["R08","R52"]), "N15":("behaviour","N13",["R65"]),
 "N79":("behaviour","N13",[]), "N26":("aggregate","N01",[]), "N27":("store","N26",["R04"]),
 "N28":("store","N26",["R21"]), "N74":("interface","N28",["R31","R32"]), "N75":("behaviour","N74",["R32"]),
 "N77":("behaviour","N74",["R33","R34","R44"]), "N29":("store","N26",["R37","R47"]),
 "N80":("store","N26",[]), "N81":("store","N26",[]), "N82":("store","N26",[]),
},
 own={"N69":[("K3",1),("D4",1)], "N04":[("K3",1),("A9",1),("D4",1)], "N05":[("K3",1),("A9",1),("D4",1)],
      "N06":[("K3",1),("A9",1),("D4",1)], "N70":[("K3",1),("D4",1)], "N08":[("K3",1),("D4",1)],
      "N86":STD6+[("G1",1),("G2",1),("G3",1)], "N11":list(STD6), "N12":list(STD6),
      "N14":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("A10",1),("D4",1)], "N15":list(STD6),
      "N79":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1)], "N27":list(STD6), "N28":list(STD6),
      "N74":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("A10",1),("D4",1)],
      "N75":list(STD6), "N77":list(STD6), "N29":list(STD6),
      "N80":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("G1",1),("G2",1),("G3",1)],
      "N81":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("G1",1),("G2",1),("G3",1)],
      "N82":[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1)]},
 parent_items={p:list(P7) for p in ["N02","N09","N13","N26","N28","N74"]})

# ---- batch C ----
add({
 "N45":("aggregate","N01",[]), "N46":("behaviour","N45",["R36","R46"]), "N47":("surface","N45",["R37","R47"]),
 "N48":("surface","N45",["R05","R38","R48"]), "N49":("aggregate","N01",[]), "N50":("surface","N49",["R05","R49"]),
 "N51":("behaviour","N49",["R50"]), "N52":("surface","N49",["R51"]), "N53":("behaviour","N49",["R22","R42"]),
 "N54":("behaviour","N49",["R53"]), "N55":("surface","N01",["R57"]), "N56":("surface","N55",["R54","R57"]),
 "N57":("behaviour","N55",["R20"]), "N58":("behaviour","N55",["R23","R43"]), "N59":("surface","N55",["R05","R55"]),
 "N60":("surface","N01",["R56","R67"]), "N61":("surface","N60",["R58"]), "N62":("surface","N60",["R59"]),
 "N63":("surface","N60",["R60"]), "N87":("store","N60",[]), "N64":("aggregate","N01",[]),
 "N65":("surface","N64",["R14"]), "N66":("surface","N64",["R14"]), "N67":("surface","N64",["R14"]),
 "N68":("statement","N01",["R10"]),
},
 own={n:list(STD6) for n in ["N46","N47","N48","N50","N51","N52","N53","N54","N55","N56","N57","N58",
                             "N59","N60","N61","N62","N63","N65","N66","N67"]},
 parent_items={p:P7+PUAT for p in ["N45","N49","N55","N60","N64"]})
OWN["N87"]=[("K1",1),("K2",1),("A2",1),("A3",1),("A4",1),("G1",1),("G2",1),("G3",1)]
OWN["N68"]=[("K3",1),("D4",1)]

# ---- the root ----
EL["N01"]=("aggregate", None, [])
PARENT["N01"]=P7+PUAT

# ---- canonical sizes under case law 1.4 ----
KIND={"N16":"behavioural","N17":"behavioural","N18":"behavioural",
      "N69":"behavioural","N04":"behavioural","N05":"behavioural","N06":"behavioural",  # P-4
      "N70":"compliance","N08":"compliance","N68":"compliance"}
A9S={"N16":"S","N04":"S","N05":None,"N06":None}   # None = zero stated targets (1.4 filter, named hole)
GS={"N43":"M","N86":"L","N80":"S","N81":"S","N87":"S"}
SIZES={
 # B canonical: P-1 -> N24,N25 M; P-2 -> N72 M; mini-pair -> N17,N18 L
 "N16":"M","N17":"L","N18":"L","N20":"M","N21":"S","N22":"S","N23":"S","N24":"M","N25":"M",
 "N84":"M","N85":"L","N72":"M","N34":"XL","N83":"L","N73":"M","N37":"S","N38":"S","N39":"S",
 "N41":"M","N42":"S","N43":"M","N44":"S",
 # A canonical: P-4 kinds; P-5 -> N29 M; P-6 -> N82 unsizeable (absent)
 "N69":"M","N04":"M","N05":"M","N06":"S","N70":"M","N08":"S","N11":"M","N12":"M","N14":"M",
 "N15":"M","N79":"M","N27":"M","N28":"S","N74":"M","N75":"L","N77":"L","N29":"M","N80":"S","N81":"S",
 # C canonical (measured identical): N68 unsizeable (absent)
 "N46":"M","N47":"M","N48":"M","N50":"M","N51":"M","N52":"M","N53":"M","N54":"M","N55":"M","N56":"M",
 "N57":"S","N58":"M","N59":"M","N60":"S","N61":"S","N62":"S","N63":"S","N87":"M","N65":"S","N66":"S","N67":"S",
}
N86_VARIANTS=("L","XL")   # the one un-adjudicated divergence

# ---- rate table v0.1 (+ addendum A1) ----
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
 ("U1","*"):{"S":(4,8,16),"M":(8,16,32),"L":(16,28,48),"XL":(24,40,72)},
 ("U2","*"):{"S":(4,8,20),"M":(8,16,32),"L":(12,24,48),"XL":(20,36,64)},
 ("U3","*"):{"S":(4,12,32),"M":(8,20,48),"L":(12,32,64),"XL":(20,48,96)},
 ("O1","*"):{"S":(4,8,16),"M":(8,16,32),"L":(16,28,48),"XL":(24,40,72)},
 ("G1","*"):{"S":(2,4,8),"M":(4,8,16),"L":(8,16,28),"XL":(12,24,40)},
 ("G2","*"):{"S":(2,4,12),"M":(4,12,24),"L":(8,20,40),"XL":(16,32,56)},
 ("G3","*"):{"S":(0.8,2,4),"M":(2,4,8),"L":(4,8,16),"XL":(8,12,24)},
}
ONCE = [  # (label, (O,M,P)) -- sizes computed: bracket M unless stated
 ("A1 test strategy [M]",(16,28,48)), ("U4 acceptance record [M]",(8,12,24)),
 ("D1 mobilisation [M]",(16,32,56)), ("D3 status reporting [M]",(16,32,64)),
 ("D6 risk mgmt [M]",(8,20,40)), ("E2 pipeline [M]",(16,28,56)),
 ("E3 promotion [L: 3 envs]",(8,16,32)), ("E4 config mgmt [M]",(8,12,24)),
 ("E6 cutover [M]",(16,28,56)), ("E7 hosting [L: 3 envs]",(24,44,80)),
 ("O2 runbook [M]",(12,24,40)), ("O3 handover pack [M]",(8,20,36)),
 ("O4 release notes [single]",(2,4,8)), ("S1 security review [M]",(16,28,48)),
 ("S2 pentest [L: 24 surf+iface]",(20,32,56)), ("S3 remediation [L]",(24,48,112)),
 ("E1 dev [S]",(4,8,20)), ("E1 stage [M]",(8,16,32)), ("E1 prod [L]",(16,28,56)),
 ("W-R64 currency policy [single]",(4,12,32)),
]
C3_RATE=0.20
def E(c): o,m,p=c; return (o+4*m+p)/6.0
def band(n,c): return "S" if n<=c[0] else "M" if n<=c[1] else "L" if n<=c[2] else "XL"

kids={e:[] for e in EL}
for e,(_,p,_) in EL.items():
    if p in kids: kids[p].append(e)
def sub(e):
    out=[e]
    for c in kids[e]: out+=sub(c)
    return out

def key(act, cls, kind):
    if act=="K1": return ("K1","int") if cls=="interface" else ("K1","bss")
    if act=="K2": return ("K2","int") if cls=="interface" else ("K2","sto") if cls=="store" else ("K2","bs")
    if act=="K3": return ("K3",kind)
    return (act,"*")

def assemble(n86):
    sizes=dict(SIZES); sizes["N86"]=n86
    leafE={}; holes=[]
    for e,items in OWN.items():
        cls,_,cov=EL[e]
        for act,cnt in items:
            if act=="D4": s=band(len(cov),(1,3,6))
            elif act=="A9":
                s=A9S.get(e)
                if s is None: holes.append((e,"A9","zero targets - 1.4 filter")); continue
            elif act in ("G1","G2","G3"): s=GS[e]
            else:
                s=sizes.get(e)
                if s is None: holes.append((e,act,"unsizeable (P-6/M10)")); continue
            cell=T[key(act,cls,KIND.get(e))].get(s)
            if cell is None: holes.append((e,act,f"refused cell {s}")); continue
            leafE[e]=leafE.get(e,0.0)+E(cell)*cnt
    for par,items in PARENT.items():
        st=sub(par)
        leaves=[x for x in st if not kids[x]]
        si=sum(1 for x in st if EL[x][0] in ("store","interface"))
        surf=sum(1 for x in st if EL[x][0]=="surface")
        for act,cnt in items:
            if act=="A8": s=band(si,(1,3,6))
            elif act in ("U1","U2","U3","O1"):
                if surf==0: continue  # activity gated on a surface in the subtree
                s=band(surf,(1,3,6))
            else: s=band(len(leaves),(3,8,14))
            leafE[par]=leafE.get(par,0.0)+E(T[(act,"*")][s])*cnt
    c3={p:C3_RATE*sum(leafE.get(x,0.0) for x in sub(p)) for p in PARENT}
    once=sum(E(c) for _,c in ONCE)
    tot_leaf=sum(leafE.values()); tot_c3=sum(c3.values())
    return leafE,c3,once,holes,tot_leaf,tot_c3,tot_leaf+tot_c3+once

if __name__=="__main__":
    for n86 in N86_VARIANTS:
        leafE,c3,once,holes,tl,tc3,total=assemble(n86)
        print(f"=== variant N86={n86} ===")
        print(f" element leaf E (incl. root own items): {tl:.2f}")
        print(f" C3 all parents: {tc3:.2f}   of which root C3: {c3['N01']:.2f}")
        print(f" once + E1 + W-R64 layer: {once:.2f}")
        print(f" GRAND TOTAL: {total:.0f} net person-hours  (= {total/8:.1f} person-days at 8 h)")
        print(f" holes ({len(holes)}): {holes}")
    lo=assemble("L")[6]; hi=assemble("XL")[6]
    print(f"=== range from the one un-adjudicated divergence: {lo:.0f} .. {hi:.0f} net person-hours  (x{hi/lo:.4f}) ===")
    print("=== unit: net hours of work on the task. Leave, holidays, sickness and presence are NOT")
    print("===       included and are not parameters of this method (docs/constants.md).")
    # layer share and root C3 share, variant L
    leafE,c3,once,holes,tl,tc3,total=assemble("L")
    print(f" layer share of element leaf total: {once/tl*100:.1f}%")
    print(f" root C3 as share of grand total: {c3['N01']/total*100:.1f}%")
    print(f" root own per-parent items: {leafE.get('N01',0.0):.2f}")
