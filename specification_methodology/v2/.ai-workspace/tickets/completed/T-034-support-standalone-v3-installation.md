# T-034 - Support standalone V3 installation

- id: T-034
- type: feature
- status: completed
- review_status: satisfied
- change_class: implementation_refinement
- re_entry_point: design/TOOLCHAIN_MANAGER.md
- created_at: 2026-10-19
- completed_at: 2026-10-19
- owner: specification_methodology
- pen_holder: codex
- work_authorization: direct owner request to update the installer for V3 while the common candidate is reviewed

## Outcome and boundary

Install an exact annotated V3 release whose published project root contains
`standards/`, `plugins/spec/`, `LICENSE`, and `release/release-note.md`. Preserve
existing release identities, manifest digests, exact-cut selection, atomic
installation, verification, and consumer-owned basis decisions. Installation
does not require an a_c implementation, a formal interpretation, or STDO
Representation. Their separate work is expressly excluded by the owner.

The consuming implementation is the current toolchain Python build tenant in
`specification_methodology/v2/`. Its operative builder remains
`stdo://releases/v2.5.0-rc.4/`, manifest SHA-256
`4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e`;
live verification returned valid with no failures before construction.
This is a cross-version distribution adapter, not a change to the builder
basis or either version's method meaning.

## Writer activation

Actor: Codex root, separate Writer activation under the accepted project
Reference-Frame Basis. Source checkpoint: `c4f59356`, isolated branch
`codex/v3-standalone-installer`. Granted operations: edit installer code,
affected tests, design and usage documentation, package version, and work
evidence; create local checkpoints; run tests and isolated fixture installs;
update the local installer executable after verification. Territory is this
toolchain child and its work carriers. No modification of the reviewed common
candidate, original tenants, a_c, Representation, immutable installed STDO
releases, real consumer definitions, release refs/selectors, or remote refs.

The bounded read-only audit identified the source-layout mismatch and confirmed
that basic installer commands have no excluded companion dependency. Root owns
the implementation. A separate nonauthor review will evaluate the frozen diff.

## Construction and proof

1. Recognize the standalone layout only at the published V3 project root
   `specification_methodology/v3/`. Do not choose build tenants. Reject absent
   and ambiguous source layouts, retaining prior layouts for older releases.
2. Map physical package paths to the established logical manifest paths;
   preserve the canonical standards digest recipe and record actual Git trees.
3. Exercise install, manifest, verify, resolve, repeat install, V3 consumer sync
   and bootstrap, plus missing/ambiguous/tampered inputs and V2 regressions.
4. Re-root all 81 bytes-exact members of common tree
   `082df4ea2b7b3658aab528bbfbcfe81234ccc810` into an isolated Git release
   fixture. Use actual annotated fixture refs and the real CLI. This proves
   installer compatibility; it is not a release or semantic qualification.
5. Preserve adoption's existing two-field mutation contract. Document that a
   V2-to-V3 consumer migration must review and replace obsolete entrypoint
   locators explicitly; schema validation alone does not establish resolution.
6. Review the frozen implementation independently, retain reproducible evidence,
   and deliver the verified installer without cutting or adopting V3.

## State

Completed within the authorized distribution-mechanics scope. The nonauthor
review returned `satisfied` with no material findings at `4d5de9aa`;
Executive consumed that bounded result and the passing regression evidence,
then activated the already-authorized Writer integration and executable update.
The implementation is on main as `1a37ee9f` and `79fa6edb`, and local `stdo`
reports `0.1.5`.

All 179 regression tests pass. Source and installed CLI replays reproduce all
81 common package payloads through a real annotated temporary Git tag.
Historical manifest identity remains exact, all eleven installed code modules
match the reviewed source, dependency versions are unchanged, and all 807
existing shared-store files are byte-identical. The
[result and evidence](../../comments/codex/20261019T034_v3_installer/RESULT.md)
retain subjects, commands, review, initial diagnostic failure and final results.

No method release, semantic candidate acceptance, real consumer migration,
remote publication, a_c or Representation work is claimed or selected.
