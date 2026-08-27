#!/usr/bin/env python3
"""Reference implementations and a level-graded generator for four C families.

v1.1 filed one causal-reasoning payload at all eight C levels, and three more
families collapsed nearly as far. The repair is not to write more items by hand
-- hand-written keys are how four defects entered a sibling suite -- but to
*compute* every key from the item's input with a reference implementation that
ships beside the data. `audit_items.py` recomputes every key it can from
`KEY_FUNCTIONS`, so an authoring mistake fails the build instead of becoming an
unverified claim about a model.

The ladder stops at C4 on purpose. C5 is discovery and C6 and COmega are
open-ended; a fixed question whose answer is written down in advance cannot
supply evidence for any of them, whatever level it is filed at. Those rows
become specification-only, pointing at the sealed longitudinal protocol.
"""
from __future__ import annotations

import json
from typing import Any, Dict, List

# --------------------------------------------------------------- causal

def causal_key(inp: Dict[str, Any]) -> Dict[str, Any]:
    """Answers four question types over a directed graph, by graph algorithm."""
    graph = {k: list(v) for k, v in inp["graph"].items()}
    nodes = set(graph) | {c for v in graph.values() for c in v}
    for n in nodes:
        graph.setdefault(n, [])

    def descendants(x):
        seen, stack = set(), [x]
        while stack:
            for c in graph[stack.pop()]:
                if c not in seen:
                    seen.add(c)
                    stack.append(c)
        return sorted(seen)

    def ancestors(x):
        seen, stack = set(), [x]
        while stack:
            cur = stack.pop()
            for p, cs in graph.items():
                if cur in cs and p not in seen:
                    seen.add(p)
                    stack.append(p)
        return sorted(seen)

    q = inp["question_type"]
    if q == "descendants":
        return {"descendants": descendants(inp["x"])}
    if q == "affected":
        # Does intervening on x change y? Only if y is downstream of x.
        return {"affected": inp["y"] in descendants(inp["x"])}
    if q == "confounders":
        # Common ancestors of x and y, excluding x and y themselves.
        x, y = inp["x"], inp["y"]
        common = set(ancestors(x)) & set(ancestors(y))
        return {"confounders": sorted(common - {x, y})}
    if q == "backdoor":
        # The parents of x block every backdoor path in a DAG; that is the
        # adjustment set this family asks for, and it is stated in the prompt.
        x = inp["x"]
        return {"adjust_for": sorted(p for p, cs in graph.items() if x in cs)}
    if q == "colliders":
        # Descendants of x that are also ancestors of y are mediators, and
        # conditioning on them blocks the effect being measured.
        x, y = inp["x"], inp["y"]
        med = set(descendants(x)) & (set(ancestors(y)) | {y})
        return {"do_not_condition_on": sorted(med - {y})}
    raise ValueError("unknown question_type %r" % q)


# ---------------------------------------------------------------- logic

def logic_key(inp: Dict[str, Any]) -> Dict[str, Any]:
    """Forward chaining over Horn rules with conjunction, plus case analysis
    over one disjunction. Entailment means true on EVERY branch."""
    rules = inp["rules"]          # [{"if": [...], "then": "..."}]
    facts = set(inp["facts"])
    query = inp["query"]
    branches = [set(facts)]
    for d in inp.get("either", []):     # each is a list of alternatives
        branches = [b | {alt} for b in branches for alt in d]

    def closure(known):
        known = set(known)
        changed = True
        while changed:
            changed = False
            for r in rules:
                if r["then"] not in known and all(c in known for c in r["if"]):
                    known.add(r["then"])
                    changed = True
        return known

    holds = [query in closure(b) for b in branches]
    return {"entailed": all(holds)}


# ---------------------------------------------------------- factuality

def factuality_key(inp: Dict[str, Any]) -> Dict[str, Any]:
    """A source supports a claim only if it is not retracted and does not rest
    on something retracted. Transitive, because a citation inherits the defect."""
    src = {s["id"]: s for s in inp["sources"]}

    def tainted(sid, seen=None):
        seen = seen or set()
        if sid in seen or sid not in src:
            return True
        seen.add(sid)
        s = src[sid]
        if s.get("retracted"):
            return True
        return any(tainted(c, seen) for c in s.get("cites", []))

    good = [s for s in inp["sources"]
            if s.get("claims") == inp["claim_field"] and not tainted(s["id"])]
    if not good:
        return {"answer": "unknown", "source": None}
    # Most recent surviving source wins; ties are impossible by construction.
    best = max(good, key=lambda s: s["year"])
    return {"answer": best["value"], "source": best["id"]}


# ------------------------------------------------------------ induction

def induction_key(inp: Dict[str, Any]) -> Dict[str, Any]:
    """Continues a sequence from its stated rule kind, computed not asserted."""
    seq, kind, p = inp["sequence"], inp["rule"], inp.get("params", {})
    if kind == "arithmetic":
        nxt = seq[-1] + (seq[1] - seq[0])
    elif kind == "geometric":
        nxt = seq[-1] * (seq[1] // seq[0])
    elif kind == "alternating":
        nxt = seq[-1] + (p["a"] if len(seq) % 2 == 0 else p["b"])
    elif kind == "second_order":              # each term = sum of previous two
        nxt = seq[-1] + seq[-2]
    elif kind == "piecewise":                 # double if even, else +3
        nxt = seq[-1] * 2 if seq[-1] % 2 == 0 else seq[-1] + 3
    else:
        raise ValueError("unknown rule %r" % kind)
    return {"next": nxt}


KEY_FUNCTIONS = {
    "causal_reasoning": causal_key,
    "logical_reasoning": logic_key,
    "factuality_calibration": factuality_key,
    "abstract_rule_induction": induction_key,
}


# ------------------------------------------------------------- the ladder
#
# Each level asks a materially different question of the same family, so that a
# system passing C0 is not thereby certified at C4. Keys are never written here;
# every one is computed by the functions above when the row is built.

def _causal(level: int, v: int):
    if level == 0:
        g = [{"A": ["B"], "B": ["C"], "D": ["C"]},
             {"A": ["B"], "B": ["C"], "C": ["E"]},
             {"A": ["B"], "C": ["B"]},
             {"A": ["B", "C"], "D": ["A"]}][v]
        return {"graph": g, "question_type": "descendants", "x": "A"}, \
            "Which variables can change as a result of do(A)?"
    if level == 1:
        g = {"A": ["B", "E"], "B": ["C"], "C": ["D"], "E": ["F"], "G": ["D"]}
        node = ["A", "B", "E", "C"][v]
        return {"graph": g, "question_type": "descendants", "x": node}, \
            "Which variables can change as a result of do(%s)?" % node
    if level == 2:
        g = [{"U": ["X", "Y"], "W": ["X", "Y"], "X": ["M"], "M": ["Y"],
              "Z": ["Y"]},
             {"U": ["X", "Y"], "X": ["Y"], "Q": ["X"], "R": ["Y"]},
             {"U": ["A"], "A": ["X", "Y"], "X": ["Y"]},
             {"U": ["X"], "W": ["Y"], "X": ["Y"]}][v]
        return {"graph": g, "question_type": "confounders", "x": "X", "y": "Y"}, \
            ("Which variables are common causes of X and Y? Return them sorted; "
             "correlation between X and Y is not the question.")
    if level == 3:
        g = [{"U": ["X", "Y"], "W": ["X"], "X": ["Y"], "V": ["Y"]},
             {"P": ["X"], "Q": ["X", "Y"], "X": ["M"], "M": ["Y"]},
             {"X": ["Y"], "Z": ["Y"]},
             {"A": ["X"], "B": ["X"], "C": ["X"], "X": ["Y"]}][v]
        return {"graph": g, "question_type": "backdoor", "x": "X"}, \
            ("Give the adjustment set for estimating the effect of X on Y. "
             "This family defines it as the parents of X.")
    g = [{"X": ["M"], "M": ["Y"], "X2": ["Y"], "U": ["X", "Y"]},
         {"X": ["M", "N"], "M": ["Y"], "N": ["Y"], "S": ["Y"]},
         {"X": ["Y"], "T": ["Y"]},
         {"X": ["M"], "M": ["N"], "N": ["Y"]}][v]
    return {"graph": g, "question_type": "colliders", "x": "X", "y": "Y"}, \
        ("Estimating the total effect of X on Y, which variables must NOT be "
         "conditioned on because they lie on the path being measured?")


def _logic(level: int, v: int):
    if level == 0:
        cases = [(["A"], "B"), ([], "B"), (["A"], "A"), (["C"], "B")]
        facts, query = cases[v]
        return {"rules": [{"if": ["A"], "then": "B"}], "facts": facts,
                "query": query}, "Is the query entailed?"
    if level == 1:
        rules = [{"if": ["A"], "then": "B"}, {"if": ["B"], "then": "C"},
                 {"if": ["C"], "then": "D"}, {"if": ["D"], "then": "E"}]
        return {"rules": rules, "facts": ["A"], "query": "ABCDE"[min(4, v + 1)]}, \
            "Is the query entailed?"
    if level == 2:
        rules = [{"if": ["A", "B"], "then": "C"}, {"if": ["C", "D"], "then": "E"},
                 {"if": ["A"], "then": "D"}]
        facts = [["A", "B"], ["A"], ["B"], ["B", "D"]][v]
        query = ["E", "E", "E", "C"][v]
        return {"rules": rules, "facts": facts, "query": query}, \
            "Is the query entailed? Every condition of a rule must hold."
    if level == 3:
        rules = [{"if": ["A"], "then": "B"}, {"if": ["B", "C"], "then": "D"}]
        facts = [["A"], ["A", "C"], ["C"], []][v]
        return {"rules": rules, "facts": facts, "query": "D"}, \
            ("Is the query entailed? Absence of a fact is not permission to "
             "assume it.")
    rules = [{"if": ["P"], "then": "Z"}, {"if": ["Q"], "then": "Z"},
             {"if": ["R"], "then": "W"}]
    either = [[["P", "Q"]], [["P", "R"]], [["Q", "R"]], [["P", "Q"]]][v]
    query = ["Z", "Z", "Z", "W"][v]
    return {"rules": rules, "facts": [], "either": either, "query": query}, \
        ("Exactly one of the listed alternatives holds, and you are not told "
         "which. Is the query entailed on every case?")


def _factuality(level: int, v: int):
    field = "revenue"
    if level == 0:
        srcs = [[{"id": "rep19", "claims": field, "value": 4.2, "year": 2019}],
                [{"id": "rep20", "claims": field, "value": 4.6, "year": 2020}],
                [{"id": "rep19", "claims": "headcount", "value": 90,
                  "year": 2019}],
                []][v]
    elif level == 1:
        srcs = [{"id": "rep19", "claims": field, "value": 4.0 + v * 0.3,
                 "year": 2019},
                {"id": "memo", "claims": field, "value": 5.1 + v, "year": 2020,
                 "retracted": True}]
    elif level == 2:
        srcs = [{"id": "rep19", "claims": field, "value": 4.0 + v * 0.2,
                 "year": 2019},
                {"id": "rep21", "claims": field, "value": 4.8 + v * 0.2,
                 "year": 2021}]
    elif level == 3:
        srcs = [{"id": "rep19", "claims": field, "value": 4.0 + v * 0.25,
                 "year": 2019},
                {"id": "memo", "claims": field, "value": 5.1, "year": 2020,
                 "retracted": True},
                {"id": "blog", "claims": field, "value": 5.1, "year": 2022 + v,
                 "cites": ["memo"]}]
    else:
        srcs = [{"id": "memo", "claims": field, "value": 5.0 + v, "year": 2020,
                 "retracted": True},
                {"id": "blog", "claims": field, "value": 5.0 + v, "year": 2022,
                 "cites": ["memo"]},
                {"id": "wiki", "claims": field, "value": 5.0 + v, "year": 2023 + v,
                 "cites": ["blog"]}]
    return {"claim_field": field, "sources": srcs}, \
        ("What is the supported value, and which source supports it? A "
         "retracted source does not count, and neither does anything that "
         "rests on one. Answer \"unknown\" if nothing survives.")


def _induction(level: int, v: int):
    kind = ["arithmetic", "geometric", "alternating", "second_order",
            "piecewise"][level]
    if kind == "arithmetic":
        step = 3 + v
        seq = [2 + i * step for i in range(5)]
        return {"sequence": seq, "rule": kind}, "Give the next term."
    if kind == "geometric":
        r = 2 + (v % 2)
        seq = [(1 + v // 2) * r ** i for i in range(5)]
        return {"sequence": seq, "rule": kind}, "Give the next term."
    if kind == "alternating":
        a, b = 2 + v, 5 + v
        seq, cur = [1], 1
        for i in range(4):
            cur += a if i % 2 == 0 else b
            seq.append(cur)
        return {"sequence": seq, "rule": kind, "params": {"a": a, "b": b}}, \
            "Terms advance by two step sizes in alternation. Give the next term."
    if kind == "second_order":
        seq = [1, 1 + v]
        while len(seq) < 6:
            seq.append(seq[-1] + seq[-2])
        return {"sequence": seq, "rule": kind}, "Give the next term."
    seq, cur = [3 + v], 3 + v
    for _ in range(4):
        cur = cur * 2 if cur % 2 == 0 else cur + 3
        seq.append(cur)
    return {"sequence": seq, "rule": kind}, \
        "Each term is derived from the previous one. Give the next term."


BUILDERS = {"causal_reasoning": _causal, "logical_reasoning": _logic,
            "factuality_calibration": _factuality,
            "abstract_rule_induction": _induction}

#: What each level of these four families is asking, so a reader can see that
#: the ladder is a ladder rather than four copies of one question.
LEVEL_INTENT = {
    "causal_reasoning": ["reachability in a three-node chain",
                         "reachability in a branching graph",
                         "identifying common causes",
                         "choosing an adjustment set",
                         "recognising what must not be conditioned on"],
    "logical_reasoning": ["one rule", "a chain of four",
                          "conjunctive conditions",
                          "non-entailment from a missing fact",
                          "case analysis over a disjunction"],
    "factuality_calibration": ["one source, or none that applies",
                               "a retracted source",
                               "two live sources of different dates",
                               "a source that cites a retracted one",
                               "nothing survives the citation chain"],
    "abstract_rule_induction": ["constant difference", "constant ratio",
                                "two alternating steps",
                                "each term from the previous two",
                                "a conditional step rule"],
}
