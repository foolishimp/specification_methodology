# Plan: review of the first common build, against the baseline and on its own

Author: the Claude tenant session. It wrote the baseline (Claude RC9) and
most of the register's agreed forms. T-003 step 6 classes its review of
this build as a supplementary port and readback review: it cannot count as
independent review of the baseline content or of the register's wording.
This post is commentary. It accepts, merges or releases nothing.

The owner asked: "review against baseline and as its own standalone work".
This plan records the expectations before the candidate is opened. It was
written after reading only the contract and the pins, not the package,
`BUILD.md` or Codex's handoff post.

## Subject

- Package: `build_tenants/common/` on `tenant/common/standalone-v3`, tree
  `082df4ea2b7b3658aab528bbfbcfe81234ccc810`, 81 files. The tree is the
  same at the build commit `49445152` and at the evidence commit
  `d60dead4`.
- Construction record: T-003 and `.ai-workspace/common-build/` at
  `d60dead4`; handoff `156ac5af` on `main`.
- Baseline: Claude's package at `3a209713`. Donor: Codex `c46e9f96`.
  Shared requirements: `4c340f7`.

## Expectations

These sources hold them:

- the [register](20261018T114951Z_REVIEW_LOAN_LISTS_AGREED.md#the-register)
  at `d9a030d0`;
- this session's [readback](20261018T144743Z_READBACK_COMMON_BUILD_PLAYBACK.md)
  at `0cb4eea3`;
- T-003 at `2e7fa0f6`. T-003 adds the owner's standalone boundary and a
  longer exclusion list.

## Checks against the baseline

1. Strip the prior-version citation pattern from a copy of the baseline
   package, then diff that copy against the common package. Sort every
   remaining hunk into one of three kinds:
   - a register item;
   - a consumer or frame update of an item;
   - unexplained.
2. Compare file lists. Every dropped and every new file needs a reason.
3. For every block the baseline has and common lacks, look for modal force
   (must, never, only, requires). Where it carries an obligation, find
   where that obligation now lives.
4. Find each register item by section and quoted text, not by the
   register's line numbers.
5. Check that the eight meaning changes (M1–M7, A1) are each mapped, in the
   construction record, to their exact hunks and frame copies, so that the
   owner can decline one without the others.
6. Confirm the following:
   - R1–R4 and R6 are not landed;
   - no item from T-003's exclusion list is present;
   - the five-value result algebra, the entities and the responsibility
     boundaries are unchanged;
   - ACTIVATION §3 is unchanged.
7. Check the records: the 19 `not` values, the ten deferred compression
   rows, the ten conserved-but-changed rows, rows 93–96 and P1's class.

## Checks on the package as standalone work

1. Links and anchors resolve inside the package.
2. Search for history: prior versions, rc.2, loan IDs, agent names, tenant
   paths, `a_c/` and proposal markers. T-003's exception for generic law
   about revisions and provenance is judged by hand.
3. Self-application: does the package's own release, conservation or
   traceability law, applied to this candidate as a successor, require
   something the boundary moved outside the package?
4. Coherence: A1 at §6 against the four "complete Product view" passages.
   An inconsistency there depends on the owner's decision on A1's reach.
5. A reader that knows only the package. One Fable subagent at maximum
   effort gets a materialised copy of the package, with no repository or
   workspace, and three to five tasks drawn from the package's own entry
   routes. It reports every guess, dead route and term used before its
   definition. It shares this session's model family.
6. Mechanics, reproduced rather than taken from the report:
   - materialise the package from git and run the installed verifier;
   - run the package's own checks;
   - seed one defect per adopted gate (G1–G4, G6, G7) in a scratch copy;
   - spot-check frame copies byte for byte against their owner sections.
7. Side checks:
   - the admission's edits to `GOALS.md`, `stdo_3.json` and
     `build_tenants/README.md` against T-003's grant;
   - the committed Codex review files against the SHA-256 values in the
     register's Records.

## Severity

- **Blocks freeze:** a lost obligation, an unexplained meaning change, a
  broken route, history inside the package, or a mechanical claim that does
  not reproduce.
- **Material:** a register item in the wrong form or at the wrong owner, or
  a record defect.
- **Minor:** wording or style.

Items that are the owner's decision are listed apart from findings.
