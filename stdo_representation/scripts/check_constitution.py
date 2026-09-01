#!/usr/bin/env python3
"""Focused constitutional checks for the thin STDO Representation Product."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import subprocess
import tarfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPRESENTATION_VERSION = "2.5.0-rc.4"
REPRESENTATION_VERSION_LINE = "2.5.0"
STDO_CUT = "v2.5.0-rc.4"
STDO_BASIS = "stdo://releases/v2.5.0-rc.4/"
STDO_QUALIFIED_REF = "refs/tags/specification_methodology/v2.5.0-rc.4"
STDO_TAG_OBJECT = "032dac0c833111547f7dd4b290c5316ed9b70f97"
STDO_COMMIT = "7a25668a8fecfd26f895759af3bec4708727964a"
STDO_TREE = "737af9a7a2779dbf59e7c81232e7efd4dd98692a"
STDO_SUBTREE_TREE = "a9565f923213759984f936d087cd7cebd0f44a74"
STDO_STANDARDS_TREE = "d6642edac9fb509a68b2ffc81d3404f2360b34e4"
STDO_MANIFEST = "4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e"
STDO_MEMBER_SET = "504db879867f60e46ed4dea60509d12056d10cdd8c3460dc94abf7bc56542656"
CALCULUS_REF = "stdo://releases/v2.5.0-rc.4/standards/AXIOMATIC_CALCULUS.md"
AXIOM_VERSION = "2.5.0-rc.4"
AXIOM_QUALIFIED_REF = "refs/tags/axiom_indexer/v2.5.0-rc.4"
AXIOM_CANDIDATE_RELEASE_PATH = Path("releases/v2.5.0.md")
AXIOM_CANDIDATE_RELEASE_SHA256 = (
    "2f4643a5b184a33ab9cd65c1de09b53ffee747012cd1108b795fc6df92263e8d"
)
AXIOM_PRODUCT_FILES = (
    Path("build_tenants/core/code/ac.py"),
    Path("skills/axiomatize-corpus/SKILL.md"),
    Path("skills/axiomatize-corpus/agents/openai.yaml"),
    Path("skills/axiomatize-corpus/references/output-contract.md"),
    Path("skills/axiomatize-corpus/references/program.schema.json"),
)
AXIOM_PRODUCT_LINKS = {
    Path(".agents/skills/axiomatize-corpus"): "../../skills/axiomatize-corpus",
    Path(".claude/skills/axiomatize-corpus"): "../../skills/axiomatize-corpus",
}
AXIOM_CANDIDATE_INVENTORY_SHA256 = (
    "7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6"
)
AXIOM_EXECUTABLE_SHA256 = (
    "dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672"
)
AXIOM_SCHEMA_SHA256 = "61c9d26fabb1d844f643712632f6a6551a1c6f7f8ddfef604673e57b7c6b3b7b"
AXIOM_OUTPUT_CONTRACT_SHA256 = (
    "fd0996009b890e464399863e1f16bb9b9ca7820cb5aa04e95244618849983694"
)
FRAME_URI = "urn:stdo-representation:reference-frame-basis:source-project:15"
FRAME_PATH = Path("specification/REFERENCE_FRAME_BASIS.md")
FRAME_SHA256 = "e55baf9e244be377140374636b2ec8bde361aec38ee27f260daba02baef2342e"
FRAME_DECISION_PATH = Path(
    ".ai-workspace/decisions/20260902T003317_frame_basis_rev15_acceptance.json"
)
FRAME_DECISION_SHA256 = (
    "ecad96e450c97bc3ad276bf1d541bda7fae860a88363451e851be689f6b57a92"
)
FRAME_DECISION_SCOPE = (
    "Accept the exact revision-15 project frame basis for construction and "
    "qualification of the coordinated STDO Representation 2.5.0-rc.4 cohort "
    "subject against exact locally tagged Source STDO v2.5.0-rc.4 and the "
    "exact seven-member Axiom Indexer v2.5.0-rc.4 candidate; this decision "
    "grants no tag, push, remote-ref, or Product-acceptance effect."
)
FRAME_DECISION_TIME = "2026-09-02T00:33:17+10:00"
FRAME_DECISION_SOURCE = (
    "Delegated ratification by Codex under the Product owner's direct authority "
    "grant in this collaboration to update STDO Representation so it stays "
    "current with STDO, align the release-matched cohort under the exact STDO "
    "version, and complete release only after qualification. This record does "
    "not claim that the Product owner personally inspected these exact "
    "revision-15 bytes."
)
FRAME_DECISION_EVIDENCE_REFS = (
    "./specification/PRODUCT.md#product-disposition-authority",
    "./specification/PRODUCT.md#version-relation",
    "./specification/GOALS.md#goal-008--enter-the-coordinated-release-matched-cohort",
    "./specification/requirements/REQ-P-BASIS-AND-IDENTITY.md#requirements",
    "./specification/REFERENCE_FRAME_BASIS.md#acceptance-gate",
    "../specification_methodology/releases/v2.5.0.md",
    "../axiom_indexer/releases/v2.5.0.md",
)
FRAME_DECISION_SUPERSESSION = {
    "prior_subject_sha256": (
        "sha256:c20fd096436452e24bc4d4bc68e77c1024f790b50ec82ecfd22a07759ef7cb61"
    ),
    "prior_decision_sha256": (
        "sha256:4462b28ebb5bc4fb4dfb7dc856e272321d5739fd48e2552b2b5fa23d4b19e224"
    ),
    "change": (
        "The acceptance law now admits only an explicitly user-granted bounded "
        "release-authority proxy and binds exact digest, scope, direct grant "
        "source, time, evidence, no-self-expansion, and no-personal-byte-inspection "
        "constraints."
    ),
    "disposition": (
        "The prior frame and decision bytes are superseded before commit or "
        "publication and do not accept this repaired subject."
    ),
}
FRAME_STATUS = "accepted_and_bound"
HISTORICAL_BOOTSTRAP_VERSION = "0.1.0"
HISTORICAL_BOOTSTRAP_RELEASE_PATH = Path("releases/v0.1.0.md")
HISTORICAL_BOOTSTRAP_RELEASE_SHA256 = (
    "7d7e0c78fa5fe893ae530df0069d7f18ecf69144a845f8f782d3c842fe50f876"
)
CANDIDATE_RELEASE_PATH = Path("releases/v2.5.0.md")
CANDIDATE_RELEASE_SHA256 = (
    "d91028fa2f52f86511a989cbacaaa32bff8a0a2fe71a3e380aad0e0630d597af"
)
CANDIDATE_INVENTORY_SHA256 = (
    "32dd04f5644a05c04c844a28d1978d1c1ffdd5e7f20473b7d7f8626e1e07e830"
)
CANDIDATE_RELEASE_ROWS = {
    "release version": REPRESENTATION_VERSION,
    "product-local cut": f"v{REPRESENTATION_VERSION}",
    "Project Release Namespace": "stdo_representation",
    "Project Subtree root": "stdo_representation",
    "qualified RC branch": "refs/heads/rc/stdo_representation/2.5.0",
    "qualified immutable tag ref": ("refs/tags/stdo_representation/v2.5.0-rc.4"),
    "qualified version-line selector": "refs/tags/stdo_representation/v2.5.0",
    "qualified release branch": "refs/heads/release/stdo_representation/2.5.0",
    "matched Source STDO ref": STDO_QUALIFIED_REF,
    "public Source STDO basis": STDO_BASIS,
    "exact Axiom dependency": AXIOM_QUALIFIED_REF,
}
CANDIDATE_RELEASE_CLAIMS = (
    "`STDO-REP-2.5-RC4-C01`:",
    "`STDO-REP-2.5-RC4-C02`:",
    "`STDO-REP-2.5-RC4-C03`:",
    "`STDO-REP-2.5-RC4-C04`:",
    "`STDO-REP-2.5-RC4-C05`:",
    "`STDO-REP-2.5-RC4-C06`:",
)
CANDIDATE_RELEASE_CLAIM_IDS = tuple(
    f"STDO-REP-2.5-RC4-C{ordinal:02d}" for ordinal in range(1, 7)
)
CANDIDATE_RELEASE_C04 = (
    "`STDO-REP-2.5-RC4-C04`: the complete source-corpus record and immutable "
    "RC3-to-RC4 tag delta prove 49 source members conserved and exactly three "
    "changed; comparison with the exact tracked RC2 program across the immutable "
    "RC2-to-RC4 five-member frontier proves conservation of every prior entry "
    "grounded only in the 47 byte-identical members, while exact current clauses "
    "and routes bind the material semantics re-authored for all three RC4-changed "
    "members. Hashes prove identity and frontier membership, not semantic "
    "qualification."
)
CANDIDATE_PREDECESSOR_DISPOSITIONS = (
    "`STDO-REP-2.5-C01`: **conserved and specialized**",
    "`STDO-REP-2.5-C02`: **superseded**",
    "`STDO-REP-2.5-C03`: **conserved**",
    "`STDO-REP-2.5-C04`: **superseded**",
    "`STDO-REP-2.5-C05`: **conserved**",
)
CANDIDATE_LAYER_CLAIMS = (
    "exact Source STDO v2.5.0-rc.4 prose and plugin",
    "a_c.STDO 2.5.0-rc.4 Axiomatic Program",
    "canonical semantic compression",
    "exact Axiom Indexer v2.5.0-rc.4 Logical Constraint Map",
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
EXACT_MATCHED_VERSION_PATTERN = re.compile(
    r"^(?P<line>(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\."
    r"(?:0|[1-9][0-9]*))-rc\.(?P<ordinal>[1-9][0-9]*)$"
)
STDO_RELEASE_URI_PATTERN = re.compile(
    r"^stdo://releases/v"
    r"(?P<version>(?P<line>(?:0|[1-9][0-9]*)\."
    r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*))"
    r"-rc\.(?P<ordinal>[1-9][0-9]*))/$"
)
CANDIDATE_MEMBER_ROW_PATTERN = re.compile(
    r"^\| (?P<type>file|symlink) \| `(?P<path>[^`]+)`"
    r"(?: -> `(?P<target>[^`]+)`)? \| `(?P<sha256>[0-9a-f]{64})` \|$"
)

COMPRESSION_PATH = Path(
    "build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.4/"
    "axiomatic-program.json"
)
INDEX_PATH = COMPRESSION_PATH.with_name("logical-constraint-map.json")
SOURCE_CORPUS_PATH = COMPRESSION_PATH.with_name("source-corpus.json")
VALIDATION_REPORT_PATH = COMPRESSION_PATH.with_name("validation-report.json")
VALIDATION_REPORT_SHA256 = (
    "e79832f2e754348a9952d5ad01e97f11ecf3f18e9e332d49c0f5245171c818c9"
)
CONSERVATION_BASELINE_PROGRAM_PATH = Path(
    "build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.2/"
    "axiomatic-program.json"
)
CONSERVATION_BASELINE_PROGRAM_SHA256 = (
    "b64c1fc9b90b5d9eb5bcbeae9dce920ede637286de58c4ce5da5deb89fa9f5fc"
)
IMMUTABLE_STDO_PREDECESSORS = {
    "RC2": {
        "ref": "refs/tags/specification_methodology/v2.5.0-rc.2",
        "tag_object": "5ebd2d87ff0c0d9fcca96ba42d90253ba6fec7e3",
        "commit": "2c9a11701d567d01320482100979c9fcd54ab846",
        "standards_tree": "f636fd8dcc234e05b8aa464a35f24d843c258dc9",
        "member_count": 52,
        "member_set_sha256": (
            "a5910bc56b491b5c520910e7bdad0949c1283e8b71951f1079e1fd86f59d20e7"
        ),
    },
    "RC3": {
        "ref": "refs/tags/specification_methodology/v2.5.0-rc.3",
        "tag_object": "625e123572565a27a3953d07c6b883aa5e8f1ed2",
        "commit": "ece85fbce89e54afbccb9bd670b58650d23a007b",
        "standards_tree": "25e42fdd4480491762faebd4d0aeb7fe034057de",
        "member_count": 52,
        "member_set_sha256": (
            "8492f66bba93a1e4559b2275f01df277b5e49c24bc0a76feb028e85e4bdf5c2f"
        ),
    },
}
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


def validate_live_stdo_status(
    root: Path,
    overlay: dict[str, Any],
    installed_manifest: dict[str, Any],
    installed_manifest_sha256: str,
) -> tuple[list[str], dict[str, Any]]:
    """Execute and bind the exact stdo 0.1.2 status verification proof."""

    failures: list[str] = []
    evidence: dict[str, Any] = {
        "command": "stdo status --definition stdo_representation.json --verify",
        "toolchain": None,
        "valid": False,
    }
    try:
        version_result = subprocess.run(
            ["stdo", "--version"],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return [f"stdo 0.1.2 is unavailable: {exc}"], evidence
    if version_result.returncode != 0:
        failures.append("stdo --version failed")
    toolchain = version_result.stdout.strip()
    evidence["toolchain"] = toolchain
    if toolchain != "stdo 0.1.2":
        failures.append("live STDO proof did not use exact stdo 0.1.2")

    definition_path = (root / "stdo_representation.json").resolve()
    status_result = subprocess.run(
        [
            "stdo",
            "status",
            "--definition",
            str(definition_path),
            "--verify",
        ],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if status_result.returncode != 0:
        detail = status_result.stderr.strip() or status_result.stdout.strip()
        failures.append(f"live stdo status --verify failed: {detail}")
        return failures, evidence
    try:
        status = json.loads(status_result.stdout)
    except json.JSONDecodeError:
        failures.append("live stdo status --verify did not return JSON")
        return failures, evidence
    if not isinstance(status, dict):
        failures.append("live stdo status --verify did not return one result object")
        return failures, evidence

    basis = overlay.get("constitution", {}).get("stdo", {})
    installed_root = (
        Path.home() / "Library/Application Support/STDO/releases" / STDO_CUT
    )
    expected_fields = {
        "basis": basis.get("basis", {}).get("uri"),
        "cut": STDO_CUT,
        "definition": str(definition_path),
        "definition_id": overlay.get("product", {}).get("definition_id"),
        "failures": [],
        "installed": True,
        "manifest_sha256": installed_manifest_sha256,
        "path": str(installed_root),
        "schema": str(
            installed_root / "standards/schemas/product-definition.schema.json"
        ),
        "selector": basis.get("selector"),
        "valid": True,
    }
    for key, expected_value in expected_fields.items():
        if status.get(key) != expected_value:
            failures.append(f"live stdo status has wrong {key}")
    if status.get("release") != installed_manifest.get("release"):
        failures.append("live stdo status release does not match installed manifest")
    if status.get("standards") != installed_manifest.get("standards"):
        failures.append("live stdo status standards do not match installed manifest")
    if basis.get("basis", {}).get("manifest_sha256") != installed_manifest_sha256:
        failures.append("live stdo status manifest does not match Product Definition")

    evidence.update(
        {
            "basis": status.get("basis"),
            "cut": status.get("cut"),
            "manifest_sha256": status.get("manifest_sha256"),
            "qualified_ref": status.get("release", {}).get("qualified_ref"),
            "tag_object": status.get("release", {}).get("tag_object"),
            "valid": not failures,
        }
    )
    return failures, evidence


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
    return match.group("line")


def derive_represented_stdo_exact_version(release_uri: str) -> str:
    """Return the exact represented STDO version, including RC ordinal."""

    if not isinstance(release_uri, str):
        raise ValueError("Source STDO release URI is not a string")
    match = STDO_RELEASE_URI_PATTERN.fullmatch(release_uri)
    if match is None:
        raise ValueError("Source STDO basis is not an exact RC release URI")
    return match.group("version")


def validate_coordinated_versions(
    representation_version: Any,
    represented_release_uri: Any,
    axiom_indexer_version: Any,
) -> list[str]:
    """Require one exact same-suffix release cohort without collapsing Products."""

    failures: list[str] = []
    if not isinstance(representation_version, str) or not (
        EXACT_MATCHED_VERSION_PATTERN.fullmatch(representation_version)
    ):
        failures.append("Representation version is not an exact matched RC version")
        return failures
    try:
        represented_version = derive_represented_stdo_exact_version(
            represented_release_uri
        )
    except ValueError:
        failures.append("Source STDO basis is not an exact RC release URI")
        return failures
    if representation_version != represented_version:
        failures.append("Representation exact version does not match Source STDO")
    if axiom_indexer_version != representation_version:
        failures.append("Axiom Indexer exact version does not match Representation")
    return failures


def standards_member_delta(
    previous_members: Any, current_members: Any
) -> dict[str, list[str]]:
    """Classify exact standards-member identity across two immutable cuts."""

    def rows_by_path(rows: Any) -> dict[str, str]:
        if not isinstance(rows, list):
            raise ValueError("standards member population is not an array")
        result: dict[str, str] = {}
        for row in rows:
            if not isinstance(row, dict):
                raise ValueError("standards member is not an object")
            path = row.get("path")
            digest = row.get("sha256")
            if not isinstance(path, str) or not isinstance(digest, str):
                raise ValueError("standards member lacks path or SHA-256")
            if path in result:
                raise ValueError("standards member path is duplicated")
            result[path] = digest
        return result

    previous = rows_by_path(previous_members)
    current = rows_by_path(current_members)
    shared = set(previous) & set(current)
    return {
        "conserved": sorted(path for path in shared if previous[path] == current[path]),
        "changed": sorted(path for path in shared if previous[path] != current[path]),
        "added": sorted(set(current) - set(previous)),
        "removed": sorted(set(previous) - set(current)),
    }


def validate_program_conservation(
    previous_program: dict[str, Any],
    current_program: dict[str, Any],
    changed_member_paths: set[str],
) -> list[str]:
    """Conserve entries outside the exact changed-source member frontier."""

    failures: list[str] = []
    previous_basis = previous_program.get("source_basis")
    current_basis = current_program.get("source_basis")
    if not isinstance(previous_basis, str) or not isinstance(current_basis, str):
        return ["program conservation lacks exact source bases"]

    def normalize(value: Any, basis: str) -> Any:
        if isinstance(value, str):
            return value.replace(basis, "stdo://releases/vMATCH/standards/")
        if isinstance(value, list):
            return [normalize(row, basis) for row in value]
        if isinstance(value, dict):
            return {key: normalize(row, basis) for key, row in value.items()}
        return value

    def member_paths(row: dict[str, Any], basis: str) -> set[str]:
        result: set[str] = set()
        for source_ref in row.get("source_refs", []):
            if isinstance(source_ref, str) and source_ref.startswith(basis):
                result.add(source_ref[len(basis) :].split("#", 1)[0])
        return result

    for population in ("symbols", "clauses", "residuals"):
        previous_rows = {
            row.get("uri"): row
            for row in previous_program.get(population, [])
            if isinstance(row, dict) and isinstance(row.get("uri"), str)
        }
        current_rows = {
            row.get("uri"): row
            for row in current_program.get(population, [])
            if isinstance(row, dict) and isinstance(row.get("uri"), str)
        }
        for uri, previous_row in previous_rows.items():
            if member_paths(previous_row, previous_basis) & changed_member_paths:
                continue
            current_row = current_rows.get(uri)
            if current_row is None or normalize(
                previous_row, previous_basis
            ) != normalize(current_row, current_basis):
                failures.append(
                    f"unaffected {population} entry was not conserved: {uri}"
                )

    current_source_members: set[str] = set()
    for population in ("symbols", "clauses", "residuals"):
        for row in current_program.get(population, []):
            if isinstance(row, dict):
                current_source_members.update(member_paths(row, current_basis))
    for path in sorted(changed_member_paths - current_source_members):
        failures.append(
            f"changed Source STDO member has no current program route: {path}"
        )
    return failures


def validate_source_corpus(
    corpus: dict[str, Any],
    overlay: dict[str, Any],
    installed_manifest: dict[str, Any],
    installed_manifest_sha256: str,
    compression: dict[str, Any],
    logical_index: dict[str, Any],
) -> list[str]:
    """Bind one derived Representation subject to the complete immutable corpus."""

    failures: list[str] = []
    if corpus.get("kind") != "stdo-representation.source-corpus":
        failures.append("source corpus has the wrong kind")
    if corpus.get("schema_version") != 1:
        failures.append("source corpus has the wrong schema version")

    basis = overlay.get("constitution", {}).get("stdo", {}).get("basis", {})
    basis_uri = basis.get("uri")
    try:
        exact_version = derive_represented_stdo_exact_version(basis_uri)
    except ValueError:
        failures.append("source corpus cannot derive an exact matched version")
        return failures

    if corpus.get("representation_version") != exact_version:
        failures.append("source corpus version does not match the Product basis")
    source = corpus.get("source_release")
    if not isinstance(source, dict):
        failures.append("source corpus lacks its source release")
        return failures

    manifest_release = installed_manifest.get("release", {})
    manifest_standards = installed_manifest.get("standards", {})
    expected = {
        "cut": f"v{exact_version}",
        "uri": basis_uri,
        "qualified_ref": manifest_release.get("qualified_ref"),
        "tag_object": manifest_release.get("tag_object"),
        "commit": manifest_release.get("commit"),
        "tree": manifest_release.get("tree"),
        "project_subtree_root": manifest_release.get("project_subtree_root"),
        "project_subtree_tree": manifest_release.get("project_subtree_tree"),
        "standards_tree": manifest_release.get("standards_tree"),
        "installed_manifest_sha256": installed_manifest_sha256,
        "standards_member_count": manifest_standards.get("member_count"),
        "standards_member_set_sha256": manifest_standards.get("member_set_sha256"),
        "standards_members": manifest_standards.get("members"),
    }
    for field, expected_value in expected.items():
        if source.get(field) != expected_value:
            failures.append(f"source corpus has the wrong {field}")
    if basis.get("manifest_sha256") != installed_manifest_sha256:
        failures.append("Product basis and installed source manifest disagree")

    expected_source_basis = basis_uri + "standards/"
    if compression.get("source_basis") != expected_source_basis:
        failures.append("compression does not use the source-corpus basis")
    if logical_index.get("source_basis") != expected_source_basis:
        failures.append("logical index does not use the source-corpus basis")
    encoded = json.dumps(
        {"compression": compression, "logical_index": logical_index},
        ensure_ascii=False,
        sort_keys=True,
    )
    foreign_routes = {
        match.group(0)
        for match in re.finditer(r"stdo://releases/v[^/]+/", encoded)
        if match.group(0) != basis_uri
    }
    if foreign_routes:
        failures.append("derived artifacts contain routes from another STDO cut")
    return failures


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
    failures.extend(
        validate_representation_version(REPRESENTATION_VERSION_LINE, basis_uri)
    )
    failures.extend(
        validate_coordinated_versions(REPRESENTATION_VERSION, basis_uri, AXIOM_VERSION)
    )
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
                "20260902T003317_frame_basis_rev15_acceptance.json",
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
        failures.append("accepted project frame basis bytes changed")
        return failures

    frame_text = frame_bytes.decode("utf-8")
    if FRAME_URI not in frame_text:
        failures.append("accepted project frame basis has the wrong identity")
    normalized_frame = " ".join(frame_text.split())
    expected_status = (
        "Status: accepted and bound source-project basis, revision 15, through "
        "the exact digest-bound bounded-proxy decision named in the Acceptance Gate."
    )
    if expected_status not in normalized_frame:
        failures.append("project frame basis has the wrong acceptance status")
    required_proxy_law = (
        "The sole proxy exception is an explicitly user-granted bounded "
        "release-authority proxy.",
        "The proxy may record only that bounded acceptance.",
        "it must not claim that the Product owner personally inspected exact bytes",
        "Neither the proxy nor this frame can infer or enlarge the grant.",
    )
    for claim in required_proxy_law:
        if claim not in normalized_frame:
            failures.append(f"project frame basis lacks bounded-proxy law: {claim}")

    decision_path = root / FRAME_DECISION_PATH
    decision_bytes = decision_path.read_bytes()
    if hashlib.sha256(decision_bytes).hexdigest() != FRAME_DECISION_SHA256:
        failures.append("project frame-basis acceptance record bytes changed")
        return failures

    decision = json.loads(decision_bytes)
    expected = {
        "kind": "stdo-representation.frame-basis-acceptance",
        "schema_version": 2,
        "subject_uri": FRAME_URI,
        "subject_ref": "./specification/REFERENCE_FRAME_BASIS.md#project-frame-basis",
        "subject_sha256": "sha256:" + FRAME_SHA256,
        "method_basis_uri": (STDO_BASIS + "standards/REFERENCE_FRAME_METHOD.md"),
        "method_basis_sha256": (
            "sha256:c7f7abfa620d73e209463605517075ac375d8e79e0273d3f435c4e36155de5d8"
        ),
        "actor_identity": "urn:openai:codex:delegated-release-authority",
        "authority_identity": "urn:stdo-representation:authority:product-owner",
        "authority_mode": "explicitly-user-granted-bounded-release-authority-proxy",
        "decision": "accepted",
        "scope": FRAME_DECISION_SCOPE,
        "decided_at": FRAME_DECISION_TIME,
        "grant_source_kind": "direct-human-product-owner-conversation",
        "decision_source": FRAME_DECISION_SOURCE,
        "self_expansion_prohibited": True,
        "human_exact_byte_inspection_claimed": False,
        "supersession_record": FRAME_DECISION_SUPERSESSION,
    }
    for key, value in expected.items():
        if decision.get(key) != value:
            failures.append(f"project frame-basis acceptance has wrong {key}")
    if decision.get("evidence_refs") != list(FRAME_DECISION_EVIDENCE_REFS):
        failures.append("project frame-basis acceptance has wrong evidence_refs")
    for evidence_ref in FRAME_DECISION_EVIDENCE_REFS:
        relative = evidence_ref.split("#", maxsplit=1)[0]
        if not (root / relative).resolve().is_file():
            failures.append(
                f"project frame-basis acceptance evidence unavailable: {evidence_ref}"
            )
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
    cohort_uri = "urn:stdo-representation:a-c-text:symbol:release-matched-cohort"
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
    if symbols.get(cohort_uri, {}).get("label") != "Release-matched asset cohort":
        failures.append("Product compression does not declare cohort identity")

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


def validate_validation_report(
    report_path: Path,
    compression: dict[str, Any],
    logical_index: dict[str, Any],
) -> list[str]:
    """Bind the exact Axiom report bytes to their material RC4 evidence."""

    if not report_path.is_file():
        return ["missing exact RC4 validation report"]

    failures: list[str] = []
    report_bytes = report_path.read_bytes()
    if hashlib.sha256(report_bytes).hexdigest() != VALIDATION_REPORT_SHA256:
        failures.append("exact RC4 validation report bytes changed")
    try:
        report = json.loads(report_bytes)
    except json.JSONDecodeError:
        return failures + ["exact RC4 validation report is not JSON"]

    if report.get("kind") != "axiom-indexer.validation-report":
        failures.append("RC4 validation report has the wrong kind")
    if report.get("schema_version") != 1:
        failures.append("RC4 validation report has the wrong schema version")
    if report.get("status") != "valid" or report.get("diagnostics") != []:
        failures.append("RC4 Axiom validation report is not zero-diagnostic valid")
    if report.get("program_uri") != compression.get("uri"):
        failures.append("RC4 validation report binds the wrong program URI")
    expected_program_sha256 = "sha256:" + canonical_sha256(compression)
    if report.get("program_sha256") != expected_program_sha256:
        failures.append("RC4 validation report binds the wrong program digest")
    expected_counts = {
        name: len(value) if isinstance(value, list) else None
        for name in ("clauses", "residuals", "symbols")
        for value in (compression.get(name),)
    }
    if report.get("derived_counts") != expected_counts:
        failures.append("RC4 validation report has the wrong populations")
    if report.get("resolved_sources") != logical_index.get("resolved_sources"):
        failures.append("RC4 validation report changes the resolved source closure")
    return failures


def validate_current_projection(
    compression: dict[str, Any], logical_index: dict[str, Any]
) -> list[str]:
    """Require the current RC4 frame, cohort, and source-routing semantics."""

    failures: list[str] = []
    expected_frame_refs = [
        STDO_BASIS + "standards/" "REFERENCE_FRAME_METHOD.md#reference-frame-laws",
        STDO_BASIS + "standards/"
        "STDO_REFERENCE_FRAME_BASELINE.md#derived-executive-frame",
        STDO_BASIS + "standards/"
        "STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame",
        STDO_BASIS + "standards/"
        "STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame",
    ]
    if compression.get("frame_refs") != expected_frame_refs:
        failures.append(
            "Product compression has the wrong current RC4 frame references"
        )

    encoded = json.dumps(
        {"compression": compression, "index": logical_index},
        ensure_ascii=False,
        sort_keys=True,
    )
    if "repo://" in encoded:
        failures.append("current RC4 Product artifacts retain mutable candidate routes")
    foreign_routes = {
        match.group(0)
        for match in re.finditer(r"stdo://releases/v[^/]+/", encoded)
        if match.group(0) != STDO_BASIS
    }
    if foreign_routes:
        failures.append("current RC4 Product artifacts retain foreign STDO routes")

    required_clauses = {
        "bootstrap-resolves-exact-basis": (
            "Discover exactly one Product Definition, verify its exact immutable "
            "STDO basis, resolve its accepted Project Reference-Frame Basis or "
            "composition, and enter only the smallest dependency-ready Executive "
            "activation; prompts, summaries, maps, and prior results may route "
            "attention but cannot replace source authority or a closed frame result."
        ),
        "aggregate-compression-reenters-source": (
            "Use aggregate compression as bounded prompt authority and re-enter "
            "exact raw owners for stale, missing, conflicting, or unresolved method "
            "meaning."
        ),
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
        "cohort-exact-version-preserves-product-identity": (
            "A declared release-matched STDO cohort names the exact STDO corpus and "
            "plugin, Axiom Indexer mechanics Product, STDO Representation Product, "
            "released axiomatic program and constraint map, complete source-member "
            "digest closure, owners, qualification boundary, and publication "
            "transaction; every member carries one exact normalized version suffix "
            "while retaining separate Product identity, inventory, tag, and "
            "acceptance."
        ),
        "cohort-publication-fails-closed": (
            "Publish the complete cohort only in one atomic transport transaction "
            "after local-ref-graph qualification binds every tag object, peel, target, "
            "exact push ref, and fetched expected remote object ID or required absence; "
            "immutable tags are create-only, mutable refs use explicit per-ref "
            "compare-and-swap leases, and unsupported atomic transport, remote drift, "
            "lease mismatch, or a partial cohort refuses without force or sequential "
            "fallback."
        ),
        "cohort-source-change-invalidates-index": (
            "A change to any indexed source member invalidates the predecessor derived "
            "candidate; regenerate and mechanically validate the program, map, and "
            "complete source-member digest closure under the same new cut suffix, "
            "retaining any stale index only as immutable history."
        ),
        "cohort-two-commit-construction-is-one-publication": (
            "Freeze STDO and plugin in commit A, create and verify its local annotated "
            "tag and exact Install, derive and freeze the child Products plus source "
            "closure in commit B, qualify B before child tags, create every local cohort "
            "tag and mutable ref, and requalify the complete local ref graph before the "
            "single publication transaction."
        ),
    }
    actual_clauses = {
        row.get("uri", "").rsplit(":", 1)[-1]: row.get("statement")
        for row in compression.get("clauses", [])
        if isinstance(row, dict)
    }
    for clause, expected_statement in required_clauses.items():
        if actual_clauses.get(clause) != expected_statement:
            failures.append(
                f"current RC4 Product compression changes required clause: {clause}"
            )

    required_changed_frontier_routes = {
        "bootstrap-resolves-exact-basis": [
            STDO_BASIS + "standards/authority_compressions/"
            "stdo_bootstrap.md#stdo-discovery-bootstrap"
        ],
        "aggregate-compression-reenters-source": [
            STDO_BASIS + "standards/authority_compressions/"
            "stdo_compressed.md#re-entry-compression"
        ],
        "cohort-exact-version-preserves-product-identity": [
            STDO_BASIS
            + "standards/RELEASE_METHOD.md#coordinated-release-matched-asset-cohorts",
            STDO_BASIS
            + "standards/authority_compressions/stdo_compressed.md#prime-operating-rules",
        ],
        "cohort-publication-fails-closed": [
            STDO_BASIS
            + "standards/RELEASE_METHOD.md#two-commit-construction-and-one-publication-transaction",
            STDO_BASIS
            + "standards/authority_compressions/stdo_compressed.md#prime-operating-rules",
        ],
        "cohort-source-change-invalidates-index": [
            STDO_BASIS
            + "standards/RELEASE_METHOD.md#coordinated-release-matched-asset-cohorts"
        ],
        "cohort-two-commit-construction-is-one-publication": [
            STDO_BASIS
            + "standards/RELEASE_METHOD.md#two-commit-construction-and-one-publication-transaction",
            STDO_BASIS
            + "standards/authority_compressions/stdo_compressed.md#prime-operating-rules",
        ],
    }
    actual_clause_rows = {
        row.get("uri", "").rsplit(":", 1)[-1]: row
        for row in compression.get("clauses", [])
        if isinstance(row, dict)
    }
    for clause, expected_routes in required_changed_frontier_routes.items():
        if actual_clause_rows.get(clause, {}).get("source_refs") != expected_routes:
            failures.append(
                "current RC4 Product compression changes required source routes: "
                f"{clause}"
            )
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
            failures.append(f"native skill lacks current projection claim: {claim}")

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


def validate_axiom_candidate(
    axiom_root: Path, representation_version: str
) -> list[str]:
    """Bind construction to exact same-version Axiom candidate mechanics."""

    failures: list[str] = []
    release_path = axiom_root / AXIOM_CANDIDATE_RELEASE_PATH
    if not release_path.is_file():
        return ["missing coordinated Axiom candidate release record"]
    release_text = release_path.read_text(encoding="utf-8")
    if hashlib.sha256(release_path.read_bytes()).hexdigest() != (
        AXIOM_CANDIDATE_RELEASE_SHA256
    ):
        failures.append("coordinated Axiom candidate release record changed")
    expected_rows = {
        "release version": representation_version,
        "product-local cut": f"v{representation_version}",
        "qualified immutable tag ref": (
            f"refs/tags/axiom_indexer/v{representation_version}"
        ),
        "matched Source STDO cut": STDO_QUALIFIED_REF,
        "public Source STDO basis": STDO_BASIS,
    }
    for label, expected in expected_rows.items():
        row = f"| {label} | `{expected}` |"
        if row not in release_text:
            failures.append(f"Axiom candidate has the wrong {label}")

    inventory: list[dict[str, str]] = []
    for path in AXIOM_PRODUCT_FILES:
        full_path = axiom_root / path
        if not full_path.is_file() or full_path.is_symlink():
            failures.append(f"missing Axiom Product file: {path}")
            continue
        inventory.append(
            {
                "path": path.as_posix(),
                "type": "file",
                "sha256": hashlib.sha256(full_path.read_bytes()).hexdigest(),
            }
        )
    for path, expected_target in AXIOM_PRODUCT_LINKS.items():
        full_path = axiom_root / path
        if not full_path.is_symlink():
            failures.append(f"missing Axiom Product symlink: {path}")
            continue
        target = full_path.readlink().as_posix()
        if target != expected_target:
            failures.append(f"wrong Axiom Product symlink target: {path}")
        inventory.append(
            {
                "path": path.as_posix(),
                "type": "symlink",
                "target": target,
                "sha256": hashlib.sha256(target.encode("utf-8")).hexdigest(),
            }
        )
    inventory.sort(key=lambda row: row["path"])
    inventory_sha256 = hashlib.sha256(canonical_inventory_bytes(inventory)).hexdigest()
    if inventory_sha256 != AXIOM_CANDIDATE_INVENTORY_SHA256:
        failures.append("Axiom candidate Product inventory changed")
    if AXIOM_CANDIDATE_INVENTORY_SHA256 not in release_text:
        failures.append("Axiom candidate record lacks the exact member inventory")

    exact_file_digests = {
        Path("build_tenants/core/code/ac.py"): AXIOM_EXECUTABLE_SHA256,
        Path(
            "skills/axiomatize-corpus/references/program.schema.json"
        ): AXIOM_SCHEMA_SHA256,
        Path(
            "skills/axiomatize-corpus/references/output-contract.md"
        ): AXIOM_OUTPUT_CONTRACT_SHA256,
    }
    for path, expected_digest in exact_file_digests.items():
        full_path = axiom_root / path
        if full_path.is_file() and (
            hashlib.sha256(full_path.read_bytes()).hexdigest() != expected_digest
        ):
            failures.append(f"Axiom candidate changed exact mechanics: {path}")
    return failures


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
    """Bind the RC4 candidate record to its exact live Product and cohort."""

    failures: list[str] = []
    release_path = root / CANDIDATE_RELEASE_PATH
    if not release_path.is_file():
        return ["missing STDO Representation 2.5.0 candidate release record"]

    record_bytes = release_path.read_bytes()
    record_text = record_bytes.decode("utf-8")
    normalized_record = " ".join(record_text.split())
    if hashlib.sha256(record_bytes).hexdigest() != CANDIDATE_RELEASE_SHA256:
        failures.append("candidate release record bytes changed")
    if not record_text.startswith("# STDO Representation 2.5.0 RC4\n"):
        failures.append("candidate release record has the wrong Product version")
    expected_status = (
        "Status: frozen coordinated candidate; no STDO Representation "
        "`2.5.0-rc.4` cut is published or accepted by this record."
    )
    if expected_status not in normalized_record:
        failures.append("candidate release record has the wrong candidate status")
    required_release_semantics = (
        "Equal suffixes establish release matching and do not collapse Product "
        "identities, member sets, authorities, judgments, or qualified refs.",
        "This record grants no commit, branch, tag, selector, remote, publication, "
        "or Product-acceptance effect.",
        "Publication and Product acceptance require their separately authorized "
        "and closed relations. No record here performs either.",
    )
    for claim in required_release_semantics:
        if claim not in normalized_record:
            failures.append(f"candidate release record lacks boundary law: {claim}")
    for field, expected_value in CANDIDATE_RELEASE_ROWS.items():
        if f"| {field} | `{expected_value}` |" not in record_text:
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
    ].partition("## RC3 transition evidence")[0]
    actual_claim_ids = tuple(
        re.findall(
            r"^- `(STDO-REP-2\.5-RC4-C[0-9]{2})`:",
            claims_section,
            flags=re.MULTILINE,
        )
    )
    if actual_claim_ids != CANDIDATE_RELEASE_CLAIM_IDS:
        failures.append("candidate release record has the wrong 2.5 claim population")
    for claim in CANDIDATE_RELEASE_CLAIMS:
        if claim not in normalized_claims_section:
            failures.append(f"candidate release record lacks exact claim: {claim[:22]}")
    if CANDIDATE_RELEASE_C04 not in normalized_claims_section:
        failures.append("candidate release record lacks exact C04 semantics")
    for disposition in CANDIDATE_PREDECESSOR_DISPOSITIONS:
        if disposition not in dispositions_section:
            failures.append(
                "candidate release lacks exact predecessor disposition: "
                f"{disposition[:24]}"
            )
    for claim in CANDIDATE_LAYER_CLAIMS:
        if claim not in normalized_layer_section:
            failures.append(f"candidate release record lacks layer claim: {claim}")

    required_provenance = (
        SOURCE_CORPUS_PATH.as_posix(),
        COMPRESSION_PATH.as_posix(),
        INDEX_PATH.as_posix(),
        VALIDATION_REPORT_PATH.as_posix(),
        STDO_QUALIFIED_REF,
        STDO_TAG_OBJECT,
        STDO_COMMIT,
        STDO_MANIFEST,
        STDO_MEMBER_SET,
        AXIOM_QUALIFIED_REF,
        AXIOM_CANDIDATE_INVENTORY_SHA256,
        AXIOM_EXECUTABLE_SHA256,
        AXIOM_SCHEMA_SHA256,
        AXIOM_OUTPUT_CONTRACT_SHA256,
        AXIOM_CANDIDATE_RELEASE_SHA256,
        FRAME_SHA256,
        FRAME_DECISION_SHA256,
        "074fcb07258792008c31998ed2cf4f4234bec92f9e7be10b177569559387808d",
        "90400806e79cd09f350f285000c8579af81f621cdbe3753125ed9d74bcb6b466",
        "5b6a5df2e2429f7b1d463e2b9107ca58f5c482e9565e98e792650f41b222a4cf",
        "5237339d919d352944c42ea201ae49c48b885db02255f5ca1a67173c2b0c1c3f",
        "bdfe3c09fe196a7c1f1634d0441c616e96049961356d41f85bdead2d3a0fa8ce",
        VALIDATION_REPORT_SHA256,
    )
    for value in required_provenance:
        if value not in record_text:
            failures.append(f"candidate release lacks exact provenance: {value}")

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


def immutable_stdo_standards_members(
    root: Path, label: str
) -> tuple[list[dict[str, str]], list[str]]:
    """Reacquire one exact predecessor standards inventory from its annotated tag."""

    identity = IMMUTABLE_STDO_PREDECESSORS[label]
    ref = str(identity["ref"])
    failures: list[str] = []
    try:
        repository_root = Path(git_value(root, "rev-parse", "--show-toplevel"))
        observed = {
            "type": git_value(repository_root, "cat-file", "-t", ref),
            "tag_object": git_value(repository_root, "rev-parse", ref),
            "commit": git_value(repository_root, "rev-parse", f"{ref}^{{}}"),
            "standards_tree": git_value(
                repository_root,
                "rev-parse",
                f"{ref}^{{}}:specification_methodology/specification/standards",
            ),
        }
    except subprocess.CalledProcessError:
        return [], [f"immutable STDO {label} predecessor is unavailable"]

    if observed["type"] != "tag":
        failures.append(f"immutable STDO {label} predecessor is not annotated")
    for field in ("tag_object", "commit", "standards_tree"):
        if observed[field] != identity[field]:
            failures.append(f"immutable STDO {label} predecessor {field} changed")
    if failures:
        return [], failures

    prefix = "specification_methodology/specification/standards/"
    try:
        archive_bytes = subprocess.run(
            [
                "git",
                "-C",
                str(repository_root),
                "archive",
                "--format=tar",
                f"{ref}^{{}}",
                prefix.rstrip("/"),
            ],
            check=True,
            capture_output=True,
        ).stdout
        members: list[dict[str, str]] = []
        with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:") as archive:
            for member in archive.getmembers():
                if not member.isfile() or not member.name.startswith(prefix):
                    continue
                extracted = archive.extractfile(member)
                if extracted is None:
                    raise ValueError("tagged standards member has no file bytes")
                members.append(
                    {
                        "path": member.name[len(prefix) :],
                        "sha256": hashlib.sha256(extracted.read()).hexdigest(),
                    }
                )
    except (subprocess.CalledProcessError, tarfile.TarError, ValueError):
        return [], [f"immutable STDO {label} standards inventory cannot be reacquired"]

    members.sort(key=lambda row: row["path"])
    if len(members) != identity["member_count"]:
        failures.append(f"immutable STDO {label} standards member count changed")
    member_stream = "".join(
        f'{row["sha256"]}  specification/standards/{row["path"]}\n' for row in members
    ).encode("utf-8")
    if hashlib.sha256(member_stream).hexdigest() != identity["member_set_sha256"]:
        failures.append(f"immutable STDO {label} standards member set changed")
    return members, failures


def audit(root: Path, axiom_root: Path) -> dict[str, Any]:
    failures: list[str] = []
    overlay = load_json(root / "stdo_representation.json")
    failures.extend(validate_overlay(overlay))

    installed_manifest_path = (
        Path.home()
        / "Library/Application Support/STDO/releases/v2.5.0-rc.4/manifest.json"
    )
    installed_manifest: dict[str, Any] = {}
    installed_manifest_sha256 = ""
    stdo_status_evidence: dict[str, Any] = {
        "command": "stdo status --definition stdo_representation.json --verify",
        "toolchain": None,
        "valid": False,
    }
    if not installed_manifest_path.is_file():
        failures.append("exact installed RC4 STDO manifest is unavailable")
    else:
        installed_manifest_bytes = installed_manifest_path.read_bytes()
        installed_manifest_sha256 = hashlib.sha256(installed_manifest_bytes).hexdigest()
        try:
            installed_manifest = json.loads(installed_manifest_bytes)
        except json.JSONDecodeError:
            failures.append("exact installed RC4 STDO manifest is not JSON")
        else:
            status_failures, stdo_status_evidence = validate_live_stdo_status(
                root,
                overlay,
                installed_manifest,
                installed_manifest_sha256,
            )
            failures.extend(status_failures)

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

    compression: dict[str, Any] = {}
    logical_index: dict[str, Any] = {}
    if all((root / path).is_file() for path in (PROGRAM_PATH, MAP_PATH)):
        compression = load_json(root / PROGRAM_PATH)
        logical_index = load_json(root / MAP_PATH)
        failures.extend(validate_program_map(compression, logical_index))
        failures.extend(validate_current_projection(compression, logical_index))

    if not (root / SOURCE_CORPUS_PATH).is_file():
        failures.append("missing complete RC4 source-corpus record")
    elif installed_manifest and compression and logical_index:
        source_corpus = load_json(root / SOURCE_CORPUS_PATH)
        failures.extend(
            validate_source_corpus(
                source_corpus,
                overlay,
                installed_manifest,
                installed_manifest_sha256,
                compression,
                logical_index,
            )
        )

        current_members = source_corpus.get("source_release", {}).get(
            "standards_members"
        )
        rc3_members, rc3_failures = immutable_stdo_standards_members(root, "RC3")
        failures.extend(rc3_failures)
        if rc3_members:
            rc3_delta = standards_member_delta(rc3_members, current_members)
            expected_rc3_delta = {
                "conserved": 49,
                "changed": [
                    "RELEASE_METHOD.md",
                    "authority_compressions/stdo_bootstrap.md",
                    "authority_compressions/stdo_compressed.md",
                ],
                "added": [],
                "removed": [],
            }
            if len(rc3_delta["conserved"]) != expected_rc3_delta["conserved"]:
                failures.append("RC3 to RC4 conserved-member count is not 49")
            for population in ("changed", "added", "removed"):
                if rc3_delta[population] != expected_rc3_delta[population]:
                    failures.append(f"RC3 to RC4 {population} member delta changed")

        rc2_members, rc2_failures = immutable_stdo_standards_members(root, "RC2")
        failures.extend(rc2_failures)
        baseline_path = root / CONSERVATION_BASELINE_PROGRAM_PATH
        if not baseline_path.is_file():
            failures.append("missing tracked RC2 semantic-conservation baseline")
        elif hashlib.sha256(baseline_path.read_bytes()).hexdigest() != (
            CONSERVATION_BASELINE_PROGRAM_SHA256
        ):
            failures.append("tracked RC2 semantic-conservation baseline changed")
        elif rc2_members:
            rc2_delta = standards_member_delta(rc2_members, current_members)
            expected_rc2_delta = {
                "conserved": 47,
                "changed": [
                    "RELEASE_METHOD.md",
                    "TICKET_METHOD.md",
                    "authority_compressions/stdo_bootstrap.md",
                    "authority_compressions/stdo_compressed.md",
                    "authority_compressions/ticket_method.compressed.md",
                ],
                "added": [],
                "removed": [],
            }
            if len(rc2_delta["conserved"]) != expected_rc2_delta["conserved"]:
                failures.append("RC2 to RC4 conserved-member count is not 47")
            for population in ("changed", "added", "removed"):
                if rc2_delta[population] != expected_rc2_delta[population]:
                    failures.append(f"RC2 to RC4 {population} member delta changed")
            failures.extend(
                validate_program_conservation(
                    load_json(baseline_path), compression, set(rc2_delta["changed"])
                )
            )

    failures.extend(
        validate_validation_report(
            root / VALIDATION_REPORT_PATH,
            compression,
            logical_index,
        )
    )

    failures.extend(validate_axiom_candidate(axiom_root, REPRESENTATION_VERSION))
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
            "Source STDO 2.5.0 (exact cut v2.5.0-rc.4)",
            "axiom_indexer/v2.5.0-rc.4",
        ],
        "specification/PRODUCT.md": [
            "eight repository entries",
            "adds no local",
            "representation_exact_version = represented_stdo_exact_version",
            "local_release_key = stdo_representation",
            "Project Subtree root",
            "do not become Product meaning or membership",
        ],
        "skills/stdo-representation/SKILL.md": [
            'git -C "$stack_root" archive --format=tar "$axiom_ref"',
            'test -f "$axiom_root/build_tenants/core/code/ac.py"',
            "dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672",
            "authorized commit-B construction may use the sibling candidate",
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
            "exact_version": REPRESENTATION_VERSION,
            "version_line": REPRESENTATION_VERSION_LINE,
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
            "exact_version": REPRESENTATION_VERSION,
            "version_line": REPRESENTATION_VERSION_LINE,
            "release_record": CANDIDATE_RELEASE_PATH.as_posix(),
            "release_record_sha256": "sha256:" + CANDIDATE_RELEASE_SHA256,
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
        "stdo_status": stdo_status_evidence,
    }


def parse_args() -> argparse.Namespace:
    default_axiom = ROOT.parent / "axiom_indexer"
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
