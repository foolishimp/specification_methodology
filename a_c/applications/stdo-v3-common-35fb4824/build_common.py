#!/usr/bin/env python3
"""Bounded application orchestration for the frozen common 35fb4824 subject.

This file selects no semantic meaning and changes no Product implementation.
Its first-batch command authorizes exactly two original author calls, no retry.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

APP = Path(__file__).resolve().parent
AC = APP.parents[1]
PROOF = AC / ".ai-workspace/qualification/t010/build"
CODE = APP / "build/implementation/code"
RUN = APP / "run"
PYTHON = AC / ".venv/bin/python"
UPSTREAM = Path("/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout")
PINS = {
    "source-manifest.json": "dbf32e7f99eb7228ca361ec02f44227c05e02bb6bc447d1dd38255cd3ca4a4d4",
    "package-custody.json": "6d35a6ad6472902294b1dfdd67c4e1e752ccc1b55ea4114acf10fb7389169af7",
    "source-classification.json": "20a17b4028e4c6c1dd595b23f6c5e1efa96f609a4d1e1fb6176a85c0e67f6e3e",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path):
    return json.loads(path.read_bytes())


def save(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def environment() -> dict[str, str]:
    paths = load(PROOF / "runtime-paths.json")
    env = dict(os.environ)
    env.update(TMPDIR=paths["tmpdir"], XDG_CACHE_HOME=paths["xdg_cache_home"],
               PYTHONDONTWRITEBYTECODE="1", GIT_OPTIONAL_LOCKS="0")
    os.environ.update({key: env[key] for key in
                       ("TMPDIR", "XDG_CACHE_HOME", "PYTHONDONTWRITEBYTECODE", "GIT_OPTIONAL_LOCKS")})
    return env


def guard() -> dict:
    signal = load(PROOF / "source-closed-signal.json")
    assert signal["pins"] == PINS and signal["model_call_limit"] == 2
    for name, pin in PINS.items():
        assert sha(APP / name) == pin, "source authority metadata drift: " + name
    custody = load(APP / "package-custody.json")
    assert custody["member_count"] == len(custody["members"]) == 81
    expected_paths = set()
    for member in custody["members"]:
        path = APP / "source" / member["path"]
        assert path.is_file() and not path.is_symlink() and path.resolve().is_relative_to((APP / "source").resolve())
        assert sha(path) == member["sha256"] and path.stat().st_size == member["bytes"], member["path"]
        expected_paths.add(member["path"])
    actual_paths = {path.relative_to(APP / "source").as_posix()
                    for path in (APP / "source").rglob("*") if path.is_file() or path.is_symlink()}
    assert actual_paths == expected_paths, "frozen source member set drift"
    manifest = load(APP / "source-manifest.json")
    assert manifest["member_count"] == len(manifest["files"]) == 58
    assert sum(member["bytes"] for member in manifest["files"]) == 2000888
    implementation = load(APP / "build/implementation-manifest.json")
    for member in implementation["files"]:
        path = APP / member["snapshot"]
        assert sha(path) == member["sha256"] and path.stat().st_size == member["bytes"], member["snapshot"]
    activation = load(PROOF / "activation.json")
    assert sha(AC / "stdo_a_c.json") == activation["basis"]["product_definition"], "Product Definition drift"
    release = Path("/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2")
    for key, relative in (("manifest", "manifest.json"), ("bootstrap", "standards/authority_compressions/stdo_bootstrap.md"),
                          ("calculus", "standards/AXIOMATIC_CALCULUS.md")):
        assert sha(release / relative) == activation["basis"][key], "builder basis drift: " + key
    return {"created_at": now(), "status": "exact", "package_members": 81, "semantic_members": 58,
            "source_manifest_sha256": PINS["source-manifest.json"],
            "implementation_manifest_sha256": sha(APP / "build/implementation-manifest.json")}


def generator():
    sys.path.insert(0, str(CODE))
    import ac_generate
    return ac_generate


def command(label: str, arguments: list[str]) -> dict:
    before = guard()
    env = environment()
    invocation = {"created_at": now(), "argv": [str(PYTHON), "-B", str(CODE / "ac_generate.py"), *arguments],
                  "cwd": str(AC), "before": before, "orchestrator_sha256": sha(Path(__file__))}
    save(PROOF / "commands" / (label + ".invocation.json"), invocation)
    stdout = PROOF / "commands" / (label + ".stdout.json")
    stderr = PROOF / "commands" / (label + ".stderr.txt")
    started = time.perf_counter()
    with stdout.open("xb") as out, stderr.open("xb") as err:
        result = subprocess.run(invocation["argv"], cwd=AC, env=env, stdout=out, stderr=err, check=False)
    record = {"created_at": now(), "exit_code": result.returncode, "elapsed_wall_seconds": time.perf_counter() - started,
              "stdout_sha256": sha(stdout), "stderr_sha256": sha(stderr), "after": guard()}
    save(PROOF / "commands" / (label + ".result.json"), record)
    assert result.returncode == 0, label + " failed; retained stdout/stderr/result are decisive"
    return record


def preparation() -> None:
    environment()
    command("prepare", ["prepare", "--corpus", str(APP / "source"), "--manifest", str(APP / "source-manifest.json"),
                        "--output", str(RUN), "--mode", "graphify-ac", "--chunk-chars", "120000", "--graph-chars", "40000",
                        "--upstream", str(UPSTREAM)])
    g = generator()
    plan, chunks = g.checkpoint(RUN)
    record = {"created_at": now(), "files": len(plan["files"]), "bytes": sum(item["bytes"] for item in plan["files"]),
              "source_chars": sum(chunk["source_chars"] for chunk in chunks),
              "source_sections": sum(len(chunk["segments"]) for chunk in chunks), "chunks": len(chunks),
              "chunk_inventory": [{"id": chunk["id"], "source_chars": chunk["source_chars"], "sections": len(chunk["segments"])}
                                  for chunk in chunks],
              "plan_sha256": sha(RUN / "plan.json"), "chunks_sha256": sha(RUN / "chunks.json"), "model_calls": 0}
    save(APP / "build/preparation.json", record)
    print(json.dumps(record, indent=2))


def discovery() -> None:
    command("discovery", ["graph", "--output", str(RUN), "--upstream", str(UPSTREAM)])
    g = generator()
    g.checkpoint(RUN)
    result = g.verify_discovery(RUN)
    structural = load(RUN / "discovery/structural.json")
    coverage = load(RUN / "discovery/coverage.json")
    record = {"created_at": now(), "result": result,
              "structural_acquisition": {key: structural.get(key) for key in
                                         ("extracted_sources", "failed_sources", "error", "skipped_sources", "unsupported_sources")},
              "structural_source_files_without_nodes": coverage["structural_source_files_without_nodes"],
              "model_calls": 0, "after": guard()}
    save(APP / "build/discovery.json", record)
    print(json.dumps({"status": result["status"], "counts": result["counts"],
                      "failed_sources": structural.get("failed_sources"), "error": structural.get("error"), "model_calls": 0}, indent=2))


def first_batch() -> None:
    environment()
    before = guard()
    g = generator()
    plan, chunks = g.checkpoint(RUN)
    g.verify_discovery(RUN)
    assert not list((RUN / "actors").glob("**/attempt-*")), "initial batch cannot reuse or retry actors"
    assert not (RUN / "grounding-repairs").exists(), "no repair reservation authorized"
    preflight = load(PROOF / "environment-preflight.json")
    _, _, live = g.actor_settings("/Users/jim/bin/codex", {"model": "gpt-6-astra", "model_reasoning_effort": "high"})
    assert live == {key: preflight["native_actor"][key] for key in live}, "actor configuration/version drift"
    selected = [{"chunk": chunk["id"], "chunk_sha256": g.digest(chunk),
                 "prompt_sha256": g.sha(g.author_prompt(plan, chunk, RUN).encode()),
                 "prompt_chars": len(g.author_prompt(plan, chunk, RUN))} for chunk in chunks[:2]]
    save(APP / "build/first-batch-plan.json", {"created_at": now(), "selection": selected,
          "calls": 2, "jobs": 2, "timeout_seconds": 1200, "settings": live["settings"],
          "cli_version": live["cli_version"], "before": before,
          "claims": "Exactly two initial author calls; no retries, normalization, repairs or assembly authorized."})
    command("first-batch-author", ["author", "--output", str(RUN), "--execute", "--codex", "/Users/jim/bin/codex",
                                   "--model", "gpt-6-astra", "--effort", "high", "--timeout", "1200", "--jobs", "2", "--max-chunks", "2"])
    attempts = sorted((RUN / "actors/author").glob("*/attempt-*"))
    assert len(attempts) == 2 and {path.parent.name for path in attempts} == {item["chunk"] for item in selected}
    records = []
    for attempt in attempts:
        result = load(attempt / "result.json")
        chunk = next(value for value in chunks if value["id"] == attempt.parent.name)
        custody, custody_error = None, None
        if result["status"] == "completed" or result["failures"] == ["source_or_semantic_fragment_validation"]:
            try:
                g.actor_evidence(RUN, plan, chunk, attempt, allow_source_failure=result["status"] != "completed")
                custody = "strict_original" if result["status"] == "completed" else "source_only_failure_custody_verified"
            except (ValueError, OSError) as error:
                custody_error = str(error)
        records.append({"chunk": chunk["id"], "attempt": str(attempt.relative_to(RUN)), "result": result,
                        "custody": custody, "custody_error": custody_error,
                        "files": {path.name: {"bytes": path.stat().st_size, "sha256": sha(path)}
                                  for path in sorted(attempt.iterdir()) if path.is_file()}})
    record = {"created_at": now(), "calls": len(attempts), "closed_calls": sum((path / "result.json").is_file() for path in attempts),
              "attempts": records, "remaining_unattempted_chunks": len(chunks) - 2,
              "after": guard(), "claims": "First batch only. Remaining calls, retries, recovery and final assembly await Root disposition."}
    save(APP / "build/first-batch-result.json", record)
    print(json.dumps({"calls": record["calls"], "closed_calls": record["closed_calls"],
                      "statuses": [{"chunk": item["chunk"], "status": item["result"]["status"], "failures": item["result"]["failures"],
                                    "custody": item["custody"], "custody_error": item["custody_error"]} for item in records],
                      "remaining_unattempted_chunks": len(chunks) - 2}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("prepare", "discovery", "first-batch", "guard"))
    phase = parser.parse_args().phase
    if phase == "prepare":
        preparation()
    elif phase == "discovery":
        discovery()
    elif phase == "first-batch":
        first_batch()
    else:
        print(json.dumps(guard(), indent=2))


if __name__ == "__main__":
    main()
