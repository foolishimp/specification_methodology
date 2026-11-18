"""Pinned reusable-index acquisition; selection and rendering remain in context_core."""
from __future__ import annotations

from pathlib import Path, PurePosixPath
from typing import Any

import context_core as core

PRODUCT = Path(__file__).resolve().parents[3]
DEFINITION_ID = "urn:stdo:product-definition:purpose-context"
ENTRYPOINT = "skills/stdo-context/scripts/context.py"
CATALOG = "skills/stdo-context/indexes/CATALOG.json"


def local_file(root: Path, relative: str) -> Path:
    core._text(relative, "relative member path")
    name = PurePosixPath(relative)
    core.need(not name.is_absolute() and str(name) == relative and
              all(part not in {"", ".", ".."} for part in name.parts), "nonportable member path")
    path = root / relative
    core.need(path.is_file() and not path.is_symlink() and
              all(not parent.is_symlink() for parent in path.parents), "member must be a regular file without symlink ancestors")
    return path


def public_bundle(expected_sha256: str) -> dict[str, Any]:
    core._sha(expected_sha256, "selected public manifest")
    path = local_file(PRODUCT, "PUBLIC_MANIFEST.json")
    core.need(core.raw_digest(path.read_bytes()) == expected_sha256, "public manifest differs from selected pin")
    public = core.read_json(path)
    core.need(public.get("profile") == "purpose-context.public-manifest/1" and
              public.get("product_definition_id") == DEFINITION_ID and
              public.get("entrypoint") == ENTRYPOINT and public.get("catalog") == CATALOG,
              "unsupported Purpose Context public manifest")
    core.need(isinstance(public.get("files"), list) and bool(public["files"]), "public member inventory required")
    pins = {}
    for row in public["files"]:
        core._object(row, {"path", "sha256", "bytes"}, "public member")
        core._sha(row["sha256"], "public member hash")
        core.need(type(row["bytes"]) is int and row["bytes"] >= 0, "public member byte count required")
        core.need(row["path"] not in pins, "duplicate public member")
        body = local_file(PRODUCT, row["path"]).read_bytes()
        core.need(len(body) == row["bytes"] and core.raw_digest(body) == row["sha256"],
                  "public member differs: " + row["path"])
        pins[row["path"]] = row
    required = {ENTRYPOINT, CATALOG, "skills/stdo-context/scripts/context_core.py",
                "skills/stdo-context/scripts/context_catalog.py", "skills/stdo-context/references/authoring.md",
                "skills/stdo-context/references/index.schema.json", public.get("skill"), public.get("product_definition")}
    core.need(required <= pins.keys(), "public manifest omits a required runtime, instruction or definition member")
    definition = core.read_json(local_file(PRODUCT, public["product_definition"]))
    core.need(definition["product"]["definition_id"] == DEFINITION_ID and definition["product"]["name"] == "Purpose Context",
              "public Product Definition identity differs")
    core.need(definition["constitution"]["stdo"]["basis"] == public["construction_basis"], "public construction basis differs")
    value = core.read_json(local_file(PRODUCT, CATALOG))
    core._object(value, {"profile", "entries"}, "index catalog")
    core.need(value["profile"] == "purpose-context.index-catalog/1" and isinstance(value["entries"], list), "unsupported index catalog")
    entries = [read_entry(row, pins) for row in value["entries"]]
    core.need(len({row["entry"]["id"] for row in entries}) == len(entries), "duplicate catalog index ID")
    return {"public": public, "public_manifest_sha256": expected_sha256,
            "catalog_sha256": pins[CATALOG]["sha256"], "entries": entries}


def read_entry(entry: dict[str, Any], pins: dict[str, Any]) -> dict[str, Any]:
    core._object(entry, {"id", "description", "subject_id", "method", "purpose_id", "purpose_sha256",
                        "corpus_sha256", "view_sha256", "source_members", "family_guard", "artifacts", "standing"}, "catalog entry")
    for field in ("id", "description", "standing"):
        core._text(entry[field], "catalog " + field)
    core._object(entry["artifacts"], {"index", "purpose", "sources", "provenance"}, "catalog artifacts")
    artifacts = {}
    for name, ref in entry["artifacts"].items():
        core._object(ref, {"path", "sha256"}, "catalog artifact")
        core.need(ref["path"] in pins and pins[ref["path"]]["sha256"] == ref["sha256"], "catalog artifact not pinned by public manifest")
        artifacts[name] = core.read_json(local_file(PRODUCT, ref["path"]))
    sources, purpose, index = (artifacts[name] for name in ("sources", "purpose", "index"))
    core._object(sources, {"profile", "subject_id", "method", "source_root_kind", "method_manifest_path", "files"}, "portable sources")
    core.need(sources["profile"] == "purpose-context.sources/1" and sources["source_root_kind"] in {"installed-method-root", "development-method-root"} and
              sources["method_manifest_path"] == "manifest.json", "unsupported reusable-source binding")
    core.need(isinstance(sources["files"], list) and bool(sources["files"]), "portable source members required")
    for row in sources["files"]:
        core._object(row, {"id", "path", "sha256"}, "portable source")
        core._text(row["id"], "portable source ID")
        core._sha(row["sha256"], "portable source hash")
        name = PurePosixPath(row["path"])
        core.need(not name.is_absolute() and str(name) == row["path"] and ".." not in name.parts, "source path must be portable")
    core.need(len({row["id"] for row in sources["files"]}) == len(sources["files"]), "duplicate portable source ID")
    core.validate_purpose(purpose)
    core._guard(entry["family_guard"], "catalog family guard")
    core.need(all(clause["fact"] in purpose["facts"] for values in entry["family_guard"].values() for clause in values),
              "catalog guard names an undeclared purpose fact")
    source_members = [{"id": row["id"], "sha256": row["sha256"]} for row in sources["files"]]
    identity = {"profile": core.CORPUS_PROFILE, "subject_id": sources["subject_id"], "method": sources["method"], "files": source_members}
    core.need(entry["subject_id"] == sources["subject_id"] and entry["method"] == sources["method"] and
              entry["source_members"] == source_members and entry["corpus_sha256"] == core.digest(identity), "catalog source identity differs")
    core.need(entry["purpose_id"] == purpose["id"] == index["purpose_id"] and
              entry["purpose_sha256"] == core.digest(purpose) == index["purpose_sha256"], "catalog purpose identity differs")
    core.need(index["profile"] == core.INDEX_PROFILE and entry["corpus_sha256"] == index["corpus_sha256"] and
              entry["view_sha256"] == index["input_view_sha256"], "catalog index identity differs")
    return {"entry": entry, **artifacts}


def summary(access: dict[str, Any], item: dict[str, Any]) -> dict[str, Any]:
    entry = item["entry"]
    return {"index_id": entry["id"], "description": entry["description"], "subject_id": entry["subject_id"],
            "method": entry["method"], "purpose_id": entry["purpose_id"], "purpose_sha256": entry["purpose_sha256"],
            "corpus_sha256": entry["corpus_sha256"], "source_members": entry["source_members"],
            "family_guard": entry["family_guard"], "index_file_sha256": entry["artifacts"]["index"]["sha256"],
            "index_sha256": core.digest(item["index"]), "rules": len(item["index"]["rules"]),
            "standing": entry["standing"], "semantic_coverage": "unassessed", "covered": False,
            "public_manifest_sha256": access["public_manifest_sha256"], "catalog_sha256": access["catalog_sha256"]}


def find_entry(access: dict[str, Any], ident: str) -> dict[str, Any]:
    matches = [row for row in access["entries"] if row["entry"]["id"] == ident]
    core.need(len(matches) == 1, "no unique catalog index with the selected ID")
    return matches[0]


def source_binding(item: dict[str, Any], source_root: Path, method: dict[str, Any]) -> dict[str, Any]:
    """Hash the explicitly selected release or development manifest and members."""
    sources = item["sources"]
    core.need(method == sources["method"], "selected method differs from catalog basis; no release substitution")
    root = source_root.absolute()
    path = local_file(root, sources["method_manifest_path"])
    core.need(core.raw_digest(path.read_bytes()) == method["manifest_sha256"], "actual method manifest differs from selected basis")
    release = core.read_json(path)
    if sources["source_root_kind"] == "installed-method-root":
        core.need(release.get("kind") == "stdo.installed-release-manifest" and
                  method["uri"] == "stdo://releases/" + release["release"]["cut"] + "/", "actual installed method identity differs")
    else:
        core._object(release, {"profile", "method_uri", "standing", "predecessor", "standards"}, "development source manifest")
        core.need(release["profile"] == "purpose-context.development-method-manifest/1" and
                  release["standing"] == "development-source; unpublished; unqualified" and
                  method["uri"].startswith("urn:stdo:development-source:") and
                  release["method_uri"] == method["uri"], "actual development method identity differs")
        core._object(release["predecessor"], {"uri", "manifest_sha256"}, "development predecessor")
        core._sha(release["predecessor"]["manifest_sha256"], "development predecessor manifest")
        core.need(release["predecessor"]["uri"].startswith("stdo://releases/"), "development predecessor must name an exact release")
        core._object(release["standards"], {"installed_root", "members"}, "development standards")
        core.need(release["standards"]["installed_root"] == "standards" and
                  isinstance(release["standards"]["members"], list), "development source members required")
        for row in release["standards"]["members"]:
            core._object(row, {"path", "sha256"}, "development source member")
            core._sha(row["sha256"], "development source member hash")
            local_file(root / "standards", row["path"])
        paths = [row["path"] for row in release["standards"]["members"]]
        core.need(len(paths) == len(set(paths)) and bool(paths), "development source members must be unique and nonempty")
    standards = release["standards"]
    declared = {str(PurePosixPath(standards["installed_root"]) / row["path"]): row["sha256"] for row in standards["members"]}
    if sources["source_root_kind"] == "development-method-root":
        core.need(list(declared) == [row["path"] for row in sources["files"]], "development source closure/order differs")
    files = []
    for row in sources["files"]:
        core.need(declared.get(row["path"]) == row["sha256"], "selected source is not bound by the actual method manifest")
        body = local_file(root, row["path"]).read_bytes()
        core.need(core.raw_digest(body) == row["sha256"], "actual selected source differs: " + row["id"])
        files.append({"id": row["id"], "path": str((root / row["path"]).resolve()), "sha256": row["sha256"]})
    return {"profile": core.CORPUS_PROFILE, "subject_id": sources["subject_id"], "method": method, "files": files}


def binding_receipt(access: dict[str, Any], item: dict[str, Any], source_root: Path) -> dict[str, Any]:
    return {"profile": "purpose-context.reuse-binding/1", "index_id": item["entry"]["id"],
            "public_manifest_sha256": access["public_manifest_sha256"], "catalog_sha256": access["catalog_sha256"],
            "index_file_sha256": item["entry"]["artifacts"]["index"]["sha256"],
            "source_root": str(source_root.resolve()), "source_root_kind": item["sources"]["source_root_kind"],
            "method_manifest_sha256": item["sources"]["method"]["manifest_sha256"],
            "verification_scope": "Exact method manifest and ordered selected source members; not whole-install qualification."}


def select(access: dict[str, Any], bundle: Path, manifest: dict[str, Any], purpose: dict[str, Any],
           view: dict[str, Any], query: dict[str, Any], ident: str | None) -> tuple[dict[str, Any], dict[str, Any]]:
    receipt = core.read_json(bundle / "REUSE-BINDING.json")
    selected_id = ident if ident is not None else receipt["index_id"]
    item = find_entry(access, selected_id)
    root = Path(receipt["source_root"])
    fresh = source_binding(item, root, manifest["method"])
    matches = {"public_manifest": receipt["public_manifest_sha256"] == access["public_manifest_sha256"],
               "catalog": receipt["catalog_sha256"] == access["catalog_sha256"],
               "binding": receipt == binding_receipt(access, item, root),
               "method": manifest["method"] == item["sources"]["method"], "source": manifest == fresh,
               "purpose": purpose == item["purpose"], "query_purpose": query.get("purpose_id") == purpose["id"]}
    result = {**summary(access, item), "matches": matches, "query_sha256": core.digest(query),
              "index_path": str(local_file(PRODUCT, item["entry"]["artifacts"]["index"]["path"])), "reused": True}
    if not all(matches.values()):
        return {**result, "status": "refused", "selected": None, "reason": "catalog reuse identity mismatch"}, item
    core._object(query, {"id", "purpose_id", "facts"}, "query")
    core._text(query["id"], "query ID")
    core.need(isinstance(query["facts"], dict) and query["facts"].keys() <= purpose["facts"].keys(), "query has undeclared purpose facts")
    core.validate_index(item["index"], manifest, purpose, view)
    guard = item["entry"]["family_guard"]
    applicability = core.evaluate_guard(guard, query["facts"])
    details = [{**clause, "result": core.evaluate_guard({"all": [clause], "any": []}, query["facts"])}
               for values in guard.values() for clause in values]
    matches["family"] = applicability
    if applicability != "true":
        status = "incomplete" if applicability == "unknown" else "refused"
        return {**result, "status": status, "selected": None, "family_predicates": details,
                "reason": "family applicability is " + applicability + "; do not invent or coerce caller facts"}, item
    return {**result, "status": "selected", "selected": selected_id, "family_predicates": details,
            "mechanical_status": "valid"}, item
