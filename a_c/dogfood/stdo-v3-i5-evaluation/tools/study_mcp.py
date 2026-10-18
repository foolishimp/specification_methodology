#!/usr/bin/env python3
"""Allowlisted, metered MCP reader for the frozen direct/Graphify dogfood pilot.

The protocol implementation uses the standard library. Only the assisted tools
import the existing a_c codec and exact pinned upstream Graphify checkout.
Nothing in this server evaluates a model predicate or supplies semantic meaning.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import time
import traceback
from pathlib import Path, PurePosixPath
from typing import Any, BinaryIO
from urllib.parse import unquote

sys.dont_write_bytecode = True
UPSTREAM_COMMIT = "fe085cedddde3a18554f8749b230bfe47f3dcce7"
FAMILIES = ("symbols", "clauses", "residuals", "frame_indexes")
MAX_CALLS = 24
MAX_BYTES = 160_000
AC_ROOT = Path(__file__).resolve().parents[3]
CLAIM = "Exact frozen authored content; structural retrieval supplies no implication, applicability, authority, predicate result or semantic acceptance."


def encoded(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def parse(raw: bytes | str) -> Any:
    return json.loads(raw, object_pairs_hook=_pairs, parse_constant=lambda _: (_ for _ in ()).throw(ValueError("nonfinite JSON")))


class Refusal(ValueError):
    def __init__(self, code: str, message: str, **details: Any):
        super().__init__(message)
        self.body = {"status": "refused", "code": code, "message": message, **details}


def require(ok: bool, code: str, message: str, **details: Any) -> None:
    if not ok:
        raise Refusal(code, message, **details)


def safe_name(name: Any) -> str:
    require(isinstance(name, str) and bool(name), "invalid_path", "A nonempty allowlisted relative path is required.")
    path = PurePosixPath(name)
    require(not path.is_absolute() and ".." not in path.parts and "\\" not in name
            and str(path) == name and "\x00" not in name,
            "invalid_path", "Only canonical allowlisted relative paths are available.")
    return name


def integer(value: Any, low: int, high: int, name: str) -> int:
    require(type(value) is int and low <= value <= high, "invalid_argument", f"{name} must be an integer from {low} to {high}.")
    return value


def literal(value: Any, name: str, maximum: int = 2000) -> str:
    require(isinstance(value, str) and 0 < len(value) <= maximum, "invalid_argument", f"{name} must be a nonempty string of at most {maximum} characters.")
    return value


class Audit:
    def __init__(self, path: Path):
        self.start = time.perf_counter()
        # A run's audit trail is never silently overwritten or reused.
        path.parent.mkdir(parents=True, exist_ok=True)
        self.handle = path.open("x", encoding="utf-8")
        self.calls_attempted = 0
        self.calls_admitted = 0
        self.content_bytes = 0
        self.wire_bytes = 0
        self.pending_read_refusals = 0
        self.graph_startup_seconds = 0.0

    def write(self, event: str, **values: Any) -> None:
        self.handle.write(encoded({"event": event, "elapsed_seconds": time.perf_counter() - self.start, **values}).decode() + "\n")
        self.handle.flush()

    def counters(self) -> dict[str, Any]:
        return {"calls_attempted": self.calls_attempted, "calls_admitted": self.calls_admitted,
                "content_bytes": self.content_bytes, "wire_bytes": self.wire_bytes,
                "pending_read_refusals": self.pending_read_refusals,
                "graph_startup_seconds": self.graph_startup_seconds}


class Baseline:
    """Load and authenticate the complete allowlist once, then serve memory."""
    def __init__(self, root: Path, tenant: str):
        self.root = root.resolve(strict=True)
        require(not root.is_symlink(), "baseline_invalid", "Baseline root must be a regular directory.")
        manifest_raw = (self.root / "manifest.json").read_bytes()
        self.manifest = parse(manifest_raw)
        require(self.manifest.get("profile") == "ac.eval.native-baseline/1"
                and self.manifest.get("tenant") == tenant, "baseline_invalid", "Wrong native baseline profile or tenant.")
        self.manifest_sha256 = sha(manifest_raw)
        self.files: dict[str, bytes] = {}
        self.pins: dict[str, dict[str, Any]] = {}
        frozen_files = [{**item, "path": "sources/" + safe_name(item["path"])} for item in self.manifest["files"]]
        frozen_files += [self.manifest["native_program"],
                         {"path": self.manifest["coverage_path"], "sha256": self.manifest["coverage_sha256"],
                          "bytes": (self.root / safe_name(self.manifest["coverage_path"])).stat().st_size}]
        for item in frozen_files:
            name = safe_name(item["path"])
            require(name not in self.files, "baseline_invalid", "Duplicate baseline member.")
            path = self.root / name
            require(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(self.root)
                    and all(not parent.is_symlink() for parent in path.parents if parent != self.root.parent),
                    "baseline_invalid", "Baseline members must stay within the regular-file allowlist.")
            raw = path.read_bytes()
            require(len(raw) == item["bytes"] and sha(raw) == item["sha256"], "baseline_drift", "Baseline member differs from its frozen pin.")
            self.files[name] = raw
            self.pins[name] = {"path": name, "sha256": sha(raw), "bytes": len(raw)}
        require("program.json" in self.files and "coverage.json" in self.files,
                "baseline_invalid", "Program and coverage must occur in the frozen allowlist.")
        self.program = parse(self.files["program.json"])
        self.coverage = parse(self.files["coverage.json"])
        self.sources = {name[8:]: raw for name, raw in self.files.items() if name.startswith("sources/")}
        self.source_text: dict[str, str] = {}
        self.source_lines: dict[str, list[str]] = {}
        self.records: dict[str, tuple[str, dict[str, Any]]] = {}
        for family in FAMILIES:
            for record in self.program[family]:
                identity = record["uri"]
                require(identity not in self.records, "baseline_invalid", "Duplicate native identity.")
                self.records[identity] = (family, record)
        envelope = {key: value for key, value in self.program.items() if key not in FAMILIES}
        require(self.program["uri"] not in self.records, "baseline_invalid", "Program identity collides with a record.")
        self.records[self.program["uri"]] = ("program", envelope)
        self.roots = self.manifest["source_roots"]
        require(isinstance(self.roots, list), "baseline_invalid", "Source roots must be explicit mappings.")

    def observation(self, paths: list[str] | None = None, text_emitted: list[dict[str, Any]] | None = None) -> dict[str, Any]:
        return {"baseline_manifest_sha256": self.manifest_sha256,
                "program": self.pins["program.json"], "source_pins": self.manifest["input"],
                "source_coordinate_pins": [self.pins["sources/" + name] for name in sorted(set(paths or []))],
                "documentary_text_emitted": text_emitted or [],
                "scope": "Pins authenticate coordinates; only documentary_text_emitted identifies source text included in this tool result."}

    def resolve(self, value: str) -> tuple[str, str | None]:
        value = literal(value, "path", 4000)
        base, _, anchor = value.partition("#")
        for route in self.roots:
            if base.startswith(route["uri_prefix"]):
                base = route["path_prefix"] + unquote(base[len(route["uri_prefix"]):])
                break
        if base.startswith("sources/"):
            base = base[8:]
        base = safe_name(base)
        require(base in self.sources, "source_not_allowlisted", "Source path is absent from the frozen source allowlist.")
        return base, unquote(anchor) if anchor else None

    def text(self, name: str) -> str:
        if name not in self.source_text:
            try:
                self.source_text[name] = self.sources[name].decode("utf-8")
            except UnicodeDecodeError:
                raise Refusal("non_text_source", "This source is not UTF-8 text.") from None
        return self.source_text[name]

    def lines(self, name: str) -> list[str]:
        if name not in self.source_lines:
            # keepends conserves CRLFs and the final-newline distinction.
            self.source_lines[name] = self.text(name).splitlines(keepends=True)
        return self.source_lines[name]

    def source_routes(self, record: Any) -> list[dict[str, Any]]:
        routes: dict[tuple[str, str], dict[str, Any]] = {}
        # The exact authored coordinates stay in record; this is mechanical URI
        # resolution only, including coordinates inside literal JSON strings.
        def walk(value: Any) -> None:
            if isinstance(value, dict):
                for child in value.values():
                    walk(child)
            elif isinstance(value, list):
                for child in value:
                    walk(child)
            elif isinstance(value, str):
                candidates = [value]
                if value.startswith(("{", "[")):
                    try:
                        walk(parse(value))
                    except (ValueError, TypeError):
                        pass
                for candidate in candidates:
                    if not any(candidate.startswith(root["uri_prefix"]) for root in self.roots):
                        continue
                    try:
                        name, anchor = self.resolve(candidate)
                    except Refusal:
                        continue
                    routes[(name, anchor or "")] = {"path": name, "anchor": anchor or "", "uri": candidate,
                                                       "sha256": sha(self.sources[name])}
        walk(record)
        return [routes[key] for key in sorted(routes)]


class GraphAccess:
    def __init__(self, baseline: Baseline, args: argparse.Namespace, audit: Audit):
        self.baseline, self.args, self.audit = baseline, args, audit
        self.ready = False

    def load(self) -> None:
        if self.ready:
            return
        started = time.perf_counter()
        args = self.args
        upstream = args.upstream.resolve(strict=True)
        commit = subprocess.check_output(["git", "-C", str(upstream), "rev-parse", "HEAD"], text=True).strip()
        dirty = subprocess.check_output(["git", "-C", str(upstream), "status", "--porcelain", "--untracked-files=no"], text=True)
        require(commit == UPSTREAM_COMMIT and not dirty, "graph_pin_mismatch", "Actual Graphify checkout must be the exact clean pinned revision.")
        artifacts = args.artifacts.resolve(strict=True)
        manifest = parse((artifacts / "manifest.json").read_bytes())
        require(manifest.get("profile") == "a_c.v3-graphify-representation/1" and manifest.get("tenant") == args.tenant,
                "graph_pin_mismatch", "Wrong Graphify artifact profile or tenant.")
        for name in ("model.json.gz", "selectors.json"):
            raw = (artifacts / name).read_bytes()
            pin = manifest["artifacts"][name]
            require(len(raw) == pin["bytes"] and sha(raw) == pin["sha256"], "graph_pin_mismatch", "Frozen Graphify artifact drift.")
        require(manifest["raw_program_sha256"] == sha(self.baseline.files["program.json"]),
                "graph_pin_mismatch", "Graphify and native arms must select the same program bytes.")
        codec = args.ac_root / "build_tenants/graphify/code/ac_graph.py"
        require(sha(codec.read_bytes()) == manifest["codec_sha256"], "graph_pin_mismatch", "Codec no longer matches the frozen representation.")
        spec = importlib.util.spec_from_file_location("ac_study_frozen_codec", codec)
        require(spec is not None and spec.loader is not None, "graph_unavailable", "Cannot load frozen codec.")
        self.ac = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = self.ac
        spec.loader.exec_module(self.ac)
        model_doc = parse(gzip.decompress((artifacts / "model.json.gz").read_bytes()))
        actual_raw = args.graph.read_bytes()
        actual_doc = parse(actual_raw)
        # The actual upstream export, not a reconstructed substitute, must decode
        # to the exact frozen model before its discovery results can be exposed.
        self.model = self.ac.decode(self.ac.GraphCarrier(actual_doc))
        require(self.model.document == model_doc and self.ac.model_identity(self.model) == manifest["model"],
                "graph_pin_mismatch", "Actual Graphify carrier differs from the frozen model.")
        mapped: dict[str, tuple[str, Any]] = {}
        self.routes: dict[str, list[dict[str, Any]]] = {}
        for identity, record in self.model.records.items():
            value = record.fields.get("value", {})
            family = value.get("native_family")
            if family in FAMILIES:
                mapped[identity] = (family, parse(value["native_json"]))
                self.routes[identity] = value["routes"]
        native = {key: item for key, item in self.baseline.records.items() if item[0] in FAMILIES}
        require(mapped == native, "graph_pin_mismatch", "Graphify native payloads must equal every exact baseline record.")
        self.catalog = {}
        index = self.ac._projection_index(self.model)
        catalog = parse((artifacts / "selectors.json").read_bytes())
        require(catalog["tenant"] == args.tenant, "graph_pin_mismatch", "Selector tenant differs.")
        for selector in catalog["selectors"]:
            identity = selector["uri"]
            require(identity not in self.catalog and identity in self.baseline.records
                    and self.baseline.records[identity][0] == "frame_indexes",
                    "graph_pin_mismatch", "Duplicate or non-native selector.")
            included, pending = {identity}, [identity]
            while pending:
                for target in index.dependencies[pending.pop()]:
                    if target not in included:
                        included.add(target)
                        pending.append(target)
            require(sorted(included) == selector["required_records"] and len(included) == selector["records"],
                    "graph_pin_mismatch", "Selector catalogue differs from complete declared model closure.")
            require(included <= set(native), "graph_pin_mismatch", "Selector closure contains a non-native record.")
            self.catalog[identity] = selector
        require(set(self.catalog) == {key for key, item in native.items() if item[0] == "frame_indexes"},
                "graph_pin_mismatch", "Selector catalogue must cover every exact native selector.")
        sys.path.insert(0, str(upstream))
        from graphify.serve import _query_graph_text, _read_graph
        import graphify.serve
        require(Path(graphify.serve.__file__).resolve() == upstream / "graphify/serve.py",
                "graph_pin_mismatch", "Graphify import did not come from the pinned checkout.")
        self.query_function = _query_graph_text
        complete_graph = _read_graph(str(args.graph))
        # Learning sidecars are outside the frozen study inputs. Refuse rather
        # than admit an unpinned overlay that could change displayed answers.
        require(not complete_graph.graph.get("_learning_overlay"), "graph_pin_mismatch", "An unpinned Graphify learning overlay is present.")
        self.graph, self.discovery_scope = self.allowed_discovery_graph(complete_graph)
        self.pins = {"upstream_commit": commit, "serve_sha256": sha((upstream / "graphify/serve.py").read_bytes()),
                     "actual_graph_sha256": sha(actual_raw), "codec_sha256": manifest["codec_sha256"],
                     "model": manifest["model"], "selectors": manifest["artifacts"]["selectors.json"]}
        self.ready = True
        self.audit.graph_startup_seconds = time.perf_counter() - started
        self.audit.write("graph_startup", duration_seconds=self.audit.graph_startup_seconds, pins=self.pins,
                         nodes=self.graph.number_of_nodes(), edges=self.graph.number_of_edges(),
                         selectors_validated=len(self.catalog), discovery_scope=self.discovery_scope)

    def allowed_discovery_graph(self, complete_graph: Any) -> tuple[Any, dict[str, Any]]:
        """Induce retrieval from actual carrier nodes without privileged source.

        Closure continues to use the frozen complete model and checked catalogue;
        this filtering applies only to the additional discovery surface.
        """
        eligible: set[str] = set()
        excluded_sources = 0
        for identity, record in self.model.records.items():
            value = record.fields.get("value", {})
            family = value.get("native_family")
            if family in (*FAMILIES, "envelope"):
                eligible.add(identity)
            elif family == "source_members":
                member = parse(value["native_json"])
                if member["path"] in self.baseline.sources:
                    require(member["text"].encode("utf-8") == self.baseline.sources[member["path"]],
                            "graph_pin_mismatch", "Allowlisted graph source text differs from the native baseline.")
                    eligible.add(identity)
                else:
                    excluded_sources += 1
        excluded = set(self.model.records) - eligible
        retained: set[str] = set()
        external_targets: set[str] = set()
        for node, data in complete_graph.nodes(data=True):
            role, payload = data.get("ac_role"), data.get("ac_payload", {})
            if role == "record" and payload["record"]["id"] in eligible:
                retained.add(node)
            elif role in ("reference-occurrence", "reference-endpoint"):
                if payload["owner"] in eligible and payload["target"] not in excluded:
                    retained.add(node)
                    external_targets.add(payload["target"])
        for node, data in complete_graph.nodes(data=True):
            if data.get("ac_role") == "external" and data["ac_payload"]["external_identity"] in external_targets:
                retained.add(node)
        graph = complete_graph.subgraph(retained).copy()
        for _, data in graph.nodes(data=True):
            # Incidental clustering/display annotations may have been computed
            # over excluded sources. Keep only codec-checked payload/display
            # fields and the actual carrier's source/type coordinates.
            for key in set(data) - {"label", "ac_payload", "ac_role", "attributes", "file_type", "source_file", "norm_label"}:
                del data[key]
        logical_directed = graph.graph.get("_logical_directed", False)
        graph.graph.clear()
        graph.graph.update(_logical_directed=logical_directed, _learning_overlay={})
        scope = {"profile": "ac.eval.allowlisted-graph-discovery/1",
                 "strategy": "Induced nodes/edges from actual upstream-loaded carrier: all exact native records and envelope, allowlisted source-member records, their eligible reference occurrence/endpoint nodes and referenced external coordinates; metadata/excluded-source records/occurrences/endpoints and incidental community/ranking/overlay metadata removed.",
                 "source_allowlist_manifest_sha256": self.baseline.manifest_sha256,
                 "parent_nodes": complete_graph.number_of_nodes(), "parent_edges": complete_graph.number_of_edges(),
                 "retained_nodes": graph.number_of_nodes(), "retained_edges": graph.number_of_edges(),
                 "excluded_source_members": excluded_sources}
        return graph, scope

    def query(self, question: str, depth: int, token_budget: int) -> dict[str, Any]:
        self.load()
        result = self.query_function(self.graph, question, mode="bfs", depth=depth, token_budget=token_budget)
        return {"status": "ok", "question": question, "depth": depth, "token_budget": token_budget,
                "result": result, "graph_pins": self.pins, "discovery_scope": self.discovery_scope,
                "scope": "Actual pinned Graphify ranked/BFS discovery; token-bounded display, not complete required context.",
                "claim": CLAIM}

    def select(self, selectors: list[str], materialize: bool = False) -> dict[str, Any]:
        self.load()
        require(selectors and len(selectors) == len(set(selectors)) and len(selectors) <= 8,
                "invalid_argument", "Supply one to eight distinct exact native selector IDs.")
        require(all(identity in self.catalog for identity in selectors), "unknown_selector", "Every selector must be an exact native frame_index ID.")
        included = sorted({identity for selector in selectors for identity in self.catalog[selector]["required_records"]})
        manifest = [{"id": identity, "family": self.baseline.records[identity][0],
                     "source_routes": self.baseline.source_routes(self.baseline.records[identity][1])} for identity in included]
        result = {"status": "ok", "profile": "ac.eval.complete-declared-acquisition/1", "selectors": selectors,
                "included": included, "manifest": manifest,
                "mode": "materialized" if materialize else "complete_manifest", "native_payload_acquired": materialize,
                "documentary_source_text_acquired": False,
                "graph_pins": self.pins,
                "conditional_rule": "Establish applicability externally; request any applicable target selector explicitly or retain unknown applicability and withhold dependent action.",
                "read_routes": "Each manifest id is a read_record(id); each source_routes path/anchor is a read_source(path, anchor). Documentary source text requires explicit source reads even after native materialization.",
                "claim": CLAIM}
        if materialize:
            chosen = set(included)
            result["native"] = {family: [record for identity, (kind, record) in self.baseline.records.items()
                                         if kind == family and identity in chosen] for family in FAMILIES}
            result["acquisition_routes"] = [{"owner": identity, **route} for identity in included for route in self.routes[identity]]
        else:
            result["next_step"] = "This is the complete declared coordinate manifest. Read the required native records explicitly, or request graph_select with materialize=true to acquire the entire exact native closure within budget."
        return result


def schema(properties: dict[str, Any], required: list[str] | None = None) -> dict[str, Any]:
    return {"type": "object", "properties": properties, "required": required or [], "additionalProperties": False}


STRING = {"type": "string"}
INTEGER = {"type": "integer"}


def tool_definitions(assisted: bool) -> list[dict[str, Any]]:
    specs = [
        ("info", "Read exact candidate coverage, native counts, source routing and shared resource envelope.", schema({})),
        ("list_sources", "List frozen allowlisted source paths and hashes. Use prefix and explicit pagination; no file text is clipped.",
         schema({"prefix": STRING, "offset": INTEGER, "limit": INTEGER})),
        ("search", "Literal case-insensitive discovery over exact source lines or native IDs. Returns an explicit page with total/next_offset; matching line text is exact. Discovery pages do not establish complete context.",
         schema({"query": STRING, "scope": {"type": "string", "enum": ["source", "native"]}, "path": STRING, "family": STRING, "offset": INTEGER, "limit": INTEGER}, ["query", "scope"])),
        ("read_source", "Read exact UTF-8 source lines or one exact Markdown heading section. Use path/URI plus start_line/end_line or anchor. Large reads refuse and require narrowing.",
         schema({"path": STRING, "start_line": INTEGER, "end_line": INTEGER, "anchor": STRING}, ["path"])),
        ("list_records", "List exact native IDs in a family: symbols, clauses, residuals, frame_indexes or program. Use explicit pagination.",
         schema({"family": STRING, "offset": INTEGER, "limit": INTEGER}, ["family"])),
        ("read_record", "Read one exact native record and its source routes. Optional JSON pointer selects an exact value when a whole-record read is too large.",
         schema({"id": STRING, "pointer": STRING}, ["id"])),
    ]
    if assisted:
        specs += [
            ("graph_query", "Use actual pinned Graphify ranked/BFS discovery. This bounded display does not establish complete governing context; graph_select requests declared acquisition.",
             schema({"question": STRING, "depth": INTEGER, "token_budget": INTEGER}, ["question"])),
            ("graph_select", "Get the complete declared required-ID/source-coordinate manifest for exact native frame_index IDs. Set materialize=true for complete exact native content and routes; oversized acquisition refuses with complete manifest for explicit narrow reads, never partial success.",
             schema({"selectors": {"type": "array", "items": STRING, "minItems": 1, "maxItems": 8}, "materialize": {"type": "boolean"}}, ["selectors"])),
        ]
    return [{"name": name, "description": description, "inputSchema": inputs,
             "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False}}
            for name, description, inputs in specs]


class Server:
    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.audit = Audit(args.log)
        started = time.perf_counter()
        try:
            self.baseline = Baseline(args.baseline, args.tenant)
        except Exception as exc:
            self.audit.write("startup_failed", exception=type(exc).__name__, traceback=traceback.format_exc())
            self.audit.handle.close()
            raise
        self.definitions = tool_definitions(args.condition == "graphify")
        self.allowed_arguments = {tool["name"]: tool["inputSchema"] for tool in self.definitions}
        self.graph = GraphAccess(self.baseline, args, self.audit) if args.condition == "graphify" else None
        self.audit.write("startup", condition=args.condition, tenant=args.tenant,
                         duration_seconds=time.perf_counter() - started,
                         baseline=self.baseline.observation(),
                         limits={"tool_calls": args.max_calls, "tool_content_utf8_bytes": args.max_bytes},
                         tool_definitions_sha256=sha(encoded(self.definitions)),
                         server_sha256=sha(Path(__file__).read_bytes()))

    def handle_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        b = self.baseline
        spec = self.allowed_arguments.get(name)
        require(spec is not None, "unknown_tool", "This tool is unavailable in the current condition.")
        require(isinstance(arguments, dict) and set(arguments) <= set(spec["properties"])
                and set(spec["required"]) <= set(arguments), "invalid_argument", "Tool argument fields differ from the declared schema.")
        for key, value in arguments.items():
            kind = spec["properties"][key]["type"]
            require((kind == "string" and isinstance(value, str)) or (kind == "integer" and type(value) is int)
                    or (kind == "array" and isinstance(value, list) and all(isinstance(item, str) for item in value))
                    or (kind == "boolean" and type(value) is bool),
                    "invalid_argument", "Tool argument type differs from the declared schema.")
        if name == "info":
            return {"status": "ok", "tenant": self.args.tenant, "coverage": b.coverage,
                    "native_counts": {family: len(b.program[family]) for family in FAMILIES},
                    "program_uri": b.program["uri"], "source_roots": b.roots, "source_members": len(b.sources),
                    "resource_envelope": {"max_tool_calls": self.args.max_calls, "max_content_utf8_bytes": self.args.max_bytes,
                                          "calls_used_including_this_call": self.audit.calls_admitted,
                                          "content_bytes_preceding_this_result": self.audit.content_bytes}, "claim": CLAIM}
        if name in ("list_sources", "list_records"):
            offset = integer(arguments.get("offset", 0), 0, 1_000_000, "offset")
            limit = integer(arguments.get("limit", 40), 1, 200, "limit")
            if name == "list_sources":
                prefix = arguments.get("prefix", "")
                rows = [{"path": path, "sha256": sha(raw), "bytes": len(raw)} for path, raw in sorted(b.sources.items()) if path.startswith(prefix)]
            else:
                family = arguments["family"]
                require(family in (*FAMILIES, "program"), "invalid_argument", "Unknown native family.")
                rows = [{"id": identity, "family": kind} for identity, (kind, _) in b.records.items() if kind == family]
            return {"status": "ok", "total": len(rows), "offset": offset, "limit": limit,
                    "next_offset": offset + limit if offset + limit < len(rows) else None, "items": rows[offset:offset + limit],
                    "scope": "Explicit page of a frozen inventory; no content acquisition or semantic claim."}
        if name == "search":
            query = literal(arguments["query"], "query", 500)
            limit = integer(arguments.get("limit", 30), 1, 100, "limit")
            offset = integer(arguments.get("offset", 0), 0, 1_000_000, "offset")
            needle, scope = query.casefold(), arguments["scope"]
            matches: list[dict[str, Any]] = []
            if scope == "source":
                require("family" not in arguments, "invalid_argument", "family applies only to native search.")
                paths = [b.resolve(arguments["path"])[0]] if "path" in arguments else sorted(b.sources)
                for path in paths:
                    try:
                        lines = b.lines(path)
                    except Refusal:
                        continue
                    for ordinal, line in enumerate(lines, 1):
                        if needle in line.casefold():
                            matches.append({"path": path, "line": ordinal, "text": line})
            else:
                require(scope == "native" and "path" not in arguments, "invalid_argument", "scope must be source or native; path applies only to source search.")
                family = arguments.get("family")
                require(family is None or family in (*FAMILIES, "program"), "invalid_argument", "Unknown native family.")
                for identity, (kind, record) in b.records.items():
                    if (family is None or kind == family) and needle in encoded(record).decode().casefold():
                        matches.append({"id": identity, "family": kind})
            total = len(matches)
            matches = matches[offset:offset + limit]
            result = {"status": "ok", "query": query, "scope": "literal case-insensitive " + scope + " discovery page; not complete acquired context",
                      "matches": matches, "matches_total": total, "offset": offset, "limit": limit,
                      "next_offset": offset + limit if offset + limit < total else None, "claim": CLAIM}
            if scope == "source":
                result["source_observation_paths"] = sorted({row["path"] for row in matches})
                result["documentary_text_emitted"] = [{"path": row["path"], "start_line": row["line"], "end_line": row["line"],
                                                        "utf8_bytes": len(row["text"].encode("utf-8"))} for row in matches]
            return result
        if name == "read_source":
            path, uri_anchor = b.resolve(arguments["path"])
            anchor = arguments.get("anchor", uri_anchor)
            lines = b.lines(path)
            has_range = "start_line" in arguments or "end_line" in arguments
            require(not (anchor and has_range), "invalid_argument", "Choose an exact anchor or explicit line range, not both.")
            if anchor:
                start, end = self.anchor_range(lines, anchor)
            else:
                require(not has_range or {"start_line", "end_line"} <= set(arguments),
                        "invalid_argument", "Both start_line and end_line are required for a line range.")
                start = integer(arguments.get("start_line", 1), 1, max(1, len(lines)), "start_line")
                end = integer(arguments.get("end_line", len(lines)), start, max(start, len(lines)), "end_line")
            return {"status": "ok", "path": path, "anchor": anchor or "", "start_line": start, "end_line": end,
                    "total_lines": len(lines), "content": "".join(lines[start - 1:end]), "source_observation_paths": [path],
                    "documentary_text_emitted": [{"path": path, "anchor": anchor or "", "start_line": start, "end_line": end,
                                                  "utf8_bytes": len("".join(lines[start - 1:end]).encode("utf-8"))}],
                    "narrowing_routes": {"path": path, "start_line": start, "end_line": end}, "claim": CLAIM}
        if name == "read_record":
            identity = literal(arguments["id"], "id", 4000)
            require(identity in b.records, "unknown_record", "Native identity is absent from the exact program.")
            family, record = b.records[identity]
            value: Any = record
            pointer = arguments.get("pointer", "")
            require(pointer == "" or pointer.startswith("/"), "invalid_argument", "JSON pointer must be empty or start with /.")
            if pointer:
                try:
                    for item in pointer[1:].split("/"):
                        require(not re.search(r"~(?![01])", item), "invalid_argument", "Malformed JSON pointer escape.")
                        key = item.replace("~1", "/").replace("~0", "~")
                        if isinstance(value, list):
                            require(bool(re.fullmatch(r"0|[1-9][0-9]*", key)), "invalid_argument", "Invalid JSON pointer array index.")
                            value = value[int(key)]
                        else:
                            value = value[key]
                except (KeyError, IndexError, TypeError, ValueError):
                    raise Refusal("unknown_pointer", "JSON pointer does not select an exact native value.") from None
            routes = b.source_routes(record)
            return {"status": "ok", "id": identity, "family": family, "pointer": pointer, "record": value,
                    "record_sha256": sha(encoded(record)), "source_routes": routes,
                    "source_observation_paths": [route["path"] for route in routes],
                    "narrowing_routes": {"id": identity, "available_fields": list(value) if isinstance(value, dict) else [],
                                         "array_length": len(value) if isinstance(value, list) else None}, "claim": CLAIM}
        if name == "graph_query":
            assert self.graph is not None
            return self.graph.query(literal(arguments["question"], "question"),
                                    integer(arguments.get("depth", 2), 0, 4, "depth"),
                                    integer(arguments.get("token_budget", 1600), 100, 4000, "token_budget"))
        if name == "graph_select":
            assert self.graph is not None
            return self.graph.select(arguments["selectors"], arguments.get("materialize", False))
        raise Refusal("unknown_tool", "Tool not implemented.")

    @staticmethod
    def anchor_range(lines: list[str], anchor: str) -> tuple[int, int]:
        anchor = literal(anchor.lstrip("#"), "anchor", 500)
        headings: list[tuple[int, int, str]] = []
        seen: dict[str, int] = {}
        for ordinal, line in enumerate(lines, 1):
            explicit = re.search(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', line, re.I)
            match = re.match(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$", line)
            if match:
                title = re.sub(r"<[^>]+>", "", match[2]).lower()
                slug = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
                count = seen.get(slug, 0)
                seen[slug] = count + 1
                slug = slug if count == 0 else f"{slug}-{count}"
                headings.append((ordinal, len(match[1]), slug))
            if explicit:
                headings.append((ordinal, len(match[1]) if match else 6, explicit[1]))
        matches = [row for row in headings if row[2] == anchor]
        require(len(matches) == 1, "anchor_not_found", "Anchor must identify exactly one literal Markdown heading or explicit anchor; use exact line coordinates otherwise.")
        start, level, _ = matches[0]
        end = next((line - 1 for line, depth, _ in headings if line > start and depth <= level), len(lines))
        return start, end

    def call(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        a = self.audit
        a.calls_attempted += 1
        started = time.perf_counter()
        graph_before = a.graph_startup_seconds
        if a.calls_admitted >= self.args.max_calls:
            body = {"status": "refused", "code": "call_budget_exhausted", "message": "No further source/tool acquisitions are admitted."}
        else:
            a.calls_admitted += 1
            try:
                body = self.handle_tool(name, arguments)
            except Refusal as exc:
                body = exc.body
            except Exception as exc:
                # Detailed runtime paths stay only in the private audit log.
                a.write("tool_exception", tool=name, exception=type(exc).__name__, traceback=traceback.format_exc())
                body = {"status": "refused", "code": "infrastructure_error", "message": "The tool failed; the private audit trail retains the infrastructure failure."}
        paths = body.pop("source_observation_paths", [])
        text_emitted = body.pop("documentary_text_emitted", [])
        body["observation"] = self.baseline.observation(paths, text_emitted)
        body["budget"] = {"calls_used": a.calls_admitted, "calls_remaining": max(0, self.args.max_calls - a.calls_admitted),
                          "content_bytes_before": a.content_bytes, "content_bytes_limit": self.args.max_bytes}
        payload = encoded(body)
        remaining = self.args.max_bytes - a.content_bytes
        if len(payload) > remaining:
            a.pending_read_refusals += 1
            estimated = len(payload)
            details = {key: body[key] for key in ("manifest", "narrowing_routes", "selectors", "included") if key in body}
            body = {"status": "refused", "code": "narrow_read_required", "message": "Complete result exceeds remaining content budget. Explicitly request narrower exact source lines or native JSON pointer values; no result content was truncated.",
                    "required_utf8_bytes": estimated, "remaining_utf8_bytes": remaining, **details,
                    "observation": self.baseline.observation(), "budget": body["budget"]}
            payload = encoded(body)
            if len(payload) > remaining:
                # A full closure manifest is never silently clipped either.
                body = {"status": "refused", "code": "content_budget_exhausted", "message": "Result and its complete narrowing manifest exceed the remaining content budget; no partial acquisition is returned.",
                        "required_utf8_bytes": estimated, "remaining_utf8_bytes": remaining}
                payload = encoded(body)
                if len(payload) > remaining:
                    payload = b""
        a.content_bytes += len(payload)
        duration = time.perf_counter() - started
        a.write("tool_call", tool=name, arguments=arguments, status=body["status"], code=body.get("code"),
                duration_seconds=duration, graph_startup_seconds_in_call=a.graph_startup_seconds - graph_before,
                retrieval_seconds=max(0.0, duration - (a.graph_startup_seconds - graph_before)),
                acquisition_kind=("documentary_source_lines" if name == "read_source" else "documentary_search_lines" if name == "search" and arguments.get("scope") == "source"
                                  else "native_record" if name == "read_record" else "declared_closure_or_manifest" if name == "graph_select"
                                  else "graph_discovery" if name == "graph_query" else "inventory_or_metadata"),
                source_bytes_emitted=sum(row["utf8_bytes"] for row in body.get("observation", {}).get("documentary_text_emitted", [])),
                emitted_utf8_bytes=len(payload), emitted_text=payload.decode("utf-8"), **a.counters())
        return {"content": [{"type": "text", "text": payload.decode("utf-8")}] if payload else [],
                "isError": body["status"] == "refused"}

    def request(self, request: dict[str, Any]) -> dict[str, Any] | None:
        method = request.get("method")
        if "id" not in request:
            self.audit.write("notification", method=method)
            return None
        identity = request["id"]
        if method == "initialize":
            version = request.get("params", {}).get("protocolVersion", "2024-11-05")
            result = {"protocolVersion": version, "capabilities": {"tools": {"listChanged": False}},
                      "serverInfo": {"name": "ac_study", "version": "1.0.0"},
                      "instructions": "Use only these frozen allowlisted tools for the study. Start with info. Every tools/call including a refusal uses one of 24 calls. Tool content is capped at 160000 UTF-8 bytes per run; large reads require explicit narrowing. Literal discovery and Graphify neighborhoods supply no semantic judgment. Cite exact source path, anchor and quote. Preserve unknown applicability and coverage limitations."}
        elif method == "ping":
            result = {}
        elif method == "tools/list":
            result = {"tools": self.definitions}
        elif method == "tools/call":
            params = request.get("params", {})
            result = self.call(params.get("name", ""), params.get("arguments", {}))
        elif method in ("resources/list", "resources/templates/list", "prompts/list"):
            result = {"resources" if method == "resources/list" else "resourceTemplates" if method == "resources/templates/list" else "prompts": []}
        else:
            return {"jsonrpc": "2.0", "id": identity, "error": {"code": -32601, "message": "Method not found"}}
        return {"jsonrpc": "2.0", "id": identity, "result": result}

    def serve(self, stream: BinaryIO, output: BinaryIO) -> None:
        try:
            while True:
                message = read_message(stream)
                if message is None:
                    break
                raw, framing = message
                request: Any = None
                try:
                    request = parse(raw)
                    require(isinstance(request, dict), "invalid_request", "JSON-RPC request must be an object.")
                    response = self.request(request)
                except (ValueError, TypeError, KeyError):
                    response = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Invalid JSON-RPC message"}}
                if response is None:
                    continue
                serialized = encoded(response)
                wire = (b"Content-Length: " + str(len(serialized)).encode() + b"\r\n\r\n" + serialized
                        if framing == "headers" else serialized + b"\n")
                output.write(wire)
                output.flush()
                self.audit.wire_bytes += len(wire)
                self.audit.write("protocol_output", method=request.get("method") if isinstance(request, dict) else None,
                                 emitted_wire_utf8_bytes=len(wire), response_sha256=sha(serialized))
        finally:
            self.audit.write("shutdown", **self.audit.counters())
            self.audit.handle.close()


def read_message(stream: BinaryIO) -> tuple[bytes, str] | None:
    line = stream.readline(1_000_001)
    if not line:
        return None
    if len(line) > 1_000_000:
        raise ValueError("oversized protocol line")
    if line.lower().startswith(b"content-length:"):
        length = int(line.split(b":", 1)[1].strip())
        if not 0 <= length <= 1_000_000:
            raise ValueError("oversized protocol payload")
        while True:
            header = stream.readline(4096)
            if header in (b"\r\n", b"\n"):
                break
            if not header:
                raise ValueError("incomplete protocol headers")
        raw = stream.read(length)
        if len(raw) != length:
            raise ValueError("incomplete protocol payload")
        return raw, "headers"
    return line, "lines"


def arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tenant", choices=("codex", "claude"), required=True)
    parser.add_argument("--condition", choices=("direct", "graphify"), required=True)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--ac-root", type=Path, default=AC_ROOT)
    parser.add_argument("--artifacts", type=Path)
    parser.add_argument("--graph", type=Path)
    parser.add_argument("--upstream", type=Path)
    parser.add_argument("--max-calls", type=int, default=MAX_CALLS)
    parser.add_argument("--max-bytes", type=int, default=MAX_BYTES)
    args = parser.parse_args(argv)
    require(0 < args.max_calls <= MAX_CALLS and 0 < args.max_bytes <= MAX_BYTES,
            "invalid_budget", "Resource overrides may only reduce the common resource envelope.")
    args.artifacts = args.artifacts or args.ac_root / "dogfood" / ("stdo-v3-i5-" + args.tenant) / "artifacts"
    args.graph = args.graph or args.ac_root / "graphify-out/v3-i5" / args.tenant / "graph.json"
    if args.condition == "graphify":
        parser.error("--upstream is required for actual Graphify assistance") if args.upstream is None else None
    return args


def main(argv: list[str] | None = None) -> int:
    try:
        server = Server(arguments(argv))
        server.serve(sys.stdin.buffer, sys.stdout.buffer)
        return 0
    except Exception as exc:
        print(f"ac_study infrastructure failure: {type(exc).__name__}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
