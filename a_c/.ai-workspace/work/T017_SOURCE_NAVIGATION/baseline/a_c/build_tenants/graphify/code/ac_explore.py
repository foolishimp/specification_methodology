#!/usr/bin/env python3
"""Generate a standalone 2D/3D constraint reader from an exact a_c model/carrier."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
import sys

import ac_graph as ac

ASSETS = Path(__file__).with_name("viewer")


def groundings(value):
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str) and isinstance(value.get("quote"), str)
                and type(value.get("start_line")) is int and type(value.get("end_line")) is int):
            yield value
        for child in value.values():
            yield from groundings(child)
    elif isinstance(value, list):
        for child in value:
            yield from groundings(child)


def title(record):
    fields = record.fields
    for key in ("value", "predicate", "qualifiers", "uncertainty", "allowed_variation"):
        value = fields.get(key)
        if isinstance(value, dict):
            for name in ("label", "statement", "definition", "meaning", "detail", "text"):
                if isinstance(value.get(name), str) and value[name]:
                    return value[name]
    return str(fields.get("kind", fields.get("sort", record.identity))).rsplit(":", 1)[-1]


def view_data(document, source_root=None, focus=None, heading="STDO · Constraint explorer"):
    model = (ac.validate(document) if document.get("profile") == ac.MODEL_PROFILE
             else ac.decode(ac.GraphCarrier(document)))
    contract = model.document["dependency_contract"]
    governing = set(contract["required_relation_kinds"])
    # Reuse the acquisition implementation; this viewer does not own a second closure rule.
    dependencies = ac._projection_index(model).dependencies
    reasons = {}

    def reason(source, target, label, path=None):
        item = {"label": label}
        if path is not None:
            item["path"] = path
        reasons.setdefault((source, target), []).append(item)

    references = []
    for ref in model.references:
        if ref.schema["governing"] and ref.target in model.records:
            reason(ref.owner, ref.target, "Governing reference", list(ref.path))
        references.append({"id": "reference:" + str(len(references)), "source": ref.owner,
                           "target": ref.target, "layer": "reference",
                           "label": "/".join(ref.path), "path": list(ref.path),
                           "governing": ref.schema["governing"], "domain": ref.schema["domain"]})
    relations = []
    nodes = []
    for record in model.records.values():
        fields = record.fields
        nodes.append({"id": record.identity, "family": record.family, "label": title(record),
                      "record": fields})
        if record.family == "relations":
            source, target = fields["source"], fields["target"]
            kind = fields["kind"]
            relations.append({"id": "relation:" + record.identity, "record_id": record.identity,
                              "source": source, "target": target, "layer": "relation",
                              "label": kind.rsplit(":", 1)[-1].replace("_", " "),
                              "kind": kind, "governing": kind in governing})
            if kind in governing:
                if source in model.records:
                    reason(source, record.identity, "Retain governing relation")
                    reason(record.identity, source, "Retain relation source")
                if target in model.records:
                    reason(record.identity, target, "Retain relation target")
        if record.family in ("constraints", "latitude", "residuals"):
            subjects = [fields["subject"]] if record.family == "residuals" else fields["applies_to"]
            for subject in subjects:
                if subject in model.records:
                    reason(subject, record.identity, "Retain attached " + {
                        "constraints": "constraint", "latitude": "latitude", "residuals": "caveat"
                    }[record.family])
    required = []
    for source, targets in dependencies.items():
        for target in sorted(targets):
            ac.require((source, target) in reasons, "unexplained acquisition dependency")
            required.append({"id": "required:" + str(len(required)), "source": source,
                             "target": target, "layer": "required", "label": "Requires retention",
                             "reasons": reasons[source, target]})
    for identity, resolution in model.external.items():
        nodes.append({"id": identity, "family": "external", "label": identity.rsplit(":", 1)[-1],
                      "record": resolution})

    sources = {}
    if source_root is not None:
        root = Path(source_root).resolve(strict=True)
        paths = sorted({g["path"] for n in nodes for g in groundings(n["record"])})
        for name in paths:
            path = (root / name).resolve()
            ac.require(not Path(name).is_absolute() and path.is_relative_to(root),
                       "grounding source escapes selected root: " + name)
            ac.require(path.is_file(), "grounding source missing: " + name)
            raw = path.read_bytes()
            sources[name] = {"text": raw.decode("utf-8"), "sha256": hashlib.sha256(raw).hexdigest()}

    if focus is None:
        focus = next((n["id"] for n in nodes if n["family"] == "constraints"), nodes[0]["id"] if nodes else None)
    ac.require(focus in model.records, "initial focus is not a local record")
    return {"profile": "a_c.constraint-explorer/1", "title": heading,
            "model": ac.model_identity(model), "basis": model.document["basis"],
            "interpretation": model.document["interpretation"], "focus": focus,
            "nodes": nodes, "links": required + relations + references, "sources": sources,
            "counts": {"records": len(model.records), "external": len(model.external),
                       "required": len(required), "relations": len(relations), "references": len(references)}}


def script_json(value):
    # JSON numbers are serialized losslessly as their original spelling here. The
    # browser's lossless parser retains large integers as display tokens.
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def render(data):
    vendor = ASSETS / "vendor"
    manifest = json.loads((vendor / "manifest.json").read_text())
    for name, expected in manifest["files"].items():
        ac.require(hashlib.sha256((vendor / name).read_bytes()).hexdigest() == expected,
                   "renderer asset digest differs: " + name)
    library = (vendor / "3d-force-graph-1.80.1.min.js").read_text()
    ac.require("</script" not in library.lower(), "renderer contains an HTML script delimiter")
    template = (ASSETS / "explorer.html").read_text()
    replacements = {"@@TITLE@@": html.escape(data["title"]), "@@CSS@@": (ASSETS / "explorer.css").read_text(),
                    "@@DATA@@": script_json(data), "@@VENDOR@@": library,
                    "@@APP@@": (ASSETS / "explorer.js").read_text(),
                    "@@LICENSE@@": html.escape((vendor / "3d-force-graph-LICENSE").read_text()
                                               + "\n\n" + (vendor / "THIRD_PARTY_NOTICES.txt").read_text())}
    # One pass prevents source content which resembles a template token being changed.
    import re
    return re.sub(r"@@[A-Z]+@@", lambda m: replacements[m.group()], template)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--focus")
    parser.add_argument("--title", default="STDO · Constraint explorer")
    args = parser.parse_args(argv)
    try:
        ac.require(not args.out.exists(), "output already exists; choose a fresh path")
        data = view_data(ac.read_json(args.input), args.source_root, args.focus, args.title)
        output = render(data)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("x", encoding="utf-8") as handle:
            handle.write(output)
        print(json.dumps({"status": "generated", "output": str(args.out), "model": data["model"],
                          "counts": data["counts"], "bytes": args.out.stat().st_size}))
        return 0
    except (ac.Refusal, OSError, UnicodeError, KeyError, TypeError, ValueError) as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
