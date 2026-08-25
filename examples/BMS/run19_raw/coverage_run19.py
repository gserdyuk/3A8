# Run 19 — co-location comparison between the two repeats, Hotyn-M 1.1, Opus, order A.
# Own-coverage sets transcribed from each run's final model (section 6).
import itertools
A1 = {
"N69":"R01","N04":"R12 R66","N05":"R13 R68","N06":"R63","N70":"R72 R73","N08":"R71",
"N86":"R11 R54 R65","N11":"R11 R19","N12":"R11 R28 R65","N14":"R08 R52","N15":"R65",
"N16":"R61 R66","N17":"R09 R61","N18":"R62","N20":"R06 R21 R31 R41","N21":"R07","N22":"R15",
"N23":"R39","N24":"R26","N25":"R27","N27":"R04","N28":"R21","N74":"R31 R32","N75":"R32",
"N77":"R33 R34 R44","N29":"R37 R47","N85":"R15 R16 R17","N72":"R18 R19 R24","N34":"R25",
"N83":"R26 R27","N73":"R29","N37":"R29","N38":"R30 R38","N39":"R35","N41":"R29 R39",
"N42":"R40 R48","N43":"R41 R44","N44":"R45","N46":"R36 R46","N47":"R37 R47","N48":"R05 R38 R48",
"N50":"R05 R49","N51":"R50","N52":"R51","N53":"R22 R42","N54":"R53","N55":"R57","N56":"R54 R57",
"N57":"R20","N58":"R23 R43","N59":"R05 R55","N60":"R56 R67","N61":"R58","N62":"R59","N63":"R60",
"N65":"R14","N66":"R14","N67":"R14","N68":"R10"}
A2 = {
"A001":"R01","A026":"R71","A002":"R04","A047":"R17 R21","A069":"R32 R04","A070":"R33 R04",
"A072":"R34","A081":"R41","A084":"R44","A092":"R53","A045":"R15 R16","A046":"R16","A048":"R17",
"A049":"R18 R19 R24","A050":"R18","A052":"R19","A057":"R24","A031":"R10 R49 R55","A058":"R25",
"A059":"R25 R28 R50","A065":"R29","A063":"R29","A066":"R30 R38","A074":"R35","A064":"R29 R39",
"A080":"R40 R48","A085":"R45","A086":"R45","A076":"R37 R47","A027":"R71","A032":"R06","A033":"R07",
"A044":"R15","A054":"R21 R41","A068":"R31","A079":"R39","A003":"R05","A055":"R22","A082":"R42 R44",
"A089":"R49 R51","A090":"R50","A091":"R51","A093":"R53","A004":"R05","A042":"R57 R54","A043":"R57",
"A053":"R20","A056":"R23","A067":"R30","A075":"R35","A083":"R43 R44","A094":"R55","A096":"R56",
"A005":"R05","A039":"R36","A077":"R37","A078":"R38","A040":"R46","A087":"R47","A088":"R48",
"A035":"R14","A036":"R14","A037":"R14","A023":"R67","A024":"R67","A095":"R56","A097":"R58",
"A098":"R59","A099":"R60","A006":"R05 R36 R46 R54","A034":"R08 R52","A038":"R36 R46","A041":"R52",
"A060":"R26 R27 R34","A061":"R26","A062":"R27","A073":"R34","A008":"R11 R54","A009":"R11",
"A019":"R65 R11","A020":"R65 R11","A021":"R65 R11 R28","A051":"R19","A071":"R33","A007":"R09 R61",
"A014":"R61","A015":"R61 R10","A016":"R62","A022":"R66","A017":"R63","A018":"R63","A010":"R12 R71",
"A011":"R12 R66","A012":"R13 R68","A013":"R13 R68","A025":"R68","A028":"R72","A029":"R73","A030":"R73"}
def sets(d): return [frozenset(v.split()) for v in d.values()]
def pairs(sl):
    P=set()
    for s in sl:
        for a,b in itertools.combinations(sorted(s),2): P.add((a,b))
    return P
def assign(d):
    n=0
    for v in d.values(): n+=len(v.split())
    return n
for name,d in [("HM19-OA1",A1),("HM19-OA2",A2)]:
    sl=sets(d); P=pairs(sl)
    multi=[s for s in sl if len(s)>1]
    print(f"{name}: nodes with coverage {len(d)}  assignments {assign(d)}  nodes 2+ {len(multi)}  co-located pairs {len(P)}")
P1,P2=pairs(sets(A1)),pairs(sets(A2))
i,u=len(P1&P2),len(P1|P2)
mn=min(len(P1),len(P2))
print(f"\nJaccard {i/u:.3f}   containment {i/mn:.3f}   maxJ {mn/max(len(P1),len(P2)):.3f}   size ratio x{max(len(P1),len(P2))/mn:.2f}")
print(f"inter {i}  union {u}  agreement {(2278-len(P1^P2))/2278*100:.1f}% over C(68,2)=2278")
# nodes per requirement
from collections import Counter
for name,d in [("HM19-OA1",A1),("HM19-OA2",A2)]:
    c=Counter()
    for v in d.values():
        for r in v.split(): c[r]+=1
    print(f"{name}: requirements covered {len(c)}/68  nodes-per-req mean {sum(c.values())/len(c):.2f} max {max(c.values())} ({[r for r,n in c.items() if n==max(c.values())]})")
print("\nonly in OA1:",len(P1-P2)," only in OA2:",len(P2-P1))
