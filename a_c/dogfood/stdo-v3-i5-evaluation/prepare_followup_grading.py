#!/usr/bin/env python3
"""Create separate blind packets for the exploratory prescribed-use repeats."""
from __future__ import annotations
import importlib.util
import json
import secrets
import sys
from pathlib import Path
from prepare_grading import sha, write, factor_sources, source_checks

ROOT=Path(__file__).resolve().parent


def main():
    target=ROOT/"followup"
    frozen=json.loads((target/"freeze.json").read_bytes())
    for path,pin in frozen["files"].items():
        if sha((ROOT/path).read_bytes())!=pin["sha256"]:raise ValueError("Frozen followup input changed")
    schedule=json.loads((target/"schedule.json").read_bytes())["runs"]
    if not all((target/"runs"/r["id"]/"execution/summary.json").exists() for r in schedule):
        raise ValueError("Followup actors must all terminate before packets")
    spec=importlib.util.spec_from_file_location("ac_followup_reader",ROOT/"tools/study_mcp.py")
    reader=importlib.util.module_from_spec(spec);sys.modules[spec.name]=reader;spec.loader.exec_module(reader)
    tasks=json.loads((ROOT/"private/tasks.json").read_bytes())["candidates"]
    oracle=json.loads((ROOT/"private/oracle.json").read_bytes())["candidates"]
    mappings=[]
    for tenant in ("codex","claude"):
        task_id="C3" if tenant=="codex" else "L3"
        packets=[]
        for run in schedule:
            if run["candidate"]!=tenant:continue
            d=target/"runs"/run["id"]/"execution"
            raw=(d/"answer.json").read_bytes() if (d/"answer.json").exists() else b"{}"
            try:answer=json.loads(raw)
            except ValueError:answer={}
            label=secrets.token_hex(6)
            packets.append(dict(label=label,answer=answer,original_answer_sha256=sha(raw),
                                mechanical_citation_checks=source_checks(tenant,answer,reader,d)))
            mappings.append(dict(label=label,run_id=run["id"],candidate=tenant,condition=run["condition"],answer_sha256=sha(raw)))
        secrets.SystemRandom().shuffle(packets)
        passages={};compact=factor_sources({task_id:oracle[tenant][task_id]},passages,{})
        # Copy only condition-free assessment rules from the already blind
        # primary packet. No run identity, tool/usage log or mapping is copied.
        guide=json.loads((ROOT/"grading"/tenant/"packet.json").read_bytes())["guide"]
        guide={**guide,"allowed_read_scope":[str(target/"grading"/tenant),str(ROOT/"baselines"/tenant/"sources")],
               "instruction":guide["instruction"].replace("four questions","one question"),
               "output_contract":guide["output_contract"].replace("all32 expected criteria and12 prohibitions across4 tasks","all8 expected criteria and3 prohibitions for the one task")}
        write(target/"grading"/tenant/"packet.json",dict(profile="ac.eval.blind-actualuse-packet/1",candidate=tenant,
              frozen_oracle_sha256=sha((ROOT/"private/oracle.json").read_bytes()),guide=guide,
              tasks=[t for t in tasks[tenant] if t["id"]==task_id],oracle=compact,source_passages=passages,answers=packets))
    write(target/"private/grade-map.json",dict(profile="ac.eval.private-grade-map/1",mappings=mappings))
    print(json.dumps(dict(status="followup_blind_packets_prepared",answers=len(mappings))))


if __name__=="__main__":main()
