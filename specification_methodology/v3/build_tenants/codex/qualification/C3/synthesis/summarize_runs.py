#!/usr/bin/env python3
"""Summarize retained CLI measurements, without making acceptance claims."""
from collections import defaultdict
from decimal import Decimal
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def main():
    rows, seen = [], set()
    groups = defaultdict(lambda: {"calls": 0, "cost": Decimal(0), "seconds": 0.0})
    for path in sorted(HERE.rglob("MEASUREMENT.json")):
        value = json.loads(path.read_text())
        provider = value.get("native_result", value)
        session = provider.get("session_id")
        if not session or session in seen:
            raise ValueError("missing or duplicate provider session: " + str(path))
        seen.add(session)
        cost = Decimal(str(provider["total_cost_usd"]))
        route = str(path.relative_to(HERE))
        group = ("entry/bound" if route.startswith("entry/bound/") else
                 "entry/initial" if route.startswith("entry/") else
                 route.split("/")[0])
        seconds = value["elapsed_seconds"]
        selected = value.get("selected_input_bytes", value.get("selected_material_bytes"))
        row = {"measurement": route,
               "measurement_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
               "session_id": session, "group": group,
               "elapsed_seconds": seconds, "selected_material_bytes": selected,
               "cost_usd": float(cost), "provider_subtype": provider.get("subtype"),
               "provider_error": provider.get("is_error"), "exit_code": value["exit_code"],
               "configured_spend_limit_usd": value.get("spend_limit_usd"),
               "host_stop": value.get("host_stop")}
        rows.append(row)
        groups[group]["calls"] += 1
        groups[group]["cost"] += cost
        groups[group]["seconds"] += seconds
    total = sum((group["cost"] for group in groups.values()), Decimal(0))
    report = {
        "kind": "retained CLI run accounting",
        "aggregate_allowance_usd": 30,
        "calls": len(rows), "provider_reported_cost_usd": float(total),
        "remaining_allowance_usd": float(Decimal(30) - total),
        "aggregate_allowance_met": total <= Decimal(30),
        "summed_call_elapsed_seconds": round(sum(row["elapsed_seconds"] for row in rows), 3),
        "maximum_selected_material_bytes": max(row["selected_material_bytes"] for row in rows),
        "failed_provider_calls": [row["measurement"] for row in rows if row["provider_error"]],
        "configured_cap_overruns": [row["measurement"] for row in rows
                                    if row["configured_spend_limit_usd"] is not None
                                    and row["cost_usd"] > row["configured_spend_limit_usd"]],
        "groups": {key: {"calls": value["calls"], "cost_usd": float(value["cost"]),
                         "summed_call_elapsed_seconds": round(value["seconds"], 3)}
                   for key, value in sorted(groups.items())},
        "runs": rows,
        "limits": [
            "Provider-reported USD, not an independently verified invoice.",
            "Summed call time is not campaign wall time; calls overlapped.",
            "Selected material excludes hidden provider system context and processing.",
            "Parent and delegated Codex platform token/cost usage is not measured here.",
            "A completed provider call is not semantic acceptance.",
            "Historical failed calls remain counted; each provider session is counted once."
        ]}
    (HERE / "COSTS.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ["calls", "provider_reported_cost_usd",
                     "remaining_allowance_usd", "maximum_selected_material_bytes",
                     "configured_cap_overruns"]}, indent=2))


if __name__ == "__main__":
    main()
