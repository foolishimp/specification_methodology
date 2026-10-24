#!/usr/bin/env python3
"""Bounded fresh source-to-model operations; every effect consumes an exact grant."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / "release_tools"))
import application_contract as c
sys.path.insert(0, str(ROOT / "implementation/code"))
import ac_generate as g
import ac_grounding as h
import ac_repair as r

RUN = ROOT / "run"
PRIVATE = ROOT / "private"
OPERATIONS = ("prepare", "initial-batch", "remaining-batch", "retry-batch", "normalize", "repair-batch", "assemble")


def now():
    return datetime.now(timezone.utc).isoformat()


def actor_preflight(codex):
    c.implementation(ROOT)
    app = c.application(ROOT)
    settings = app["generation"]
    executable, overrides, metadata = g.actor_settings(codex, {"model": settings["model"],
        "model_reasoning_effort": settings["effort"], "service_tier": settings["service_tier"]})
    arguments = [piece for key, value in overrides.items() for piece in ("-c", key + "=" + json.dumps(value, ensure_ascii=False))]
    effective = json.loads(subprocess.check_output([executable, "mcp", "list", "--json", *arguments]))
    c.require(not any(row["enabled"] for row in effective), "actor MCP isolation failed")
    public = {"cli_version": metadata["cli_version"], "settings": metadata["settings"],
              "effective_mcp_inventory": [{"name": row["name"], "enabled": row["enabled"]} for row in effective],
              "model_call_performed": False,
              "python_source_parser_available": importlib.util.find_spec("tree_sitter_python") is not None}
    return metadata, public


def grant(path, expected_sha, operation):
    raw = Path(path).read_bytes()
    c.require(c.hex_digest(expected_sha) and c.sha(raw) == expected_sha, "generation grant digest differs")
    value = c.load(path)
    c.require(value["kind"] == "a_c.stdo301.generation-grant/1", "unsupported generation grant")
    c.require(isinstance(value["grant_id"], str) and value["grant_id"] and value["issuer"] == "/root", "explicit Root grant required")
    c.require(operation in value["operations"] and set(value["operations"]) <= set(OPERATIONS), "operation outside exact grant")
    c.require(type(value["max_new_calls"]) is int and value["max_new_calls"] >= 0, "explicit nonnegative call budget required")
    c.require(value.get("scheduler_sha256") == c.sha(Path(__file__).read_bytes()), "scheduler differs from the exact Root grant")
    c.check_sources(ROOT, value["source_contract_sha256"])
    return value


@contextmanager
def scheduler_lock():
    PRIVATE.mkdir(exist_ok=True)
    with (PRIVATE / "scheduler.lock").open("a") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise ValueError("another application operation is active") from error
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def runtime_paths():
    for name in ("tmp", "cache"):
        (PRIVATE / name).mkdir(exist_ok=True)
    os.environ.update(TMPDIR=str(PRIVATE / "tmp"), XDG_CACHE_HOME=str(PRIVATE / "cache"),
                      PYTHONDONTWRITEBYTECODE="1", GIT_OPTIONAL_LOCKS="0")


def checkpoint():
    c.check_sources(ROOT)
    plan, chunks = g.checkpoint(RUN)
    frozen = c.frozen(ROOT)
    manifest = c.load(ROOT / "source-manifest.json")
    c.require(plan["subject_id"] == frozen["subject_id"] and plan["files"] == c.inventory_rows(manifest["files"]), "generation source differs from frozen native payload")
    actual = [{key: segment[key] for key in ("id", "path", "start_line", "end_line", "sha256")}
              for chunk in chunks for segment in chunk["segments"]]
    c.require(actual == c.load(ROOT / "release_tools/source-sections.json")["sections"], "generation section partition differs")
    c.require(len(chunks) == frozen["chunk_count"], "generation chunk extent differs")
    settings = frozen["generation"]
    sections = [section for row in manifest["files"]
                for section in g.sections(row["path"], (ROOT / "source" / row["path"]).read_text(), frozen["subject_id"])]
    c.require(chunks == g.make_chunks(sections, settings["chunk_chars"]), "generation chunks differ from the frozen parameters/source")
    c.require(g.load(RUN / "source-manifest.json") == manifest, "generation manifest differs from frozen source")
    upstream = g.verify_upstream(Path(plan["upstream"]["root"]))
    c.require(upstream["commit"] == settings["upstream_commit"], "generation upstream differs from frozen contract")
    expected = {"profile": "ac.generation.plan/1", "mode": settings["mode"], "subject_id": frozen["subject_id"],
        "semantic_extraction_profile": g.SEMANTIC_PROFILES[settings["mode"]],
        "source_manifest_sha256": c.sha((RUN / "source-manifest.json").read_bytes()),
        "files": c.inventory_rows(manifest["files"]), "chunks_sha256": c.sha((RUN / "chunks.json").read_bytes()),
        "chunks": [{"id": chunk["id"], "segments": len(chunk["segments"]), "source_chars": chunk["source_chars"]} for chunk in chunks],
        "chunk_chars": settings["chunk_chars"], "graph_chars": settings["graph_chars"], "upstream": upstream,
        "runner_sha256": c.sha(Path(g.__file__).read_bytes()), "codec_sha256": c.sha((g.HERE / "ac_graph.py").read_bytes()),
        "assets": {path.name: c.sha(path.read_bytes()) for path in g.ASSETS.iterdir() if path.is_file()},
        "calculus": {"uri": g.ac_graph.CALCULUS_URI, "sha256": frozen["builder"]["calculus_sha256"]},
        "claim": "Fresh F_P proposal authoring; processing coverage is not semantic completeness or acceptance."}
    c.require(plan == expected, "generation plan differs from frozen contract and exact implementation")
    g.verify_discovery(RUN)
    return plan, chunks


def inventory(chunks):
    result = {chunk["id"]: r.call_inventory(RUN, chunk["id"]) for chunk in chunks}
    available = {(key, row["family"], row["attempt"]): row for key, calls in result.items() for row in calls}
    batches = PRIVATE / "batches"
    for folder in sorted(batches.iterdir()) if batches.exists() else []:
        plan = c.load(folder / "plan.json")
        result_path = folder / "result.json"
        state = c.load(result_path)["state"] if result_path.is_file() else "unclosed"
        for index, selection in enumerate(plan["selections"]):
            key = selection["chunk"]
            c.require(key in result, "scheduler reservation names an unknown chunk")
            family, attempt = selection.get("family", "author"), selection.get("attempt")
            row = available.pop((key, family, attempt), None)
            reservation = {"batch": folder.name, "selection": index, "state": state,
                           "plan_sha256": c.sha((folder / "plan.json").read_bytes()),
                           "result_sha256": c.sha(result_path.read_bytes()) if result_path.is_file() else None}
            if row is None:
                row = {"family": family, "attempt": attempt, "invocation_recorded": False,
                       "reservation_only": True}
                result[key].append(row)
            row["reservation"] = reservation
    c.require(all(len(calls) <= 3 for calls in result.values()), "shared three-call author/repair ceiling exceeded")
    return result


def status():
    plan, chunks = checkpoint()
    calls = inventory(chunks)
    strict, untouched, failures, handoffs = [], [], [], []
    for chunk in chunks:
        handoffs.extend({"chunk": chunk["id"], "attempt": row["attempt"], **row["reservation"]}
                        for row in calls[chunk["id"]] if "reservation" in row
                        and (row.get("reservation_only") or row["reservation"]["state"] in ("unclosed", "exception_stop")))
        if g.successful_attempt(RUN, "author", chunk):
            strict.append(chunk["id"])
        elif not calls[chunk["id"]]:
            untouched.append(chunk["id"])
        else:
            latest = h.latest_attempt(RUN, chunk)
            path = latest / "result.json" if latest else None
            failures.append({"chunk": chunk["id"], "latest_author": str(latest.relative_to(RUN)) if latest else None,
                             "result_sha256": c.sha(path.read_bytes()) if path and path.is_file() else None,
                             "calls_including_reservations": len(calls[chunk["id"]]),
                             "reservations": [row["reservation"] for row in calls[chunk["id"]] if "reservation" in row]})
    return {"kind": "a_c.stdo301.generation-status/1", "subject": plan["subject_id"], "chunks": len(chunks),
            "strict_originals": strict, "never_attempted": untouched, "non_strict_originals": failures,
            "calls_including_reservations": sum(map(len, calls.values())),
            "unclosed_or_exception_handoffs": handoffs,
            "state": "failure_stop" if failures or handoffs else ("authors_complete" if not untouched else "ready_for_next_batch"),
            "claim": "Strict-original status only; verified grounding derivations/repairs are separate and do not relabel originals."}


def require_acknowledged_failures(value, current):
    missing = [row for row in current["non_strict_originals"] if row["latest_author"] is None]
    for row in missing:
        reservations = row.get("reservations", [])
        c.require(reservations and all(item["state"] == "exception_stop" and item["result_sha256"] is not None
            and value.get("reconciled_batches", {}).get(item["batch"]) == item["result_sha256"] for item in reservations),
            "unfinished author requires explicit external reconciliation")
    expected = {row["latest_author"]: row["result_sha256"] for row in current["non_strict_originals"] if row["latest_author"] is not None}
    c.require(not any(key is None or digest is None for key, digest in expected.items()), "unfinished author requires explicit external reconciliation")
    acknowledged = value.get("acknowledged_failures", {})
    c.require(all(acknowledged.get(key) == digest for key, digest in expected.items()),
              "failure stop: Root must bind each failed original before continuing unrelated chunks")


def reserve(value, grant_sha, operation, selections):
    root = PRIVATE / "batches"
    root.mkdir(exist_ok=True)
    previous = sorted(root.iterdir())
    c.require(all((folder / "result.json").is_file() for folder in previous), "unfinished batch requires explicit external reconciliation")
    for prior in previous:
        if c.load(prior / "result.json")["state"] == "exception_stop":
            c.require(value.get("reconciled_batches", {}).get(prior.name) == c.sha((prior / "result.json").read_bytes()),
                      "exception stop: Root must bind the previous batch reconciliation")
    reservations = [item for prior in previous for item in c.load(prior / "plan.json")["selections"]]
    for selected in selections:
        c.require(sum(row["chunk"] == selected["chunk"] for row in reservations) < 3,
                  "shared three-call scheduler reservation ceiling exhausted")
    used = sum(len(c.load(folder / "plan.json")["selections"]) for folder in previous
               if c.load(folder / "plan.json")["grant_sha256"] == grant_sha)
    c.require(used + len(selections) <= value["max_new_calls"], "exact grant call budget exhausted")
    folder = root / f"batch-{len(previous) + 1:03d}"
    bound = []
    for selected in selections:
        family = selected.get("family", "author")
        c.require(family in ("author", "repair"), "unknown reservation family")
        parent = RUN / ("actors/author" if family == "author" else r.REPAIRS) / selected["chunk"]
        count = len(list(parent.iterdir())) if parent.exists() else 0
        attempt = (parent / f"attempt-{count + 1:03d}").relative_to(RUN).as_posix()
        c.require(not any(row.get("attempt") == attempt for row in reservations),
                  "unclosed reservation handoff cannot be reused; external reconciliation must preserve its history")
        bound.append({**selected, "family": family, "attempt": attempt})
    folder.mkdir()
    c.save(folder / "plan.json", {"kind": "a_c.stdo301.batch/1", "created_at": now(), "operation": operation,
        "grant_sha256": grant_sha, "grant_id": value["grant_id"], "selections": bound,
        "reconciled_batches": value.get("reconciled_batches", {}),
        "source_contract_sha256": value["source_contract_sha256"], "scheduler_sha256": c.sha(Path(__file__).read_bytes())})
    return folder


def author_one(plan, chunk, codex, settings):
    root = RUN / "actors/author" / chunk["id"]
    previous = sorted(root.iterdir()) if root.exists() else []
    attempt = root / f"attempt-{len(previous) + 1:03d}"
    result = g.run_actor(g.author_prompt(plan, chunk, RUN), g.ASSETS / "author.schema.json", attempt,
                         codex, 1800, settings)
    if result["status"] == "completed":
        try:
            g.author_check(g.load(attempt / "answer.json"), chunk)
            g.save(attempt / "validation.json", {"status": "structurally_valid_proposal",
                "answer_sha256": g.sha((attempt / "answer.json").read_bytes()), "chunk_sha256": g.digest(chunk),
                "claim": "Source coordinates and shape checked; semantic fitness unassessed."}, exclusive=True)
        except g.GenerationError as error:
            result["status"] = "failed"
            result["failures"].append("source_or_semantic_fragment_validation")
            result["validation_error"] = str(error)
            g.save(attempt / "result.json", result)
    if result["status"] == "completed":
        g.actor_evidence(RUN, plan, chunk, attempt, stage="author")
    return {"chunk": chunk["id"], "attempt": str(attempt.relative_to(RUN)), "status": result["status"],
            "failures": result["failures"], "result_sha256": c.sha((attempt / "result.json").read_bytes()),
            "elapsed_seconds": result["elapsed_seconds"], "usage_events": result["usage_events"]}


def author_batch(operation, value, grant_sha, codex, ids):
    plan, chunks = checkpoint()
    current = status()  # Rechecks exact completed actor evidence, never cached status.
    calls = inventory(chunks)
    if operation == "initial-batch":
        c.require(current["calls_including_reservations"] == 0, "initial batch is one-time only")
        c.require(not ids, "initial chunks follow the frozen plan")
        selected = chunks[:2]
    elif operation == "remaining-batch":
        c.require(current["calls_including_reservations"] > 0, "initial batch must close first")
        require_acknowledged_failures(value, current)
        c.require(not ids, "remaining batch selects the next never-attempted chunks")
        selected = [chunk for chunk in chunks if chunk["id"] in current["never_attempted"]][:2]
    else:
        c.require(ids and len(set(ids)) == len(ids) <= 2, "retry needs one or two distinct explicitly selected chunks")
        c.require(set(ids) <= set(value.get("retry_chunks", [])), "retry chunk outside Root grant")
        selected = [chunk for chunk in chunks if chunk["id"] in ids]
        c.require(len(selected) == len(ids), "unknown retry chunk")
        require_acknowledged_failures(value, current)
        c.require(all(chunk["id"] not in current["strict_originals"] and calls[chunk["id"]]
                      and not any(row["family"] == "repair" for row in calls[chunk["id"]]) for chunk in selected),
                  "retry cannot replace strict success or overtake a repair chain")
    c.require(selected, "no eligible author chunks")
    c.require(all(len(calls[chunk["id"]]) < 3 for chunk in selected), "shared three-call ceiling exhausted")
    metadata, public = actor_preflight(codex)
    fixed = {"settings": metadata["settings"], "cli_version": metadata["cli_version"]}
    settings_exist = (RUN / "actor-settings.json").exists()
    if settings_exist:
        c.require(g.load(RUN / "actor-settings.json") == fixed, "actor settings/CLI changed after first call")
        c.require(c.load(PRIVATE / "actor-configuration.json") == metadata, "actor configuration changed after first call")
    selections = [{"chunk": chunk["id"], "chunk_sha256": g.digest(chunk),
                   "prompt_sha256": c.sha(g.author_prompt(plan, chunk, RUN).encode()), "family": "author"} for chunk in selected]
    folder = reserve(value, grant_sha, operation, selections)
    try:
        if not settings_exist:
            c.save(RUN / "actor-settings.json", fixed)
            c.save(PRIVATE / "actor-configuration.json", metadata)
        with ThreadPoolExecutor(max_workers=2) as executor:
            results = list(executor.map(lambda chunk: author_one(plan, chunk, codex, metadata["settings"]), selected))
        result = {"closed_at": now(), "actor": public, "results": results,
                  "state": "batch_complete" if all(row["status"] == "completed" for row in results) else "failure_stop"}
        c.save(folder / "result.json", result)
        return {**result, "next_status": status()}
    except BaseException as error:
        if not (folder / "result.json").exists():
            c.save(folder / "result.json", {"closed_at": now(), "state": "exception_stop", "reason": str(error),
                                          "claim": "Batch may contain partial effects; inspect exact attempts before any further dispatch."})
        raise


def prepare(upstream):
    app = c.application(ROOT)
    paths = [row["path"] for row in c.load(ROOT / "source-manifest.json")["files"]]
    c.require(not any(Path(path).suffix in (".py", ".pyi") for path in paths)
              or importlib.util.find_spec("tree_sitter_python") is not None,
              "selected Python semantic source requires tree-sitter-python in the qualified environment; no source may be silently excluded")
    g.prepare(ROOT / "source", ROOT / "source-manifest.json", RUN, "graphify-ac", upstream,
              app["generation"]["chunk_chars"], app["generation"]["graph_chars"])
    g.build_discovery(RUN, upstream)
    plan, chunks = checkpoint()
    return {"state": "prepared", "plan_sha256": c.sha((RUN / "plan.json").read_bytes()), "chunks": len(chunks), "model_calls": 0}


def accounting():
    """Report actual retained counters; this is not a construction/review receipt."""
    plan, chunks = checkpoint()
    calls = inventory(chunks)
    rows, totals = [], {}
    for chunk in chunks:
        for call in calls[chunk["id"]]:
            row = {"chunk": chunk["id"], **call}
            if call.get("reservation_only"):
                row.update(status="unknown_reservation_handoff", usage=None)
                rows.append(row)
                continue
            attempt = RUN / call["attempt"]
            actor = attempt if call["family"] == "author" else attempt / "actor"
            if not (actor / "result.json").is_file():
                row.update(status="unfinished_or_reserved", usage=None)
            else:
                result = g.load(actor / "result.json")
                c.require(c.sha((actor / "events.jsonl").read_bytes()) == result["events_sha256"]
                          and c.sha((actor / "stderr.txt").read_bytes()) == result["stderr_sha256"], "retained actor events/stderr changed")
                observed = []
                invalid = 0
                for line in (actor / "events.jsonl").read_text().splitlines():
                    try:
                        event = json.loads(line)
                    except ValueError:
                        invalid += 1
                        continue
                    if event.get("type") == "turn.completed" and "usage" in event:
                        observed.append(event["usage"])
                c.require(observed == result["usage_events"] == g.load(actor / "usage.json")["usage_events"], "reported actor usage differs from retained events")
                c.require(bool(invalid) == ("invalid_event_json" in result["failures"]), "invalid-event accounting differs")
                row.update(status=result["status"], failures=result["failures"], usage=observed,
                           elapsed_seconds=result["elapsed_seconds"], cli_version=result["cli_version"],
                           settings={key: result["settings"][key] for key in g.SETTING_KEYS if key in result["settings"]},
                           result_sha256=c.sha((actor / "result.json").read_bytes()), answer_sha256=result["answer_sha256"],
                           events_sha256=result["events_sha256"], stderr_sha256=result["stderr_sha256"])
                for usage in observed:
                    for name, number in usage.items():
                        if type(number) in (int, float):
                            totals[name] = totals.get(name, 0) + number
            rows.append(row)
    return {"kind": "a_c.stdo301.actual-call-account/1", "subject": plan["subject_id"], "attempts": rows,
            "reported_scalar_counter_totals": totals, "calls_including_reservations": len(rows),
            "actual_invocations_recorded": sum(row["invocation_recorded"] for row in rows),
            "complete_attempt_account": all(row["status"] not in ("unfinished_or_reserved", "unknown_reservation_handoff")
                and row.get("reservation", {}).get("state") not in ("unclosed", "exception_stop") for row in rows),
            "claim": "Retained actual actor usage only, including failures. No prices, accepted-result benefit, semantic acceptance, review or construction receipt is inferred. Nested counters remain explicit in each usage record; scalar totals are not a billing formula."}


def repair_batch(value, grant_sha, codex, ids):
    plan, chunks = checkpoint()
    c.require(ids and len(set(ids)) == len(ids) <= 2 and set(ids) <= set(value.get("repair_chunks", [])), "repair needs one or two Root-selected chunks")
    by_id = {chunk["id"]: chunk for chunk in chunks}
    c.require(set(ids) <= set(by_id), "unknown repair chunk")
    calls = inventory(chunks)
    c.require(all(len(calls[key]) < 3 for key in ids), "shared three-call ceiling exhausted")
    metadata, _ = actor_preflight(codex)
    c.require(c.load(PRIVATE / "actor-configuration.json") == metadata, "actor configuration changed")
    # No implicit repair chaining: a later chain requires its explicit parent path in the grant.
    parents = value.get("repair_parents", {})
    selections = [{"chunk": key, "family": "repair", "parent": parents.get(key)} for key in ids]
    folder = reserve(value, grant_sha, "repair-batch", selections)
    try:
        attempts = [r.prepare(RUN, key, parent_repair=Path(parents[key]) if key in parents else None) for key in ids]
        with ThreadPoolExecutor(max_workers=2) as executor:
            journals = list(executor.map(lambda attempt: r.execute(RUN, attempt, codex=codex, timeout=1800), attempts))
        result = {"closed_at": now(), "state": "batch_complete" if all(journal["status"] == "complete_patch" for journal in journals) else "failure_stop",
                  "repairs": [{"chunk": key, "attempt": str(attempt.relative_to(RUN)), "status": journal["status"]}
                              for key, attempt, journal in zip(ids, attempts, journals)]}
        c.save(folder / "result.json", result)
        return result
    except BaseException as error:
        c.save(folder / "result.json", {"closed_at": now(), "state": "exception_stop", "reason": str(error)})
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("preflight", "status", "accounting", *OPERATIONS))
    parser.add_argument("--grant", type=Path)
    parser.add_argument("--grant-sha256")
    parser.add_argument("--codex", default="/Users/jim/bin/codex")
    parser.add_argument("--upstream", type=Path)
    parser.add_argument("--chunk", action="append", default=[])
    parser.add_argument("--normalization-directory", default="normalization")
    args = parser.parse_args()
    try:
        if args.operation == "preflight":
            _, result = actor_preflight(args.codex)
            if args.upstream:
                result["upstream"] = g.verify_upstream(args.upstream)["commit"]
        elif args.operation == "status":
            result = status()
        elif args.operation == "accounting":
            result = accounting()
        else:
            c.require(args.grant is not None and args.grant_sha256 is not None, "effect requires exact Root grant path and SHA256")
            value = grant(args.grant, args.grant_sha256, args.operation)
            with scheduler_lock():
                runtime_paths()
                if args.operation == "prepare":
                    c.require(args.upstream is not None, "prepare requires exact upstream checkout")
                    result = prepare(args.upstream)
                elif args.operation in ("initial-batch", "remaining-batch", "retry-batch"):
                    result = author_batch(args.operation, value, args.grant_sha256, args.codex, args.chunk)
                elif args.operation == "repair-batch":
                    result = repair_batch(value, args.grant_sha256, args.codex, args.chunk)
                elif args.operation == "normalize":
                    plan, chunks = checkpoint()
                    c.require(args.chunk and set(args.chunk) <= {row["id"] for row in chunks}, "normalize requires explicit known chunks")
                    result = {"state": "normalization_closed", "results": [h.normalize(RUN, name=args.normalization_directory, chunk_id=key) for key in args.chunk]}
                else:
                    _, chunks = checkpoint()
                    inventory(chunks)
                    # This complete assembler accepts strict originals and exact verified recovery lineages.
                    result = r.assemble(RUN, normalization_name=args.normalization_directory, allow_partial=False, upstream=args.upstream)
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 3 if result.get("state") in ("failure_stop", "exception_stop") else 0
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        print(json.dumps({"state": "refused", "reason": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
