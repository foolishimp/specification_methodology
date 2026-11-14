#!/usr/bin/env python3
"""Reproduce the portable P1 index without reauthoring its deciding content."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import sys

PRODUCT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRODUCT / "skills/stdo-context/scripts"))
import context_core as core

INDEX_ID = "stdo-3.0.4-python-pure-refactor-p1"
SUBJECT = "urn:purpose-context:corpus:stdo-3.0.4:refactoring-owners"
PINS = {
    "index": ("successor-01/execution/runs/ci02s1-index-P1/submissions/0045.json", "4fdb76d862d4ff7a9adedcf1cb6387804e39daff714cd45ecca48fb198bd3f05"),
    "corpus": ("corpus/MANIFEST.json", "0574186af2bf74f2bb398dd7ac0ee214b3db76669e30d6ea23764ff7b24622a0"),
    "workload": ("successor-01/preparation/WORKLOAD.json", "b6a54e8b278d0ba10f562416e79562fd832210595ff38e8d84545a71d6a53bb2"),
    "working_basis": ("final/WORKING-BASIS.json", "b025be5332a66d53dd488843faa840ae3b4d1e50518c0eb27b68fbc862af001c"),
    "report": ("final/REPORT.md", "5f309ab51b7881a68bdcc539d54b1f3029f7afdb17a7a5059e1b7d0a557566b6"),
}
FACTS = {
    "accepted_design_available": "Whether an accepted design for the actual task is available.",
    "action": "The authorized kind of work; realization_refactor for this index family.",
    "authority_changed": "Whether the task changes authority boundaries.",
    "effects_changed": "Whether externally observable effects change.",
    "language": "Implementation language selected for the task.",
    "language_version": "Exact language version stipulated for the task family.",
    "profile_design_module": "Whether DESIGN_MODULE is actually adopted for the target work.",
    "public_semantics_changed": "Whether public semantics or admitted domains change.",
    "pure_local": "Whether the task is a pure local deterministic transformation.",
    "role": "Actor role bound by the actual activation.",
    "sdlc_phase": "The SDLC phase of the actual work.",
    "source_state": "Whether the caller-selected governing source is current for that work.",
    "target_product": "Caller target Product identity; descriptive, never the reusable corpus identity.",
    "task": "Caller task identity; descriptive and not an applicability shortcut.",
    "grant": "Existing caller work authorization coordinate; descriptive, not newly granted by this index.",
}


def write(path: Path, value: object) -> None:
    with path.open("xb") as stream:
        stream.write((json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n").encode())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comparison-root", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, required=True, help="actual installed STDO method root")
    parser.add_argument("--out", type=Path, required=True, help="new indexes directory; refuses to overwrite")
    args = parser.parse_args()
    old = {}
    evidence = {}
    for name, (relative, expected) in PINS.items():
        data = (args.comparison_root / relative).read_bytes()
        core.need(core.raw_digest(data) == expected, "historical input differs: " + name)
        evidence[name] = {"subject": "urn:t020:ci02:" + relative, "sha256": expected, "bytes": len(data)}
        if name in {"index", "corpus", "workload"}:
            old[name] = json.loads(data)
    method = old["corpus"]["method"]
    core.need(core.raw_digest((args.source_root / "manifest.json").read_bytes()) == method["manifest_sha256"], "actual method manifest differs")
    portable_files = [{"id": row["id"], "path": row["id"], "sha256": row["sha256"]} for row in old["corpus"]["files"]]
    sources = {"profile": "purpose-context.sources/1", "subject_id": SUBJECT, "method": method,
               "source_root_kind": "installed-method-root", "method_manifest_path": "manifest.json", "files": portable_files}
    manifest = {"profile": core.CORPUS_PROFILE, "subject_id": SUBJECT, "method": method,
                "files": [{**row, "path": str((args.source_root / row["path"]).resolve())} for row in portable_files]}
    view = core.corpus_view(manifest)
    workload = old["workload"]
    core.need(workload["id"] == old["index"]["workload_id"] == "python-pure-refactor/1", "historical workload differs")
    purpose = {"id": workload["id"], "description": workload["scope"] + " " + workload["source_scope"], "facts": FACTS}
    index = copy.deepcopy(old["index"])
    index.pop("workload_id")
    index.update({"profile": core.INDEX_PROFILE, "purpose_id": purpose["id"], "purpose_sha256": core.digest(purpose),
                  "corpus_sha256": view["corpus_sha256"], "input_view_sha256": view["view_sha256"]})
    core.validate_index(index, manifest, purpose, view)
    preserved = {}
    for field in ("rules", "source_coverage", "unresolved"):
        core.need(index[field] == old["index"][field], "authored population changed: " + field)
        preserved[field] = {"unchanged": True, "canonical_sha256": core.digest(index[field]), "items": len(index[field])}
    core.need(len(index["rules"]) == 68, "expected selected P1 rule population")
    proof = {"profile": "purpose-context.index-port/1", "index_id": INDEX_ID, "historical_inputs": evidence,
             "transform": "Envelope identity/profile rebinding only; no rule, coverage-ledger or unresolved-content edits.",
             "changes": {"profile": {"from": old["index"]["profile"], "to": index["profile"]},
                         "purpose": "workload_id becomes purpose_id plus explicit purpose identity; caller target/task/grant facts remain separate",
                         "corpus": "same ordered source IDs and hashes, stable reusable corpus subject, current portable corpus/view profiles"},
             "preserved": preserved,
             "rules": [{"id": rule["id"], "canonical_sha256": core.digest(rule)} for rule in index["rules"]],
             "family_guard_origin": "Exact common stipulated family facts from the frozen workload, now tested against each caller query.",
             "historical_evidence": {"source_discriminators": "P1 retained 12/12 audited meanings in a finite independent source review.",
                                     "code_trials": "P1 supplied three held-out pure/local Python task candidates; all three met the finite checked conditions.",
                                     "scope": "One four-owner STDO 3.0.4 corpus and one workload family. This port ran no new model or task campaign."},
             "standing": "Experimental working basis. Historical assessments are not transferred to new index/corpus/query identities.",
             "semantic_coverage": "unassessed", "covered": False,
             "limits": ["Not all source meaning was assessed.", "External source owners remain excluded and explicit residuals are preserved.",
                        "No other release, broad code build, SDLC purpose or language is qualified by this artifact."]}
    core.need(not args.out.exists(), "output already exists; preserve prior generated assets")
    destination = args.out / INDEX_ID
    destination.mkdir(parents=True)
    artifacts = {}
    for name, value in (("index", index), ("purpose", purpose), ("sources", sources), ("provenance", proof)):
        path = destination / (name.upper() + ".json")
        write(path, value)
        artifacts[name] = {"path": "skills/stdo-context/indexes/" + INDEX_ID + "/" + path.name,
                           "sha256": core.raw_digest(path.read_bytes())}
    entry = {"id": INDEX_ID, "description": "STDO 3.0.4 pure/local Python refactoring under adopted DESIGN_MODULE; preserved P1 working basis.",
             "subject_id": SUBJECT, "method": method, "purpose_id": purpose["id"], "purpose_sha256": core.digest(purpose),
             "corpus_sha256": view["corpus_sha256"], "view_sha256": view["view_sha256"],
             "source_members": [{"id": row["id"], "sha256": row["sha256"]} for row in portable_files],
             "family_guard": {"all": [{"fact": name, "op": "eq", "value": value} for name, value in sorted(workload["facts"].items())], "any": []},
             "artifacts": artifacts, "standing": proof["standing"]}
    write(args.out / "CATALOG.json", {"profile": "purpose-context.index-catalog/1", "entries": [entry]})
    print(json.dumps({"status": "ported", "index_id": INDEX_ID, "rules": 68, "preserved": preserved,
                      "artifacts": artifacts, "catalog_sha256": core.raw_digest((args.out / "CATALOG.json").read_bytes())}, sort_keys=True))


if __name__ == "__main__":
    main()
