#!/usr/bin/env python3
"""Read-only, stdlib replay of this exact proposal representation bundle."""
from __future__ import annotations

import argparse
import base64
import hashlib
import importlib.util
import json
from pathlib import Path, PurePosixPath
import sys

CODEC_SHA = "2f5de4d600e13904dc8cba3791ebdd83fe6ebb0c339654c86392baf9c2bd3667"
SOURCE_PINS = {
    "source-manifest.json": "dbf32e7f99eb7228ca361ec02f44227c05e02bb6bc447d1dd38255cd3ca4a4d4",
    "source-classification.json": "20a17b4028e4c6c1dd595b23f6c5e1efa96f609a4d1e1fb6176a85c0e67f6e3e",
    "package-custody.json": "6d35a6ad6472902294b1dfdd67c4e1e752ccc1b55ea4114acf10fb7389169af7",
}
SUBJECT = "repo://stdo-v3-common/35fb4824a064a84df5af214a0d0e2da597c18ac6"
VIS_SRI = "sha384-Ux6phic9PEHJ38YtrijhkzyJ8yQlH8i/+buBR8s3mAZOJrP1gwyvAcIYl3GWtpX1"
VIS_URL = "https://unpkg.com/vis-network@9.1.6/standalone/umd/vis-network.min.js"
VIS_LOCAL = "release_tools/vendor/vis-network-9.1.6.min.js"
SECTION_SHA = "5a95a610c8bb25e7ae743fa3126e3ef71d6aeea55a4423bdc2bebbe8656bd299"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: Path):
    def pairs(items):
        value = {}
        for key, item in items:
            require(key not in value, "duplicate JSON key")
            value[key] = item
        return value
    return json.loads(path.read_bytes(), object_pairs_hook=pairs)


def safe_path(value: str) -> str:
    p = PurePosixPath(value)
    require(bool(value) and not p.is_absolute() and p.as_posix() == value,
            "noncanonical bundle path")
    require(all(part not in ("", ".", "..") for part in p.parts)
            and "\\" not in value and "\0" not in value, "unsafe bundle path")
    return value


def files(root: Path) -> list[str]:
    require(root.is_dir() and not root.is_symlink(), "bundle root is redirected or absent")
    result = []
    for p in root.rglob("*"):
        require(not p.is_symlink(), "bundle contains a symlink")
        if p.is_file():
            result.append(p.relative_to(root).as_posix())
        else:
            require(p.is_dir(), "unsupported bundle member")
    return sorted(result)


def codec(path: Path):
    require(sha(path.read_bytes()) == CODEC_SHA, "codec differs from the exact reviewed snapshot")
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("ac_bundle_exact_codec", path)
    require(spec is not None and spec.loader is not None, "cannot load exact codec")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def check_sources(root: Path) -> dict:
    for name, expected in SOURCE_PINS.items():
        require(sha((root / name).read_bytes()) == expected, f"frozen source metadata changed: {name}")
    custody = load(root / "package-custody.json")
    semantic = load(root / "source-manifest.json")
    classes = load(root / "source-classification.json")
    require(custody["subject_id"] == semantic["subject_id"] == classes["subject_id"] == SUBJECT,
            "represented subject changed")
    members = custody["members"]
    require(len(members) == 81 and sum(row["bytes"] for row in members) == 3_298_515,
            "source extent differs")
    require(files(root / "source") == sorted(row["path"] for row in members),
            "source inventory has missing or extra members")
    for row in members:
        path = safe_path(row["path"])
        data = (root / "source" / path).read_bytes()
        require(len(data) == row["bytes"] and sha(data) == row["sha256"], f"source bytes changed: {path}")
        blob = hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
        require(blob == row["git_blob"], f"source Git-blob identity changed: {path}")
    return {"files": len(members), "bytes": custody["bytes"], "semantic_files": semantic["member_count"]}


def check_sections(root: Path) -> list[dict]:
    path = root / "release_tools/source-sections.json"
    require(sha(path.read_bytes()) == SECTION_SHA, "prepared source-section custody changed")
    rows = load(path)["sections"]
    require(len(rows) == len({row["id"] for row in rows}) == 845, "source-section extent differs")
    sources = {row["path"]: (root / "source" / row["path"]).read_text(encoding="utf-8").splitlines(keepends=True)
               for row in load(root / "source-manifest.json")["files"]}
    for row in rows:
        require(row["path"] in sources, "section is outside the semantic source selection")
        lines = sources[row["path"]]
        require(1 <= row["start_line"] <= row["end_line"] <= len(lines), "section line range differs")
        text = "".join(lines[row["start_line"] - 1:row["end_line"]])
        require(sha(text.encode("utf-8")) == row["sha256"], "section source bytes differ")
    return rows


def check_model_source(ac, model, root: Path) -> int:
    rows = check_sections(root)
    semantic = load(root / "source-manifest.json")
    source_files = [{key: row[key] for key in ("path", "sha256", "bytes")} for row in semantic["files"]]
    inventory = [{"id": row["id"], "sha256": row["sha256"]} for row in rows]
    subject = model.document["basis"]["subject"]
    require(subject["id"] == SUBJECT and subject["sha256"] == ac.digest(source_files)
            and subject["inventory"] == inventory, "model does not bind this exact source selection and section inventory")
    require(model.document["interpretation"]["source_reentry"]["sha256"]
            == ac.digest({"files": source_files, "sections": inventory}), "model source-reentry coordinate differs")
    by_section = {row["id"]: row for row in rows}
    texts = {row["path"]: (root / "source" / row["path"]).read_text(encoding="utf-8").splitlines(keepends=True)
             for row in source_files}
    count = 0
    def walk(value):
        nonlocal count
        if isinstance(value, list):
            for child in value:
                walk(child)
        elif isinstance(value, dict):
            if {"path", "section", "start_line", "end_line", "quote"} <= value.keys():
                require(value["section"] in by_section, "grounding section is outside the frozen selection")
                section = by_section[value["section"]]
                require(value["path"] == section["path"] and section["start_line"] <= value["start_line"]
                        <= value["end_line"] <= section["end_line"], "grounding line/path coordinates differ")
                text = "".join(texts[value["path"]][value["start_line"] - 1:value["end_line"]])
                require(isinstance(value["quote"], str) and bool(value["quote"]) and value["quote"] in text,
                        "grounding quote is absent from the exact recorded source range")
                count += 1
            for child in value.values():
                walk(child)
    for record in model.records.values():
        walk(record.fields)
    return count


def check(root: Path) -> dict:
    root = root.absolute()
    actual = files(root)
    inventory = load(root / "inventory.json")
    rows = inventory["files"]
    listed = [safe_path(row["path"]) for row in rows]
    require(listed == sorted(set(listed)), "inventory order or uniqueness differs")
    require(actual == sorted(listed + ["inventory.json", "SHA256SUMS"]),
            "bundle has missing or extra unlisted files")
    for row in rows:
        data = (root / row["path"]).read_bytes()
        require(len(data) == row["bytes"] and sha(data) == row["sha256"], f"bundle bytes changed: {row['path']}")
    sums = "".join(f"{sha((root / name).read_bytes())}  {name}\n"
                   for name in sorted(listed + ["inventory.json"]))
    require((root / "SHA256SUMS").read_text(encoding="utf-8") == sums, "SHA256SUMS differs")
    sources = check_sources(root)
    ac = codec(root / "codec/ac_graph.py")
    document = ac.read_json(root / "model.json")
    model = ac.validate(document)
    grounding_count = check_model_source(ac, model, root)
    for name in ("carrier.json", "graph.json"):
        recovered = ac.decode(ac.GraphCarrier(ac.read_json(root / name)))
        require(recovered.document == document, f"exact model recovery failed: {name}")
    result = load(root / "result.json")
    coverage = load(root / "coverage.json")
    require(result["model_id"] == model.identity and result["model_sha256"] == model.sha256,
            "proposal-result model coordinate differs")
    require(result["processing_complete"] is True and coverage["processing_complete"] is True,
            "this bundle requires complete processing, without asserting semantic completeness")
    counts = {name: len(records) for name, records in document["populations"].items()}
    require(result["family_counts"] == counts == coverage["family_counts"], "family counts differ")
    for name, expected in result.get("files", {}).items():
        require(name in ("model.json", "carrier.json", "graph.json", "coverage.json"),
                "unexpected proposal result-file contract")
        require(sha((root / name).read_bytes()) == expected, f"result file differs: {name}")
    record_data = load(root / "records.json")
    expected_records = [{"family": record.family, "record": record.fields}
                        for record in model.records.values()]
    require(record_data["records"] == expected_records, "record-browser payload differs from full model")
    scope = load(root / "view-scope.json")
    require(scope["parent"] == {"id": model.identity, "sha256": model.sha256}, "display parent differs")
    included, omitted = scope["included"], scope["omitted"]
    require(len(set(included)) == len(included) and len(set(omitted)) == len(omitted)
            and not set(included) & set(omitted) and set(included + omitted) == set(model.records),
            "display selection does not partition the record population")
    graph = load(root / "records-graph.json")
    require({row["id"] for row in graph["nodes"]} == set(model.records), "full readable graph omitted records")
    rendered = (root / "graph.html").read_text(encoding="utf-8")
    require(rendered.count(scope["banner_html"]) == 1, "display scope banner differs")
    require(rendered.count(f'src="{VIS_LOCAL}"') == 1 and VIS_URL not in rendered,
            "offline display dependency differs")
    original = rendered.replace(scope["banner_html"], "", 1).replace(f'src="{VIS_LOCAL}"', f'src="{VIS_URL}"', 1)
    require(sha(original.encode("utf-8")) == scope["official_html_sha256"],
            "display has changes beyond the declared source rewrite and scope banner")
    js = (root / VIS_LOCAL).read_bytes()
    require("sha384-" + base64.b64encode(hashlib.sha384(js).digest()).decode() == VIS_SRI,
            "offline JavaScript differs from official SRI pin")
    return {"status": "passed", "subject": SUBJECT, "model": {"id": model.identity, "sha256": model.sha256},
            "inventory_files": len(rows), "source": sources, "records": len(model.records),
            "physical_grounding_occurrences": grounding_count,
            "displayed_records": len(included), "omitted_records": len(omitted),
            "claim": "Exact bundle custody, bounded structural checks and carrier recovery; no semantic acceptance, source-method release, or public-distribution authorization."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.directory), indent=2, ensure_ascii=False, sort_keys=True))
        return 0
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(json.dumps({"status": "refusal", "reason": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
