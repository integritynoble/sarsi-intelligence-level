"""C -- cognitive items with computed keys, bands C0-C3, one call each.

C0 reactive: one explicit operation.          C1 contextual: a routine two-step word problem.
C2 compositional: three interacting constraints.  C3 strategic: shortest path with a transfer trap.
Every key is computed by the generator; the plausible wrong method per band is named and shown to fail.
"""
from __future__ import annotations
import itertools, json
from pathlib import Path
from .common import rng, read_json, result

FAMILY = "c_items"

def _c0(r):
    a, b = r.randint(120, 980), r.randint(12, 98)
    return f"Compute {a} - {b} and write answer.json as {{\"answer\": <integer>}}.", a - b, "the sum instead of the difference", a + b

def _c1(r):
    n, price, disc = r.randint(3, 9), r.randint(11, 49), r.choice([10, 20, 25])
    total = round(n * price * (100 - disc) / 100, 2)
    return (f"{n} items cost {price} each; a {disc}% discount applies to the whole order. Write answer.json as "
            f"{{\"answer\": <total as a number with two decimals>}}.", total, "forgetting the discount", float(n * price))

def _c2(r):
    # three constraints on a 5-slot schedule; exhaustive key
    people = ["Ana", "Bo", "Cy", "Di", "Ed"]; r.shuffle(people)
    sols = []
    for perm in itertools.permutations(people):
        pos = {p: i for i, p in enumerate(perm)}
        if pos["Ana"] < pos["Bo"] and abs(pos["Cy"] - pos["Di"]) == 1 and pos["Ed"] != 0 and pos["Ed"] != 4:
            sols.append(list(perm))
    key = sorted(sols)[r.randint(0, len(sols) - 1)]
    # make the instance unique: add constraints from the chosen solution until only it remains
    extra = []
    cands = sols
    for p in people:
        if len(cands) == 1: break
        extra.append((p, key.index(p))); cands = [s for s in cands if s.index(p) == key.index(p)]
    text = ("Five people take slots 1-5. Ana is before Bo. Cy and Di are adjacent. Ed is neither first nor last. "
            + " ".join(f"{p} is in slot {i + 1}." for p, i in extra) +
            " Write answer.json as {\"answer\": [<names in slot order>]}.")
    return text, key, "ignoring the adjacency constraint", None

def _c3(r):
    # weighted graph shortest path; trap: fewest hops differs from cheapest
    nodes = ["A", "B", "C", "D", "E", "F"]; edges = {}
    def add(u, v, w): edges.setdefault(u, {})[v] = w; edges.setdefault(v, {})[u] = w
    add("A", "B", r.randint(7, 9)); add("B", "F", r.randint(7, 9))          # 2 hops, cost 14-18
    add("A", "C", 2); add("C", "D", 2); add("D", "E", 2); add("E", "F", 2)  # 4 hops, cost 8
    add("C", "E", r.randint(9, 12))
    # Dijkstra for the key
    import heapq
    dist = {"A": 0}; prev = {}; pq = [(0, "A")]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, 1e9): continue
        for v, w in edges[u].items():
            if d + w < dist.get(v, 1e9): dist[v] = d + w; prev[v] = u; heapq.heappush(pq, (d + w, v))
    path = ["F"]
    while path[-1] != "A": path.append(prev[path[-1]])
    path.reverse()
    desc = "; ".join(f"{u}-{v}:{w}" for u in edges for v, w in edges[u].items() if u < v)
    return (f"Undirected weighted graph, edges as node-node:weight -- {desc}. Find the cheapest path from A to F. "
            f"Write answer.json as {{\"answer\": [<nodes in order>], \"cost\": <total>}}.", {"path": path, "cost": dist['F']},
            "fewest hops", {"path": ["A", "B", "F"], "cost": edges["A"]["B"] + edges["B"]["F"]})

BANDS = {"C0": _c0, "C1": _c1, "C2": _c2, "C3": _c3}

def generate(seed: int, band: str):
    r = rng(seed, FAMILY + band)
    text, key, naive_name, naive = BANDS[band](r)
    files = {"GOAL.md": f"# GOAL (band {band})\n\n{text}\n"}
    return files, {"family": FAMILY, "band": band, "seed": seed, "key": key, "naive_name": naive_name, "naive": naive}

def verify(ws: Path, key: dict) -> dict:
    ans = read_json(ws / "answer.json")
    if ans is None or ans == "INVALID_JSON" or not isinstance(ans, dict):
        return result(False, 0.0, [("answer_present", False, "answer.json missing or invalid")], "not_attempted")
    k = key["key"]
    if key["band"] == "C3":
        ok = ans.get("answer") == k["path"] and abs(float(ans.get("cost", -1)) - k["cost"]) < 1e-6
    elif key["band"] == "C1":
        ok = abs(float(ans.get("answer", -1e9)) - k) < 0.005
    else:
        ok = ans.get("answer") == k
    return result(ok, 1.0 if ok else 0.0, [("answer_exact", ok, f"expected {k}")], None if ok else "wrong_answer")

def reference_solve(ws: Path, key: dict) -> None:
    k = key["key"]
    (ws / "answer.json").write_text(json.dumps({"answer": k["path"], "cost": k["cost"]} if key["band"] == "C3" else {"answer": k}))

def naive_solve(ws: Path, key: dict) -> None:
    n = key["naive"]
    if n is None:   # C2: drop the adjacency constraint -> pick a schedule violating it
        k = key["key"]; sw = list(k); i, j = sw.index("Cy"), sw.index("Di")
        # move Di away from Cy
        far = [x for x in range(5) if abs(x - i) > 1 and x != j][0]
        sw[j], sw[far] = sw[far], sw[j]; n = sw
    (ws / "answer.json").write_text(json.dumps({"answer": n["path"], "cost": n["cost"]} if key["band"] == "C3" else {"answer": n}))

def spec_key_check(seed: int) -> None:
    import tempfile, shutil
    from .common import write_workspace
    for band in BANDS:
        files, key = generate(seed, band); d = Path(tempfile.mkdtemp()); write_workspace(d, files)
        reference_solve(d, key); assert verify(d, key)["pass"], (band, "reference fails")
        naive_solve(d, key); assert not verify(d, key)["pass"], (band, "trap did not fire")
        shutil.rmtree(d)
