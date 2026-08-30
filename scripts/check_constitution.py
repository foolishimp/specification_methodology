#!/usr/bin/env python3
"""Check decidable STDO Representation source-project invariants.

The checker proves only the structural and declared-boundary conditions named in
its output. It does not assess semantic compression adequacy, accept a reference
frame or representation profile, or judge an LLM response.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, NoReturn


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "specification"

REQUIREMENT_STATUSES = {"Active", "Deferred", "Superseded", "Orphaned"}
REQUIREMENT_CATEGORIES = {
    "Capability",
    "Constraint / Guarantee",
    "Governance",
    "Verification",
}
TICKET_FIELDS = {
    "id",
    "title",
    "type",
    "ticket_category",
    "status",
    "goal",
    "change_intent",
    "change_class",
    "re_entry_point",
    "triaged_at",
    "created_at",
    "updated_at",
}
TICKET_TYPES = {"feature", "bug", "spike", "chore"}
TICKET_CATEGORIES = {"ordinary", "implementation_migration"}
CHANGE_CLASSES = {
    "goal_reprice",
    "intent_reprice",
    "product_reprice",
    "requirement_reprice",
    "design_reframe",
    "realization_refactor",
}
LANE_STATUS = {
    "backlog": "backlog",
    "active": "active",
    "completed": "completed",
}
EXPECTED_REQUIREMENTS = {
    "REQ-P-BASIS-AND-IDENTITY.md",
    "REQ-P-COMPRESSION-VERIFICATION.md",
    "REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md",
    "REQ-P-FP-CONSUMPTION.md",
    "REQ-P-REPRESENTATION-ALGEBRA.md",
    "REQ-P-SELECTION-AND-ACCEPTANCE.md",
}
TRAVERSAL_IDENTITIES = {
    "F_D": "urn:stdo:concept:axiomatic-calculus:f-d",
    "F_P": "urn:stdo:concept:axiomatic-calculus:f-p",
    "F_H": "urn:stdo:concept:axiomatic-calculus:f-h",
}
ROLE_IDENTITIES = {
    "Executive": (
        "stdo://releases/v2.5.0-rc.1/standards/"
        "STDO_REFERENCE_FRAME_BASELINE.md#executive"
    ),
    "Worker": (
        "stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#worker"
    ),
    "Reviewer": (
        "stdo://releases/v2.5.0-rc.1/standards/"
        "STDO_REFERENCE_FRAME_BASELINE.md#reviewer"
    ),
}
STDO_SCHEMA_URI = (
    "stdo://releases/v2.5.0-rc.1/standards/schemas/product-definition.schema.json"
)
STDO_SELECTOR = "stdo://channels/2.5.0"
STDO_BASIS_URI = "stdo://releases/v2.5.0-rc.1/"
STDO_MANIFEST_SHA256 = (
    "3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338"
)
STDO_MEMBER_COUNT = 51
STDO_MEMBER_SET_SHA256 = (
    "87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5"
)
AXIOMATIC_CALCULUS_SHA256 = (
    "cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d"
)
CALCULUS_BASIS_IDENTITY = (
    "urn:stdo:axiomatic-calculus-basis:sha256:"
    "bac18f57d655ce730462b84d62306d4af9ef3ebe1292f9889d67fe877f31d0da"
)
SUBJECT_BASIS_IDENTITY = (
    "urn:stdo-representation:subject-basis:stdo:sha256:"
    "73f2581c2d8466a2c8e41b842c2178495431ff28450192f00368ec9fff8766a6"
)
FRAME_BASIS_IDENTITY = "urn:stdo-representation:reference-frame-basis:source-project:7"
GTL_PROFILE_IDENTITY = "urn:stdo-index:gtl-profile:axiom-index:7"
T002_ACCEPTED_WHAT_MEMBER_SET_IDENTITY = (
    "sha256:4158caca78aeadd4dd31e802f9801ee2b81e0f1a96fc2774705db909d3bbf35e"
)
T002_ACCEPTED_FRAME_BASIS_IDENTITY = (
    "urn:stdo-representation:reference-frame-basis:source-project:3"
)
T002_ACCEPTED_FRAME_BASIS_SHA256 = (
    "sha256:b589485673b72536c222c9cd52b8f36ac250533a1eaaee4d0303754788045ec0"
)
T002_ACCEPTED_GTL_PROFILE_SHA256 = (
    "sha256:27b496722bfea537ed9e3a8c412c3ca162f83e723ecd9b783e1697d8ffae5f47"
)
T002_ACCEPTED_GTL_PROFILE_IDENTITY = (
    "urn:stdo-representation:gtl-profile:stdo-gtl:0.7.0"
)
PRODUCT_OWNER_ACTOR = "https://github.com/foolishimp"
PRODUCT_OWNER_AUTHORITY = "urn:stdo-representation:authority:product-owner"
PRODUCT_OWNER_GRANT = "urn:stdo-representation:grant:product-owner:1"
PRODUCT_OWNER_GRANT_SCOPE = (
    "Select and accept project-owned frame bases, representation profiles, Source "
    "STDO semantic selections, candidate STDO.gtl Products, and tenant-qualified "
    "releases; authorize deterministic construction; and issue bounded build-time "
    "operation grants for proposal-only semantic-compilation and deterministic "
    "structural-evaluation traversals; excludes "
    "changing Source STDO or transferring semantic, review, acceptance, release, "
    "or runtime authority to a traversal."
)
ROLE_BINDING_URI = (
    "./specification/requirements/"
    "REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md#cross-context-role-import"
)
EXPECTED_DISAMBIGUATIONS = {
    term: {
        "uri": ROLE_BINDING_URI,
        "term": term,
        "context": "urn:stdo-representation:bounded-context:product",
        "disambiguates": [identity],
        "resolves_to": identity,
        "authority": [identity, ROLE_BINDING_URI],
        "basis": ["#/constitution/stdo/basis"],
        "applies_to": ["urn:stdo:product-definition:stdo-representation"],
    }
    for term, identity in ROLE_IDENTITIES.items()
}
GTL_CARRIER_COORDINATE = {
    "authority_inventory_count": 33,
    "authority_root": "specification/requirements/gtl/",
    "authority_tree_sha1": "21a44b1941a1055d6abd973937e65b83e359de1b",
    "commit_sha1": "8d7f965a3fae7d1acea6a9db298798480fd4cc2f",
    "repository": "https://github.com/foolishimp/abiogenesis.git",
}
GTL_CARRIER_BASIS_PREFIX = "urn:stdo-representation:carrier-basis:gtl:sha256:"


class CheckFailure(RuntimeError):
    """One explicit source-project invariant failed."""


def fail(message: str) -> NoReturn:
    raise CheckFailure(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_ascii_coordinate_bytes(value: object) -> bytes:
    """Serialize the closed ASCII GTL basis coordinate in its RFC 8785 form.

    This helper is intentionally not advertised as a general JCS implementation.
    The governed coordinate contains only ASCII object names/strings and one
    non-negative integer, for which this serialization is the exact JCS result.
    """

    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def reject_duplicate_object_names(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            fail(f"duplicate JSON object name: {key}")
        result[key] = value
    return result


def load_json_unique(path: Path) -> Any:
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_object_names,
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail(f"cannot read unique-name JSON {path}: {exc}")


def parse_ticket_metadata(text: str, source: str) -> dict[str, str]:
    """Parse only the contiguous metadata header immediately below the H1."""

    lines = text.splitlines()
    require(bool(lines) and lines[0].startswith("# "), f"missing ticket H1: {source}")
    index = 1
    while index < len(lines) and not lines[index].strip():
        index += 1

    values: dict[str, str] = {}
    metadata_pattern = re.compile(r"([a-z][a-z0-9_]*): (.+)")
    while index < len(lines) and lines[index].strip():
        match = metadata_pattern.fullmatch(lines[index])
        require(
            match is not None, f"invalid ticket metadata line {index + 1}: {source}"
        )
        key, value = match.groups()
        require(key not in values, f"duplicate ticket metadata key {key}: {source}")
        values[key] = value
        index += 1

    require(bool(values), f"missing ticket metadata header: {source}")
    return values


def one_metadata_value(text: str, key: str, source: Path) -> str:
    matches = re.findall(rf"^{re.escape(key)}: (.+)$", text, re.MULTILINE)
    require(len(matches) == 1, f"expected one {key} metadata value: {source}")
    return matches[0]


def active_requirement_members(spec_root: Path = SPEC) -> list[Path]:
    members: list[Path] = []
    seen_ids: dict[str, Path] = {}
    requirement_paths = sorted((spec_root / "requirements").glob("REQ-P-*.md"))
    require(
        {path.name for path in requirement_paths} == EXPECTED_REQUIREMENTS,
        "active requirement file inventory differs from the closed expected set",
    )

    for path in requirement_paths:
        text = path.read_text(encoding="utf-8")
        status = one_metadata_value(text, "Status", path)
        category = one_metadata_value(text, "Category", path)
        require(
            status in REQUIREMENT_STATUSES,
            f"invalid requirement status {status}: {path}",
        )
        require(
            category in REQUIREMENT_CATEGORIES,
            f"invalid requirement category {category}: {path}",
        )

        ids = re.findall(r"\*\*(REQ-P-[A-Z]+-\d{3})\*\*", text)
        require(bool(ids), f"no requirement identities: {path}")
        require(len(ids) == len(set(ids)), f"duplicate requirement identity in {path}")
        for requirement_id in ids:
            require(
                requirement_id not in seen_ids,
                f"duplicate requirement identity {requirement_id}: {path} and "
                f"{seen_ids.get(requirement_id)}",
            )
            seen_ids[requirement_id] = path
        if status == "Active":
            members.append(path)
    return members


def what_member_set_identity(
    requirements: list[Path], spec_root: Path = SPEC
) -> tuple[str, list[str]]:
    members = [spec_root / "INTENT.md", spec_root / "PRODUCT.md", *requirements]
    ordered = members[:2] + sorted(
        members[2:], key=lambda path: path.relative_to(spec_root).as_posix()
    )
    identity_input = bytearray()
    paths: list[str] = []
    for path in ordered:
        require(path.is_file(), f"missing WHAT member: {path}")
        relative = path.relative_to(spec_root).as_posix()
        paths.append(relative)
        digest = sha256_bytes(path.read_bytes())
        identity_input.extend(relative.encode("utf-8"))
        identity_input.append(0)
        identity_input.extend(digest.encode("ascii"))
        identity_input.extend(b"\n")
    return sha256_bytes(bytes(identity_input)), paths


def validate_ticket_metadata(values: dict[str, str], path: Path) -> None:
    missing = TICKET_FIELDS - values.keys()
    require(not missing, f"missing ticket metadata {sorted(missing)}: {path}")
    require(values["type"] in TICKET_TYPES, f"invalid ticket type: {path}")
    require(
        values["ticket_category"] in TICKET_CATEGORIES,
        f"invalid ticket category: {path}",
    )
    require(
        values["change_class"] in CHANGE_CLASSES,
        f"invalid ticket change class: {path}",
    )
    lane = path.parent.name
    require(lane in LANE_STATUS, f"invalid ticket lane {lane}: {path}")
    require(
        values["status"] == LANE_STATUS[lane],
        f"ticket status/lane mismatch: {path}",
    )


def check_tickets(root: Path = ROOT) -> tuple[int, dict[str, dict[str, str]]]:
    count = 0
    records: dict[str, dict[str, str]] = {}
    ticket_root = root / ".ai-workspace" / "tickets"
    for path in sorted(ticket_root.glob("*/*.md")):
        if path.name == "README.md":
            continue
        values = parse_ticket_metadata(path.read_text(encoding="utf-8"), str(path))
        validate_ticket_metadata(values, path)
        require(values["id"] not in records, f"duplicate ticket id {values['id']}")
        records[values["id"]] = values
        count += 1
    return count, records


def require_text(text: str, needle: str, source: Path) -> None:
    require(needle in text, f"missing required declaration {needle!r}: {source}")


def check_semantic_compilation_contract(text: str, source: Path) -> None:
    for declaration in (
        "CandidatePayload = {",
        "SemanticCompilationProposal = {",
        "SemanticCompilationCandidate = {",
        "schema_version: 2",
        "source_members: SourceMember[51]",
        "compiler_invocation: CompilerInvocation",
        "candidate_model: ACModel",
        "proposed_record_provenance: RecordProvenanceBinding[]",
        "proposed_evaluated_members: EvaluatedMember[51]",
        "semantic_objects: SemanticObject[]",
        "typed_relations: TypedRelation[]",
        "constraints: Constraint[]",
        "latitudes: Latitude[]",
        "residuals: Residual[]",
        "traversals: Traversal[]",
        "transformations: Transformation[]",
        "judgments: Judgment[]",
        "external_resolutions: ExternalResolution[]",
        "RecordProvenanceBinding = {",
        'provenance_kind: "subject_derived"',
        "CompilerProvenanceBundle = {",
        "members: CompilerProvenanceMember[9]",
        "CandidateStructureResultIdentity =",
        "CandidateStructureEvaluationGrantIdentity =",
        "CandidateStructureEvaluationGrant = {",
        "CandidateStructureResult = {",
        "semantic_compilation_candidate_identity:",
        "semantic_compilation_candidate_sha256: Sha256",
        "candidate_structure_result_identity:",
        "candidate_structure_result_sha256: Sha256",
        "subject_identity: SemanticCompilationCandidateIdentity",
        "subject_sha256: Sha256",
        "proposal_dispositions: ProposalDisposition[]",
        "decided_at: RFC3339 timestamp",
        "evidence_refs: non-empty sorted duplicate-free URI-reference[]",
        "proposed_generated_source_keys: GeneratedSourceKeyBinding[]",
        '"evaluated_member" | "model_record" | "selection" |',
        "provenance_sha256: Sha256",
        "ConstructCandidate(",
        'Every\n`proposal_kind = "model_record"` disposition is exactly',
        "every model record and its `P_B` row are accepted\nunchanged",
    ):
        require_text(text, declaration, source)


def check_functor_application_notation(surfaces: dict[Path, str]) -> None:
    for source, text in surfaces.items():
        require(
            re.search(r"\bF_[DPH]\s*\(", text) is None,
            f"bare F_D(...), F_P(...), or F_H(...) notation bypasses "
            f"functor application: {source}",
        )


def check_carrier_neutral_compiler(product: str, fp_contract: str) -> None:
    require(
        "G_profile" not in product and "G_profile" not in fp_contract,
        "tenant profile leaked into carrier-neutral semantic compilation",
    )


def check_selection_acceptance_topology(
    product: str, selection_contract: str, source: Path
) -> None:
    for declaration in (
        "The ledger is itself the exact `F_H[v_select]` decision",
        "It has no second acceptance record.",
        'subject_kind = "interpreted_model"',
        "J_B.decision = accepted",
    ):
        require(
            declaration in product or declaration in selection_contract,
            f"missing selection/acceptance topology {declaration!r}: {source}",
        )
    require(
        '"semantic_selection_ledger"' not in product,
        f"selection ledger incorrectly requires a second acceptance record: {source}",
    )


def check_carrier_admission_judgment(text: str, source: Path) -> None:
    for declaration in (
        "Encode_T(M_B*, P_B*, Ledger_B, J_B, Profile_T, CarrierBasis_T)\n"
        "  -> G_{B,T}",
        "D_{G,T} =\n  F_D[v_carrier_admission]" "(G_{B,T}, Profile_T, CarrierBasis_T)",
        "-> admitted | refuse",
        "returns only `D_{G,T}`",
        "leaving the evaluated carrier bytes and identity\nunchanged",
    ):
        require_text(text, declaration, source)
    require(
        re.search(
            r"F_D\[v_carrier_admission\]\([^)]*\)\s*->\s*G_\{B,T\}",
            text,
        )
        is None,
        "carrier admission transforms or promotes the carrier instead of "
        f"returning a separate judgment: {source}",
    )


def check_exploratory_quickstart(text: str, source: Path) -> None:
    require_text(
        text,
        "This bare model call is exploratory probabilistic processing.",
        source,
    )
    require_text(
        text,
        "**not** an\nExecutive Context Assignment, Reviewer activation, Context Packet",
        source,
    )


def check_definition(root: Path = ROOT) -> dict[str, Any]:
    definition_path = root / "stdo_representation.json"
    definition = load_json_unique(definition_path)
    require(isinstance(definition, dict), "Product Definition root is not an object")

    require(definition.get("$schema") == STDO_SCHEMA_URI, "unexpected STDO schema")
    constitution = definition.get("constitution")
    require(isinstance(constitution, dict), "constitution is not an object")
    stdo = constitution.get("stdo")
    require(isinstance(stdo, dict), "STDO constitution is not an object")
    require(stdo.get("selector") == STDO_SELECTOR, "unexpected STDO selector")
    require(
        stdo.get("basis")
        == {
            "uri": STDO_BASIS_URI,
            "manifest_sha256": STDO_MANIFEST_SHA256,
        },
        "unexpected immutable STDO basis",
    )
    entrypoints = constitution.get("entrypoints")
    require(isinstance(entrypoints, list), "STDO entrypoints are not an array")
    entrypoint_uris = {
        item.get("uri") for item in entrypoints if isinstance(item, dict)
    }
    require(
        "standards/AXIOMATIC_CALCULUS.md" in entrypoint_uris,
        "Axiomatic Calculus is not an STDO entrypoint",
    )
    require(
        "standards/ODD_METHOD.md" not in entrypoint_uris,
        "ODD Method leaked into the carrier-neutral baseline",
    )

    how = definition.get("how")
    require(isinstance(how, dict), "HOW is not an object")
    require(
        how.get("common") == ["./build_tenants/semantic_compile/"],
        "semantic_compile is not the exact common construction surface",
    )
    tenants = how.get("build_tenants")
    require(isinstance(tenants, list), "build tenants are not an array")
    require(
        {item.get("id") for item in tenants if isinstance(item, dict)}
        == {
            "urn:stdo-representation:build-tenant:gtl",
            "urn:stdo-representation:build-tenant:json-schema",
        },
        "GTL and JSON Schema tenant registry is not exact",
    )

    frame_bases = definition.get("reference_frame_bases")
    require(
        frame_bases == [],
        "an unaccepted Project Reference-Frame Basis occupies the operative overlay",
    )

    local_constitution = definition.get("local_constitution")
    require(isinstance(local_constitution, dict), "local constitution is not an object")
    disambiguations = local_constitution.get("disambiguations")
    require(isinstance(disambiguations, list), "missing local disambiguations")
    require(
        len(disambiguations) == len(EXPECTED_DISAMBIGUATIONS),
        "unexpected semantic disambiguation count",
    )
    observed: dict[str, dict[str, Any]] = {}
    for item in disambiguations:
        require(isinstance(item, dict), "semantic resolution is not an object")
        term = item.get("term")
        require(isinstance(term, str), "invalid semantic resolution term")
        require(term not in observed, f"duplicate semantic resolution for {term}")
        observed[term] = item
    require(
        observed == EXPECTED_DISAMBIGUATIONS,
        "engagement-role disambiguation records are not exact",
    )
    return definition


def main() -> None:
    definition = check_definition()
    required_files = [
        SPEC / "GOALS.md",
        SPEC / "INTENT.md",
        SPEC / "PRODUCT.md",
        SPEC / "REFERENCE_FRAME_BASIS.md",
        *(SPEC / "requirements" / name for name in sorted(EXPECTED_REQUIREMENTS)),
        ROOT / "scripts" / "test_check_constitution.py",
        ROOT / "build_tenants" / "gtl" / "design" / "GTL_AXIOM_INDEX_PROFILE.json",
    ]
    for path in required_files:
        require(path.is_file(), f"missing required file: {path}")

    retired = SPEC / "requirements" / "REQ-P-PROJECTION-AND-CONFORMANCE.md"
    require(
        not retired.exists(),
        "retired deterministic-assessment requirement remains live",
    )
    require(
        (ROOT / "build_tenants" / "semantic_compile").is_dir(),
        "missing common semantic_compile construction surface",
    )

    product_path = SPEC / "PRODUCT.md"
    intent_path = SPEC / "INTENT.md"
    algebra_path = SPEC / "requirements" / "REQ-P-REPRESENTATION-ALGEBRA.md"
    context_path = SPEC / "requirements" / "REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md"
    fp_path = SPEC / "requirements" / "REQ-P-FP-CONSUMPTION.md"
    selection_path = SPEC / "requirements" / "REQ-P-SELECTION-AND-ACCEPTANCE.md"
    frame_path = SPEC / "REFERENCE_FRAME_BASIS.md"
    profile_path = (
        ROOT / "build_tenants" / "gtl" / "design" / "GTL_AXIOM_INDEX_PROFILE.json"
    )

    product = product_path.read_text(encoding="utf-8")
    intent = intent_path.read_text(encoding="utf-8")
    algebra = algebra_path.read_text(encoding="utf-8")
    context_contract = context_path.read_text(encoding="utf-8")
    fp_contract = fp_path.read_text(encoding="utf-8")
    selection_contract = selection_path.read_text(encoding="utf-8")
    frame_basis = frame_path.read_text(encoding="utf-8")
    profile = load_json_unique(profile_path)

    require(isinstance(profile, dict), "GTL axiom-index profile is not an object")
    require(
        profile.get("identity") == GTL_PROFILE_IDENTITY,
        "unexpected active GTL profile identity",
    )
    require(
        profile.get("calculus_basis", {}).get("identity") == CALCULUS_BASIS_IDENTITY,
        "GTL profile does not bind the exact calculus basis",
    )
    require(
        profile.get("source_basis", {}).get("release_uri") == STDO_BASIS_URI,
        "GTL profile does not bind the exact STDO subject",
    )
    profile_tenant = profile.get("build_tenant", {})
    profile_carrier_basis = profile_tenant.get("carrier_basis", {})
    derived_carrier_digest = sha256_bytes(
        canonical_ascii_coordinate_bytes(GTL_CARRIER_COORDINATE)
    )
    require(
        profile_tenant.get("identity") == "urn:stdo-representation:build-tenant:gtl",
        "GTL profile does not bind the selected build tenant",
    )
    require(
        profile_carrier_basis.get("coordinate") == GTL_CARRIER_COORDINATE,
        "GTL profile carrier coordinate differs from the frozen basis",
    )
    require(
        profile_carrier_basis.get("identity")
        == GTL_CARRIER_BASIS_PREFIX + derived_carrier_digest,
        "GTL profile carrier-basis identity is not content-derived",
    )
    require(
        profile.get("canonicalization", {}).get("coordinate_algorithm")
        == "RFC8785_JCS_SHA256",
        "GTL profile does not bind exact coordinate canonicalization",
    )
    require(
        profile.get("publication_contract", {})
        .get("module_publication", {})
        .get("raw_admission_contract_ref")
        == "urn:abiogenesis:contract:gtl:module-publication:5.0.0",
        "GTL profile does not bind the frozen ModulePublication contract",
    )

    require_text(
        product,
        "F_P[v_reason](Index_B, W, I, R, K) -> J_reason",
        product_path,
    )
    require_text(product, "F_K[v](upstream_v) -> result_v", product_path)
    for identity in (CALCULUS_BASIS_IDENTITY, SUBJECT_BASIS_IDENTITY):
        prefix, digest = identity.rsplit(":", 1)
        require_text(algebra, prefix + ":", algebra_path)
        require_text(algebra, digest, algebra_path)
    require_text(product, AXIOMATIC_CALCULUS_SHA256, product_path)
    require_text(product, "M_B* = (b_M, I, O, E, C, L, X, V, T, J)", product_path)
    require_text(
        product,
        "Encode_T(M_B*, P_B*, Ledger_B, J_B, Profile_T, CarrierBasis_T)",
        product_path,
    )
    require_text(algebra, "Population_M = {", algebra_path)
    require_text(algebra, "ModelBasisIdentity =", algebra_path)
    require_text(algebra, 'b_M = "urn:stdo-index:model-basis:sha256:"', algebra_path)
    require_text(algebra, "I = Local_M disjoint_union External_M", algebra_path)
    require_text(algebra, "P_B = RecordProvenanceBinding[]", algebra_path)
    require_text(algebra, "dom(P_B) = Local_M", algebra_path)
    require_text(algebra, 'provenance_kind: "subject_derived"', algebra_path)
    require_text(algebra, "Resolution_M(x) = {", algebra_path)
    require_text(
        algebra,
        "a_c.STDO = (id(a_c.STDO*), M_B*, P_B*, Ledger_B, J_B)",
        algebra_path,
    )
    require_text(context_contract, "ExecutiveContextAssignment = {", context_path)
    require_text(context_contract, "ContextProjectionManifest = {", context_path)
    require_text(
        context_contract,
        "Index_A = project(Index_B, Z(A), L_context)",
        context_path,
    )
    require_text(context_contract, "P_A = P_B restricted to Local_{M_A}", context_path)
    require_text(
        context_contract, "stdo://releases/v2.5.0-rc.1/standards/", context_path
    )
    for role in ("executive", "worker", "reviewer"):
        require_text(
            context_contract,
            f"STDO_REFERENCE_FRAME_BASELINE.md#{role}",
            context_path,
        )
    check_semantic_compilation_contract(selection_contract, selection_path)
    check_selection_acceptance_topology(product, selection_contract, product_path)
    require_text(selection_contract, "GeneratedSourceKeyBinding = {", selection_path)
    require_text(
        selection_contract,
        "candidate_model_content_identity: Sha256",
        selection_path,
    )
    require_text(product, "admitting_authority_refs", product_path)
    require_text(product, "ReleaseRecord = {", product_path)
    require_text(frame_basis, "Status: acceptance-controlled", frame_path)
    require_text(frame_basis, FRAME_BASIS_IDENTITY, frame_path)
    require_text(frame_basis, STDO_MEMBER_SET_SHA256, frame_path)
    require_text(frame_basis, AXIOMATIC_CALCULUS_SHA256, frame_path)
    require_text(
        frame_basis,
        "urn:stdo-representation:frame:semantic-compilation",
        frame_path,
    )
    require_text(frame_basis, "`E-COMPILATION`", frame_path)
    for declaration in (
        "F_i^7 = <Q_i, B_7, M_i, C_7, I_i, A_i, E_i, X_i, R_7, J_i, K_i, D_i>",
        "Every activation binds the exact role envelope",
        "### Generic specialist-family disposition",
        "### Testing-frame acquisition",
    ):
        require_text(frame_basis, declaration, frame_path)
    require_text(intent, "STDO Symbolic Axiomatic Program", intent_path)
    require_text(intent, "Programmatic Semantic Index", intent_path)
    require_text(product, "STDO Symbolic Axiomatic Program", product_path)
    require_text(product, "STDO Programmatic Semantic Index Product", product_path)
    require_text(product, "S_B = (B_STDO, Members_B, Bytes_B)", product_path)
    require_text(product, "F_P[v_compile]", product_path)
    require_text(product, "Encode_T", product_path)
    require_text(product, "Reliability here is structural", product_path)
    require_text(product, "not a frozen-GTL `GtlProgram`", product_path)
    require_text(product, "vector database", product_path)
    require_text(
        product,
        "Unaccepted proposal and\nstructural-evaluation evidence may exist",
        product_path,
    )
    require_text(
        frame_basis,
        "remains proposed and T-003 remains non-executable",
        frame_path,
    )
    check_functor_application_notation(
        {
            product_path: product,
            intent_path: intent,
            algebra_path: algebra,
            context_path: context_contract,
            fp_path: fp_contract,
            selection_path: selection_contract,
            frame_path: frame_basis,
        }
    )
    check_carrier_neutral_compiler(product, fp_contract)
    check_carrier_admission_judgment(product, product_path)
    require(
        "token-minimal" not in product and "token-minimal" not in context_contract,
        "least lawful record closure is still misrepresented as token minimality",
    )
    for value in (
        PRODUCT_OWNER_ACTOR,
        PRODUCT_OWNER_AUTHORITY,
        PRODUCT_OWNER_GRANT,
        PRODUCT_OWNER_GRANT_SCOPE,
    ):
        require_text(product, value, product_path)
    require("Assessment Disposition" not in product, "assessment Product term returned")
    require(
        "REQ-P-CONF"
        not in "\n".join(path.read_text(encoding="utf-8") for path in required_files),
        "retired assessment requirement identity returned",
    )

    for identity in TRAVERSAL_IDENTITIES.values():
        require_text(product, identity, product_path)
        require_text(fp_contract, identity, fp_path)

    requirements = active_requirement_members()
    what_digest, what_members = what_member_set_identity(requirements)
    ticket_count, tickets = check_tickets()
    require(
        "T-002" in tickets and "T-003" in tickets,
        "required T-002/T-003 records missing",
    )
    require(tickets["T-002"]["status"] == "completed", "T-002 must be completed")
    require(tickets["T-003"]["status"] == "active", "T-003 must be active")

    what_identity = f"sha256:{what_digest}"
    frame_digest = f"sha256:{sha256_bytes(frame_path.read_bytes())}"
    profile_digest = f"sha256:{sha256_bytes(profile_path.read_bytes())}"
    expected_ticket_bindings = {
        "T-002": {
            "candidate_what_member_set_identity": T002_ACCEPTED_WHAT_MEMBER_SET_IDENTITY,
            "candidate_frame_basis_identity": T002_ACCEPTED_FRAME_BASIS_IDENTITY,
            "candidate_frame_basis_sha256": T002_ACCEPTED_FRAME_BASIS_SHA256,
            "candidate_gtl_profile_identity": T002_ACCEPTED_GTL_PROFILE_IDENTITY,
            "candidate_gtl_profile_sha256": T002_ACCEPTED_GTL_PROFILE_SHA256,
        },
        "T-003": {
            "required_what_member_set_identity": what_identity,
            "required_frame_basis_identity": FRAME_BASIS_IDENTITY,
            "required_frame_basis_sha256": frame_digest,
            "required_profile_identity": GTL_PROFILE_IDENTITY,
            "required_profile_sha256": profile_digest,
        },
    }
    for ticket_id, expected in expected_ticket_bindings.items():
        for key, value in expected.items():
            require(
                tickets[ticket_id].get(key) == value,
                f"{ticket_id} {key} does not bind its exact declared subject",
            )

    print(
        json.dumps(
            {
                "check_scope": (
                    "source-project structure, metadata, identity inputs, and "
                    "declared traversal boundaries; semantic adequacy and human "
                    "acceptance are not evaluated"
                ),
                "definition_id": definition["product"]["definition_id"],
                "requirement_members": len(requirements),
                "ticket_records": ticket_count,
                "what_member_set_identity": what_identity,
                "what_members": what_members,
                "stdo_basis_uri": STDO_BASIS_URI,
                "stdo_manifest_sha256": STDO_MANIFEST_SHA256,
                "stdo_member_count": STDO_MEMBER_COUNT,
                "stdo_member_set_sha256": STDO_MEMBER_SET_SHA256,
                "calculus_basis_identity": CALCULUS_BASIS_IDENTITY,
                "subject_basis_identity": SUBJECT_BASIS_IDENTITY,
                "frame_basis_sha256": frame_digest,
                "frame_basis_status": "proposed; acceptance remains open",
                "gtl_profile_identity": GTL_PROFILE_IDENTITY,
                "gtl_profile_sha256": profile_digest,
                "current_model_status": "no accepted current a_c.STDO",
                "current_carrier_status": "no current a_c.STDO.GTL artifact claimed",
                "downstream_reentry_required": [
                    "T-003",
                    "GTL representation profile",
                    "README.md",
                    "QUICKSTART.md",
                ],
                "context_projection_contract": "Executive, Worker, Reviewer",
                "structural_checks_pass": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    try:
        main()
    except CheckFailure as exc:
        print(f"constitution check failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from None
