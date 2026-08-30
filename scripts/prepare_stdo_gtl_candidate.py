#!/usr/bin/env python3
"""Replay preparation only for the exact historical first STDO.gtl basis."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import tarfile
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "build_tenants" / "gtl" / "representation" / "selection-policy.json"
PROFILE = ROOT / "build_tenants" / "gtl" / "design" / "GTL_REPRESENTATION_PROFILE.md"
FRAME_BASIS = ROOT / "specification" / "REFERENCE_FRAME_BASIS.md"
CODE = ROOT / "build_tenants" / "gtl" / "code"
DEFAULT_OUTPUT = (
    ROOT / "build_tenants" / "gtl" / "representation" / "candidates" / "stdo-2.4.3-rc.3"
)
SOURCE_URI = "stdo://releases/v2.4.3-rc.3/"
SOURCE_MANIFEST_SHA = "312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551"
SOURCE_MEMBER_SET = "127a6fb213eb5e12bcf6180cb73016a003ccfda80651b476055f19a22ca10275"
PROFILE_IDENTITY = "urn:stdo-representation:gtl-profile:stdo-gtl:0.7.0"
FRAME_BASIS_IDENTITY = "urn:stdo-representation:reference-frame-basis:source-project:3"
HISTORICAL_WHAT_MEMBER_SET_IDENTITY = (
    "sha256:4158caca78aeadd4dd31e802f9801ee2b81e0f1a96fc2774705db909d3bbf35e"
)
HISTORICAL_PROFILE_SHA256 = (
    "sha256:27b496722bfea537ed9e3a8c412c3ca162f83e723ecd9b783e1697d8ffae5f47"
)
HISTORICAL_FRAME_BASIS_SHA256 = (
    "sha256:b589485673b72536c222c9cd52b8f36ac250533a1eaaee4d0303754788045ec0"
)
BUILD_TENANT_IDENTITY = "urn:stdo-representation:build-tenant:gtl"
F_H = "urn:stdo:concept:graph-native-odd:f-h"
AGGREGATE_MEMBER = "authority_compressions/stdo_compressed.md"
BASELINE_MEMBER = "STDO_REFERENCE_FRAME_BASELINE.md"
GLOBAL_CONTEXT = "urn:stdo:bounded-context:method-identity"
GLOBAL_SCOPE = f"{SOURCE_URI}standards/"
FRAME_FAMILIES = (
    "Product",
    "Design",
    "Design Component",
    "Public Boundary",
    "Entity",
    "Operator",
    "Owner",
    "Effect",
    "Reuse/Foundation",
    "Install",
    "Proof",
)
ENGAGEMENT_ROLES = ("Executive", "Worker", "Reviewer")
FRAME_AUTHORITIES = (
    "./specification/GOALS.md",
    "./specification/PRODUCT.md#product-authority",
    "./specification/requirements/REQ-P-BASIS-AND-IDENTITY.md",
    "./specification/requirements/REQ-P-COMPRESSION-VERIFICATION.md",
    "./specification/requirements/REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md",
    "./specification/requirements/REQ-P-FP-CONSUMPTION.md",
    "./specification/requirements/REQ-P-REPRESENTATION-ALGEBRA.md",
    "./specification/requirements/REQ-P-SELECTION-AND-ACCEPTANCE.md",
)


class PreparationFailure(RuntimeError):
    """The candidate cannot be prepared from the exact selected bases."""


def require_historical_preparation_basis(
    current_what: str, profile_sha: str, frame_sha: str
) -> None:
    observed = (current_what, profile_sha, frame_sha)
    expected = (
        HISTORICAL_WHAT_MEMBER_SET_IDENTITY,
        HISTORICAL_PROFILE_SHA256,
        HISTORICAL_FRAME_BASIS_SHA256,
    )
    if observed != expected:
        raise PreparationFailure(
            "legacy preparer is historical-only; active WHAT requires an immutable "
            "F_P[v_compile] Semantic Compilation Candidate and a new digest-qualified "
            "candidate coordinate"
        )


def run(argv: list[str], *, cwd: Path, capture: bool = False) -> str:
    completed = subprocess.run(
        argv,
        cwd=cwd,
        check=False,
        text=True,
        capture_output=capture,
    )
    if completed.returncode != 0:
        detail = completed.stderr if capture else "see command output above"
        raise PreparationFailure(f"{' '.join(argv)} failed: {detail}")
    return completed.stdout if capture else ""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def write_canonical(path: Path, value: Any) -> None:
    path.write_bytes(canonical_bytes(value))


def write_pretty(path: Path, value: Any) -> None:
    path.write_bytes(pretty_bytes(value))


def pretty_bytes(value: Any) -> bytes:
    return (
        f"{json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True)}\n".encode(
            "utf-8"
        )
    )


def slug(value: str) -> str:
    result = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not result:
        raise PreparationFailure(f"cannot derive a local key from {value!r}")
    return result


def selected_store(configured: Path | None) -> Path:
    if configured is not None:
        return configured.expanduser().resolve()
    override = os.environ.get("STDO_STORE")
    if override:
        return Path(override).expanduser().resolve()
    return (Path.home() / "Library" / "Application Support" / "STDO").resolve()


def load_source(
    store: Path,
) -> tuple[Path, dict[str, Any], bytes, dict[str, str]]:
    release = store / "releases" / "v2.4.3-rc.3"
    manifest_path = release / "manifest.json"
    manifest_bytes = manifest_path.read_bytes()
    if sha256(manifest_bytes) != SOURCE_MANIFEST_SHA:
        raise PreparationFailure("installed Source STDO manifest digest differs")
    manifest = json.loads(manifest_bytes)
    members = manifest["standards"]["members"]
    if (
        manifest["standards"]["member_count"] != 47
        or manifest["standards"]["member_set_sha256"] != SOURCE_MEMBER_SET
        or len(members) != 47
    ):
        raise PreparationFailure("installed Source STDO inventory differs")
    digests: dict[str, str] = {}
    for row in members:
        path = release / "standards" / row["path"]
        observed = sha256(path.read_bytes())
        if observed != row["sha256"]:
            raise PreparationFailure(f"Source STDO member differs: {row['path']}")
        digests[row["path"]] = f"sha256:{observed}"
    return release, manifest, manifest_bytes, digests


def what_identity() -> str:
    specification = ROOT / "specification"
    members = [specification / "INTENT.md", specification / "PRODUCT.md"]
    members.extend(sorted((specification / "requirements").glob("REQ-P-*.md")))
    digest = hashlib.sha256()
    for path in members:
        relative = path.relative_to(specification).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(sha256(path.read_bytes()).encode("ascii"))
        digest.update(b"\n")
    return f"sha256:{digest.hexdigest()}"


def source_uri(member: str, fragment: str | None = None) -> str:
    value = f"{SOURCE_URI}standards/{member}"
    return value if fragment is None else f"{value}#{fragment}"


def locator(
    digests: dict[str, str], member: str, fragment: str | None
) -> dict[str, Any]:
    return {
        "basis_uri": SOURCE_URI,
        "member_path": member,
        "member_sha256": digests[member],
        "fragment": fragment,
    }


def generated_source_key(primary: dict[str, Any], local_key: str) -> str:
    preimage = {
        "primary_source_locator": primary,
        "local_declaration_key": local_key,
    }
    return (
        "urn:stdo-representation:source-key:sha256:"
        f"{sha256(canonical_bytes(preimage))}"
    )


def address(
    source_key: str,
    term: str,
    context: str,
    authority: str,
    scope: str,
) -> dict[str, Any]:
    return {
        "source_key": source_key,
        "term": term,
        "bounded_context": context,
        "owning_authority": authority,
        "selected_basis": {
            "release_uri": SOURCE_URI,
            "installed_manifest_sha256": f"sha256:{SOURCE_MANIFEST_SHA}",
        },
        "governed_scope": scope,
    }


def record_identity(kind: str, semantic_address: dict[str, Any]) -> str:
    coordinate = {"record_kind": kind, "semantic_address": semantic_address}
    return (
        f"urn:stdo-representation:{kind}:sha256:"
        f"{sha256(canonical_bytes(coordinate))}"
    )


def parse_aggregate(path: Path) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = defaultdict(list)
    current: str | None = None
    active: list[str] | None = None
    in_frontmatter = False
    frontmatter_seen = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw == "---" and not frontmatter_seen:
            in_frontmatter = True
            frontmatter_seen = True
            continue
        if raw == "---" and in_frontmatter:
            in_frontmatter = False
            continue
        if in_frontmatter:
            continue
        if raw.startswith("## "):
            if current is not None and active is not None:
                sections[current].append(" ".join(active))
            current = raw[3:].strip()
            sections.setdefault(current, [])
            active = None
            continue
        if current is None:
            continue
        if raw.startswith("- "):
            if active is not None:
                sections[current].append(" ".join(active))
            active = [raw[2:].strip()]
        elif active is not None and raw.strip():
            active.append(raw.strip())
    if current is not None and active is not None:
        sections[current].append(" ".join(active))
    return dict(sections)


def constraint_class(default: str, statement: str) -> str:
    lowered = statement.casefold()
    if any(term in lowered for term in ("must not", "cannot ", "do not ")):
        return "prohibition"
    if any(term in lowered for term in ("fail closed", "refuse", "invalid")):
        return "refusal"
    if any(term in lowered for term in ("must ", "requires ", "shall ")):
        return "obligation"
    return default


def prepare_records(
    release: Path,
    manifest: dict[str, Any],
    digests: dict[str, str],
    policy: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, str], list[dict[str, Any]], dict[str, Any],]:
    records: list[dict[str, Any]] = []
    reasons: dict[str, str] = {}
    generated: dict[str, dict[str, Any]] = {}
    ids: dict[str, str] = {}
    frame_route_refs: dict[str, set[str]] = defaultdict(set)
    role_route_refs: dict[str, set[str]] = defaultdict(set)

    def add_record(
        kind: str,
        semantic_address: dict[str, Any],
        fields: dict[str, Any],
        locators: list[dict[str, Any]],
        reason: str,
        generated_binding: tuple[dict[str, Any], str] | None = None,
        name: str | None = None,
    ) -> str:
        identity = record_identity(kind, semantic_address)
        if any(row["id"] == identity for row in records):
            raise PreparationFailure(f"duplicate record identity {identity}")
        row = {"kind": kind, "id": identity, **fields}
        row["semantic_address"] = semantic_address
        row["source_locators"] = sorted(
            locators,
            key=lambda item: (
                item["member_path"],
                item["fragment"] or "",
                item["member_sha256"],
            ),
        )
        records.append(row)
        reasons[identity] = reason
        if generated_binding is not None:
            primary, local_key = generated_binding
            source_key = semantic_address["source_key"]
            generated[source_key] = {
                "source_key": source_key,
                "primary_source_locator": primary,
                "local_declaration_key": local_key,
            }
        if name is not None:
            ids[name] = identity
        return identity

    aggregate_authority = source_uri(AGGREGATE_MEMBER)
    aggregate_locator = locator(digests, AGGREGATE_MEMBER, None)
    basis_address = address(
        SOURCE_URI,
        "Source STDO v2.4.3-rc.3",
        GLOBAL_CONTEXT,
        aggregate_authority,
        GLOBAL_SCOPE,
    )
    basis_id = add_record(
        "atom",
        basis_address,
        {"atom_class": "basis", "label": "Source STDO v2.4.3-rc.3"},
        [aggregate_locator],
        "Retains the exact immutable Source STDO basis selected by the Product.",
        name="basis",
    )

    context_members = {
        section["bounded_context"]: section["authority_member"]
        for section in policy["sections"].values()
    }
    for context, member in sorted(context_members.items()):
        location = locator(digests, member, None)
        semantic_address = address(
            context,
            context.rsplit(":", 1)[-1].replace("-", " ").title(),
            context,
            source_uri(member),
            GLOBAL_SCOPE,
        )
        add_record(
            "atom",
            semantic_address,
            {
                "atom_class": "bounded_context",
                "label": semantic_address["term"],
            },
            [location],
            "Retains an exact Source STDO bounded-context identity required for semantic isolation.",
            name=f"context:{context}",
        )

    authority_members = sorted(
        {section["authority_member"] for section in policy["sections"].values()}
        | {AGGREGATE_MEMBER}
    )
    for member in authority_members:
        authority = source_uri(member)
        semantic_address = address(
            authority,
            Path(member).stem.replace("_", " ").title(),
            GLOBAL_CONTEXT,
            authority,
            GLOBAL_SCOPE,
        )
        add_record(
            "atom",
            semantic_address,
            {"atom_class": "authority", "label": semantic_address["term"]},
            [locator(digests, member, None)],
            "Retains the exact Source STDO authority carrier used by represented declarations.",
            name=f"authority:{member}",
        )

    document_ids: dict[str, str] = {}
    for member in manifest["standards"]["members"]:
        member_path = member["path"]
        member_uri = source_uri(member_path)
        semantic_address = address(
            member_uri,
            member_path,
            GLOBAL_CONTEXT,
            member_uri,
            GLOBAL_SCOPE,
        )
        document_ids[member_path] = add_record(
            "atom",
            semantic_address,
            {"atom_class": "document", "label": member_path},
            [locator(digests, member_path, None)],
            "Retains the exact installed member identity and source re-entry route; this route atom does not restate or replace the member's law.",
        )

    relation_kinds: dict[str, str] = {}
    relation_location = locator(digests, AGGREGATE_MEMBER, "authority-flow")
    for relation in ("composed_of", "declared_by", "member_of", "part_of", "precedes"):
        local_key = f"relation-kind:{relation}"
        source_key = generated_source_key(relation_location, local_key)
        semantic_address = address(
            source_key,
            relation,
            GLOBAL_CONTEXT,
            aggregate_authority,
            source_uri(AGGREGATE_MEMBER, "authority-flow"),
        )
        relation_kinds[relation] = add_record(
            "atom",
            semantic_address,
            {"atom_class": "relation_kind", "label": relation},
            [relation_location],
            "Retains a closed structural relation kind explicitly used by the selected STDO graph.",
            generated_binding=(relation_location, local_key),
        )

    membership_context = ids[f"context:{GLOBAL_CONTEXT}"]
    membership_owner = ids[f"authority:{AGGREGATE_MEMBER}"]
    global_scope_location = locator(digests, AGGREGATE_MEMBER, "governing-claim")
    global_scope_key = "scope:complete-standards-member-set"
    global_scope_source = generated_source_key(global_scope_location, global_scope_key)
    global_scope_address = address(
        global_scope_source,
        "Complete Source STDO standards member set",
        GLOBAL_CONTEXT,
        aggregate_authority,
        GLOBAL_SCOPE,
    )
    global_scope_id = add_record(
        "atom",
        global_scope_address,
        {"atom_class": "scope", "label": "Complete standards member set"},
        [global_scope_location],
        "Retains the governed scope of the complete immutable standards member set.",
        generated_binding=(global_scope_location, global_scope_key),
        name="scope:global",
    )

    for member_path, document_id in sorted(document_ids.items()):
        location = locator(digests, member_path, None)
        local_key = f"edge:member-of:{member_path}"
        source_key = generated_source_key(location, local_key)
        semantic_address = address(
            source_key,
            f"{member_path} member of Source STDO v2.4.3-rc.3",
            GLOBAL_CONTEXT,
            source_uri(member_path),
            GLOBAL_SCOPE,
        )
        add_record(
            "edge",
            semantic_address,
            {
                "source_ref": document_id,
                "relation_kind_ref": relation_kinds["member_of"],
                "target_ref": basis_id,
                "context_ref": membership_context,
                "owner_ref": membership_owner,
                "scope_ref": global_scope_id,
                "cross_context": None,
            },
            [location],
            "Retains exact membership of this installed member in the selected immutable Source STDO cut.",
            generated_binding=(location, local_key),
        )

    frame_context = ids["context:urn:stdo:bounded-context:reference-frame-evaluation"]
    frame_owner = ids["authority:REFERENCE_FRAME_METHOD.md"]
    frame_scope_location = locator(
        digests, BASELINE_MEMBER, "derived-generic-specialist-frame-set"
    )
    frame_scope_key = "scope:generic-specialist-frame-set"
    frame_scope_source = generated_source_key(frame_scope_location, frame_scope_key)
    frame_scope_address = address(
        frame_scope_source,
        "Generic specialist-frame set",
        "urn:stdo:bounded-context:reference-frame-evaluation",
        source_uri("REFERENCE_FRAME_METHOD.md"),
        source_uri(BASELINE_MEMBER, "derived-generic-specialist-frame-set"),
    )
    frame_scope_id = add_record(
        "atom",
        frame_scope_address,
        {"atom_class": "scope", "label": "Generic specialist-frame set"},
        [frame_scope_location],
        "Retains the exact governed scope of the Source STDO generic specialist-frame families.",
        generated_binding=(frame_scope_location, frame_scope_key),
        name="scope:frames",
    )

    frame_ids: dict[str, str] = {}
    for family in FRAME_FAMILIES:
        location = locator(
            digests, BASELINE_MEMBER, "derived-generic-specialist-frame-set"
        )
        local_key = f"reference-frame-family:{slug(family)}"
        source_key = generated_source_key(location, local_key)
        semantic_address = address(
            source_key,
            family,
            "urn:stdo:bounded-context:reference-frame-evaluation",
            source_uri("REFERENCE_FRAME_METHOD.md"),
            source_uri(BASELINE_MEMBER, "derived-generic-specialist-frame-set"),
        )
        frame_ids[family] = add_record(
            "atom",
            semantic_address,
            {"atom_class": "reference_frame", "label": family},
            [location],
            "Retains one Source STDO generic specialist-frame family for role-bound context projection.",
            generated_binding=(location, local_key),
        )

    role_ids: dict[str, str] = {}
    for role in ENGAGEMENT_ROLES:
        fragment = role.lower()
        role_uri = source_uri(BASELINE_MEMBER, fragment)
        semantic_address = address(
            role_uri,
            role,
            "urn:stdo:bounded-context:reference-frame-evaluation",
            source_uri("REFERENCE_FRAME_METHOD.md"),
            source_uri(BASELINE_MEMBER, fragment),
        )
        role_ids[role] = add_record(
            "atom",
            semantic_address,
            {"atom_class": "role", "label": role},
            [locator(digests, BASELINE_MEMBER, fragment)],
            "Retains one exact Source STDO engagement-role declaration for authorized context assignment.",
        )

    for label, target in {**frame_ids, **role_ids}.items():
        fragment = (
            label.lower()
            if label in ENGAGEMENT_ROLES
            else "derived-generic-specialist-frame-set"
        )
        location = locator(digests, BASELINE_MEMBER, fragment)
        local_key = f"edge:declared-by:{slug(label)}"
        source_key = generated_source_key(location, local_key)
        semantic_address = address(
            source_key,
            f"{label} declared by the Source STDO frame baseline",
            "urn:stdo:bounded-context:reference-frame-evaluation",
            source_uri("REFERENCE_FRAME_METHOD.md"),
            source_uri(BASELINE_MEMBER, fragment),
        )
        add_record(
            "edge",
            semantic_address,
            {
                "source_ref": target,
                "relation_kind_ref": relation_kinds["declared_by"],
                "target_ref": document_ids[BASELINE_MEMBER],
                "context_ref": frame_context,
                "owner_ref": frame_owner,
                "scope_ref": frame_scope_id,
                "cross_context": None,
            },
            [location],
            "Retains the declared Source STDO frame or engagement-role ownership route.",
            generated_binding=(location, local_key),
        )

    method_location = locator(digests, AGGREGATE_MEMBER, "method-identity")
    method_scope_key = "scope:stdo-method-identity"
    method_scope_source = generated_source_key(method_location, method_scope_key)
    method_scope_address = address(
        method_scope_source,
        "STDO method identity",
        GLOBAL_CONTEXT,
        source_uri("SPEC_METHOD.md"),
        source_uri(AGGREGATE_MEMBER, "method-identity"),
    )
    method_scope_id = add_record(
        "atom",
        method_scope_address,
        {"atom_class": "scope", "label": "STDO method identity"},
        [method_location],
        "Retains the declared scope of the four STDO method pillars.",
        generated_binding=(method_location, method_scope_key),
        name="scope:method",
    )
    pillar_members = {
        "Specification": "SPEC_METHOD.md",
        "Ticketing": "TICKET_METHOD.md",
        "Design": "DESIGN_MODULE_METHOD.md",
        "Outcome-Driven Development": "ODD_METHOD.md",
    }
    stdo_key = "concept:stdo"
    stdo_source = generated_source_key(method_location, stdo_key)
    stdo_address = address(
        stdo_source,
        "STDO",
        GLOBAL_CONTEXT,
        source_uri("SPEC_METHOD.md"),
        source_uri(AGGREGATE_MEMBER, "method-identity"),
    )
    stdo_id = add_record(
        "atom",
        stdo_address,
        {"atom_class": "concept", "label": "STDO"},
        [method_location],
        "Retains the exact STDO shorthand and its four-pillar composition.",
        generated_binding=(method_location, stdo_key),
    )
    for pillar, member in pillar_members.items():
        pillar_uri = source_uri(member)
        pillar_address = address(
            pillar_uri,
            pillar,
            GLOBAL_CONTEXT,
            pillar_uri,
            source_uri(AGGREGATE_MEMBER, "method-identity"),
        )
        pillar_id = add_record(
            "atom",
            pillar_address,
            {"atom_class": "method", "label": pillar},
            [method_location, locator(digests, member, None)],
            "Retains one exact STDO method pillar and its owning Source STDO member.",
        )
        local_key = f"edge:stdo-composed-of:{slug(pillar)}"
        source_key = generated_source_key(method_location, local_key)
        edge_address = address(
            source_key,
            f"STDO composed of {pillar}",
            GLOBAL_CONTEXT,
            source_uri("SPEC_METHOD.md"),
            source_uri(AGGREGATE_MEMBER, "method-identity"),
        )
        add_record(
            "edge",
            edge_address,
            {
                "source_ref": stdo_id,
                "relation_kind_ref": relation_kinds["composed_of"],
                "target_ref": pillar_id,
                "context_ref": membership_context,
                "owner_ref": ids["authority:SPEC_METHOD.md"],
                "scope_ref": method_scope_id,
                "cross_context": None,
            },
            [method_location],
            "Retains the exact four-pillar composition declared by STDO method identity.",
            generated_binding=(method_location, local_key),
        )

    flow_layers = (
        ("Goals", "intent"),
        ("Intent", "intent"),
        ("Product Definition", "product_definition"),
        ("Requirements", "requirement"),
        ("Design", "design"),
        ("Code", "design"),
        ("Events", "evidence"),
        ("Projection", "evidence"),
        ("Delta", "evidence"),
        ("Scenarios", "evidence"),
        ("Gap Analysis", "evidence"),
        ("Repricing", "state"),
    )
    flow_location = locator(digests, AGGREGATE_MEMBER, "authority-flow")
    flow_scope_key = "scope:authority-flow-graph"
    flow_scope_source = generated_source_key(flow_location, flow_scope_key)
    flow_scope_address = address(
        flow_scope_source,
        "STDO authority flow",
        "urn:stdo:bounded-context:recursive-product-taxonomy",
        source_uri("SPEC_METHOD.md"),
        source_uri(AGGREGATE_MEMBER, "authority-flow"),
    )
    flow_scope_id = add_record(
        "atom",
        flow_scope_address,
        {"atom_class": "scope", "label": "STDO authority flow"},
        [flow_location],
        "Retains the governed scope of STDO's smallest-owner authority flow.",
        generated_binding=(flow_location, flow_scope_key),
        name="scope:flow",
    )
    flow_ids: list[tuple[str, str]] = []
    for label, atom_class in flow_layers:
        local_key = f"authority-layer:{slug(label)}"
        source_key = generated_source_key(flow_location, local_key)
        layer_address = address(
            source_key,
            label,
            "urn:stdo:bounded-context:recursive-product-taxonomy",
            source_uri("SPEC_METHOD.md"),
            source_uri(AGGREGATE_MEMBER, "authority-flow"),
        )
        layer_id = add_record(
            "atom",
            layer_address,
            {"atom_class": atom_class, "label": label},
            [flow_location],
            "Retains one declared authority/re-entry layer in the Source STDO flow.",
            generated_binding=(flow_location, local_key),
        )
        flow_ids.append((label, layer_id))
    for (left_label, left_id), (right_label, right_id) in zip(flow_ids, flow_ids[1:]):
        local_key = f"edge:precedes:{slug(left_label)}:{slug(right_label)}"
        source_key = generated_source_key(flow_location, local_key)
        edge_address = address(
            source_key,
            f"{left_label} precedes {right_label}",
            "urn:stdo:bounded-context:recursive-product-taxonomy",
            source_uri("SPEC_METHOD.md"),
            source_uri(AGGREGATE_MEMBER, "authority-flow"),
        )
        add_record(
            "edge",
            edge_address,
            {
                "source_ref": left_id,
                "relation_kind_ref": relation_kinds["precedes"],
                "target_ref": right_id,
                "context_ref": ids[
                    "context:urn:stdo:bounded-context:recursive-product-taxonomy"
                ],
                "owner_ref": ids["authority:SPEC_METHOD.md"],
                "scope_ref": flow_scope_id,
                "cross_context": None,
            },
            [flow_location],
            "Retains one directed dependency in the declared STDO authority and re-entry flow.",
            generated_binding=(flow_location, local_key),
        )

    sections = parse_aggregate(release / "standards" / AGGREGATE_MEMBER)
    expected_sections = set(policy["sections"])
    if set(sections) != expected_sections:
        missing = sorted(expected_sections - set(sections))
        extra = sorted(set(sections) - expected_sections)
        raise PreparationFailure(
            f"aggregate section population differs: missing={missing}, extra={extra}"
        )
    additional: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in policy["additional_statements"]:
        additional[row["section"]].append(row)

    aggregate_document_id = document_ids[AGGREGATE_MEMBER]
    for heading, profile in policy["sections"].items():
        section_slug = slug(heading)
        section_location = locator(digests, AGGREGATE_MEMBER, section_slug)
        context = profile["bounded_context"]
        authority_member = profile["authority_member"]
        authority = source_uri(authority_member)
        scope = source_uri(AGGREGATE_MEMBER, section_slug)
        scope_key = f"scope:{section_slug}"
        scope_source = generated_source_key(section_location, scope_key)
        scope_address = address(scope_source, heading, context, authority, scope)
        section_scope_id = add_record(
            "atom",
            scope_address,
            {"atom_class": "scope", "label": heading},
            [section_location],
            "Retains the exact governed scope of one aggregate compression section.",
            generated_binding=(section_location, scope_key),
            name=f"scope:{section_slug}",
        )
        clause_key = f"clause:{section_slug}"
        clause_source = generated_source_key(section_location, clause_key)
        clause_address = address(clause_source, heading, context, authority, scope)
        clause_id = add_record(
            "atom",
            clause_address,
            {"atom_class": "clause", "label": heading},
            [section_location],
            "Retains one exact aggregate compression clause as a semantic navigation and source re-entry node.",
            generated_binding=(section_location, clause_key),
            name=f"clause:{section_slug}",
        )
        edge_key = f"edge:part-of:{section_slug}"
        edge_source = generated_source_key(section_location, edge_key)
        edge_address = address(
            edge_source,
            f"{heading} part of STDO compressed authority",
            context,
            authority,
            scope,
        )
        add_record(
            "edge",
            edge_address,
            {
                "source_ref": clause_id,
                "relation_kind_ref": relation_kinds["part_of"],
                "target_ref": aggregate_document_id,
                "context_ref": ids[f"context:{context}"],
                "owner_ref": ids[f"authority:{authority_member}"],
                "scope_ref": section_scope_id,
                "cross_context": None,
            },
            [section_location],
            "Retains the aggregate clause-to-document containment route.",
            generated_binding=(section_location, edge_key),
        )

        statements: list[tuple[str, str]] = [
            (profile["default_constraint_class"], statement)
            for statement in sections[heading]
        ]
        statements.extend(
            (row["constraint_class"], row["statement"]) for row in additional[heading]
        )
        for index, (default_class, statement) in enumerate(statements, start=1):
            local_fragment = f"{section_slug}/declaration-{index:03d}"
            statement_location = locator(digests, AGGREGATE_MEMBER, local_fragment)
            local_key = f"constraint:{local_fragment}"
            source_key = generated_source_key(statement_location, local_key)
            statement_address = address(
                source_key,
                f"{heading} declaration {index:03d}",
                context,
                authority,
                scope,
            )
            frames = set(profile["frame_families"])
            lowered = statement.casefold()
            for family, keywords in policy["keyword_frame_routes"].items():
                if any(keyword.casefold() in lowered for keyword in keywords):
                    frames.add(family)
            constraint_id = add_record(
                "constraint",
                statement_address,
                {
                    "constraint_class": constraint_class(default_class, statement),
                    "statement": statement,
                    "applies_to_refs": [clause_id],
                    "context_ref": ids[f"context:{context}"],
                    "owner_ref": ids[f"authority:{authority_member}"],
                    "scope_ref": section_scope_id,
                    "declared_latitude": None,
                },
                [statement_location],
                "Retains one exact top-level declaration from the released aggregate compression as a source-addressed passive constraint.",
                generated_binding=(statement_location, local_key),
            )
            for family in frames:
                frame_route_refs[family].add(constraint_id)
            if heading == "Reference Frame Engagement Compression":
                for role in ENGAGEMENT_ROLES:
                    role_route_refs[role].add(constraint_id)

    records.sort(key=lambda row: row["id"])
    projection_routes = {
        "kind": "stdo-representation.gtl-projection-route-candidates",
        "schema_version": 1,
        "source_stdo_uri": SOURCE_URI,
        "frame_routes": [
            {
                "frame_family": family,
                "frame_ref": frame_ids[family],
                "mandatory_program_refs": sorted(
                    {frame_ids[family], *frame_route_refs[family]}
                ),
            }
            for family in FRAME_FAMILIES
        ],
        "role_routes": [
            {
                "engagement_role": role,
                "role_ref": role_ids[role],
                "role_program_refs": sorted({role_ids[role], *role_route_refs[role]}),
            }
            for role in ENGAGEMENT_ROLES
        ],
        "status": "candidate; each exact Executive Context Assignment selects and accepts its own applicable routes",
    }
    return (
        records,
        reasons,
        [generated[key] for key in sorted(generated)],
        projection_routes,
    )


def selection_ledger(
    manifest: dict[str, Any],
    records: list[dict[str, Any]],
    reasons: dict[str, str],
    generated: list[dict[str, Any]],
    what_sha: str,
    profile_sha: str,
    policy: dict[str, Any],
) -> tuple[dict[str, Any], bytes, str]:
    grouped: dict[tuple[bytes, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        owner = record["semantic_address"]["owning_authority"]
        locator_bytes = canonical_bytes(record["source_locators"])
        grouped[(locator_bytes, owner)].append(record)
    selections: list[dict[str, Any]] = []
    for (locator_bytes, owner), owned in grouped.items():
        locators = json.loads(locator_bytes)
        selection_ref = (
            "urn:stdo-representation:selection:sha256:"
            f"{sha256(canonical_bytes({'source_locators': locators, 'source_owner': owner}))}"
        )
        rationale = " ".join(sorted({reasons[record["id"]] for record in owned}))
        selections.append(
            {
                "selection_ref": selection_ref,
                "source_locators": locators,
                "disposition": "retained",
                "representation_refs": sorted(record["id"] for record in owned),
                "rationale": rationale,
                "source_owner": owner,
                "ordered_relation": False,
            }
        )
    selections.sort(key=lambda row: row["selection_ref"])
    selection_by_member: dict[str, list[str]] = defaultdict(list)
    for row in selections:
        for location in row["source_locators"]:
            selection_by_member[location["member_path"]].append(row["selection_ref"])
    evaluated = []
    for member in manifest["standards"]["members"]:
        member_path = member["path"]
        refs = sorted(set(selection_by_member[member_path]))
        if not refs:
            raise PreparationFailure(
                f"selection policy left one installed member unevaluated: {member_path}"
            )
        evaluated.append(
            {
                "member_path": member_path,
                "member_sha256": f"sha256:{member['sha256']}",
                "disposition": "contains_retained_material",
                "selection_refs": refs,
                "rationale": "The selected graph retains this exact member's source-route atom and immutable basis-membership edge; any additional represented declarations are named by the cited selection rows.",
            }
        )
    authority = policy["authority_binding"]
    ledger = {
        "kind": "stdo-representation.semantic-selection-ledger",
        "schema_version": 1,
        "source_stdo_uri": SOURCE_URI,
        "source_stdo_manifest_sha256": f"sha256:{SOURCE_MANIFEST_SHA}",
        "source_member_set_sha256": f"sha256:{SOURCE_MEMBER_SET}",
        "what_member_set_identity": what_sha,
        "build_tenant_identity": BUILD_TENANT_IDENTITY,
        "representation_profile_identity": PROFILE_IDENTITY,
        "representation_profile_sha256": profile_sha,
        "representation_records_sha256": f"sha256:{sha256(canonical_bytes(sorted(records, key=lambda row: row['id'])))}",
        "evaluated_members": evaluated,
        "selections": selections,
        "generated_source_keys": generated,
        "residual_uncertainty": [],
        "author": {
            "traversal_ref": F_H,
            "actor_identity": authority["actor_identity"],
            "authority_identity": authority["authority_identity"],
            "grant_identity": authority["grant_identity"],
            "grant_scope": authority["grant_scope"],
            "subject": "Source STDO v2.4.3-rc.3 semantic selection for the first STDO.gtl Product candidate",
            "basis_refs": sorted(
                [
                    SOURCE_URI,
                    "https://github.com/foolishimp/abiogenesis/commit/8d7f965a3fae7d1acea6a9db298798480fd4cc2f",
                    f"https://github.com/foolishimp/stdo_representation/commit/{run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture=True).strip()}",
                ]
            ),
        },
        "supersedes": None,
    }
    ledger_bytes = canonical_bytes(ledger)
    ledger_sha = sha256(ledger_bytes)
    identity = (
        "urn:stdo-representation:semantic-selection-ledger:sha256:" f"{ledger_sha}"
    )
    return ledger, ledger_bytes, identity


def frozen_gtl_repository(configured: Path | None, workspace: Path) -> Path:
    commit = "8d7f965a3fae7d1acea6a9db298798480fd4cc2f"
    if configured is not None:
        repository = configured.resolve()
    else:
        sibling = ROOT.parent / "abiogenesis"
        if (sibling / ".git").exists():
            repository = sibling.resolve()
        else:
            repository = workspace / "abiogenesis.git"
            run(
                [
                    "git",
                    "clone",
                    "--filter=blob:none",
                    "--no-checkout",
                    "https://github.com/foolishimp/abiogenesis.git",
                    str(repository),
                ],
                cwd=workspace,
            )
            run(["git", "fetch", "origin", commit], cwd=repository)
    if (
        run(
            ["git", "rev-parse", f"{commit}^{{commit}}"], cwd=repository, capture=True
        ).strip()
        != commit
    ):
        raise PreparationFailure("frozen GTL commit does not resolve exactly")
    tree = run(
        ["git", "rev-parse", f"{commit}:specification/requirements/gtl"],
        cwd=repository,
        capture=True,
    ).strip()
    if tree != "21a44b1941a1055d6abd973937e65b83e359de1b":
        raise PreparationFailure("frozen GTL authority tree differs")
    return repository


def publisher_product(
    workspace: Path, configured_abiogenesis: Path | None
) -> tuple[bytes, dict[str, Any], bytes, dict[str, Any]]:
    commit = run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture=True).strip()
    code_tree = run(
        ["git", "rev-parse", "HEAD:build_tenants/gtl/code"],
        cwd=ROOT,
        capture=True,
    ).strip()
    if run(
        ["git", "status", "--porcelain", "--", "build_tenants/gtl/code"],
        cwd=ROOT,
        capture=True,
    ).strip():
        raise PreparationFailure("publisher code has uncommitted changes")
    repository = frozen_gtl_repository(configured_abiogenesis, workspace)
    frozen_archive = workspace / "frozen-gtl.tar"
    run(
        [
            "git",
            "archive",
            "--format=tar",
            "--output",
            str(frozen_archive),
            "8d7f965a3fae7d1acea6a9db298798480fd4cc2f",
            "build_tenants/abiogenesis/typescript",
        ],
        cwd=repository,
    )
    frozen_source = workspace / "frozen-source"
    frozen_source.mkdir()
    with tarfile.open(frozen_archive, "r:") as bundle:
        bundle.extractall(frozen_source, filter="data")
    frozen_tenant = frozen_source / "build_tenants" / "abiogenesis" / "typescript"
    run(["npm", "ci", "--ignore-scripts"], cwd=frozen_tenant)
    run(["npm", "run", "build"], cwd=frozen_tenant)

    code_archive = workspace / "publisher-source.tar"
    run(
        [
            "git",
            "archive",
            "--format=tar",
            "--output",
            str(code_archive),
            "HEAD",
            "build_tenants/gtl/code",
        ],
        cwd=ROOT,
    )
    publisher_source = workspace / "publisher-source"
    publisher_source.mkdir()
    with tarfile.open(code_archive, "r:") as bundle:
        bundle.extractall(publisher_source, filter="data")
    package = publisher_source / "build_tenants" / "gtl" / "code"
    run(
        ["npm", "ci", "--ignore-scripts", "--legacy-peer-deps"],
        cwd=package,
    )
    scope = package / "node_modules" / "@abiogenesis"
    scope.mkdir(parents=True, exist_ok=True)
    os.symlink(frozen_tenant, scope / "typescript-tenant", target_is_directory=True)
    run(["npm", "run", "build"], cwd=package)
    run(["npm", "test"], cwd=package)
    pack_output = workspace / "pack"
    pack_output.mkdir()
    run(
        ["npm", "pack", "--pack-destination", str(pack_output)],
        cwd=package,
    )
    artifacts = list(pack_output.glob("*.tgz"))
    if len(artifacts) != 1:
        raise PreparationFailure("npm pack did not produce exactly one artifact")
    artifact_bytes = artifacts[0].read_bytes()
    members: list[dict[str, str]] = []
    with tarfile.open(artifacts[0], "r:gz") as bundle:
        for entry in bundle.getmembers():
            if not entry.isfile():
                continue
            extracted = bundle.extractfile(entry)
            if extracted is None:
                raise PreparationFailure(f"cannot read packed member {entry.name}")
            member_path = entry.name.removeprefix("package/")
            members.append(
                {
                    "path": member_path,
                    "sha256": f"sha256:{sha256(extracted.read())}",
                }
            )
    members.sort(key=lambda row: row["path"])
    content_rows = "".join(
        f"{member['path']}\0{member['sha256']}\n" for member in members
    ).encode("utf-8")
    artifact_sha = f"sha256:{sha256(artifact_bytes)}"
    content_sha = f"sha256:{sha256(content_rows)}"
    descriptor_ref = "urn:stdo-representation:descriptor:gtl-toolchain:0.1.0"
    contribution_ref = (
        "urn:stdo-representation:contribution-manifest:gtl-toolchain:0.1.0"
    )
    manifest = {
        "kind": "stdo-representation.gtl-toolchain-product",
        "schema_version": 1,
        "repository": "https://github.com/foolishimp/stdo_representation.git",
        "commit_sha1": commit,
        "tree_sha1": code_tree,
        "artifact_digest": artifact_sha,
        "product_content_digest": content_sha,
        "descriptor_ref": descriptor_ref,
        "contribution_manifest_ref": contribution_ref,
        "package_name": "@foolishimp/stdo-representation-gtl",
        "package_version": "0.1.0",
        "module_path": "./semantics",
        "named_symbol": "STDO_GTL_PRODUCT_SEMANTICS",
        "members": members,
        "supersedes": None,
    }
    manifest_bytes = canonical_bytes(manifest)
    manifest_sha = f"sha256:{sha256(manifest_bytes)}"
    basis = {
        "owning_product_id": (
            "urn:stdo-representation:gtl-toolchain-product:sha256:"
            f"{manifest_sha.removeprefix('sha256:')}"
        ),
        "artifact_digest": artifact_sha,
        "product_content_digest": content_sha,
        "product_manifest_digest": manifest_sha,
        "descriptor_ref": descriptor_ref,
        "contribution_manifest_ref": contribution_ref,
        "package_name": "@foolishimp/stdo-representation-gtl",
        "package_version": "0.1.0",
        "module_path": "./semantics",
        "named_symbol": "STDO_GTL_PRODUCT_SEMANTICS",
    }
    return artifact_bytes, manifest, manifest_bytes, basis


def selection_review(
    records: list[dict[str, Any]],
    ledger: dict[str, Any],
    ledger_identity: str,
    ledger_sha: str,
    profile_sha: str,
    frame_sha: str,
    publisher_basis: dict[str, Any],
) -> str:
    constraints = [row for row in records if row["kind"] == "constraint"]
    rows = [
        "# STDO.gtl Semantic Selection Review",
        "",
        "Status: candidate requiring exact `F_H` review and acceptance; no Product has been constructed.",
        "",
        "## Exact subjects",
        "",
        f"- Source STDO: `{SOURCE_URI}`",
        f"- Source manifest: `sha256:{SOURCE_MANIFEST_SHA}`",
        f"- Semantic Selection Ledger: `{ledger_identity}`",
        f"- Ledger SHA-256: `{ledger_sha}`",
        f"- GTL profile: `{PROFILE_IDENTITY}` / `{profile_sha}`",
        f"- Project frame basis: `{FRAME_BASIS_IDENTITY}` / `{frame_sha}`",
        f"- Publisher Product: `{publisher_basis['owning_product_id']}`",
        "",
        "## Population",
        "",
        f"- Evaluated Source STDO members: {len(ledger['evaluated_members'])}",
        f"- Semantic selections: {len(ledger['selections'])}",
        f"- Generated source-key bindings: {len(ledger['generated_source_keys'])}",
        f"- Atoms: {sum(row['kind'] == 'atom' for row in records)}",
        f"- Edges: {sum(row['kind'] == 'edge' for row in records)}",
        f"- Passive constraints: {len(constraints)}",
        "- Residual uncertainty recorded by this candidate: none",
        "",
        "Every installed member contributes an exact route atom and basis-membership edge. The selected aggregate compression contributes every top-level declaration plus the five explicit prose declarations in `selection-policy.json`. This is a proposed semantic selection, not a machine proof of completeness.",
        "",
        "## Selected passive constraints",
        "",
        "| # | Source route | Class | Statement |",
        "|---:|---|---|---|",
    ]
    for index, record in enumerate(constraints, start=1):
        location = record["source_locators"][0]
        route = f"{location['member_path']}#{location['fragment']}"
        statement = record["statement"].replace("|", "\\|")
        rows.append(
            f"| {index} | `{route}` | `{record['constraint_class']}` | {statement} |"
        )
    rows.extend(
        [
            "",
            "## Acceptance boundary",
            "",
            "Acceptance must bind the exact ledger bytes and does not accept the resulting Product, release, measurements, projections, or probabilistic observations in advance.",
            "",
        ]
    )
    return "\n".join(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--store", type=Path)
    parser.add_argument("--abiogenesis-repository", type=Path)
    parser.add_argument("--output-directory", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    output = args.output_directory.resolve()
    if output.exists():
        raise PreparationFailure(f"output already exists: {output}")
    current_what = what_identity()
    profile_sha = f"sha256:{sha256(PROFILE.read_bytes())}"
    frame_sha = f"sha256:{sha256(FRAME_BASIS.read_bytes())}"
    require_historical_preparation_basis(current_what, profile_sha, frame_sha)
    policy = json.loads(POLICY.read_text(encoding="utf-8"))
    store = selected_store(args.store)
    release, manifest, manifest_bytes, digests = load_source(store)
    records, reasons, generated, projection_routes = prepare_records(
        release, manifest, digests, policy
    )
    ledger, ledger_bytes, ledger_identity = selection_ledger(
        manifest,
        records,
        reasons,
        generated,
        current_what,
        profile_sha,
        policy,
    )
    ledger_sha = f"sha256:{sha256(ledger_bytes)}"
    with tempfile.TemporaryDirectory(prefix="stdo-gtl-candidate-") as directory:
        workspace = Path(directory)
        (
            artifact,
            publisher_manifest,
            publisher_manifest_bytes,
            publisher_basis,
        ) = publisher_product(workspace, args.abiogenesis_repository)
    plan_base = {
        "kind": "stdo-representation.gtl-build-plan-base",
        "schema_version": 1,
        "source_stdo": {
            "release_uri": SOURCE_URI,
            "installed_manifest_sha256": f"sha256:{SOURCE_MANIFEST_SHA}",
            "standards_member_set_sha256": f"sha256:{SOURCE_MEMBER_SET}",
        },
        "what_member_set_identity": current_what,
        "representation_profile_identity": PROFILE_IDENTITY,
        "representation_profile_sha256": profile_sha,
        "frame_basis_identity": FRAME_BASIS_IDENTITY,
        "frame_basis_sha256": frame_sha,
        "frame_admitting_authority_refs": list(FRAME_AUTHORITIES),
        "semantic_selection_ledger_identity": ledger_identity,
        "semantic_selection_ledger_sha256": ledger_sha,
        "publisher": publisher_basis,
        "records": records,
    }
    authority = policy["authority_binding"]
    review_bytes = selection_review(
        records,
        ledger,
        ledger_identity,
        ledger_sha,
        profile_sha,
        frame_sha,
        publisher_basis,
    ).encode("utf-8")
    projection_bytes = pretty_bytes(projection_routes)
    evidence_refs = sorted(
        [
            "projection-route-candidates.json?sha256=" f"{sha256(projection_bytes)}",
            "publisher/gtl-toolchain-product.json?sha256="
            f"{sha256(publisher_manifest_bytes)}",
            f"selection-policy.json?sha256={sha256(POLICY.read_bytes())}",
            f"selection-review.md?sha256={sha256(review_bytes)}",
        ]
    )
    acceptance_request = {
        "kind": "stdo-representation.f-h-acceptance-request",
        "schema_version": 1,
        "status": "pending",
        "requested_actor_identity": authority["actor_identity"],
        "requested_authority_identity": authority["authority_identity"],
        "requested_grant_identity": authority["grant_identity"],
        "requested_grant_scope": authority["grant_scope"],
        "required_basis_refs": ledger["author"]["basis_refs"],
        "subjects": [
            {
                "subject_kind": "reference_frame_basis",
                "subject_identity": FRAME_BASIS_IDENTITY,
                "subject_sha256": frame_sha,
                "path": "../../../../specification/REFERENCE_FRAME_BASIS.md",
            },
            {
                "subject_kind": "representation_profile",
                "subject_identity": PROFILE_IDENTITY,
                "subject_sha256": profile_sha,
                "path": "../../design/GTL_REPRESENTATION_PROFILE.md",
            },
            {
                "subject_kind": "semantic_selection_ledger",
                "subject_identity": ledger_identity,
                "subject_sha256": ledger_sha,
                "path": "semantic-selection-ledger.json",
            },
        ],
        "evidence_refs": evidence_refs,
        "effect_of_acceptance": "Authorizes deterministic construction against only these unchanged subjects; it does not accept or release the resulting Product.",
    }
    summary = {
        "kind": "stdo-representation.gtl-candidate-preparation",
        "schema_version": 1,
        "construction_status": "blocked_pending_f_h_acceptance",
        "source_stdo_uri": SOURCE_URI,
        "what_member_set_identity": current_what,
        "semantic_selection_ledger_identity": ledger_identity,
        "semantic_selection_ledger_sha256": ledger_sha,
        "profile_sha256": profile_sha,
        "frame_basis_sha256": frame_sha,
        "publisher_product_identity": publisher_basis["owning_product_id"],
        "publisher_artifact_sha256": publisher_basis["artifact_digest"],
        "record_counts": {
            "atoms": sum(row["kind"] == "atom" for row in records),
            "edges": sum(row["kind"] == "edge" for row in records),
            "constraints": sum(row["kind"] == "constraint" for row in records),
        },
        "evaluated_members": len(ledger["evaluated_members"]),
        "selection_rows": len(ledger["selections"]),
        "residual_uncertainty": len(ledger["residual_uncertainty"]),
        "projection_route_counts": {
            row["frame_family"]: len(row["mandatory_program_refs"])
            for row in projection_routes["frame_routes"]
        },
    }
    temporary = output.parent / f".{output.name}.tmp-{os.getpid()}"
    temporary.mkdir(parents=True)
    try:
        (temporary / "publisher").mkdir()
        (temporary / "selection-policy.json").write_bytes(POLICY.read_bytes())
        (temporary / "source-manifest.json").write_bytes(manifest_bytes)
        (temporary / "semantic-selection-ledger.json").write_bytes(ledger_bytes)
        write_canonical(
            temporary / "publisher" / "gtl-toolchain-product.json",
            publisher_manifest,
        )
        (temporary / "publisher" / "gtl-toolchain-product.tgz").write_bytes(artifact)
        write_pretty(temporary / "build-plan-base.json", plan_base)
        (temporary / "projection-route-candidates.json").write_bytes(projection_bytes)
        write_pretty(temporary / "acceptance-request.json", acceptance_request)
        write_pretty(temporary / "candidate-summary.json", summary)
        (temporary / "selection-review.md").write_bytes(review_bytes)
        output.parent.mkdir(parents=True, exist_ok=True)
        temporary.rename(output)
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (PreparationFailure, KeyError, OSError, ValueError) as error:
        raise SystemExit(f"STDO.gtl candidate preparation failed: {error}") from None
