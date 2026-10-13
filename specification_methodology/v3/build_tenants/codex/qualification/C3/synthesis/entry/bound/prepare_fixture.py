#!/usr/bin/env python3
"""Build and verify a disposable qualification subject, never an installation."""
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ORACLE = HERE.parents[1] / "runs/oracle/ORACLE.json"
RELEASE = "stdo://releases/v2.5.1-rc.2/"
MANIFEST = "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782"
IDENTITY = "urn:stdo:qualification-fixture:entry-d1"


def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value if isinstance(value, str) else json.dumps(value, indent=2) + "\n")


def main():
    if (HERE / "FIXTURE_VALIDATION.json").exists():
        raise RuntimeError("Preserve the already verified fixture")
    root = Path(tempfile.mkdtemp(prefix="stdo-bound-entry-", dir="/private/tmp"))
    c = next(c for c in json.loads(ORACLE.read_text())["cases"] if c["id"] == "D1-ordinary-discovery-probe")
    put(root / "TASK.md", c["task"] + "\n")
    for path, body in c["workspace"].items():
        put(root / "workspace" / path, body)
    definition = {
        "$schema": RELEASE + "standards/schemas/product-definition.schema.json",
        "kind": "stdo.product-definition",
        "product": {"definition_id": IDENTITY,
                    "name": "Disposable D1 method-qualification fixture",
                    "source_project": "./",
                    "bounded_context": {"id": IDENTITY + ":context", "definition": "./TASK.md"}},
        "constitution": {
            "stdo": {"source": {"repository": "https://github.com/foolishimp/specification_methodology.git"},
                     "selector": "stdo://channels/2.5.1", "basis": {"uri": RELEASE, "manifest_sha256": MANIFEST}},
            "additional_authorities": ["./TASK.md", "./EXECUTION_CONTRACT.md"],
            "entrypoints": [{"basis": "#/constitution/stdo/basis", "uri": "standards/authority_compressions/stdo_bootstrap.md"}],
            "agent_bootstrap": {"entrypoint": "#/constitution/entrypoints/0", "targets": ["./AGENTS.md"]}},
        "local_constitution": {"axioms": [], "overrides": [], "disambiguations": []},
        "reference_frame_bases": [{"uri": "./REFERENCE_FRAME_BASIS.md", "authority": ["./EXECUTION_CONTRACT.md"], "applies_to": [IDENTITY]}],
        "what": {"intent": "./TASK.md", "product": "./TASK.md", "specification": ["./TASK.md"]},
        "how": {"common": [], "build_tenants": [{"id": IDENTITY + ":supplied", "root": "./workspace/", "design": ["./DESIGN.md"], "implementation": ["./workspace/"]}]},
        "ticketing": {"goals": "./TASK.md", "tickets": {"root": "./records/tickets/", "lanes": {"backlog": "./records/tickets/backlog/", "active": "./records/tickets/active/", "completed": "./records/tickets/completed/"}}, "comments": {"root": "./records/comments/"}},
        "composition": []}
    put(root / "stdo_fixture.json", definition)
    put(root / "DESIGN.md", "# Supplied fixture design\n\nThe supplied files under `workspace/` realise the task in [TASK.md](TASK.md).\nThe task grant bounds changes to that workspace. This fixture declares no\nadditional interface policy or solution design.\n")
    put(root / "AGENTS.md", "# Qualification Fixture\n\nSelect [stdo_fixture.json](stdo_fixture.json), its exact installed basis and\n[execution contract](EXECUTION_CONTRACT.md). This is a disposable method-use\nsubject. The ordinary entry and task-specific material are selected by the\nactivation; this file does not replace their owners.\n")
    put(root / "REFERENCE_FRAME_BASIS.md", "# Fixture Reference-Frame Basis\n\nThis fixture uses the exact installed [STDO Reference-Frame Baseline](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md),\nwithin the subject and authority of [its execution contract](EXECUTION_CONTRACT.md).\nNo baseline role, required evaluation or independence obligation is removed.\nThe acting model inspects the task and current files, selects the applicable\nordinary work route and returns proposed edits. The host is the separately\nbound executor and fixture evaluator; it observes actual files and records\napplication or rejection. The actor may not assert those later effects.\nTask-specific acquisition follows the selected method's ordinary entry; this\nbasis does not supply a selected task frame or task solution.\n")
    put(root / "EXECUTION_CONTRACT.md", "# Disposable Task Execution Contract\n\n## Grant\n\nThe owning Executive authorises this fixture under EC-CODEX-SYN-01's bounded\nentry-harness repair activation. The subject is the Product identified by\n[stdo_fixture.json](stdo_fixture.json); its complete requested outcome is the\nunchanged [D1 task](TASK.md), and its current implementation is `workspace/`.\nThis is a qualification test subject, not a new published product or a user app.\n\nThe grant permits a fresh actor to inspect the selected method and fixture,\nselect applicable frames, and return exact edit proposals for `workspace/`.\nThe host validates proposals against the fixed independent oracle and applies\nonly proposals within the grant. No task-specific solution is granted by this\ncontract. The existing grant and task are sufficient upstream work authority;\nno new user approval is required to return proposals.\n\n## Effects and return\n\nThe actor has Read, Glob and Grep only. The host alone applies accepted fixture\nproposals and writes durable observations. The actor's actual return and host\napplication or rejection record are the run-scoped work carrier. No ticket or\nsprint relationship is adopted for this disposable task; the schema's ticket\npaths are merely available carrier locations. Candidate availability, correctness\nand acceptance remain separate; this grant does not predetermine any judgment.\n\n## Limits and basis\n\nEach call has 120000 selected prompt/tool-material bytes, 15 minutes and USD 2.\nThe exact installed rc.2 basis remains construction authority. When a frozen\nv3 source candidate is selected, it is the explicitly declared experimental\nmethod under test, not a claimed installed or accepted release. If an actual\nrequired relation remains unresolved, return that limit truthfully.\n")
    for d in ("records/tickets/backlog", "records/tickets/active", "records/tickets/completed", "records/comments"):
        (root / d).mkdir(parents=True)
    command = ["stdo", "status", "--definition", str(root / "stdo_fixture.json"), "--verify"]
    p = subprocess.run(command, capture_output=True, text=True)
    put(HERE / "STATUS_STDOUT.json", p.stdout)
    put(HERE / "STATUS_STDERR.txt", p.stderr)
    if p.returncode:
        raise RuntimeError("Real stdo status failed; preserve its output")
    status = json.loads(p.stdout)
    assert status["valid"] and status["installed"] and status["failures"] == []
    assert status["definition_id"] == IDENTITY and status["manifest_sha256"] == MANIFEST
    files = []
    for p in sorted(root.rglob("*")):
        if p.is_file():
            body = p.read_bytes(); rel = str(p.relative_to(root))
            files.append({"path": rel, "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()})
            dst = HERE / "fixture" / rel; dst.parent.mkdir(parents=True, exist_ok=True); dst.write_bytes(body)
    report = {"fixture_root": str(root), "definition_id": IDENTITY, "command": command,
              "status_valid": status["valid"], "installed_basis": status["basis"],
              "manifest_sha256": status["manifest_sha256"], "files": files,
              "task_identical_to_original_oracle": (root / "TASK.md").read_text() == c["task"] + "\n",
              "original_workspace_identical": all((root / "workspace" / k).read_text() == v for k,v in c["workspace"].items()),
              "paid_calls_permitted_only_after_parent_selects_new_source_cut": True}
    put(HERE / "FIXTURE_VALIDATION.json", report)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
