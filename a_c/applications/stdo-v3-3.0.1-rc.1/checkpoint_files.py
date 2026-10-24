#!/usr/bin/env python3
"""Print a bounded public file inventory; never stage files or inspect private actors."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / "release_tools"))
import application_contract as c

TOP_FILES = {".gitignore", "application.json", "README.md", "freeze_sources.py", "run_generation.py", "construction_account.py",
             "checkpoint_files.py", "package_release.py", "source-contract.json", "source-selection.json", "source-manifest.json",
             "source-classification.json", "package-custody.json", "SOURCE-READINESS.md", "PUBLIC-FILES.json"}
PUBLIC_TREES = {"implementation", "release_tools", "source"}
PRIVATE_TREES = {"run", "private", "bundle", "dist", ".venv", "__pycache__"}


def inventory(root=ROOT):
    rows = []
    for item in sorted(root.iterdir()):
        c.require(not item.is_symlink(), "redirected application member")
        if item.name in PRIVATE_TREES:
            continue
        if item.is_file():
            c.require(item.name in TOP_FILES, "unclassified top-level file: " + item.name)
            names = [] if item.name == "PUBLIC-FILES.json" else [item.name]
        elif item.name in PUBLIC_TREES:
            names = [item.name + "/" + name for name in c.files(item)]
        elif item.name == "test_env":
            names = ["test_env/" + path.name for path in sorted(item.iterdir()) if path.is_file() and path.suffix == ".py"]
        else:
            raise ValueError("unclassified top-level directory: " + item.name)
        for name in names:
            raw = c.exact_file(root, name).read_bytes()
            rows.append({"path": name, "bytes": len(raw), "sha256": c.sha(raw)})
    return {"kind": "a_c.stdo301.public-checkpoint-inventory/1", "files": sorted(rows, key=lambda row: row["path"]),
            "excluded": ["run/ (all actor bodies, raw events and working proposals)", "private/ (configuration, invocation plans and scheduler records)",
                         "bundle/ and dist/ (only an explicitly selected reviewed delivery may be checkpointed later)", ".venv/ (isolated local dependencies)", "test_env/.tmp/", "PUBLIC-FILES.json (self)"],
            "claim": "Explicit public path selection only; no Git staging, semantic review or publication."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paths", action="store_true")
    args = parser.parse_args()
    result = inventory()
    if args.paths:
        print("\n".join(row["path"] for row in result["files"]))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
