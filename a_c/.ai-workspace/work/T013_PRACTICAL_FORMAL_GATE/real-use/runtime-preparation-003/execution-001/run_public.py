#!/usr/bin/env python3
"""Retain one authorized Phase A public CLI call; never dispatch an actor."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import time

BASE = Path(__file__).resolve().parent
PYTHON = "/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12"
PRODUCT = Path("/Users/jim/src/apps/specification_methodology/a_c")
OPERATIONS = {"source.read", "context.assemble", "contract.preflight"}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arm", choices=("ungated", "gated"), required=True)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--label", required=True)
    args = parser.parse_args()
    request_path = args.request.resolve()
    if not request_path.is_relative_to(BASE / "requests"):
        raise ValueError("Request must be retained in this Phase A request territory")
    request = json.loads(request_path.read_bytes())
    if request.get("operation") not in OPERATIONS:
        raise ValueError("Phase A has no dispatch or actor invocation grant")
    if not re.fullmatch(r"[a-z0-9-]+", args.label):
        raise ValueError("Invalid observation label")
    target = BASE / "observations" / args.arm / args.label
    target.mkdir(parents=True, exist_ok=False)
    policy = BASE / "runtime" / args.arm / "policy.json"
    command = [PYTHON, "-B", str(PRODUCT / "build_tenants/graphify/code/ac_support.py"),
               "--policy", str(policy), "--policy-sha256", sha(policy),
               "--principal", "executive", "call", "--request", str(request_path)]
    started_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    start = time.monotonic()
    with (target / "response.json").open("xb") as stdout, (target / "stderr.log").open("xb") as stderr:
        process = subprocess.run(command, cwd=PRODUCT.parent,
                                 env=os.environ | {"PYTHONDONTWRITEBYTECODE": "1"},
                                 stdout=stdout, stderr=stderr, check=False)
    elapsed = time.monotonic() - start
    children = resource.getrusage(resource.RUSAGE_CHILDREN)
    parent = resource.getrusage(resource.RUSAGE_SELF)
    response = None
    parse_error = None
    try:
        response = json.loads((target / "response.json").read_bytes())
    except (ValueError, UnicodeError) as exc:
        parse_error = str(exc)
    observation = {
        "schema": "a_c.T013.phase-a-public-operation/1",
        "started_utc": started_utc,
        "finished_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "arm": args.arm, "operation": request["operation"], "command": command,
        "request_sha256": sha(request_path), "policy_sha256": sha(policy),
        "exit_code": process.returncode, "whole_invocation_wall_seconds": elapsed,
        "operator_elapsed_through_response_parse_seconds": time.monotonic() - start,
        "children_user_seconds": children.ru_utime,
        "children_system_seconds": children.ru_stime,
        "children_maxrss_bytes_darwin": children.ru_maxrss,
        "operator_maxrss_bytes_darwin": parent.ru_maxrss,
        "resource_scope": "One public CLI invocation and waited descendants; Darwin RUSAGE_CHILDREN aggregate high-water observation, not a per-stage or compiler physical-memory bound.",
        "response_sha256": sha(target / "response.json"),
        "response_bytes": (target / "response.json").stat().st_size,
        "stderr_sha256": sha(target / "stderr.log"),
        "response_status": response.get("status") if isinstance(response, dict) else None,
        "parse_error": parse_error, "actor_or_model_invocations": 0,
        "monetary_cost": None,
    }
    (target / "PROCESS.json").write_text(json.dumps(observation, indent=2) + "\n")
    print(json.dumps({"arm": args.arm, "operation": request["operation"],
                      "label": args.label, "exit_code": process.returncode,
                      "status": observation["response_status"], "wall_seconds": elapsed,
                      "refusal": response.get("refusal") if isinstance(response, dict) else parse_error}))
    if process.returncode != 0 or not isinstance(response, dict) or response.get("status") != "ok":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
