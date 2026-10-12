from __future__ import annotations

import hashlib
import json
import re
import unittest
from collections.abc import Mapping
from copy import deepcopy
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
STANDARD = ROOT / "specification/standards/AXIOMATIC_CALCULUS.md"
PRODUCT = ROOT / "specification/PRODUCT.md"
COMPRESSION = (
    ROOT
    / "specification/standards/authority_compressions/axiomatic_calculus.compressed.md"
)

CORE_POPULATIONS = {"O", "E", "C", "L", "X", "V", "T", "J"}
RECORD_KIND_BY_POPULATION = {
    "O": "urn:stdo:concept:axiomatic-calculus:record-kind:semantic-object",
    "E": "urn:stdo:concept:axiomatic-calculus:record-kind:typed-relation",
    "C": "urn:stdo:concept:axiomatic-calculus:record-kind:constraint",
    "L": "urn:stdo:concept:axiomatic-calculus:record-kind:latitude",
    "X": "urn:stdo:concept:axiomatic-calculus:record-kind:residual",
    "V": "urn:stdo:concept:axiomatic-calculus:record-kind:traversal",
    "T": "urn:stdo:concept:axiomatic-calculus:record-kind:transformation",
    "J": "urn:stdo:concept:axiomatic-calculus:record-kind:judgment",
}
EXTERNAL_RESOLUTION_FIELDS = {
    "external_identity",
    "reference_domain",
    "external_target_kind",
    "resolved_target_identity",
    "basis_relation",
    "resolution_basis",
    "evidence_identity",
}
TRANSFORMATION_FIELDS = {
    "id",
    "traversal",
    "domain_model",
    "codomain_model",
    "context",
    "owner",
    "scope",
    "basis",
    "operation_authority",
    "preconditions",
    "preservation_relation",
    "preserved",
    "introduced",
    "removed",
    "external_preserved",
    "external_introduced",
    "external_removed",
    "external_resolution_witnesses",
    "residuals",
    "evidence",
    "provenance",
    "stop_states",
    "invalidation",
    "re_entry",
}
RECORD_FIELDS_BY_POPULATION = {
    "O": {"id", "sort", "context", "owner", "scope", "basis", "value"},
    "E": {
        "id",
        "kind",
        "source",
        "target",
        "context",
        "owner",
        "scope",
        "basis",
        "qualifiers",
    },
    "C": {
        "id",
        "kind",
        "applies_to",
        "predicate",
        "context",
        "owner",
        "scope",
        "basis",
        "judgment_kind",
        "latitude_ref",
        "refusal",
    },
    "L": {
        "id",
        "applies_to",
        "allowed_variation",
        "forbidden_variation",
        "context",
        "owner",
        "scope",
        "basis",
        "invalidation",
    },
    "X": {
        "id",
        "subject",
        "kind",
        "uncertainty",
        "consequence",
        "context",
        "owner",
        "scope",
        "basis",
        "re_entry",
        "invalidation",
    },
    "V": {
        "id",
        "domain",
        "codomain",
        "context",
        "owner",
        "scope",
        "basis",
        "preconditions",
        "postconditions",
        "authority",
        "evidence",
        "provenance",
        "stop_states",
    },
    "T": TRANSFORMATION_FIELDS,
    "J": {
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
    },
}
REFERENCE_DOMAIN_FIELDS = {
    "cardinality",
    "allowed_local_record_kinds",
    "allowed_semantic_object_sorts",
    "allowed_external_target_kinds",
    "required_basis_relation",
}
MODEL_FIELDS = {
    "id",
    "basis",
    "signature",
    "canonical_record_grammar",
    "populations",
    "identities",
    "external_resolutions",
}
RECORD_KIND_TO_POPULATION = {
    record_kind: population
    for population, record_kind in RECORD_KIND_BY_POPULATION.items()
}
INSTALLED_RC3 = Path.home() / "Library/Application Support/STDO/releases/v2.4.3-rc.3"
INSTALLED_RC3_MANIFEST_SHA256 = (
    "312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551"
)
RELEASE_URI_RE = re.compile(
    r"stdo://releases/v(?![^/]*-rc\.[^/]*-rc\.)"
    r"[0-9A-Za-z][0-9A-Za-z._+-]*-rc\.[1-9][0-9]*/"
)
EXPECTED_DERIVATION_TARGETS = {
    "IDENTITY_METHOD.md#core-law",
    "IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004",
    "SPEC_METHOD.md#bounded-context-semantic-resolution",
    "REFERENCE_FRAME_METHOD.md#position",
    "REFERENCE_FRAME_METHOD.md#evaluation",
    "SPEC_METHOD.md#agentic-construction-execution-stdo-up-020",
    "SPEC_METHOD.md#ambiguity-governance-rule",
    "REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates",
    "REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation",
    "REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation",
    "REFERENCE_FRAME_METHOD.md#rf-012-closed-results",
    "SPEC_METHOD.md#constitutional-chain",
    "REFERENCE_FRAME_METHOD.md#reference-frame-laws",
    "SPEC_METHOD.md#one-constitutional-surface-and-version-boundary-stdo-surface-001",
}


def record_fixture(
    population: str,
    identity: str,
    basis: str = "urn:test:basis:1",
) -> dict[str, object]:
    common = {
        "id": identity,
        "context": "urn:test:context",
        "owner": "urn:test:owner",
        "scope": "urn:test:scope",
        "basis": basis,
    }
    fixtures: dict[str, dict[str, object]] = {
        "O": {**common, "sort": "concept", "value": {"name": identity}},
        "E": {
            **common,
            "kind": "urn:test:relation-kind",
            "source": "urn:test:source",
            "target": "urn:test:target",
            "qualifiers": {"direction": "source-to-target"},
        },
        "C": {
            **common,
            "kind": "urn:test:constraint-kind",
            "applies_to": "urn:test:subject",
            "predicate": {"operator": "equals"},
            "judgment_kind": "urn:test:judgment-kind",
            "latitude_ref": "urn:test:latitude",
            "refusal": "refusal",
        },
        "L": {
            **common,
            "applies_to": "urn:test:subject",
            "allowed_variation": [],
            "forbidden_variation": [],
            "invalidation": "urn:test:invalidation",
        },
        "X": {
            **common,
            "subject": "urn:test:subject",
            "kind": "urn:test:residual-kind",
            "uncertainty": "urn:test:uncertainty",
            "consequence": "urn:test:consequence",
            "re_entry": "urn:test:re-entry",
            "invalidation": "urn:test:invalidation",
        },
        "V": {
            **common,
            "domain": "urn:test:domain",
            "codomain": "urn:test:codomain",
            "preconditions": [],
            "postconditions": [],
            "authority": "urn:test:authority",
            "evidence": [],
            "provenance": [],
            "stop_states": ["refusal"],
        },
        "T": {
            **common,
            "traversal": "urn:test:traversal",
            "domain_model": "urn:test:model:before",
            "codomain_model": "urn:test:model:after",
            "operation_authority": "urn:test:authority",
            "preconditions": [],
            "preservation_relation": "urn:test:preservation-relation",
            "preserved": [],
            "introduced": [],
            "removed": [],
            "external_preserved": [],
            "external_introduced": [],
            "external_removed": [],
            "external_resolution_witnesses": [],
            "residuals": [],
            "evidence": [],
            "provenance": [],
            "stop_states": ["refusal"],
            "invalidation": "urn:test:invalidation",
            "re_entry": "urn:test:re-entry",
        },
        "J": {
            **common,
            "kind": "urn:test:judgment-kind",
            "subject": "urn:test:subject",
            "subject_digest": "sha256:" + "0" * 64,
            "evaluator": "urn:test:evaluator",
            "authority": "urn:test:authority",
            "decision": "accepted",
            "evidence": [],
            "provenance": [],
            "decided_at": "2026-08-30T00:00:00Z",
        },
    }
    return fixtures[population]


def record_structure_issues(population: str, record: object) -> list[str]:
    if not isinstance(record, Mapping):
        return [f"invalid_record:{population}"]
    issues: list[str] = []
    if set(record) != RECORD_FIELDS_BY_POPULATION[population]:
        issues.append(f"record_shape:{population}")
    for field in ("id", "context", "owner", "scope", "basis"):
        if not isinstance(record.get(field), str) or not record.get(field):
            issues.append(f"invalid_record_coordinate:{population}:{field}")
    return issues


def population_issues(populations: Mapping[str, object]) -> list[str]:
    issues = [
        f"missing_population:{name}" for name in CORE_POPULATIONS - populations.keys()
    ]
    issues.extend(
        f"unknown_population:{name}" for name in populations.keys() - CORE_POPULATIONS
    )
    seen: set[str] = set()
    for name, records in populations.items():
        if name not in CORE_POPULATIONS:
            continue
        if not isinstance(records, list):
            issues.append(f"invalid_population:{name}")
            continue
        for record in records:
            issues.extend(record_structure_issues(name, record))
            if not isinstance(record, Mapping):
                continue
            identity = record.get("id")
            if not isinstance(identity, str) or not identity:
                issues.append(f"missing_record_identity:{name}")
            elif identity in seen:
                issues.append(f"duplicate_record_identity:{identity}")
            else:
                seen.add(identity)
    return sorted(issues)


def model_population_issues(
    populations: Mapping[str, object],
    identities: set[str],
    external_resolutions: dict[str, dict[str, object]],
    model_basis: str,
) -> list[str]:
    issues = population_issues(populations)
    local: set[str] = set()
    for records in populations.values():
        if not isinstance(records, list):
            continue
        for record in records:
            if isinstance(record, Mapping) and isinstance(record.get("id"), str):
                local.add(str(record["id"]))
    external = set(external_resolutions)
    if local & external:
        issues.append("local_external_ambiguity")
    if identities != local | external:
        issues.append("identity_universe_not_closed")
    for population, records in populations.items():
        if population not in CORE_POPULATIONS or not isinstance(records, list):
            continue
        for record in records:
            if isinstance(record, Mapping) and record.get("basis") != model_basis:
                issues.append(f"record_basis_mismatch:{record.get('id')}")
    for identity, resolution in external_resolutions.items():
        if not isinstance(resolution, Mapping):
            issues.append(f"external_resolution_not_record:{identity}")
        elif set(resolution) != EXTERNAL_RESOLUTION_FIELDS:
            issues.append(f"external_resolution_shape:{identity}")
        elif resolution.get("external_identity") != identity:
            issues.append(f"external_resolution_identity:{identity}")
        elif any(
            not isinstance(resolution.get(field), str) or not resolution.get(field)
            for field in EXTERNAL_RESOLUTION_FIELDS
        ):
            issues.append(f"external_resolution_coordinate:{identity}")
        elif (
            resolution.get("basis_relation") == "same-basis"
            and resolution.get("resolution_basis") != model_basis
        ):
            issues.append(f"external_resolution_basis:{identity}")
    return sorted(issues)


def reference_issue(
    populations: dict[str, list[dict[str, str]]],
    reference: str,
    allowed_populations: set[str],
    allowed_sorts: set[str] | None = None,
) -> str | None:
    matches = [
        (name, record)
        for name, records in populations.items()
        for record in records
        if record.get("id") == reference
    ]
    if not matches:
        return "dangling_reference"
    if len(matches) != 1:
        return "ambiguous_reference"
    population, record = matches[0]
    if population not in allowed_populations:
        return "wrong_record_kind"
    if allowed_sorts is not None and record.get("sort") not in allowed_sorts:
        return "wrong_semantic_object_sort"
    return None


def reference_domain_issues(
    populations: dict[str, list[dict[str, object]]],
    references: list[str],
    domain: dict[str, object],
    external_resolutions: dict[str, dict[str, object]],
    source_basis: str,
    domain_identity: str,
) -> list[str]:
    issues: list[str] = []
    if set(domain) != REFERENCE_DOMAIN_FIELDS:
        issues.append("reference_domain_shape")
    cardinality = domain.get("cardinality")
    if cardinality == "exactly_one" and len(references) != 1:
        issues.append("cardinality_mismatch")
    elif cardinality == "zero_or_one" and len(references) > 1:
        issues.append("cardinality_mismatch")
    elif cardinality == "one_or_more" and not references:
        issues.append("cardinality_mismatch")
    elif cardinality not in {
        "exactly_one",
        "zero_or_one",
        "zero_or_more",
        "one_or_more",
    }:
        issues.append("unknown_cardinality")
    valid_reference_identities = all(
        isinstance(reference, str) and bool(reference) for reference in references
    )
    if not valid_reference_identities:
        issues.append("invalid_reference_identity")
    elif len(references) != len(set(references)):
        issues.append("duplicate_reference")

    domain_collections: dict[str, list[object]] = {}
    for field in (
        "allowed_local_record_kinds",
        "allowed_semantic_object_sorts",
        "allowed_external_target_kinds",
    ):
        value = domain.get(field)
        if not isinstance(value, list):
            issues.append(f"reference_domain_collection:{field}")
            domain_collections[field] = []
        else:
            domain_collections[field] = value
            valid_identities = all(
                isinstance(item, str) and bool(item) for item in value
            )
            if not valid_identities:
                issues.append(f"reference_domain_identity:{field}")
            elif len(value) != len(set(value)):
                issues.append(f"reference_domain_duplicates:{field}")
    allowed_record_kinds = {
        item
        for item in domain_collections["allowed_local_record_kinds"]
        if isinstance(item, str)
    }
    if not allowed_record_kinds <= set(RECORD_KIND_TO_POPULATION):
        issues.append("unknown_local_record_kind")
    allowed_populations = {
        RECORD_KIND_TO_POPULATION[kind]
        for kind in allowed_record_kinds & set(RECORD_KIND_TO_POPULATION)
    }
    allowed_sorts = {
        item
        for item in domain_collections["allowed_semantic_object_sorts"]
        if isinstance(item, str)
    }
    allowed_external = {
        item
        for item in domain_collections["allowed_external_target_kinds"]
        if isinstance(item, str)
    }
    required_basis = domain.get("required_basis_relation")
    if not isinstance(required_basis, str) or not required_basis:
        issues.append("invalid_required_basis_relation")
    for reference in references:
        if not isinstance(reference, str) or not reference:
            continue
        local_matches = [
            (population, record)
            for population, records in populations.items()
            for record in records
            if record.get("id") == reference
        ]
        external = external_resolutions.get(reference)
        if local_matches and external is not None:
            issues.append(f"local_external_ambiguity:{reference}")
            continue
        if len(local_matches) > 1:
            issues.append(f"ambiguous_local_reference:{reference}")
            continue
        if local_matches:
            population, record = local_matches[0]
            if population not in allowed_populations:
                issues.append(f"wrong_record_kind:{reference}")
            elif (
                population == "O"
                and allowed_sorts
                and record.get("sort") not in allowed_sorts
            ):
                issues.append(f"wrong_semantic_object_sort:{reference}")
            elif required_basis == "same-basis" and record.get("basis") != source_basis:
                issues.append(f"wrong_local_basis:{reference}")
            continue
        if external is None:
            issues.append(f"dangling_reference:{reference}")
        elif set(external) != EXTERNAL_RESOLUTION_FIELDS:
            issues.append(f"external_resolution_shape:{reference}")
        elif external.get("external_identity") != reference:
            issues.append(f"external_resolution_identity:{reference}")
        elif external.get("reference_domain") != domain_identity:
            issues.append(f"wrong_reference_domain:{reference}")
        elif external.get("external_target_kind") not in allowed_external:
            issues.append(f"wrong_external_target_kind:{reference}")
        elif external.get("basis_relation") != required_basis:
            issues.append(f"wrong_basis_relation:{reference}")
        elif (
            required_basis == "same-basis"
            and external.get("resolution_basis") != source_basis
        ):
            issues.append(f"wrong_resolution_basis:{reference}")
        elif any(
            not isinstance(external.get(field), str) or not external.get(field)
            for field in EXTERNAL_RESOLUTION_FIELDS
        ):
            issues.append(f"invalid_external_coordinate:{reference}")
    return sorted(issues)


def model_fixture_issues(model: object) -> list[str]:
    if not isinstance(model, Mapping):
        return ["model_not_record"]
    issues: list[str] = []
    if set(model) != MODEL_FIELDS:
        issues.append("model_shape")
    for field in ("id", "basis", "signature", "canonical_record_grammar"):
        if not isinstance(model.get(field), str) or not model.get(field):
            issues.append(f"model_coordinate:{field}")
    populations = model.get("populations")
    identities = model.get("identities")
    external_resolutions = model.get("external_resolutions")
    if not isinstance(populations, dict):
        issues.append("model_populations")
    if not isinstance(identities, set) or any(
        not isinstance(identity, str) or not identity for identity in identities
    ):
        issues.append("model_identities")
    if not isinstance(external_resolutions, dict):
        issues.append("model_external_resolutions")
    if (
        isinstance(populations, dict)
        and isinstance(identities, set)
        and isinstance(external_resolutions, dict)
        and isinstance(model.get("basis"), str)
    ):
        issues.extend(
            model_population_issues(
                populations,
                identities,
                external_resolutions,
                str(model["basis"]),
            )
        )
    return sorted(issues)


def local_record_map(
    model: Mapping[str, object],
) -> dict[str, tuple[str, Mapping[str, object]]]:
    result: dict[str, tuple[str, Mapping[str, object]]] = {}
    populations = model["populations"]
    assert isinstance(populations, Mapping)
    for population, records in populations.items():
        assert isinstance(population, str) and isinstance(records, list)
        for record in records:
            assert isinstance(record, Mapping) and isinstance(record.get("id"), str)
            result[str(record["id"])] = (population, record)
    return result


def transformation_issues(
    domain: dict[str, object],
    codomain: dict[str, object],
    transformation: dict[str, object],
    equality: dict[str, object] | None = None,
) -> list[str]:
    issues: list[str] = []
    if set(transformation) != TRANSFORMATION_FIELDS:
        issues.append("transformation_shape_mismatch")
    for field in (
        "id",
        "traversal",
        "operation_authority",
        "preservation_relation",
        "context",
        "owner",
        "scope",
        "basis",
    ):
        if not transformation.get(field):
            issues.append(f"missing_transformation_coordinate:{field}")
    for field in (
        "preconditions",
        "residuals",
        "evidence",
        "provenance",
        "stop_states",
    ):
        if not isinstance(transformation.get(field), list):
            issues.append(f"invalid_transformation_collection:{field}")
    if transformation.get("domain_model") != domain.get("id"):
        issues.append("domain_model_mismatch")
    if transformation.get("codomain_model") != codomain.get("id"):
        issues.append("codomain_model_mismatch")
    bases = {domain.get("basis"), codomain.get("basis"), transformation.get("basis")}
    if len(bases) != 1:
        issues.append("basis_mismatch")
    if domain.get("signature") != codomain.get("signature"):
        issues.append("signature_mismatch")

    model_errors: list[str] = []
    for label, model in (("domain", domain), ("codomain", codomain)):
        model_errors.extend(f"{label}_{issue}" for issue in model_fixture_issues(model))
    issues.extend(model_errors)
    if model_errors:
        return sorted(issues)
    domain_records = local_record_map(domain)
    codomain_records = local_record_map(codomain)
    preserved_values = transformation.get("preserved", [])
    removed_values = transformation.get("removed", [])
    introduced_values = transformation.get("introduced", [])
    if not all(
        isinstance(value, list)
        for value in (preserved_values, removed_values, introduced_values)
    ):
        return sorted([*issues, "invalid_local_delta_collection"])
    preserved = set(preserved_values)
    removed = set(removed_values)
    introduced = set(introduced_values)
    if any(
        len(value) != len(set(value))
        for value in (preserved_values, removed_values, introduced_values)
    ):
        issues.append("duplicate_local_delta_identity")
    if preserved & removed or set(domain_records) != preserved | removed:
        issues.append("invalid_domain_partition")
    if preserved & introduced or set(codomain_records) != preserved | introduced:
        issues.append("invalid_codomain_partition")
    if introduced & set(domain_records):
        issues.append("introduced_local_not_fresh")
    if removed & set(codomain_records):
        issues.append("removed_local_retained")

    for identity in preserved & domain_records.keys() & codomain_records.keys():
        before_population, before = domain_records[identity]
        after_population, after = codomain_records[identity]
        coordinates = ("id", "record_kind", "context", "owner", "scope", "basis")
        if before_population != after_population or any(
            before.get(field) != after.get(field)
            for field in coordinates
            if field != "record_kind"
        ):
            issues.append(f"preserved_coordinate_mismatch:{identity}")
            continue
        if domain.get("canonical_record_grammar") == codomain.get(
            "canonical_record_grammar"
        ) and jcs(before) == jcs(after):
            continue
        expected_equality = {
            "domain_model": str(domain["id"]),
            "codomain_model": str(codomain["id"]),
            "record_id": identity,
            "record_kind": RECORD_KIND_BY_POPULATION[before_population],
            "domain_basis": str(domain["basis"]),
            "codomain_basis": str(codomain["basis"]),
            "preservation_relation": str(transformation["preservation_relation"]),
            "decision": "equal",
        }
        if equality != expected_equality:
            issues.append(f"preserved_without_exact_equality:{identity}")

    domain_external = domain.get("external_resolutions", {})
    codomain_external = codomain.get("external_resolutions", {})
    if not isinstance(domain_external, dict) or not isinstance(codomain_external, dict):
        return sorted([*issues, "invalid_external_resolution_map"])
    resolution_maps: list[dict[bytes, Mapping[str, object]]] = []
    for resolutions in (domain_external, codomain_external):
        by_coordinate: dict[bytes, Mapping[str, object]] = {}
        for external_identity, resolution in resolutions.items():
            if not isinstance(resolution, Mapping):
                issues.append("invalid_external_resolution")
                continue
            if resolution.get("external_identity") != external_identity:
                issues.append(f"external_resolution_identity:{external_identity}")
            coordinate = jcs(resolution)
            if coordinate in by_coordinate:
                issues.append("duplicate_external_resolution")
            by_coordinate[coordinate] = resolution
        resolution_maps.append(by_coordinate)
    domain_resolution_by_coordinate, codomain_resolution_by_coordinate = resolution_maps
    external_values = (
        transformation.get("external_preserved", []),
        transformation.get("external_removed", []),
        transformation.get("external_introduced", []),
    )
    if not all(isinstance(value, list) for value in external_values):
        return sorted([*issues, "invalid_external_delta_collection"])
    external_coordinate_sets: list[set[bytes]] = []
    for values in external_values:
        if not all(isinstance(value, Mapping) for value in values):
            return sorted([*issues, "invalid_external_delta_coordinate"])
        coordinates = [jcs(value) for value in values]
        if len(coordinates) != len(set(coordinates)):
            issues.append("duplicate_external_delta_coordinate")
        external_coordinate_sets.append(set(coordinates))
    external_preserved, external_removed, external_introduced = external_coordinate_sets
    if external_preserved & external_removed or set(
        domain_resolution_by_coordinate
    ) != (external_preserved | external_removed):
        issues.append("invalid_external_domain_partition")
    if external_preserved & external_introduced or set(
        codomain_resolution_by_coordinate
    ) != (external_preserved | external_introduced):
        issues.append("invalid_external_codomain_partition")
    if external_introduced & set(domain_resolution_by_coordinate):
        issues.append("introduced_external_not_fresh")
    if external_removed & set(codomain_resolution_by_coordinate):
        issues.append("removed_external_retained")

    witness_values = transformation.get("external_resolution_witnesses", [])
    if not isinstance(witness_values, list):
        return sorted([*issues, "invalid_external_witness_collection"])
    witnesses: dict[bytes, Mapping[str, object]] = {}
    for witness in witness_values:
        if not isinstance(witness, Mapping):
            issues.append("invalid_external_witness")
            continue
        resolution = witness.get("external_resolution")
        if not isinstance(resolution, Mapping):
            issues.append("invalid_external_witness_coordinate")
            continue
        coordinate = jcs(resolution)
        if coordinate in witnesses:
            issues.append("duplicate_external_witness")
        witnesses[coordinate] = witness
    if set(witnesses) != external_preserved:
        issues.append("external_witness_population_mismatch")
    witness_fields = {
        "external_resolution",
        "domain_model",
        "codomain_model",
        "domain_resolution",
        "codomain_resolution",
        "decision",
        "evidence",
    }
    for coordinate in external_preserved & witnesses.keys():
        witness = witnesses[coordinate]
        if set(witness) != witness_fields:
            issues.append("external_witness_shape")
            continue
        if (
            witness.get("domain_model") != domain.get("id")
            or witness.get("codomain_model") != codomain.get("id")
            or witness.get("domain_resolution")
            != domain_resolution_by_coordinate.get(coordinate)
            or witness.get("codomain_resolution")
            != codomain_resolution_by_coordinate.get(coordinate)
            or domain_resolution_by_coordinate.get(coordinate)
            != codomain_resolution_by_coordinate.get(coordinate)
            or witness.get("decision") != "equal"
            or not witness.get("evidence")
        ):
            issues.append("external_resolution_not_preserved")
    return sorted(issues)


def utf16_key(value: str) -> bytes:
    return value.encode("utf-16-be", "surrogatepass")


def jcs(value: object) -> bytes:
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
        members = [
            jcs(key) + b":" + jcs(value[key]) for key in sorted(value, key=utf16_key)
        ]
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


def calculus_basis_identity(basis_bytes: bytes) -> str:
    return (
        "urn:stdo:axiomatic-calculus-basis:sha256:"
        + hashlib.sha256(basis_bytes).hexdigest()
    )


def markdown_heading_fragments(raw: bytes) -> set[str]:
    fragments: set[str] = set()
    counts: dict[str, int] = {}
    for line in raw.decode("utf-8").splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match is None:
            continue
        title = re.sub(r"[`*_~]", "", match.group(1)).lower()
        base = "".join(
            character
            for character in title
            if character.isalnum() or character in {"-", "_", " "}
        )
        base = re.sub(r"\s+", "-", base.strip())
        occurrence = counts.get(base, 0)
        counts[base] = occurrence + 1
        fragments.add(base if occurrence == 0 else f"{base}-{occurrence}")
    return fragments


def calculus_basis_fixture() -> (
    tuple[
        dict[str, object],
        bytes,
        bytes,
        bytes,
        dict[str, bytes],
        str,
    ]
):
    derivation_release = "stdo://releases/v2.4.3-rc.3/"
    publication_release = "stdo://releases/v2.5.0-rc.1/"
    principle_refs = sorted(
        (
            derivation_release + "standards/" + target
            for target in EXPECTED_DERIVATION_TARGETS
        ),
        key=utf16_key,
    )
    derivation_paths = sorted(
        {target.split("#", 1)[0] for target in EXPECTED_DERIVATION_TARGETS}
    )
    derivation_manifest_path = INSTALLED_RC3 / "manifest.json"
    if not derivation_manifest_path.is_file():
        raise AssertionError(
            f"missing installed RC3 manifest: {derivation_manifest_path}"
        )
    derivation_manifest_bytes = derivation_manifest_path.read_bytes()
    derivation_member_bytes = {
        path: (INSTALLED_RC3 / "standards" / path).read_bytes()
        for path in derivation_paths
    }
    publication_manifest = {
        "kind": "stdo.installed-release-manifest",
        "schema_version": 1,
        "release": {"cut": "v2.5.0-rc.1"},
        "standards": {
            "member_count": 1,
            "members": [
                {
                    "path": "AXIOMATIC_CALCULUS.md",
                    "sha256": hashlib.sha256(STANDARD.read_bytes()).hexdigest(),
                }
            ],
        },
    }
    publication_manifest_bytes = jcs(publication_manifest)
    basis = {
        "kind": "stdo.axiomatic-calculus-basis",
        "schema_version": 1,
        "concept_identity": "urn:stdo:concept:axiomatic-calculus:a-c",
        "derivation_basis": {
            "release_uri": derivation_release,
            "manifest_sha256": "sha256:"
            + hashlib.sha256(derivation_manifest_bytes).hexdigest(),
            "principle_refs": principle_refs,
        },
        "publication_basis": {
            "release_uri": publication_release,
            "manifest_sha256": "sha256:"
            + hashlib.sha256(publication_manifest_bytes).hexdigest(),
            "member_uri": publication_release + "standards/AXIOMATIC_CALCULUS.md",
            "member_sha256": "sha256:"
            + hashlib.sha256(STANDARD.read_bytes()).hexdigest(),
        },
    }
    basis_bytes = jcs(basis)
    identity = calculus_basis_identity(basis_bytes)
    return (
        basis,
        basis_bytes,
        derivation_manifest_bytes,
        publication_manifest_bytes,
        derivation_member_bytes,
        identity,
    )


def calculus_basis_issues(
    claimed_identity: str,
    basis_bytes: bytes,
    derivation_manifest_bytes: bytes,
    publication_manifest_bytes: bytes,
    derivation_member_bytes: Mapping[str, bytes],
) -> list[str]:
    issues: list[str] = []
    expected_identity = calculus_basis_identity(basis_bytes)
    if claimed_identity != expected_identity:
        issues.append("calculus_basis_identity_mismatch")
    if hashlib.sha256(derivation_manifest_bytes).hexdigest() != (
        INSTALLED_RC3_MANIFEST_SHA256
    ):
        issues.append("derivation_manifest_not_exact_installed_rc3")
    try:
        basis = parse_unique_json(basis_bytes)
        derivation_manifest = parse_unique_json(derivation_manifest_bytes)
        publication_manifest = parse_unique_json(publication_manifest_bytes)
    except (ValueError, json.JSONDecodeError):
        return ["non_unique_or_invalid_json"]
    if not all(
        isinstance(value, Mapping)
        for value in (basis, derivation_manifest, publication_manifest)
    ):
        return ["basis_or_manifest_not_object"]
    try:
        if jcs(basis) != basis_bytes:
            issues.append("basis_not_exact_jcs")
    except ValueError:
        issues.append("basis_not_i_json")
    expected_basis_fields = {
        "kind",
        "schema_version",
        "concept_identity",
        "derivation_basis",
        "publication_basis",
    }
    if set(basis) != expected_basis_fields:
        issues.append("basis_shape_mismatch")
    if (
        basis.get("kind") != "stdo.axiomatic-calculus-basis"
        or basis.get("schema_version") != 1
    ):
        issues.append("basis_kind_or_schema_mismatch")
    if basis.get("concept_identity") != "urn:stdo:concept:axiomatic-calculus:a-c":
        issues.append("concept_identity_mismatch")
    derivation = basis.get("derivation_basis")
    publication = basis.get("publication_basis")
    if not isinstance(derivation, Mapping) or not isinstance(publication, Mapping):
        return [*issues, "basis_coordinate_missing"]
    if set(derivation) != {"release_uri", "manifest_sha256", "principle_refs"}:
        issues.append("derivation_basis_shape_mismatch")
    if set(publication) != {
        "release_uri",
        "manifest_sha256",
        "member_uri",
        "member_sha256",
    }:
        issues.append("publication_basis_shape_mismatch")
    derivation_release = derivation.get("release_uri")
    publication_release = publication.get("release_uri")
    if (
        not isinstance(derivation_release, str)
        or RELEASE_URI_RE.fullmatch(derivation_release) is None
    ):
        issues.append("derivation_release_not_immutable")
    if (
        not isinstance(publication_release, str)
        or RELEASE_URI_RE.fullmatch(publication_release) is None
    ):
        issues.append("publication_release_not_immutable")
    if derivation_release == publication_release:
        issues.append("same_carrier_derivation")
    if derivation_release != "stdo://releases/v2.4.3-rc.3/":
        issues.append("derivation_release_mismatch")
    expected_refs = sorted(
        (
            str(derivation_release) + "standards/" + target
            for target in EXPECTED_DERIVATION_TARGETS
        ),
        key=utf16_key,
    )
    principle_refs = derivation.get("principle_refs")
    if principle_refs != expected_refs:
        issues.append("derivation_principle_set_mismatch")
    if not isinstance(principle_refs, list) or any(
        not absolute_uri(ref) or not str(ref).startswith(str(derivation_release))
        for ref in principle_refs
    ):
        issues.append("cyclic_or_unresolved_derivation_ref")
    if isinstance(principle_refs, list) and (
        len(principle_refs) != len(set(principle_refs))
        or principle_refs != sorted(principle_refs, key=utf16_key)
    ):
        issues.append("derivation_principles_not_unique_sorted")
    if publication.get("member_uri") != (
        str(publication_release) + "standards/AXIOMATIC_CALCULUS.md"
    ):
        issues.append("publication_member_uri_mismatch")
    for coordinate, manifest_bytes in (
        (derivation, derivation_manifest_bytes),
        (publication, publication_manifest_bytes),
    ):
        if coordinate.get("manifest_sha256") != (
            "sha256:" + hashlib.sha256(manifest_bytes).hexdigest()
        ):
            issues.append("manifest_digest_mismatch")
    if publication.get("member_sha256") != (
        "sha256:" + hashlib.sha256(STANDARD.read_bytes()).hexdigest()
    ):
        issues.append("publication_member_digest_mismatch")
    for manifest in (derivation_manifest, publication_manifest):
        if (
            manifest.get("kind") != "stdo.installed-release-manifest"
            or manifest.get("schema_version") != 1
        ):
            issues.append("manifest_kind_or_schema_mismatch")
    manifests = (
        ("derivation", derivation_manifest),
        ("publication", publication_manifest),
    )
    manifest_members: dict[str, dict[str, Mapping[str, object]]] = {}
    for label, manifest in manifests:
        standards = manifest.get("standards")
        if not isinstance(standards, Mapping) or not isinstance(
            standards.get("members"), list
        ):
            issues.append(f"{label}_manifest_members_missing")
            continue
        members = standards["members"]
        if standards.get("member_count") != len(members):
            issues.append(f"{label}_manifest_count_mismatch")
        by_path: dict[str, Mapping[str, object]] = {}
        for member in members:
            if not isinstance(member, Mapping) or set(member) != {"path", "sha256"}:
                issues.append(f"{label}_manifest_member_shape")
                continue
            path = member.get("path")
            member_digest = member.get("sha256")
            if not isinstance(path, str) or not re.fullmatch(
                r"[0-9a-f]{64}", str(member_digest)
            ):
                issues.append(f"{label}_manifest_member_coordinate")
                continue
            if path in by_path:
                issues.append(f"{label}_manifest_member_duplicate")
            by_path[path] = member
        manifest_members[label] = by_path

    derivation_cut = str(derivation_release).rstrip("/").rsplit("/", 1)[-1]
    derivation_release_record = derivation_manifest.get("release")
    if not isinstance(derivation_release_record, Mapping) or (
        derivation_release_record.get("cut") != derivation_cut
    ):
        issues.append("derivation_manifest_release_mismatch")
    publication_cut = str(publication_release).rstrip("/").rsplit("/", 1)[-1]
    publication_release_record = publication_manifest.get("release")
    if not isinstance(publication_release_record, Mapping) or (
        publication_release_record.get("cut") != publication_cut
    ):
        issues.append("publication_manifest_release_mismatch")

    expected_derivation_paths = {
        target.split("#", 1)[0] for target in EXPECTED_DERIVATION_TARGETS
    }
    if set(derivation_member_bytes) != expected_derivation_paths:
        issues.append("derivation_resolution_population_mismatch")
    derivation_members = manifest_members.get("derivation", {})
    for target in EXPECTED_DERIVATION_TARGETS:
        path, fragment = target.split("#", 1)
        member = derivation_members.get(path)
        member_bytes = derivation_member_bytes.get(path)
        if member is None or member_bytes is None:
            issues.append(f"derivation_member_unresolved:{path}")
            continue
        if member.get("sha256") != hashlib.sha256(member_bytes).hexdigest():
            issues.append(f"derivation_member_digest_mismatch:{path}")
        if fragment not in markdown_heading_fragments(member_bytes):
            issues.append(f"derivation_fragment_unresolved:{path}#{fragment}")

    publication_member = manifest_members.get("publication", {}).get(
        "AXIOMATIC_CALCULUS.md"
    )
    if publication_member is None or publication_member.get("sha256") != (
        hashlib.sha256(STANDARD.read_bytes()).hexdigest()
    ):
        issues.append("publication_member_not_unique")
    return sorted(issues)


def record_body(text: str, name: str) -> str:
    match = re.search(
        rf"^{re.escape(name)} = \{{\n(.*?)^\}}$", text, re.MULTILINE | re.DOTALL
    )
    if match is None:
        raise AssertionError(f"missing record {name}")
    return match.group(1)


class AxiomaticCalculusTests(unittest.TestCase):
    def test_calculus_declares_closed_carrier_neutral_kernel(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        for declaration in (
            "# The STDO Axiomatic Calculus for Governed Symbolic Systems",
            "urn:stdo:concept:axiomatic-calculus:a-c",
            "urn:stdo:bounded-context:axiomatic-calculus",
            "Sigma = (",
            "RecordKind,",
            "ResidualKind,",
            "M_b = (b, I, O, E, C, L, X, V, T, J)",
            "Population_M = {",
            "RefDomain_Sigma(record_kind, field)",
            "### AC-001 Closed Signature",
            "### AC-019 Valid Model",
            "a_c       = the pure calculus",
            "a_c.X     = subject X interpreted as a model of a_c",
            "a_c.X.C   = that accepted model encoded in carrier C",
        ):
            self.assertIn(declaration, text)
        for non_claim in (
            "universal applicability",
            "logical completeness",
            "consistency",
            "decidability",
            "soundness",
            "category-theoretic status",
        ):
            self.assertIn(non_claim, text)

    def test_record_kind_population_is_total_finite_and_not_reified(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        body = record_body(text, "RecordKind_ac")
        record_kinds = set(
            re.findall(r"urn:stdo:concept:axiomatic-calculus:record-kind:[a-z-]+", body)
        )
        self.assertEqual(record_kinds, set(RECORD_KIND_BY_POPULATION.values()))
        self.assertIn("not placed in `O` merely by", text)

        populations = {
            name: [record_fixture(name, f"urn:test:{name.lower()}")]
            for name in CORE_POPULATIONS
        }
        self.assertEqual(population_issues(populations), [])

        missing = dict(populations)
        missing.pop("J")
        self.assertIn("missing_population:J", population_issues(missing))

        unknown = {**populations, "Q": [{"id": "urn:test:q"}]}
        self.assertIn("unknown_population:Q", population_issues(unknown))

        wrong_family_shape = {
            name: [dict(records[0])] for name, records in populations.items()
        }
        wrong_family_shape["O"] = [record_fixture("J", "urn:test:wrong-family")]
        self.assertIn("record_shape:O", population_issues(wrong_family_shape))

        duplicate = {name: [dict(records[0])] for name, records in populations.items()}
        duplicate["V"][0]["id"] = duplicate["O"][0]["id"]
        self.assertTrue(
            any(
                result.startswith("duplicate_record_identity:")
                for result in population_issues(duplicate)
            )
        )

        external_identity = "urn:test:external:authority"
        external_resolution = {
            "external_identity": external_identity,
            "reference_domain": "urn:test:reference-domain:authority",
            "external_target_kind": "authority",
            "resolved_target_identity": "urn:external:authority:one",
            "basis_relation": "same-basis",
            "resolution_basis": "urn:test:basis:1",
            "evidence_identity": "urn:test:evidence:external-resolution",
        }
        identities = {
            str(record["id"]) for records in populations.values() for record in records
        } | {external_identity}
        self.assertEqual(
            model_population_issues(
                populations,
                identities,
                {external_identity: external_resolution},
                "urn:test:basis:1",
            ),
            [],
        )
        ambiguous = {
            name: [dict(row) for row in rows] for name, rows in populations.items()
        }
        ambiguous["O"].append(record_fixture("O", external_identity))
        self.assertIn(
            "local_external_ambiguity",
            model_population_issues(
                ambiguous,
                identities,
                {external_identity: external_resolution},
                "urn:test:basis:1",
            ),
        )
        self.assertIn(
            "identity_universe_not_closed",
            model_population_issues(
                populations,
                identities | {"urn:test:orphan"},
                {},
                "urn:test:basis:1",
            ),
        )
        missing_coordinate = dict(external_resolution)
        missing_coordinate.pop("evidence_identity")
        self.assertIn(
            f"external_resolution_shape:{external_identity}",
            model_population_issues(
                populations,
                identities,
                {external_identity: missing_coordinate},
                "urn:test:basis:1",
            ),
        )
        extra_coordinate = {**external_resolution, "undeclared": "value"}
        self.assertIn(
            f"external_resolution_shape:{external_identity}",
            model_population_issues(
                populations,
                identities,
                {external_identity: extra_coordinate},
                "urn:test:basis:1",
            ),
        )

    def test_reference_domains_resolve_across_exact_record_families(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        self.assertIn("allowed_local_record_kinds", text)
        self.assertIn("wrong-record-kind", text)
        populations = {name: [] for name in CORE_POPULATIONS}
        authority = record_fixture("O", "urn:test:authority")
        authority["sort"] = "authority"
        concept = record_fixture("O", "urn:test:concept")
        concept["sort"] = "concept"
        populations["O"] = [authority, concept]
        populations["V"] = [record_fixture("V", "urn:test:traversal")]
        populations["J"] = [record_fixture("J", "urn:test:judgment")]

        self.assertIsNone(reference_issue(populations, "urn:test:traversal", {"V"}))
        self.assertIsNone(
            reference_issue(populations, "urn:test:authority", {"O"}, {"authority"})
        )
        self.assertEqual(
            reference_issue(populations, "urn:test:traversal", {"O"}),
            "wrong_record_kind",
        )
        self.assertEqual(
            reference_issue(populations, "urn:test:concept", {"O"}, {"authority"}),
            "wrong_semantic_object_sort",
        )
        self.assertEqual(
            reference_issue(populations, "urn:test:missing", {"V"}),
            "dangling_reference",
        )

        ambiguous = {
            name: [dict(row) for row in rows] for name, rows in populations.items()
        }
        ambiguous["J"].append({"id": "urn:test:traversal"})
        self.assertEqual(
            reference_issue(ambiguous, "urn:test:traversal", {"V"}),
            "ambiguous_reference",
        )

        traversal_domain = {
            "cardinality": "exactly_one",
            "allowed_local_record_kinds": [RECORD_KIND_BY_POPULATION["V"]],
            "allowed_semantic_object_sorts": [],
            "allowed_external_target_kinds": ["published-traversal"],
            "required_basis_relation": "same-basis",
        }
        self.assertEqual(
            reference_domain_issues(
                populations,
                ["urn:test:traversal"],
                traversal_domain,
                {},
                "urn:test:basis:1",
                "urn:test:reference-domain:traversal",
            ),
            [],
        )
        self.assertIn(
            "cardinality_mismatch",
            reference_domain_issues(
                populations,
                ["urn:test:traversal", "urn:test:traversal"],
                traversal_domain,
                {},
                "urn:test:basis:1",
                "urn:test:reference-domain:traversal",
            ),
        )
        external_identity = "urn:test:external:traversal"
        external_resolution = {
            "external_identity": external_identity,
            "reference_domain": "urn:test:reference-domain:traversal",
            "external_target_kind": "published-traversal",
            "resolved_target_identity": "urn:published:traversal:one",
            "basis_relation": "same-basis",
            "resolution_basis": "urn:test:basis:1",
            "evidence_identity": "urn:test:evidence:resolution",
        }
        self.assertEqual(
            reference_domain_issues(
                populations,
                [external_identity],
                traversal_domain,
                {external_identity: external_resolution},
                "urn:test:basis:1",
                "urn:test:reference-domain:traversal",
            ),
            [],
        )
        wrong_basis = {**external_resolution, "basis_relation": "translated-basis"}
        self.assertIn(
            f"wrong_basis_relation:{external_identity}",
            reference_domain_issues(
                populations,
                [external_identity],
                traversal_domain,
                {external_identity: wrong_basis},
                "urn:test:basis:1",
                "urn:test:reference-domain:traversal",
            ),
        )
        wrong_reference_domain = {
            **external_resolution,
            "reference_domain": "urn:test:reference-domain:other",
        }
        self.assertIn(
            f"wrong_reference_domain:{external_identity}",
            reference_domain_issues(
                populations,
                [external_identity],
                traversal_domain,
                {external_identity: wrong_reference_domain},
                "urn:test:basis:1",
                "urn:test:reference-domain:traversal",
            ),
        )
        wrong_resolution_basis = {
            **external_resolution,
            "resolution_basis": "urn:test:basis:other",
        }
        self.assertIn(
            f"wrong_resolution_basis:{external_identity}",
            reference_domain_issues(
                populations,
                [external_identity],
                traversal_domain,
                {external_identity: wrong_resolution_basis},
                "urn:test:basis:1",
                "urn:test:reference-domain:traversal",
            ),
        )
        self.assertIn(
            "local_external_ambiguity:urn:test:traversal",
            reference_domain_issues(
                populations,
                ["urn:test:traversal"],
                traversal_domain,
                {"urn:test:traversal": external_resolution},
                "urn:test:basis:1",
                "urn:test:reference-domain:traversal",
            ),
        )

        collection_domain = {**traversal_domain, "cardinality": "zero_or_more"}
        self.assertIn(
            "duplicate_reference",
            reference_domain_issues(
                populations,
                ["urn:test:traversal", "urn:test:traversal"],
                collection_domain,
                {},
                "urn:test:basis:1",
                "urn:test:reference-domain:traversal",
            ),
        )
        wrong_local_basis = {
            name: [dict(record) for record in records]
            for name, records in populations.items()
        }
        wrong_local_basis["V"][0]["basis"] = "urn:test:basis:other"
        self.assertIn(
            "wrong_local_basis:urn:test:traversal",
            reference_domain_issues(
                wrong_local_basis,
                ["urn:test:traversal"],
                traversal_domain,
                {},
                "urn:test:basis:1",
                "urn:test:reference-domain:traversal",
            ),
        )
        malformed_domain = dict(traversal_domain)
        malformed_domain.pop("required_basis_relation")
        malformed_domain["undeclared"] = "value"
        self.assertIn(
            "reference_domain_shape",
            reference_domain_issues(
                populations,
                ["urn:test:traversal"],
                malformed_domain,
                {},
                "urn:test:basis:1",
                "urn:test:reference-domain:traversal",
            ),
        )

    def test_functor_kinds_are_exact_and_vector_qualified(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        for identity in (
            "F_D = urn:stdo:concept:axiomatic-calculus:f-d",
            "F_P = urn:stdo:concept:axiomatic-calculus:f-p",
            "F_H = urn:stdo:concept:axiomatic-calculus:f-h",
            "F_K[v](X_v) -> Y_v | Omega_v",
        ):
            self.assertIn(identity, text)
        self.assertIsNone(re.search(r"\bF_[DPH]\s*\(", text))
        self.assertIn(
            "This standard introduces the generic calculus identities `F_D`, `F_P`, and",
            text,
        )
        for derivation_target in (
            "REFERENCE_FRAME_METHOD.md#position",
            "REFERENCE_FRAME_METHOD.md#evaluation",
            "SPEC_METHOD.md#agentic-construction-execution-stdo-up-020",
        ):
            self.assertIn(derivation_target, text)
        self.assertNotIn("deterministic admission separation", text)

    def test_admission_is_a_judgment_over_unchanged_carrier(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        self.assertIn(
            "D_C = F_D[v_carrier_admission](G_C, Profile_C, CarrierBasis_C)",
            text,
        )
        self.assertIn("`D_C` is a judgment over unchanged carrier bytes", text)
        self.assertNotRegex(
            text,
            r"F_D\[v_carrier_admission\]\([^)]*\)\s*->\s*G_C",
        )
        self.assertIn("It is not embedded in `id(a_c.X)`", text)
        self.assertIn(
            "is not embedded in `id(a_c.X.C)`",
            text,
        )
        self.assertNotIn("+ semantic acceptance identity", text)
        self.assertNotIn("+ carrier admission judgment identity", text)
        self.assertIn("derivation_basis", text)
        self.assertIn("publication_basis", text)
        self.assertIn("distinct immutable successor carrier", text)
        self.assertIn("a_c.X + exact accepted semantic judgment J_X", text)
        self.assertNotIn("a_c.X + exact carrier C", text)
        self.assertNotIn("same-release semantic addresses", text)

    def test_fundamental_records_carry_direct_coordinates(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        for name in (
            "SemanticObject",
            "TypedRelation",
            "Constraint",
            "Latitude",
            "Residual",
            "Judgment",
            "v",
            "t",
        ):
            body = record_body(text, name)
            for coordinate in ("context", "owner", "scope", "basis"):
                self.assertRegex(body, rf"\b{coordinate}\b", f"{name}.{coordinate}")
        self.assertRegex(record_body(text, "Constraint"), r"\bjudgment_kind\b")
        transformation = record_body(text, "t")
        for field in (
            "preservation_relation",
            "external_preserved",
            "external_introduced",
            "external_removed",
            "external_resolution_witnesses",
        ):
            self.assertRegex(transformation, rf"\b{field}\b")

    def test_transformation_binds_exact_models_basis_and_equality(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        self.assertIn(
            "`domain_model` and `codomain_model` resolve exact content identities",
            text,
        )
        self.assertIn("byte-identical under one exact canonical record grammar", text)
        external_identity = "urn:test:external:authority"
        external_resolution = {
            "external_identity": external_identity,
            "reference_domain": "urn:test:reference-domain:authority",
            "external_target_kind": "authority",
            "resolved_target_identity": "urn:published:authority:one",
            "basis_relation": "same-basis",
            "resolution_basis": "urn:test:basis:1",
            "evidence_identity": "urn:test:evidence:resolution",
        }
        before_populations = {name: [] for name in CORE_POPULATIONS}
        before_populations["O"] = [record_fixture("O", "urn:test:record:a")]
        before = {
            "id": "urn:test:model:before",
            "basis": "urn:test:basis:1",
            "signature": "urn:test:signature:1",
            "canonical_record_grammar": "urn:test:grammar:jcs",
            "populations": before_populations,
            "identities": {"urn:test:record:a", external_identity},
            "external_resolutions": {external_identity: external_resolution},
        }
        after = deepcopy(before)
        after["id"] = "urn:test:model:after"
        transformation = {
            "id": "urn:test:transformation:one",
            "traversal": "urn:test:traversal:one",
            "domain_model": before["id"],
            "codomain_model": after["id"],
            "context": "urn:test:context",
            "owner": "urn:test:owner",
            "scope": "urn:test:scope",
            "basis": before["basis"],
            "operation_authority": "urn:test:authority:transform",
            "preconditions": [],
            "preservation_relation": "urn:test:relation:record-equality",
            "preserved": ["urn:test:record:a"],
            "removed": [],
            "introduced": [],
            "external_preserved": [external_resolution],
            "external_removed": [],
            "external_introduced": [],
            "external_resolution_witnesses": [
                {
                    "external_resolution": external_resolution,
                    "domain_model": before["id"],
                    "codomain_model": after["id"],
                    "domain_resolution": external_resolution,
                    "codomain_resolution": external_resolution,
                    "decision": "equal",
                    "evidence": ["urn:test:evidence:external-preservation"],
                }
            ],
            "residuals": [],
            "evidence": ["urn:test:evidence:transformation"],
            "provenance": ["urn:test:provenance:transformation"],
            "stop_states": ["refusal"],
            "invalidation": "urn:test:invalidation",
            "re_entry": "urn:test:re-entry",
        }
        self.assertEqual(
            transformation_issues(before, after, transformation),
            [],
        )

        for mutation in ("missing", "extra"):
            invalid_before = deepcopy(before)
            invalid_after = deepcopy(after)
            invalid_transformation = deepcopy(transformation)
            invalid_resolution = dict(external_resolution)
            if mutation == "missing":
                invalid_resolution.pop("evidence_identity")
            else:
                invalid_resolution["undeclared"] = "value"
            invalid_before["external_resolutions"][
                external_identity
            ] = invalid_resolution
            invalid_after["external_resolutions"][
                external_identity
            ] = invalid_resolution
            invalid_transformation["external_preserved"] = [invalid_resolution]
            invalid_transformation["external_resolution_witnesses"][0].update(
                {
                    "external_resolution": invalid_resolution,
                    "domain_resolution": invalid_resolution,
                    "codomain_resolution": invalid_resolution,
                }
            )
            invalid_issues = transformation_issues(
                invalid_before,
                invalid_after,
                invalid_transformation,
            )
            self.assertTrue(
                any("external_resolution_shape" in issue for issue in invalid_issues),
                invalid_issues,
            )

        incomplete_after = deepcopy(after)
        incomplete_after["populations"]["O"].append({"id": "urn:test:record:new"})
        incomplete_after["identities"].add("urn:test:record:new")
        incomplete_introduction = {
            **transformation,
            "introduced": ["urn:test:record:new"],
        }
        self.assertIn(
            "codomain_record_shape:O",
            transformation_issues(
                before,
                incomplete_after,
                incomplete_introduction,
            ),
        )

        locator = {**transformation, "domain_model": "workspace/current"}
        self.assertIn(
            "domain_model_mismatch",
            transformation_issues(before, after, locator),
        )

        changed = deepcopy(after)
        changed["populations"]["O"][0]["value"] = {"name": "changed"}
        self.assertIn(
            "preserved_without_exact_equality:urn:test:record:a",
            transformation_issues(before, changed, transformation),
        )
        no_bytes_before = deepcopy(before)
        no_bytes_after = deepcopy(after)
        no_bytes_after["canonical_record_grammar"] = "urn:test:grammar:other"
        self.assertIn(
            "preserved_without_exact_equality:urn:test:record:a",
            transformation_issues(no_bytes_before, no_bytes_after, transformation),
        )
        equality = {
            "domain_model": str(before["id"]),
            "codomain_model": str(changed["id"]),
            "record_id": "urn:test:record:a",
            "record_kind": RECORD_KIND_BY_POPULATION["O"],
            "domain_basis": str(before["basis"]),
            "codomain_basis": str(changed["basis"]),
            "preservation_relation": str(transformation["preservation_relation"]),
            "decision": "equal",
        }
        self.assertEqual(
            transformation_issues(before, changed, transformation, equality),
            [],
        )

        changed_basis = {**changed, "basis": "urn:test:basis:2"}
        self.assertIn(
            "basis_mismatch",
            transformation_issues(before, changed_basis, transformation, equality),
        )

        changed_kind = deepcopy(after)
        changed_kind["populations"]["O"] = []
        changed_kind["populations"]["E"] = [record_fixture("E", "urn:test:record:a")]
        self.assertIn(
            "preserved_coordinate_mismatch:urn:test:record:a",
            transformation_issues(before, changed_kind, transformation),
        )

        incomplete_partition = {**transformation, "preserved": []}
        self.assertIn(
            "invalid_domain_partition",
            transformation_issues(before, after, incomplete_partition),
        )

        recycled_local = {
            **transformation,
            "preserved": [],
            "removed": ["urn:test:record:a"],
            "introduced": ["urn:test:record:a"],
        }
        recycled_local_issues = transformation_issues(before, after, recycled_local)
        self.assertIn("introduced_local_not_fresh", recycled_local_issues)
        self.assertIn("removed_local_retained", recycled_local_issues)

        recycled_external = {
            **transformation,
            "external_preserved": [],
            "external_removed": [external_resolution],
            "external_introduced": [external_resolution],
            "external_resolution_witnesses": [],
        }
        recycled_external_issues = transformation_issues(
            before, after, recycled_external
        )
        self.assertIn("introduced_external_not_fresh", recycled_external_issues)
        self.assertIn("removed_external_retained", recycled_external_issues)

        changed_external = {
            **after,
            "external_resolutions": {
                external_identity: {
                    **external_resolution,
                    "resolved_target_identity": "urn:published:authority:two",
                }
            },
        }
        self.assertIn(
            "external_resolution_not_preserved",
            transformation_issues(before, changed_external, transformation),
        )
        missing_witness = {
            **transformation,
            "external_resolution_witnesses": [],
        }
        self.assertIn(
            "external_witness_population_mismatch",
            transformation_issues(before, after, missing_witness),
        )

        missing_traversal = dict(transformation)
        missing_traversal.pop("traversal")
        missing_traversal_issues = transformation_issues(
            before, after, missing_traversal
        )
        self.assertIn("transformation_shape_mismatch", missing_traversal_issues)
        self.assertIn(
            "missing_transformation_coordinate:traversal",
            missing_traversal_issues,
        )

    def test_calculus_basis_is_exact_jcs_acyclic_and_cross_carrier(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        derivation_section = text.split("## Derivation Provenance", 1)[1].split(
            "## Scope", 1
        )[0]
        linked_targets = set(re.findall(r"\]\(([^)]+#[^)]+)\)", derivation_section))
        self.assertEqual(linked_targets, EXPECTED_DERIVATION_TARGETS)

        (
            basis,
            basis_bytes,
            derivation_manifest_bytes,
            publication_manifest_bytes,
            derivation_member_bytes,
            identity,
        ) = calculus_basis_fixture()
        self.assertEqual(
            calculus_basis_issues(
                identity,
                basis_bytes,
                derivation_manifest_bytes,
                publication_manifest_bytes,
                derivation_member_bytes,
            ),
            [],
        )
        self.assertEqual(
            identity,
            "urn:stdo:axiomatic-calculus-basis:sha256:"
            + hashlib.sha256(basis_bytes).hexdigest(),
        )
        with self.assertRaisesRegex(ValueError, "duplicate_object_name"):
            parse_unique_json(b'{"kind":1,"kind":2}')
        pretty = json.dumps(basis, ensure_ascii=False, indent=2).encode()
        self.assertIn(
            "basis_not_exact_jcs",
            calculus_basis_issues(
                identity,
                pretty,
                derivation_manifest_bytes,
                publication_manifest_bytes,
                derivation_member_bytes,
            ),
        )
        self.assertIn(
            "calculus_basis_identity_mismatch",
            calculus_basis_issues(
                "urn:stdo:axiomatic-calculus-basis:sha256:" + "0" * 64,
                basis_bytes,
                derivation_manifest_bytes,
                publication_manifest_bytes,
                derivation_member_bytes,
            ),
        )

        same_carrier = json.loads(json.dumps(basis))
        publication_release = same_carrier["publication_basis"]["release_uri"]
        same_carrier["derivation_basis"]["release_uri"] = publication_release
        same_carrier["derivation_basis"]["principle_refs"] = sorted(
            (
                publication_release + "standards/" + target
                for target in EXPECTED_DERIVATION_TARGETS
            ),
            key=utf16_key,
        )
        self.assertIn(
            "same_carrier_derivation",
            calculus_basis_issues(
                calculus_basis_identity(jcs(same_carrier)),
                jcs(same_carrier),
                derivation_manifest_bytes,
                publication_manifest_bytes,
                derivation_member_bytes,
            ),
        )

        cyclic = json.loads(json.dumps(basis))
        cyclic["derivation_basis"]["principle_refs"][0] = (
            cyclic["publication_basis"]["member_uri"] + "#exact-calculus-identity"
        )
        self.assertIn(
            "cyclic_or_unresolved_derivation_ref",
            calculus_basis_issues(
                calculus_basis_identity(jcs(cyclic)),
                jcs(cyclic),
                derivation_manifest_bytes,
                publication_manifest_bytes,
                derivation_member_bytes,
            ),
        )

        wrong_member = json.loads(json.dumps(basis))
        wrong_member["publication_basis"]["member_sha256"] = "sha256:" + "0" * 64
        self.assertIn(
            "publication_member_digest_mismatch",
            calculus_basis_issues(
                calculus_basis_identity(jcs(wrong_member)),
                jcs(wrong_member),
                derivation_manifest_bytes,
                publication_manifest_bytes,
                derivation_member_bytes,
            ),
        )

        forged_manifest = parse_unique_json(derivation_manifest_bytes)
        self.assertIsInstance(forged_manifest, dict)
        forged_manifest = deepcopy(forged_manifest)
        forged_path = "IDENTITY_METHOD.md"
        for member in forged_manifest["standards"]["members"]:
            if member["path"] == forged_path:
                member["sha256"] = hashlib.sha256(forged_path.encode()).hexdigest()
        forged_manifest_bytes = jcs(forged_manifest)
        forged_basis = deepcopy(basis)
        forged_basis["derivation_basis"]["manifest_sha256"] = (
            "sha256:" + hashlib.sha256(forged_manifest_bytes).hexdigest()
        )
        forged_basis_bytes = jcs(forged_basis)
        self.assertIn(
            f"derivation_member_digest_mismatch:{forged_path}",
            calculus_basis_issues(
                calculus_basis_identity(forged_basis_bytes),
                forged_basis_bytes,
                forged_manifest_bytes,
                publication_manifest_bytes,
                derivation_member_bytes,
            ),
        )

        fragment_members = dict(derivation_member_bytes)
        fragment_members[forged_path] = fragment_members[forged_path].replace(
            b"## Core Law",
            b"## Removed Core Law",
            1,
        )
        fragment_manifest = parse_unique_json(derivation_manifest_bytes)
        self.assertIsInstance(fragment_manifest, dict)
        fragment_manifest = deepcopy(fragment_manifest)
        for member in fragment_manifest["standards"]["members"]:
            if member["path"] == forged_path:
                member["sha256"] = hashlib.sha256(
                    fragment_members[forged_path]
                ).hexdigest()
        fragment_manifest_bytes = jcs(fragment_manifest)
        fragment_basis = deepcopy(basis)
        fragment_basis["derivation_basis"]["manifest_sha256"] = (
            "sha256:" + hashlib.sha256(fragment_manifest_bytes).hexdigest()
        )
        fragment_basis_bytes = jcs(fragment_basis)
        self.assertIn(
            "derivation_fragment_unresolved:IDENTITY_METHOD.md#core-law",
            calculus_basis_issues(
                calculus_basis_identity(fragment_basis_bytes),
                fragment_basis_bytes,
                fragment_manifest_bytes,
                publication_manifest_bytes,
                fragment_members,
            ),
        )

        unresolved_members = dict(derivation_member_bytes)
        unresolved_members.pop("IDENTITY_METHOD.md")
        self.assertIn(
            "derivation_resolution_population_mismatch",
            calculus_basis_issues(
                identity,
                basis_bytes,
                derivation_manifest_bytes,
                publication_manifest_bytes,
                unresolved_members,
            ),
        )

    def test_calculus_has_no_application_or_runtime_binding(self) -> None:
        for path in (STANDARD, COMPRESSION):
            text = path.read_text(encoding="utf-8")
            for forbidden in (
                "ABIogenesis",
                "ABG",
                "HoG",
                "graph-native-odd",
                "ODD_METHOD.md",
                "## STDO Application",
                "a_c.STDO",
                "a_c.STDO.GTL",
                "Encode_GTL",
            ):
                self.assertNotIn(forbidden, text, f"{path.name}: {forbidden}")

    def test_stdo_product_keeps_the_three_layers_distinct(self) -> None:
        text = PRODUCT.read_text(encoding="utf-8")
        self.assertIn("## Axiomatic Calculus Boundary", text)
        self.assertIn("STDO principles -> a_c", text)
        self.assertIn("a_c + exact subject X -> a_c.X", text)
        self.assertIn(
            "a_c.X + exact accepted semantic judgment J_X -> accepted a_c.X", text
        )
        self.assertIn("accepted a_c.X + exact carrier C -> a_c.X.C", text)
        self.assertIn("distinct governed layers", text)
        self.assertIn("not automatically independently released", text)


if __name__ == "__main__":
    unittest.main()
