#!/usr/bin/env python3
"""Isolated F_P repair of invalid grounding entries, with invariant statements.

This separate profile never relaxes the frozen source-authoring or F_D evidence
gates. Selecting different grounding evidence creates a new proposed
interpretation, not a mechanically proven semantically equivalent interpretation.
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

import ac_generate as g
import ac_graph
import ac_grounding as h

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "grounding_repair"
PROFILE = "a_c.grounding.f-p-repair/1"
REPAIRS = "grounding-repairs"
LIMIT = 3
GROUND_FIELDS = ("section_id", "quote", "start_line", "end_line")


class RepairError(ValueError):
    """The grounding-only proposal-repair contract is not satisfied."""


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RepairError(message)


def code_pins() -> dict[str, str]:
    return {"repair": g.sha(Path(__file__).read_bytes()), "generator": g.sha(Path(g.__file__).read_bytes()),
            "grounding": g.sha(Path(h.__file__).read_bytes()), "codec": g.sha(Path(ac_graph.__file__).read_bytes()),
            **{"asset:" + path.name: g.sha(path.read_bytes()) for path in sorted(ASSETS.iterdir()) if path.is_file()}}


def expanded_schema(chunk: dict[str, Any], invalid: list[dict[str, Any]]) -> dict[str, Any]:
    schema = g.load(ASSETS / "patch.schema.json")
    properties = schema["properties"]["patches"]["items"]["properties"]
    properties["replacement"]["properties"]["section_id"]["enum"] = [section["id"] for section in chunk["segments"]]
    properties["record_key"]["enum"] = sorted({value["record_key"] for value in invalid})
    return schema


def meaning_payload(answer: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(answer)
    for _, _, ground in h.anchors(result):
        for name in GROUND_FIELDS:
            ground[name] = "<permitted-f-p-grounding-coordinate>"
    return result


def invalid_anchors(answer: dict[str, Any], chunk: dict[str, Any]) -> list[dict[str, Any]]:
    sections = {section["id"]: section for section in chunk["segments"]}
    values = []
    for family in h.AUTHOR_FAMILIES:
        for ordinal, record in enumerate(answer[family]):
            for index, ground in enumerate(record["grounding"]):
                if ground["section_id"] not in sections:
                    reason = "section_id is outside the exact dispatched chunk"
                elif not h.strict_anchor(ground, sections[ground["section_id"]]):
                    reason = "quote is not exact at the supplied range or line range is invalid"
                else:
                    continue
                values.append({"family": family, "record_key": record["key"], "record_ordinal": ordinal, "grounding_index": index,
                               "grounding": copy.deepcopy(ground), "diagnostic": reason})
    return values


def preflight(answer: dict[str, Any], chunk: dict[str, Any]) -> list[dict[str, Any]]:
    require(not g.schema_errors(answer, g.load(g.ASSETS / "author.schema.json")), "parent draft is not author-schema-valid")
    records = [record for family in h.AUTHOR_FAMILIES for record in answer[family]]
    keys = [record["key"] for record in records]
    require(len(keys) == len(set(keys)), "non-grounding duplicate record keys cannot be repaired")
    concepts = {record["key"] for record in answer["concepts"]}
    residuals = {record["key"] for record in answer["residuals"]}
    for record in answer["relations"]:
        require(record["source_key"] in concepts and record["target_key"] in concepts, "non-grounding relation endpoints cannot be repaired")
    for record in answer["constraints"] + answer["latitude"]:
        require(bool(record["applies_to_keys"]) and set(record["applies_to_keys"]) <= concepts, "non-grounding attachment targets cannot be repaired")
    for record in answer["residuals"]:
        require(record["subject_key"] in set(keys) - residuals, "non-grounding residual subject cannot be repaired")
    dispositions = answer["dispositions"]
    sections = {section["id"] for section in chunk["segments"]}
    require(len(dispositions) == len(sections) and {value["section_id"] for value in dispositions} == sections,
            "non-grounding section dispositions cannot be repaired")
    selected = set()
    for value in dispositions:
        chosen = value["keys"]
        require(len(chosen) == len(set(chosen)) and set(chosen) <= set(keys), "non-grounding disposition keys cannot be repaired")
        require(value["decision"] not in ("retained", "residual") or bool(chosen), "non-grounding empty retained disposition cannot be repaired")
        require(value["decision"] != "residual" or bool(set(chosen) & residuals), "non-grounding residual disposition cannot be repaired")
        selected.update(chosen)
    require(selected == set(keys), "non-grounding disposition coverage cannot be repaired")
    invalid = invalid_anchors(answer, chunk)
    require(bool(invalid), "no mechanically invalid grounding entries; this profile cannot reassess strict-valid evidence")
    return invalid


def apply_patch(answer: dict[str, Any], chunk: dict[str, Any], patch: dict[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    require(not g.schema_errors(patch, g.load(ASSETS / "patch.schema.json")), "repair output does not match grounding-patch schema")
    if patch["decision"] == "refuse":
        require(not patch["patches"] and bool(patch["refusal_reason"].strip()), "refusal requires no patches and an explicit reason")
        return None, patch["refusal_reason"]
    require(patch["decision"] == "patch" and bool(patch["patches"]) and patch["refusal_reason"] == "", "patch decision requires patches and no refusal reason")
    invalid = {(value["family"], value["record_key"], value["grounding_index"]): value for value in preflight(answer, chunk)}
    sections = {section["id"]: section for section in chunk["segments"]}
    derived, seen = copy.deepcopy(answer), set()
    for value in patch["patches"]:
        target = (value["family"], value["record_key"], value["grounding_index"])
        require(target not in seen, "duplicate grounding-patch target")
        seen.add(target)
        require(target in invalid, "patch target is absent or already strict-valid in the parent")
        position = invalid[target]["record_ordinal"]
        replacement = value["replacement"]
        require(replacement["section_id"] in sections, "replacement selects evidence outside the exact dispatched source chunk")
        require(h.strict_anchor(replacement, sections[replacement["section_id"]]), "replacement quote/range is not exact source grounding")
        derived[value["family"]][position]["grounding"][value["grounding_index"]] = copy.deepcopy(replacement)
    require(g.canonical(meaning_payload(answer)) == g.canonical(meaning_payload(derived)), "non-grounding statement, key, disposition, population or order changed")
    try:
        g.author_check(derived, chunk)
        return derived, None
    except g.GenerationError as exc:
        require(bool(invalid_anchors(derived, chunk)), "remaining whole-draft failure is outside invalid-grounding repair scope: " + str(exc))
        return derived, str(exc)


def call_inventory(output: Path, chunk_id: str) -> list[dict[str, Any]]:
    output = output.resolve(strict=True)
    result = []
    for family, folder in (("author", output / "actors/author" / chunk_id), ("repair", output / REPAIRS / chunk_id)):
        if folder.exists():
            require(folder.resolve().is_relative_to(output), "call budget namespace escapes selected run")
            for path in sorted(folder.iterdir()):
                if path.is_dir():
                    require(path.resolve().is_relative_to(output), "call attempt escapes selected run")
                    require(re.fullmatch(r"attempt-[0-9]+", path.name) is not None, "unexpected call directory in shared budget namespace")
                    result.append({"family": family, "attempt": str(path.relative_to(output)),
                                   "invocation_recorded": (path / ("invocation.json" if family == "author" else "actor/invocation.json")).exists()})
    return result


def safe_attempt(output: Path, attempt: Path) -> Path:
    output = output.resolve(strict=True)
    if not attempt.is_absolute():
        candidate = attempt.resolve()
        attempt = candidate if candidate.is_relative_to(output) else output / attempt
    require(attempt.resolve().is_relative_to((output / REPAIRS).resolve()) and attempt.resolve().is_relative_to(output.resolve()), "repair path escapes selected run")
    require(re.fullmatch(r"attempt-[0-9]+", attempt.name) is not None, "invalid repair-attempt name")
    return attempt


def choose_chunk(output: Path, chunk_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    plan, chunks = g.checkpoint(output)
    selected = [chunk for chunk in chunks if chunk["id"] == chunk_id]
    require(len(selected) == 1, "unknown source chunk")
    if plan["mode"] in g.GRAPH_MODES:
        g.verify_discovery(output)
    return plan, selected[0]


def parent_draft(output: Path, plan: dict[str, Any], chunk: dict[str, Any], parent: dict[str, str], visiting: set[str] | None = None) -> tuple[dict[str, Any], dict[str, Any]]:
    if parent["kind"] == "author":
        attempt = output / g.safe_relative(parent["path"])
        require(h.latest_attempt(output, chunk) == attempt, "parent is not the latest completed original author attempt")
        answer, proof = h.evidence(output, plan, chunk, attempt)
        return answer, {"kind": "author", "path": parent["path"], "evidence": proof}
    require(parent["kind"] == "repair", "unsupported repair-parent kind")
    attempt = safe_attempt(output, Path(parent["path"]))
    answer, journal = verify(output, attempt, require_complete=False, _visiting=visiting)
    require(answer is not None and journal["status"] in ("complete_patch", "incomplete_patch"), "repair parent has no scope-valid proposed draft")
    return answer, {"kind": "repair", "path": parent["path"], "journal_sha256": g.sha((attempt / "journal.json").read_bytes()),
                    "derived_answer_sha256": g.sha((attempt / "derived-answer.json").read_bytes()), "status": journal["status"]}


def prompt_text(output: Path, plan: dict[str, Any], chunk: dict[str, Any], answer: dict[str, Any], invalid: list[dict[str, Any]], parent: dict[str, str]) -> str:
    context = {"profile": PROFILE, "subject_id": plan["subject_id"], "mode": plan["mode"], "source_chunk": chunk["id"],
               "parent": parent, "parent_draft": answer, "invalid_grounding_entries": invalid,
               "source_data": json.loads(g.source_payload(chunk, output))}
    if plan["mode"] in g.GRAPH_MODES:
        context["graphify_discovery_data"] = g.graph_context(output, chunk, plan["graph_chars"])
    return (ASSETS / "repair.txt").read_text() + "\nREPAIR_DATA_JSON:\n" + json.dumps(context, ensure_ascii=False, separators=(",", ":"))


def prepare(output: Path, chunk_id: str, *, parent_repair: Path | None = None) -> Path:
    output = output.resolve(strict=True)
    plan, chunk = choose_chunk(output, chunk_id)
    inventory = call_inventory(output, chunk_id)
    require(len(inventory) < LIMIT, "shared three-call author+repair ceiling exhausted, including reserved/failed/unfinished attempts")
    if parent_repair:
        prior = safe_attempt(output, parent_repair)
        require(prior.parent.name == chunk_id, "repair parent belongs to a different chunk")
        parent = {"kind": "repair", "path": str(prior.relative_to(output))}
    else:
        prior = h.latest_attempt(output, chunk)
        require(prior is not None, "no complete original actor draft")
        parent = {"kind": "author", "path": str(prior.relative_to(output))}
    answer, proof = parent_draft(output, plan, chunk, parent)
    invalid = preflight(answer, chunk)
    prompt = prompt_text(output, plan, chunk, answer, invalid, parent)
    folder = output / REPAIRS / chunk_id
    existing = list(folder.iterdir()) if folder.exists() else []
    attempt = folder / f"attempt-{len(existing) + 1:03d}"
    require(not any(value["family"] == "repair" and not (output / value["attempt"] / "journal.json").exists() for value in inventory), "an earlier repair reservation is unfinished")
    attempt.mkdir(parents=True, exist_ok=False)
    (attempt / "prompt.txt").write_text(prompt)
    g.save(attempt / "parent-answer.json", answer, exclusive=True)
    g.save(attempt / "patch.schema.json", expanded_schema(chunk, invalid), exclusive=True)
    request = {"profile": PROFILE, "chunk": chunk_id, "mode": plan["mode"], "parent": parent, "parent_proof": proof,
               "parent_answer_sha256": g.sha((attempt / "parent-answer.json").read_bytes()), "invalid_grounding_entries": invalid,
               "prompt_sha256": g.sha(prompt.encode()), "schema_sha256": g.sha((attempt / "patch.schema.json").read_bytes()),
               "source_chunk_sha256": g.digest(chunk), "source_plan_sha256": g.sha((output / "plan.json").read_bytes()),
               "code_pins": code_pins(), "actor_settings": g.load(output / "actor-settings.json"),
               "budget_limit": LIMIT, "budget_before_reservation": inventory,
               "claim": "New F_P evidence-selection proposal with invariant non-grounding statement bytes; semantic equivalence and acceptance unassessed."}
    g.save(attempt / "request.json", request, exclusive=True)
    return attempt


def verify_request(output: Path, attempt: Path, visiting: set[str] | None = None) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    output = output.resolve(strict=True)
    attempt = safe_attempt(output, attempt)
    request = g.load(attempt / "request.json")
    require(request.get("profile") == PROFILE and request.get("chunk") == attempt.parent.name, "repair request profile/chunk differs")
    plan, chunk = choose_chunk(output, request["chunk"])
    require(request["code_pins"] == code_pins(), "repair/generator/grounding/codec/prompt/schema code drift")
    require(request["source_chunk_sha256"] == g.digest(chunk) and request["source_plan_sha256"] == g.sha((output / "plan.json").read_bytes()), "repair source plan/chunk changed")
    require(request["actor_settings"] == g.load(output / "actor-settings.json"), "repair settings differ from frozen source actors")
    answer, proof = parent_draft(output, plan, chunk, request["parent"], visiting)
    require(proof == request["parent_proof"], "repair parent evidence changed")
    require(g.sha((attempt / "parent-answer.json").read_bytes()) == request["parent_answer_sha256"] and g.canonical(g.load(attempt / "parent-answer.json")) == g.canonical(answer), "retained parent draft changed")
    invalid = preflight(answer, chunk)
    require(invalid == request["invalid_grounding_entries"], "repair diagnostics changed")
    require(request["schema_sha256"] == g.sha((attempt / "patch.schema.json").read_bytes()) and g.load(attempt / "patch.schema.json") == expanded_schema(chunk, invalid), "expanded per-chunk repair schema changed")
    expected = prompt_text(output, plan, chunk, answer, invalid, request["parent"])
    require(g.sha((attempt / "prompt.txt").read_bytes()) == request["prompt_sha256"] == g.sha(expected.encode()), "repair prompt differs from exact parent/source/treatment context")
    inventory = call_inventory(output, chunk["id"])
    require(len(inventory) <= LIMIT and request["budget_limit"] == LIMIT, "shared three-call author+repair ceiling exceeded")
    return request, plan, chunk, answer


def actor_evidence(attempt: Path, request: dict[str, Any]) -> tuple[dict[str, Any], dict[str, str]]:
    actor = attempt / "actor"
    names = ("invocation.json", "prompt.txt", "answer.json", "events.jsonl", "stderr.txt", "usage.json", "result.json")
    require(all((actor / name).is_file() and (actor / name).resolve().is_relative_to(attempt.resolve()) for name in names), "repair actor evidence missing or escaping attempt")
    invocation, result = g.load(actor / "invocation.json"), g.load(actor / "result.json")
    require(invocation.get("profile") == "ac.generation.actor-invocation/1" and result.get("profile") == "ac.generation.actor-result/1", "unknown repair actor evidence")
    require(result.get("status") == "completed" and result.get("failures") == [] and type(result.get("cli_exit_code")) is int and result["cli_exit_code"] == 0,
            "repair actor did not complete a clean CLI turn")
    require(result.get("timed_out") is False and result.get("user_config_unchanged") is True and result.get("schema_errors") == [] and result.get("unexpected_item_types") == [], "repair actor timeout/config/schema/isolation failure")
    settings = request["actor_settings"]
    require(invocation.get("settings") == result.get("settings") == settings["settings"] and invocation.get("cli_version") == result.get("cli_version") == settings["cli_version"], "repair actor model/settings/CLI differ")
    require(isinstance(invocation.get("config_path"), str) and re.fullmatch(r"[0-9a-f]{64}", invocation.get("config_sha256", "")) is not None, "repair configuration coordinates malformed")
    require(invocation.get("prompt_sha256") == request["prompt_sha256"] == g.sha((actor / "prompt.txt").read_bytes()), "repair actor prompt differs")
    require(invocation.get("schema_sha256") == request["schema_sha256"], "repair actor schema differs")
    for name, field in (("answer.json", "answer_sha256"), ("events.jsonl", "events_sha256"), ("stderr.txt", "stderr_sha256")):
        require(result.get(field) == g.sha((actor / name).read_bytes()), "repair actor raw artifact changed: " + name)
    expected_overrides = {"features.shell_tool": False, "features.apps": False, "features.multi_agent": False, "features.memories": False,
                          "features.js_repl": False, "web_search": "disabled", "project_doc_max_bytes": 0}
    overrides = invocation.get("inline_overrides", {})
    require(all(overrides.get(key) == value and type(overrides.get(key)) is type(value) for key, value in expected_overrides.items()), "repair actor isolation overrides differ")
    require(all(overrides.get(key) == value for key, value in settings["settings"].items()), "repair actor setting overrides differ")
    inventory = invocation.get("effective_mcp_inventory")
    require(isinstance(inventory, list) and all(row.get("enabled") is False and overrides.get("mcp_servers." + row["name"] + ".enabled") is False for row in inventory), "repair actor MCP isolation failed")
    for key, value in overrides.items():
        if key in settings["settings"] or key in expected_overrides:
            continue
        require(re.fullmatch(r"mcp_servers\.[A-Za-z0-9_-]+\.(enabled|command)", key) is not None and (value is False if key.endswith(".enabled") else value == "/usr/bin/false"), "unexpected repair actor override")
    command = invocation.get("command")
    require(isinstance(command, list) and all(isinstance(value, str) for value in command) and bool(command), "repair actor command missing")
    base, configured, index = [], {}, 0
    while index < len(command):
        if command[index] != "-c":
            base.append(command[index]); index += 1
        else:
            require(index + 1 < len(command) and "=" in command[index + 1], "repair argv override malformed")
            key, value = command[index + 1].split("=", 1)
            require(key not in configured, "duplicate repair argv override")
            configured[key] = json.loads(value); index += 2
    expected = [command[0], "exec", "--json", "--ephemeral", "--sandbox", "read-only", "--skip-git-repo-check", "--color", "never",
                "--output-schema", str((attempt / "patch.schema.json").resolve()), "--output-last-message", str((actor / "answer.json").resolve()),
                "--cd", str((actor / "empty-workspace").resolve()), "-"]
    require(base == expected and configured == overrides, "repair actual argv differs from isolated custom-profile invocation")
    cwd = Path(invocation.get("cwd", ""))
    expected_cwd = (actor / "empty-workspace").resolve()
    require(str(cwd) not in ("", ".") and ".." not in cwd.parts and (cwd.resolve() == expected_cwd if cwd.is_absolute() else expected_cwd.parts[-len(cwd.parts):] == cwd.parts), "repair actor cwd differs")
    events = [json.loads(line) for line in (actor / "events.jsonl").read_text().splitlines()]
    require(not any(event.get("type") in ("error", "turn.failed") for event in events), "repair actor event failure")
    usage = [event["usage"] for event in events if event.get("type") == "turn.completed" and "usage" in event]
    require(bool(usage) and usage == result.get("usage_events") == g.load(actor / "usage.json").get("usage_events"), "repair actor usage absent or contradictory")
    kinds = [event["item"].get("type") for event in events if event.get("type") in ("item.started", "item.completed") and isinstance(event.get("item"), dict)]
    require(all(kind in ("agent_message", "reasoning") for kind in kinds), "repair actor actually used a disallowed tool")
    patch = g.load(actor / "answer.json")
    require(not g.schema_errors(patch, g.load(attempt / "patch.schema.json")), "repair patch schema invalid")
    return patch, {"actor/" + name: g.sha((actor / name).read_bytes()) for name in names}


def execute(output: Path, attempt: Path, *, codex: str = "codex", timeout: int = 1200) -> dict[str, Any]:
    output = output.resolve(strict=True)
    started = time.perf_counter()
    attempt = safe_attempt(output, attempt)
    request, plan, chunk, answer = verify_request(output, attempt)
    require(not (attempt / "actor").exists() and not (attempt / "journal.json").exists(), "repair attempt already started; prepare another call within shared ceiling")
    require(1 <= timeout <= 3600, "repair timeout outside supported range")
    _, _, settings = g.actor_settings(codex, request["actor_settings"]["settings"])
    require(settings["cli_version"] == request["actor_settings"]["cli_version"] and settings["settings"] == request["actor_settings"]["settings"], "repair CLI/model/settings preflight differs")
    raw = g.run_actor((attempt / "prompt.txt").read_text(), attempt / "patch.schema.json", attempt / "actor", codex, timeout, request["actor_settings"]["settings"])
    journal = {"profile": PROFILE, "chunk": chunk["id"], "status": "failed_actor", "code_pins": code_pins(),
               "request_sha256": g.sha((attempt / "request.json").read_bytes()), "parent_meaning_sha256": g.digest(meaning_payload(answer)),
               "usage_events": raw.get("usage_events", []), "strict_validation_error": None,
               "claim": request["claim"]}
    journal["unverified_actor_pins"] = {str(path.relative_to(attempt)): g.sha(path.read_bytes()) for path in (attempt / "actor").iterdir() if path.is_file()}
    try:
        patch, pins = actor_evidence(attempt, request)
        journal["actor_pins"] = pins
        derived, error = apply_patch(answer, chunk, patch)
        if derived is None:
            journal.update(status="refused", refusal=error)
        else:
            g.save(attempt / "derived-answer.json", derived, exclusive=True)
            journal.update(status="complete_patch" if error is None else "incomplete_patch", strict_validation_error=error,
                           derived_answer_sha256=g.sha((attempt / "derived-answer.json").read_bytes()), derived_meaning_sha256=g.digest(meaning_payload(derived)),
                           remaining_invalid_grounding_entries=invalid_anchors(derived, chunk))
    except (RepairError, g.GenerationError, h.GroundingError, OSError, ValueError) as exc:
        journal["failure"] = str(exc)
        journal["status"] = "invalid_patch" if raw.get("status") == "completed" else "failed_actor"
    choose_chunk(output, chunk["id"])
    journal["elapsed_seconds"] = time.perf_counter() - started
    g.save(attempt / "journal.json", journal, exclusive=True)
    return journal


def verify(output: Path, attempt: Path, *, require_complete: bool = True, _visiting: set[str] | None = None) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    output = output.resolve(strict=True)
    attempt = safe_attempt(output, attempt)
    key = str(attempt.resolve())
    visiting = set(_visiting or ())
    require(key not in visiting and len(visiting) < LIMIT, "cyclic or over-budget repair parent chain")
    visiting.add(key)
    request, plan, chunk, parent = verify_request(output, attempt, visiting)
    journal = g.load(attempt / "journal.json")
    require(journal.get("profile") == PROFILE and journal.get("chunk") == chunk["id"] and journal.get("code_pins") == code_pins(), "repair journal profile/chunk/code differs")
    require(journal.get("request_sha256") == g.sha((attempt / "request.json").read_bytes()), "repair request changed after execution")
    require(journal.get("parent_meaning_sha256") == g.digest(meaning_payload(parent)), "repair parent meaning commitment changed")
    current_pins = {str(path.relative_to(attempt)): g.sha(path.read_bytes()) for path in (attempt / "actor").iterdir() if path.is_file()}
    require(journal.get("unverified_actor_pins") == current_pins, "repair raw actor artifacts changed")
    if journal.get("status") in ("failed_actor", "invalid_patch"):
        require(not require_complete, "repair actor or patch failed; no complete repair")
        raw = g.load(attempt / "actor/result.json")
        require(journal.get("usage_events") == raw.get("usage_events", []), "failed repair usage changed")
        try:
            patch, _ = actor_evidence(attempt, request)
            apply_patch(parent, chunk, patch)
        except (RepairError, g.GenerationError, h.GroundingError, OSError, ValueError) as exc:
            require(journal.get("failure") == str(exc) and journal["status"] == ("invalid_patch" if raw.get("status") == "completed" else "failed_actor"), "failed repair claim differs from exact recomputation")
            return None, journal
        raise RepairError("journal claims a failed repair whose checks now succeed")
    require(journal.get("status") in ("complete_patch", "incomplete_patch", "refused"), "unknown repair verification status")
    patch, pins = actor_evidence(attempt, request)
    require(journal.get("actor_pins") == pins and journal.get("usage_events") == g.load(attempt / "actor/result.json")["usage_events"], "repair actor evidence or usage changed")
    expected, error = apply_patch(parent, chunk, patch)
    if expected is None:
        require(journal["status"] == "refused" and journal.get("refusal") == error, "repair refusal changed")
        require(not require_complete, "repair actor explicitly refused")
        return None, journal
    status = "complete_patch" if error is None else "incomplete_patch"
    require(journal["status"] == status and journal.get("strict_validation_error") == error, "repair whole-draft validation claim differs")
    derived = g.load(attempt / "derived-answer.json")
    require(g.sha((attempt / "derived-answer.json").read_bytes()) == journal.get("derived_answer_sha256") and g.canonical(derived) == g.canonical(expected), "derived repair draft differs from exact patch application")
    require(journal.get("parent_meaning_sha256") == g.digest(meaning_payload(parent)) == g.digest(meaning_payload(derived)) == journal.get("derived_meaning_sha256"), "non-grounding authored statements changed")
    require(journal.get("remaining_invalid_grounding_entries") == invalid_anchors(derived, chunk), "remaining grounding diagnostics changed")
    if require_complete:
        require(error is None, "incomplete repair draft cannot enter complete assembly")
        g.author_check(derived, chunk)
    return derived, journal


def assemble(output: Path, *, normalization_name: str = "normalization", allow_partial: bool = False, upstream: Path | None = None) -> dict[str, Any]:
    output = output.resolve(strict=True)
    started = time.perf_counter()
    plan, chunks = g.checkpoint(output)
    formal_checker = g._formal_selection(output, plan, None)
    if plan["mode"] in g.GRAPH_MODES:
        g.verify_discovery(output)
    answers, provenance, selections = {}, [], []
    for chunk in chunks:
        require(len(call_inventory(output, chunk["id"])) <= LIMIT, "shared three-call ceiling exceeded for assembled or excluded chunk")
        folder = output / REPAIRS / chunk["id"]
        repairs = sorted(path for path in folder.iterdir() if path.is_dir()) if folder.exists() else []
        if repairs:
            attempt = repairs[-1]
            require((attempt / "journal.json").is_file(), "latest repair is unfinished")
            answer, journal = verify(output, attempt, require_complete=False)
            if answer is None or journal["status"] != "complete_patch":
                require(allow_partial, "latest repair is refused or incomplete; complete assembly refuses")
                selections.append({"chunk": chunk["id"], "status": "excluded_repair", "attempt": str(attempt.relative_to(output)), "journal_sha256": g.sha((attempt / "journal.json").read_bytes())})
                continue
            g.author_check(answer, chunk)
            proof = {"chunk": chunk["id"], "derivation": "verified_f-p-grounding-patch", "attempt": str(attempt.relative_to(output)),
                     "answer_sha256": journal["derived_answer_sha256"], "repair_journal_sha256": g.sha((attempt / "journal.json").read_bytes())}
        else:
            normalization = h.normalization_root(output, normalization_name) / chunk["id"]
            if normalization.exists():
                recorded = g.load(normalization / "journal.json")
                if allow_partial and recorded.get("status") == "refused":
                    require(recorded.get("profile") == "ac.generation.grounding-normalization/1" and recorded.get("chunk") == chunk["id"] and recorded.get("policy") == h.POLICY and
                            recorded.get("policy_sha256") == g.digest(h.POLICY) and recorded.get("normalizer_sha256") == g.sha(Path(h.__file__).read_bytes()), "refused F_D normalization custody differs")
                    original = h.latest_attempt(output, chunk)
                    require(original is not None and recorded.get("selected_original_attempt") == str(original.relative_to(output)) and recorded.get("unverified_original_pins") == h.unverified_pins(output, original), "refused F_D original evidence changed")
                    selections.append({"chunk": chunk["id"], "status": "excluded_f-d-refusal", "journal_sha256": g.sha((normalization / "journal.json").read_bytes()), "original_attempt": str(original.relative_to(output))})
                    continue
                answer, journal = h.verify_normalization(output, plan, chunk, normalization)
                proof = {"chunk": chunk["id"], "derivation": "verified_f-d-grounding", "answer_sha256": journal["derived_answer_sha256"],
                         "normalization_journal_sha256": g.sha((normalization / "journal.json").read_bytes())}
            else:
                attempt = h.latest_attempt(output, chunk)
                if attempt is None:
                    require(allow_partial, "missing original draft")
                    continue
                answer, original = h.evidence(output, plan, chunk, attempt)
                try:
                    g.author_check(answer, chunk)
                except g.GenerationError:
                    require(allow_partial, "original needs verified grounding recovery or F_P repair")
                    continue
                proof = {"chunk": chunk["id"], "derivation": "strict_original", "attempt": str(attempt.relative_to(output)), "answer_sha256": g.sha((attempt / "answer.json").read_bytes())}
        answers[chunk["id"]] = answer
        provenance.append(proof)
        selections.append(proof)
    require(allow_partial or len(answers) == len(chunks), "not every source chunk has a strict complete proposed draft")
    model, coverage = g.model_from_answers(plan, chunks, answers, provenance)
    checked = ac_graph.validate(model)
    carrier = ac_graph.materialize(checked)
    require(ac_graph.decode(carrier).document == model, "repaired carrier changed model")
    destination = output / ("repaired-proposal" if len(answers) == len(chunks) else "repaired-partial-proposal")
    require(not destination.exists(), "repaired proposal already exists")
    g.checkpoint(output)
    destination.mkdir()
    g.save(destination / "model.json", model, exclusive=True)
    g.save(destination / "carrier.json", carrier.document, exclusive=True)
    coverage["grounding_repair"] = {"profile": PROFILE, "selections": selections, "shared_fp_call_limit": LIMIT,
                                     "claim": "New proposal; non-grounding statement bytes preserved. Semantic equivalence, fidelity and acceptance unassessed."}
    g.save(destination / "coverage.json", coverage, exclusive=True)
    trial = None
    if plan["mode"] in g.GRAPH_MODES:
        modules = g.upstream_modules(upstream or Path(plan["upstream"]["root"]))
        graph = modules["build"].build_from_json(ac_graph.extraction(carrier), dedup=False)
        communities = modules["cluster"].cluster(graph)
        require(modules["export"].to_json(graph, communities, str(destination / "graph.json"), force=True, built_at_commit=g.UPSTREAM_COMMIT), "actual upstream repaired graph export refused")
        recovered = ac_graph.decode(ac_graph.GraphCarrier(g.load(destination / "graph.json")))
        require(recovered.document == model, "actual upstream repaired graph round trip changed model")
        trial = {"commit": g.UPSTREAM_COMMIT, "nodes": graph.number_of_nodes(), "edges": graph.number_of_edges(), "model_sha256": recovered.sha256}
    result = {"profile": PROFILE, "status": "proposed" if len(answers) == len(chunks) else "partial_proposal", "processing_complete": coverage["processing_complete"],
              "model_id": model["id"], "model_sha256": checked.sha256, "family_counts": coverage["family_counts"], "upstream_trial": trial,
              "fd_assembly_elapsed_seconds": time.perf_counter() - started,
              "files": {path.name: g.sha(path.read_bytes()) for path in destination.iterdir() if path.is_file()},
              "claim": coverage["grounding_repair"]["claim"]}
    g.check_formal_proposal(plan, destination, result, formal_checker=formal_checker)
    g.save(destination / "result.json", result, exclusive=True)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("prepare", "execute", "verify", "assemble"):
        p = commands.add_parser(name)
        p.add_argument("--output", type=Path, required=True)
        if name == "prepare":
            p.add_argument("--chunk", required=True)
            p.add_argument("--parent-repair", type=Path)
        elif name in ("execute", "verify"):
            p.add_argument("--attempt", type=Path, required=True)
            if name == "execute":
                p.add_argument("--codex", default="codex")
                p.add_argument("--timeout", type=int, default=1200)
            else:
                p.add_argument("--allow-incomplete", action="store_true")
        else:
            p.add_argument("--normalization-directory", default="normalization")
            p.add_argument("--allow-partial", action="store_true")
            p.add_argument("--upstream", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "prepare":
            result = {"attempt": str(prepare(args.output, args.chunk, parent_repair=args.parent_repair))}
        elif args.command == "execute":
            result = execute(args.output, args.attempt, codex=args.codex, timeout=args.timeout)
        elif args.command == "verify":
            _, result = verify(args.output, args.attempt, require_complete=not args.allow_incomplete)
        else:
            result = assemble(args.output, normalization_name=args.normalization_directory, allow_partial=args.allow_partial, upstream=args.upstream)
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return g.formal_exit(result) or (1 if result.get("status") in ("failed_actor", "invalid_patch", "refused", "incomplete_patch") else 0)
    except (RepairError, g.GenerationError, g.ac_formal_gate.GateError, h.GroundingError, ac_graph.Refusal, OSError, ValueError, KeyError, TypeError) as exc:
        print("repair refused: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
