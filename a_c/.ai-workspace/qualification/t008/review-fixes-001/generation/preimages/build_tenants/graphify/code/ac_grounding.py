#!/usr/bin/env python3
"""Optional F_D source-anchor recovery, preserving every F_P meaning field.

Original actor answers, failures and usage are immutable inputs. This module
never invokes an actor. It can recover quote/range coordinates through one
unique whitespace-run-equivalent occurrence in the SAME supplied section.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import re
import sys
import time
from typing import Any

import ac_generate as generation
import ac_graph

HERE = Path(__file__).resolve().parent
AUTHOR_FAMILIES = ("concepts", "relations", "constraints", "latitude", "residuals")
ANCHOR_FIELDS = ("quote", "start_line", "end_line")
POLICY = {
    "id": "a_c.grounding.unique-whitespace-runs/1",
    "scope": "Only quote/start_line/end_line inside the five known grounding arrays; section_id and all other fields remain unchanged.",
    "equivalence": "Collapse each maximal Unicode whitespace run to one ASCII space; strip outer whitespace only. Preserve every non-whitespace character, case, punctuation and inter-character whitespace boundary.",
    "uniqueness": "Exactly one normalized occurrence in the same supplied source section, including coordinate-only repairs. Already strict-valid anchors are unchanged without a recovery claim.",
    "claim": "F_D source re-entry normalization only; no semantic rewriting, completeness judgment, new F_P usage or semantic acceptance.",
}


class GroundingError(ValueError):
    """The bounded anchor/custody contract is not satisfied."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GroundingError(message)


def spans(text: str) -> tuple[str, list[tuple[int, int]]]:
    """Collapse runs, never delete internal word boundaries; map back to source."""
    normalized, positions = [], []
    index = 0
    while index < len(text):
        start = index
        if text[index].isspace():
            while index < len(text) and text[index].isspace():
                index += 1
            normalized.append(" ")
            positions.append((start, index))
        else:
            normalized.append(text[index])
            positions.append((index, index + 1))
            index += 1
    if normalized and normalized[0] == " ":
        normalized.pop(0)
        positions.pop(0)
    if normalized and normalized[-1] == " ":
        normalized.pop()
        positions.pop()
    return "".join(normalized), positions


def nongrounding(answer: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(answer)
    for family in AUTHOR_FAMILIES:
        for record in result[family]:
            for ground in record["grounding"]:
                for key in ANCHOR_FIELDS:
                    ground[key] = "<permitted-source-anchor-coordinate>"
    return result


def anchors(answer: dict[str, Any]):
    for family in AUTHOR_FAMILIES:
        for ordinal, record in enumerate(answer[family]):
            for index, ground in enumerate(record["grounding"]):
                yield f"/{family}/{ordinal}/grounding/{index}", record["key"], ground


def strict_anchor(ground: dict[str, Any], section: dict[str, Any]) -> bool:
    first, last = ground["start_line"], ground["end_line"]
    if not (section["start_line"] <= first <= last <= section["end_line"]):
        return False
    lines = section["text"].splitlines(keepends=True)
    text = "".join(lines[first - section["start_line"]:last - section["start_line"] + 1])
    return bool(ground["quote"].strip()) and ground["quote"] in text


def recover_anchor(ground: dict[str, Any], section: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
    require(ground["section_id"] == section["id"], "source section identity cannot change")
    if strict_anchor(ground, section):
        return copy.deepcopy(ground), None
    query, _ = spans(ground["quote"])
    require(bool(query), "quote has no non-whitespace lexical content")
    source, positions = spans(section["text"])
    found = source.find(query)
    require(found >= 0, "no whitespace-run-equivalent lexical occurrence in the same supplied section")
    require(source.find(query, found + 1) < 0, "ambiguous whitespace-run-equivalent quote occurrences in the same supplied section")
    end = found + len(query)
    raw_first, raw_end = positions[found][0], positions[end - 1][1]
    literal = section["text"][raw_first:raw_end]
    require(spans(literal)[0] == query, "normalization failed to preserve lexical characters and whitespace boundaries")
    first_line = section["start_line"] + section["text"][:raw_first].count("\n")
    last_line = section["start_line"] + section["text"][:raw_end - 1].count("\n")
    recovered = {**ground, "quote": literal, "start_line": first_line, "end_line": last_line}
    require(strict_anchor(recovered, section), "recovered anchor failed exact original-source range check")
    witness = {"normalized_quote_sha256": generation.sha(query.encode()), "normalized_occurrence_count": 1,
               "normalized_start": found, "normalized_end": end, "section_character_start": raw_first,
               "section_character_end": raw_end, "section_sha256": section["sha256"],
               "word_boundaries_preserved": True, "outer_whitespace_search_trimmed": ground["quote"] != ground["quote"].strip()}
    return recovered, witness


def normalize_answer(answer: dict[str, Any], chunk: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    errors = generation.schema_errors(answer, generation.load(generation.ASSETS / "author.schema.json"))
    require(not errors, "original answer is not schema-valid: " + "; ".join(errors[:10]))
    sections = {section["id"]: section for section in chunk["segments"]}
    derived = copy.deepcopy(answer)
    changes = []
    for path, key, ground in anchors(derived):
        require(ground["section_id"] in sections, path + ": grounding names a section outside this exact source chunk")
        old = copy.deepcopy(ground)
        try:
            recovered, witness = recover_anchor(ground, sections[ground["section_id"]])
        except GroundingError as exc:
            raise GroundingError(f"record[{key}]{path}: {exc}") from exc
        if witness is not None:
            ground.update(recovered)
            changes.append({"path": path, "record_key": key, "section_id": ground["section_id"],
                            "old": {name: old[name] for name in ANCHOR_FIELDS}, "new": {name: ground[name] for name in ANCHOR_FIELDS},
                            "witness": witness})
    require(generation.canonical(nongrounding(answer)) == generation.canonical(nongrounding(derived)), "non-grounding F_P payload or section identity changed")
    # This catches every non-anchor authoring defect as well as derived anchors.
    generation.author_check(derived, chunk)
    return derived, changes


def latest_attempt(output: Path, chunk: dict[str, Any]) -> Path | None:
    folder = output / "actors" / "author" / chunk["id"]
    if not folder.exists():
        return None
    candidates = sorted(path for path in folder.iterdir() if path.is_dir())
    if not candidates:
        return None
    require((candidates[-1] / "result.json").is_file(), "newer original actor attempt is incomplete; wait for its result")
    return candidates[-1]


def evidence(output: Path, plan: dict[str, Any], chunk: dict[str, Any], attempt: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """Authenticate retained coordinates/audit consistency, not issuer legitimacy."""
    frozen_plan, frozen_chunks = generation.checkpoint(output)
    require(generation.canonical(plan) == generation.canonical(frozen_plan), "supplied plan differs from exact frozen plan")
    matches = [value for value in frozen_chunks if value["id"] == chunk["id"]]
    require(len(matches) == 1 and generation.canonical(matches[0]) == generation.canonical(chunk), "supplied chunk differs from exact frozen chunk")
    plan, chunk = frozen_plan, matches[0]
    if plan["mode"] in generation.GRAPH_MODES:
        generation.verify_discovery(output)
    require(attempt.resolve().is_relative_to(output.resolve()), "actor attempt escapes the selected run")
    require(attempt.resolve().is_relative_to((output / "actors/author" / chunk["id"]).resolve()), "actor attempt escapes expected source chunk")
    paths = ("answer.json", "result.json", "invocation.json", "prompt.txt", "events.jsonl", "stderr.txt", "usage.json")
    require(all((attempt / name).is_file() for name in paths), "incomplete actor evidence")
    require(all((attempt / name).resolve().is_relative_to(output.resolve()) for name in paths), "actor evidence symlink escapes selected run")
    result = generation.load(attempt / "result.json")
    invocation = generation.load(attempt / "invocation.json")
    settings = generation.load(output / "actor-settings.json")
    require(result.get("profile") == "ac.generation.actor-result/1" and invocation.get("profile") == "ac.generation.actor-invocation/1", "unknown actor evidence profile")
    allowed = result.get("status") == "completed" and result.get("failures") == [] or (
        result.get("status") == "failed" and result.get("failures") == ["source_or_semantic_fragment_validation"] and isinstance(result.get("validation_error"), str))
    require(allowed, "actor failure is not solely source-fragment validation")
    require(type(result.get("cli_exit_code")) is int and result.get("cli_exit_code") == 0 and result.get("timed_out") is False and result.get("user_config_unchanged") is True,
            "CLI exit/timeout/config custody failed")
    require(result.get("schema_errors") == [] and result.get("unexpected_item_types") == [], "schema or isolation failure cannot be normalized")
    for name, field in (("answer.json", "answer_sha256"), ("events.jsonl", "events_sha256"), ("stderr.txt", "stderr_sha256")):
        require(generation.sha((attempt / name).read_bytes()) == result.get(field), "stale original " + name)
    require(invocation.get("settings") == settings["settings"] == result.get("settings"), "frozen actor settings differ")
    require(invocation.get("cli_version") == settings["cli_version"] == result.get("cli_version"), "frozen actor CLI version differs")
    require(isinstance(invocation.get("config_path"), str) and re.fullmatch(r"[0-9a-f]{64}", invocation.get("config_sha256", "")) is not None, "original configuration coordinates are malformed")
    schema = generation.ASSETS / "author.schema.json"
    require(invocation.get("schema_sha256") == plan["assets"][schema.name] == generation.sha(schema.read_bytes()), "actor author schema identity differs")
    prompt = generation.author_prompt(plan, chunk, output)
    require(invocation.get("prompt_sha256") == generation.sha((attempt / "prompt.txt").read_bytes()) == generation.sha(prompt.encode()),
            "actor prompt does not belong to this exact source chunk and discovery context")
    overrides = invocation.get("inline_overrides", {})
    required_overrides = {"features.shell_tool": False, "features.apps": False, "features.multi_agent": False,
                          "features.memories": False, "features.js_repl": False, "web_search": "disabled", "project_doc_max_bytes": 0}
    require(all(overrides.get(key) == value and type(overrides.get(key)) is type(value) for key, value in required_overrides.items()), "actor tool/document isolation overrides differ")
    require(all(overrides.get(key) == value for key, value in settings["settings"].items()), "command model/settings overrides differ")
    inventory = invocation.get("effective_mcp_inventory")
    require(isinstance(inventory, list) and all(row.get("enabled") is False for row in inventory), "actor MCP isolation failed")
    for row in inventory:
        require(overrides.get("mcp_servers." + row["name"] + ".enabled") is False, "effective MCP disablement is missing")
    for key, value in overrides.items():
        if key in settings["settings"] or key in required_overrides:
            continue
        require(re.fullmatch(r"mcp_servers\.[A-Za-z0-9_-]+\.(enabled|command)", key) is not None, "unexpected actor override")
        require(value is False if key.endswith(".enabled") else value == "/usr/bin/false", "unsafe MCP override")
    command = invocation.get("command")
    require(isinstance(command, list) and len(command) > 1 and all(isinstance(item, str) for item in command), "invalid actor argv")
    base, arguments, index = [], {}, 0
    while index < len(command):
        if command[index] != "-c":
            base.append(command[index])
            index += 1
            continue
        require(index + 1 < len(command) and "=" in command[index + 1], "invalid inline configuration argv")
        key, value = command[index + 1].split("=", 1)
        require(key not in arguments, "duplicate command override")
        arguments[key] = json.loads(value)
        index += 2
    require(arguments == overrides, "recorded command and inline overrides differ")
    expected = [command[0], "exec", "--json", "--ephemeral", "--sandbox", "read-only", "--skip-git-repo-check", "--color", "never",
                "--output-schema", str(schema.resolve()), "--output-last-message", str((attempt / "answer.json").resolve()),
                "--cd", str((attempt / "empty-workspace").resolve()), "-"]
    require(base == expected, "actor argv is not the isolated ephemeral source-authoring invocation")
    declared_cwd = Path(invocation.get("cwd", ""))
    expected_cwd = (attempt / "empty-workspace").resolve()
    require(str(declared_cwd) not in ("", ".") and ".." not in declared_cwd.parts, "invalid recorded actor cwd")
    require(declared_cwd.resolve() == expected_cwd if declared_cwd.is_absolute() else expected_cwd.parts[-len(declared_cwd.parts):] == declared_cwd.parts, "recorded actor cwd differs")
    events = [json.loads(line) for line in (attempt / "events.jsonl").read_text().splitlines()]
    require(not any(event.get("type") in ("error", "turn.failed") for event in events), "actor event stream contains a failed turn")
    usage = [event["usage"] for event in events if event.get("type") == "turn.completed" and "usage" in event]
    require(bool(usage) and usage == result.get("usage_events") == generation.load(attempt / "usage.json").get("usage_events"), "retained CLI usage is absent or contradictory")
    item_types = [event["item"].get("type") for event in events if event.get("type") in ("item.started", "item.completed") and isinstance(event.get("item"), dict)]
    require(all(kind in ("agent_message", "reasoning") for kind in item_types), "actual actor tool/isolation violation")
    answer = generation.load(attempt / "answer.json")
    require(not generation.schema_errors(answer, generation.load(schema)), "raw actor answer is not schema-valid")
    original_error = None
    try:
        generation.author_check(answer, chunk)
    except generation.GenerationError as exc:
        original_error = str(exc)
    if result["status"] == "failed":
        require(original_error is not None and result.get("validation_error") == original_error, "recorded original source-validation failure contradicts exact recomputation")
    pins = {str((attempt / name).relative_to(output)): generation.sha((attempt / name).read_bytes()) for name in paths}
    pins["actor-settings.json"] = generation.sha((output / "actor-settings.json").read_bytes())
    for name in ("plan.json", "source-manifest.json", "chunks.json"):
        pins[name] = generation.sha((output / name).read_bytes())
    if (attempt / "validation.json").exists():
        validation = generation.load(attempt / "validation.json")
        require(validation.get("answer_sha256") == result["answer_sha256"] and validation.get("chunk_sha256") == generation.digest(chunk), "strict original validation belongs to a different answer/chunk")
        pins[str((attempt / "validation.json").relative_to(output))] = generation.sha((attempt / "validation.json").read_bytes())
    proof = {"original_attempt": str(attempt.relative_to(output)), "original_status": result["status"],
             "original_recorded_failure": result.get("validation_error"), "original_strict_validation_error": original_error,
             "original_usage_events": usage, "pins": pins, "chunk_sha256": generation.digest(chunk),
             "source_sections": [{key: section[key] for key in ("id", "path", "start_line", "end_line", "sha256")} for section in chunk["segments"]]}
    return answer, proof


def normalization_root(output: Path, name: str) -> Path:
    require(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", name) is not None, "normalization directory must be one safe basename")
    root = output / name
    require(root.resolve().is_relative_to(output.resolve()), "normalization directory symlink escapes selected run")
    return root


def unverified_pins(output: Path, attempt: Path) -> dict[str, str]:
    """Custody of refused input bytes is not validation of the retained claims."""
    return {str((attempt / name).relative_to(output)): generation.sha((attempt / name).read_bytes())
            for name in ("answer.json", "result.json", "invocation.json", "prompt.txt", "events.jsonl", "stderr.txt", "usage.json")
            if (attempt / name).is_file()}


def normalize(output: Path, *, name: str = "normalization", chunk_id: str | None = None) -> dict[str, Any]:
    started = time.perf_counter()
    plan, chunks = generation.checkpoint(output)
    if plan["mode"] in generation.GRAPH_MODES:
        generation.verify_discovery(output)
    root = normalization_root(output, name)
    rows = []
    selected = [chunk for chunk in chunks if chunk_id is None or chunk["id"] == chunk_id]
    require(bool(selected), "unknown selected source chunk")
    for chunk in selected:
        chunk_started = time.perf_counter()
        destination = root / chunk["id"]
        if destination.exists():
            derived, journal = verify_normalization(output, plan, chunk, destination)
            rows.append({"chunk": chunk["id"], "status": journal["status"], "reused": True, "changes": len(journal["changes"]),
                         "fd_verification_elapsed_seconds": time.perf_counter() - chunk_started})
            continue
        attempt = latest_attempt(output, chunk)
        if attempt is None:
            rows.append({"chunk": chunk["id"], "status": "pending_original_actor"})
            continue
        journal: dict[str, Any] = {"profile": "ac.generation.grounding-normalization/1", "policy": POLICY,
                                   "policy_sha256": generation.digest(POLICY), "normalizer_sha256": generation.sha(Path(__file__).read_bytes()),
                                   "chunk": chunk["id"], "status": "refused", "changes": [],
                                   "selected_original_attempt": str(attempt.relative_to(output)),
                                   "unverified_original_pins": unverified_pins(output, attempt)}
        derived = None
        try:
            answer, proof = evidence(output, plan, chunk, attempt)
            journal["original_evidence"] = proof
            derived, changes = normalize_answer(answer, chunk)
            journal.update(status="derived_validated" if changes else "validated_original", changes=changes,
                           non_grounding_sha256=generation.digest(nongrounding(answer)),
                           derived_non_grounding_sha256=generation.digest(nongrounding(derived)))
        except (GroundingError, generation.GenerationError, OSError, ValueError) as exc:
            journal["refusal"] = str(exc)
        generation.checkpoint(output)  # source and frozen code still unchanged
        journal["fd_elapsed_seconds"] = time.perf_counter() - chunk_started
        destination.mkdir(parents=True, exist_ok=False)
        if derived is not None and journal["status"] != "refused":
            generation.save(destination / "derived-answer.json", derived, exclusive=True)
            journal["derived_answer_sha256"] = generation.sha((destination / "derived-answer.json").read_bytes())
        generation.save(destination / "journal.json", journal, exclusive=True)
        rows.append({"chunk": chunk["id"], "status": journal["status"], "changes": len(journal["changes"]), "refusal": journal.get("refusal"), "fd_elapsed_seconds": journal["fd_elapsed_seconds"]})
    return {"profile": "ac.generation.normalization-result/1", "normalization_directory": name, "chunks": rows,
            "new_fp_calls": 0, "fd_elapsed_seconds": time.perf_counter() - started, "claim": POLICY["claim"]}


def verify_normalization(output: Path, plan: dict[str, Any], chunk: dict[str, Any], folder: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    journal = generation.load(folder / "journal.json")
    require(journal.get("profile") == "ac.generation.grounding-normalization/1" and journal.get("chunk") == chunk["id"], "normalization proof identifies a different chunk/profile")
    require(journal.get("status") in ("derived_validated", "validated_original"), "normalization was refused; preserve it and choose a fresh normalization directory after F_P repair")
    require(journal.get("policy") == POLICY and journal.get("policy_sha256") == generation.digest(POLICY), "normalization policy changed")
    require(journal.get("normalizer_sha256") == generation.sha(Path(__file__).read_bytes()), "normalizer code changed since proof creation")
    original = journal["original_evidence"]
    for path, expected in original["pins"].items():
        relative = generation.safe_relative(path)
        target = output / relative
        require(target.resolve(strict=True).is_relative_to(output.resolve()), "normalization evidence pin escapes run")
        require(generation.sha(target.read_bytes()) == expected, "stale normalization evidence: " + path)
    attempt = output / generation.safe_relative(original["original_attempt"])
    require(latest_attempt(output, chunk) == attempt, "a newer original actor attempt exists; preserve this proof and use a fresh normalization directory")
    answer, current_proof = evidence(output, plan, chunk, attempt)
    require(current_proof == original, "original actor evidence differs from normalization proof")
    expected_answer, expected_changes = normalize_answer(answer, chunk)
    require(journal["status"] == ("derived_validated" if expected_changes else "validated_original"), "normalization status misstates no-op versus recovery")
    derived = generation.load(folder / "derived-answer.json")
    require(generation.sha((folder / "derived-answer.json").read_bytes()) == journal.get("derived_answer_sha256"), "derived answer changed")
    require(generation.canonical(derived) == generation.canonical(expected_answer) and journal.get("changes") == expected_changes, "derived answer or normalization witness differs from deterministic recovery")
    original_hash, derived_hash = generation.digest(nongrounding(answer)), generation.digest(nongrounding(derived))
    require(original_hash == derived_hash == journal.get("non_grounding_sha256") == journal.get("derived_non_grounding_sha256"), "non-grounding authored payload or source section changed")
    generation.author_check(derived, chunk)
    return derived, journal


def assemble(output: Path, *, name: str = "normalization", allow_partial: bool = False, upstream: Path | None = None) -> dict[str, Any]:
    started = time.perf_counter()
    plan, chunks = generation.checkpoint(output)
    if plan["mode"] in generation.GRAPH_MODES:
        generation.verify_discovery(output)
    root = normalization_root(output, name)
    answers, provenance, recoveries, refusals = {}, [], [], []
    for chunk in chunks:
        folder = root / chunk["id"]
        if folder.exists():
            journal = generation.load(folder / "journal.json")
            if allow_partial and journal.get("status") == "refused":
                require(journal.get("profile") == "ac.generation.grounding-normalization/1" and journal.get("chunk") == chunk["id"], "partial refusal belongs to a different chunk/profile")
                require(journal.get("policy") == POLICY and journal.get("policy_sha256") == generation.digest(POLICY) and journal.get("normalizer_sha256") == generation.sha(Path(__file__).read_bytes()), "partial refusal policy or normalizer changed")
                attempt = latest_attempt(output, chunk)  # still refuse active/new incomplete retry
                require(attempt is not None and journal.get("selected_original_attempt") == str(attempt.relative_to(output)), "refused normalization belongs to a different original attempt")
                require(journal.get("unverified_original_pins") == unverified_pins(output, attempt), "refused original bytes changed after normalization")
                refusals.append({"chunk": chunk["id"], "refusal": journal.get("refusal"), "journal_sha256": generation.sha((folder / "journal.json").read_bytes()),
                                 "original_attempt": journal["selected_original_attempt"], "unverified_original_pins": journal["unverified_original_pins"]})
                continue
            answer, journal = verify_normalization(output, plan, chunk, folder)
            answers[chunk["id"]] = answer
            proof = journal["original_evidence"]
            provenance.append({"chunk": chunk["id"], "attempt": proof["original_attempt"], "original_answer_sha256": proof["pins"][proof["original_attempt"] + "/answer.json"],
                               "answer_sha256": journal["derived_answer_sha256"], "normalization_journal_sha256": generation.sha((folder / "journal.json").read_bytes()),
                               "normalization_directory": name, "derivation": journal["status"]})
            recoveries.append({"chunk": chunk["id"], "status": journal["status"], "changes": len(journal["changes"])})
        else:
            attempt = latest_attempt(output, chunk)
            if attempt is None:
                continue
            try:
                answer, proof = evidence(output, plan, chunk, attempt)
            except GroundingError as exc:
                if not allow_partial:
                    raise
                refusals.append({"chunk": chunk["id"], "refusal": str(exc), "original_attempt": str(attempt.relative_to(output)), "unverified_original_pins": unverified_pins(output, attempt)})
                continue
            try:
                generation.author_check(answer, chunk)
            except generation.GenerationError as exc:
                if allow_partial:
                    refusals.append({"chunk": chunk["id"], "refusal": str(exc), "original_attempt": str(attempt.relative_to(output))})
                    continue
                raise GroundingError("strict original draft needs explicit normalization or fresh F_P repair: " + chunk["id"])
            answers[chunk["id"]] = answer
            provenance.append({"chunk": chunk["id"], "attempt": str(attempt.relative_to(output)), "answer_sha256": generation.sha((attempt / "answer.json").read_bytes()),
                               "invocation_sha256": generation.sha((attempt / "invocation.json").read_bytes()), "derivation": "strict_original"})
    require(allow_partial or len(answers) == len(chunks), "missing valid exact-source drafts; normal grounded assembly refuses")
    model, coverage = generation.model_from_answers(plan, chunks, answers, provenance)
    checked = ac_graph.validate(model)
    carrier = ac_graph.materialize(checked)
    require(ac_graph.decode(carrier).document == model, "grounded proposal carrier changed authored model")
    generation.checkpoint(output)
    destination = output / ("grounded-proposal" if len(answers) == len(chunks) else "grounded-partial-proposal")
    require(not destination.exists(), "grounded proposal already exists; no overwrite permitted")
    destination.mkdir()
    generation.save(destination / "model.json", model, exclusive=True)
    generation.save(destination / "carrier.json", carrier.document, exclusive=True)
    coverage["grounding_normalization"] = {"policy": POLICY, "normalization_directory": name, "recoveries": recoveries, "excluded_refusals": refusals, "new_fp_calls": 0}
    generation.save(destination / "coverage.json", coverage, exclusive=True)
    trial = None
    if plan["mode"] in generation.GRAPH_MODES:
        modules = generation.upstream_modules(upstream or Path(plan["upstream"]["root"]))
        graph = modules["build"].build_from_json(ac_graph.extraction(carrier), dedup=False)
        communities = modules["cluster"].cluster(graph)
        require(modules["export"].to_json(graph, communities, str(destination / "graph.json"), force=True, built_at_commit=generation.UPSTREAM_COMMIT), "actual upstream grounded proposal export refused")
        recovered = ac_graph.decode(ac_graph.GraphCarrier(generation.load(destination / "graph.json")))
        require(recovered.document == model, "actual upstream grounded proposal round trip changed model")
        trial = {"commit": generation.UPSTREAM_COMMIT, "nodes": graph.number_of_nodes(), "edges": graph.number_of_edges(), "decoded_model_sha256": recovered.sha256}
    result = {"profile": "ac.generation.grounded-proposal/1", "status": "proposed" if len(answers) == len(chunks) else "partial_proposal",
              "mode": plan["mode"], "model_id": model["id"], "model_sha256": checked.sha256, "processing_complete": coverage["processing_complete"],
              "family_counts": coverage["family_counts"], "grounding_recoveries": recoveries, "new_fp_calls": 0, "upstream_trial": trial,
              "fd_assembly_elapsed_seconds": time.perf_counter() - started,
              "files": {path.name: generation.sha(path.read_bytes()) for path in destination.iterdir() if path.is_file()}, "claim": POLICY["claim"]}
    generation.save(destination / "result.json", result, exclusive=True)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("normalize", "assemble"):
        p = sub.add_parser(name)
        p.add_argument("--output", type=Path, required=True)
        p.add_argument("--normalization-directory", default="normalization")
        if name == "normalize":
            p.add_argument("--chunk")
        else:
            p.add_argument("--allow-partial", action="store_true")
            p.add_argument("--upstream", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "normalize":
            result = normalize(args.output, name=args.normalization_directory, chunk_id=args.chunk)
        else:
            result = assemble(args.output, name=args.normalization_directory, allow_partial=args.allow_partial, upstream=args.upstream)
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 1 if any(row.get("status") == "refused" for row in result.get("chunks", [])) else 0
    except (GroundingError, generation.GenerationError, ac_graph.Refusal, OSError, ValueError, KeyError, TypeError) as exc:
        print("grounding refused: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
