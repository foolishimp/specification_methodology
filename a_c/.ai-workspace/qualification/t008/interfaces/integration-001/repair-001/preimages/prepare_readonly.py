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


def prepare(output: Path, product_root: Path) -> Object:
    """Create only a new operator-selected example directory."""
    output = output.absolute()
    product_root = product_root.resolve(strict=True)
    if output.exists() or output.is_symlink():
        raise ValueError("Example output must be a fresh path; existing evidence is never overwritten")
    definition_raw = (product_root / "stdo_a_c.json").read_bytes()
    definition = cast(Object, core.parse_json(definition_raw))
    product_id = cast(str, cast(Object, definition["product"])["definition_id"])
    profile_path = "build_tenants/graphify/design/fd-method-claude-rc9.json"
    profile_raw = (product_root / profile_path).read_bytes()
    if hashlib.sha256(profile_raw).hexdigest() != core.PROFILE_SHA256:
        raise ValueError("The selected source does not contain the exact supported Claude RC9 profile")
    design_path = "build_tenants/graphify/design/fd-support.md"
    design_raw = (product_root / design_path).read_bytes()
    definition_ref = _source("product", "stdo_a_c.json", definition_raw)
    profile_ref = _source("product", profile_path, profile_raw)
    design_ref = _source("product", design_path, design_raw)
    operator_ref = _source("operator", "OPERATOR.md", NOTICE.encode("utf-8"))
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
                "mechanism": {"id": "product-policy-preflight/1", "source": design_ref,
                              "implementation_sha256": "0" * 64},
                "result_surface": {"root": str(evidence_root), "namespace": "readonly-demo", "consumer": "read-only-example"},
                "scope": {"kind": "read-only-example", "Product_work_authority": False},
            },
        },
        "method_profile": {"id": core.PROFILE_ID, "sha256": core.PROFILE_SHA256, "source": profile_ref},
        "sources": {
            "product": {
                "path": str(product_root), "kind": "workspace", "writable": False,
                "read_scope": [
                    {"path": "stdo_a_c.json", "kind": "file"},
                    {"path": "specification", "kind": "directory"},
                    {"path": "build_tenants/graphify/design", "kind": "directory"},
                    {"path": "build_tenants/graphify/test_env/fixtures/toy_model.json", "kind": "file"},
                    {"path": "build_tenants/graphify/examples/subject.md", "kind": "file"},
                ],
            },
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
            "scope": [{"root": "product", "path": "stdo_a_c.json", "kind": "file"}],
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
    (output / "control" / "OPERATOR.md").write_bytes(NOTICE.encode("utf-8"))
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
    args = parser.parse_args()
    try:
        result = prepare(cast(Path, args.out), cast(Path, args.product_root))
        print(core.canonical(result).decode("utf-8"))
        return 0
    except (OSError, ValueError, core.SupportError, KeyError) as exc:
        print(f"Read-only setup refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
