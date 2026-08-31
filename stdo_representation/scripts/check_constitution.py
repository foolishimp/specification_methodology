#!/usr/bin/env python3
"""Focused constitutional checks for the thin STDO Representation Product."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPRESENTATION_VERSION = "2.5.0"
STDO_BASIS = "stdo://releases/v2.5.0-rc.2/"
STDO_MANIFEST = "313e23116623a3bfbe96d279e089489aac466584982e1c34171ef244f0ec680a"
STDO_MEMBER_SET = "a5910bc56b491b5c520910e7bdad0949c1283e8b71951f1079e1fd86f59d20e7"
CALCULUS_REF = "stdo://releases/v2.5.0-rc.2/standards/AXIOMATIC_CALCULUS.md"
AXIOM_TAG_OBJECT = "e7afc8a42a7123aebe91cb7582cb037b1aae612d"
AXIOM_COMMIT = "dc3e00998da36dae6ac7b76b340431a85096c83c"
AXIOM_TREE = "8c9ad5f5e99a60c18fb8c1802471753afb226272"
FRAME_URI = "urn:stdo-representation:reference-frame-basis:source-project:14"
FRAME_PATH = Path("specification/REFERENCE_FRAME_BASIS.md")
FRAME_SHA256 = "6cc05636ea00797e44f6ebb661d342d5b8cfb59cbde2a81059062dddf6eb106f"
FRAME_DECISION_PATH = Path(
    ".ai-workspace/decisions/20260901T074151_frame_basis_rev14_acceptance.json"
)
FRAME_DECISION_SHA256 = (
    "68394d5118a6250972aa06db995a5d020c2f09996c90b0dfe70d4d8e908e8eba"
)
FRAME_STATUS = "accepted_and_bound"
HISTORICAL_BOOTSTRAP_VERSION = "0.1.0"
HISTORICAL_BOOTSTRAP_RELEASE_PATH = Path("releases/v0.1.0.md")
HISTORICAL_BOOTSTRAP_RELEASE_SHA256 = (
    "7d7e0c78fa5fe893ae530df0069d7f18ecf69144a845f8f782d3c842fe50f876"
)
CANDIDATE_RELEASE_PATH = Path("releases/v2.5.0.md")
CANDIDATE_INVENTORY_SHA256 = (
    "a4a798b8206738c1dc966cf240590b6664472a57f928e0a9b4868b733f849c3d"
)
CANDIDATE_RELEASE_FIELDS = {
    "represented STDO version": "2.5.0",
    "represented exact cut": "refs/tags/specification_methodology/v2.5.0-rc.2",
    "Representation version": "2.5.0",
    "accepted Representation release": ("refs/tags/stdo_representation/v2.5.0-rc.1"),
    "Representation candidate ref pattern": (
        "refs/tags/stdo_representation/v2.5.0-rc.<n>"
    ),
    "version-line selector": "refs/tags/stdo_representation/v2.5.0",
    "RC branch": "refs/heads/rc/stdo_representation/2.5.0",
    "release branch": "refs/heads/release/stdo_representation/2.5.0",
}
CANDIDATE_RELEASE_CLAIMS = (
    "`STDO-REP-2.5-C01`: the Product version equals represented STDO semantic "
    "version `2.5.0` while every Product and RC identity remains distinct.",
    "`STDO-REP-2.5-C02`: the Product carries one canonical source-linked "
    "`a_c.STDO` semantic compression for exact Source STDO `v2.5.0-rc.2`.",
    "`STDO-REP-2.5-C03`: the logical constraint index deterministically binds "
    "the unchanged compression and exposes source re-entry for every indexed "
    "item.",
    "`STDO-REP-2.5-C04`: the explicit Axiom Indexer Product dependency relation "
    "binds exact `v0.1.0-rc.1` mechanics without mutable-sibling substitution.",
    "`STDO-REP-2.5-C05`: one concise native skill lets Codex and Claude select "
    "visible reference frames, retain open solution space, join exact ordered "
    "sections, and re-enter Source STDO without treating the index as truth or "
    "authority.",
)
CANDIDATE_RELEASE_CLAIM_IDS = tuple(
    f"STDO-REP-2.5-C{ordinal:02d}" for ordinal in range(1, 6)
)
CANDIDATE_PREDECESSOR_DISPOSITIONS = (
    "`STDO-REP-2.5-C01`: **conserved**",
    "`STDO-REP-2.5-C02`: **superseded**",
    "`STDO-REP-2.5-C03`: **conserved**",
    "`STDO-REP-2.5-C04`: **conserved**",
    "`STDO-REP-2.5-C05`: **conserved**",
)
CANDIDATE_LAYER_CLAIMS = (
    "published Source STDO v2.5.0-rc.2 prose",
    "a_c.STDO 2.5.0 Axiomatic Program",
    "canonical semantic compression",
    "Axiom Indexer Logical Constraint Map",
    "deterministic index over the unchanged compression",
    "native frame selection and bounded source re-entry",
    "caller-authored ordered sections with ACTION last",
    "Source STDO remains semantic authority.",
    "The map is an index and read model, not a semantic decision.",
    "it is not a prompt engine, schema, renderer, or automatic selector.",
)

SEMANTIC_VERSION_PATTERN = re.compile(
    r"^(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)$"
)
STDO_RELEASE_URI_PATTERN = re.compile(
    r"^stdo://releases/v"
    r"(?P<version>(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\."
    r"(?:0|[1-9][0-9]*))"
    r"-rc\.(?:[1-9][0-9]*)/$"
)
CANDIDATE_MEMBER_ROW_PATTERN = re.compile(
    r"^\| (?P<type>file|symlink) \| `(?P<path>[^`]+)`"
    r"(?: -> `(?P<target>[^`]+)`)? \| `(?P<sha256>[0-9a-f]{64})` \|$"
)

COMPRESSION_PATH = Path(
    "build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.2/"
    "axiomatic-program.json"
)
INDEX_PATH = COMPRESSION_PATH.with_name("logical-constraint-map.json")
# Backward-compatible names for callers that use the Axiom Indexer artifact terms.
PROGRAM_PATH = COMPRESSION_PATH
MAP_PATH = INDEX_PATH
SKILL_ROOT = Path("skills/stdo-representation")
PRODUCT_FILES = (
    COMPRESSION_PATH,
    INDEX_PATH,
    SKILL_ROOT / "SKILL.md",
    SKILL_ROOT / "agents/openai.yaml",
    SKILL_ROOT / "references/codex.md",
    SKILL_ROOT / "references/claude.md",
)
PRODUCT_LINKS = {
    Path(".agents/skills/stdo-representation"): "../../skills/stdo-representation",
    Path(".claude/skills/stdo-representation"): "../../skills/stdo-representation",
}
ACTIVE_REQUIREMENTS = {
    "README.md",
    "REQ-P-BASIS-AND-IDENTITY.md",
    "REQ-P-CANDIDATE-VALIDATION.md",
    "REQ-P-DOGFOOD-VERIFICATION.md",
    "REQ-P-NATIVE-FRAME-USE.md",
    "REQ-P-STDO-AUTHORING-MAP.md",
}
HISTORICAL_ROOTS = (
    Path("build_tenants/semantic_compile"),
    Path("build_tenants/gtl"),
    Path("build_tenants/json_schema"),
)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def derive_represented_stdo_semver(release_uri: str) -> str:
    """Return the represented STDO semantic version from one exact RC URI."""

    if not isinstance(release_uri, str):
        raise ValueError("Source STDO release URI is not a string")
    match = STDO_RELEASE_URI_PATTERN.fullmatch(release_uri)
    if match is None:
        raise ValueError("Source STDO basis is not an exact RC release URI")
    return match.group("version")


def validate_representation_version(
    representation_version: str, represented_release_uri: Any
) -> list[str]:
    """Check that Representation inherits the represented STDO semantic version."""

    failures: list[str] = []
    if not isinstance(
        representation_version, str
    ) or not SEMANTIC_VERSION_PATTERN.fullmatch(representation_version):
        failures.append("Representation version is not a semantic version")

    try:
        represented_version = derive_represented_stdo_semver(represented_release_uri)
    except ValueError:
        failures.append(
            "Source STDO basis does not encode an exact RC semantic version"
        )
        return failures

    if representation_version != represented_version:
        failures.append(
            "Representation version does not match represented STDO semantic version"
        )
    return failures


def validate_overlay(overlay: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    basis = overlay.get("constitution", {}).get("stdo", {}).get("basis", {})
    basis_uri = basis.get("uri")
    if basis_uri != STDO_BASIS:
        failures.append("Product Definition selects the wrong STDO basis")
    failures.extend(validate_representation_version(REPRESENTATION_VERSION, basis_uri))
    if basis.get("manifest_sha256") != STDO_MANIFEST:
        failures.append("Product Definition selects the wrong STDO manifest")
    if overlay.get("constitution", {}).get("additional_authorities") != []:
        failures.append("unexpected additional constitutional authority")

    expected_entrypoints = [
        "standards/authority_compressions/stdo_bootstrap.md",
        "standards/SPEC_METHOD.md",
        "standards/REFERENCE_FRAME_METHOD.md",
        "standards/STDO_REFERENCE_FRAME_BASELINE.md",
        "standards/AXIOMATIC_CALCULUS.md",
        "standards/IDENTITY_METHOD.md",
        "standards/RELEASE_METHOD.md",
    ]
    actual_entrypoints = [
        row.get("uri") for row in overlay.get("constitution", {}).get("entrypoints", [])
    ]
    if actual_entrypoints != expected_entrypoints:
        failures.append("constitutional entrypoints do not match the thin Product")

    expected_frame_bases = [
        {
            "uri": "./specification/REFERENCE_FRAME_BASIS.md#project-frame-basis",
            "authority": [
                "./specification/PRODUCT.md#product-disposition-authority",
                "./.ai-workspace/decisions/"
                "20260901T074151_frame_basis_rev14_acceptance.json",
            ],
            "applies_to": ["urn:stdo:product-definition:stdo-representation"],
        }
    ]
    if overlay.get("reference_frame_bases") != expected_frame_bases:
        failures.append("accepted project frame basis binding is not exact")
    expected_composition = [
        {
            "product_definition": "../axiom_indexer/stdo_default.json",
            "target_definition_id": "urn:stdo:product-definition:axiom-indexer",
            "relation": (
                "./specification/PRODUCT.md"
                "#axiom-indexer-product-dependency-relation"
            ),
            "contracts": [
                "./specification/PRODUCT.md#exact-dependency-bases",
                "./specification/requirements/REQ-P-CANDIDATE-VALIDATION.md"
                "#imported-validation-boundary",
                "./specification/requirements/REQ-P-NATIVE-FRAME-USE.md"
                "#frame-use-relation",
            ],
        }
    ]
    if overlay.get("composition") != expected_composition:
        failures.append("Axiom Indexer Product dependency composition is not exact")

    how = overlay.get("how", {})
    if how.get("common") != []:
        failures.append("thin Product unexpectedly selects common implementation")
    tenants = how.get("build_tenants")
    if not isinstance(tenants, list) or len(tenants) != 1:
        failures.append("thin Product must select exactly one build tenant")
    elif tenants[0] != {
        "id": "urn:stdo-representation:build-tenant:axiom-indexer",
        "root": "./build_tenants/axiom_indexer/",
        "design": ["./build_tenants/axiom_indexer/README.md"],
        "implementation": ["./build_tenants/axiom_indexer/representation/"],
    }:
        failures.append("active build tenant is not the thin Axiom Indexer tenant")

    role_uri = "./specification/requirements/REQ-P-NATIVE-FRAME-USE.md#role-bindings"
    roles = overlay.get("local_constitution", {}).get("disambiguations", [])
    if [row.get("term") for row in roles] != ["Executive", "Worker", "Reviewer"]:
        failures.append("role disambiguation population is wrong")
    if any(row.get("uri") != role_uri for row in roles):
        failures.append("role disambiguation does not route to native frame use")

    expected_axioms = [
        {
            "uri": "./specification/PRODUCT.md#shared-source-release-profile",
            "authority": ["./specification/PRODUCT.md#product-disposition-authority"],
            "applies_to": ["urn:stdo:product-definition:stdo-representation"],
        }
    ]
    if overlay.get("local_constitution", {}).get("axioms") != expected_axioms:
        failures.append("Product-local shared-source release profile is not exact")
    return failures


def validate_frame_basis(root: Path) -> list[str]:
    failures: list[str] = []
    frame_bytes = (root / FRAME_PATH).read_bytes()
    if hashlib.sha256(frame_bytes).hexdigest() != FRAME_SHA256:
        failures.append("proposed project frame basis bytes changed")
        return failures

    frame_text = frame_bytes.decode("utf-8")
    if FRAME_URI not in frame_text:
        failures.append("proposed project frame basis has the wrong identity")
    expected_status = (
        "Status: proposed source-project basis, revision 14; Product-owner "
        "acceptance\nand overlay binding are pending."
    )
    if expected_status not in frame_text:
        failures.append("project frame basis has the wrong proposed status")

    decision_path = root / FRAME_DECISION_PATH
    decision_bytes = decision_path.read_bytes()
    if hashlib.sha256(decision_bytes).hexdigest() != FRAME_DECISION_SHA256:
        failures.append("project frame-basis acceptance record bytes changed")
        return failures

    decision = json.loads(decision_bytes)
    expected = {
        "subject_uri": FRAME_URI,
        "subject_ref": "./specification/REFERENCE_FRAME_BASIS.md#project-frame-basis",
        "subject_sha256": "sha256:" + FRAME_SHA256,
        "actor_identity": "https://github.com/foolishimp",
        "authority_identity": "urn:stdo-representation:authority:product-owner",
        "decision": "accepted",
    }
    for key, value in expected.items():
        if decision.get(key) != value:
            failures.append(f"project frame-basis acceptance has wrong {key}")
    return failures


def validate_semantic_boundaries(compression: dict[str, Any]) -> list[str]:
    """Protect the recursive Product identities encoded by the compression."""

    failures: list[str] = []
    symbols = {
        row.get("uri"): row
        for row in compression.get("symbols", [])
        if isinstance(row, dict) and isinstance(row.get("uri"), str)
    }
    clauses = {
        row.get("uri"): row
        for row in compression.get("clauses", [])
        if isinstance(row, dict) and isinstance(row.get("uri"), str)
    }
    install_uri = "urn:stdo-representation:a-c-text:symbol:install"
    release_cut_uri = "urn:stdo-representation:a-c-text:symbol:release-cut"
    obsolete_uri = "urn:stdo-representation:a-c-text:symbol:installed-release"
    if obsolete_uri in symbols:
        failures.append(
            "Product compression retains collapsed installed-release identity"
        )
    if (
        symbols.get(install_uri, {}).get("label")
        != "Verified installed Product instance"
    ):
        failures.append("Product compression does not declare the Install identity")
    if symbols.get(release_cut_uri, {}).get("label") != "Immutable RC release cut":
        failures.append("Product compression does not declare the Release Cut identity")

    product_definition_clause = clauses.get(
        "urn:stdo-representation:a-c-text:clause:"
        "product-definition-schema-closes-routing-shape",
        {},
    )
    expected_product_definition_statement = (
        "A Product Definition structurally binds one Product-Definition identity for "
        "a continuing mutable WHAT line, exact STDO basis, local constitutional "
        "relations, reference-frame bases, WHAT, HOW, work carriers, and composition "
        "under a closed schema; it is not immutable Product identity."
    )
    if (
        product_definition_clause.get("statement")
        != expected_product_definition_statement
    ):
        failures.append(
            "Product compression collapses Product-Definition and Product identity"
        )

    manifest_clause = clauses.get(
        "urn:stdo-representation:a-c-text:clause:"
        "manifest-schema-closes-release-shape",
        {},
    )
    release_clause = clauses.get(
        "urn:stdo-representation:a-c-text:clause:release-rc-is-immutable", {}
    )
    manifest_arguments = manifest_clause.get("arguments", [])
    release_arguments = release_clause.get("arguments", [])
    if not manifest_arguments or manifest_arguments[0].get("ref") != install_uri:
        failures.append("Product compression does not bind the manifest to Install")
    if not release_arguments or release_arguments[0].get("ref") != release_cut_uri:
        failures.append(
            "Product compression does not bind RC publication to Release Cut"
        )
    return failures


def validate_compression_index(
    compression: dict[str, Any], logical_index: dict[str, Any]
) -> list[str]:
    """Validate the Axiom program as compression and its map as the bound index."""

    failures = validate_semantic_boundaries(compression)
    if compression.get("kind") != "axiom-indexer.axiomatic-program":
        failures.append("Product compression has the wrong Axiom program kind")
    if logical_index.get("kind") != "axiom-indexer.logical-constraint-map":
        failures.append("Product index has the wrong Axiom logical-map kind")
    if compression.get("calculus_ref") != CALCULUS_REF:
        failures.append("Product compression selects the wrong calculus")
    expected_source = STDO_BASIS + "standards/"
    if compression.get("source_basis") != expected_source:
        failures.append("Product compression selects the wrong source basis")
    if logical_index.get("source_basis") != expected_source:
        failures.append("Product index selects the wrong source basis")
    if logical_index.get("calculus_ref") != compression.get("calculus_ref"):
        failures.append("Product index changes the compression calculus")
    if logical_index.get("program_uri") != compression.get("uri"):
        failures.append("Product index does not bind the Product compression URI")
    compression_digest = "sha256:" + canonical_sha256(compression)
    if logical_index.get("program_sha256") != compression_digest:
        failures.append("Product index does not bind the canonical Product compression")
    if logical_index.get("frame_refs") != compression.get("frame_refs"):
        failures.append("Product index changes the compression frame references")
    if logical_index.get("vocabulary_refs") != compression.get("vocabulary_refs"):
        failures.append("Product index changes the compression vocabulary references")

    compression_item_uris: set[str] = set()
    index_item_uris: set[str] = set()
    for name in ("symbols", "clauses", "residuals"):
        compression_value = compression.get(name)
        index_value = logical_index.get(name)
        if not isinstance(compression_value, list):
            failures.append(f"Product compression {name} is not an array")
            continue
        compression_uris = [
            row.get("uri")
            for row in compression_value
            if isinstance(row, dict) and isinstance(row.get("uri"), str)
        ]
        if len(compression_uris) != len(compression_value):
            failures.append(f"Product compression {name} contains an invalid URI row")
        compression_item_uris.update(compression_uris)

        if isinstance(index_value, dict):
            index_uris = list(index_value)
        elif isinstance(index_value, list):
            index_uris = [
                row.get("uri")
                for row in index_value
                if isinstance(row, dict) and isinstance(row.get("uri"), str)
            ]
            if len(index_uris) != len(index_value):
                failures.append(f"Product index {name} contains an invalid URI row")
        else:
            index_uris = []
            failures.append(f"Product index {name} has the wrong shape")
        index_item_uris.update(index_uris)

        if index_uris != compression_uris:
            failures.append(f"Product index changes the compression {name} identities")

    source_routes = logical_index.get("source_routes")
    if isinstance(source_routes, dict):
        source_route_uris = set(source_routes)
    else:
        source_route_uris = set()
        failures.append("Product index source routes have the wrong shape")
    if source_route_uris != compression_item_uris:
        failures.append(
            "Product index source routes are not total over compression items"
        )
    if source_route_uris != index_item_uris:
        failures.append("Product index source routes do not match index items")
    index_digest = logical_index.get("map_sha256")
    if not isinstance(index_digest, str) or not index_digest.startswith("sha256:"):
        failures.append("Product index has no intrinsic digest")
    return failures


def validate_program_map(
    program: dict[str, Any], logical_map: dict[str, Any]
) -> list[str]:
    """Compatibility alias for the explicit compression-to-index validation."""

    return validate_compression_index(program, logical_map)


def validate_rc2_projection(
    compression: dict[str, Any], logical_index: dict[str, Any]
) -> list[str]:
    """Require the released RC2 frame and source-routing semantics."""

    failures: list[str] = []
    expected_frame_refs = [
        "stdo://releases/v2.5.0-rc.2/standards/"
        "REFERENCE_FRAME_METHOD.md#reference-frame-laws",
        "stdo://releases/v2.5.0-rc.2/standards/"
        "STDO_REFERENCE_FRAME_BASELINE.md#derived-executive-frame",
        "stdo://releases/v2.5.0-rc.2/standards/"
        "STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame",
        "stdo://releases/v2.5.0-rc.2/standards/"
        "STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame",
    ]
    if compression.get("frame_refs") != expected_frame_refs:
        failures.append("Product compression has the wrong RC2 frame references")

    encoded = json.dumps(
        {"compression": compression, "index": logical_index},
        ensure_ascii=False,
        sort_keys=True,
    )
    if "repo://" in encoded:
        failures.append("RC2 Product artifacts retain mutable candidate routes")
    if "stdo://releases/v2.5.0-rc.1/" in encoded:
        failures.append("RC2 Product artifacts retain RC1 Source STDO routes")

    required_clauses = {
        "engagement-return-topology": (
            "Executive locks the outcome and basis, selects the smallest "
            "dependency-ready evaluation frontier, consumes closed Worker, Reviewer, "
            "and specialist results, and alone assigns priority, current-boundary "
            "effect, disposition, and the next authorized action; Reviewer returns "
            "evidence-bound severity and technical triage without repair, priority, "
            "blocking, or continuation authority."
        ),
        "executive-promotion-constraints": (
            "Executive blocks a valid mandatory-claim falsification governed by a "
            "non-waivable hard stop regardless of priority, does not mechanically "
            "block a below-cutoff finding without a hard stop, returns an out-of-claim "
            "observation for bounded repricing or re-entry rather than claim-relative "
            "blocking, and reactivates or retains indeterminate any unsupported "
            "technical assessment instead of rewriting Reviewer evidence."
        ),
        "profile-qualification-separates-mechanical-and-semantic-evidence": (
            "Mechanical document checks may protect exact table shape, result "
            "cardinality, source-digest congruence, and named refusal boundaries, but "
            "remain structural evidence only; semantic truth and profile qualification "
            "require a capable source-linked Reviewer evaluation, and qualification "
            "binds both evidence kinds without claiming either as the other."
        ),
        "reference-frame-preserves-open-realization": (
            "Do not turn a finite substrate-neutral evaluation context into a prompt "
            "engine, universal carrier, controller, or solution plan: include the "
            "relations material to its declared evaluation and leave realization "
            "choices not owned by those relations with their governing Product, "
            "design, and authorized actor."
        ),
        "reviewer-result-triage-is-total": (
            "Reviewer projection is total across the Reference Frame Method result "
            "algebra: satisfied carries an explicit no-finding state and not-applicable "
            "triage; falsified carries exact findings with complete or explicitly "
            "indeterminate triage fields; indeterminate preserves evidence gaps; "
            "out_of_frame means the evaluated claim requires an undeclared material "
            "relation or evaluator capability and carries indeterminate triage plus "
            "reconfiguration pressure; invalid_basis carries basis failure and refuses "
            "consumption."
        ),
    }
    actual_clauses = {
        row.get("uri", "").rsplit(":", 1)[-1]: row.get("statement")
        for row in compression.get("clauses", [])
        if isinstance(row, dict)
    }
    for clause, expected_statement in required_clauses.items():
        if actual_clauses.get(clause) != expected_statement:
            failures.append(f"RC2 Product compression changes frame clause: {clause}")
    return failures


def validate_native_layout(root: Path) -> list[str]:
    """Check the lean caller-authored projection without creating an engine."""

    failures: list[str] = []
    skill_text = (root / SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    required_skill_claims = (
        "Reviewer evaluates the exact subject and evidence without repair",
        "Executive alone consumes the complete Product view",
        "open solution space",
        "`ACTION` last",
        "not a prompt engine, schema, selector, or renderer",
    )
    for claim in required_skill_claims:
        if claim not in skill_text:
            failures.append(f"native skill lacks RC2 projection claim: {claim}")

    layouts = {
        "codex": (
            root / SKILL_ROOT / "references/codex.md",
            (
                "1. `Role and outcome`",
                "2. `Reference frame and exact subject`",
                "3. `Hard constraints`",
                "4. `Index context and evidence routes`",
                "5. `Open solution space`",
                "6. `Return and stop contract`",
                "7. `ACTION`",
            ),
        ),
        "claude": (
            root / SKILL_ROOT / "references/claude.md",
            (
                "1. `<role_and_outcome>`",
                "2. `<reference_frame_and_exact_subject>`",
                "3. `<hard_constraints>`",
                "4. `<index_context_and_evidence_routes>`",
                "5. `<open_solution_space>`",
                "6. `<return_and_stop_contract>`",
                "7. `<ACTION>`",
            ),
        ),
    }
    for target, (path, markers) in layouts.items():
        text = path.read_text(encoding="utf-8")
        normalized_text = " ".join(text.split())
        positions = [text.find(marker) for marker in markers]
        if any(position < 0 for position in positions) or positions != sorted(
            positions
        ):
            failures.append(f"{target} layout does not preserve the seven-part order")
        if "not a prompt engine, schema, selector, or renderer" not in normalized_text:
            failures.append(f"{target} layout loses the no-prompt-engine boundary")
    return failures


def validate_historical_bootstrap(root: Path) -> list[str]:
    """Protect the immutable 0.1.0 bootstrap release record in the live tree."""

    path = root / HISTORICAL_BOOTSTRAP_RELEASE_PATH
    if not path.is_file():
        return ["missing historical STDO Representation 0.1.0 release record"]
    if (
        hashlib.sha256(path.read_bytes()).hexdigest()
        != HISTORICAL_BOOTSTRAP_RELEASE_SHA256
    ):
        return ["historical STDO Representation 0.1.0 release record changed"]
    return []


def compute_product_inventory(
    root: Path,
) -> tuple[list[dict[str, str]], list[str]]:
    """Digest the eight Product members under the release inventory law."""

    inventory: list[dict[str, str]] = []
    failures: list[str] = []
    for path in PRODUCT_FILES:
        full_path = root / path
        if not full_path.is_file() or full_path.is_symlink():
            failures.append(f"missing regular Product member for release: {path}")
            continue
        inventory.append(
            {
                "path": path.as_posix(),
                "type": "file",
                "sha256": hashlib.sha256(full_path.read_bytes()).hexdigest(),
            }
        )

    for path, expected_target in PRODUCT_LINKS.items():
        full_path = root / path
        if not full_path.is_symlink():
            failures.append(f"missing symlink Product member for release: {path}")
            continue
        actual_target = full_path.readlink().as_posix()
        if actual_target != expected_target:
            failures.append(f"wrong Product symlink target for release: {path}")
        inventory.append(
            {
                "path": path.as_posix(),
                "type": "symlink",
                "target": actual_target,
                "sha256": hashlib.sha256(actual_target.encode("utf-8")).hexdigest(),
            }
        )

    inventory.sort(key=lambda row: row["path"])
    return inventory, failures


def canonical_inventory_bytes(inventory: list[dict[str, str]]) -> bytes:
    """Encode sorted Product rows exactly as the release record declares."""

    rows = sorted(inventory, key=lambda row: row["path"])
    return "".join(
        f'{row["sha256"]}  {row["type"]}  {row["path"]}\n' for row in rows
    ).encode("utf-8")


def parse_candidate_inventory(record_text: str) -> list[dict[str, str]]:
    """Read the Product member table from the candidate release record."""

    inventory: list[dict[str, str]] = []
    for line in record_text.splitlines():
        match = CANDIDATE_MEMBER_ROW_PATTERN.fullmatch(line)
        if match is None:
            continue
        row = {
            "path": match.group("path"),
            "type": match.group("type"),
            "sha256": match.group("sha256"),
        }
        target = match.group("target")
        if target is not None:
            row["target"] = target
        inventory.append(row)
    inventory.sort(key=lambda row: row["path"])
    return inventory


def validate_candidate_release(root: Path) -> list[str]:
    """Bind the 2.5.0 candidate record to its exact live Product subject."""

    failures: list[str] = []
    release_path = root / CANDIDATE_RELEASE_PATH
    if not release_path.is_file():
        return ["missing STDO Representation 2.5.0 candidate release record"]

    record_text = release_path.read_text(encoding="utf-8")
    normalized_record = " ".join(record_text.split())
    if not record_text.startswith("# STDO Representation 2.5.0\n"):
        failures.append("candidate release record has the wrong Product version")
    expected_status = (
        "Status: frozen RC2-basis source candidate; no new immutable STDO "
        "Representation RC is published or accepted by this record."
    )
    if expected_status not in normalized_record:
        failures.append("candidate release record has the wrong candidate status")
    for field, expected_value in CANDIDATE_RELEASE_FIELDS.items():
        field_matches = re.findall(
            rf"^{re.escape(field)}: ([^\n]+)$", record_text, flags=re.MULTILINE
        )
        if field_matches != [expected_value]:
            failures.append(f"candidate release record has the wrong {field}")
    layer_section = record_text.partition("## Layer relation")[2].partition(
        "## Candidate claims"
    )[0]
    normalized_layer_section = " ".join(layer_section.split())
    claims_section = record_text.partition("## Candidate claims")[2].partition(
        "The accepted RC1 claims"
    )[0]
    normalized_claims_section = " ".join(claims_section.split())
    dispositions_section = record_text.partition("The accepted RC1 claims")[
        2
    ].partition("## Exact bases")[0]
    actual_claim_ids = tuple(
        re.findall(
            r"^- `(STDO-REP-2\.5-C[0-9]{2})`:",
            claims_section,
            flags=re.MULTILINE,
        )
    )
    if actual_claim_ids != CANDIDATE_RELEASE_CLAIM_IDS:
        failures.append("candidate release record has the wrong 2.5 claim population")
    for claim in CANDIDATE_RELEASE_CLAIMS:
        if claim not in normalized_claims_section:
            failures.append(f"candidate release record lacks exact claim: {claim[:22]}")
    for disposition in CANDIDATE_PREDECESSOR_DISPOSITIONS:
        if disposition not in dispositions_section:
            failures.append(
                "candidate release lacks exact predecessor disposition: "
                f"{disposition[:24]}"
            )
    for claim in CANDIDATE_LAYER_CLAIMS:
        if claim not in normalized_layer_section:
            failures.append(f"candidate release record lacks layer claim: {claim}")

    inventory, inventory_failures = compute_product_inventory(root)
    failures.extend(inventory_failures)
    expected_member_count = len(PRODUCT_FILES) + len(PRODUCT_LINKS)
    if len(inventory) != expected_member_count:
        failures.append("candidate Product inventory does not contain eight members")

    declared_inventory = parse_candidate_inventory(record_text)
    if declared_inventory != inventory:
        failures.append(
            "candidate release declared Product inventory does not match live member bytes"
        )

    inventory_sha256 = hashlib.sha256(canonical_inventory_bytes(inventory)).hexdigest()
    if inventory_sha256 != CANDIDATE_INVENTORY_SHA256:
        failures.append(
            "candidate Product inventory digest does not match frozen 2.5.0 inventory"
        )
    declared_inventory_digests = re.findall(
        r"Its SHA-256 is\s+`([0-9a-f]{64})`\.", record_text
    )
    if declared_inventory_digests != [inventory_sha256]:
        failures.append("candidate release declares the wrong Product inventory digest")

    return failures


def git_value(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def audit(root: Path, axiom_root: Path) -> dict[str, Any]:
    failures: list[str] = []
    overlay = load_json(root / "stdo_representation.json")
    failures.extend(validate_overlay(overlay))
    failures.extend(validate_frame_basis(root))
    historical_bootstrap_failures = validate_historical_bootstrap(root)
    failures.extend(historical_bootstrap_failures)
    candidate_release_failures = validate_candidate_release(root)
    failures.extend(candidate_release_failures)

    actual_requirements = {
        path.name for path in (root / "specification/requirements").glob("*.md")
    }
    if actual_requirements != ACTIVE_REQUIREMENTS:
        failures.append("active requirement inventory does not match the thin Product")

    for path in PRODUCT_FILES:
        if not (root / path).is_file():
            failures.append(f"missing Product file: {path}")
    for path, target in PRODUCT_LINKS.items():
        full_path = root / path
        if not full_path.is_symlink() or full_path.readlink().as_posix() != target:
            failures.append(f"wrong or missing Product symlink: {path}")

    if not failures and all(
        (root / path).is_file() for path in (PROGRAM_PATH, MAP_PATH)
    ):
        compression = load_json(root / PROGRAM_PATH)
        logical_index = load_json(root / MAP_PATH)
        failures.extend(validate_program_map(compression, logical_index))
        failures.extend(validate_rc2_projection(compression, logical_index))
    if all((root / path).is_file() for path in PRODUCT_FILES):
        failures.extend(validate_native_layout(root))

    for historical in HISTORICAL_ROOTS:
        if not (root / historical).is_dir():
            failures.append(f"missing retained historical root: {historical}")
        readme = root / historical / "README.md"
        if readme.is_file() and "excluded" not in readme.read_text(encoding="utf-8"):
            failures.append(f"historical root is not explicitly excluded: {historical}")

    required_text = {
        "specification/GOALS.md": ["zero local", "v0.1.0-rc.1"],
        "specification/INTENT.md": [
            "LLM supplies every frame",
            "canonical semantic compression",
            "logical constraint index",
        ],
        "specification/PRODUCT.md": [
            "eight repository entries",
            "adds no local",
            "representation_version = represented_stdo_version",
            "local_release_key = stdo_representation",
            "Project Subtree root",
            "do not become Product meaning or membership",
        ],
        "skills/stdo-representation/SKILL.md": [
            'git -C "$stack_root" archive --format=tar "$axiom_ref"',
            'test -f "$axiom_root/build_tenants/core/code/ac.py"',
            "dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672",
            "mutable `axiom_indexer/` sibling",
        ],
        ".ai-workspace/tickets/completed/T-003-construct-stdo-gtl.md": [
            "change_class: product_reprice",
            "build-tenant:axiom-indexer",
        ],
    }
    for relative, needles in required_text.items():
        content = (root / relative).read_text(encoding="utf-8")
        for needle in needles:
            if needle not in content:
                failures.append(f"{relative} lacks thin-Product claim: {needle}")

    try:
        if (
            git_value(axiom_root, "rev-parse", "refs/tags/v0.1.0-rc.1")
            != AXIOM_TAG_OBJECT
        ):
            failures.append("installed Axiom Indexer tag object mismatch")
        if (
            git_value(axiom_root, "rev-parse", "refs/tags/v0.1.0-rc.1^{}")
            != AXIOM_COMMIT
        ):
            failures.append("installed Axiom Indexer commit mismatch")
        if git_value(axiom_root, "rev-parse", "HEAD^{tree}") != AXIOM_TREE:
            failures.append("installed Axiom Indexer tree mismatch")
    except (FileNotFoundError, subprocess.CalledProcessError):
        failures.append("exact installed Axiom Indexer release is unavailable")

    compression = (
        load_json(root / COMPRESSION_PATH)
        if (root / COMPRESSION_PATH).is_file()
        else {}
    )
    logical_index = (
        load_json(root / INDEX_PATH) if (root / INDEX_PATH).is_file() else {}
    )
    represented_basis = (
        overlay.get("constitution", {}).get("stdo", {}).get("basis", {}).get("uri")
    )
    try:
        represented_stdo_version = derive_represented_stdo_semver(represented_basis)
    except ValueError:
        represented_stdo_version = None
    candidate_inventory, _ = compute_product_inventory(root)
    candidate_inventory_sha256 = hashlib.sha256(
        canonical_inventory_bytes(candidate_inventory)
    ).hexdigest()
    return {
        "valid": not failures,
        "failures": failures,
        "product": {
            "version_line": REPRESENTATION_VERSION,
            "represented_stdo_version": represented_stdo_version,
            "member_count": len(PRODUCT_FILES) + len(PRODUCT_LINKS),
            "compression_sha256": "sha256:" + canonical_sha256(compression)
            if compression
            else None,
            "index_sha256": logical_index.get("map_sha256"),
            # Preserve the Axiom artifact names for existing machine consumers.
            "program_sha256": "sha256:" + canonical_sha256(compression)
            if compression
            else None,
            "map_sha256": logical_index.get("map_sha256"),
        },
        "historical_bootstrap": {
            "version_line": HISTORICAL_BOOTSTRAP_VERSION,
            "release_record": HISTORICAL_BOOTSTRAP_RELEASE_PATH.as_posix(),
            "release_record_sha256": "sha256:" + HISTORICAL_BOOTSTRAP_RELEASE_SHA256,
            "status": "conserved" if not historical_bootstrap_failures else "invalid",
        },
        "candidate_release": {
            "version_line": REPRESENTATION_VERSION,
            "release_record": CANDIDATE_RELEASE_PATH.as_posix(),
            "member_count": len(candidate_inventory),
            "inventory_sha256": "sha256:" + candidate_inventory_sha256,
            "status": "frozen" if not candidate_release_failures else "invalid",
        },
        "frame_basis": {
            "uri": FRAME_URI,
            "sha256": "sha256:" + FRAME_SHA256,
            "decision_sha256": "sha256:" + FRAME_DECISION_SHA256,
            "status": FRAME_STATUS,
        },
    }


def parse_args() -> argparse.Namespace:
    default_axiom = (
        Path.home() / "Library/Application Support/Axiom Indexer/releases/v0.1.0-rc.1"
    )
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--axiom-indexer-root", type=Path, default=default_axiom)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = audit(args.root.resolve(), args.axiom_indexer_root.resolve())
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
