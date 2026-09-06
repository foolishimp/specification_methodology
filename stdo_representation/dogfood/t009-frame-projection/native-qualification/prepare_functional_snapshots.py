"""Bind the already selected finite functional cases to fresh native snapshots."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
OUT = HERE / "functional-run-001"
RETAINED = OUT / "retained-preparation"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    original = json.loads((RETAINED / "cases.json").read_text())
    original["shared_fixture"]["candidate_facts"] = {
        "L1": {
            "public": "Complete Public identities and serialized values equal public_before.",
            "upstream_root_helper": "All upstream, root and helper relations unchanged.",
            "other_obligations": "All other declared cache-repair obligations satisfied.",
            "variable_inputs": "Only the per-case supplied cache observations and accepted-design coverage remain variable. A case-local design_input or observations value overrides only its named variable.",
            "reserved_owner_acceptance": False,
            "author_independent_review_required": False,
        }
    }
    clarification = (
        "Root fixture-owner clarification before exposure: L1 is the shared case subject with complete Public identities and serialized values equal public_before, all upstream/root/helper relations unchanged, and all other declared cache-repair obligations satisfied; only the per-case supplied cache observations and accepted-design coverage remain variable. No reserved O or author-independent review condition is applicable to this local claim. Add this explicit candidate_facts.L1 premise once in the retained functional input fixture, with case-local design_input/observations overriding only their named variable. Keep initial /tmp inputs/oracles as historical preparation, retain the clarification text and a new input/oracle freeze before any native exposure. No new Product law or inferred success: missing/failing cache observations and missing/stale/ambiguous design coverage must still withhold closure. This supplies the intended positive case's previously implicit identity, rather than grading a lawful missing-premise answer as failure.\n"
    )
    for name, text in [("case-inputs.json", json.dumps(original, indent=2) + "\n"),
                       ("fixture-owner-clarification.txt", clarification)]:
        path = OUT / name
        if path.exists():
            raise RuntimeError(f"Refuse overwrite: {path}")
        path.write_text(text)
    oracle = json.loads((RETAINED / "oracles.json").read_text())
    oracle["predecessor_oracle_sha256"] = digest(RETAINED / "oracles.json")
    oracle["frozen_before_native_exposure"] = datetime.now(timezone.utc).isoformat()
    oracle["fixture_owner_clarification_sha256"] = digest(OUT / "fixture-owner-clarification.txt")
    oracle["input_sha256"] = digest(OUT / "case-inputs.json")
    oracle["clarification_effect"] = "L1 identity carries explicit complete preserving facts; per-case design/observation variants remain binding. The original fourteen outcome conditions are unchanged."
    (OUT / "oracles.json").write_text(json.dumps(oracle, indent=2) + "\n")
    contexts = []
    initial = json.loads((HERE / "fp-run-001/contexts.json").read_text())["contexts"]
    for source_context in initial:
        host, condition = source_context["host"], source_context["condition"]
        source_dir = Path(source_context["directory"])
        source_snapshot = Path(source_context["snapshot"])
        before = json.loads((source_dir / "snapshot-before.json").read_text())
        dest = OUT / source_context["name"]
        snapshot = dest / "snapshot"
        snapshot.mkdir(parents=True, exist_ok=False)
        for relative, expected in before.items():
            if relative == "SNAPSHOT_INPUTS.json" or relative.startswith("specification_methodology/") or "/native-case-inputs/" in relative:
                continue
            path = source_snapshot / relative
            if digest(path) != expected:
                raise RuntimeError(f"Original snapshot drift: {path}")
            target = snapshot / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
        rep = snapshot / "stdo_representation"
        for source, name in [(OUT / "case-inputs.json", "case-inputs.json"),
                             (RETAINED / "cache.py", "cache.py"),
                             (RETAINED / "fixture_probe.py", "fixture_probe.py")]:
            shutil.copy2(source, rep / name)
        binding_path = rep / "invocation-bindings.json"
        bindings = json.loads(binding_path.read_text())
        bindings["bindings"][0]["path"] = str(rep / "dogfood/t009-frame-projection/run-001/source")
        binding_path.write_text(json.dumps(bindings, indent=2) + "\n")
        source_inputs = json.loads((source_snapshot / "SNAPSHOT_INPUTS.json").read_text())
        source_inputs["relocation"]["invocation_bindings_sha256"] = digest(binding_path)
        source_inputs["qualification_selection"] = "Explicit Executive selection of this exact source candidate for the finite T009 functional cases. Only case local grants an actual disposable cache.py edit and fixture probe; every other case is response-only. No release, consumer operation or successor frame acceptance."
        source_inputs["functional_case_input_sha256"] = digest(rep / "case-inputs.json")
        source_inputs["files"] = {str(p.relative_to(snapshot)): digest(p) for p in sorted(snapshot.rglob("*")) if p.is_file()}
        (snapshot / "SNAPSHOT_INPUTS.json").write_text(json.dumps(source_inputs, indent=2) + "\n")
        subprocess.run(["git", "init", "--quiet", str(snapshot)], check=True)
        if condition == "projection":
            for native in (".agents", ".claude"):
                link = rep / native / "skills/stdo-representation"
                link.parent.mkdir(parents=True)
                link.symlink_to("../../skills/stdo-representation")
        frame_context = (
            "Work on the selected finite P0/B0 fixture and explicit per-case variants in case-inputs.json. Shared fixture facts apply in every case unless that case overrides the named input. "
            "L1's shared candidate facts are explicitly supplied in candidate_facts, including the scope of variables. Do not replace a missing or failing variant with another case's positive fact. "
            "The represented source is the unchanged 52-member candidate aggregate 86370472a9b7eabe52933d5bcd8093bb94435392420d38e8d145976317a4d2ca; the caller's operating STDO basis remains v2.5.0-rc.4. "
            "This is authorized bounded candidate-law qualification, not adoption of the represented source or successor frame declarations. Read ../SNAPSHOT_INPUTS.json for exact inputs and physical relocation.")
        if condition == "source":
            reading = (
                "Evaluate directly from exact owning source under dogfood/t009-frame-projection/run-001/source/standards/. "
                "Start from SPEC_METHOD.md#computed-classification-and-treatment and #construction-assessment-and-delegation, "
                "TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity and #condition-based-closure-and-reuse, "
                "REFERENCE_FRAME_METHOD.md#applicability-and-required-results and #result-conjunction, "
                "STDO_REFERENCE_FRAME_BASELINE.md#engagement-applicability and the appropriate source frame, "
                "and DESIGN_MODULE_METHOD.md for accepted design use. Follow other material source sections as needed. "
                "No program, map, projection or candidate skill is supplied in this direct-source condition.")
        else:
            reading = (
                "Use $stdo-representation (Claude: the stdo-representation skill) through this snapshot's native route and start from the exact candidate logical map. "
                "Use skills/stdo-representation/references/frame-index-use.md to resolve the frozen run-002 construction-subject.json, unchanged run-001 program and sources, and exact repaired Axiom dependency. "
                "Inspect frame_refs and source routes; judge the actual applicable frame and bounded index region for the ordinary request. "
                "Use a declared frame-index projection where its declared scope is applicable; available indexes do not themselves select the task's frame. "
                "When invoking project, use ../axiom_indexer/build_tenants/core/code/ac.py with invocation-bindings.json, program in run-001, map in run-002, and stdout output. "
                "Read only the material clauses/residuals and re-enter their exact owning source where needed. "
                "The old physical bindings are retained provenance only. Author proof/design referenced by the manifest is deliberately excluded; no semantic case input is thereby omitted. "
                "This explicit current-candidate handoff replaces ordinary released-map acquisition for this evaluation only; do not fetch tags or install releases.")
        sections = [
            ("Role and outcome", "Apply the selected STDO source to the 32 ordinary cases in case-inputs.json. For case local, act as the already authorized bounded Writer and actually repair the disposable cache fixture and check it. For every other case, provide a response-only evaluation. Complete the requested work in this fresh context."),
            ("Reference frame and exact subject", frame_context),
            ("Hard constraints", "Read only inside this snapshot and write only its stdo_representation/cache.py under case local's explicit grant. You may run python3 fixture_probe.py for that exact disposable fixture. Do not edit fixture_probe.py, case-inputs.json, source, map, skills, tickets, definitions or any other file. Do not perform consumer, update, install, release, deletion or git mutation operations. Do not read the parent repository, network, design, frozen expected outcomes, prior native answers or another actor's result. No task authorizations are supplied by a skill or digest."),
            ("Index context and evidence routes", "Read case-inputs.json in full, plus cache.py and fixture_probe.py for the actual local repair. The input facts and fixture are identical in the two evidence conditions. " + reading),
            ("Open solution space", "Choose the bounded reading order, source re-entry and implementation under the actual grant. All judgments and applicability choices remain yours. Distinguish computed facts, residual semantic judgment and original owner authority, without inventing new conditions or assuming missing premises."),
            ("Return and stop contract", "Return the actual local change and observed finite probe results, then a compact result for every case ID. State the material facts/delta, appropriate owner or frame, supported disposition and next work, and any unresolved condition; cite exact source routes, grouping shared routes if useful. Preserve differences among every named variant. Return the independent decisions yourself rather than writing instructions for another evaluator. This is a finite application exercise, not acceptance of a release or a live consumer path. Stop after the result."),
            ("ACTION", "Handle all 32 cases now: perform only the explicitly granted disposable cache.py repair and probe, and give response-only assessments for the other 31 cases."),
        ]
        if host == "claude":
            prompt = "\n\n".join(f"<{label.lower().replace(' ', '_')}>\n{body}\n</{label.lower().replace(' ', '_')}>" for label, body in sections) + "\n"
        else:
            prompt = "\n\n".join(f"{label}\n{body}" for label, body in sections) + "\n"
        (dest / "prompt.txt").write_text(prompt)
        before = {str(p.relative_to(snapshot)): digest(p) for p in sorted(snapshot.rglob("*"))
                  if p.is_file() and ".git" not in p.relative_to(snapshot).parts and not p.is_symlink()}
        (dest / "snapshot-before.json").write_text(json.dumps(before, indent=2) + "\n")
        contexts.append({"name": source_context["name"], "host": host, "condition": condition,
                         "directory": str(dest), "snapshot": str(snapshot), "cwd": str(rep),
                         "sandbox": "workspace-write", "allow_fixture_edit": True,
                         "prompt_sha256": digest(dest / "prompt.txt"),
                         "snapshot_manifest_sha256": digest(dest / "snapshot-before.json")})
    (OUT / "contexts.json").write_text(json.dumps({"prepared_at": datetime.now(timezone.utc).isoformat(),
          "oracles_sha256": digest(OUT / "oracles.json"), "input_sha256": digest(OUT / "case-inputs.json"),
          "contexts": contexts}, indent=2) + "\n")
    print(json.dumps({"contexts": len(contexts), "oracles_sha256": digest(OUT / "oracles.json"),
                      "input_sha256": digest(OUT / "case-inputs.json")}, indent=2))


if __name__ == "__main__":
    main()
