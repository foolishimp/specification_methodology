"""No-provider source-arm custody probe while the companion bundle is prepared.

The exact RC1 source plus byte-frozen Axiom mechanics is sufficient for this
mechanical probe. It is deliberately not a final native comparison context.
"""
from pathlib import Path
import json
import shutil

from prepare_native import HERE, copy_members, definition, profile, sha, snapshot, write
from run_native import preflight


def main():
    target = HERE / "source-preflight"
    if target.exists():
        raise SystemExit("Refuse overwriting source custody probe")
    root = Path("/Users/jim/src/apps/specification_methodology")
    source = Path("/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.1")
    expected_manifest = "5d306da13994e69aa9f215d4c1cd2d0be96283c1e33a652b58e6e9262d036b64"
    if sha(source / "manifest.json") != expected_manifest:
        raise SystemExit("Source manifest drift")
    preimage = json.loads((HERE.parent / "companion/preimage.json").read_text())
    subject = preimage["axiom_product"]
    members = subject["members"] if isinstance(subject, dict) else subject
    target.mkdir()
    write(target / "withheld.txt", "Source custody probe; not task evidence.\n")
    contexts = []
    for host in ("codex", "claude"):
        name = "source-custody-" + host
        work, runtime, evidence = (target / name / p for p in ("worksite", "runtime", "evidence"))
        work.mkdir(parents=True)
        runtime.mkdir()
        evidence.mkdir()
        shutil.copytree(HERE / "packet", work, dirs_exist_ok=True)
        write(runtime / "zsh/.zshenv", 'export TMPPREFIX="$TMPDIR/zsh"\n')
        store = work / "native/stdo-store"
        shutil.copytree(source, store / "releases/v2.5.1-rc.1")
        axi = work / "native/axiom_indexer"
        copy_members(root / "axiom_indexer", axi, members)
        write(work / "native-context.json", {"source_store": str(store), "axiom_root": str(axi), "presentation": "source", "subject": "no-provider custody probe; not a final native comparison context"})
        write(work / "stdo_task.json", definition("v2.5.1-rc.1", expected_manifest))
        write(evidence / "sandbox.sb", profile(work, runtime))
        write(evidence / "snapshot-before.json", snapshot(work))
        contexts.append({"name": name, "host": host, "worksite": str(work), "runtime": str(runtime), "directory": str(evidence), "outer_profile": str(evidence / "sandbox.sb")})
    selection = target / "selection.json"
    write(selection, {"contexts": contexts, "provider_execution": "forbidden; custody probes only", "source_manifest_sha256": expected_manifest})
    for context in contexts:
        result = preflight(context, selection)
        print(json.dumps({"context": context["name"], "status": result["status"], "provider_calls": 0}), flush=True)


if __name__ == "__main__":
    main()
