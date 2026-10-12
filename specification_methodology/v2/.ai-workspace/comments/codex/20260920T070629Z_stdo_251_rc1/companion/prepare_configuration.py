"""Construct successor frame/Definition proposals without promoting live bindings."""
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[6]
INSTALL = Path("/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.1")
DEST = OUT / "configuration-proposals"
PRE = OUT / "preimages"
OLD = "stdo://releases/v2.5.0-rc.7/"
NEW = "stdo://releases/v2.5.1-rc.1/"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def rebind(value):
    if isinstance(value, str):
        return value.replace(OLD, NEW)
    if isinstance(value, list):
        return [rebind(v) for v in value]
    if isinstance(value, dict):
        return {k: rebind(v) for k, v in value.items()}
    return value


def main():
    if DEST.exists():
        raise ValueError("Preserve the exact existing configuration proposals")
    manifest = json.loads((INSTALL / "manifest.json").read_text())
    preimage = json.loads((OUT / "preimage.json").read_text())
    rows = []
    for child in ("axiom_indexer", "stdo_representation"):
        paths = [ROOT / child / "specification" / name for name in ("PRODUCT.md", "INTENT.md", "GOALS.md")]
        paths += sorted((ROOT / child / "specification/requirements").glob("*.md"))
        rows += [{"path": str(p.relative_to(ROOT)), "sha256": sha(p)} for p in paths]
    selection = {
        "kind": "stdo.rc1-internal-configuration-subject", "schema_version": 1,
        "source_stdo": {"uri": NEW, "installed_manifest_sha256": sha(INSTALL / "manifest.json"),
                        "release": manifest["release"], "standards": manifest["standards"]},
        "axiom_product": preimage["axiom_product"],
        "representation_product": json.loads((OUT / "representation-members.json").read_text()),
        "owning_sources": rows,
        "semantic_delta": {"path": str((OUT / "semantic-delta.json").relative_to(ROOT)), "sha256": sha(OUT / "semantic-delta.json")},
        "mechanical_conservation": {"path": str((OUT / "construction-conservation.json").relative_to(ROOT)), "sha256": sha(OUT / "construction-conservation.json")},
        "source_drift_refusal": {"path": str((OUT / "negative-source-drift/result.json").relative_to(ROOT)), "sha256": sha(OUT / "negative-source-drift/result.json")},
        "matched_cohort": {"path": "stack_release.json", "sha256": sha(ROOT / "stack_release.json")},
        "release_notes": [{"path": child + "/releases/v2.5.1.md", "sha256": sha(ROOT / child / "releases/v2.5.1.md")}
                          for child in ("axiom_indexer", "stdo_representation")],
        "closed_independent_assessments": [{"path": str((OUT.parent / name).relative_to(ROOT)), "sha256": sha(OUT.parent / name)}
                                           for name in ("source-review.json", "representation-semantic-review.json", "companion-review.json")],
        "qualification_scope": "Four fresh source/map by Codex/Claude contexts on the compact three-case packet, actual executable fixture observations, and separate independent comparison. These are selected claims, not prewritten completed results.",
        "configuration_scope": "Internal local complete 2.5.1 RC1 preparation, independent of ABI T-288. No publication, external adoption, immutable Product acceptance or future release authority."
    }
    put(DEST / "selection-subject.json", selection)
    selection_ref = "repo://specification-methodology/.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/companion/configuration-proposals/selection-subject.json"
    proposals = []
    for child, label, revision, identity, definition, begin, end in [
        ("axiom_indexer", "Axiom Indexer", 12, "urn:axiom-indexer:frame-set:release-readiness:12", "stdo_default.json", "## Shared Coordinates, Evidence, And Results", "## Coverage Ledger"),
        ("stdo_representation", "STDO Representation", 20, "urn:stdo-representation:reference-frame-basis:source-project:20", "stdo_representation.json", "## Shared coordinate, evidence, and result law", "## Coverage ledger")]:
        frame_path = ROOT / child / "specification/REFERENCE_FRAME_BASIS.md"
        definition_path = ROOT / child / definition
        prior_frame = PRE / child / "specification/REFERENCE_FRAME_BASIS.md"
        prior_definition = PRE / child / definition
        if sha(frame_path) != sha(prior_frame) or sha(definition_path) != sha(prior_definition):
            raise ValueError("Live configuration changed before proposal: " + child)
        prior_decision_path = ROOT / child / ".ai-workspace/decisions/20260915_rc7_frame_basis_acceptance.json"
        prior_decision = json.loads(prior_decision_path.read_text())
        if prior_decision["subject_sha256"] != "sha256:" + sha(frame_path):
            raise ValueError("Prior accepted frame is not exact")
        old_text = frame_path.read_text()
        common = old_text[old_text.index(begin):old_text.index(end)]
        # This copied interval contains current contract/actor law and identified
        # RC4 historical exclusions. Only its current RC7 coordinates change.
        common = common.replace("2.5.0-rc.7", "2.5.1-rc.1").replace("RC7", "2.5.1 RC1")
        common = common.replace("releases/v2.5.0.md", "releases/v2.5.1.md").replace("`axiom_indexer/v2.5.0`", "`axiom_indexer/v2.5.1`")
        if child == "stdo_representation":
            old_scope = """The proposed current evaluation boundary is the selected 2.5.1 RC1 configuration,
qualification and release above under the verified 2.5.1 RC1 basis. RC4 construction
and publication remain closed historical phases."""
            new_scope = """The proposed current evaluation boundary is the selected local 2.5.1 RC1
configuration and complete candidate qualification under the verified source.
Publication and external adoption are unselected. RC7 and earlier publication
results remain closed for their own immutable subjects."""
            if old_scope not in common:
                raise ValueError("Expected current triage scope is absent")
            common = common.replace(old_scope, new_scope, 1)
        namespace = "axiom-indexer" if child == "axiom_indexer" else "stdo-representation"
        decision = ".ai-workspace/decisions/20260920_251_rc1_frame_basis_acceptance.json"
        header = f"""# {label} Project Reference-Frame Basis

Status at proposal handoff: proposed and unaccepted declaration, revision {revision}.
The exact accepted RC7 predecessor and live Product Definition remain operative
until the separately assessed successor configuration decision is consumed.
This proposal grants no construction, acceptance, publication or adoption effect.

## Project frame basis

```text
frame_set_uri = "{identity}"
governed_workspace = "repo://{namespace}/"
governed_subject = "urn:{namespace}:bounded-context:product"
governed_outcome = "qualify the complete local 2.5.1 RC1 candidate and its exact internal configuration, independently of ABI delivery, with publication and external adoption unselected"
frame_set_authority = "urn:{namespace}:authority:product-owner"
reference_frame_method = "{NEW}standards/REFERENCE_FRAME_METHOD.md"
reference_frame_method_sha256 = "sha256:{sha(INSTALL / 'standards/REFERENCE_FRAME_METHOD.md')}"
reference_frame_baseline = "{NEW}standards/STDO_REFERENCE_FRAME_BASELINE.md"
reference_frame_baseline_sha256 = "sha256:{sha(INSTALL / 'standards/STDO_REFERENCE_FRAME_BASELINE.md')}"
release_method = "{NEW}standards/RELEASE_METHOD.md"
release_method_sha256 = "sha256:{sha(INSTALL / 'standards/RELEASE_METHOD.md')}"
stdo_manifest_sha256 = "sha256:{sha(INSTALL / 'manifest.json')}"
```

## Authority and selected subject

The Product owner retains declaration and disposition authority under
`specification/PRODUCT.md#product-disposition-authority`. A generic evaluator
cannot accept its own frame. The current direct owner instruction,
“we can prepare 2.5.1 RC1 without any dependency”, and the exact role/write
grants are retained at
`repo://specification-methodology/.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/README.md`.
That request selects local complete matched-cohort preparation. It grants no
publication or external adoption. Each actual effect still requires its own
exact Worker/Writer operation scope; evaluation supplies none.

The exact selected source, Product/requirement bytes, conserved seven-member
Axiom mechanics, nine-member Representation subject, program/map, semantic
delta and mechanical evidence are bound by
`{selection_ref}`,
SHA-256 `{sha(DEST / 'selection-subject.json')}`.
The Source STDO cut is local annotated tag `{manifest['release']['tag_object']}`,
commit `{manifest['release']['commit']}`. Future child-cut objects are results
of separately granted local construction, never fabricated prerequisites.

The successor represents accepted T031 interface integration and the shared
validity, complete-path, operational-assumption, supported-threat, guidance
fidelity, retention and continuity amendments. It adds no generic Axiom
mechanics, semantic interpreter, reference-frame family, permanent actor,
universal quota or runtime authority. Source meaning, structural properties,
native use and decision authority remain distinct claims.

## Conservation boundary

The accepted predecessor declaration is `{prior_decision['subject_uri']}`,
SHA-256 `{sha(frame_path)}`, accepted through
`.ai-workspace/decisions/20260915_rc7_frame_basis_acceptance.json`, SHA-256
`{sha(prior_decision_path)}`. Its exact bytes remain in the
preparation record's `companion/preimages/{child}/specification/REFERENCE_FRAME_BASIS.md`.
Its accepted scope and historical closed results are not relabelled as current.

The contract and actor sections below preserve the predecessor's evaluation
relations and independence conditions with current exact release coordinates.
Historical RC4 exclusions remain historical. The Reference Frame Method and
Release Method have unchanged bytes; material baseline/source changes receive
their own current assessment. The current phase and conjunction below replace
old release-phase bookkeeping, not Product obligations.

"""
        trailer = f"""## Current applicability, coverage and conjunction

Each activation selects the actual owning question, exact subject, actor,
evidence, source/role basis and return consumer. Available frame names activate
nothing by themselves. All applicable mandatory constraints retain valid
support; absent, stale, wrong-subject, conflicted, incapable or unknown support
withholds only its dependent conclusion. Unknown is neither false nor satisfied.

The current producer/consumer relations are:

- Exact Axiom member conservation and applicable mechanical checks produce
  structural facts. Reproduced RC1 map/report, both projection modes and actual
  stale-source refusal qualify the changed input relation. Reuse unchanged
  mechanical evidence within its exact original scope; no duplicate runtime
  matrix follows solely from a matched version change.
- Independently assessed source/program/index fidelity consumes exact source
  and current mechanical facts. It preserves all applicable permissions,
  exclusions, invalidators, premise/exception links and residuals. Structural
  success does not supply that judgment.
- Fresh native source/map contexts consume frozen subjects, the same ordinary
  task and evidence, and permitted source routes. Material executable fixture
  observations qualify their own finite properties. The separately activated
  comparison assessor acquires both finished conditions and source independently
  under the unchanged independence envelope; author agreement, private oracles
  and green deterministic checks cannot substitute for observed ordinary use.
- Current Product/source/mechanical/native results and exact dependency/member
  closure feed complete local candidate readiness. Local commit/ref construction
  follows its separate grant. No published child ref, remote publication result,
  external adoption or ABI ticket closure is a prerequisite to preparation.
- Publication, published cohort integrity and `F-EXACT-CUT` remain unselected.
  A later authorized publication requires its then-current full ref graph and
  remote expectations plus applicable release checks. Published-cut assessment
  produces its own verdict after actual publication; neither a local tag nor
  this proposal establishes it.

At proposal handoff, construction/mechanical and source-assessment records retain
their exact reported states. Native comparison, complete candidate disposition
and configuration acceptance are not prewritten passes. Their later closed
records supply their own claim, subject, time, actor and evidence.

Only closed applicable results cross frame boundaries. A changed source,
program/map, skill, operation, grant, frame, actor capability, evidence population,
workspace observation or dependency invalidates affected conclusions. Valid
independent survivors remain usable; role or status change alone requires no
repeat derivation. A declaration change is a new assessment subject.

## Residuals and acceptance gate

No complete admitted `M_b`, unique semantic interpretation, universal model
reliability, performance improvement, ABI runtime outcome or external consumer
adoption is claimed. Native usefulness remains bounded by the exercised task,
actor, host/model configuration and supplied context. Source framing and actual
runtime/user evidence qualify different relations.

The live RC7 declaration and Definition remain operative until independent
conservation assessment and a separately recorded exact internal configuration
decision at `{decision}` are consumed. That decision may bind only this
declaration URI/digest and proposed `{definition}` under the current direct
owner instruction. It records actual actor, owner authority, grant source,
time, exact evidence, scope and exclusions. Prior RC7 proxy authority is not
reused or expanded, and no human exact-byte inspection is claimed.

This is internal construction/qualification configuration only. It does not
accept immutable Product meaning, publish, authorize a future release, promote
an external caller's basis or replace STDO source authoring RC4. Existing
construction can obtain candidates and assessment evidence while the declaration
is proposed; no circular acceptance prerequisite is added. K-DOGFOOD and any
other required independence retain their stated separation.
"""
        candidate_frame = DEST / child / "REFERENCE_FRAME_BASIS.md"
        candidate_frame.parent.mkdir(parents=True)
        candidate_frame.write_text(header + common + trailer)
        candidate_definition = rebind(json.loads(definition_path.read_text()))
        candidate_definition["constitution"]["stdo"]["selector"] = "stdo://channels/2.5.1"
        candidate_definition["constitution"]["stdo"]["basis"]["manifest_sha256"] = sha(INSTALL / "manifest.json")
        candidate_definition["reference_frame_bases"][0]["authority"] = [
            "./specification/PRODUCT.md#product-disposition-authority", "./" + decision]
        candidate_definition_path = DEST / child / definition
        put(candidate_definition_path, candidate_definition)
        proposals.append({"project": child, "frame_uri": identity,
                          "frame_proposal": str(candidate_frame.relative_to(ROOT)), "frame_sha256": sha(candidate_frame),
                          "definition_proposal": str(candidate_definition_path.relative_to(ROOT)), "definition_sha256": sha(candidate_definition_path),
                          "live_frame_sha256": sha(frame_path), "live_definition_sha256": sha(definition_path),
                          "proposed_decision_path": child + "/" + decision,
                          "disposition": "Proposed only; independent assessment and separate exact configuration decision required before promotion."})
    put(DEST / "manifest.json", {"kind": "stdo.rc1-configuration-proposals", "schema_version": 1,
                                "selection_subject_sha256": sha(DEST / "selection-subject.json"), "proposals": proposals})
    print(json.dumps({"configuration_manifest": str((DEST / "manifest.json").relative_to(ROOT)),
                      "sha256": sha(DEST / "manifest.json"), "proposals": proposals}, indent=2))


if __name__ == "__main__":
    main()
