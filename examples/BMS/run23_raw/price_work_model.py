# run 23 — price the batch-B work model from sensor size classes x rate table v0.1
# All numbers here are transcribed from docs/rate_table.md (v0.1) and run21_raw/HW21-B1.md.
# The ONLY inputs that come from the Hotyn-D 2.0 sensors are SIZES_RUN1 / SIZES_RUN2 below
# (element size classes, N16's statement kind, two special counts). Everything else is arithmetic.

# --- structure: id -> (class, parent, coverage ids) --- from HM19-OA1 / HW21-B1
EL = {
    "N16": ("statement", "root", ["R61", "R66"]),
    "N17": ("surface", "N16", ["R09", "R61"]),
    "N18": ("surface", "N16", ["R62"]),
    "N19": ("aggregate", "root", []),
    "N20": ("interface", "N19", ["R06", "R21", "R31", "R41"]),
    "N21": ("interface", "N19", ["R07"]),
    "N22": ("interface", "N19", ["R15"]),
    "N23": ("interface", "N19", ["R39"]),
    "N24": ("interface", "N19", ["R26"]),
    "N25": ("interface", "N19", ["R27"]),
    "N84": ("behaviour", "N19", []),
    "N30": ("aggregate", "root", []),
    "N85": ("behaviour", "N30", ["R15", "R16", "R17"]),
    "N72": ("behaviour", "N30", ["R18", "R19", "R24"]),
    "N33": ("aggregate", "root", []),
    "N34": ("behaviour", "N33", ["R25"]),
    "N83": ("behaviour", "N33", ["R26", "R27"]),
    "N73": ("behaviour", "N33", ["R29"]),
    "N36": ("aggregate", "root", []),
    "N37": ("behaviour", "N36", ["R29"]),
    "N38": ("surface", "N36", ["R30", "R38"]),
    "N39": ("behaviour", "N36", ["R35"]),
    "N40": ("aggregate", "root", []),
    "N41": ("behaviour", "N40", ["R29", "R39"]),
    "N42": ("surface", "N40", ["R40", "R48"]),
    "N43": ("store", "N40", ["R41", "R44"]),
    "N44": ("behaviour", "N40", ["R45"]),
}
PARENTS = ["N16", "N19", "N30", "N33", "N36", "N40"]

# --- work items per element (activity, count) --- from HW21-B1; x2 = two declared cycles
OWN_ITEMS = {
    "N16": [("K3", 1), ("A9", 1), ("D4", 1)],
    "N17": [("K1", 1), ("K2", 1), ("A2", 1), ("A3", 1), ("A4", 1), ("D4", 1)],
    "N18": [("K1", 1), ("K2", 1), ("A2", 1), ("A3", 1), ("A4", 1), ("D4", 1)],
    "N84": [("K1", 1), ("K2", 1), ("A2", 1), ("A3", 1), ("A4", 1)],
    "N43": [("K1", 1), ("K2", 1), ("A2", 1), ("A3", 1), ("A4", 1), ("D4", 1),
            ("G1", 1), ("G2", 1), ("G3", 1)],
}
for n in ["N20", "N21", "N22", "N23", "N24", "N25"]:
    OWN_ITEMS[n] = [("K1", 1), ("K2", 1), ("A2", 1), ("A3", 1), ("A4", 1), ("A10", 1), ("D4", 1)]
for n in ["N85", "N72", "N34", "N83", "N73", "N37", "N39", "N41", "N44", "N38", "N42"]:
    OWN_ITEMS[n] = [("K1", 1), ("K2", 1), ("A2", 1), ("A3", 1), ("A4", 1), ("D4", 1)]

PARENT_ITEMS = {p: [("A5", 2), ("A6", 2), ("A7", 1), ("A8", 1), ("D2", 1)] for p in PARENTS}
for p in ["N16", "N36", "N40"]:  # subtree holds a surface -> UAT + user documentation fired
    PARENT_ITEMS[p] += [("U1", 1), ("U2", 2), ("U3", 2), ("O1", 1)]

# --- rate table v0.1 --- (O, M, P) per size; None = cell refused by Hotyn-K (M > 10)
T = {
    ("K1", "bss"):  {"S": (0.25, 0.5, 1), "M": (0.5, 1, 2), "L": (1, 2, 3.5), "XL": (2, 3.5, 6)},
    ("K1", "int"):  {"S": (0.5, 1, 2), "M": (1, 2, 4), "L": (2, 3.5, 6), "XL": (3, 5, 9)},
    ("K2", "bs"):   {"S": (0.5, 1, 2), "M": (1, 2.5, 5), "L": (2.5, 5, 9), "XL": (5, 8, 14)},
    ("K2", "int"):  {"S": (1, 2, 4), "M": (2, 3.5, 7), "L": (3, 6, 10), "XL": (5, 9, 15)},
    ("K2", "sto"):  {"S": (0.5, 1, 2), "M": (1, 2, 3.5), "L": (2, 4, 7), "XL": (3.5, 6.5, 11)},
    ("K3", "compliance"):  {"S": (0.25, 0.5, 1.5), "M": (0.5, 1.5, 3), "L": (1, 2.5, 5), "XL": (2, 4, 8)},
    ("K3", "behavioural"): {"S": (1, 2, 4), "M": (2, 4, 8), "L": (3, 6, 12), "XL": None},
    ("A2", "*"): {"S": (0.25, 0.5, 1), "M": (0.5, 1, 2), "L": (1, 2, 3.5), "XL": (1.5, 3, 5)},
    ("A3", "*"): {"S": (0.5, 1, 2), "M": (1, 2, 4), "L": (2, 3.5, 6), "XL": (3, 5.5, 9)},
    ("A4", "*"): {"S": (0.1, 0.25, 0.5), "M": (0.25, 0.5, 1), "L": (0.5, 1, 2), "XL": (0.75, 1.5, 3)},
    ("A9", "*"): {"S": (1, 2, 4), "M": (2, 3.5, 7), "L": (3, 5.5, 10), "XL": (4, 8, 14)},
    ("A10", "*"): {"S": (0.5, 1, 2.5), "M": (1, 2, 4), "L": (2, 3.5, 7), "XL": (3, 5, 10)},
    ("A5", "*"): {"S": (0.5, 1, 2), "M": (1, 2, 4), "L": (2, 3.5, 6), "XL": (3, 5, 9)},
    ("A6", "*"): {"S": (0.5, 1.5, 4), "M": (1, 3, 7), "L": (2, 5, 10), "XL": (3, 7, 14)},
    ("A7", "*"): {"S": (1, 2, 4), "M": (2, 4, 7), "L": (3, 6, 10), "XL": (4, 8, 14)},
    ("A8", "*"): {"S": (0.25, 0.5, 1.5), "M": (0.5, 1.5, 3), "L": (1, 2.5, 5), "XL": (2, 4, 8)},
    ("D2", "*"): {"S": (0.5, 1, 2), "M": (1, 2, 4), "L": (2, 3.5, 6), "XL": (3, 5, 8)},
    ("D4", "*"): {"S": (0.25, 0.5, 1), "M": (0.5, 1, 2), "L": (1, 2, 4), "XL": (1.5, 3, 6)},
    ("U1", "*"): {"S": (0.5, 1, 2), "M": (1, 2, 4), "L": (2, 3.5, 6), "XL": (3, 5, 9)},
    ("U2", "*"): {"S": (0.5, 1, 2.5), "M": (1, 2, 4), "L": (1.5, 3, 6), "XL": (2.5, 4.5, 8)},
    ("U3", "*"): {"S": (0.5, 1.5, 4), "M": (1, 2.5, 6), "L": (1.5, 4, 8), "XL": (2.5, 6, 12)},
    ("O1", "*"): {"S": (0.5, 1, 2), "M": (1, 2, 4), "L": (2, 3.5, 6), "XL": (3, 5, 9)},
    ("G1", "*"): {"S": (0.25, 0.5, 1), "M": (0.5, 1, 2), "L": (1, 2, 3.5), "XL": (1.5, 3, 5)},
    ("G2", "*"): {"S": (0.25, 0.5, 1.5), "M": (0.5, 1.5, 3), "L": (1, 2.5, 5), "XL": (2, 4, 7)},
    ("G3", "*"): {"S": (0.1, 0.25, 0.5), "M": (0.25, 0.5, 1), "L": (0.5, 1, 2), "XL": (1, 1.5, 3)},
}
C3_RATE = 0.20

def band(n, cuts):  # cuts = (S_max, M_max, L_max)
    return "S" if n <= cuts[0] else "M" if n <= cuts[1] else "L" if n <= cuts[2] else "XL"

def kids(p):
    return [e for e, (_, par, _) in EL.items() if par == p]

def computed_sizes():
    """Position-derived and mechanical sizes -- no judgement anywhere here."""
    sz = {}
    for p in PARENTS:
        ch = kids(p)
        leaves = [c for c in ch if EL[c][0] != "aggregate"]
        sz[("parent", p)] = band(len(leaves), (3, 8, 14))                      # A5 A6 A7 D2
        si = sum(1 for c in ch if EL[c][0] in ("store", "interface"))
        sz[("A8", p)] = band(si, (1, 3, 6))
        surf = sum(1 for c in ch if EL[c][0] == "surface")
        sz[("surf", p)] = band(surf, (1, 3, 6)) if surf else None              # U1 U2 U3 O1
    for e, (cls, _, cov) in EL.items():
        if cov and cls != "aggregate":
            sz[("D4", e)] = band(len(cov), (1, 3, 6))
    return sz

def table_key(act, el, sizes):
    cls, kind = EL[el][0], sizes.get("N16_kind")
    if act == "K1":
        return ("K1", "int") if cls == "interface" else ("K1", "bss")
    if act == "K2":
        return ("K2", "int") if cls == "interface" else ("K2", "sto") if cls == "store" else ("K2", "bs")
    if act == "K3":
        return ("K3", kind)
    return (act, "*")

def price(sizes):
    """sizes: {'N17': 'M', ..., 'N16_kind': 'behavioural'|'compliance', 'N16_A9': 'S'.., 'N43_G': 'M'..}"""
    comp = computed_sizes()
    rows, holes = [], []
    for e, items in OWN_ITEMS.items():
        for act, cnt in items:
            if act == "D4":
                s = comp[("D4", e)]
            elif act == "A9":
                s = sizes["N16_A9"]
            elif act in ("G1", "G2", "G3"):
                s = sizes["N43_G"]
            else:
                s = sizes.get(e)
                if s is None:  # element reported unsizeable by the sensor -> a named hole
                    holes.append((e, act, "unsizeable")); continue
            cell = T[table_key(act, e, sizes)].get(s)
            if cell is None:
                holes.append((e, act, s)); continue
            o, m, p = cell
            rows += [(e, act, s, (o + 4 * m + p) / 6.0)] * cnt
    for par, items in PARENT_ITEMS.items():
        for act, cnt in items:
            s = comp[("A8", par)] if act == "A8" else comp[("surf", par)] if act in ("U1", "U2", "U3", "O1") else comp[("parent", par)]
            o, m, p = T[(act, "*")][s]
            rows += [(par, act, s, (o + 4 * m + p) / 6.0)] * cnt
    leaf = {}
    for e, act, s, ev in rows:
        leaf[e] = leaf.get(e, 0.0) + ev
    c3 = {}
    for par in PARENTS:
        base = leaf.get(par, 0.0) + sum(leaf.get(c, 0.0) for c in kids(par))
        c3[par] = C3_RATE * base
    tot_leaf, tot_c3 = sum(leaf.values()), sum(c3.values())
    proj = {}
    for e, (_, _, cov) in EL.items():
        for r in cov:
            proj[r] = proj.get(r, 0.0) + leaf.get(e, 0.0)
    return {"rows": rows, "leaf": leaf, "c3": c3, "total": tot_leaf + tot_c3,
            "tot_leaf": tot_leaf, "tot_c3": tot_c3, "proj": proj, "holes": holes}

# --- sensor outputs, transcribed from run23_raw/HD23-B1.md / HD23-B2.md ---
# N17 and N18 are absent deliberately: BOTH runs reported them unsizeable (surface class, zero
# user tasks named) -> their class-driven items are priced as named holes, identically in both runs.
SIZES_RUN1 = {
    "N16": "M", "N20": "M", "N21": "S", "N22": "S", "N23": "S", "N24": "S", "N25": "S",
    "N84": "M", "N85": "L", "N72": "L", "N34": "XL", "N83": "L", "N73": "M",
    "N37": "S", "N38": "S", "N39": "S", "N41": "M", "N42": "S", "N43": "M", "N44": "S",
    "N16_kind": "behavioural", "N16_A9": "S", "N43_G": "M",
}
SIZES_RUN2 = {
    "N16": "M", "N20": "M", "N21": "S", "N22": "S", "N23": "S", "N24": "M", "N25": "M",
    "N84": "M", "N85": "L", "N72": "M", "N34": "XL", "N83": "L", "N73": "M",
    "N37": "S", "N38": "S", "N39": "S", "N41": "M", "N42": "S", "N43": "M", "N44": "S",
    "N16_kind": "behavioural", "N16_A9": "S", "N43_G": "M",
}

if __name__ == "__main__":
    if not (SIZES_RUN1 and SIZES_RUN2):
        raise SystemExit("fill SIZES_RUN1 / SIZES_RUN2 from the transcribed sensor outputs first")
    r1, r2 = price(SIZES_RUN1), price(SIZES_RUN2)
    n_items = sum(c for it in OWN_ITEMS.values() for _, c in it) + \
              sum(c for it in PARENT_ITEMS.values() for _, c in it)
    print("items priced (each run):", n_items)
    for name, r in (("run1", r1), ("run2", r2)):
        print(f"{name}: leaf {r['tot_leaf']:.2f}  C3 {r['tot_c3']:.2f}  TOTAL {r['total']:.2f}  holes {r['holes']}")
    hi, lo = max(r1["total"], r2["total"]), min(r1["total"], r2["total"])
    print(f"Sigma-E ratio: x{hi / lo:.4f}")
    diffs = [e for e in SIZES_RUN1 if SIZES_RUN1[e] != SIZES_RUN2.get(e)]
    print("class/size differences:", diffs or "none")
    print("\nper-requirement projection (run1 vs run2, overlapping rows, do not sum):")
    for r in sorted(set(r1["proj"]) | set(r2["proj"])):
        a, b = r1["proj"].get(r, 0.0), r2["proj"].get(r, 0.0)
        rat = max(a, b) / min(a, b) if min(a, b) > 0 else float("inf")
        print(f"  {r}: {a:8.2f}  {b:8.2f}   x{rat:.3f}")
