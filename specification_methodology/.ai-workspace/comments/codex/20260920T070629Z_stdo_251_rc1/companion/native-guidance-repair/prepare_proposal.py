"""Prepare a native-guidance replacement without changing any live member."""
from pathlib import Path
import difflib
import hashlib
import json

OUT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[7]
LIVE = ROOT / "stdo_representation/skills/stdo-representation/SKILL.md"
EXPECTED = "e25ab254c3f2329f3a93264328c373b8355ea8eb9855dfebbb451f91b467b674"


def sha(content):
    return hashlib.sha256(content).hexdigest()


def main():
    before = LIVE.read_bytes()
    if sha(before) != EXPECTED:
        raise ValueError("Frozen live skill differs from the exact diagnosed subject")
    if (OUT / "SKILL.md").exists():
        raise ValueError("Preserve the existing proposed replacement")
    original = before.decode()
    old = """   This is caller guidance, not a prompt engine, schema, selector, or renderer.
   Resolve the same exact selected Axiom dependency, then run its pure
   joiner:

   ```sh
   python3 <axiom-indexer-root>/build_tenants/core/code/ac.py join \\
     --input <sections.json> \\
     --output <request.txt>
   ```

Return through the caller's declared return relation, to Executive when that
role is selected, with the selected frame details, source re-entry, validation
result, unresolved residuals and resulting request path or bounded answer.
Do not load unrelated index regions merely because they are available.
"""
    new = """   Preserve every case and discriminator in the selected declared result and
   stop contracts. Do not paraphrase them into a different result algebra or
   collapse distinct refusal, uncertainty, scope or basis outcomes into a
   generic status. Before joining, compare the authored handoff with the
   selected clauses and the caller's requested return contract; repair omitted
   conditions, changed meanings or unsupported additions. Re-enter the exact
   source when those contracts are unresolved.

   Resolve the same exact selected Axiom dependency. Supply the authored JSON
   array directly on stdin and receive the exact joined text on stdout:

   ```sh
   python3 <axiom-indexer-root>/build_tenants/core/code/ac.py join \\
     --input /dev/stdin
   ```

   In a read-only activation, keep this computation on stdin/stdout; create no
   scratch input or output files and do not redirect stdout to a file. Every
   file output path, including `--output`, requires an applicable write grant.
   The caller authors and checks the request; the pure joiner only concatenates
   its supplied strings and cannot establish semantic fidelity.

Return through the caller's declared return relation, to Executive when that
role is selected, with the selected frame details, source re-entry, validation
result, unresolved residuals and resulting request path or bounded answer.
Preserve the requested return format and field types. When ordered sections
and joined text are requested, return the actual ordered label/text array and
exact joiner stdout in their declared fields, with correct escaping when the
carrier is JSON. A prose summary, placeholder or pointer to another block does
not supply those values. If bare structured output is requested, do not add
Markdown fences or substitute prose. Do not load unrelated index regions
merely because they are available.
"""
    if original.count(old) != 1:
        raise ValueError("The selected request/return passage changed")
    proposed = original.replace(old, new, 1)
    (OUT / "SKILL.preimage.md").write_bytes(before)
    (OUT / "SKILL.md").write_text(proposed)
    (OUT / "SKILL.diff").write_text("".join(difflib.unified_diff(
        original.splitlines(True), proposed.splitlines(True),
        fromfile="stdo-representation/SKILL.md@frozen-native-subject",
        tofile="stdo-representation/SKILL.md@proposed-guidance-repair")))
    review = ROOT / "specification_methodology/.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/native-review/claude-comparison.json"
    record = {
        "kind": "stdo.rc1-native-guidance-repair-proposal", "schema_version": 1,
        "status": "proposed-only", "re_entry": "realization_refactor",
        "role": "Worker", "operation": "Prepare an exact canonical native-skill replacement and bounded finding-to-delta rationale inside this evidence directory only.",
        "authority": "Parent Executive consumed the closed Claude F-DOGFOOD falsified result and explicitly granted this bounded proposal. Parent independently assesses and promotes any repair; original native observations remain unchanged.",
        "live_path": str(LIVE.relative_to(ROOT)), "preimage_sha256": sha(before),
        "proposed_path": str((OUT / "SKILL.md").relative_to(ROOT)), "proposed_sha256": sha(proposed.encode()),
        "closed_comparison": {"path": str(review.relative_to(ROOT)), "sha256": sha(review.read_bytes())},
        "findings": {
            "CN-01": "Preserve every declared result/stop case and discriminator; compare authored handoff against selected clauses before joining. No task-specific expected result or hardcoded algebra is added.",
            "CN-02": "Make the default join example stdin/stdout; explicitly exclude scratch creation and file redirection in read-only activation and retain the grant requirement for any output path.",
            "CN-03": "Retain requested output format/types and place the actual ordered label/text array and exact joined stdout into their declared return fields. Prose substitutes and external-block pointers do not satisfy those fields."
        },
        "conservation": {"only_selected_request_and_return_passage_changed": True,
                         "live_skill_unchanged": LIVE.read_bytes() == before,
                         "source_program_map_mechanics_and_native_observations_not_modified": True},
        "claim": "A bounded guidance proposal under existing fidelity, effect-scope and return obligations. Independent assessment, promotion and new-subject native effectiveness remain unperformed here."
    }
    if not record["conservation"]["live_skill_unchanged"]:
        raise ValueError("Live skill changed during proposal preparation")
    (OUT / "proposal.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"proposed_path": record["proposed_path"],
                      "proposed_sha256": record["proposed_sha256"],
                      "live_skill_sha256": sha(LIVE.read_bytes()),
                      "proposal_manifest_sha256": sha((OUT / "proposal.json").read_bytes())}))


if __name__ == "__main__":
    main()
