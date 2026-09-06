"""Prepare one fresh local-case use of the selected stdout guidance repair."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import tarfile


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
REP = REPO / "stdo_representation"
RUN4 = REP / "dogfood/t009-frame-projection/run-004"
DEST = HERE / "output-scope-run-001"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n")


def main():
    DEST.mkdir(exist_ok=False)
    previous = HERE / "qualification-subject-001.json"
    if digest(previous) != "afdf9b61a6331068e31584209640e8c312fc7d1276d1345ea32db258a4a37726":
        raise RuntimeError("Previous native evidence freeze changed")
    for name, expected in json.loads(previous.read_text())["files"].items():
        if digest(HERE / name) != expected:
            raise RuntimeError(f"Previous evidence drift: {name}")
    subject_path = RUN4 / "construction-subject.json"
    if digest(subject_path) != "1d13124c1c298d6cde9f0193c3160532658401b90d9db24f6a5fd0cd57d88903":
        raise RuntimeError("Selected subject drift")
    subject = json.loads(subject_path.read_text())
    verified = {str(subject_path.relative_to(REPO)): digest(subject_path)}
    for name, expected in subject["files"].items():
        path = (RUN4 / name).resolve()
        if digest(path) != expected:
            raise RuntimeError(f"Construction member drift: {name}")
        verified[str(path.relative_to(REPO))] = expected
    for field in ("native_source_files", "owning_representation_files"):
        for name, expected in subject[field].items():
            path = (RUN4 / subject["representation_root"] / name).resolve()
            if digest(path) != expected:
                raise RuntimeError(f"Bound native/owner drift: {name}")
            verified[str(path.relative_to(REPO))] = expected
    source = REP / "dogfood/t009-frame-projection/run-001/source"
    source_manifest = json.loads((source / "source-manifest.json").read_text())
    for member in source_manifest["members"]:
        path = source / "standards" / member["path"]
        if digest(path) != member["sha256"]:
            raise RuntimeError(f"Source drift: {path}")
        verified[str(path.relative_to(REPO))] = member["sha256"]
    dep = json.loads((RUN4 / subject["axiom_candidate"]["subject_file"]).read_text())
    for name, expected in dep["files"].items():
        path = (RUN4 / subject["axiom_candidate"]["repository_root"] / name).resolve()
        if digest(path) != expected:
            raise RuntimeError(f"Dependency drift: {name}")
        verified[str(path.relative_to(REPO))] = expected
    functional = HERE / "functional-run-001"
    old_oracles = json.loads((functional / "oracles.json").read_text())
    oracle = {
        "kind": "t009.output-scope-local-native-oracles",
        "frozen_before_native_exposure": datetime.now(timezone.utc).isoformat(),
        "previous_qualification_subject_sha256": digest(previous),
        "original_functional_oracles_sha256": digest(functional / "oracles.json"),
        "unchanged_case_input_sha256": digest(functional / "case-inputs.json"),
        "candidate_subject_sha256": digest(subject_path),
        "selected_case": "local",
        "inherited_local_condition": old_oracles["conditions"][0],
        "necessary_and_sufficient_fixture_premises": "The fixture supplies complete unchanged Public identities/values, upstream/root/helper relations, current accepted D0/A0 complete trace and all other obligations. For this exact finite cache claim, the actual candidate must satisfy both declared owner probe outcomes. No reserved O or independent closing assessment applies. Missing or failing actual observations cannot be replaced by the supplied other facts.",
        "native_interface_condition": "Actor discovers/reads the selected native guide, selects a useful projection within its declared scope, and actually invokes the exact projector for read-only inspection. Every actual write must remain within the sole cache.py grant; output-file creation/deletion violates that condition even if final poststate hides it.",
        "evidence_condition": "Retain exact argv, model, input identities, raw tool operations, native owner probe and complete before/after files. Correct cache behavior and interface/grant conformity are assessed separately.",
        "scope": "One fresh Claude projection context only. No32case orFP04 rerun. Same original functional input, initial fixture and host capability; guide/current manifest and necessary physical invocation bindings change. No expected CLI spelling or outcome oracle is supplied to the actor."
    }
    write(DEST / "oracles.json", oracle)
    context_dir = DEST / "claude-projection"
    context_dir.mkdir()
    old_context = HERE / "functional-run-002/claude-projection"
    archive = old_context / "snapshot.tar.gz"
    archive_subject = json.loads((old_context / "archive-subject.json").read_text())
    if digest(archive) != archive_subject["archive_sha256"]:
        raise RuntimeError("Original snapshot archive drift")
    with tarfile.open(archive, "r:gz") as tar:
        tar.extractall(context_dir, filter="data")
    snapshot = context_dir / "snapshot"
    rep = snapshot / "stdo_representation"
    before_rebinding = {str(p.relative_to(snapshot)): digest(p) for p in snapshot.rglob("*")
                        if p.is_file() and not p.is_symlink()}
    if before_rebinding != archive_subject["files"]:
        raise RuntimeError("Reconstructed original snapshot drift")
    shutil.copy2(functional / "retained-preparation/cache.py", rep / "cache.py")
    guide = "skills/stdo-representation/references/frame-index-use.md"
    shutil.copy2(REP / guide, rep / guide)
    next_subject = rep / "dogfood/t009-frame-projection/run-004/construction-subject.json"
    next_subject.parent.mkdir()
    shutil.copy2(subject_path, next_subject)
    bindings = json.loads((rep / "invocation-bindings.json").read_text())
    bindings["bindings"][0]["path"] = str(rep / "dogfood/t009-frame-projection/run-001/source")
    write(rep / "invocation-bindings.json", bindings)
    inputs = json.loads((snapshot / "SNAPSHOT_INPUTS.json").read_text())
    inputs["construction_subject_sha256"] = digest(subject_path)
    inputs["qualification_selection"] = "Explicit Executive qualification of one local fixture case using the exact run-004 native guide and unchanged source/program/map/views. Only cache.py repair and the owner fixture probe are granted; the other31retained cases are outside this activation. No operation, adoption or successor frame acceptance."
    inputs["relocation"]["invocation_bindings_sha256"] = digest(rep / "invocation-bindings.json")
    inputs["files"] = {str(p.relative_to(snapshot)): digest(p) for p in sorted(snapshot.rglob("*"))
                       if p.is_file() and not p.is_symlink() and p != snapshot / "SNAPSHOT_INPUTS.json"}
    write(snapshot / "SNAPSHOT_INPUTS.json", inputs)
    subprocess.run(["git", "init", "--quiet", str(snapshot)], check=True)
    prompt = (old_context / "prompt.txt").read_text()
    prompt = prompt.replace("Apply the selected STDO source to the 32 ordinary cases in case-inputs.json. For case local, act as the already authorized bounded Writer and actually repair the disposable cache fixture and check it. For every other case, provide a response-only evaluation. Complete the requested work in this fresh context.",
        "Apply the selected STDO source to case local in case-inputs.json. Act as the already authorized bounded Writer and actually repair the disposable cache fixture and check it. The other retained cases are outside this activation. Complete the requested work in this fresh context.")
    prompt = prompt.replace("Read case-inputs.json in full, plus cache.py and fixture_probe.py for the actual local repair.",
        "Read case-inputs.json's shared fixture and local case, plus cache.py and fixture_probe.py for the actual local repair.")
    prompt = prompt.replace("frozen run-003 construction-subject.json", "frozen run-004 construction-subject.json")
    prompt = prompt.replace("Then return one compact row/result for every case ID containing disposition, decisive fact or unknown, next lawful action and exact source route. Explain shared C/J/O distinctions once where unchanged; reuse common acquired source/evidence instead of repeating whole frame declarations for each variant. Preserve every named variant's distinct inputs.",
        "Then return the local case's disposition, decisive fact or unknown, next lawful action and exact source route. State the material C/J/O distinction once.")
    prompt = prompt.replace("Handle all 32 cases now: perform only the explicitly granted disposable cache.py repair and probe, and give response-only assessments for the other 31 cases.",
        "Handle case local now: perform only the explicitly granted disposable cache.py repair and probe, then return its bounded result.")
    (context_dir / "prompt.txt").write_text(prompt)
    before = {str(p.relative_to(snapshot)): digest(p) for p in sorted(snapshot.rglob("*"))
              if p.is_file() and not p.is_symlink() and ".git" not in p.relative_to(snapshot).parts}
    write(context_dir / "snapshot-before.json", before)
    context = {"name": "output-scope-run-001/claude-projection", "host": "claude", "condition": "projection",
               "directory": str(context_dir), "snapshot": str(snapshot), "cwd": str(rep),
               "sandbox": "workspace-write", "allow_fixture_edit": True,
               "prompt_sha256": digest(context_dir / "prompt.txt"),
               "snapshot_manifest_sha256": digest(context_dir / "snapshot-before.json")}
    write(DEST / "contexts.json", {"prepared_at": datetime.now(timezone.utc).isoformat(),
          "candidate_sha256": digest(subject_path), "oracles_sha256": digest(DEST / "oracles.json"),
          "contexts": [context]})
    write(DEST / "input-subject-freeze.json", {"frozen_before_native_exposure": datetime.now(timezone.utc).isoformat(),
          "candidate_subject_sha256": digest(subject_path), "guide_sha256": digest(REP / guide),
          "oracles_sha256": digest(DEST / "oracles.json"), "contexts_sha256": digest(DEST / "contexts.json"),
          "runner_sha256": digest(HERE / "run_native_contexts.py"), "verified_source_files": verified,
          "original_snapshot_archive_sha256": digest(archive),
          "snapshot_delta_from_original_poststate": {key: {"before": before_rebinding.get(key), "after": before.get(key)}
              for key in sorted(set(before) | set(before_rebinding)) if before.get(key) != before_rebinding.get(key)},
          "host_capability": "Use unchanged original functional Claude runner and allowlist, not the separate FP04 directory-change correction. Exact argv/model remains observable in execution evidence."})
    print(json.dumps({"contexts": 1, "oracles_sha256": digest(DEST / "oracles.json"),
          "input_freeze_sha256": digest(DEST / "input-subject-freeze.json")}, indent=2))


if __name__ == "__main__":
    main()
