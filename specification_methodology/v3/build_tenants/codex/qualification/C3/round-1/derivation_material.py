"""Build and check the selected successor's self-contained derivation evidence.

This is qualification tooling, not an installed admission engine. Verification
reads only a supplied package and basis/manifest bytes. Its historical addresses
are resolved as data; no predecessor directory or network resolver is available.
"""
import argparse
from collections import Counter
import copy
import difflib
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unicodedata


RESOURCE = "standards/verification_material/DERIVATION_SOURCES.json"
CALCULUS = "standards/AXIOMATIC_CALCULUS.md"
PROFILE = "standards/TRAVERSAL_OCCURRENCE_PROFILE.md"
BUILDER_SHA = "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782"
ADDRESS_RULE = {
    "kind": "markdown-atx-heading-addresses", "schema_version": 1,
    "heading_levels": "1 through 6, outside fenced code",
    "normalization": "remove HTML tags and backticks; NFC; lowercase",
    "slug": "remove characters outside Unicode word, hyphen and whitespace; replace each whitespace with hyphen",
    "duplicate_slug": "append ordinal -1, -2, ...; retain each occurrence",
    "explicit_anchor": "HTML a id or name also contributes one address",
    "resolution": "the requested address occurs exactly once",
}
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
    # Consume every inline address in the selected section, or refuse it. There
    # is no filename/fragment character filter that silently drops a new link.
    addresses = re.findall(r"\]\(([^\n)]+)\)", body)
    fail_if(not addresses or body.count("](") != len(addresses) or
            re.search(r"\]\s*\[|^\s*\[[^]]+\]:", body, re.M),
            "unsupported derivation address syntax")
    for address in addresses:
        parts = address.split("#")
        fail_if(len(parts) != 2 or not parts[0].endswith(".md") or not parts[1] or
                "/" in parts[0] or parts[0] in {".md", "..md"} or
                any(c.isspace() for c in address), "unsupported derivation address")
    return sorted({release + "standards/" + a for a in addresses},
                  key=lambda a: a.encode("utf-16-be"))


def heading_addresses(text):
    found = Counter(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))
    counts = Counter()
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                fence = (marker[1][0], len(marker[1]))
            elif marker[1][0] == fence[0] and len(marker[1]) >= fence[1]:
                fence = None
            continue
        if fence is not None:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            heading = re.sub(r"<[^>]*>", "", match[1]).replace("`", "")
            slug = unicodedata.normalize("NFC", heading).lower()
            slug = re.sub(r"\s", "-", re.sub(r"[^\w\-\s]", "", slug))
            number = counts[slug]
            counts[slug] += 1
            found[slug + ("-%d" % number if number else "")] += 1
    return found


def resolves_once(content, fragment, absent, ambiguous):
    count = heading_addresses(content)[fragment]
    fail_if(count == 0, absent)
    fail_if(count != 1, ambiguous)


def members(manifest):
    declared = manifest["standards"]
    fail_if(declared["member_count"] != len(declared["members"]), "manifest member count")
    stream = "".join("%s  %s/%s\n" % (r["sha256"], declared["source_root"], r["path"])
                     for r in sorted(declared["members"], key=lambda r: r["path"]))
    fail_if(sha(stream.encode()) != declared["member_set_sha256"], "manifest member-set digest")
    result = {}
    for row in manifest["standards"]["members"]:
        name = "standards/" + row["path"]
        fail_if(name in result, "duplicate manifest member")
        result[name] = row["sha256"]
    return result


def read_member(root, name, inventory):
    fail_if(name not in inventory, "uncatalogued publication member: " + name)
    path = root / name
    fail_if(Path(name).is_absolute() or ".." in Path(name).parts or
            any(p.is_symlink() for p in [path] + list(path.parents) if p != root and root in p.parents) or
            root.resolve() not in path.resolve().parents,
            "member escapes publication package")
    fail_if(not path.is_file(), "publication member absent: " + name)
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
              "semantic_address_rule": ADDRESS_RULE,
              "principle_refs": principle_refs, "members": projections}
    path = root / RESOURCE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    return result


def verify(root, manifest_bytes, calculus_basis_bytes, profile_basis_bytes):
    manifest, basis, profile = map(load, [manifest_bytes, calculus_basis_bytes, profile_basis_bytes])
    fail_if(set(basis) != {"kind", "schema_version", "concept_identity", "derivation_basis", "publication_basis"},
            "calculus record shape")
    fail_if(set(profile) != {"kind", "schema_version", "concept_identity", "calculus_basis_identity",
                            "occurrence_signature", "occurrence_signature_sha256", "publication_basis"},
            "profile record shape")
    fail_if(set(basis["derivation_basis"]) != {"release_uri", "manifest_sha256", "principle_refs"},
            "derivation record shape")
    publication_fields = {"release_uri", "manifest_sha256", "member_uri", "member_sha256"}
    fail_if(set(basis["publication_basis"]) != publication_fields or
            set(profile["publication_basis"]) != publication_fields, "publication record shape")
    fail_if(set(profile["occurrence_signature"]) != {"kind", "schema_version", "calculus_basis_identity",
            "calculus_signature_schema_clause_ref", "occurrence_signature_clause_refs", "profile_member_sha256"},
            "signature record shape")
    inventory = members(manifest)
    calculus = read_member(root, CALCULUS, inventory)
    profile_text = read_member(root, PROFILE, inventory).decode()
    material = load(read_member(root, RESOURCE, inventory))
    fail_if(material["kind"] != "stdo.derivation-verification-material" or
            material["schema_version"] != 1, "verification-material kind/version")
    fail_if(material.get("semantic_address_rule") != ADDRESS_RULE, "unsupported semantic address rule")
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
        last_end = 0
        for segment in entry["segments"]:
            if set(segment) == {"literal_utf8"}:
                pieces.append(segment["literal_utf8"].encode())
            else:
                fail_if(set(segment) != {"start_byte", "end_byte"}, "reconstruction segment shape")
                start, end = segment["start_byte"], segment["end_byte"]
                fail_if(type(start) is not int or type(end) is not int or
                        not 0 <= start < end <= len(source), "reconstruction range")
                fail_if(start < last_end, "overlapping or unordered reconstruction ranges")
                last_end = end
                pieces.append(source[start:end])
        content = b"".join(pieces)
        fail_if(sha(content) != old_inventory[name] or
                sha(content) != entry["historical_member_sha256"], "reconstructed historical digest")
        resolved[name] = content
    fail_if(set(resolved) != expected_members, "missing historical verification member")
    resolves_once(calculus.decode(), "core-signature", "missing calculus schema fragment",
                  "ambiguous calculus schema fragment")
    for reference in required:
        name, fragment = reference[len(historical_release):].split("#", 1)
        resolves_once(resolved[name].decode(), fragment, "missing historical fragment",
                      "ambiguous historical fragment")
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
    fail_if(signature["occurrence_signature_clause_refs"] != expected_refs, "profile signature population")
    for fragment in PROFILE_FRAGMENTS:
        resolves_once(profile_text, fragment, "missing profile signature fragment",
                      "ambiguous profile signature fragment")
    fail_if(profile["occurrence_signature_sha256"] != "sha256:" + sha(canonical(signature)) or
            signature["profile_member_sha256"] != "sha256:" + inventory[PROFILE], "profile signature digest")
    pp = profile["publication_basis"]
    fail_if(pp["release_uri"] != release or pp["manifest_sha256"] != "sha256:" + sha(manifest_bytes) or
            pp["member_uri"] != release + PROFILE or
            pp["member_sha256"] != "sha256:" + inventory[PROFILE], "profile publication basis")
    return {"valid": True, "historical_principle_refs_verified": len(required),
            "historical_members_reconstructed": len(resolved),
            "calculus_basis_identity": calculus_id,
            "profile_basis_identity": identity(profile, "traversal-occurrence-profile-basis")}


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
            stream = "".join("%s  %s/%s\n" % (r["sha256"], inventory["source_root"], r["path"])
                             for r in sorted(rows, key=lambda r: r["path"]))
            inventory["member_set_sha256"] = sha(stream.encode())
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
        # Measure data acquisition at the Python audit boundary, rather than
        # asserting a zero count. Warm the one lazy codec before that boundary.
        "codec".encode("utf-16-be")
        observed = {"active": False, "data_reads": [], "network_events": []}

        def audit(event, args):
            if not observed["active"]:
                return
            if event == "open" and isinstance(args[0], (str, bytes)):
                path = Path(args[0]).resolve()
                fail_if(cold.resolve() not in path.parents, "verification read outside supplied package")
                observed["data_reads"].append(str(path.relative_to(cold.resolve())))
            elif event.startswith("socket."):
                observed["network_events"].append(event)
                raise ValueError("verification attempted network access")

        sys.addaudithook(audit)
        observed["active"] = True
        try:
            positive = verify(cold, manifest, basis, profile)
        finally:
            observed["active"] = False
        positive["observed_acquisition"] = {
            "boundary": "Python audit open/socket events during verify; interpreter and fixture setup excluded",
            "package_data_reads": observed["data_reads"],
            "outside_package_reads": 0,
            "network_events": observed["network_events"],
        }
        resource_path = cold / RESOURCE
        original = resource_path.read_bytes()
        controls = []

        def refused(label, expected, mb=manifest, bb=basis, pb=profile):
            try:
                verify(cold, mb, bb, pb)
            except (ValueError, KeyError, FileNotFoundError, TypeError, UnicodeError) as error:
                if str(error) != expected:
                    raise AssertionError("wrong refusal for %s: expected %r, got %r" %
                                         (label, expected, str(error))) from error
                controls.append({"case": label, "refused": True, "expected_reason": expected,
                                 "reason": str(error)})
            else:
                raise RuntimeError("negative accepted: " + label)

        resource_path.unlink()
        refused("verification resource absent; original cut unavailable", "publication member absent: " + RESOURCE)
        resource_path.write_bytes(original + b" ")
        refused("resource differs from publication digest", "publication member digest: " + RESOURCE)
        resource_path.write_bytes(original)
        damaged = load(original)
        damaged["members"].pop()
        resource_path.write_text(json.dumps(damaged))
        mb, bb, pb = fixture(cold)
        refused("missing historical member under coherent publication pins", "missing historical verification member", mb, bb, pb)
        resource_path.write_bytes(original)
        damaged = load(original)
        segment = next(s for m in damaged["members"] for s in m["segments"] if "start_byte" in s)
        segment["end_byte"] -= 1
        resource_path.write_text(json.dumps(damaged))
        mb, bb, pb = fixture(cold)
        refused("wrong reconstruction under coherent publication pins", "reconstructed historical digest", mb, bb, pb)
        resource_path.write_bytes(original)
        damaged = load(basis)
        damaged["derivation_basis"]["principle_refs"] = damaged["derivation_basis"]["principle_refs"][:-1]
        refused("incomplete declared principle population", "incomplete or invented principle refs", bb=canonical(damaged))
        damaged = load(basis)
        damaged["derivation_basis"]["manifest_sha256"] = "sha256:" + "0" * 64
        refused("historical digest substituted", "historical manifest digest", bb=canonical(damaged))
        damaged = load(profile)
        damaged["occurrence_signature"]["calculus_basis_identity"] = "urn:stdo:wrong-calculus"
        refused("profile imports another calculus identity", "profile calculus binding", pb=canonical(damaged))
        damaged = load(basis)
        damaged["unowned_field"] = "extra"
        refused("extra calculus record field", "calculus record shape", bb=canonical(damaged))
        original_calculus = (cold / CALCULUS).read_bytes()
        (cold / CALCULUS).write_bytes(original_calculus.replace(b"## Core Signature\n", b"## Missing Schema\n"))
        mb, bb, pb = fixture(cold)
        refused("schema clause absent under coherent publication pins", "missing calculus schema fragment", mb, bb, pb)
        (cold / CALCULUS).write_bytes(original_calculus)

        def damaged_material(label, expected, change):
            material = load(original)
            change(material)
            resource_path.write_text(json.dumps(material))
            mb, bb, pb = fixture(cold)
            refused(label, expected, mb, bb, pb)
            resource_path.write_bytes(original)

        damaged_material("semantic-address rule absent", "unsupported semantic address rule",
                         lambda m: m.pop("semantic_address_rule"))
        damaged_material("duplicate historical member", "duplicate or extra historical member",
                         lambda m: m["members"].append(copy.deepcopy(m["members"][0])))
        damaged_material("duplicate byte range", "overlapping or unordered reconstruction ranges",
                         lambda m: m["members"][0]["segments"].insert(1, copy.deepcopy(m["members"][0]["segments"][0])))
        damaged_material("out-of-order byte ranges", "overlapping or unordered reconstruction ranges",
                         lambda m: m["members"][0]["segments"].reverse())
        damaged_material("unbound literal reconstruction bytes", "reconstructed historical digest",
                         lambda m: m["members"][0]["segments"].append({"literal_utf8": "altered"}))
        damaged_material("source pin differs from published member", "reconstruction source pin",
                         lambda m: m["members"][0].update(source_member_sha256="0" * 64))
        damaged_material("relative path escape", "uncatalogued publication member: ../outside.md",
                         lambda m: m["members"][0].update(source_member="../outside.md"))

        profile_path = cold / PROFILE
        original_profile = profile_path.read_bytes()
        profile_path.write_bytes(original_profile + b'\n<a id="occurrence-identity"></a>\n')
        mb, bb, pb = fixture(cold)
        refused("duplicate semantic address under coherent publication pins", "ambiguous profile signature fragment", mb, bb, pb)
        profile_path.write_bytes(original_profile)

        first = load(original)["members"][0]["source_member"]
        member_path = cold / first
        source_bytes = member_path.read_bytes()
        external = cold.parent / "outside.md"
        external.write_bytes(source_bytes)
        member_path.unlink()
        member_path.symlink_to(external)
        refused("member symlink outside publication", "member escapes publication package")
        member_path.unlink()
        member_path.write_bytes(source_bytes)

        # An authentic historical member lacks this substituted fragment, even
        # after every current publication pin and reference list is refreshed.
        old_target = b"IDENTITY_METHOD.md#core-law"
        calculus_path = cold / CALCULUS
        calculus_path.write_bytes(original_calculus.replace(old_target, b"IDENTITY_METHOD.md#missing-historical-clause"))
        material = load(original)
        material["principle_refs"] = refs(calculus_path.read_bytes(), material["historical_release_uri"])
        resource_path.write_text(json.dumps(material))
        mb, bb, pb = fixture(cold)
        refused("missing authentic historical fragment under coherent pins", "missing historical fragment", mb, bb, pb)
        resource_path.write_bytes(original)
        calculus_path.write_bytes(original_calculus)

        wider = refs(b"## Derivation Provenance\n[X](METHOD2.md#clause_2)\n", "stdo://releases/v0.0.0-rc.2/")
        fail_if(wider != ["stdo://releases/v0.0.0-rc.2/standards/METHOD2.md#clause_2"],
                "derivation address silently omitted")
        literal_bytes = sum(len(s["literal_utf8"].encode()) for m in load(original)["members"]
                            for s in m["segments"] if "literal_utf8" in s)
        return {"kind": "bounded_derivation_verification_check", "positive": positive,
                "negative_controls": controls, "valid": all(c["refused"] for c in controls),
                "resource_bytes": len(original), "literal_reconstruction_bytes": literal_bytes,
                "address_population_guard": "digit/underscore address retained; unsupported syntax refuses",
                "limits": ["Hypothetical schema-valid publication fixture, not an issued release",
                           "Content/reference verification, not independent derivation or acceptance",
                           "Canonical checker limited to string/integer identity records",
                           "Publication member-set stream follows the installed manifest recipe",
                           "Identity verification is qualification tooling, not a native installed admission engine"]}


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
