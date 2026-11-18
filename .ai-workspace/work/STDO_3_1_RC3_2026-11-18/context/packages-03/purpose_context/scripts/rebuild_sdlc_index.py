#!/usr/bin/env python3
"""Rebuild one authored SDLC index with the existing context core; no model calls."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import tempfile

PRODUCT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRODUCT / "skills/stdo-context/scripts"))
import context_core as core

AUTHORING = PRODUCT / "authoring/sdlc-workflow"
INDEX_ID = "stdo-development-sdlc-workflow-v1"
RELATIVE = Path("skills/stdo-context/indexes") / INDEX_ID
METHOD_URI = "urn:stdo:development-source:sdlc-defaults-2026-11-14"
PREDECESSOR = {"uri": "stdo://releases/v3.0.5-rc.1/", "manifest_sha256": "64c026667abba933d289317793dbe80b5f9ab822a9870307795584402e460e1c"}


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(value if isinstance(value, bytes) else encoded(value))


def section(body, heading):
    lines = body.decode("utf-8").splitlines(keepends=True)
    matches = [n for n, line in enumerate(lines) if line.rstrip("\r\n") == heading]
    core.need(len(matches) == 1, "source heading not unique: " + heading)
    start = matches[0]
    level = len(heading) - len(heading.lstrip("#"))
    end = len(lines)
    for n in range(start + 1, len(lines)):
        match = re.match(r"^(#{1,6}) ", lines[n])
        if match and len(match[1]) <= level:
            end = n
            break
    return start + 1, end, "".join(lines[start:end]).encode()


def generate(source_root, output):
    closure = core.read_json(AUTHORING / "SOURCE-CLOSURE.json")
    purpose = core.read_json(AUTHORING / "PURPOSE.json")
    recipe = core.read_json(AUTHORING / "RULES.json")
    for row in recipe["requirements"]:
        core.need(core.raw_digest((PRODUCT / row["path"]).read_bytes()) == row["sha256"],
                  "authoring requirements changed; re-enter affected meanings: " + row["path"])
    source_bytes = {}
    members = []
    for row in closure["members"]:
        relative = Path(row["path"])
        core.need(not relative.is_absolute() and ".." not in relative.parts, "source path is not portable")
        path = source_root / relative
        core.need(path.is_file() and not path.is_symlink() and
                  all(not x.is_symlink() for x in path.parents), "source is not a regular physical file")
        body = path.read_bytes()
        source_bytes[row["id"]] = body
        members.append({"path": row["path"], "sha256": core.raw_digest(body)})
        write(output / "source/standards" / row["path"], body)
    candidate = {"profile": "purpose-context.development-method-manifest/1", "method_uri": METHOD_URI,
                 "standing": "development-source; unpublished; unqualified", "predecessor": PREDECESSOR,
                 "standards": {"installed_root": "standards", "members": members}}
    write(output / "source/manifest.json", candidate)
    method = {"uri": METHOD_URI, "manifest_sha256": core.raw_digest(encoded(candidate))}
    sources = {"profile": "purpose-context.sources/1", "subject_id": closure["subject_id"], "method": method,
               "source_root_kind": "development-method-root", "method_manifest_path": "manifest.json",
               "files": [{"id": row["id"], "path": "standards/" + row["path"], "sha256": member["sha256"]}
                         for row, member in zip(closure["members"], members)]}
    manifest = {"profile": core.CORPUS_PROFILE, "subject_id": sources["subject_id"], "method": method,
                "files": [{**row, "path": str((output / "source" / row["path"]).resolve())} for row in sources["files"]]}
    view = core.corpus_view(manifest)
    rules = []
    for authored in recipe["rules"]:
        rule = {key: value for key, value in authored.items() if key != "grounds"}
        rule["source_refs"] = []
        for ground in authored["grounds"]:
            start, end, body = section(source_bytes[ground["source_id"]], ground["heading"])
            core.need(core.raw_digest(body) == ground["section_sha256"],
                      "source ground changed; re-enter rule " + rule["id"] + ": " + ground["heading"])
            rule["source_refs"].append({"source_id": ground["source_id"], "start_line": start, "end_line": end})
        rules.append(rule)
    index = {"profile": core.INDEX_PROFILE, "purpose_id": purpose["id"], "purpose_sha256": core.digest(purpose),
             "corpus_sha256": view["corpus_sha256"], "input_view_sha256": view["view_sha256"], "rules": rules,
             "source_coverage": [], "unresolved": recipe["unresolved"]}
    for row in closure["members"]:
        ids = [rule["id"] for rule in rules if any(g["source_id"] == row["id"] for g in rule["source_refs"])]
        index["source_coverage"].append({"source_id": row["id"], "status": "represented" if ids else "no_applicable_rules",
                                         "rule_ids": ids, "reason": row["purpose_relation"]})
    checked = core.validate_index(index, manifest, purpose, view)
    inputs = ["specification/requirements/README.md", "specification/requirements/SDLC-WORKFLOW.md",
              "authoring/sdlc-workflow/SOURCE-CLOSURE.json", "authoring/sdlc-workflow/PURPOSE.json",
              "authoring/sdlc-workflow/RULES.json", "scripts/rebuild_sdlc_index.py"]
    provenance = {"profile": "purpose-context.sdlc-provenance/1", "index_id": INDEX_ID,
                  "standing": "authored development candidate; semantic coverage unassessed",
                  "predecessor": PREDECESSOR, "construction_basis": core.read_json(PRODUCT / "stdo_purpose_context.json")["constitution"]["stdo"]["basis"],
                  "coverage_predicate": purpose["description"], "source_closure": closure,
                  "inputs": [{"path": name, "sha256": core.raw_digest((PRODUCT / name).read_bytes())} for name in inputs],
                  "rebuild": "python3 -B purpose_context/scripts/rebuild_sdlc_index.py --source-root specification_methodology/v3/build_tenants/common/standards",
                  "check": "Append --check to compare without changing generated files.",
                  "mechanical_validation": checked,
                  "assessment": "External exact-index/corpus/query assessment only; no old verdict transferred.",
                  "limits": ["A candidate source selection is not an operative partial constitution or published cut.",
                             "Workflow constraints do not prove task admission, repair success, policy selection or boundary acceptance.",
                             "Processing ledger and deterministic controls cannot certify source-semantic completeness.",
                             "Technical specialist design/profile law and concrete Product requirements are separately acquired task inputs."]}
    for name, value in (("INDEX.json", index), ("PURPOSE.json", purpose), ("SOURCES.json", sources), ("PROVENANCE.json", provenance)):
        write(output / name, value)
    artifacts = {key: {"path": str(RELATIVE / name), "sha256": core.raw_digest((output / name).read_bytes())}
                 for key, name in (("index", "INDEX.json"), ("purpose", "PURPOSE.json"), ("sources", "SOURCES.json"), ("provenance", "PROVENANCE.json"))}
    entry = {"id": INDEX_ID, "description": "Explicit development SDLC workflow defaults; ordinary QA, diagnosis, bounded repair, boundary and reuse constraints.",
             "subject_id": sources["subject_id"], "method": method, "purpose_id": purpose["id"], "purpose_sha256": core.digest(purpose),
             "corpus_sha256": view["corpus_sha256"], "view_sha256": view["view_sha256"],
             "source_members": [{"id": row["id"], "sha256": row["sha256"]} for row in sources["files"]],
             "family_guard": recipe["family_guard"], "artifacts": artifacts,
             "standing": "development candidate; explicit trial/adoption only; external exact-query assessment required for covered standing"}
    return entry


def public_manifest():
    value = core.read_json(PRODUCT / "PUBLIC_MANIFEST.json")
    paths = sorted(path for path in PRODUCT.rglob("*") if path.is_file() and not path.is_symlink()
                   and ".ai-workspace" not in path.parts and "__pycache__" not in path.parts
                   and path.name != "PUBLIC_MANIFEST.json" and path.suffix != ".pyc")
    value["files"] = [{"path": str(path.relative_to(PRODUCT)), "sha256": core.raw_digest(path.read_bytes()),
                       "bytes": path.stat().st_size} for path in paths]
    return encoded(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="purpose-context-sdlc-") as temporary:
        temporary = Path(temporary)
        entry = generate(args.source_root.resolve(), temporary)
        catalog_path = PRODUCT / "skills/stdo-context/indexes/CATALOG.json"
        catalog = core.read_json(catalog_path)
        entries = [row for row in catalog["entries"] if row["id"] != INDEX_ID]
        entries.append(entry)
        catalog["entries"] = entries
        changes = []
        generated = {PRODUCT / RELATIVE / path.relative_to(temporary): path.read_bytes()
                     for path in temporary.rglob("*") if path.is_file()}
        generated[catalog_path] = encoded(catalog)
        for path, body in generated.items():
            if not path.exists() or path.read_bytes() != body:
                changes.append(str(path.relative_to(PRODUCT)))
                if not args.check:
                    write(path, body)
        public = public_manifest()
        manifest_path = PRODUCT / "PUBLIC_MANIFEST.json"
        if manifest_path.read_bytes() != public:
            changes.append("PUBLIC_MANIFEST.json")
            if not args.check:
                manifest_path.write_bytes(public)
        print(json.dumps({"status": "stale" if args.check and changes else "current" if args.check else "rebuilt",
                          "index_id": INDEX_ID, "method": entry["method"], "changed_files": changes,
                          "public_manifest_sha256": core.raw_digest(manifest_path.read_bytes())}, indent=2))
        return 1 if args.check and changes else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (core.Refusal, OSError, ValueError, KeyError) as error:
        print(json.dumps({"status": "refused", "reason": str(error)}), file=sys.stderr)
        raise SystemExit(2)
