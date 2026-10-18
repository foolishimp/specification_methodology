"""Independent bounded manifest/bootstrap readback; no repository mutations.

Run with a Python providing jsonschema:
  python -B package_probe.py /path/to/specification_methodology

Only Git objects named below are read. Materialization uses an automatically
removed fresh temporary directory. No shared installed release is changed.
This checks admitted inputs and a schema specimen, not native toolchain use,
semantic sufficiency, release eligibility or owner acceptance.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import jsonschema

REPO = Path(sys.argv[1]).resolve()
A = "4a63c9293ddaa568803b81f1ed5dcc1d3dc19cec"
B = "a85f9ec98e43b942048a6c151aafd9662d2def90"
PREFIX = "specification_methodology/v3/build_tenants/claude/"


def git(*args):
    return subprocess.check_output(["git", "-C", str(REPO), *args])


def blob(path, commit=A):
    return git("show", commit + ":" + PREFIX + path)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, description):
    if not condition:
        raise AssertionError(description)


manifest_bytes = blob("release/manifest.json", B)
manifest = json.loads(manifest_bytes)
release = manifest["release"]
require(release["commit"] == A, "manifest source")
for key, ref in (
    ("tree", A + "^{tree}"),
    ("standards_tree", A + ":" + PREFIX + "standards"),
    ("project_subtree_tree", A + ":" + PREFIX.rstrip("/")),
):
    require(git("rev-parse", ref).decode().strip() == release[key], key)
require(git("cat-file", "-t", release["tag_object"]).decode().strip() == "tag", "annotated tag object")
require(git("rev-parse", release["qualified_ref"]).decode().strip() == release["tag_object"], "qualified ref names recorded object")
require(git("rev-parse", release["tag_object"] + "^{}").decode().strip() == A,
        "recorded tag peels to candidate")
require(not git("diff", "--name-only", A, B, "--", *(
    PREFIX + path for path in ("standards", "plugins", "a_c")
)), "published subject unchanged between source and records")

with tempfile.TemporaryDirectory(prefix="claude-rc5-independent-") as tmp:
    root = Path(tmp).resolve()
    verified = []

    def materialize(source, destination, digest):
        value = blob(source)
        require(sha(value) == digest, "member digest: " + source)
        target = root / destination
        require(target.resolve().is_relative_to(root), "member stays inside scratch")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(value)
        verified.append(destination)

    for label, group, source_root in (
        ("standards", manifest["standards"], "standards"),
        ("plugin", manifest["auxiliary"]["plugin"], "plugins/spec"),
    ):
        members = group["members"]
        require(len(members) == group["member_count"], label + " count")
        names = [m["path"] for m in members]
        require(len(names) == len(set(names)), label + " unique paths")
        source_names = git("ls-tree", "-r", "--name-only", A, "--",
                           PREFIX + source_root).decode().splitlines()
        require(set(names) == {p[len(PREFIX + source_root) + 1:] for p in source_names},
                label + " complete source inventory")
        for member in members:
            materialize(source_root + "/" + member["path"],
                        group["installed_root"] + "/" + member["path"], member["sha256"])
    std = manifest["standards"]
    calculated_set = sha("".join(
        m["sha256"] + "  " + m["path"] + "\n"
        for m in sorted(std["members"], key=lambda m: m["path"])
    ).encode())
    require(calculated_set == std["member_set_sha256"], "standards member-set digest")
    license_record = manifest["auxiliary"]["license"]
    materialize(license_record["path"], "LICENSE", license_record["sha256"])
    note = manifest["auxiliary"]["release_note"]
    materialize("release/release-note.md", note["installed_path"], note["sha256"])
    schema = json.loads((root / "standards/schemas/installed-release-manifest.schema.json").read_bytes())
    jsonschema.validators.validator_for(schema)(schema).validate(manifest)

    # From here the bootstrap specimen uses only materialized package bytes.
    fixture = json.loads((root / "standards/templates/PRODUCT_DEFINITION_TEMPLATE.json").read_bytes())
    replacements = {
        "REPLACE_WITH_IMMUTABLE_CUT": release["cut"],
        "REPLACE_WITH_VERSION_LINE": "v3",
        "REPLACE_WITH_64_LOWERCASE_HEX_SHA256": sha(manifest_bytes),
        "replace-me": "independent-bootstrap-specimen",
        "Replace Me": "Independent Bootstrap Specimen",
        "replace-with-reference-frame-authority": "reference-frame-authority",
    }
    value = json.dumps(fixture)
    for old, new in replacements.items():
        value = value.replace(old, new)
    fixture = json.loads(value)
    fixture["local_constitution"]["disambiguations"] = []
    require("REPLACE_WITH" not in json.dumps(fixture) and "replace-with" not in json.dumps(fixture),
            "all specimen placeholders resolved")
    product_schema = json.loads((root / "standards/schemas/product-definition.schema.json").read_bytes())
    validator = jsonschema.validators.validator_for(product_schema)
    validator.check_schema(product_schema)
    validator(product_schema).validate(fixture)
    entrypoints = [entry["uri"] for entry in fixture["constitution"]["entrypoints"]]
    require(all((root / entry).is_file() for entry in entrypoints), "all specimen entrypoints admitted")
    program = json.loads(blob("a_c/i3/axiomatic-program.json"))
    current_interpretation = {
        "clauses": len(program["clauses"]),
        "frame_indexes": len(program["frame_indexes"]),
        "residuals": len(program["residuals"]),
        "calculus_ref": program["calculus_ref"],
        "source_basis": program["source_basis"],
    }
    print(json.dumps({
        "candidate": A, "recording_commit": B,
        "manifest_sha256": sha(manifest_bytes),
        "verified_member_count": len(verified),
        "standards_count": std["member_count"],
        "plugin_count": manifest["auxiliary"]["plugin"]["member_count"],
        "standards_member_set_sha256": calculated_set,
        "manifest_schema": "valid", "product_definition_specimen_schema": "valid",
        "template_entrypoints": entrypoints,
        "source_to_records_standards_plugins_a_c": "unchanged",
        "interpretation_inventory": current_interpretation,
        "limits": ["No installer or host activation was run", "Specimen is schema-valid, not an accepted Product",
                   "No semantic a_c fidelity inference", "No publication or release acceptance"],
    }, indent=2))
