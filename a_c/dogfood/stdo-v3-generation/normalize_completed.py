#!/usr/bin/env python3
"""Record bounded F_D checks for newly closed drafts; never dispatch F_P."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parents[1] / "build_tenants/graphify/code"))
import ac_generate as g
import ac_grounding as h


def main() -> None:
    expected = g.load(ROOT / "grounding-freeze-final.json")["files"]["a_c/build_tenants/graphify/code/ac_grounding.py"]["sha256"]
    g.require(g.sha(Path(h.__file__).read_bytes()) == expected, "grounding helper changed after final review")
    rows = []
    for candidate in ("codex", "claude"):
        for mode in ("graphify-ac", "direct"):
            output = ROOT / "runs-v2" / candidate / mode
            _, chunks = g.checkpoint(output)
            for chunk in chunks:
                attempt_root = output / "actors/author" / chunk["id"]
                attempts = sorted(attempt_root.glob("attempt-*"))
                if not attempts:
                    continue
                attempt = attempts[-1]
                result_path = attempt / "result.json"
                if not result_path.exists():
                    continue
                try:
                    result = g.load(result_path)
                except ValueError:
                    continue  # The source stage may still be writing its result.
                if result["status"] == "completed" and not (attempt / "validation.json").exists():
                    continue  # Wait for frozen source validation to finish.
                name = "normalization-initial" if attempt.name == "attempt-001" else "normalization-retry-" + attempt.name[-3:]
                if (output / name / chunk["id"]).exists():
                    continue
                if attempt.name == "attempt-001" and (output / "normalization-first" / chunk["id"]).exists():
                    continue
                normalized = h.normalize(output, name=name, chunk_id=chunk["id"])
                row = {"candidate": candidate, "mode": mode, "attempt": str(attempt.relative_to(output)),
                       "original_status": result["status"], "original_error": result.get("validation_error"),
                       "normalization": normalized}
                evidence = ROOT / "evidence/grounding-observations"
                evidence.mkdir(exist_ok=True)
                g.save(evidence / f"{candidate}-{mode}-{chunk['id']}-{attempt.name}.json", row, exclusive=True)
                rows.append(row)
    print(json.dumps({"new_fp_calls": 0, "new_observations": rows}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
