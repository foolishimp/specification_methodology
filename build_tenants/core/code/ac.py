#!/usr/bin/env python3
"""Validate Axiom Indexer programs and join LLM-supplied text sections."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urldefrag, urlparse


TOP_KEYS = {
    "kind",
    "schema_version",
    "uri",
    "calculus_ref",
    "source_basis",
    "frame_refs",
    "vocabulary_refs",
    "symbols",
    "clauses",
    "residuals",
}
SYMBOL_KEYS = {"uri", "kind", "label", "source_refs"}
CLAUSE_KEYS = {
    "uri",
    "clause_type",
    "operator",
    "arguments",
    "statement",
    "source_refs",
}
ARGUMENT_KEYS = {"role", "ref", "literal"}
RESIDUAL_KEYS = {
    "uri",
    "kind",
    "subject_refs",
    "detail",
    "re_entry_refs",
    "source_refs",
}
RESIDUAL_KINDS = {"ambiguity", "conflict", "omission", "unresolved"}
CLAUSE_TYPES = {"relation", "constraint"}
URI_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+$")


class DuplicateKeyError(ValueError):
    pass


def unique_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def sha256(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def is_uri(value: Any) -> bool:
    if not isinstance(value, str) or not URI_RE.fullmatch(value):
        return False
    if re.search(r"%(?![0-9A-Fa-f]{2})", value):
        return False
    parsed = urlparse(value)
    if not parsed.scheme:
        return False
    remainder = value[len(parsed.scheme) + 1 :]
    return not remainder.startswith("//") or bool(parsed.netloc)


def diagnostic(
    issues: list[dict[str, str]],
    code: str,
    record: str,
    field: str,
    ref: str | None = None,
) -> None:
    row = {"code": code, "record": record, "field": field}
    if ref is not None:
        row["ref"] = ref
    issues.append(row)


def heading_slugs(text: str) -> set[str]:
    slugs: set[str] = set()
    occurrences: dict[str, int] = {}
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        base = match.group(1).strip().lower()
        base = re.sub(r"[^\w\- ]", "", base, flags=re.UNICODE)
        base = re.sub(r"[\s\-]+", "-", base).strip("-")
        count = occurrences.get(base, 0)
        occurrences[base] = count + 1
        slugs.add(base if count == 0 else f"{base}-{count}")
    return slugs


class Resolver:
    def __init__(self, binding_path: Path, value: Any):
        if not isinstance(value, dict) or set(value) != {
            "kind",
            "schema_version",
            "bindings",
        }:
            raise ValueError("invalid_binding_set_shape")
        if value["kind"] != "axiom-indexer.binding-set" or value["schema_version"] != 1:
            raise ValueError("unsupported_binding_set")
        rows = value["bindings"]
        if not isinstance(rows, list) or not rows:
            raise ValueError("empty_binding_set")
        seen: set[str] = set()
        self.bindings: list[tuple[str, Path]] = []
        for row in rows:
            if not isinstance(row, dict) or set(row) != {"uri_prefix", "path"}:
                raise ValueError("invalid_binding_shape")
            prefix = row["uri_prefix"]
            physical = row["path"]
            if not is_uri(prefix) or not isinstance(physical, str) or not physical:
                raise ValueError("invalid_binding_coordinate")
            if prefix in seen:
                raise ValueError("duplicate_binding_prefix")
            seen.add(prefix)
            root = Path(physical)
            if not root.is_absolute():
                root = binding_path.parent / root
            self.bindings.append((prefix, root.resolve()))
        self.bindings.sort(key=lambda pair: len(pair[0]), reverse=True)

    def resolve(self, uri: str) -> tuple[Path, str | None]:
        base_uri, fragment = urldefrag(uri)
        matches = [
            (prefix, root)
            for prefix, root in self.bindings
            if base_uri.startswith(prefix)
        ]
        if not matches:
            raise ValueError("unresolved_uri")
        longest = len(matches[0][0])
        matches = [row for row in matches if len(row[0]) == longest]
        if len(matches) != 1:
            raise ValueError("ambiguous_uri")
        prefix, root = matches[0]
        relative = unquote(base_uri[len(prefix) :]).lstrip("/")
        target = (root / relative).resolve()
        try:
            target.relative_to(root)
        except ValueError as exc:
            raise ValueError("binding_escape") from exc
        if not target.exists():
            raise ValueError("missing_resource")
        if fragment:
            if not target.is_file() or target.suffix.lower() not in {
                ".md",
                ".markdown",
            }:
                raise ValueError("unsupported_fragment")
            if fragment not in heading_slugs(target.read_text(encoding="utf-8")):
                raise ValueError("unresolved_fragment")
        return target, fragment or None

    def resolve_file(self, uri: str) -> tuple[Path, str | None]:
        target, fragment = self.resolve(uri)
        if not target.is_file():
            raise ValueError("resource_not_file")
        return target, fragment


def exact_keys(
    value: Any,
    expected: set[str],
    issues: list[dict[str, str]],
    record: str,
    field: str,
) -> bool:
    if not isinstance(value, dict):
        diagnostic(issues, "wrong_shape", record, field)
        return False
    missing = sorted(expected - set(value))
    extra = sorted(set(value) - expected)
    for key in missing:
        diagnostic(issues, "missing_field", record, f"{field}.{key}")
    for key in extra:
        diagnostic(issues, "unknown_field", record, f"{field}.{key}")
    return not missing and not extra


def uri_list(
    value: Any,
    issues: list[dict[str, str]],
    record: str,
    field: str,
    *,
    nonempty: bool = False,
) -> list[str]:
    if not isinstance(value, list):
        diagnostic(issues, "wrong_shape", record, field)
        return []
    if nonempty and not value:
        diagnostic(issues, "empty_set", record, field)
    valid: list[str] = []
    for ref in value:
        if not is_uri(ref):
            diagnostic(issues, "invalid_uri", record, field, str(ref))
        else:
            valid.append(ref)
    if len(valid) != len(set(valid)):
        diagnostic(issues, "duplicate_ref", record, field)
    if valid != sorted(valid):
        diagnostic(issues, "noncanonical_order", record, field)
    return valid


def validate_program(program: Any, resolver: Resolver) -> dict[str, Any]:
    issues: list[dict[str, str]] = []
    root = (
        program.get("uri", "urn:axiom-indexer:diagnostic:program")
        if isinstance(program, dict)
        else "urn:axiom-indexer:diagnostic:program"
    )
    if not exact_keys(program, TOP_KEYS, issues, root, "$program"):
        return report(program, issues, {})
    if program["kind"] != "axiom-indexer.axiomatic-program":
        diagnostic(issues, "wrong_kind", root, "kind")
    if program["schema_version"] != 1:
        diagnostic(issues, "wrong_schema_version", root, "schema_version")
    if not is_uri(program["uri"]):
        diagnostic(issues, "invalid_uri", root, "uri", str(program["uri"]))
    resolved_sources: dict[str, str] = {}
    if not is_uri(program["calculus_ref"]):
        diagnostic(
            issues,
            "invalid_uri",
            root,
            "calculus_ref",
            str(program["calculus_ref"]),
        )
    else:
        try:
            path, _ = resolver.resolve_file(program["calculus_ref"])
            resolved_sources[program["calculus_ref"]] = sha256(path.read_bytes())
        except ValueError as exc:
            diagnostic(issues, str(exc), root, "calculus_ref", program["calculus_ref"])
    if not is_uri(program["source_basis"]):
        diagnostic(
            issues, "invalid_uri", root, "source_basis", str(program["source_basis"])
        )
    else:
        try:
            resolver.resolve(program["source_basis"])
        except ValueError as exc:
            diagnostic(issues, str(exc), root, "source_basis", program["source_basis"])

    frames = uri_list(program["frame_refs"], issues, root, "frame_refs")
    vocabulary = uri_list(program["vocabulary_refs"], issues, root, "vocabulary_refs")
    for frame in frames:
        try:
            path, _ = resolver.resolve_file(frame)
            resolved_sources[frame] = sha256(path.read_bytes())
        except ValueError as exc:
            diagnostic(issues, str(exc), root, "frame_refs", frame)

    item_lists = {
        "symbols": program["symbols"],
        "clauses": program["clauses"],
        "residuals": program["residuals"],
    }
    items: dict[str, dict[str, Any]] = {}
    for field, rows in item_lists.items():
        if not isinstance(rows, list):
            diagnostic(issues, "wrong_shape", root, field)
            item_lists[field] = []
            continue
        uris = [
            row.get("uri")
            for row in rows
            if isinstance(row, dict) and is_uri(row.get("uri"))
        ]
        if uris != sorted(uris):
            diagnostic(issues, "noncanonical_order", root, field)
        for row in rows:
            if not isinstance(row, dict) or not is_uri(row.get("uri")):
                diagnostic(issues, "invalid_item_uri", root, field)
                continue
            uri = row["uri"]
            if uri in items:
                diagnostic(issues, "duplicate_identity", uri, "uri", uri)
            else:
                items[uri] = row

    def source_refs(row: dict[str, Any], record: str) -> None:
        refs = uri_list(
            row.get("source_refs"), issues, record, "source_refs", nonempty=True
        )
        for ref in refs:
            if is_uri(program["source_basis"]) and not ref.startswith(
                program["source_basis"]
            ):
                diagnostic(issues, "source_outside_basis", record, "source_refs", ref)
                continue
            try:
                path, _ = resolver.resolve_file(ref)
                resolved_sources[ref] = sha256(path.read_bytes())
            except ValueError as exc:
                diagnostic(issues, str(exc), record, "source_refs", ref)

    for row in item_lists["symbols"]:
        if not isinstance(row, dict):
            continue
        record = row.get("uri", root)
        if not exact_keys(row, SYMBOL_KEYS, issues, record, "symbol"):
            continue
        if not is_uri(row["uri"]):
            diagnostic(issues, "invalid_uri", record, "uri", str(row["uri"]))
        if row["kind"] not in vocabulary:
            diagnostic(
                issues, "undeclared_vocabulary", record, "kind", str(row["kind"])
            )
        if not isinstance(row["label"], str) or not row["label"].strip():
            diagnostic(issues, "empty_label", record, "label")
        source_refs(row, record)

    local_ids = set(items)
    external_ids = set(frames) | set(vocabulary)
    for row in item_lists["clauses"]:
        if not isinstance(row, dict):
            continue
        record = row.get("uri", root)
        if not exact_keys(row, CLAUSE_KEYS, issues, record, "clause"):
            continue
        if row["clause_type"] not in CLAUSE_TYPES:
            diagnostic(issues, "invalid_clause_type", record, "clause_type")
        if row["operator"] not in vocabulary:
            diagnostic(
                issues,
                "undeclared_vocabulary",
                record,
                "operator",
                str(row["operator"]),
            )
        if not isinstance(row["statement"], str) or not row["statement"].strip():
            diagnostic(issues, "empty_statement", record, "statement")
        arguments = row["arguments"]
        if not isinstance(arguments, list) or not arguments:
            diagnostic(issues, "empty_arguments", record, "arguments")
        else:
            for argument in arguments:
                if not isinstance(argument, dict):
                    diagnostic(issues, "wrong_shape", record, "arguments")
                    continue
                for key in sorted(set(argument) - ARGUMENT_KEYS):
                    diagnostic(issues, "unknown_field", record, f"arguments.{key}")
                if "role" not in argument:
                    diagnostic(issues, "missing_field", record, "arguments.role")
                    continue
                role = argument.get("role")
                if role not in vocabulary:
                    diagnostic(
                        issues,
                        "undeclared_vocabulary",
                        record,
                        "arguments.role",
                        str(role),
                    )
                has_ref = "ref" in argument
                has_literal = "literal" in argument
                if has_ref == has_literal:
                    diagnostic(issues, "invalid_argument_value", record, "arguments")
                elif has_ref:
                    ref = argument["ref"]
                    if not is_uri(ref):
                        diagnostic(
                            issues, "invalid_uri", record, "arguments.ref", str(ref)
                        )
                    elif ref not in local_ids and ref not in external_ids:
                        diagnostic(issues, "dangling_ref", record, "arguments.ref", ref)
                elif (
                    not isinstance(argument["literal"], (str, int, float, bool))
                    and argument["literal"] is not None
                ):
                    diagnostic(
                        issues, "invalid_argument_value", record, "arguments.literal"
                    )
        source_refs(row, record)

    for row in item_lists["residuals"]:
        if not isinstance(row, dict):
            continue
        record = row.get("uri", root)
        if not exact_keys(row, RESIDUAL_KEYS, issues, record, "residual"):
            continue
        if row["kind"] not in RESIDUAL_KINDS:
            diagnostic(issues, "invalid_residual_kind", record, "kind")
        if not isinstance(row["detail"], str) or not row["detail"].strip():
            diagnostic(issues, "empty_detail", record, "detail")
        for ref in uri_list(row["subject_refs"], issues, record, "subject_refs"):
            if ref not in local_ids:
                diagnostic(issues, "dangling_ref", record, "subject_refs", ref)
        for ref in uri_list(
            row["re_entry_refs"], issues, record, "re_entry_refs", nonempty=True
        ):
            if ref in frames:
                continue
            try:
                resolver.resolve_file(ref)
            except ValueError as exc:
                diagnostic(issues, str(exc), record, "re_entry_refs", ref)
        source_refs(row, record)

    return report(program, issues, resolved_sources)


def report(
    program: Any, issues: list[dict[str, str]], resolved_sources: dict[str, str]
) -> dict[str, Any]:
    issues.sort(
        key=lambda row: tuple(
            row.get(key, "") for key in ("record", "field", "code", "ref")
        )
    )
    safe_program = program if isinstance(program, dict) else {}
    try:
        digest = sha256(canonical_bytes(program))
    except (TypeError, ValueError, UnicodeEncodeError):
        digest = "unavailable"
        diagnostic(
            issues,
            "noncanonical_value",
            safe_program.get("uri", "urn:axiom-indexer:diagnostic:program"),
            "$program",
        )
        issues.sort(
            key=lambda row: tuple(
                row.get(key, "") for key in ("record", "field", "code", "ref")
            )
        )
    return {
        "kind": "axiom-indexer.validation-report",
        "schema_version": 1,
        "status": "valid" if not issues else "invalid",
        "program_uri": safe_program.get("uri"),
        "program_sha256": digest,
        "resolved_sources": [
            {"uri": uri, "sha256": resolved_sources[uri]}
            for uri in sorted(resolved_sources)
        ],
        "derived_counts": {
            key: len(safe_program.get(key, []))
            if isinstance(safe_program.get(key), list)
            else 0
            for key in ("symbols", "clauses", "residuals")
        },
        "diagnostics": issues,
    }


def instantiate(program: dict[str, Any], validation: dict[str, Any]) -> dict[str, Any]:
    outgoing: dict[str, list[str]] = {
        row["uri"]: []
        for family in ("symbols", "clauses", "residuals")
        for row in program[family]
    }
    for clause in program["clauses"]:
        for argument in clause["arguments"]:
            ref = argument.get("ref")
            if ref in outgoing:
                outgoing[ref].append(clause["uri"])
    for refs in outgoing.values():
        refs.sort()
    result = {
        "kind": "axiom-indexer.logical-constraint-map",
        "schema_version": 1,
        "program_uri": program["uri"],
        "program_sha256": validation["program_sha256"],
        "calculus_ref": program["calculus_ref"],
        "source_basis": program["source_basis"],
        "frame_refs": program["frame_refs"],
        "vocabulary_refs": program["vocabulary_refs"],
        "resolved_sources": validation["resolved_sources"],
        "symbols": {
            row["uri"]: {"kind": row["kind"], "label": row["label"]}
            for row in program["symbols"]
        },
        "clauses": program["clauses"],
        "constraints": [
            row["uri"]
            for row in program["clauses"]
            if row["clause_type"] == "constraint"
        ],
        "outgoing_clause_refs": outgoing,
        "residuals": program["residuals"],
        "source_routes": {
            row["uri"]: row["source_refs"]
            for family in ("symbols", "clauses", "residuals")
            for row in program[family]
        },
    }
    result["map_sha256"] = sha256(canonical_bytes(result))
    return result


def join_sections(sections: Any) -> str:
    if not isinstance(sections, list):
        raise ValueError("invalid_sections")
    parts: list[str] = []
    for section in sections:
        if not isinstance(section, dict) or set(section) != {"label", "text"}:
            raise ValueError("invalid_section")
        label = section["label"]
        text = section["text"]
        if not isinstance(label, str) or not isinstance(text, str):
            raise ValueError("invalid_section")
        parts.append(label + "\n" + text)
    result = "\n\n".join(parts)
    try:
        result.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("invalid_section_encoding") from exc
    return result


def write_json(path: Path | None, value: Any) -> None:
    data = canonical_bytes(value) + b"\n"
    if path is None:
        sys.stdout.buffer.write(data)
    else:
        path.write_bytes(data)


def write_text(path: Path | None, value: str) -> None:
    data = value.encode("utf-8")
    if path is None:
        sys.stdout.buffer.write(data)
    else:
        path.write_bytes(data)


def input_failure(ref: str) -> dict[str, Any]:
    return {
        "kind": "axiom-indexer.validation-report",
        "schema_version": 1,
        "status": "invalid",
        "program_uri": None,
        "program_sha256": "unavailable",
        "resolved_sources": [],
        "derived_counts": {"symbols": 0, "clauses": 0, "residuals": 0},
        "diagnostics": [
            {
                "code": "input_error",
                "record": "urn:axiom-indexer:diagnostic:input",
                "field": "input",
                "ref": ref,
            }
        ],
    }


def clear_stale_map(path: Path | None) -> None:
    if path is not None and (path.is_file() or path.is_symlink()):
        path.unlink()


def path_alias(left: Path, right: Path) -> bool:
    if left.resolve() == right.resolve():
        return True
    try:
        return left.exists() and right.exists() and left.samefile(right)
    except OSError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--program", type=Path, required=True)
    validate_parser.add_argument("--bindings", type=Path, required=True)
    validate_parser.add_argument("--output", type=Path)
    validate_parser.add_argument("--emit-map", type=Path)
    join_parser = subparsers.add_parser("join")
    join_parser.add_argument("--input", type=Path, required=True)
    join_parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.command == "join":
        if args.output is not None and path_alias(args.input, args.output):
            print("join_error:input_output_path_alias", file=sys.stderr)
            return 2
        try:
            sections = load_json(args.input)
            joined = join_sections(sections)
        except (
            OSError,
            UnicodeDecodeError,
            json.JSONDecodeError,
            DuplicateKeyError,
            ValueError,
        ) as exc:
            print(f"join_error:{exc}", file=sys.stderr)
            return 2
        write_text(args.output, joined)
        return 0

    inputs = [args.program, args.bindings]
    outputs = [path for path in (args.output, args.emit_map) if path]
    input_alias = any(
        path_alias(output, source) for output in outputs for source in inputs
    )
    output_alias = len(outputs) == 2 and path_alias(outputs[0], outputs[1])
    if input_alias or output_alias:
        if args.emit_map is not None and not any(
            path_alias(args.emit_map, source) for source in inputs
        ):
            clear_stale_map(args.emit_map)
        write_json(None, input_failure("input_output_path_alias"))
        return 2
    try:
        program = load_json(args.program)
        binding_value = load_json(args.bindings)
        resolver = Resolver(args.bindings, binding_value)
        validation = validate_program(program, resolver)
    except (OSError, json.JSONDecodeError, DuplicateKeyError, ValueError) as exc:
        failure = input_failure(str(exc))
        write_json(args.output, failure)
        clear_stale_map(args.emit_map)
        return 2
    write_json(args.output, validation)
    if validation["status"] == "valid" and args.emit_map is not None:
        write_json(args.emit_map, instantiate(program, validation))
    elif validation["status"] == "invalid":
        clear_stale_map(args.emit_map)
    return 0 if validation["status"] == "valid" else 1


if __name__ == "__main__":
    raise SystemExit(main())
