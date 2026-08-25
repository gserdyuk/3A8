# Run 22 - two estimates of one work model (batch B, 197 items), Hotyn-D 1.0, Opus.
# Items are identical by construction, so the comparison is about magnitude.
E1 = {"N16":75.17,"N17":45.09,"N18":27.00,"N19":57.01,"N20":47.76,"N21":25.58,"N22":45.41,
      "N23":31.42,"N24":19.84,"N25":19.34,"N84":25.25,"N30":35.76,"N85":48.00,"N72":40.34,
      "N33":35.01,"N34":29.67,"N83":25.25,"N73":33.00,"N36":52.41,"N37":22.49,"N38":26.92,
      "N39":19.08,"N40":55.43,"N41":28.99,"N42":26.92,"N43":33.83,"N44":23.50}
E2 = {"N16":56.16,"N17":31.33,"N18":20.16,"N19":41.66,"N20":35.99,"N21":22.50,"N22":36.99,
      "N23":27.49,"N24":16.02,"N25":16.02,"N84":18.65,"N30":29.67,"N85":41.98,"N72":35.17,
      "N33":28.00,"N34":24.49,"N83":20.49,"N73":27.00,"N36":36.84,"N37":14.67,"N38":20.32,
      "N39":15.34,"N40":39.84,"N41":21.65,"N42":18.49,"N43":24.00,"N44":20.83}
INT1, INT2 = 191.09, 148.34
L1, L2 = sum(E1.values()), sum(E2.values())
print(f"leaf effort   : {L1:8.2f} vs {L2:8.2f}   x{L1/L2:.3f}")
print(f"integration   : {INT1:8.2f} vs {INT2:8.2f}   x{INT1/INT2:.3f}")
print(f"TOTAL          : {L1+INT1:8.2f} vs {L2+INT2:8.2f}   x{(L1+INT1)/(L2+INT2):.3f}")
print(f"leaves         : 209 vs 208   x{209/208:.3f}")
print(f"pd per leaf    : {L1/209:8.2f} vs {L2/208:8.2f}   x{(L1/209)/(L2/208):.3f}")
print()
cov = {"R06":["N20"],"R07":["N21"],"R09":["N17"],"R15":["N22","N85"],"R16":["N85"],"R17":["N85"],
 "R18":["N72"],"R19":["N72"],"R21":["N20"],"R24":["N72"],"R25":["N34"],"R26":["N24","N83"],
 "R27":["N25","N83"],"R29":["N73","N37","N41"],"R30":["N38"],"R31":["N20"],"R35":["N39"],
 "R38":["N38"],"R39":["N23","N41"],"R40":["N42"],"R41":["N20","N43"],"R44":["N43"],"R45":["N44"],
 "R48":["N42"],"R61":["N16","N17"],"R62":["N18"],"R66":["N16"]}
print("effort per requirement, and the ratio between the two runs")
rats=[]
for r,els in cov.items():
    a=sum(E1[e] for e in els); b=sum(E2[e] for e in els); rats.append(a/b)
    print(f"  {r}: {a:7.2f} vs {b:7.2f}   x{a/b:.3f}")
import statistics as st
print(f"\nratio across 27 requirements: min x{min(rats):.3f}  max x{max(rats):.3f}  "
      f"mean x{st.mean(rats):.3f}  stdev {st.pstdev(rats):.3f}")
print(f"requirements differing by more than x1.5: {sum(1 for x in rats if x>1.5 or x<1/1.5)}")
print(f"spread of the ratio itself: x{max(rats)/min(rats):.3f}")
