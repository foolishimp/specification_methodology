"""Public JSON CLI and legacy MCP stdio projection of a_c support tools.

The core owns schemas and deterministic relations; effects owns persistence,
admission and external effects. This adapter supplies neither work authority
nor semantic judgments. MCP support is pinned to revision 2025-11-25.
"""
from __future__ import annotations

import argparse
from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import hashlib
import json
import sys
from pathlib import Path
import time
from typing import BinaryIO, NoReturn, TypeAlias, cast

import ac_support_core as core
import ac_support_effects as effects
from ac_support_core import JSON, Object


PROTOCOL_VERSION = "2025-11-25"
SERVER_VERSION = "0.1.0"
RESPONSE_SCHEMA = "a_c.fd-support.response/1"
# Only the pre-policy protocol guard uses this bound. Once a trusted policy is
# loaded, its explicit max_message_bytes is the selected transport bound.
BOOTSTRAP_MAX_MESSAGE_BYTES = 1_048_576


@dataclass(frozen=True)
class _Number:
    """A finite transport number with its decimal/exponent token preserved."""
    lexeme: str

    def __post_init__(self) -> None:
        if not Decimal(self.lexeme).is_finite():
            raise ValueError("Nonfinite transport number")


Wire: TypeAlias = None | bool | int | str | _Number | list["Wire"] | dict[str, "Wire"]
WireObject: TypeAlias = dict[str, Wire]


def _wire_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate transport key")
        result[key] = value
    return result


def _nonfinite(token: str) -> object:
    raise ValueError("Nonfinite transport token: " + token)


def _wire_value(value: object, depth: int = 0) -> Wire:
    if depth > 128:
        raise ValueError("Transport JSON exceeds the finite nesting bound")
    if value is None or type(value) in (bool, int) or isinstance(value, _Number):
        return cast(Wire, value)
    if isinstance(value, str):
        value.encode("utf-8")
        return value
    if isinstance(value, list):
        return [_wire_value(item, depth + 1) for item in value]
    if isinstance(value, dict) and all(isinstance(key, str) for key in value):
        return {key: _wire_value(item, depth + 1) for key, item in value.items()}
    raise ValueError("Unsupported transport JSON value")


def _parse_wire(raw: bytes) -> Wire:
    value: object = json.loads(raw.decode("utf-8"), object_pairs_hook=_wire_pairs,
                               parse_float=_Number, parse_constant=_nonfinite)
    return _wire_value(value)


def _wire_bytes(value: object) -> bytes:
    if value is None:
        return b"null"
    if type(value) is bool:
        return b"true" if value else b"false"
    if type(value) is int:
        return str(value).encode("ascii")
    if isinstance(value, _Number):
        return value.lexeme.encode("ascii")
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False).encode("utf-8")
    if isinstance(value, list):
        return b"[" + b",".join(_wire_bytes(item) for item in value) + b"]"
    if isinstance(value, dict) and all(isinstance(key, str) for key in value):
        return b"{" + b",".join(_wire_bytes(key) + b":" + _wire_bytes(item)
                                 for key, item in sorted(value.items())) + b"}"
    raise ValueError("Cannot serialize unsupported/nonfinite transport value")


def _unretained_response(error: core.SupportError, *, request: Object | None = None) -> Object:
    """Describe an unavailable boundary without claiming a durable reference."""
    failed = error.code in {
        "internal_failure", "observation_unavailable", "evidence_publication_failed",
        "effect_unreconciled", "effect_completion_unknown",
    }
    diagnostic = error.document()
    gaps = cast(list[JSON], diagnostic["gaps"])
    diagnostic["gaps"] = [*gaps, {"unretained_scope": "no complete durable response evidence"}]
    return {
        "schema": RESPONSE_SCHEMA,
        "id": request["id"] if request is not None else None,
        "operation": request["operation"] if request is not None else None,
        "status": "error" if failed else "refused",
        "result": None,
        "refusal": diagnostic,
        "operation_outcome": None,
        "evidence": None,
    }


def execute(runtime: core.Runtime, request: JSON) -> Object:
    """Use one core catalog and the sole effect/retention boundaries."""
    try:
        bound = core.validate_request(request)
    except core.SupportError as exc:
        return _unretained_response(exc)
    try:
        operation = cast(str, bound["operation"])
        if operation == "contract.preflight":
            outcome = effects.execute_effect(runtime, bound, core.build_preflight(runtime, bound))
        elif operation == "work.write":
            outcome = effects.execute_effect(runtime, bound, None)
        elif operation in core.EFFECT_OPERATIONS:
            outcome = effects.execute_effect(runtime, bound, None)
        else:
            outcome = core.execute_read(runtime, bound)
    except core.SupportError as exc:
        outcome = core.refusal_outcome(runtime, bound, exc)
    except Exception as exc:
        outcome = core.refusal_outcome(runtime, bound, core.SupportError(
            "internal_failure", "Unexpected operation failure; no semantic result is inferred",
            gaps=[{"exception": type(exc).__name__, "reason": str(exc)}],
        ))
    try:
        return effects.persist_outcome(runtime, bound, outcome)
    except core.SupportError as exc:
        # Persistence owns the normal failed-publication projection. This is a
        # last-resort diagnostic only: never retry an effect or advertise an
        # unpublished content hash as durable evidence.
        return _unretained_response(exc, request=bound)
    except Exception as exc:
        return _unretained_response(core.SupportError(
            "evidence_publication_failed", "Response evidence could not be retained",
            gaps=[{"exception": type(exc).__name__, "reason": str(exc),
                   "effect_state": "unknown; acquire existing intent and observations before retry"}],
        ), request=bound)


def _load_runtime(policy: str, expected_sha256: str, principal: str) -> core.Runtime:
    runtime = core.Runtime.from_policy(policy, expected_sha256, principal)
    store = effects.EvidenceStore(runtime)
    return runtime.with_callbacks(store.resolve, store.query_artifacts)


def _message_limit(runtime: core.Runtime) -> int:
    limits = cast(Object, runtime.policy["limits"])
    value = limits["max_message_bytes"]
    if type(value) is not int or value < 1:
        raise core.SupportError("contract_violation", "Policy max_message_bytes must be a positive integer")
    return value


def _write(stream: BinaryIO, value: object) -> tuple[bytes, Object]:
    raw = _wire_bytes(value) + b"\n"
    started = time.time_ns()
    written = 0
    while written < len(raw):
        count = stream.write(raw[written:])
        if count is None or count <= 0:
            raise OSError("Transport did not write the complete message")
        written += count
    stream.flush()
    return raw, {"clock": "unix_ns", "started_ns": started, "ended_ns": time.time_ns()}


def _deliver(runtime: core.Runtime, request: Object, response: Object,
             target: BinaryIO, *, wire: WireObject | None = None) -> None:
    raw, interval = _write(target, response if wire is None else wire)
    if response.get("evidence") is None:
        return
    try:
        # This pure builder re-acquires the protected OperationEvidence and
        # selects only actual public-response acquisitions. A Context summary
        # cannot attest delivery of its retained actor-context body.
        event = core.transport_observation(runtime, request, response, interval,
                                           hashlib.sha256(raw).hexdigest(), len(raw))
        effects.EvidenceStore(runtime).retain(event)
    except Exception as exc:
        # The response was already written. Missing publication keeps delivery
        # potential/unknown in protected history; never patch a prior envelope,
        # emit another public result or silently retry persistence.
        print(f"Transport observation unavailable; delivery evidence remains unknown: {type(exc).__name__}: {exc}", file=sys.stderr)


def _rpc_error(request_id: Wire, code: int, message: str) -> WireObject:
    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}


def _rpc_result(request_id: Wire, value: Object) -> WireObject:
    return {"jsonrpc": "2.0", "id": request_id, "result": cast(Wire, value)}


def _tool_entries(runtime: core.Runtime | None = None) -> list[JSON]:
    result: list[JSON] = []
    entries = cast(list[JSON], core.inventory(profile=None if runtime is None else runtime.method_profile)["operations"])
    for entry in entries:
        contract = cast(Object, entry)
        name = cast(str, contract["name"])
        fragment = contract["checked_fragment"]
        description = fragment if isinstance(fragment, str) else core.canonical(fragment).decode("utf-8")
        result.append({
            "name": name,
            "description": description,
            "inputSchema": core.request_schema(name),
            "outputSchema": contract["output_schema"],
        })
    return sorted(result, key=lambda item: cast(str, cast(Object, item)["name"]))


def _initialize_params(value: Wire) -> bool:
    if not isinstance(value, dict):
        return False
    if set(value) - {"protocolVersion", "capabilities", "clientInfo", "_meta"}:
        return False
    if not isinstance(value.get("protocolVersion"), str) or not value["protocolVersion"]:
        return False
    if not isinstance(value.get("capabilities"), dict):
        return False
    info = value.get("clientInfo")
    return (isinstance(info, dict) and isinstance(info.get("name"), str)
            and bool(info["name"]) and isinstance(info.get("version"), str)
            and bool(info["version"]) and ("_meta" not in value or isinstance(value["_meta"], dict)))


def serve_mcp(
    runtime: core.Runtime | None,
    source: BinaryIO,
    target: BinaryIO,
    *,
    startup_error: core.SupportError | None = None,
) -> int:
    """Serve the finite legacy protocol; protocol ids never become work ids."""
    maximum = _message_limit(runtime) if runtime is not None else BOOTSTRAP_MAX_MESSAGE_BYTES
    initializing = False
    initialized = False
    tools = _tool_entries(runtime) if runtime is not None else []
    names = {cast(str, cast(Object, tool)["name"]) for tool in tools}
    while True:
        raw = source.readline(maximum + 1)
        if not raw:
            return 0 if startup_error is None else 2
        if len(raw) > maximum:
            _write(target, _rpc_error(None, -32700, "Message exceeds the selected byte boundary"))
            return 2
        try:
            value = _parse_wire(raw)
        except (ValueError, UnicodeError, RecursionError, InvalidOperation):
            _write(target, _rpc_error(None, -32700, "Invalid UTF-8 or finite JSON message"))
            continue
        if not isinstance(value, dict):
            _write(target, _rpc_error(None, -32600, "Expected one JSON-RPC object"))
            continue
        has_id = "id" in value
        request_id = value.get("id")
        valid_id = type(request_id) in (str, int) or isinstance(request_id, _Number)
        method = value.get("method")
        if (value.get("jsonrpc") != "2.0" or not isinstance(method, str)
                or set(value) - {"jsonrpc", "id", "method", "params"}
                or (has_id and not valid_id)):
            _write(target, _rpc_error(request_id if valid_id else None, -32600, "Invalid JSON-RPC request"))
            continue
        params = value.get("params", {})
        if not isinstance(params, dict):
            if has_id:
                _write(target, _rpc_error(request_id, -32602, "MCP parameters must be an object"))
            continue
        if "_meta" in params and not isinstance(params["_meta"], dict):
            if has_id:
                _write(target, _rpc_error(request_id, -32602, "MCP _meta must be an object"))
            continue
        if not has_id:
            if method == "notifications/initialized" and initializing and not initialized:
                if not set(params) - {"_meta"} and ("_meta" not in params or isinstance(params["_meta"], dict)):
                    initialized = True
            # A notification never launches a named tool, including tools/call.
            continue
        if method == "initialize":
            if initializing or not _initialize_params(params):
                _write(target, _rpc_error(request_id, -32602, "Invalid or repeated initialize"))
            elif startup_error is not None:
                _write(target, {"jsonrpc": "2.0", "id": request_id, "error": {
                    "code": -32002, "message": "Trusted runtime initialization failed",
                    "data": cast(Wire, startup_error.document()),
                }})
                return 1 if startup_error.code in {"internal_failure", "observation_unavailable", "evidence_publication_failed"} else 2
            else:
                initializing = True
                _write(target, _rpc_result(request_id, {
                    "protocolVersion": PROTOCOL_VERSION,
                    "capabilities": {"tools": {"listChanged": False}},
                    "serverInfo": {"name": "a_c.graphify.fd-support", "version": SERVER_VERSION},
                    "instructions": "Each tool takes the full a_c.fd-support.request/1 envelope. Keep its caller id stable for an exact retry. Discover authority, checked fragments and unsupported variants with tools.describe.",
                }))
            continue
        if method == "ping":
            if set(params) - {"_meta"}:
                _write(target, _rpc_error(request_id, -32602, "ping has no operation parameters"))
            else:
                _write(target, _rpc_result(request_id, {}))
            continue
        if not initialized:
            _write(target, _rpc_error(request_id, -32002, "initialize and notifications/initialized are required"))
            continue
        if method == "tools/list":
            if set(params) - {"_meta"}:
                _write(target, _rpc_error(request_id, -32602, "No pagination cursor is valid for this complete finite inventory"))
            else:
                _write(target, _rpc_result(request_id, {"tools": tools}))
            continue
        if method != "tools/call":
            _write(target, _rpc_error(request_id, -32601, "Unsupported protocol method"))
            continue
        if set(params) - {"name", "arguments", "_meta"} or not isinstance(params.get("name"), str):
            _write(target, _rpc_error(request_id, -32602, "Invalid tools/call parameters"))
            continue
        name = cast(str, params["name"])
        if name not in names:
            _write(target, _rpc_error(request_id, -32602, "Unknown tool"))
            continue
        try:
            # Reparse the actual full sub-envelope through the strict public
            # grammar. _Number preserves 1.0/1e0, including integral values;
            # legal outer metadata can never weaken the operation grammar.
            request = core.parse_request(_wire_bytes(params.get("arguments")))
        except core.SupportError as exc:
            _write(target, _rpc_error(request_id, -32602, exc.reason))
            continue
        if request["operation"] != name:
            _write(target, _rpc_error(request_id, -32602, "Tool name differs from full-envelope operation"))
            continue
        assert runtime is not None
        response = execute(runtime, request)
        wire = _rpc_result(request_id, {
            "content": [{"type": "text", "text": core.canonical(response).decode("utf-8")}],
            "structuredContent": response,
            "isError": response["status"] != "ok",
        })
        _deliver(runtime, request, response, target, wire=wire)


class _Parser(argparse.ArgumentParser):
    def error(self, message: str) -> NoReturn:
        raise core.SupportError("malformed_request", message)


def _startup_options(parser: argparse.ArgumentParser, *, required: bool = False) -> None:
    parser.add_argument("--policy", required=required, help="Trusted operator-selected policy JSON path")
    parser.add_argument("--policy-sha256", required=required, help="Exact expected policy byte digest")
    parser.add_argument("--principal", required=required, help="Fixed operator-selected requester principal")


def _parser() -> argparse.ArgumentParser:
    parser = _Parser(description=__doc__)
    _startup_options(parser)
    commands = parser.add_subparsers(dest="command", required=True, parser_class=_Parser)
    call = commands.add_parser("call", help="Execute one full JSON request")
    call.add_argument("--request", required=True, help="Request JSON file or - for stdin")
    commands.add_parser("mcp", help="Serve legacy MCP2025-11-25 over stdin/stdout")
    supervisor = commands.add_parser("_supervise", help=argparse.SUPPRESS)
    _startup_options(supervisor, required=True)
    supervisor.add_argument("--attempt-id", required=True)
    supervisor.add_argument("--attempt-sha256", required=True)
    return parser


def _exit_status(response: Object) -> int:
    return 0 if response["status"] == "ok" else 2 if response["status"] == "refused" else 1


def main(argv: Sequence[str] | None = None) -> int:
    """Run an operator-started CLI/server without altering host configuration."""
    try:
        args = _parser().parse_args(argv)
        if not all(isinstance(getattr(args, key), str) and getattr(args, key)
                   for key in ("policy", "policy_sha256", "principal")):
            raise core.SupportError("malformed_request", "--policy, --policy-sha256 and --principal are required")
    except core.SupportError as exc:
        response = _unretained_response(exc)
        _write(sys.stdout.buffer, response)
        return _exit_status(response)
    request: Object | None = None
    try:
        runtime = _load_runtime(cast(str, args.policy), cast(str, args.policy_sha256), cast(str, args.principal))
    except Exception as exc:
        error = exc if isinstance(exc, core.SupportError) else core.SupportError(
            "observation_unavailable", "Trusted runtime could not be acquired",
            gaps=[{"exception": type(exc).__name__, "reason": str(exc)}],
        )
        if args.command == "mcp":
            print(error.reason, file=sys.stderr)
            return serve_mcp(None, sys.stdin.buffer, sys.stdout.buffer, startup_error=error)
        if args.command == "_supervise":
            print(error.reason, file=sys.stderr)
            return 1
        response = _unretained_response(error)
        _write(sys.stdout.buffer, response)
        return _exit_status(response)
    if args.command == "_supervise":
        try:
            return effects.supervise(runtime, {"id": cast(str, args.attempt_id), "sha256": cast(str, args.attempt_sha256)})
        except Exception as exc:
            print(f"Supervisor reentry failed: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 1
    if args.command == "mcp":
        try:
            return serve_mcp(runtime, sys.stdin.buffer, sys.stdout.buffer)
        except (BrokenPipeError, KeyboardInterrupt):
            return 1
    try:
        maximum = _message_limit(runtime)
        if args.request == "-":
            raw = sys.stdin.buffer.read(maximum + 1)
        else:
            with Path(cast(str, args.request)).open("rb") as source:
                raw = source.read(maximum + 1)
        if len(raw) > maximum:
            raise core.SupportError("malformed_request", "Request exceeds selected max_message_bytes")
        request = core.parse_request(raw)
        response = execute(runtime, request)
    except core.SupportError as exc:
        response = _unretained_response(exc)
    except Exception as exc:
        response = _unretained_response(core.SupportError(
            "observation_unavailable", "Request input could not be acquired",
            gaps=[{"exception": type(exc).__name__, "reason": str(exc)}],
        ))
    try:
        if request is None:
            _write(sys.stdout.buffer, response)
        else:
            _deliver(runtime, request, response, sys.stdout.buffer)
    except BrokenPipeError:
        return 1
    return _exit_status(response)


if __name__ == "__main__":
    raise SystemExit(main())
