# Run 21 — two crossings of the same 25-element subtree set, Hotyn-W 1.1, Opus.
# A work item is a pair (element, activity). Both runs cross the same tree, so the pairs are
# directly comparable — this is the step-2 analogue of step 1's requirement co-location Jaccard.
PARENT = "A5c1 A5c2 A6c1 A6c2 A7 A8 D2".split()
BUILD  = "K1 K2 A2 A3 A4".split()
SEED   = "G1 G2 G3".split()

A1 = {
 "N02": PARENT, "N09": PARENT, "N13": PARENT, "N26": PARENT,
 "N69": ["K3","D4"], "N04": ["K3","A9","D4"], "N05": ["K3","A9","D4"],
 "N06": ["K3","A9","D4"],                      # classified statement
 "N70": ["K3","D4"], "N08": ["K3","D4"],
 "N86": BUILD+["D4"]+SEED, "N11": BUILD+["D4"], "N12": BUILD+["D4"],
 "N14": BUILD+["A10","D4"], "N15": BUILD+["D4"], "N79": BUILD,
 "N27": BUILD+["D4"], "N28": BUILD+["D4"]+PARENT, "N74": BUILD+["A10","D4"]+PARENT,
 "N75": BUILD+["D4"], "N77": BUILD+["D4"], "N29": BUILD+["D4"],
 "N80": BUILD+SEED, "N81": BUILD+SEED, "N82": BUILD,
}
A2 = dict(A1)
A2["N06"] = BUILD+["D4"]                       # classified store; G1-G3 refused by judgement

cls1 = {"N06":"statement"}; cls2 = {"N06":"store"}   # the only class that differs

def pairs(d): return {(e,a) for e,acts in d.items() for a in acts}
P1,P2 = pairs(A1), pairs(A2)
i,u = len(P1&P2), len(P1|P2)
print(f"items: repeat1 {len(P1)}  repeat2 {len(P2)}  ratio x{max(len(P1),len(P2))/min(len(P1),len(P2)):.3f}")
print(f"Jaccard over (element, activity) pairs: {i/u:.3f}   intersection {i}  union {u}")
print(f"only in repeat1: {sorted(P1-P2)}")
print(f"only in repeat2: {sorted(P2-P1)}")
print(f"class agreement: {25-len(cls1)}/25 identical; differing: {list(cls1)} -> {cls1['N06']} vs {cls2['N06']}")
print(f"judgement refusals: 13 vs 16 - the 3 extra are N06 x G1,G2,G3, a consequence of the same class call")
