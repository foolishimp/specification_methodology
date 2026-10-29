"""One selected local custody operation; never executes the retained proofs."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import time

import transport as t


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OLD = HERE.parent / "evidence-transport-001"


def write(name, value):
    with (HERE / name).open("xb") as stream:
        stream.write(t.encode(value))


def stamps(path):
    s = path.stat()
    return {"bytes": s.st_size, "inode": s.st_ino, "mtime_ns": s.st_mtime_ns}


def equal_files(a, b):
    with a.open("rb") as x, b.open("rb") as y:
        while True:
            block = x.read(t.CHUNK)
            t.need(y.read(len(block)) == block, "restored bytes differ from original")
            if not block:
                t.need(not y.read(1), "restored extra bytes")
                return


def main():
    started = time.monotonic()
    inventory = t.decode((HERE / "STAT-INVENTORY-001.json").read_bytes())
    old_selected = t.decode((OLD / "SELECTED.json").read_bytes())
    historical = old_selected["historical_pins"].copy()
    old_manifest_raw = (OLD / "payload/MANIFEST.json").read_bytes()
    t.need(t.raw_sha(old_manifest_raw) == "59732cdb8f956e07ecc1734c63e5c29b3281f8047c4c58b4e5211409a24635ea", "old manifest changed")
    old_manifest = t.decode(old_manifest_raw)
    known = {"GateLocalNames.olean.private": (118435848, "6a2baff9b75dbe940c910dcbd74f855fa00035e21379c0a37e5cd076f92766d7"),
             "GateExternalNames.olean.private": (109636952, "e4a66c78c10f6a7151c65c84cf7a8ccdfebe247c0d43136f83224e015596f9a3")}
    rows = []
    before = {}
    for item in inventory["files"]:
        path = t.file_path(ROOT, item["path"])
        t.need(path.name in known, "unexpected oversized member; no omission allowed")
        before[item["path"]] = stamps(path)
        t.need(before[item["path"]] == {k: item[k] for k in ("bytes", "inode", "mtime_ns")}, "file changed since inventory")
        identity = t.file_identity(path)
        size, digest = known[path.name]
        t.need(identity == {"bytes": size, "sha256": digest}, "new payload identity requires a separate disposition")
        rows.append({"path": item["path"], **identity})
        if not item["previous_transport"]:
            pin_path = path.parent / "manifest.json"
            raw = pin_path.read_bytes()
            pin = t.decode(raw)["members"][path.name]
            t.need(pin == digest, "original manifest does not match selected bytes")
            historical.append({"member_path": item["path"], "declared_member_sha256": pin,
                               "pin_source": pin_path.relative_to(ROOT).as_posix(),
                               "pin_source_sha256": t.raw_sha(raw)})
    t.rows_valid(rows)
    t.need(shutil.disk_usage(HERE).free > sum(x["bytes"] for x in rows) + 128 * 1024**2,
           "insufficient free space for exact disposable roundtrip")
    write("ORIGINALS-BEFORE.json", {"observed_utc": datetime.now(timezone.utc).isoformat(), "files": before})
    write("SELECTED.json", {"schema": "a_c.evidence-transport-selection/1", "files": rows,
                            "historical_pins": historical})
    selection = t.file_identity(HERE / "SELECTED.json")["sha256"]
    print(json.dumps({"phase": "all-original-identities-verified", "files": len(rows), "selection_sha256": selection}), flush=True)
    prepared = t.prepare(ROOT, HERE / "SELECTED.json", selection, HERE / "payload")
    write("PREPARE.json", {"observed_utc": datetime.now(timezone.utc).isoformat(), **prepared})
    new_manifest, _ = t.manifest_load(HERE / "payload", prepared["manifest_sha256"])
    t.need(new_manifest["payloads"] == old_manifest["payloads"], "compressed identity differs from original transport")
    for item in new_manifest["payloads"]:
        equal_files(HERE / "payload" / item["path"], OLD / "payload" / item["path"])
    print(json.dumps({"phase": "prepared", **prepared, "compressed_bytes_equal_transport001": True}), flush=True)
    target = HERE / "roundtrip-restored"
    restored = t.restore(HERE / "payload", prepared["manifest_sha256"], target)
    restored_stamps = {}
    for row in rows:
        path = target / row["path"]
        equal_files(ROOT / row["path"], path)
        t.need(t.file_identity(path) == {k: row[k] for k in ("bytes", "sha256")}, "restored identity mismatch")
        restored_stamps[row["path"]] = stamps(path)
    repeated = t.restore(HERE / "payload", prepared["manifest_sha256"], target)
    t.need(not repeated["restored"] and len(repeated["already_present_identical"]) == len(rows), "repeat restore changed population")
    t.need(restored_stamps == {row["path"]: stamps(target / row["path"]) for row in rows}, "repeat restore rewrote existing files")
    final = t.verify(HERE / "payload", prepared["manifest_sha256"], ROOT)
    t.need(before == {row["path"]: stamps(ROOT / row["path"]) for row in rows}, "original file metadata changed")
    shutil.rmtree(target)
    write("ROUNDTRIP.json", {"schema": "a_c.T013.evidence-transport-roundtrip/1",
                            "closed_utc": datetime.now(timezone.utc).isoformat(),
                            "manifest_sha256": prepared["manifest_sha256"], "selection_sha256": selection,
                            "restoration": restored, "repeat_restore": repeated,
                            "all_restored_files_compared_byte_for_byte_and_sha256": len(rows),
                            "repeat_inode_mtime_preserved": True, "original_inode_mtime_preserved": True,
                            "compressed_payloads_byte_identical_to_transport001": True,
                            "final_original_comparison": final,
                            "disposable_restored_copies_removed": not target.exists(),
                            "originals_removed_or_overwritten": [], "wall_seconds": time.monotonic() - started})
    print(json.dumps({"phase": "roundtrip-complete", "files": len(rows), "wall_seconds": time.monotonic()-started}), flush=True)


if __name__ == "__main__":
    main()
