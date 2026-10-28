"""Selected Lean checker effect adapter; no request can select executable code.

Configuration is a trusted startup input. Its identity pins the independently
versioned checker and support population. This module launches only that fixed
CLI; retained status JSON is never a substitute for executing it.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time
from typing import Any


CONFIG = "a_c.graphify.formal-checker/1"
EXITS = {"verified": 0, "refused": 2, "unsupported": 3, "incomplete": 4}


class GateError(Exception):
    def __init__(self, status: str, reason: str):
        super().__init__(reason)
        self.status = status


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode()


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in items:
        if key in value:
            raise GateError("refused", "Duplicate JSON key")
        value[key] = item
    return value


def _json(raw: bytes) -> Any:
    try:
        return json.loads(raw, object_pairs_hook=_pairs,
                          parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
    except (ValueError, UnicodeError) as exc:
        raise GateError("incomplete", "Checker output is not finite JSON") from exc


def _regular(path: Path) -> bytes:
    if not path.is_absolute() or any(p.is_symlink() for p in (path, *path.parents)) or not path.is_file():
        raise GateError("refused", "Checker or evidence path is not an absolute regular file")
    return path.read_bytes()


def validate_config(config: Any) -> dict[str, Any]:
    fields = {"schema", "root", "python", "entry_sha256", "adapter_sha256", "runtime_identity", "timeout_seconds"}
    if not isinstance(config, dict) or set(config) != fields or config["schema"] != CONFIG:
        raise GateError("unsupported", "Unsupported trusted formal checker configuration")
    python = config["python"]
    if (not isinstance(python, dict) or set(python) != {"path", "sha256"}
            or not isinstance(config["root"], str) or not Path(config["root"]).is_absolute()
            or not isinstance(python["path"], str) or not Path(python["path"]).is_absolute()
            or type(config["timeout_seconds"]) is not int or config["timeout_seconds"] < 1):
        raise GateError("unsupported", "Invalid trusted checker path, interpreter or limit")
    identity = config["runtime_identity"]
    if (not isinstance(identity, dict) or set(identity) != {"sha256", "pins"}
            or not isinstance(identity["pins"], dict) or not identity["pins"]):
        raise GateError("unsupported", "Checker selection lacks its complete runtime identity")
    for digest in (config["entry_sha256"], config["adapter_sha256"], python["sha256"], identity["sha256"]):
        if not isinstance(digest, str) or re.fullmatch("[0-9a-f]{64}", digest) is None:
            raise GateError("unsupported", "Invalid selected checker digest")
    if any(not isinstance(name, str) or not isinstance(digest, str) or re.fullmatch("[0-9a-f]{64}", digest) is None
           for name, digest in identity["pins"].items()):
        raise GateError("unsupported", "Invalid selected runtime member pin")
    if sha(_regular(Path(__file__).resolve())) != config["adapter_sha256"]:
        raise GateError("refused", "Selected Graphify formal adapter implementation changed")
    return config


def _pins(config: dict[str, Any]) -> None:
    """Parent-owned inspection precedes importing any selected checker helper."""
    root = Path(config["root"])
    identity = config["runtime_identity"]
    pins = identity["pins"]
    if sha(canonical(pins)) != identity["sha256"] or not {"scripts/formal_gate.py", "profiles/proof-support-v1.json"} <= set(pins):
        raise GateError("refused", "Selected checker identity or support manifest pin is incomplete")
    actual = {str(path.relative_to(root)) for pattern in ("scripts/*.py", "profiles/*.json") for path in root.glob(pattern)}
    selected = {path for path in pins if (path.startswith("scripts/") and path.endswith(".py")) or (path.startswith("profiles/") and path.endswith(".json"))}
    if actual != selected:
        raise GateError("refused", "Selected deciding checker module/profile population changed")
    for name, expected in pins.items():
        if not isinstance(name, str) or Path(name).is_absolute() or ".." in Path(name).parts:
            raise GateError("refused", "Selected runtime pin escapes the checker root")
        if sha(_regular(root / name)) != expected:
            raise GateError("refused", "Selected deciding checker dependency changed: " + name)


def _owned_groups(checker_pid: int) -> tuple[set[int], list[str]]:
    """Bounded POSIX observation, limited to this invocation's private descendants."""
    groups = {checker_pid}
    observations = []
    try:
        census = subprocess.run(["/bin/ps", "-axo", "pid=,ppid=,pgid="], capture_output=True,
                                timeout=1, env={"PATH": os.defpath}, check=False)
        if census.returncode != 0:
            return groups, ["descendant census unavailable; nested-group attribution unresolved"]
        rows = {pid: (parent, group) for pid, parent, group in
                (map(int, line.split()) for line in census.stdout.splitlines() if line.strip())}
        owned = {checker_pid}
        while True:
            found = {pid for pid, (parent, _) in rows.items() if parent in owned}
            if found <= owned:
                break
            owned.update(found)
        excluded = {os.getpgrp()}
        ancestor = os.getpid()
        while ancestor in rows:
            parent, group = rows[ancestor]
            excluded.add(group)
            if parent == ancestor or parent <= 0:
                break
            ancestor = parent
        for pid in owned:
            if pid not in rows:
                continue
            group = rows[pid][1]
            if group > 1 and group in owned and group not in excluded:
                groups.add(group)
            elif group != checker_pid:
                observations.append("observed descendant group was not positively attributable as private")
        groups -= excluded
        observations.append("census at monotonic_ns=" + str(time.monotonic_ns()) + "; owned PID/PPID/PGID="
                            + json.dumps({pid: rows[pid] for pid in sorted(owned) if pid in rows}, sort_keys=True))
        observations.append("observed owned private process groups: " + ",".join(map(str, sorted(groups))))
        if checker_pid not in rows:
            observations.append("checker absent from census; reparented descendant attribution unresolved")
    except (OSError, ValueError, subprocess.SubprocessError):
        observations.append("descendant census failed; nested-group attribution unresolved")
    return groups, observations


def _invoke(config: dict[str, Any], args: list[str], *, selecting: bool = False) -> subprocess.CompletedProcess[bytes]:
    validate_config(config)
    entry = Path(config["root"]) / "scripts" / "formal_gate.py"
    python = Path(config["python"]["path"])
    if sha(_regular(entry)) != config["entry_sha256"] or sha(_regular(python)) != config["python"]["sha256"]:
        raise GateError("refused", "Selected checker entry or interpreter changed")
    if not selecting:
        _pins(config)
    try:
        # No caller command, shell, plugin path, or PYTHONPATH participates.
        argv = [str(python), "-E", "-s", "-B", "-X", "pycache_prefix=" + os.devnull, str(entry), *args]
        process = subprocess.Popen(argv, cwd=config["root"], env={"PATH": os.defpath, "HOME": os.environ.get("HOME", "")},
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True, close_fds=True)
        try:
            stdout, stderr = process.communicate(timeout=config["timeout_seconds"])
        except subprocess.TimeoutExpired:
            groups, cleanup = _owned_groups(process.pid)
            for signum in (signal.SIGTERM, signal.SIGKILL):
                if signum == signal.SIGKILL:
                    # A trusted compiler/helper may finish spawning its private
                    # child during TERM grace. Reobserve before the final signal.
                    observed, details = _owned_groups(process.pid)
                    groups.update(observed)
                    cleanup.extend(details)
                for group in sorted(groups, reverse=True):
                    try:
                        os.killpg(group, signum)
                        cleanup.append(signal.Signals(signum).name + " sent to owned group " + str(group)
                                       + " at monotonic_ns=" + str(time.monotonic_ns()))
                    except ProcessLookupError:
                        cleanup.append("owned group " + str(group) + " absent")
                try:
                    process.communicate(timeout=2)
                    cleanup.append("checker exit and captured pipe closure observed")
                    live = set()
                    for group in groups:
                        try:
                            os.killpg(group, 0)
                            live.add(group)
                        except ProcessLookupError:
                            pass
                    if not live:
                        cleanup.append("observed owned process groups absent after cleanup")
                        break
                    if signum == signal.SIGKILL:
                        cleanup.append("remaining group members received SIGKILL; descendant reap not independently observed")
                        break
                except subprocess.TimeoutExpired:
                    cleanup.append("pipe/process end not observed within cleanup bound")
            else:
                for stream in (process.stdout, process.stderr):
                    if stream is not None:
                        stream.close()
                try:
                    process.wait(timeout=1)
                except subprocess.TimeoutExpired:
                    cleanup.append("checker process end unresolved")
            raise GateError("incomplete", "Checker outer timeout; " + "; ".join(cleanup)
                            + "; descendants outside observed private groups are not established ended") from None
        return subprocess.CompletedProcess(argv, process.returncode, stdout, stderr)
    except OSError as exc:
        raise GateError("incomplete", "Selected checker could not complete: " + str(exc)) from exc


def current(config: dict[str, Any]) -> None:
    result = _invoke(config, ["identity"])
    if result.returncode != 0:
        raise GateError("incomplete", "Selected checker identity could not be acquired")
    if _json(result.stdout) != config["runtime_identity"]:
        raise GateError("refused", "Selected checker implementation, support or toolchain changed")


def select_checker(root: Path, python: Path, timeout_seconds: int = 600) -> dict[str, Any]:
    """Explicit local startup selection, never called by an untrusted request."""
    root, python = root.resolve(strict=True), python.resolve(strict=True)
    config = {"schema": CONFIG, "root": str(root), "python": {"path": str(python), "sha256": sha(_regular(python))},
              "entry_sha256": sha(_regular(root / "scripts/formal_gate.py")),
              "adapter_sha256": sha(_regular(Path(__file__).resolve())),
              "runtime_identity": {"sha256": "0" * 64, "pins": {"selection-pending": "0" * 64}},
              "timeout_seconds": timeout_seconds}
    result = _invoke(config, ["identity"], selecting=True)
    if result.returncode != 0:
        raise GateError("incomplete", "Checker startup identity acquisition failed: " + result.stderr.decode(errors="replace"))
    config["runtime_identity"] = _json(result.stdout)
    validate_config(config)
    current(config)
    return config


def load_config(path: Path, expected_sha256: str) -> dict[str, Any]:
    raw = _regular(path.absolute())
    if sha(raw) != expected_sha256:
        raise GateError("refused", "Trusted checker configuration digest changed")
    return validate_config(_json(raw))


def _result(config: dict[str, Any], process: subprocess.CompletedProcess[bytes], bundle: Path) -> dict[str, Any]:
    (bundle.parent / "checker.stdout").write_bytes(process.stdout)
    (bundle.parent / "checker.stderr").write_bytes(process.stderr)
    result = _json(process.stdout)
    if (not isinstance(result, dict) or result.get("schema") != "a_c.formal-gate.result/1"
            or result.get("status") not in EXITS or EXITS[result["status"]] != process.returncode):
        raise GateError("incomplete", "Checker exit/result contract mismatch")
    if result["status"] == "verified":
        raw = _regular(bundle / "result.json")
        if _json(raw) != result or result.get("runtime_identity") != config["runtime_identity"]:
            raise GateError("refused", "Checker result or deciding runtime identity mismatch")
    current(config)
    return result


def verify(config: dict[str, Any], raw: bytes, format: str, selections: list[dict[str, Any]],
           views: Any, context_binding: Any, output: Path) -> dict[str, Any]:
    """Verify exact acquired bytes and actual ordered views in a fresh directory."""
    current(config)
    output = output.absolute()
    output.mkdir(parents=True, exist_ok=False)
    source = output / "input.json"; source.write_bytes(raw)
    view_binding = None
    if views is not None:
        view_raw = canonical(views); path = output / "views.json"; path.write_bytes(view_raw)
        view_binding = {"path": str(path), "raw_sha256": sha(view_raw)}
    request = {"schema": "a_c.formal-gate.request/1", "input": {"format": format, "path": str(source), "raw_sha256": sha(raw)},
               "selections": selections, "supplied_views": view_binding, "context_binding": context_binding}
    request_path = output / "request.json"; request_path.write_bytes(canonical(request))
    bundle = output / "bundle"
    result = _result(config, _invoke(config, ["verify", "--request", str(request_path), "--output", str(bundle)]), bundle)
    if result["status"] == "verified" and (result.get("request_sha256") != sha(canonical(request))
            or result.get("selections") != selections or result.get("context_binding") != context_binding):
        raise GateError("refused", "Checker result does not bind the actual integration request")
    return {"result": result, "bundle": str(bundle),
            "result_sha256": sha(_regular(bundle / "result.json")) if (bundle / "result.json").is_file() else None,
            "request_sha256": sha(canonical(request)), "input_sha256": sha(raw),
            "views_sha256": None if views is None else sha(canonical(views))}


def receipt(run: dict[str, Any]) -> dict[str, Any]:
    """Integer-only support envelope; complete timing JSON stays hash-bound beside it."""
    result = run["result"]
    return {**run, "result": {key: result.get(key) for key in
            ("schema", "status", "reason", "model", "selections", "context_binding", "runtime_identity")}}


def recheck(config: dict[str, Any], retained: dict[str, Any], output: Path) -> dict[str, Any]:
    """Fresh proof replay from a hash-bound protected receipt, never saved success."""
    current(config)
    bundle = Path(retained["bundle"])
    raw = _regular(bundle / "result.json")
    if sha(raw) != retained["result_sha256"] or receipt({"result": _json(raw)})["result"] != receipt(retained)["result"]:
        raise GateError("refused", "Retained checker result changed")
    output = output.absolute(); output.mkdir(parents=True, exist_ok=False)
    replay = output / "bundle"
    result = _result(config, _invoke(config, ["check-evidence", "--bundle", str(bundle), "--output", str(replay)]), replay)
    if result["status"] == "verified":
        for key in ("model", "selections", "context_binding", "runtime_identity"):
            if result.get(key) != retained["result"].get(key):
                raise GateError("refused", "Replayed evidence changed its exact " + key)
    return {"result": result, "bundle": str(replay),
            "result_sha256": sha(_regular(replay / "result.json")) if (replay / "result.json").is_file() else None,
            "replayed_result_sha256": retained["result_sha256"]}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean-root", type=Path, required=True)
    parser.add_argument("--python", type=Path, default=Path(sys.executable))
    parser.add_argument("--timeout-seconds", type=int, default=600)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        config = select_checker(args.lean_root, args.python, args.timeout_seconds)
        with args.output.open("xb") as stream:
            stream.write(canonical(config))
        print(json.dumps({"configuration": str(args.output), "sha256": sha(args.output.read_bytes())}, sort_keys=True))
        return 0
    except (GateError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
