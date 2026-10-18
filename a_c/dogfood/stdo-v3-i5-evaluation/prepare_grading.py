#!/usr/bin/env python3
"""Copy original answers into condition-blinded, source-grounded packets.

Run only after all eight actor processes terminate. The private map is never
given to the graders. No original answer, protocol or oracle is rewritten.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import secrets
import sys

ROOT = Path(__file__).resolve().parent


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def write(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as handle:
        json.dump(value, handle, ensure_ascii=False, sort_keys=True, indent=2)
        handle.write("\n")


def factor_sources(value, table, index):
    """Deduplicate exact source passages; preserve every field via references."""
    if isinstance(value, dict):
        if {"path", "quote", "source_sha256", "line_start", "line_end"} <= set(value):
            identity = sha(json.dumps(value, sort_keys=True, ensure_ascii=False).encode())
            if identity not in index:
                key = f"S{len(table)+1:03}"
                index[identity] = key
                table[key] = value
            return dict(source_ref=index[identity])
        return {key: factor_sources(child, table, index) for key, child in value.items()}
    if isinstance(value, list):
        return [factor_sources(child, table, index) for child in value]
    return value


def strings(value):
    if isinstance(value, dict):
        for child in value.values():
            yield from strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from strings(child)
    elif isinstance(value, str):
        yield value
        if value.startswith(("{", "[")):
            try:
                yield from strings(json.loads(value))
            except ValueError:
                pass


def source_checks(tenant: str, answer: dict, reader, directory: Path) -> list[dict]:
    baseline = reader.Baseline(ROOT / "baselines" / tenant, tenant)
    emitted = []
    audit = directory / "tool-audit.jsonl"
    for line in audit.read_text().splitlines() if audit.exists() else []:
        event = json.loads(line)
        if event.get("event") == "tool_call" and event.get("emitted_text"):
            emitted.extend(strings(json.loads(event["emitted_text"])))
    result = []
    for task in answer.get("tasks", []):
        citations = []
        for number, citation in enumerate(task.get("sources", [])):
            row = dict(index=number, supplied=citation)
            try:
                path, uri_anchor = baseline.resolve(citation["path"])
                raw = baseline.text(path)
                anchor = citation["anchor"] or uri_anchor or ""
                quote = citation["quote"]
                if not quote:
                    raise ValueError("empty quote")
                row.update(path_allowlisted=True, source_sha256=sha(baseline.sources[path]),
                           exact_quote_in_member=quote in raw,
                           whitespace_normalized_quote_in_member=" ".join(quote.split()) in " ".join(raw.split()),
                           exact_quote_observed=any(quote in text for text in emitted),
                           whitespace_normalized_quote_observed=any(" ".join(quote.split()) in " ".join(text.split()) for text in emitted))
                # Permit exact line coordinates when a source has no heading.
                line_matches=list(re.finditer(r"(?:^|[\s,(;])(?:#?L|lines?\s+)(\d+)(?:\s*[-:\u2013\u2014]\s*(?:L)?(\d+))?(?=$|[\s,;)])", anchor, re.I))
                if len(line_matches)>1:
                    raise ValueError("multiple ambiguous explicit line coordinates")
                if line_matches:
                    line=line_matches[0]
                    start, end = int(line[1]), int(line[2] or line[1])
                    if not 1 <= start <= end <= len(baseline.lines(path)):
                        raise ValueError("line coordinate out of range")
                    row["coordinate_interpretation"]="explicit line coordinate, including a combined heading plus line reference"
                else:
                    start, end = reader.Server.anchor_range(baseline.lines(path), anchor)
                    row["coordinate_interpretation"]="literal Markdown heading or explicit anchor"
                section = "".join(baseline.lines(path)[start-1:end])
                row.update(coordinate_valid=True, line_start=start, line_end=end,
                           exact_quote_at_coordinate=quote in section,
                           whitespace_normalized_quote_at_coordinate=" ".join(quote.split()) in " ".join(section.split()))
                row["strict_citation_valid"] = row["exact_quote_at_coordinate"]
            except (ValueError, KeyError, TypeError) as exc:
                row.update(strict_citation_valid=False, error=str(exc))
            citations.append(row)
        result.append(dict(task_id=task["id"], citations=citations,
                           strict_valid_count=sum(row["strict_citation_valid"] for row in citations)))
    return result


def main() -> None:
    freeze = json.loads((ROOT / "freeze.json").read_bytes())
    for name, pin in freeze["files"].items():
        if sha((ROOT / name).read_bytes()) != pin["sha256"]:
            raise ValueError("pre-answer frozen file changed: " + name)
    schedule = json.loads((ROOT / "schedule.json").read_bytes())["runs"]
    for run in schedule:
        if not (ROOT / "runs" / run["id"] / "execution/summary.json").exists():
            raise ValueError("all scheduled runs must terminate first")
    spec = importlib.util.spec_from_file_location("ac_study_citation_reader", ROOT / "tools/study_mcp.py")
    reader = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = reader
    spec.loader.exec_module(reader)
    tasks = json.loads((ROOT / "private/tasks.json").read_bytes())["candidates"]
    oracle = json.loads((ROOT / "private/oracle.json").read_bytes())
    mapping = []
    for tenant in ("codex", "claude"):
        packets = []
        for run in schedule:
            if run["candidate"] != tenant:
                continue
            identity = secrets.token_hex(6)
            directory = ROOT / "runs" / run["id"] / "execution"
            raw = (directory / "answer.json").read_bytes() if (directory / "answer.json").exists() else b"{}"
            try:
                answer = json.loads(raw)
            except ValueError:
                answer = {}
            checks = source_checks(tenant, answer, reader, directory)
            packets.append(dict(label=identity, answer=answer, original_answer_sha256=sha(raw),
                                mechanical_citation_checks=checks))
            mapping.append(dict(label=identity, run_id=run["id"], candidate=tenant,
                                condition=run["condition"], answer_sha256=sha(raw)))
        secrets.SystemRandom().shuffle(packets)
        passages = {}
        compact_oracle = factor_sources(oracle["candidates"][tenant], passages, {})
        guide = dict(
            purpose="Nonauthor, condition-blinded semantic assessment of bounded dogfood outputs. No acceptance.",
            allowed_read_scope=[str(ROOT / "grading" / tenant), str(ROOT / "baselines" / tenant / "sources")],
            excluded_scope="Do not read run folders, protocol, schedule, private map, usage, tool logs or other study files.",
            grades=["met", "partial", "missed", "incorrect"],
            criterion_policy="Met=full faithful meaning. Partial=some faithful subset with no material contradiction. Missed=absent/undecidable. Incorrect=material contradiction. Semantic equivalence earns credit; tool choice/verbosity/preferred phrasing earns none.",
            score_policy="Expected criteria only; critical weight2, ordinary weight1; met1, partial0.5, missed/incorrect0. Prohibitions give no credit for silence and veto passing when asserted.",
            pass_policy="Every critical criterion met, no prohibited claim asserted, weighted score>=80%, and at least one exact documentary citation valid at its section/line and semantically supporting a deciding claim. A threshold pass can still contain noncritical omissions.",
            instruction="For EACH anonymous answer and EACH of its four questions, judge every frozen expected criterion with short answer excerpt and reason, every prohibited claim (asserted/absent/ambiguous), citation relevance, unsupported claims and any answer-level condition/tool-use disclosure. Preserve positive, negative and unresolved branches on stipulated facts. Source quotes in the oracle are exact; re-enter the allowed owner documents where needed. Mechanical checks do not judge semantic relevance. Do not repair, rewrite or author actor answers.",
            source_table="Each source_coordinates source_ref resolves to the complete exact passage in source_passages; duplicate passages are factored without omitted content.",
            output_contract="Write grades.json in your own grading/<candidate>/ folder only. Top object: profile, candidate, assessor, answers:[{label,tasks:[{id,criteria:[{id,grade,answer_excerpt,reason}],prohibitions:[{id,status,reason}],supporting_valid_citation_indices:[integers],citation_notes,unsupported_claims:[strings],blinding_disclosures:[strings]}]}], limitations:[strings]. Include all32 expected criteria and12 prohibitions across4 tasks for every answer; no condition guesses. Score aggregation will be mechanical later.",
        )
        write(ROOT / "grading" / tenant / "packet.json", dict(profile="ac.eval.blind-packet/1", candidate=tenant,
              frozen_oracle_sha256=sha((ROOT/"private/oracle.json").read_bytes()),
              frozen_tasks_sha256=sha((ROOT/"private/tasks.json").read_bytes()),
              guide=guide, tasks=tasks[tenant], oracle=compact_oracle, source_passages=passages, answers=packets))
    write(ROOT / "private/grade-map.json", dict(profile="ac.eval.private-grade-map/1", mappings=mapping))
    print(json.dumps(dict(status="blind_packets_prepared", candidates=2, answers=len(mapping))))


if __name__ == "__main__":
    main()
