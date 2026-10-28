"""Explicitly authored demonstration data; no semantic acceptance is asserted."""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys
from typing import Sequence, cast

TENANT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TENANT / "code"))
from ac_graph import (  # noqa: E402
    CALCULUS_SHA256, CALCULUS_URI, CORE_FIELDS, FUNCTORS, MODEL_PROFILE,
    JSON, Object, canonical, digest, grammar, obj, seq, string, validate,
    write_json,
)

PREFIX = "urn:a-c:toy:"


def uid(suffix: str) -> str:
    return PREFIX + suffix


def jo(**values: object) -> Object:
    """Typed JSON boundary for the hand-authored fixture below."""
    result = cast(Object, values)
    grammar(result)
    return result


def schema(kind: str, **values: object) -> Object:
    return jo(type=kind, **values)


def ref(local: Sequence[str] = (), remote: Sequence[str] = (), *, governing: bool = False, sorts: Sequence[str] = ()) -> Object:
    return jo(type="ref", domain=uid("reference-domain:declared"), local_families=list(local), local_sorts=list(sorts), external_kinds=[uid("external-kind:" + k) for k in remote], basis_relation=uid("basis-relation:exact"), governing=governing)


def array(items: Object, minimum: int = 0, maximum: int | None = None) -> Object:
    result = jo(type="array", items=items, min_items=minimum)
    if maximum is not None:
        result["max_items"] = maximum
    return result


def closed(**fields: Object) -> Object:
    return jo(type="object", fields=fields)


def coord(name: str, text: str) -> Object:
    return jo(id=uid(name), sha256=hashlib.sha256(text.encode("utf-8")).hexdigest())


def seal(model: Object) -> Object:
    """Refresh explicit fixture commitments after a deliberate test mutation."""
    signature = obj(model["signature"], "signature")
    signature["sha256"] = digest(jo(id=signature["id"], definition=signature["definition"]))
    interpretation = obj(model["interpretation"], "interpretation")
    obj(interpretation["selection_ledger"], "ledger")["sha256"] = digest(interpretation["dispositions"])
    return model


def toy_model() -> Object:
    text = (TENANT / "examples" / "subject.md").read_text(encoding="utf-8")
    source_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    common_schemas = jo(id=schema("identity"), context=ref(remote=("context",)), owner=ref(remote=("actor",)), scope=array(ref(remote=("scope",)), 1), basis=ref(remote=("basis",)))
    object_ref = ref(("objects",), governing=True, sorts=(uid("sort:statement"),))
    object_refs = array(object_ref)
    text_schema = schema("string", min_length=1)
    common_values = jo(context=uid("context"), owner=uid("author"), scope=[uid("scope")], basis=uid("basis"))
    stop_ref = ref(remote=("stop",))
    evidence_ref = ref(("objects",), ("evidence",), governing=False)
    authority_ref = ref(remote=("authority",))
    all_fields: Object = {}

    def fields(family: str, **specific: Object) -> None:
        result = dict(common_schemas)
        result.update(specific)
        all_fields[family] = result

    value_schema = closed(text=text_schema, arguments=object_refs)
    fields("objects", sort=ref(remote=("sort",)), value=value_schema)
    qualifier_schema = closed(role=schema("enum", values=["required", "discovery"]), arguments=object_refs)
    fields("relations", kind=ref(remote=("relation-kind",)), source=object_ref, target=object_ref, qualifiers=qualifier_schema)
    predicate_schema = closed(operator=schema("enum", values=["requires-external-review"]), arguments=object_refs)
    fields("constraints", kind=ref(remote=("constraint-kind",)), applies_to=array(object_ref, 1), predicate=predicate_schema, judgment_kind=ref(remote=("judgment-kind",)), latitude_ref=array(ref(("latitude",), governing=True), 0, 1), refusal=stop_ref)
    fields("latitude", applies_to=array(object_ref, 1), allowed_variation=array(text_schema, 1), forbidden_variation=array(text_schema, 1), invalidation=ref(remote=("invalidation",)))
    residual_subject = ref(("objects", "relations", "constraints"), governing=True)
    reentry = array(ref(("traversals",), governing=False))
    fields("residuals", subject=residual_subject, kind=ref(remote=("residual-kind",)), uncertainty=text_schema, consequence=text_schema, re_entry=reentry, invalidation=ref(remote=("invalidation",)))
    fields("traversals", domain=ref(remote=("domain",)), codomain=ref(remote=("domain",)), preconditions=array(ref(("constraints",), governing=True)), postconditions=array(ref(("constraints",), governing=True)), authority=authority_ref, evidence=array(evidence_ref), provenance=array(evidence_ref), stop_states=array(stop_ref, 1))
    fields("transformations", traversal=ref(("traversals",), governing=True), domain_model=ref(remote=("model",)), codomain_model=ref(remote=("model",)), operation_authority=authority_ref, preconditions=array(ref(("constraints",), governing=True)), preservation_relation=ref(remote=("preservation-law",)), preserved=object_refs, introduced=array(ref(remote=("future-record",))), removed=object_refs, external_preserved=array(ref(remote=("external-resolution",))), external_introduced=array(ref(remote=("external-resolution",))), external_removed=array(ref(remote=("external-resolution",))), external_resolution_witnesses=array(ref(remote=("witness",))), residuals=array(ref(("residuals",), governing=True)), evidence=array(evidence_ref), provenance=array(evidence_ref), stop_states=array(stop_ref, 1), invalidation=ref(remote=("invalidation",)), re_entry=reentry)
    fields("judgments", kind=ref(remote=("judgment-kind",)), subject=object_ref, subject_digest=text_schema, evaluator=ref(remote=("actor",)), authority=authority_ref, decision=schema("enum", values=["indeterminate", "refused", "accepted"]), evidence=array(evidence_ref, 1), provenance=array(evidence_ref, 1), decided_at=text_schema)

    statement_sort = uid("sort:statement")
    requires = uid("relation-kind:requires")
    discovery = uid("relation-kind:discovery")
    constraint_kind = uid("constraint-kind:review")
    residual_kind = uid("residual-kind:uncertainty")
    judgment_kind = uid("judgment-kind:review")
    definition = jo(fields=all_fields, sorts={statement_sort: jo(value=value_schema)}, relation_kinds={requires: jo(source=object_ref, target=object_ref, qualifiers=qualifier_schema), discovery: jo(source=object_ref, target=object_ref, qualifiers=qualifier_schema)}, constraint_kinds={constraint_kind: jo(applies_to=array(object_ref, 1), predicate=predicate_schema)}, residual_kinds={residual_kind: jo(subject=residual_subject, uncertainty=text_schema, consequence=text_schema, re_entry=reentry, invalidation=ref(remote=("invalidation",)))}, judgment_kinds={judgment_kind: jo(subject=object_ref, decision=schema("enum", values=["indeterminate", "refused", "accepted"]), evidence=array(evidence_ref, 1))}, functor_kinds=list(FUNCTORS), stop_kinds=[uid("stop:refusal")], required_families=list(CORE_FIELDS))

    def record(name: str, **specific: object) -> Object:
        result = dict(common_values)
        result.update(jo(id=uid(name), **specific))
        return result

    a = record("object:a", sort=statement_sort, value=jo(text="A requires B. A may be restated; its unresolved reading stays visible.", arguments=[uid("object:a"), uid("object:a"), uid("object:b")]))
    b = record("object:b", sort=statement_sort, value=jo(text="B also requires A, creating a finite cycle.", arguments=[]))
    c = record("object:c", sort=statement_sort, value=jo(text="C is a provenance-only discovery lead; acquiring A does not require C.", arguments=[]))
    relations: list[JSON] = []
    for name, source, target, kind, role in (
        ("parallel:one", "a", "b", requires, "required"),
        ("parallel:two", "a", "b", requires, "required"),
        ("reverse", "b", "a", requires, "required"),
        ("self", "a", "a", requires, "required"),
        ("discovery", "a", "c", discovery, "discovery"),
    ):
        relations.append(record("relation:" + name, kind=kind, source=uid("object:" + source), target=uid("object:" + target), qualifiers=jo(role=role, arguments=[uid("object:" + source), uid("object:" + source)])))
    latitude = record("latitude:wording", applies_to=[uid("object:a")], allowed_variation=["Restate words while preserving the declared dependency."], forbidden_variation=["Remove the dependency or unresolved reading."], invalidation=uid("invalidation"))
    constraint = record("constraint:review", kind=constraint_kind, applies_to=[uid("object:a")], predicate=jo(operator="requires-external-review", arguments=[uid("object:a")]), judgment_kind=judgment_kind, latitude_ref=[uid("latitude:wording")], refusal=uid("stop:refusal"))
    residual = record("residual:reading", subject=uid("object:a"), kind=residual_kind, uncertainty="Whether A's wording preserves every material reading is unassessed.", consequence="Semantic acceptance remains open.", re_entry=[uid("traversal:review")], invalidation=uid("invalidation"))
    traversal = record("traversal:review", domain=uid("domain:proposal"), codomain=uid("domain:judgment"), preconditions=[uid("constraint:review")], postconditions=[], authority=uid("authority"), evidence=[uid("object:c")], provenance=[uid("object:c")], stop_states=[uid("stop:refusal")])
    transformation = record("transformation:inert", traversal=uid("traversal:review"), domain_model=uid("model:external-before"), codomain_model=uid("model:external-after"), operation_authority=uid("authority"), preconditions=[], preservation_relation=uid("preservation-law"), preserved=[uid("object:a"), uid("object:b"), uid("object:c")], introduced=[], removed=[], external_preserved=[], external_introduced=[], external_removed=[], external_resolution_witnesses=[], residuals=[uid("residual:reading")], evidence=[], provenance=[], stop_states=[uid("stop:refusal")], invalidation=uid("invalidation"), re_entry=[uid("traversal:review")])
    judgment = record("judgment:unassessed", kind=judgment_kind, subject=uid("object:a"), subject_digest=digest(a), evaluator=uid("author"), authority=uid("authority"), decision="indeterminate", evidence=[uid("evidence:authored-fixture")], provenance=[uid("evidence:authored-fixture")], decided_at="2026-10-15T00:00:00Z")
    populations = jo(objects=[c, a, b], relations=relations, constraints=[constraint], latitude=[latitude], residuals=[residual], traversals=[traversal], transformations=[transformation], judgments=[judgment])
    external_members: dict[str, str] = {
        "context": "context", "author": "actor", "scope": "scope", "basis": "basis",
        "sort:statement": "sort", "relation-kind:requires": "relation-kind", "relation-kind:discovery": "relation-kind",
        "constraint-kind:review": "constraint-kind", "residual-kind:uncertainty": "residual-kind", "judgment-kind:review": "judgment-kind",
        "authority": "authority", "invalidation": "invalidation", "stop:refusal": "stop", "domain:proposal": "domain", "domain:judgment": "domain",
        "model:external-before": "model", "model:external-after": "model", "preservation-law": "preservation-law", "evidence:authored-fixture": "evidence",
    }
    resolutions: list[JSON] = [jo(external_identity=uid(name), reference_domain=uid("reference-domain:declared"), external_target_kind=uid("external-kind:" + kind), resolved_target_identity=uid("resolved:" + name), basis_relation=uid("basis-relation:exact"), resolution_basis=uid("basis"), evidence_identity=uid("evidence:external-coordinates")) for name, kind in sorted(external_members.items())]
    local_ids = [string(obj(r, "record")["id"], "record/id") for family in populations.values() for r in seq(family, "population")]
    dispositions: list[JSON] = [jo(source=uid("source:subject.md"), decision="retained", records=local_ids, authority=uid("authority"), basis=uid("basis"), reason="Explicit demonstration interpretation; all inert families are retained for carrier testing, without claiming semantic validity.")]
    interpretation = jo(contract=coord("interpretation-contract", "Explicit demonstration contract: preserve all eight populations; structural tests only; no semantic acceptance or transformation execution."), selection_ledger=coord("selection-ledger", "replaced by seal"), interpreter=coord("interpreter", "Hand-authored toy interpretation."), authority=coord("authority", "Simulation coordinates only; no authority grant is established."), source_reentry=coord("source-reentry", "examples/subject.md"), invalidation=coord("invalidation", "Any change to the exact subject, signature, interpretation or external resolution coordinates invalidates prior evidence."), provenance=[coord("evidence:authoring", "Authored demonstration fixture for independent Graphify a_c realization.")], dispositions=dispositions)
    model = jo(profile=MODEL_PROFILE, id=uid("model:proposal"), basis=jo(id=uid("basis"), calculus=jo(uri=CALCULUS_URI, sha256=CALCULUS_SHA256), subject=jo(id=uid("subject"), sha256=source_hash, inventory=[jo(id=uid("source:subject.md"), sha256=source_hash)])), coordinates=common_values, signature=jo(id=uid("signature"), sha256="", definition=definition), interpretation=interpretation, identity_universe=sorted(local_ids + [uid(k) for k in external_members]), external_resolutions=resolutions, populations=populations, dependency_contract=jo(id=uid("dependency-contract"), required_relation_kinds=[requires], attachment_families=["constraints", "latitude", "residuals"]), functor_bindings={uid("traversal:review"): FUNCTORS[1]})
    # The model envelope carries context/owner/scope, while each record also binds basis.
    obj(model["coordinates"], "coordinates").pop("basis")
    seal(model)
    validate(model)
    return model


def simulated_judgment(model: Object, label: str = "one") -> Object:
    """Test-only supplied acceptance coordinates, never actual acceptance."""
    interpretation = obj(model["interpretation"], "interpretation")
    coordinates = obj(model["coordinates"], "coordinates")
    return jo(id=uid("SIMULATION:acceptance:" + label), kind="urn:a-c:judgment-kind:semantic-acceptance", subject=model["id"], subject_digest=digest(model), context=coordinates["context"], owner=coordinates["owner"], scope=coordinates["scope"], basis=obj(model["basis"], "basis")["id"], evaluator=uid("SIMULATION:evaluator"), authority=interpretation["authority"], decision="accepted", evidence=[coord("SIMULATION:evidence:" + label, "Test-only acceptance coordinates; not a real semantic judgment.")], provenance=[coord("SIMULATION:provenance", "Mechanics test fixture only.")], decided_at="2026-10-15T00:00:00Z", decision_contract=interpretation["contract"])


if __name__ == "__main__":
    model = toy_model()
    write_json(TENANT / "test_env" / "fixtures" / "toy_model.json", model)
    print(digest(model))
