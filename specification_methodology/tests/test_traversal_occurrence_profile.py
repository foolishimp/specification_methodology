from __future__ import annotations

import copy
import hashlib
import json
import re
import unittest
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
STANDARD = ROOT / "specification/standards/TRAVERSAL_OCCURRENCE_PROFILE.md"
CALCULUS = ROOT / "specification/standards/AXIOMATIC_CALCULUS.md"
PRODUCT = ROOT / "specification/PRODUCT.md"
COMPRESSION = (
    ROOT / "specification/standards/authority_compressions/"
    "traversal_occurrence_profile.compressed.md"
)

CONTEXT = "urn:fixture:context"
OWNER = "urn:fixture:owner"
SCOPE = "urn:fixture:scope"
BASIS = "urn:fixture:profile-basis"
AUTHORITY = "urn:fixture:authority"
FUNCTOR = "urn:stdo:concept:axiomatic-calculus:f-p"
PREDECESSOR_RELEASE_URI = "stdo://releases/v2.4.3-rc.3/"
INSTALLED_RC3 = Path.home() / "Library/Application Support/STDO/releases/v2.4.3-rc.3"
INSTALLED_RC3_MANIFEST_SHA256 = (
    "312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551"
)

EXPECTED_CALCULUS_DERIVATION_TARGETS = {
    "IDENTITY_METHOD.md#core-law",
    "IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004",
    "REFERENCE_FRAME_METHOD.md#evaluation",
    "REFERENCE_FRAME_METHOD.md#position",
    "REFERENCE_FRAME_METHOD.md#reference-frame-laws",
    "REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates",
    "REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation",
    "REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation",
    "REFERENCE_FRAME_METHOD.md#rf-012-closed-results",
    "SPEC_METHOD.md#agentic-construction-execution-stdo-up-020",
    "SPEC_METHOD.md#ambiguity-governance-rule",
    "SPEC_METHOD.md#bounded-context-semantic-resolution",
    "SPEC_METHOD.md#constitutional-chain",
    "SPEC_METHOD.md#one-constitutional-surface-and-version-boundary-stdo-surface-001",
}
PREDECESSOR_MEMBER_SHA256 = {
    "IDENTITY_METHOD.md": (
        "e65b875464cc93a3f9186d915ad88603755de34bac6f27072562ed34c13f64cd"
    ),
    "REFERENCE_FRAME_METHOD.md": (
        "a270453802ae03d6871c408d782094180b938aca22399ce817451fdd4551b174"
    ),
    "SPEC_METHOD.md": (
        "50b825969ae23c5a42f7f3776fd2ab4146836349dfd4ef7a548dc2b6349b389c"
    ),
}
TYPED_RELATION_FIELDS = {
    "id",
    "kind",
    "source",
    "target",
    "context",
    "owner",
    "scope",
    "basis",
    "qualifiers",
}
TYPED_RELATION_URI_FIELDS = {
    "id",
    "source",
    "target",
    "context",
    "owner",
    "scope",
    "basis",
}

RECORD_POPULATIONS = {
    "urn:stdo:concept:axiomatic-calculus:record-kind:semantic-object": "O",
    "urn:stdo:concept:axiomatic-calculus:record-kind:typed-relation": "E",
    "urn:stdo:concept:axiomatic-calculus:record-kind:constraint": "C",
    "urn:stdo:concept:axiomatic-calculus:record-kind:latitude": "L",
    "urn:stdo:concept:axiomatic-calculus:record-kind:residual": "X",
    "urn:stdo:concept:axiomatic-calculus:record-kind:traversal": "V",
    "urn:stdo:concept:axiomatic-calculus:record-kind:transformation": "T",
    "urn:stdo:concept:axiomatic-calculus:record-kind:judgment": "J",
}
EVENT_KINDS = {
    "urn:stdo:traversal-occurrence:event-kind:claim-admission",
    "urn:stdo:traversal-occurrence:event-kind:occurrence-admission",
    "urn:stdo:traversal-occurrence:event-kind:effect-disposition",
    "urn:stdo:traversal-occurrence:event-kind:external-fact-admission",
}
EVENT_SCOPES = {"occurrence_scoped", "subject_scoped", "authority_scoped"}
QUALIFIER_KEYS = {
    "cardinality",
    "authority_ref",
    "evidence_refs",
    "provenance_refs",
    "invalidation_ref",
    "inverse_kind_ref_or_none",
    "preservation",
    "loss",
    "refusal",
}
RELATION_CARDINALITY = {
    "application_of": "exactly_one",
    "applies_traversal": "exactly_one",
    "bound_to_subject": "exactly_one",
    "intends": "exactly_one",
    "observes_before": "zero_or_one",
    "observes_after": "zero_or_one",
    "invokes_effect": "zero_or_one",
    "operation_of_kind": "exactly_one",
    "targets_subject": "exactly_one",
    "authorized_by": "exactly_one",
    "disposition_for": "zero_or_one",
    "evidenced_by": "zero_or_more",
    "event_for": "zero_or_one",
    "frontier_contains": "zero_or_more",
    "projects_frontier": "exactly_one",
    "identity_depends_on": "zero_or_more",
    "causally_precedes_occurrence": "zero_or_more",
    "causally_precedes_event": "zero_or_more",
    "supports_event": "zero_or_more",
    "corrects_event": "zero_or_more",
    "component_of_occurrence": "zero_or_one",
    "admits_claim": "exactly_one",
    "materializes_relation": "exactly_one",
    "transition_for": "exactly_one",
}
RESOLUTION_FIELDS = {
    "external_identity",
    "reference_domain",
    "external_target_kind",
    "resolved_target_identity",
    "basis_relation",
    "resolution_basis",
    "evidence_identity",
}
EXTERNAL_DELTA_FIELDS = {
    "external_preserved",
    "external_introduced",
    "external_removed",
}
WITNESS_RESOLUTION_FIELDS = {
    "external_resolution",
    "domain_resolution",
    "codomain_resolution",
}
EXTERNAL_WITNESS_FIELDS = {
    "external_resolution",
    "domain_model",
    "codomain_model",
    "domain_resolution",
    "codomain_resolution",
    "decision",
    "evidence",
}
SEED_KEYS = {
    "profile_basis",
    "application",
    "traversal",
    "functor_kind",
    "subject_binding",
    "intended_outcome",
    "lineage",
    "identity_dependencies",
}
SIGNATURE_FRAGMENTS = [
    "#authority-and-adoption",
    "#candidate-judgment-event-and-relation-separation",
    "#causality-and-typed-lineage",
    "#closed-constraint-judgment-residual-and-stop-kinds",
    "#closed-event-kind-population",
    "#closed-relation-families",
    "#closed-semantic-object-sorts",
    "#event-frontier-and-projection",
    "#mutable-subject-effect-relation",
    "#occurrence-identity",
]
PROFILE_MEMBER_PATH = "standards/TRAVERSAL_OCCURRENCE_PROFILE.md"
SHA256_RE = re.compile(r"sha256:[0-9a-f]{64}")
RELEASE_URI_RE = re.compile(
    r"stdo://releases/v(?![^/]*-rc\.[^/]*-rc\.)"
    r"[0-9A-Za-z][0-9A-Za-z._+-]*-rc\.[1-9][0-9]*/"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def installed_standard_bytes(member_name: str) -> bytes:
    member_path = INSTALLED_RC3 / "standards" / member_name
    if not member_path.is_file():
        raise AssertionError(f"missing installed RC3 member: {member_path}")
    return member_path.read_bytes()


def markdown_heading_fragments(raw: bytes) -> set[str]:
    fragments: set[str] = set()
    for line in raw.decode("utf-8").splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*$", line)
        if match is None:
            continue
        heading = match.group(1).replace("`", "").lower()
        heading = re.sub(r"[^\w\- ]", "", heading)
        fragments.add(re.sub(r"\s+", "-", heading.strip()))
    return fragments


def expanded_transformation_external_ref_paths() -> set[str]:
    delta_paths = {
        f"{delta}[].{field}"
        for delta in EXTERNAL_DELTA_FIELDS
        for field in RESOLUTION_FIELDS
    }
    witness_resolution_paths = {
        f"external_resolution_witnesses[].{resolution}.{field}"
        for resolution in WITNESS_RESOLUTION_FIELDS
        for field in RESOLUTION_FIELDS
    }
    return (
        delta_paths
        | witness_resolution_paths
        | {
            "external_resolution_witnesses[].domain_model",
            "external_resolution_witnesses[].codomain_model",
            "external_resolution_witnesses[].evidence",
        }
    )


def utf16_key(value: str) -> bytes:
    return value.encode("utf-16-be", "surrogatepass")


def jcs(value: object) -> bytes:
    """Exact RFC 8785 bytes for the profile fixture's I-JSON value subset."""
    if value is None:
        return b"null"
    if value is True:
        return b"true"
    if value is False:
        return b"false"
    if isinstance(value, int) and not isinstance(value, bool):
        if abs(value) > 9_007_199_254_740_991:
            raise ValueError("non_i_json_integer")
        return str(value).encode("ascii")
    if isinstance(value, float):
        raise ValueError("unsupported_or_non_i_json_number")
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode()
    if isinstance(value, list):
        return b"[" + b",".join(jcs(item) for item in value) + b"]"
    if isinstance(value, Mapping):
        if any(not isinstance(key, str) for key in value):
            raise ValueError("non_string_object_name")
        members = []
        for key in sorted(value, key=utf16_key):
            members.append(jcs(key) + b":" + jcs(value[key]))
        return b"{" + b",".join(members) + b"}"
    raise ValueError("non_i_json_value")


def parse_unique_json(raw: bytes) -> object:
    def unique(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate_object_name")
            result[key] = value
        return result

    return json.loads(raw, object_pairs_hook=unique)


def digest(value: object) -> str:
    return "sha256:" + hashlib.sha256(jcs(value)).hexdigest()


def absolute_uri(value: object) -> bool:
    return isinstance(value, str) and bool(urlsplit(value).scheme)


def semantic_object(
    identity: str, sort: str, value: Mapping[str, object]
) -> dict[str, Any]:
    return {
        "id": identity,
        "sort": sort,
        "context": CONTEXT,
        "owner": OWNER,
        "scope": SCOPE,
        "basis": BASIS,
        "value": dict(value),
    }


def relation_qualifiers(kind: str | None = None) -> dict[str, object]:
    return {
        "cardinality": RELATION_CARDINALITY.get(kind, "exactly_one"),
        "authority_ref": AUTHORITY,
        "evidence_refs": ["urn:fixture:evidence"],
        "provenance_refs": ["urn:fixture:provenance"],
        "invalidation_ref": "urn:fixture:relation-invalidation",
        "inverse_kind_ref_or_none": None,
        "preservation": "meaning_preserved",
        "loss": "none",
        "refusal": "refuse_missing",
    }


def qualifier_issues(value: object, kind: str | None = None) -> list[str]:
    if not isinstance(value, Mapping) or set(value) != QUALIFIER_KEYS:
        return ["invalid_qualifier_shape"]
    issues: list[str] = []
    domains = {
        "cardinality": {"exactly_one", "zero_or_one", "zero_or_more", "one_or_more"},
        "preservation": {"identity_preserved", "meaning_preserved", "not_applicable"},
        "loss": {"none", "declared_loss"},
        "refusal": {
            "refuse_missing",
            "refuse_duplicate",
            "refuse_wrong_type",
            "refuse_invalid_basis",
            "refuse_out_of_scope",
            "not_applicable",
        },
    }
    for field, allowed in domains.items():
        if value.get(field) not in allowed:
            issues.append(f"invalid_qualifier_{field}")
    if kind in RELATION_CARDINALITY and value.get("cardinality") != (
        RELATION_CARDINALITY[kind]
    ):
        issues.append("relation_cardinality_mismatch")
    if value.get("preservation") != "meaning_preserved":
        issues.append("relation_preservation_mismatch")
    if value.get("loss") != "none":
        issues.append("relation_loss_mismatch")
    if value.get("refusal") == "not_applicable":
        issues.append("relation_refusal_unavailable")
    if value.get("inverse_kind_ref_or_none") is not None:
        issues.append("relation_inverse_not_declared")
    for field in ("authority_ref", "invalidation_ref"):
        if not absolute_uri(value.get(field)):
            issues.append(f"invalid_qualifier_{field}")
    inverse = value.get("inverse_kind_ref_or_none")
    if inverse is not None and not absolute_uri(inverse):
        issues.append("invalid_qualifier_inverse_kind_ref")
    for field in ("evidence_refs", "provenance_refs"):
        refs = value.get(field)
        if (
            not isinstance(refs, list)
            or not all(isinstance(ref, str) for ref in refs)
            or len(refs) != len(set(refs))
            or not all(absolute_uri(ref) for ref in refs)
        ):
            issues.append(f"invalid_qualifier_{field}")
    return issues


def typed_relation(
    identity: str, kind: str, source: str, target: str, qualifiers: object | None = None
) -> dict[str, Any]:
    return {
        "id": identity,
        "kind": kind,
        "source": source,
        "target": target,
        "context": CONTEXT,
        "owner": OWNER,
        "scope": SCOPE,
        "basis": BASIS,
        "qualifiers": relation_qualifiers(kind) if qualifiers is None else qualifiers,
    }


def typed_relation_issues(
    record: Mapping[str, object], expected_basis: str = BASIS
) -> list[str]:
    issues: list[str] = []
    if set(record) != TYPED_RELATION_FIELDS:
        issues.append("typed_relation_shape_mismatch")
    for field in TYPED_RELATION_URI_FIELDS:
        if not absolute_uri(record.get(field)):
            issues.append(f"typed_relation_uri_mismatch:{field}")
    if record.get("basis") != expected_basis:
        issues.append("relation_basis_mismatch")
    kind = record.get("kind")
    if kind not in RELATION_CARDINALITY:
        issues.append("unknown_relation_kind")
    issues.extend(qualifier_issues(record.get("qualifiers"), str(kind)))
    return issues


def relation_population_issues(
    population: Iterable[Mapping[str, object]], expected_basis: str = BASIS
) -> list[str]:
    rows = list(population)
    issues: list[str] = []
    identities = [row.get("id") for row in rows]
    triples = [(row.get("kind"), row.get("source"), row.get("target")) for row in rows]
    if len(identities) != len(set(identities)):
        issues.append("duplicate_relation_identity")
    if len(triples) != len(set(triples)):
        issues.append("duplicate_relation_edge")
    for row in rows:
        issues.extend(typed_relation_issues(row, expected_basis))
    return issues


def judgment(
    identity: str, kind: str, subject: Mapping[str, object], decision: str = "admitted"
) -> dict[str, Any]:
    return {
        "id": identity,
        "kind": kind,
        "subject": subject["id"],
        "subject_digest": digest(subject),
        "context": CONTEXT,
        "owner": OWNER,
        "scope": SCOPE,
        "basis": BASIS,
        "evaluator": "urn:fixture:evaluator",
        "authority": AUTHORITY,
        "decision": decision,
        "evidence": ["urn:fixture:evidence"],
        "provenance": ["urn:fixture:provenance"],
        "decided_at": "urn:fixture:decision-coordinate",
    }


def occurrence_seed(
    value: Mapping[str, object], basis: str = BASIS
) -> dict[str, object]:
    return {
        "profile_basis": basis,
        "application": value["application_ref"],
        "traversal": value["traversal_ref"],
        "functor_kind": value["functor_kind_ref"],
        "subject_binding": value["subject_binding_ref"],
        "intended_outcome": value["intended_outcome_ref"],
        "lineage": value["lineage_refs"],
        "identity_dependencies": value["identity_dependency_refs"],
    }


def occurrence_identity(seed: Mapping[str, object]) -> str:
    if set(seed) != SEED_KEYS:
        raise ValueError("incomplete_or_future_derived_seed")
    return "urn:fixture:occurrence:" + digest(seed)


def relations(
    population: Iterable[Mapping[str, object]],
    kind: str,
    *,
    source: str | None = None,
    target: str | None = None,
) -> list[Mapping[str, object]]:
    return [
        relation
        for relation in population
        if relation.get("kind") == kind
        and (source is None or relation.get("source") == source)
        and (target is None or relation.get("target") == target)
    ]


def singleton_target(
    population: Iterable[Mapping[str, object]], kind: str, source: str
) -> tuple[str | None, bool]:
    matches = relations(population, kind, source=source)
    return (matches[0].get("target") if len(matches) == 1 else None, len(matches) == 1)


def population_issues(
    populations: Mapping[str, list[Mapping[str, object]]],
    identities: set[str],
    external_identities: set[str],
) -> list[str]:
    issues: list[str] = []
    if set(populations) != set(RECORD_POPULATIONS):
        issues.append("record_kind_population_not_total")
    local: list[str] = []
    for records in populations.values():
        local.extend(str(record.get("id")) for record in records)
    if len(local) != len(set(local)):
        issues.append("local_population_not_disjoint")
    local_set = set(local)
    if local_set & external_identities:
        issues.append("local_external_ambiguity")
    if identities != local_set | external_identities:
        issues.append("identity_universe_not_closed")
    return issues


def reference_domain_issues(
    domain: Mapping[str, object],
    refs: list[str],
    local: Mapping[str, Mapping[str, object]],
    external: Mapping[str, Mapping[str, object]],
) -> list[str]:
    issues: list[str] = []
    cardinality = domain.get("cardinality")
    bounds = {"1": (1, 1), "0..1": (0, 1), "0..*": (0, None), "1..*": (1, None)}
    if cardinality not in bounds:
        return ["undeclared_cardinality"]
    minimum, maximum = bounds[str(cardinality)]
    if len(refs) < minimum or (maximum is not None and len(refs) > maximum):
        issues.append("reference_cardinality_mismatch")
    if len(refs) != len(set(refs)):
        issues.append("duplicate_reference")
    for ref in refs:
        local_target = local.get(ref)
        external_target = external.get(ref)
        if local_target is not None and external_target is not None:
            issues.append("local_external_reference_ambiguity")
            continue
        if local_target is not None:
            if local_target.get("family") not in domain.get("local_families", set()):
                issues.append("reference_wrong_local_family")
            allowed_sorts = domain.get("local_sorts", set())
            if allowed_sorts and local_target.get("sort") not in allowed_sorts:
                issues.append("reference_wrong_local_sort")
            if local_target.get("basis") != domain.get("basis"):
                issues.append("reference_wrong_basis")
        elif external_target is not None:
            if external_target.get("kind") not in domain.get("external_kinds", set()):
                issues.append("reference_wrong_external_kind")
            if external_target.get("basis_relation") != domain.get("basis_relation"):
                issues.append("reference_wrong_external_basis_relation")
        else:
            issues.append("dangling_reference")
    return issues


def resolution_coordinate(label: str) -> dict[str, str]:
    return {
        "external_identity": f"urn:fixture:external:{label}",
        "reference_domain": f"urn:fixture:reference-domain:{label}",
        "external_target_kind": "urn:fixture:external-target-kind",
        "resolved_target_identity": f"urn:fixture:resolved-target:{label}",
        "basis_relation": "urn:fixture:basis-relation",
        "resolution_basis": "urn:fixture:resolution-basis",
        "evidence_identity": f"urn:fixture:evidence:{label}",
    }


def transformation_external_fixture() -> dict[str, object]:
    preserved = resolution_coordinate("preserved")
    return {
        "external_preserved": [preserved],
        "external_introduced": [resolution_coordinate("introduced")],
        "external_removed": [resolution_coordinate("removed")],
        "external_resolution_witnesses": [
            {
                "external_resolution": copy.deepcopy(preserved),
                "domain_model": "urn:fixture:model:domain",
                "codomain_model": "urn:fixture:model:codomain",
                "domain_resolution": copy.deepcopy(preserved),
                "codomain_resolution": copy.deepcopy(preserved),
                "decision": "equal",
                "evidence": "urn:fixture:evidence:preservation",
            }
        ],
    }


def transformation_external_issues(value: Mapping[str, object]) -> list[str]:
    issues: list[str] = []
    expected_fields = EXTERNAL_DELTA_FIELDS | {"external_resolution_witnesses"}
    if set(value) != expected_fields:
        issues.append("external_transformation_shape_mismatch")
    coordinate_keys: dict[str, list[str]] = {}
    for field in EXTERNAL_DELTA_FIELDS:
        coordinates = value.get(field)
        if not isinstance(coordinates, list):
            issues.append(f"invalid_{field}_population")
            coordinate_keys[field] = []
            continue
        keys: list[str] = []
        for coordinate in coordinates:
            if (
                not isinstance(coordinate, Mapping)
                or set(coordinate) != RESOLUTION_FIELDS
            ):
                issues.append(f"invalid_{field}_coordinate_shape")
                continue
            if not all(absolute_uri(item) for item in coordinate.values()):
                issues.append(f"invalid_{field}_coordinate_reference")
            keys.append(digest(coordinate))
        if len(keys) != len(set(keys)):
            issues.append(f"duplicate_{field}_coordinate")
        coordinate_keys[field] = keys
    if set(coordinate_keys.get("external_preserved", [])) & set(
        coordinate_keys.get("external_introduced", [])
    ):
        issues.append("preserved_introduced_coordinate_overlap")
    if set(coordinate_keys.get("external_preserved", [])) & set(
        coordinate_keys.get("external_removed", [])
    ):
        issues.append("preserved_removed_coordinate_overlap")

    witnesses = value.get("external_resolution_witnesses")
    if not isinstance(witnesses, list):
        return [*issues, "invalid_external_witness_population"]
    witness_keys: list[str] = []
    witnessed_coordinates: list[str] = []
    for witness in witnesses:
        if not isinstance(witness, Mapping) or set(witness) != EXTERNAL_WITNESS_FIELDS:
            issues.append("invalid_external_witness_shape")
            continue
        witness_keys.append(digest(witness))
        if witness.get("decision") != "equal":
            issues.append("invalid_external_witness_decision")
        for field in ("domain_model", "codomain_model", "evidence"):
            if not absolute_uri(witness.get(field)):
                issues.append(f"invalid_external_witness_{field}")
        resolutions = [
            witness.get(field) for field in sorted(WITNESS_RESOLUTION_FIELDS)
        ]
        if any(
            not isinstance(coordinate, Mapping)
            or set(coordinate) != RESOLUTION_FIELDS
            or not all(absolute_uri(item) for item in coordinate.values())
            for coordinate in resolutions
        ):
            issues.append("invalid_external_witness_resolution")
            continue
        if not all(coordinate == resolutions[0] for coordinate in resolutions[1:]):
            issues.append("external_witness_resolution_mismatch")
        witnessed_coordinates.append(digest(resolutions[0]))
    if len(witness_keys) != len(set(witness_keys)):
        issues.append("duplicate_external_witness")
    if sorted(witnessed_coordinates) != sorted(
        coordinate_keys.get("external_preserved", [])
    ):
        issues.append("external_witness_population_mismatch")
    return issues


def occurrence_fixture() -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    application = semantic_object(
        "urn:fixture:application",
        "TraversalApplication",
        {
            "traversal_ref": "urn:fixture:traversal",
            "functor_kind_ref": FUNCTOR,
            "input_refs": ["urn:fixture:input"],
            "application_contract_ref": "urn:fixture:application-contract",
        },
    )
    occurrence_value = {
        "application_ref": application["id"],
        "traversal_ref": application["value"]["traversal_ref"],
        "functor_kind_ref": application["value"]["functor_kind_ref"],
        "subject_binding_ref": "urn:fixture:subject-binding",
        "intended_outcome_ref": "urn:fixture:intended-outcome",
        "lineage_refs": ["urn:fixture:cause", "urn:fixture:component"],
        "identity_dependency_refs": ["urn:fixture:identity-input"],
    }
    occurrence = semantic_object(
        occurrence_identity(occurrence_seed(occurrence_value)),
        "Occurrence",
        occurrence_value,
    )
    edge_specs = [
        ("application_of", occurrence["id"], application["id"]),
        ("applies_traversal", application["id"], "urn:fixture:traversal"),
        ("bound_to_subject", occurrence["id"], "urn:fixture:subject-binding"),
        ("intends", occurrence["id"], "urn:fixture:intended-outcome"),
        ("identity_depends_on", occurrence["id"], "urn:fixture:identity-input"),
        ("causally_precedes_occurrence", "urn:fixture:cause", occurrence["id"]),
        ("component_of_occurrence", "urn:fixture:component", occurrence["id"]),
    ]
    edges = [
        typed_relation(f"urn:fixture:edge:{index}", kind, source, target)
        for index, (kind, source, target) in enumerate(edge_specs)
    ]
    return {application["id"]: application, occurrence["id"]: occurrence}, edges


def occurrence_issues(
    objects: Mapping[str, Mapping[str, object]], edges: list[Mapping[str, object]]
) -> list[str]:
    issues = relation_population_issues(edges)
    occurrences = [
        record for record in objects.values() if record.get("sort") == "Occurrence"
    ]
    if len(occurrences) != 1:
        return ["missing_unique_occurrence"]
    occurrence = occurrences[0]
    value = occurrence["value"]
    if not isinstance(value, Mapping):
        return ["invalid_occurrence_value"]
    if occurrence["id"] != occurrence_identity(
        occurrence_seed(value, str(occurrence["basis"]))
    ):
        issues.append("occurrence_identity_preimage_mismatch")

    application_ref, exact_application = singleton_target(
        edges, "application_of", str(occurrence["id"])
    )
    if not exact_application or application_ref != value.get("application_ref"):
        issues.append("application_of_mismatch")
        return issues
    application = objects.get(str(application_ref))
    if application is None or application.get("sort") != "TraversalApplication":
        issues.append("application_wrong_sort")
        return issues
    application_value = application.get("value")
    if not isinstance(application_value, Mapping):
        issues.append("application_value_invalid")
        return issues
    if application_value.get("traversal_ref") != value.get("traversal_ref"):
        issues.append("application_traversal_mismatch")
    if application_value.get("functor_kind_ref") != value.get("functor_kind_ref"):
        issues.append("application_functor_mismatch")
    traversal_ref, exact_traversal = singleton_target(
        edges, "applies_traversal", str(application_ref)
    )
    if not exact_traversal or traversal_ref != value.get("traversal_ref"):
        issues.append("applies_traversal_mismatch")
    for kind, field in (
        ("bound_to_subject", "subject_binding_ref"),
        ("intends", "intended_outcome_ref"),
    ):
        target, exact = singleton_target(edges, kind, str(occurrence["id"]))
        if not exact or target != value.get(field):
            issues.append(f"{kind}_mismatch")
    dependency_targets = {
        str(edge["target"])
        for edge in relations(
            edges, "identity_depends_on", source=str(occurrence["id"])
        )
    }
    if dependency_targets != set(value.get("identity_dependency_refs", [])):
        issues.append("identity_dependency_mismatch")
    lineage_sources = {
        str(edge["source"])
        for kind in ("causally_precedes_occurrence", "component_of_occurrence")
        for edge in relations(edges, kind, target=str(occurrence["id"]))
    }
    if lineage_sources != set(value.get("lineage_refs", [])):
        issues.append("lineage_mismatch")
    return issues


def operation_fixture() -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    objects, edges = occurrence_fixture()
    occurrence = next(
        record for record in objects.values() if record["sort"] == "Occurrence"
    )
    subject = semantic_object(
        "urn:fixture:subject-binding",
        "SubjectBinding",
        {
            "subject_ref": "urn:fixture:mutable-subject",
            "authority_ref": AUTHORITY,
            "invalidation_ref": "urn:fixture:subject-invalidation",
        },
    )
    kind = semantic_object(
        "urn:fixture:operation-kind",
        "OperationKind",
        {
            "operation_contract_ref": "urn:fixture:operation-contract",
            "target_sort_ref": "urn:fixture:target-sort",
            "invalidation_ref": "urn:fixture:operation-kind-invalidation",
        },
    )
    operation = semantic_object(
        "urn:fixture:operation",
        "EffectOperation",
        {
            "operation_kind_ref": kind["id"],
            "subject_binding_ref": subject["id"],
            "effect_territory_ref": "urn:fixture:territory",
            "operation_contract_ref": kind["value"]["operation_contract_ref"],
            "invalidation_ref": "urn:fixture:operation-invalidation",
        },
    )
    grant = semantic_object(
        "urn:fixture:grant",
        "OperationGrant",
        {
            "issuer_ref": AUTHORITY,
            "subject_binding_ref": subject["id"],
            "allowed_operation_kind_refs": [kind["id"]],
            "allowed_effect_territory_ref": "urn:fixture:territory",
            "invalidation_ref": "urn:fixture:grant-invalidation",
        },
    )
    invocation = semantic_object(
        "urn:fixture:invocation",
        "EffectInvocation",
        {
            "occurrence_ref": occurrence["id"],
            "operation_ref": operation["id"],
            "executor_ref": "urn:fixture:executor",
            "actor_ref": "urn:fixture:actor",
            "operation_grant_ref": grant["id"],
            "effect_territory_ref": "urn:fixture:territory",
            "input_refs": ["urn:fixture:operation-input"],
        },
    )
    objects.update(
        {
            record["id"]: record
            for record in (subject, kind, operation, grant, invocation)
        }
    )
    for index, (relation_kind, source, target) in enumerate(
        (
            ("operation_of_kind", operation["id"], kind["id"]),
            ("targets_subject", operation["id"], subject["id"]),
            ("authorized_by", invocation["id"], grant["id"]),
            ("invokes_effect", occurrence["id"], invocation["id"]),
        ),
        start=len(edges),
    ):
        edges.append(
            typed_relation(f"urn:fixture:edge:{index}", relation_kind, source, target)
        )
    return objects, edges


def operation_issues(
    objects: Mapping[str, Mapping[str, object]], edges: list[Mapping[str, object]]
) -> list[str]:
    issues = relation_population_issues(edges)
    operation = next(
        record for record in objects.values() if record.get("sort") == "EffectOperation"
    )
    invocation = next(
        record
        for record in objects.values()
        if record.get("sort") == "EffectInvocation"
    )
    occurrence = objects[str(invocation["value"]["occurrence_ref"])]
    grant = objects.get(str(invocation["value"]["operation_grant_ref"]))
    operation_value = operation["value"]
    invocation_value = invocation["value"]
    if invocation_value.get("operation_ref") != operation["id"]:
        issues.append("invocation_operation_mismatch")
    for kind, expected in (
        ("operation_of_kind", operation_value.get("operation_kind_ref")),
        ("targets_subject", operation_value.get("subject_binding_ref")),
    ):
        target, exact = singleton_target(edges, kind, str(operation["id"]))
        if not exact or target != expected:
            issues.append(f"{kind}_mismatch")
    authorized_target, exact_authorized = singleton_target(
        edges, "authorized_by", str(invocation["id"])
    )
    if not exact_authorized or authorized_target != invocation_value.get(
        "operation_grant_ref"
    ):
        issues.append("authorized_by_mismatch")
    invoked_target, exact_invoked = singleton_target(
        edges, "invokes_effect", str(occurrence["id"])
    )
    if not exact_invoked or invoked_target != invocation["id"]:
        issues.append("invokes_effect_mismatch")
    if grant is None or grant.get("sort") != "OperationGrant":
        return [*issues, "grant_missing_or_wrong_sort"]
    grant_value = grant["value"]
    subject_refs = {
        operation_value.get("subject_binding_ref"),
        grant_value.get("subject_binding_ref"),
        occurrence["value"].get("subject_binding_ref"),
    }
    if len(subject_refs) != 1:
        issues.append("operation_subject_grant_mismatch")
    if operation_value.get("operation_kind_ref") not in grant_value.get(
        "allowed_operation_kind_refs", []
    ):
        issues.append("operation_kind_not_granted")
    operation_kind = objects.get(str(operation_value.get("operation_kind_ref")))
    if operation_kind is None or operation_kind.get("sort") != "OperationKind":
        issues.append("operation_kind_missing_or_wrong_sort")
    elif operation_value.get("operation_contract_ref") != operation_kind.get(
        "value", {}
    ).get("operation_contract_ref"):
        issues.append("operation_kind_contract_mismatch")
    territories = {
        operation_value.get("effect_territory_ref"),
        invocation_value.get("effect_territory_ref"),
        grant_value.get("allowed_effect_territory_ref"),
    }
    if len(territories) != 1:
        issues.append("effect_territory_mismatch")
    return issues


def event_issues(
    event: Mapping[str, object], records: Mapping[str, Mapping[str, object]]
) -> list[str]:
    issues: list[str] = []
    value = event.get("value")
    if event.get("sort") != "FrameworkEvent" or not isinstance(value, Mapping):
        return ["event_wrong_sort"]
    event_kind = value.get("event_kind_ref")
    if event_kind not in EVENT_KINDS:
        return ["unknown_event_kind"]
    payload = records.get(str(value.get("payload_ref")))
    if payload is None or digest(payload) != value.get("payload_sha256"):
        issues.append("event_payload_binding_mismatch")
        return issues
    scope = value.get("scope_class")
    occurrence_ref = value.get("occurrence_ref_or_none")
    claim_ref = value.get("claim_ref_or_none")
    claim_judgment_ref = value.get("claim_judgment_ref_or_none")
    if scope not in EVENT_SCOPES:
        issues.append("unknown_event_scope")
    if event_kind.endswith(":claim-admission"):
        if payload.get("sort") != "RelationClaim" or payload["id"] != claim_ref:
            issues.append("claim_event_payload_mismatch")
        claim_judgment = records.get(str(claim_judgment_ref))
        if claim_judgment is None or claim_judgment.get("subject") != claim_ref:
            issues.append("claim_event_judgment_mismatch")
        if payload["value"].get("source_frontier_ref") != value.get(
            "source_frontier_ref"
        ):
            issues.append("claim_event_frontier_mismatch")
    elif event_kind.endswith(":occurrence-admission"):
        if (
            payload.get("sort") != "Occurrence"
            or scope != "occurrence_scoped"
            or occurrence_ref != payload["id"]
        ):
            issues.append("occurrence_event_binding_mismatch")
        if claim_ref is not None or claim_judgment_ref is not None:
            issues.append("occurrence_event_has_claim")
    elif event_kind.endswith(":effect-disposition"):
        invocation = records.get(
            str(payload.get("value", {}).get("invocation_ref_or_none"))
        )
        if (
            payload.get("sort") != "EffectDisposition"
            or scope != "occurrence_scoped"
            or invocation is None
        ):
            issues.append("effect_event_payload_mismatch")
        elif occurrence_ref != invocation.get("value", {}).get("occurrence_ref"):
            issues.append("effect_event_occurrence_mismatch")
        if claim_ref is not None or claim_judgment_ref is not None:
            issues.append("effect_event_has_claim")
    else:
        if payload.get("sort") == "FrameworkEvent" or scope not in {
            "subject_scoped",
            "authority_scoped",
        }:
            issues.append("external_event_payload_or_scope_mismatch")
        if (
            occurrence_ref is not None
            or claim_ref is not None
            or claim_judgment_ref is not None
        ):
            issues.append("external_event_has_forbidden_binding")
    if scope == "occurrence_scoped" and occurrence_ref is None:
        issues.append("missing_occurrence_scope")
    if scope in {"subject_scoped", "authority_scoped"} and occurrence_ref is not None:
        issues.append("fabricated_occurrence_scope")
    return issues


def semantic_cut_fixture() -> dict[str, Any]:
    source = semantic_object(
        "urn:fixture:frontier:0",
        "EventFrontier",
        {
            "event_set_identity": "urn:fixture:event-set:0",
            "member_event_refs": [],
            "projection_basis_ref": "urn:fixture:projection-basis",
            "precedence_law_ref": "urn:fixture:precedence-law",
        },
    )
    claim_qualifiers = relation_qualifiers("supports_event")
    claim = semantic_object(
        "urn:fixture:claim",
        "RelationClaim",
        {
            "relation_kind_ref": "supports_event",
            "source_ref": "urn:fixture:source",
            "target_ref": "urn:fixture:target",
            "relation_qualifiers": claim_qualifiers,
            "claimant_ref": "urn:fixture:claimant",
            "claim_basis_ref": BASIS,
            "source_frontier_ref": source["id"],
        },
    )
    claim_judgment = judgment("urn:fixture:judgment:claim", "claim_admission", claim)
    event = semantic_object(
        "urn:fixture:event",
        "FrameworkEvent",
        {
            "event_kind_ref": "urn:stdo:traversal-occurrence:event-kind:claim-admission",
            "payload_ref": claim["id"],
            "payload_sha256": digest(claim),
            "scope_class": "authority_scoped",
            "occurrence_ref_or_none": None,
            "claim_ref_or_none": claim["id"],
            "claim_judgment_ref_or_none": claim_judgment["id"],
            "source_frontier_ref": source["id"],
        },
    )
    event_judgment = judgment("urn:fixture:judgment:event", "event_admission", event)
    relation_preimage = {
        "claim_ref": claim["id"],
        "claim_judgment_ref": claim_judgment["id"],
        "event_ref": event["id"],
        "event_judgment_ref": event_judgment["id"],
        "profile_basis": BASIS,
    }
    relation = typed_relation(
        "urn:fixture:materialized:" + digest(relation_preimage),
        claim["value"]["relation_kind_ref"],
        claim["value"]["source_ref"],
        claim["value"]["target_ref"],
        claim["value"]["relation_qualifiers"],
    )
    successor = semantic_object(
        "urn:fixture:frontier:1",
        "EventFrontier",
        {
            "event_set_identity": "urn:fixture:event-set:1",
            "member_event_refs": [event["id"]],
            "projection_basis_ref": source["value"]["projection_basis_ref"],
            "precedence_law_ref": source["value"]["precedence_law_ref"],
        },
    )
    cut = semantic_object(
        "urn:fixture:semantic-cut",
        "SemanticAdmissionCut",
        {
            "claim_ref": claim["id"],
            "claim_judgment_ref": claim_judgment["id"],
            "event_ref": event["id"],
            "event_judgment_ref": event_judgment["id"],
            "materialized_relation_ref": relation["id"],
            "source_frontier_ref": source["id"],
            "successor_frontier_ref": successor["id"],
        },
    )
    cut_judgment = judgment("urn:fixture:judgment:cut", "semantic_cut_admission", cut)
    edges = [
        typed_relation(
            "urn:fixture:edge:admits", "admits_claim", event["id"], claim["id"]
        ),
        typed_relation(
            "urn:fixture:edge:materializes",
            "materializes_relation",
            event["id"],
            relation["id"],
        ),
        typed_relation(
            "urn:fixture:edge:frontier",
            "frontier_contains",
            successor["id"],
            event["id"],
        ),
    ]
    return {
        "source_frontier": source,
        "claim": claim,
        "claim_judgment": claim_judgment,
        "event": event,
        "event_judgment": event_judgment,
        "relation": relation,
        "successor_frontier": successor,
        "cut": cut,
        "cut_judgment": cut_judgment,
        "edges": edges,
    }


def judgment_issues(
    record: Mapping[str, object], kind: str, subject: Mapping[str, object]
) -> list[str]:
    expected_fields = {
        "id",
        "kind",
        "subject",
        "subject_digest",
        "context",
        "owner",
        "scope",
        "basis",
        "evaluator",
        "authority",
        "decision",
        "evidence",
        "provenance",
        "decided_at",
    }
    issues: list[str] = []
    if set(record) != expected_fields:
        issues.append("judgment_shape_mismatch")
    if record.get("kind") != kind:
        issues.append("judgment_kind_mismatch")
    if record.get("subject") != subject.get("id") or record.get(
        "subject_digest"
    ) != digest(subject):
        issues.append("judgment_subject_binding_mismatch")
    if record.get("basis") != subject.get("basis"):
        issues.append("judgment_basis_mismatch")
    if record.get("decision") != "admitted":
        issues.append("judgment_not_admitted")
    return issues


def semantic_cut_issues(bundle: Mapping[str, Any]) -> list[str]:
    required = {
        "source_frontier",
        "claim",
        "claim_judgment",
        "event",
        "event_judgment",
        "relation",
        "successor_frontier",
        "cut",
        "cut_judgment",
        "edges",
    }
    if set(bundle) != required:
        return ["incomplete_semantic_cut"]
    claim, event, cut = bundle["claim"], bundle["event"], bundle["cut"]
    issues = []
    cut_records = [record for name, record in bundle.items() if name != "edges"]
    cut_record_identities = [record.get("id") for record in cut_records]
    if not all(absolute_uri(identity) for identity in cut_record_identities):
        issues.append("semantic_cut_record_identity_invalid")
    if len(cut_record_identities) != len(set(cut_record_identities)):
        issues.append("semantic_cut_record_identity_collision")
    issues.extend(judgment_issues(bundle["claim_judgment"], "claim_admission", claim))
    issues.extend(judgment_issues(bundle["event_judgment"], "event_admission", event))
    issues.extend(
        judgment_issues(bundle["cut_judgment"], "semantic_cut_admission", cut)
    )
    records = {
        str(record["id"]): record for name, record in bundle.items() if name != "edges"
    }
    issues.extend(event_issues(event, records))
    cut_value, claim_value, event_value = cut["value"], claim["value"], event["value"]
    source_refs = {
        claim_value.get("source_frontier_ref"),
        event_value.get("source_frontier_ref"),
        cut_value.get("source_frontier_ref"),
    }
    if len(source_refs) != 1:
        issues.append("source_frontier_mismatch")
    exact_refs = {
        "claim_ref": claim["id"],
        "claim_judgment_ref": bundle["claim_judgment"]["id"],
        "event_ref": event["id"],
        "event_judgment_ref": bundle["event_judgment"]["id"],
        "materialized_relation_ref": bundle["relation"]["id"],
        "source_frontier_ref": bundle["source_frontier"]["id"],
        "successor_frontier_ref": bundle["successor_frontier"]["id"],
    }
    if any(cut_value.get(field) != expected for field, expected in exact_refs.items()):
        issues.append("semantic_cut_ref_mismatch")
    source_members = bundle["source_frontier"]["value"].get("member_event_refs")
    successor_members = bundle["successor_frontier"]["value"].get("member_event_refs")
    if (
        not isinstance(source_members, list)
        or len(source_members) != len(set(source_members))
        or event["id"] in source_members
        or not isinstance(successor_members, list)
        or len(successor_members) != len(set(successor_members))
        or successor_members != sorted([*source_members, event["id"]])
    ):
        issues.append("successor_frontier_mismatch")
    frontier_values = [
        bundle[name]["value"] for name in ("source_frontier", "successor_frontier")
    ]
    if len({value.get("projection_basis_ref") for value in frontier_values}) != 1:
        issues.append("frontier_projection_basis_mismatch")
    if len({value.get("precedence_law_ref") for value in frontier_values}) != 1:
        issues.append("frontier_precedence_law_mismatch")
    if len({record.get("basis") for record in records.values()}) != 1:
        issues.append("semantic_cut_basis_mismatch")
    relation = bundle["relation"]
    issues.extend(
        qualifier_issues(
            claim_value.get("relation_qualifiers"),
            str(claim_value.get("relation_kind_ref")),
        )
    )
    if (
        relation.get("kind") != claim_value.get("relation_kind_ref")
        or relation.get("source") != claim_value.get("source_ref")
        or relation.get("target") != claim_value.get("target_ref")
        or relation.get("qualifiers") != claim_value.get("relation_qualifiers")
        or relation.get("basis") != claim.get("basis")
    ):
        issues.append("materialized_relation_mismatch")
    relation_preimage = {
        "claim_ref": claim["id"],
        "claim_judgment_ref": bundle["claim_judgment"]["id"],
        "event_ref": event["id"],
        "event_judgment_ref": bundle["event_judgment"]["id"],
        "profile_basis": BASIS,
    }
    if relation.get("id") != "urn:fixture:materialized:" + digest(relation_preimage):
        issues.append("materialized_relation_identity_mismatch")
    edges = bundle.get("edges")
    if not isinstance(edges, list):
        issues.append("required_edge_population_missing")
    else:
        edge_identities = [edge.get("id") for edge in edges]
        if not all(absolute_uri(identity) for identity in edge_identities):
            issues.append("semantic_cut_edge_identity_invalid")
        if len([*cut_record_identities, *edge_identities]) != len(
            set([*cut_record_identities, *edge_identities])
        ):
            issues.append("semantic_cut_global_identity_collision")
        issues.extend(relation_population_issues([relation, *edges]))
        required_edges = [
            ("admits_claim", event["id"], claim["id"]),
            ("materializes_relation", event["id"], relation["id"]),
            (
                "frontier_contains",
                bundle["successor_frontier"]["id"],
                event["id"],
            ),
        ]
        actual_edges = [
            (edge.get("kind"), edge.get("source"), edge.get("target")) for edge in edges
        ]
        if sorted(actual_edges) != sorted(required_edges):
            issues.append("required_edge_population_mismatch")
    return issues


def admit_semantic_cut(
    bundle: Mapping[str, Any], seen: dict[tuple[object, ...], str]
) -> str:
    issues = semantic_cut_issues(bundle)
    if issues:
        return "refused:" + issues[0]
    key = (
        bundle["claim"]["id"],
        bundle["claim_judgment"]["id"],
        bundle["event_judgment"]["id"],
        bundle["source_frontier"]["id"],
        bundle["cut"]["basis"],
        bundle["cut_judgment"]["authority"],
    )
    candidate_digest = digest(bundle)
    prior = seen.get(key)
    if prior is not None:
        return "idempotent" if prior == candidate_digest else "refuse_duplicate"
    seen[key] = candidate_digest
    return "admitted"


def installed_manifest(members: list[dict[str, str]]) -> dict[str, object]:
    return {
        "kind": "stdo.installed-release-manifest",
        "schema_version": 1,
        "standards": {"member_count": len(members), "members": members},
    }


def manifest_member_issues(
    manifest: object, member_path: str, member_sha256: str
) -> list[str]:
    if not isinstance(manifest, Mapping):
        return ["manifest_not_object"]
    issues: list[str] = []
    if (
        manifest.get("kind") != "stdo.installed-release-manifest"
        or manifest.get("schema_version") != 1
    ):
        issues.append("manifest_kind_or_schema_mismatch")
    standards = manifest.get("standards")
    if not isinstance(standards, Mapping) or not isinstance(
        standards.get("members"), list
    ):
        return [*issues, "manifest_members_missing"]
    members = standards["members"]
    if standards.get("member_count") != len(members):
        issues.append("manifest_member_count_mismatch")
    matches = [member for member in members if member.get("path") == member_path]
    if len(matches) != 1 or matches[0].get("sha256") != member_sha256:
        issues.append("member_not_exact_manifest_member")
    return issues


def basis_fixture() -> tuple[dict[str, object], bytes, bytes, dict[str, object], str]:
    release_uri = "stdo://releases/v2.5.0-rc.1/"
    predecessor_uri = PREDECESSOR_RELEASE_URI
    member_uri = release_uri + PROFILE_MEMBER_PATH
    calculus_member_path = "standards/AXIOMATIC_CALCULUS.md"
    calculus_member_uri = release_uri + calculus_member_path
    member_digest = "sha256:" + sha256(STANDARD)
    calculus_member_bytes = CALCULUS.read_bytes()
    calculus_member_digest = hashlib.sha256(calculus_member_bytes).hexdigest()
    derivation_member_bytes = {
        path: installed_standard_bytes(path) for path in PREDECESSOR_MEMBER_SHA256
    }
    predecessor_manifest_path = INSTALLED_RC3 / "manifest.json"
    if not predecessor_manifest_path.is_file():
        raise AssertionError(
            f"missing installed RC3 manifest: {predecessor_manifest_path}"
        )
    predecessor_manifest_bytes = predecessor_manifest_path.read_bytes()
    if hashlib.sha256(predecessor_manifest_bytes).hexdigest() != (
        INSTALLED_RC3_MANIFEST_SHA256
    ):
        raise AssertionError("installed RC3 manifest identity mismatch")
    manifest = installed_manifest(
        [
            {"path": calculus_member_path, "sha256": calculus_member_digest},
            {
                "path": PROFILE_MEMBER_PATH,
                "sha256": member_digest.removeprefix("sha256:"),
            },
        ]
    )
    manifest_bytes = jcs(manifest)
    calculus_basis_record = {
        "kind": "stdo.axiomatic-calculus-basis",
        "schema_version": 1,
        "concept_identity": "urn:stdo:concept:axiomatic-calculus:a-c",
        "derivation_basis": {
            "release_uri": predecessor_uri,
            "manifest_sha256": "sha256:"
            + hashlib.sha256(predecessor_manifest_bytes).hexdigest(),
            "principle_refs": sorted(
                [
                    f"{predecessor_uri}standards/{target}"
                    for target in EXPECTED_CALCULUS_DERIVATION_TARGETS
                ],
                key=utf16_key,
            ),
        },
        "publication_basis": {
            "release_uri": release_uri,
            "manifest_sha256": digest(manifest),
            "member_uri": calculus_member_uri,
            "member_sha256": "sha256:" + calculus_member_digest,
        },
    }
    calculus_basis_bytes = jcs(calculus_basis_record)
    calculus_basis = (
        "urn:stdo:axiomatic-calculus-basis:sha256:"
        + hashlib.sha256(calculus_basis_bytes).hexdigest()
    )
    signature = {
        "kind": "stdo.traversal-occurrence-signature",
        "schema_version": 1,
        "calculus_basis_identity": calculus_basis,
        "calculus_signature_schema_clause_ref": calculus_member_uri + "#core-signature",
        "occurrence_signature_clause_refs": [
            member_uri + fragment for fragment in SIGNATURE_FRAGMENTS
        ],
        "profile_member_sha256": member_digest,
    }
    basis = {
        "kind": "stdo.traversal-occurrence-profile-basis",
        "schema_version": 1,
        "concept_identity": "urn:stdo:concept:traversal-occurrence-profile",
        "calculus_basis_identity": calculus_basis,
        "occurrence_signature": signature,
        "occurrence_signature_sha256": digest(signature),
        "publication_basis": {
            "release_uri": release_uri,
            "manifest_sha256": digest(manifest),
            "member_uri": member_uri,
            "member_sha256": member_digest,
        },
    }
    basis_bytes = jcs(basis)
    identity = (
        "urn:stdo:traversal-occurrence-profile-basis:sha256:"
        + hashlib.sha256(basis_bytes).hexdigest()
    )
    resolution = {
        "calculus_basis_bytes": calculus_basis_bytes,
        "calculus_member_bytes": calculus_member_bytes,
        "calculus_publication_manifest_bytes": manifest_bytes,
        "calculus_derivation_manifest_bytes": predecessor_manifest_bytes,
        "calculus_derivation_member_bytes": derivation_member_bytes,
    }
    return basis, basis_bytes, manifest_bytes, resolution, identity


def imported_calculus_basis_issues(
    expected_identity: object, resolution: Mapping[str, object]
) -> tuple[list[str], Mapping[str, object] | None]:
    required_resolution = {
        "calculus_basis_bytes",
        "calculus_member_bytes",
        "calculus_publication_manifest_bytes",
        "calculus_derivation_manifest_bytes",
        "calculus_derivation_member_bytes",
    }
    if set(resolution) != required_resolution:
        return (["incomplete_calculus_resolution"], None)
    byte_keys = required_resolution - {"calculus_derivation_member_bytes"}
    if any(not isinstance(resolution.get(key), bytes) for key in byte_keys):
        return (["invalid_calculus_resolution_bytes"], None)
    derivation_member_bytes = resolution.get("calculus_derivation_member_bytes")
    if not isinstance(derivation_member_bytes, Mapping) or any(
        not isinstance(path, str) or not isinstance(member_bytes, bytes)
        for path, member_bytes in derivation_member_bytes.items()
    ):
        return (["invalid_calculus_derivation_member_bytes"], None)
    calculus_basis_bytes = resolution["calculus_basis_bytes"]
    publication_manifest_bytes = resolution["calculus_publication_manifest_bytes"]
    derivation_manifest_bytes = resolution["calculus_derivation_manifest_bytes"]
    calculus_member_bytes = resolution["calculus_member_bytes"]
    assert isinstance(calculus_basis_bytes, bytes)
    assert isinstance(publication_manifest_bytes, bytes)
    assert isinstance(derivation_manifest_bytes, bytes)
    assert isinstance(calculus_member_bytes, bytes)
    try:
        basis = parse_unique_json(calculus_basis_bytes)
        publication_manifest = parse_unique_json(publication_manifest_bytes)
        derivation_manifest = parse_unique_json(derivation_manifest_bytes)
    except (ValueError, json.JSONDecodeError):
        return (["invalid_calculus_resolution_json"], None)
    if not isinstance(basis, Mapping):
        return (["calculus_basis_not_object"], None)
    if not isinstance(derivation_manifest, Mapping):
        return (["calculus_derivation_manifest_invalid"], basis)
    issues: list[str] = []
    expected_basis_keys = {
        "kind",
        "schema_version",
        "concept_identity",
        "derivation_basis",
        "publication_basis",
    }
    if set(basis) != expected_basis_keys or jcs(basis) != calculus_basis_bytes:
        issues.append("calculus_basis_shape_or_jcs_mismatch")
    calculated_identity = (
        "urn:stdo:axiomatic-calculus-basis:sha256:"
        + hashlib.sha256(calculus_basis_bytes).hexdigest()
    )
    if expected_identity != calculated_identity:
        issues.append("calculus_basis_identity_mismatch")
    if (
        basis.get("kind") != "stdo.axiomatic-calculus-basis"
        or basis.get("schema_version") != 1
        or basis.get("concept_identity") != "urn:stdo:concept:axiomatic-calculus:a-c"
    ):
        issues.append("calculus_basis_kind_schema_or_concept_mismatch")
    derivation = basis.get("derivation_basis")
    publication = basis.get("publication_basis")
    if not isinstance(derivation, Mapping) or not isinstance(publication, Mapping):
        return ([*issues, "calculus_basis_boundary_missing"], basis)
    if set(derivation) != {"release_uri", "manifest_sha256", "principle_refs"}:
        issues.append("calculus_derivation_shape_mismatch")
    if set(publication) != {
        "release_uri",
        "manifest_sha256",
        "member_uri",
        "member_sha256",
    }:
        issues.append("calculus_publication_shape_mismatch")
    derivation_uri = derivation.get("release_uri")
    publication_uri = publication.get("release_uri")
    if (
        not isinstance(derivation_uri, str)
        or RELEASE_URI_RE.fullmatch(derivation_uri) is None
        or not isinstance(publication_uri, str)
        or RELEASE_URI_RE.fullmatch(publication_uri) is None
        or derivation_uri == publication_uri
    ):
        issues.append("calculus_release_boundary_invalid")
    if derivation_uri != PREDECESSOR_RELEASE_URI:
        issues.append("calculus_derivation_release_mismatch")
    if (
        derivation.get("manifest_sha256")
        != "sha256:" + hashlib.sha256(derivation_manifest_bytes).hexdigest()
    ):
        issues.append("calculus_derivation_manifest_mismatch")
    if hashlib.sha256(derivation_manifest_bytes).hexdigest() != (
        INSTALLED_RC3_MANIFEST_SHA256
    ):
        issues.append("calculus_derivation_manifest_not_exact_installed_rc3")
    derivation_release = derivation_manifest.get("release")
    if not isinstance(derivation_release, Mapping) or (
        derivation_release.get("cut") != "v2.4.3-rc.3"
    ):
        issues.append("calculus_derivation_manifest_release_mismatch")
    if (
        publication.get("manifest_sha256")
        != "sha256:" + hashlib.sha256(publication_manifest_bytes).hexdigest()
    ):
        issues.append("calculus_publication_manifest_mismatch")
    calculus_member_sha = hashlib.sha256(calculus_member_bytes).hexdigest()
    calculus_member_path = "standards/AXIOMATIC_CALCULUS.md"
    if (
        publication.get("member_uri") != f"{publication_uri}{calculus_member_path}"
        or publication.get("member_sha256") != "sha256:" + calculus_member_sha
    ):
        issues.append("calculus_member_binding_mismatch")
    issues.extend(
        f"calculus_publication:{issue}"
        for issue in manifest_member_issues(
            publication_manifest, calculus_member_path, calculus_member_sha
        )
    )
    try:
        derivation_section = (
            calculus_member_bytes.decode("utf-8")
            .split("## Derivation Provenance", 1)[1]
            .split("## Scope", 1)[0]
        )
        declared_targets = set(re.findall(r"\]\(([^)]+#[^)]+)\)", derivation_section))
    except (UnicodeDecodeError, IndexError):
        declared_targets = set()
    if declared_targets != EXPECTED_CALCULUS_DERIVATION_TARGETS:
        issues.append("calculus_member_derivation_set_mismatch")
    principle_refs = derivation.get("principle_refs")
    expected_principle_refs = sorted(
        (
            f"{derivation_uri}standards/{target}"
            for target in EXPECTED_CALCULUS_DERIVATION_TARGETS
        ),
        key=utf16_key,
    )
    if (
        not isinstance(principle_refs, list)
        or principle_refs != expected_principle_refs
        or principle_refs != sorted(principle_refs, key=utf16_key)
        or len(principle_refs) != len(set(principle_refs))
    ):
        issues.append("calculus_principle_refs_invalid")
    expected_member_paths = {
        target.split("#", 1)[0] for target in EXPECTED_CALCULUS_DERIVATION_TARGETS
    }
    if set(derivation_member_bytes) != expected_member_paths:
        issues.append("calculus_derivation_member_population_mismatch")
    if isinstance(derivation_manifest, Mapping):
        for member_path in sorted(expected_member_paths):
            member_bytes = derivation_member_bytes.get(member_path)
            if not isinstance(member_bytes, bytes):
                issues.append("calculus_derivation_member_missing")
                continue
            member_sha = hashlib.sha256(member_bytes).hexdigest()
            issues.extend(
                f"calculus_derivation:{issue}"
                for issue in manifest_member_issues(
                    derivation_manifest, member_path, member_sha
                )
            )
            expected_sha = PREDECESSOR_MEMBER_SHA256.get(member_path)
            if derivation_uri == PREDECESSOR_RELEASE_URI and expected_sha != member_sha:
                issues.append("calculus_derivation_member_bytes_mismatch")
        if isinstance(principle_refs, list):
            for principle_ref in principle_refs:
                parsed = urlsplit(principle_ref)
                base = principle_ref.removesuffix(f"#{parsed.fragment}")
                member_path = base.removeprefix(f"{derivation_uri}standards/")
                member_bytes = derivation_member_bytes.get(member_path)
                if (
                    not parsed.fragment
                    or not base.startswith(str(derivation_uri))
                    or not isinstance(member_bytes, bytes)
                    or parsed.fragment not in markdown_heading_fragments(member_bytes)
                ):
                    issues.append("calculus_principle_ref_unresolved")
                    break
    else:
        issues.append("calculus_derivation_manifest_invalid")
    return issues, basis


def profile_basis_issues(
    basis_bytes: bytes,
    manifest_bytes: bytes,
    calculus_resolution: Mapping[str, object],
) -> list[str]:
    issues: list[str] = []
    try:
        basis = parse_unique_json(basis_bytes)
        manifest = parse_unique_json(manifest_bytes)
    except (ValueError, json.JSONDecodeError):
        return ["non_unique_or_invalid_json"]
    if not isinstance(basis, Mapping) or not isinstance(manifest, Mapping):
        return ["basis_or_manifest_not_object"]
    try:
        if jcs(basis) != basis_bytes:
            issues.append("basis_not_exact_jcs")
    except ValueError:
        issues.append("basis_not_i_json")
    expected_basis_keys = {
        "kind",
        "schema_version",
        "concept_identity",
        "calculus_basis_identity",
        "occurrence_signature",
        "occurrence_signature_sha256",
        "publication_basis",
    }
    if set(basis) != expected_basis_keys:
        issues.append("basis_shape_mismatch")
    if (
        basis.get("kind") != "stdo.traversal-occurrence-profile-basis"
        or basis.get("schema_version") != 1
    ):
        issues.append("basis_kind_or_schema_mismatch")
    if basis.get("concept_identity") != "urn:stdo:concept:traversal-occurrence-profile":
        issues.append("concept_identity_mismatch")
    signature = basis.get("occurrence_signature")
    publication = basis.get("publication_basis")
    if not isinstance(signature, Mapping) or not isinstance(publication, Mapping):
        return [*issues, "missing_signature_or_publication"]
    expected_signature_keys = {
        "kind",
        "schema_version",
        "calculus_basis_identity",
        "calculus_signature_schema_clause_ref",
        "occurrence_signature_clause_refs",
        "profile_member_sha256",
    }
    if set(signature) != expected_signature_keys:
        issues.append("signature_shape_mismatch")
    if (
        signature.get("kind") != "stdo.traversal-occurrence-signature"
        or signature.get("schema_version") != 1
    ):
        issues.append("signature_kind_or_schema_mismatch")
    if signature.get("calculus_basis_identity") != basis.get("calculus_basis_identity"):
        issues.append("calculus_basis_mismatch")
    calculus_issues, calculus_basis = imported_calculus_basis_issues(
        basis.get("calculus_basis_identity"), calculus_resolution
    )
    issues.extend(calculus_issues)
    release_uri = publication.get("release_uri")
    member_uri = publication.get("member_uri")
    if (
        not isinstance(release_uri, str)
        or RELEASE_URI_RE.fullmatch(release_uri) is None
    ):
        issues.append("release_uri_not_immutable")
    if (
        not absolute_uri(member_uri)
        or member_uri != f"{release_uri}{PROFILE_MEMBER_PATH}"
    ):
        issues.append("member_uri_mismatch")
    calculus_publication = (
        calculus_basis.get("publication_basis")
        if isinstance(calculus_basis, Mapping)
        else None
    )
    calculus_member_uri = (
        calculus_publication.get("member_uri")
        if isinstance(calculus_publication, Mapping)
        else None
    )
    if (
        signature.get("calculus_signature_schema_clause_ref")
        != f"{calculus_member_uri}#core-signature"
    ):
        issues.append("calculus_clause_ref_mismatch")
    expected_clause_refs = [
        f"{member_uri}{fragment}" for fragment in SIGNATURE_FRAGMENTS
    ]
    if signature.get("occurrence_signature_clause_refs") != expected_clause_refs:
        issues.append("signature_clause_refs_mismatch")
    for field in ("manifest_sha256", "member_sha256"):
        if SHA256_RE.fullmatch(str(publication.get(field))) is None:
            issues.append(f"invalid_{field}")
    if SHA256_RE.fullmatch(str(signature.get("profile_member_sha256"))) is None:
        issues.append("invalid_signature_member_digest")
    if publication.get("member_sha256") != signature.get("profile_member_sha256"):
        issues.append("member_digest_mismatch")
    if publication.get("member_sha256") != "sha256:" + sha256(STANDARD):
        issues.append("member_bytes_mismatch")
    if basis.get("occurrence_signature_sha256") != digest(signature):
        issues.append("signature_digest_mismatch")
    if (
        publication.get("manifest_sha256")
        != "sha256:" + hashlib.sha256(manifest_bytes).hexdigest()
    ):
        issues.append("manifest_digest_mismatch")
    issues.extend(
        f"profile_publication:{issue}"
        for issue in manifest_member_issues(
            manifest, PROFILE_MEMBER_PATH, sha256(STANDARD)
        )
    )
    return issues


def adoption_issues(adoption: Mapping[str, object]) -> list[str]:
    required = {
        "profile_basis",
        "subject_binding",
        "vocabulary_mapping",
        "authorities",
        "frontier_law",
        "invalidation",
        "qualification_evidence",
    }
    return [f"missing:{key}" for key in sorted(required - set(adoption))]


def is_acyclic(edges: Iterable[tuple[str, str]]) -> bool:
    adjacency: dict[str, set[str]] = {}
    for source, target in edges:
        adjacency.setdefault(source, set()).add(target)
        adjacency.setdefault(target, set())
    active: set[str] = set()
    closed: set[str] = set()

    def visit(node: str) -> bool:
        if node in active:
            return False
        if node in closed:
            return True
        active.add(node)
        if not all(visit(target) for target in adjacency[node]):
            return False
        active.remove(node)
        closed.add(node)
        return True

    return all(visit(node) for node in adjacency)


class TraversalOccurrenceProfileTests(unittest.TestCase):
    def test_profile_boundary_and_exact_calculus_population(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        self.assertIn("urn:stdo:concept:traversal-occurrence-profile", text)
        self.assertIn("urn:stdo:bounded-context:traversal-occurrence-profile", text)
        self.assertIn(
            "Sigma_occurrence = instantiate_signature(b_ac, OccurrenceSignatureDefinition)",
            text,
        )
        self.assertIn("M_occ,b = (b, I, O, E, C, L, X, V, T, J)", text)
        self.assertIn("Population_M_occ = {", text)
        self.assertIn("RefDomain_Sigma_occurrence(record_kind, qualified_field)", text)
        for row in (
            "O:Occurrence.value.application_ref",
            "O:EffectOperation.value.operation_kind_ref",
            "O:SemanticAdmissionCut.value.materialized_relation_ref",
            "E:<each RelationKind>.source/target",
            "C:*.latitude_ref",
            "L:*.applies_to",
            "X:*.re_entry",
            "V:*.domain/codomain",
            "T:*.preservation_relation",
            "J:*.subject",
        ):
            self.assertIn(f"`{row}`", text)
        for record_kind, population in RECORD_POPULATIONS.items():
            self.assertIn(f"{record_kind} -> {population}", text)
        self.assertNotIn("record-kind:event", text)
        self.assertIn("Availability is not adoption", text)
        self.assertNotIn(
            "TRAVERSAL_OCCURRENCE_PROFILE", CALCULUS.read_text(encoding="utf-8")
        )

        populations = {kind: [] for kind in RECORD_POPULATIONS}
        populations[next(iter(RECORD_POPULATIONS))] = [{"id": "urn:fixture:local"}]
        self.assertEqual(
            population_issues(
                populations,
                {"urn:fixture:local", "urn:fixture:external"},
                {"urn:fixture:external"},
            ),
            [],
        )
        missing = dict(populations)
        missing.pop(next(iter(RECORD_POPULATIONS)))
        self.assertIn(
            "record_kind_population_not_total", population_issues(missing, set(), set())
        )
        duplicate = {kind: list(records) for kind, records in populations.items()}
        duplicate[list(RECORD_POPULATIONS)[1]] = [{"id": "urn:fixture:local"}]
        self.assertIn(
            "local_population_not_disjoint",
            population_issues(duplicate, {"urn:fixture:local"}, set()),
        )

    def test_finite_reference_domains_reject_family_sort_external_cardinality_and_basis_bypasses(
        self,
    ) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        sort_rows = re.findall(r"^\| `([^`]+)` \| ([^\n]+) \|$", text, re.MULTILINE)
        excluded = {"evidence_sha256_refs"}
        for sort, contract in sort_rows[:19]:
            fields = re.findall(r"`([^`]+)`", contract)
            for field in fields:
                if (
                    field.endswith(("_ref", "_refs", "_ref_or_none"))
                    or field in {"model_identity", "event_set_identity"}
                ) and field not in excluded:
                    self.assertIn(f"`O:{sort}.value.{field}`", text)

        for required in (
            "D_ext = {",
            "W_ext = {",
            "Q_ext = {",
            "for every d in D_ext and q in Q_ext:",
            "for every w in W_ext and q in Q_ext:",
            "external_resolution_witnesses[].domain_model",
            "external_resolution_witnesses[].codomain_model",
            "external_resolution_witnesses[].evidence",
        ):
            self.assertIn(required, text)
        for field in RESOLUTION_FIELDS:
            self.assertIn(f"ResolutionRefDomain({field})", text)
        self.assertEqual(len(expanded_transformation_external_ref_paths()), 45)

        resolution_targets = {
            "external_identity": ("MutableSubject", "B_adopted"),
            "reference_domain": ("Sigma:ReferenceDomain", "B_profile"),
            "external_target_kind": ("Sigma:ExternalTargetKind", "B_profile"),
            "resolved_target_identity": ("MutableSubject", "B_adopted"),
            "basis_relation": ("Sigma:BasisRelation", "B_profile"),
            "resolution_basis": ("ProductAdoptionBasis", "B_adopted"),
            "evidence_identity": ("Evidence", "B_adopted"),
        }
        for field, (target_kind, basis_relation) in resolution_targets.items():
            with self.subTest(resolution_field=field):
                ref = f"urn:fixture:resolution:{field}"
                resolution_domain = {
                    "cardinality": "1",
                    "local_families": set(),
                    "local_sorts": set(),
                    "external_kinds": {target_kind},
                    "basis": BASIS,
                    "basis_relation": basis_relation,
                }
                target = {ref: {"kind": target_kind, "basis_relation": basis_relation}}
                self.assertEqual(
                    reference_domain_issues(resolution_domain, [ref], {}, target),
                    [],
                )
                wrong_kind = {
                    ref: {"kind": "WrongKind", "basis_relation": basis_relation}
                }
                self.assertIn(
                    "reference_wrong_external_kind",
                    reference_domain_issues(resolution_domain, [ref], {}, wrong_kind),
                )
                wrong_basis = {ref: {"kind": target_kind, "basis_relation": "B_wrong"}}
                self.assertIn(
                    "reference_wrong_external_basis_relation",
                    reference_domain_issues(resolution_domain, [ref], {}, wrong_basis),
                )

        external_fixture = transformation_external_fixture()
        self.assertEqual(transformation_external_issues(external_fixture), [])
        external_mutations = {
            "missing-nested-field": lambda value: value["external_preserved"][0].pop(
                "reference_domain"
            ),
            "extra-nested-field": lambda value: value["external_removed"][
                0
            ].__setitem__("undeclared", "urn:fixture:undeclared"),
            "duplicate-coordinate": lambda value: value["external_introduced"].append(
                copy.deepcopy(value["external_introduced"][0])
            ),
            "missing-witness": lambda value: value[
                "external_resolution_witnesses"
            ].clear(),
            "changed-witness-resolution": lambda value: value[
                "external_resolution_witnesses"
            ][0]["codomain_resolution"].__setitem__(
                "resolved_target_identity", "urn:fixture:changed"
            ),
            "wrong-witness-decision": lambda value: value[
                "external_resolution_witnesses"
            ][0].__setitem__("decision", "equivalent"),
            "unresolved-witness-evidence": lambda value: value[
                "external_resolution_witnesses"
            ][0].__setitem__("evidence", "not-an-identity"),
        }
        for name, mutate in external_mutations.items():
            with self.subTest(external_coordinate=name):
                candidate = copy.deepcopy(external_fixture)
                mutate(candidate)
                self.assertTrue(transformation_external_issues(candidate))

        domain = {
            "cardinality": "1",
            "local_families": {"O"},
            "local_sorts": {"TraversalApplication"},
            "external_kinds": set(),
            "basis": BASIS,
            "basis_relation": "B_model",
        }
        valid = {
            "urn:fixture:application": {
                "family": "O",
                "sort": "TraversalApplication",
                "basis": BASIS,
            }
        }
        self.assertEqual(
            reference_domain_issues(domain, ["urn:fixture:application"], valid, {}),
            [],
        )
        bypasses = {
            "cardinality": (
                ["urn:fixture:application", "urn:fixture:other"],
                {**valid, "urn:fixture:other": valid["urn:fixture:application"]},
                {},
            ),
            "family": (
                ["urn:fixture:application"],
                {
                    "urn:fixture:application": {
                        **valid["urn:fixture:application"],
                        "family": "E",
                    }
                },
                {},
            ),
            "sort": (
                ["urn:fixture:application"],
                {
                    "urn:fixture:application": {
                        **valid["urn:fixture:application"],
                        "sort": "OperationKind",
                    }
                },
                {},
            ),
            "basis": (
                ["urn:fixture:application"],
                {
                    "urn:fixture:application": {
                        **valid["urn:fixture:application"],
                        "basis": "urn:wrong",
                    }
                },
                {},
            ),
            "external-kind": (
                ["urn:fixture:application"],
                {},
                {
                    "urn:fixture:application": {
                        "kind": "TraversalInput",
                        "basis_relation": "B_model",
                    }
                },
            ),
            "ambiguous": (
                ["urn:fixture:application"],
                valid,
                {
                    "urn:fixture:application": {
                        "kind": "TraversalInput",
                        "basis_relation": "B_model",
                    }
                },
            ),
        }
        for name, (refs, local, external) in bypasses.items():
            with self.subTest(name=name):
                self.assertTrue(reference_domain_issues(domain, refs, local, external))
        external_domain = {
            **domain,
            "local_families": set(),
            "local_sorts": set(),
            "external_kinds": {"TraversalInput"},
            "basis_relation": "B_adopted",
        }
        self.assertIn(
            "reference_wrong_external_basis_relation",
            reference_domain_issues(
                external_domain,
                ["urn:fixture:external-input"],
                {},
                {
                    "urn:fixture:external-input": {
                        "kind": "TraversalInput",
                        "basis_relation": "B_model",
                    }
                },
            ),
        )

    def test_occurrence_seed_and_all_mirroring_edges_are_exact(self) -> None:
        objects, edges = occurrence_fixture()
        self.assertEqual(occurrence_issues(objects, edges), [])
        occurrence = next(
            record for record in objects.values() if record["sort"] == "Occurrence"
        )
        application = next(
            record
            for record in objects.values()
            if record["sort"] == "TraversalApplication"
        )
        self.assertNotEqual(
            occurrence["id"],
            occurrence_identity(
                {
                    **occurrence_seed(occurrence["value"]),
                    "application": "urn:fixture:retry",
                }
            ),
        )
        with self.assertRaisesRegex(ValueError, "future_derived"):
            occurrence_identity(
                {
                    **occurrence_seed(occurrence["value"]),
                    "post_observation": "urn:future",
                }
            )

        mutations = {
            "application_of": lambda o, e: e.__setitem__(
                0, {**e[0], "target": "urn:wrong"}
            ),
            "application_traversal": lambda o, e: o[application["id"]][
                "value"
            ].__setitem__("traversal_ref", "urn:wrong"),
            "subject": lambda o, e: next(
                edge for edge in e if edge["kind"] == "bound_to_subject"
            ).__setitem__("target", "urn:wrong"),
            "dependency": lambda o, e: e.append(
                typed_relation(
                    "urn:extra", "identity_depends_on", occurrence["id"], "urn:extra"
                )
            ),
            "lineage": lambda o, e: next(
                edge for edge in e if edge["kind"] == "component_of_occurrence"
            ).__setitem__("source", "urn:wrong"),
            "duplicate-edge": lambda o, e: e.append(
                {**e[0], "id": "urn:fixture:duplicate-edge"}
            ),
            "duplicate-identity": lambda o, e: e.append(
                {
                    **typed_relation(
                        "urn:fixture:edge:0", "supports_event", "urn:a", "urn:b"
                    ),
                }
            ),
            "invalid-qualifier": lambda o, e: e[0].__setitem__(
                "qualifiers", {"preservation": "meaning_preserved"}
            ),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                bad_objects, bad_edges = copy.deepcopy(objects), copy.deepcopy(edges)
                mutate(bad_objects, bad_edges)
                self.assertTrue(occurrence_issues(bad_objects, bad_edges))

    def test_relation_kind_qualifier_contract_is_total_and_exact(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        contract_section = text.split(
            "`Cardinality_occurrence` is the following total function", 1
        )[1].split("Every relation and", 1)[0]
        declared = dict(
            re.findall(
                r"^\| `([^`]+)` \| `([^`]+)` \|$",
                contract_section,
                re.MULTILINE,
            )
        )
        self.assertEqual(declared, RELATION_CARDINALITY)

        valid_cardinalities = {
            "exactly_one",
            "zero_or_one",
            "zero_or_more",
            "one_or_more",
        }
        for kind, cardinality in RELATION_CARDINALITY.items():
            with self.subTest(kind=kind):
                qualifiers = relation_qualifiers(kind)
                self.assertEqual(qualifier_issues(qualifiers, kind), [])
                wrong_cardinality = copy.deepcopy(qualifiers)
                wrong_cardinality["cardinality"] = next(
                    value for value in valid_cardinalities if value != cardinality
                )
                self.assertIn(
                    "relation_cardinality_mismatch",
                    qualifier_issues(wrong_cardinality, kind),
                )

        common_falsifiers = {
            "preservation": ("preservation", "identity_preserved"),
            "loss": ("loss", "declared_loss"),
            "inverse": ("inverse_kind_ref_or_none", "supports_event"),
            "refusal": ("refusal", "not_applicable"),
        }
        for name, (field, value) in common_falsifiers.items():
            with self.subTest(common_qualifier=name):
                qualifiers = relation_qualifiers("admits_claim")
                qualifiers[field] = value
                self.assertTrue(qualifier_issues(qualifiers, "admits_claim"))

    def test_operation_instance_kind_subject_territory_and_grant_are_exact(
        self,
    ) -> None:
        objects, edges = operation_fixture()
        self.assertEqual(operation_issues(objects, edges), [])
        operation = next(
            record for record in objects.values() if record["sort"] == "EffectOperation"
        )
        invocation = next(
            record
            for record in objects.values()
            if record["sort"] == "EffectInvocation"
        )
        grant = next(
            record for record in objects.values() if record["sort"] == "OperationGrant"
        )
        operation_kind = next(
            record for record in objects.values() if record["sort"] == "OperationKind"
        )
        mutations = {
            "kind-edge": lambda o, e: next(
                edge for edge in e if edge["kind"] == "operation_of_kind"
            ).__setitem__("target", "urn:wrong"),
            "target-edge": lambda o, e: next(
                edge for edge in e if edge["kind"] == "targets_subject"
            ).__setitem__("target", "urn:wrong"),
            "grant-edge": lambda o, e: next(
                edge for edge in e if edge["kind"] == "authorized_by"
            ).__setitem__("target", "urn:wrong"),
            "operation-ref": lambda o, e: o[invocation["id"]]["value"].__setitem__(
                "operation_ref", "urn:wrong"
            ),
            "grant-kind": lambda o, e: o[grant["id"]]["value"].__setitem__(
                "allowed_operation_kind_refs", ["urn:wrong"]
            ),
            "territory": lambda o, e: o[operation["id"]]["value"].__setitem__(
                "effect_territory_ref", "urn:wrong"
            ),
            "operation-contract": lambda o, e: o[operation_kind["id"]][
                "value"
            ].__setitem__("operation_contract_ref", "urn:wrong-contract"),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                bad_objects, bad_edges = copy.deepcopy(objects), copy.deepcopy(edges)
                mutate(bad_objects, bad_edges)
                self.assertTrue(operation_issues(bad_objects, bad_edges))

    def test_closed_event_kinds_enforce_payload_digest_and_scope(self) -> None:
        bundle = semantic_cut_fixture()
        records = {
            record["id"]: record for name, record in bundle.items() if name != "edges"
        }
        self.assertEqual(event_issues(bundle["event"], records), [])
        self.assertEqual(len(EVENT_KINDS), 4)
        text = STANDARD.read_text(encoding="utf-8")
        for event_kind in EVENT_KINDS:
            self.assertIn(event_kind, text)

        bad = copy.deepcopy(bundle["event"])
        bad["value"]["event_kind_ref"] = "urn:fixture:unknown-event-kind"
        self.assertEqual(event_issues(bad, records), ["unknown_event_kind"])
        bad = copy.deepcopy(bundle["event"])
        bad["value"]["payload_sha256"] = "sha256:" + "0" * 64
        self.assertIn("event_payload_binding_mismatch", event_issues(bad, records))
        bad = copy.deepcopy(bundle["event"])
        bad["value"]["occurrence_ref_or_none"] = "urn:fictional"
        self.assertIn("fabricated_occurrence_scope", event_issues(bad, records))
        bad = copy.deepcopy(bundle["event"])
        bad["value"]["scope_class"] = "unknown_scope"
        self.assertIn("unknown_event_scope", event_issues(bad, records))

    def test_semantic_cut_uses_actual_judgments_and_conserves_frontiers(self) -> None:
        bundle = semantic_cut_fixture()
        self.assertEqual(semantic_cut_issues(bundle), [])
        seen: dict[tuple[object, ...], str] = {}
        self.assertEqual(admit_semantic_cut(bundle, seen), "admitted")
        self.assertEqual(admit_semantic_cut(bundle, seen), "idempotent")

        def collide_frontier_identities(candidate: dict[str, Any]) -> None:
            shared_identity = candidate["source_frontier"]["id"]
            candidate["successor_frontier"]["id"] = shared_identity
            candidate["cut"]["value"]["successor_frontier_ref"] = shared_identity
            frontier_edge = next(
                edge
                for edge in candidate["edges"]
                if edge["kind"] == "frontier_contains"
            )
            frontier_edge["source"] = shared_identity
            candidate["cut_judgment"]["subject_digest"] = digest(candidate["cut"])

        mutations = {
            "missing-cut-judgment": lambda b: b.pop("cut_judgment"),
            "claim-held": lambda b: b["claim_judgment"].__setitem__("decision", "hold"),
            "event-wrong-subject": lambda b: b["event_judgment"].__setitem__(
                "subject", "urn:wrong"
            ),
            "cut-wrong-digest": lambda b: b["cut_judgment"].__setitem__(
                "subject_digest", "sha256:" + "0" * 64
            ),
            "source-frontier": lambda b: b["event"]["value"].__setitem__(
                "source_frontier_ref", "urn:wrong"
            ),
            "successor-frontier": lambda b: b["successor_frontier"][
                "value"
            ].__setitem__("member_event_refs", []),
            "relation-endpoint": lambda b: b["relation"].__setitem__(
                "target", "urn:wrong"
            ),
            "missing-required-edge": lambda b: b["edges"].pop(),
            "reversed-required-edge": lambda b: b["edges"][0].update(
                {"source": b["claim"]["id"], "target": b["event"]["id"]}
            ),
            "duplicate-edge": lambda b: b["edges"].append(
                {**b["edges"][0], "id": "urn:fixture:duplicate-cut-edge"}
            ),
            "duplicate-edge-identity": lambda b: b["edges"].append(
                {
                    **typed_relation(
                        b["edges"][0]["id"],
                        "supports_event",
                        b["event"]["id"],
                        b["event"]["id"],
                    )
                }
            ),
            "invalid-claim-qualifier": lambda b: b["claim"]["value"].__setitem__(
                "relation_qualifiers", {"preservation": "meaning_preserved"}
            ),
            "invalid-edge-qualifier": lambda b: b["edges"][0].__setitem__(
                "qualifiers",
                {**relation_qualifiers("admits_claim"), "loss": "unknown"},
            ),
            "enum-valid-wrong-cardinality": lambda b: b["edges"][0][
                "qualifiers"
            ].__setitem__("cardinality", "zero_or_more"),
            "cross-basis-edge": lambda b: b["edges"][0].__setitem__(
                "basis", "urn:wrong-basis"
            ),
            "cross-basis-frontier": lambda b: b["successor_frontier"].__setitem__(
                "basis", "urn:wrong-basis"
            ),
            "frontier-projection-basis": lambda b: b["successor_frontier"][
                "value"
            ].__setitem__("projection_basis_ref", "urn:wrong-projection-basis"),
            "duplicate-frontier-member": lambda b: b["successor_frontier"][
                "value"
            ].__setitem__("member_event_refs", [b["event"]["id"], b["event"]["id"]]),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                bad = copy.deepcopy(bundle)
                mutate(bad)
                self.assertTrue(semantic_cut_issues(bad))

        exact_shape_and_identity_falsifiers = {
            "distinct-frontiers": (
                collide_frontier_identities,
                "semantic_cut_record_identity_collision",
            ),
            "edge-collides-with-subject": (
                lambda b: b["edges"][0].__setitem__("id", b["claim"]["id"]),
                "semantic_cut_global_identity_collision",
            ),
            "edge-extra-field": (
                lambda b: b["edges"][0].__setitem__("undeclared", "value"),
                "typed_relation_shape_mismatch",
            ),
            "edge-missing-owner": (
                lambda b: b["edges"][0].pop("owner"),
                "typed_relation_shape_mismatch",
            ),
            "edge-non-uri-id": (
                lambda b: b["edges"][0].__setitem__("id", "not-an-absolute-uri"),
                "semantic_cut_edge_identity_invalid",
            ),
            "relation-extra-field": (
                lambda b: b["relation"].__setitem__("undeclared", "value"),
                "typed_relation_shape_mismatch",
            ),
            "relation-missing-owner": (
                lambda b: b["relation"].pop("owner"),
                "typed_relation_shape_mismatch",
            ),
            "relation-non-uri-scope": (
                lambda b: b["relation"].__setitem__("scope", "not-an-absolute-uri"),
                "typed_relation_uri_mismatch:scope",
            ),
        }
        for name, (
            mutate,
            expected_issue,
        ) in exact_shape_and_identity_falsifiers.items():
            with self.subTest(name=name):
                bad = copy.deepcopy(bundle)
                mutate(bad)
                self.assertIn(expected_issue, semantic_cut_issues(bad))

        rival = copy.deepcopy(bundle)
        rival["relation"]["qualifiers"] = {"preservation": "identity_preserved"}
        self.assertEqual(
            admit_semantic_cut(rival, seen), "refused:materialized_relation_mismatch"
        )

    def test_basis_requires_exact_jcs_uris_digests_and_manifest_membership(
        self,
    ) -> None:
        basis, basis_bytes, manifest_bytes, resolution, identity = basis_fixture()

        def issues(
            candidate: Mapping[str, object] | bytes,
            candidate_manifest: bytes = manifest_bytes,
            candidate_resolution: Mapping[str, object] = resolution,
        ) -> list[str]:
            raw = candidate if isinstance(candidate, bytes) else jcs(candidate)
            return profile_basis_issues(raw, candidate_manifest, candidate_resolution)

        self.assertEqual(issues(basis_bytes), [])
        self.assertEqual(len(EXPECTED_CALCULUS_DERIVATION_TARGETS), 14)
        derivation_manifest_bytes = resolution["calculus_derivation_manifest_bytes"]
        self.assertIsInstance(derivation_manifest_bytes, bytes)
        self.assertEqual(
            hashlib.sha256(derivation_manifest_bytes).hexdigest(),
            INSTALLED_RC3_MANIFEST_SHA256,
        )
        derivation_manifest = parse_unique_json(derivation_manifest_bytes)
        self.assertEqual(derivation_manifest["release"]["cut"], "v2.4.3-rc.3")
        self.assertEqual(derivation_manifest["standards"]["member_count"], 47)
        self.assertEqual(
            derivation_manifest["standards"]["member_count"],
            len(derivation_manifest["standards"]["members"]),
        )
        derivation_section = (
            CALCULUS.read_text(encoding="utf-8")
            .split("## Derivation Provenance", 1)[1]
            .split("## Scope", 1)[0]
        )
        self.assertEqual(
            set(re.findall(r"\]\(([^)]+#[^)]+)\)", derivation_section)),
            EXPECTED_CALCULUS_DERIVATION_TARGETS,
        )
        derivation_members = resolution["calculus_derivation_member_bytes"]
        self.assertIsInstance(derivation_members, Mapping)
        for path, expected_sha in PREDECESSOR_MEMBER_SHA256.items():
            member_bytes = derivation_members[path]
            self.assertEqual(hashlib.sha256(member_bytes).hexdigest(), expected_sha)
            expected_fragments = {
                target.split("#", 1)[1]
                for target in EXPECTED_CALCULUS_DERIVATION_TARGETS
                if target.split("#", 1)[0] == path
            }
            self.assertLessEqual(
                expected_fragments, markdown_heading_fragments(member_bytes)
            )
        self.assertEqual(
            identity,
            "urn:stdo:traversal-occurrence-profile-basis:sha256:"
            + hashlib.sha256(basis_bytes).hexdigest(),
        )
        self.assertEqual(jcs({"b": "x", "a": [3, True]}), b'{"a":[3,true],"b":"x"}')
        with self.assertRaisesRegex(ValueError, "non_i_json"):
            jcs(9_007_199_254_740_992)
        with self.assertRaisesRegex(ValueError, "duplicate_object_name"):
            parse_unique_json(b'{"kind":1,"kind":2}')

        altered = copy.deepcopy(basis)
        altered["kind"] = "wrong"
        self.assertIn(
            "basis_kind_or_schema_mismatch",
            issues(altered),
        )
        altered = copy.deepcopy(basis)
        altered["publication_basis"]["release_uri"] = "stdo://mutable/latest/"
        self.assertIn(
            "release_uri_not_immutable",
            issues(altered),
        )
        altered = copy.deepcopy(basis)
        altered["occurrence_signature"]["occurrence_signature_clause_refs"] = altered[
            "occurrence_signature"
        ]["occurrence_signature_clause_refs"][:-1]
        self.assertIn(
            "signature_clause_refs_mismatch",
            issues(altered),
        )
        altered = copy.deepcopy(basis)
        altered["occurrence_signature_sha256"] = "sha256:" + "0" * 64
        self.assertIn(
            "signature_digest_mismatch",
            issues(altered),
        )
        pretty = json.dumps(basis, ensure_ascii=False, indent=2).encode()
        self.assertIn("basis_not_exact_jcs", issues(pretty))
        manifest = parse_unique_json(manifest_bytes)
        manifest["standards"]["members"] = manifest["standards"]["members"][:-1]
        altered = copy.deepcopy(basis)
        altered["publication_basis"]["manifest_sha256"] = digest(manifest)
        self.assertIn(
            "profile_publication:member_not_exact_manifest_member",
            issues(altered, jcs(manifest)),
        )

        incomplete_resolution = dict(resolution)
        incomplete_resolution.pop("calculus_basis_bytes")
        self.assertIn(
            "incomplete_calculus_resolution",
            issues(basis, candidate_resolution=incomplete_resolution),
        )
        wrong_member = dict(resolution)
        wrong_member["calculus_member_bytes"] += b"\n"
        self.assertIn(
            "calculus_member_binding_mismatch",
            issues(basis, candidate_resolution=wrong_member),
        )
        missing_member = dict(resolution)
        calculus_manifest = parse_unique_json(
            missing_member["calculus_publication_manifest_bytes"]
        )
        calculus_manifest["standards"]["members"] = [
            member
            for member in calculus_manifest["standards"]["members"]
            if member["path"] != "standards/AXIOMATIC_CALCULUS.md"
        ]
        calculus_manifest["standards"]["member_count"] = len(
            calculus_manifest["standards"]["members"]
        )
        missing_member["calculus_publication_manifest_bytes"] = jcs(calculus_manifest)
        self.assertIn(
            "calculus_publication:member_not_exact_manifest_member",
            issues(basis, candidate_resolution=missing_member),
        )
        missing_derivation_member = copy.deepcopy(resolution)
        missing_derivation_member["calculus_derivation_member_bytes"].pop(
            "IDENTITY_METHOD.md"
        )
        self.assertIn(
            "calculus_derivation_member_population_mismatch",
            issues(basis, candidate_resolution=missing_derivation_member),
        )
        changed_derivation_member = copy.deepcopy(resolution)
        changed_derivation_member["calculus_derivation_member_bytes"][
            "IDENTITY_METHOD.md"
        ] += b"\n"
        self.assertIn(
            "calculus_derivation_member_bytes_mismatch",
            issues(basis, candidate_resolution=changed_derivation_member),
        )

        subset_manifest = installed_manifest(
            [
                {
                    "path": path,
                    "sha256": hashlib.sha256(member_bytes).hexdigest(),
                }
                for path, member_bytes in sorted(derivation_members.items())
            ]
        )
        subset_manifest_bytes = jcs(subset_manifest)
        subset_resolution = copy.deepcopy(resolution)
        subset_resolution["calculus_derivation_manifest_bytes"] = subset_manifest_bytes
        subset_calculus_basis = parse_unique_json(
            subset_resolution["calculus_basis_bytes"]
        )
        subset_calculus_basis["derivation_basis"]["manifest_sha256"] = (
            "sha256:" + hashlib.sha256(subset_manifest_bytes).hexdigest()
        )
        subset_calculus_basis_bytes = jcs(subset_calculus_basis)
        subset_resolution["calculus_basis_bytes"] = subset_calculus_basis_bytes
        subset_calculus_identity = (
            "urn:stdo:axiomatic-calculus-basis:sha256:"
            + hashlib.sha256(subset_calculus_basis_bytes).hexdigest()
        )
        subset_profile_basis = copy.deepcopy(basis)
        subset_profile_basis["calculus_basis_identity"] = subset_calculus_identity
        subset_profile_basis["occurrence_signature"][
            "calculus_basis_identity"
        ] = subset_calculus_identity
        subset_profile_basis["occurrence_signature_sha256"] = digest(
            subset_profile_basis["occurrence_signature"]
        )
        self.assertIn(
            "calculus_derivation_manifest_not_exact_installed_rc3",
            issues(subset_profile_basis, candidate_resolution=subset_resolution),
        )
        same_carrier = dict(resolution)
        calculus_basis = parse_unique_json(same_carrier["calculus_basis_bytes"])
        calculus_basis["derivation_basis"]["release_uri"] = calculus_basis[
            "publication_basis"
        ]["release_uri"]
        same_carrier["calculus_basis_bytes"] = jcs(calculus_basis)
        self.assertIn(
            "calculus_release_boundary_invalid",
            issues(basis, candidate_resolution=same_carrier),
        )
        self.assertIn(
            "calculus_derivation_release_mismatch",
            issues(basis, candidate_resolution=same_carrier),
        )
        unresolved_principle = dict(resolution)
        calculus_basis = parse_unique_json(unresolved_principle["calculus_basis_bytes"])
        calculus_basis["derivation_basis"]["principle_refs"][0] = (
            calculus_basis["derivation_basis"]["release_uri"]
            + "standards/UNKNOWN.md#missing"
        )
        calculus_basis["derivation_basis"]["principle_refs"].sort(key=utf16_key)
        unresolved_principle["calculus_basis_bytes"] = jcs(calculus_basis)
        self.assertIn(
            "calculus_principle_ref_unresolved",
            issues(basis, candidate_resolution=unresolved_principle),
        )

        invented_fragment = copy.deepcopy(resolution)
        calculus_basis = parse_unique_json(invented_fragment["calculus_basis_bytes"])
        calculus_basis["derivation_basis"]["principle_refs"][0] = (
            calculus_basis["derivation_basis"]["release_uri"]
            + "standards/IDENTITY_METHOD.md#invented-but-absent"
        )
        calculus_basis["derivation_basis"]["principle_refs"].sort(key=utf16_key)
        forged_calculus_bytes = jcs(calculus_basis)
        invented_fragment["calculus_basis_bytes"] = forged_calculus_bytes
        forged_calculus_identity = (
            "urn:stdo:axiomatic-calculus-basis:sha256:"
            + hashlib.sha256(forged_calculus_bytes).hexdigest()
        )
        forged_profile_basis = copy.deepcopy(basis)
        forged_profile_basis["calculus_basis_identity"] = forged_calculus_identity
        forged_profile_basis["occurrence_signature"][
            "calculus_basis_identity"
        ] = forged_calculus_identity
        forged_profile_basis["occurrence_signature_sha256"] = digest(
            forged_profile_basis["occurrence_signature"]
        )
        invented_issues = issues(
            forged_profile_basis, candidate_resolution=invented_fragment
        )
        self.assertIn("calculus_principle_refs_invalid", invented_issues)
        self.assertIn("calculus_principle_ref_unresolved", invented_issues)

    def test_identity_and_causal_dags_do_not_collapse_typed_lineage(self) -> None:
        for edges in ([("basis", "occurrence")], [("o1", "o2")], [("e1", "e2")]):
            self.assertTrue(is_acyclic(edges))
            self.assertFalse(is_acyclic([*edges, (edges[-1][1], edges[0][0])]))
        wider = [("e1", "e2"), ("e2", "e1")]
        self.assertFalse(is_acyclic(wider))
        self.assertTrue(is_acyclic([]))  # no causal edge is implied by wider lineage

    def test_adoption_boundary_and_compressed_authority_stay_exact(self) -> None:
        adoption = {
            "profile_basis": BASIS,
            "subject_binding": "urn:fixture:binding-law",
            "vocabulary_mapping": "urn:fixture:mapping",
            "authorities": "urn:fixture:authorities",
            "frontier_law": "urn:fixture:frontier-law",
            "invalidation": "urn:fixture:invalidation",
            "qualification_evidence": "urn:fixture:qualification",
        }
        self.assertEqual(adoption_issues(adoption), [])
        adoption.pop("authorities")
        self.assertEqual(adoption_issues(adoption), ["missing:authorities"])

        text = STANDARD.read_text(encoding="utf-8")
        for forbidden in ("ABIogenesis", "ABG", "HoG", "GTL", "Worker", "GraphCall"):
            self.assertNotIn(forbidden, text)
        product = PRODUCT.read_text(encoding="utf-8")
        self.assertIn("## Traversal Occurrence Profile", product)
        self.assertIn("Profile availability is not Product adoption", product)
        compression = COMPRESSION.read_text(encoding="utf-8")
        match = re.search(r"^source_digest: ([0-9a-f]{64})$", compression, re.MULTILINE)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), sha256(STANDARD))
        for required in (
            "RecordKind_ac",
            "EventKind_occurrence",
            "application_of",
            "cut judgments",
            "OperationKind",
            "RFC 8785",
            "exact profile member path",
            "D_ext",
            "Cardinality_occurrence",
            "fourteen",
        ):
            self.assertIn(required, compression)


if __name__ == "__main__":
    unittest.main()
