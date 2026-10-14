#!/usr/bin/env python3
"""Prepare bounded same-evidence grader inputs; never execute an actor."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_text())


def between(text, start, end):
    return text[text.index(start):text.index(end, text.index(start))]


def actor_json(path):
    raw = path.read_text().strip()
    if raw.startswith("```"):
        match = re.fullmatch(r"```json\s*\n(.*)\n```", raw, re.S)
        if not match:
            raise ValueError(f"Unexpected actor carrier: {path}")
        raw = match.group(1)
    return json.loads(raw)


def tree(root):
    return {str(p.relative_to(root)): p.read_bytes()
            for p in sorted(root.rglob("*")) if p.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--prefix", required=True)
    args = parser.parse_args()
    trial = args.directory.resolve()
    synthesis = trial.parent
    repo = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
    source_path = "specification_methodology/v3/build_tenants/codex/successor/standards/FOUNDATIONS.md"
    source_bytes = subprocess.check_output(["git", "show", args.source_commit + ":" + source_path], cwd=repo)
    source = source_bytes.decode()
    workspace = between(source, "## Workspace and context", "## Bounded construction")
    excerpts = [
        ("Result: verdict, performance and effects", between(source, "The verdict has exactly these values:", "A refined value is the pair")),
        ("Result: candidate predicates", between(source, "Candidate availability, candidate fitness", "A lawful yield")),
        ("Conjunction: authentication, coverage and decision", between(source, "First authenticate each contribution", "The composite declaration distinguishes")),
        ("Workspace: reality and acquisition", between(workspace, "## Workspace and context", "An observation binds its source")),
        ("Workspace: reuse and recovery", workspace[workspace.index("Reuse requires supported applicability"):]),
    ]
    oracle_path = synthesis / "runs/oracle/ORACLE.json"
    oracle_sha = digest(oracle_path.read_bytes())
    oracle = load(oracle_path)
    report = load(trial / "APPLICATION_REPORT.json")
    assert report["candidate_commit"] == args.source_commit
    assert report["oracle_sha256"] == oracle_sha and report["oracle_unchanged"]
    retained_reports = {"C1", "C2", "C3", "C3b", "C8", "D1"}
    instruction = f"""Independently grade ten fresh actor returns against the fixed oracle and supplied exact source excerpts at {args.source_commit}. Assess each case as supported / finding / indeterminate, with a precise counterexample for each finding. Distinguish application or test success from semantic correctness and distinguish actor claims from later host evidence. Do not invent a review, alter the oracle, excuse an unsupported claim, or infer current release acceptance. Output at most 1800 words: one compact row per case, then material findings and scope limits. No source restatement or long essay.

Evidence projection: original task/workspace and every expected/forbidden oracle condition; every edit and structured actor result; full actor reports only where the oracle expressly checks report content (C1,C2,C3,C3b,C8,D1). Four other narrative reports and oracle rationale commentary are omitted; grade the supplied edits/results, not unseen prose. Source excerpts are exact but selected; unused algebra/refinement clauses are omitted. Host scripts independently confirmed after = original workspace plus full replacements, original inputs/provider outputs unchanged, and exact grants. Counts are host checks, not semantic verdicts. Applied bodies are represented once as replacements. Execution rows are [name, actual exit, expected exit, required diagnostic, stdout]; commands and full traces remain in ASSERTIONS.json. No external service was invoked. Missing execution rows mean no subprocess; record-level checks can still occur. Aggregate host counts: {compact(report['totals'])}.
"""
    pieces = [instruction]
    for label, excerpt in excerpts:
        pieces.append("\nEXACT SOURCE: " + label + "\n" + excerpt)
    inputs = []
    for case in oracle["cases"]:
        directory = trial / case["id"]
        inp, task, application, assertions = (load(directory / n) for n in ("INPUT.json", "TASK.json", "APPLY.json", "ASSERTIONS.json"))
        assert inp["candidate_commit"] == args.source_commit == application["candidate_commit"] == assertions["candidate_commit"]
        assert inp["oracle_sha256"] == assertions["oracle_sha256"] == oracle_sha
        assert task == {k: case[k] for k in ("id", "task", "workspace")}
        assert application["application_status"] == "applied" and application["inputs_unchanged"]
        for name, entry in application["inputs_before"].items():
            assert digest((directory / name).read_bytes()) == entry["sha256"], (case["id"], name)
        actor = actor_json(directory / "actor/RESULT.md")
        expected = {k: v.encode() for k, v in case["workspace"].items()}
        assert tree(directory / "workspace") == expected
        for edit in actor["edits"]:
            expected[edit["path"]] = edit["content"].encode()
        actual = tree(directory / "after")
        assert actual == expected, case["id"]
        projected_actor = {k: actor[k] for k in ("edits", "results")}
        report_included = case["id"].split("-", 1)[0] in retained_reports
        if report_included:
            projected_actor["report"] = actor["report"]
        host = {
            "counts": assertions["counts"],
            "failed_checks": [v for v in assertions["checks"] if v["status"] != "met"],
            "executions": [[e["name"], e["returncode"], e["expected_returncode"], e["required_stderr_fragment"], e["stdout"]] for e in assertions["executions"]],
        }
        block = "\nCASE " + case["id"] + "\nORACLE " + compact({k: v for k, v in case.items() if k != "rationale"}) + "\nACTOR " + compact(projected_actor) + "\nHOST " + compact(host) + "\n"
        pieces.append(block)
        manifest = {k: digest(v) for k, v in actual.items()}
        inputs.append({"case": case["id"], "bytes": len(block.encode()), "report_included": report_included, "actor_result_sha256": digest((directory / "actor/RESULT.md").read_bytes()), "assertions_sha256": digest((directory / "ASSERTIONS.json").read_bytes()), "applied_tree_sha256": digest(compact(manifest).encode())})
    body = "".join(pieces)
    prompts = [(synthesis / "prompts" / f"{args.prefix}-{n}.txt", f"Independent grader {n}.\n" + body) for n in (1, 2)]
    max_bytes = max(len(content.encode()) for _, content in prompts)
    if max_bytes > 80000:
        raise ValueError(f"Packet is {max_bytes} bytes, exceeds 80000; no output written")
    for path, content in prompts:
        path.parent.mkdir(exist_ok=True)
        path.write_text(content)
    metadata = {
        "candidate_commit": args.source_commit, "oracle_sha256": oracle_sha,
        "source_path": source_path, "source_sha256": digest(source_bytes),
        "common_packet_sha256": digest(body.encode()), "packet_body_bytes": len(body.encode()),
        "same_evidence_for_both": True, "prompt_byte_cap": 80000,
        "case_inputs": inputs,
        "prompts": [{"path": str(path.relative_to(synthesis)), "bytes": len(content.encode()), "sha256": digest(content.encode())} for path, content in prompts],
        "projection": instruction,
        "standing": "Prepared only; no paid calls, grading results or semantic acceptance.",
    }
    (trial / "GRADING_INPUTS.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps({"candidate_commit": args.source_commit, "cases": len(inputs), "prompt_bytes": max_bytes, "prompts": metadata["prompts"]}, indent=2))


if __name__ == "__main__":
    main()
