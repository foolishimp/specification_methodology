#!/usr/bin/env python3
"""Classify retained drafts and emit explicit next-call selections; no effects."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parents[1] / "build_tenants/graphify/code"))
import ac_generate as g
import ac_grounding as h
import ac_repair as r


def classify(output, chunk):
    plan, _ = r.choose_chunk(output, chunk["id"])
    inventory = r.call_inventory(output, chunk["id"])
    budget = len(inventory)
    folder = output / r.REPAIRS / chunk["id"]
    repairs = sorted(folder.glob("attempt-*"))
    parent = None
    if repairs:
        last = repairs[-1]
        if not (last / "journal.json").exists():
            if not (last / "actor").exists():
                r.verify_request(output, last)
                return "prepared_repair", {"prepared_attempt": str(last.relative_to(output))}, None, budget
            return "unfinished_repair", None, None, budget
        answer, journal = r.verify(output, last, require_complete=False)
        if journal["status"] == "complete_patch":
            return "complete_repair", None, None, budget
        if answer is not None and journal["status"] == "incomplete_patch":
            parent = {"kind": "repair", "path": str(last.relative_to(output))}
    if parent is None:
        try:
            original = h.latest_attempt(output, chunk)
        except h.GroundingError:
            return "unfinished_author", None, None, budget
        if original is None:
            return "unstarted_author", None, None, budget
        try:
            answer, _ = h.evidence(output, plan, chunk, original)
        except (h.GroundingError, g.GenerationError, OSError, ValueError) as exc:
            result = g.load(original / "result.json")
            retryable = {"process_timeout", "cli_nonzero_exit", "missing_backend_usage", "output_schema_failure", "invalid_event_json"}
            failures = set(result.get("failures", []))
            if result.get("status") != "failed" or not failures or not failures <= retryable:
                raise  # Custody/isolation/configuration failures require diagnosis.
            for filename, field in (("answer.json", "answer_sha256"), ("events.jsonl", "events_sha256"), ("stderr.txt", "stderr_sha256")):
                path = original / filename
                if result.get(field) is not None:
                    g.require(path.is_file() and g.sha(path.read_bytes()) == result[field], "failed actor evidence changed: " + filename)
            return ("needs_fresh_author" if budget < r.LIMIT else "exhausted_author"), None, str(exc), budget
        try:
            _, changes = h.normalize_answer(answer, chunk)
            return ("fd_recoverable" if changes else "strict_original"), None, None, budget
        except (h.GroundingError, g.GenerationError):
            parent = {"kind": "author", "path": str(original.relative_to(output))}
    try:
        answer, _ = r.parent_draft(output, plan, chunk, parent)
        r.preflight(answer, chunk)
    except (r.RepairError, h.GroundingError, g.GenerationError, OSError, ValueError) as exc:
        return ("needs_fresh_author" if budget < r.LIMIT and not repairs else "unsupported_or_exhausted"), None, str(exc), budget
    if budget >= r.LIMIT:
        return "exhausted_grounding", None, None, budget
    return "needs_fp_repair", ({"parent_repair": parent["path"]} if parent["kind"] == "repair" else {}), None, budget


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    rows, repair_selection, author_selection = [], [], []
    any_repairs = bool(list((ROOT / "runs-v2").glob("*/*/grounding-repairs/*/attempt-*")))
    for candidate in ("codex", "claude"):
        for mode in ("graphify-ac", "direct"):
            output = ROOT / "runs-v2" / candidate / mode
            _, chunks = g.checkpoint(output)
            for chunk in chunks:
                item = {"candidate": candidate, "mode": mode, "chunk": chunk["id"]}
                try:
                    status, extra, diagnostic, budget = classify(output, chunk)
                except (r.RepairError, h.GroundingError, g.GenerationError, OSError, ValueError) as exc:
                    rows.append({**item, "status": "evidence_error", "diagnostic": str(exc)})
                    continue
                rows.append({**item, "status": status, "calls_or_reservations": budget, "diagnostic": diagnostic})
                if status in ("needs_fp_repair", "prepared_repair"):
                    repair_selection.append({**item, **extra})
                if status == "needs_fresh_author":
                    author_count = len(list((output / "actors/author" / chunk["id"]).glob("attempt-*")))
                    author_selection.append({**item, "attempt": author_count + 1})
    result = {"profile": "ac.generation.next-work-plan/1", "states": dict(Counter(row["status"] for row in rows)),
              "rows": rows, "repair_selection": repair_selection, "fresh_author_selection": author_selection,
              "fresh_author_coordinator_allowed": not any_repairs,
              "claim": "Mechanical eligibility only. Initial coordinator must close before repairs; old author-only coordinator is excluded after repair reservations begin. Evidence errors require diagnosis, not replacement calls."}
    text = json.dumps(result, indent=2) + "\n"
    if args.out:
        args.out.open("x").write(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
