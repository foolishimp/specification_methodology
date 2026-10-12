"""Replay native-authored join inputs; report structure/custody, never semantics."""
from pathlib import Path
import argparse
import json
import re
import subprocess

from prepare_native import sha, write
from run_native import PYTHON, environment, prefix


def parse_final(text):
    stripped = text.strip()
    if stripped.startswith("```\n") and stripped.endswith("\n```"):
        stripped = stripped[4:-4]
    try:
        return json.loads(stripped), "plain_json"
    except ValueError:
        blocks = re.findall(r"^```json\s*\n(.*?)\n```\s*$", text, flags=re.M | re.S)
        if len(blocks) != 1:
            raise ValueError("No unique fenced JSON return")
        return json.loads(blocks[0]), "unique_fenced_json; surrounding prose retained in raw final"


def check(context, output_name="return-mechanics.json"):
    evidence = Path(context["directory"])
    destination = evidence / output_name
    if destination.exists():
        raise RuntimeError("Refuse overwriting return observation")
    final = evidence / "final.txt"
    result = {"context": context["name"], "scope": "Output structure and exact join replay only; independent semantic assessment required"}
    if not final.is_file():
        result.update(status="no_final", checks=[])
        write(destination, result)
        return result
    result["final_sha256"] = sha(final)
    try:
        value, presentation = parse_final(final.read_text())
        result["presentation"] = presentation
    except (ValueError, TypeError) as error:
        result.update(status="unparseable_final", error=str(error), checks=[])
        write(destination, result)
        return result
    required = {"case_a", "case_b", "case_c", "selected_frames", "source_reentry", "handoff_sections", "joined_request", "limits"}
    checks = [{"claim": "required_top_level_fields", "pass": isinstance(value, dict) and required <= set(value)}]
    if not isinstance(value, dict):
        result.update(status="structure_failed", checks=checks)
        write(destination, result)
        return result
    sections = value.get("handoff_sections")
    shaped = isinstance(sections, list) and len(sections) == 7 and all(isinstance(row, dict) and set(row) == {"label", "text"} and isinstance(row["label"], str) and isinstance(row["text"], str) for row in sections)
    checks.append({"claim": "seven_native_authored_section_rows", "pass": shaped})
    checks.append({"claim": "action_is_last", "pass": shaped and sections[-1]["label"].strip().upper() == "ACTION"})
    if shaped:
        work = Path(context["worksite"])
        native = json.loads((work / "native-context.json").read_text())
        env, _ = environment(context)
        command = prefix(context) + [PYTHON, "-B", str(Path(native["axiom_root"]) / "build_tenants/core/code/ac.py"), "join", "--input", "/dev/stdin"]
        observed = subprocess.run(command, cwd=work, env=env, input=json.dumps(sections), capture_output=True, text=True, timeout=45)
        result["join_replay"] = {"argv": command, "exit_code": observed.returncode, "stdout": observed.stdout, "stderr": observed.stderr}
        checks.append({"claim": "native_joined_request_matches_exact_replay", "pass": observed.returncode == 0 and observed.stdout == value.get("joined_request")})
    result.update(checks=checks, status="mechanically_consistent" if all(row["pass"] for row in checks) else "structure_or_join_failed")
    write(destination, result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--contexts", type=Path, required=True)
    args = parser.parse_args()
    for context in json.loads(args.contexts.read_text())["contexts"]:
        print(json.dumps({key: value for key, value in check(context).items() if key in ("context", "status")}), flush=True)


if __name__ == "__main__":
    main()
