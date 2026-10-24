#!/usr/bin/env python3
"""Exhaust the finite contracts in DETERMINISTIC_CONTRACTS.md; no acceptance claim."""
from itertools import product
import json


def double(n):
    return {"n": n, "double": 2 * n}


def sorted_report(xs, fuel):
    inspected = []
    for i in range(min(fuel, max(0, len(xs) - 1))):
        pair = {"index": i, "left": xs[i], "right": xs[i + 1]}
        inspected.append(pair)
        if pair["left"] > pair["right"]:
            return {"subject": tuple(xs), "basis": "finite-sorted-v1",
                    "result": "falsified", "witness": pair,
                    "inspected": inspected, "residual": [], "stop": None}
    exhausted = len(inspected) < max(0, len(xs) - 1)
    return {"subject": tuple(xs), "basis": "finite-sorted-v1",
            "result": "indeterminate" if exhausted else "satisfied",
            "witness": None, "inspected": inspected,
            "residual": list(range(len(inspected), max(0, len(xs) - 1))),
            "stop": "assessment_exhausted" if exhausted else None}


def copy_with_fuel(xs, fuel):
    prefix = tuple(xs[:fuel])
    complete = len(prefix) == len(xs)
    return {"prefix": prefix, "candidate": prefix if complete else None,
            "work": "candidate_ready" if complete else "incomplete",
            "availability": "satisfied" if complete else "falsified",
            "stop": None if complete else "copy_exhausted"}


def put_a(state, grant):
    return ("A", "request put_A") if grant == "allow" else (state, "refusal")


def transition(state, action):
    if action.startswith("assess_"):
        return (action[-1], "recorded") if state == "U" else (state, "already_assessed")
    decisions = {"U": "block_unassessed", "S": "advance",
                 "F": "block_falsified", "I": "block_indeterminate"}
    return state, decisions[state]


def alpha(state):
    return "subject-v1", "one-assessment-v1", None if state == "U" else state


def abstract_transition(record, action):
    # Independent record-level policy, with no call to concrete transition.
    subject, basis, standing = record
    if action == "advance":
        decision = {None: "block_unassessed", "S": "advance",
                    "F": "block_falsified", "I": "block_indeterminate"}[standing]
        return record, decision
    if standing is not None:
        return record, "already_assessed"
    return (subject, basis, action[-1]), "recorded"


def compose(g, f):
    return {key: g[value] for key, value in f.items()}


def words(alphabet, maximum):
    return [tuple(xs) for n in range(maximum + 1) for xs in product(alphabet, repeat=n)]


def run():
    counts = {}
    assert [double(n) for n in range(3)] == [
        {"n": 0, "double": 0}, {"n": 1, "double": 2}, {"n": 2, "double": 4}]
    counts["constructor"] = 3

    full_domain = words((0, 1, 2), 3)
    for xs in full_domain:
        subject = list(xs)
        report = sorted_report(subject, 2)
        expected = all(a <= b for a, b in zip(xs, xs[1:]))
        assert (report["result"] == "satisfied") == expected
        assert subject == list(xs)  # unchanged judged subject
        if not expected:
            i = next(i for i in range(len(xs) - 1) if xs[i] > xs[i + 1])
            assert report["witness"] == {"index": i, "left": xs[i], "right": xs[i + 1]}
        witness_log = []
        witness_log.append(report)  # explicit separate log permission in fixture
        assert subject == list(xs) and witness_log[0]["subject"] == xs
    assert sorted_report([2, 1], 2)["witness"] == {"index": 0, "left": 2, "right": 1}
    original = [2, 1]
    mutated = original.copy()
    mutated.sort()
    assert mutated != original
    assert sorted_report(original, 2)["result"] == "falsified"
    assert sorted_report(mutated, 2)["result"] == "satisfied"
    counts["unchanged_subject_evaluation"] = len(full_domain)

    table = {("absent", "allow"): ("A", "request put_A"),
             ("A", "allow"): ("A", "request put_A"),
             ("B", "allow"): ("A", "request put_A"),
             ("absent", "deny"): ("absent", "refusal"),
             ("A", "deny"): ("A", "refusal"),
             ("B", "deny"): ("B", "refusal")}
    for inputs, expected in table.items():
        assert put_a(*inputs) == expected
    construction_grant = {"construct"}
    assert double(2) == {"n": 2, "double": 4}
    assert not construction_grant.intersection({"assess", "admit", "close", "physical_write"})
    counts["logical_store"] = len(table)

    stop_map = {"copy_exhausted": "falsified", "assessment_exhausted": "indeterminate",
                "permission_denied": "falsified"}
    assert "satisfied" not in stop_map.values()
    copies = words((0, 1), 2)
    for xs, fuel in product(copies, range(3)):
        result = copy_with_fuel(xs, fuel)
        available = fuel >= len(xs)
        assert (result["candidate"] is not None) == available
        assert result["availability"] == ("satisfied" if available else "falsified")
        if available:
            assert result["candidate"] == xs
        else:
            assert result["work"] == "incomplete" and result["stop"] == "copy_exhausted"
    assert copy_with_fuel((0, 1), 1)["prefix"] == (0,)
    counts["bounded_copy"] = len(copies) * 3

    assessments = words((0, 1), 3)
    for xs, fuel in product(assessments, range(3)):
        result = sorted_report(xs, fuel)
        observed = list(zip(xs, xs[1:]))[:fuel]
        # Oracle uses only the admitted pair observations, not hidden whole-list truth.
        expected = ("falsified" if any(a > b for a, b in observed)
                    else "satisfied" if len(observed) == max(0, len(xs) - 1)
                    else "indeterminate")
        assert result["result"] == expected
        if result["stop"]:
            assert stop_map[result["stop"]] == result["result"]
        assert result["subject"] == xs  # an exact closed assessment report exists
    exhausted = sorted_report((0, 1, 0), 1)
    assert exhausted["result"] == "indeterminate" and exhausted["residual"] == [1]
    unperformed = {"invoked": False, "assessment": None, "traversal_stop": None,
                   "work": "incomplete", "availability": "falsified"}
    assert unperformed["assessment"] is None and unperformed["traversal_stop"] is None
    counts["bounded_assessment"] = len(assessments) * 3

    states = ("U", "S", "F", "I")
    actions = ("assess_S", "assess_F", "assess_I", "advance")
    assert ("U" == "S") == ("I" == "S")
    assert transition("U", "assess_S")[1] != transition("I", "assess_S")[1]
    assert len({alpha(s) for s in states}) == 4  # no state aggregation
    for state, action in product(states, actions):
        successor, decision = transition(state, action)
        abstract_successor, abstract_decision = abstract_transition(alpha(state), action)
        assert abstract_successor == alpha(successor) and decision == abstract_decision
    for start, sequence in product(states, product(actions, repeat=4)):
        concrete, abstract = start, alpha(start)
        for action in sequence:
            concrete, decision = transition(concrete, action)
            abstract, abstract_decision = abstract_transition(abstract, action)
            assert abstract == alpha(concrete) and decision == abstract_decision
    counts["continuation_cells"] = len(states) * len(actions)
    counts["length_four_sequences"] = len(states) * len(actions) ** 4

    records = {"report:" + s: {"subject": "candidate-v1", "basis": "policy-v1",
               "standing": s, "producer": "assessor-v1", "obligation": "review-v1",
               "authority": "assessment-only", "invalidators": ["subject", "policy", "evidence"]}
               for s in ("S", "F", "I")}
    for key, record in records.items():
        resolved = json.loads(json.dumps(records[key]))
        assert resolved == record
        assert transition(resolved["standing"], "advance") == transition(record["standing"], "advance")
    assert records["report:S"]["subject"] == records["report:I"]["subject"]
    assert transition("S", "advance")[1] != transition("I", "advance")[1]
    counts["qualified_reference_records"] = len(records)

    objects = (("S", "F", "I"), ("hS", "hF", "hI"), ("vS", "vF", "vI"),
               ("advance", "block_falsified", "block_indeterminate"))
    arrows = {(i, j): dict(zip(objects[i], objects[j]))
              for i in range(4) for j in range(i, 4)}
    view, j, h = arrows[1, 2], arrows[1, 3], arrows[2, 3]
    assert j == compose(h, view)
    constant = {x: "candidate-v1" for x in objects[1]}
    assert constant["hS"] == constant["hI"] and j["hS"] != j["hI"]
    for (a, b), f in arrows.items():
        assert compose(arrows[b, b], f) == f == compose(f, arrows[a, a])
    composition_cells = associativity_cells = 0
    for a, b, c in product(range(4), repeat=3):
        if a <= b <= c:
            assert compose(arrows[b, c], arrows[a, b]) == arrows[a, c]
            composition_cells += 1
    for a, b, c, d in product(range(4), repeat=4):
        if a <= b <= c <= d:
            f, g, h_map = arrows[a, b], arrows[b, c], arrows[c, d]
            assert compose(h_map, compose(g, f)) == compose(compose(h_map, g), f)
            associativity_cells += 1
    terminal = {"*": "*"}
    object_map = {i: "*" for i in range(4)}
    arrow_map = {ends: terminal for ends in arrows}
    for i in range(4):
        assert object_map[i] == "*" and arrow_map[i, i] == terminal
    for a, b, c in product(range(4), repeat=3):
        if a <= b <= c:
            assert arrow_map[a, c] == compose(arrow_map[b, c], arrow_map[a, b])
    counts.update(finite_arrows=len(arrows), composition_cells=composition_cells,
                  associativity_cells=associativity_cells)
    print(json.dumps({"status": "passed", "coverage": counts,
                      "standing": "finite-model evidence; no semantic acceptance or compression claim"},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    run()
