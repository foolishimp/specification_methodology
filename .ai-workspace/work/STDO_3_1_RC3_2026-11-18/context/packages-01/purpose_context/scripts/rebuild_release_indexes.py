#!/usr/bin/env python3
"""Construct separately named indexes from an actual selected native release."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import re
import sys

import rebuild_sdlc_index as development

PRODUCT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRODUCT / "skills/stdo-context/scripts"))
import context_catalog as catalog
import context_core as core

encoded = development.encoded
section = development.section
INDEXES = Path("skills/stdo-context/indexes")


def source_text(root: Path, ref: dict) -> bytes:
    lines = catalog.local_file(root, ref["source_id"]).read_bytes().splitlines(keepends=True)
    return b"".join(lines[ref["start_line"] - 1:ref["end_line"]])


def conserved_ref(old_root: Path, new_root: Path, ref: dict) -> dict:
    wanted = source_text(old_root, ref)
    lines = catalog.local_file(new_root, ref["source_id"]).read_bytes().splitlines(keepends=True)
    count = ref["end_line"] - ref["start_line"] + 1
    matches = [n for n in range(len(lines) - count + 1) if b"".join(lines[n:n + count]) == wanted]
    core.need(len(matches) == 1, "source ground is not uniquely conserved: " + str(ref))
    return {"source_id": ref["source_id"], "start_line": matches[0] + 1, "end_line": matches[0] + count}


def inputs_pin(names: list[str]) -> list[dict]:
    return [{"path": name, "sha256": core.raw_digest(catalog.local_file(PRODUCT, name).read_bytes())}
            for name in names]


def apply_source_amendment(rule: dict, amendment: dict, root: Path) -> None:
    """Apply an explicit reviewed successor claim, refusing changed source grounds."""
    core.need(rule["text"] == amendment["expected_text"],
              "rule amendment predecessor differs: " + rule["id"])
    refs = []
    for ground in amendment["grounds"]:
        ref = {k: ground[k] for k in ("source_id", "start_line", "end_line")}
        path_ref = {**ref, "source_id": ground["path"]}
        core.need(core.raw_digest(source_text(root, path_ref)) == ground["sha256"],
                  "amended source changed; re-enter " + rule["id"])
        refs.append(ref)
    core.need(bool(refs), "amended rule requires actual source grounds")
    rule["text"] = amendment["replacement_text"]
    rule["source_refs"] = refs


def apply_sdlc_amendments(rules: list[dict], root: Path, authoring: dict) -> None:
    """Apply owned, source-checked declarations without rewriting historical recipes."""
    for amendment in authoring.get("sdlc_rule_amendments", []):
        for ground in amendment["grounds"]:
            _, _, body = section(catalog.local_file(
                root, "standards/" + ground["source_id"] + ".md").read_bytes(), ground["heading"])
            core.need(core.raw_digest(body) == ground["section_sha256"],
                      "SDLC amendment source changed; re-enter " + amendment["rule_id"])
        matches = [rule for rule in rules if rule["id"] == amendment["rule_id"]]
        core.need(len(matches) == 1, "SDLC amendment rule is not unique")
        for field, change in amendment["fields"].items():
            core.need(matches[0].get(field) == change["expected"],
                      "SDLC amendment predecessor differs: " + amendment["rule_id"] + "." + field)
            matches[0][field] = copy.deepcopy(change["replacement"])


def native_sources(root: Path, method: dict, subject: str, rows: list[dict]) -> tuple[dict, dict, dict]:
    sources = {"profile": "purpose-context.sources/1", "subject_id": subject, "method": method,
               "source_root_kind": "installed-method-root", "method_manifest_path": "manifest.json",
               "files": [{"id": row["id"], "path": row["path"],
                          "sha256": core.raw_digest(catalog.local_file(root, row["path"]).read_bytes())}
                         for row in rows]}
    manifest = catalog.source_binding({"sources": sources}, root, method)
    return sources, manifest, core.corpus_view(manifest)


def python_index(root: Path, predecessor_root: Path, method: dict, authoring: dict,
                 previous: dict, version: str) -> tuple[dict, dict]:
    old_dir = PRODUCT / INDEXES / previous["id"]
    old_sources = core.read_json(old_dir / "SOURCES.json")
    old_index = core.read_json(old_dir / "INDEX.json")
    old_purpose = core.read_json(old_dir / "PURPOSE.json")
    for row in old_sources["files"]:
        core.need(core.raw_digest(catalog.local_file(predecessor_root, row["path"]).read_bytes()) == row["sha256"],
                  "predecessor source differs: " + row["id"])
    ident = "stdo-" + version + "-python-pure-refactor-v2"
    sources, manifest, view = native_sources(root, method,
        "urn:purpose-context:corpus:stdo-" + version + ":python-refactoring-closure-v2", old_sources["files"])
    purpose = copy.deepcopy(old_purpose)
    old_version = previous["method"]["uri"].removeprefix("stdo://releases/v").removesuffix("/")
    core.need(purpose["description"].count("STDO " + old_version) == 1, "unexpected predecessor purpose")
    purpose["description"] = purpose["description"].replace("STDO " + old_version, "STDO " + version)
    index = copy.deepcopy(old_index)
    moves = []
    for rule in index["rules"]:
        amendment = authoring.get("python_source_amendments", {}).get(rule["id"])
        if amendment is not None:
            apply_source_amendment(rule, amendment, root)
            continue
        for n, before in enumerate(rule["source_refs"]):
            after = conserved_ref(predecessor_root, root, before)
            rule["source_refs"][n] = after
            if before != after:
                moves.append({"rule_id": rule["id"], "before": before, "after": after,
                              "span_sha256": core.raw_digest(source_text(predecessor_root, before)),
                              "span_bytes_equal": True})
    amendment = authoring["python_carrier_amendment"]
    rule = next(r for r in index["rules"] if r["id"] == amendment["rule_id"])
    core.need(rule["text"] == amendment["expected_text"], "Python amendment predecessor differs")
    start, end, body = section(catalog.local_file(root, amendment["source_id"]).read_bytes(), amendment["heading"])
    core.need(core.raw_digest(body) == amendment["section_sha256"], "Python carrier section changed; re-enter authoring")
    rule["text"] += amendment["append_text"]
    rule["source_refs"] = [{"source_id": amendment["source_id"], "start_line": start, "end_line": end}]
    index.update(corpus_sha256=view["corpus_sha256"], input_view_sha256=view["view_sha256"],
                 purpose_sha256=core.digest(purpose))
    for coverage in index["source_coverage"]:
        grounded = [r["id"] for r in index["rules"]
                    if any(ref["source_id"] == coverage["source_id"] for ref in r["source_refs"])]
        coverage["rule_ids"] = [ident for ident in coverage["rule_ids"] if ident in grounded]
        coverage["rule_ids"] += [ident for ident in grounded if ident not in coverage["rule_ids"]]
    delta = {"profile": "purpose-context.release-source-delta/1", "predecessor_index": previous["id"],
             "source_members": [{"id": old["id"], "before_sha256": old["sha256"],
                                 "after_sha256": new["sha256"], "equal": old["sha256"] == new["sha256"]}
                                for old, new in zip(old_sources["files"], sources["files"], strict=True)],
             "conserved_span_moves": moves, "purpose_fact_meanings_equal": purpose["facts"] == old_purpose["facts"],
             "family_guard_equal": True,
             "rule_changes": [{"id": old["id"], "changed_fields": [k for k in old if old[k] != new[k]],
                               "before_sha256": core.digest(old), "after_sha256": core.digest(new)}
                              for old, new in zip(old_index["rules"], index["rules"], strict=True)],
             "authoring_disposition": amendment["disposition"],
             "source_coverage_equal": index["source_coverage"] == old_index["source_coverage"],
             "unresolved_equal": index["unresolved"] == old_index["unresolved"],
             "standing": "Author source-impact record; no independent semantic judgment or transferred assessment."}
    checked = core.validate_index(index, manifest, purpose, view)
    return artifacts(ident, previous, sources, purpose, index, view, delta, checked, authoring, version)


def sdlc_index(root: Path, method: dict, authoring: dict, previous: dict, version: str) -> tuple[dict, dict]:
    closure = core.read_json(PRODUCT / "authoring/sdlc-workflow/SOURCE-CLOSURE.json")
    recipe = core.read_json(PRODUCT / "authoring/sdlc-workflow/RULES.json")
    for row in recipe["requirements"]:
        core.need(core.raw_digest(catalog.local_file(PRODUCT, row["path"]).read_bytes()) == row["sha256"],
                  "SDLC authoring requirement changed; re-enter: " + row["path"])
    ident = "stdo-" + version + "-sdlc-workflow-v1"
    rows = [{"id": row["id"], "path": "standards/" + row["path"]} for row in closure["members"]]
    sources, manifest, view = native_sources(root, method,
        "urn:purpose-context:corpus:stdo-" + version + ":sdlc-workflow-v1", rows)
    purpose = core.read_json(PRODUCT / "authoring/sdlc-workflow/PURPOSE.json")
    old_purpose = core.read_json(PRODUCT / INDEXES / previous["id"] / "PURPOSE.json")
    purpose["description"] = purpose["description"].replace(
        "The selected development projection is a trial/adopted guidance subject under the caller separately bound complete constitution, not a partial constitution or published release.",
        "The selected guidance belongs to exact native STDO " + version + "; the caller binds its complete operative constitution and actual Product adoption. An index is not a partial constitution or an adoption decision.")
    purpose["facts"]["adopted_defaults"] = purpose["facts"]["adopted_defaults"].replace(
        "this exact development default projection", "this exact default projection from the selected native cut")
    purpose["facts"]["operative_basis"] = purpose["facts"]["operative_basis"].replace(
        "kept separate from this development source target", "matched to this selected native source target")
    rules = []
    for authored in recipe["rules"]:
        rule = {k: copy.deepcopy(v) for k, v in authored.items() if k != "grounds"}
        rule["source_refs"] = []
        amendment = authoring.get("sdlc_source_amendments", {}).get(rule["id"])
        if amendment is not None:
            apply_source_amendment(rule, amendment, root)
            rules.append(rule)
            continue
        for ground in authored["grounds"]:
            start, end, body = section(catalog.local_file(root, "standards/" + ground["source_id"] + ".md").read_bytes(), ground["heading"])
            core.need(core.raw_digest(body) == ground["section_sha256"], "SDLC deciding source changed; re-enter " + rule["id"])
            rule["source_refs"].append({"source_id": ground["source_id"], "start_line": start, "end_line": end})
        rules.append(rule)
    amendment = authoring["sdlc_source_role_amendment"]
    rule = next(r for r in rules if r["id"] == amendment["rule_id"])
    core.need(rule["text"] == amendment["expected_text"], "SDLC amendment predecessor differs")
    rule["text"] = amendment["replacement_text"]
    apply_sdlc_amendments(rules, root, authoring)
    old_index = core.read_json(PRODUCT / INDEXES / previous["id"] / "INDEX.json")
    old_sources = core.read_json(PRODUCT / INDEXES / previous["id"] / "SOURCES.json")
    index = {"profile": core.INDEX_PROFILE, "purpose_id": purpose["id"], "purpose_sha256": core.digest(purpose),
             "corpus_sha256": view["corpus_sha256"], "input_view_sha256": view["view_sha256"],
             "rules": rules, "source_coverage": copy.deepcopy(old_index["source_coverage"]),
             "unresolved": copy.deepcopy(recipe["unresolved"])}
    index["source_coverage"][0]["reason"] = "Adopted guidance from the selected native cut projects the workflow; its cited owning clauses decide."
    delta = {"profile": "purpose-context.release-source-delta/1", "predecessor_index": previous["id"],
             "source_members": [{"id": old["id"], "before_sha256": old["sha256"],
                                 "after_sha256": new["sha256"], "equal": old["sha256"] == new["sha256"]}
                                for old, new in zip(old_sources["files"], sources["files"], strict=True)],
             "purpose_changed_fields": [k for k in old_purpose if old_purpose[k] != purpose[k]],
             "fact_wording_changes": {k: {"before": old_purpose["facts"][k], "after": v}
                                      for k, v in purpose["facts"].items() if old_purpose["facts"][k] != v},
             "family_guard_equal": previous["family_guard"] == recipe["family_guard"],
             "rule_changes": [{"id": old["id"], "changed_fields": [k for k in old if old[k] != new[k]],
                               "before_sha256": core.digest(old), "after_sha256": core.digest(new)}
                              for old, new in zip(old_index["rules"], rules, strict=True)],
             "authoring_disposition": amendment["disposition"],
             "declared_rule_amendments": copy.deepcopy(authoring.get("sdlc_rule_amendments", [])),
             "source_coverage_before": old_index["source_coverage"],
             "source_coverage_after": index["source_coverage"],
             "unresolved_equal": index["unresolved"] == old_index["unresolved"],
             "standing": "Source role and exact-binding successor; no predecessor assessment transferred."}
    checked = core.validate_index(index, manifest, purpose, view)
    return artifacts(ident, previous, sources, purpose, index, view, delta, checked, authoring, version)


def artifacts(ident: str, previous: dict, sources: dict, purpose: dict, index: dict, view: dict,
              delta: dict, checked: dict, authoring: dict, version: str) -> tuple[dict, dict]:
    relative = INDEXES / ident
    names = ["scripts/rebuild_release_indexes.py", "scripts/rebuild_sdlc_index.py",
             "authoring/release-targets/" + version + ".json",
             "authoring/sdlc-workflow/SOURCE-CLOSURE.json", "authoring/sdlc-workflow/PURPOSE.json",
             "authoring/sdlc-workflow/RULES.json"]
    provenance = {"profile": "purpose-context.release-provenance/1", "index_id": ident,
                  "method": sources["method"], "construction_basis": core.read_json(PRODUCT / "stdo_purpose_context.json")["constitution"]["stdo"]["basis"],
                  "predecessor": previous, "inputs": inputs_pin(names), "source_delta_sha256": core.raw_digest(encoded(delta)),
                  "mechanical_validation": checked, "semantic_coverage": "unassessed", "covered": False,
                  "standing": "Exact native-cut index candidate; publication and applicable independent assessment are external records.",
                  "limits": ["Constraint coverage does not prove task admission, implementation correctness or acceptance.",
                             "An exact query needs its applicable external assessment; prior judgments are not transferred.",
                             "No implicit adoption, global installation or all-method compatibility is supplied."]}
    values = {"INDEX.json": index, "PURPOSE.json": purpose, "SOURCES.json": sources,
              "PROVENANCE.json": provenance, "SOURCE-DELTA.json": delta}
    generated = {relative / name: encoded(value) for name, value in values.items()}
    entry = {**copy.deepcopy(previous), "id": ident, "description": purpose["description"],
             "subject_id": sources["subject_id"], "method": sources["method"], "purpose_id": purpose["id"],
             "purpose_sha256": core.digest(purpose), "corpus_sha256": view["corpus_sha256"], "view_sha256": view["view_sha256"],
             "source_members": [{"id": row["id"], "sha256": row["sha256"]} for row in sources["files"]],
             "artifacts": {key: {"path": str(relative / name), "sha256": core.raw_digest(generated[relative / name])}
                           for key, name in [("index", "INDEX.json"), ("purpose", "PURPOSE.json"), ("sources", "SOURCES.json"), ("provenance", "PROVENANCE.json")]},
             "standing": "Exact native-cut constraint index; external exact-query assessment required for covered standing."}
    return entry, generated


def build(args: argparse.Namespace) -> dict:
    core.need(re.fullmatch(r"\d+\.\d+\.\d+(?:-rc\.\d+)?", args.version) is not None, "invalid exact release version")
    authoring = core.read_json(PRODUCT / "authoring/release-targets" / (args.version + ".json"))
    core.need(authoring["target_version"] == args.version, "release authoring target differs")
    method = {"uri": "stdo://releases/v" + args.version + "/", "manifest_sha256": args.method_manifest_sha256}
    core._sha(method["manifest_sha256"], "selected native manifest")
    root = args.method_root.absolute()
    raw = catalog.local_file(root, "manifest.json").read_bytes()
    native = json.loads(raw)
    core.need(core.raw_digest(raw) == method["manifest_sha256"] and native.get("kind") == "stdo.installed-release-manifest"
              and native["release"]["cut"] == "v" + args.version, "actual selected native cut or manifest differs")
    collection = core.read_json(PRODUCT / INDEXES / "CATALOG.json")
    by_id = {entry["id"]: entry for entry in collection["entries"]}
    py_entry, py_files = python_index(root, args.predecessor_source_root.absolute(), method, authoring,
                                      by_id[authoring["python_predecessor_index"]], args.version)
    sd_entry, sd_files = sdlc_index(root, method, authoring, by_id[authoring["sdlc_predecessor_index"]], args.version)
    selected = {py_entry["id"], sd_entry["id"]}
    collection["entries"] = [e for e in collection["entries"] if e["id"] not in selected] + [py_entry, sd_entry]
    generated = {**py_files, **sd_files, INDEXES / "CATALOG.json": encoded(collection)}
    public = core.read_json(PRODUCT / "PUBLIC_MANIFEST.json")
    public["release"] = {"version": args.version, "native_method": method,
                         "standing": "Release candidate; publication and qualification are externally recorded."}
    all_files = {p.relative_to(PRODUCT): p.read_bytes() for p in PRODUCT.rglob("*")
                 if p.is_file() and not p.is_symlink() and ".ai-workspace" not in p.parts
                 and "__pycache__" not in p.parts and p.name != "PUBLIC_MANIFEST.json" and p.suffix != ".pyc"}
    all_files.update(generated)
    public["files"] = [{"path": str(p), "sha256": core.raw_digest(body), "bytes": len(body)}
                       for p, body in sorted(all_files.items())]
    generated[Path("PUBLIC_MANIFEST.json")] = encoded(public)
    changed = [str(p) for p, body in generated.items() if not (PRODUCT / p).exists() or (PRODUCT / p).read_bytes() != body]
    if not args.check:
        for p, body in generated.items():
            development.write(PRODUCT / p, body)
    return {"status": "stale" if args.check and changed else "current" if args.check else "rebuilt",
            "method": method, "indexes": sorted(selected), "changed_files": changed,
            "public_manifest_sha256": core.raw_digest(generated[Path("PUBLIC_MANIFEST.json")])}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True)
    parser.add_argument("--method-root", type=Path, required=True)
    parser.add_argument("--method-manifest-sha256", required=True)
    parser.add_argument("--predecessor-source-root", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        result = build(args)
        print(json.dumps(result, indent=2))
        return 1 if result["status"] == "stale" else 0
    except (core.Refusal, OSError, ValueError, KeyError, StopIteration) as error:
        print(json.dumps({"status": "refused", "reason": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
