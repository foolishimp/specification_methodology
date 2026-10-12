# Checkpoint: STDO 2.4.1 Pre-RC Qualification

- prepared_at: 2026-08-17T04:06:00Z
- prepared_by: Codex authoring Worker
- checkpoint_status: passed_ready_to_publish_immutable_rc1
- decision_authority: Jim, direct human Product owner
- selected_release_path: normal_rc_then_tap
- predecessor_release: `v2.4.0`
- predecessor_commit: `e05984c4f3b75525e6d962f6b9d72bbedd8e271a`
- predecessor_tag_object: `66118f3c5808536df5e5393d725e54e4eebc45f4`
- target_rc_branch: `rc/2.4.1`
- target_rc_tag: `v2.4.1-rc.1`
- target_release_branch: `release/2.4.1`
- target_release_tag: `v2.4.1`
- candidate_generation: 02
- standards_members: 43
- standards_disposition: six changed, 37 byte-conserved, zero added, zero removed
- standards_aggregate:
  `0f46a3d583f321da0445331566ef878e11e19e16e71c54fb9a8e66c5fff4ce91`
- product_sha256:
  `aa1eb79808be2b82acc59d58b27965dbbce3d14135c11084461b7191493cf066`
- release_note_sha256:
  `7756e23f34ccd06280549ebb81fb1cdd0a8b77da291516ddd46f16a511ca27ea`

## Release Subject And Excluded Source State

The normative release subject is the exact 43-member
`specification/standards/` inventory. Protected release-scoped claim inputs are
`specification/PRODUCT.md` and `releases/v2.4.1.md`. The Apache-2.0 and plugin
assets named by the release note are conserved protected carrier inputs outside
the normative member inventory.

Goals, tickets, comments, qualification records, review records, and
publication bookkeeping are co-located mutable source-project state. They may
be included in the repository carrier but are excluded from the Product and
release-scoped claim byte sets. No excluded-state change may alter a qualified
property or silently revise the protected subjects.

## Fresh Construction

The declared neutral input carrier is:

- `.ai-workspace/comments/codex/20260817T034022Z_INPUT_stdo_2_4_1_amendment_qualification.md`;
- SHA-256:
  `f06e4b5be3dc5da79905469921e3f55706ae4cdd6d7f8b40a922ce72bdc6455e`.

The fresh constructor result is:

- actor/session: Claude Opus 5,
  `e212d5eb-dd92-43a7-8e27-2542e7aef375`;
- `.ai-workspace/comments/claude/20260817T040350Z_QUALIFICATION_stdo_2_4_1_amendment_fresh_constructor.md`;
- SHA-256:
  `4ecf46336c5828ec9fd41b1b40e6c7539b8e7a590049822c514f265a560ce448`;
- population: every `F-01..F-12` and `T-01..T-11` case and sub-case;
- closed result: `candidate_ready` / `satisfied`; and
- repository mutation by constructor: none.

The constructor reproduced every protected identity and predecessor/member
disposition. Its retained `G-2..G-8` cases are synthetic-input or
synthetic-Product gaps that correctly exercise refusal and residual behavior;
they are not candidate-method defects.

## Deterministic Pre-RC Qualification

The authoring Worker independently reproduced:

- exact predecessor commit, annotated tag, current `main`, and `origin/main`;
- 43 predecessor and 43 successor standards members;
- exactly six changed and 37 byte-conserved standards members;
- every source digest pin and changed-member release-table digest;
- aggregate, Product, and release-note identities above;
- equal minimum semantic projections in the Codex and Claude bootstrap
  templates after platform-label normalization;
- byte-equal canonical root and plugin Apache-2.0 licenses;
- valid marketplace and plugin JSON;
- one active T-010 plus factual T-007, T-008, and T-009 publication closure;
- balanced Markdown fences; and
- `git diff --check`.

Local and remote `rc/2.4.1`, `v2.4.1-rc.1`, `release/2.4.1`, and `v2.4.1`
identities were absent at this checkpoint. The unrelated pre-existing untracked
2.4.0 commentary files are not part of the intended 2.4.1 RC commit.

## Next Authorized Transition

The candidate may now be committed as one final-ready RC carrier, pushed,
published as mutable branch `rc/2.4.1` plus immutable annotated tag
`v2.4.1-rc.1`, and independently reviewed at that exact commit and tree.

This checkpoint does not perform the independent review, human exact-subject
acceptance, final tap, or publication closure.
