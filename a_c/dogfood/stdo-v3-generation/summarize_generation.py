#!/usr/bin/env python3
"""Summarize retained generation evidence; never infer billing or acceptance."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIELDS = (
    "input_tokens", "cached_input_tokens", "cache_write_input_tokens",
    "output_tokens", "reasoning_output_tokens",
)


def load(path: Path):
    return json.loads(path.read_text())


def summarize_run(root: Path) -> dict:
    plan = load(root / "plan.json")
    attempts = []
    totals = Counter()
    field_events = Counter()
    original_invocations = list((root / "actors").rglob("invocation.json")) if (root / "actors").exists() else []
    repair_invocations = list((root / "grounding-repairs").glob("*/attempt-*/actor/invocation.json")) if (root / "grounding-repairs").exists() else []
    for invocation in sorted(original_invocations + repair_invocations):
        folder = invocation.parent
        is_repair = folder.name == "actor" and folder.parent.parent.parent.name == "grounding-repairs"
        path = folder / "result.json"
        result = load(path) if path.exists() else None
        item = {
            "path": str(folder.relative_to(ROOT)),
            "stage": "grounding-repair" if is_repair else folder.parent.parent.name,
            "chunk": folder.parent.parent.name if is_repair else folder.parent.name,
            "status": result["status"] if result else "in_progress_or_interrupted",
            "validated": (folder / "validation.json").exists(),
            "usage_reported": bool(result and result.get("usage_events")),
            "elapsed_seconds": result.get("elapsed_seconds") if result else None,
            "failures": result.get("failures", []) if result else [],
            "validation_error": result.get("validation_error") if result else None,
        }
        if result:
            item["result_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            for event in result.get("usage_events", []):
                for key in FIELDS:
                    if key in event:
                        value = event[key]
                        if isinstance(value, int) and not isinstance(value, bool) and value >= 0:
                            totals[key] += value
                            field_events[key] += 1
        if is_repair:
            journal_path = folder.parent / "journal.json"
            item["repair_journal"] = load(journal_path) if journal_path.exists() else None
        attempts.append(item)
    known = sum(item["usage_reported"] for item in attempts)
    completed = {item["chunk"] for item in attempts if item["stage"] == "author" and item["status"] == "completed" and item["validated"]}
    proposal_paths = [root / name / "result.json" for name in ("proposal", "grounded-proposal", "repaired-proposal")]
    present = [path for path in proposal_paths if path.exists()]
    if len(present) > 1:
        raise ValueError("Multiple final proposals require explicit disposition: " + str(root))
    proposal_path = present[0] if present else None
    proposal = load(proposal_path) if proposal_path else None
    first = [item for item in attempts if item["stage"] == "author" and Path(item["path"]).name == "attempt-001"]
    normalizations = []
    for path in sorted(root.glob("normalization*/*/journal.json")):
        journal = load(path)
        if journal.get("profile") != "ac.generation.grounding-normalization/1":
            continue
        normalizations.append({
            "path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "chunk": journal["chunk"], "status": journal["status"],
            "changes": len(journal["changes"]), "refusal": journal.get("refusal"),
            "original_attempt": journal.get("original_evidence", {}).get("original_attempt"),
            "fd_elapsed_seconds": journal.get("fd_elapsed_seconds"),
            "new_fp_calls": 0,
        })
    discovery_path = root / "discovery" / "result.json"
    discovery = load(discovery_path) if discovery_path.exists() else None
    return {
        "subject": plan["subject_id"], "mode": plan["mode"],
        "plan_sha256": hashlib.sha256((root / "plan.json").read_bytes()).hexdigest(),
        "planned_chunks": len(plan["chunks"]), "validated_author_chunks": len(completed),
        "source_files": len(plan["files"]), "source_bytes": sum(f["bytes"] for f in plan["files"]),
        "attempts": attempts, "attempt_count": len(attempts),
        "strict_first_attempt_states": dict(Counter(item["status"] for item in first)),
        "strict_first_attempt_validated": sum(item["validated"] for item in first),
        "fp_repair_calls": sum(item["stage"] == "grounding-repair" for item in attempts),
        "attempts_with_usage": known, "attempts_without_usage": len(attempts) - known,
        "reported_usage_totals": {key: totals[key] if field_events[key] else None for key in FIELDS},
        "reported_usage_field_event_counts": dict(field_events),
        "sum_recorded_actor_seconds": sum(item["elapsed_seconds"] or 0 for item in attempts),
        "timing_scope": "Sum of completed actor elapsed intervals, including failed attempts; not concurrent wall time.",
        "normalization_journals": normalizations,
        "sum_recorded_normalization_seconds": sum(row["fd_elapsed_seconds"] for row in normalizations if isinstance(row["fd_elapsed_seconds"], (int, float)) and not isinstance(row["fd_elapsed_seconds"], bool)),
        "normalization_timing_scope": "Sum of recorded journal-creation intervals, including refusals; unrecorded verification/orchestration/engineering time is not claimed.",
        "normalization_scope": "Separate F_D source-locator recovery; original failures and usage remain in attempt totals.",
        "discovery": discovery, "proposal": proposal,
        "proposal_path": str(proposal_path.parent.relative_to(ROOT)) if proposal_path else None,
        "proposal_file_bytes": {p.name: p.stat().st_size for p in proposal_path.parent.iterdir() if p.is_file()} if proposal_path else None,
        "state": "proposed" if proposal else "incomplete_generation",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    runs = []
    for candidate in ("codex", "claude"):
        for mode in ("graphify-ac", "direct"):
            root = ROOT / "runs-v2" / candidate / mode
            if (root / "plan.json").exists():
                runs.append({"candidate": candidate, **summarize_run(root)})
    result = {
        "profile": "ac.generation.results/2", "runs": runs,
        "claim_boundary": [
            "All retained source-generation attempts are included, including failures and repairs.",
            "Unreported usage remains unknown; totals cover reported counters only.",
            "Reasoning is reported separately and is not added to output tokens again.",
            "Cached input subtraction is not a billing formula; no dollars are inferred.",
            "Synthetic smokes, engineering, oracle and assessment costs are separate.",
            "Supported mechanical grounding recovery creates no new F_P usage and does not erase strict first-pass failures.",
            "Conditional F_P grounding repairs are counted as model calls, including their failed outcomes and usage; unchanged statement bytes do not prove equivalence.",
            "A complete structural proposal does not establish semantic fidelity or owner acceptance.",
            "One repeat per treatment/candidate does not establish a population timing effect.",
        ],
    }
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
