"""Build and check the selected successor's self-contained derivation evidence.

This is qualification tooling, not an installed admission engine. Verification
reads only a supplied package and basis/manifest bytes. Its historical addresses
are resolved as data; no predecessor directory or network resolver is available.
"""
import argparse
import copy
import difflib
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile


RESOURCE = "standards/verification_material/DERIVATION_SOURCES.json"
CALCULUS = "standards/AXIOMATIC_CALCULUS.md"
PROFILE = "standards/TRAVERSAL_OCCURRENCE_PROFILE.md"
BUILDER_SHA = "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782"
PROFILE_FRAGMENTS = [
    "authority-and-adoption", "candidate-judgment-event-and-relation-separation",
    "causality-and-typed-lineage", "closed-constraint-judgment-residual-and-stop-kinds",
    "closed-event-kind-population", "closed-relation-families",
    "closed-semantic-object-sorts", "event-frontier-and-projection",
    "mutable-subject-effect-relation", "occurrence-identity",
]


def sha(value):
    return hashlib.sha256(value).hexdigest()


def fail_if(condition, message):
    if condition:
        raise ValueError(message)


def pairs(items):
    result = {}
    for key, value in items:
        fail_if(key in result, "duplicate JSON name")
        result[key] = value
    return result


def load(value):
    return json.loads(value, object_pairs_hook=pairs)


def canonical(value):
    # The selected identity records use strings and exact small integer fields;
    # floats and non-I-JSON surrogates are outside this bounded checker domain.
    if isinstance(value, dict):
        return b"{" + b",".join(canonical(k) + b":" + canonical(value[k])
                for k in sorted(value, key=lambda k: k.encode("utf-16-be"))) + b"}"
    if isinstance(value, list):
        return b"[" + b",".join(canonical(v) for v in value) + b"]"
    if isinstance(value, str):
        value.encode("utf-8")
        return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode()
    fail_if(type(value) is not int or abs(value) > 9007199254740991,
            "unsupported canonical field")
    return str(value).encode()


def identity(record, kind):
    return "urn:stdo:" + kind + ":sha256:" + sha(canonical(record))


def section(text, heading):
    start = text.index("## " + heading + "\n")
    end = text.find("\n## ", start + 3)
    return text[start:end if end >= 0 else len(text)]


def refs(calculus, release):
    body = section(calculus.decode(), "Derivation Provenance")
    addresses = re.findall(r"\]\(([A-Z_]+\.md#[a-z0-9-]+)\)", body)
    return sorted({release + "standards/" + a for a in addresses},
                  key=lambda a: a.encode("utf-16-be"))


def members(manifest):
    result = {}
    for row in manifest["standards"]["members"]:
        name = "standards/" + row["path"]
        fail_if(name in result, "duplicate manifest member")
        result[name] = row["sha256"]
    return result


def read_member(root, name, inventory):
    fail_if(name not in inventory, "uncatalogued publication member: " + name)
    path = root / name
    fail_if(path.is_symlink() or root.resolve() not in path.resolve().parents,
            "member escapes publication package")
    content = path.read_bytes()
    fail_if(sha(content) != inventory[name], "publication member digest: " + name)
    return content


def build(root, historical):
    manifest_bytes = (historical / "manifest.json").read_bytes()
    fail_if(sha(manifest_bytes) != BUILDER_SHA, "unverified builder manifest")
    manifest = load(manifest_bytes)
    release = "stdo://releases/" + manifest["release"]["cut"] + "/"
    principle_refs = refs((root / CALCULUS).read_bytes(), release)
    old_inventory = members(manifest)
    projections = []
    for name in sorted({r[len(release):].split("#")[0] for r in principle_refs}):
        old = (historical / name).read_bytes()
        fail_if(sha(old) != old_inventory[name], "historical member digest")
        current = (root / name).read_bytes()
        old_lines, new_lines = old.splitlines(keepends=True), current.splitlines(keepends=True)
        offsets = [0]
        for line in new_lines:
            offsets.append(offsets[-1] + len(line))
        segments = []
        for tag, a, b, c, d in difflib.SequenceMatcher(
                None, old_lines, new_lines, autojunk=False).get_opcodes():
            if tag == "equal":
                segments.append({"start_byte": offsets[c], "end_byte": offsets[d]})
            elif tag in {"delete", "replace"}:
                segments.append({"literal_utf8": b"".join(old_lines[a:b]).decode()})
        projections.append({"historical_member": name,
                            "historical_member_sha256": old_inventory[name],
                            "source_member": name, "source_member_sha256": sha(current),
                            "segments": segments})
    result = {"kind": "stdo.derivation-verification-material", "schema_version": 1,
              "historical_release_uri": release,
              "historical_manifest_sha256": BUILDER_SHA,
              "historical_manifest_utf8": manifest_bytes.decode(),
              "principle_refs": principle_refs, "members": projections}
    path = root / RESOURCE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    return result


def verify(root, manifest_bytes, calculus_basis_bytes, profile_basis_bytes):
    manifest, basis, profile = map(load, [manifest_bytes, calculus_basis_bytes, profile_basis_bytes])
    inventory = members(manifest)
    calculus = read_member(root, CALCULUS, inventory)
    profile_text = read_member(root, PROFILE, inventory).decode()
    material = load(read_member(root, RESOURCE, inventory))
    fail_if(material["kind"] != "stdo.derivation-verification-material" or
            material["schema_version"] != 1, "verification-material kind/version")
    publication = basis["publication_basis"]
    release = publication["release_uri"]
    fail_if(not re.fullmatch(r"stdo://releases/v\d+\.\d+\.\d+-rc\.[1-9]\d*/", release),
            "publication release URI")
    fail_if(manifest["release"]["cut"] != release.split("/")[-2], "publication cut")
    fail_if(publication["manifest_sha256"] != "sha256:" + sha(manifest_bytes) or
            publication["member_uri"] != release + CALCULUS or
            publication["member_sha256"] != "sha256:" + sha(calculus), "calculus publication basis")
    fail_if(basis["kind"] != "stdo.axiomatic-calculus-basis" or
            basis["schema_version"] != 1 or
            basis["concept_identity"] != "urn:stdo:concept:axiomatic-calculus:a-c",
            "calculus kind/version/concept")
    derivation = basis["derivation_basis"]
    historical_release = derivation["release_uri"]
    fail_if(historical_release == release or historical_release != material["historical_release_uri"],
            "same-carrier or inconsistent derivation")
    historical_bytes = material["historical_manifest_utf8"].encode()
    fail_if(sha(historical_bytes) != material["historical_manifest_sha256"] or
            derivation["manifest_sha256"] != "sha256:" + sha(historical_bytes),
            "historical manifest digest")
    historical_manifest = load(historical_bytes)
    fail_if(historical_release != "stdo://releases/" + historical_manifest["release"]["cut"] + "/",
            "historical manifest cut")
    required = refs(calculus, historical_release)
    fail_if(not required or derivation["principle_refs"] != required or
            material["principle_refs"] != required, "incomplete or invented principle refs")
    old_inventory = members(historical_manifest)
    expected_members = {r[len(historical_release):].split("#")[0] for r in required}
    resolved = {}
    for entry in material["members"]:
        name = entry["historical_member"]
        fail_if(name in resolved or name not in expected_members, "duplicate or extra historical member")
        source = read_member(root, entry["source_member"], inventory)
        fail_if(sha(source) != entry["source_member_sha256"], "reconstruction source pin")
        pieces = []
        for segment in entry["segments"]:
            if set(segment) == {"literal_utf8"}:
                pieces.append(segment["literal_utf8"].encode())
            else:
                fail_if(set(segment) != {"start_byte", "end_byte"}, "reconstruction segment shape")
                start, end = segment["start_byte"], segment["end_byte"]
                fail_if(type(start) is not int or type(end) is not int or
                        not 0 <= start <= end <= len(source), "reconstruction range")
                pieces.append(source[start:end])
        content = b"".join(pieces)
        fail_if(sha(content) != old_inventory[name] or
                sha(content) != entry["historical_member_sha256"], "reconstructed historical digest")
        resolved[name] = content
    fail_if(set(resolved) != expected_members, "missing historical verification member")
    # Use the existing documentary semantic-address rule, not a second slugger.
    from importlib.util import spec_from_file_location, module_from_spec
    checker_path = Path(__file__).parents[1] / "check_candidate.py"
    spec = spec_from_file_location("documentary_check", checker_path)
    checker = module_from_spec(spec)
    spec.loader.exec_module(checker)
    for reference in required:
        name, fragment = reference[len(historical_release):].split("#", 1)
        fail_if(fragment not in checker.anchors(resolved[name].decode()), "missing historical fragment")
    calculus_id = identity(basis, "axiomatic-calculus-basis")
    signature = profile["occurrence_signature"]
    fail_if(profile["kind"] != "stdo.traversal-occurrence-profile-basis" or
            profile["schema_version"] != 1 or
            profile["concept_identity"] != "urn:stdo:concept:traversal-occurrence-profile" or
            profile["calculus_basis_identity"] != calculus_id or
            signature["calculus_basis_identity"] != calculus_id, "profile calculus binding")
    fail_if(signature["kind"] != "stdo.traversal-occurrence-signature" or
            signature["schema_version"] != 1 or
            signature["calculus_signature_schema_clause_ref"] != release + CALCULUS + "#core-signature",
            "signature calculus schema")
    expected_refs = [release + PROFILE + "#" + f for f in PROFILE_FRAGMENTS]
    fail_if(signature["occurrence_signature_clause_refs"] != expected_refs or
            not set(PROFILE_FRAGMENTS) <= checker.anchors(profile_text), "profile signature population")
    fail_if(profile["occurrence_signature_sha256"] != "sha256:" + sha(canonical(signature)) or
            signature["profile_member_sha256"] != "sha256:" + inventory[PROFILE], "profile signature digest")
    pp = profile["publication_basis"]
    fail_if(pp["release_uri"] != release or pp["manifest_sha256"] != "sha256:" + sha(manifest_bytes) or
            pp["member_uri"] != release + PROFILE or
            pp["member_sha256"] != "sha256:" + inventory[PROFILE], "profile publication basis")
    return {"valid": True, "historical_principle_refs_verified": len(required),
            "historical_members_reconstructed": len(resolved),
            "calculus_basis_identity": calculus_id,
            "profile_basis_identity": identity(profile, "traversal-occurrence-profile-basis"),
            "predecessor_or_network_reads": 0}


def fixture(root):
    material = load((root / RESOURCE).read_bytes())
    manifest = load(material["historical_manifest_utf8"])
    release = "stdo://releases/v0.0.0-rc.1/"
    manifest["release"].update(cut="v0.0.0-rc.1", tag_object="0" * 40, commit="0" * 40,
                               tree="0" * 40, standards_tree="0" * 40,
                               qualified_ref="refs/tags/specification_methodology/v0.0.0-rc.1")
    for inventory, folder in [(manifest["standards"], "standards"),
                              (manifest["auxiliary"]["plugin"], "plugins/spec")]:
        rows = [{"path": str(p.relative_to(root / folder)), "sha256": sha(p.read_bytes())}
                for p in sorted((root / folder).rglob("*")) if p.is_file()]
        inventory.update(members=rows, member_count=len(rows))
        if folder == "standards":
            inventory["member_set_sha256"] = sha(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode())
    manifest_bytes = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
    common = {"release_uri": release, "manifest_sha256": "sha256:" + sha(manifest_bytes)}
    basis = {"kind": "stdo.axiomatic-calculus-basis", "schema_version": 1,
             "concept_identity": "urn:stdo:concept:axiomatic-calculus:a-c",
             "derivation_basis": {"release_uri": material["historical_release_uri"],
                                  "manifest_sha256": "sha256:" + material["historical_manifest_sha256"],
                                  "principle_refs": material["principle_refs"]},
             "publication_basis": dict(common, member_uri=release + CALCULUS,
                                       member_sha256="sha256:" + sha((root / CALCULUS).read_bytes()))}
    calculus_id = identity(basis, "axiomatic-calculus-basis")
    signature = {"kind": "stdo.traversal-occurrence-signature", "schema_version": 1,
                 "calculus_basis_identity": calculus_id,
                 "calculus_signature_schema_clause_ref": release + CALCULUS + "#core-signature",
                 "occurrence_signature_clause_refs": [release + PROFILE + "#" + f for f in PROFILE_FRAGMENTS],
                 "profile_member_sha256": "sha256:" + sha((root / PROFILE).read_bytes())}
    profile = {"kind": "stdo.traversal-occurrence-profile-basis", "schema_version": 1,
               "concept_identity": "urn:stdo:concept:traversal-occurrence-profile",
               "calculus_basis_identity": calculus_id, "occurrence_signature": signature,
               "occurrence_signature_sha256": "sha256:" + sha(canonical(signature)),
               "publication_basis": dict(common, member_uri=release + PROFILE,
                                         member_sha256=signature["profile_member_sha256"])}
    return manifest_bytes, canonical(basis), canonical(profile)


def test(root):
    from jsonschema import Draft202012Validator
    with tempfile.TemporaryDirectory(prefix="stdo-codex-identity-") as name:
        cold = Path(name) / "successor"
        shutil.copytree(root, cold)
        manifest, basis, profile = fixture(cold)
        schema = load((cold / "standards/schemas/installed-release-manifest.schema.json").read_bytes())
        Draft202012Validator(schema).validate(load(manifest))
        positive = verify(cold, manifest, basis, profile)
        resource_path = cold / RESOURCE
        original = resource_path.read_bytes()
        controls = []

        def refused(label, mb=manifest, bb=basis, pb=profile):
            try:
                verify(cold, mb, bb, pb)
            except (ValueError, KeyError, FileNotFoundError, TypeError, UnicodeError) as error:
                controls.append({"case": label, "refused": True, "reason": str(error)})
            else:
                raise RuntimeError("negative accepted: " + label)

        resource_path.unlink()
        refused("verification resource absent; original cut unavailable")
        resource_path.write_bytes(original + b" ")
        refused("resource differs from publication digest")
        resource_path.write_bytes(original)
        damaged = load(original)
        damaged["members"].pop()
        resource_path.write_text(json.dumps(damaged))
        mb, bb, pb = fixture(cold)
        refused("missing historical member under coherent publication pins", mb, bb, pb)
        resource_path.write_bytes(original)
        damaged = load(original)
        segment = next(s for m in damaged["members"] for s in m["segments"] if "start_byte" in s)
        segment["end_byte"] -= 1
        resource_path.write_text(json.dumps(damaged))
        mb, bb, pb = fixture(cold)
        refused("wrong reconstruction under coherent publication pins", mb, bb, pb)
        resource_path.write_bytes(original)
        damaged = load(basis)
        damaged["derivation_basis"]["principle_refs"] = damaged["derivation_basis"]["principle_refs"][:-1]
        refused("incomplete declared principle population", bb=canonical(damaged))
        damaged = load(basis)
        damaged["derivation_basis"]["manifest_sha256"] = "sha256:" + "0" * 64
        refused("historical digest substituted", bb=canonical(damaged))
        damaged = load(profile)
        damaged["occurrence_signature"]["calculus_basis_identity"] = "urn:stdo:wrong-calculus"
        refused("profile imports another calculus identity", pb=canonical(damaged))
        return {"kind": "bounded_derivation_verification_check", "positive": positive,
                "negative_controls": controls, "valid": all(c["refused"] for c in controls),
                "resource_bytes": len(original),
                "limits": ["Hypothetical schema-valid publication fixture, not an issued release",
                           "Content/reference verification, not independent derivation or acceptance",
                           "Canonical checker limited to string/integer identity records"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--build-from", type=Path)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[3] / "successor"
    if args.build_from:
        built = build(root, args.build_from)
        print(json.dumps({"principle_refs": len(built["principle_refs"]), "members": len(built["members"]),
                          "literal_reconstruction_bytes": sum(len(s["literal_utf8"].encode())
                           for m in built["members"] for s in m["segments"] if "literal_utf8" in s)}))
    if args.test:
        report = test(root)
        Path(__file__).with_name("IDENTITY_CHECK.json").write_text(json.dumps(report, indent=2) + "\n")
        print(json.dumps(report, indent=2))
