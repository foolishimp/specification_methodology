#!/usr/bin/env python3
"""Read-only package qualification; writes only its report in this directory.

The optional refresh experiment uses an isolated copy below this directory.
Artifact success is not semantic conservation, independent review, acceptance,
an installed release, or proof that a projected frame is sufficient for a task.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unicodedata
from urllib.parse import unquote


HERE = Path(__file__).resolve().parent
SUPPORT = HERE.parent
TENANT = HERE.parents[2]
PACKAGE = TENANT / "successor"
COMMON = TENANT.parents[1] / "specification/requirements/PREDECESSOR_CLAIMS.md"
INSTALLED = Path.home() / "Library/Application Support/STDO/releases/v2.5.1-rc.2"
BUILDER_SHA = "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782"
CHILD = "TRAVERSAL_OCCURRENCE_PROFILE.md#closed-profile-signature-fourteen-members"


def sha_bytes(value):
    return hashlib.sha256(value).hexdigest()


def sha(path):
    return sha_bytes(path.read_bytes())


def json_read(path):
    return json.loads(path.read_text())


def slug(value):
    value = re.sub(r"<[^>]*>", "", value).replace("`", "").lower()
    value = unicodedata.normalize("NFC", value)
    return re.sub(r"\s", "-", re.sub(r"[^\w\-\s]", "", value))


def visible_lines(text):
    """Preserve offsets while excluding fenced and inline code from links."""
    fence = None
    for number, line in enumerate(text.splitlines(keepends=True), 1):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                fence = (marker[1][0], len(marker[1]))
            elif marker[1][0] == fence[0] and len(marker[1]) >= fence[1]:
                fence = None
            yield number, "\n" if line.endswith("\n") else ""
        elif fence is None:
            yield number, re.sub(r"(`+).*?\1", "", line)
        else:
            yield number, "\n" if line.endswith("\n") else ""


def headings(text):
    """ATX headings with source offsets, excluding fenced code."""
    result, counts, offset, fence = [], {}, 0, None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                fence = (marker[1][0], len(marker[1]))
            elif marker[1][0] == fence[0] and len(marker[1]) >= fence[1]:
                fence = None
        elif fence is None:
            match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
            if match:
                key = slug(match[2])
                count = counts.get(key, 0)
                counts[key] = count + 1
                result.append({"level": len(match[1]), "heading": match[2],
                               "anchor": key + ("-" + str(count) if count else ""),
                               "offset": offset})
        offset += len(line)
    return result


def anchors(text):
    return ({item["anchor"] for item in headings(text)} |
            set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text)))


def section(text, anchor):
    found = headings(text)
    selected = [(index, item) for index, item in enumerate(found)
                if item["anchor"] == anchor]
    if len(selected) != 1:
        raise ValueError("absent or ambiguous selected source heading: " + anchor)
    index, item = selected[0]
    end = next((later["offset"] for later in found[index + 1:]
                if later["level"] <= item["level"]), len(text))
    return item, text[item["offset"]:end].rstrip() + "\n"


def confined(root, route):
    path = (root / unquote(route)).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError:
        raise ValueError("path escapes its declared owner: " + route)
    return path


def tree_pins(root):
    return {str(path.relative_to(root)): {"sha256": sha(path), "bytes": path.stat().st_size}
            for path in sorted(root.rglob("*")) if path.is_file()}


def read_fingerprint():
    record = {"package": tree_pins(PACKAGE)}
    for name in ["CANDIDATE.json", "CONSERVATION.json", "FRAME_INPUTS.json", "refresh_views.py"]:
        path = SUPPORT / name
        record[name] = sha(path) if path.exists() else None
    record["common_frontier"] = sha(COMMON)
    record["checker"] = sha(Path(__file__))
    return sha_bytes(json.dumps(record, sort_keys=True, separators=(",", ":")).encode())


def common_rows(text):
    """Acquire identities from common WHAT, not from either tenant's loci."""
    rows, member, mode = {}, None, None
    for line in text.splitlines():
        heading = re.match(r"^## (.+)$", line)
        if heading:
            title = heading[1]
            member = title if title.endswith(".md") else None
            mode = ("standards" if title == "Standards members beyond the sixteen bodies"
                    else "auxiliary" if title == "Auxiliary members" else None)
        if not line.startswith("|"):
            continue
        cells = [item.strip() for item in line.strip().strip("|").split("|")]
        if member and len(cells) > 1:
            anchor = re.fullmatch(r"`(#[^`]+)`", cells[1])
            if anchor:
                identity = member + anchor[1]
                if identity in rows:
                    raise ValueError("duplicate common row: " + identity)
                rows[identity] = "standards/" + member
        elif mode and cells:
            named = re.fullmatch(r"`([^`]+)`", cells[0])
            if named:
                identity = ("standards/" if mode == "standards" else "") + named[1]
                if identity in rows:
                    raise ValueError("duplicate common member row: " + identity)
                rows[identity] = identity
    return rows


def markdown_links(text):
    """Inline, reference and HTML links; fenced/inline examples are excluded."""
    visible = "".join(line for _, line in visible_lines(text))
    definitions = {}
    for match in re.finditer(r'^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)', visible, re.M):
        definitions[" ".join(match[1].lower().split())] = match[2].strip("<>")
    for match in re.finditer(r'(?<!!)\[[^\]\n]*\]\((<[^>\n]+>|[^\n]+?)\)', visible):
        yield match[1].strip().strip("<>").split(' "')[0].split(" '")[0]
    for match in re.finditer(r'(?<!!)\[([^\]\n]+)\]\[([^\]\n]*)\]', visible):
        key = " ".join((match[2] or match[1]).lower().split())
        yield definitions.get(key, "UNRESOLVED_REFERENCE:" + key)
    for match in re.finditer(r'(?<!!)(?<!\])\[([^\]\n]+)\](?![\[(\]:])', visible):
        key = " ".join(match[1].lower().split())
        if key in definitions:
            yield definitions[key]
    for match in re.finditer(r'<a\s+[^>]*href=["\']([^"\']+)', visible):
        yield match[1]


class Check:
    def __init__(self):
        self.failures, self.counts, self.details, self.signals = [], {}, {}, []

    def fail(self, group, message):
        self.failures.append({"group": group, "message": message})

    def inventory(self):
        declared = json_read(SUPPORT / "CANDIDATE.json")
        actual = tree_pins(PACKAGE)
        members = declared["members"]
        paths = [row["path"] for row in members]
        if len(paths) != len(set(paths)):
            self.fail("inventory", "duplicate package member path")
        if set(paths) != set(actual):
            self.fail("inventory", "inventory/tree difference: " + json.dumps({
                "undeclared": sorted(set(actual) - set(paths)),
                "missing": sorted(set(paths) - set(actual))}))
        for row in members:
            try:
                confined(PACKAGE, row["path"])
            except ValueError as error:
                self.fail("inventory", str(error))
                continue
            if actual.get(row["path"]) != {"sha256": row["sha256"], "bytes": row["bytes"]}:
                self.fail("inventory", "byte/hash mismatch: " + row["path"])
        self.counts["package_members"] = len(actual)
        self.counts["package_bytes"] = sum(row["bytes"] for row in actual.values())
        self.details["candidate_standing"] = declared.get("standing")
        self.details["inventory_input_commit"] = declared.get("inventory_input_commit")
        commit = declared.get("inventory_input_commit")
        if not commit or not re.fullmatch(r"[0-9a-f]{40}", commit):
            self.fail("inventory", "missing exact inventory input commit")
            return
        repo = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=TENANT, text=True).strip())
        prefix = str(PACKAGE.relative_to(repo))
        frozen = 0
        for row in members:
            result = subprocess.run(["git", "show", commit + ":" + prefix + "/" + row["path"]],
                                    cwd=TENANT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode or sha_bytes(result.stdout) != row["sha256"] or len(result.stdout) != row["bytes"]:
                self.fail("frozen_inventory", "declared commit does not carry pinned member: " + row["path"])
            else:
                frozen += 1
        self.counts["members_verified_at_declared_commit"] = frozen

    def frontier(self):
        expected = common_rows(COMMON.read_text())
        mapping = json_read(SUPPORT / "CONSERVATION.json")
        rows = mapping["rows"]
        ids = [row["id"] for row in rows]
        if len(expected) != 691 or CHILD not in expected:
            self.fail("frontier", "common selected frontier is not 691 rows including synthetic child")
        if len(ids) != len(set(ids)) or set(ids) != set(expected):
            self.fail("frontier", "conservation/common row difference: " + json.dumps({
                "missing": sorted(set(expected) - set(ids)), "extra": sorted(set(ids) - set(expected))}))
        acceptable = {"conserved", "superseded", "intentionally removed", "not applicable"}
        for row in rows:
            if row.get("source_member") != expected.get(row["id"]):
                self.fail("frontier", "wrong source member: " + row["id"])
            if row.get("disposition") not in acceptable:
                self.fail("frontier", "unresolved/unknown author disposition: " + row["id"])
            disposition = row.get("disposition")
            if disposition == "not applicable" and not row.get("reason"):
                self.fail("frontier", "not-applicable row lacks its bounded reason: " + row["id"])
            if disposition == "intentionally removed" and not row.get("owner_decision"):
                self.fail("frontier", "reserved removal lacks its owner decision reference: " + row["id"])
            locus = row.get("successor_locus")
            if not locus and disposition in {"not applicable", "intentionally removed"}:
                continue
            locus = locus or ""
            name, _, fragment = locus.partition("#")
            try:
                target = confined(PACKAGE, name)
                if not name or not target.is_file():
                    raise ValueError("absent own successor locus")
                if fragment and fragment not in anchors(target.read_text()):
                    raise ValueError("absent own successor anchor")
                if row.get("successor_sha256") != sha(target):
                    raise ValueError("missing or stale per-row successor pin")
            except (ValueError, OSError) as error:
                self.fail("frontier", row["id"] + ": " + str(error))
        for name, pin in mapping.get("successor_member_pins", {}).items():
            target = confined(PACKAGE, name)
            if not target.is_file() or sha(target) != pin["sha256"] or target.stat().st_size != pin["bytes"]:
                self.fail("frontier", "stale conservation member pin: " + name)
        if set(mapping["source_member_pins"]) != set(expected.values()):
            self.fail("frontier", "predecessor member pins do not cover the complete common member set")
        self.counts["common_frontier_rows"] = len(expected)
        self.counts["conservation_rows"] = len(rows)
        self.details["author_disposition_counts"] = {value: sum(row.get("disposition") == value for row in rows)
                                                    for value in sorted(acceptable)}
        self.details["synthetic_child"] = next((row for row in rows if row["id"] == CHILD), None)
        frontier = json_read(SUPPORT / "FRONTIER.json")
        frontier_ids = [row["id"] for row in frontier["rows"]]
        self.details["frontier_acquisition_snapshot"] = {
            "input_commit": frontier.get("input_commit"), "rows": len(frontier_ids),
            "matches_current_common_row_ids": len(frontier_ids) == len(set(frontier_ids)) and set(frontier_ids) == set(expected),
            "standing": "input acquisition snapshot; current common WHAT supplies the compared row identities"}
        self.predecessor(mapping)

    def predecessor(self, mapping):
        if sha(INSTALLED / "manifest.json") != BUILDER_SHA or mapping["builder_manifest_sha256"] != BUILDER_SHA:
            self.fail("predecessor", "builder manifest pin mismatch")
        good = 0
        for name, pin in mapping["source_member_pins"].items():
            target = confined(INSTALLED, name)
            if not target.is_file() or sha(target) != pin["sha256"] or target.stat().st_size != pin["bytes"]:
                self.fail("predecessor", "source member pin mismatch: " + name)
            else:
                good += 1
        self.counts["predecessor_members_verified"] = good

    def links_and_surface(self):
        checked = external = logical = 0
        attribution = []
        for path in sorted(PACKAGE.rglob("*")):
            if not path.is_file():
                continue
            name = str(path.relative_to(PACKAGE))
            if path.is_symlink():
                self.fail("surface", "package symlink is not an exact independent member: " + name)
            try:
                text = path.read_text()
            except UnicodeDecodeError:
                continue
            attribution.extend([name] * text.count("Dimitar Popov"))
            if path.suffix == ".json":
                try:
                    json.loads(text)
                except ValueError as error:
                    self.fail("json", name + ": " + str(error))
                self.counts["json_members"] = self.counts.get("json_members", 0) + 1
            if path.suffix != ".md":
                continue
            if any(line.rstrip() != line for line in text.splitlines()):
                self.fail("surface", "trailing whitespace: " + name)
            self.counts["markdown_members"] = self.counts.get("markdown_members", 0) + 1
            for number, line in visible_lines(text):
                if re.match(r"^(Author|Status|Standing|Date|Revision):", line) and not (
                        name == "README.md" and line.strip() == "Author: Dimitar Popov."):
                    self.fail("surface", "construction header: %s:%d" % (name, number))
                if re.match(r"^(generated_by|generated_at):", line):
                    self.fail("surface", "construction provenance in package: %s:%d" % (name, number))
            for target in markdown_links(text):
                if target.startswith("UNRESOLVED_REFERENCE:"):
                    self.fail("links", name + " -> " + target)
                    continue
                logical_match = re.match(r"^stdo://releases/([^/]+)/(.+)$", target)
                if logical_match:
                    logical += 1
                    if logical_match[1] == "v2.5.1-rc.2":
                        route = logical_match[2]
                        dest_name, _, fragment = route.partition("#")
                        destination = INSTALLED / unquote(dest_name)
                    else:
                        external += 1
                        continue
                elif re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    external += 1
                    continue
                else:
                    route, _, fragment = target.partition("#")
                    destination = (path.parent / unquote(route)).resolve() if route else path
                checked += 1
                if not destination.exists():
                    self.fail("links", name + " -> missing " + target)
                elif fragment and destination.suffix == ".md" and unquote(fragment) not in anchors(destination.read_text()):
                    self.fail("links", name + " -> missing fragment " + target)
        if attribution != ["README.md"]:
            self.fail("surface", "attribution must occur once at package README: " + repr(attribution))
        for forbidden in ["CONSERVATION.json", "CANDIDATE.json", "qualification", "reviews", ".ai-workspace"]:
            if (PACKAGE / forbidden).exists():
                self.fail("surface", "support carrier in Product: " + forbidden)
        self.counts.update({"links_resolved_locally": checked, "external_links_not_fetched": external,
                            "logical_release_links": logical, "author_attributions": len(attribution)})

    def excerpts(self):
        index = json_read(SUPPORT / "FRAME_INPUTS.json")
        exact = relocated = 0
        for frame in index["frames"]:
            view = confined(PACKAGE, frame["path"])
            if sha(view) != frame["sha256"] or view.stat().st_size != frame["bytes"]:
                self.fail("excerpts", "view pin mismatch: " + frame["path"])
            chunks = view.read_text().split("\nSource:")[1:]
            if len(chunks) != len(frame["routes"]):
                self.fail("excerpts", "source chunk count mismatch: " + frame["path"])
                continue
            for route, chunk in zip(frame["routes"], chunks):
                owner = confined(PACKAGE, route["owner"])
                try:
                    heading, raw = section(owner.read_text(), route["anchor"])
                    if sha(owner) != route.get("owner_sha256") or sha_bytes(raw.encode()) != route.get("section_sha256"):
                        raise ValueError("owner or excerpt pin mismatch")
                    expected_route = "../" + str(Path(route["owner"]).relative_to("standards")) + "#" + route["anchor"]
                    if "](" + expected_route + ")" not in chunk.split("\n", 1)[0]:
                        raise ValueError("source header route differs")
                    if "SHA256 `" + sha(owner) + "`" not in chunk.split("\n", 1)[0]:
                        raise ValueError("source header digest differs")
                    def relocate(match):
                        nonlocal relocated
                        target = match[2]
                        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                            return match[0]
                        if target.startswith("#"):
                            relocated += 1
                            target = owner.name + target
                        return match[1] + "../" + target + match[3]
                    rendered = re.sub(r"(\[[^\]]*\]\()([^\n]+?)(\))", relocate, raw)
                    displayed = chunk.split("\n\n", 1)[1].rstrip() + "\n"
                    if displayed != rendered:
                        raise ValueError("excerpt differs from exact source after declared relocation")
                    exact += 1
                except (ValueError, KeyError, IndexError, OSError) as error:
                    self.fail("excerpts", frame["path"] + "#" + route["anchor"] + ": " + str(error))
        self.counts["exact_excerpt_sections"] = exact
        self.counts["local_fragment_relocations_checked"] = relocated
        self.counts["excerpt_views"] = len(index["frames"])
        for view in index.get("source_linked_summaries", []):
            path = confined(PACKAGE, view["path"])
            if sha(path) != view["sha256"] or path.stat().st_size != view["bytes"]:
                self.fail("excerpts", "summary pin mismatch: " + view["path"])
            for route in view["routes"]:
                owner = confined(PACKAGE, route["owner"])
                if sha(owner) != route["owner_sha256"] or route["anchor"] not in anchors(owner.read_text()):
                    self.fail("excerpts", "summary source mismatch: " + route["owner"])
        self.compressions()

    def compressions(self):
        pins = 0
        for path in sorted((PACKAGE / "standards/authority_compressions").glob("*.md")):
            text = path.read_text()
            if not text.startswith("---\n"):
                continue
            front = text[4:].split("---", 1)[0]
            source = re.search(r"^source_ref: (.+)$", front, re.M)
            if source:
                pin = re.search(r"^source_digest: ([0-9a-f]{64})$", front, re.M)
                if not pin or sha((path.parent / source[1]).resolve()) != pin[1]:
                    self.fail("compressions", "source digest mismatch: " + path.name)
                pins += 1
            for match in re.finditer(r"^  ([\w/.-]+): ([0-9a-f]{64})$", front, re.M):
                if sha(PACKAGE / "standards" / match[1]) != match[2]:
                    self.fail("compressions", "watched digest mismatch: " + path.name + ":" + match[1])
                pins += 1
        self.counts["compression_source_pins"] = pins

    def schemas(self):
        try:
            from jsonschema import Draft202012Validator
        except ImportError:
            self.fail("schemas", "jsonschema is unavailable; no schema validation performed")
            return
        standard = PACKAGE / "standards"
        definition_schema = json_read(standard / "schemas/product-definition.schema.json")
        manifest_schema = json_read(standard / "schemas/installed-release-manifest.schema.json")
        Draft202012Validator.check_schema(definition_schema)
        Draft202012Validator.check_schema(manifest_schema)
        template = json_read(standard / "templates/PRODUCT_DEFINITION_TEMPLATE.json")
        raw = json.dumps(template).replace("REPLACE_WITH_IMMUTABLE_CUT", "v3.0.0-rc.1").replace(
            "REPLACE_WITH_64_LOWERCASE_HEX_SHA256", "0" * 64).replace("REPLACE_WITH_VERSION_LINE", "3.0.0")
        positive = json.loads(raw)
        validator = Draft202012Validator(definition_schema)
        errors = list(validator.iter_errors(positive))
        for error in errors:
            self.fail("schemas", "hypothetical definition: " + error.message)
        controls = []
        for key, value in [("uri", "stdo://channels/3.0.0"), ("manifest_sha256", "1" * 63)]:
            negative = copy.deepcopy(positive)
            negative["constitution"]["stdo"]["basis"][key] = value
            rejected = bool(list(validator.iter_errors(negative)))
            controls.append({"field": key, "rejected": rejected})
            if not rejected:
                self.fail("schemas", "wrong definition basis accepted: " + key)
        entrypoints = template["constitution"]["entrypoints"]
        for entry in entrypoints:
            target = confined(PACKAGE, entry["uri"])
            if not target.is_file() or entry["basis"] != "#/constitution/stdo/basis":
                self.fail("schemas", "unresolved or unbound template entrypoint: " + entry["uri"])
        bootstrap = template["constitution"]["agent_bootstrap"]["entrypoint"]
        if bootstrap != "#/constitution/entrypoints/0" or entrypoints[0]["uri"] != "standards/authority_compressions/stdo_bootstrap.md":
            self.fail("schemas", "bootstrap entrypoint position no longer names the selected discovery member")
        manifest = copy.deepcopy(json_read(INSTALLED / "manifest.json"))
        manifest["release"] = {"cut": "v0.0.0-rc.1", "tag_object": "0" * 40,
                               "commit": "0" * 40, "tree": "0" * 40, "standards_tree": "0" * 40}
        for folder, inventory in [("standards", manifest["standards"]),
                                  ("plugins/spec", manifest["auxiliary"]["plugin"])]:
            rows = [{"path": str(path.relative_to(PACKAGE / folder)), "sha256": sha(path)}
                    for path in sorted((PACKAGE / folder).rglob("*")) if path.is_file()]
            inventory["members"], inventory["member_count"] = rows, len(rows)
            if folder == "standards":
                stream = "".join("%s  %s/%s\n" % (row["sha256"], inventory["source_root"], row["path"]) for row in rows)
                inventory["member_set_sha256"] = sha_bytes(stream.encode())
        manifest["auxiliary"]["license"]["sha256"] = sha(PACKAGE / "LICENSE")
        manifest["auxiliary"]["release_note"] = {"source_path": "releases/v0.0.0.md", "installed_path": "release/release-note.md",
                                                   "sha256": sha(SUPPORT / "surface-repair/release-note-fixture.md")}
        validator = Draft202012Validator(manifest_schema)
        for error in validator.iter_errors(manifest):
            self.fail("schemas", "hypothetical manifest: " + error.message)
        negative = copy.deepcopy(manifest)
        negative["auxiliary"]["uncatalogued_history"] = {"path": "provenance/note.md"}
        rejected = bool(list(validator.iter_errors(negative)))
        if not rejected:
            self.fail("schemas", "unrecognised installed auxiliary category accepted")
        members = set(tree_pins(PACKAGE))
        mapped = {name for name in members if name.startswith(("standards/", "plugins/spec/"))} | {"LICENSE"}
        if members - mapped != {"README.md"}:
            self.fail("schemas", "package contains members outside the declared install namespaces and package entry")
        self.details["schema_checks"] = {"schemas_checked": 2, "definition_controls": controls,
            "extra_auxiliary_category_rejected": rejected, "template_entrypoints_resolved": len(entrypoints),
            "install_namespace_product_members": len(mapped), "package_entry_excluded_from_hypothetical_install": "README.md",
            "subject": "hypothetical instances only; no release, install, sync or channel change"}

    def ownership_signals(self):
        patterns = [r"baseline result family", r"owns? (?:the )?(?:shared |core )?result algebra",
                    r"complete Product view", r"result algebra is", r"generated_by:", r"generated_at:"]
        for path in sorted((PACKAGE / "standards").rglob("*.md")):
            for number, line in visible_lines(path.read_text()):
                for pattern in patterns:
                    if re.search(pattern, line, re.I):
                        self.signals.append({"path": str(path.relative_to(PACKAGE)), "line": number,
                            "pattern": pattern, "text": line.strip(),
                            "standing": "search signal, not a demonstrated semantic contradiction"})

    def refresh_experiment(self):
        with tempfile.TemporaryDirectory(prefix="artifact-refresh-", dir=str(HERE)) as tmp:
            isolated = Path(tmp) / "tenant"
            isolated_support = isolated / "qualification/C3"
            isolated_support.mkdir(parents=True)
            shutil.copytree(PACKAGE, isolated / "successor")
            for name in ["FRAME_INPUTS.json", "refresh_views.py"]:
                shutil.copy2(SUPPORT / name, isolated_support / name)
            def snapshot():
                return {"package": tree_pins(isolated / "successor"),
                        "index": sha(isolated_support / "FRAME_INPUTS.json")}
            before = snapshot()
            reports, states = [], []
            for _ in range(2):
                run = subprocess.run([sys.executable, str(isolated_support / "refresh_views.py")],
                                     cwd=isolated, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=60)
                reports.append({"exit_code": run.returncode, "stdout": run.stdout.strip(), "stderr": run.stderr.strip()})
                states.append(snapshot())
                if run.returncode:
                    self.fail("refresh", "isolated refresh failed")
            after = states[-1]
            if before != states[0] or states[0] != after:
                changed = sorted(name for name in set(before["package"]) | set(states[0]["package"]) | set(after["package"])
                                 if before["package"].get(name) != states[0]["package"].get(name)
                                 or states[0]["package"].get(name) != after["package"].get(name))
                self.fail("refresh", "refresh changes already-qualified bytes: " + json.dumps(changed))
            self.details["refresh_experiment"] = {"live_package_written": False,
                "runs": reports, "unchanged_after_first_run": before == states[0],
                "second_run_idempotent": states[0] == after,
                "limit": "exact artifact regeneration only, not semantic sufficiency"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--idempotence", action="store_true", help="run refresh twice on an isolated local copy")
    parser.add_argument("--output", type=Path, default=HERE / "ARTIFACT_CHECK.json")
    args = parser.parse_args()
    output = args.output.resolve()
    if output.parent != HERE:
        parser.error("report must be directly inside qualification/C3/synthesis")
    started = time.monotonic()
    initial = read_fingerprint()
    checker = Check()
    for name in ["inventory", "frontier", "links_and_surface", "excerpts", "schemas", "ownership_signals"]:
        try:
            getattr(checker, name)()
        except Exception as error:
            checker.fail(name, type(error).__name__ + ": " + str(error))
    if args.idempotence:
        try:
            checker.refresh_experiment()
        except Exception as error:
            checker.fail("refresh", type(error).__name__ + ": " + str(error))
    final = read_fingerprint()
    if initial != final:
        checker.fail("subject", "inputs changed during checking; discard this result and rerun on a stable subject")
    report = {"kind": "stdo_synthesis_artifact_qualification", "valid": not checker.failures,
        "input_fingerprint_before": initial, "input_fingerprint_after": final,
        "recording_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=TENANT, text=True).strip(),
        "python_executable": sys.executable, "python_version": sys.version,
        "counts": checker.counts, "details": checker.details, "failures": checker.failures,
        "ownership_search_signals": checker.signals, "elapsed_seconds": round(time.monotonic() - started, 3),
        "limits": ["Artifact coordinates and reproducibility, not semantic conservation or whole-method fitness",
                   "Author dispositions and resolved loci are not independent acceptance",
                   "Source-bound excerpts are not proof of task sufficiency or ordinary-use success",
                   "Schema instances and release note are hypothetical; no release, installation or plugin-host proof",
                   "Ownership search signals require contextual review; their absence proves no semantic property",
                   "External web links were not fetched; known installed rc.2 routes were checked locally",
                   "This qualification Writer authored package consumer laws; this is not independent semantic review"]}
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"valid": report["valid"], "counts": checker.counts,
                      "failures": len(checker.failures), "first_failures": checker.failures[:12],
                      "report": str(output), "elapsed_seconds": report["elapsed_seconds"]}, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
