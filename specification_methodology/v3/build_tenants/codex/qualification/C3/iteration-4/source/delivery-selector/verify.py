#!/usr/bin/env python3
"""Reproduce the bounded selector repair and its authored account amendment."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / ".git").exists())
TENANT = Path("specification_methodology/v3/build_tenants/codex")
SOURCE_PREIMAGE = "cd19955505a0350b5d9b0f19d00c89e6d1810aa6"
ACCOUNT_PREIMAGE = "199c6d29bc02590a8b7f252043fc43223c09808d"
IDENTITY = TENANT / "successor/standards/IDENTITY_METHOD.md"
RELEASE = TENANT / "successor/standards/RELEASE_METHOD.md"
ACCOUNT = TENANT / "qualification/C3/iteration-3/DETERMINATIONS.json"
TARGET = "IDENTITY_METHOD.release-version-boundary"


def sha(body):
    return hashlib.sha256(body).hexdigest()


def frozen(path, ref=SOURCE_PREIMAGE):
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT)


def section(raw, heading):
    pattern = re.compile(rb"^#{1,6} .+\n", re.M)
    matches = list(pattern.finditer(raw))
    for i, item in enumerate(matches):
        if item.group().decode().rstrip() == heading:
            start = item.start()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
            body = raw[start:end]
            return {"start_byte": start, "end_byte": end,
                    "start_line": raw[:start].count(b"\n") + 1,
                    "end_line": raw[:end].count(b"\n"),
                    "body_sha256": sha(body), "bytes": len(body)}, body
    raise AssertionError(heading)


def main():
    old = frozen(IDENTITY)
    new = (ROOT / IDENTITY).read_bytes()
    before, old_body = section(old, "## Release Version Boundary")
    after, body = section(new, "## Release Version Boundary")
    assert old[:before["start_byte"]] == new[:after["start_byte"]]
    assert old[before["end_byte"]:] == new[after["end_byte"]:]
    assert b"latest-accepted" in old_body and b"latest-accepted" not in body
    assert b"highest-ordinal published immutable RC cut" in body
    assert b"independently of the cut's\nacceptance" in body
    assert b"Moving it does not change a consumer's operative basis" in body
    release = frozen(RELEASE)
    assert release == (ROOT / RELEASE).read_bytes(), "Release owner changed"
    release_bindings = []
    for heading, anchor in [("## Release Identities", "release-identities"),
                            ("## Selector And Consumer Adoption", "selector-and-consumer-adoption")]:
        coords, _ = section(release, heading)
        release_bindings.append({"path": str(RELEASE), "anchor": anchor, "heading": heading[3:], **coords})
    original_account = frozen(ACCOUNT, ACCOUNT_PREIMAGE)
    assert original_account == frozen(ACCOUNT)
    units = {r["id"]: r for r in json.loads(original_account)["determinations"]}
    existing = units[TARGET]
    canonical = ["RELEASE_METHOD.release-identities", "RELEASE_METHOD.selector-and-consumer-adoption"]
    assert all(unit_id in units for unit_id in canonical)
    dependencies = list(dict.fromkeys(existing["dependencies"] + canonical))
    relations = existing["dependency_relations"] + [
        {"id": canonical[0], "kind": "contract_application",
         "binding": "Release Method owns the immutable cut and highest-published version-line selector identities consumed by this identity boundary.",
         "required_when": "the selected task determines release identities or a version-line selector target"},
        {"id": canonical[1], "kind": "contract_application",
         "binding": "Release Method owns the distinction between publication discovery, exact consumer basis and explicit consumer adoption.",
         "required_when": "the selected task determines selector meaning or reliance on consumer adoption"},
    ]
    argument = dict(existing["argument"])
    argument.update({
        "conditional_consequence": "Object identity, immutable cut identity and discovery selectors denote different subjects. Identity consumes Release Method's publication-selected target and separate adoption relation; cut acceptance cannot substitute for publication when determining the selector, and discovery cannot change the consumer's exact basis.",
        "policy_choices": ["The highest-ordinal published selector target and explicit consumer-adoption transition are Release Method policies. Identity consumes those owners and introduces no alternative selector policy."],
        "source_refs": list(dict.fromkeys(existing["argument"]["source_refs"] + canonical)),
    })
    source_pin = {"path": str(IDENTITY), "preimage_sha256": sha(old), "sha256": sha(new),
                  "preimage_bytes": len(old), "bytes": len(new)}
    patch = {
        "kind": "stdo.delivery-selector-authored-account-patch", "schema_version": 1,
        "activation": "I4-DELIVERY-SELECTOR", "source_preimage": SOURCE_PREIMAGE,
        "account_preimage": {"commit": ACCOUNT_PREIMAGE, "path": str(ACCOUNT), "sha256": sha(original_account), "unchanged_at_source_preimage": True},
        "standing": "author_input_not_independent_fidelity_or_acceptance",
        "source_pins": [source_pin], "canonical_owner_pins": release_bindings,
        "patches": [{
            "id": TARGET, "path": str(IDENTITY), "heading": "Release Version Boundary", "anchor": "release-version-boundary",
            "change_kind": "canonical_release_owner_correction", "new_decision_scope": False,
            "predicate_or_result_change": True, "result_mapping_change": False,
            "preimage_body_sha256": before["body_sha256"], "body_sha256": after["body_sha256"],
            "body_hash_rule": "UTF-8 bytes from the heading start through all content and blank/separator lines before the next heading; heading included.",
            "source_range": after,
            "semantic_fields": {
                "predicate": "Object identity, immutable release identity, publication coordinates and mutable selectors remain distinct. A version-line selector names the highest-ordinal published immutable RC cut for its project/version line independently of acceptance, and selector movement does not change a consumer's operative basis.",
                "obligations": existing["obligations"] + [
                    "Interpret the mutable version-line selector under Release Method as highest-ordinal published immutable RC, not latest-accepted.",
                    "Keep the cut's acceptance separate from publication-selected discovery; moving the selector does not adopt a new consumer basis.",
                    "Consumer adoption is the explicit transition owned by the consumer's governing authority under Release Method.",
                ],
                "dependencies": dependencies, "dependency_relations": relations,
                "argument": argument,
            },
            "preserve_existing_fields": ["permissions_exceptions", "result_mapping", "representation_kind", "applicability", "consumers"],
            "source_pin_action": "Refresh the member pin and changed heading/source-clause spans at the integrated freeze. The old declaration block containing latest-accepted is superseded by this owner-corrected meaning; add the final publication/acceptance/adoption paragraph with its actual declaration/obligation roles.",
            "acquisition_binding": "The two added Release owner dependencies are genuine conditions for applying this release identity boundary; they are not a consumer inventory. Their required_when values restrict the selected release/selector/adoption task. No family-table consumer fan-out is added.",
        }],
        "affected_dependencies": [
            {"id": "IDENTITY_METHOD.governing-relations", "action": "Its I4 family row for Release Version Boundary already assigns exact identities and selector/adoption mechanics to Release. Preserve its argument and source_refs-only consumer provenance; refresh the member pin and verify the formerly contradictory consumer at the new source hash."},
            {"id": "FOUNDATIONS.identity-state-and-evidence", "action": "Its existing consumer/provenance route to the identity boundary retains meaning; no foundation predicate or authority changes. Reuse only with the updated subject binding."},
            {"id": canonical[0], "action": "Canonical owner unchanged; consume its pinned exact subject and highest-published selector identity."},
            {"id": canonical[1], "action": "Canonical owner unchanged; consume its separation of discovery, exact basis and explicit adoption."},
        ],
        "integration_limits": ["No current account, generated interpretation, frame, compression or Release source is modified.",
                               "Preserve the earlier closed source/delivery artifacts and their historical source pins.",
                               "Interpretation/source-block integration and independent frozen readback remain with their assigned owners."],
    }
    (HERE / "ACCOUNT_PATCH.json").write_text(json.dumps(patch, ensure_ascii=False, indent=2) + "\n")
    counterexample = {
        "id": "DEL-SELECTOR-01", "kind": "hypothetical_semantic_counterexample",
        "subject": "One project and version line with accepted rc.1 and published, unaccepted rc.2",
        "published_cuts": [{"rc_ordinal": 1, "accepted": True}, {"rc_ordinal": 2, "accepted": False}],
        "consumer_exact_basis_ordinal": 1,
        "old_identity_latest_accepted_target": 1,
        "canonical_release_and_repaired_identity_target": 2,
        "consumer_exact_basis_after_selector_movement": 1,
        "reason": "Publication determines the highest-ordinal selector target. Acceptance does not select it, and publication/selector movement does not authorize or perform consumer adoption.",
        "source_refs": [TARGET, *canonical],
        "standing": "author_constructed_counterexample_for_independent_readback; no runtime publication_or_adoption_trial",
    }
    (HERE / "COUNTEREXAMPLE.json").write_text(json.dumps(counterexample, indent=2) + "\n")
    closed = TENANT / "qualification/C3/iteration-4/source/delivery"
    paths = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", SOURCE_PREIMAGE, "--", str(closed)], cwd=ROOT, text=True).splitlines()
    assert paths
    for path in paths:
        assert frozen(path) == (ROOT / path).read_bytes(), f"Closed return altered: {path}"
    check = subprocess.run(["git", "diff", "--check", "--", str(IDENTITY), str(HERE.relative_to(ROOT))], cwd=ROOT, text=True, capture_output=True)
    assert check.returncode == 0, check.stdout + check.stderr
    result = {
        "activation": "I4-DELIVERY-SELECTOR", "source_preimage": SOURCE_PREIMAGE,
        "source_pins": [source_pin], "changed_heading": TARGET,
        "preimage_heading": before, "current_heading": after,
        "body_hash_rule": patch["patches"][0]["body_hash_rule"],
        "all_bytes_outside_changed_heading_identical": True,
        "release_member_byte_identical": True, "release_sha256": sha(release),
        "closed_delivery_artifacts_byte_identical": len(paths),
        "canonical_owner_pins": release_bindings,
        "source_counterexample_binding": "DEL-SELECTOR-01", "scoped_whitespace": "passed",
        "limits": "Author source/integrity checks; no independent semantic judgment, generated-output check, release effect or acceptance.",
    }
    (HERE / "CHECKS.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"changed_heading": TARGET, "identity_sha256": sha(new), "heading_body_sha256": after["body_sha256"], "all_other_identity_bytes_unchanged": True, "release_unchanged": True, "closed_delivery_artifacts_unchanged": len(paths), "whitespace": "passed"}))


if __name__ == "__main__":
    main()
