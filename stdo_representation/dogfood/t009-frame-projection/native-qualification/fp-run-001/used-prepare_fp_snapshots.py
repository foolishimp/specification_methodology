"""Prepare finite native qualification inputs without exposing expected outcomes."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
REP = REPO / "stdo_representation"
RUN1 = REP / "dogfood/t009-frame-projection/run-001"
RUN2 = REP / "dogfood/t009-frame-projection/run-002"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def copy_file(path, snapshot):
    target = snapshot / path.relative_to(REPO)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, target)
    if digest(target) != digest(path):
        raise RuntimeError(f"Copy mismatch: {path}")


def main():
    if not (HERE / "oracles.json").is_file():
        raise RuntimeError("Oracles must be frozen first")
    subject = json.loads((RUN2 / "construction-subject.json").read_text())
    source_manifest = json.loads((RUN1 / "source/source-manifest.json").read_text())
    case_files = sorted((RUN1 / "native-case-inputs").glob("FP*.json"))
    evidence_files = {REPO / e["repository_path"] for f in case_files
                      for e in json.loads(f.read_text())["retained_evidence"]}
    common = case_files + sorted(evidence_files) + [RUN1 / "source/source-manifest.json"]
    common += [RUN1 / "source/standards" / m["path"] for m in source_manifest["members"]]
    projection = [RUN1 / "axiomatic-program.json", RUN1 / "bindings.json",
                  RUN2 / "construction-subject.json", RUN2 / "logical-constraint-map.json",
                  RUN2 / "axiom-candidate-subject.json"]
    projection += sorted((RUN2 / "projections").glob("*.json"))
    projection += [p for p in (REP / "skills/stdo-representation").rglob("*") if p.is_file()]
    projection += [REP / "releases/v2.5.0.md", REP / "specification/GOALS.md",
                   REP / "stdo_representation.json", REP / "specification/REFERENCE_FRAME_BASIS.md",
                   REP / ".ai-workspace/decisions/20260902T030553_frame_basis_rev16_acceptance.json"]
    projection += [REPO / "axiom_indexer" / p for p in [
        "build_tenants/core/code/ac.py",
        "skills/axiomatize-corpus/references/program.schema.json",
        "skills/axiomatize-corpus/references/output-contract.md"]]
    contexts = []
    for host in ("codex", "claude"):
        for condition in ("source", "projection"):
            name = f"{host}-{condition}"
            dest = HERE / "fp-run-001" / name
            snapshot = dest / "snapshot"
            if dest.exists():
                raise RuntimeError(f"Refusing to overwrite {dest}")
            snapshot.mkdir(parents=True)
            for path in common + (projection if condition == "projection" else []):
                copy_file(path, snapshot)
            subprocess.run(["git", "init", "--quiet", str(snapshot)], check=True)
            snapshot_rep = snapshot / "stdo_representation"
            relocated_source = snapshot_rep / "dogfood/t009-frame-projection/run-001/source"
            binding = {
                "kind": "axiom-indexer.binding-set", "schema_version": 1,
                "bindings": [{"uri_prefix": "repo://stdo-t009-construction/" +
                    source_manifest["source_set_sha256"] + "/", "path": str(relocated_source)}]}
            (snapshot_rep / "invocation-bindings.json").write_text(json.dumps(binding, indent=2) + "\n")
            if condition == "projection":
                for native in (".agents", ".claude"):
                    path = snapshot_rep / native / "skills/stdo-representation"
                    path.parent.mkdir(parents=True)
                    path.symlink_to("../../skills/stdo-representation")
            inputs = {
                "kind": "t009.native-read-only-input-snapshot",
                "condition": condition,
                "source_aggregate_sha256": source_manifest["source_set_sha256"],
                "original_construction_subject_sha256": digest(RUN2 / "construction-subject.json"),
                "represented_source_release": None,
                "operative_stdo_release": subject["operative_stdo_release"],
                "qualification_selection": "Explicit Executive selection of this frozen source candidate for read-only native semantic evaluation. No source adoption, frame-basis successor acceptance, release or consumer operation is selected.",
                "relocation": {"original_bindings_sha256": digest(RUN1 / "bindings.json"),
                    "invocation_bindings_file": "stdo_representation/invocation-bindings.json",
                    "invocation_bindings_sha256": digest(snapshot_rep / "invocation-bindings.json"),
                    "rule": "Same exact URI namespace and source member bytes; physical snapshot binding only. Original bindings are retained evidence, not this invocation's routing."},
                "excluded": "Design, semantic-source comparison, expected outcomes, author worker results and earlier native answers are deliberately absent. Their absence is not a missing semantic premise in a case.",
                "files": {str(p.relative_to(snapshot)): digest(p) for p in sorted(snapshot.rglob("*"))
                    if p.is_file() and ".git" not in p.relative_to(snapshot).parts and not p.is_symlink()}}
            (snapshot / "SNAPSHOT_INPUTS.json").write_text(json.dumps(inputs, indent=2) + "\n")
            role = "You are a fresh, bounded semantic evaluator. Evaluate seven independent logical cases from their stated facts and retained evidence, and return your own assessments."
            subject_text = (
                "This is explicitly authorized T009 read-only qualification of the frozen working-source subject, not ordinary released use or successor acceptance. "
                "The caller's operating STDO basis is v2.5.0-rc.4. The represented candidate source is the exact 52-member snapshot with aggregate "
                + source_manifest["source_set_sha256"] + ". Read ../SNAPSHOT_INPUTS.json for identities and invocation relocation. "
                "All paths below are relative to the current stdo_representation directory unless stated otherwise. "
                "The cases describe retained isolated run006 evidence and explicit logical variants; their historical paths are evidence identities, not permission to inspect or operate on current external consumers. "
                "Select and explain the Worker and/or Reviewer source frame appropriate to each requested evaluation. Evaluation of a permitted next action is not execution of that action.")
            hard = (
                "Read only within this snapshot. Do not perform consumer, updater, publication, source-edit or git mutation operations; do not change any files. "
                "Do not search the parent repository, network, author design, expected outcomes, past native answers or other actors' results. "
                "Treat each case's explicitly stipulated facts as inputs for that case; do not import another case's facts to fill its missing premises. "
                "Use exact evidence to assess the bounded claims, with uncertainty and qualification where warranted. This session is authorized to complete the logical evaluations and return; no additional operation effects are authorized.")
            common_routes = (
                "Read all seven dogfood/t009-frame-projection/run-001/native-case-inputs/FP01.json through FP07.json. "
                "Their retained_evidence.repository_path values resolve from the snapshot root (one directory above this working directory). "
                "Those six retained evidence files are copied byte-for-byte. The case facts and questions are the same in both evidence conditions.")
            if condition == "source":
                context = common_routes + (
                    " Evaluate directly from the exact owning source files in dogfood/t009-frame-projection/run-001/source/standards/. "
                    "Start with SPEC_METHOD.md#explicit-complete-consumer-update and #computed-classification-and-treatment; "
                    "TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity and #condition-based-closure-and-reuse; "
                    "REFERENCE_FRAME_METHOD.md#applicability-and-required-results, #return-a-closed-result and #result-conjunction; "
                    "STDO_REFERENCE_FRAME_BASELINE.md#engagement-applicability, #derived-worker-frame and #derived-reviewer-frame. "
                    "Follow other material source sections if needed. No program, map, derived view or candidate skill is supplied in this source-only condition.")
            else:
                context = common_routes + (
                    " Use $stdo-representation (Claude: the stdo-representation skill) from this snapshot's native skill route. "
                    "The exact current candidate is selected, through skills/stdo-representation/references/frame-index-use.md and "
                    "dogfood/t009-frame-projection/run-002/construction-subject.json. "
                    "Start from the map's declared indexes, judge the applicable selection, then invoke the exact candidate projector in materialized mode with your chosen index URI(s), "
                    "using ../axiom_indexer/build_tenants/core/code/ac.py and invocation-bindings.json for this relocated snapshot. "
                    "Use stdout (omit --output); the program is in run-001 and map in run-002. "
                    "The original binding file is retained provenance; using its original absolute path would leave this snapshot and is outside the invocation. "
                    "Read the resulting materialized clauses and their source routes; re-enter exact owning source when meaning requires. "
                    "The manifest references author proof/design deliberately excluded from the snapshot; these are not required semantic case inputs. "
                    "This exact candidate handoff supersedes ordinary released-map acquisition for this evaluation only; do not try to fetch tags or install a release.")
            open_space = "Choose your own bounded inspection tools and evidence reading order. Do not assume an authored rule's referenced premise is already observed evidence. Identify material contradictions if present."
            return_text = (
                "Return one concise result for each FP01..FP07: selected source frame(s) and why; exact supported/unsupported or indeterminate claim; "
                "material C facts, residual J and original O where applicable; satisfied or missing premises, conditions and exceptions; "
                "permitted next-work assessment, uncertainty and invalidators; and exact source routes. "
                "Your results must be your own evaluation, not a copied author verdict. Summarize the actual input/tool verification and stop after the response. "
                "Do not draft a prompt for another actor or defer these requested evaluations merely to propose doing them.")
            sections = [("Role and outcome", role), ("Reference frame and exact subject", subject_text),
                        ("Hard constraints", hard), ("Index context and evidence routes", context),
                        ("Open solution space", open_space), ("Return and stop contract", return_text),
                        ("ACTION", "Evaluate FP01 through FP07 now using the selected evidence condition and return the seven bounded results.")]
            if host == "claude":
                prompt = "\n\n".join(f"<{label.lower().replace(' ', '_')}>\n{body}\n</{label.lower().replace(' ', '_')}>" for label, body in sections) + "\n"
            else:
                prompt = "\n\n".join(f"{label}\n{body}" for label, body in sections) + "\n"
            (dest / "prompt.txt").write_text(prompt)
            before = {str(p.relative_to(snapshot)): digest(p) for p in sorted(snapshot.rglob("*"))
                      if p.is_file() and ".git" not in p.relative_to(snapshot).parts and not p.is_symlink()}
            (dest / "snapshot-before.json").write_text(json.dumps(before, indent=2) + "\n")
            contexts.append({"name": name, "host": host, "condition": condition,
                "directory": str(dest), "cwd": str(snapshot_rep), "snapshot": str(snapshot),
                "prompt_sha256": digest(dest / "prompt.txt"), "snapshot_manifest_sha256": digest(dest / "snapshot-before.json")})
    result = {"prepared_at": datetime.now(timezone.utc).isoformat(),
              "oracles_sha256": digest(HERE / "oracles.json"), "contexts": contexts}
    (HERE / "fp-run-001/contexts.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"contexts": len(contexts), "manifest": str(HERE / "fp-run-001/contexts.json")}, indent=2))


if __name__ == "__main__":
    main()
