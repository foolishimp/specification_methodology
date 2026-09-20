"""Prepare fresh exact-basis contexts. No provider execution or semantic grading."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value if isinstance(value, str) else json.dumps(value, indent=2) + "\n")


def snapshot(root):
    return {str(p.relative_to(root)): {"type": "symlink", "target": os.readlink(p)}
            if p.is_symlink() else {"type": "file", "sha256": sha(p)}
            for p in sorted(Path(root).rglob("*")) if p.is_file() or p.is_symlink()}


def safe_relative(value):
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("Non-local inventory member: " + value)
    return path


def copy_members(source, destination, members):
    for row in members:
        relative = safe_relative(row["path"])
        src, dst = source / relative, destination / relative
        observed = hashlib.sha256(os.readlink(src).encode()).hexdigest() if src.is_symlink() else sha(src)
        if observed != row["sha256"]:
            raise ValueError("Member drift: " + str(src))
        dst.parent.mkdir(parents=True, exist_ok=True)
        if row.get("type") == "symlink":
            if os.readlink(src) != row["target"]:
                raise ValueError("Symlink drift: " + str(src))
            dst.symlink_to(row["target"])
        else:
            shutil.copy2(src, dst)


def profile(work, runtime, transport_files=()):
    q = lambda value: json.dumps(str(value))
    # Keep the actual HOME/CODEX_HOME unchanged. Only the existing auth file is
    # readable through that state root; no credentials are copied into evidence.
    actual_codex_root = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    auth = actual_codex_root / "auth.json"
    hidden = {Path("/Users/jim/src"), Path("/Users/jim/.codex"), Path("/Users/jim/.codex-alt"), Path("/Users/jim/.claude"), Path("/Users/jim/.agents"), actual_codex_root}
    lines = ["(version 1)", "(allow default)"]
    transport_exceptions = "".join(" (require-not (literal " + q(row["path"]) + "))" for row in transport_files)
    for root in sorted(hidden):
        lines.append("(deny file-read-data (require-all (subpath " + q(root) + ") (require-not (subpath " + q(work) + ")) (require-not (subpath " + q(runtime) + ")) (require-not (literal " + q(auth) + "))" + transport_exceptions + "))")
    lines.append("(deny file-write* (require-all (require-not (subpath " + q(runtime) + ")) (require-not (subpath \"/dev\"))))")
    for row in transport_files:
        lines.append("(allow file-write-data (literal " + q(row["path"]) + "))")
    return "\n".join(lines) + "\n"


def definition(cut, manifest_sha):
    return {"$schema": f"stdo://releases/{cut}/standards/schemas/product-definition.schema.json", "kind": "stdo.product-definition",
        "product": {"definition_id": "urn:stdo-251-qualification:delivery", "name": "Delivery work packet", "source_project": "./", "bounded_context": None},
        "constitution": {"stdo": {"source": {"repository": "https://github.com/foolishimp/specification_methodology.git"}, "selector": "stdo://channels/2.5.1", "basis": {"uri": f"stdo://releases/{cut}/", "manifest_sha256": manifest_sha}},
            "additional_authorities": ["./project.md", "./task.md"], "entrypoints": [{"basis": "#/constitution/stdo/basis", "uri": "standards/authority_compressions/stdo_bootstrap.md"}], "agent_bootstrap": {"entrypoint": "#/constitution/entrypoints/0", "targets": ["./AGENTS.md", "./CLAUDE.md"]}},
        "local_constitution": {"axioms": [], "overrides": [], "disambiguations": []},
        "reference_frame_bases": [{"uri": "./qualification-basis.md", "authority": ["./task.md"], "applies_to": ["urn:stdo-251-qualification:delivery"]}],
        "what": {"intent": "./project.md", "product": "./project.md", "specification": ["./project.md"]},
        "how": {"common": [], "build_tenants": [{"id": "urn:stdo-251-qualification:fixture", "root": "./", "design": ["./project.md"], "implementation": ["./fixture.py"]}]},
        "ticketing": {"goals": "./task.md", "tickets": {"root": "./records/", "lanes": {"backlog": "./records/", "active": "./records/", "completed": "./records/"}}, "comments": {"root": "./records/"}}, "composition": []}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--binding", type=Path, required=True)
    parser.add_argument("--attempt", default="attempt-01")
    parser.add_argument("--hosts", nargs="+", choices=("codex", "claude"), default=["codex", "claude"])
    parser.add_argument("--arms", nargs="+", choices=("source", "map-first"), default=["source", "map-first"])
    args = parser.parse_args()
    safe_relative(args.attempt)
    target = HERE / args.attempt
    if target.exists():
        raise SystemExit("Refuse existing native attempt: " + str(target))
    binding = json.loads(args.binding.read_text())
    cut = binding["cut"]
    if cut != "v2.5.1-rc.1":
        raise SystemExit("Unexpected qualification cut")
    source = Path(binding["source_release_root"])
    if sha(source / "manifest.json") != binding["source_manifest_sha256"]:
        raise SystemExit("Source manifest drift")
    source_manifest = json.loads((source / "manifest.json").read_text())
    if source_manifest["release"]["cut"] != cut:
        raise SystemExit("Source cut mismatch")
    for row in source_manifest["standards"]["members"]:
        if sha(source / "standards" / safe_relative(row["path"])) != row["sha256"]:
            raise SystemExit("Source member drift: " + row["path"])
    cohort_path = Path(binding["cohort_manifest"])
    if sha(cohort_path) != binding["cohort_sha256"]:
        raise SystemExit("Cohort drift")
    cohort = json.loads(cohort_path.read_text())
    if cohort["cohort"]["cut"] != cut:
        raise SystemExit("Cohort cut mismatch")
    oracle_binding = json.loads((HERE / "oracle-binding.json").read_text())
    if oracle_binding["status"] != "bound" or oracle_binding["oracle_sha256"] != sha(HERE / "oracle.md"):
        raise SystemExit("Independent oracle is not bound to the source")
    for row in oracle_binding["source_members"]:
        if sha(source / row["path"]) != row["sha256"]:
            raise SystemExit("Oracle source member drift")
    mechanics = subprocess.run([sys.executable, "-B", str(HERE / "check_fixture.py")], capture_output=True, text=True)
    if mechanics.returncode:
        raise SystemExit("Fixture checks failed: " + mechanics.stderr)
    import jsonschema
    schema = json.loads((source / "standards/schemas/product-definition.schema.json").read_text())
    selected_definition = definition(cut, binding["source_manifest_sha256"])
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(selected_definition)
    target.mkdir()
    write(target / "fixture-checks.json", json.loads(mechanics.stdout))
    write(target / "binding.json", binding)
    write(target / "withheld.txt", "Custody probe, not task evidence.\n")
    contexts = []
    for host in args.hosts:
        for arm in args.arms:
            name = f"delivery-{host}-{arm}"
            context_root = target / name
            work, runtime, evidence = (context_root / p for p in ("worksite", "runtime", "evidence"))
            work.mkdir(parents=True)
            runtime.mkdir()
            evidence.mkdir()
            write(runtime / "zsh/.zshenv", 'export TMPPREFIX="$TMPDIR/zsh"\n')
            shutil.copytree(HERE / "packet", work, dirs_exist_ok=True)
            store = work / "native/stdo-store"
            shutil.copytree(source, store / "releases" / cut)
            product_names = ["axiom_indexer"] + (["stdo_representation"] if arm == "map-first" else [])
            for product in product_names:
                details = binding["products"][product]
                product_root = Path(details["root"])
                dest = work / "native" / product
                copy_members(product_root, dest, cohort["products"][product]["subject"]["members"])
                copy_members(product_root, dest, details["support_members"])
            write(work / "native/cohort.json", cohort)
            write(work / "native/bindings.json", {"kind": "axiom-indexer.binding-set", "schema_version": 1, "bindings": [{"uri_prefix": f"stdo://releases/{cut}/", "path": str(store / "releases" / cut)}]})
            write(work / "stdo_task.json", selected_definition)
            write(work / "records/candidate-identities.json", {"C1": {"path": "records/C1.md", "sha256": sha(work / "records/C1.md")}, "C2": {"path": "records/C2.md", "sha256": sha(work / "records/C2.md")}})
            write(work / "qualification-basis.md", f"# Qualification frame basis\n\nExact {cut}, manifest {binding['source_manifest_sha256']}. The task and project\nrecord supply the fixture Product facts and read-only grant. Select material\nframes from the exact supplied baseline and return the bounded evaluation to\nthe qualification coordinator. No mutation, actual actor activation, acceptance,\npublication or consumer adoption is granted. This binds a frozen qualification\nsubject, not a claim that the cohort candidate is already published.\n")
            axi, rep = work / "native/axiom_indexer", work / "native/stdo_representation"
            context = {"subject": "exact frozen RC1 qualification candidate", "source_revision": binding["source_revision"], "source_manifest_sha256": binding["source_manifest_sha256"], "cohort_sha256": binding["cohort_sha256"], "presentation": arm, "caller_definition": "stdo_task.json", "caller_frame_basis": "qualification-basis.md", "source_store": str(store), "source_basis": selected_definition["constitution"]["stdo"]["basis"], "axiom_root": str(axi), "representation_root": str(rep) if arm == "map-first" else None, "bindings": "native/bindings.json", "cohort_manifest": "native/cohort.json", "evidence": ["project.md", "fixture.py"]}
            write(work / "native-context.json", context)
            for hostdir in (".agents", ".claude"):
                for product in product_names:
                    skill = "axiomatize-corpus" if product == "axiom_indexer" else "stdo-representation"
                    link = work / hostdir / "skills" / skill
                    link.parent.mkdir(parents=True, exist_ok=True)
                    link.symlink_to(f"../../native/{product}/skills/{skill}")
            route = "Discover stdo-representation and begin from its selected map; explicitly select material frames and re-enter exact source where needed." if arm == "map-first" else "Use exact Source STDO from the bound source store. This source-control arm supplies no Representation map."
            instruction = "Fresh qualification worksite. Read task.md and native-context.json, then the selected Product Definition and frame basis. " + route + "\nUse the discovered Axiom skill for the exact pure joiner. Read-only inspection and stdout computation are allowed; no file effects or other actors. Return actual source/tool observations and the bounded result.\n"
            write(work / "AGENTS.md", instruction)
            write(work / "CLAUDE.md", instruction)
            write(evidence / "prompt.txt", "Complete task.md under the supplied native context and exact read-only grant. Return the bounded task result and actual handoff evidence. Use targeted source inspection; keep the result near 1,200 words.\n")
            transport_files = binding.get("nonsemantic_transport", []) if host == "codex" else []
            write(evidence / "sandbox.sb", profile(work, runtime, transport_files))
            write(evidence / "snapshot-before.json", snapshot(work))
            contexts.append({"name": name, "host": host, "arm": arm, "worksite": str(work), "runtime": str(runtime), "directory": str(evidence), "outer_profile": str(evidence / "sandbox.sb"), "models": binding["models"], "allowed_writes": [], "nonsemantic_transport": transport_files, "status": "ready_for_mechanical_preflight"})
    write(target / "coverage-selection.json", {"binding_sha256": sha(args.binding), "cohort_sha256": binding["cohort_sha256"], "source_manifest_sha256": binding["source_manifest_sha256"], "oracle_sha256": sha(HERE / "oracle.md"), "oracle_binding_sha256": sha(HERE / "oracle-binding.json"), "packet": snapshot(HERE / "packet"), "prepare_sha256": sha(Path(__file__)), "comparison": binding.get("comparison"), "contexts": contexts, "native_execution": "not started; parent acceptance and trigger required"})
    print(json.dumps({"prepared": str(target), "contexts": len(contexts), "provider_calls": 0}))


if __name__ == "__main__":
    main()
