"""Replay only the frozen returned T2 function; emit independent probe evidence."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


RETURN_COMMIT = "28e46fdd0d751f23f3ae93ea107d05efd393606d"
ANSWER_PATH = (
    "specification_methodology/v3/build_tenants/codex/qualification/C3/"
    "iteration-3/review-repair/use/runs/T2/ANSWER.md"
)
ANSWER_SHA256 = "677ad83cc49ed43295bd0dcd611c53d11c5e0a74a89d54a879ae0d67d51d1673"


def main():
    # This script is stored inside the selected worktree; no live source is read.
    repository = Path(__file__).resolve().parents[10]
    answer_bytes = subprocess.check_output(
        ["git", "show", RETURN_COMMIT + ":" + ANSWER_PATH], cwd=repository
    )
    assert hashlib.sha256(answer_bytes).hexdigest() == ANSWER_SHA256
    blocks = re.findall(r"```python\n(.*?)```", answer_bytes.decode(), re.S)
    code = next(block for block in blocks if block.startswith("def build_dockets("))
    namespace = {}
    exec(compile(code, "frozen-T2-return", "exec"), namespace)
    function = namespace["build_dockets"]

    cases = [
        (
            "B1",
            (("R17", "high"), ("R18", "unknown"), ("R19", "low"), ("R20", "unknown")),
            {"outcome": "planned", "dockets": {"isolation": ["R17"], "service": ["R19"], "inspection": ["R18", "R20"]}},
        ),
        (
            "B2",
            (("R17", "high"), ("R19", "low"), ("R17", "low")),
            {"outcome": "rejected", "reason": "duplicate_id", "request_id": "R17", "positions": (1, 3)},
        ),
        (
            "mixed_order",
            (("H2", "high"), ("U2", "unknown"), ("L2", "low"), ("H1", "high"), ("L1", "low"), ("U1", "unknown")),
            {"outcome": "planned", "dockets": {"isolation": ["H2", "H1"], "service": ["L2", "L1"], "inspection": ["U2", "U1"]}},
        ),
        (
            "same_risk_duplicate",
            (("U", "unknown"), ("U", "unknown")),
            {"outcome": "rejected", "reason": "duplicate_id", "request_id": "U", "positions": (1, 2)},
        ),
        (
            "late_duplicate_after_all_risks",
            (("H", "high"), ("L", "low"), ("U", "unknown"), ("Z", "low"), ("L", "high")),
            {"outcome": "rejected", "reason": "duplicate_id", "request_id": "L", "positions": (2, 5)},
        ),
        (
            "empty_admitted_batch",
            (),
            {"outcome": "planned", "dockets": {"isolation": [], "service": [], "inspection": []}},
        ),
    ]
    results = []
    for name, batch, expected in cases:
        before = repr(batch)
        docket_local_observed = []

        def trace(frame, event, arg):
            if frame.f_code is function.__code__ and "dockets" in frame.f_locals:
                docket_local_observed.append(event)
            return trace

        sys.settrace(trace)
        try:
            observed = function(batch)
        finally:
            sys.settrace(None)
        checks = {
            "exact_result": observed == expected,
            "input_preserved": repr(batch) == before,
        }
        if expected["outcome"] == "rejected":
            checks["no_returned_docket"] = "dockets" not in observed
            checks["no_docket_local_constructed"] = not docket_local_observed
        passed = all(checks.values())
        results.append({"name": name, "batch": batch, "expected": expected, "observed": observed, "checks": checks, "status": "passed" if passed else "failed"})

    report = {
        "assessment": "EC-CODEX-I3-03 independent T2 replay",
        "return_commit": RETURN_COMMIT,
        "answer_path": ANSWER_PATH,
        "answer_sha256": ANSWER_SHA256,
        "function_sha256": hashlib.sha256(code.encode()).hexdigest(),
        "python": sys.version,
        "scope": "Frozen returned function, six finite immutable tuple probes; no task effects or network calls.",
        "original_execution_provenance": "This independent replay does not authenticate the actor's original reported process execution.",
        "results": results,
        "counts": {"passed": sum(r["status"] == "passed" for r in results), "failed": sum(r["status"] == "failed" for r in results)},
    }
    print(json.dumps(report, indent=2))
    return 0 if all(r["status"] == "passed" for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
