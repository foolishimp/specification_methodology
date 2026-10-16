"""Finite witnesses for common I5 requirements; no tenant qualification claim."""

import json
from fractions import Fraction
from itertools import product


def histogram(values):
    result = {}
    for value in values:
        result[value] = result.get(value, 0) + 1
    return result


def faulty_histogram(values):
    return {value: 1 for value in values}


def counts_match(values, result):
    # Predicate derived from the stated count obligation, using a distinct path.
    return set(values) == set(result) and all(
        result[value] == sum(item == value for item in values)
        for value in set(values)
    )


def weak_assertion_case():
    cases = [values for size in range(5) for values in product((-1, 0, 1), repeat=size)]
    assert len(cases) == 121
    defects = sum(not counts_match(values, faulty_histogram(values)) for values in cases)
    weak_passes = sum(set(values) == set(faulty_histogram(values)) for values in cases)
    assert all(counts_match(values, histogram(values)) for values in cases)
    assert defects == 105 and weak_passes == 121
    # Equal key observations conceal opposite truth for the same count obligation.
    values = (0, 0)
    good, bad = histogram(values), faulty_histogram(values)
    assert set(good) == set(bad)
    assert counts_match(values, good) and not counts_match(values, bad)
    return {"domain_cases": len(cases), "weak_check_passes": weak_passes,
            "faulty_outputs_rejected_by_count_predicate": defects,
            "correct_outputs_pass": len(cases), "observation_alias": True}


def composition_case():
    # Each local predicate holds, but its relation does not establish the next precondition.
    first_output = 1
    first_post = first_output >= 0
    second_pre = first_output > 1
    assert first_post and not second_pre
    # Necessary-condition success also fails to establish the stronger final target.
    local = first_output >= 0
    target = first_output == 2
    assert local and not target
    return {"missing_join_detected": True, "weak_final_condition_detected": True}


def correlation_case():
    # Declared finite model conditional on a fault: equiprobable shared causes.
    worlds = ("shared_miss", "shared_detect")
    m1 = [world == "shared_miss" for world in worlds]
    m2 = list(m1)
    marginal = Fraction(sum(m1), len(worlds))
    joint = Fraction(sum(a and b for a, b in zip(m1, m2)), len(worlds))
    assert marginal == Fraction(1, 2)
    assert joint == Fraction(1, 2) and joint != marginal * marginal
    assert joint == marginal * Fraction(1, 1)  # P(M2 | M1, fault) = 1.
    return {"joint_miss": str(joint), "unsupported_independent_product": str(marginal * marginal)}


def targeted_change_case():
    # Explicit toy validity model. These names are facts, not filenames.
    dependencies = {
        "sum": {"sum_obligation", "sum_implementation", "runtime"},
        "histogram": {"count_obligation", "hist_implementation", "count_oracle", "runtime"},
        "integration": {"sum_obligation", "count_obligation", "sum_implementation",
                        "hist_implementation", "count_oracle", "runtime"},
    }

    def select(changed, unknown=(), mandatory=()):
        return {name for name, facts in dependencies.items() if facts & changed} | set(unknown) | set(mandatory)

    values = (0, 0, 1)

    def evaluate_hist_and_join(result):
        return {
            "histogram": "satisfied" if counts_match(values, result) else "falsified",
            "integration": "satisfied" if counts_match(values, result)
            and sum(values) == sum(value * count for value, count in result.items()) else "falsified",
        }

    old_results = dict(evaluate_hist_and_join(faulty_histogram(values)),
                       sum="satisfied" if sum(values) == 1 else "falsified")
    assert old_results == {"sum": "satisfied", "histogram": "falsified", "integration": "falsified"}
    affected = select({"hist_implementation"})
    assert affected == {"histogram", "integration"}
    retained = {name: value for name, value in old_results.items() if name not in affected}
    assert retained == {"sum": "satisfied"}
    assert select({"count_obligation"}) == {"histogram", "integration"}
    assert select({"count_oracle"}) == {"histogram", "integration"}
    assert select({"runtime"}) == set(dependencies)
    assert select({"hist_implementation"}, unknown={"sum"}) == set(dependencies)
    assert select({"hist_implementation"}, mandatory={"sum"}) == set(dependencies)

    # Actual bounded re-execution after the repair; preserved sum check is separate.
    repaired = histogram(values)
    new_results = evaluate_hist_and_join(repaired)
    combined = dict(retained, **new_results)
    assert combined == dict.fromkeys(dependencies, "satisfied")
    assert old_results["histogram"] == "falsified"  # Historical evidence is not rewritten.
    return {"affected": sorted(affected), "retained": sorted(retained),
            "combined": combined, "prior_failure_preserved": True,
            "scope": "declared toy dependencies and one repaired input"}


if __name__ == "__main__":
    print(json.dumps({"standing": "bounded author witnesses, not universal proof or tenant use",
                      "weak_assertion": weak_assertion_case(),
                      "composition": composition_case(),
                      "correlation": correlation_case(),
                      "targeted_change": targeted_change_case()}, indent=2, sort_keys=True))
