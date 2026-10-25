"""Finite operator-selected composition and mediated disclosure checks.

This module consumes explicit policy, never infers authority from prose.  It is
part of the support implementation, not an OS sandbox or a semantic reviewer.
"""
from __future__ import annotations

import base64
from bisect import bisect_left
from html.parser import HTMLParser
import copy
from pathlib import Path
import re
import time
from urllib.parse import unquote, urlsplit
from typing import cast

import ac_support_core as c

SCHEMA = "a_c.fd-support.composition/1"
CONTROL = frozenset({"dispatch.observe", "dispatch.cancel", "events.wait"})
SUPPORTED = frozenset({
    "tools.describe", "composition.inspect", "source.read", "workspace.observe",
    "records.find", "records.read", "graph.project", "work.project",
    "context.assemble", "contract.preflight", "dispatch.start",
    "return.capture", "return.check", "review.prepare", "evidence.read",
    *CONTROL,
})


def _bool(value: c.JSON) -> bool:
    if type(value) is not bool:
        raise c.SupportError("contract_violation", "Composition flag must be boolean")
    return value


def _refs(value: c.JSON, *, nonempty: bool = False) -> list[c.Object]:
    values = [c.validate_content(ref, "SourceRef") for ref in c.as_list(value)]
    if nonempty and not values:
        raise c.SupportError("authority_missing", "Composition requires source-bound authority")
    return values


def _ids(value: c.JSON, population: c.Object | None = None) -> list[str]:
    values = c._strings(value)
    c._unique(values, "composition selection")
    if population is not None and any(name not in population for name in values):
        raise c.SupportError("basis_missing", "Composition selection names an unknown member")
    return values


def load(runtime: c.Runtime, source: c.Object) -> c.Object:
    """Validate shape once; selected material authority is rechecked at use."""
    c.validate_content(source, "SourceRef")
    if source["selector"] is not None:
        raise c.SupportError("contract_violation", "Composition declaration selects a whole document")
    raw = c._source_bytes(runtime, source)
    if len(raw) > c.integer(c.as_object(runtime.policy["limits"])["max_bytes"]):
        raise c.SupportError("budget_exceeded", "Composition document exceeds configured bound")
    doc = c.as_object(c.parse_json(raw))
    c.exact_keys(doc, ("schema", "id", "authority_sources", "edges", "resources", "bindings"))
    if doc["schema"] != SCHEMA:
        raise c.SupportError("unsupported_contract", "Unsupported composition declaration")
    c.text(doc["id"]); _refs(doc["authority_sources"], nonempty=True)
    edges = c.as_object(doc["edges"]); resources = c.as_object(doc["resources"])
    bindings = c.as_object(doc["bindings"])
    limit = c.integer(c.as_object(runtime.policy["limits"])["max_files"])
    if len(edges) + len(resources) + len(bindings) > limit:
        raise c.SupportError("budget_exceeded", "Composition population exceeds configured bound")
    for name, raw_edge in edges.items():
        c.text(name); edge = c.as_object(raw_edge)
        c.exact_keys(edge, ("source_definition", "source_id", "index", "target_definition", "target_id", "relation", "contracts"))
        c.text(edge["source_id"]); c.text(edge["target_id"]); c.integer(edge["index"])
        for field in ("source_definition", "target_definition", "relation"):
            c.validate_content(edge[field], "SourceRef")
            if c.as_object(edge[field])["selector"] is not None:
                raise c.SupportError("unsupported_contract", "Edge identity pins whole source documents")
        if any(ref["selector"] is not None for ref in _refs(edge["contracts"], nonempty=True)):
            raise c.SupportError("unsupported_contract", "Edge contracts pin whole source documents")
    for name, raw_resource in resources.items():
        c.text(name); resource = c.as_object(raw_resource)
        c.exact_keys(resource, ("source", "owner", "complete", "parents"))
        c.validate_content(resource["source"], "SourceRef")
        c.text(resource["owner"]); _bool(resource["complete"])
        _ids(resource["parents"], resources)
    for name in resources:
        _closure(resources, name)
    principals = c.as_object(runtime.policy["principals"])
    for name, raw_binding in bindings.items():
        if name not in principals:
            raise c.SupportError("authority_missing", "Composition principal is not registered")
        binding = c.as_object(raw_binding)
        c.exact_keys(binding, ("engagement", "purpose", "route", "operations", "allow", "exclude", "exports", "require_complete", "clean_room", "host_isolation", "output"))
        c.text(binding["engagement"]); c.text(binding["purpose"])
        _ids(binding["route"], edges); _ids(binding["operations"])
        _ids(binding["allow"], resources); _ids(binding["exclude"], resources)
        for flag in ("require_complete", "clean_room", "host_isolation"):
            _bool(binding[flag])
        export_ids: list[str] = []
        for raw_export in c.as_list(binding["exports"]):
            export = c.as_object(raw_export)
            c.exact_keys(export, ("resource", "authority", "eligible"))
            name_export = c.text(export["resource"])
            if name_export not in resources:
                raise c.SupportError("basis_missing", "Composition export has no source")
            export_ids.append(name_export); c.validate_content(export["authority"], "SourceRef")
            _bool(export["eligible"])
        c._unique(export_ids, "composition exports")
        output = c.as_object(binding["output"])
        c.exact_keys(output, ("complete", "sources")); _bool(output["complete"])
        _ids(output["sources"], resources)
    return doc


def _closure(resources: c.Object, name: str) -> list[str]:
    order: list[str] = []; active: set[str] = set(); done: set[str] = set()
    stack: list[tuple[str, bool]] = [(name, False)]
    while stack:
        current, leaving = stack.pop()
        if leaving:
            active.remove(current); done.add(current); order.append(current); continue
        if current in active:
            raise c.SupportError("basis_ambiguous", "Cyclic information provenance is unsupported")
        if current in done:
            continue
        if current not in resources:
            raise c.SupportError("basis_missing", "Information provenance member is absent")
        active.add(current); stack.append((current, True))
        for parent in reversed(c._strings(c.as_object(resources[current])["parents"])):
            stack.append((parent, False))
    return order


def _binding(runtime: c.Runtime, principal: str) -> tuple[c.Object, c.Object]:
    doc = runtime.composition
    if doc is None:
        raise c.SupportError("basis_missing", "No composition declaration is selected")
    bindings = c.as_object(doc["bindings"])
    if principal not in bindings:
        raise c.SupportError("authority_missing", "No composition binding for the selected principal")
    return doc, c.as_object(bindings[principal])


def current(runtime: c.Runtime) -> None:
    if runtime.composition is not None:
        c.read_source(runtime, c.as_object(runtime.policy["composition"]))


def _local(runtime: c.Runtime, source: c.Object) -> Path:
    if source["engine"] != "workspace-regular-file":
        raise c.SupportError("unsupported_contract", "Composition edges currently use registered local regular-file definitions")
    return c.source_path(runtime, source)


# Finite local scanner adapted from the independently delivered manager;
# source custody is recorded in PRODUCT_COMPOSITION_01/fragment-scanner-loan.json.
# This copy has no sibling runtime import.
class _Anchors(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.values: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if value is not None and (key == "id" or (tag == "a" and key == "name")):
                self.values.add(value)


def _markdown_text(text: str) -> str:
    """Remove comments and fenced/indented examples before identifying anchors."""
    lines: list[str] = []
    fence: str | None = None
    paragraph = False
    for line in re.sub(r"<!--.*?-->", "", text, flags=re.S).splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence is not None:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
                lines.append("")
            continue
        if match:
            fence = match[1]
            lines.append("")
            paragraph = False
        elif not line.strip():
            lines.append("")
            paragraph = False
        elif line.startswith(("    ", "\t")) and not paragraph:
            lines.append("")
        else:
            # Indentation cannot start a code block inside an open paragraph;
            # it may contain the continuation or delimiter of an inline span.
            line = re.sub(r"^ {1,3}(?=#)", "", line)
            lines.append(line)
            paragraph = not bool(re.match(r"^#{1,6}(?:[ \t]+|$)", line))
    return "\n".join(lines)


_MARKDOWN_HTML_TAG = (
    r'</[A-Za-z][A-Za-z0-9-]*\s*>'
    r'|<[A-Za-z][A-Za-z0-9-]*'
    r'''(?:\s+[A-Za-z_:][A-Za-z0-9_.:-]*(?:\s*=\s*(?:[^\s"'=<>`]+|'[^']*'|"[^"]*"))?)*'''
    r'\s*/?>'
)
_MARKDOWN_INLINE_TOKEN = re.compile(
    r"\\[!\"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~]|`+|" + _MARKDOWN_HTML_TAG
)


def _markdown_html(text: str) -> str:
    """Select raw HTML tags outside Markdown escapes and inline code.

    A code span closes only at a maximal backtick run of the same width,
    including across line endings. Escapes apply outside spans; raw HTML tags
    are consumed atomically, so backticks in their attributes are not Markdown
    delimiters. This is the supported fragment scanner, not a Markdown renderer.
    """
    tags: list[str] = []
    # Inline code cannot cross a paragraph boundary or an ATX block boundary.
    for block in re.split(r"(\n[ \t]*\n|(?m:^[ ]{0,3}#{1,6}[^\S\n]+.*$))", text):
        runs: dict[int, list[int]] = {}
        for run in re.finditer(r"`+", block):
            runs.setdefault(len(run[0]), []).append(run.start())
        cursor = 0
        while token := _MARKDOWN_INLINE_TOKEN.search(block, cursor):
            value = token[0]
            cursor = token.end()
            if value.startswith("\\"):
                continue
            if value.startswith("`"):
                width = len(value)
                starts = runs.get(width, [])
                next_run = bisect_left(starts, cursor)
                if next_run < len(starts):
                    cursor = starts[next_run] + width
                continue
            tags.append(value)
    return "\n".join(tags)



def _uri_source(runtime: c.Runtime, base: c.Object, uri: str, selected: c.Object) -> None:
    parts = urlsplit(uri)
    if parts.scheme not in ("", "file") or parts.netloc not in ("", "localhost") or parts.query:
        raise c.SupportError("unsupported_contract", "Composition edge reference requires supported local resolution")
    base_path = _local(runtime, base)
    expected = Path(unquote(parts.path)) if parts.path else base_path
    if not expected.is_absolute():
        expected = base_path.parent / expected
    # Lexical normalization does not follow symlinks. Actual acquisition checks
    # every selected path component through the registered source root.
    import os
    expected = Path(os.path.abspath(expected))
    actual = _local(runtime, selected)
    if actual != expected:
        raise c.SupportError("basis_stale", "Edge URI does not bind the selected exact source")
    full = copy.deepcopy(selected); full["selector"] = None
    raw = c._source_bytes(runtime, full)
    fragment = unquote(parts.fragment)
    if not fragment:
        return
    if fragment.startswith("/"):
        c.pointer(c.parse_json(raw), fragment); return
    try:
        text = raw.decode("utf-8")
    except UnicodeError as exc:
        raise c.SupportError("unsupported_contract", "Named edge fragment requires UTF-8 Markdown") from exc
    visible = _markdown_text(text)
    parsed = _Anchors(); parsed.feed(_markdown_html(visible))
    anchors = parsed.values
    counts: dict[str, int] = {}
    for heading in re.findall(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", visible, re.M):
        heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
        slug = re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
        count = counts.get(slug, 0); counts[slug] = count + 1
        anchors.add(slug if count == 0 else slug + "-" + str(count))
    if fragment not in anchors:
        raise c.SupportError("basis_missing", "Composition reference fragment is absent")


def route(runtime: c.Runtime, principal: str) -> c.Object:
    doc, binding = _binding(runtime, principal); current(runtime)
    if binding["host_isolation"] is True:
        raise c.SupportError("unsupported_contract", "Composition supports mediated checks, not required host isolation")
    for source in _refs(doc["authority_sources"], nonempty=True):
        c.read_source(runtime, source)
    identity = c.text(c.as_object(runtime.policy["product"])["definition_id"])
    selected_definition = c.as_object(runtime.policy["product"])["definition"]
    edges = c.as_object(doc["edges"])
    for edge_id in c._strings(binding["route"]):
        edge = c.as_object(edges[edge_id])
        if edge["source_id"] != identity:
            raise c.SupportError("basis_stale", "Composition route identities do not join")
        source_ref = c.as_object(edge["source_definition"])
        target_ref = c.as_object(edge["target_definition"])
        if source_ref != selected_definition:
            raise c.SupportError("basis_stale", "Composition route must use the selected exact definition at every join")
        source = c._source_json(runtime, source_ref); target = c._source_json(runtime, target_ref)
        if c.pointer(source, "/product/definition_id") != identity or c.pointer(target, "/product/definition_id") != edge["target_id"]:
            raise c.SupportError("basis_stale", "Composition definition identity differs")
        selected = c.as_object(c.pointer(source, "/composition/" + str(c.integer(edge["index"]))))
        c.exact_keys(selected, ("product_definition", "target_definition_id", "relation", "contracts"))
        if selected["target_definition_id"] != edge["target_id"]:
            raise c.SupportError("basis_stale", "Composition target identity differs from its edge")
        _uri_source(runtime, source_ref, c.text(selected["product_definition"]), target_ref)
        _uri_source(runtime, source_ref, c.text(selected["relation"]), c.as_object(edge["relation"]))
        refs = _refs(edge["contracts"], nonempty=True); uris = c._strings(selected["contracts"])
        if len(refs) != len(uris):
            raise c.SupportError("basis_stale", "Composition contract population differs")
        for uri, ref in zip(uris, refs):
            _uri_source(runtime, source_ref, uri, ref)
        identity = c.text(edge["target_id"])
        selected_definition = target_ref
    return binding


def material_refs(runtime: c.Runtime, principal: str) -> list[c.JSON]:
    if runtime.composition is None:
        return []
    doc, binding = _binding(runtime, principal)
    refs: list[c.JSON] = [runtime.policy["composition"], *c.as_list(doc["authority_sources"])]
    for edge_id in c._strings(binding["route"]):
        edge = c.as_object(c.as_object(doc["edges"])[edge_id])
        refs.extend([edge["source_definition"], edge["target_definition"], edge["relation"], *c.as_list(edge["contracts"])])
    refs.extend(c.as_object(item)["authority"] for item in c.as_list(binding["exports"]))
    output = c.as_object(binding["output"])
    refs.extend(c.as_object(c.as_object(doc["resources"])[name])["source"] for name in c._strings(output["sources"]))
    return refs


def _contains(parent: c.Object, child: c.Object) -> bool:
    if any(parent[key] != child[key] for key in ("engine", "root", "path", "object", "sha256")):
        return False
    if parent["selector"] is None:
        return True
    if child["selector"] is None:
        return False
    p = c.as_object(parent["selector"]); q = c.as_object(child["selector"])
    if "lines" in p and "lines" in q:
        left = c.as_list(p["lines"]); right = c.as_list(q["lines"])
        return c.integer(left[0]) <= c.integer(right[0]) <= c.integer(right[1]) <= c.integer(left[1])
    if "json_pointer" in p and "json_pointer" in q:
        left_pointer = str(p["json_pointer"]); right_pointer = str(q["json_pointer"])
        return not left_pointer or right_pointer == left_pointer or right_pointer.startswith(left_pointer + "/")
    return False


def _locator(runtime: c.Runtime, source: c.Object) -> str:
    if source["engine"] == "retained-evidence":
        return "evidence:" + c.text(source["path"])
    roots = c.as_object(runtime.policy["sources"])
    if source["root"] not in roots:
        raise c.SupportError("history_incomplete", "Prior source root cannot be resolved under this policy")
    root = c.as_object(roots[c.text(source["root"])])
    return c.text(source["engine"]) + ":" + str(Path(c.text(root["path"])) / c.text(source["path"]))


def _snapshot(runtime: c.Runtime, resources: c.Object, name: str) -> c.Object:
    resource = c.as_object(resources[name])
    origins: list[c.JSON] = []
    for origin in _closure(resources, name):
        item = c.as_object(resources[origin]); source = c.as_object(item["source"])
        origins.append({"id": origin, "source": source, "locator": _locator(runtime, source), "complete": item["complete"]})
    return {"id": name, "source": resource["source"], "origins": origins,
            "complete": all(c.as_object(item)["complete"] is True for item in origins)}


def _unknown(source: c.JSON) -> c.Object:
    return {"id": "unresolved-external-provenance", "source": source,
            "origins": [], "complete": False, "unknown": True}


def _eligible(runtime: c.Runtime, binding: c.Object, snapshot: c.Object, *, require_allow: bool) -> None:
    doc = cast(c.Object, runtime.composition); resources = c.as_object(doc["resources"])
    complete_required = binding["require_complete"] is True or binding["clean_room"] is True or bool(c.as_list(binding["exclude"]))
    if snapshot.get("unknown") is True:
        if complete_required:
            raise c.SupportError("basis_missing", "Unresolved provenance cannot establish this receiving information policy")
        return  # An unresolved influence is retained; it grants no source access.
    name = c.text(snapshot["id"])
    if require_allow and name == "unclassified-prior-source":
        matches = [key for key in c._strings(binding["allow"]) if _contains(c.as_object(c.as_object(resources[key])["source"]), c.as_object(snapshot["source"]))]
        if len(matches) == 1:
            name = matches[0]  # Exact access eligibility, never retrospective completeness.
    if require_allow and name not in c._strings(binding["allow"]):
        raise c.SupportError("acquisition_denied", "Selected route does not permit this source")
    if require_allow and (name not in resources or not _contains(c.as_object(c.as_object(resources[name])["source"]), c.as_object(snapshot["source"]))):
        raise c.SupportError("acquisition_denied", "Historical source version is not selected for this disclosure")
    if complete_required and snapshot["complete"] is not True:
        raise c.SupportError("basis_missing", "Declared information provenance is incomplete")
    excludes = c._strings(binding["exclude"])
    excluded_locators = {_locator(runtime, c.as_object(c.as_object(resources[key])["source"])) for key in excludes}
    forbidden = any(c.as_object(origin)["id"] in excludes or c.as_object(origin)["locator"] in excluded_locators for origin in c.as_list(snapshot["origins"]))
    if not forbidden:
        return
    # A forbidden root itself cannot be laundered through its own export entry.
    root_locator = next((c.as_object(item)["locator"] for item in c.as_list(snapshot["origins"]) if c.as_object(item)["id"] == name), None)
    if name not in excludes and root_locator not in excluded_locators:
        for raw in c.as_list(binding["exports"]):
            export = c.as_object(raw)
            if export["resource"] == name and export["eligible"] is True and name in resources and c.as_object(resources[name])["source"] == snapshot["source"]:
                c.read_source(runtime, c.as_object(export["authority"])); return
    raise c.SupportError("acquisition_denied", "Receiving information policy excludes this provenance")


def authorize_source(runtime: c.Runtime, source: c.Object, principal: str | None = None) -> c.Object | None:
    if runtime.composition is None:
        return None
    principal = runtime.principal_id if principal is None else principal
    doc, _ = _binding(runtime, principal); binding = route(runtime, principal)
    resources = c.as_object(doc["resources"])
    candidates = [name for name in c._strings(binding["allow"]) if _contains(c.as_object(c.as_object(resources[name])["source"]), source)]
    if not candidates:
        raise c.SupportError("acquisition_denied", "Selected route does not permit this exact source selection")
    # Duplicate registrations are not alternative authority escape routes.
    if len(candidates) != 1:
        raise c.SupportError("basis_ambiguous", "Source has multiple selected composition registrations")
    owners = {c.text(c.as_object(runtime.policy["product"])["definition_id"])}
    for edge_id in c._strings(binding["route"]):
        owners.add(c.text(c.as_object(c.as_object(doc["edges"])[edge_id])["target_id"]))
    if c.as_object(resources[candidates[0]])["owner"] not in owners:
        raise c.SupportError("authority_missing", "Source owner is outside this explicitly selected route")
    snapshot = _snapshot(runtime, resources, candidates[0]); _eligible(runtime, binding, snapshot, require_allow=True)
    actor = c.as_object(c.as_object(runtime.policy["principals"])[principal])
    return {"declaration": runtime.policy["composition"], "actor_id": actor["actor_id"],
            "engagement": binding["engagement"], "purpose": binding["purpose"],
            "route": binding["route"], "resources": [snapshot]}


def _exposures(runtime: c.Runtime, actor_id: str) -> list[c.Object]:
    """Use observed delivery and stable actor identity, independent of policy id."""
    records, query = c._history(runtime, "acquisition", {"payload.schema": "a_c.fd-support.acquisition/1", "payload.recipient": actor_id})
    if query["complete"] is not True:
        raise c.SupportError("history_incomplete", "Actor acquisition history is incomplete")
    delivered_refs: set[str] = set()
    transports, tq = c._history(runtime, "acquisition", {"payload.schema": "a_c.fd-support.transport-observation/1", "payload.recipient": actor_id})
    if tq["complete"] is not True:
        raise c.SupportError("history_incomplete", "Actor delivery history is incomplete")
    for envelope in transports:
        payload = c.as_object(envelope["payload"])
        if c.as_object(payload["delivery"])["state"] == "write_flushed":
            delivered_refs.update(c.text(c.as_object(ref)["id"]) for ref in c.as_list(payload["acquisitions"]))
    events, eq = c._history(runtime, "raw", {"payload.schema": "a_c.fd-support.attempt-event/1", "payload.kind": "context_delivery"})
    if eq["complete"] is not True:
        raise c.SupportError("history_incomplete", "Context delivery history is incomplete")
    delivered_contexts: set[str] = set()
    context_inputs: dict[str, c.Object] = {}
    for event in events:
        data = c.as_object(c.as_object(event["payload"])["data"])
        if not isinstance(data.get("context"), dict):
            continue
        context = c.as_object(c.load_artifact(runtime, c.as_object(data["context"]), "context")["payload"])
        actor = c.as_object(c.as_object(context["packet"])["actor_authority"])
        if actor["actor_id"] == actor_id and context["rendered_sha256"] == data.get("rendered_sha256") and c.integer(data.get("bytes", 0)) > 0:
            delivered_contexts.add(c.text(c.as_object(data["context"])["id"]))
            context_inputs[c.text(c.as_object(data["context"])["id"])] = context
    # A reserved attempt without a delivery observation can have crossed the
    # physical write boundary before evidence publication failed. Conservatively
    # retain its whole declared Context as possible exposure. A positive zero-
    # byte observation is the only declared non-delivery used here.
    attempts, aq = c._history(runtime, "attempt", {"payload.schema": "a_c.fd-support.attempt/1"})
    if aq["complete"] is not True:
        raise c.SupportError("history_incomplete", "Attempt acquisition-parent history is incomplete")
    observed_contexts = {c.text(c.as_object(c.as_object(c.as_object(item["payload"])["data"])["context"])["id"]) for item in events if isinstance(c.as_object(c.as_object(item["payload"])["data"]).get("context"), dict)}
    for attempt in attempts:
        ref = c.as_object(c.as_object(attempt["payload"])["context"])
        context_payload = c.as_object(c.load_artifact(runtime, ref, "context")["payload"])
        actor = c.as_object(c.as_object(context_payload["packet"])["actor_authority"])
        if actor["actor_id"] == actor_id and c.text(ref["id"]) not in observed_contexts:
            delivered_contexts.add(c.text(ref["id"]))
            context_inputs[c.text(ref["id"])] = context_payload
    if delivered_contexts:
        operations, oq = c._history(runtime, "operation", {"payload.request.operation": "context.assemble"})
        if oq["complete"] is not True:
            raise c.SupportError("history_incomplete", "Context acquisition-parent history is incomplete")
        for operation in operations:
            payload = c.as_object(operation["payload"]); response = c.as_object(payload["response_without_evidence"])
            result = response.get("result")
            if not isinstance(result, dict) or not isinstance(result.get("artifact"), dict):
                continue
            if c.as_object(result["artifact"])["id"] in delivered_contexts:
                delivered_refs.update(c.text(c.as_object(ref)["id"]) for ref in c.as_list(payload["acquisitions"]))
    exposed: list[c.Object] = []
    for context_id, context_payload in context_inputs.items():
        scoped = context_payload.get("composition")
        if not isinstance(scoped, dict) or "input_sources" not in scoped:
            raise c.SupportError("history_incomplete", "Prior authored Context has no complete retained composition provenance")
        exposed.extend(c.as_object(item) for item in c.as_list(scoped["input_sources"]))
    for envelope in records:
        payload = c.as_object(envelope["payload"])
        # Public content can have been written before a transport receipt was
        # retained. Prepared-only public records are possible exposure; they
        # are not relabelled as observed delivery.
        if "sha256:" + c.digest(envelope) not in delivered_refs and payload.get("channel") != "public-response":
            continue
        scope = payload.get("composition")
        if not isinstance(scope, dict):
            # Unscoped earlier content has unknown derivation; never infer that
            # a new policy retrospectively established its complete provenance.
            source = c.as_object(payload["source"])
            exposed.append({"id": "unclassified-prior-source", "source": source, "complete": False,
                            "origins": [{"id": "unclassified-prior-source", "source": source, "locator": _locator(runtime, source), "complete": False}]})
        else:
            exposed.extend(c.as_object(item) for item in c.as_list(scope["resources"]))
    return exposed


def prior_exposure(runtime: c.Runtime, principal: str) -> None:
    if runtime.composition is None:
        return
    _, binding = _binding(runtime, principal)
    if binding["clean_room"] is not True:
        return
    actor = c.as_object(c.as_object(runtime.policy["principals"])[principal])
    for snapshot in _exposures(runtime, c.text(actor["actor_id"])):
        try:
            _eligible(runtime, binding, snapshot, require_allow=False)
        except c.SupportError as exc:
            raise c.SupportError("basis_stale", "Prior actor exposure prevents this clean-room continuation; eligible re-entry is required") from exc


def context(runtime: c.Runtime, payload: c.Object, principal: str) -> None:
    if runtime.composition is None:
        return
    route(runtime, principal); prior_exposure(runtime, principal)
    for source in c._context_material_sources(payload):
        authorize_source(runtime, c.as_object(source), principal)
    saved = payload.get("composition")
    if not isinstance(saved, dict) or saved.get("declaration") != runtime.policy["composition"]:
        raise c.SupportError("basis_stale", "Context composition binding differs; assemble a current context")


def output_sources(runtime: c.Runtime, attempt_ref: c.Object) -> list[c.Object]:
    attempt = c.as_object(c.load_artifact(runtime, attempt_ref, "attempt")["payload"])
    context_payload = c.as_object(c.load_artifact(runtime, c.as_object(attempt["context"]), "context")["payload"])
    saved = context_payload.get("composition")
    if not isinstance(saved, dict):
        raise c.SupportError("basis_missing", "Actor output has no retained composition provenance binding")
    snapshots = [c.as_object(item) for item in c.as_list(saved["output_sources"])]
    if saved["output_complete"] is not True:
        snapshots.append(_unknown(saved["declaration"]))
    actor = c.as_object(c.as_object(context_payload["packet"])["actor_authority"])
    snapshots.extend(_exposures(runtime, c.text(actor["actor_id"])))
    return snapshots


def authorize_output(runtime: c.Runtime, attempt_ref: c.Object) -> list[c.Object]:
    if runtime.composition is None:
        return []
    _, binding = _binding(runtime, runtime.principal_id)
    snapshots = output_sources(runtime, attempt_ref)
    for snapshot in snapshots:
        _eligible(runtime, binding, snapshot, require_allow=True)
    return snapshots


def context_binding(runtime: c.Runtime, packet: c.Object, principal: str) -> c.Object | None:
    if runtime.composition is None:
        return None
    doc, binding = _binding(runtime, principal)
    output = c.as_object(binding["output"]); resources = c.as_object(doc["resources"])
    snapshots = [_snapshot(runtime, resources, name) for name in c._strings(output["sources"])]
    if output["complete"] is not True:
        snapshots.append(_unknown(runtime.policy["composition"]))
    for snapshot in snapshots:
        _eligible(runtime, binding, snapshot, require_allow=True)
    inputs = authored_context(runtime, principal)
    for ref in c._all_source_refs(packet):
        scope = authorize_source(runtime, ref, principal)
        if scope is not None:
            inputs.extend(c.as_object(item) for item in c.as_list(scope["resources"]))
    snapshots.extend(inputs)
    return c.document({"declaration": runtime.policy["composition"], "engagement": binding["engagement"],
            "purpose": binding["purpose"], "route": binding["route"],
            "output_complete": output["complete"], "output_sources": snapshots,
            "input_sources": inputs,
            "declared_input_provenance_complete": all(item["complete"] is True for item in inputs)})


def authored_context(runtime: c.Runtime, target: str) -> list[c.Object]:
    """Inline packet text is requester-produced content, not exempt source data."""
    doc, producer = _binding(runtime, runtime.principal_id)
    _, receiver = _binding(runtime, target)
    output = c.as_object(producer["output"])
    resources = c.as_object(doc["resources"])
    snapshots = [_snapshot(runtime, resources, name) for name in c._strings(output["sources"])]
    if output["complete"] is not True:
        snapshots.append(_unknown(runtime.policy["composition"]))
    snapshots.extend(_exposures(runtime, c.text(runtime.principal["actor_id"])))
    for snapshot in snapshots:
        _eligible(runtime, receiver, snapshot, require_allow=True)
    return snapshots


def evidence(runtime: c.Runtime, envelope: c.Object) -> list[c.Object]:
    """Only known inline-content carriers are qualified for mediated readback."""
    payload = c.as_object(envelope["payload"]); kind = envelope["kind"]
    # A raw retained envelope also contains metadata/source coordinates.  Exact
    # readback cannot silently redact an excluded origin from those bytes.
    for ref in c._all_source_refs(envelope):
        authorize_source(runtime, ref)
    if kind == "context":
        raise c.SupportError("unsupported_contract", "Whole Context envelopes contain protected composition metadata; use admitted actor delivery")
    if kind == "return":
        if c.as_object(payload["producer"]).get("authenticated") is not True:
            raise c.SupportError("basis_missing", "Unauthenticated return has no qualified composition disclosure path")
        return authorize_output(runtime, c.as_object(payload["attempt"]))
    if kind == "raw" and payload.get("schema") == "a_c.fd-support.process-output/1" and payload.get("complete") is True:
        attempt_ref = c.as_object(payload["attempt"])
        events, query = c._history(runtime, "raw", {"payload.schema": "a_c.fd-support.attempt-event/1", "payload.attempt.id": attempt_ref["id"], "payload.kind": "output_finalized"})
        output_ref: c.Object = {"id": "sha256:" + c.digest(envelope), "sha256": c.digest(envelope)}
        if query["complete"] is not True or not any(any(c.as_object(c.as_object(event["payload"])["data"]).get(stream) == output_ref for stream in ("stdout", "stderr")) for event in events):
            raise c.SupportError("basis_missing", "Output has no actual finalized process provenance")
        return authorize_output(runtime, attempt_ref)
    raise c.SupportError("unsupported_contract", "This retained-content shape has no qualified composition disclosure path")


def before(runtime: c.Runtime, request: c.Object) -> None:
    if runtime.composition is None:
        return
    operation = c.text(request["operation"])
    if operation not in SUPPORTED:
        raise c.SupportError("unsupported_contract", "Operation has no qualified composition disclosure path")
    if operation in CONTROL:
        # Existing operation/grant ownership still applies, even when the
        # previously selected composition contract has advanced or been revoked.
        return
    binding = route(runtime, runtime.principal_id)
    if operation not in c._strings(binding["operations"]):
        raise c.SupportError("authority_missing", "Operation is absent from the selected composition binding")
    if operation not in ("tools.describe", "composition.inspect"):
        prior_exposure(runtime, runtime.principal_id)
    args = c.as_object(request["arguments"])
    if operation == "tools.describe" and args.get("operation") is not None and args["operation"] not in SUPPORTED:
        raise c.SupportError("unsupported_contract", "Requested operation is outside the selected composition fragment")
    if operation in ("source.read", "records.find", "records.read", "graph.project", "work.project", "review.prepare"):
        for ref in c._all_source_refs(args):
            authorize_source(runtime, ref)
    if operation == "review.prepare" and args.get("expectations") is not None:
        prior = c.load_artifact(runtime, c.as_object(args["expectations"]), "expectation")
        provenance = c.as_object(prior["provenance"])
        if c.as_object(provenance["actor"])["actor_id"] != runtime.principal["actor_id"] or provenance["policy_sha256"] != runtime.policy_sha256:
            raise c.SupportError("unsupported_contract", "Review expectation disclosure requires its original actor and exact policy")
    if operation == "context.assemble":
        packet = c.as_object(args["packet"]); principal, _ = c._validate_packet(runtime, packet)
        route(runtime, principal); prior_exposure(runtime, principal)
        authored_context(runtime, principal)
        for ref in [*c._all_source_refs(packet), *c._all_source_refs(args["models"]), *[c.as_object(item) for item in c.as_list(args["sources"])], *[c.as_object(item) for item in c.as_list(args["late_acquisition"])]]:
            authorize_source(runtime, ref)
            authorize_source(runtime, ref, principal)
        for ref in c._all_source_refs(args["envelope"]):
            authorize_source(runtime, ref)
    elif operation == "workspace.observe":
        resources = c.as_object(cast(c.Object, runtime.composition)["resources"])
        for raw in c.as_list(args["scope"]):
            scope = c.as_object(raw)
            if scope["kind"] != "file":
                raise c.SupportError("unsupported_contract", "Composition observation requires explicit file scopes")
            matching = [c.as_object(c.as_object(resources[name])["source"]) for name in c._strings(binding["allow"]) if c.as_object(c.as_object(resources[name])["source"])["root"] == scope["root"] and c.as_object(c.as_object(resources[name])["source"])["path"] == scope["path"]]
            if not matching or any(ref["selector"] is not None for ref in matching):
                raise c.SupportError("acquisition_denied", "Observed file is not allowed as a whole source")
            for ref in matching:
                authorize_source(runtime, ref)
    elif operation == "evidence.read":
        evidence(runtime, c.load_artifact(runtime, c.as_object(args["artifact"])))
    elif operation == "contract.preflight":
        grant = c.as_object(c.as_object(runtime.policy["grants"])[c.text(args["grant_id"])])
        admission = c.as_object(grant["admission"])
        if c.as_list(admission["required_predicates"]) or "admission_record" in args or c.as_list(args["observations"]):
            raise c.SupportError("unsupported_contract", "Additional admission evaluations, overrides and retained observations need a composition disclosure contract")
        for ref in c._all_source_refs(grant):
            authorize_source(runtime, ref)
        if any(isinstance(ref, dict) and set(ref) == {"id", "sha256"} for ref in c.as_list(grant["preconditions"])):
            raise c.SupportError("unsupported_contract", "Retained admission preconditions need a composition disclosure contract")
    elif operation == "return.capture":
        authorize_source(runtime, c.as_object(args["return_contract"]))
        envelope = c.load_artifact(runtime, c.as_object(args["payload"]), "raw")
        payload = c.as_object(envelope["payload"])
        if payload.get("attempt") != args["attempt"]:
            raise c.SupportError("basis_stale", "Output disclosure binds another attempt")
        evidence(runtime, envelope)
        authorize_output(runtime, c.as_object(args["attempt"]))
    elif operation == "return.check":
        envelope = c.load_artifact(runtime, c.as_object(args["return"]), "return")
        evidence(runtime, envelope)
        retained = c.as_object(envelope["payload"])
        attempt = c.as_object(c.load_artifact(runtime, c.as_object(retained["attempt"]), "attempt")["payload"])
        if args["context"] != attempt["context"] or c.as_list(args["observations"]) or c.as_list(args["predicates"]):
            raise c.SupportError("unsupported_contract", "Alternate Contexts and extra return evaluations need a composition disclosure contract")
        authorize_output(runtime, c.as_object(retained["attempt"]))


def inspect(runtime: c.Runtime) -> c.Object:
    if runtime.composition is None:
        return c.document({"selected": False, "supported_operations": sorted(SUPPORTED)})
    binding = route(runtime, runtime.principal_id)
    return c.document({"selected": True, "declaration": runtime.policy["composition"],
            "principal": runtime.principal_id, "actor_id": runtime.principal["actor_id"],
            "engagement": binding["engagement"], "purpose": binding["purpose"],
            "route": binding["route"], "allowed_resource_ids": binding["allow"],
            "supported_operations": sorted(SUPPORTED.intersection(c._strings(binding["operations"]))),
            "enforcement": "operator-declared mediated acquisition only; no host isolation",
            "semantic_adequacy": "not assessed"})


def finish(runtime: c.Runtime, request: c.Object, outcome: c.CoreOutcome) -> c.CoreOutcome:
    if runtime.composition is None or outcome.get("result") is None:
        return outcome
    operation = c.text(request["operation"])
    if operation == "tools.describe":
        value = c.as_object(c.as_object(outcome["result"])["value"])
        value["operations"] = [item for item in c.as_list(value["operations"]) if c.as_object(item)["name"] in SUPPORTED]
    if operation == "contract.preflight":
        result = c.as_object(outcome["result"]); value = c.as_object(result["value"])
        result["value"] = {key: value[key] for key in ("context", "contract_sha256", "grant_id", "executor_id", "result_key", "requester", "target", "contract_state", "decision")}
        c.as_object(result["value"])["checks"] = [{"predicate": c.as_object(item)["predicate"], "core_value": c.as_object(item)["core_value"]} for item in c.as_list(value["evaluations"])]
    if operation in ("return.capture", "return.check"):
        args = c.as_object(request["arguments"])
        result = c.as_object(outcome["result"])
        if operation == "return.capture":
            attempt = c.as_object(args["attempt"]); retained = c.as_object(result["artifact"])
        else:
            retained = c.as_object(args["return"])
            original = c.as_object(c.load_artifact(runtime, retained, "return")["payload"])
            attempt = c.as_object(original["attempt"])
        snapshots = authorize_output(runtime, attempt)
        _, binding = _binding(runtime, runtime.principal_id)
        now = time.time_ns()
        payload: c.Object = {"schema": "a_c.fd-support.acquisition/1", "recipient": runtime.principal["actor_id"],
                            "source": {"engine": "retained-evidence", "root": "evidence", "path": retained["id"], "object": None, "sha256": retained["sha256"], "selector": None},
                            "model": None, "selection": None, "operation": operation,
                            "content_sha256": c.digest(result["value"]), "channel": "public-response",
                            "delivery": {"state": "prepared", "interval": {"clock": "unix_ns", "started_ns": now, "ended_ns": now}},
                            "composition": {"declaration": runtime.policy["composition"], "actor_id": runtime.principal["actor_id"], "engagement": binding["engagement"], "purpose": binding["purpose"], "route": binding["route"], "resources": cast(list[c.JSON], snapshots)}}
        envelope, ref = c.make_artifact("acquisition", payload, c.provenance(runtime, request, now, now))
        c.as_list(outcome["artifacts"]).append(envelope); c.as_list(outcome["acquisitions"]).append(ref)
    if operation in ("dispatch.observe", "events.wait"):
        result = c.as_object(outcome["result"]); value = c.as_object(result["value"])
        # Wait has a nested observation. Keep only control facts and protected
        # output locators, never arbitrary executor/event payloads.
        def redact(raw: c.Object) -> c.Object:
            keep = {key: copy.deepcopy(raw[key]) for key in ("attempt", "cursor", "process_end", "consumer_receipt") if key in raw}
            keep["history_complete"] = not c.as_list(raw.get("history_gaps", []))
            output = raw.get("output")
            if isinstance(output, dict):
                keep["output"] = {key: output[key] for key in ("stdout", "stderr", "process_end") if key in output}
            keep["effect"] = {"value": "completion_unknown", "end_established": False}
            keep["limits"] = ["Redacted control view; content readback requires its own composition permission."]
            return keep
        if isinstance(value.get("observation"), dict):
            value["observation"] = redact(c.as_object(value["observation"]))
        else:
            result["value"] = redact(value)
    return outcome
