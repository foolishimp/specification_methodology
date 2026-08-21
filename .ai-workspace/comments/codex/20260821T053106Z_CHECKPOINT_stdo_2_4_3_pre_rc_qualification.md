# Checkpoint: STDO 2.4.3 Pre-RC Qualification

- prepared_at: 2026-08-21T05:31:06Z
- prepared_by: Codex authoring Worker
- checkpoint_status: passed_ready_to_publish_immutable_rc1
- decision_authority: Jim, direct human Product owner
- standing_instruction: `ok release 2.4.3`
- selected_release_path: normal_rc_then_tap
- mutable_source_base: `19723b85142bf6219c4828cbfc1445f4eb8c3074`
- predecessor_release: `v2.4.2`
- predecessor_commit: `e50ee39a4e446dd781e6dc4e490076588c71982d`
- predecessor_tag_object: `d4724fff241f5511d47a30aa05ec9ff70f28d8d6`
- target_rc_branch: `rc/2.4.3`
- target_rc_tag: `v2.4.3-rc.1`
- target_release_branch: `release/2.4.3`
- target_release_tag: `v2.4.3`
- standards_members: 45
- standards_disposition: 21 changed, 24 byte-conserved, zero added, zero removed
- standards_aggregate:
  `3617ba1b13f134284564621b6e61dbce361d2f6341b768e4d90b5a47554c67cd`
- intent_sha256:
  `7ca105c692728b6b457e07794c0d5bfb6a82b0e2b61e283da3ae61bc2d84017f`
- product_sha256:
  `18fd94183f6c8d0515c21fb2bab1d3c27214172b50a5d423b5ec43a902828770`
- release_note_sha256:
  `b1d190be486b8e7a3266584cdb7680106ddd1400239f539fbca1623a12c8d08b`
- product_definition_schema_sha256:
  `3a617bdcd1665198d518af2103d02280a33603c2133e730e43ccbe55f10fab35`
- product_definition_template_sha256:
  `cdd5498f4357751a9e002e35ac843f4b83c70272171279631176ef888cb5c40d`

## Release Subject And Excluded Source State

The normative release subject is the exact 45-member
`specification/standards/` inventory declared in `releases/v2.4.3.md`.
Protected release-scoped claim inputs are `specification/INTENT.md`,
`specification/PRODUCT.md`, and that release note. The Apache-2.0 and plugin
assets named by the note are conserved protected carrier inputs outside the
normative member inventory.

T-012, comments, qualification and review records, acceptance records, branch
and tag existence, and publication bookkeeping are co-located mutable source-
project state outside the Product and release-scoped claim byte sets. No
excluded-state change may alter a qualified property or silently revise the
protected subjects.

Five pre-existing untracked 2.4.0 commentary files are unrelated to this
release and are excluded from the intended RC commit:

- `.ai-workspace/comments/codex/20260806T112919Z_LOG_admission_owner_constitution_and_abi_repair.md`;
- `.ai-workspace/comments/codex/20260811T023301Z_CHECKPOINT_stdo_2_4_0_direct_final_review_activation.md`;
- `.ai-workspace/comments/codex/20260811T024000Z_INPUT_stdo_2_4_0_reference_frame_qualification.md`;
- `.ai-workspace/comments/codex/20260812T062045Z_CHECKPOINT_stdo_2_4_0_direct_final_review_activation.md`; and
- `.ai-workspace/comments/codex/20260812T062045Z_INPUT_stdo_2_4_0_reference_frame_qualification.md`.

## Remote And Predecessor Identity

After `git fetch --prune --tags origin`, local `main` and `origin/main` both
resolved to `19723b85142bf6219c4828cbfc1445f4eb8c3074` with zero divergence.
Local and remote `rc/2.4.3`, `v2.4.3-rc.1`, `release/2.4.3`, and `v2.4.3`
identities were absent.

The local and remote annotated predecessor tag `v2.4.2` resolves to tag object
`d4724fff241f5511d47a30aa05ec9ff70f28d8d6` and peels to
`e50ee39a4e446dd781e6dc4e490076588c71982d`; local and remote
`release/2.4.2` resolve to the same commit. The predecessor aggregate remains
`5b5957d1a43be52a03b1316d442f2d797ba86a084550a1346dfc2dc6254123be`.
No published predecessor reference was moved or amended.

## Deterministic Pre-RC Qualification

The authoring Worker reproduced:

- exact release-note inventory order, membership, disposition, and SHA-256 for
  all 45 standards members;
- exact predecessor comparison of 21 changed, 24 byte-conserved, zero added,
  and zero removed members;
- the canonical aggregate and protected Intent, Product, release-note, schema,
  and Product Definition template identities above;
- all 18 compression digest edges: 17 deciding-source edges and one separately
  classified non-deciding glossary-index edge;
- 57 glossary index rows spanning all ten source-declared bounded contexts,
  with 27 distinct exact owning or relation clause locators and zero glossary
  term-definition headings;
- owner-context congruence for every glossary row and successful resolution of
  every cited file and heading;
- the semantic-address unique-resolution rule and the required `Frame`,
  `Owner`, `Product`, `Tenant`, and `User` collision/refusal cases;
- the positive local-resolution and complete cross-context-relation rules plus
  zero-candidate, multiple-candidate, selection, glossary-fallback, incomplete-
  relation, authority/basis, loss, and invalidation negatives;
- unchanged recursive-product concepts imported into World Model and all ten
  required coordinates of the directional Builder Project specialization;
- strict Draft 2020-12 structural validation with Ajv 8.17.1 and URI format
  assertion with `ajv-formats` 3.0.1;
- 13 Product Definition Overlay cases: four positive shapes, six structural
  negatives, two structural-versus-URI-assertion boundaries, and one selected-
  candidate semantic-membership refusal;
- equal minimum semantics in the Codex and Claude bootstrap templates after
  normalizing platform names, bootstrap filenames, and non-semantic line
  wrapping, at normalized SHA-256
  `b6dad87c46ea1a16cb9486ae57bda3047190acdc4a165874b7658716be6ca15f`;
- byte-equal canonical root and plugin Apache-2.0 licenses;
- exact release-note bindings for the repository README, marketplace registry,
  plugin manifest, and refresh skill;
- successful parsing of all five repository JSON documents;
- stable version-neutral live Intent and Product truth, no consumer-local
  provenance names in the generic reference-frame baseline, and a separately
  classified non-deciding glossary index;
- 62 relative Markdown file or anchor targets across 22 changed or protected
  Markdown surfaces;
- balanced Markdown fences across all 24 intended changed, protected, ticket,
  and checkpoint Markdown surfaces; and
- `git diff --check`.

## Checker Corrections

Initial author-side checker invocations exposed four harness defects: a zsh
loop reused the reserved `path` variable, a frontmatter parser treated a
multiline line-end as an end-of-block, a bootstrap comparison retained non-
semantic line wrapping, and a README assertion omitted the word `locator` from
the exact non-deciding-index phrase. Each checker was corrected and rerun to
the passing result above. No Product, standards, Intent, schema, template, or
release-note byte changed in response.

## Qualification Boundary And Open Gates

This checkpoint establishes deterministic mutable-source readiness for one
immutable RC publication. It is author-side evidence, not independent exact-
carrier review, human acceptance, or final publication.

The following final-release gates remain open:

- commit the exact intended carrier and publish and reacquire its immutable RC
  identity;
- perform required clean reconstruction against that frozen subject;
- obtain independent exact-carrier review by an actor who did not author the
  candidate;
- prove the proposed final carrier has zero protected-byte delta from the
  reviewed RC;
- bind direct human acceptance to that exact subject, carrier, and delta; and
- only then create and push the final release branch and annotated tag.

The standing human release instruction authorizes this governed process. It
does not convert this mutable-source checkpoint into independent review or
exact-carrier acceptance.

## Next Authorized Transition

The candidate may now be committed as one final-ready RC carrier, pushed to
`main` and mutable `rc/2.4.3`, and published as immutable annotated tag
`v2.4.3-rc.1`. The exact pushed carrier must then be independently evaluated
before the final release is tapped.
