#!/usr/bin/env python3
"""Exercise the tenant against an unchanged, exact upstream Graphify checkout.

This runs the real builder, exporter, loader and local query helper. It neither
installs Graphify nor substitutes mocks for upstream calls. Passing establishes
only the declared mechanical boundary on the supplied conformance fixture.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib
import importlib.metadata
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from collections import Counter
from collections.abc import Iterator, Mapping
from typing import Protocol, cast


UPSTREAM_COMMIT = "fe085cedddde3a18554f8749b230bfe47f3dcce7"
UPSTREAM_VERSION = "0.9.90"
QUALIFICATION_PACKAGES = {"networkx": "3.4.2", "tree-sitter": "0.25.2"}
TENANT_ROOT = Path(__file__).resolve().parents[1]
CODEC = TENANT_ROOT / "code" / "ac_graph.py"


class QualificationError(Exception):
    """A required boundary property could not be established."""


class NodeView(Protocol):
    def __iter__(self) -> Iterator[str]: ...

    def __getitem__(self, key: str) -> Mapping[str, object]: ...


class Graph(Protocol):
    @property
    def nodes(self) -> NodeView: ...

    def number_of_nodes(self) -> int: ...

    def number_of_edges(self) -> int: ...


class BuildAPI(Protocol):
    def build_from_json(
        self, extraction: dict[str, object], *, dedup: bool = True
    ) -> Graph: ...


class ExportAPI(Protocol):
    def to_json(
        self,
        graph: Graph,
        communities: dict[int, list[str]],
        output_path: str,
        *,
        force: bool = False,
        built_at_commit: str | None = None,
    ) -> bool: ...


class PathsAPI(Protocol):
    def load_node_link_graph(self, path_or_data: Path) -> Graph: ...


class QueryAPI(Protocol):
    def _query_graph_text(
        self,
        graph: Graph,
        question: str,
        *,
        mode: str = "bfs",
        depth: int = 3,
        token_budget: int = 2000,
        graph_path: str | None = None,
        seeds: list[str] | None = None,
    ) -> str: ...


class ValidateAPI(Protocol):
    def validate_extraction(self, extraction: dict[str, object]) -> list[str]: ...


def require(condition: bool, message: str) -> None:
    if not condition:
        raise QualificationError(message)


def object_map(value: object, context: str) -> dict[str, object]:
    if not isinstance(value, dict) or not all(isinstance(k, str) for k in value):
        raise QualificationError(f"{context} must be an object with string keys")
    return cast(dict[str, object], value)


def object_list(value: object, context: str) -> list[dict[str, object]]:
    if not isinstance(value, list):
        raise QualificationError(f"{context} must be a list")
    return [object_map(item, context) for item in value]


def load_object(path: Path) -> dict[str, object]:
    raw: object = json.loads(path.read_text(encoding="utf-8"))
    return object_map(raw, str(path))


def write_object(path: Path, value: dict[str, object]) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )


def file_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_process(arguments: list[str], *, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        arguments,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def git(upstream: Path, *arguments: str) -> str:
    result = run_process(["git", "-C", str(upstream), *arguments])
    require(result.returncode == 0, f"upstream Git inspection failed: {result.stderr.strip()}")
    return result.stdout.strip()


def verify_upstream(upstream: Path) -> dict[str, object]:
    require(upstream.is_dir(), f"upstream checkout is missing: {upstream}")
    root = Path(git(upstream, "rev-parse", "--show-toplevel")).resolve()
    require(root == upstream, "--upstream must identify the checkout root")
    head = git(upstream, "rev-parse", "HEAD")
    require(head == UPSTREAM_COMMIT, f"unsupported upstream revision {head}; expected {UPSTREAM_COMMIT}")
    status = git(upstream, "status", "--porcelain=v1", "--untracked-files=all")
    require(not status, "upstream checkout is modified or has untracked files")
    versions: dict[str, object] = {}
    for package, expected in QUALIFICATION_PACKAGES.items():
        try:
            version = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError as exc:
            raise QualificationError(
                f"missing qualification dependency {package}=={expected}; "
                "install test_env/requirements-qualification.txt"
            ) from exc
        require(version == expected, f"qualification dependency {package}=={version}; expected {expected}")
        versions[package] = version
    return {"commit": head, "version": UPSTREAM_VERSION, "clean": True, "packages": versions}


def upstream_module(upstream: Path, name: str) -> object:
    try:
        module = importlib.import_module(name)
    except ModuleNotFoundError as exc:
        raise QualificationError(
            f"actual upstream {name} requires unavailable module {exc.name}; "
            "qualification was not skipped"
        ) from exc
    require(module.__file__ is not None, f"upstream module {name} has no source file")
    source = Path(cast(str, module.__file__)).resolve()
    require(source.is_relative_to(upstream), f"{name} imported from the wrong source: {source}")
    return module


def codec(arguments: list[str], *, refusal: bool = False) -> subprocess.CompletedProcess[str]:
    result = run_process([sys.executable, str(CODEC), *arguments])
    if refusal:
        require(result.returncode != 0, f"codec accepted tampered graph: {' '.join(arguments)}")
        require(bool(result.stderr.strip()), "codec refusal did not explain the failure")
    else:
        require(
            result.returncode == 0,
            f"codec failed ({result.returncode}): {' '.join(arguments)}\n{result.stderr.strip()}",
        )
    return result


def graph_ids(graph: dict[str, object]) -> set[str]:
    nodes = object_list(graph.get("nodes"), "graph.nodes")
    identities: list[str] = []
    for node in nodes:
        identity = node.get("id")
        require(isinstance(identity, str), "graph node has a non-string identity")
        identities.append(cast(str, identity))
    require(len(identities) == len(set(identities)), "graph contains duplicate node identities")
    return set(identities)


def fixture_coverage(model: dict[str, object], graph: dict[str, object]) -> dict[str, object]:
    """Refuse vacuous compatibility claims over a fixture missing edge cases."""
    populations = object_map(model.get("populations"), "model.populations")
    expected_families = {
        "objects", "relations", "constraints", "latitude", "residuals",
        "traversals", "transformations", "judgments",
    }
    require(set(populations) == expected_families, "fixture does not declare all eight record families")
    family_counts: dict[str, object] = {}
    local_ids: set[str] = set()
    for family, population in populations.items():
        records = object_list(population, f"populations.{family}")
        require(bool(records), f"boundary fixture must exercise the {family} family")
        family_counts[family] = len(records)
        for record in records:
            identity = record.get("id")
            require(isinstance(identity, str), "fixture record lacks an identity")
            local_ids.add(cast(str, identity))

    pairs: Counter[tuple[str, str]] = Counter()
    for relation in object_list(populations["relations"], "relations"):
        source, target = relation.get("source"), relation.get("target")
        require(isinstance(source, str) and isinstance(target, str), "relation endpoints must be exact identities")
        pairs[(cast(str, source), cast(str, target))] += 1
    require(any(count > 1 for count in pairs.values()), "fixture has no distinct parallel relations")
    require(any(a != b and (b, a) in pairs for a, b in pairs), "fixture has no reversed relations")
    require(any(a == b for a, b in pairs), "fixture has no self-relation")

    roles: Counter[str] = Counter()
    record_ids: set[str] = set()
    repeated: Counter[tuple[str, str, tuple[str, ...]]] = Counter()
    for node in object_list(graph.get("nodes"), "graph.nodes"):
        role = node.get("ac_role")
        require(isinstance(role, str), "materialized graph node lacks an ac_role")
        roles[cast(str, role)] += 1
        payload = object_map(node.get("ac_payload"), "ac_payload")
        if role == "record":
            record = object_map(payload.get("record"), "record payload")
            record_id = record.get("id")
            require(isinstance(record_id, str), "record node lacks its semantic identity")
            record_ids.add(cast(str, record_id))
        elif role == "reference-occurrence":
            owner, target, path = payload.get("owner"), payload.get("target"), payload.get("path")
            require(isinstance(owner, str) and isinstance(target, str), "occurrence lacks exact owner/target identities")
            require(isinstance(path, list) and bool(path), "occurrence lacks its field path")
            field_path = cast(list[object], path)
            require(all(isinstance(part, str) for part in field_path), "occurrence path has a non-string component")
            exact_path = cast(list[str], field_path)
            if exact_path[-1].isdigit():
                repeated[(cast(str, owner), cast(str, target), tuple(exact_path[:-1]))] += 1
    require(record_ids == local_ids, "materialized record identities do not match exact fixture populations")
    require(roles["record"] == len(local_ids), "materialization merged or duplicated local records")
    require(any(count > 1 for count in repeated.values()), "fixture has no repeated ordered reference target")
    return {
        "family_counts": family_counts,
        "node_roles": dict(sorted(roles.items())),
        "parallel_relations": True,
        "reversed_relations": True,
        "self_relation": True,
        "repeated_ordered_references": True,
    }


def tamper_trials(graph: dict[str, object], temporary: Path) -> list[str]:
    """Corrupt actual upstream output and require explicit decoder refusal."""
    checks: list[str] = []
    nodes = object_list(graph.get("nodes"), "exported nodes")
    occurrences = [node for node in nodes if node.get("ac_role") == "reference-occurrence"]
    records = [node for node in nodes if node.get("ac_role") == "record"]
    require(bool(occurrences) and bool(records), "tamper trials need records and occurrences")
    victim_id = occurrences[0]["id"]
    missing = copy.deepcopy(graph)
    missing["nodes"] = [node for node in nodes if node["id"] != victim_id]
    missing["links"] = [
        link for link in object_list(graph.get("links"), "exported links")
        if link.get("source") != victim_id and link.get("target") != victim_id
    ]
    missing_path = temporary / "missing-occurrence.json"
    write_object(missing_path, missing)
    codec(["decode", str(missing_path), "--out", str(temporary / "must-not-recover-1.json")], refusal=True)
    checks.append("decoder refuses removal of an occurrence and both incident edges from actual upstream output")

    changed = copy.deepcopy(graph)
    record_node = next(node for node in object_list(changed["nodes"], "nodes") if node.get("ac_role") == "record")
    payload = object_map(record_node["ac_payload"], "record payload")
    record = object_map(payload["record"], "record")
    record["id"] = "urn:a-c:qualification:tampered-record"
    changed_path = temporary / "changed-record.json"
    write_object(changed_path, changed)
    codec(["decode", str(changed_path), "--out", str(temporary / "must-not-recover-2.json")], refusal=True)
    checks.append("decoder refuses a changed semantic record in actual upstream output")

    reversed_graph = copy.deepcopy(graph)
    occurrence = next(
        object_map(node["ac_payload"], "occurrence payload")
        for node in object_list(reversed_graph["nodes"], "nodes")
        if node.get("ac_role") == "reference-occurrence"
        and object_map(node["ac_payload"], "occurrence payload").get("owner")
        != object_map(node["ac_payload"], "occurrence payload").get("target")
    )
    # The carrier is an undirected graph: the owner/target occurrence payload
    # carries semantic direction, while storage edge order is incidental.
    occurrence["owner"], occurrence["target"] = occurrence["target"], occurrence["owner"]
    reversed_path = temporary / "reversed-semantic-occurrence.json"
    write_object(reversed_path, reversed_graph)
    codec(["decode", str(reversed_path), "--out", str(temporary / "must-not-recover-3.json")], refusal=True)
    checks.append("decoder refuses reversed semantic owner/target roles in actual upstream output")

    changed_index = copy.deepcopy(graph)
    indexed_node = next(node for node in object_list(changed_index["nodes"], "nodes") if node.get("ac_role") == "record")
    attributes = object_map(indexed_node.get("attributes"), "native search attributes")
    attributes["semantic_identity"] = "urn:a-c:qualification:misleading-search-identity"
    changed_index_path = temporary / "changed-native-search-attributes.json"
    write_object(changed_index_path, changed_index)
    codec(["decode", str(changed_index_path), "--out", str(temporary / "must-not-recover-4.json")], refusal=True)
    checks.append("decoder refuses altered derived native-search attributes without a model change")
    return checks


def qualification(
    upstream: Path, fixture: Path, discovery_query: str, expected_record: str
) -> dict[str, object]:
    upstream_evidence = verify_upstream(upstream)
    require(CODEC.is_file(), f"tenant codec is missing: {CODEC}")
    require(fixture.is_file(), f"conformance fixture is missing: {fixture}")
    fixture_digest = file_digest(fixture)
    codec_digest = file_digest(CODEC)
    sys.path.insert(0, str(upstream))
    builder = cast(BuildAPI, upstream_module(upstream, "graphify.build"))
    exporter = cast(ExportAPI, upstream_module(upstream, "graphify.export"))
    loader = cast(PathsAPI, upstream_module(upstream, "graphify.paths"))
    query = cast(QueryAPI, upstream_module(upstream, "graphify.serve"))
    validator = cast(ValidateAPI, upstream_module(upstream, "graphify.validate"))
    upstream_sources: dict[str, object] = {}
    for name in ("build", "export", "paths", "serve", "validate"):
        relative = f"graphify/{name}.py"
        require(git(upstream, "ls-files", "--error-unmatch", "--", relative) == relative, f"untracked upstream module: {relative}")
        upstream_sources[relative] = file_digest(upstream / relative)
    upstream_evidence["entrypoint_sha256"] = upstream_sources
    checks: list[str] = []
    original_model = load_object(fixture)
    populations = object_map(original_model.get("populations"), "populations")
    expected_records = [
        record
        for population in populations.values()
        for record in object_list(population, "population")
        if record.get("id") == expected_record
    ]
    require(len(expected_records) == 1, "native query expectation must identify exactly one authored record")
    require(
        bool(discovery_query.strip())
        and discovery_query.lower() in json.dumps(expected_records[0], ensure_ascii=False).lower(),
        "native discovery query must occur in the expected authored record",
    )

    with tempfile.TemporaryDirectory(prefix="ac-graphify-qualification-") as directory:
        temporary = Path(directory)
        materialized = temporary / "proposal.json"
        exported = temporary / "upstream.json"
        recovered = temporary / "recovered.json"
        codec(["validate", str(fixture)])
        codec(["materialize", str(fixture), "--out", str(materialized)])
        proposal = load_object(materialized)
        coverage = fixture_coverage(original_model, proposal)
        expected_ids = graph_ids(proposal)
        links = object_list(proposal.get("links", proposal.get("edges")), "graph links")
        errors = validator.validate_extraction(copy.deepcopy(proposal))
        require(not errors, f"materialized extraction violates actual upstream schema: {errors}")
        built = builder.build_from_json(copy.deepcopy(proposal), dedup=False)
        require(set(built.nodes) == expected_ids, "actual upstream builder rekeyed, merged or discarded semantic nodes")
        require(
            built.number_of_edges() == len(links),
            f"actual upstream builder kept {built.number_of_edges()} edges from {len(links)} declared links; "
            "occurrence edge roles were merged or discarded",
        )
        checks.append("actual builder preserves all node identities and occurrence edges with dedup=False")
        require(
            exporter.to_json(built, {}, str(exported), built_at_commit=UPSTREAM_COMMIT),
            "actual upstream exporter refused to write a fresh graph",
        )
        persisted = load_object(exported)
        exported_digest = file_digest(exported)
        require(graph_ids(persisted) == expected_ids, "actual upstream exporter changed semantic node identities")
        loaded = loader.load_node_link_graph(exported)
        require(set(loaded.nodes) == expected_ids, "actual upstream loader changed semantic node identities")
        require(loaded.number_of_edges() == len(links), "actual upstream loader changed occurrence edge count")
        checks.append("actual export and path loader preserve node identities and occurrence edge count")
        codec(["decode", str(exported), "--out", str(recovered)])
        require(load_object(recovered) == original_model, "upstream build/export/decode changed the declared model")
        checks.append("tenant decoder recovers the exact declared model after actual upstream processing")
        checks.extend(tamper_trials(persisted, temporary))

        # Explicit seeds exercise actual upstream resolution, traversal and text
        # rendering without treating their bounded output as governing closure.
        seed = next(
            cast(str, node["id"])
            for node in object_list(proposal["nodes"], "nodes")
            if node.get("ac_role") == "record"
        )
        label = loaded.nodes[seed].get("label")
        require(isinstance(label, str) and bool(label), "query seed has no label")
        query_text = query._query_graph_text(
            loaded,
            cast(str, label),
            mode="bfs",
            depth=2,
            token_budget=2000,
            graph_path=str(exported),
            seeds=[seed],
        )
        require("Traversal: BFS" in query_text, "actual upstream query did not traverse the graph")
        require(cast(str, label) in query_text, "actual upstream query did not retain its exact seed")
        require("NODE " in query_text, "actual upstream query returned no node context")
        checks.append("actual local query helper resolves an exact seed and renders graph context")

        # Depth zero permits only ranked search seeds, preventing unrelated
        # traversal or a metadata hub from accidentally satisfying the trial.
        discovery_text = query._query_graph_text(
            loaded,
            discovery_query,
            mode="bfs",
            depth=0,
            token_budget=2000,
            graph_path=str(exported),
        )
        require(
            any(line.startswith("NODE ") and expected_record in line for line in discovery_text.splitlines()),
            "actual unseeded Graphify search did not retrieve the expected authored semantic record",
        )
        checks.append("actual unseeded local query retrieves the expected semantic record from authored wording at depth zero")

    require(file_digest(fixture) == fixture_digest, "conformance fixture changed during qualification")
    require(file_digest(CODEC) == codec_digest, "tenant codec changed during qualification; rerun on a frozen candidate")
    verify_upstream(upstream)
    return {
        "status": "passed",
        "claim": "bounded actual-upstream representation compatibility; no semantic admission or efficiency claim",
        "upstream": upstream_evidence,
        "fixture": {"path": str(fixture), "sha256": fixture_digest},
        "codec_sha256": codec_digest,
        "qualification_script_sha256": file_digest(Path(__file__).resolve()),
        "python_version": sys.version.split()[0],
        "exported_graph_sha256": exported_digest,
        "coverage": coverage,
        "nodes": len(expected_ids),
        "edges": len(links),
        "checks": checks,
        "query_excerpt": query_text[:1800],
        "query_characters": len(query_text),
        "query_sha256": hashlib.sha256(query_text.encode("utf-8")).hexdigest(),
        "native_discovery": {
            "query": discovery_query,
            "expected_record": expected_record,
            "scope": {"mode": "bfs", "depth": 0, "token_budget": 2000, "explicit_seeds": False},
            "characters": len(discovery_text),
            "excerpt": discovery_text[:2400],
            "sha256": hashlib.sha256(discovery_text.encode("utf-8")).hexdigest(),
            "claim": "fixture retrieval only; no implication, governing closure, semantic acceptance or efficiency proof",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream", required=True, type=Path, help="unchanged checkout at the exact supported commit")
    parser.add_argument("--fixture", type=Path, default=TENANT_ROOT / "test_env" / "fixtures" / "toy_model.json")
    parser.add_argument("--query", default="unresolved reading", help="authored wording for actual unseeded native search")
    parser.add_argument("--expect-record", default="urn:a-c:toy:object:a", help="semantic record identity expected from native search")
    parser.add_argument("--out", type=Path, help="optional JSON report path")
    arguments = parser.parse_args()
    try:
        report = qualification(
            arguments.upstream.resolve(), arguments.fixture.resolve(),
            arguments.query, arguments.expect_record,
        )
        exit_code = 0
    except Exception as exc:
        report = {"status": "failed", "error": f"{type(exc).__name__}: {exc}"}
        exit_code = 1
    rendered = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if arguments.out is not None:
        arguments.out.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
