"""Emit invocation-local bindings after verifying supplied source and theory."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package-root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--theory-root", type=Path, required=True)
    args = parser.parse_args()
    package, theory = args.package_root.resolve(), args.theory_root.resolve()
    inventory = json.loads((package / "interpretation/SOURCE_INVENTORY.json").read_text())
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    basis = inventory["encoding_theory"]
    if digest(theory / "manifest.json") != basis["manifest_sha256"] or digest(theory / basis["member"]) != basis["member_sha256"]:
        raise SystemExit("The supplied theory does not match the fixed encoding basis")
    for row in inventory["document_members"]:
        relative = Path(row["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise SystemExit("Unsafe documentary source coordinate")
        path = package / relative
        if not path.is_file() or path.is_symlink() or digest(path) != row["sha256"]:
            raise SystemExit("Documentary subject drift: " + row["path"])
    for name, key in (("program.json", "program_file_sha256"), ("source-account.json", "semantic_account_sha256"), ("SIGNATURE.md", "vocabulary_sha256"), ("FRAMES.md", "frames_sha256"), ("MAPPING.json", "mapping_sha256")):
        path = package / "interpretation" / name
        if not path.is_file() or path.is_symlink() or digest(path) != inventory["interpretation"][key]:
            raise SystemExit("Interpretation carrier drift: " + name)
    print(json.dumps({"kind": "axiom-indexer.binding-set", "schema_version": 1,
        "bindings": [{"uri_prefix": "repo://codex-v3/successor/", "path": str(package)},
                     {"uri_prefix": basis["release_uri"], "path": str(theory)}]}, indent=2))


if __name__ == "__main__":
    main()
