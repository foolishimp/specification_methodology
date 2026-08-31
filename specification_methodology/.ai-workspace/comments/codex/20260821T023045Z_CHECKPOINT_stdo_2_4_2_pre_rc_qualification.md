# Checkpoint: STDO 2.4.2 Pre-RC Qualification

- prepared_at: 2026-08-21T02:30:45Z
- prepared_by: Codex authoring Worker
- checkpoint_status: passed_ready_to_publish_immutable_rc1
- decision_authority: Jim, direct human Product owner
- standing_instruction: `ok release 2.4.2 and push to remote`
- selected_release_path: normal_rc_then_tap
- mutable_source_base: `a46b13ccff452386c5879fb106c30c6b98cc895d`
- predecessor_release: `v2.4.1`
- predecessor_commit: `c37452a390e8456863eeb4e3d5bf9c9a237a44ed`
- predecessor_tag_object: `a570e3d46df0b1e635d55bbcf060139c2bdfcb71`
- target_rc_branch: `rc/2.4.2`
- target_rc_tag: `v2.4.2-rc.1`
- target_release_branch: `release/2.4.2`
- target_release_tag: `v2.4.2`
- standards_members: 45
- standards_disposition: 17 changed, 26 byte-conserved, two added, zero removed
- standards_aggregate:
  `5b5957d1a43be52a03b1316d442f2d797ba86a084550a1346dfc2dc6254123be`
- product_sha256:
  `a568e61c2a120fa1f013359bf3b49a59b128482e4c938c2b2401babbcdd7330c`
- release_note_sha256:
  `6a9eb8da6220c7dbc326e061490f9e6be5823b8d9557931816e1c9ad429c337c`
- product_definition_schema_sha256:
  `59739be97bc8caa688ce522e6e8a6b0c616395c6cea9f58d1caed73f6e5c1db1`
- product_definition_template_sha256:
  `9438031c8f1c77002699388b55da3176b13236f21ec6f102c50a95fa0b4e7a14`

## Release Subject And Excluded Source State

The normative release subject is the exact 45-member
`specification/standards/` inventory declared in `releases/v2.4.2.md`.
Protected release-scoped claim inputs are `specification/PRODUCT.md` and that
release note. The Apache-2.0 and plugin assets named by the note are conserved
protected carrier inputs outside the normative member inventory.

The active goal ticket, comments, qualification records, review records,
acceptance records, branch and tag existence, and publication bookkeeping are
co-located mutable source-project state outside the Product and release-scoped
claim byte sets. The deleted `specification/GOALS.md` is intentionally absent;
T-011 is the bounded current goal carrier. No excluded-state change may alter a
qualified property or silently revise the protected subjects.

Five pre-existing untracked 2.4.0 commentary files are unrelated to this
candidate and are excluded from the intended RC commit:

- `.ai-workspace/comments/codex/20260806T112919Z_LOG_admission_owner_constitution_and_abi_repair.md`;
- `.ai-workspace/comments/codex/20260811T023301Z_CHECKPOINT_stdo_2_4_0_direct_final_review_activation.md`;
- `.ai-workspace/comments/codex/20260811T024000Z_INPUT_stdo_2_4_0_reference_frame_qualification.md`;
- `.ai-workspace/comments/codex/20260812T062045Z_CHECKPOINT_stdo_2_4_0_direct_final_review_activation.md`; and
- `.ai-workspace/comments/codex/20260812T062045Z_INPUT_stdo_2_4_0_reference_frame_qualification.md`.

## Remote And Predecessor Identity

After `git fetch --prune origin`, local `main` and `origin/main` both resolved
to `a46b13ccff452386c5879fb106c30c6b98cc895d` with zero divergence. Local and
remote `rc/2.4.2`, `v2.4.2-rc.1`, `release/2.4.2`, and `v2.4.2` identities were
absent.

The annotated predecessor tag `v2.4.1` still peels to
`c37452a390e8456863eeb4e3d5bf9c9a237a44ed`; `release/2.4.1` resolves to that
same commit. No published predecessor reference was moved or amended.

## Deterministic Pre-RC Qualification

The authoring Worker reproduced:

- exact release-note inventory order, membership, disposition, and SHA-256 for
  all 45 standards members;
- 43 predecessor members and the exact successor disposition of 17 changed,
  26 byte-conserved, two added, and zero removed;
- the canonical aggregate, Product, release-note, schema, and template
  identities above;
- all 17 source-to-compression digest edges across six compression assets,
  including the normative schema edge in the aggregate compression;
- strict Draft 2020-12 structural validation with Ajv 8.17.1 and URI format
  assertion with `ajv-formats` 3.0.1;
- positive schema cases for the default template, a null bounded context, and
  an identity-complete composition edge;
- negative schema cases for missing and empty reference-frame bases, an
  embedded frame registry, missing composition target identity, empty
  governing contracts, and malformed asserted URI syntax;
- equal minimum semantics in the Codex and Claude bootstrap templates after
  normalizing their declared platform-specific names and bootstrap filenames;
- byte-equal canonical root and plugin Apache-2.0 licenses;
- exact release-note bindings for the repository README, marketplace registry,
  plugin manifest, and refresh skill;
- valid marketplace, plugin, schema, and template JSON;
- no release version, predecessor identity, or candidate aggregate embedded in
  the live `specification/PRODUCT.md`;
- balanced Markdown fences across changed and protected Markdown files; and
- `git diff --check`.

## Harness Corrections

The first compression-check invocation selected only filenames ending in
`.compressed.md`, which excluded the aggregate file named
`stdo_compressed.md`. The corrected invocation selected all six compression
assets and reproduced all 17 edges.

The first auxiliary-asset invocation used `.codex-plugin` paths. The repository
assets and release note correctly use `.claude-plugin`; the corrected invocation
reproduced every declared digest and both JSON documents parsed. These were
checker-configuration errors. No candidate byte changed in response.

## Qualification Boundary And Open Gates

This checkpoint establishes deterministic mutable-source readiness for one
immutable RC publication. It is not an independent review and does not claim a
fresh-constructor result where the exact-cut evaluator requires one.

The following final-release gates remain open:

- publish and reacquire the exact immutable RC identity;
- perform any required clean reconstruction against that frozen subject;
- obtain independent exact-cut review by an actor who did not author the
  candidate;
- bind direct human acceptance to the exact release subject, reviewed carrier,
  and final-delta relation; and
- only then create and push the final release branch and annotated tag.

The standing human release instruction authorizes this governed process. It
does not convert this mutable-source checkpoint into independent review or
exact-carrier acceptance.

## Next Authorized Transition

The candidate may now be committed as one final-ready RC carrier, pushed, and
published as mutable branch `rc/2.4.2` plus immutable annotated tag
`v2.4.2-rc.1`. The exact pushed carrier must then be independently evaluated
before the final release is tapped.
