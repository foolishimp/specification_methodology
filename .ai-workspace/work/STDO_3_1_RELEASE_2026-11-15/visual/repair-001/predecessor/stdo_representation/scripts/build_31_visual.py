#!/usr/bin/env python3
"""Replay the bounded, source-authored 3.1 visual through the public project API.

This release recipe creates source navigation and the explicitly authored
annotations in visual_31_annotations.json. It is not a semantic extractor or a
context engine. Exact quote checks refuse changed source; assess a new recipe
for a different cut. No historical model is imported or rebound.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CUT = "v3.1.0-rc.1"
SELECTED = ("ACTIVATION.md", "SDLC_DEFAULTS.md", "TICKETS.md")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def check(condition, message):
    if not condition:
        raise ValueError(message)


def authored_answer(chunk, recipe):
    segments = chunk["segments"]
    answer = {name: [] for name in
              ("concepts", "relations", "constraints", "latitude", "residuals",
               "dispositions", "limitations")}
    keys = set()

    def key(prefix, text):
        candidate = prefix + re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
        if candidate in keys:
            candidate += "_" + digest(text.encode())[:12]
        check(candidate not in keys, "navigation identity collision")
        keys.add(candidate)
        return candidate

    def heading_ground(segment):
        lines = segment["text"].splitlines()
        index = next(i for i, line in enumerate(lines) if line.strip())
        line = segment["start_line"] + index
        return {"section_id": segment["id"], "start_line": line,
                "end_line": line, "quote": lines[index]}

    files = {}
    for segment in segments:
        path = segment["path"]
        ground = heading_ground(segment)
        if path not in files:
            ident = key("file_", Path(path).name)
            files[path] = ident
            answer["concepts"].append({"key": ident, "label": Path(path).name,
                "definition": "Exact selected native source member. Its complete text is embedded for source re-entry; this node supplies navigation, not a complete interpretation.",
                "grounding": [ground], "conditions": [], "exceptions": []})
        ident = key("section_", Path(path).name + "_" + segment["heading"])
        answer["concepts"].append({"key": ident,
            "label": Path(path).name + " · " + segment["heading"],
            "definition": "Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.",
            "grounding": [ground], "conditions": [], "exceptions": []})
        relation = key("contains_", ident)
        answer["relations"].append({"key": relation, "kind": "contains_source_section",
            "source_key": files[path], "target_key": ident,
            "meaning": "The selected source member contains this section. This is a structural navigation relation and grants no semantic authority.",
            "governing": False, "conditions": [], "exceptions": [], "grounding": [ground]})
        residual = key("unrepresented_", ident)
        answer["residuals"].append({"key": residual, "subject_key": ident,
            "uncertainty": "This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented.",
            "consequence": "Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.",
            "grounding": [ground]})

    def ground_query(query):
        matches = []
        for segment in segments:
            if Path(segment["path"]).name != query["file"]:
                continue
            if query["quote"] in segment["text"]:
                before = segment["text"].split(query["quote"], 1)[0]
                start = segment["start_line"] + before.count("\n")
                matches.append({"section_id": segment["id"], "start_line": start,
                    "end_line": start + query["quote"].count("\n"), "quote": query["quote"]})
        check(len(matches) == 1, "authored quote absent or ambiguous: " + query["file"] + " " + query["quote"][:70])
        return matches[0]

    for entry in recipe["annotations"]:
        record = dict(entry["record"])
        check(record["key"] not in keys, "authored identity collision")
        keys.add(record["key"])
        record["grounding"] = [ground_query(q) for q in entry["grounds"]]
        answer[entry["family"]].append(record)
    populations = [row for family in ("concepts", "relations", "constraints", "latitude", "residuals")
                   for row in answer[family]]
    for segment in segments:
        selected = [row["key"] for row in populations
                    if any(g["section_id"] == segment["id"] for g in row["grounding"])]
        answer["dispositions"].append({"section_id": segment["id"], "decision": "residual",
            "keys": selected,
            "reason": "Complete section navigation and exact source re-entry are retained. Only explicitly selected annotations interpret body meaning; the visible section residual retains the unrepresented remainder. This is no whole-section semantic acceptance."})
    answer["limitations"] = recipe["limitations"]
    return answer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--native-root", type=Path, required=True)
    parser.add_argument("--native-manifest-sha256", required=True)
    parser.add_argument("--stdo", default="stdo")
    parser.add_argument("--out", type=Path, default=ROOT / "build_tenants/a_c/representation/stdo-v3.1.0-rc.1")
    args = parser.parse_args()
    native = args.native_root.resolve(strict=True)
    raw = (native / "manifest.json").read_bytes()
    check(digest(raw) == args.native_manifest_sha256, "native manifest digest differs")
    manifest = json.loads(raw)
    check(manifest["release"]["cut"] == CUT, "recipe requires exact native " + CUT)
    entries = {row["path"]: row for row in manifest["standards"]["members"]}
    selected = []
    auxiliary = ["AXIOMATIC_CALCULUS.md"]
    for name in (*SELECTED, *auxiliary):
        check(name in entries, "native member missing: " + name)
        member = native / "standards" / name
        check(not member.is_symlink(), "redirected native member: " + name)
        data = member.read_bytes()
        check(digest(data) == entries[name]["sha256"], "native member changed: " + name)
        selected.append({"path": "standards/" + name, "sha256": digest(data), "bytes": len(data),
                         "use": "visual source corpus" if name in SELECTED else "Axiom conversion calculus provenance only; not visually interpreted"})
    out = args.out.absolute()
    check(out.is_relative_to(ROOT) and not out.exists(), "choose a fresh output inside this Product")
    source = out / "source"
    (source / "standards").mkdir(parents=True)
    (source / "manifest.json").write_bytes(raw)
    for row in selected:
        (source / row["path"]).write_bytes((native / row["path"]).read_bytes())
    recipe_path = ROOT / "scripts/visual_31_annotations.json"
    recipe = json.loads(recipe_path.read_text())
    provider = ROOT.parent / "a_c"
    public = provider / "PUBLIC_MANIFEST.json"
    public_doc = json.loads(public.read_text())
    check(public_doc["version"] == CUT[1:], "provider version differs from cohort")
    for member in public_doc["files"]:
        data = (provider / member["path"]).read_bytes()
        check(digest(data) == member["sha256"] and len(data) == member["bytes"],
              "provider member changed: " + member["path"])
    binding = {"profile": "stdo-representation.native-visual-binding/1", "version": CUT[1:],
        "represented_source": {"uri": "stdo://releases/" + CUT + "/", "manifest_sha256": digest(raw),
                               "release": manifest["release"]},
        "construction_basis": json.loads((ROOT / "stdo_representation.json").read_text())["constitution"]["stdo"]["basis"],
        "provider": {"product": "urn:stdo:product-definition:a-c-implementations", "version": (provider / "VERSION").read_text().strip(), "public_manifest_sha256": digest(public.read_bytes())},
        "recipe_sha256": digest(recipe_path.read_bytes()), "generator_sha256": digest(Path(__file__).read_bytes()),
        "selected_native_members": selected,
        "unselected_standard_members": [row for row in manifest["standards"]["members"] if row["path"] not in (*SELECTED, *auxiliary)],
        "scope": recipe["scope"], "limits": recipe["limitations"],
        "author": "OpenAI Codex visual Products Writer; host-session source authoring; no isolated actor telemetry",
        "assessment": "Structural checks and Writer observations do not supply independent source-fidelity acceptance."}
    save(out / "SOURCE_BINDING.json", binding)
    logs = out / "commands"
    serial = 0

    def command(label, argv):
        nonlocal serial
        serial += 1
        result = subprocess.run(argv, capture_output=True, text=True)
        save(logs / (str(serial).zfill(2) + "-" + label + ".json"),
             {"argv": argv, "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr})
        check(result.returncode == 0, label + " failed; retained exact command result")
        return json.loads(result.stdout)

    cli = [sys.executable, "-B", str(provider / "scripts/ac.py"), "project"]
    run = out / "run"
    selection = [str((source / "standards" / name).relative_to(ROOT)) for name in SELECTED]
    prepare = cli + ["prepare", "--project", str(ROOT), "--definition", "stdo_representation.json",
                     "--out", str(run), "--chunk-chars", "3000000", "--stdo", args.stdo,
                     "--title", "STDO 3.1 · Source navigation and selected work/context relations"]
    for path in selection:
        prepare += ["--source", path]
    command("prepare", prepare)
    chunks = json.loads((run / "generation/chunks.json").read_text())
    check(len(chunks) == 1, "recipe requires one coherent authored task")
    task = command("task", cli + ["task", "--run", str(run)])
    save(out / "authoring/TASK.json", task)
    answer = authored_answer(chunks[0], recipe)
    save(out / "authoring/ANSWER.json", answer)
    command("submit", cli + ["submit", "--run", str(run), "--chunk", chunks[0]["id"],
                            "--answer", str(out / "authoring/ANSWER.json"),
                            "--author", binding["author"]])
    built = command("build", cli + ["build", "--run", str(run)])
    command("status", cli + ["status", "--run", str(run)])
    command("reuse", cli + ["build", "--run", str(run)])
    save(out / "GENERATION.json", {"profile": "stdo-representation.bounded-generation/1",
        "represented_source": binding["represented_source"],
        "source_binding_sha256": digest((out / "SOURCE_BINDING.json").read_bytes()),
        "native_member_mapping": [{"project_source_path": path,
            "native_member_path": "standards/" + Path(path).name,
            "sha256": entries[Path(path).name]["sha256"]} for path in selection],
        "sections": len(chunks[0]["segments"]), "annotations": len(recipe["annotations"]),
        "records": {family: len(answer[family]) for family in ("concepts", "relations", "constraints", "latitude", "residuals")},
        "model": built["model"], "source_manifest_sha256": built["source_manifest_sha256"],
        "standing": "Fresh source-authored bounded visual; independent source-fidelity assessment is separate."})
    print(json.dumps({"out": str(out), "model": built["model"], "status": "built"}))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}), file=sys.stderr)
        raise SystemExit(2)
