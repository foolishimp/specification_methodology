#!/usr/bin/env python3
"""Validate blind assessments, then unblind and aggregate frozen-pilot evidence."""
from __future__ import annotations
from collections import Counter
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GRADES = {"met": 1, "partial": .5, "missed": 0, "incorrect": 0}


def load(path):
    return json.loads(path.read_bytes())


def keyed(rows, field, expected):
    result = {row[field]: row for row in rows}
    if len(result) != len(rows) or set(result) != set(expected):
        raise ValueError(f"Missing/extra/duplicate {field}: {set(result) ^ set(expected)}")
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--followup",action="store_true")
    args=parser.parse_args()
    base=ROOT/"followup" if args.followup else ROOT
    freeze = load(base / "freeze.json")
    for name, pin in freeze["files"].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != pin["sha256"]:
            raise ValueError("Frozen input changed: " + name)
    mapping = keyed(load(base/"private/grade-map.json")["mappings"], "label",
                    [x["label"] for x in load(base/"private/grade-map.json")["mappings"]])
    per_run = []
    for tenant in ("codex", "claude"):
        packet = load(base/"grading"/tenant/"packet.json")
        grades = load(base/"grading"/tenant/"grades.json")
        original = {row["label"]:row for row in packet["answers"]}
        supplement=base/"grading"/tenant/"citation-checks-v3.json"
        if not supplement.exists():supplement=base/"grading"/tenant/"citation-checks-v2.json"
        if supplement.exists():
            updated=keyed(load(supplement)["answers"],"label",original)
            for label,row in updated.items():
                original[label]["mechanical_citation_checks"]=row["mechanical_citation_checks"]
        graded = keyed(grades["answers"], "label", original)
        for label, grade in graded.items():
            run = mapping[label]
            directory = base/"runs"/run["run_id"]/"execution"
            summary = load(directory/"summary.json")
            raw = (directory/"answer.json").read_bytes() if (directory/"answer.json").exists() else b"{}"
            if hashlib.sha256(raw).hexdigest() != original[label]["original_answer_sha256"]:
                raise ValueError("Answer changed after packet preparation")
            task_grades = keyed(grade["tasks"], "id", packet["oracle"])
            citation_checks = {row["task_id"]:row for row in original[label]["mechanical_citation_checks"]}
            results=[]
            for task_id, task in task_grades.items():
                oracle=packet["oracle"][task_id]
                expected={row["id"]:row for row in oracle["expected_semantic_criteria"]}
                criteria=keyed(task["criteria"],"id",expected)
                prohibited={row["id"]:row for row in oracle["forbidden_claims"]}
                prohibitions=keyed(task["prohibitions"],"id",prohibited)
                earned=0;weight=0;critical_unmet=[]
                for identity, assessment in criteria.items():
                    value=assessment["grade"]
                    if value not in GRADES:raise ValueError("Unknown criterion grade")
                    w=2 if expected[identity]["critical"] else 1
                    earned+=w*GRADES[value];weight+=w
                    if expected[identity]["critical"] and value!="met":critical_unmet.append(identity)
                asserted=[i for i,r in prohibitions.items() if r["status"]=="asserted"]
                ambiguous=[i for i,r in prohibitions.items() if r["status"]=="ambiguous"]
                if any(r["status"] not in ("asserted","absent","ambiguous") for r in prohibitions.values()):raise ValueError("Unknown prohibition grade")
                mechanically_valid={row["index"] for row in citation_checks.get(task_id,{}).get("citations",[]) if row.get("strict_citation_valid") and row["supplied"]["path"].endswith(".md")}
                supported=mechanically_valid & set(task["supporting_valid_citation_indices"])
                passed=not critical_unmet and not asserted and not ambiguous and earned/weight>=.8 and bool(supported)
                results.append(dict(id=task_id,score=round(100*earned/weight,4),earned_weight=earned,total_weight=weight,
                                    critical_unmet=critical_unmet,prohibited_asserted=asserted,prohibited_ambiguous=ambiguous,
                                    critical_incorrect=[i for i in critical_unmet if criteria[i]["grade"]=="incorrect"],
                                    supported_valid_citations=sorted(supported),strict_valid_citations=len(mechanically_valid),
                                    threshold_pass=passed,practical_pass=passed and summary["status"]=="completed",
                                    criterion_counts=dict(Counter(r["grade"] for r in criteria.values())),
                                    unsupported_claims=task["unsupported_claims"],blinding_disclosures=task["blinding_disclosures"]))
            usage={}
            for event in summary["usage_events"]:
                for key,value in event.items():
                    if isinstance(value,int):usage[key]=usage.get(key,0)+value
            audit=[json.loads(line) for line in (directory/"tool-audit.jsonl").read_text().splitlines()] if (directory/"tool-audit.jsonl").exists() else []
            calls=[row for row in audit if row["event"]=="tool_call"]
            workflow=None
            if args.followup and run["condition"]=="graphify":
                ok=lambda row:row["status"]=="ok" and row["emitted_utf8_bytes"]>0
                queries=[i for i,row in enumerate(calls) if row["tool"]=="graph_query" and ok(row)]
                selections=[i for i,row in enumerate(calls) if row["tool"]=="graph_select" and not row["arguments"].get("materialize",False) and ok(row)]
                reads=[i for i,row in enumerate(calls) if row["tool"]=="read_source" and ok(row)]
                workflow=any(q<s<r for q in queries for s in selections for r in reads)
            expected_ids=[task["id"] for task in packet["tasks"]]
            answer_ids=[task.get("id") for task in original[label]["answer"].get("tasks",[])]
            ids_valid=answer_ids==expected_ids
            if not ids_valid:
                for result in results:result["practical_pass"]=False
            if workflow is False:
                for result in results:result["practical_pass"]=False
            per_run.append(dict(run_id=run["run_id"],candidate=tenant,condition=run["condition"],blind_label=label,
                                status=summary["status"],errors=summary["errors"],usage=usage,
                                usage_reported=bool(summary["usage_events"]),answer_task_ids_exact=ids_valid,
                                prescribed_tool_order_compliant=workflow,
                                elapsed_seconds=summary["elapsed_seconds"],tool_calls=summary["tool_calls_attempted"],
                                content_utf8_bytes=summary["content_utf8_bytes"],wire_utf8_bytes=summary["wire_utf8_bytes"],
                                source_text_utf8_bytes=summary["source_text_utf8_bytes"],graph_startup_seconds=summary["graph_startup_seconds"],
                                graph_uptake=summary["graph_uptake"],tool_counts=dict(Counter(row["tool"] for row in calls)),
                                refusal_codes=dict(Counter(row["code"] for row in calls if row.get("code"))),
                                score=round(100*sum(t["earned_weight"] for t in results)/sum(t["total_weight"] for t in results),4),
                                threshold_task_passes=sum(t["threshold_pass"] for t in results),practical_task_passes=sum(t["practical_pass"] for t in results),
                                tasks=results))
    per_run.sort(key=lambda r:r["run_id"])
    cells=[]
    for tenant in ("codex","claude"):
        for condition in ("direct","graphify"):
            rows=[r for r in per_run if r["candidate"]==tenant and r["condition"]==condition]
            returned=[r for r in rows if r["answer_task_ids_exact"]]
            cells.append(dict(candidate=tenant,condition=condition,runs=len(rows),valid_runs=sum(r["status"]=="completed" for r in rows),
                              mean_score=sum(r["score"] for r in rows)/len(rows),threshold_task_passes=sum(r["threshold_task_passes"] for r in rows),
                              returned_runs=len(returned),mean_score_returned=sum(r["score"] for r in returned)/len(returned) if returned else None,
                              practical_task_passes=sum(r["practical_task_passes"] for r in rows),task_answers=sum(len(r["tasks"]) for r in rows),
                              critical_unmet=sum(len(t["critical_unmet"]) for r in rows for t in r["tasks"]),
                              critical_incorrect=sum(len(t["critical_incorrect"]) for r in rows for t in r["tasks"]),
                              critical_unmet_returned=sum(len(t["critical_unmet"]) for r in returned for t in r["tasks"]),
                              prohibited_assertions=sum(len(t["prohibited_asserted"]) for r in rows for t in r["tasks"]),
                              graph_uptake_runs=sum(r["graph_uptake"] for r in rows),
                              usage_reported_runs=sum(r["usage_reported"] for r in rows),
                              total_usage={k:sum(r["usage"].get(k,0) for r in rows) for k in {k for r in rows for k in r["usage"]}},
                              mean_elapsed_seconds=sum(r["elapsed_seconds"] for r in rows)/len(rows),
                              mean_calls=sum(r["tool_calls"] for r in rows)/len(rows),mean_content_utf8_bytes=sum(r["content_utf8_bytes"] for r in rows)/len(rows),
                              total_graph_startup_seconds=sum(r["graph_startup_seconds"] for r in rows)))
    result=dict(profile="ac.eval.actualuse-summary/1" if args.followup else "ac.eval.summary/1",freeze_sha256=hashlib.sha256((base/"freeze.json").read_bytes()).hexdigest(),runs=per_run,cells=cells,
                limitations=["Two repeats of four questions per candidate; no independent sampling/significance claim.",
                             "Condition-blinded same-family nonauthor assessment, not owner acceptance.",
                             "Assisted treatment bundles Graphify discovery with a_c declared acquisition; uptake optional.",
                             "Structured semantic contracts, not full native a_c re-authoring or calculus conformance.",
                             "Backend-reported tokens/cache, not dollars, billing discounts or corrected accepted-result cost."])
    if args.followup:
        result["limitations"][0]="One purposively selected original question per candidate, one repeat per condition; exploratory prescribed-use workflow, separate from primary."
    (base/"results.json").write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n")
    print(json.dumps(dict(cells=cells),indent=2))


if __name__=="__main__":main()
