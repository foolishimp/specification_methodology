# T-008 — Reprice Represented STDO Basis To RC2

- id: T-008
- title: Reprice STDO Representation 2.5.0 to published Source STDO RC2
- type: change
- ticket_category: constitutional
- status: completed
- review_status: go
- goal: GOAL-007
- change_intent: >-
    Replace the represented and constitutional Source STDO RC1 basis with exact
    published RC2 while preserving the Product version, shape, dependency, and
    accepted Representation RC1 history.
- change_class: requirement_reprice
- re_entry_point: specification/requirements/REQ-P-BASIS-AND-IDENTITY.md
- triaged_at: 2026-09-01
- created_at: 2026-09-01
- updated_at: 2026-09-01
- completed_at: 2026-09-01
- owner: stdo_representation
- pen_holder: codex
- work_authorization: direct_human_authorization_2026-09-01

## Exact basis

- Source STDO release: `stdo://releases/v2.5.0-rc.2/`
- installed-manifest SHA-256:
  `313e23116623a3bfbe96d279e089489aac466584982e1c34171ef244f0ec680a`
- standards member aggregate:
  `a5910bc56b491b5c520910e7bdad0949c1283e8b71951f1079e1fd86f59d20e7`
- candidate artifact root:
  `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.2/`
- accepted frame basis: revision 14, SHA-256
  `6cc05636ea00797e44f6ebb661d342d5b8cfb59cbde2a81059062dddf6eb106f`
- acceptance decision SHA-256:
  `68394d5118a6250972aa06db995a5d020c2f09996c90b0dfe70d4d8e908e8eba`

## Scope

1. Reprice active WHAT, Product Definition basis, bootstrap, and operator
   documentation to exact published Source STDO RC2.
2. Present project frame basis revision 14 for Product-owner digest acceptance
   and keep the overlay's `reference_frame_bases` empty until that decision
   exists.
3. After acceptance and exact overlay binding, reproduce and review the RC2
   compression and logical constraint index, then reprice only the native
   instruction routes and proof surfaces required by the unchanged Product.
4. Preserve semantic version `2.5.0`, the eight-member Product shape, exact
   Axiom Indexer `v0.1.0-rc.1` dependency, and all published Representation RC1
   refs, bytes, claims, decisions, and evidence.

## Refusal

- Do not reuse revision 13 acceptance for changed revision 14 bytes.
- Do not substitute mutable Specification Methodology source for immutable
  Source STDO RC2.
- Do not infer frame activation from authorship, validation, artifact presence,
  prior acceptance, or this ticket.
- Do not add a local engine, prompt orchestrator, GTL, automatic frame
  selection, or Product member.
- Do not publish or move any STDO Representation ref under this ticket without
  a separate exact release grant.

## Closure evidence

- Candidate commit `37e555de89320eafafefdcb529acfba05ad3b614`, tree
  `8ac263fc4bc66df0626b734f6c580007efc5c994`, and Project Subtree tree
  `ae9ab1273700e5845a9692fabeb46cba117a6ecf` bind the reviewed source
  candidate. The eight-member inventory is
  `a4a798b8206738c1dc966cf240590b6664472a57f928e0a9b4868b733f849c3d`.
- Independent candidate and Quickstart follow-up reviews returned GO with no
  remaining P0, P1, P2, or P3 findings. Constitution checks, normal and
  optimized tests, exact Source STDO verification, fleet verification, lint,
  formatting, and JSON checks pass.
- Fresh native Codex receipt SHA-256
  `a3a723e63a2f2076f454993da71c153678dd50a9b2c5f34f5e8a48a166838db1`
  records a clean native pickup and byte-exact join.
- Fresh native Claude receipt SHA-256
  `8cea975311702c03d9eea6419c66916b56ab6aaf7888260d1136613168e46eb5`
  records the same functional path and preserves its run-local HOLD for an
  unexpected temporary-file write and inaccurate no-write report.
- The initial full self-review receipt SHA-256
  `84edd489d9e4f2631e0646cd3a2ba554d7ab33688aa68f5f2fccdb5b67d65a02`
  returned `indeterminate` before Claude evidence existed and records its
  out-of-population memory reads. It is negative process evidence, not the
  qualifying result.
- The bounded C05 Reviewer result SHA-256
  `5a6424fa461913721c305b383dd7fef9f62d6ca2411c3ebd96836514deefd86d`
  returned `satisfied` with zero claim findings; run receipt SHA-256 is
  `b12810a48daa05a187dfa991df16c0a859e9090575245ab695fb999850656d5d`.

## Executive disposition

The RC2-basis requirement reprice and source-candidate freeze are complete.
The first indeterminate review is retained and replaced only as the current
qualification input by the later capable C05 activation; its result is not
silently rewritten.

The Claude temporary-file/reporting observation is outside C05 and receives
priority `P5` for the current promotion boundary: preserve the native run's
local HOLD and observe, but do not change Product bytes or block this source
candidate. No mandatory claim remains falsified, indeterminate, out of frame,
or on an invalid basis. This ticket grants and performs no STDO Representation
publication, acceptance, tag, selector, or branch mutation.
