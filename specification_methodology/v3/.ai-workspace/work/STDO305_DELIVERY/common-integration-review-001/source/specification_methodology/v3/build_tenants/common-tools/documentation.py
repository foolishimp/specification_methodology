#!/usr/bin/env python3
"""Bundle and verify the required offline documentation in a native STDO payload."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

VERSION = "3.0.4"
DOC_ROOT = "standards/documentation/"
VIEWER_SHA256 = "ea40c989b1f933f52294b71dba972775c8d51d836ae5842fbc44f69648dd4eb6"
MODEL_SHA256 = "691c4ab0d0993312a31e7e2371070ea4758fdf74b32862ff4d5a32d05af79fbf"
SOURCE_COMMIT = "35fb4824a064a84df5af214a0d0e2da597c18ac6"
SOURCE_ID = "repo://stdo-v3-common/" + SOURCE_COMMIT
MODEL_ID = "urn:a-c:generation:0657852b6fd1fa48457c3f7d:model:2e6f0d59737b5bca00691b60"
CODE_SHA256 = "26e8e1e93221781b7a25fc48ad457c7ea97275cd08dcadba91075cbf8b1be8c9"
PROOF_MEMBERS = {"index.html", "PROOFS.json", "report.json", "sources/AC.lean", *{"sources/AC/" + n + ".lean" for n in ("Audit", "Closure", "Fixture", "Model", "Projection", "Run", "Toy")}}
MEMBERS = {"index.html", "README.md", "constraint-explorer/index.html", "code-explorer/index.html", "DOCUMENTATION.json", *{"proofs/" + p for p in PROOF_MEMBERS}}


def current():
    here = str(Path(__file__).resolve().parent)
    if here not in sys.path:
        sys.path.insert(0, here)
    import documentation_current
    return documentation_current


def proof_checker():
    path = Path(__file__).resolve().with_name("proof_reader.py")
    try:
        spec = importlib.util.spec_from_file_location("stdo_proof_reader", path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    except (OSError, ImportError) as exc:
        raise ValueError("required proof reader checker unavailable: " + str(exc)) from exc


def package_checker():
    """Use the registered package checker's route semantics, never work records."""
    path = Path(__file__).resolve().with_name("package_tools.py")
    try:
        spec = importlib.util.spec_from_file_location("stdo_documentation_package_tools", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except (OSError, ImportError) as exc:
        raise ValueError("required package checker unavailable: " + str(exc)) from exc


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def viewer_data(raw):
    require(sha(raw) == VIEWER_SHA256, "viewer differs from selected documentation artifact")
    match = re.search(rb'<script id="explorer-data" type="application/json">(.*?)</script>', raw, re.S)
    require(match is not None, "viewer data missing")
    data = json.loads(match[1])
    require(data["model"]["id"] == MODEL_ID and data["model"]["sha256"] == MODEL_SHA256,
            "viewer model identity differs")
    require(data["basis"]["subject"]["id"] == SOURCE_ID, "viewer subject differs")
    return data


def guide():
    return f"""# STDO {VERSION} documentation

Open the [documentation home](index.html), then choose:

- [Constraints](constraint-explorer/index.html): STDO's historical common model.
- [Code example](code-explorer/index.html): ABIogenesis requirements, selected
  canonicalization code and test sources, with attributed proposed traces.
- [Lean proofs](proofs/index.html): proof statements, source and retained results.
- [Use the tools](../tooling/README.md): create a writable copy to build your own.

All three readers open in a browser.
These files are installed with STDO {VERSION}; no additional download or
Graphify, Lean, a_c or Node installation is needed to read them.

## Open an installed copy

The ordinary manager resolves the local file:

```sh
stdo resolve stdo://releases/v{VERSION}/standards/documentation/index.html
```

Open the returned `path` in a desktop browser. The file and its explorer work
offline. A browser with WebGL supports 3D and 2D. The initial Layered view,
search, Files navigation and full text reader remain available without WebGL.
No service is needed.

## Read and follow constraints

1. Search the constraints, select another record family, or use **Files** to
   browse the represented source folders and files.
2. Select a result to read its complete statement, conditions and exceptions.
3. Follow labelled authored relations or required-retention links. They have
   different meanings; a graph edge does not assert a proved implication.
4. Read attached caveats and source quotations. Open a quotation to see its
   embedded source file and highlighted lines.
5. Use the reading trail and Back to revisit exact steps, including parallel
   and self-relations. Selecting an unrelated result begins a new trail.
6. Switch **3D**, **2D** or **Layered** to view the same selected record,
   relationships and reading trail. Focus, expand or show the overview. Drag
   to orbit in force views; scroll and use zoom controls in Layered.
7. Use **Show in files** or **Back to file** to move between source discovery
   and logical connections. Folder order does not create a semantic relation.

## Code and proof examples

The ABI example is the reviewed T-019 artifact: a frozen representation of
ABIogenesis and a four-file code/test selection. Its five proposed trace links
cover part of canonical ordering and serialization. They do not establish the
broader roundtrip/admission clauses, executed tests or semantic satisfaction.
The reader names its source, author, parser and unresolved endpoints. Use the
browser's Back button or open readers in separate tabs to return to this home.

The Lean reader shows exact T-011 proof sources and its retained independent
report. It explains finite closure and record-preserving projection, premises
and limits. This historical report is not a new Lean run or a proof of the
code overlay. The [proof catalog](proofs/PROOFS.json) binds its sources.

## Represented source and current method

**Distributed with STDO {VERSION}; represented source: historical common cut
{SOURCE_COMMIT[:8]}.** This preserves the T-014 representation and source data
with the current unified reader. It contains 1,987 local records (841 constraints), 1,021 external
resolutions and 58 embedded source files. It is not a source-matched map of
the {VERSION} standards and has not acquired that authority by being bundled.

Use the [installed current method](../README.md) and
[Getting Started](../../plugins/spec/references/GETTING_STARTED.md) for current
method decisions. The explorer's embedded source remains the historical source
it names. Lean's structural closure and projection proofs do not prove the
English constraint predicates. [DOCUMENTATION.json](DOCUMENTATION.json) binds
the distributing version, represented source and exact documentation bytes.
""".encode()


def landing():
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="icon" href="data:,"><title>STDO {VERSION} documentation</title>
<style>body{{margin:0;background:#111b24;color:#e9eff2;font:16px/1.7 system-ui,sans-serif}}main{{max-width:900px;margin:6vh auto;padding:28px}}small,a{{color:#a9d5bf}}h1{{font-size:38px;line-height:1.2}}h2{{font-size:22px;margin:0}}.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:18px}}article{{border:1px solid #354654;border-radius:10px;padding:23px}}p{{max-width:76ch}}.scope{{color:#b7c5d1;font-size:14px}}footer{{margin-top:32px;border-top:1px solid #354654;padding-top:20px}}</style></head>
<body><main><small>INSTALLED DOCUMENTATION · STDO {VERSION}</small>
<h1>Read the reasoning.<br>Follow it into source and proof.</h1>
<p>These readers work offline. Explore the same selected information in 3D, 2D or Layered views, or follow the files and full text.</p>
<div class="cards">
<article><h2><a href="constraint-explorer/index.html">Constraints →</a></h2><p>Follow STDO constraints, conditions, caveats and source passages.</p><p class="scope">Historical common {SOURCE_COMMIT[:8]}: 1,987 records, including 841 constraints.</p></article>
<article><h2><a href="code-explorer/index.html">Code example →</a></h2><p>Navigate ABIogenesis requirements into selected canonicalization code and test sources.</p><p class="scope">A reviewed four-file example. Proposed trace links retain their limits; test source is not a test result.</p></article>
<article><h2><a href="proofs/index.html">Lean proofs →</a></h2><p>Read closure and projection theorems, their premises, exact Lean source and retained proof evidence.</p><p class="scope">Historical T-011 report; structural results do not prove English requirements or this code example.</p></article>
<article><h2><a href="../tooling/README.md">Use the tools →</a></h2><p>Materialize the bundled a_c and Skills source into a writable workspace and build your own project's representation.</p><p class="scope">Reading needs no setup. Running optional Graphify or Lean paths requires their declared dependencies.</p></article>
</div><footer><p><a href="README.md">Reading guide</a> · <a href="../README.md">Current standards</a> · <a href="../../plugins/spec/references/GETTING_STARTED.md">Getting Started</a> · <a href="DOCUMENTATION.json">Exact inventory</a></p>
<p class="scope">Use current installed standards for current method decisions. Historical representations keep their own source identity. 3D and 2D use WebGL; Layered and text remain available without it. Open entries in separate tabs or use browser Back. No service is needed.</p></footer>
</main></body></html>
""".encode()


def bundle(viewer, destination, code_viewer, proofs):
    viewer, destination = Path(viewer).resolve(), Path(destination)
    require(not destination.is_symlink(), "redirected destination")
    # Resolve platform aliases such as macOS /var -> /private/var before overlap
    # checks. A fresh directory beneath that canonical parent is a valid output.
    destination = destination.resolve()
    require(not destination.exists(), "documentation destination already exists")
    require(not viewer.is_relative_to(destination), "output overlaps imported viewer")
    raw = viewer.read_bytes()
    viewer_data(raw)
    code_raw = Path(code_viewer).read_bytes()
    require(sha(code_raw) == CODE_SHA256, "code viewer differs from reviewed artifact")
    proof_paths = list(Path(proofs).rglob("*"))
    require(not any(p.is_symlink() for p in proof_paths), "redirected proof payload")
    proof_files = {p.relative_to(proofs).as_posix(): p.read_bytes() for p in proof_paths if p.is_file()}
    proof_checker().check_payload(proof_files)
    files = {"index.html": landing(), "README.md": guide(), "constraint-explorer/index.html": raw,
             "code-explorer/index.html": code_raw, **{"proofs/" + p: b for p, b in proof_files.items()}}
    metadata = {"kind": "stdo.installed-documentation/1", "distribution_version": VERSION,
                "role": "non-normative-documentation", "entrypoint": "index.html",
                "code_example": {"subject": "ABIogenesis T-019 canonicalization", "viewer_sha256": CODE_SHA256},
                "source": {"identity": SOURCE_ID, "commit": SOURCE_COMMIT,
                           "standing": "historical-common-proposal", "model_identity": MODEL_ID,
                           "model_sha256": MODEL_SHA256, "viewer_sha256": VIEWER_SHA256},
                "members": [{"path": p, "bytes": len(b), "sha256": sha(b)} for p, b in sorted(files.items())]}
    files["DOCUMENTATION.json"] = encoded(metadata)
    check_files(files)
    destination.mkdir(parents=True, exist_ok=False)
    for name, data in files.items():
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as handle:
            handle.write(data)
    return {"status": "bundled", "version": VERSION, "members": len(files), "destination": str(destination)}


def check_files(files):
    if json.loads(files.get("DOCUMENTATION.json", b"{}")).get("kind") == "stdo.installed-documentation/2":
        return current().check_files(files)
    require(set(files) == MEMBERS, "required documentation member set differs")
    metadata = json.loads(files["DOCUMENTATION.json"])
    require(metadata["kind"] == "stdo.installed-documentation/1"
            and metadata["distribution_version"] == VERSION and metadata["role"] == "non-normative-documentation"
            and metadata["entrypoint"] == "index.html", "documentation distribution contract differs")
    require(metadata["source"] == {"identity": SOURCE_ID, "commit": SOURCE_COMMIT,
            "standing": "historical-common-proposal", "model_identity": MODEL_ID,
            "model_sha256": MODEL_SHA256, "viewer_sha256": VIEWER_SHA256}, "source identity contradicts selection")
    expected = [{"path": p, "bytes": len(b), "sha256": sha(b)} for p, b in sorted(files.items()) if p != "DOCUMENTATION.json"]
    require(metadata["members"] == expected, "documentation member bytes differ")
    viewer_data(files["constraint-explorer/index.html"])
    require(sha(files["code-explorer/index.html"]) == CODE_SHA256 and
            metadata.get("code_example") == {"subject": "ABIogenesis T-019 canonicalization", "viewer_sha256": CODE_SHA256},
            "code viewer differs from reviewed artifact")
    proof_checker().check_payload({p[len("proofs/"):]: raw for p, raw in files.items() if p.startswith("proofs/")})
    # Navigation and historical/current-source distinctions are controlled content.
    require(files["index.html"] == landing() and files["README.md"] == guide(), "documentation entry or guide differs")
    return {"status": "checked", "version": VERSION, "members": len(files), "viewer_sha256": VIEWER_SHA256}


def check_payload(payload):
    package_tools = package_checker()
    files = {p[len(DOC_ROOT):]: b for p, b in payload.items() if p.startswith(DOC_ROOT)}
    result = check_files(files)
    required = {DOC_ROOT + name for name in ("index.html", "README.md", "constraint-explorer/index.html")}
    getting_started = "plugins/spec/references/GETTING_STARTED.md"
    for source in ("standards/README.md", getting_started):
        targets = set()
        # The controlled entry surfaces use inline navigation links. Resource
        # references (images or unused reference definitions) do not qualify.
        visible = package_tools.visible_markdown(payload.get(source, b"").decode())
        visible = re.sub(r"<!--[\s\S]*$", "", visible)  # unfinished comments
        lines = visible.splitlines()
        try:
            for line, reference in package_tools.markdown_references(visible):
                inline = r"(?<![!\\])\[[^\]\\\n]+\]\(\s*" + re.escape(reference) + r"\s*\)"
                if not re.search(inline, lines[line - 1]):
                    continue
                target = package_tools.local_target(source, reference)
                if target is not None:
                    targets.add(target[0])
        except package_tools.CheckError as exc:
            raise ValueError(f"invalid documentation route in {source}: {exc}") from exc
        require(required <= targets and required <= payload.keys(),
                f"required documentation links missing or misdirected in {source}")
    text = payload[getting_started].decode()
    commands = re.findall(r"(?m)^stdo resolve (stdo://\S+/standards/documentation/index\.html)\s*$", text)
    require(commands == [f"stdo://releases/v{result['version']}/standards/documentation/index.html"],
            "Getting Started documentation command selects a different release")
    return result


def check(root):
    root = Path(root)
    paths = sorted(root.rglob("*"))
    require(not any(p.is_symlink() for p in paths), "redirected package member")
    return check_payload({p.relative_to(root).as_posix(): p.read_bytes() for p in paths if p.is_file()})


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    b = commands.add_parser("bundle")
    b.add_argument("--viewer", type=Path, required=True)
    b.add_argument("--destination", type=Path, required=True)
    b.add_argument("--code-viewer", type=Path, required=True)
    b.add_argument("--proofs", type=Path, required=True)
    n = commands.add_parser("bundle-current")
    n.add_argument("--repository", type=Path, required=True)
    n.add_argument("--selection", type=Path, required=True)
    n.add_argument("--selection-sha256", required=True)
    n.add_argument("--destination", type=Path, required=True)
    c = commands.add_parser("check")
    c.add_argument("root", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "bundle-current":
            result = current().build(args.repository, args.selection, args.selection_sha256, args.destination)
        else:
            result = bundle(args.viewer, args.destination, args.code_viewer, args.proofs) if args.command == "bundle" else check(args.root)
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
