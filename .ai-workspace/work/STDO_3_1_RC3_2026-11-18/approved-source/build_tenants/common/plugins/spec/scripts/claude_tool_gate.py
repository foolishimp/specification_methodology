#!/usr/bin/env python3
"""Opt-in Claude PreToolUse projection of an already-authorized exact policy.

No wildcard matching, shell interpretation, grant inference or global setup.
Use with the documented session hook's onFailure=block setting. See the
plugin's HOST_BINDING.md for the remaining host/context boundaries.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys

# An installed plugin is immutable, including when the host omits Python -B.
sys.dont_write_bytecode = True
from read_basis import Refusal, decoded, digest


def canonical_path(value, *, existing=True):
    if not isinstance(value, str) or not value or "\0" in value:
        raise Refusal("invalid_path")
    path = Path(value)
    if (not path.is_absolute() or str(path) != value or ".." in path.parts
            or path.resolve(strict=existing) != path):
        raise Refusal("noncanonical_path")
    return path


def unique_strings(value):
    if (not isinstance(value, list) or not all(isinstance(v, str) and v and "\0" not in v for v in value)
            or len(set(value)) != len(value)):
        raise Refusal("invalid_policy_list")
    return value


def load_policy(path, expected):
    if re.fullmatch(r"[0-9a-f]{64}", expected) is None:
        raise Refusal("invalid_policy_digest")
    raw = canonical_path(path).read_bytes()
    if digest(raw) != expected:
        raise Refusal("policy_digest_mismatch")
    policy = decoded(raw)
    fields = {"kind", "schema_version", "policy_id", "authority_ref", "cwd", "read_paths", "bash_commands", "skills"}
    if not isinstance(policy, dict) or set(policy) != fields:
        raise Refusal("invalid_policy_fields")
    if policy["kind"] != "stdo.claude-tool-policy" or policy["schema_version"] != 1:
        raise Refusal("unsupported_policy")
    for key in ("policy_id", "authority_ref"):
        if not isinstance(policy[key], str) or not policy[key].strip():
            raise Refusal("missing_policy_identity")
    if not canonical_path(policy["cwd"]).is_dir():
        raise Refusal("invalid_cwd")
    for value in unique_strings(policy["read_paths"]):
        if not canonical_path(value).is_file():
            raise Refusal("read_path_not_file")
    unique_strings(policy["bash_commands"])
    for value in unique_strings(policy["skills"]):
        if re.fullmatch(r"[A-Za-z0-9_.:-]+", value) is None:
            raise Refusal("invalid_skill_name")
    return policy


def decide(policy, event):
    if not isinstance(event, dict) or event.get("hook_event_name") != "PreToolUse":
        raise Refusal("wrong_hook_event")
    if str(canonical_path(event.get("cwd"))) != policy["cwd"]:
        raise Refusal("cwd_mismatch")
    tool, value = event.get("tool_name"), event.get("tool_input")
    if not isinstance(value, dict):
        raise Refusal("invalid_tool_input")
    if tool == "Read":
        if not set(value) <= {"file_path", "offset", "limit"} or "file_path" not in value:
            raise Refusal("unsupported_read_input")
        for key in ("offset", "limit"):
            if key in value and (type(value[key]) is not int or value[key] < 1):
                raise Refusal("invalid_read_range")
        if value["file_path"] not in policy["read_paths"]:
            raise Refusal("read_not_listed")
        canonical_path(value["file_path"])
    elif tool == "Bash":
        if not set(value) <= {"command", "description", "timeout", "run_in_background"}:
            raise Refusal("unsupported_bash_input")
        if value.get("run_in_background", False) is not False:
            raise Refusal("background_not_supported")
        if "timeout" in value and (type(value["timeout"]) is not int or value["timeout"] <= 0):
            raise Refusal("invalid_command_timeout")
        if "description" in value and not isinstance(value["description"], str):
            raise Refusal("invalid_command_description")
        if value.get("command") not in policy["bash_commands"]:
            raise Refusal("command_not_listed")
    elif tool == "Skill":
        if set(value) != {"skill"} or value["skill"] not in policy["skills"]:
            raise Refusal("skill_not_listed")
    else:
        raise Refusal("tool_not_supported")
    return "allow", "exact_policy_match"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", required=True)
    parser.add_argument("--policy-sha256", required=True)
    parser.add_argument("--audit", help="explicit authorized append-only JSONL result surface")
    args = parser.parse_args(argv)
    event = None
    decision, reason = "deny", "unverified_policy"
    try:
        policy = load_policy(args.policy, args.policy_sha256)
        if str(Path.cwd().resolve()) != policy["cwd"]:
            raise Refusal("hook_cwd_mismatch")
        event = decoded(sys.stdin.read())
        decision, reason = decide(policy, event)
    except (Refusal, OSError, ValueError, KeyError, TypeError) as exc:
        reason = str(exc)
    if args.audit:
        record = {"policy_sha256": args.policy_sha256, "decision": decision, "reason": reason,
                  "event_sha256": digest(json.dumps(event, sort_keys=True).encode()),
                  "tool_use_id": event.get("tool_use_id") if isinstance(event, dict) else None,
                  "tool_name": event.get("tool_name") if isinstance(event, dict) else None}
        try:
            path = canonical_path(args.audit, existing=False)
            if not path.parent.is_dir():
                raise Refusal("audit_parent_missing")
            fd = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT | os.O_NOFOLLOW, 0o600)
            try:
                raw = (json.dumps(record, sort_keys=True) + "\n").encode()
                if os.write(fd, raw) != len(raw):
                    raise OSError("partial_audit_write")
            finally:
                os.close(fd)
        except (Refusal, OSError, ValueError, TypeError):
            decision, reason = "deny", "audit_unavailable"
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
        "permissionDecision": decision, "permissionDecisionReason": reason}}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
