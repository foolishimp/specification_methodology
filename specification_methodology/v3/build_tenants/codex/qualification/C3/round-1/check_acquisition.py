"""Reassemble the public responsibility views using their published routes.

No task oracle, author frame recipe or private expected answer is consumed.
This checks reproducible selection/rendering; actor sufficiency is separate.
"""
import hashlib
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import re


base = Path(__file__).resolve().parents[3]
root = base / "successor"
spec = spec_from_file_location("view_renderer", base / "qualification/C3/refresh_views.py")
renderer = module_from_spec(spec)
spec.loader.exec_module(renderer)
index_path = base / "qualification/C3/FRAME_INPUTS.json"
public_index = (root / "standards/README.md").read_text()
paths = sorted(set(re.findall(r"\]\((frames/[A-Z_]+\.md)\)", public_index)))
before = {p: hashlib.sha256((root / "standards" / p).read_bytes()).hexdigest() for p in paths}
index_before = hashlib.sha256(index_path.read_bytes()).hexdigest()
renderer.refresh()
assert index_before == hashlib.sha256(index_path.read_bytes()).hexdigest(), "non-idempotent index refresh"
checks = []
for relative in paths:
    view = root / "standards" / relative
    content = view.read_text()
    parts = [content.split("\nSource:", 1)[0].rstrip()]
    for match in re.finditer(r"\nSource: \[([^\n]+?)\]\(\.\./([^#]+)#([^\)]+)\); "
                             r"SHA256 `([0-9a-f]{64})`\.\n\n", content):
        owner = root / "standards" / match[2]
        source = owner.read_text()
        headings = list(re.finditer(r"^(#{2,6}) (.+)$", source, re.M))
        selected = [(i, h) for i, h in enumerate(headings) if renderer.slug(h[2]) == match[3]]
        assert len(selected) == 1, "ambiguous source selection"
        i, heading = selected[0]
        end = next((h.start() for h in headings[i + 1:] if len(h[1]) <= len(heading[1])), len(source))
        original = source[heading.start():end].rstrip() + "\n"
        assert hashlib.sha256(owner.read_bytes()).hexdigest() == match[4], "stale public source pin"
        parts.append(match[0] + re.sub(r"(\[[^\]]*\]\()([^\n]+?)(\))", renderer.relocate, original))
    rebuilt = ("\n".join(parts).rstrip() + "\n").encode()
    assert len(parts) > 1 and rebuilt == view.read_bytes(), "non-reproducible published view"
    unchanged = before[relative] == hashlib.sha256(view.read_bytes()).hexdigest()
    assert unchanged, "non-idempotent view refresh"
    checks.append({"path": "standards/" + relative, "bytes": len(rebuilt),
                   "source_headers": len(parts) - 1,
                   "reproduced_from_published_owner_routes": True, "refresh_is_idempotent": unchanged})
report = {"kind": "responsibility_acquisition_check",
          "entry": "successor/plugins/spec/skills/stdo-work/SKILL.md#acquire-the-responsibility-frame",
          "views": checks, "valid": True,
          "limits": ["Exact route/excerpt reproduction, not actor discovery or material-sufficiency acceptance",
                     "No task oracle or candidate expected answers used"]}
Path(__file__).with_name("ACQUISITION_CHECK.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
