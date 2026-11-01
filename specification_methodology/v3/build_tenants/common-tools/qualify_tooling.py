#!/usr/bin/env python3
"""Qualify extracted public tooling against an existing disposable native install."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--qualification", type=Path, required=True)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--python", type=Path, required=True)
    parser.add_argument("--upstream", type=Path, required=True)
    parser.add_argument("--parser-path", type=Path, required=True)
    args = parser.parse_args()
    prior = json.loads(args.qualification.read_bytes())
    installed = Path(prior["installed_root"]).resolve()
    manager = prior["manager"]["executable"]
    store = installed.parents[1]
    run = args.run.resolve()
    if run.exists() or run.is_relative_to(installed):
        raise ValueError("qualification target must be absent and outside install")
    run.mkdir(parents=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONPATH=str(args.parser_path.resolve()))
    results = []

    def command(label, argv, expected=0, parse=True):
        value = subprocess.run([str(x) for x in argv], cwd=run, env=env, capture_output=True, text=True, timeout=180)
        if value.returncode != expected:
            raise ValueError(label + ": " + value.stdout[-3000:] + value.stderr[-3000:])
        payload = json.loads(value.stdout if expected == 0 else value.stderr) if parse else value.stdout
        results.append({"operation": label, "argv": [str(x) for x in argv], "returncode": value.returncode,
                        "stdout_sha256": hashlib.sha256(value.stdout.encode()).hexdigest(),
                        "stderr_sha256": hashlib.sha256(value.stderr.encode()).hexdigest(),
                        "status": payload.get("status") if isinstance(payload, dict) else "completed"})
        return payload

    def cli(script, *arguments, expected=0):
        flags = ["-I", "-B"] if script.name == "materialize.py" else ["-B"]
        return command(script.name + ":" + str(arguments[0]), [args.python, *flags, script, *arguments], expected)

    materializer = installed / "standards/tooling/materialize.py"
    extracted = run / "tool-workspace"
    before = {p.relative_to(installed).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in installed.rglob("*") if p.is_file()}
    command("resolve-tool", [manager, "--store", store, "resolve", "stdo://releases/v3.0.3/standards/tooling/materialize.py"])
    command("resolve-code", [manager, "--store", store, "resolve", "stdo://releases/v3.0.3/standards/documentation/code-explorer/index.html"])
    command("resolve-proofs", [manager, "--store", store, "resolve", "stdo://releases/v3.0.3/standards/documentation/proofs/index.html"])
    cli(materializer, "check")
    case_alias = installed.with_name(installed.name.upper())
    if case_alias.exists() and os.path.samefile(case_alias, installed):
        cli(materializer, "materialize", "--destination", case_alias / "must-not-materialize", expected=2)
        command("case-alias-bundle-refusal", [args.python, "-I", "-B", materializer,
                "--bundle", installed / "STANDARDS/tooling", "materialize", "--destination", installed / "must-not-materialize"], expected=2)
        if (installed / "must-not-materialize").exists():
            raise ValueError("case alias wrote beneath installed release")
    cli(materializer, "materialize", "--destination", extracted)
    cli(materializer, "verify-tree", "--destination", extracted)
    refused = cli(materializer, "materialize", "--destination", extracted, expected=2)
    if refused["status"] != "refused":
        raise ValueError("existing destination did not refuse")

    tenant = extracted / "a_c/build_tenants/graphify"
    # Reuse declared synthetic fixture content, imported from the extracted
    # package only. It is source-contract test data, never LLM-quality evidence.
    sys.dont_write_bytecode = True
    sys.path[:0] = [str(tenant / "test_env"), str(tenant / "code")]
    from test_ac_generate import SOURCE, fixture_answer
    from test_ac_code import TYPESCRIPT, TEST
    import ac_explore

    project = run / "synthetic-project"
    (project / "specification").mkdir(parents=True)
    (project / "src").mkdir(); (project / "tests").mkdir()
    source = project / "specification/RULES.md"; source.write_text(SOURCE)
    (project / "src/evidence.ts").write_text(TYPESCRIPT)
    (project / "tests/evidence.test.mjs").write_text(TEST)
    definition = {"$schema": "stdo://releases/v3.0.3/standards/schemas/product-definition.schema.json",
        "kind": "stdo.product-definition", "product": {"definition_id": "urn:stdo303:qualification:project",
            "name": "Synthetic installed-tool qualification", "source_project": "./", "bounded_context": None},
        "constitution": {"stdo": {"source": {"repository": "https://github.com/foolishimp/specification_methodology.git"},
            "selector": "stdo://channels/3.0.3", "basis": {"uri": "stdo://releases/v3.0.3/", "manifest_sha256": prior["manifest_sha256"]}},
            "additional_authorities": [], "entrypoints": [{"basis": "#/constitution/stdo/basis", "uri": "standards/frames/bootstrap.md"}],
            "agent_bootstrap": {"entrypoint": "#/constitution/entrypoints/0", "targets": ["./AGENTS.md"]}},
        "local_constitution": {"axioms": [], "overrides": [], "disambiguations": []},
        "reference_frame_bases": [{"uri": "./specification/RULES.md", "authority": ["./specification/RULES.md"],
                                   "applies_to": ["urn:stdo303:qualification:project"]}],
        "what": {"intent": "./specification/RULES.md", "product": "./specification/RULES.md", "specification": ["./specification/RULES.md"]},
        "how": {"common": [], "build_tenants": [{"id": "urn:stdo303:qualification:tenant", "root": "./src/",
            "design": ["./specification/RULES.md"], "implementation": ["./src/"]}]},
        "ticketing": {"goals": "./specification/RULES.md", "tickets": {"root": "./work/tickets/", "lanes": {"backlog": "./work/tickets/backlog/", "active": "./work/tickets/active/", "completed": "./work/tickets/completed/"}},
                      "comments": {"root": "./work/comments/"}, "sprints": {"root": "./work/sprints/"}}, "composition": []}
    definition_path = project / "stdo_sample.json"
    definition_path.write_text(json.dumps(definition, indent=2) + "\n")
    wrapper = run / "selected-stdo"
    wrapper.write_text("#!" + str(args.python.resolve()) + "\nimport os,sys\nos.execv(" + repr(manager) + ", [" + repr(manager) + ", '--store', " + repr(str(store)) + ", *sys.argv[1:]])\n")
    wrapper.chmod(0o755)
    command("real-manager-project-basis", [wrapper, "status", "--definition", definition_path, "--verify"])
    representation = run / "representation"
    project_cli = tenant / "code/ac_project.py"
    cli(project_cli, "prepare", "--project", project, "--definition", definition_path, "--out", representation, "--stdo", wrapper)
    task = cli(project_cli, "task", "--run", representation)
    chunks = json.loads((representation / "generation/chunks.json").read_bytes())
    if len(chunks) != 1 or task["status"] != "authoring_required":
        raise ValueError("unexpected fixture task")
    answer = run / "synthetic-answer.json"; answer.write_text(json.dumps(fixture_answer(chunks[0]), indent=2) + "\n")
    cli(project_cli, "submit", "--run", representation, "--chunk", chunks[0]["id"], "--answer", answer, "--author", "synthetic packaging fixture; no LLM-quality claim")
    built = cli(project_cli, "build", "--run", representation)
    cli(project_cli, "status", "--run", representation)
    if cli(project_cli, "build", "--run", representation)["status"] != "reused":
        raise ValueError("representation reuse failed")
    code_cli = tenant / "code/ac_code.py"; code_run = run / "code-overlay"
    cli(code_cli, "prepare", "--project", project, "--model", built["artifacts"]["model"],
        "--manifest", representation / "source-manifest.json", "--source-root", representation / "generation/corpus",
        "--code", "src/evidence.ts", "--test", "tests/evidence.test.mjs", "--upstream", args.upstream.resolve(), "--out", code_run)
    code_task = cli(code_cli, "task", "--run", code_run)
    mapping = code_task["template"]
    requirement = next(record for record in code_task["base_records"] if record["family"] == "constraints")
    implementation = next(node for node in code_task["code_entities"] if node["family"] == "code" and node["label"] == "requireEvidence()")
    test = next(node for node in code_task["code_entities"] if node["family"] == "test" and node["label"] == "testEvidence()")
    ground = next(ac_explore.groundings(requirement["record"]))
    ground = {k: ground[k] for k in ("path", "start_line", "end_line", "quote")}
    mapping["links"] = []
    for identity, kind, left, right, grounds in (("implementation", "proposed_realization", requirement, implementation, [ground, *implementation["record"]["grounding"]]),
            ("test", "test_source_for", implementation, test, [*implementation["record"]["grounding"], *test["record"]["grounding"]])):
        mapping["links"].append({"id": identity, "kind": kind, "source": left["id"], "target": right["id"],
            "rationale": "Synthetic packaging fixture mapping for the availability guard and its caller.",
            "conditions": [], "limitations": ["No semantic acceptance or test execution."], "grounding": grounds})
    mapping["unresolved"] = [{"subject": requirement["id"], "reason": "External policy remains unresolved."}]
    mapping_path = run / "mapping.json"; mapping_path.write_text(json.dumps(mapping, indent=2) + "\n")
    code_built = cli(code_cli, "build", "--run", code_run, "--mapping", mapping_path, "--author", "synthetic packaging fixture")
    cli(code_cli, "status", "--run", code_run)
    if cli(code_cli, "build", "--run", code_run, "--mapping", mapping_path, "--author", "synthetic packaging fixture")["status"] != "reused":
        raise ValueError("code overlay reuse failed")
    source.write_text(SOURCE + "Changed input.\n")
    cli(project_cli, "status", "--run", representation, expected=2)
    cli(code_cli, "status", "--run", code_run, expected=2)
    source.write_text(SOURCE)
    page = code_run / "built/explorer.html"; original = page.read_bytes(); page.write_bytes(original + b"tamper")
    cli(code_cli, "status", "--run", code_run, expected=2)
    page.write_bytes(original)
    cli(code_cli, "status", "--run", code_run)
    codex = extracted / "stdo_skills/build_tenants/codex"
    command("codex-package", [args.python, "-B", codex / "tests/verify_package.py", codex, "--repository", extracted])
    command("claude-package", [args.python, "-B", extracted / "stdo_skills/build_tenants/claude/tests/check_package.py"])
    command("formal-help", [args.python, "-I", "-S", "-B", extracted / "a_c/build_tenants/lean/scripts/formal_gate.py", "--help"], parse=False)
    cli(materializer, "verify-tree", "--destination", extracted)
    final = command("final-manager-verification", [manager, "--store", store, "verify", "v3.0.3", "--manifest-sha256", prior["manifest_sha256"]])
    after = {p.relative_to(installed).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
             for p in installed.rglob("*") if p.is_file()}
    if before != after or final["valid"] is not True:
        raise ValueError("installed release changed during materialization/tool use")
    report = {"kind": "stdo303.installed-tooling-qualification/1", "synthetic_local_tag": True,
              "public_release": False, "original_repository_runtime_dependency": False,
              "installation_unchanged": True, "source_tree_pristine_after_use": True,
              "manifest_sha256": prior["manifest_sha256"], "python": str(args.python),
              "upstream": str(args.upstream), "parser_environment": str(args.parser_path),
              "representation": built, "code_overlay": code_built, "operations": results,
              "limits": ["Synthetic authoring data; no LLM quality or ABI execution claim.",
                         "Existing local pinned Graphify/parser environment, not a delivered installation.",
                         "No fresh Lean proof, Skills host, browser/WebGL or publication qualification."]}
    (run / "qualification.json").write_text(json.dumps(report, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "qualified", "operations": len(results), "installation_unchanged": True,
                      "report": str(run / "qualification.json")}, indent=2))


if __name__ == "__main__":
    main()
