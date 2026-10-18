#!/usr/bin/env python3
"""Describe observed locator failures without inferring semantic correctness."""
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parents[1] / "build_tenants/graphify/code"))
import ac_generate as g
import ac_grounding as h


def main():
    groups = []
    for candidate in ("codex", "claude"):
        for mode in ("graphify-ac", "direct"):
            output = ROOT / "runs-v2" / candidate / mode
            _, chunks = g.checkpoint(output)
            all_ids = {s["id"] for c in chunks for s in c["segments"]}
            graph_ids = set()
            if mode == "graphify-ac":
                graph_ids = {n["id"] for n in g.load(output / "discovery/graph.json")["nodes"]}
            kinds, cases = Counter(), []
            anchors_total = drafts = 0
            for chunk in chunks:
                path = output / "actors/author" / chunk["id"] / "attempt-001"
                if not (path / "result.json").is_file() or not (path / "answer.json").is_file():
                    continue
                answer = g.load(path / "answer.json")
                if g.schema_errors(answer, g.load(g.ASSETS / "author.schema.json")):
                    continue
                drafts += 1
                sections = {s["id"]: s for s in chunk["segments"]}
                for pointer, key, ground in h.anchors(answer):
                    anchors_total += 1
                    sid = ground["section_id"]
                    if sid not in sections:
                        if sid in all_ids:
                            kind = "known_source_section_outside_dispatched_chunk"
                        elif sid in graph_ids:
                            kind = "discovery_node_id_used_as_source_section"
                        elif "/source/" in sid and any(s.split("/source/", 1)[-1] == sid.split("/source/", 1)[-1] for s in sections):
                            kind = "source_path_and_heading_match_but_subject_prefix_differs"
                        else:
                            kind = "other_unknown_section_identifier"
                    elif h.strict_anchor(ground, sections[sid]):
                        kinds["strict_valid"] += 1
                        continue
                    else:
                        try:
                            _, witness = h.recover_anchor(ground, sections[sid])
                            kind = "unique_same_section_whitespace_or_range_recovery"
                        except h.GroundingError as exc:
                            kind = "ambiguous_quote" if "ambiguous" in str(exc) else "no_same_section_whitespace_equivalent_quote"
                    kinds[kind] += 1
                    cases.append({"chunk": chunk["id"], "record_key": key, "field": pointer,
                                  "kind": kind, "section_id": sid,
                                  "answer_sha256": g.sha((path / "answer.json").read_bytes())})
            groups.append({"candidate": candidate, "mode": mode, "schema_valid_initial_drafts_observed": drafts,
                           "grounding_entries": anchors_total, "classes": dict(kinds), "failures": cases})
    print(json.dumps({"profile": "ac.generation.grounding-diagnostics/1",
                      "observed_at": datetime.now(timezone.utc).isoformat(), "groups": groups,
                      "claim": "Observed source-locator syntax/range/quotation classes only; these do not establish why a model made an error or whether its statement is faithful."}, indent=2))


if __name__ == "__main__":
    main()
