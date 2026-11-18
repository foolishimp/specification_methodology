#!/usr/bin/env python3
"""Prepare, inspect and check purpose-built context using selected source files."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any

# Resolve the physical bundle for copied installs and either host's symlink entry.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import context_core as core
import context_catalog as reusable


def write_new(path: Path, value: Any) -> None:
    with path.open("xb") as handle:
        handle.write(value if isinstance(value, bytes) else core.canonical(value) + b"\n")


def prepare(sources_path: Path, purpose_path: Path, output: Path) -> dict[str, Any]:
    request = core.read_json(sources_path)
    core._object(request, {"subject_id", "method", "files"}, "source selection")
    core.need(isinstance(request["files"], list) and bool(request["files"]), "selected source files required")
    files = []
    for row in request["files"]:
        core._object(row, {"id", "path"}, "selected source")
        core._text(row["path"], "selected source path")
        path = Path(row["path"])
        if not path.is_absolute():
            path = sources_path.absolute().parent / path
        core.need(path.is_file() and not path.is_symlink() and all(not parent.is_symlink() for parent in path.parents),
                  "selected source must be a regular file without symlink ancestors")
        path = path.resolve()
        files.append({"id": row["id"], "path": str(path), "sha256": core.raw_digest(path.read_bytes())})
    manifest = {"profile": core.CORPUS_PROFILE, "subject_id": request["subject_id"], "method": request["method"], "files": files}
    purpose = core.read_json(purpose_path)
    return prepare_manifest(manifest, purpose, output)


def prepare_manifest(manifest: dict[str, Any], purpose: dict[str, Any], output: Path) -> dict[str, Any]:
    """One preparation path for explicit new sources and catalog-bound source members."""
    view = core.corpus_view(manifest)
    core.validate_purpose(purpose)
    binding = {"profile": "stdo.context-bundle/1", "manifest_sha256": core.digest(manifest),
               "purpose_sha256": core.digest(purpose), "corpus_sha256": view["corpus_sha256"], "view_sha256": view["view_sha256"]}
    prompt = core.build_prompt(view, purpose,
        "Use the active stdo-context skill's scripts/context.py catalog, search and read commands with this bundle. "
        "The current session authors INDEX.json. Validate that actual file with the same helper; no model is invoked by the helper.")
    template = {"profile": core.INDEX_PROFILE, "purpose_id": purpose["id"], "purpose_sha256": binding["purpose_sha256"],
                "corpus_sha256": binding["corpus_sha256"], "input_view_sha256": binding["view_sha256"], "rules": [],
                "source_coverage": [{"source_id": row["id"], "status": "unresolved", "rule_ids": [],
                                     "reason": "Selected source interpretation has not been completed."} for row in manifest["files"]],
                "unresolved": []}
    core.need(not output.exists(), "output directory already exists; preserve the prior attempt")
    output.mkdir(parents=True, exist_ok=False)
    for name, value in (("MANIFEST.json", manifest), ("PURPOSE.json", purpose), ("BUNDLE.json", binding),
                        ("AUTHORING.md", prompt.encode()), ("INDEX-TEMPLATE.json", template)):
        write_new(output / name, value)
    return {"status": "prepared", "bundle": str(output.resolve()), **binding,
            "source_members": len(manifest["files"]), "index": "not authored", "semantic_coverage": "unassessed"}


def load_bundle(path: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    manifest, purpose, binding = (core.read_json(path / name) for name in ("MANIFEST.json", "PURPOSE.json", "BUNDLE.json"))
    core.validate_purpose(purpose)
    view = core.corpus_view(manifest)
    expected = {"profile": "stdo.context-bundle/1", "manifest_sha256": core.digest(manifest),
                "purpose_sha256": core.digest(purpose), "corpus_sha256": view["corpus_sha256"], "view_sha256": view["view_sha256"]}
    core.need(binding == expected, "bundle identity differs; re-enter exact source/purpose selection")
    return manifest, purpose, view


def page(items: list[dict[str, Any]], offset: int, limit: int) -> dict[str, Any]:
    core.need(type(offset) is int and 0 <= offset <= len(items), "page offset outside results")
    core.need(type(limit) is int and limit > 0, "page limit must be positive")
    end = min(len(items), offset + limit)
    return {"items": items[offset:end], "offset": offset, "next_offset": end if end < len(items) else None,
            "total_items": len(items)}


def catalog(view: dict[str, Any], offset: int, limit: int) -> dict[str, Any]:
    return page([{**source, "characters": len(doc["content"]), "body_sha256": core.raw_digest(doc["content"].encode())}
                 for source, doc in zip(view["source_catalog"], view["documents"])], offset, limit)


def search(view: dict[str, Any], text: str, offset: int, limit: int) -> dict[str, Any]:
    core._text(text, "literal search text")
    hits = []
    for doc in view["documents"]:
        body = doc["content"]
        for match in re.finditer(re.escape(text), body, re.IGNORECASE):
            start, end = max(0, match.start() - 120), min(len(body), match.end() + 240)
            hits.append({"source_id": doc["id"], "match_start_char": match.start(), "match_end_char": match.end(),
                         "source_line": body.count("\n", 0, match.start()) + 1,
                         "start_char": start, "end_char": end, "content": body[start:end]})
    return {"match": "literal, case-insensitive; read surrounding clauses and exceptions", **page(hits, offset, limit)}


def read_source(view: dict[str, Any], source_id: str, start: int, count: int) -> dict[str, Any]:
    matches = [doc for doc in view["documents"] if doc["id"] == source_id]
    core.need(len(matches) == 1, "source is outside the selected corpus")
    body = matches[0]["content"]
    core.need(type(start) is int and 0 <= start <= len(body), "source offset outside body")
    core.need(type(count) is int and count > 0, "read character count must be positive")
    end = min(len(body), start + count)
    return {"source_id": source_id, "body_sha256": core.raw_digest(body.encode()), "characters": len(body),
            "start_char": start, "end_char": end, "next_char": end if end < len(body) else None, "content": body[start:end]}


def execute(args: argparse.Namespace) -> dict[str, Any]:
    if args.operation == "prepare":
        return prepare(args.sources, args.purpose, args.out)
    if args.operation in {"indexes", "bind", "select", "consume"}:
        access = reusable.public_bundle(args.public_manifest_sha256)
        if args.operation == "indexes":
            return {"status": "catalog_verified", "public_manifest_sha256": access["public_manifest_sha256"],
                    "catalog_sha256": access["catalog_sha256"],
                    "entries": [reusable.summary(access, item) for item in access["entries"]]}
        if args.operation == "bind":
            item = reusable.find_entry(access, args.index_id)
            method = {"uri": args.method_uri, "manifest_sha256": args.method_manifest_sha256}
            manifest = reusable.source_binding(item, args.source_root, method)
            prepared = prepare_manifest(manifest, item["purpose"], args.out)
            receipt = reusable.binding_receipt(access, item, args.source_root)
            write_new(args.out / "REUSE-BINDING.json", receipt)
            return {**prepared, **reusable.summary(access, item), "status": "bound", "index": "existing authored index",
                    "matches": {"public_manifest": True, "catalog": True, "actual_method_manifest": True,
                                "ordered_source_members": True, "purpose": True}, "binding": receipt}
    manifest, purpose, view = load_bundle(args.bundle)
    if args.operation in {"select", "consume"}:
        query = core.read_json(args.query)
        selection, item = reusable.select(access, args.bundle, manifest, purpose, view, query, args.index_id)
        if args.operation == "select" or selection["status"] != "selected":
            return selection
        assessment = core.read_json(args.assessment) if args.assessment else None
        core.need(args.byte_budget >= 0, "context byte budget must be nonnegative")
        context = core.compile_context(item["index"], query, manifest, purpose, assessment,
                                       trial_binding=args.trial_binding, byte_budget=args.byte_budget)
        built = deliver(context, args.out, args.byte_budget)
        write_new(args.out / "SELECTION.json", selection)
        return {**built, "selection": selection}
    if args.operation == "catalog":
        return catalog(view, args.offset, args.limit)
    if args.operation == "search":
        return search(view, args.text, args.offset, args.limit)
    if args.operation == "read":
        return read_source(view, args.source, args.start_char, args.max_chars)
    index = core.read_json(args.index)
    validated = core.validate_index(index, manifest, purpose, view)
    if args.operation == "validate":
        return validated
    query = core.read_json(args.query)
    assessment = core.read_json(args.assessment) if args.assessment else None
    core.need(args.byte_budget >= 0, "context byte budget must be nonnegative")
    if args.operation == "build":
        context = core.compile_context(index, query, manifest, purpose, assessment,
                                       trial_binding=args.trial_binding, byte_budget=args.byte_budget)
        return deliver(context, args.out, args.byte_budget)
    core.need(args.context.stat().st_size <= args.byte_budget, "received context exceeds selected byte budget")
    actual = core.read_json(args.context)
    core.need(args.markdown.read_bytes() == actual["markdown"].encode(), "actual Markdown differs from supplied context")
    result = core.check_context(actual, index, query, manifest, purpose, assessment, trial_binding=args.trial_binding)
    return {**result, "context_bytes": args.context.stat().st_size, "byte_budget": args.byte_budget,
            "context_file_sha256": core.raw_digest(args.context.read_bytes()),
            "markdown_file_sha256": core.raw_digest(args.markdown.read_bytes())}


def deliver(context: dict[str, Any], output: Path, byte_budget: int) -> dict[str, Any]:
    core.need(not output.exists(), "output directory already exists; preserve the prior context")
    output.mkdir(parents=True, exist_ok=False)
    write_new(output / "CONTEXT.json", context)
    write_new(output / "CONTEXT.md", context["markdown"].encode())
    return {"status": "constructed", "context": str((output / "CONTEXT.json").resolve()),
            "markdown": str((output / "CONTEXT.md").resolve()),
            "context_bytes": len(core.canonical(context) + b"\n"), "byte_budget": byte_budget,
            "payload_sha256": context["payload_sha256"], "markdown_sha256": context["markdown_sha256"],
            "selection_status": context["payload"]["selection_status"], "use": context["payload"]["use"],
            "covered": context["payload"]["covered"], "semantic_coverage": context["payload"]["semantic_coverage"]["status"]}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    commands = result.add_subparsers(dest="operation", required=True)
    prepare_parser = commands.add_parser("prepare", help="pin an explicit source selection and purpose; no index authoring")
    for name in ("sources", "purpose", "out"):
        prepare_parser.add_argument("--" + name, type=Path, required=True)
    for name in ("indexes", "bind", "select", "consume"):
        command = commands.add_parser(name)
        command.add_argument("--public-manifest-sha256", required=True)
        if name != "indexes":
            command.add_argument("--index-id", required=name in {"bind", "consume"})
        if name == "bind":
            command.add_argument("--source-root", type=Path, required=True,
                                 help="actual installed method root containing manifest.json and standards/; not the standards directory")
            command.add_argument("--method-uri", required=True)
            command.add_argument("--method-manifest-sha256", required=True)
            command.add_argument("--out", type=Path, required=True)
        if name in {"select", "consume"}:
            command.add_argument("--bundle", type=Path, required=True)
            command.add_argument("--query", type=Path, required=True)
        if name == "consume":
            command.add_argument("--assessment", type=Path)
            command.add_argument("--trial-binding")
            command.add_argument("--byte-budget", type=int, required=True)
            command.add_argument("--out", type=Path, required=True)
    for name in ("catalog", "search", "read", "validate", "build", "check"):
        command = commands.add_parser(name)
        command.add_argument("--bundle", type=Path, required=True)
        if name in ("catalog", "search"):
            command.add_argument("--offset", type=int, default=0)
            command.add_argument("--limit", type=int, default=12)
        if name == "search":
            command.add_argument("--text", required=True)
        if name == "read":
            command.add_argument("--source", required=True)
            command.add_argument("--start-char", type=int, default=0)
            command.add_argument("--max-chars", type=int, default=4096)
        if name in ("validate", "build", "check"):
            command.add_argument("--index", type=Path, required=True)
        if name in ("build", "check"):
            command.add_argument("--query", type=Path, required=True)
            command.add_argument("--assessment", type=Path)
            command.add_argument("--trial-binding")
            command.add_argument("--byte-budget", type=int, required=True)
        if name == "build":
            command.add_argument("--out", type=Path, required=True)
        if name == "check":
            command.add_argument("--context", type=Path, required=True)
            command.add_argument("--markdown", type=Path, required=True)
    # This limits a whole stdout response, not an authored context artifact.
    for command in commands.choices.values():
        command.add_argument("--response-bytes", type=int, default=16384)
    return result


def main() -> int:
    args = parser().parse_args()
    try:
        core.need(args.response_bytes >= 1024, "response byte budget must be at least 1024")
        result = execute(args)
        wire = core.canonical(result) + b"\n"
        core.need(len(wire) <= args.response_bytes, "response budget insufficient; request a smaller page or explicitly larger response; no truncation")
        sys.stdout.buffer.write(wire)
        return 3 if result.get("status") == "incomplete" else 2 if result.get("status") == "refused" else 0
    except (core.Refusal, OSError, ValueError, TypeError, KeyError) as exc:
        sys.stderr.write(json.dumps({"status": "refused", "reason": str(exc)}, ensure_ascii=False) + "\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
