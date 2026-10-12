# T-018 - Publish STDO 2.5.0 RC1

- id: T-018
- title: Qualify and publish the joined STDO 2.5.0 RC1 carrier
- type: release
- ticket_category: release
- status: completed
- review_status: satisfied_published
- goal: publish one immutable reviewable STDO 2.5.0 RC containing the qualified a_c, Reference Frame boundary repair, and optional Traversal Occurrence Profile
- change_intent: close the supplied release-blocking findings, reconcile the exact successor inventory and release claims, and publish v2.5.0-rc.1 without inferring Product acceptance
- change_class: bounded_release
- re_entry_point: specification/GOALS.md
- triaged_at: 2026-08-30
- created_at: 2026-08-30
- updated_at: 2026-08-30
- completed_at: 2026-08-30
- owner: specification_methodology
- pen_holder: codex
- work_authorization: direct_human_authorization_2026-08-30
- predecessor_release: v2.4.3-rc.3
- predecessor_commit: eb87a20247beeb93de394523ebdf8faecfd71949
- predecessor_manifest_sha256: 312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551
- target_release_line: 2.5.0
- target_rc: v2.5.0-rc.1
- release_note: releases/v2.5.0.md
- depends_on: T-015, T-016, T-017 qualified and closed
- published_tag_object: 42f59b6cd24071d9c445a29ae2a691cf0828211e
- published_commit: ca6694314c4e9a56d3facae3eef06fe2792104c9
- published_manifest_sha256: 3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338
- accepted_product_cut: v2.5.0-rc.1

## Intake Triage

**Substantive?** Yes. The joined candidate adds the carrier-neutral axiomatic
calculus, repairs Reference Frame principle/profile/Product binding boundaries,
and adds one optional application-neutral traversal-occurrence profile.

**Boundary crossed?** Current Goals, release-scoped claims, the exact standards
inventory, source-project qualification, Git release carriers, and remote
publication. No downstream adoption, interpreted subject, carrier encoding,
runtime specialization, or final Product acceptance is authorized.

**Smallest lawful re-entry.** The constitutional re-entry remains owned by
T-015 through T-017. This ticket is their downstream release-publication
carrier and does not reopen or merge their independent outcomes.

## Admission Gate

Publication refuses until:

1. `a_c` has a closed finite record-kind and model-population law usable by the
   occurrence profile;
2. occurrence fields, typed relations, auxiliary domains, and admission
   judgments are congruent and their negative trials are substantive;
3. this source Product carries one complete Project Reference-Frame Basis;
4. deterministic functor provenance and transformation identities are exact;
5. the source project operates over verified `v2.4.3-rc.3` builder authority;
6. the complete successor member inventory and every semantic disposition are
   reconciled; and
7. all structural, digest, compression, packaging, installed-path, and
   independent pre-publication review gates pass.

## Publication Boundary

The Product subject is the exact `specification/standards/` member set declared
by `releases/v2.5.0.md`. The release note, license, plugin payload, and
subordinate toolchain assets are release-scoped auxiliary claims. Product,
Goals, tickets, comments, review records, and branch bookkeeping remain source
state unless the release note names them as protected claim inputs.

Publication creates and remotely verifies:

- mutable `rc/2.5.0` at the exact carrier commit;
- immutable annotated `v2.5.0-rc.1` at that commit;
- annotated `v2.5.0` selector at that commit; and
- optional `release/2.5.0` at that commit.

Publishing the RC supplies an immutable subject for exact-cut review. It does
not itself accept the RC as a Product or authorize any consumer adoption.

## Closure Law

This ticket closes only after the exact carrier is committed, all four release
refs are atomically published and remotely reacquired, the manifest and member
inventory reproduce from the immutable tag, and an independent exact-cut
review is recorded. Any qualifying-byte repair after publication requires
`v2.5.0-rc.2`; no published immutable tag may move.

## Non-Closure Conditions

- a green structural suite substitutes for the supplied semantic findings;
- mutable source or a checkpoint commit is called the RC;
- release-scoped bytes disagree with the immutable carrier;
- an unresolved predecessor claim lacks a semantic disposition;
- publication is represented as Product acceptance; or
- downstream STDO adoption is inferred from selector movement.

## Completion Evidence

Every closure condition is satisfied:

- immutable annotated RC: `v2.5.0-rc.1`, tag object
  `42f59b6cd24071d9c445a29ae2a691cf0828211e`;
- peeled commit: `ca6694314c4e9a56d3facae3eef06fe2792104c9`;
- repository tree: `f0fac91f195b1f1506423060556bd36b3256d835`;
- standards tree: `48a3e52b0aaf24b6d1d38ff551349e19b9b3c208`;
- standards inventory: 51 members with aggregate
  `87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5`;
- installed-manifest SHA-256:
  `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`;
- remote `rc/2.5.0`, `release/2.5.0`, immutable RC tag, and annotated
  `v2.5.0` selector reacquired at the peeled commit;
- independent exact-cut review: `GO`, `P0=0`, `P1=0`, `P2=0`, recorded in
  `.ai-workspace/comments/codex/20260829T203033Z_REVIEW_stdo_2_5_0_rc_1_exact_cut.md`;
  and
- direct human Product acceptance recorded in
  `.ai-workspace/comments/human/20260830T085826Z_DECISION_accept_stdo_2_5_0.md`.

Under the governing Release Method, the accepted Product is the immutable RC
itself. Acceptance creates no second final carrier. The existing release refs
remain unchanged, and no consumer adoption is inferred.
