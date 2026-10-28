#!/usr/bin/env python3
"""Independent, bounded source-data bridge; this Python code is not Lean-proved.

Only the two pinned signatures are supported. Complete source fields are retained.
No Graphify, v3 implementation, network service or third-party Python package
is loaded. See design/IMPORTER.md for checked and unproved properties.
"""
from __future__ import annotations

import argparse
from collections import deque
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import sys

FAMILIES = (
    "objects", "relations", "constraints", "latitude", "residuals",
    "traversals", "transformations", "judgments",
)
MODEL_FIELDS = (
    "profile", "id", "basis", "coordinates", "signature", "interpretation",
    "identity_universe", "external_resolutions", "populations",
    "dependency_contract", "functor_bindings",
)
MODEL_PROFILE = "a_c.graphify.model/1"
CARRIER_PROFILE = "a_c.graphify.carrier/1"
CALCULUS_URI = "stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md"
CALCULUS_SHA256 = "cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d"
SIGNATURE_SHA256 = "ba18237c16ba9bed43b058c27b135a7bb2f19fd8d79ee0ac76b309df26ba3ee7"
TOY_SIGNATURE_SHA256 = "2b5fe15584eba0e75c0c033b6f9ee5aac4fe45a41fad919e14fd544fa871419c"
TOY_RAW_SHA256 = "a72d423a222ecd84a429e28796c93ba07ac8b79d40caf3b74af02c36029f3b0b"
TOY_MODEL_SHA256 = "d275eb906b8ac2871e6fd7415065c1dabf915242e8583fe3e202bc723a18dec3"
MODEL_SHA256 = "b3f97a2667c277c21417230421aca02c26b3a7b19baa598197e94f67c5439151"
RAW_SHA256 = {
    "MODEL.json": "fc3114dd666218c387a64846b755a14979182f488de64ffff6a6d305a9698793",
    "CARRIER.json": "e77be91716c8f4a7e45ba19fabd818b88115c40872dd22d754f896892b584b8b",
    "GRAPHIFY_EXTRACTION.json": "5a8115141979c4e5873256a816c483a8cd64f906d08555aaee73c0cf0a3e33cb",
}
FIXTURE_DIR = Path(__file__).resolve().parents[1] / "fixtures" / "stdo-3.0.2"
TOY_FIXTURE_DIR = FIXTURE_DIR.parent / "toy"
VARIANTS = {
    "objects": ("sorts", "sort"),
    "relations": ("relation_kinds", "kind"),
    "constraints": ("constraint_kinds", "kind"),
    "residuals": ("residual_kinds", "kind"),
    "judgments": ("judgment_kinds", "kind"),
}
RESOLUTION_FIELDS = (
    "external_identity", "reference_domain", "external_target_kind",
    "resolved_target_identity", "basis_relation", "resolution_basis",
    "evidence_identity",
)


class Refusal(ValueError):
    """The requested source/certificate is outside or violates this contract."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Refusal(message)


def _object(value, where: str) -> dict:
    require(type(value) is dict, f"{where}: expected object")
    return value


def _array(value, where: str) -> list:
    require(type(value) is list, f"{where}: expected array")
    return value


def _exact(value, fields, where: str) -> dict:
    value = _object(value, where)
    require(set(value) == set(fields), f"{where}: missing or unknown fields")
    return value


def _identity(value, where: str) -> str:
    require(type(value) is str and re.fullmatch(r"[A-Za-z][A-Za-z0-9+.-]*:\S+", value) is not None,
            f"{where}: expected explicit identity")
    return value


def _unique_strings(value, where: str) -> list[str]:
    values = _array(value, where)
    require(all(type(v) is str for v in values), f"{where}: expected strings")
    require(len(values) == len(set(values)), f"{where}: duplicate member")
    return values


def _sha(value, where: str) -> str:
    require(type(value) is str and re.fullmatch(r"[0-9a-f]{64}", value) is not None,
            f"{where}: expected lowercase SHA-256")
    return value


def _coordinate(value, where: str) -> None:
    _exact(value, ("id", "sha256"), where)
    _identity(value["id"], where)
    _sha(value["sha256"], where)


def _grammar(value, depth: int = 0) -> None:
    require(depth < 100, "JSON nesting exceeds supported depth")
    if value is None or type(value) in (bool, int):
        return
    if type(value) is str:
        try:
            value.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise Refusal("unpaired Unicode surrogate") from exc
        return
    if type(value) is list:
        for item in value:
            _grammar(item, depth + 1)
        return
    if type(value) is dict:
        for key, item in value.items():
            require(type(key) is str, "object key is not a string")
            _grammar(key, depth + 1)
            _grammar(item, depth + 1)
        return
    raise Refusal("only integer-valued JSON is supported")


def canonical(value) -> str:
    _grammar(value)
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value) -> str:
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def _pairs(pairs) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: str | Path) -> dict:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=_pairs)
        _grammar(value)
        return _object(value, "document")
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        raise Refusal(f"unreadable JSON: {exc}") from exc


def _schema(schema: dict, contracts: set) -> None:
    """Check the finite schema language, collecting *all* external contracts."""
    _object(schema, "schema")
    kind = schema.get("type")
    if kind in ("identity", "integer", "boolean", "null"):
        _exact(schema, ("type",), "scalar schema")
    elif kind == "string":
        require(set(schema) <= {"type", "min_length"}, "unsupported string schema")
        require(type(schema.get("min_length", 0)) is int and schema.get("min_length", 0) >= 0,
                "invalid minimum string length")
    elif kind == "enum":
        _exact(schema, ("type", "values"), "enum schema")
        require(bool(_unique_strings(schema["values"], "enum")), "empty enum")
    elif kind == "array":
        require({"type", "items"} <= set(schema) <= {"type", "items", "min_items", "max_items"},
                "unsupported array schema")
        low, high = schema.get("min_items", 0), schema.get("max_items")
        require(type(low) is int and low >= 0, "invalid minimum cardinality")
        require(high is None or (type(high) is int and high >= low), "invalid maximum cardinality")
        _schema(schema["items"], contracts)
    elif kind == "object":
        _exact(schema, ("type", "fields"), "object schema")
        for field in _object(schema["fields"], "schema fields").values():
            _schema(field, contracts)
    elif kind == "ref":
        _exact(schema, ("type", "domain", "local_families", "local_sorts", "external_kinds",
                        "basis_relation", "governing"), "reference schema")
        _identity(schema["domain"], "reference domain")
        _identity(schema["basis_relation"], "reference basis relation")
        require(type(schema["governing"]) is bool, "governing must be Boolean")
        require(set(_unique_strings(schema["local_families"], "local families")) <= set(FAMILIES),
                "unknown local family")
        for key in ("local_sorts", "external_kinds"):
            for value in _unique_strings(schema[key], key):
                _identity(value, key)
        contracts.update((schema["domain"], kind, schema["basis_relation"])
                         for kind in schema["external_kinds"])
    else:
        raise Refusal(f"unsupported schema type: {kind}")


def _check_value(value, schema, owner, path, local, external, references) -> None:
    where = f"record[{owner}]/{'/'.join(str(segment) for segment in path)}"
    kind = schema["type"]
    if kind == "ref":
        target = _identity(value, where)
        require((target in local) != (target in external), f"{where}: dangling/ambiguous reference")
        if target in local:
            record = local[target]
            require(record["family"] in schema["local_families"], f"{where}: wrong local family")
            require(record["family"] != "objects" or not schema["local_sorts"]
                    or record["record"]["sort"] in schema["local_sorts"], f"{where}: wrong local sort")
            resolved = record["index"]
        else:
            remote = external[target]
            require(remote["external_target_kind"] in schema["external_kinds"], f"{where}: wrong external kind")
            require(remote["reference_domain"] == schema["domain"] and
                    remote["basis_relation"] == schema["basis_relation"], f"{where}: external domain/basis mismatch")
            resolved = target
        references.append({"owner": owner, "path": list(path), "target": resolved,
                           "governing": schema["governing"], "domain": schema["domain"],
                           "schema": deepcopy(schema)})
    elif kind == "identity":
        _identity(value, where)
        require(path == ("id",), "identity declaration outside record id")
    elif kind == "array":
        values = _array(value, where)
        require(len(values) >= schema.get("min_items", 0), f"{where}: below minimum cardinality")
        require("max_items" not in schema or len(values) <= schema["max_items"], f"{where}: above maximum cardinality")
        for ordinal, item in enumerate(values):
            _check_value(item, schema["items"], owner, path + (ordinal,), local, external, references)
    elif kind == "object":
        _exact(value, schema["fields"], where)
        for field in sorted(schema["fields"]):
            _check_value(value[field], schema["fields"][field], owner, path + (field,), local, external, references)
    elif kind == "string":
        require(type(value) is str and len(value) >= schema.get("min_length", 0), f"{where}: expected string")
    elif kind == "enum":
        require(type(value) is str and value in schema["values"], f"{where}: unknown enum")
    elif kind == "integer":
        require(type(value) is int, f"{where}: expected integer")
    elif kind == "boolean":
        require(type(value) is bool, f"{where}: expected Boolean")
    elif kind == "null":
        require(value is None, f"{where}: expected null")
    else:
        raise Refusal(f"unsupported value type: {kind}")


def _import_model(model: dict) -> dict:
    _grammar(model)
    _exact(model, MODEL_FIELDS, "model")
    require(model["profile"] == MODEL_PROFILE, "unsupported model profile")
    _identity(model["id"], "model id")
    basis = _exact(model["basis"], ("id", "calculus", "subject"), "basis")
    _identity(basis["id"], "basis id")
    require(basis["calculus"] == {"uri": CALCULUS_URI, "sha256": CALCULUS_SHA256}, "unsupported calculus basis")
    subject = _exact(basis["subject"], ("id", "sha256", "inventory"), "subject")
    _identity(subject["id"], "subject id")
    _sha(subject["sha256"], "subject digest")
    inventory = []
    for item in _array(subject["inventory"], "inventory"):
        _coordinate(item, "inventory coordinate")
        inventory.append(item["id"])
    require(bool(inventory) and len(inventory) == len(set(inventory)), "empty or duplicate subject inventory")
    coords = _exact(model["coordinates"], ("context", "owner", "scope"), "coordinates")
    _identity(coords["context"], "context")
    _identity(coords["owner"], "owner")
    require(bool(_unique_strings(coords["scope"], "scope")), "empty scope")
    for value in coords["scope"]:
        _identity(value, "scope")

    signature = _exact(model["signature"], ("id", "sha256", "definition"), "signature")
    require(signature["sha256"] in (SIGNATURE_SHA256, TOY_SIGNATURE_SHA256) and
            digest({"id": signature["id"], "definition": signature["definition"]}) == signature["sha256"],
            "unsupported or stale signature; this adapter requires a pinned signature")
    definition = signature["definition"]
    contracts = set()
    for fields in definition["fields"].values():
        for schema in fields.values():
            _schema(schema, contracts)
    for group, _ in VARIANTS.values():
        for fields in definition[group].values():
            for schema in fields.values():
                _schema(schema, contracts)

    populations = _exact(model["populations"], FAMILIES, "populations")
    records, local = [], {}
    for family in FAMILIES:
        population = _array(populations[family], family)
        require(family not in definition["required_families"] or bool(population), "empty required population")
        for ordinal, record in enumerate(population):
            _exact(record, definition["fields"][family], family)
            rid = _identity(record["id"], "record id")
            require(rid not in local, "duplicate local identity")
            require(record["basis"] == basis["id"], "mixed record basis")
            require(all(record[k] == coords[k] for k in coords), "record context/owner/scope mismatch")
            entry = {"index": len(records), "family": family, "ordinal": ordinal, "record": deepcopy(record)}
            records.append(entry)
            local[rid] = entry

    external = {}
    for resolution in _array(model["external_resolutions"], "external resolutions"):
        _exact(resolution, RESOLUTION_FIELDS, "external resolution")
        for field, value in resolution.items():
            _identity(value, field)
        eid = resolution["external_identity"]
        require(eid not in local and eid not in external, "duplicate or colliding external identity")
        require(resolution["resolution_basis"] == basis["id"], "external resolution basis mismatch")
        require((resolution["reference_domain"], resolution["external_target_kind"], resolution["basis_relation"])
                in contracts, "undeclared external resolution contract")
        external[eid] = resolution
    universe = _unique_strings(model["identity_universe"], "identity universe")
    require(set(universe) == set(local) | set(external), "identity universe differs from local/external union")

    references = []
    for rid in sorted(local):
        item, record = local[rid], local[rid]["record"]
        family = item["family"]
        fields = dict(definition["fields"][family])
        if family in VARIANTS:
            group, selector = VARIANTS[family]
            require(record[selector] in definition[group], "undeclared sort/kind")
            fields.update(definition[group][record[selector]])
        for field in sorted(fields):
            _check_value(record[field], fields[field], item["index"], (field,), local, external, references)
        if family == "constraints":
            require(record["judgment_kind"] in definition["judgment_kinds"], "unknown constraint judgment kind")
        if family in ("traversals", "transformations"):
            require(set(record["stop_states"]) <= set(definition["stop_kinds"]), "unknown stop state")

    interpretation = _exact(model["interpretation"], (
        "contract", "selection_ledger", "interpreter", "authority", "source_reentry",
        "invalidation", "provenance", "dispositions"), "interpretation")
    for key in ("contract", "selection_ledger", "interpreter", "authority", "source_reentry", "invalidation"):
        _coordinate(interpretation[key], key)
    require(bool(_array(interpretation["provenance"], "provenance")), "missing interpretation provenance")
    for item in interpretation["provenance"]:
        _coordinate(item, "provenance")
    sources, covered = set(), set()
    for disposition in _array(interpretation["dispositions"], "dispositions"):
        _exact(disposition, ("source", "decision", "records", "authority", "basis", "reason"), "disposition")
        source = _identity(disposition["source"], "disposition source")
        require(source in inventory and source not in sources, "duplicate/unknown disposition source")
        sources.add(source)
        require(disposition["decision"] in ("retained", "omitted", "residual", "inapplicable", "refused"), "unknown disposition")
        named = _unique_strings(disposition["records"], "disposition records")
        require(set(named) <= set(local), "disposition names missing record")
        require(disposition["decision"] not in ("retained", "residual") or bool(named), "missing retained record")
        require(disposition["decision"] != "residual" or any(local[r]["family"] == "residuals" for r in named), "missing residual disposition")
        require(disposition["basis"] == basis["id"] and disposition["authority"] == interpretation["authority"]["id"], "disposition basis/authority mismatch")
        require(type(disposition["reason"]) is str and bool(disposition["reason"]), "missing disposition reason")
        covered.update(named)
    require(sources == set(inventory) and covered == set(local), "incomplete source/record dispositions")
    require(interpretation["selection_ledger"]["sha256"] == digest(interpretation["dispositions"]), "stale selection ledger")

    dependency = _exact(model["dependency_contract"], ("id", "required_relation_kinds", "attachment_families"), "dependency contract")
    _identity(dependency["id"], "dependency id")
    governing = _unique_strings(dependency["required_relation_kinds"], "required relation kinds")
    require(set(governing) <= set(definition["relation_kinds"]), "unknown governing relation kind")
    require(dependency["attachment_families"] == ["constraints", "latitude", "residuals"], "incomplete attachment family declaration")
    bindings = _object(model["functor_bindings"], "functor bindings")
    require(set(bindings) == {r["record"]["id"] for r in records if r["family"] == "traversals"}, "incomplete traversal bindings")
    require(all(k in definition["functor_kinds"] for k in bindings.values()), "unknown functor binding")

    edges = {(ref["owner"], ref["target"]) for ref in references
             if type(ref["target"]) is int and ref["governing"]}
    for item in records:
        record, index, family = item["record"], item["index"], item["family"]
        if family == "relations" and record["kind"] in governing:
            if record["source"] in local:
                source = local[record["source"]]["index"]
                edges.update(((source, index), (index, source)))
            if record["target"] in local:
                edges.add((index, local[record["target"]]["index"]))
        if family in dependency["attachment_families"]:
            subjects = [record["subject"]] if family == "residuals" else record["applies_to"]
            edges.update((local[s]["index"], index) for s in subjects if s in local)
    return {"envelope": deepcopy({k: v for k, v in model.items() if k != "populations"}),
            "records": records, "references": references,
            "edges": [list(edge) for edge in sorted(edges)], "model_sha256": digest(model)}


def import_model(model: dict) -> dict:
    try:
        return _import_model(model)
    except (KeyError, TypeError, RecursionError) as exc:
        raise Refusal(f"malformed source model: {exc}") from exc


def reconstruct(imported: dict) -> dict:
    """Recover every source field, including empty population keys and order."""
    model = deepcopy(imported["envelope"])
    require("populations" not in model, "envelope cannot embed populations")
    model["populations"] = {family: [] for family in FAMILIES}
    for index, item in enumerate(imported["records"]):
        require(item["index"] == index and item["family"] in FAMILIES, "bad imported record coordinate")
        population = model["populations"][item["family"]]
        require(item["ordinal"] == len(population), "bad imported population ordinal")
        population.append(deepcopy(item["record"]))
    return model


def check_imported(imported: dict) -> None:
    try:
        require(canonical(import_model(reconstruct(imported))) == canonical(imported), "stale or altered imported data")
    except (KeyError, TypeError, RecursionError) as exc:
        raise Refusal(f"malformed imported data: {exc}") from exc


def _node(node_id, role, payload):
    return {"id": node_id, "label": node_id, "file_type": "document",
            "source_file": "a_c://authored-model", "ac_role": role, "ac_payload": payload}


def _expected_carrier(imported: dict) -> dict:
    """Reconstruct the declared carrier profile without loading its producer."""
    envelope, records = imported["envelope"], imported["records"]
    identity = {"id": envelope["id"], "sha256": imported["model_sha256"], "profile": MODEL_PROFILE}
    metadata = {"profile": CARRIER_PROFILE, "model_identity": identity, "envelope": envelope,
                "claim": "proposed model representation; external judgment evidence does not change this subject or establish carrier admission"}
    nodes = [_node("urn:a-c:graph:metadata", "metadata", metadata)]
    local_nodes, external_nodes = {}, {}
    for number, item in enumerate(sorted(records, key=lambda r: r["record"]["id"])):
        record = item["record"]
        nid = f"urn:a-c:graph:record:{number}"
        local_nodes[item["index"]] = nid
        node = _node(nid, "record", {"family": item["family"], "ordinal": item["ordinal"], "record": record})
        display = json.dumps(record.get("value", record.get("kind", "")), sort_keys=True, ensure_ascii=False)
        node["label"] = nid + " " + record["id"] + " " + display[:240]
        node["attributes"] = {
            "semantic_identity": record["id"], "record_family": item["family"],
            "display_scope": "deterministic authored-field excerpts; complete record in ac_payload",
            **{key: json.dumps(value, sort_keys=True, ensure_ascii=False)[:512]
               for key, value in record.items() if key not in ("id", "context", "owner", "scope", "basis")},
        }
        nodes.append(node)
    for number, resolution in enumerate(sorted(envelope["external_resolutions"], key=lambda r: r["external_identity"])):
        nid = f"urn:a-c:graph:external:{number}"
        external_nodes[resolution["external_identity"]] = nid
        nodes.append(_node(nid, "external", resolution))
    edges = []
    for number, ref in enumerate(imported["references"]):
        occurrence, endpoint = f"urn:a-c:graph:occurrence:{number}", f"urn:a-c:graph:endpoint:{number}"
        target = ref["target"]
        # The source-derived path is typed; only the optional legacy carrier
        # profile serializes array positions as strings. Never feed that lossy
        # path encoding into the formal Reference.path.
        payload = {"owner": records[ref["owner"]]["record"]["id"], "path": [str(step) for step in ref["path"]],
                   "target": records[target]["record"]["id"] if type(target) is int else target}
        nodes.extend((_node(occurrence, "reference-occurrence", payload), _node(endpoint, "reference-endpoint", payload)))
        target_node = local_nodes[target] if type(target) is int else external_nodes[target]
        for source, destination, role in (
            (local_nodes[ref["owner"]], occurrence, "reference-owner"),
            (occurrence, endpoint, "reference-slot"),
            (endpoint, target_node, "reference-target"),
        ):
            edges.append({"source": source, "target": destination, "relation": role,
                          "confidence": "EXTRACTED", "source_file": "a_c://authored-model", "ac_role": role})
    return {"nodes": nodes, "edges": edges}


def _normalized_carrier(carrier: dict) -> tuple[dict, dict]:
    _grammar(carrier)
    if "links" in carrier:
        _exact(carrier, ("directed", "multigraph", "graph", "nodes", "links"), "native carrier")
        require(carrier["directed"] is False and carrier["multigraph"] is False, "carrier flags must be Boolean false")
        require(carrier["graph"] == {"ac_profile": CARRIER_PROFILE}, "carrier profile mismatch")
        edge_values = carrier["links"]
    else:
        _exact(carrier, ("nodes", "edges"), "extraction carrier")
        edge_values = carrier["edges"]
    nodes, edges = {}, {}
    for node in _array(carrier["nodes"], "carrier nodes"):
        _object(node, "carrier node")
        expected = ["id", "label", "file_type", "source_file", "ac_role", "ac_payload"]
        if node.get("ac_role") == "record":
            expected.append("attributes")
        _exact(node, expected, "carrier node")
        nid = _identity(node["id"], "node id")
        require(nid not in nodes, "duplicate carrier node")
        nodes[nid] = node
    for edge in _array(edge_values, "carrier edges"):
        _exact(edge, ("source", "target", "relation", "confidence", "source_file", "ac_role"), "carrier edge")
        source, target = edge["source"], edge["target"]
        require(type(source) is str and type(target) is str and source in nodes and target in nodes,
                "dangling carrier edge")
        key = tuple(sorted((source, target)))
        require(key not in edges, "duplicate/collapsed carrier edge")
        edges[key] = {k: v for k, v in edge.items() if k not in ("source", "target")}
    return nodes, edges


def recover_carrier(carrier: dict) -> dict:
    """Recover source records, then check every carrier node/edge/display field."""
    try:
        nodes, edges = _normalized_carrier(carrier)
        metadata = [n["ac_payload"] for n in nodes.values() if n["ac_role"] == "metadata"]
        require(len(metadata) == 1, "carrier must contain exactly one metadata node")
        _exact(metadata[0], ("profile", "model_identity", "envelope", "claim"), "carrier metadata")
        model = deepcopy(_object(metadata[0]["envelope"], "carrier envelope"))
        require("populations" not in model, "carrier embeds a duplicate population source")
        populations = {family: {} for family in FAMILIES}
        for node in nodes.values():
            if node["ac_role"] == "record":
                payload = _exact(node["ac_payload"], ("family", "ordinal", "record"), "record payload")
                family, ordinal = payload["family"], payload["ordinal"]
                require(type(family) is str and family in populations, "unknown carrier family")
                require(type(ordinal) is int and ordinal >= 0 and ordinal not in populations[family], "bad carrier ordinal")
                populations[family][ordinal] = payload["record"]
        model["populations"] = {}
        for family, population in populations.items():
            require(set(population) == set(range(len(population))), "incomplete carrier population ordinals")
            model["populations"][family] = [population[i] for i in range(len(population))]
        imported = import_model(model)
        expected_nodes, expected_edges = _normalized_carrier(_expected_carrier(imported))
        require(nodes == expected_nodes and edges == expected_edges, "carrier differs from complete source encoding")
        return model
    except (KeyError, TypeError, RecursionError) as exc:
        raise Refusal(f"malformed carrier: {exc}") from exc


def load_checked(path: str | Path) -> dict:
    document = read_json(path)
    model = recover_carrier(document) if "nodes" in document else document
    import_model(model)
    return model


def _seed_indices(seeds, count):
    _array(seeds, "seeds")
    require(bool(seeds) and all(type(i) is int and 0 <= i < count for i in seeds), "nonempty local seed indices required")
    require(len(set(seeds)) == len(seeds), "duplicate seed")


def check_certificate(imported: dict, certificate: dict) -> bool:
    """Executable certificate check; Lean proves the corresponding core law."""
    check_imported(imported)
    try:
        count = len(imported["records"])
        seeds = certificate["seeds"]
        _seed_indices(seeds, count)
        for key in ("included", "excluded"):
            values = _array(certificate[key], key)
            require(all(type(i) is int and 0 <= i < count for i in values), "non-integer/out-of-domain membership")
        seen = set(seeds)
        edges = {tuple(pair) for pair in imported["edges"]}
        for value in _array(certificate["order"], "certificate order"):
            require(type(value) is int and 0 <= value < count and value not in seen, "duplicate/out-of-domain certificate step")
            require(any((prior, value) in edges for prior in seen), "unreachable certificate step")
            seen.add(value)
        require(certificate["included"] == sorted(seen), "certificate membership disagrees with reachability order")
        require(all(source not in seen or target in seen for source, target in edges), "certificate is not dependency-closed")
        require(certificate["excluded"] == sorted(set(range(count)) - seen), "incomplete exclusion boundary")
        budget = certificate.get("budget_records")
        require(budget is None or (type(budget) is int and budget >= 0 and len(seen) <= budget), "insufficient or invalid budget")
        core = {key: certificate[key] for key in ("seeds", "order", "included", "excluded", "budget_records")}
        if set(certificate) != set(core):
            expected = {**core, **_projection_fields(imported, seeds, sorted(seen), budget)}
            require(canonical(certificate) == canonical(expected), "projection changes parent, selection, retained data or boundaries")
        return True
    except (KeyError, TypeError, RecursionError) as exc:
        raise Refusal(f"malformed certificate: {exc}") from exc


def _projection_fields(imported: dict, seeds: list[int], included: list[int], budget: int | None) -> dict:
    records = imported["records"]
    seen = set(included)
    excluded = sorted(set(range(len(records))) - seen)
    refs = [r for r in imported["references"] if r["owner"] in seen]
    external_ids = {r["target"] for r in refs if type(r["target"]) is str}
    retained_residuals = [i for i in included if records[i]["family"] == "residuals"]
    excluded_residuals = [i for i in excluded if records[i]["family"] == "residuals"]
    identity = {record["record"]["id"]: record["index"] for record in records}
    crossing = [deepcopy(r) for r in records if r["family"] == "relations" and r["index"] not in seen
                and (identity.get(r["record"]["source"]) in seen or identity.get(r["record"]["target"]) in seen)]
    return {
        "required_count": len(included),
        "parent": {"id": imported["envelope"]["id"], "sha256": imported["model_sha256"]},
        "selection": {"seeds": list(seeds), "dependency_contract": deepcopy(imported["envelope"]["dependency_contract"]),
                      "budget_records": budget},
        "envelope": deepcopy(imported["envelope"]),
        "records": [deepcopy(records[i]) for i in included],
        "boundary": {
            "external": [deepcopy(r) for r in imported["envelope"]["external_resolutions"] if r["external_identity"] in external_ids],
            "non_governing_references": [deepcopy(r) for r in refs if type(r["target"]) is int and r["target"] not in seen],
            "retained_residuals": retained_residuals,
            "excluded_residuals": excluded_residuals,
            "unresolved_residual_records": [deepcopy(records[i]) for i in retained_residuals],
            "excluded_residual_records": [deepcopy(records[i]) for i in excluded_residuals],
            "crossing_relations": crossing,
            "invalidation": deepcopy(imported["envelope"]["interpretation"]["invalidation"]),
            "standing": "Retained and excluded residuals remain unresolved; exclusion is not disposition.",
        },
        "claim": "View of exact parent under declared dependencies; no source, interpretation or acceptance authority.",
    }


def closure_certificate(imported: dict, seeds: list[int], budget: int | None = None) -> dict:
    check_imported(imported)
    records = imported["records"]
    _seed_indices(seeds, len(records))
    require(budget is None or (type(budget) is int and budget >= 0), "budget must be a nonnegative record count")
    adjacency = {i: [] for i in range(len(records))}
    for source, target in imported["edges"]:
        adjacency[source].append(target)
    seen, pending, order = set(seeds), deque(seeds), []
    while pending:
        for target in adjacency[pending.popleft()]:
            if target not in seen:
                seen.add(target)
                order.append(target)
                pending.append(target)
    require(budget is None or len(seen) <= budget,
            f"required closure needs {len(seen)} records; budget {budget} refuses without truncation")
    included, excluded = sorted(seen), sorted(set(range(len(records))) - seen)
    result = {
        "seeds": list(seeds), "order": order, "included": included, "excluded": excluded,
        "budget_records": budget, **_projection_fields(imported, seeds, included, budget),
    }
    check_certificate(imported, result)
    return result


def verify_fixture(directory: str | Path = FIXTURE_DIR) -> dict:
    directory = Path(directory)
    for name, expected in RAW_SHA256.items():
        try:
            actual = hashlib.sha256((directory / name).read_bytes()).hexdigest()
        except OSError as exc:
            raise Refusal(f"missing fixture: {name}") from exc
        require(actual == expected, f"raw fixture digest mismatch: {name}")
    custody = read_json(directory / "CUSTODY.json")
    require(custody.get("raw_sha256") == RAW_SHA256 and custody.get("canonical_model_sha256") == MODEL_SHA256
            and custody.get("signature_sha256") == SIGNATURE_SHA256, "custody disagrees with pinned identities")
    model = load_checked(directory / "MODEL.json")
    imported = import_model(model)
    require(imported["model_sha256"] == MODEL_SHA256, "canonical fixture identity mismatch")
    require(reconstruct(imported) == model, "source-field reconstruction mismatch")
    for name in ("CARRIER.json", "GRAPHIFY_EXTRACTION.json"):
        require(load_checked(directory / name) == model, f"carrier does not recover exact model: {name}")
    histogram = {}
    for seed in range(len(imported["records"])):
        size = len(closure_certificate(imported, [seed])["included"])
        histogram[str(size)] = histogram.get(str(size), 0) + 1
    return {"raw_sha256": dict(RAW_SHA256), "model_sha256": imported["model_sha256"],
            "records": len(imported["records"]), "references": len(imported["references"]),
            "edges": len(imported["edges"]), "singleton_closure_histogram": dict(sorted(histogram.items())),
            "source_reconstruction": "exact", "carrier_recovery": "both exact",
            "proof_boundary": "Python import/custody/check results; generic Lean proofs are a separate check."}


def verify_toy_fixture(directory: str | Path = TOY_FIXTURE_DIR) -> dict:
    directory = Path(directory)
    try:
        raw = hashlib.sha256((directory / "MODEL.json").read_bytes()).hexdigest()
    except OSError as exc:
        raise Refusal("missing toy fixture") from exc
    require(raw == TOY_RAW_SHA256, "raw toy fixture digest mismatch")
    custody = read_json(directory / "CUSTODY.json")
    require(custody.get("raw_sha256") == {"MODEL.json": TOY_RAW_SHA256}
            and custody.get("canonical_model_sha256") == TOY_MODEL_SHA256
            and custody.get("signature_sha256") == TOY_SIGNATURE_SHA256, "toy custody disagrees with pinned identities")
    model = load_checked(directory / "MODEL.json")
    imported = import_model(model)
    require(imported["model_sha256"] == TOY_MODEL_SHA256 and reconstruct(imported) == model,
            "toy source identity/reconstruction mismatch")
    histogram = {}
    for seed in range(len(imported["records"])):
        size = len(closure_certificate(imported, [seed])["included"])
        histogram[str(size)] = histogram.get(str(size), 0) + 1
    return {"raw_sha256": {"MODEL.json": raw}, "model_sha256": imported["model_sha256"],
            "records": len(imported["records"]), "references": len(imported["references"]),
            "edges": len(imported["edges"]), "families": {f: len(model["populations"][f]) for f in FAMILIES},
            "singleton_closure_histogram": dict(sorted(histogram.items())), "source_reconstruction": "exact",
            "proof_boundary": "Synthetic all-family structural input; no transformation execution or semantic acceptance."}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    inputs = parser.add_mutually_exclusive_group()
    inputs.add_argument("--fixture", type=Path, default=FIXTURE_DIR)
    inputs.add_argument("--toy", action="store_true", help="use the pinned application-neutral all-family example")
    parser.add_argument("--seed", type=int, action="append", help="local record index; repeat for a seed set")
    parser.add_argument("--budget", type=int, help="complete required local-record budget")
    args = parser.parse_args(argv)
    try:
        directory = TOY_FIXTURE_DIR if args.toy else args.fixture
        custody = verify_toy_fixture(directory) if args.toy else verify_fixture(directory)
        if args.seed is None:
            result = custody
        else:
            imported = import_model(load_checked(directory / "MODEL.json"))
            result = closure_certificate(imported, args.seed, args.budget)
        print(json.dumps({"status": "checked", "result": result}, indent=2, ensure_ascii=False))
        return 0
    except Refusal as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}))
        return 2


if __name__ == "__main__":
    sys.exit(main())
