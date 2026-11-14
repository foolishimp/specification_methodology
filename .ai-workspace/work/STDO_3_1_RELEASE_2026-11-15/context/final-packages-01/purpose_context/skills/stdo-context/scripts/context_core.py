#!/usr/bin/env python3
"""Purpose-built context from exact selected source documents.

Mechanical selection and delivery checks do not establish semantic coverage.
Native authoring is supplied by the caller; this module never invokes a model.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
CONTRACT = HERE.parent / "references"
CORPUS_PROFILE = "stdo.context-corpus/1"
INDEX_PROFILE = "stdo.context-index/1"
VIEW_PROFILE = "stdo.context-view/1"
CONTEXT_PROFILE = "stdo.context/1"
RULE_FIELDS = {"id", "kind", "text", "when", "conditions", "exceptions", "depends_on", "precedence", "source_refs", "unknowns"}
KINDS = {"obligation", "prohibition", "permission", "definition", "verification"}


class Refusal(ValueError):
    """An exact input, supported contract or mechanical obligation failed."""


def need(condition: bool, message: str) -> None:
    if not condition:
        raise Refusal(message)


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def raw_digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def read_json(path: str | Path) -> dict[str, Any]:
    result = json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=_pairs,
                        parse_constant=lambda value: (_ for _ in ()).throw(Refusal("nonfinite JSON: " + value)))
    need(isinstance(result, dict), "JSON root must be an object")
    return result


def _object(value: Any, fields: set[str], where: str) -> None:
    need(isinstance(value, dict) and set(value) == fields, where + ": unexpected/missing fields")


def _text(value: Any, where: str) -> None:
    need(isinstance(value, str) and bool(value.strip()), where + ": nonempty text required")


def _sha(value: Any, where: str) -> None:
    need(isinstance(value, str) and bool(re.fullmatch(r"[0-9a-f]{64}", value)), where + ": SHA-256 required")


def _strings(value: Any, where: str) -> None:
    need(isinstance(value, list), where + ": list required")
    for item in value:
        _text(item, where)
    need(len(set(value)) == len(value), where + ": duplicate value")


def load_corpus(manifest: dict[str, Any] | str | Path) -> dict[str, Any]:
    """Reacquire every corpus member, retaining source content outside views."""
    value = read_json(manifest) if isinstance(manifest, (str, Path)) else copy.deepcopy(manifest)
    _object(value, {"profile", "subject_id", "method", "files"}, "corpus")
    need(value["profile"] == CORPUS_PROFILE, "unsupported corpus profile")
    _text(value["subject_id"], "subject_id")
    _object(value["method"], {"uri", "manifest_sha256"}, "method")
    _text(value["method"]["uri"], "method.uri")
    _sha(value["method"]["manifest_sha256"], "method.manifest_sha256")
    need(isinstance(value["files"], list) and bool(value["files"]), "nonempty corpus required")
    members: list[dict[str, Any]] = []
    seen: set[str] = set()
    for entry in value["files"]:
        _object(entry, {"id", "path", "sha256"}, "source")
        _text(entry["id"], "source.id")
        _sha(entry["sha256"], "source.sha256")
        need(entry["id"] not in seen, "duplicate source identity")
        seen.add(entry["id"])
        path = Path(entry["path"])
        need(path.is_absolute() and path.is_file() and not path.is_symlink(), "source must be an existing absolute regular file")
        need(all(not parent.is_symlink() for parent in path.parents), "symlink source ancestor")
        data = path.read_bytes()
        need(raw_digest(data) == entry["sha256"], "stale source: " + entry["id"])
        text = data.decode("utf-8")
        members.append({**entry, "text": text, "line_count": len(text.splitlines())})
    identity = {"profile": value["profile"], "subject_id": value["subject_id"], "method": value["method"],
                "files": [{"id": row["id"], "sha256": row["sha256"]} for row in value["files"]]}
    return {"manifest": value, "corpus_sha256": digest(identity), "members": members}


def _source_refs(refs: Any, corpus: dict[str, Any], where: str, *, nonempty: bool = True) -> None:
    need(isinstance(refs, list) and (bool(refs) or not nonempty), where + ": source refs required")
    members = {row["id"]: row for row in corpus["members"]}
    for ref in refs:
        _object(ref, {"source_id", "start_line", "end_line"}, where)
        need(ref["source_id"] in members, where + ": unknown source")
        need(type(ref["start_line"]) is int and type(ref["end_line"]) is int and
             1 <= ref["start_line"] <= ref["end_line"] <= members[ref["source_id"]]["line_count"], where + ": invalid source interval")
    need(len({canonical(ref) for ref in refs}) == len(refs), where + ": duplicate source ref")


def _source_view(corpus: dict[str, Any]) -> dict[str, Any]:
    docs = [{"id": row["id"], "content": "".join(f"{number}: {line}\n" for number, line in enumerate(row["text"].splitlines(), 1)),
             "source_refs": [] if not row["line_count"] else [{"source_id": row["id"], "start_line": 1, "end_line": row["line_count"]}]}
            for row in corpus["members"]]
    result = {"profile": VIEW_PROFILE, "encoding": "prose", "corpus_sha256": corpus["corpus_sha256"],
              "representation_sha256": None,
              "source_catalog": [{"id": row["id"], "sha256": row["sha256"], "line_count": row["line_count"]} for row in corpus["members"]],
              "documents": docs}
    result["view_sha256"] = digest(result)
    return result


def corpus_view(manifest: dict[str, Any] | str | Path) -> dict[str, Any]:
    """Exact numbered source text; no semantic rewriting or provider dependency."""
    return _source_view(load_corpus(manifest))


def check_view(view: dict[str, Any], corpus: dict[str, Any]) -> None:
    need(view == _source_view(corpus), "source view differs from exact selected corpus")


def validate_purpose(purpose: dict[str, Any]) -> None:
    _object(purpose, {"id", "description", "facts"}, "purpose")
    _text(purpose["id"], "purpose.id")
    _text(purpose["description"], "purpose.description")
    need(isinstance(purpose["facts"], dict), "purpose.facts must map fact names to their meanings")
    for name, meaning in purpose["facts"].items():
        _text(name, "purpose fact name")
        _text(meaning, "purpose fact meaning")
    canonical(purpose)


def build_prompt(view: dict[str, Any], purpose: dict[str, Any], reader_instructions: str = "") -> str:
    validate_purpose(purpose)
    instructions = (CONTRACT / "authoring.md").read_text(encoding="utf-8")
    binding = {"purpose": purpose, "purpose_sha256": digest(purpose), "corpus_sha256": view["corpus_sha256"],
               "input_view_sha256": view["view_sha256"], "source_catalog": view["source_catalog"]}
    return instructions + "\n\nEXACT INPUT\n" + canonical(binding).decode() + "\n\nSOURCE ACCESS\n" + reader_instructions + "\n\nOUTPUT SCHEMA\n" + (CONTRACT / "index.schema.json").read_text(encoding="utf-8")


def _guard(value: Any, where: str) -> None:
    _object(value, {"all", "any"}, where)
    for operator in ("all", "any"):
        need(isinstance(value[operator], list), where + ": predicates must be a list")
        for clause in value[operator]:
            _object(clause, {"fact", "op", "value"}, where)
            _text(clause["fact"], where)
            need(clause["op"] in {"eq", "ne", "contains", "not_contains"}, where + ": unsupported predicate")
            need(type(clause["value"]) in {str, bool, int}, where + ": scalar predicate value required")


def _same(left: Any, right: Any) -> bool:
    return type(left) is type(right) and left == right


def evaluate_guard(guard: dict[str, Any], facts: dict[str, Any]) -> str:
    """Three-valued predicate evaluation; missing/null/type-mismatched is unknown."""
    _guard(guard, "guard")
    def clause(item: dict[str, Any]) -> str:
        if item["fact"] not in facts or facts[item["fact"]] is None:
            return "unknown"
        actual, wanted = facts[item["fact"]], item["value"]
        if item["op"] in {"eq", "ne"}:
            if type(actual) is not type(wanted):
                return "unknown"
            yes = _same(actual, wanted)
            if item["op"] == "ne":
                yes = not yes
        else:
            if not isinstance(actual, list):
                return "unknown"
            yes = any(_same(value, wanted) for value in actual)
            if item["op"] == "not_contains":
                yes = not yes
        return "true" if yes else "false"
    all_values = [clause(item) for item in guard["all"]]
    any_values = [clause(item) for item in guard["any"]]
    all_result = "false" if "false" in all_values else "unknown" if "unknown" in all_values else "true"
    any_result = "true" if not any_values or "true" in any_values else "unknown" if "unknown" in any_values else "false"
    return "false" if "false" in (all_result, any_result) else "unknown" if "unknown" in (all_result, any_result) else "true"


def validate_index(index: dict[str, Any], manifest: dict[str, Any] | str | Path,
                   purpose: dict[str, Any], view: dict[str, Any] | None = None) -> dict[str, Any]:
    corpus = load_corpus(manifest)
    validate_purpose(purpose)
    _object(index, {"profile", "corpus_sha256", "input_view_sha256", "purpose_id", "purpose_sha256", "rules", "source_coverage", "unresolved"}, "index")
    need(index["profile"] == INDEX_PROFILE, "unsupported index profile")
    need(index["corpus_sha256"] == corpus["corpus_sha256"], "index corpus differs")
    _sha(index["input_view_sha256"], "input_view_sha256")
    need(index["purpose_id"] == purpose["id"] and index["purpose_sha256"] == digest(purpose), "index purpose differs")
    need(index["input_view_sha256"] == _source_view(corpus)["view_sha256"], "index source view differs")
    if view is not None:
        check_view(view, corpus)
        need(index["input_view_sha256"] == view["view_sha256"], "index input view differs")
    need(isinstance(index["rules"], list), "rules must be a list")
    rules: dict[str, dict[str, Any]] = {}
    for rule in index["rules"]:
        _object(rule, RULE_FIELDS, "rule")
        _text(rule["id"], "rule.id")
        need(rule["id"] not in rules, "duplicate rule identity")
        rules[rule["id"]] = rule
        need(rule["kind"] in KINDS, "unsupported rule kind")
        _text(rule["text"], "rule.text")
        _guard(rule["when"], "rule.when")
        need(all(item["fact"] in purpose["facts"] for items in rule["when"].values() for item in items), "rule guard names undeclared purpose fact")
        for field in ("conditions", "depends_on", "unknowns"):
            _strings(rule[field], "rule." + field)
        _source_refs(rule["source_refs"], corpus, "rule.source_refs")
        need(isinstance(rule["exceptions"], list), "exceptions must be a list")
        for exception in rule["exceptions"]:
            _object(exception, {"when", "text"}, "exception")
            _guard(exception["when"], "exception.when")
            need(all(item["fact"] in purpose["facts"] for items in exception["when"].values() for item in items), "exception guard names undeclared purpose fact")
            _text(exception["text"], "exception.text")
        need(isinstance(rule["precedence"], list), "precedence must be a list")
        for precedence in rule["precedence"]:
            _object(precedence, {"over", "reason"}, "precedence")
            _text(precedence["over"], "precedence.over")
            _text(precedence["reason"], "precedence.reason")
    for rule in rules.values():
        need(all(target in rules and target != rule["id"] for target in rule["depends_on"]), "missing/self rule dependency")
        need(all(item["over"] in rules and item["over"] != rule["id"] for item in rule["precedence"]), "missing/self precedence target")
    visiting: set[str] = set()
    done: set[str] = set()
    def precedence_walk(ident: str) -> None:
        need(ident not in visiting, "cyclic precedence")
        if ident in done:
            return
        visiting.add(ident)
        for edge in rules[ident]["precedence"]:
            precedence_walk(edge["over"])
        visiting.remove(ident)
        done.add(ident)
    for ident in rules:
        precedence_walk(ident)
    need(isinstance(index["source_coverage"], list), "source coverage ledger required")
    source_ids = [entry["id"] for entry in corpus["members"]]
    coverage_ids: list[str] = []
    for entry in index["source_coverage"]:
        _object(entry, {"source_id", "status", "rule_ids", "reason"}, "source coverage")
        coverage_ids.append(entry["source_id"])
        need(entry["status"] in {"represented", "no_applicable_rules", "unresolved"}, "unsupported processing disposition")
        _strings(entry["rule_ids"], "source coverage.rule_ids")
        _text(entry["reason"], "source coverage.reason")
        need(all(ident in rules for ident in entry["rule_ids"]), "coverage names missing rule")
        expected = {rule["id"] for rule in rules.values() if any(ref["source_id"] == entry["source_id"] for ref in rule["source_refs"])}
        need(set(entry["rule_ids"]) == expected, "source coverage loses or invents grounded rule")
        need(entry["status"] != "represented" or bool(expected), "represented source has no grounded rule")
        need(entry["status"] != "no_applicable_rules" or not expected, "inapplicable source has grounded rules")
    need(len(coverage_ids) == len(source_ids) and set(coverage_ids) == set(source_ids), "source coverage omits/duplicates corpus members")
    need(isinstance(index["unresolved"], list), "unresolved list required")
    for unresolved in index["unresolved"]:
        _object(unresolved, {"text", "material", "source_refs"}, "unresolved")
        _text(unresolved["text"], "unresolved.text")
        need(type(unresolved["material"]) is bool, "material flag must be bool")
        _source_refs(unresolved["source_refs"], corpus, "unresolved.source_refs", nonempty=False)
    return {"status": "mechanically_valid", "index_sha256": digest(index), "corpus_sha256": corpus["corpus_sha256"],
            "rules": len(rules), "source_members": len(source_ids), "semantic_coverage": "unassessed",
            "limit": "Processing accounting, source intervals and declared relations do not detect omitted source meaning."}


def compile_context(index: dict[str, Any], query: dict[str, Any], manifest: dict[str, Any] | str | Path,
                    purpose: dict[str, Any], assessment: dict[str, Any] | None = None, *, trial_binding: str | None = None,
                    byte_budget: int | None = None) -> dict[str, Any]:
    """Apply shared guards/closure and render retained rules with honest standing."""
    checked = validate_index(index, manifest, purpose)
    _object(query, {"id", "purpose_id", "facts"}, "query")
    _text(query["id"], "query.id")
    need(query["purpose_id"] == index["purpose_id"], "query purpose differs")
    need(isinstance(query["facts"], dict) and all(isinstance(key, str) and key for key in query["facts"]), "query facts must be an object")
    need(set(query["facts"]) <= set(purpose["facts"]), "query names undeclared purpose fact")
    canonical(query)
    rules = {rule["id"]: rule for rule in index["rules"]}
    applicability = {ident: evaluate_guard(rule["when"], query["facts"]) for ident, rule in rules.items()}
    roots = [ident for ident in rules if applicability[ident] != "false"]
    included: set[str] = set()
    reasons: list[dict[str, Any]] = []
    pending = [(None, ident, "applicability:" + applicability[ident]) for ident in roots]
    while pending:
        source, ident, reason = pending.pop(0)
        edge = {"from": source, "to": ident, "reason": reason}
        if edge not in reasons:
            reasons.append(edge)
        if ident in included:
            continue
        included.add(ident)
        pending.extend((ident, target, "dependency") for target in rules[ident]["depends_on"])
        pending.extend((ident, item["over"], "precedence-context") for item in rules[ident]["precedence"])
    selected: list[dict[str, Any]] = []
    gaps: list[dict[str, str]] = []
    for ident, rule in rules.items():
        if ident not in included:
            continue
        exceptions = [{"text": item["text"], "when": copy.deepcopy(item["when"]),
                       "applicability": evaluate_guard(item["when"], query["facts"])} for item in rule["exceptions"]]
        selected.append({"rule": copy.deepcopy(rule), "applicability": applicability[ident], "exception_assessments": exceptions})
        if applicability[ident] == "unknown":
            gaps.append({"rule": ident, "reason": "applicability facts unknown"})
        if any(item["applicability"] == "unknown" for item in exceptions):
            gaps.append({"rule": ident, "reason": "exception applicability unknown"})
        gaps.extend({"rule": ident, "reason": value} for value in rule["unknowns"])
    gaps.extend({"rule": "corpus", "reason": item["text"]} for item in index["unresolved"] if item["material"])
    gaps.extend({"rule": "source:" + item["source_id"], "reason": item["reason"]} for item in index["source_coverage"] if item["status"] == "unresolved")
    semantic = {"status": "unassessed", "assessment": None}
    if assessment is not None:
        _object(assessment, {"index_sha256", "corpus_sha256", "query_sha256", "status", "evaluator", "evidence"}, "assessment")
        need(assessment["index_sha256"] == checked["index_sha256"] and assessment["corpus_sha256"] == checked["corpus_sha256"] and
             assessment["query_sha256"] == digest(query), "assessment exact subject differs")
        need(assessment["status"] in {"supported", "falsified", "unknown"}, "unsupported semantic assessment")
        _text(assessment["evaluator"], "assessment.evaluator")
        _strings(assessment["evidence"], "assessment.evidence")
        need(bool(assessment["evidence"]), "assessment evidence missing")
        semantic = {"status": assessment["status"], "assessment": copy.deepcopy(assessment)}
    covered = not gaps and semantic["status"] == "supported"
    if trial_binding is not None:
        _text(trial_binding, "trial_binding")
    body = {"profile": CONTEXT_PROFILE, "index_sha256": checked["index_sha256"], "corpus_sha256": checked["corpus_sha256"],
            "purpose_sha256": digest(purpose), "query": copy.deepcopy(query), "query_sha256": digest(query), "mechanical_status": "valid",
            "selection_status": "incomplete" if gaps else "ready", "semantic_coverage": semantic,
            "covered": covered, "use": "assessed-context" if covered else "experimental-candidate" if trial_binding else "withheld",
            "trial_binding": trial_binding, "selected": selected, "excluded": [ident for ident in rules if ident not in included],
            "reasons": reasons, "gaps": gaps,
            "limit": "Declared closure and supplied assessment are separate; no automatic source-semantic coverage, actor authority or code-quality theorem."}
    rendered = render_context(body)
    result = {"payload": body, "markdown": rendered, "payload_sha256": digest(body), "markdown_sha256": raw_digest(rendered.encode())}
    if byte_budget is not None:
        need(type(byte_budget) is int and byte_budget >= 0, "byte budget must be nonnegative integer")
        need(len(canonical(result) + b"\n") <= byte_budget, "context budget insufficient; no truncation")
    return result


def render_context(payload: dict[str, Any]) -> str:
    lines = ["# Governing context", "", "Query: " + payload["query"]["id"],
             "Selection: " + payload["selection_status"], "Source-semantic coverage: " + payload["semantic_coverage"]["status"],
             "Use: " + payload["use"], "", "Apply the task's actual requirements and domain. Rules below constrain the work; they supply no task solution."]
    for selected in payload["selected"]:
        rule = selected["rule"]
        lines.extend(["", "## " + rule["id"] + " (" + rule["kind"] + ")", "Applicability: " + selected["applicability"], rule["text"],
                      "Guard: " + canonical(rule["when"]).decode()])
        lines.extend("Condition: " + value for value in rule["conditions"])
        lines.extend("Exception (" + item["applicability"] + "): " + item["text"] + " | guard " + canonical(item["when"]).decode() for item in selected["exception_assessments"])
        lines.extend("Depends on: " + value for value in rule["depends_on"])
        lines.extend("Precedence over " + value["over"] + ": " + value["reason"] for value in rule["precedence"])
        lines.extend("Source: " + value["source_id"] + ":" + str(value["start_line"]) + "-" + str(value["end_line"]) for value in rule["source_refs"])
        lines.extend("Unresolved: " + value for value in rule["unknowns"])
    if payload["gaps"]:
        lines.extend(["", "## Unresolved coverage"])
        lines.extend(item["rule"] + ": " + item["reason"] for item in payload["gaps"])
    lines.extend(["", payload["limit"], ""])
    return "\n".join(lines)


def check_context(actual: dict[str, Any], index: dict[str, Any], query: dict[str, Any],
                  manifest: dict[str, Any] | str | Path, purpose: dict[str, Any], assessment: dict[str, Any] | None = None,
                  *, trial_binding: str | None = None) -> dict[str, Any]:
    """Compare supplied content to expected content; never replace supplied bytes."""
    _object(actual, {"payload", "markdown", "payload_sha256", "markdown_sha256"}, "context")
    need(actual["payload_sha256"] == digest(actual["payload"]), "payload hash mismatch")
    need(actual["markdown_sha256"] == raw_digest(actual["markdown"].encode()), "Markdown hash mismatch")
    supplied = actual["payload"]
    expected = compile_context(index, query, manifest, purpose, assessment, trial_binding=trial_binding)
    need(actual == expected, "supplied context differs from declared selection/rendering")
    return {"status": "content_verified", "payload_sha256": actual["payload_sha256"], "markdown_sha256": actual["markdown_sha256"],
            "semantic_coverage": supplied["semantic_coverage"]["status"], "covered": supplied["covered"],
            "limit": "Exact supplied content compared with separately selected inputs. Recipient receipt, authority and assessment authenticity remain external."}


