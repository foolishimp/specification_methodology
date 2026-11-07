#!/usr/bin/env python3
"""Install a current host binding using a separate, verified runtime anchor."""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys


def materializer(bundle):
    path = bundle / 'materialize.py'
    spec = importlib.util.spec_from_file_location("stdo_materializer", path)
    module = importlib.util.module_from_spec(spec)
    exec(compile(path.read_bytes(), str(path), 'exec'), module.__dict__)
    return module


def runtime_tools(bundle):
    path = bundle / 'runtime.py'
    spec = importlib.util.spec_from_file_location("stdo_runtime_derivation", path)
    module = importlib.util.module_from_spec(spec)
    exec(compile(path.read_bytes(), str(path), 'exec'), module.__dict__)
    return module


def anchor_definition(version, manifest_sha, repository):
    identity = "urn:stdo:runtime-installation-anchor:" + manifest_sha
    basis = {"uri": f"stdo://releases/v{version}/", "manifest_sha256": manifest_sha}
    version_line = version.split("-rc.", 1)[0]
    return {"$schema": basis["uri"] + "standards/schemas/product-definition.schema.json",
        "kind": "stdo.product-definition",
        "product": {"definition_id": identity, "name": "STDO runtime installation anchor " + version,
                    "source_project": "./", "bounded_context": {"id": identity + ":scope", "definition": "./README.md#scope"}},
        "constitution": {"stdo": {"source": {"repository": repository}, "selector": "stdo://channels/" + version_line, "basis": basis},
                         "additional_authorities": ["./README.md"],
                         "entrypoints": [{"basis": "#/constitution/stdo/basis", "uri": "standards/frames/bootstrap.md"}],
                         "agent_bootstrap": {"entrypoint": "#/constitution/entrypoints/0", "targets": ["./AGENTS.md"]}},
        "local_constitution": {"axioms": [], "overrides": [], "disambiguations": []},
        "reference_frame_bases": [{"uri": "./README.md#frame", "authority": ["./README.md#scope"], "applies_to": [identity]}],
        "what": {"intent": "./README.md#intent", "product": "./README.md#scope", "specification": ["./README.md#requirements"]},
        "how": {"common": ["./README.md#implementation"], "build_tenants": [
            {"id": identity + ":installation", "root": "./", "design": ["./README.md#implementation"], "implementation": ["./INSTALLATION.json"]}]},
        "ticketing": {"goals": "./README.md#intent", "tickets": {"root": "./work/tickets/", "lanes": {
            "backlog": "./work/tickets/backlog/", "active": "./work/tickets/active/", "completed": "./work/tickets/completed/"}},
            "comments": {"root": "./work/comments/"}}, "composition": []}


ANCHOR_GUIDE = """# Runtime installation anchor

## Intent
Expose the selected installed native workflow and its host provider.

## Scope
This definition identifies only this runtime installation. It is not a
construction Product adoption or authority for a nominated project's work.
Every operation resolves the nominated Product's own exact basis and grant.

## Requirements
Retain the verified native manifest, exact tool source inventory, manager
result and setup receipt. Refuse changed, stale or incomplete installations.

## Frame
The enclosing owner-selected installation instruction permits setup and
verification only. Product work, semantic acceptance and release decisions
retain their own authority. A host skill supplies no new authority.

## Implementation
INSTALLATION.json records this runtime's exact installed inputs. The host
installer owns its separate file inventory and runtime configuration.
"""


def launcher_source(contract):
    """A generated binding, not a second manager implementation."""
    return ('''#!/usr/bin/env python3
import hashlib,json,os,pathlib,subprocess,sys
C = ''' + repr(contract) + '''
def regular(name):
    p=pathlib.Path(name)
    if not p.is_absolute() or any(q.is_symlink() for q in (p,*p.parents)) or not p.is_file():
        raise ValueError("Selected runtime launcher input redirected or missing")
    return p.read_bytes()
try:
    if any(x=="--store" or x.startswith("--store=") for x in sys.argv[1:]):
        raise ValueError("Runtime launcher store is fixed; another store requires a new explicit anchor")
    if hashlib.sha256(regular(C['manager'])).hexdigest()!=C['manager_sha256']:
        raise ValueError("Selected underlying manager executable changed")
    if hashlib.sha256(regular(C['manifest'])).hexdigest()!=C['manifest_sha256']:
        raise ValueError("Selected store/native manifest changed")
    if pathlib.Path(C['store']).resolve(strict=True)!=pathlib.Path(C['store']):
        raise ValueError("Selected store path changed")
    result=subprocess.run([C['manager'],'--store',C['store'],*sys.argv[1:]],capture_output=True)
    sys.stderr.buffer.write(result.stderr)
    try:
        value=json.loads(result.stdout)
    except (ValueError,UnicodeDecodeError):
        sys.stdout.buffer.write(result.stdout)
    else:
        if isinstance(value,dict):
            value['runtime_launcher']={'path':str(pathlib.Path(__file__).absolute()),
                'sha256':hashlib.sha256(regular(__file__)).hexdigest(),**C}
        print(json.dumps(value,indent=2))
    raise SystemExit(result.returncode)
except (OSError,ValueError) as error:
    print(json.dumps({'status':'refused','reason':str(error)}));raise SystemExit(2)
''').encode()


def run(args):
    bundle = Path(__file__).absolute().parent
    tool = materializer(bundle)
    meta, sources = tool.source_bytes(tool.read_bundle(bundle))
    tool.require(meta["kind"] == "stdo.installed-tooling/2", "current installed tooling required")
    if args.command == "derive-runtime":
        return runtime_tools(bundle).derive(tool, bundle, args.tools, args.destination, args.receipt)
    if args.command == "bootstrap-lean":
        return runtime_tools(bundle).bootstrap(tool, args.derivation, args.derivation_sha256, args.python, args.output)
    tools_root = tool.ordinary_path(args.tools); anchor = tool.ordinary_path(args.anchor)
    method = tool.ordinary_path(args.method_root); store = tool.ordinary_path(args.store)
    workspace = tool.ordinary_path(args.workspace)
    tool.require(workspace.is_dir() and not anchor.exists(), "existing host workspace and absent anchor required")
    protected = (method, tools_root, bundle)
    for root in protected:
        for output in (anchor, workspace):
            tool.require(not output.is_relative_to(root) and not root.is_relative_to(output), "setup output overlaps protected inputs")
            tool.require(not any(p.exists() and os.path.samefile(p, root) for p in (output, *output.parents)), "setup output aliases protected inputs")
            tool.require(not any(p.exists() and output.exists() and os.path.samefile(p, output) for p in (root, *root.parents)), "protected input aliases setup output")
    version = meta["distribution_version"]; cut = "v" + version
    tool.require(method == store / "releases" / cut, "method root does not belong to selected store")
    for row in meta["sources"]:
        raw = tool.ordinary_path(tools_root / row["archive_path"]).read_bytes()
        tool.require(tool.sha(raw) == row["sha256"] and len(raw) == row["bytes"], "materialized source differs: " + row["archive_path"])
    ac_root = tools_root / "a_c"; derivation = None
    tool.require(bool(args.runtime_ac) == bool(args.derivation) == bool(args.derivation_sha256), "runtime, derivation and digest must be selected together")
    if args.runtime_ac:
        runtime = runtime_tools(bundle)
        derivation = runtime.load(tool, args.derivation, args.derivation_sha256)
        runtime.validate(tool, derivation, require_support=True)
        ac_root = tool.ordinary_path(args.runtime_ac)
        tool.require(derivation["runtime_root"] == str(ac_root) and derivation["source_root"] == str(tools_root / "a_c") and
                     derivation["tooling_manifest_sha256"] == tool.sha((bundle / "TOOLING.json").read_bytes()), "runtime derivation belongs to another source selection")
        runtime.separate(tool, anchor, ac_root); runtime.separate(tool, workspace, ac_root)
    manifest_raw = tool.ordinary_path(method / "manifest.json").read_bytes(); manifest_sha = tool.sha(manifest_raw)
    tool.require(manifest_sha == args.manifest_sha256, "native manifest differs from explicit selection")
    env = dict(os.environ, STDO_STORE=str(store))
    command = [str(Path(args.stdo).absolute()), "--store", str(store), "verify", cut, "--manifest-sha256", manifest_sha]
    verified = subprocess.run(command, env=env, capture_output=True, text=True, timeout=60)
    value = json.loads(verified.stdout)
    tool.require(verified.returncode == 0 and value.get("valid") is True and value.get("failures") == [] and
                 value.get("path") == str(method) and value.get("manifest_sha256") == manifest_sha,
                 "manager did not verify the selected native installation")
    selected = json.loads((bundle / "SELECTION.json").read_bytes())
    for row in selected["source_freeze"]["members"] + selected["source_freeze"]["native_contracts"]:
        tool.require(tool.sha(tool.ordinary_path(method / row["path"]).read_bytes()) == row["sha256"], "native source differs from tool cohort")
    definition = anchor_definition(version, manifest_sha, args.repository)
    anchor.mkdir(parents=True, exist_ok=False)
    for relative in ("work/tickets/backlog", "work/tickets/active", "work/tickets/completed", "work/comments"):
        (anchor / relative).mkdir(parents=True, exist_ok=True)
    (anchor / "README.md").write_text(ANCHOR_GUIDE)
    (anchor / "AGENTS.md").write_text("Read README.md. This scope is a runtime installation anchor only.\n")
    (anchor / "stdo_runtime.json").write_bytes(tool.encoded(definition))
    manager = tool.ordinary_path(args.stdo)
    launcher_contract = {"manager": str(manager), "manager_sha256": tool.sha(manager.read_bytes()),
                         "store": str(store), "manifest": str(method / "manifest.json"), "manifest_sha256": manifest_sha}
    launcher = anchor / "stdo"
    launcher_raw = launcher_source(launcher_contract)
    launcher.write_bytes(launcher_raw); launcher.chmod(0o755)
    installation = {"kind": "stdo.runtime-installation-anchor/1", "version": version,
                    "basis": definition["constitution"]["stdo"]["basis"], "source_identity_sha256": meta["source_identity_sha256"],
                    "method_root": str(method), "tools_root": str(tools_root), "manager_argv": command, "manager_result": value,
                    "ac_root": str(ac_root), "runtime_derivation": ({"path": str(args.derivation), "sha256": args.derivation_sha256,
                        "profile_sha256": derivation["profile_sha256"]} if derivation is not None else None),
                    "launcher": {"path": str(launcher), "sha256": tool.sha(launcher_raw), **launcher_contract},
                    "tooling_manifest_sha256": tool.sha((bundle / "TOOLING.json").read_bytes())}
    (anchor / "INSTALLATION.json").write_bytes(tool.encoded(installation))
    command = [str(Path(args.python).absolute()), "-B", str(tools_root / "stdo_skills/scripts/manage_skills.py"), "install",
        "--package", str(tools_root / "stdo_skills"), "--workspace", str(workspace), "--definition", str(anchor / "stdo_runtime.json"),
        "--method-root", str(method), "--ac-root", str(ac_root), "--host", args.host,
        "--stdo", str(launcher), "--python", str(Path(args.python).absolute())]
    installed = subprocess.run(command, env=env, capture_output=True, text=True, timeout=180)
    receipt = {"argv": command, "returncode": installed.returncode, "stdout": installed.stdout, "stderr": installed.stderr}
    (anchor / "host-execution.json").write_bytes(tool.encoded(receipt))
    tool.require(installed.returncode == 0, "host install failed; retain anchor and host-execution.json before recovery")
    return {"status": "installed", "host": args.host, "anchor": str(anchor), "method_root": str(method),
            "basis": installation["basis"], "result": json.loads(installed.stdout)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    host = sub.add_parser("host")
    for key in ("tools", "anchor", "method-root", "workspace", "store", "stdo", "python"):
        host.add_argument("--" + key, type=Path, required=True)
    host.add_argument("--host", choices=("codex", "claude"), required=True)
    host.add_argument("--manifest-sha256", required=True)
    host.add_argument("--repository", default="https://github.com/foolishimp/specification_methodology.git")
    host.add_argument("--runtime-ac", type=Path)
    host.add_argument("--derivation", type=Path)
    host.add_argument("--derivation-sha256")
    derive = sub.add_parser("derive-runtime")
    for name in ("tools", "destination", "receipt"):
        derive.add_argument("--" + name, type=Path, required=True)
    bootstrap = sub.add_parser("bootstrap-lean")
    for name in ("derivation", "python", "output"):
        bootstrap.add_argument("--" + name, type=Path, required=True)
    bootstrap.add_argument("--derivation-sha256", required=True)
    try:
        print(json.dumps(run(parser.parse_args()), indent=2)); return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as error:
        print(json.dumps({"status": "refused_or_incomplete", "reason": str(error), "recovery": "Retain partial setup and receipts; reconcile before retry."})); return 2


if __name__ == "__main__":
    raise SystemExit(main())
