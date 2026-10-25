"""Bounded, read-only resolution of explicitly declared Product composition.

Resolution is a byte/identity/fragment observation, never an authority grant or
an assessment of the relation's meaning. No network resource is acquired.
"""

from __future__ import annotations

from bisect import bisect_left
from collections import deque
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import stat
from typing import Any, Iterable
from urllib.parse import unquote, urlsplit, urlunsplit

from .errors import StdoError
from .product_definition import definition_status, discover_definitions, load_binding
from .references import heading_slugs
from .store import Store
from .util import sha256_bytes


class ResolutionError(StdoError):
    def __init__(self, code: str, message: str, *, unsupported: bool = False):
        super().__init__(message)
        self.code = code
        self.unsupported = unsupported


def _physical_root(path: Path) -> Path:
    candidate = path.absolute()
    for part in [*reversed(candidate.parents), candidate]:
        if part.is_symlink():
            raise StdoError(f"Composition resolver root traverses a symlink: {part}")
    if not candidate.is_dir():
        raise StdoError(f"Composition resolver root is not a directory: {candidate}")
    return candidate.resolve()


class _Anchors(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.values: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if value is not None and (key == "id" or (tag == "a" and key == "name")):
                self.values.add(value)


def _markdown_text(text: str) -> str:
    """Remove comments and fenced/indented examples before identifying anchors."""
    lines: list[str] = []
    fence: str | None = None
    paragraph = False
    for line in re.sub(r"<!--.*?-->", "", text, flags=re.S).splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence is not None:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
                lines.append("")
            continue
        if match:
            fence = match[1]
            lines.append("")
            paragraph = False
        elif not line.strip():
            lines.append("")
            paragraph = False
        elif line.startswith(("    ", "\t")) and not paragraph:
            lines.append("")
        else:
            # Indentation cannot start a code block inside an open paragraph;
            # it may contain the continuation or delimiter of an inline span.
            line = re.sub(r"^ {1,3}(?=#)", "", line)
            lines.append(line)
            paragraph = not bool(re.match(r"^#{1,6}(?:[ \t]+|$)", line))
    return "\n".join(lines)


_MARKDOWN_HTML_TAG = (
    r'</[A-Za-z][A-Za-z0-9-]*\s*>'
    r'|<[A-Za-z][A-Za-z0-9-]*'
    r'''(?:\s+[A-Za-z_:][A-Za-z0-9_.:-]*(?:\s*=\s*(?:[^\s"'=<>`]+|'[^']*'|"[^"]*"))?)*'''
    r'\s*/?>'
)
_MARKDOWN_INLINE_TOKEN = re.compile(
    r"\\[!\"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~]|`+|" + _MARKDOWN_HTML_TAG
)


def _markdown_html(text: str) -> str:
    """Select raw HTML tags outside Markdown escapes and inline code.

    A code span closes only at a maximal backtick run of the same width,
    including across line endings. Escapes apply outside spans; raw HTML tags
    are consumed atomically, so backticks in their attributes are not Markdown
    delimiters. This is the supported fragment scanner, not a Markdown renderer.
    """
    tags: list[str] = []
    # Inline code cannot cross a paragraph boundary or an ATX block boundary.
    for block in re.split(r"(\n[ \t]*\n|(?m:^[ ]{0,3}#{1,6}[^\S\n]+.*$))", text):
        runs: dict[int, list[int]] = {}
        for run in re.finditer(r"`+", block):
            runs.setdefault(len(run[0]), []).append(run.start())
        cursor = 0
        while token := _MARKDOWN_INLINE_TOKEN.search(block, cursor):
            value = token[0]
            cursor = token.end()
            if value.startswith("\\"):
                continue
            if value.startswith("`"):
                width = len(value)
                starts = runs.get(width, [])
                next_run = bisect_left(starts, cursor)
                if next_run < len(starts):
                    cursor = starts[next_run] + width
                continue
            tags.append(value)
    return "\n".join(tags)


def _check_fragment(path: Path, raw: bytes, fragment: str) -> str:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ResolutionError("unsupported_fragment", f"Fragment requires UTF-8 text: {path}", unsupported=True) from exc
    suffix = path.suffix.lower()
    if suffix in {".md", ".markdown", ".html", ".htm"}:
        visible = _markdown_text(text) if suffix in {".md", ".markdown"} else text
        anchors = _Anchors()
        anchors.feed(_markdown_html(visible) if suffix in {".md", ".markdown"} else visible)
        values = anchors.values
        if suffix in {".md", ".markdown"}:
            values = values | heading_slugs(visible)
        if fragment not in values:
            raise ResolutionError("missing_fragment", f"Fragment does not resolve: {path}#{fragment}")
        return "markdown" if suffix in {".md", ".markdown"} else "html"
    if suffix == ".json" and fragment.startswith("/"):
        try:
            value: Any = json.loads(text)
            for token in fragment[1:].split("/"):
                if re.search(r"~(?![01])", token):
                    raise ValueError("invalid JSON Pointer escape")
                token = token.replace("~1", "/").replace("~0", "~")
                if isinstance(value, list):
                    if not re.fullmatch(r"0|[1-9][0-9]*", token):
                        raise ValueError("invalid JSON Pointer array index")
                    value = value[int(token)]
                elif isinstance(value, dict):
                    value = value[token]
                else:
                    raise ValueError("JSON Pointer traverses a scalar")
        except (ValueError, KeyError, IndexError) as exc:
            raise ResolutionError("missing_fragment", f"JSON Pointer does not resolve: {path}#{fragment}: {exc}") from exc
        return "json-pointer"
    raise ResolutionError("unsupported_fragment", f"Unsupported fragment form: {path}#{fragment}", unsupported=True)


class _Resolver:
    def __init__(self, root: Path, store: Store, max_file_bytes: int):
        self.root = root
        self.store = store
        self.max_file_bytes = max_file_bytes
        self.acquired: dict[Path, str] = {}
        self.boundaries: dict[Path, Path] = {}

    def local_path(self, candidate: Path, *, boundary: Path | None = None) -> Path:
        root = self.root if boundary is None else boundary
        if root.is_symlink() or not root.is_dir():
            raise ResolutionError("symlink_reference", f"Resolver boundary is no longer a physical directory: {root}")
        try:
            parts = candidate.relative_to(root).parts
        except ValueError as exc:
            raise ResolutionError("outside_boundary", f"Reference is outside resolver boundary {root}: {candidate}") from exc
        current = root
        for part in parts:
            if part == "..":
                if current == root:
                    raise ResolutionError("outside_boundary", f"Reference escapes resolver boundary {root}: {candidate}")
                current = current.parent
                continue
            current = current / part
            try:
                mode = current.lstat().st_mode
            except OSError as exc:
                raise ResolutionError("unresolved_reference", f"Reference does not resolve: {candidate}: {exc}") from exc
            if stat.S_ISLNK(mode):
                raise ResolutionError("symlink_reference", f"Reference traverses a symlink: {current}")
            if not (stat.S_ISREG(mode) or stat.S_ISDIR(mode)):
                raise ResolutionError("unsupported_entry", f"Reference names a non-file/directory entry: {current}", unsupported=True)
        return current

    def read(self, path: Path) -> bytes:
        try:
            if path.stat().st_size > self.max_file_bytes:
                raise ResolutionError("resource_limit", f"Reference exceeds {self.max_file_bytes} bytes: {path}")
            with path.open("rb") as stream:
                raw = stream.read(self.max_file_bytes + 1)
        except OSError as exc:
            raise ResolutionError("unresolved_reference", f"Cannot acquire reference: {path}: {exc}") from exc
        if len(raw) > self.max_file_bytes:
            raise ResolutionError("resource_limit", f"Reference exceeds {self.max_file_bytes} bytes: {path}")
        digest = sha256_bytes(raw)
        prior = self.acquired.setdefault(path, digest)
        if prior != digest:
            raise ResolutionError("reference_changed", f"Reference changed during verification: {path}")
        return raw

    def resolve(self, reference: str, base: Path, *, definition: bool = False) -> dict[str, Any]:
        if not isinstance(reference, str) or not reference or re.search(r"[\x00-\x20\\]|%(?![0-9A-Fa-f]{2})", reference):
            raise ResolutionError("invalid_reference", f"Invalid URI reference: {reference!r}")
        try:
            parsed = urlsplit(reference)
            path_text = unquote(parsed.path, errors="strict")
            fragment = unquote(parsed.fragment, errors="strict")
        except (ValueError, UnicodeError) as exc:
            raise ResolutionError("invalid_reference", f"Invalid URI reference: {reference!r}") from exc
        if "\x00" in path_text or "\\" in path_text:
            raise ResolutionError("invalid_reference", f"Invalid URI path: {reference!r}")
        if parsed.query:
            raise ResolutionError("unsupported_reference", f"Reference queries are unsupported: {reference}", unsupported=True)
        if definition and parsed.fragment:
            raise ResolutionError("invalid_definition_reference", f"Product target must name a complete definition: {reference}")
        if parsed.scheme == "stdo":
            if ";" in path_text:
                raise ResolutionError("unsupported_reference", f"STDO path parameters are unsupported: {reference}", unsupported=True)
            # Store.resolve verifies the selected immutable installation. It never installs.
            try:
                path = self.store.resolve(urlunsplit(parsed._replace(fragment="")))
            except StdoError as exc:
                raise ResolutionError("unresolved_installed_reference", str(exc)) from exc
            self.boundaries[path] = self.store.root / "releases" / path.relative_to(self.store.root / "releases").parts[0]
        elif parsed.scheme in {"", "file"} and parsed.netloc in {"", "localhost"}:
            if not parsed.scheme and parsed.netloc:
                raise ResolutionError("unsupported_reference", f"Network-path references are unsupported: {reference}", unsupported=True)
            candidate = Path(path_text) if path_text else base
            if not candidate.is_absolute():
                candidate = base.parent / candidate
            path = self.local_path(candidate)
        else:
            raise ResolutionError("unsupported_reference", f"Unsupported reference scheme or host: {reference}", unsupported=True)
        if definition and not path.is_file():
            raise ResolutionError("invalid_definition_reference", f"Product target is not a regular file: {reference}")
        result: dict[str, Any] = {"reference": reference, "status": "resolved", "path": str(path), "kind": "directory" if path.is_dir() else "file"}
        if path.is_file():
            raw = self.read(path)
            result["sha256"] = sha256_bytes(raw)
            result["bytes"] = len(raw)
            if parsed.fragment:
                result["fragment"] = fragment
                result["fragment_kind"] = _check_fragment(path, raw, fragment)
        elif parsed.fragment:
            raise ResolutionError("unsupported_fragment", f"Directory fragments are unsupported: {reference}", unsupported=True)
        return result

    def observe(self, reference: Any, base: Path, *, definition: bool = False) -> dict[str, Any]:
        try:
            return self.resolve(reference, base, definition=definition)
        except ResolutionError as exc:
            return {"reference": reference, "status": "unsupported" if exc.unsupported else "failed", "code": exc.code, "message": str(exc)}

    def guard_schema(self, document: dict[str, Any], base: Path) -> None:
        reference = document.get("$schema")
        resolved = self.resolve(reference, base, definition=True)
        try:
            schema = json.loads(self.read(Path(resolved["path"])))
        except (ValueError, UnicodeError) as exc:
            raise ResolutionError("invalid_schema", f"Invalid schema JSON: {reference}") from exc
        pending = [schema]
        while pending:
            value = pending.pop()
            if isinstance(value, dict):
                for key in ("$ref", "$dynamicRef", "$recursiveRef"):
                    ref = value.get(key)
                    if ref is not None and (not isinstance(ref, str) or not ref.startswith("#")):
                        raise ResolutionError("unsupported_schema_reference", f"External schema reference is unsupported without acquisition: {ref!r}", unsupported=True)
                pending.extend(value.values())
            elif isinstance(value, list):
                pending.extend(value)


def verify_composition(
    definitions: Iterable[Path | str], store: Store, *, resolver_root: Path | str,
    max_definitions: int = 1000, max_edges: int = 10000, max_file_bytes: int = 8 * 1024 * 1024,
) -> dict[str, Any]:
    """Verify selected definitions and their explicit dependency closure.

    The caller chooses the local acquisition boundary and the installed Store.
    The returned checks do not grant access or assess prose-owned authority.
    """
    for limit in (max_definitions, max_edges, max_file_bytes):
        if type(limit) is not int or limit < 1:
            raise StdoError("Composition verification limits must be positive integers")
    root = _physical_root(Path(resolver_root))
    resolver = _Resolver(root, store, max_file_bytes)
    selected = list(dict.fromkeys(resolver.local_path(Path(path).absolute()) for path in definitions))
    queue = deque(selected)
    queued = set(selected)
    results: dict[Path, dict[str, Any]] = {}
    identities: dict[str, Path] = {}
    failures: list[dict[str, Any]] = []
    edges_seen = 0
    while queue:
        requested = queue.popleft()
        if len(results) >= max_definitions:
            failures.append({"code": "resource_limit", "message": f"Composition exceeds {max_definitions} definitions", "definition": str(requested)})
            break
        path = requested
        item: dict[str, Any] = {"definition": str(path), "definition_id": None, "selected": path in selected, "valid": False, "failures": [], "composition": []}
        results[path] = item
        try:
            # Installed target files have already passed Store.resolve, which supplies
            # a separate, exact resource capability. Relative references remain local.
            if path not in resolver.acquired:
                path = resolver.local_path(path)
                item["definition"] = str(path)
            raw = resolver.read(path)
            document = json.loads(raw)
            if not isinstance(document, dict):
                raise ResolutionError("invalid_definition", f"Definition must be an object: {path}")
            resolver.guard_schema(document, path)
            binding = load_binding(path)
            if binding.document_sha256 != sha256_bytes(raw):
                raise ResolutionError("reference_changed", f"Definition changed during acquisition: {path}")
            status = definition_status(path, store, verify=True)
            item.update(status)
            item["document_sha256"] = sha256_bytes(raw)
            identity = document.get("product", {}).get("definition_id")
            if not isinstance(identity, str) or not identity:
                raise ResolutionError("invalid_identity", f"Definition has no Product identity: {path}")
            prior = identities.setdefault(identity, requested)
            if prior != requested:
                message = f"Duplicate Product-Definition Identity {identity!r}: {prior} and {requested}"
                item["failures"].append(message)
                results[prior]["failures"].append(message)
                results[prior]["valid"] = False
            if item["failures"]:
                item["valid"] = False
                continue
            edges = document.get("composition", [])
            if not isinstance(edges, list):
                raise ResolutionError("invalid_composition", f"composition must be an array: {path}")
            for index, edge in enumerate(edges):
                edges_seen += 1
                if edges_seen > max_edges:
                    raise ResolutionError("resource_limit", f"Composition exceeds {max_edges} edges")
                row: dict[str, Any] = {"index": index, "source_definition": str(path), "source_definition_id": identity, "valid": False, "references": {}, "failures": []}
                item["composition"].append(row)
                if not isinstance(edge, dict) or set(edge) != {"product_definition", "target_definition_id", "relation", "contracts"} or not isinstance(edge.get("contracts"), list) or not edge["contracts"] or not isinstance(edge.get("target_definition_id"), str):
                    row["failures"].append({"code": "invalid_edge", "message": "Expected the four-field composition edge with a nonempty contract list"})
                    continue
                row["target_definition_id"] = edge["target_definition_id"]
                target = resolver.observe(edge["product_definition"], path, definition=True)
                row["references"] = {"product_definition": target, "relation": resolver.observe(edge["relation"], path), "contracts": [resolver.observe(ref, path) for ref in edge["contracts"]]}
                for field, observation in [("product_definition", target), ("relation", row["references"]["relation"]), *((f"contracts/{i}", ref) for i, ref in enumerate(row["references"]["contracts"]))]:
                    if observation["status"] != "resolved":
                        row["failures"].append({"field": field, **observation})
                if target["status"] == "resolved":
                    target_path = Path(target["path"])
                    try:
                        target_document = json.loads(resolver.read(target_path))
                        actual_id = target_document.get("product", {}).get("definition_id") if isinstance(target_document, dict) else None
                        if actual_id != edge["target_definition_id"]:
                            raise ResolutionError("target_identity_mismatch", f"Expected {edge['target_definition_id']!r}, found {actual_id!r} at {target_path}")
                        row["target_definition"] = str(target_path)
                        if target_path not in queued:
                            queue.append(target_path)
                            queued.add(target_path)
                    except (StdoError, ValueError, UnicodeError, AttributeError) as exc:
                        row["failures"].append({"field": "product_definition", "code": getattr(exc, "code", "invalid_target_definition"), "message": str(exc)})
                row["valid"] = not row["failures"]
            item["valid"] = not item["failures"] and all(row["valid"] for row in item["composition"])
        except (StdoError, OSError, ValueError, UnicodeError, AttributeError, RecursionError) as exc:
            item["valid"] = False
            item["failures"].append(str(exc))
            item["resolution_failure"] = {"code": getattr(exc, "code", "invalid_definition"), "message": str(exc), "status": "unsupported" if getattr(exc, "unsupported", False) else "failed"}

    for path in list(resolver.acquired):
        try:
            resolver.local_path(path, boundary=resolver.boundaries.get(path, root))
            resolver.read(path)
        except (StdoError, OSError) as exc:
            failure = {"code": "reference_changed", "path": str(path), "message": f"Reference changed during verification: {exc}"}
            failures.append(failure)
            for item in results.values():
                if item["definition"] == str(path) or item.get("schema") == str(path):
                    item["valid"] = False
                    item["failures"].append(failure["message"])
                for row in item["composition"]:
                    refs = row["references"]
                    observations = [refs.get("product_definition", {}), refs.get("relation", {}), *refs.get("contracts", [])]
                    if any(ref.get("path") == str(path) for ref in observations):
                        row["valid"] = False
                        row["failures"].append(failure)

    # Invalid dependency evidence invalidates each consuming edge, including cycles.
    changed = True
    while changed:
        changed = False
        for item in results.values():
            for row in item["composition"]:
                target = row.get("target_definition")
                if row["valid"] and target and not results.get(Path(target), {}).get("valid", False):
                    row["valid"] = False
                    row["failures"].append({"field": "product_definition", "code": "invalid_target_definition", "message": f"Target definition or its composition closure did not verify: {target}"})
                    changed = True
            if item["valid"] and any(not row["valid"] for row in item["composition"]):
                item["valid"] = False
                changed = True
    for item in results.values():
        for row in item["composition"]:
            item["failures"].extend(f"composition/{row['index']}: {failure['message']}" for failure in row["failures"])
    valid = bool(selected) and not failures and all(item["valid"] for item in results.values())
    return {"kind": "stdo.composition-verification", "schema_version": 1, "resolver_root": str(root), "installed_resources": "verified immutable stdo://releases/ resources from the selected local Store", "limits": {"definitions": max_definitions, "edges": max_edges, "file_bytes": max_file_bytes}, "valid": valid, "failures": failures, "definitions": list(results.values()), "authority_and_semantic_adequacy": "not evaluated"}


def verify_fleet_composition(
    selection: Path | str, store: Store, *, resolver_root: Path | str | None = None,
) -> dict[str, Any]:
    """Select a file or discover a directory, then verify only declared closure."""
    selected = Path(selection).absolute()
    boundary = _physical_root(Path(resolver_root) if resolver_root is not None else (selected if selected.is_dir() else selected.parent))
    selected = _Resolver(boundary, store, 8 * 1024 * 1024).local_path(selected)
    definitions = discover_definitions(selected)
    if not definitions:
        raise StdoError(f"No stdo_<label>.json definitions found under {selected}")
    report = verify_composition(definitions, store, resolver_root=boundary)
    report["root"] = str(selected)
    return report
