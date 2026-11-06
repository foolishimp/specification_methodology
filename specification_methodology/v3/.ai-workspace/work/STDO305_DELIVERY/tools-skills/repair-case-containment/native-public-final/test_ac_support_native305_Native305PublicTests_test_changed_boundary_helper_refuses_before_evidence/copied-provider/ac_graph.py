#!/usr/bin/env python3
"""Bounded, mechanically checked Graphify realization of explicitly authored a_c."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import re
import sys
from typing import Mapping, Sequence, TypeAlias, cast

JSON: TypeAlias = "None | bool | int | float | str | list[JSON] | dict[str, JSON]"
Object: TypeAlias = dict[str, JSON]
MODEL_PROFILE = "a_c.graphify.model/1"
GRAPH_PROFILE = "a_c.graphify.carrier/1"
CALCULUS_URI = "stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md"
CALCULUS_SHA256 = "cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d"
FUNCTORS = tuple("urn:stdo:concept:axiomatic-calculus:f-" + k for k in ("d", "p", "h"))
CORE_FIELDS: Mapping[str, tuple[str, ...]] = {
    "objects": ("id", "sort", "context", "owner", "scope", "basis", "value"),
    "relations": ("id", "kind", "source", "target", "context", "owner", "scope", "basis", "qualifiers"),
    "constraints": ("id", "kind", "applies_to", "predicate", "context", "owner", "scope", "basis", "judgment_kind", "latitude_ref", "refusal"),
    "latitude": ("id", "applies_to", "allowed_variation", "forbidden_variation", "context", "owner", "scope", "basis", "invalidation"),
    "residuals": ("id", "subject", "kind", "uncertainty", "consequence", "context", "owner", "scope", "basis", "re_entry", "invalidation"),
    "traversals": ("id", "domain", "codomain", "context", "owner", "scope", "basis", "preconditions", "postconditions", "authority", "evidence", "provenance", "stop_states"),
    "transformations": ("id", "traversal", "domain_model", "codomain_model", "context", "owner", "scope", "basis", "operation_authority", "preconditions", "preservation_relation", "preserved", "introduced", "removed", "external_preserved", "external_introduced", "external_removed", "external_resolution_witnesses", "residuals", "evidence", "provenance", "stop_states", "invalidation", "re_entry"),
    "judgments": ("id", "kind", "subject", "subject_digest", "context", "owner", "scope", "basis", "evaluator", "authority", "decision", "evidence", "provenance", "decided_at"),
}
VARIANTS: Mapping[str, tuple[str, str, tuple[str, ...]]] = {
    "objects": ("sorts", "sort", ("value",)),
    "relations": ("relation_kinds", "kind", ("source", "target", "qualifiers")),
    "constraints": ("constraint_kinds", "kind", ("applies_to", "predicate")),
    "residuals": ("residual_kinds", "kind", ("subject", "uncertainty", "consequence", "re_entry", "invalidation")),
    "judgments": ("judgment_kinds", "kind", ("subject", "decision", "evidence")),
}
MODEL_FIELDS = ("profile", "id", "basis", "coordinates", "signature", "interpretation", "identity_universe", "external_resolutions", "populations", "dependency_contract", "functor_bindings")
RESOLUTION_FIELDS = ("external_identity", "reference_domain", "external_target_kind", "resolved_target_identity", "basis_relation", "resolution_basis", "evidence_identity")


class Refusal(ValueError):
    """The declared mechanical contract is not satisfied."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Refusal(message)


def obj(value: JSON, path: str) -> Object:
    require(isinstance(value, dict), f"{path}: expected object")
    return cast(Object, value)


def seq(value: JSON, path: str) -> list[JSON]:
    require(isinstance(value, list), f"{path}: expected array")
    return cast(list[JSON], value)


def string(value: JSON, path: str) -> str:
    require(isinstance(value, str) and bool(value), f"{path}: expected nonempty string")
    return cast(str, value)


def identity(value: JSON, path: str) -> str:
    result = string(value, path)
    require(bool(re.fullmatch(r"[A-Za-z][A-Za-z0-9+.-]*:[^\s]+", result)), f"{path}: expected absolute identity")
    return result


def keys(value: Object, expected: Sequence[str], path: str) -> None:
    require(set(value) == set(expected), f"{path}: expected fields {sorted(expected)}, got {sorted(value)}")


def strings(value: JSON, path: str, unique: bool = True) -> list[str]:
    values = [string(v, path) for v in seq(value, path)]
    require(not unique or len(values) == len(set(values)), f"{path}: duplicate member")
    return values


def grammar(value: JSON, path: str = "$", depth: int = 0, *, annotations: bool = False) -> None:
    require(depth < 100, f"{path}: nesting exceeds declared grammar")
    if value is None or isinstance(value, (bool, int, str)):
        if isinstance(value, str):
            require(not any(0xD800 <= ord(c) <= 0xDFFF for c in value), f"{path}: unpaired Unicode surrogate")
        return
    if isinstance(value, float):
        require(annotations and math.isfinite(value), f"{path}: floating point is outside semantic grammar")
        return
    if isinstance(value, list):
        for i, v in enumerate(value):
            grammar(v, f"{path}/{i}", depth + 1, annotations=annotations)
        return
    require(isinstance(value, dict), f"{path}: floating point or unsupported JSON value")
    for k, v in cast(Object, value).items():
        require(isinstance(k, str), f"{path}: non-string key")
        grammar(k, path, depth + 1, annotations=annotations)
        grammar(v, f"{path}/{k}", depth + 1, annotations=annotations)


def canonical(value: JSON) -> bytes:
    grammar(value)
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(value: JSON) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def sha(value: JSON, path: str) -> str:
    result = string(value, path)
    require(bool(re.fullmatch(r"[a-f0-9]{64}", result)), f"{path}: expected SHA-256")
    return result


def coordinate(value: JSON, path: str) -> None:
    item = obj(value, path)
    keys(item, ("id", "sha256"), path)
    identity(item["id"], path + "/id")
    sha(item["sha256"], path + "/sha256")


def _pairs(pairs: list[tuple[str, JSON]]) -> Object:
    result: Object = {}
    for k, v in pairs:
        require(k not in result, f"JSON: duplicate key {k}")
        result[k] = v
    return result


def read_json(path: str | Path) -> Object:
    try:
        value = cast(JSON, json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=_pairs))
        grammar(value, annotations=True)
        return obj(value, "$")
    except (OSError, json.JSONDecodeError) as exc:
        raise Refusal(f"cannot read JSON: {exc}") from exc


def write_json(path: str | Path, value: JSON) -> None:
    grammar(value, annotations=True)
    Path(path).write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")


@dataclass(frozen=True)
class Record:
    family: str
    identity: str
    fields: Object


@dataclass(frozen=True)
class Reference:
    owner: str
    path: tuple[str, ...]
    target: str
    schema: Object


@dataclass(frozen=True)
class Signature:
    identity: str
    definition: Object

    def fields_for(self, record: Record) -> Object:
        fields = dict(obj(obj(self.definition["fields"], "signature/fields")[record.family], record.family))
        if record.family in VARIANTS:
            group, selector, _ = VARIANTS[record.family]
            kind = string(record.fields[selector], selector)
            variants = obj(self.definition[group], group)
            require(kind in variants, f"{record.identity}: unknown {selector} {kind}")
            fields.update(obj(variants[kind], kind))
        return fields


@dataclass(frozen=True)
class Model:
    document: Object
    identity: str
    sha256: str
    signature: Signature
    records: Mapping[str, Record]
    external: Mapping[str, Object]
    references: tuple[Reference, ...]


def schema_check(schema_value: JSON, path: str) -> None:
    schema = obj(schema_value, path)
    kind = string(schema.get("type"), path + "/type")
    allowed: Mapping[str, set[str]] = {
        "null": {"type"}, "boolean": {"type"}, "integer": {"type"},
        "string": {"type", "min_length"}, "identity": {"type"},
        "enum": {"type", "values"}, "object": {"type", "fields"},
        "array": {"type", "items", "min_items", "max_items"},
        "ref": {"type", "domain", "local_families", "local_sorts", "external_kinds", "basis_relation", "governing"},
    }
    require(kind in allowed, f"{path}: unsupported schema type {kind}")
    require(set(schema) <= allowed[kind], f"{path}: unknown schema fields")
    if kind == "ref":
        keys(schema, tuple(allowed[kind]), path)
        identity(schema["domain"], path + "/domain")
        identity(schema["basis_relation"], path + "/basis_relation")
        require(type(schema["governing"]) is bool, f"{path}: governing role must be explicit Boolean")
        families = strings(schema["local_families"], path + "/local_families")
        require(set(families) <= set(CORE_FIELDS), f"{path}: unknown local family")
        for name in ("local_sorts", "external_kinds"):
            for v in strings(schema[name], path + "/" + name):
                identity(v, path + "/" + name)
        require(bool(families or seq(schema["external_kinds"], path)), f"{path}: empty reference domain")
        require(not seq(schema["local_sorts"], path) or "objects" in families, f"{path}: sort domain without object family")
    elif kind == "enum":
        keys(schema, ("type", "values"), path)
        require(bool(strings(schema["values"], path)), f"{path}: empty enum")
    elif kind == "object":
        keys(schema, ("type", "fields"), path)
        for key, child in obj(schema["fields"], path).items():
            schema_check(child, path + "/" + key)
    elif kind == "array":
        require("items" in schema, f"{path}: missing items")
        schema_check(schema["items"], path + "/items")
        minimum = schema.get("min_items", 0)
        maximum = schema.get("max_items")
        require(type(minimum) is int and minimum >= 0, f"{path}: bad minimum")
        require(maximum is None or (type(maximum) is int and maximum >= cast(int, minimum)), f"{path}: bad maximum")
    elif kind == "string" and "min_length" in schema:
        require(type(schema["min_length"]) is int and schema["min_length"] >= 0, f"{path}: bad length")


def check_value(value: JSON, schema: Object, record: Record, path: tuple[str, ...], records: Mapping[str, Record], external: Mapping[str, Object], refs: list[Reference]) -> None:
    kind = string(schema["type"], "schema/type")
    location = record.identity + "/" + "/".join(path)
    if kind == "ref":
        target = identity(value, location)
        local = records.get(target)
        remote = external.get(target)
        require((local is None) != (remote is None), f"{location}: dangling or ambiguous reference {target}")
        if local is not None:
            require(local.family in strings(schema["local_families"], location), f"{location}: wrong target family")
            sorts = strings(schema["local_sorts"], location)
            require(local.family != "objects" or not sorts or local.fields["sort"] in sorts, f"{location}: wrong target sort")
        else:
            assert remote is not None
            require(remote["external_target_kind"] in strings(schema["external_kinds"], location), f"{location}: wrong external kind")
            require(remote["reference_domain"] == schema["domain"] and remote["basis_relation"] == schema["basis_relation"], f"{location}: wrong external domain or basis relation")
        refs.append(Reference(record.identity, path, target, schema))
    elif kind == "identity":
        identity(value, location)
        require(path == ("id",), f"{location}: identity declaration only permitted for record id")
    elif kind == "array":
        values = seq(value, location)
        minimum = cast(int, schema.get("min_items", 0))
        maximum = schema.get("max_items")
        require(len(values) >= minimum and (maximum is None or len(values) <= cast(int, maximum)), f"{location}: cardinality")
        for i, child in enumerate(values):
            check_value(child, obj(schema["items"], location), record, path + (str(i),), records, external, refs)
    elif kind == "object":
        object_values = obj(value, location)
        fields = obj(schema["fields"], location)
        keys(object_values, tuple(fields), location)
        for field in sorted(fields):
            check_value(object_values[field], obj(fields[field], location), record, path + (field,), records, external, refs)
    elif kind == "enum":
        require(isinstance(value, str) and value in strings(schema["values"], location), f"{location}: unknown enum value")
    elif kind == "string":
        require(isinstance(value, str) and len(value) >= cast(int, schema.get("min_length", 0)), f"{location}: expected string")
    elif kind == "integer":
        require(type(value) is int, f"{location}: expected integer")
    elif kind == "boolean":
        require(type(value) is bool, f"{location}: expected Boolean")
    elif kind == "null":
        require(value is None, f"{location}: expected null")
    else:
        raise Refusal(f"{location}: unsupported type {kind}")


def _ref_type(schema: JSON, array: bool, path: str) -> None:
    value = obj(schema, path)
    if array:
        require(value["type"] == "array", f"{path}: profile requires reference array")
        value = obj(value["items"], path)
    require(value["type"] == "ref", f"{path}: profile requires typed reference")


def _fixed_local_family(schema: JSON, array: bool, family: str, path: str) -> None:
    """Signature specialization cannot replace a core record-family relation."""
    _ref_type(schema, array, path)
    domain = obj(schema, path)
    if array:
        domain = obj(domain["items"], path)
    require(
        strings(domain["local_families"], path) == [family]
        and not seq(domain["external_kinds"], path),
        f"{path}: fixed core family must resolve locally to {family}",
    )


def _external_only(schema: JSON, array: bool, path: str) -> None:
    _ref_type(schema, array, path)
    domain = obj(schema, path)
    if array:
        domain = obj(domain["items"], path)
    require(not seq(domain["local_families"], path), f"{path}: model/resolution coordinates are not local core records")


def _external_contracts(schema_value: JSON) -> set[tuple[str, str, str]]:
    """Collect admitted exact external contracts, including unused/nested ones."""
    schema = obj(schema_value, "schema")
    kind = string(schema["type"], "schema/type")
    result: set[tuple[str, str, str]] = set()
    if kind == "ref":
        for target_kind in strings(schema["external_kinds"], "external_kinds"):
            result.add((string(schema["domain"], "domain"), target_kind, string(schema["basis_relation"], "basis_relation")))
    elif kind == "array":
        result.update(_external_contracts(schema["items"]))
    elif kind == "object":
        for field in obj(schema["fields"], "fields").values():
            result.update(_external_contracts(field))
    return result


def _validate(document: Object) -> Model:
    grammar(document)
    keys(document, MODEL_FIELDS, "model")
    require(document["profile"] == MODEL_PROFILE, "unsupported model profile")
    model_id = identity(document["id"], "model/id")
    basis = obj(document["basis"], "basis")
    keys(basis, ("id", "calculus", "subject"), "basis")
    basis_id = identity(basis["id"], "basis/id")
    calculus = obj(basis["calculus"], "basis/calculus")
    keys(calculus, ("uri", "sha256"), "calculus")
    require(calculus == {"uri": CALCULUS_URI, "sha256": CALCULUS_SHA256}, "unsupported or stale calculus basis")
    subject = obj(basis["subject"], "basis/subject")
    keys(subject, ("id", "sha256", "inventory"), "subject")
    identity(subject["id"], "subject/id")
    sha(subject["sha256"], "subject/sha256")
    inventory: set[str] = set()
    for item in seq(subject["inventory"], "subject/inventory"):
        coordinate(item, "subject/item")
        source_id = string(obj(item, "source")["id"], "source/id")
        require(source_id not in inventory, "duplicate subject inventory identity")
        inventory.add(source_id)
    require(bool(inventory), "empty subject inventory unsupported")
    coordinates = obj(document["coordinates"], "coordinates")
    keys(coordinates, ("context", "owner", "scope"), "coordinates")
    identity(coordinates["context"], "coordinates/context")
    identity(coordinates["owner"], "coordinates/owner")
    scope = strings(coordinates["scope"], "coordinates/scope")
    require(bool(scope), "empty scope")
    for scope_id in scope:
        identity(scope_id, "scope")
    signature_doc = obj(document["signature"], "signature")
    keys(signature_doc, ("id", "sha256", "definition"), "signature")
    signature_id = identity(signature_doc["id"], "signature/id")
    require(sha(signature_doc["sha256"], "signature/sha256") == digest({"id": signature_id, "definition": signature_doc["definition"]}), "stale signature digest")
    definition = obj(signature_doc["definition"], "signature/definition")
    keys(definition, ("fields", "sorts", "relation_kinds", "constraint_kinds", "residual_kinds", "judgment_kinds", "functor_kinds", "stop_kinds", "required_families"), "signature/definition")
    require(set(strings(definition["functor_kinds"], "functor_kinds")) <= set(FUNCTORS), "unknown functor kind")
    for stop in strings(definition["stop_kinds"], "stop_kinds"):
        identity(stop, "stop kind")
    required = strings(definition["required_families"], "required_families")
    require(set(required) <= set(CORE_FIELDS), "unknown required population")
    base_fields = obj(definition["fields"], "signature/fields")
    keys(base_fields, tuple(CORE_FIELDS), "signature/fields")
    external_contracts: set[tuple[str, str, str]] = set()
    for family, names in CORE_FIELDS.items():
        fields = obj(base_fields[family], "signature/" + family)
        keys(fields, names, "signature/" + family)
        require(obj(fields["id"], family)["type"] == "identity", "record id must be identity declaration")
        for name, schema in fields.items():
            schema_check(schema, family + "/" + name)
            external_contracts.update(_external_contracts(schema))
        for name in ("context", "owner", "basis"):
            _ref_type(fields[name], False, family + "/" + name)
        _ref_type(fields["scope"], True, family + "/scope")
    for family, (group, selector, override_names) in VARIANTS.items():
        _ref_type(obj(base_fields[family], family)[selector], False, family + "/" + selector)
        variants = obj(definition[group], group)
        for variant_id, overrides_value in variants.items():
            identity(variant_id, group)
            overrides = obj(overrides_value, variant_id)
            keys(overrides, override_names, variant_id)
            for name, schema in overrides.items():
                schema_check(schema, variant_id + "/" + name)
                external_contracts.update(_external_contracts(schema))
            if family == "relations":
                _ref_type(overrides["source"], False, variant_id + "/source")
                _ref_type(overrides["target"], False, variant_id + "/target")
            elif family in ("constraints", "residuals", "judgments"):
                _ref_type(overrides["applies_to" if family == "constraints" else "subject"], family == "constraints", variant_id)
    for family, scalar, arrays in (
        ("relations", ("source", "target"), ()),
        ("constraints", ("judgment_kind",), ("applies_to", "latitude_ref")),
        ("latitude", (), ("applies_to",)),
        ("residuals", ("subject",), ()),
        ("traversals", ("domain", "codomain", "authority"), ("preconditions", "postconditions", "evidence", "provenance", "stop_states")),
        ("transformations", ("traversal", "domain_model", "codomain_model", "operation_authority", "preservation_relation"), ("preconditions", "preserved", "introduced", "removed", "external_preserved", "external_introduced", "external_removed", "external_resolution_witnesses", "residuals", "evidence", "provenance", "stop_states")),
        ("judgments", ("subject", "evaluator", "authority"), ("evidence", "provenance")),
    ):
        fields = obj(base_fields[family], family)
        for name in scalar:
            _ref_type(fields[name], False, family + "/" + name)
        for name in arrays:
            _ref_type(fields[name], True, family + "/" + name)
    for family, field, array, target_family in (
        ("constraints", "latitude_ref", True, "latitude"),
        ("transformations", "traversal", False, "traversals"),
        ("transformations", "residuals", True, "residuals"),
    ):
        _fixed_local_family(obj(base_fields[family], family)[field], array, target_family, family + "/" + field)
    # These coordinates name complete models or exact external resolution tuples,
    # neither of which is one of the eight local fundamental record families.
    transformation_fields = obj(base_fields["transformations"], "transformations")
    for field in ("domain_model", "codomain_model"):
        _external_only(transformation_fields[field], False, "transformations/" + field)
    for field in ("external_preserved", "external_introduced", "external_removed", "external_resolution_witnesses"):
        _external_only(transformation_fields[field], True, "transformations/" + field)
    populations = obj(document["populations"], "populations")
    keys(populations, tuple(CORE_FIELDS), "populations")
    records: dict[str, Record] = {}
    for family, names in CORE_FIELDS.items():
        population = seq(populations[family], family)
        require(family not in required or bool(population), f"{family}: required population empty")
        for value in population:
            fields = obj(value, family)
            keys(fields, names, family)
            rid = identity(fields["id"], family + "/id")
            require(rid not in records, f"duplicate record identity {rid}")
            require(fields["basis"] == basis_id, f"{rid}: mixed basis unsupported")
            require(all(fields[k] == coordinates[k] for k in ("context", "owner", "scope")), f"{rid}: context/owner/scope mismatch")
            records[rid] = Record(family, rid, fields)
    external: dict[str, Object] = {}
    for value in seq(document["external_resolutions"], "external_resolutions"):
        resolution = obj(value, "external resolution")
        keys(resolution, RESOLUTION_FIELDS, "external resolution")
        for key, coordinate_value in resolution.items():
            identity(coordinate_value, "external resolution/" + key)
        eid = string(resolution["external_identity"], "external identity")
        require(eid not in external and eid not in records, f"duplicate or local/external collision {eid}")
        require(resolution["resolution_basis"] == basis_id, f"{eid}: external resolution basis mismatch")
        contract = (
            string(resolution["reference_domain"], "reference_domain"),
            string(resolution["external_target_kind"], "external_target_kind"),
            string(resolution["basis_relation"], "basis_relation"),
        )
        require(contract in external_contracts, f"{eid}: external resolution has no declared reference-domain contract")
        external[eid] = resolution
    universe = strings(document["identity_universe"], "identity_universe")
    require(set(universe) == set(records) | set(external), "identity universe is not exactly local disjoint-union external")
    signature = Signature(signature_id, definition)
    refs: list[Reference] = []
    for rid in sorted(records):
        record = records[rid]
        fields = signature.fields_for(record)
        for field in sorted(fields):
            check_value(record.fields[field], obj(fields[field], field), record, (field,), records, external, refs)
        if record.family == "constraints":
            require(record.fields["judgment_kind"] in obj(definition["judgment_kinds"], "judgment_kinds"), f"{rid}: unknown judgment kind")
        if record.family in ("traversals", "transformations"):
            require(set(strings(record.fields["stop_states"], "stop_states")) <= set(strings(definition["stop_kinds"], "stop_kinds")), f"{rid}: unknown stop kind")
    interpretation = obj(document["interpretation"], "interpretation")
    keys(interpretation, ("contract", "selection_ledger", "interpreter", "authority", "source_reentry", "invalidation", "provenance", "dispositions"), "interpretation")
    for field in ("contract", "selection_ledger", "interpreter", "authority", "source_reentry", "invalidation"):
        coordinate(interpretation[field], "interpretation/" + field)
    provenance = seq(interpretation["provenance"], "interpretation/provenance")
    require(bool(provenance), "interpretation provenance required")
    for coord in provenance:
        coordinate(coord, "interpretation/provenance")
    dispositions = seq(interpretation["dispositions"], "dispositions")
    seen_sources: set[str] = set()
    covered: set[str] = set()
    for value in dispositions:
        item = obj(value, "disposition")
        keys(item, ("source", "decision", "records", "authority", "basis", "reason"), "disposition")
        source_id = identity(item["source"], "disposition/source")
        require(source_id in inventory and source_id not in seen_sources, "unknown or duplicate disposition source")
        seen_sources.add(source_id)
        require(item["decision"] in ("retained", "omitted", "residual", "inapplicable", "refused"), "unknown disposition")
        selected = strings(item["records"], "disposition/records")
        require(set(selected) <= set(records), "disposition names unknown record")
        require(item["decision"] not in ("retained", "residual") or bool(selected), "retained/residual disposition requires records")
        require(item["decision"] != "residual" or any(records[r].family == "residuals" for r in selected), "residual disposition requires residual record")
        require(item["basis"] == basis_id and item["authority"] == obj(interpretation["authority"], "authority")["id"], "disposition basis/authority mismatch")
        string(item["reason"], "disposition/reason")
        covered.update(selected)
    require(seen_sources == inventory and covered == set(records), "selection ledger must cover exact inventory and every local record")
    require(obj(interpretation["selection_ledger"], "ledger")["sha256"] == digest(dispositions), "stale selection ledger digest")
    dependencies = obj(document["dependency_contract"], "dependency_contract")
    keys(dependencies, ("id", "required_relation_kinds", "attachment_families"), "dependency_contract")
    identity(dependencies["id"], "dependency_contract/id")
    governing = strings(dependencies["required_relation_kinds"], "required_relation_kinds")
    require(set(governing) <= set(obj(definition["relation_kinds"], "relation kinds")), "unknown governing relation kind")
    require(strings(dependencies["attachment_families"], "attachment_families") == ["constraints", "latitude", "residuals"], "profile requires complete attachment families")
    bindings = obj(document["functor_bindings"], "functor_bindings")
    require(set(bindings) == {r.identity for r in records.values() if r.family == "traversals"}, "functor bindings must cover exact traversal population")
    require(all(v in strings(definition["functor_kinds"], "functor kinds") for v in bindings.values()), "unknown functor binding")
    return Model(document, model_id, digest(document), signature, records, external, tuple(refs))


def validate(document: Object) -> Model:
    try:
        return _validate(document)
    except (KeyError, TypeError, RecursionError) as exc:
        raise Refusal(f"malformed or unsupported model: {exc}") from exc


def _fresh(model: Model) -> Model:
    current = validate(model.document)
    require(current == model, "validated model or derived coordinates changed; validate a new exact subject")
    return current


def model_identity(model: Model) -> Object:
    return {"id": model.identity, "sha256": model.sha256, "profile": MODEL_PROFILE}


def judgment_check(judgment: Object, model: Model) -> None:
    keys(judgment, ("id", "kind", "subject", "subject_digest", "context", "owner", "scope", "basis", "evaluator", "authority", "decision", "evidence", "provenance", "decided_at", "decision_contract"), "external semantic judgment")
    for field in ("id", "kind", "subject", "context", "owner", "basis", "evaluator"):
        identity(judgment[field], "judgment/" + field)
    require(judgment["kind"] == "urn:a-c:judgment-kind:semantic-acceptance", "encoding requires semantic-acceptance judgment")
    require(judgment["subject"] == model.identity and judgment["subject_digest"] == model.sha256, "judgment exact subject/digest mismatch")
    require(judgment["decision"] == "accepted", "semantic judgment is not accepted")
    require(judgment["basis"] == obj(model.document["basis"], "basis")["id"], "judgment basis mismatch")
    coords = obj(model.document["coordinates"], "coordinates")
    require(all(judgment[k] == coords[k] for k in ("context", "owner", "scope")), "judgment scope coordinates mismatch")
    interpretation = obj(model.document["interpretation"], "interpretation")
    for field in ("authority", "decision_contract"):
        coordinate(judgment[field], "judgment/" + field)
    require(judgment["authority"] == interpretation["authority"], "judgment authority differs from declared selection authority")
    require(judgment["decision_contract"] == interpretation["contract"], "judgment decision contract differs from declared contract")
    for field in ("evidence", "provenance"):
        values = seq(judgment[field], "judgment/" + field)
        require(bool(values), "judgment requires evidence and provenance")
        for value in values:
            coordinate(value, "judgment/" + field)
    string(judgment["decided_at"], "judgment/decided_at")


@dataclass(frozen=True)
class GraphCarrier:
    document: Object


def _node(node_id: str, role: str, payload: JSON) -> Object:
    return {"id": node_id, "label": node_id, "file_type": "document", "source_file": "a_c://authored-model", "ac_role": role, "ac_payload": payload}


def _edge(source: str, target: str, role: str) -> Object:
    return {"source": source, "target": target, "relation": role, "confidence": "EXTRACTED", "source_file": "a_c://authored-model", "ac_role": role}


def materialize(model: Model, judgment: Object | None = None) -> GraphCarrier:
    model = _fresh(model)
    if judgment is not None:
        judgment_check(judgment, model)
    envelope = {k: v for k, v in model.document.items() if k != "populations"}
    metadata: Object = {"profile": GRAPH_PROFILE, "model_identity": model_identity(model), "envelope": envelope, "claim": "proposed model representation; external judgment evidence does not change this subject or establish carrier admission"}
    nodes: list[JSON] = [_node("urn:a-c:graph:metadata", "metadata", metadata)]
    edges: list[JSON] = []
    record_nodes: dict[str, str] = {}
    external_nodes: dict[str, str] = {}
    ordinals: dict[str, int] = {}
    for family, population in obj(model.document["populations"], "populations").items():
        for ordinal, value in enumerate(seq(population, family)):
            ordinals[string(obj(value, family)["id"], "record/id")] = ordinal
    for i, rid in enumerate(sorted(model.records)):
        node_id = f"urn:a-c:graph:record:{i}"
        record_nodes[rid] = node_id
        record = model.records[rid]
        node = _node(node_id, "record", {"family": record.family, "ordinal": ordinals[rid], "record": record.fields})
        display = json.dumps(record.fields.get("value", record.fields.get("kind", "")), ensure_ascii=False, sort_keys=True)
        node["label"] = node_id + " " + record.identity + " " + display[:240]
        node["attributes"] = {
            "semantic_identity": record.identity,
            "record_family": record.family,
            "display_scope": "deterministic authored-field excerpts; complete record in ac_payload",
            **{k: json.dumps(v, ensure_ascii=False, sort_keys=True)[:512] for k, v in record.fields.items() if k not in ("id", "context", "owner", "scope", "basis")},
        }
        nodes.append(node)
    for i, eid in enumerate(sorted(model.external)):
        node_id = f"urn:a-c:graph:external:{i}"
        external_nodes[eid] = node_id
        nodes.append(_node(node_id, "external", model.external[eid]))
    for i, ref in enumerate(model.references):
        node_id = f"urn:a-c:graph:occurrence:{i}"
        endpoint_id = f"urn:a-c:graph:endpoint:{i}"
        nodes.append(_node(node_id, "reference-occurrence", {"owner": ref.owner, "path": list(ref.path), "target": ref.target}))
        nodes.append(_node(endpoint_id, "reference-endpoint", {"owner": ref.owner, "path": list(ref.path), "target": ref.target}))
        edges.append(_edge(record_nodes[ref.owner], node_id, "reference-owner"))
        edges.append(_edge(node_id, endpoint_id, "reference-slot"))
        target_node = record_nodes.get(ref.target, external_nodes.get(ref.target))
        assert target_node is not None
        edges.append(_edge(endpoint_id, target_node, "reference-target"))
    result: Object = {"directed": False, "multigraph": False, "graph": {"ac_profile": GRAPH_PROFILE}, "nodes": nodes, "links": edges}
    if judgment is not None:
        result["ac_evidence"] = {"semantic_judgment": judgment}
    return GraphCarrier(result)


def extraction(carrier: GraphCarrier) -> Object:
    result = {"nodes": carrier.document["nodes"], "edges": carrier.document["links"]}
    if "ac_evidence" in carrier.document:
        result["ac_evidence"] = carrier.document["ac_evidence"]
    return result


def _normalized_graph(document: Object) -> tuple[dict[str, Object], dict[tuple[str, str], Object]]:
    # Flagless extraction input is supported; supplied node-link declarations
    # must agree with this exact undirected, simple graph profile.
    for field in ("directed", "multigraph"):
        if field in document:
            require(document[field] is False, f"{field}: carrier profile requires exact Boolean false")
    if "graph" in document:
        graph_metadata = obj(document["graph"], "graph metadata")
        if "ac_profile" in graph_metadata:
            require(graph_metadata["ac_profile"] == GRAPH_PROFILE, "unsupported graph.ac_profile")
    nodes: dict[str, Object] = {}
    for value in seq(document.get("nodes"), "graph/nodes"):
        node = obj(value, "graph/node")
        required: tuple[str, ...] = ("id", "label", "file_type", "source_file", "ac_role", "ac_payload")
        if node.get("ac_role") == "record":
            required += ("attributes",)
        require(set(required) <= set(node), "missing tenant-owned node attribute")
        node_id = string(node["id"], "node/id")
        require(node_id not in nodes, "duplicate graph node")
        nodes[node_id] = {k: node[k] for k in required}
        grammar(nodes[node_id])
    require(not ("links" in document and "edges" in document), "ambiguous links and edges")
    edges: dict[tuple[str, str], Object] = {}
    for value in seq(document.get("links", document.get("edges")), "graph/links"):
        edge = obj(value, "graph/edge")
        required = ("source", "target", "relation", "confidence", "source_file", "ac_role")
        require(set(required) <= set(edge), "missing tenant-owned edge attribute")
        source, target = string(edge["source"], "edge/source"), string(edge["target"], "edge/target")
        require(source in nodes and target in nodes, "dangling graph edge")
        key = (source, target) if source <= target else (target, source)
        require(key not in edges, "collapsed or duplicated graph edge")
        # Upstream's undirected writer may reverse endpoints. Occurrence payloads
        # bind semantic direction; endpoint membership is checked independently.
        edges[key] = {k: edge[k] for k in required if k not in ("source", "target")}
        grammar(edges[key])
    return nodes, edges


def _decode(carrier: GraphCarrier) -> Model:
    grammar(carrier.document, annotations=True)
    nodes, edges = _normalized_graph(carrier.document)
    metadata_nodes = [n for n in nodes.values() if n["ac_role"] == "metadata"]
    require(len(metadata_nodes) == 1, "exactly one metadata node required")
    metadata = obj(metadata_nodes[0]["ac_payload"], "metadata")
    keys(metadata, ("profile", "model_identity", "envelope", "claim"), "metadata")
    require(metadata["profile"] == GRAPH_PROFILE, "unsupported carrier profile")
    document = dict(obj(metadata["envelope"], "envelope"))
    require("populations" not in document, "embedded populations are not a decoding source")
    populations: Object = {family: [] for family in CORE_FIELDS}
    ordered: dict[str, dict[int, JSON]] = {family: {} for family in CORE_FIELDS}
    for node in nodes.values():
        if node["ac_role"] == "record":
            payload = obj(node["ac_payload"], "record payload")
            keys(payload, ("family", "ordinal", "record"), "record payload")
            family = string(payload["family"], "record family")
            require(family in populations, "unknown record family")
            ordinal = payload["ordinal"]
            require(type(ordinal) is int and ordinal >= 0, "bad population ordinal")
            index = cast(int, ordinal)
            require(index not in ordered[family], "duplicate population ordinal")
            ordered[family][index] = payload["record"]
    for family, members in ordered.items():
        require(set(members) == set(range(len(members))), "missing population ordinal")
        populations[family] = [members[i] for i in range(len(members))]
    document["populations"] = populations
    model = validate(document)
    require(metadata["model_identity"] == model_identity(model), "model identity/digest mismatch")
    if "ac_evidence" in carrier.document:
        evidence = obj(carrier.document["ac_evidence"], "ac_evidence")
        keys(evidence, ("semantic_judgment",), "ac_evidence")
        judgment_check(obj(evidence["semantic_judgment"], "semantic judgment"), model)
    expected_nodes, expected_edges = _normalized_graph(materialize(model).document)
    require(nodes == expected_nodes and edges == expected_edges, "graph differs from complete semantic encoding")
    return model


def decode(carrier: GraphCarrier) -> Model:
    try:
        return _decode(carrier)
    except (KeyError, TypeError, RecursionError) as exc:
        raise Refusal(f"malformed or unsupported carrier: {exc}") from exc


def carrier_identity(carrier: GraphCarrier) -> Object:
    """Identity of checked semantic representation; excludes external evidence."""
    model = decode(carrier)
    semantic = materialize(model).document
    return {"profile": GRAPH_PROFILE, "sha256": digest(semantic), "model": model_identity(model)}


def inspect(model: Model, record_id: str) -> Object:
    model = _fresh(model)
    require(record_id in model.records, "unknown local identity")
    record = model.records[record_id]
    return {"parent": model_identity(model), "family": record.family, "record": record.fields, "references": [{"path": list(r.path), "target": r.target, "domain": r.schema["domain"]} for r in model.references if r.owner == record_id], "claim": "typed structural references only"}


def find(model: Model, text: str) -> Object:
    model = _fresh(model)
    require(bool(text), "empty search unsupported")
    matches: list[JSON] = [{"id": r.identity, "family": r.family} for r in model.records.values() if text.casefold() in canonical(r.fields).decode("utf-8").casefold()]
    return {"parent": model_identity(model), "query": text, "matches": matches, "scope": "literal case-insensitive record content; no inference or ranking"}


@dataclass(frozen=True)
class _ProjectionIndex:
    """Indexes scoped to one checked operation, never cached on a mutable model."""

    identities: tuple[str, ...]
    dependencies: Mapping[str, set[str]]
    references: Mapping[str, list[tuple[int, Reference]]]
    families: Mapping[str, list[Record]]


def _projection_index(model: Model) -> _ProjectionIndex:
    contract = obj(model.document["dependency_contract"], "dependency_contract")
    governing = set(strings(contract["required_relation_kinds"], "required relation kinds"))
    dependencies: dict[str, set[str]] = {rid: set() for rid in model.records}
    references: dict[str, list[tuple[int, Reference]]] = {rid: [] for rid in model.records}
    families: dict[str, list[Record]] = {family: [] for family in CORE_FIELDS}
    for ordinal, ref in enumerate(model.references):
        references[ref.owner].append((ordinal, ref))
        if ref.target in model.records and ref.schema["governing"] is True:
            dependencies[ref.owner].add(ref.target)
    for record in model.records.values():
        families[record.family].append(record)
        if record.family == "relations" and record.fields["kind"] in governing:
            source = string(record.fields["source"], "source")
            target = string(record.fields["target"], "target")
            if source in model.records:
                dependencies[source].add(record.identity)
                dependencies[record.identity].add(source)
            if target in model.records:
                dependencies[record.identity].add(target)
        if record.family in ("constraints", "latitude", "residuals"):
            field = "subject" if record.family == "residuals" else "applies_to"
            subjects = [record.fields[field]] if field == "subject" else seq(record.fields[field], field)
            for value in subjects:
                subject = string(value, field)
                if subject in model.records:
                    dependencies[subject].add(record.identity)
    return _ProjectionIndex(tuple(sorted(model.records)), dependencies, references, families)


def _project_checked(model: Model, index: _ProjectionIndex, seeds: Sequence[str], budget: int | None) -> Object:
    require(bool(seeds) and len(set(seeds)) == len(seeds), "nonempty unique seeds required")
    require(all(seed in model.records for seed in seeds), "seed is not a local identity")
    require(budget is None or budget >= 0, "negative budget")
    contract = obj(model.document["dependency_contract"], "dependency_contract")
    included = set(seeds)
    pending = list(seeds)
    while pending:
        for target in index.dependencies[pending.pop()]:
            if target not in included:
                included.add(target)
                pending.append(target)
    require(budget is None or len(included) <= budget, f"required closure needs {len(included)} records; budget {budget} refuses without truncation")
    selected_references = sorted((entry for rid in included for entry in index.references[rid]), key=lambda entry: entry[0])
    external = sorted({ref.target for _, ref in selected_references if ref.target in model.external})
    crossing: list[JSON] = []
    for record in index.families["relations"]:
        if record.identity not in included:
            if record.fields["source"] in included or record.fields["target"] in included:
                crossing.append({"id": record.identity, "kind": record.fields["kind"], "source": record.fields["source"], "target": record.fields["target"]})
    populations: Object = {family: [r.fields for r in index.families[family] if r.identity in included] for family in CORE_FIELDS}
    non_governing_boundary: list[JSON] = [{"owner": r.owner, "path": list(r.path), "target": r.target, "domain": r.schema["domain"]} for _, r in selected_references if r.target in model.records and r.target not in included]
    seed_values: list[JSON] = list(seeds)
    included_values: list[JSON] = [v for v in sorted(included)]
    excluded_values: list[JSON] = [v for v in index.identities if v not in included]
    residual_values: list[JSON] = [v for v in sorted(rid for rid in included if model.records[rid].family == "residuals")]
    return {"profile": "a_c.graphify.projection/1", "parent": model_identity(model), "selection": {"seeds": seed_values, "dependency_contract": contract, "budget_records": budget}, "included": included_values, "excluded": excluded_values, "populations": populations, "boundary": {"external": [model.external[eid] for eid in external], "unresolved_residuals": residual_values, "crossing_relations": crossing, "non_governing_references": non_governing_boundary, "invalidation": obj(model.document["interpretation"], "interpretation")["invalidation"]}, "claim": "view of exact parent; not a replacement complete model or semantic acceptance"}


def project(model: Model, seeds: Sequence[str], budget: int | None = None) -> Object:
    model = _fresh(model)
    return _project_checked(model, _projection_index(model), seeds, budget)


def project_many(model: Model, selections: Sequence[tuple[Sequence[str], int | None]]) -> list[Object]:
    """Project an ordered batch with one freshness check; any refusal aborts it."""
    model = _fresh(model)
    index = _projection_index(model)
    return [_project_checked(model, index, seeds, budget) for seeds, budget in selections]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "materialize", "encode", "decode", "find", "inspect", "project"):
        child = sub.add_parser(command)
        child.add_argument("input")
        if command in ("materialize", "encode", "decode", "project"):
            child.add_argument("--out", required=True)
        if command in ("materialize", "encode"):
            child.add_argument("--extraction", action="store_true")
        if command == "encode":
            child.add_argument("--judgment", required=True)
        if command == "find":
            child.add_argument("text")
        if command == "inspect":
            child.add_argument("identity")
        if command == "project":
            child.add_argument("--seed", action="append", required=True)
            child.add_argument("--budget", type=int)
    for command in ("transform", "overlay", "execute", "evaluate-predicate"):
        sub.add_parser(command)
    args = parser.parse_args(argv)
    try:
        if args.command in ("transform", "overlay", "execute", "evaluate-predicate"):
            raise Refusal(f"{args.command} is unsupported by this declared fragment")
        if hasattr(args, "out"):
            output_path = Path(args.out)
            inputs = [Path(args.input)]
            if args.command == "encode":
                inputs.append(Path(args.judgment))
            for input_path in inputs:
                require(output_path.resolve() != input_path.resolve(), "output aliases an unchanged input subject")
                require(not (output_path.exists() and input_path.exists() and output_path.samefile(input_path)), "output aliases an unchanged input subject")
            require(not output_path.exists(), "output already exists; choose a fresh artifact path")
        source = read_json(args.input)
        if args.command == "decode":
            model = decode(GraphCarrier(source))
            write_json(args.out, model.document)
            result: Object = {"status": "decoded", "model": model_identity(model)}
        elif args.command in ("materialize", "encode"):
            model = validate(source)
            judgment = read_json(args.judgment) if args.command == "encode" else None
            carrier = materialize(model, judgment)
            write_json(args.out, extraction(carrier) if args.extraction else carrier.document)
            result = {"status": "proposal-view" if judgment is None else "supplied-accepted-judgment-encoding", "model": model_identity(model), "claim": "no issuer-authority proof or carrier admission"}
        elif args.command == "validate":
            model = validate(source)
            result = {"status": "structurally-checked", "model": model_identity(model), "records": len(model.records), "references": len(model.references), "claim": "declared fragment only; no semantic acceptance or full calculus validity"}
        else:
            model = decode(GraphCarrier(source))
            if args.command == "find":
                result = find(model, args.text)
            elif args.command == "inspect":
                result = inspect(model, args.identity)
            else:
                result = project(model, args.seed, args.budget)
                write_json(args.out, result)
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
    except (Refusal, KeyError, TypeError, RecursionError) as exc:
        print(json.dumps({"status": "refusal", "reason": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
