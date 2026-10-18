#!/usr/bin/env python3
"""Build and inspect separate Graphify transports of the frozen V3 candidates.

The existing authored programs supply meaning. This adapter preserves their JSON
and the pinned native checker's explicit acquisition relation. Source-member
nodes add literal discovery over the documentary corpus without adding premises.
No live v3 checkout, indexer installation, model service or Graphify package is
needed by this CLI. Actual upstream qualification is a separate procedure.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import gzip
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import sys
import tarfile
import time
from typing import Any, Sequence
from urllib.parse import quote, unquote

HERE = Path(__file__).resolve().parent
AC_ROOT = HERE.parent
CODEC = AC_ROOT / "build_tenants/graphify/code/ac_graph.py"
sys.path.insert(0, str(CODEC.parent))
import ac_graph as ac  # noqa: E402

Obj = dict[str, Any]
FAMILIES = ("symbols", "clauses", "residuals", "frame_indexes")
CLAIM = ("proposed lossless transport of an existing authored interpretation; "
         "source discovery adds no semantic premise, acceptance or efficiency claim")
OWNER_INSTRUCTION = "latest v3 claude and codex are done and going independent review; build a graphify version for each"


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _pairs(pairs: list[tuple[str, Any]]) -> Obj:
    result: Obj = {}
    for key, value in pairs:
        ac.require(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def parse(raw: bytes | str, *, annotations: bool = False) -> Obj:
    value = json.loads(raw, object_pairs_hook=_pairs)
    ac.grammar(value, annotations=annotations)
    ac.require(isinstance(value, dict), "expected JSON object")
    return value


def rows(value: Any) -> list[Obj]:
    ac.require(isinstance(value, list) and all(isinstance(row, dict) for row in value), "expected object array")
    return value


def canonical(value: Any) -> bytes:
    return ac.canonical(value)


def pretty(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def safe_path(name: str) -> str:
    ac.require(isinstance(name, str) and bool(name), "empty custody path")
    path = PurePosixPath(name)
    ac.require(not path.is_absolute() and ".." not in path.parts and str(path) == name,
               "unsafe/noncanonical custody path: " + name)
    return name


@dataclass(frozen=True)
class Subject:
    root: Path
    config: Obj
    manifest: Obj
    members: dict[str, bytes]
    program: Obj

    def uid(self, suffix: str) -> str:
        return "urn:a-c:dogfood:stdo-v3-i5:" + self.config["tenant"] + ":" + suffix

    def source_path(self, uri: str) -> str | None:
        base = uri.split("#", 1)[0]
        for route in self.config["source_roots"]:
            if base.startswith(route["uri_prefix"]):
                tail = unquote(base[len(route["uri_prefix"]):])
                name = safe_path(route["path_prefix"] + tail)
                ac.require(name in self.members, "source route absent from custody: " + uri)
                return name
        return None

    def source_id(self, name: str) -> str:
        return self.uid("source:" + quote(name, safe="/"))


def load_subject(tenant: str, root: Path | None = None) -> Subject:
    root = root or HERE / ("stdo-v3-i5-" + tenant)
    config = parse((root / "subject.json").read_bytes())
    ac.require(config["profile"] == "a_c.v3-consumer/1" and config["tenant"] == tenant, "wrong consumer profile")
    raw = (root / "input/manifest.json").read_bytes()
    ac.require(sha(raw) == config["input_manifest_sha256"], "input manifest drift")
    manifest = parse(raw)
    ac.require(manifest["profile"] == "a_c.v3-frozen-input/1" and manifest["tenant"] == tenant, "wrong input profile")
    ac.require(config["program_path"] == manifest["program_path"] and config["source_roots"] == manifest["source_roots"], "input routing disagreement")
    archive = manifest["archive"]
    ac.require(archive["path"] == "candidate.tar.gz", "unsupported archive coordinate")
    raw_archive = (root / "input/candidate.tar.gz").read_bytes()
    ac.require(len(raw_archive) == archive["bytes"] and sha(raw_archive) == archive["sha256"], "input archive drift")
    expected: dict[str, Obj] = {}
    for row in rows(manifest["members"]):
        name = safe_path(row["path"])
        ac.require(name not in expected and row["mode"] in ("100644", "100755"), "duplicate/nonregular inventory member")
        expected[name] = row
    members: dict[str, bytes] = {}
    seen: set[str] = set()
    with tarfile.open(fileobj=io.BytesIO(raw_archive), mode="r:gz") as stream:
        for entry in stream:
            name = safe_path(entry.name.rstrip("/") if entry.isdir() else entry.name)
            ac.require(name not in seen, "duplicate archive member")
            seen.add(name)
            if entry.isdir():
                ac.require(any(p.startswith(name + "/") for p in expected), "unknown archive directory")
                continue
            ac.require(entry.isfile() and name in expected, "unknown/nonregular archive member")
            handle = stream.extractfile(entry)
            ac.require(handle is not None, "unreadable archive member")
            assert handle is not None
            content = handle.read()
            pin = expected[name]
            ac.require(len(content) == pin["bytes"] and sha(content) == pin["sha256"], "custody member drift: " + name)
            blob = hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()
            ac.require(blob == pin["git_blob"], "Git blob mismatch: " + name)
            members[name] = content
    ac.require(set(members) == set(expected), "incomplete archive custody")
    program = parse(members[safe_path(config["program_path"])])
    subject = Subject(root, config, manifest, members, program)
    validate_native(subject)
    return subject


def native_items(program: Obj) -> dict[str, tuple[str, Obj]]:
    result: dict[str, tuple[str, Obj]] = {}
    for family in FAMILIES:
        for row in rows(program.get(family, [])):
            identity = ac.identity(row["uri"], family + "/uri")
            ac.require(identity not in result, "duplicate native identity: " + identity)
            result[identity] = (family, row)
    return result


def validate_native(subject: Subject) -> None:
    program = subject.program
    ac.require(program["kind"] == "axiom-indexer.axiomatic-program" and program["schema_version"] == 1, "unsupported native program")
    ac.require(program["calculus_ref"] == ac.CALCULUS_URI, "unselected encoding calculus")
    items = native_items(program)
    local = {key for key, (family, _) in items.items() if family != "frame_indexes"}
    external = set(program["vocabulary_refs"]) | set(program["frame_refs"])
    ac.require(not local & external, "native local/external collision")
    for _, (family, item) in items.items():
        for route in item.get("source_refs", []):
            subject.source_path(route)
        if family == "clauses":
            for arg in rows(item["arguments"]):
                ac.require("role" in arg and ("ref" in arg) != ("literal" in arg), "invalid native argument")
                if "ref" in arg:
                    ac.require(arg["ref"] in local | external, "unresolved native argument reference")
        elif family == "residuals":
            ac.require(bool(item["subject_refs"]) and all(ref in local for ref in item["subject_refs"]), "invalid residual subjects")
            for route in item["re_entry_refs"]:
                subject.source_path(route)
        elif family == "frame_indexes":
            for field, target_family in (("clause_refs", "clauses"), ("residual_refs", "residuals")):
                ac.require(all(ref in items and items[ref][0] == target_family for ref in item[field]), "wrong native selector root kind")


def mapping_contract(subject: Subject) -> Obj:
    return {
        "id": subject.uid("mapping:1"), "claim": CLAIM,
        "native_content": "Every native symbol, clause, residual and selector retains exact JSON content, identity and ordinal. The envelope retains all other fields.",
        "required": "Close explicit local clause-argument refs, selector roots, residual subjects, and residuals attached to an included subject, matching the pinned native checker.",
        "non_governing": "Acquisition-route literals, source links and document nodes are inspectable without becoming native required dependencies. Unknown applicability remains unresolved.",
        "core_families": "Opaque program elements are transport objects, distinguished by native_family and sort; they are not invented core constraint, residual or judgment instances. All eight core population keys remain explicit.",
        "sources": "Archived Markdown members are literal discovery objects, linked by exact authored source coordinates; their presence asserts no additional interpretation coverage.",
    }


def signature(subject: Subject) -> Obj:
    uid = subject.uid
    def s(kind: str, **kw: Any) -> Obj:
        return dict(type=kind, **kw)
    def arr(item: Obj, minimum: int = 0) -> Obj:
        return s("array", items=item, min_items=minimum)
    def obj(**kw: Obj) -> Obj:
        return s("object", fields=kw)
    def ref(local: Sequence[str] = (), remote: Sequence[str] = (), governing: bool = False) -> Obj:
        return s("ref", domain=uid("reference-domain"), local_families=list(local), local_sorts=[],
                 external_kinds=[uid("external-kind:" + k) for k in remote], basis_relation=uid("basis-relation"), governing=governing)
    text = s("string")
    nonempty = s("string", min_length=1)
    local = ref(("objects",), governing=True)
    other = ref(("objects",), ("native-reference",))
    occurrence = lambda target: obj(kind=nonempty, origin=nonempty, pointer=nonempty, target=target)
    value = obj(a_text=nonempty, native_family=s("enum", values=[*FAMILIES, "envelope", "source_members"]),
                native_json=nonempty, ordinal=s("integer"), required_refs=arr(occurrence(local)),
                non_governing_refs=arr(occurrence(other)), routes=arr(obj(ordinal=s("integer"), role=nonempty, payload=nonempty, targets=arr(other))))
    common = dict(id=s("identity"), context=ref(remote=("context",)), owner=ref(remote=("owner",)),
                  scope=arr(ref(remote=("scope",)), 1), basis=ref(remote=("basis",)))
    fields: Obj = {}
    def family(name: str, **kw: Any) -> None:
        fields[name] = dict(common, **kw)
    evidence = arr(ref(remote=("evidence",)))
    constraints = arr(ref(("constraints",), governing=True))
    object_refs = arr(local)
    reentry = arr(ref(remote=("native-reference",)))
    invalidation = ref(remote=("invalidation",))
    family("objects", sort=ref(remote=("sort",)), value=value)
    family("relations", kind=ref(remote=("relation-kind",)), source=local, target=local, qualifiers=obj())
    family("constraints", kind=ref(remote=("constraint-kind",)), applies_to=object_refs, predicate=text,
           judgment_kind=ref(remote=("judgment-kind",)), latitude_ref=arr(ref(("latitude",), governing=True)), refusal=ref(remote=("stop",)))
    family("latitude", applies_to=object_refs, allowed_variation=arr(text), forbidden_variation=arr(text), invalidation=invalidation)
    family("residuals", subject=local, kind=ref(remote=("residual-kind",)), uncertainty=text, consequence=text, re_entry=reentry, invalidation=invalidation)
    family("traversals", domain=ref(remote=("domain",)), codomain=ref(remote=("domain",)), preconditions=constraints,
           postconditions=constraints, authority=ref(remote=("authority",)), evidence=evidence, provenance=evidence, stop_states=arr(ref(remote=("stop",))))
    family("transformations", traversal=ref(("traversals",), governing=True), domain_model=ref(remote=("model",)),
           codomain_model=ref(remote=("model",)), operation_authority=ref(remote=("authority",)), preconditions=constraints,
           preservation_relation=ref(remote=("preservation-law",)), preserved=object_refs, introduced=object_refs, removed=object_refs,
           external_preserved=arr(ref(remote=("resolution",))), external_introduced=arr(ref(remote=("resolution",))),
           external_removed=arr(ref(remote=("resolution",))), external_resolution_witnesses=arr(ref(remote=("witness",))),
           residuals=arr(ref(("residuals",), governing=True)), evidence=evidence, provenance=evidence,
           stop_states=arr(ref(remote=("stop",))), invalidation=invalidation, re_entry=reentry)
    family("judgments", kind=ref(remote=("judgment-kind",)), subject=local, subject_digest=nonempty,
           evaluator=ref(remote=("actor",)), authority=ref(remote=("authority",)), decision=nonempty, evidence=evidence, provenance=evidence, decided_at=nonempty)
    return dict(fields=fields, sorts={uid("sort:" + k): {"value": value} for k in [*FAMILIES, "envelope", "source_members"]},
                relation_kinds={}, constraint_kinds={}, residual_kinds={}, judgment_kinds={}, functor_kinds=[], stop_kinds=[], required_families=["objects"])


def authored_display(item: Obj) -> str:
    """Lead bounded upstream excerpts with an existing authored predicate."""
    for argument in item.get("arguments", []):
        if argument["role"].endswith("#semantic-record") and "literal" in argument:
            semantic = parse(argument["literal"])
            for field in ("predicate", "definition", "binding"):
                if isinstance(semantic.get(field), str) and semantic[field]:
                    return semantic[field]
    return str(item.get("statement") or item.get("scope") or item.get("label") or item.get("detail") or item["uri"])


def build_model(subject: Subject) -> ac.Model:
    uid, program = subject.uid, subject.program
    items = native_items(program)
    local = {key for key, (family, _) in items.items() if family != "frame_indexes"}
    docs = {name: payload for name, payload in subject.members.items() if name.endswith(".md")}
    common = dict(context=uid("context"), owner=uid("transport-owner"), scope=[uid("scope:frozen-input")], basis=uid("basis"))
    external = {common["context"]: "context", common["owner"]: "owner", common["scope"][0]: "scope", common["basis"]: "basis"}
    external.update({uid("sort:" + k): "sort" for k in [*FAMILIES, "envelope", "source_members"]})
    records: list[Obj] = []
    affected: dict[str, list[tuple[str, int]]] = {}
    for residual in rows(program["residuals"]):
        for i, target in enumerate(residual["subject_refs"]):
            affected.setdefault(target, []).append((residual["uri"], i))
    def edge(kind: str, origin: str, pointer: str, target: str) -> Obj:
        return dict(kind=kind, origin=origin, pointer=pointer, target=target)
    def other(target: str) -> str:
        if target not in items:
            ac.require(target not in external or external[target] == "native-reference", "external kind collision")
            external[target] = "native-reference"
        return target
    def value(family: str, native: Obj, ordinal: int, display: str) -> Obj:
        return dict(a_text=display, native_family=family, native_json=canonical(native).decode(), ordinal=ordinal,
                    required_refs=[], non_governing_refs=[], routes=[])
    def record(identity: str, family: str, data: Obj) -> None:
        records.append(dict(common, id=identity, sort=uid("sort:" + family), value=data))
    for family in FAMILIES:
        for ordinal, item in enumerate(rows(program.get(family, []))):
            identity = item["uri"]
            display = authored_display(item)
            if family == "clauses":
                display += "\n" + "\n".join(str(a["literal"]) for a in item["arguments"] if "literal" in a)
            data = value(family, item, ordinal, display)
            for i, route in enumerate(item.get("source_refs", [])):
                path = subject.source_path(route)
                target = subject.source_id(path) if path in docs else other(route)
                data["non_governing_refs"].append(edge("source", identity, "/source_refs/" + str(i), target))
            if family == "clauses":
                for i, arg in enumerate(item["arguments"]):
                    pointer = "/arguments/" + str(i)
                    if "ref" in arg:
                        target = arg["ref"]
                        governing = target in local
                        data["required_refs" if governing else "non_governing_refs"].append(
                            edge("argument", identity, pointer + "/ref", target if governing else other(target)))
                    elif arg["role"].endswith("#acquisition-route"):
                        route = parse(arg["literal"])
                        ac.require(route["acquisition"] in ("conditional", "provenance"), "unsupported acquisition route")
                        data["routes"].append(dict(ordinal=i, role=arg["role"], payload=arg["literal"],
                                                   targets=[other(route[k]) for k in ("target", "target_index")]))
            elif family == "residuals":
                data["required_refs"] += [edge("residual-subject", identity, "/subject_refs/" + str(i), target)
                                           for i, target in enumerate(item["subject_refs"])]
            elif family == "frame_indexes":
                for field in ("clause_refs", "residual_refs"):
                    data["required_refs"] += [edge("selector-root", identity, "/" + field + "/" + str(i), target)
                                               for i, target in enumerate(item[field])]
            for residual_id, i in affected.get(identity, []):
                data["required_refs"].append(edge("affected-residual", residual_id, "/subject_refs/" + str(i), residual_id))
            record(identity, family, data)
    envelope = {key: val for key, val in program.items() if key not in FAMILIES}
    record(uid("program-envelope"), "envelope", value("envelope", envelope, 0, "Exact native program envelope"))
    for ordinal, (name, raw) in enumerate(sorted(docs.items())):
        text = raw.decode("utf-8")
        native = dict(path=name, sha256=sha(raw), text=text)
        record(subject.source_id(name), "source_members", value("source_members", native, ordinal, name + "\n" + text))
    populations = {family: [] for family in ac.CORE_FIELDS}
    populations["objects"] = records
    ids = [record["id"] for record in records]
    ac.require(len(ids) == len(set(ids)) and not set(ids) & set(external), "transport identity collision")
    basis = uid("basis")
    coordinate = lambda identity, raw: dict(id=identity, sha256=sha(raw))
    authority = coordinate(uid("authority:T-003-owner-instruction"), OWNER_INSTRUCTION.encode())
    source_id = uid("input:native-program")
    source_ids = [subject.source_id(name) for name in sorted(docs)]
    dispositions = [dict(source=source_id, decision="retained", records=[i for i in ids if i not in source_ids], authority=authority["id"], basis=basis,
                         reason="Exact authored program transport; coverage remains the source candidate's declared coverage."),
                    dict(source=uid("input:manifest"), decision="retained" if source_ids else "omitted", records=source_ids,
                         authority=authority["id"], basis=basis,
                         reason="Pinned archive inventory supplies literal Markdown discovery objects without adding semantic premises.")]
    definition = signature(subject)
    signature_id = uid("signature:1")
    resolutions = [dict(external_identity=identity, reference_domain=uid("reference-domain"),
                        external_target_kind=uid("external-kind:" + kind), resolved_target_identity=identity,
                        basis_relation=uid("basis-relation"), resolution_basis=basis,
                        evidence_identity="urn:sha256:" + subject.manifest["archive"]["sha256"])
                   for identity, kind in sorted(external.items())]
    document = dict(
        profile=ac.MODEL_PROFILE, id=uid("model:proposal:1"),
        basis=dict(id=basis, calculus=dict(uri=ac.CALCULUS_URI, sha256=ac.CALCULUS_SHA256),
                   subject=dict(id=program["uri"], sha256=sha(subject.members[subject.config["program_path"]]),
                                inventory=[coordinate(source_id, subject.members[subject.config["program_path"]]),
                                           coordinate(uid("input:manifest"), (subject.root / "input/manifest.json").read_bytes())])),
        coordinates={key: val for key, val in common.items() if key != "basis"},
        signature=dict(id=signature_id, definition=definition, sha256=ac.digest(dict(id=signature_id, definition=definition))),
        interpretation=dict(contract=coordinate(uid("mapping:1"), canonical(mapping_contract(subject))),
                            selection_ledger=coordinate(uid("selection-ledger"), canonical(dispositions)),
                            interpreter=coordinate(uid("interpreter:transport"), Path(__file__).read_bytes()), authority=authority,
                            source_reentry=coordinate(uid("input:manifest"), (subject.root / "input/manifest.json").read_bytes()),
                            invalidation=coordinate(uid("invalidation"), b"Changed input, mapping, builder or codec invalidates previous construction evidence."),
                            provenance=[coordinate(uid("input:subject"), (subject.root / "subject.json").read_bytes())], dispositions=dispositions),
        identity_universe=sorted(ids + list(external)), external_resolutions=resolutions, populations=populations,
        dependency_contract=dict(id=uid("dependency-contract:native-explicit-closure"), required_relation_kinds=[],
                                 attachment_families=["constraints", "latitude", "residuals"]), functor_bindings={})
    return ac.validate(document)


def recover_program(model: ac.Model) -> Obj:
    recovered: dict[str, dict[int, Obj]] = {family: {} for family in [*FAMILIES, "envelope"]}
    for record in model.records.values():
        data = record.fields["value"]
        family = data["native_family"]
        if family in recovered:
            ordinal = data["ordinal"]
            ac.require(ordinal not in recovered[family], "duplicate native ordinal")
            native = parse(data["native_json"])
            ac.require(family == "envelope" or native["uri"] == record.identity, "native identity mismatch")
            recovered[family][ordinal] = native
    ac.require(set(recovered["envelope"]) == {0}, "missing native envelope")
    result = dict(recovered["envelope"][0])
    for family in FAMILIES:
        values = recovered[family]
        ac.require(set(values) == set(range(len(values))), "noncontiguous native ordinals")
        result[family] = [values[i] for i in range(len(values))]
    return result


def native_closure(program: Obj, selectors: Sequence[Obj]) -> set[str]:
    """Independent raw-program oracle matching pinned RC2 explicit-reference rules."""
    items = {row["uri"]: (family, row) for family in ("symbols", "clauses", "residuals") for row in program[family]}
    affected: dict[str, set[str]] = {}
    for residual in program["residuals"]:
        for subject in residual["subject_refs"]:
            affected.setdefault(subject, set()).add(residual["uri"])
    pending = [target for selector in selectors for field in ("clause_refs", "residual_refs") for target in selector[field]]
    included: set[str] = set()
    while pending:
        identity = pending.pop()
        if identity in included:
            continue
        ac.require(identity in items, "closure target outside native items")
        included.add(identity)
        family, item = items[identity]
        pending.extend(affected.get(identity, set()))
        if family == "clauses":
            pending.extend(a["ref"] for a in item["arguments"] if a.get("ref") in items)
        elif family == "residuals":
            pending.extend(item["subject_refs"])
    return included


def verify_transport(subject: Subject, model: ac.Model) -> Obj:
    ac.require(recover_program(model) == subject.program, "native program round trip differs")
    expected = build_model(subject)
    ac.require(model.document == expected.document, "transport payload, routes, occurrences or source content differs")
    selectors = rows(subject.program["frame_indexes"])
    projections = ac.project_many(model, [([s["uri"]], None) for s in selectors])
    catalogue = []
    for selector, view in zip(selectors, projections):
        expected_ids = native_closure(subject.program, [selector]) | {selector["uri"]}
        ac.require(set(view["included"]) == expected_ids, "native selector closure differs: " + selector["uri"])
        catalogue.append(dict(uri=selector["uri"], scope=selector["scope"], records=len(expected_ids),
                              required_records=sorted(expected_ids)))
    return dict(selectors=len(catalogue), all_required_closures_match=True, catalogue=catalogue)


def read_document(path: Path, *, annotations: bool = False) -> Obj:
    raw = path.read_bytes()
    return parse(gzip.decompress(raw) if path.suffix == ".gz" else raw, annotations=annotations)


def emit(path: Path, raw: bytes, protected: Sequence[Path] = ()) -> None:
    resolved = path.resolve()
    ac.require(not path.is_symlink(), "symlink output refused")
    for source in protected:
        ac.require(resolved != source.resolve() and source.resolve() not in resolved.parents, "output aliases protected input")
        ac.require(not (path.exists() and source.is_file() and path.samefile(source)), "hardlink output aliases input")
    if path.exists():
        ac.require(path.is_file() and path.read_bytes() == raw, "different existing output refuses: " + str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(raw)


def build(tenant: str, out_dir: Path | None = None, plain_graph: Path | None = None) -> Obj:
    started = time.perf_counter()
    subject = load_subject(tenant)
    out_dir = out_dir or subject.root / "artifacts"
    model = build_model(subject)
    carrier = ac.materialize(model)
    recovered = ac.decode(carrier)
    ac.require(recovered.document == model.document, "carrier round trip differs")
    checked = verify_transport(subject, recovered)
    files = {"model.json.gz": gzip.compress(canonical(model.document) + b"\n", mtime=0),
             "graph.json.gz": gzip.compress(canonical(carrier.document) + b"\n", mtime=0),
             "selectors.json": pretty(dict(tenant=tenant, selectors=checked["catalogue"]))}
    counts = {family: len(subject.program.get(family, [])) for family in FAMILIES}
    counts.update(source_members=sum(r.fields["value"]["native_family"] == "source_members" for r in model.records.values()),
                  graph_nodes=len(carrier.document["nodes"]), graph_edges=len(carrier.document["links"]))
    manifest = dict(profile="a_c.v3-graphify-representation/1", tenant=tenant, claim=CLAIM,
                    input_manifest_sha256=subject.config["input_manifest_sha256"], subject_sha256=sha((subject.root / "subject.json").read_bytes()),
                    checkpoint_commit=subject.manifest["checkpoint_commit"], package_commit=subject.manifest["package_commit"],
                    raw_program_sha256=sha(subject.members[subject.config["program_path"]]), canonical_program_sha256=ac.digest(subject.program),
                    builder_sha256=sha(Path(__file__).read_bytes()), codec_sha256=sha(CODEC.read_bytes()),
                    model=ac.model_identity(model), carrier_sha256=ac.digest(carrier.document), counts=counts,
                    mapping_contract=mapping_contract(subject), coverage=subject.config["coverage"],
                    selector_check={k: v for k, v in checked.items() if k != "catalogue"},
                    artifacts={name: dict(bytes=len(raw), sha256=sha(raw)) for name, raw in files.items()})
    files["manifest.json"] = pretty(manifest)
    protected = [subject.root / "input", subject.root / "subject.json", Path(__file__), CODEC]
    for name, raw in files.items():
        emit(out_dir / name, raw, protected)
    if plain_graph:
        emit(plain_graph, canonical(carrier.document) + b"\n", protected)
    return dict(status="built", tenant=tenant, counts=counts, selector_check=manifest["selector_check"],
                output=str(out_dir), elapsed_seconds=round(time.perf_counter() - started, 3), claim=CLAIM)


def load_representation(tenant: str, out_dir: Path | None = None, graph_path: Path | None = None) -> tuple[Subject, ac.Model, Obj]:
    subject = load_subject(tenant)
    out_dir = out_dir or subject.root / "artifacts"
    manifest = parse((out_dir / "manifest.json").read_bytes())
    ac.require(manifest["profile"] == "a_c.v3-graphify-representation/1" and manifest["tenant"] == tenant, "wrong representation profile")
    ac.require(manifest["builder_sha256"] == sha(Path(__file__).read_bytes()) and manifest["codec_sha256"] == sha(CODEC.read_bytes()), "builder or codec changed; rebuild required")
    ac.require(manifest["input_manifest_sha256"] == subject.config["input_manifest_sha256"] and manifest["subject_sha256"] == sha((subject.root / "subject.json").read_bytes()), "representation input binding differs")
    ac.require(set(manifest["artifacts"]) == {"model.json.gz", "graph.json.gz", "selectors.json"}, "incomplete artifact inventory")
    for name, pin in manifest["artifacts"].items():
        raw = (out_dir / name).read_bytes()
        ac.require(len(raw) == pin["bytes"] and sha(raw) == pin["sha256"], "artifact drift: " + name)
    model = ac.decode(ac.GraphCarrier(read_document(graph_path or out_dir / "graph.json.gz", annotations=True)))
    ac.require(model.document == read_document(out_dir / "model.json.gz"), "stored model and recovered model differ")
    ac.require(ac.model_identity(model) == manifest["model"], "model identity differs")
    canonical_carrier = ac.materialize(model)
    ac.require(ac.digest(canonical_carrier.document) == manifest["carrier_sha256"], "semantic carrier identity differs")
    checked = verify_transport(subject, model)
    ac.require(read_document(out_dir / "selectors.json") == dict(tenant=tenant, selectors=checked["catalogue"]), "selector catalogue differs")
    expected_counts = {family: len(subject.program.get(family, [])) for family in FAMILIES}
    expected_counts.update(source_members=sum(r.fields["value"]["native_family"] == "source_members" for r in model.records.values()),
                           graph_nodes=len(canonical_carrier.document["nodes"]), graph_edges=len(canonical_carrier.document["links"]))
    ac.require(manifest["counts"] == expected_counts and manifest["mapping_contract"] == mapping_contract(subject)
               and manifest["coverage"] == subject.config["coverage"]
               and manifest["checkpoint_commit"] == subject.manifest["checkpoint_commit"]
               and manifest["package_commit"] == subject.manifest["package_commit"]
               and manifest["raw_program_sha256"] == sha(subject.members[subject.config["program_path"]])
               and manifest["canonical_program_sha256"] == ac.digest(subject.program)
               and manifest["selector_check"] == {k: v for k, v in checked.items() if k != "catalogue"}
               and manifest["claim"] == CLAIM, "representation metadata differs from source")
    return subject, model, manifest


def choose_selectors(program: Obj, names: Sequence[str]) -> list[Obj]:
    selectors = rows(program["frame_indexes"])
    result = []
    for name in names:
        matches = [s for s in selectors if s["uri"] == name]
        if not matches:
            matches = [s for s in selectors if any(s["uri"].endswith(marker + name)
                                                  for marker in (":index:", ":frame-index:"))]
        ac.require(len(matches) == 1, "selector must be an exact URI or unique exact index suffix: " + name)
        ac.require(matches[0] not in result, "duplicate selector")
        result.append(matches[0])
    return result


def select(subject: Subject, model: ac.Model, names: Sequence[str], budget: int | None = None) -> Obj:
    selectors = choose_selectors(subject.program, names)
    view = ac.project(model, [s["uri"] for s in selectors], budget)
    included = set(view["included"])
    ac.require(included == native_closure(subject.program, selectors) | {s["uri"] for s in selectors}, "selection closure mismatch")
    native = {family: [row for row in subject.program[family] if row["uri"] in included] for family in ("symbols", "clauses", "residuals")}
    routes = [dict(owner=identity, **route) for identity in sorted(included)
              for route in model.records[identity].fields["value"]["routes"]]
    return dict(profile="a_c.v3-graphify-selection/1", tenant=subject.config["tenant"], native_selectors=selectors,
                projection=view, native=native, acquisition_routes=routes,
                conditional_rule="Establish applicability externally; add an applicable target selector explicitly, or retain unknown applicability and withhold dependent action.", claim=CLAIM)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tenant", required=True, choices=("codex", "claude"))
    parser.add_argument("--artifacts", type=Path)
    parser.add_argument("--graph", type=Path, help="actual upstream-exported graph to recover and use")
    sub = parser.add_subparsers(dest="command", required=True)
    build_parser = sub.add_parser("build")
    build_parser.add_argument("--plain-graph", type=Path)
    sub.add_parser("check")
    sub.add_parser("selectors")
    find_parser = sub.add_parser("find")
    find_parser.add_argument("text")
    inspect_parser = sub.add_parser("inspect")
    inspect_parser.add_argument("identity")
    source_parser = sub.add_parser("source")
    source_parser.add_argument("path_or_uri")
    select_parser = sub.add_parser("select")
    select_parser.add_argument("selector", nargs="+")
    select_parser.add_argument("--budget", type=int)
    select_parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "build":
            ac.require(args.graph is None, "build does not consume an external graph")
            result = build(args.tenant, args.artifacts, args.plain_graph)
        elif args.command == "source":
            subject = load_subject(args.tenant)
            name = args.path_or_uri if args.path_or_uri in subject.members else subject.source_path(args.path_or_uri)
            ac.require(name in subject.members, "unknown frozen source coordinate")
            sys.stdout.buffer.write(subject.members[name])
            return 0
        else:
            subject, model, manifest = load_representation(args.tenant, args.artifacts, args.graph)
            if args.command == "check":
                result = dict(status="passed", tenant=args.tenant, counts=manifest["counts"],
                              selector_check=manifest["selector_check"], native_program_round_trip=True, claim=CLAIM)
            elif args.command == "selectors":
                result = read_document((args.artifacts or subject.root / "artifacts") / "selectors.json")
            elif args.command == "find":
                result = ac.find(model, args.text)
            elif args.command == "inspect":
                result = ac.inspect(model, args.identity)
                result["native"] = parse(model.records[args.identity].fields["value"]["native_json"])
            else:
                selection = select(subject, model, args.selector, args.budget)
                if args.out:
                    protected = [subject.root / "input", subject.root / "subject.json", subject.root / "prepare.py",
                                 args.artifacts or subject.root / "artifacts", Path(__file__), CODEC]
                    if args.graph:
                        protected.append(args.graph)
                    emit(args.out, pretty(selection), protected)
                result = dict(status="selected", tenant=args.tenant, records=len(selection["projection"]["included"]),
                              counts={family: len(value) for family, value in selection["native"].items()},
                              acquisition_routes=len(selection["acquisition_routes"]), output=str(args.out) if args.out else None, claim=CLAIM)
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
    except (ac.Refusal, OSError, KeyError, TypeError, ValueError, tarfile.TarError, UnicodeError) as exc:
        print(json.dumps(dict(status="refusal", reason=str(exc)), ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
