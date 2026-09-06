"""Retain verified native snapshot archives without embedding nested Git repositories."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import tarfile


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("run", type=Path)
    args = parser.parse_args()
    for context in json.loads((args.run / "contexts.json").read_text())["contexts"]:
        dest = Path(context["directory"])
        snapshot = Path(context["snapshot"])
        if not (dest / "execution-result.json").is_file():
            raise RuntimeError(f"Not completed: {dest}")
        expected = json.loads((dest / "snapshot-after.json").read_text())
        current = {str(p.relative_to(snapshot)): sha(p.read_bytes())
                   for p in sorted(snapshot.rglob("*"))
                   if p.is_file() and ".git" not in p.relative_to(snapshot).parts and not p.is_symlink()}
        if current != expected:
            raise RuntimeError(f"Post-run snapshot drift: {dest}")
        links = {str(p.relative_to(snapshot)): str(p.readlink())
                 for p in snapshot.rglob("*") if p.is_symlink()}
        archive = dest / "snapshot.tar.gz"
        if archive.exists():
            raise RuntimeError(f"Refuse overwrite: {archive}")
        with tarfile.open(archive, "w:gz", dereference=False) as tar:
            tar.add(snapshot, arcname="snapshot", filter=lambda member:
                    None if ".git" in Path(member.name).parts else member)
        archived_files, archived_links = {}, {}
        with tarfile.open(archive, "r:gz") as tar:
            for member in tar.getmembers():
                rel = str(Path(member.name).relative_to("snapshot"))
                if member.isfile():
                    archived_files[rel] = sha(tar.extractfile(member).read())
                elif member.issym():
                    archived_links[rel] = member.linkname
        if archived_files != expected or archived_links != links:
            raise RuntimeError(f"Archive verification failed: {archive}")
        record = {"kind": "t009.native-snapshot-archive", "archive": archive.name,
                  "archive_sha256": sha(archive.read_bytes()),
                  "files": archived_files, "symlinks": archived_links,
                  "excluded": "Generated .git metadata only; every input/post-run file and native link is retained.",
                  "original_snapshot_directory": str(snapshot),
                  "replay": "Extract snapshot.tar.gz and initialize a fresh Git root. For a relocated replay, preserve URI/member identity, explicitly rebind invocation-bindings.json to the extracted source, refresh invocation manifests and regenerate verification. Restore cache.py from the retained original fixture before replaying the functional repair. Original argv and raw output remain evidence of the original physical invocation."}
        (dest / "archive-subject.json").write_text(json.dumps(record, indent=2) + "\n")
        shutil.rmtree(snapshot)
        print(json.dumps({"context": context["name"], "archive_sha256": record["archive_sha256"],
                          "verified_files": len(archived_files), "native_links": len(links)}), flush=True)


if __name__ == "__main__":
    main()
