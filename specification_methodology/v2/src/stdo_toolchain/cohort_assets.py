"""Shared exact-cohort semantic asset integrity checks.

Extracted from the existing stack release checker so released asset closure has
one executable owner for publication qualification and consumer update planning.
"""
from __future__ import annotations

import hashlib
import json
import re
from typing import Any, Iterable, Protocol

STDO_URI = re.compile(r"stdo://releases/(v\d+\.\d+\.\d+-rc\.[1-9]\d*)/")

class View(Protocol):
    def exists(self, relative: str) -> bool: ...
    def read_bytes(self, relative: str) -> bytes: ...
    def read_json(self, relative: str) -> Any: ...

def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()

def canonical_value_sha256(value: Any) -> str:
    return sha256(json.dumps(value, ensure_ascii=False, allow_nan=False,
                             separators=(",", ":"), sort_keys=True).encode("utf-8"))

def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)

def read_json(view: View, relative: str, failures: list[str]) -> Any | None:
    if not view.exists(relative):
        failures.append(f"missing JSON asset: {relative}")
        return None
    try:
        return view.read_json(relative)
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"invalid JSON asset {relative}: {exc}")
        return None

def normalize_version(value: str) -> str:
    return value[1:] if value.startswith("v") else value

def iter_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for member in value:
            yield from iter_strings(member)
    elif isinstance(value, dict):
        for member in value.values():
            yield from iter_strings(member)


def validate_source_routes(
    payload: Any, cut: str, label: str, failures: list[str]
) -> None:
    for value in iter_strings(payload):
        for matched in STDO_URI.findall(value):
            require(
                matched == cut,
                f"{label}: cross-cut STDO URI {matched}; expected {cut}",
                failures,
            )


def resolved_source_path(uri: str, source_uri: str) -> str | None:
    prefix = f"{source_uri}standards/"
    if not uri.startswith(prefix):
        return None
    return uri[len(prefix) :].split("#", 1)[0]


def validate_semantic_index(
    view: View,
    manifest: dict[str, Any],
    standards: list[dict[str, str]],
    failures: list[str],
) -> None:
    asset = manifest["assets"]["stdo_semantic_index"]
    root = asset["root"].rstrip("/")
    paths = {
        key: f"{root}/{asset[key]}"
        for key in ("source_corpus", "program", "map", "validation_report")
    }
    payloads = {key: read_json(view, path, failures) for key, path in paths.items()}
    if any(value is None for value in payloads.values()):
        return

    version = manifest["cohort"]["version"]
    cut = manifest["cohort"]["cut"]
    source_uri = f"stdo://releases/{cut}/"
    source_basis = f"{source_uri}standards/"
    product = manifest["products"]["specification_methodology"]
    freeze = product["freeze"]
    source = payloads["source_corpus"]
    require(
        source.get("kind") == "stdo-representation.source-corpus",
        "semantic source-corpus kind mismatch",
        failures,
    )
    require(
        normalize_version(str(source.get("representation_version", ""))) == version,
        "semantic source-corpus version mismatch",
        failures,
    )
    release = source.get("source_release", {})
    expected_release = {
        "cut": cut,
        "uri": source_uri,
        "qualified_ref": product["release_ref"],
        "tag_object": freeze["tag_object"],
        "commit": freeze["commit"],
        "tree": freeze["tree"],
        "project_subtree_root": product["subtree"],
        "project_subtree_tree": freeze["project_subtree_tree"],
        "standards_tree": freeze["standards_tree"],
        "installed_manifest_sha256": freeze["installed_manifest_sha256"],
        "standards_member_count": freeze["standards_member_count"],
        "standards_member_set_sha256": freeze["standards_member_set_sha256"],
    }
    for field, expected in expected_release.items():
        require(
            release.get(field) == expected,
            f"semantic source-corpus {field} mismatch",
            failures,
        )
    actual_members = release.get("standards_members")
    require(
        actual_members == standards,
        "semantic source-corpus does not reproduce the exact ordered STDO inventory",
        failures,
    )

    program = payloads["program"]
    constraint_map = payloads["map"]
    report = payloads["validation_report"]
    require(
        program.get("source_basis") == source_basis,
        "program source basis mismatch",
        failures,
    )
    require(
        constraint_map.get("source_basis") == source_basis,
        "constraint-map source basis mismatch",
        failures,
    )
    require(
        f"stdo-v{version}" in str(program.get("uri", "")),
        "program URI does not carry exact cohort version",
        failures,
    )
    require(
        constraint_map.get("program_uri") == program.get("uri"),
        "constraint map points to another program URI",
        failures,
    )
    require(
        report.get("program_uri") == program.get("uri"),
        "validation report points to another program URI",
        failures,
    )
    program_digest = f"sha256:{canonical_value_sha256(program)}"
    require(
        constraint_map.get("program_sha256") == program_digest,
        "constraint map does not bind the canonical program digest",
        failures,
    )
    require(
        report.get("program_sha256") == program_digest,
        "validation report does not bind the canonical program digest",
        failures,
    )
    require(
        constraint_map.get("program_sha256") == report.get("program_sha256"),
        "constraint map and validation report disagree on program digest",
        failures,
    )
    map_without_digest = dict(constraint_map)
    declared_map_digest = map_without_digest.pop("map_sha256", None)
    require(
        declared_map_digest == f"sha256:{canonical_value_sha256(map_without_digest)}",
        "constraint map intrinsic digest mismatch",
        failures,
    )
    require(report.get("status") == "valid", "semantic validation is invalid", failures)
    require(
        report.get("diagnostics") == [], "semantic validation has diagnostics", failures
    )
    for key, payload in payloads.items():
        validate_source_routes(payload, cut, key, failures)

    member_digests = {row["path"]: row["sha256"] for row in standards}
    require(
        constraint_map.get("resolved_sources") == report.get("resolved_sources"),
        "constraint map and validation report resolved-source sets differ",
        failures,
    )
    resolved_uris = {
        row.get("uri")
        for row in report.get("resolved_sources", [])
        if isinstance(row, dict)
    }
    for uri in iter_strings(program):
        relative = resolved_source_path(uri, source_uri)
        if relative:
            require(
                uri in resolved_uris,
                f"program source ref is absent from resolved-source proof: {uri}",
                failures,
            )
    for label, payload in (("map", constraint_map), ("report", report)):
        for row in payload.get("resolved_sources", []):
            uri = row.get("uri", "")
            relative = resolved_source_path(uri, source_uri)
            require(
                relative is not None,
                f"{label}: unbound resolved source {uri}",
                failures,
            )
            if relative is None:
                continue
            require(
                relative in member_digests,
                f"{label}: resolved source is absent from STDO inventory: {relative}",
                failures,
            )
            expected_digest = member_digests.get(relative)
            actual_digest = str(row.get("sha256", "")).removeprefix("sha256:")
            require(
                actual_digest == expected_digest,
                f"{label}: resolved source digest mismatch for {relative}",
                failures,
            )

    note_path = manifest["products"]["stdo_representation"]["release_note"]
    if view.exists(note_path):
        note = view.read_bytes(note_path).decode("utf-8")
        bound_paths = [
            paths["source_corpus"].removeprefix("stdo_representation/"),
            *asset["release_member_paths"],
            paths["validation_report"].removeprefix("stdo_representation/"),
        ]
        for relative in bound_paths:
            repository_path = f"stdo_representation/{relative}"
            require(
                relative in note,
                f"Representation release note does not bind {relative}",
                failures,
            )
            require(
                sha256(view.read_bytes(repository_path)) in note,
                f"Representation release note lacks exact digest for {relative}",
                failures,
            )


