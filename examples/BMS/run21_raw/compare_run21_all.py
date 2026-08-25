# Run 21 - three batches, two repeats each, Hotyn-W 1.1, Opus, same product model HM19-OA1.
# A work item is a pair (element, activity). Both repeats cross the same tree, so pairs compare directly.
import itertools
PARENT = "A5c1 A5c2 A6c1 A6c2 A7 A8 D2".split()          # per-parent, no surface in subtree
PARENT_U = PARENT + "U1 U2c1 U2c2 U3c1 U3c2 O1".split()   # per-parent, surface in subtree
BUILD  = "K1 K2 A2 A3 A4".split()
SEED   = "G1 G2 G3".split()
E = lambda *xs: [a for x in xs for a in (x if isinstance(x,list) else [x])]

# ---- batch A, 25 elements
A1 = {"N02":PARENT,"N09":PARENT,"N13":PARENT,"N26":PARENT,
 "N69":["K3","D4"],"N04":["K3","A9","D4"],"N05":["K3","A9","D4"],"N06":["K3","A9","D4"],
 "N70":["K3","D4"],"N08":["K3","D4"],
 "N86":E(BUILD,"D4",SEED),"N11":E(BUILD,"D4"),"N12":E(BUILD,"D4"),"N14":E(BUILD,"A10","D4"),
 "N15":E(BUILD,"D4"),"N79":BUILD,"N27":E(BUILD,"D4"),"N28":E(BUILD,"D4",PARENT),
 "N74":E(BUILD,"A10","D4",PARENT),"N75":E(BUILD,"D4"),"N77":E(BUILD,"D4"),"N29":E(BUILD,"D4"),
 "N80":E(BUILD,SEED),"N81":E(BUILD,SEED),"N82":BUILD}
A2 = dict(A1); A2["N06"] = E(BUILD,"D4")

# ---- batch B, 27 elements - the two repeats were identical
B1 = {"N16":E("K3","A9","D4",PARENT_U),"N17":E(BUILD,"D4"),"N18":E(BUILD,"D4"),
 "N19":PARENT,"N30":PARENT,"N33":PARENT,"N36":PARENT_U,"N40":PARENT_U,
 "N84":BUILD,"N43":E(BUILD,"D4",SEED)}
for n in "N20 N21 N22 N23 N24 N25".split(): B1[n]=E(BUILD,"A10","D4")
for n in "N85 N72 N34 N83 N73 N37 N38 N39 N41 N42 N44".split(): B1[n]=E(BUILD,"D4")
B2 = dict(B1)

# ---- batch C, 25 elements
C1 = {"N45":PARENT_U,"N49":PARENT_U,"N64":PARENT_U,
 "N55":E(BUILD,"D4",PARENT_U),"N60":E(BUILD,"D4",PARENT_U),
 "N87":E(BUILD,SEED),"N68":["K3","D4"]}
for n in "N46 N47 N48 N50 N51 N52 N53 N54 N56 N57 N58 N59 N61 N62 N63 N65 N66 N67".split(): C1[n]=E(BUILD,"D4")
C2 = dict(C1); C2["N60"] = E("K3","A9","D4",PARENT_U); C2["N87"] = BUILD

def pairs(d): return {(e,a) for e,acts in d.items() for a in acts}
tot1=tot2=inter=union=0
for name,(x,y) in [("A",(A1,A2)),("B",(B1,B2)),("C",(C1,C2))]:
    P,Q = pairs(x),pairs(y)
    i,u = len(P&Q),len(P|Q)
    tot1+=len(P); tot2+=len(Q); inter+=i; union+=u
    print(f"batch {name}: {len(P):4d} vs {len(Q):4d} items   Jaccard {i/u:.3f}   only-in-1 {sorted(P-Q)}   only-in-2 {sorted(Q-P)}")
print(f"\nCOMBINED: repeat1 {tot1} items, repeat2 {tot2} items, ratio x{max(tot1,tot2)/min(tot1,tot2):.3f}")
print(f"COMBINED Jaccard: {inter/union:.3f}  (intersection {inter}, union {union})")
print("class disagreements: N06 statement/store (A), N60 surface/statement (C), N65 surface/behaviour (C, no item consequence)")
print(f"class agreement: 74 of 77 elements = {74/77:.3f}")
