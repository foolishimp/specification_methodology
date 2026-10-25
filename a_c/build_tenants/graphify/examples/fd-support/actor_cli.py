"""Optional transport-only executor for an operator-pinned Claude/Codex CLI.

No provider, model, prompt, work grant or semantic answer is selected here.
Register this fixed helper/plan/dependency chain in an actual admitted Attempt
to obtain that outer tool's authentication; a direct run authenticates nothing.
"""
from __future__ import annotations

import argparse
from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
import hashlib
import json
import os
from pathlib import Path
import selectors
import stat
import subprocess
import sys
import time
from typing import BinaryIO, cast

CODE = Path(__file__).resolve().parents[2] / "code"
sys.path.insert(0, str(CODE))
import ac_support_core as core  # noqa: E402
from ac_support_core import JSON, Object  # noqa: E402


SCHEMA = "a_c.fd-support.actor-cli-plan/1"
DECODERS = {"claude-result-json/1": "claude", "claude-result-jsonl/1": "claude", "codex-final-jsonl/1": "codex"}


class TransportError(ValueError):
    """A transport/plan failure, never a semantic Worker or review result."""


def _object(value: JSON) -> Object:
    if not isinstance(value, dict):
        raise TransportError("Expected an object")
    return value


def _text(value: JSON) -> str:
    if not isinstance(value, str) or not value or "\0" in value:
        raise TransportError("Expected a nonempty string without NUL")
    return value


def _integer(value: JSON) -> int:
    if type(value) is not int or value < 1:
        raise TransportError("Expected a positive integer bound")
    return value


def _keys(value: Object, expected: tuple[str, ...]) -> None:
    if set(value) != set(expected):
        raise TransportError("Unknown or missing plan fields")


def _path(value: JSON) -> Path:
    path = Path(_text(value))
    if not path.is_absolute() or ".." in path.parts:
        raise TransportError("Operator paths must be absolute and exact")
    for ancestor in (*reversed(path.parents), path):
        if ancestor.is_symlink():
            raise TransportError("Symlink components are unsupported in pinned actor paths")
    return path


def _regular(path: Path) -> bytes:
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(path, flags)
    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise TransportError("Pinned dependency is not a regular file")
        with os.fdopen(descriptor, "rb", closefd=False) as stream:
            return stream.read()
    finally:
        os.close(descriptor)


def _pin(value: JSON) -> Object:
    pin = _object(value)
    _keys(pin, ("path", "sha256"))
    path = _path(pin["path"])
    expected = _text(pin["sha256"])
    if len(expected) != 64 or any(char not in "0123456789abcdef" for char in expected):
        raise TransportError("Dependency digest must be lowercase SHA-256")
    if hashlib.sha256(_regular(path)).hexdigest() != expected:
        raise TransportError("Pinned executable/dependency bytes changed: " + str(path))
    return pin


@dataclass(frozen=True)
class Plan:
    path: Path
    sha256: str
    raw: bytes
    document: Object


def load_plan(path: Path, expected_sha256: str) -> Plan:
    path = _path(str(path.absolute()))
    raw = _regular(path)
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise TransportError("Plan differs from the operator's expected byte digest")
    value = _object(core.parse_json(raw))
    _keys(value, ("schema", "id", "backend", "executable", "argv", "dependencies", "cwd", "environment",
                  "settings", "decoder", "evidence_directory", "limits"))
    if value["schema"] != SCHEMA or value["backend"] not in ("claude", "codex"):
        raise TransportError("Unsupported actor plan/backend")
    _text(value["id"])
    executable = _pin(value["executable"])
    if not isinstance(value["argv"], list) or not value["argv"]:
        raise TransportError("Complete fixed argv is required")
    argv = [_text(item) for item in value["argv"]]
    if argv[0] != executable["path"]:
        raise TransportError("argv[0] must equal the pinned executable")
    dependencies = value["dependencies"]
    if not isinstance(dependencies, list):
        raise TransportError("Dependencies must be an explicit array")
    seen: set[str] = set()
    for dependency in dependencies:
        pinned = _pin(dependency)
        name = _text(pinned["path"])
        if name in seen:
            raise TransportError("Duplicate dependency path")
        seen.add(name)
    cwd = _path(value["cwd"])
    if not cwd.is_dir():
        raise TransportError("Registered working directory is unavailable")
    environment = _object(value["environment"])
    for name, item in environment.items():
        if not name or "=" in name or "\0" in name or not isinstance(item, str) or "\0" in item:
            raise TransportError("Environment must be an explicit string map")
        if name in {"HOME", "home", "CODEX_HOME"}:
            raise TransportError("HOME/home/CODEX_HOME overrides are unsupported")
    inherited_names = core.environment_passthrough(value["settings"], environment)
    if inherited_names and value["backend"] != "claude":
        raise TransportError("The selected credential pass-through is supported only for the Claude backend")
    if DECODERS.get(_text(value["decoder"])) != value["backend"]:
        raise TransportError("Decoder does not match the fixed backend")
    _path(value["evidence_directory"])
    limits = _object(value["limits"])
    _keys(limits, ("max_input_bytes", "max_output_bytes", "timeout_ms", "termination_grace_ms"))
    for item in limits.values():
        _integer(item)
    return Plan(path, expected_sha256, raw, value)


def _write_all(stream: BinaryIO, raw: bytes) -> None:
    position = 0
    while position < len(raw):
        written = stream.write(raw[position:])
        if written is None or written <= 0:
            raise OSError("Incomplete transport evidence write")
        position += written


def _save(path: Path, raw: bytes) -> None:
    with path.open("xb") as stream:
        _write_all(stream, raw)
        stream.flush()
        os.fsync(stream.fileno())


def _save_json(path: Path, value: JSON) -> None:
    _save(path, core.canonical(value) + b"\n")


def _capture(plan: Plan, payload: bytes, output: Path, inherited: dict[str, str]) -> Object:
    value = plan.document
    limits = _object(value["limits"])
    maximum = _integer(limits["max_output_bytes"])
    timeout = _integer(limits["timeout_ms"]) / 1000
    grace = _integer(limits["termination_grace_ms"]) / 1000
    started = time.time_ns()
    process: subprocess.Popen[bytes] | None = None
    failure: str | None = None
    signals: list[JSON] = []
    counts = {"stdout": 0, "stderr": 0}
    eof = {"stdout": False, "stderr": False}
    forwarded = 0
    with (output / "vendor.stdout").open("xb", buffering=0) as stdout, (output / "vendor.stderr").open("xb", buffering=0) as stderr:
        selector = selectors.DefaultSelector()
        try:
            # Recheck the same frozen plan and all dependencies at the actual
            # launch edge. Neither a new prompt nor settings are appended.
            load_plan(plan.path, plan.sha256)
            process = subprocess.Popen(
                [_text(item) for item in cast(list[JSON], value["argv"])],
                executable=_text(_object(value["executable"])["path"]),
                cwd=_text(value["cwd"]),
                env={**{key: cast(str, item) for key, item in _object(value["environment"]).items()}, **inherited},
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                shell=False,
            )
            assert process.stdin is not None and process.stdout is not None and process.stderr is not None
            deadline = time.monotonic() + timeout
            for pipe, name in ((process.stdout, "stdout"), (process.stderr, "stderr")):
                os.set_blocking(pipe.fileno(), False)
                selector.register(pipe, selectors.EVENT_READ, name)
            if payload:
                os.set_blocking(process.stdin.fileno(), False)
                selector.register(process.stdin, selectors.EVENT_WRITE, "stdin")
            else:
                process.stdin.close()
            while selector.get_map():
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    failure = "timeout; output/effect completion remains unknown"
                    break
                events = selector.select(remaining)
                if not events:
                    failure = "timeout; output/effect completion remains unknown"
                    break
                for key, _ in events:
                    pipe = cast(BinaryIO, key.fileobj)
                    name = cast(str, key.data)
                    if name == "stdin":
                        try:
                            forwarded += os.write(pipe.fileno(), payload[forwarded:forwarded + 65536])
                        except BrokenPipeError:
                            failure = "actor closed input before the complete Context was forwarded"
                            break
                        if forwarded == len(payload):
                            selector.unregister(pipe)
                            pipe.close()
                    else:
                        chunk = os.read(pipe.fileno(), 65536)
                        if not chunk:
                            eof[name] = True
                            selector.unregister(pipe)
                            pipe.close()
                        else:
                            _write_all(stdout if name == "stdout" else stderr, chunk)
                            counts[name] += len(chunk)
                            if sum(counts.values()) > maximum:
                                failure = "output byte bound exceeded; retained output is a partial observation"
                                break
                if failure is not None:
                    break
            if failure is None:
                try:
                    process.wait(timeout=max(0.001, deadline - time.monotonic()))
                except subprocess.TimeoutExpired:
                    failure = "parent end not observed by the selected deadline"
        except (OSError, ValueError, core.SupportError) as exc:
            failure = type(exc).__name__ + ": " + str(exc)
        finally:
            for key in list(selector.get_map().values()):
                pipe = cast(BinaryIO, key.fileobj)
                selector.unregister(pipe)
                pipe.close()
            selector.close()
            if process is not None and process.poll() is None:
                for label, action in (("terminate", process.terminate), ("kill", process.kill)):
                    observed: Object = {"signal": label, "at_ns": time.time_ns(), "scope": "registered parent process only"}
                    try:
                        action()
                        observed["delivery"] = "requested"
                    except OSError as exc:
                        observed["delivery"] = "unavailable"
                        observed["reason"] = str(exc)
                    signals.append(observed)
                    try:
                        process.wait(timeout=grace)
                        break
                    except subprocess.TimeoutExpired:
                        pass
            for stream in (stdout, stderr):
                stream.flush()
                os.fsync(stream.fileno())
    code = None if process is None else process.poll()
    complete = failure is None and code == 0 and forwarded == len(payload) and all(eof.values())
    if failure is None and not complete:
        failure = "nonzero parent exit or incomplete input/output transport"
    return {
        "schema": "a_c.fd-support.actor-cli-observation/1", "pid": None if process is None else process.pid,
        "started_ns": started, "ended_ns": time.time_ns(), "returncode": code,
        "input_bytes": len(payload), "input_forwarded_bytes": forwarded,
        "stdout_bytes": counts["stdout"], "stderr_bytes": counts["stderr"],
        "stdout_eof": eof["stdout"], "stderr_eof": eof["stderr"],
        "output_available": complete, "failure": failure, "termination_requests": signals,
        "unknowns": ["descendant/process-tree end and external side effects", "host/model active-context size",
                     "backend retries or unreported usage", "semantic outcome and owner disposition"],
    }


def _pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for name, item in pairs:
        if name in value:
            raise TransportError("Duplicate vendor JSON key")
        value[name] = item
    return value


def _nonfinite(token: str) -> object:
    raise TransportError("Nonfinite vendor JSON token: " + token)


def _vendor_json(raw: str) -> dict[str, object]:
    value: object = json.loads(raw, object_pairs_hook=_pairs, parse_float=Decimal, parse_constant=_nonfinite)
    if not isinstance(value, dict):
        raise TransportError("Vendor event must be an object")
    return cast(dict[str, object], value)


def decode_final(raw: bytes, decoder: str) -> tuple[bytes, Object]:
    """Decode transport only; preserve actual answer text and reject repairs."""
    text = raw.decode("utf-8")
    if decoder == "claude-result-json/1":
        records = [_vendor_json(text)]
        lines: list[JSON] = [None]
    elif decoder in ("claude-result-jsonl/1", "codex-final-jsonl/1"):
        retained = [(index, line) for index, line in enumerate(text.splitlines(), 1) if line.strip()]
        records = [_vendor_json(line) for _, line in retained]
        lines = [index for index, _ in retained]
    else:
        raise TransportError("Unsupported deterministic vendor decoder")
    if not records:
        raise TransportError("No actual final vendor output")
    observations: list[JSON] = []
    for index, row in enumerate(records):
        fields = [field for field in ("usage", "modelUsage", "total_cost_usd", "cost_usd", "model", "session_id", "thread_id") if field in row]
        if fields:
            observations.append({"event_index": index, "source": "vendor.stdout", "line": lines[index],
                                 "pointers": ["/" + field for field in fields]})
    if decoder.startswith("claude-"):
        finals = [index for index, row in enumerate(records) if row.get("type") == "result"]
        if finals != [len(records) - 1]:
            raise TransportError("Expected exactly one terminal Claude result")
        final = records[-1]
        if final.get("subtype") != "success" or final.get("is_error") is not False:
            raise TransportError("Claude reported an error/non-success result")
        answer = final.get("result")
        if not isinstance(answer, str) or not answer:
            raise TransportError("Claude final text is absent; structured-output alternatives are not selected")
        pointer = "/result"
        index = len(records) - 1
    else:
        terminals = [index for index, row in enumerate(records) if row.get("type") in ("turn.completed", "turn.failed")]
        if terminals != [len(records) - 1] or records[-1].get("type") != "turn.completed":
            raise TransportError("Expected exactly one completed terminal Codex turn")
        messages: list[tuple[int, str]] = []
        for index, row in enumerate(records[:-1]):
            item = row.get("item")
            if row.get("type") == "item.completed" and isinstance(item, dict) and item.get("type") == "agent_message":
                answer_value = item.get("text")
                if not isinstance(answer_value, str):
                    raise TransportError("Codex completed message text is malformed")
                messages.append((index, answer_value))
        if not messages or not messages[-1][1]:
            raise TransportError("Codex final completed agent message is absent")
        index, answer = messages[-1]
        pointer = "/item/text"
    payload = answer.encode("utf-8")
    parsed = core.parse_json(payload)
    if not isinstance(parsed, dict) or parsed.get("schema") != "a_c.fd-support.closed-return/1":
        raise TransportError("Actual final payload is not a strict public closed-return object")
    return payload, {
        "decoder": decoder, "final_source": {"file": "vendor.stdout", "line": lines[index], "event_index": index, "pointer": pointer},
        "payload_sha256": hashlib.sha256(payload).hexdigest(), "payload_bytes": len(payload),
        "vendor_observations": observations,
        "limits": ["Vendor usage/settings remain exact raw-source observations, not normalized cost or self-certified producer identity",
                   "Opaque payload grammar only; the selected return contract and semantic judgment are checked by their existing owners"],
    }


def run(plan: Plan, source: BinaryIO, target: BinaryIO) -> int:
    output = _path(plan.document["evidence_directory"])
    if output.exists():
        raise TransportError("Evidence directory must be fresh; previous attempts are never overwritten")
    if not output.parent.is_dir():
        raise TransportError("Evidence parent must already exist")
    output.mkdir(mode=0o700)
    _save(output / "plan.json", plan.raw)
    limits = _object(plan.document["limits"])
    payload = source.read(_integer(limits["max_input_bytes"]) + 1)
    _save(output / "context.bin", payload)
    # These paths come unchanged from the actual registered helper process,
    # never from the plan/request. Selected credential values are acquired only
    # into the private child environment and are never recorded or hashed.
    inherited = {name: os.environ[name] for name in ("HOME", "home", "CODEX_HOME") if name in os.environ}
    inherited_names = core.environment_passthrough(plan.document["settings"], plan.document["environment"])
    credentials = {name: os.environ[name] for name in inherited_names if name in os.environ}
    invocation: Object = {
        "schema": "a_c.fd-support.actor-cli-invocation/1", "plan_sha256": plan.sha256,
        "backend": plan.document["backend"], "executable": plan.document["executable"],
        "argv": plan.document["argv"], "dependencies": plan.document["dependencies"],
        "cwd": plan.document["cwd"], "environment": plan.document["environment"],
        "protected_environment_pass_through": {key: value for key, value in inherited.items()},
        "protected_environment_provenance": "unchanged values already present in the registered helper process; absent stays absent",
        "settings_declared": plan.document["settings"], "decoder": plan.document["decoder"],
        "input_sha256": hashlib.sha256(payload).hexdigest(), "input_bytes": len(payload),
        "input_complete": len(payload) <= _integer(limits["max_input_bytes"]),
        "authority": "none conferred by helper; actual registered Attempt/Preflight owns authentication and Context binding",
        "limitations": ["No shell, prompt append, helper retry, model migration, global configuration or HOME/CODEX_HOME override",
                        "Selected settings/default preservation and complete helper/loader dependencies require exact operator proof; labels are declarations"],
    }
    if inherited_names:
        invocation["environment_passthrough"] = [{"name": name, "present": name in credentials} for name in inherited_names]
    _save_json(output / "invocation.json", invocation)
    if not invocation["input_complete"]:
        _save_json(output / "result.json", {"output_available": False, "actor_launched": False, "failure": "input byte bound exceeded; retained Context prefix only"})
        return 2
    observed = _capture(plan, payload, output, {**inherited, **credentials})
    _save_json(output / "process.json", observed)
    if not observed["output_available"]:
        _save_json(output / "result.json", {"output_available": False, "actor_launched": observed["pid"] is not None, "failure": observed["failure"], "semantic_result": None})
        return 1
    try:
        answer, decoded = decode_final((output / "vendor.stdout").read_bytes(), _text(plan.document["decoder"]))
    except (ValueError, UnicodeError, core.SupportError, ArithmeticError) as exc:
        _save_json(output / "result.json", {"output_available": False, "actor_launched": True, "failure": type(exc).__name__ + ": " + str(exc), "semantic_result": None})
        return 1
    _save(output / "final.payload", answer)
    _save_json(output / "decoded.json", decoded)
    _save_json(output / "result.json", {"output_available": True, "actor_launched": True,
                                       "payload_sha256": hashlib.sha256(answer).hexdigest(), "semantic_result": None,
                                       "limits": ["Actual opaque output only; no work acceptance, independence or effect-completion claim"]})
    _write_all(target, answer)
    target.flush()
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--plan-sha256", required=True)
    args = parser.parse_args(argv)
    try:
        plan = load_plan(cast(Path, args.plan), cast(str, args.plan_sha256))
        code = run(plan, sys.stdin.buffer, sys.stdout.buffer)
        if code:
            print("Actor transport failed; acquire its raw/partial evidence before any separately authorized retry", file=sys.stderr)
        return code
    except (OSError, ValueError, core.SupportError, ArithmeticError) as exc:
        print(f"Actor transport unavailable: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
