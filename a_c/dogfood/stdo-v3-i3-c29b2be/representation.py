#!/usr/bin/env python3
"""Transport the frozen Codex V3 I3 authored program through the a_c Graphify tenant."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import gzip
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import statistics
import sys
import tarfile
import time
from typing import Mapping, Sequence, cast

HERE = Path(__file__).resolve().parent
AC_ROOT = HERE.parents[1]
CODEC = AC_ROOT / "build_tenants/graphify/code/ac_graph.py"
sys.path.insert(0, str(CODEC.parent))
import ac_graph as ac  # noqa: E402
from ac_graph import JSON, Object  # noqa: E402
PREFIX = "urn:a-c:dogfood:stdo-v3-i3-c29b2be:"
SOURCE_PREFIX = "repo://codex-v3/successor/"
VOCABULARY = SOURCE_PREFIX + "interpretation/SIGNATURE.md#"
SOURCE_COMMIT = "c29b2be37f9a12e050478be97793927d99c01781"
PACKAGE_COMMIT = "ef5e514f5ffff4176b55ca687e56fe3c8b97efc1"
PACKAGE_TREE = "3648bfc1a664ec8e7f93a686d7818461f4034cac"
MANIFEST_SHA256 = "9f71927ee90ef25081658016a85d2cc8f1a7b551e5874b46ceaa150619140f2e"
ARCHIVE_SHA256 = "13aed5e6ba34955865c7de8099fce462bbb1affb790b6106376ab46a7da2be05"
PROGRAM_FILE = "interpretation/program.json"
ACCOUNT_FILE = "interpretation/source-account.json"
INVENTORY_FILE = "interpretation/SOURCE_INVENTORY.json"
MAPPING_FILE = "interpretation/MAPPING.json"
ENVELOPE_ID = PREFIX + "program-envelope"
CLAUSE_SORT = PREFIX + "sort:native-clause"
SELECTOR_SORT = PREFIX + "sort:native-selector"
ENVELOPE_SORT = PREFIX + "sort:program-envelope"
RESIDUAL_KIND = PREFIX + "residual-kind:transported-unresolved"
CLAIM = "proposed lossless transport of the authored interpretation; no independent v3 semantic acceptance, carrier admission or release"
MAPPING_CONTRACT: Object = {
    "id": PREFIX + "mapping-contract:1",
    "subject": "exact frozen native program, not a new interpretation of documentary STDO",
    "clause_mapping": "original URI and ordered exact native payload; typed adjacent location/ref pairs govern",
    "route_mapping": "ordered exact native route payload; typed target and target_index never govern automatically",
    "selector_mapping": "original URI, ordinal, payload and governing native roots",
    "residual_mapping": "only original residuals; exact native payload and authored subject",
    "empty_populations": ["relations", "constraints", "latitude", "traversals", "transformations", "judgments"],
    "conditional_rule": "establish applicability externally; select target index additionally only when applicable; unknown applicability withholds dependent action",
    "claim": CLAIM,
}
OWNER_INSTRUCTION = "v3 iteration 3 has completed, another session is reviewing it, can you use it to create a v3 representation"


def uid(suffix: str) -> str:
    return PREFIX + suffix


def jo(**values: object) -> Object:
    result = cast(Object, values)
    ac.grammar(result)
    return result


def sha_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _unique(pairs: list[tuple[str, JSON]]) -> Object:
    result: Object = {}
    for key, value in pairs:
        ac.require(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def parse(value: bytes | str, path: str, *, annotations: bool = False) -> Object:
    try:
        document = cast(JSON, json.loads(value, object_pairs_hook=_unique))
        ac.grammar(document, annotations=annotations)
        return ac.obj(document, path)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ac.Refusal(path + ": invalid JSON: " + str(exc)) from exc


def objects(value: JSON, path: str) -> list[Object]:
    return [ac.obj(item, path) for item in ac.seq(value, path)]


def text(value: JSON, path: str) -> str:
    return ac.string(value, path)


def integer(value: JSON, path: str) -> int:
    ac.require(type(value) is int and value >= 0, path + ": expected nonnegative integer")
    return cast(int, value)


def coordinate(identity: str, value: bytes) -> Object:
    return jo(id=identity, sha256=sha_bytes(value))


@dataclass(frozen=True)
class NativeSubject:
    members: Mapping[str, bytes]
    manifest: Object
    program: Object
    account: Object
    inventory: Object
    mapping: Object
    pin_counts: Object


def load_frozen(input_dir: Path = HERE / "input") -> NativeSubject:
    """Read and authenticate all frozen members without extracting archive paths."""
    manifest_raw = (input_dir / "manifest.json").read_bytes()
    ac.require(sha_bytes(manifest_raw) == MANIFEST_SHA256, "frozen manifest drift")
    manifest = parse(manifest_raw, "manifest")
    ac.require(manifest["source_commit"] == SOURCE_COMMIT, "wrong source checkpoint")
    ac.require(manifest["package_commit"] == PACKAGE_COMMIT and manifest["package_tree"] == PACKAGE_TREE, "wrong package identity")
    archive_pin = ac.obj(manifest["archive"], "manifest/archive")
    ac.require(archive_pin["path"] == "candidate.tar.gz", "unexpected archive path")
    archive = (input_dir / "candidate.tar.gz").read_bytes()
    ac.require(sha_bytes(archive) == ARCHIVE_SHA256 == archive_pin["sha256"], "frozen archive drift")
    ac.require(len(archive) == archive_pin["bytes"], "frozen archive size drift")
    expected: dict[str, Object] = {}
    for row in objects(manifest["members"], "manifest/members"):
        name = text(row["path"], "member/path")
        ac.require(name not in expected, "duplicate manifest member")
        expected[name] = row
    ac.require(len(expected) == 89, "wrong frozen member count")
    members: dict[str, bytes] = {}
    seen_archive_names: set[str] = set()
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as stream:
        for member in stream:
            name = member.name
            path = PurePosixPath(name)
            ac.require(not path.is_absolute() and ".." not in path.parts and name not in seen_archive_names, "unsafe/duplicate archive coordinate")
            seen_archive_names.add(name)
            if member.isdir():
                ac.require(any(candidate.startswith(name.rstrip("/") + "/") for candidate in expected), "unknown archive directory")
                continue
            ac.require(member.isfile(), "nonregular archive member")
            ac.require(name in expected and name not in members, "unknown/duplicate archive member")
            handle = stream.extractfile(member)
            ac.require(handle is not None, "unreadable archive member")
            assert handle is not None
            payload = handle.read()
            pin = expected[name]
            ac.require(len(payload) == pin["bytes"] and sha_bytes(payload) == pin["sha256"], "frozen member drift: " + name)
            members[name] = payload
    ac.require(set(members) == set(expected), "incomplete frozen archive")
    return verify_native(members, manifest)


def verify_owner_pins(members: Mapping[str, bytes], account: Object) -> Object:
    """Verify the authored line/body and byte/block pins, without semantic inference."""
    owner_count = block_count = 0
    seen: set[str] = set()
    for row in objects(account["determinations"], "determinations"):
        row_id = text(row["id"], "determination/id")
        ac.require(row_id not in seen, "duplicate determination identity")
        seen.add(row_id)
        owner = ac.obj(row["owner"], row_id + "/owner")
        path = text(owner["path"], "owner/path")
        ac.require(path in members, "source owner not in frozen custody")
        source = members[path]
        if owner.get("unit_scope") == "whole_member":
            body = source
        else:
            lines = source.decode("utf-8").splitlines(keepends=True)
            start = integer(owner["start_line"], "owner/start_line")
            end = integer(owner["end_line"], "owner/end_line")
            ac.require(1 <= start <= end <= len(lines), "source owner line range")
            body = "".join(lines[start - 1:end]).encode("utf-8")
        ac.require(sha_bytes(body) == owner["body_sha256"], "source owner body pin drift: " + row_id)
        owner_count += 1
        for block in objects(row["source_clauses"], "source_clauses"):
            begin = integer(block["byte_start"], "block/byte_start")
            finish = integer(block["byte_end"], "block/byte_end")
            ac.require(0 <= begin < finish <= len(source), "source block byte range")
            ac.require(sha_bytes(source[begin:finish]) == block["sha256"], "source block pin drift: " + row_id)
            block_count += 1
    ac.require(owner_count == 701, "wrong source owner population")
    return jo(owner_body_pins=owner_count, source_block_pins=block_count)


def required_pairs(clause: Object) -> list[Object]:
    """Preserve native occurrence coordinates; never resolve them against one guessed object."""
    arguments = objects(clause["arguments"], "clause/arguments")
    result: list[Object] = []
    for ordinal, argument in enumerate(arguments):
        role = text(argument["role"], "argument/role")
        ac.require(set(argument) in ({"role", "literal"}, {"role", "ref"}), "unsupported native argument fields")
        if "ref" in argument:
            ac.require(ordinal > 0, "native reference lacks location argument")
            previous = arguments[ordinal - 1]
            ac.require(previous["role"] == VOCABULARY + "reference-location" and "literal" in previous, "native reference lacks adjacent location")
            result.append(jo(ordinal=ordinal, pointer=previous["literal"], role=role, target=argument["ref"]))
        elif role == VOCABULARY + "reference-location":
            ac.require(ordinal + 1 < len(arguments) and "ref" in arguments[ordinal + 1], "orphan native reference location")
    return result


def route_occurrences(clause: Object) -> list[Object]:
    result: list[Object] = []
    for ordinal, argument in enumerate(objects(clause["arguments"], "arguments")):
        if argument["role"] == VOCABULARY + "acquisition-route":
            literal = text(argument["literal"], "acquisition-route/literal")
            payload = parse(literal, "acquisition-route")
            result.append(jo(ordinal=ordinal, payload=literal, target=payload["target"], target_index=payload["target_index"]))
    return result


def authored_display(clause: Object) -> str:
    """A source-authored excerpt for native discovery, not an authored new summary."""
    for argument in objects(clause["arguments"], "arguments"):
        if argument["role"] == VOCABULARY + "semantic-record":
            native = parse(text(argument["literal"], "semantic-record literal"), "semantic-record")
            for field in ("predicate", "definition", "binding"):
                candidate = native.get(field)
                if isinstance(candidate, str) and candidate:
                    return candidate
    return text(clause["statement"], "clause/statement")


def verify_native(members: Mapping[str, bytes], manifest: Object) -> NativeSubject:
    program = parse(members[PROGRAM_FILE], PROGRAM_FILE)
    account = parse(members[ACCOUNT_FILE], ACCOUNT_FILE)
    inventory = parse(members[INVENTORY_FILE], INVENTORY_FILE)
    mapping = parse(members[MAPPING_FILE], MAPPING_FILE)
    ac.require(program["kind"] == "axiom-indexer.axiomatic-program" and program["schema_version"] == 1, "unsupported native program")
    ac.require(program["calculus_ref"] == ac.CALCULUS_URI and program["source_basis"] == SOURCE_PREFIX, "native program basis drift")
    theory = ac.obj(inventory["encoding_theory"], "encoding_theory")
    ac.require(theory["member_sha256"] == ac.CALCULUS_SHA256 and text(theory["release_uri"], "theory/release_uri") + "standards/AXIOMATIC_CALCULUS.md" == ac.CALCULUS_URI, "encoding theory pin mismatch")
    document_members: set[str] = set()
    for row in objects(inventory["document_members"], "document_members"):
        name = text(row["path"], "document/path")
        ac.require(name not in document_members and name in members, "unknown/duplicate documentary member")
        document_members.add(name)
        ac.require(len(members[name]) == row["bytes"] and sha_bytes(members[name]) == row["sha256"], "documentary pin drift: " + name)
    ac.require(len(document_members) == 80 and document_members == {name for name in members if not name.startswith("interpretation/")}, "documentary inventory mismatch")
    interpretation = ac.obj(inventory["interpretation"], "interpretation pins")
    for path, key in (
        (PROGRAM_FILE, "program_file_sha256"), (ACCOUNT_FILE, "semantic_account_sha256"),
        ("interpretation/SIGNATURE.md", "vocabulary_sha256"), ("interpretation/FRAMES.md", "frames_sha256"), (MAPPING_FILE, "mapping_sha256"),
    ):
        ac.require(sha_bytes(members[path]) == interpretation[key], "interpretation pin drift: " + path)
    ac.require(program["uri"] == interpretation["program_uri"], "native program identity drift")
    pin_counts = verify_owner_pins(members, account)
    contracts = ac.obj(account["semantic_contracts"], "semantic_contracts")
    ac.require(len(contracts) == 37, "wrong semantic contract population")
    clauses = objects(program["clauses"], "clauses")
    selectors = objects(program["frame_indexes"], "frame_indexes")
    residuals = objects(program["residuals"], "residuals")
    clause_ids = [text(c["uri"], "clause/uri") for c in clauses]
    selector_ids = [text(s["uri"], "selector/uri") for s in selectors]
    residual_ids = [text(r["uri"], "residual/uri") for r in residuals]
    ac.require(len(clauses) == len(set(clause_ids)) == 705, "wrong clause population")
    ac.require(len(selectors) == len(set(selector_ids)) == 725, "wrong selector population")
    ac.require(len(residuals) == len(set(residual_ids)) == 2, "wrong residual population")
    row_by_clause: dict[str, Object] = {}
    mapping_rows = objects(mapping["rows"], "mapping/rows")
    ac.require(len(mapping_rows) == 701, "wrong mapping row population")
    for row in mapping_rows:
        clause_id = text(row["clause"], "mapping/clause")
        ac.require(clause_id in clause_ids and row["index"] in selector_ids and clause_id not in row_by_clause, "invalid source mapping binding")
        row_by_clause[clause_id] = row
    pair_count = provenance = conditional = inline_count = 0
    for clause in clauses:
        pair_count += len(required_pairs(clause))
        for pair in required_pairs(clause):
            ac.require(pair["target"] in clause_ids, "native required target is not a clause")
        for argument in objects(clause["arguments"], "arguments"):
            if argument["role"] == VOCABULARY + "inlined-contract":
                contract = parse(text(argument["literal"], "inlined-contract"), "inlined-contract")
                pointer = text(contract["definition_pointer"], "definition_pointer")
                ac.require(pointer.startswith("/semantic_contracts/"), "inline contract pointer outside source account")
                name = pointer[len("/semantic_contracts/"):].replace("~1", "/").replace("~0", "~")
                ac.require(name in contracts and contract["definition"] == contracts[name], "inlined contract definition drift")
                ac.require(contract["identity"] == "urn:codex-stdo3:iteration-3-r2:contract:" + name, "inlined contract identity drift")
                inline_count += 1
        for occurrence in route_occurrences(clause):
            route = parse(text(occurrence["payload"], "route/payload"), "route")
            target = text(route["target"], "route/target")
            ac.require(target in clause_ids and route["target_index"] in selector_ids, "dangling native route")
            ac.require(target in row_by_clause, "route target has no documentary owner")
            row = row_by_clause[target]
            owner = ac.obj(row["owner"], "route owner")
            ac.require(route["source"] == row["source"] and route["native_source"] == row["native_source"], "route source coordinate drift")
            ac.require(route["source_body_sha256"] == owner["body_sha256"], "route body pin drift")
            ac.require(route["source_member_sha256"] == sha_bytes(members[text(owner["path"], "owner/path")]), "route member pin drift")
            if route["acquisition"] == "provenance":
                provenance += 1
            else:
                ac.require(route["acquisition"] == "conditional", "unknown acquisition role")
                qualification = ac.obj(route["qualification"], "conditional qualification")
                text(qualification["required_when"], "conditional required_when")
                text(route["unknown_applicability"], "conditional unknown applicability")
                conditional += 1
    for selector in selectors:
        ac.require(set(ac.strings(selector["clause_refs"], "selector/clause_refs")) <= set(clause_ids), "dangling selector clause root")
        ac.require(set(ac.strings(selector["residual_refs"], "selector/residual_refs")) <= set(residual_ids), "dangling selector residual root")
    for residual in residuals:
        subjects = ac.strings(residual["subject_refs"], "residual/subject_refs")
        ac.require(len(subjects) == 1 and subjects[0] in clause_ids, "unsupported residual subject binding")
    ac.require((pair_count, provenance, conditional, inline_count) == (7741, 2046, 30, 410), "native occurrence counts drift")
    return NativeSubject(members, manifest, program, account, inventory, mapping, pin_counts)


def schema(kind: str, **values: object) -> Object:
    return jo(type=kind, **values)


def ref(local: Sequence[str] = (), remote: Sequence[str] = (), *, governing: bool = False, sorts: Sequence[str] = ()) -> Object:
    return jo(type="ref", domain=uid("reference-domain:transport"), local_families=list(local), local_sorts=list(sorts), external_kinds=[uid("external-kind:" + kind) for kind in remote], basis_relation=uid("basis-relation:frozen-input"), governing=governing)


def array(items: Object, minimum: int = 0) -> Object:
    return jo(type="array", items=items, min_items=minimum)


def closed(**fields: Object) -> Object:
    return jo(type="object", fields=fields)


def signature_definition() -> Object:
    """Declare a transport signature, including lawful empty core families."""
    string_schema = schema("string")
    nonempty = schema("string", min_length=1)
    int_schema = schema("integer")
    local_ref = ref(("objects",), governing=True, sorts=(CLAUSE_SORT,))
    clause_value = closed(
        a_summary=nonempty, native_json=nonempty, ordinal=int_schema,
        required_refs=array(closed(ordinal=int_schema, pointer=nonempty, role=nonempty, target=local_ref)),
        routes=array(closed(ordinal=int_schema, payload=nonempty, target=ref(("objects",), sorts=(CLAUSE_SORT,)), target_index=ref(("objects",), sorts=(SELECTOR_SORT,)))),
    )
    selector_value = closed(a_scope=nonempty, native_json=nonempty, ordinal=int_schema, roots=array(local_ref), residual_roots=array(ref(("residuals",), governing=True)))
    envelope_value = closed(a_kind=nonempty, native_json=nonempty, raw_program_sha256=nonempty)
    object_refs = array(local_ref)
    common = jo(id=schema("identity"), context=ref(remote=("context",)), owner=ref(remote=("transport-owner",)), scope=array(ref(remote=("scope",)), 1), basis=ref(remote=("basis",)))
    fields: Object = {}

    def family(name: str, **specific: Object) -> None:
        fields[name] = dict(common, **specific)

    family("objects", sort=ref(remote=("sort",)), value=clause_value)
    family("relations", kind=ref(remote=("relation-kind",)), source=local_ref, target=local_ref, qualifiers=closed())
    family("constraints", kind=ref(remote=("constraint-kind",)), applies_to=object_refs, predicate=string_schema, judgment_kind=ref(remote=("judgment-kind",)), latitude_ref=array(ref(("latitude",), governing=True)), refusal=ref(remote=("stop",)))
    family("latitude", applies_to=object_refs, allowed_variation=array(string_schema), forbidden_variation=array(string_schema), invalidation=ref(remote=("invalidation",)))
    residual_subject = ref(("objects",), governing=True, sorts=(CLAUSE_SORT,))
    residual_uncertainty = closed(a_detail=nonempty, native_json=nonempty, ordinal=int_schema)
    reentry = array(ref(remote=("source-route",)))
    invalidation = ref(remote=("invalidation",))
    family("residuals", subject=residual_subject, kind=ref(remote=("residual-kind",)), uncertainty=residual_uncertainty, consequence=nonempty, re_entry=reentry, invalidation=invalidation)
    constraint_refs = array(ref(("constraints",), governing=True))
    evidence = array(ref(remote=("evidence",)))
    stops = array(ref(remote=("stop",)))
    family("traversals", domain=ref(remote=("domain",)), codomain=ref(remote=("domain",)), preconditions=constraint_refs, postconditions=constraint_refs, authority=ref(remote=("authority",)), evidence=evidence, provenance=evidence, stop_states=stops)
    family("transformations", traversal=ref(("traversals",), governing=True), domain_model=ref(remote=("model",)), codomain_model=ref(remote=("model",)), operation_authority=ref(remote=("authority",)), preconditions=constraint_refs, preservation_relation=ref(remote=("preservation-law",)), preserved=object_refs, introduced=object_refs, removed=object_refs, external_preserved=array(ref(remote=("external-resolution",))), external_introduced=array(ref(remote=("external-resolution",))), external_removed=array(ref(remote=("external-resolution",))), external_resolution_witnesses=array(ref(remote=("witness",))), residuals=array(ref(("residuals",), governing=True)), evidence=evidence, provenance=evidence, stop_states=stops, invalidation=invalidation, re_entry=reentry)
    family("judgments", kind=ref(remote=("judgment-kind",)), subject=local_ref, subject_digest=nonempty, evaluator=ref(remote=("actor",)), authority=ref(remote=("authority",)), decision=nonempty, evidence=evidence, provenance=evidence, decided_at=nonempty)
    return jo(fields=fields, sorts={CLAUSE_SORT: jo(value=clause_value), SELECTOR_SORT: jo(value=selector_value), ENVELOPE_SORT: jo(value=envelope_value)}, relation_kinds={}, constraint_kinds={}, residual_kinds={RESIDUAL_KIND: jo(subject=residual_subject, uncertainty=residual_uncertainty, consequence=nonempty, re_entry=reentry, invalidation=invalidation)}, judgment_kinds={}, functor_kinds=[], stop_kinds=[], required_families=["objects", "residuals"])


def build_model(subject: NativeSubject) -> ac.Model:
    program = subject.program
    basis_id = uid("basis")
    common = jo(context=uid("context:program-transport"), owner=uid("transport-owner"), scope=[uid("scope:frozen-authored-program")], basis=basis_id)

    def record(identity: str, **specific: object) -> Object:
        return dict(common, **jo(id=identity, **specific))

    records: list[JSON] = []
    for ordinal, clause in enumerate(objects(program["clauses"], "clauses")):
        records.append(record(text(clause["uri"], "clause/uri"), sort=CLAUSE_SORT, value=jo(a_summary=authored_display(clause), native_json=ac.canonical(clause).decode("utf-8"), ordinal=ordinal, required_refs=required_pairs(clause), routes=route_occurrences(clause))))
    for ordinal, selector in enumerate(objects(program["frame_indexes"], "frame_indexes")):
        records.append(record(text(selector["uri"], "selector/uri"), sort=SELECTOR_SORT, value=jo(a_scope=selector["scope"], native_json=ac.canonical(selector).decode("utf-8"), ordinal=ordinal, roots=selector["clause_refs"], residual_roots=selector["residual_refs"])))
    envelope = {key: value for key, value in program.items() if key not in ("clauses", "frame_indexes", "residuals")}
    records.append(record(ENVELOPE_ID, sort=ENVELOPE_SORT, value=jo(a_kind=program["kind"], native_json=ac.canonical(envelope).decode("utf-8"), raw_program_sha256=sha_bytes(subject.members[PROGRAM_FILE]))))
    residuals: list[JSON] = []
    source_routes: set[str] = set()
    for ordinal, native in enumerate(objects(program["residuals"], "residuals")):
        routes = ac.strings(native["re_entry_refs"], "re_entry_refs")
        source_routes.update(routes)
        residuals.append(record(text(native["uri"], "residual/uri"), subject=ac.seq(native["subject_refs"], "subject_refs")[0], kind=RESIDUAL_KIND, uncertainty=jo(a_detail=native["detail"], native_json=ac.canonical(native).decode("utf-8"), ordinal=ordinal), consequence=native["detail"], re_entry=routes, invalidation=uid("invalidation:frozen-input-drift")))
    populations = jo(**{family: [] for family in ac.CORE_FIELDS})
    populations["objects"] = records
    populations["residuals"] = residuals
    external_kinds = {
        uid("context:program-transport"): "context", uid("transport-owner"): "transport-owner",
        uid("scope:frozen-authored-program"): "scope", basis_id: "basis",
        CLAUSE_SORT: "sort", SELECTOR_SORT: "sort", ENVELOPE_SORT: "sort",
        RESIDUAL_KIND: "residual-kind", uid("invalidation:frozen-input-drift"): "invalidation",
    }
    external_kinds.update({route: "source-route" for route in source_routes})
    resolutions: list[JSON] = [jo(external_identity=identity, reference_domain=uid("reference-domain:transport"), external_target_kind=uid("external-kind:" + kind), resolved_target_identity=identity, basis_relation=uid("basis-relation:frozen-input"), resolution_basis=basis_id, evidence_identity="urn:sha256:" + ARCHIVE_SHA256) for identity, kind in sorted(external_kinds.items())]
    local_ids = [text(ac.obj(row, "record")["id"], "record/id") for values in populations.values() for row in ac.seq(values, "population")]
    source_id = SOURCE_PREFIX + PROGRAM_FILE
    authority = coordinate(uid("authority:owner-instruction:T-002"), OWNER_INSTRUCTION.encode("utf-8"))
    dispositions: list[JSON] = [jo(source=source_id, decision="retained", records=local_ids, authority=authority["id"], basis=basis_id, reason="Complete deterministic transport of the exact authored program; no new interpretation, semantic authority or acceptance. Documentary corpus and source account remain in frozen input custody.")]
    definition = signature_definition()
    signature_id = uid("signature:transport:1")
    interpretation = jo(
        contract=coordinate(text(MAPPING_CONTRACT["id"], "contract/id"), ac.canonical(MAPPING_CONTRACT)),
        selection_ledger=coordinate(uid("selection-ledger"), ac.canonical(dispositions)),
        interpreter=coordinate(uid("interpreter:deterministic-transport"), Path(__file__).read_bytes()),
        authority=authority,
        source_reentry=coordinate(SOURCE_PREFIX + INVENTORY_FILE, subject.members[INVENTORY_FILE]),
        invalidation=coordinate(uid("invalidation:frozen-input-drift"), b"Any change in exact input, mapping contract, builder, signature or carrier invalidates evidence for the previous representation."),
        provenance=[coordinate(uid("input:manifest"), ac.canonical(subject.manifest)), coordinate(SOURCE_PREFIX + ACCOUNT_FILE, subject.members[ACCOUNT_FILE]), coordinate(SOURCE_PREFIX + "interpretation/SIGNATURE.md", subject.members["interpretation/SIGNATURE.md"])],
        dispositions=dispositions,
    )
    document = jo(
        profile=ac.MODEL_PROFILE, id=uid("model:proposal:1"),
        basis=jo(id=basis_id, calculus=jo(uri=ac.CALCULUS_URI, sha256=ac.CALCULUS_SHA256), subject=jo(id=program["uri"], sha256=sha_bytes(subject.members[PROGRAM_FILE]), inventory=[coordinate(source_id, subject.members[PROGRAM_FILE])])),
        coordinates={key: value for key, value in common.items() if key != "basis"},
        signature=jo(id=signature_id, definition=definition, sha256=ac.digest(jo(id=signature_id, definition=definition))),
        interpretation=interpretation, identity_universe=sorted(local_ids + list(external_kinds)), external_resolutions=resolutions, populations=populations,
        dependency_contract=jo(id=uid("dependency-contract:native-required-references:1"), required_relation_kinds=[], attachment_families=["constraints", "latitude", "residuals"]), functor_bindings={},
    )
    return ac.validate(document)


def recover_program(model: ac.Model) -> Object:
    """Recover only the original native program, independently of transport-derived fields."""
    envelope_record = model.records.get(ENVELOPE_ID)
    ac.require(envelope_record is not None, "missing native program envelope")
    assert envelope_record is not None
    value = ac.obj(envelope_record.fields["value"], "envelope/value")
    recovered = parse(text(value["native_json"], "envelope/native_json"), "program envelope")
    for sort, family, destination, field in (
        (CLAUSE_SORT, "objects", "clauses", "value"),
        (SELECTOR_SORT, "objects", "frame_indexes", "value"),
        (RESIDUAL_KIND, "residuals", "residuals", "uncertainty"),
    ):
        ordered: dict[int, Object] = {}
        for record in model.records.values():
            if record.family == family and record.fields["sort" if family == "objects" else "kind"] == sort:
                content = ac.obj(record.fields[field], "native content")
                ordinal = integer(content["ordinal"], "native ordinal")
                ac.require(ordinal not in ordered, "duplicate native ordinal")
                ordered[ordinal] = parse(text(content["native_json"], "native_json"), "native payload")
        ac.require(set(ordered) == set(range(len(ordered))), "incomplete native ordinal population")
        recovered[destination] = [ordered[i] for i in range(len(ordered))]
    return recovered


def native_closure(program: Object, selector: Object) -> tuple[set[str], set[str]]:
    """Independent oracle: raw native ref arguments, with no mapped fields or codec indexes."""
    dependencies = {text(c["uri"], "clause/uri"): {text(argument["ref"], "argument/ref") for argument in objects(c["arguments"], "arguments") if "ref" in argument} for c in objects(program["clauses"], "clauses")}
    included = set(ac.strings(selector["clause_refs"], "selector roots"))
    pending = list(included)
    while pending:
        for target in dependencies[pending.pop()]:
            if target not in included:
                included.add(target)
                pending.append(target)
    residuals = set(ac.strings(selector["residual_refs"], "residual roots"))
    for native in objects(program["residuals"], "residuals"):
        if included.intersection(ac.strings(native["subject_refs"], "residual subjects")):
            residuals.add(text(native["uri"], "residual/uri"))
    return included, residuals


def compare_selectors(subject: NativeSubject, model: ac.Model) -> Object:
    selectors = objects(subject.program["frame_indexes"], "selectors")
    selections: list[tuple[Sequence[str], int | None]] = [([text(selector["uri"], "selector/uri")], None) for selector in selectors]
    views = ac.project_many(model, selections)
    closure_sizes: list[int] = []
    for selector, view in zip(selectors, views):
        expected_clauses, expected_residuals = native_closure(subject.program, selector)
        populations = ac.obj(view["populations"], "projection/populations")
        actual_clauses = {text(row["id"], "clause/id") for row in objects(populations["objects"], "objects") if row["sort"] == CLAUSE_SORT}
        actual_residuals = {text(row["id"], "residual/id") for row in objects(populations["residuals"], "residuals")}
        ac.require(actual_clauses == expected_clauses, "selector clause closure mismatch: " + text(selector["uri"], "selector"))
        ac.require(actual_residuals == expected_residuals, "selector residual closure mismatch: " + text(selector["uri"], "selector"))
        ac.require(set(ac.strings(view["included"], "included")) == expected_clauses | expected_residuals | {text(selector["uri"], "selector")}, "unexpected selector expansion")
        closure_sizes.append(len(expected_clauses))
    return jo(selectors_compared=len(selectors), required_clause_closure=jo(min=min(closure_sizes), median=int(statistics.median(closure_sizes)), max=max(closure_sizes)), claim="exact equality with original native direct-reference closure for every selector; no interpretation-fidelity judgment")


def verify_transport(subject: NativeSubject, model: ac.Model) -> None:
    ac.require(recover_program(model) == subject.program, "source program JSON recovery mismatch")
    expected = build_model(subject)
    ac.require(model.document == expected.document, "representation differs from deterministic native transport")


def gzip_bytes(document: Object) -> bytes:
    target = io.BytesIO()
    with gzip.GzipFile(filename="", fileobj=target, mode="wb", compresslevel=6, mtime=0) as stream:
        stream.write(ac.canonical(document) + b"\n")
    return target.getvalue()


def emit(path: Path, payload: bytes, *, protected: Sequence[Path] = ()) -> None:
    target = path.resolve()
    protected_input = (HERE / "input").resolve()
    ac.require(not target.is_relative_to(protected_input), "output aliases frozen input custody")
    ac.require(not any(target == item.resolve() or (path.exists() and item.exists() and path.samefile(item)) for item in protected), "output aliases an input")
    if path.exists():
        ac.require(path.is_file() and not path.is_symlink() and path.read_bytes() == payload, "output already exists with different bytes; choose a fresh path: " + str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)


def load_document(path: Path, *, annotations: bool = False) -> Object:
    raw = path.read_bytes()
    return parse(gzip.decompress(raw) if path.suffix == ".gz" else raw, str(path), annotations=annotations)


def artifact_bundle(subject: NativeSubject, model: ac.Model, carrier: ac.GraphCarrier, *, stored_gzip: Mapping[str, bytes] | None = None) -> tuple[dict[str, bytes], Object]:
    """Recompute all catalogue/manifest statements from checked source and model."""
    catalog_rows: list[JSON] = []
    closure_sizes: list[int] = []
    for selector in objects(subject.program["frame_indexes"], "selectors"):
        clauses, residuals = native_closure(subject.program, selector)
        closure_sizes.append(len(clauses))
        catalog_rows.append(jo(uri=selector["uri"], frame_ref=selector["frame_ref"], scope=selector["scope"], required_clauses=len(clauses), retained_residuals=len(residuals)))
    selector_check = jo(selectors_compared=len(catalog_rows), required_clause_closure=jo(min=min(closure_sizes), median=int(statistics.median(closure_sizes)), max=max(closure_sizes)), claim="exact equality with original native direct-reference closure for every selector; no interpretation-fidelity judgment")
    model_bytes = ac.canonical(model.document) + b"\n"
    graph_bytes = ac.canonical(carrier.document) + b"\n"
    if stored_gzip is None:
        compressed_model = gzip_bytes(model.document)
        compressed_graph = gzip_bytes(carrier.document)
    else:
        compressed_model = stored_gzip["model.json.gz"]
        compressed_graph = stored_gzip["graph.json.gz"]
        ac.require(gzip.decompress(compressed_model) == model_bytes, "stored model does not contain the exact canonical model bytes")
        ac.require(gzip.decompress(compressed_graph) == graph_bytes, "stored graph does not contain the exact canonical graph bytes")
    files = {"model.json.gz": compressed_model, "graph.json.gz": compressed_graph, "selectors.json": json.dumps(jo(kind="a_c.v3-i3.selector-catalog", parent=ac.model_identity(model), selectors=catalog_rows), ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8") + b"\n"}
    counts = jo(clauses=705, selectors=725, residuals=2, required_reference_occurrences=7741, provenance_routes=2046, conditional_routes=30, inline_contract_arguments=410, semantic_contracts_in_frozen_account=37, records=len(model.records), typed_references=len(model.references), graph_nodes=len(ac.seq(carrier.document["nodes"], "nodes")), graph_links=len(ac.seq(carrier.document["links"], "links")))
    manifest = jo(
        kind="a_c.v3-i3.graphify-representation", schema_version=1, claim=CLAIM,
        input=jo(source_commit=SOURCE_COMMIT, package_commit=PACKAGE_COMMIT, package_tree=PACKAGE_TREE, frozen_manifest_sha256=MANIFEST_SHA256, archive_sha256=ARCHIVE_SHA256, raw_program_sha256=sha_bytes(subject.members[PROGRAM_FILE]), canonical_program_sha256=ac.digest(subject.program)),
        mapping_contract=MAPPING_CONTRACT, builder=jo(path="representation.py", sha256=sha_bytes(Path(__file__).read_bytes())), codec=jo(path="build_tenants/graphify/code/ac_graph.py", sha256=sha_bytes(CODEC.read_bytes())),
        model=ac.model_identity(model), semantic_graph_sha256=ac.digest(carrier.document), counts=counts, pin_checks=subject.pin_counts, selector_check=selector_check,
        sizes=jo(raw_program_bytes=len(subject.members[PROGRAM_FILE]), canonical_program_bytes=len(ac.canonical(subject.program)), model_json_bytes=len(model_bytes), graph_json_bytes=len(graph_bytes)),
        artifacts={name: jo(bytes=len(payload), sha256=sha_bytes(payload)) for name, payload in sorted(files.items())},
    )
    files["manifest.json"] = json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8") + b"\n"
    return files, manifest


def build(out_dir: Path, plain_graph: Path | None = None) -> Object:
    started = time.perf_counter()
    subject = load_frozen()
    model = build_model(subject)
    carrier = ac.materialize(model)
    recovered = ac.decode(carrier)
    ac.require(recovered.document == model.document, "generic carrier round trip mismatch")
    verify_transport(subject, recovered)
    selector_check = compare_selectors(subject, recovered)
    files, manifest = artifact_bundle(subject, model, carrier)
    ac.require(selector_check == manifest["selector_check"], "selector oracle statistics disagree")
    for name, payload in files.items():
        emit(out_dir / name, payload)
    if plain_graph is not None:
        emit(plain_graph, ac.canonical(carrier.document) + b"\n")
    return jo(status="built-proposal-representation", output=str(out_dir), model=ac.model_identity(model), counts=manifest["counts"], selector_check=selector_check, elapsed_seconds=str(round(time.perf_counter() - started, 3)), claim=CLAIM)


def load_representation(out_dir: Path, graph_path: Path | None = None) -> tuple[NativeSubject, ac.Model, Object]:
    subject = load_frozen()
    manifest = load_document(out_dir / "manifest.json")
    ac.require(manifest["kind"] == "a_c.v3-i3.graphify-representation" and manifest["schema_version"] == 1, "unsupported representation manifest")
    ac.require(ac.obj(manifest["builder"], "builder")["sha256"] == sha_bytes(Path(__file__).read_bytes()), "builder changed since representation construction")
    ac.require(ac.obj(manifest["codec"], "codec")["sha256"] == sha_bytes(CODEC.read_bytes()), "codec changed since representation construction")
    for name, pin_value in ac.obj(manifest["artifacts"], "artifacts").items():
        ac.require(name in ("model.json.gz", "graph.json.gz", "selectors.json"), "unexpected artifact name")
        pin = ac.obj(pin_value, "artifact pin")
        payload = (out_dir / name).read_bytes()
        ac.require(len(payload) == pin["bytes"] and sha_bytes(payload) == pin["sha256"], "artifact pin drift: " + name)
    ac.require(set(ac.obj(manifest["artifacts"], "artifacts")) == {"model.json.gz", "graph.json.gz", "selectors.json"}, "incomplete representation artifacts")
    model = ac.decode(ac.GraphCarrier(load_document(graph_path or out_dir / "graph.json.gz", annotations=True)))
    ac.require(ac.model_identity(model) == manifest["model"], "artifact model identity drift")
    ac.require(load_document(out_dir / "model.json.gz") == model.document, "model/carrier disagreement")
    verify_transport(subject, model)
    stored_gzip = {name: (out_dir / name).read_bytes() for name in ("model.json.gz", "graph.json.gz")}
    expected_files, expected_manifest = artifact_bundle(subject, model, ac.materialize(model), stored_gzip=stored_gzip)
    ac.require(manifest == expected_manifest, "representation manifest metadata differs from deterministic source-derived expectations")
    for name, expected_bytes in expected_files.items():
        ac.require((out_dir / name).read_bytes() == expected_bytes, "representation artifact differs from deterministic source-derived expectation: " + name)
    return subject, model, manifest


def select(subject: NativeSubject, model: ac.Model, selector_name: str, budget: int | None = None) -> Object:
    selectors = objects(subject.program["frame_indexes"], "selectors")
    exact = [s for s in selectors if s["uri"] == selector_name]
    candidates = exact or [s for s in selectors if text(s["uri"], "selector/uri").endswith(":index:" + selector_name)]
    ac.require(len(candidates) == 1, "selector must name one exact URI or exact index suffix")
    native = candidates[0]
    view = ac.project(model, [text(native["uri"], "selector/uri")], budget)
    expected_clauses, expected_residuals = native_closure(subject.program, native)
    included = set(ac.strings(view["included"], "included"))
    ac.require(expected_clauses | expected_residuals | {text(native["uri"], "selector")} == included, "selected closure differs from original native program")
    conditional: list[JSON] = []
    provenance: list[JSON] = []
    for clause in objects(subject.program["clauses"], "clauses"):
        if clause["uri"] in included:
            for occurrence in route_occurrences(clause):
                route = parse(text(occurrence["payload"], "route/payload"), "route")
                entry = jo(owner=clause["uri"], ordinal=occurrence["ordinal"], route=route, target_already_required=route["target"] in included, target_index_selected=route["target_index"] in included)
                (conditional if route["acquisition"] == "conditional" else provenance).append(entry)
    return jo(kind="a_c.v3-i3.selection", native_selector=native, projection=view, acquisition_routes=jo(conditional=conditional, provenance=provenance), conditional_rule=MAPPING_CONTRACT["conditional_rule"], claim=CLAIM)


def selection_summary(selection: Object) -> Object:
    view = ac.obj(selection["projection"], "projection")
    populations = ac.obj(view["populations"], "populations")
    routes = ac.obj(selection["acquisition_routes"], "routes")
    native = ac.obj(selection["native_selector"], "native selector")
    return jo(status="selected-complete-required-view", selector=native["uri"], scope=native["scope"], parent=view["parent"], records=len(ac.seq(view["included"], "included")), clauses=sum(row["sort"] == CLAUSE_SORT for row in objects(populations["objects"], "objects")), residuals=len(ac.seq(populations["residuals"], "residuals")), conditional_routes=len(ac.seq(routes["conditional"], "conditional")), provenance_routes=len(ac.seq(routes["provenance"], "provenance")), conditional_rule=MAPPING_CONTRACT["conditional_rule"], claim=CLAIM)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifacts", type=Path, default=HERE / "artifacts")
    parser.add_argument("--graph", type=Path, help="check/use an actual upstream-exported graph in place of the stored graph")
    subparsers = parser.add_subparsers(dest="command", required=True)
    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("--plain-graph", type=Path)
    subparsers.add_parser("check")
    select_parser = subparsers.add_parser("select")
    select_parser.add_argument("selector")
    select_parser.add_argument("--budget", type=int)
    select_parser.add_argument("--out", type=Path)
    find_parser = subparsers.add_parser("find")
    find_parser.add_argument("text")
    inspect_parser = subparsers.add_parser("inspect")
    inspect_parser.add_argument("identity")
    try:
        args = parser.parse_args(argv)
        started = time.perf_counter()
        if args.command == "build":
            ac.require(args.graph is None, "build does not consume an external graph")
            result = build(args.artifacts, args.plain_graph)
        else:
            subject, model, manifest = load_representation(args.artifacts, args.graph)
            if args.command == "check":
                result = jo(status="checked-proposal-transport", model=ac.model_identity(model), source_program_json_round_trip=True, generic_carrier_round_trip=True, pins=subject.pin_counts, counts=manifest["counts"], selector_check=compare_selectors(subject, model), elapsed_seconds=str(round(time.perf_counter() - started, 3)), claim=CLAIM)
            elif args.command == "select":
                selection = select(subject, model, args.selector, args.budget)
                if args.out is not None:
                    protected = [args.artifacts / name for name in ("manifest.json", "graph.json.gz", "model.json.gz", "selectors.json")]
                    if args.graph is not None:
                        protected.append(args.graph)
                    emit(args.out, json.dumps(selection, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8") + b"\n", protected=protected)
                result = selection_summary(selection)
            elif args.command == "find":
                result = ac.find(model, args.text)
            else:
                result = ac.inspect(model, args.identity)
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
    except (ac.Refusal, OSError, KeyError, TypeError, ValueError, tarfile.TarError) as exc:
        print(json.dumps({"status": "refusal", "reason": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
