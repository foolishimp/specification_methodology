#!/usr/bin/env python3
"""Source-first, proposal-only a_c authoring with an optional Graphify front end.

The tenant owns the workflow, including fresh F_P calls. It does not turn graph
edges into normative facts. Exact source remains available to every author call.
No existing a_c model, generated map, prior answer or semantic acceptance is an
input. Graphify and Codex are imported/invoked only by the stages that need them.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import copy
import hashlib
import importlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import stat
import subprocess
import sys
import time
import tomllib
from typing import Any, TYPE_CHECKING
from urllib.parse import quote

import ac_graph

if TYPE_CHECKING:
    import ac_formal_gate
else:
    # This new bridge is loaded from the exact sibling source bytes, never by
    # an ambient module/package name or a possibly stale bytecode cache.
    from types import ModuleType
    _formal_path = Path(__file__).resolve().with_name("ac_formal_gate.py")
    if _formal_path.is_symlink() or not _formal_path.is_file():
        raise RuntimeError("Formal bridge must be the selected regular source file")
    _formal_source = _formal_path.read_bytes()
    ac_formal_gate = ModuleType("ac_formal_gate")
    ac_formal_gate.__file__ = str(_formal_path)
    exec(compile(_formal_source, str(_formal_path), "exec"), ac_formal_gate.__dict__)
    ac_formal_gate.__dict__["__a_c_loaded_sha256__"] = hashlib.sha256(_formal_source).hexdigest()

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "generation"
UPSTREAM_COMMIT = "fe085cedddde3a18554f8749b230bfe47f3dcce7"
UPSTREAM_PROMPT = "graphify/skills/codex/references/extraction-spec.md"
FAMILIES = tuple(ac_graph.CORE_FIELDS)
SETTING_KEYS = ("model", "model_provider", "model_reasoning_effort", "model_reasoning_summary", "model_verbosity", "service_tier")
GRAPH_MODES = ("graphify-ac", "graphify")
SEMANTIC_PROFILES = {
    "graphify-ac": "a_c.graphify.source-semantic-extraction/1",
    "graphify": "graphify.codex.extraction-plus-a_c.authoring/1",
    "direct": "a_c.direct.source-authoring/1",
}


class GenerationError(ValueError):
    """A source, authoring, isolation or preservation obligation failed."""


def require(ok: bool, text: str) -> None:
    if not ok:
        raise GenerationError(text)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def digest(value: Any) -> str:
    return sha(canonical(value))


def _decode(raw: bytes) -> Any:
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            require(key not in result, f"duplicate JSON key {key}")
            result[key] = value
        return result
    def invalid_constant(value: str) -> None:
        raise GenerationError("non-finite JSON constant " + value)
    return json.loads(raw, object_pairs_hook=pairs, parse_constant=invalid_constant)


def load(path: Path) -> Any:
    return _decode(path.read_bytes())


def save(path: Path, value: Any, *, exclusive: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x" if exclusive else "w", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")


def safe_relative(path: str) -> str:
    require(isinstance(path, str) and bool(path) and "\\" not in path, "source path must be POSIX relative")
    p = PurePosixPath(path)
    require(not p.is_absolute() and all(part not in (".", "..", "") for part in path.split("/")), "source path escapes corpus")
    return str(p)


def source_uri(subject: str, path: str) -> str:
    return subject.rstrip("/") + "/source/" + quote(path, safe="/")


def sections(path: str, text: str, subject: str) -> list[dict[str, Any]]:
    """Partition bytes at headings; heading identities do not depend on line numbers."""
    lines = text.splitlines(keepends=True)
    if not lines:
        return [{"id": source_uri(subject, path) + "#preamble", "path": path,
                 "heading": "preamble", "start_line": 1, "end_line": 1, "text": ""}]
    starts: list[tuple[int, str]] = [(0, "preamble")]
    ancestry: list[str] = []
    counts: dict[str, int] = {}
    fence_char, fence_width = "", 0
    for index, line in enumerate(lines):
        # Bounded fenced-block recognition (CommonMark 0.31.2): up to three
        # spaces of indentation; a closer has the same marker, enough width,
        # and only horizontal whitespace after it. Shorter examples stay data.
        content = line.rstrip("\r\n\v\f\x1c\x1d\x1e\x85\u2028\u2029")
        if fence_char:
            if re.fullmatch(r" {0,3}" + re.escape(fence_char) + "{" + str(fence_width) + r",}[ \t]*", content):
                fence_char, fence_width = "", 0
            continue
        fence = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", content)
        if fence and (fence.group(1)[0] == "~" or "`" not in fence.group(2)):
            fence_char, fence_width = fence.group(1)[0], len(fence.group(1))
            continue
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line) if Path(path).suffix.lower() in (".md", ".markdown", ".mdown") else None
        if not heading:
            continue
        level, title = len(heading.group(1)), heading.group(2)
        ancestry = ancestry[:level - 1]
        ancestry.append(title)
        key = "/".join(ancestry)
        counts[key] = counts.get(key, 0) + 1
        label = key + (f"~{counts[key]}" if counts[key] > 1 else "")
        if index == 0:
            starts[0] = (0, label)
        else:
            starts.append((index, label))
    result = []
    for ordinal, (start, heading) in enumerate(starts):
        end = starts[ordinal + 1][0] if ordinal + 1 < len(starts) else len(lines)
        value = "".join(lines[start:end])
        result.append({"id": source_uri(subject, path) + "#" + quote(heading, safe=""), "path": path,
                       "heading": heading, "start_line": start + 1, "end_line": end, "text": value})
    require("".join(section["text"] for section in result) == text, "section partition lost source")
    return result


def make_chunks(all_sections: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    """No sampling or truncation: every character occurs in exactly one segment."""
    segments: list[dict[str, Any]] = []
    for section in all_sections:
        lines = section["text"].splitlines(keepends=True) or [""]
        require(all(len(line) <= limit for line in lines), f"{section['path']}: a single line exceeds --chunk-chars; reformat or increase explicit limit")
        parts: list[tuple[int, list[str]]] = []
        group: list[str] = []
        count = 0
        start = section["start_line"]
        for line in lines:
            if group and count + len(line) > limit:
                parts.append((start, group))
                start += len(group)
                group, count = [], 0
            group.append(line)
            count += len(line)
        parts.append((start, group))
        for first, group in parts:
            segment = dict(section)
            segment.update(text="".join(group), start_line=first, end_line=first + len(group) - 1)
            if len(parts) > 1:
                segment["parent_section_id"] = section["id"]
                segment["id"] += "/part/" + sha(segment["text"].encode())[:20]
            segment["sha256"] = sha(segment["text"].encode())
            segments.append(segment)
    chunks: list[dict[str, Any]] = []
    current: list[dict[str, Any]] = []
    count = 0
    for segment in segments:
        if current and count + len(segment["text"]) > limit:
            chunks.append({"id": "chunk-" + digest(current)[:20], "segments": current})
            current, count = [], 0
        current.append(segment)
        count += len(segment["text"])
    if current:
        chunks.append({"id": "chunk-" + digest(current)[:20], "segments": current})
    require(len({segment["id"] for chunk in chunks for segment in chunk["segments"]}) == len(segments), "ambiguous section/part identities")
    for chunk in chunks:
        chunk["source_chars"] = sum(len(segment["text"]) for segment in chunk["segments"])
    return chunks


def verify_upstream(path: Path) -> dict[str, Any]:
    path = path.resolve(strict=True)
    def git(*args: str) -> str:
        return subprocess.check_output(["git", "-C", str(path), *args], text=True).strip()
    require(Path(git("rev-parse", "--show-toplevel")).resolve() == path, "--upstream must name checkout root")
    require(git("rev-parse", "HEAD") == UPSTREAM_COMMIT, "upstream revision differs from tenant pin")
    require(not git("status", "--porcelain=v1", "--untracked-files=all"), "upstream checkout is modified")
    prompt = path / UPSTREAM_PROMPT
    return {"root": str(path), "commit": UPSTREAM_COMMIT, "prompt_path": UPSTREAM_PROMPT,
            "prompt_sha256": sha(prompt.read_bytes())}


def upstream_modules(path: Path) -> dict[str, Any]:
    verify_upstream(path)
    sys.path.insert(0, str(path.resolve()))
    modules = {}
    for name in ("extract", "build", "cluster", "export", "semantic_cleanup"):
        module = importlib.import_module("graphify." + name)
        require(Path(module.__file__).resolve().is_relative_to(path.resolve()), "Graphify imported from wrong installation")
        modules[name] = module
    return modules


def _selected_path(checker: dict[str, Any] | None, path: Path, *, write: bool = False,
                   directory: bool = False, absent: bool = False) -> Path:
    if checker is not None:
        return ac_formal_gate.guard_path(checker, path, output=write, directory=directory, absent=absent)
    return path


def _selected_read(checker: dict[str, Any] | None, path: Path) -> bytes:
    return ac_formal_gate.read_selected(checker, path) if checker is not None else path.read_bytes()


def _resolve_selection(plan: dict[str, Any], retained: Any, present: bool,
                       selected: dict[str, Any] | None) -> dict[str, Any] | None:
    prior = plan.get("formal_checker")
    if present:
        require(prior is None or retained == prior, "prepared formal checker selection changed")
        prior = retained
    elif prior is not None:
        raise GenerationError("prepared required formal checker selection is missing")
    if prior is not None and selected is not None:
        require(prior == selected, "required formal checker cannot be changed during generation")
    result = prior if prior is not None else selected
    if result is not None:
        ac_formal_gate.validate_config(result)
    return result


def _startup(output: Path, selected: dict[str, Any] | None = None) -> tuple[dict[str, Any], dict[str, Any] | None]:
    """Read only the operator-owned fixed startup files before reservation.

    This does not authenticate arbitrary request-selected run directories. The
    operator/wrapper owns the run and selection, under the cooperative host
    contract. No plan-named content is read until selected guards are active.
    """
    if selected is not None:
        ac_formal_gate.validate_config(selected)
        _selected_path(selected, output, write=True, directory=True)
    plan_path, selection_path = output / "plan.json", output / "formal-selection.json"
    _selected_path(selected, plan_path)
    _selected_path(selected, selection_path, absent=True)
    plan_raw = plan_path.read_bytes()
    present = selection_path.exists()
    selection_raw = selection_path.read_bytes() if present else None
    try:
        plan = _decode(plan_raw)
        retained = _decode(selection_raw) if present else None
    except (ValueError, UnicodeError) as exc:
        raise GenerationError("Malformed trusted generation startup metadata") from None
    checker = _resolve_selection(plan, retained, present, selected)
    if checker is not None:
        _selected_path(checker, output, write=True, directory=True)
        require(_selected_read(checker, plan_path) == plan_raw, "generation plan changed during startup")
        _selected_path(checker, selection_path, absent=True)
        if present:
            require(_selected_read(checker, selection_path) == selection_raw, "formal selection changed during startup")
    return plan, checker


def _selected_run(output: Path, selected: dict[str, Any] | None = None) -> tuple[dict[str, Any], dict[str, Any] | None]:
    """Metadata-only scan of the actual selected run, never a registered root.

    Downstream retained journals/actor files stay confined to this run. Concurrent
    host replacement after inspection is outside the cooperative host contract.
    """
    plan, checker = _startup(output, selected)
    if checker is not None:
        pending = [output]
        while pending:
            directory = pending.pop()
            for path in directory.iterdir():
                mode = path.lstat().st_mode
                is_directory = stat.S_ISDIR(mode)
                _selected_path(checker, path, directory=is_directory)
                if is_directory:
                    pending.append(path)
    return plan, checker


def _run_member(output: Path, path: Path) -> Path:
    """Direct selected entry boundary before its first retained-member read."""
    _, checker = _selected_run(output)
    if checker is not None:
        require(path.absolute().resolve().is_relative_to(output.absolute().resolve()), "selected member escapes retained run")
        _selected_path(checker, path)
    return path


def _run_path(output: Path, path: Path, *, write: bool = False, directory: bool = False,
              absent: bool = False) -> Path:
    _, checker = _startup(output)
    return _selected_path(checker, path, write=write, directory=directory, absent=absent)


def _upstream_path(output: Path, path: Path) -> Path:
    _run_path(output, path, directory=True)
    _run_path(output, path / UPSTREAM_PROMPT)
    return path


def prepare(corpus: Path, manifest_path: Path, output: Path, mode: str, upstream: Path | None,
            chunk_chars: int = 120_000, graph_chars: int = 40_000, *, formal_checker: dict[str, Any] | None = None) -> dict[str, Any]:
    require(mode in SEMANTIC_PROFILES, "unsupported generation mode")
    require(1_000 <= chunk_chars <= 500_000 and 1_000 <= graph_chars <= 200_000, "explicit chunk/graph character envelope outside supported range")
    if formal_checker is not None:
        ac_formal_gate.validate_config(formal_checker)
        _selected_path(formal_checker, output, write=True)
        _selected_path(formal_checker, corpus, directory=True)
        if upstream is not None:
            _selected_path(formal_checker, upstream, directory=True)
            _selected_path(formal_checker, upstream / UPSTREAM_PROMPT)
    corpus = corpus.resolve(strict=True)
    manifest = _decode(_selected_read(formal_checker, manifest_path))
    require(isinstance(manifest, dict) and isinstance(manifest.get("files"), list) and manifest["files"], "corpus manifest requires nonempty files array")
    subject = manifest.get("subject_id")
    require(isinstance(subject, str) and re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:[^\s]+$", subject), "manifest requires absolute subject_id")
    upstream_record = verify_upstream(upstream) if upstream else None
    require(mode == "direct" or upstream_record is not None, "Graphify mode requires --upstream")
    require(not output.exists(), "output already exists; use stage commands to resume")
    pinned, all_sections, file_seen = [], [], set()
    for entry in manifest["files"]:
        path = safe_relative(entry["path"])
        require(path not in file_seen, "duplicate corpus source path")
        file_seen.add(path)
        source = corpus / path
        require(source.resolve(strict=True).is_relative_to(corpus), "source symlink escapes corpus")
        raw = _selected_read(formal_checker, source)
        require(sha(raw) == entry["sha256"], f"source digest mismatch: {path}")
        if "bytes" in entry:
            require(len(raw) == entry["bytes"], f"source byte count mismatch: {path}")
        text = raw.decode("utf-8")
        require("\r" not in text, f"{path}: CR line endings unsupported; pin LF source explicitly")
        pinned.append({"path": path, "sha256": sha(raw), "bytes": len(raw)})
        all_sections.extend(sections(path, text, subject))
    chunks = make_chunks(all_sections, chunk_chars)
    # Validate all inputs before creating the checkpoint directory.
    output.mkdir(parents=True)
    for entry in pinned:
        destination = output / "corpus" / entry["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        _selected_path(formal_checker, destination, write=True).write_bytes(_selected_read(formal_checker, corpus / entry["path"]))
    save(output / "source-manifest.json", manifest, exclusive=True)
    save(output / "chunks.json", chunks, exclusive=True)
    if mode == "graphify":
        (output / "upstream-extraction-spec.md").write_bytes(_selected_read(formal_checker, Path(upstream_record["root"]) / UPSTREAM_PROMPT))
    assets = {path.name: sha(path.read_bytes()) for path in sorted(ASSETS.iterdir()) if path.is_file()}
    plan = {"profile": "ac.generation.plan/1", "mode": mode, "subject_id": subject,
            "semantic_extraction_profile": SEMANTIC_PROFILES[mode],
            "source_manifest_sha256": sha((output / "source-manifest.json").read_bytes()),
            "files": pinned, "chunks_sha256": sha((output / "chunks.json").read_bytes()),
            "chunks": [{"id": chunk["id"], "segments": len(chunk["segments"]), "source_chars": chunk["source_chars"]} for chunk in chunks],
            "chunk_chars": chunk_chars, "graph_chars": graph_chars, "upstream": upstream_record,
            "runner_sha256": sha(Path(__file__).read_bytes()), "codec_sha256": sha((HERE / "ac_graph.py").read_bytes()),
            "assets": assets, "calculus": {"uri": ac_graph.CALCULUS_URI, "sha256": ac_graph.CALCULUS_SHA256},
            "claim": "Fresh F_P proposal authoring; processing coverage is not semantic completeness or acceptance."}
    if formal_checker is not None:
        plan["formal_checker"] = formal_checker
        save(output / "formal-selection.json", formal_checker, exclusive=True)
    save(output / "plan.json", plan, exclusive=True)
    return plan


def checkpoint(output: Path, *, formal_checker: dict[str, Any] | None = None) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    plan, checker = _selected_run(output, formal_checker)
    require(plan.get("profile") == "ac.generation.plan/1", "unknown generation plan")
    def read(path: Path) -> bytes:
        return _selected_read(checker, path)
    require(sha(read(output / "source-manifest.json")) == plan["source_manifest_sha256"], "source manifest changed")
    chunks_raw = read(output / "chunks.json")
    require(sha(chunks_raw) == plan["chunks_sha256"], "chunk plan changed")
    require(sha(read(Path(__file__))) == plan["runner_sha256"], "runner changed since preparation; create a new plan")
    require(sha(read(HERE / "ac_graph.py")) == plan["codec_sha256"], "codec changed since preparation")
    require({path.name: sha(read(path)) for path in ASSETS.iterdir() if path.is_file()} == plan["assets"], "generation schemas/prompts changed")
    for entry in plan["files"]:
        relative = safe_relative(entry["path"]) if checker is not None else entry["path"]
        source = output / "corpus" / relative
        _selected_path(checker, source)
        require(source.resolve(strict=True).is_relative_to((output / "corpus").resolve()), "snapshot source escapes checkpoint")
        require(sha(read(source)) == entry["sha256"], "frozen source bytes changed: " + relative)
    if plan["mode"] == "graphify":
        require(sha(read(output / "upstream-extraction-spec.md")) == plan["upstream"]["prompt_sha256"], "upstream prompt changed")
    chunks = _decode(chunks_raw)
    if checker is not None:
        for chunk in chunks:
            require("/" not in safe_relative(chunk["id"]), "selected chunk id must be one safe basename")
            for segment in chunk["segments"]:
                safe_relative(segment["path"])
    return plan, chunks


def schema_errors(value: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    """Small validator for the closed JSON Schema subset authored in generation/."""
    errors: list[str] = []
    kind = schema.get("type")
    if isinstance(kind, list):
        return [] if any(not schema_errors(value, {**schema, "type": candidate}, path) for candidate in kind) else [path + ": no matching type"]
    types = {"object": dict, "array": list, "string": str, "integer": int, "number": (int, float), "boolean": bool, "null": type(None)}
    if kind in types and (not isinstance(value, types[kind]) or kind in ("integer", "number") and isinstance(value, bool)):
        return [path + ": expected " + str(kind)]
    if "enum" in schema and value not in schema["enum"]:
        errors.append(path + ": invalid enum")
    if kind == "object":
        required = schema.get("required", [])
        props = schema.get("properties", {})
        if not set(required) <= set(value) or schema.get("additionalProperties") is False and not set(value) <= set(props):
            errors.append(path + ": missing/additional fields")
        for key in set(value) & set(props):
            errors.extend(schema_errors(value[key], props[key], path + "/" + key))
    if kind == "array":
        if len(value) < schema.get("minItems", 0) or len(value) > schema.get("maxItems", 10**9):
            errors.append(path + ": array length")
        for index, child in enumerate(value):
            errors.extend(schema_errors(child, schema["items"], path + "/" + str(index)))
    if kind == "string" and (len(value) < schema.get("minLength", 0) or "pattern" in schema and not re.fullmatch(schema["pattern"], value)):
        errors.append(path + ": string constraint")
    if kind in ("integer", "number") and (value < schema.get("minimum", -float("inf")) or value > schema.get("maximum", float("inf"))):
        errors.append(path + ": number range")
    return errors


def author_check(answer: dict[str, Any], chunk: dict[str, Any]) -> None:
    errors = schema_errors(answer, load(ASSETS / "author.schema.json"))
    require(not errors, "author schema: " + "; ".join(errors[:10]))
    segment_map = {segment["id"]: segment for segment in chunk["segments"]}
    records = [record for family in ("concepts", "relations", "constraints", "latitude", "residuals") for record in answer[family]]
    keys = [record["key"] for record in records]
    require(len(keys) == len(set(keys)), "author record keys are not unique within chunk")
    concept_keys = {record["key"] for record in answer["concepts"]}
    for record in records:
        record_path = "record[" + record["key"] + "]"
        require(bool(record["grounding"]), record_path + ": every authored record requires exact source grounding")
        for ordinal, ground in enumerate(record["grounding"]):
            ground_path = record_path + "/grounding/" + str(ordinal)
            require(ground["section_id"] in segment_map, ground_path + ": grounding names source outside chunk")
            segment = segment_map[ground["section_id"]]
            first, last = ground["start_line"], ground["end_line"]
            require(segment["start_line"] <= first <= last <= segment["end_line"], ground_path + ": grounding line range escapes supplied section")
            lines = segment["text"].splitlines(keepends=True)
            excerpt = "".join(lines[first - segment["start_line"]:last - segment["start_line"] + 1])
            require(bool(ground["quote"].strip()) and ground["quote"] in excerpt, ground_path + ": grounding quote is not exact source at declared range")
    for relation in answer["relations"]:
        require(relation["source_key"] in concept_keys and relation["target_key"] in concept_keys, "relation endpoints must be declared local concepts")
    for record in answer["constraints"] + answer["latitude"]:
        require(set(record["applies_to_keys"]) <= concept_keys and record["applies_to_keys"], "attachment targets must be declared local concepts")
    for record in answer["residuals"]:
        require(record["subject_key"] in set(keys) - {record["key"]}, "residual subject must be another local declared record")
        require(record["subject_key"] not in {r["key"] for r in answer["residuals"]}, "residual subjects must be concepts/relations/constraints/latitude")
    dispositions = answer["dispositions"]
    require(len(dispositions) == len(segment_map) and {d["section_id"] for d in dispositions} == set(segment_map), "section dispositions do not cover exact supplied sections")
    selected: set[str] = set()
    residual_keys = {record["key"] for record in answer["residuals"]}
    for disposition in dispositions:
        chosen = disposition["keys"]
        require(len(chosen) == len(set(chosen)) and set(chosen) <= set(keys), "disposition has duplicate/unknown record key")
        require(disposition["decision"] not in ("retained", "residual") or bool(chosen), "retained/residual section requires authored records")
        require(disposition["decision"] != "residual" or bool(set(chosen) & residual_keys), "residual disposition requires residual record")
        # A source section may select cross-linked records, but must retain at
        # least one record actually grounded in that section when claiming it.
        if disposition["decision"] in ("retained", "residual"):
            require(any(record["key"] in chosen and any(g["section_id"] == disposition["section_id"] for g in record["grounding"]) for record in records), "retained section has no local grounded record")
        selected.update(chosen)
    require(selected == set(keys), "selection ledger omits authored records")


def semantic_check(answer: dict[str, Any], chunk: dict[str, Any], output: Path, modules: dict[str, Any]) -> None:
    errors = schema_errors(answer, load(ASSETS / "extraction.schema.json"))
    require(not errors, "extraction schema: " + "; ".join(errors[:10]))
    # Validator can normalize hyperedge aliases. Inspect a copy; raw actor bytes
    # and their documented concept/rationale types are never sanitized.
    errors = modules["semantic_cleanup"].validate_semantic_fragment(copy.deepcopy(answer))
    require(not errors, "upstream semantic fragment: " + "; ".join(errors[:10]))
    files = {str((output / "corpus" / segment["path"]).resolve()) for segment in chunk["segments"]}
    ids = [node["id"] for node in answer["nodes"]]
    require(len(ids) == len(set(ids)), "duplicate semantic node identity within fragment")
    for entry in answer["nodes"] + answer["edges"] + answer["hyperedges"]:
        require(entry["source_file"] in files, "semantic fragment source_file is not a verbatim supplied source path")
    nonempty = {str((output / "corpus" / segment["path"]).resolve()) for segment in chunk["segments"] if segment["text"].strip()}
    require(nonempty <= {node["source_file"] for node in answer["nodes"]}, "semantic extraction omits a nonempty supplied source file; retain at least a named document node")
    for edge in answer["edges"]:
        require(edge["source"] in set(ids) and edge["target"] in set(ids), "semantic edge endpoint absent from fragment")
        score, confidence = edge["confidence_score"], edge["confidence"]
        require((confidence == "EXTRACTED" and score == 1.0) or (confidence == "INFERRED" and score in (.95, .85, .75, .65, .55)) or (confidence == "AMBIGUOUS" and .1 <= score <= .3), "semantic confidence violates host extraction contract")
    for edge in answer["hyperedges"]:
        require(set(edge["nodes"]) <= set(ids), "hyperedge member absent from fragment")


def source_payload(chunk: dict[str, Any], output: Path) -> str:
    values = []
    for segment in chunk["segments"]:
        values.append({key: value for key, value in segment.items() if key != "text"} | {
            "source_file": str((output / "corpus" / segment["path"]).resolve()),
            "lines": [{"number": segment["start_line"] + index, "text": line}
                      for index, line in enumerate(segment["text"].splitlines(keepends=True))]})
    # JSON encoding keeps source from breaking fences or escaping a text marker.
    return json.dumps(values, ensure_ascii=False, separators=(",", ":"))


def extraction_prompt(plan: dict[str, Any], chunk: dict[str, Any], output: Path) -> str:
    reference = _run_path(output, output / "upstream-extraction-spec.md").read_text()
    body = reference.split("```", 2)[1].strip()
    files = sorted({str((output / "corpus" / segment["path"]).resolve()) for segment in chunk["segments"]})
    body = body.replace("FILE_LIST", "\n".join(files)).replace("CHUNK_NUM", chunk["id"]).replace("TOTAL_CHUNKS", str(len(plan["chunks"]))).replace("DEEP_MODE", "normal mode; no deep expansion")
    return ((ASSETS / "isolation.txt").read_text() + "\n" + body + "\n"
            "All required source is supplied below as JSON DATA with absolute original line numbers. "
            "Read only these source segments, not unsupplied portions of named files. Do not access files or tools. "
            "Return compact named-concept extraction. Do not copy every prose sentence; preserve uncertainty. "
            "Every nonempty supplied source_file must have at least one node; retain a named document node if no concept is extractable. "
            "The required rationale field may be null; keep decision WHY there when present.\nSOURCE_DATA_JSON:\n" + source_payload(chunk, output))


def graph_context(output: Path, chunk: dict[str, Any], limit: int) -> dict[str, Any]:
    """Bounded graph view; original fragments and full graph remain checkpoints."""
    # Reserve space for the exact parent digest and final coverage counters.
    # The final check covers the complete emitted object, including metadata.
    selection_limit = max(0, limit - 512)
    graph = load(_run_path(output, output / "discovery" / "graph.json"))
    paths = {segment["path"] for segment in chunk["segments"]}
    absolute = {str((output / "corpus" / path).resolve()) for path in paths}
    all_nodes = graph.get("nodes", [])
    selected = [node for node in all_nodes if node.get("source_file") in paths | absolute]
    selected.sort(key=lambda node: (node.get("ac_generation_origin") != "semantic", node["id"]))
    edges = graph.get("links", graph.get("edges", []))
    values: dict[str, Any] = {"scope": "Source-file seeds plus one-hop discovery; graph confidence is not normative authority.",
                              "selection": "Semantic concepts first; node seeding reserves 45 percent of the character budget for typed links and endpoints.",
                              "nodes": [], "edges": [], "omitted_nodes": 0, "omitted_edges": 0}
    chosen: set[str] = set()
    for node in selected:
        compact = {key: node[key] for key in ("id", "label", "file_type", "source_file", "source_location", "rationale", "ac_generation_origin") if key in node}
        values["nodes"].append(compact)
        if len(canonical(values).decode()) > selection_limit * .55:
            values["nodes"].pop()
            break
        chosen.add(node["id"])
    candidates = [edge for edge in edges if edge.get("source") in chosen or edge.get("target") in chosen]
    candidates.sort(key=lambda edge: (not (edge.get("source") in chosen and edge.get("target") in chosen),
                                      edge.get("ac_generation_origin") != "semantic", str(edge.get("source")), str(edge.get("target")), str(edge.get("relation"))))
    all_by_id = {node["id"]: node for node in all_nodes}
    for edge in candidates:
        missing = [identity for identity in (edge["source"], edge["target"]) if identity not in chosen]
        nodes = [{key: all_by_id[identity][key] for key in ("id", "label", "file_type", "source_file", "source_location", "rationale", "ac_generation_origin") if key in all_by_id[identity]} for identity in missing if identity in all_by_id]
        compact = {key: edge[key] for key in ("source", "target", "relation", "confidence", "confidence_score", "source_file", "source_location", "ac_generation_origin") if key in edge}
        values["nodes"].extend(nodes)
        values["edges"].append(compact)
        if len(canonical(values).decode()) > selection_limit:
            values["edges"].pop()
            if nodes:
                del values["nodes"][-len(nodes):]
            continue
        chosen.update(node["id"] for node in nodes)
    values["omitted_nodes"] = len(all_nodes) - len(values["nodes"])
    values["omitted_edges"] = len(edges) - len(values["edges"])
    values["full_graph_sha256"] = sha((output / "discovery" / "graph.json").read_bytes())
    values["semantic_seed_nodes"] = sum(node.get("ac_generation_origin") == "semantic" for node in values["nodes"])
    require(len(canonical(values).decode()) <= limit, "complete graph discovery context exceeds --graph-chars")
    return values


def author_prompt(plan: dict[str, Any], chunk: dict[str, Any], output: Path) -> str:
    prompt = (ASSETS / "isolation.txt").read_text() + "\n" + (ASSETS / "author.txt").read_text()
    prompt += "\nSUBJECT_DATA_JSON:\n" + json.dumps({"subject_id": plan["subject_id"], "source_manifest_sha256": plan["source_manifest_sha256"], "calculus_basis": plan["calculus"], "chunk": chunk["id"],
                                                      "semantic_extraction_profile": plan["semantic_extraction_profile"]}, ensure_ascii=False)
    if plan["mode"] in GRAPH_MODES:
        context = graph_context(output, chunk, plan["graph_chars"])
        prompt += "\nGRAPHIFY_DISCOVERY_DATA_JSON:\n" + json.dumps(context, ensure_ascii=False, separators=(",", ":"))
    prompt += "\nSOURCE_DATA_JSON:\n" + source_payload(chunk, output)
    return prompt


def actor_settings(codex: str, chosen: dict[str, Any] | None = None) -> tuple[str, dict[str, Any], dict[str, Any]]:
    executable = shutil.which(codex)
    require(executable is not None, "Codex CLI is unavailable")
    config_path = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "config.toml"
    raw = config_path.read_bytes()
    config = tomllib.loads(raw.decode())
    settings = {key: config[key] for key in SETTING_KEYS if key in config}
    settings.update(chosen or {})
    require("model" in settings and "model_reasoning_effort" in settings, "existing CLI config must select model and reasoning effort")
    inventory = json.loads(subprocess.check_output([executable, "mcp", "list", "--json"]))
    overrides = dict(settings)
    overrides.update({"features.shell_tool": False, "features.apps": False, "features.multi_agent": False,
                      "features.memories": False, "features.js_repl": False, "web_search": "disabled", "project_doc_max_bytes": 0})
    for name in set(config.get("mcp_servers", {})) | {row["name"] for row in inventory}:
        require(re.fullmatch(r"[A-Za-z0-9_-]+", name) is not None, "MCP name unsupported by inline CLI isolation")
        if name not in config.get("mcp_servers", {}):
            overrides["mcp_servers." + name + ".command"] = "/usr/bin/false"
        overrides["mcp_servers." + name + ".enabled"] = False
    return executable, overrides, {"settings": settings, "config_path": str(config_path), "config_sha256": sha(raw),
                                   "cli_version": subprocess.check_output([executable, "--version"], text=True).strip()}


def run_actor(prompt: str, schema: Path, attempt: Path, codex: str, timeout: int,
              expected_settings: dict[str, Any] | None = None) -> dict[str, Any]:
    require(not attempt.exists(), "actor attempt path exists")
    executable, overrides, metadata = actor_settings(codex, expected_settings)
    if expected_settings is not None:
        require(metadata["settings"] == expected_settings, "CLI model/settings changed between generation stages")
    attempt.mkdir(parents=True)
    work = attempt / "empty-workspace"
    work.mkdir()
    (attempt / "prompt.txt").write_text(prompt, encoding="utf-8")
    arguments = []
    for key, value in overrides.items():
        arguments.extend(["-c", key + "=" + json.dumps(value, ensure_ascii=False)])
    effective = json.loads(subprocess.check_output([executable, "mcp", "list", "--json", *arguments], cwd=work))
    require(not any(row["enabled"] for row in effective), "actor MCP isolation failed")
    command = [executable, "exec", "--json", "--ephemeral", "--sandbox", "read-only", "--skip-git-repo-check", "--color", "never",
               "--output-schema", str(schema.resolve()), "--output-last-message", str((attempt / "answer.json").resolve()),
               "--cd", str(work.resolve()), *arguments, "-"]
    invocation = {"profile": "ac.generation.actor-invocation/1", **metadata, "command": command,
                  "inline_overrides": overrides, "cwd": str(work), "prompt_sha256": sha(prompt.encode()),
                  "schema_sha256": sha(schema.read_bytes()), "timeout_seconds": timeout,
                  "effective_mcp_inventory": [{"name": row["name"], "enabled": row["enabled"]} for row in effective]}
    save(attempt / "invocation.json", invocation, exclusive=True)
    started = time.perf_counter()
    timed_out = False
    with (attempt / "events.jsonl").open("xb") as events, (attempt / "stderr.txt").open("xb") as errors:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=events, stderr=errors, cwd=work, start_new_session=True)
        try:
            process.communicate(prompt.encode(), timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.communicate(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.communicate()
    elapsed = time.perf_counter() - started
    failures: list[str] = []
    if timed_out:
        failures.append("process_timeout")
    if process.returncode:
        failures.append("cli_nonzero_exit")
    parsed = []
    invalid = 0
    for line in (attempt / "events.jsonl").read_text().splitlines():
        try:
            parsed.append(json.loads(line))
        except ValueError:
            invalid += 1
    if invalid:
        failures.append("invalid_event_json")
    usage = [event["usage"] for event in parsed if event.get("type") == "turn.completed" and "usage" in event]
    if not usage:
        failures.append("missing_backend_usage")
    item_types = [event["item"].get("type") for event in parsed if event.get("type") in ("item.started", "item.completed") and isinstance(event.get("item"), dict)]
    unexpected = sorted({kind for kind in item_types if kind not in ("agent_message", "reasoning")}, key=str)
    if unexpected:
        failures.append("isolation_violation")
    answer_sha = None
    try:
        answer = load(attempt / "answer.json")
        answer_sha = sha((attempt / "answer.json").read_bytes())
        output_errors = schema_errors(answer, load(schema))
    except (OSError, ValueError) as exc:
        output_errors = [str(exc)]
    if output_errors:
        failures.append("output_schema_failure")
    config_unchanged = sha(Path(metadata["config_path"]).read_bytes()) == metadata["config_sha256"]
    if not config_unchanged:
        failures.append("user_config_changed")
    result = {"profile": "ac.generation.actor-result/1", "status": "completed" if not failures else "failed",
              "failures": failures, "elapsed_seconds": elapsed, "usage_events": usage, "cli_exit_code": process.returncode,
              "timed_out": timed_out, "unexpected_item_types": unexpected, "schema_errors": output_errors,
              "user_config_unchanged": config_unchanged, "answer_sha256": answer_sha,
              "events_sha256": sha((attempt / "events.jsonl").read_bytes()), "stderr_sha256": sha((attempt / "stderr.txt").read_bytes()),
              "settings": metadata["settings"], "cli_version": metadata["cli_version"]}
    save(attempt / "usage.json", {"usage_events": usage, "claim": "Exact CLI-reported counters; no price or billing inference."}, exclusive=True)
    save(attempt / "result.json", result, exclusive=True)
    return result


def actor_evidence(output: Path, plan: dict[str, Any], chunk: dict[str, Any], attempt: Path, *,
                   stage: str = "author", allow_source_failure: bool = False) -> tuple[dict[str, Any], dict[str, Any]]:
    """Authenticate retained coordinates/audit consistency, not issuer legitimacy."""
    require(stage in ("author", "extract"), "unknown actor evidence stage")
    require(not allow_source_failure or stage == "author", "source-failure recovery is author-only")
    frozen_plan, frozen_chunks = checkpoint(output)
    require(canonical(plan) == canonical(frozen_plan), "supplied plan differs from exact frozen plan")
    matches = [value for value in frozen_chunks if value["id"] == chunk["id"]]
    require(len(matches) == 1 and canonical(matches[0]) == canonical(chunk), "supplied chunk differs from exact frozen chunk")
    plan, chunk = frozen_plan, matches[0]
    require(stage != "extract" or plan["mode"] == "graphify", "selected mode has no graph extraction actor")
    if stage == "author" and plan["mode"] in GRAPH_MODES:
        verify_discovery(output)
    require(attempt.resolve().is_relative_to(output.resolve()), "actor attempt escapes the selected run")
    require(attempt.resolve().is_relative_to((output / "actors" / stage / chunk["id"]).resolve()), "actor attempt escapes expected source chunk")
    paths = ("answer.json", "result.json", "invocation.json", "prompt.txt", "events.jsonl", "stderr.txt", "usage.json")
    require(all((attempt / name).is_file() for name in paths), "incomplete actor evidence")
    require(all((attempt / name).resolve().is_relative_to(output.resolve()) for name in paths), "actor evidence symlink escapes selected run")
    for name in paths:
        _run_path(output, attempt / name)
    _run_path(output, attempt / "validation.json", absent=True)
    _run_path(output, output / "actor-settings.json")
    result = load(attempt / "result.json")
    invocation = load(attempt / "invocation.json")
    settings = load(output / "actor-settings.json")
    require(result.get("profile") == "ac.generation.actor-result/1" and invocation.get("profile") == "ac.generation.actor-invocation/1", "unknown actor evidence profile")
    allowed = result.get("status") == "completed" and result.get("failures") == [] or (
        allow_source_failure and result.get("status") == "failed" and result.get("failures") == ["source_or_semantic_fragment_validation"] and isinstance(result.get("validation_error"), str))
    require(allowed, "actor failure is not solely source-fragment validation")
    require(type(result.get("cli_exit_code")) is int and result.get("cli_exit_code") == 0 and result.get("timed_out") is False and result.get("user_config_unchanged") is True,
            "CLI exit/timeout/config custody failed")
    require(result.get("schema_errors") == [] and result.get("unexpected_item_types") == [], "schema or isolation failure in actor evidence")
    for name, field in (("answer.json", "answer_sha256"), ("events.jsonl", "events_sha256"), ("stderr.txt", "stderr_sha256")):
        require(sha((attempt / name).read_bytes()) == result.get(field), "stale original " + name)
    require(invocation.get("settings") == settings["settings"] == result.get("settings"), "frozen actor settings differ")
    require(invocation.get("cli_version") == settings["cli_version"] == result.get("cli_version"), "frozen actor CLI version differs")
    require(isinstance(invocation.get("config_path"), str) and re.fullmatch(r"[0-9a-f]{64}", invocation.get("config_sha256", "")) is not None, "original configuration coordinates are malformed")
    schema = ASSETS / ("extraction.schema.json" if stage == "extract" else "author.schema.json")
    require(invocation.get("schema_sha256") == plan["assets"][schema.name] == sha(schema.read_bytes()), "actor schema identity differs")
    prompt = extraction_prompt(plan, chunk, output) if stage == "extract" else author_prompt(plan, chunk, output)
    require(invocation.get("prompt_sha256") == sha((attempt / "prompt.txt").read_bytes()) == sha(prompt.encode()),
            "actor prompt does not belong to this exact source chunk and discovery context")
    overrides = invocation.get("inline_overrides", {})
    required_overrides = {"features.shell_tool": False, "features.apps": False, "features.multi_agent": False,
                          "features.memories": False, "features.js_repl": False, "web_search": "disabled", "project_doc_max_bytes": 0}
    require(all(overrides.get(key) == value and type(overrides.get(key)) is type(value) for key, value in required_overrides.items()), "actor tool/document isolation overrides differ")
    require(all(overrides.get(key) == value for key, value in settings["settings"].items()), "command model/settings overrides differ")
    inventory = invocation.get("effective_mcp_inventory")
    require(isinstance(inventory, list) and all(isinstance(row, dict) and isinstance(row.get("name"), str) and row.get("enabled") is False for row in inventory), "actor MCP isolation failed")
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
    require(expected_cwd.is_dir() and expected_cwd.is_relative_to(attempt.resolve()) and not any(expected_cwd.iterdir()), "actor workspace is not retained empty and isolated")
    events = [json.loads(line) for line in (attempt / "events.jsonl").read_text().splitlines()]
    require(all(isinstance(event, dict) for event in events), "invalid actor event object")
    require(not any(event.get("type") in ("error", "turn.failed") for event in events), "actor event stream contains a failed turn")
    usage = [event["usage"] for event in events if event.get("type") == "turn.completed" and "usage" in event]
    require(bool(usage) and usage == result.get("usage_events") == load(attempt / "usage.json").get("usage_events"), "retained CLI usage is absent or contradictory")
    item_types = [event["item"].get("type") for event in events if event.get("type") in ("item.started", "item.completed") and isinstance(event.get("item"), dict)]
    require(all(kind in ("agent_message", "reasoning") for kind in item_types), "actual actor tool/isolation violation")
    answer = load(attempt / "answer.json")
    require(not schema_errors(answer, load(schema)), "raw actor answer is not schema-valid")
    original_error = None
    try:
        if stage == "extract":
            semantic_check(answer, chunk, output, upstream_modules(Path(plan["upstream"]["root"])))
        else:
            author_check(answer, chunk)
    except GenerationError as exc:
        original_error = str(exc)
    if not allow_source_failure:
        require(original_error is None, "completed actor fails exact source validation: " + str(original_error))
        require((attempt / "validation.json").is_file(), "completed actor lacks strict source validation")
    if result["status"] == "failed":
        require(original_error is not None and result.get("validation_error") == original_error, "recorded original source-validation failure contradicts exact recomputation")
    pins = {str((attempt / name).relative_to(output)): sha((attempt / name).read_bytes()) for name in paths}
    pins["actor-settings.json"] = sha((output / "actor-settings.json").read_bytes())
    for name in ("plan.json", "source-manifest.json", "chunks.json"):
        pins[name] = sha((output / name).read_bytes())
    if (attempt / "validation.json").exists():
        validation = load(attempt / "validation.json")
        require(validation.get("answer_sha256") == result["answer_sha256"] and validation.get("chunk_sha256") == digest(chunk), "strict original validation belongs to a different answer/chunk")
        pins[str((attempt / "validation.json").relative_to(output))] = sha((attempt / "validation.json").read_bytes())
    proof = {"original_attempt": str(attempt.relative_to(output)), "original_status": result["status"],
             "original_recorded_failure": result.get("validation_error"), "original_strict_validation_error": original_error,
             "original_usage_events": usage, "pins": pins, "chunk_sha256": digest(chunk),
             "source_sections": [{key: section[key] for key in ("id", "path", "start_line", "end_line", "sha256")} for section in chunk["segments"]]}
    return answer, proof

def successful_attempt(output: Path, stage: str, chunk: dict[str, Any]) -> Path | None:
    """Reuse only the latest strictly validated attempt with complete frozen custody."""
    require(stage in ("extract", "author"), "unknown actor stage")
    root = output / "actors" / stage / chunk["id"]
    attempts = sorted(path for path in root.iterdir() if path.is_dir()) if root.exists() else []
    if not attempts:
        return None
    attempt = attempts[-1]
    # A newer failed/unfinished retry remains visible; never fall back to an
    # older success. Stage execution still requires explicit --retry-failed.
    _run_path(output, attempt / "result.json", absent=True)
    _run_path(output, attempt / "validation.json", absent=True)
    if not (attempt / "result.json").is_file() or load(attempt / "result.json").get("status") != "completed":
        return None
    if not (attempt / "validation.json").is_file():
        return None
    actor_evidence(output, load(output / "plan.json"), chunk, attempt, stage=stage)
    return attempt


def stage(output: Path, name: str, *, execute: bool, codex: str = "codex", timeout: int = 1200,
          max_chunks: int | None = None, jobs: int = 1, retry_failed: bool = False,
          upstream: Path | None = None, model: str | None = None, effort: str | None = None) -> dict[str, Any]:
    plan, chunks = checkpoint(output)
    require(name in ("extract", "author"), "unknown actor stage")
    require(name != "extract" or plan["mode"] == "graphify", "selected mode has no graph extraction actor")
    require(1 <= jobs <= 4 and 1 <= timeout <= 3600, "unsupported jobs/timeout")
    require(max_chunks is None or max_chunks > 0, "--max-chunks must be positive")
    if name == "author" and plan["mode"] in GRAPH_MODES:
        require((output / "discovery" / "result.json").exists(), "build the discovery graph before authoring")
        verify_discovery(output)
    modules = upstream_modules(_upstream_path(output, upstream or Path(plan["upstream"]["root"]))) if name == "extract" else None
    pending = [chunk for chunk in chunks if successful_attempt(output, name, chunk) is None]
    selected = pending[:max_chunks] if max_chunks is not None else pending
    settings_path = _run_path(output, output / "actor-settings.json", write=True)
    if execute and selected:
        chosen = {key: value for key, value in (("model", model), ("model_reasoning_effort", effort)) if value is not None}
        _, _, metadata = actor_settings(codex, chosen)
        if settings_path.exists():
            fixed = load(settings_path)
            require(fixed["settings"] == metadata["settings"] and fixed["cli_version"] == metadata["cli_version"], "actor settings/CLI changed across chunks")
        else:
            save(settings_path, {"settings": metadata["settings"], "cli_version": metadata["cli_version"]}, exclusive=True)
    def one(chunk: dict[str, Any]) -> dict[str, Any]:
        prompt = extraction_prompt(plan, chunk, output) if name == "extract" else author_prompt(plan, chunk, output)
        if not execute:
            path = output / "prepared-prompts" / name / (chunk["id"] + ".txt")
            _run_path(output, path, write=True)
            path.parent.mkdir(parents=True, exist_ok=True)
            if path.exists():
                require(path.read_text() == prompt, "prepared prompt changed")
            else:
                path.write_text(prompt)
            return {"chunk": chunk["id"], "status": "prepared_only", "prompt_chars": len(prompt)}
        root = output / "actors" / name / chunk["id"]
        attempts = sorted(root.iterdir()) if root.exists() else []
        require(not attempts or retry_failed, f"{chunk['id']}: failed/interrupted attempt preserved; explicit --retry-failed required")
        attempt = root / f"attempt-{len(attempts) + 1:03d}"
        _run_path(output, attempt, write=True)
        result = run_actor(prompt, ASSETS / ("extraction.schema.json" if name == "extract" else "author.schema.json"), attempt, codex, timeout, load(settings_path)["settings"])
        if result["status"] == "completed":
            try:
                answer = load(attempt / "answer.json")
                if name == "extract":
                    semantic_check(answer, chunk, output, modules)
                else:
                    author_check(answer, chunk)
                save(attempt / "validation.json", {"status": "structurally_valid_proposal", "answer_sha256": sha((attempt / "answer.json").read_bytes()),
                                                    "chunk_sha256": digest(chunk), "claim": "Source coordinates and declared shape checked; semantic fitness unassessed."}, exclusive=True)
            except GenerationError as exc:
                result["status"] = "failed"
                result["failures"].append("source_or_semantic_fragment_validation")
                result["validation_error"] = str(exc)
                save(attempt / "result.json", result)
        return {"chunk": chunk["id"], "attempt": str(attempt.relative_to(output)), **result}
    with ThreadPoolExecutor(max_workers=jobs) as executor:
        results = list(executor.map(one, selected))
    completed = [chunk["id"] for chunk in chunks if successful_attempt(output, name, chunk)]
    summary = {"profile": "ac.generation.stage/1", "stage": name, "mode": plan["mode"], "processed": results,
               "completed_chunks": completed, "remaining_chunks": [chunk["id"] for chunk in chunks if chunk["id"] not in completed],
               "status": "completed" if len(completed) == len(chunks) else "incomplete"}
    save(_run_path(output, output / (name + "-status.json"), write=True), summary)
    return summary


def verify_discovery(output: Path) -> dict[str, Any]:
    record = load(_run_path(output, output / "discovery" / "result.json"))
    _run_path(output, output / "discovery" / "coverage.json")
    require(record.get("status") == "completed", "discovery graph incomplete")
    mode = load(output / "plan.json")["mode"]
    require(record.get("mode") == mode and mode in GRAPH_MODES, "discovery treatment differs from generation plan")
    for path, expected in record["files"].items():
        require(sha(_run_member(output, output / "discovery" / path).read_bytes()) == expected, "discovery graph changed: " + path)
    chunks = {chunk["id"]: chunk for chunk in load(output / "chunks.json")}
    for entry in load(output / "discovery" / "coverage.json")["chunks"]:
        require(entry["id"] in chunks, "discovery provenance names unknown source chunk")
        if mode == "graphify":
            attempt = successful_attempt(output, "extract", chunks[entry["id"]])
            require(attempt is not None and str(attempt.relative_to(output)) == entry["attempt"], "discovery extraction checkpoint changed")
            require(sha((attempt / "answer.json").read_bytes()) == entry["answer_sha256"], "discovery fragment changed")
        else:
            require("attempt" not in entry and "answer_sha256" not in entry, "structural-only discovery cannot claim an extraction actor")
    require({entry["id"] for entry in load(output / "discovery" / "coverage.json")["chunks"]} == set(chunks), "discovery provenance does not cover exact chunk plan")
    return record


def build_discovery(output: Path, upstream: Path | None = None) -> dict[str, Any]:
    plan, chunks = checkpoint(output)
    require(plan["mode"] in GRAPH_MODES, "direct mode does not build a discovery graph")
    folder = _run_path(output, output / "discovery", write=True)
    if folder.exists():
        return verify_discovery(output)
    attempts = [successful_attempt(output, "extract", chunk) for chunk in chunks] if plan["mode"] == "graphify" else []
    require(plan["mode"] != "graphify" or all(attempts), "every source chunk needs a validated fresh semantic extraction before graph build")
    modules = upstream_modules(_upstream_path(output, upstream or Path(plan["upstream"]["root"])))
    folder.mkdir()
    started = time.perf_counter()
    corpus = (output / "corpus").resolve()
    structural = modules["extract"].extract([_run_path(output, corpus / entry["path"]) for entry in plan["files"]], cache_root=folder, root=corpus, parallel=False)
    save(folder / "structural.json", structural)
    require(not structural.get("failed_sources") and not structural.get("error"), "upstream structural extraction failed required sources; raw failure retained in discovery/structural.json")
    require(set(structural.get("extracted_sources", [])) == {str(corpus / entry["path"]) for entry in plan["files"]}, "upstream structural dispatch did not cover exact corpus")
    fragments = [load(attempt / "answer.json") for attempt in attempts]
    # No sanitize_semantic_fragment: that pinned helper discards valid documented
    # concept/rationale node types. Preserve every raw fragment independently.
    build_fragments = copy.deepcopy(fragments)
    for fragment in build_fragments:
        for entry in fragment["nodes"] + fragment["edges"]:
            entry["ac_generation_origin"] = "semantic"
            entry["_origin"] = "semantic"
    graph = modules["build"].build([structural, *build_fragments], directed=True, dedup=False, root=corpus)
    communities = modules["cluster"].cluster(graph)
    require(modules["export"].to_json(graph, communities, str(folder / "graph.json"), force=True, built_at_commit=UPSTREAM_COMMIT), "upstream exporter refused discovery graph")
    counts = {"structural_nodes": len(structural.get("nodes", [])), "structural_edges": len(structural.get("edges", [])),
              "raw_semantic_nodes": sum(len(fragment["nodes"]) for fragment in fragments),
              "raw_semantic_edges": sum(len(fragment["edges"]) for fragment in fragments),
              "graph_nodes": graph.number_of_nodes(), "graph_edges": graph.number_of_edges(),
              "communities": len(communities)}
    structural_node_files = {node.get("source_file") for node in structural.get("nodes", [])}
    chunk_coverage = []
    for ordinal, chunk in enumerate(chunks):
        entry = {"id": chunk["id"], "source_segments_supplied": [{key: segment[key] for key in ("id", "path", "start_line", "end_line", "sha256")} for segment in chunk["segments"]]}
        if plan["mode"] == "graphify":
            entry.update(attempt=str(attempts[ordinal].relative_to(output)), answer_sha256=sha((attempts[ordinal] / "answer.json").read_bytes()),
                         nodes_by_source_file={str((corpus / path).resolve()): sum(node["source_file"] == str((corpus / path).resolve()) for node in fragments[ordinal]["nodes"])
                                               for path in sorted({segment["path"] for segment in chunk["segments"]})})
        chunk_coverage.append(entry)
    coverage = {"processing": ("all exact source chunks supplied to fresh stock semantic extraction actors" if plan["mode"] == "graphify" else
                               "all exact source files dispatched to deterministic structural extraction; fresh F_P source processing occurs in the later a_c-aware author stage"),
                "discovery_profile": "graphify.structural-and-semantic-discovery/1" if plan["mode"] == "graphify" else "a_c.graphify.structural-discovery/1",
                "semantic_extraction_profile": plan["semantic_extraction_profile"],
                "structural_failed_sources": structural.get("failed_sources", []),
                "structural_source_files_without_nodes": [entry["path"] for entry in plan["files"] if entry["path"] not in structural_node_files and str(corpus / entry["path"]) not in structural_node_files],
                "chunks": chunk_coverage,
                "counts": counts, "semantic_completeness": "unassessed",
                "limitation": "Upstream DiGraph may coalesce parallel edges and repeated IDs; raw fragments retain original declarations. Graph discovery is not normative authority."}
    save(folder / "coverage.json", coverage)
    result = {"profile": "ac.generation.discovery/1", "status": "completed", "mode": plan["mode"], "upstream": plan["upstream"],
              "semantic_extraction_profile": plan["semantic_extraction_profile"],
              "elapsed_seconds": time.perf_counter() - started, "counts": counts,
              "files": {name: sha((folder / name).read_bytes()) for name in ("structural.json", "graph.json", "coverage.json")}}
    save(folder / "result.json", result)
    return result


def _schema(kind: str, **values: Any) -> dict[str, Any]:
    return {"type": kind, **values}


def _array(items: dict[str, Any], minimum: int = 0) -> dict[str, Any]:
    return _schema("array", items=items, min_items=minimum)


def _closed(**fields: Any) -> dict[str, Any]:
    return _schema("object", fields=fields)


def model_from_answers(plan: dict[str, Any], chunks: list[dict[str, Any]],
                       answers: dict[str, dict[str, Any]], provenance: list[dict[str, str]]) -> tuple[dict[str, Any], dict[str, Any]]:
    """Encode ONLY declared F_P choices; the adapter supplies structural packaging."""
    subject = plan["subject_id"]
    prefix = "urn:a-c:generation:" + sha(subject.encode())[:24] + ":"
    def uid(name: str) -> str:
        return prefix + quote(name, safe=":/")
    external_members: dict[str, str] = {}
    def external(name: str, kind: str) -> str:
        identity = uid(name)
        require(identity not in external_members or external_members[identity] == kind, "external identity kind conflict")
        external_members[identity] = kind
        return identity
    def ref(local: tuple[str, ...] = (), remote: tuple[str, ...] = (), governing: bool = False) -> dict[str, Any]:
        return _schema("ref", domain=uid("reference-domain:declared"), local_families=list(local), local_sorts=[],
                       external_kinds=[uid("external-kind:" + kind) for kind in remote], basis_relation=uid("basis-relation:exact"), governing=governing)
    text = _schema("string", min_length=1)
    texts = _array(text)
    identity = _schema("identity")
    basis_id = external("basis", "basis")
    common = {"context": external("context:source-first-proposal", "context"), "owner": external("actor:f-p-author", "actor"),
              "scope": [external("scope:source-corpus", "scope")], "basis": basis_id}
    fields_common = {"id": identity, "context": ref(remote=("context",)), "owner": ref(remote=("actor",)),
                     "scope": _array(ref(remote=("scope",)), 1), "basis": ref(remote=("basis",))}
    concept_ref = ref(("objects",), governing=True)
    concept_refs = _array(concept_ref, 1)
    attachment_ref = ref(("objects", "relations", "constraints", "latitude"), governing=True)
    ground_schema = _closed(section=ref(remote=("source-section",)), path=text, start_line=_schema("integer"),
                            end_line=_schema("integer"), quote=text)
    grounding = _array(ground_schema, 1)
    value_schema = _closed(label=text, definition=text, conditions=texts, exceptions=texts, grounding=grounding)
    predicate_schema = _closed(statement=text, conditions=texts, exceptions=texts, uncertainty=_schema("string"), grounding=grounding)
    qualifier_schema = _closed(kind=text, meaning=text, conditions=texts, exceptions=texts, grounding=grounding)
    stop_ref, authority_ref = ref(remote=("stop",)), ref(remote=("authority",))
    invalid_ref = ref(remote=("invalidation",))
    evidence_ref = ref(("objects",), ("evidence",))
    all_fields: dict[str, Any] = {}
    def fields(family: str, **specific: Any) -> None:
        all_fields[family] = {**fields_common, **specific}
    fields("objects", sort=ref(remote=("sort",)), value=value_schema)
    fields("relations", kind=ref(remote=("relation-kind",)), source=concept_ref, target=concept_ref, qualifiers=qualifier_schema)
    fields("constraints", kind=ref(remote=("constraint-kind",)), applies_to=concept_refs, predicate=predicate_schema,
           judgment_kind=ref(remote=("judgment-kind",)), latitude_ref=_array(ref(("latitude",), governing=True)), refusal=stop_ref)
    # Latitude's fixed core fields are free JSON schema values. Rich structures
    # retain exact grounding and explicit allowed/forbidden choices.
    variation_schema = _closed(statements=texts, grounding=grounding)
    fields("latitude", applies_to=concept_refs, allowed_variation=variation_schema, forbidden_variation=variation_schema, invalidation=invalid_ref)
    residual_uncertainty = _closed(statement=text, grounding=grounding)
    reentry = _array(ref(("traversals",)))
    fields("residuals", subject=attachment_ref, kind=ref(remote=("residual-kind",)), uncertainty=residual_uncertainty,
           consequence=text, re_entry=reentry, invalidation=invalid_ref)
    fields("traversals", domain=ref(remote=("domain",)), codomain=ref(remote=("domain",)), preconditions=_array(ref(("constraints",), governing=True)),
           postconditions=_array(ref(("constraints",), governing=True)), authority=authority_ref, evidence=_array(evidence_ref), provenance=_array(evidence_ref), stop_states=_array(stop_ref, 1))
    fields("transformations", traversal=ref(("traversals",), governing=True), domain_model=ref(remote=("model",)), codomain_model=ref(remote=("model",)), operation_authority=authority_ref,
           preconditions=_array(ref(("constraints",), governing=True)), preservation_relation=ref(remote=("preservation-law",)), preserved=_array(concept_ref), introduced=_array(ref(remote=("future-record",))),
           removed=_array(concept_ref), external_preserved=_array(ref(remote=("external-resolution",))), external_introduced=_array(ref(remote=("external-resolution",))), external_removed=_array(ref(remote=("external-resolution",))),
           external_resolution_witnesses=_array(ref(remote=("witness",))), residuals=_array(ref(("residuals",), governing=True)), evidence=_array(evidence_ref), provenance=_array(evidence_ref), stop_states=_array(stop_ref, 1), invalidation=invalid_ref, re_entry=reentry)
    fields("judgments", kind=ref(remote=("judgment-kind",)), subject=concept_ref, subject_digest=text, evaluator=ref(remote=("actor",)), authority=authority_ref,
           decision=_schema("enum", values=["indeterminate", "refused", "accepted"]), evidence=_array(evidence_ref, 1), provenance=_array(evidence_ref, 1), decided_at=text)
    sort = external("sort:authored-concept", "sort")
    constraint_kind = external("constraint-kind:authored-source-statement", "constraint-kind")
    residual_kind = external("residual-kind:authored-uncertainty", "residual-kind")
    judgment_kind = external("judgment-kind:external-semantic-review", "judgment-kind")
    invalidation = external("invalidation:source-or-interpretation-change", "invalidation")
    stop = external("stop:no-execution-or-acceptance", "stop")
    authority = external("authority:proposal-authoring-only", "authority")
    relation_kinds: dict[str, Any] = {}
    populations: dict[str, list[Any]] = {family: [] for family in FAMILIES}
    inventory, dispositions, section_details = [], [], []
    missing = []
    def coord(name: str, value: Any) -> dict[str, str]:
        return {"id": uid(name), "sha256": digest(value)}
    def record(rid: str, **specific: Any) -> dict[str, Any]:
        return {"id": rid, **common, **specific}
    for chunk in chunks:
        segments = {segment["id"]: segment for segment in chunk["segments"]}
        for section_id, segment in segments.items():
            inventory.append({"id": section_id, "sha256": segment["sha256"]})
            # Section identities are source coordinates; never local statements.
            external_members[section_id] = "source-section"
        if chunk["id"] not in answers:
            missing.append(chunk["id"])
            for section_id in segments:
                dispositions.append({"source": section_id, "decision": "refused", "records": [], "authority": authority,
                                     "basis": basis_id, "reason": "No validated F_P output for exact source chunk; no semantic coverage claimed."})
            continue
        answer = answers[chunk["id"]]
        author_check(answer, chunk)
        authored = [entry for family in ("concepts", "relations", "constraints", "latitude", "residuals") for entry in answer[family]]
        identities = {entry["key"]: uid("record:" + sha((entry["grounding"][0]["section_id"] + "\0" + entry["key"]).encode())[:32]) for entry in authored}
        def grounds(entry: dict[str, Any]) -> list[dict[str, Any]]:
            return [{"section": ground["section_id"], "path": segments[ground["section_id"]]["path"],
                     "start_line": ground["start_line"], "end_line": ground["end_line"], "quote": ground["quote"]} for ground in entry["grounding"]]
        for entry in answer["concepts"]:
            populations["objects"].append(record(identities[entry["key"]], sort=sort, value={"label": entry["label"], "definition": entry["definition"],
                                                    "conditions": entry["conditions"], "exceptions": entry["exceptions"], "grounding": grounds(entry)}))
        for entry in answer["relations"]:
            kind = external("relation-kind:" + ("governing:" if entry["governing"] else "discovery:") + entry["kind"], "relation-kind")
            endpoint = ref(("objects",), governing=entry["governing"])
            relation_kinds[kind] = {"source": endpoint, "target": endpoint, "qualifiers": qualifier_schema}
            populations["relations"].append(record(identities[entry["key"]], kind=kind, source=identities[entry["source_key"]], target=identities[entry["target_key"]],
                qualifiers={"kind": entry["kind"], "meaning": entry["meaning"], "conditions": entry["conditions"], "exceptions": entry["exceptions"], "grounding": grounds(entry)}))
        for entry in answer["constraints"]:
            populations["constraints"].append(record(identities[entry["key"]], kind=constraint_kind, applies_to=[identities[key] for key in entry["applies_to_keys"]],
                predicate={"statement": entry["statement"], "conditions": entry["conditions"], "exceptions": entry["exceptions"], "uncertainty": entry["uncertainty"], "grounding": grounds(entry)},
                judgment_kind=judgment_kind, latitude_ref=[], refusal=stop))
        for entry in answer["latitude"]:
            populations["latitude"].append(record(identities[entry["key"]], applies_to=[identities[key] for key in entry["applies_to_keys"]],
                allowed_variation={"statements": entry["allowed"], "grounding": grounds(entry)}, forbidden_variation={"statements": entry["forbidden"], "grounding": grounds(entry)}, invalidation=invalidation))
        for entry in answer["residuals"]:
            populations["residuals"].append(record(identities[entry["key"]], subject=identities[entry["subject_key"]], kind=residual_kind,
                uncertainty={"statement": entry["uncertainty"], "grounding": grounds(entry)}, consequence=entry["consequence"], re_entry=[], invalidation=invalidation))
        for entry in answer["dispositions"]:
            dispositions.append({"source": entry["section_id"], "decision": entry["decision"], "records": [identities[key] for key in entry["keys"]],
                                 "authority": authority, "basis": basis_id, "reason": entry["reason"]})
        section_details.append({"chunk": chunk["id"], "dispositions": answer["dispositions"], "limitations": answer["limitations"]})
    local = [entry["id"] for family in populations.values() for entry in family]
    require(len(local) == len(set(local)), "source-derived authored identity collision across chunks; preserve outputs and resolve explicitly")
    definition = {"fields": all_fields, "sorts": {sort: {"value": value_schema}}, "relation_kinds": relation_kinds,
                  "constraint_kinds": {constraint_kind: {"applies_to": concept_refs, "predicate": predicate_schema}},
                  "residual_kinds": {residual_kind: {"subject": attachment_ref, "uncertainty": residual_uncertainty, "consequence": text, "re_entry": reentry, "invalidation": invalid_ref}},
                  "judgment_kinds": {judgment_kind: {"subject": concept_ref, "decision": _schema("enum", values=["indeterminate", "refused", "accepted"]), "evidence": _array(evidence_ref, 1)}},
                  "functor_kinds": list(ac_graph.FUNCTORS), "stop_kinds": [stop], "required_families": []}
    signature_id = uid("signature:compact-source-proposal-v1")
    signature = {"id": signature_id, "definition": definition, "sha256": digest({"id": signature_id, "definition": definition})}
    # Every external tuple has an explicit schema contract, even when unused by
    # empty populations. Their coordinates declare meaning, not authenticated authority.
    resolutions = [{"external_identity": eid, "reference_domain": uid("reference-domain:declared"), "external_target_kind": uid("external-kind:" + kind),
                    "resolved_target_identity": eid, "basis_relation": uid("basis-relation:exact"), "resolution_basis": basis_id,
                    "evidence_identity": uid("evidence:explicit-generation-signature")} for eid, kind in sorted(external_members.items())]
    contract = {"profile": "ac.generation.contract/1", "mode": plan["mode"], "calculus": plan["calculus"], "author_schema_sha256": plan["assets"]["author.schema.json"],
                "semantic_extraction_profile": plan["semantic_extraction_profile"],
                "meaning": "F_P-authored source interpretation. Five declared active record families; traversals/transformations/judgments unimplemented and explicitly empty. Source documents and templates are interpreted as documents; prescribed operations are not executed or accepted.",
                "limits": ["Proposal only; no semantic acceptance or full coverage claim.", "Source supplies meaning; graph supplies fallible discovery data.",
                           "References are chunk-local; cross-chunk identity/conservation requires independent review.", "Conditions, exceptions and uncertainty are inert source-linked statements, not executed predicates."]}
    interpretation = {"contract": coord("interpretation-contract", contract), "selection_ledger": {"id": uid("selection-ledger"), "sha256": digest(dispositions)},
                      "interpreter": coord("interpreter:f-p-cli", provenance), "authority": {"id": authority, "sha256": digest("Owner-authorized proposal authoring; no semantic acceptance or operation authority.")},
                      "source_reentry": coord("source-reentry", {"files": plan["files"], "sections": inventory}), "invalidation": {"id": invalidation, "sha256": digest("Any source, signature, interpretation or provenance change invalidates previous evidence.")},
                      "provenance": [coord("provenance:generation-plan", plan), coord("provenance:author-invocations", provenance)], "dispositions": dispositions}
    model = {"profile": ac_graph.MODEL_PROFILE, "id": uid("model:" + digest({"plan": plan, "answers": answers})[:24]),
             "basis": {"id": basis_id, "calculus": plan["calculus"], "subject": {"id": subject, "sha256": digest(plan["files"]), "inventory": inventory}},
             "coordinates": {key: common[key] for key in ("context", "owner", "scope")}, "signature": signature, "interpretation": interpretation,
             "identity_universe": sorted(local + list(external_members)), "external_resolutions": resolutions, "populations": populations,
             "dependency_contract": {"id": uid("dependency-contract:authored-governing-relations"), "required_relation_kinds": sorted(kind for kind in relation_kinds if ":governing:" in kind),
                                     "attachment_families": ["constraints", "latitude", "residuals"]}, "functor_bindings": {}}
    ac_graph.validate(model)
    coverage = {"profile": "ac.generation.coverage/1", "mode": plan["mode"], "processing_complete": not missing,
                "chunks_total": len(chunks), "chunks_authored": len(answers), "chunks_missing": missing,
                "source_sections": len(inventory), "family_counts": {family: len(values) for family, values in populations.items()},
                "section_dispositions": section_details, "interpretation_contract": contract, "semantic_completeness": "unassessed",
                "unresolved_boundaries": [{"chunk": item["chunk"], "author_declared_limitations": item["limitations"]} for item in section_details],
                "semantic_acceptance": "not requested or issued", "unqualified": ["cross-chunk consolidation", "normative interpretation fidelity", "complete calculus conformance", "accepted-result cost"]}
    return model, coverage


def _formal_selection(output: Path, plan: dict[str, Any], selected: dict[str, Any] | None) -> dict[str, Any] | None:
    path = output / "formal-selection.json"
    if selected is not None:
        ac_formal_gate.validate_config(selected)
        _selected_path(selected, output, write=True, directory=True)
        _selected_path(selected, path, absent=True)
    present = path.exists()
    # This fixed inherited startup locator has the same trusted custody as plan.
    raw = path.read_bytes() if present else None
    result = _resolve_selection(plan, _decode(raw) if present else None, present, selected)
    if result is not None:
        _selected_path(result, output, write=True, directory=True)
        _selected_path(result, path, write=not present)
        if present:
            require(_selected_read(result, path) == raw, "formal selection changed during startup")
        else:
            save(path, result, exclusive=True)
    return result


def check_formal_proposal(plan: dict[str, Any], folder: Path, result: dict[str, Any], *,
                          formal_checker: dict[str, Any] | None = None) -> None:
    """One required-gate policy for direct, grounded and repaired producers."""
    formal_checker = _formal_selection(folder.parent, plan, formal_checker)
    if formal_checker is not None:
        gate: dict[str, Any] = {"required": True, "status": "verified", "checker_sha256": digest(formal_checker), "runs": [],
                                "scope": "exact generated model and actual carrier; no semantic acceptance"}
        try:
            for format in ("model", "carrier"):
                raw = _selected_read(formal_checker, folder / (format + ".json"))
                run = ac_formal_gate.verify(formal_checker, raw, format, [], None, None, folder / ("formal-" + format))
                gate["runs"].append(run)
                if run["result"]["status"] != "verified":
                    gate["status"] = run["result"]["status"]
                    gate["reason"] = run["result"].get("reason")
                    break
        except (ac_formal_gate.GateError, OSError) as exc:
            gate["status"] = exc.status if isinstance(exc, ac_formal_gate.GateError) else "incomplete"
            gate["reason"] = str(exc)
        if gate["status"] != "verified":
            result["status"] = "unverified_proposal"
        result["formal_gate"] = gate


def assemble(output: Path, *, allow_partial: bool = False, upstream: Path | None = None,
             formal_checker: dict[str, Any] | None = None) -> dict[str, Any]:
    plan, chunks = checkpoint(output, formal_checker=formal_checker)
    formal_checker = _formal_selection(output, plan, formal_checker)
    if plan["mode"] in GRAPH_MODES:
        verify_discovery(output)
    answers, provenance = {}, []
    for chunk in chunks:
        attempt = successful_attempt(output, "author", chunk)
        if attempt:
            answer = load(attempt / "answer.json")
            author_check(answer, chunk)
            answers[chunk["id"]] = answer
            provenance.append({"chunk": chunk["id"], "attempt": str(attempt.relative_to(output)), "answer_sha256": sha((attempt / "answer.json").read_bytes()),
                               "invocation_sha256": sha((attempt / "invocation.json").read_bytes())})
    require(allow_partial or len(answers) == len(chunks), "missing validated F_P chunks; normal assembly refuses. --allow-partial explicitly marks refused sections")
    model, coverage = model_from_answers(plan, chunks, answers, provenance)
    model_checked = ac_graph.validate(model)
    carrier = ac_graph.materialize(model_checked)
    require(ac_graph.decode(carrier).document == model, "proposal carrier did not preserve authored model")
    folder = _run_path(output, output / ("partial-proposal" if len(answers) < len(chunks) else "proposal"), write=True)
    require(not folder.exists(), "assembled proposal already exists; preserve immutable result")
    folder.mkdir()
    save(folder / "model.json", model)
    save(folder / "carrier.json", carrier.document)
    save(folder / "coverage.json", coverage)
    upstream_trial = None
    if plan["mode"] in GRAPH_MODES:
        modules = upstream_modules(_upstream_path(output, upstream or Path(plan["upstream"]["root"])))
        graph = modules["build"].build_from_json(ac_graph.extraction(carrier), dedup=False)
        communities = modules["cluster"].cluster(graph)
        require(modules["export"].to_json(graph, communities, str(folder / "graph.json"), force=True, built_at_commit=UPSTREAM_COMMIT), "upstream proposal export refused")
        recovered = ac_graph.decode(ac_graph.GraphCarrier(load(folder / "graph.json")))
        require(recovered.document == model, "actual upstream proposal round trip changed model")
        upstream_trial = {"commit": UPSTREAM_COMMIT, "nodes": graph.number_of_nodes(), "edges": graph.number_of_edges(), "decoded_model_sha256": recovered.sha256}
    result = {"profile": "ac.generation.proposal/1", "status": "proposed" if coverage["processing_complete"] else "partial_proposal",
              "mode": plan["mode"], "model_id": model["id"], "model_sha256": model_checked.sha256, "family_counts": coverage["family_counts"],
              "processing_complete": coverage["processing_complete"], "upstream_trial": upstream_trial,
              "files": {path.name: sha(path.read_bytes()) for path in folder.iterdir() if path.is_file()},
              "claim": "Mechanically valid, source-grounded F_P proposal and lossless carrier; interpretation fidelity and semantic acceptance unassessed."}
    check_formal_proposal(plan, folder, result, formal_checker=formal_checker)
    save(folder / "result.json", result)
    return result


def formal_exit(value: Any) -> int:
    if isinstance(value, dict):
        selected = value.get("formal_gate")
        if isinstance(selected, dict) and selected.get("required"):
            return ac_formal_gate.EXITS[selected["status"]]
        return max((formal_exit(child) for child in value.values()), default=0)
    return max((formal_exit(child) for child in value), default=0) if isinstance(value, list) else 0

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("prepare", help="freeze exact raw source, source sections, chunk plan and prompt/schema/code identities")
    p.add_argument("--corpus", type=Path, required=True)
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--mode", choices=("direct", "graphify-ac", "graphify"), default="graphify-ac",
                   help="graphify-ac: preferred one-F_P creation; graphify: stock extraction plus second F_P; direct: source-only control")
    p.add_argument("--upstream", type=Path)
    p.add_argument("--chunk-chars", type=int, default=120_000)
    p.add_argument("--graph-chars", type=int, default=40_000)
    for name in ("extract", "author", "run"):
        p = commands.add_parser(name, help="prepare or execute fresh isolated actors; resume exact completed chunks")
        p.add_argument("--output", type=Path, required=True)
        p.add_argument("--execute", action="store_true")
        p.add_argument("--codex", default="codex")
        p.add_argument("--timeout", type=int, default=1200)
        p.add_argument("--max-chunks", type=int)
        p.add_argument("--jobs", type=int, default=1)
        p.add_argument("--retry-failed", action="store_true")
        p.add_argument("--upstream", type=Path)
        p.add_argument("--model", help="explicit model override; frozen for every executed chunk/stage")
        p.add_argument("--effort", choices=("low", "medium", "high", "xhigh", "max"))
    for name in ("graph", "assemble"):
        p = commands.add_parser(name)
        p.add_argument("--output", type=Path, required=True)
        p.add_argument("--upstream", type=Path)
        if name == "assemble":
            p.add_argument("--allow-partial", action="store_true")
    for name in ("prepare", "assemble", "run"):
        p = commands.choices[name]
        p.add_argument("--formal-checker", type=Path, help="select a REQUIRED pinned checker configuration")
        p.add_argument("--formal-checker-sha256", help="trusted startup digest of the exact checker configuration")
    args = parser.parse_args(argv)
    try:
        formal_checker = None
        if args.command in ("prepare", "assemble", "run"):
            require(bool(args.formal_checker) == bool(args.formal_checker_sha256), "formal checker requires both path and trusted configuration digest")
            if args.formal_checker:
                formal_checker = ac_formal_gate.load_config(args.formal_checker, args.formal_checker_sha256)
        if args.command == "prepare":
            result = prepare(args.corpus, args.manifest, args.output, args.mode, args.upstream, args.chunk_chars, args.graph_chars, formal_checker=formal_checker)
        elif args.command in ("extract", "author"):
            result = stage(args.output, args.command, execute=args.execute, codex=args.codex, timeout=args.timeout, max_chunks=args.max_chunks,
                           jobs=args.jobs, retry_failed=args.retry_failed, upstream=args.upstream, model=args.model, effort=args.effort)
        elif args.command == "graph":
            result = build_discovery(args.output, args.upstream)
        elif args.command == "assemble":
            result = assemble(args.output, allow_partial=args.allow_partial, upstream=args.upstream, formal_checker=formal_checker)
        else:
            plan, _ = checkpoint(args.output, formal_checker=formal_checker)
            formal_checker = _formal_selection(args.output, plan, formal_checker)
            results = []
            if plan["mode"] == "graphify-ac":
                results.append(build_discovery(args.output, args.upstream))
            for name in (["extract", "author"] if plan["mode"] == "graphify" else ["author"]):
                result = stage(args.output, name, execute=args.execute, codex=args.codex, timeout=args.timeout, max_chunks=args.max_chunks,
                               jobs=args.jobs, retry_failed=args.retry_failed, upstream=args.upstream, model=args.model, effort=args.effort)
                results.append(result)
                if result["status"] != "completed":
                    break
                if name == "extract":
                    results.append(build_discovery(args.output, args.upstream))
            if results[-1]["status"] == "completed" and args.execute:
                results.append(assemble(args.output, upstream=args.upstream, formal_checker=formal_checker))
            result = {"stages": results}
            if formal_checker is not None and not any("formal_gate" in item for item in results):
                result["formal_gate"] = {"required": True, "status": "incomplete", "reason": "Generation did not produce an assembled proposal for the required formal gate"}
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        def failed(value: Any) -> bool:
            if isinstance(value, dict):
                return value.get("status") == "failed" or any(failed(child) for child in value.values())
            return isinstance(value, list) and any(failed(child) for child in value)
        if formal_exit(result):
            return formal_exit(result)
        return 1 if failed(result) else 0
    except (GenerationError, ac_graph.Refusal, ac_formal_gate.GateError, OSError, ValueError, subprocess.SubprocessError) as exc:
        print("generation refused: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
