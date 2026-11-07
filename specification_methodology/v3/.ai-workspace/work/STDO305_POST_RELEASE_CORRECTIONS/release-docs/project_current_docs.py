"""Apply only the reviewed scope of the unreleased proof-document projection."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "specification_methodology/v3/build_tenants/common-tools"))
import current_assets as a
import proof_reader_current as proof
import documentation_current as docs

base = ROOT / "specification_methodology/v3/build_tenants/common/standards/documentation"
assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() == "6edfffb2f8a35b244782749383fb19105d9227d9"
start = time.monotonic()
files = a.read_tree(base)
before = dict(files)
old_metadata = json.loads(files["DOCUMENTATION.json"])
assert old_metadata["members"] == a.inventory({p: raw for p, raw in files.items() if p != "DOCUMENTATION.json"})
before_dir = HERE / "before"
(before_dir / "documentation-SELECTION.json").write_bytes(files["SELECTION.json"])
(before_dir / "DOCUMENTATION.json").write_bytes(files["DOCUMENTATION.json"])
proof_files = {p.removeprefix("proofs/"): raw for p, raw in files.items() if p.startswith("proofs/")}
old_catalog = json.loads(proof_files["PROOFS.json"])
for name, (key, _) in proof.DOCUMENT_LINKS.items():
    ref = json.loads(proof_files["SELECTION.json"])[key]
    original = subprocess.check_output(["git", "show", proof.DOCUMENT_SOURCE_COMMIT + ":" + ref["path"]], cwd=ROOT)
    assert original == proof_files[name] and a.sha(original) == ref["sha256"]
proof.project_documents(proof_files)
catalog, sources = proof.catalog(proof_files)
assert {k: v for k, v in catalog.items() if k not in ("members", "documentation_projection")} == {k: v for k, v in old_catalog.items() if k != "members"}
proof_files["PROOFS.json"] = a.encoded(catalog)
proof_files["index.html"] = proof.render(catalog, sources)
files.update({"proofs/" + p: raw for p, raw in proof_files.items()})
selected = json.loads(files["SELECTION.json"])
selected["proof_catalog"] = {"path": (base / "proofs/PROOFS.json").relative_to(ROOT).as_posix(), "sha256": a.sha(proof_files["PROOFS.json"])}
files["SELECTION.json"] = a.encoded(selected)
(HERE / "documentation-selection.json").write_bytes(files["SELECTION.json"])
files["DOCUMENTATION.json"] = a.encoded(docs.metadata(files))
allowed = {"SELECTION.json", "DOCUMENTATION.json", "proofs/correspondence.md", "proofs/library-provenance.md", "proofs/PROOFS.json", "proofs/index.html", "proofs/source-documents/correspondence.md.txt", "proofs/source-documents/library-provenance.md.txt"}
changed = {p for p in files if before.get(p) != files[p]}
assert changed == allowed
delta = []
for path in sorted(changed):
    target = base / path
    assert target.read_bytes() == before[path] if path in before else not target.exists()
    delta.append({"path": target.relative_to(ROOT).as_posix(), "before": None if path not in before else {"sha256": a.sha(before[path]), "bytes": len(before[path]), "mode": oct(target.stat().st_mode & 0o777)}, "after": {"sha256": a.sha(files[path]), "bytes": len(files[path]), "mode": oct(target.stat().st_mode & 0o777) if target.exists() else "0o644"}})
(HERE / "GENERATED_DELTA.json").write_bytes(a.encoded({"preimage": "6edfffb2f8a35b244782749383fb19105d9227d9", "changes": delta, "unchanged_members": sorted(set(before) - changed), "scope": "Unreleased link presentation and current inventory only; original selection and published evidence remain in Git/release custody; no Lean, viewer or representation regeneration."}))
for path in sorted(changed):
    target = base / path
    assert target.read_bytes() == before[path] if path in before else not target.exists()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(files[path])
print(json.dumps({"status": "projected", "changed": len(changed), "unchanged": len(set(before) - changed), "seconds": time.monotonic() - start, "proof_catalog_sha256": a.sha(proof_files["PROOFS.json"]), "documentation_sha256": a.sha(files["DOCUMENTATION.json"])}))
