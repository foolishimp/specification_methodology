"""Retain completed hosts' exact-session output transport and fixture observations."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("run", type=Path)
    args = parser.parse_args()
    for context in json.loads((args.run / "contexts.json").read_text())["contexts"]:
        dest = Path(context["directory"])
        if not (dest / "execution-result.json").is_file():
            raise RuntimeError(f"Incomplete host process: {dest}")
        raw = (dest / "stdout.jsonl").read_text()
        if context["host"] == "claude":
            rows = [json.loads(line) for line in raw.splitlines() if line.strip()]
            init = next(row for row in rows if row.get("type") == "system" and row.get("subtype") == "init")
            session = init["session_id"]
            paths = set(re.findall(r"/Users/jim/\.claude/projects/[^\s\"']+/" + re.escape(session) + r"/tool-results/[^\s\"'\\]+", raw))
            copied = []
            for path in sorted(paths):
                source = Path(path)
                if not source.is_file():
                    continue
                target = dest / "host-tool-results" / source.name
                target.parent.mkdir(exist_ok=True)
                shutil.copy2(source, target)
                copied.append({"original_path": path, "retained_path": str(target.relative_to(dest)), "sha256": digest(target)})
            record = {"session_id": session, "host_model": init["model"], "host_working_directory": init["cwd"],
                      "same_session_host_tool_output_spill": copied,
                      "scope_note": "Exact-session tool outputs stored automatically by the host outside the snapshot. These retain the transport for original source/view reads, not additional source or author inputs."}
            (dest / "host-tool-output-provenance.json").write_text(json.dumps(record, indent=2) + "\n")
        if context.get("allow_fixture_edit"):
            cwd = Path(context["cwd"])
            before = {p.name: digest(p) for p in [cwd / "cache.py", cwd / "fixture_probe.py", cwd / "case-inputs.json"]}
            result = subprocess.run(["python3", "-B", "fixture_probe.py"], cwd=cwd, capture_output=True, text=True)
            (dest / "post-host-probe.stdout.json").write_text(result.stdout)
            (dest / "post-host-probe.stderr.txt").write_text(result.stderr)
            try:
                payload = json.loads(result.stdout)
                all_satisfied = payload.get("domain_complete") is True and all(row.get("satisfied") is True for row in payload.get("observations", [])) and len(payload.get("observations", [])) == 2
            except ValueError:
                payload, all_satisfied = None, False
            after = {p.name: digest(p) for p in [cwd / "cache.py", cwd / "fixture_probe.py", cwd / "case-inputs.json"]}
            record = {"argv": ["python3", "-B", "fixture_probe.py"], "cwd": str(cwd), "exit_code": result.returncode,
                      "files_before": before, "files_after": after, "payload": payload,
                      "both_declared_outcomes_satisfied": all_satisfied,
                      "qualification": "Post-host Writer observation of the exact remaining fixture. Native actor's own probe and response remain separately in raw stdout; this check cannot substitute for absent native use or source assessment."}
            (dest / "post-host-probe-result.json").write_text(json.dumps(record, indent=2) + "\n")
        print(context["name"], "collected")


if __name__ == "__main__":
    main()
