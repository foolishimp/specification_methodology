"""Prepare the exact selected repair recheck and the unexposed functional matrix."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import tarfile

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
REP = REPO / "stdo_representation"
RUN1 = REP / "dogfood/t009-frame-projection/run-001"
RUN3 = REP / "dogfood/t009-frame-projection/run-003"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def copy(path, snapshot):
    dest = snapshot / path.relative_to(REPO)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, dest)


def main():
    subject_path = RUN3 / "construction-subject.json"
    if digest(subject_path) != "907ea9d5e2400314c9c81e601b0c215142d98286b6d1f66f8e79403c2d86b84a":
        raise RuntimeError("Construction subject drift")
    subject = json.loads(subject_path.read_text())
    verified = {str(subject_path.relative_to(REPO)): digest(subject_path)}
    for name, expected in subject["files"].items():
        path = RUN3 / name
        if digest(path) != expected:
            raise RuntimeError(f"Subject drift: {path}")
        verified[str(path.resolve().relative_to(REPO))] = expected
    for name, expected in subject["native_source_files"].items():
        path = REP / name
        if digest(path) != expected:
            raise RuntimeError(f"Native source drift: {path}")
        verified[str(path.relative_to(REPO))] = expected
    sm = json.loads((RUN1 / "source/source-manifest.json").read_text())
    records = []
    for member in sm["members"]:
        path = RUN1 / "source/standards" / member["path"]
        if digest(path) != member["sha256"]:
            raise RuntimeError(f"Source drift: {path}")
        records.append(member["sha256"] + "  " + member["path"] + "\n")
    aggregate = hashlib.sha256("".join(sorted(records, key=lambda x: x[66:])).encode()).hexdigest()
    if aggregate != subject["source_aggregate_sha256"]:
        raise RuntimeError("Source aggregate drift")
    axiom_subject = json.loads((RUN3 / "axiom-candidate-subject.json").read_text())
    for name, expected in axiom_subject["files"].items():
        path = REPO / "axiom_indexer" / name
        if digest(path) != expected:
            raise RuntimeError(f"Dependency drift: {path}")
        verified[str(path.relative_to(REPO))] = expected
    frozen = {"frozen_before_new_native_exposure": datetime.now(timezone.utc).isoformat(),
              "construction_subject_sha256": digest(subject_path), "source_aggregate_sha256": aggregate,
              "fp_oracles_sha256": digest(HERE / "oracles.json"),
              "functional_input_sha256": digest(HERE / "functional-run-001/case-inputs.json"),
              "functional_oracles_sha256": digest(HERE / "functional-run-001/oracles.json"),
              "files": verified,
              "scope": "Only FP04 projection recheck on both hosts, plus the not previously exposed functional32 matrix on both hosts and both evidence conditions. Source and case expectations remain unchanged. No source-baseline rerun."}
    (HERE / "run003-input-freeze.json").write_text(json.dumps(frozen, indent=2) + "\n")
    source_files = [RUN1 / "source/source-manifest.json"] + [RUN1 / "source/standards" / m["path"] for m in sm["members"]]
    projected_files = [subject_path, RUN3 / subject["program_file"], RUN3 / subject["map_file"],
                       RUN1 / "bindings.json", RUN3 / "axiom-candidate-subject.json"]
    projected_files += sorted((RUN3 / "projections").glob("*.json"))
    projected_files += [p for p in (REP / "skills/stdo-representation").rglob("*") if p.is_file()]
    projected_files += [REP / "releases/v2.5.0.md", REP / "specification/GOALS.md",
                        REP / "stdo_representation.json", REP / "specification/REFERENCE_FRAME_BASIS.md",
                        REP / ".ai-workspace/decisions/20260902T030553_frame_basis_rev16_acceptance.json"]
    projected_files += [REPO / "axiom_indexer" / name for name in ["build_tenants/core/code/ac.py",
                        "skills/axiomatize-corpus/references/program.schema.json",
                        "skills/axiomatize-corpus/references/output-contract.md"]]
    fp04 = RUN1 / "native-case-inputs/FP04.json"
    evidence = [REPO / e["repository_path"] for e in json.loads(fp04.read_text())["retained_evidence"]]
    for entry in json.loads(fp04.read_text())["retained_evidence"]:
        if digest(REPO / entry["repository_path"]) != entry["sha256"]:
            raise RuntimeError("FP04 evidence drift")
    all_contexts, fp_contexts, functional_contexts = [], [], []
    selections = [("fp04-run-003", h, "projection") for h in ("codex", "claude")]
    selections += [("functional-run-002", h, c) for h in ("codex", "claude") for c in ("source", "projection")]
    for run_name, host, condition in selections:
        functional = run_name.startswith("functional")
        dest = HERE / run_name / f"{host}-{condition}"
        snapshot = dest / "snapshot"
        snapshot.mkdir(parents=True, exist_ok=False)
        for path in source_files + (projected_files if condition == "projection" else []) + ([] if functional else [fp04] + evidence):
            copy(path, snapshot)
        rep = snapshot / "stdo_representation"
        if functional:
            for source, name in [(HERE / "functional-run-001/case-inputs.json", "case-inputs.json"),
                    (HERE / "functional-run-001/retained-preparation/cache.py", "cache.py"),
                    (HERE / "functional-run-001/retained-preparation/fixture_probe.py", "fixture_probe.py")]:
                shutil.copy2(source, rep / name)
        binding = {"kind": "axiom-indexer.binding-set", "schema_version": 1,
                   "bindings": [{"uri_prefix": "repo://stdo-t009-construction/" + aggregate + "/",
                                 "path": str(rep / "dogfood/t009-frame-projection/run-001/source")}]}
        (rep / "invocation-bindings.json").write_text(json.dumps(binding, indent=2) + "\n")
        inputs = {"kind": "t009.native-input-snapshot", "condition": condition,
                  "source_aggregate_sha256": aggregate,
                  "construction_subject_sha256": digest(subject_path),
                  "represented_source_release": None, "operative_stdo_release": subject["operative_stdo_release"],
                  "qualification_selection": "Explicit Executive native qualification of this exact construction candidate. " + ("Only case local grants a disposable cache.py edit and its fixture probe; all other cases are response-only." if functional else "FP04 is response-only; no operation effects."),
                  "relocation": {"original_bindings_sha256": digest(RUN1 / "bindings.json"),
                                 "invocation_bindings_file": "stdo_representation/invocation-bindings.json",
                                 "invocation_bindings_sha256": digest(rep / "invocation-bindings.json"),
                                 "rule": "Same source URI namespace and exact member bytes; explicitly selected physical relocation only."},
                  "excluded": "Author design, semantic-delta/conservation, expected outcomes and prior native answers are deliberately absent; they are not case inputs.",
                  "files": {str(p.relative_to(snapshot)): digest(p) for p in sorted(snapshot.rglob("*")) if p.is_file()}}
        (snapshot / "SNAPSHOT_INPUTS.json").write_text(json.dumps(inputs, indent=2) + "\n")
        subprocess.run(["git", "init", "--quiet", str(snapshot)], check=True)
        if condition == "projection":
            for native in (".agents", ".claude"):
                link = rep / native / "skills/stdo-representation"
                link.parent.mkdir(parents=True)
                link.symlink_to("../../skills/stdo-representation")
        if functional:
            prompt = (HERE / "functional-run-001" / f"{host}-{condition}" / "prompt.txt").read_text()
            prompt = prompt.replace("frozen run-002 construction-subject.json, unchanged run-001 program and sources", "frozen run-003 construction-subject.json, its exact program/map and retained source snapshot")
            prompt = prompt.replace("program in run-001, map in run-002", "program and map in run-003")
            start = "Return the actual local change and observed finite probe results, then a compact result for every case ID. State the material facts/delta, appropriate owner or frame, supported disposition and next work, and any unresolved condition; cite exact source routes, grouping shared routes if useful. Preserve differences among every named variant."
            replacement = "Return the actual cache.py change and owner fixture_probe.py observations. Then return one compact row/result for every case ID containing disposition, decisive fact or unknown, next lawful action and exact source route. Explain shared C/J/O distinctions once where unchanged; reuse common acquired source/evidence instead of repeating whole frame declarations for each variant. Preserve every named variant's distinct inputs."
            if start not in prompt:
                raise RuntimeError("Functional return contract changed unexpectedly")
            prompt = prompt.replace(start, replacement)
        else:
            prompt = (HERE / "fp-run-001" / f"{host}-projection" / "prompt.txt").read_text()
            prompt = prompt.replace("seven independent logical cases", "the one FP04 logical case")
            prompt = prompt.replace("All paths below", "All paths below")
            prompt = prompt.replace("Read all seven dogfood/t009-frame-projection/run-001/native-case-inputs/FP01.json through FP07.json.", "Read dogfood/t009-frame-projection/run-001/native-case-inputs/FP04.json.")
            prompt = prompt.replace("construction-subject.json", "construction-subject.json")
            prompt = prompt.replace("dogfood/t009-frame-projection/run-002/", "dogfood/t009-frame-projection/run-003/")
            prompt = prompt.replace("the program is in run-001 and map in run-002", "the program and map are in run-003")
            prompt = prompt.replace("Return one concise result for each FP01..FP07", "Return one concise result for FP04")
            prompt = prompt.replace("Evaluate FP01 through FP07 now using the selected evidence condition and return the seven bounded results.", "Evaluate FP04 now using the selected evidence condition and return its bounded result.")
        (dest / "prompt.txt").write_text(prompt)
        before = {str(p.relative_to(snapshot)): digest(p) for p in sorted(snapshot.rglob("*"))
                  if p.is_file() and ".git" not in p.relative_to(snapshot).parts and not p.is_symlink()}
        (dest / "snapshot-before.json").write_text(json.dumps(before, indent=2) + "\n")
        context = {"name": f"{run_name}/{host}-{condition}", "host": host, "condition": condition,
                   "directory": str(dest), "snapshot": str(snapshot), "cwd": str(rep),
                   "sandbox": "workspace-write" if functional else "read-only",
                   "allow_fixture_edit": functional, "prompt_sha256": digest(dest / "prompt.txt"),
                   "snapshot_manifest_sha256": digest(dest / "snapshot-before.json")}
        all_contexts.append(context)
        (functional_contexts if functional else fp_contexts).append(context)
    for name, contexts in [("fp04-run-003", fp_contexts), ("functional-run-002", functional_contexts)]:
        (HERE / name / "contexts.json").write_text(json.dumps({"prepared_at": datetime.now(timezone.utc).isoformat(),
              "candidate_sha256": digest(subject_path), "oracles_sha256": frozen["functional_oracles_sha256" if name.startswith("functional") else "fp_oracles_sha256"],
              "contexts": contexts}, indent=2) + "\n")
    (HERE / "run003-contexts.json").write_text(json.dumps({"contexts": all_contexts}, indent=2) + "\n")
    # Preserve the earlier unexposed snapshots as preparation, without gitlinks.
    old = HERE / "functional-run-001"
    for context in json.loads((old / "contexts.json").read_text())["contexts"]:
        dest = Path(context["directory"])
        snapshot = Path(context["snapshot"])
        expected = json.loads((dest / "snapshot-before.json").read_text())
        archive = dest / "unexposed-snapshot.tar.gz"
        with tarfile.open(archive, "w:gz", dereference=False) as tar:
            tar.add(snapshot, arcname="snapshot", filter=lambda m: None if ".git" in Path(m.name).parts else m)
        with tarfile.open(archive, "r:gz") as tar:
            actual = {str(Path(m.name).relative_to("snapshot")): hashlib.sha256(tar.extractfile(m).read()).hexdigest()
                      for m in tar.getmembers() if m.isfile()}
        if actual != expected:
            raise RuntimeError("Unexposed archive mismatch")
        (dest / "unexposed-archive-subject.json").write_text(json.dumps({"archive_sha256": digest(archive),
            "status": "Preparation only; no native invocation. Replaced by fresh run003-bound functional-run-002."}, indent=2) + "\n")
        shutil.rmtree(snapshot)
    print(json.dumps({"contexts": len(all_contexts), "source_aggregate_sha256": aggregate,
                      "input_freeze_sha256": digest(HERE / "run003-input-freeze.json")}, indent=2))


if __name__ == "__main__":
    main()
