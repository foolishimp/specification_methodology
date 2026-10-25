"""Prepare a fresh read-only public-interface example; grant no Product work.

This is operator setup, not an admission mechanism. It registers no executor,
work grant or semantic producer. A trusted operator remains responsible for the
selected source roots and fixed principals. No model or provider is invoked.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import cast

CODE = Path(__file__).resolve().parents[2] / "code"
sys.path.insert(0, str(CODE))
import ac_support_core as core  # noqa: E402
from ac_support_core import JSON, Object  # noqa: E402


READ_OPERATIONS = (
    "tools.describe", "workspace.observe", "source.read", "records.find",
    "records.read", "graph.project", "relations.query", "evidence.read", "work.project",
)
NOTICE = """# Read-only acquisition example

This file is operator-authored demonstration configuration. It supplies no
Product work grant, owner admission, independent review, semantic verdict,
acceptance or release authority. The three example principals are local tool
identities, not actual LLM producers or independent assessors.

The operator permits only the selected discovery/acquisition/query operations
over the explicitly configured read roots. Work grants and executors are empty.
The Product admission binding contains an unqualified all-zero implementation
digest: it is a required configuration placeholder, never a working mechanism
or a replacement for the Product's existing authorized binding.

Preflight, dispatch and authoritative writing are denied. Real work requires a
separately established Product-located owner binding, actual existing grant,
exact implementation and executor identities, current inputs, durable result
surface and applicable method contract. No fields in this example create them.
"""


def _write_json(path: Path, value: JSON) -> bytes:
    raw = (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n").encode("utf-8")
    with path.open("xb") as stream:
        stream.write(raw)
    return raw


def _source(root: str, path: str, raw: bytes) -> Object:
    return {"engine": "workspace-regular-file", "root": root, "path": path,
            "object": None, "sha256": hashlib.sha256(raw).hexdigest(), "selector": None}


def _request(identity: str, operation: str, arguments: Object) -> Object:
    return {"schema": core.REQUEST, "id": identity, "operation": operation, "arguments": arguments}


def prepare(output: Path, product_root: Path, *, profile: str = "claude-rc9", definition_name: str = "stdo_a_c.json") -> Object:
    """Create only a new operator-selected example directory."""
    output = output.absolute()
    product_root = product_root.resolve(strict=True)
    if output.exists() or output.is_symlink():
        raise ValueError("Example output must be a fresh path; existing evidence is never overwritten")
    # The trusted setup selects the real new directory once, before policy or
    # SourceRef hashes exist. Runtime paths still refuse symlink aliases.
    output = output.resolve(strict=False)
    core._relative(definition_name)
    definition_raw = (product_root / definition_name).read_bytes()
    definition = cast(Object, core.parse_json(definition_raw))
    product_id = cast(str, cast(Object, definition["product"])["definition_id"])
    native = profile == "stdo-3.0.1"
    if profile not in ("claude-rc9", "stdo-3.0.1"):
        raise ValueError("Select one explicit supported profile")
    tool_root = Path(__file__).resolve().parents[4]
    profile_path = "build_tenants/graphify/design/fd-method-" + ("stdo-3.0.1" if native else "claude-rc9") + ".json"
    profile_raw = (tool_root / profile_path).read_bytes()
    profile_id = core.NATIVE_PROFILE_ID if native else core.PROFILE_ID
    profile_sha = core.NATIVE_PROFILE_SHA256 if native else core.PROFILE_SHA256
    if native and core.pointer(definition, "/constitution/stdo/basis") != {"uri": "stdo://releases/v3.0.1-rc.1/", "manifest_sha256": core.NATIVE_MANIFEST_SHA256}:
        raise ValueError("Native setup requires the exact released 3.0.1 Product basis")
    if hashlib.sha256(profile_raw).hexdigest() != profile_sha:
        raise ValueError("The selected source does not contain the exact supported Claude RC9 profile")
    design_path = "build_tenants/graphify/design/fd-support.md"
    design_raw = (tool_root / design_path).read_bytes()
    definition_ref = _source("product", definition_name, definition_raw)
    profile_ref = _source("tool", profile_path, profile_raw)
    design_ref = _source("tool", design_path, design_raw)
    implementation_path = "build_tenants/graphify/code/ac_support_core.py"
    implementation_raw = (tool_root / implementation_path).read_bytes()
    implementation_ref = _source("tool", implementation_path, implementation_raw)
    notice = NOTICE
    if native:
        notice = notice.replace("an unqualified all-zero implementation\ndigest", "the actual current implementation\ndigest")
    operator_ref = _source("operator", "OPERATOR.md", notice.encode("utf-8"))
    evidence_root = output / "evidence"
    principals: Object = {}
    for role in ("Executive", "Worker", "Reviewer"):
        principals[role.lower()] = {
            "actor_id": "urn:a-c:fd-support:read-only-example:" + role.lower(),
            "role": role, "family": "example-no-model", "authorship": "operator-example",
            "operations": list(READ_OPERATIONS), "role_binding": operator_ref, "role_transition": None,
        }
    policy: Object = {
        "schema": "a_c.fd-support.policy/1", "id": "urn:a-c:fd-support:read-only-example",
        "product": {
            "definition_id": product_id, "definition": definition_ref,
            "authority_binding": {
                "definition_locator": "/reference_frame_bases/0/authority/0",
                "owner_record": operator_ref,
                "mechanism": {"id": "product-policy-preflight/1", "source": implementation_ref if native else design_ref,
                              "implementation_sha256": hashlib.sha256(implementation_raw).hexdigest() if native else "0" * 64},
                "result_surface": {"root": str(evidence_root), "namespace": "readonly-demo", "consumer": "read-only-example"},
                "scope": {"kind": "read-only-example", "Product_work_authority": False},
            },
        },
        "method_profile": {"id": profile_id, "sha256": profile_sha, "source": profile_ref},
        "sources": {
            "product": {
                "path": str(product_root), "kind": "workspace", "writable": False,
                "read_scope": [
                    {"path": definition_name, "kind": "file"},
                    {"path": "specification", "kind": "directory"},
                    {"path": "build_tenants/graphify/design", "kind": "directory"},
                    {"path": "build_tenants/graphify/test_env/fixtures/toy_model.json", "kind": "file"},
                    {"path": "build_tenants/graphify/examples/subject.md", "kind": "file"},
                ],
            },
            "tool": {"path": str(tool_root), "kind": "workspace", "writable": False,
                     "read_scope": [{"path": profile_path, "kind": "file"}, {"path": design_path, "kind": "file"}, {"path": implementation_path, "kind": "file"}]},
            "operator": {"path": str(output / "control"), "kind": "workspace", "writable": False,
                         "read_scope": [{"path": "OPERATOR.md", "kind": "file"}]},
        },
        "principals": principals,
        "grants": {}, "predicates": {}, "operators": {}, "executors": {}, "event_sinks": {},
        "independence_policy": None, "evidence_root": str(evidence_root),
        "limits": {"max_message_bytes": 1_048_576, "max_files": 1024, "max_bytes": 8_388_608,
                   "max_history_records": 10000, "max_wait_ms": 1000},
        "authority_sources": [operator_ref],
    }
    requests: dict[str, Object] = {
        "describe.json": _request("readonly-describe-001", "tools.describe", {}),
        "read-product.json": _request("readonly-product-001", "source.read", {"source": definition_ref, "encoding": "utf8"}),
        "observe.json": _request("readonly-observe-001", "workspace.observe", {
            "scope": [{"root": "product", "path": definition_name, "kind": "file"}],
        }),
        "denied-preflight.json": _request("readonly-denied-001", "contract.preflight", {
            "context": {"id": "sha256:" + "0" * 64, "sha256": "0" * 64},
            "grant_id": "no-grant-is-registered", "executor_id": "no-executor-is-registered",
            "result_key": "no-result-is-admitted", "observations": [],
        }),
    }
    for request in requests.values():
        core.validate_request(request)
    output.mkdir(mode=0o700)
    (output / "control").mkdir()
    (output / "requests").mkdir()
    evidence_root.mkdir()
    (output / "control" / "OPERATOR.md").write_bytes(notice.encode("utf-8"))
    policy_raw = _write_json(output / "policy.json", policy)
    for name, request in requests.items():
        _write_json(output / "requests" / name, request)
    session: list[Object] = [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
            "protocolVersion": "2025-11-25", "capabilities": {},
            "clientInfo": {"name": "ordinary-readonly-example", "version": "1"},
        }},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
        {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {
            "name": "source.read", "arguments": requests["read-product.json"],
        }},
    ]
    with (output / "mcp-session.jsonl").open("xb") as stream:
        for message in session:
            stream.write(core.canonical(message) + b"\n")
    summary: Object = {
        "schema": "a_c.fd-support.read-only-example/1", "output": str(output),
        "policy": str(output / "policy.json"), "policy_sha256": hashlib.sha256(policy_raw).hexdigest(),
        "principals": ["executive", "worker", "reviewer"], "permitted_operations": list(READ_OPERATIONS),
        "Product_work_grants": 0, "registered_executors": 0, "model_calls": 0,
        "qualification": "Operator setup only; no admission, independent review, Product acceptance or benefit claim",
    }
    _write_json(output / "SETUP.json", summary)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path, help="Fresh directory beneath an existing parent")
    parser.add_argument("--product-root", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--profile", choices=("claude-rc9", "stdo-3.0.1"), default="claude-rc9")
    parser.add_argument("--definition-name", default="stdo_a_c.json", help="Product-relative exact definition path")
    args = parser.parse_args()
    try:
        result = prepare(cast(Path, args.out), cast(Path, args.product_root), profile=args.profile, definition_name=args.definition_name)
        print(core.canonical(result).decode("utf-8"))
        return 0
    except (OSError, ValueError, core.SupportError, KeyError) as exc:
        print(f"Read-only setup refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
