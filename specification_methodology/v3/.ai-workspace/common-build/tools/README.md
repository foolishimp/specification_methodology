# Common package tooling

This tooling implements the mechanical G1–G5 and A3 construction contributions under [T-003](../../tickets/active/T-003-COMMON-standalone-v3-construction.md). It stays outside the delivered V3 package. It does not confer semantic qualification, acceptance, release or installation.

`package_tools.py` is one standalone standard-library program. It accepts an explicit package root and works from an unrelated working directory. It neither imports nor executes candidate code or project helpers. Use Python 3.11 or later; the recorded controls identify the actual interpreter tested.

## Trusted invocation

The trusted base is the selected Python executable and its standard library, plus the short inline launcher below. Obtain the checker's SHA256 from an already selected construction checkpoint or its independently trusted return. Do not compute the expected pin from an unchecked local copy immediately before running it: that detects no tampering.

Run this launcher with `-I -S` so the working directory, `PYTHONPATH`, user packages and site customizations cannot supply initial imports. The launcher authenticates the complete checker bytes before compiling or executing any of them. The checker has no project helper closure beyond that single authenticated file. This arrangement does not authenticate the interpreter or the separately selected installed verifier; those are explicit development-tool dependencies.

```sh
python3 -I -S -c 'import hashlib, pathlib, sys
p = pathlib.Path(sys.argv[1])
b = p.read_bytes()
if hashlib.sha256(b).hexdigest() != sys.argv[2]:
    raise SystemExit("checker digest mismatch before execution")
sys.argv = [str(p)] + sys.argv[3:]
exec(compile(b, str(p), "exec"), {"__name__": "__main__", "__file__": str(p), "__authenticated_checker_sha256__": hashlib.sha256(b).hexdigest()})
' /absolute/path/package_tools.py SELECTED_CHECKER_SHA256 check \
  --root /absolute/path/common \
  --inventory /absolute/path/common-freeze.json \
  --inventory-sha256 SELECTED_INVENTORY_SHA256 \
  --report /absolute/path/package-check.json
```

The output reports whether that authenticated launcher was used. Calling the script directly is supported for development but does not attest pre-execution checker authentication. A checker cannot establish its own trust by hashing itself after execution starts.

## Commands

The following are arguments to the authenticated checker invocation, following the checker path and selected checker pin above. Every output must be outside the candidate. Existing inventories, reports and destinations are never overwritten.

```text
freeze --root PACKAGE --inventory NEW_INVENTORY_JSON
check --root PACKAGE --inventory INVENTORY_JSON --inventory-sha256 SHA256 [--report NEW_REPORT_JSON]
materialize --root PACKAGE --inventory INVENTORY_JSON --inventory-sha256 SHA256 \
  --coordinates COORDINATES_JSON --coordinates-sha256 SHA256 \
  --destination NEW_DIRECTORY [--report NEW_REPORT_JSON]
```

`freeze` captures all regular files, bytes, per-file SHA256 and complete directory membership. It is an identity capture, not a review or successful check. The inventory itself must subsequently be selected by an external exact SHA256. No label-only or coordinate exception is implicit. Any intended change receives a new reviewed freeze.

`check` verifies the supplied inventory pin before consuming it. It requires complete membership and exact member bytes, parses every JSON member (rejecting duplicate keys and non-JSON constants), checks declared references, applies the publication policy, and exposes all advisory signals. File, broken and directory symlinks, a symlink package root and special filesystem entries fail explicitly. Case-folded and Unicode-normalized duplicate path identities fail. Ordinary empty directories are inventoried; materialization rejects them because the installed manifest cannot represent them.

Exit status is `0` for the command's declared checks passing, `1` for reported check failures, and `2` for invalid inputs or an operational failure. Reports distinguish mechanical validity from method qualification. A refused materialization may leave no destination; an I/O failure during copying can leave an explicitly unsuccessful partial destination. It is never selected or installed automatically.

## Publication and reference policy

The inventory selects `standalone-v3-publication-1`. This policy rejects concrete prior-version routes, construction-history paths and stale construction/version headers. Examples include `stdo://releases/v2...`, author comparison or common-build records in `.ai-workspace/`, donor tenant paths, `qualification/C3/`, `a_c/iN/`, and a normative entry headed `RC9` or `Status: under construction`. Header checks are not applied to starter templates. Fenced examples are not live routes. Ordinary Author/Date/Status template fields, generic `.ai-workspace/tickets/` carrier declarations, attribution, and generic method rules about historical evidence, revisions and predecessors remain lawful. Semantic inspection must still establish that no dependency on earlier work survives; lexical checking is bounded evidence.

Local reference checks cover Markdown inline, full/collapsed/defined shortcut, HTML and file autolinks outside code examples. They resolve relative paths and anchors, including percent-encoded traversal, duplicate Markdown heading IDs, explicit HTML IDs and JSON pointers. JSON `$ref` values, explicit `standards/` or `plugins/` routes, and non-template path-shaped `path`, `owner`, `uri`, `source`, `file`, `member` and `href` fields are checked. Template-generated project paths are not candidate dependencies. External citations and explicit placeholders are listed in the report; their contents and availability are not verified. Plain prose, unlinked code-formatted filenames, custom Markdown extensions, generated-project routes, JSON-schema conformance and frame-excerpt fidelity require their separate review or checks.

Retired owner filenames and phrases such as “complete Product view” are advisory signals. They are visible in every check report and never silently converted into semantic failures or edit authority. Whitespace is not a qualification gate.

## Explicit materialization coordinates

Materialization uses the same authenticated in-memory package bytes that passed the complete check. It copies every package member unchanged at the same path and adds the canonical installed manifest. It refuses all files outside `standards/**`, `plugins/spec/**`, `LICENSE` and `release/release-note.md`; nothing is silently omitted or relocated. The package entry is `standards/README.md`.

Supply a JSON object with exactly these keys. Replace every bracketed identity before invoking the command; no tag or commit is created or asserted to exist by this tool.

```json
{
  "release": {
    "cut": "<explicit-v3-RC-coordinate>",
    "tag_object": "<explicit-Git-object-id>",
    "commit": "<explicit-Git-object-id>",
    "tree": "<explicit-Git-object-id>",
    "standards_tree": "<explicit-Git-object-id>",
    "project_release_namespace": "specification_methodology",
    "qualified_ref": "refs/tags/specification_methodology/<same-explicit-v3-RC-coordinate>",
    "project_subtree_root": "specification_methodology/v3",
    "project_subtree_tree": "<explicit-Git-object-id>"
  },
  "release_note": {
    "package_path": "release/release-note.md",
    "source_path": "releases/<version-without-RC-suffix>.md",
    "installed_path": "release/release-note.md"
  }
}
```

The namespace and subtree are explicit compatibility constraints of the installed STDO verifier, not donor-specific defaults. The cut, object identities and qualified ref have no defaults. The prospective release-note source path must agree with the cut. The supplied coordinates are separately pinned by SHA256. Until a release-shaped staging commit and exact source selection exist, they are declared staging inputs rather than authenticated release facts.

The standards aggregate hashes the UTF-8 bytes of sorted lines:

```text
<member SHA256>  specification/standards/<member-relative path>\n
```

There are exactly two spaces between the digest and path and one LF after each line. Canonical manifest JSON matches the installed toolchain's sorted, indented, ASCII-escaped serialization with a final LF. A digest over `standards/<path>` is incompatible and the negative control proves the installed verifier rejects it.

## Installed verifier boundary

After materialization, use the explicitly selected toolchain interpreter to call `stdo_toolchain.manifest.verify_materialization` over that isolated directory and its manifest. This reads and verifies the materialized files; it is not `stdo install` and does not alter the install registry, selectors, release trees, tags or remotes. A future actual install needs the release-shaped source layout and source-object attestation that this tool does not provide.

```sh
/absolute/path/to/selected-toolchain/python -I -c 'import json, sys
from pathlib import Path
from stdo_toolchain.manifest import verify_materialization
p = Path(sys.argv[1])
failures = verify_materialization(p, json.loads((p / "manifest.json").read_bytes()))
print(json.dumps({"valid": not failures, "failures": failures}))
raise SystemExit(bool(failures))
' /absolute/path/materialized-package
```

The fixture tests exercise the actual installed toolchain's verifier and canonical JSON implementation with deliberately fictional, documented staging coordinates. They establish compatible package mechanics, not a selected V3 release identity.

## Targeted controls

```sh
python3 -I -m unittest discover -s /absolute/path/tools/tests -v
```

The controls test unchanged input; one-byte mutation; member addition/removal/duplication; empty directories; pinned-inventory tampering; every symlink kind; invalid/duplicate JSON; escaping, missing and malformed references; header and route metadata; preservation of legitimate templates, generic predecessor law and external attribution; visible nonblocking advisories; rejected donor coordinates; complete unchanged materialization; and the canonical standards digest against the installed verifier. A modified checker containing an attempted side effect is rejected by the launcher before the side effect executes. A local module cannot shadow the initial standard-library imports.

The bounded Writer's durable return and test receipt are in `../returns/package-tools.json`, `../returns/package-tools.md` and `../returns/package-tests.json`. These are authored construction evidence. Independent review and the integrated candidate freeze remain separate work.
