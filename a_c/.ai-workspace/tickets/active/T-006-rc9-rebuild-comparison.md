# T-006 RC9 rebuild and comparison preparation

Status: current-version checkpoint and separate RC9 rebuild complete as inputs
for the planned comparison tests. New semantic assessment, comparison tests,
acceptance and release remain outside this completed increment.

## Owner instruction and basis

Jim requested a commit checkpoint of everything produced by this a_c work,
followed by rebuilding against the latest Claude and Codex versions so that
older/newer and Claude/Codex performance can be compared. The completed old
generation study and all its raw evidence are preserved at commit
`efae9c74`. This instruction grants local Git commits of this work, not a push
or inclusion of other sessions' V3 review files.

The independent Product continues to operate against installed STDO
v2.5.1-rc.2, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
V3 candidate documents are subjects, not operating authority. This is dogfood,
with no RC qualification, acceptance, publication or V3 dependency selected.

## Outcome and experimental boundary

Preserve `dogfood/stdo-v3-generation/` byte for byte. Build fresh Graphify and
direct-source representations of each latest source cut in a separate
`dogfood/stdo-v3-generation-rc9/` study. Reuse the exact checkpointed generator,
authoring contract, grounding helpers, model/settings, source-selection rule,
chunk ceiling and per-chunk budget. Retain all failed calls and recoveries.
Never seed new actors with old representations, grades or semantic probes.

Prepare an indexed comparison matrix of the eight old/new representations and
their source identities, generation evidence and resource totals. Performance
tests planned by the owner remain distinct from build verification. Old
source-bound fidelity grades do not qualify the new models.

Latest clean subjects resolved at 2026-10-18 07:30:30 UTC:

- Codex RC9 package `5592168e26759f37e730aed12c030a6061709ec4`, custody HEAD
  `c46e9f96381097245a6714164f03b72ad32116c0`.
- Claude RC9 source `c2cfa9b908d1722ae3f26c32fa4ece691083bdc3`, custody HEAD
  `3a2097137c3588ba44b98e3ea801ac7f2be1daf0`.

Codex's selected owner-source bytes are identical to the old RC5 corpus; its
fresh rebuild measures generation variability and changed subject coordinates.
Claude changes only `standards/ASSURANCE.md` and `standards/FOUNDATIONS.md`
among selected inputs. Both candidates remain unaccepted and unreleased.

## Activations and write territories

- Executive `/root` coordinates scope, consumes closed source and launch
  reviews, and does not mutate while acting in that role.
- Writer `/root` owns this ticket, the new study's orchestration, protocol,
  plans, fresh actor execution/evidence, mechanical assembly and comparison
  index; a_c README/Goals completion links; and local Git checkpoints of these
  effects. The existing ignored `.venv` may be used without global changes.
- Read-only `/root/ac_latest_sources` resolved the latest clean cuts and
  verified candidate member custody and exact selected-source deltas. Its
  closed return is consumed before source freezing.
- Writer `/root/ac_latest_sources` is now activated only for the new study's
  `freeze_sources.py`, `corpora/`, `evidence/source-custody.json` and
  `evidence/source-delta.json`, using immutable Git blobs. No candidate, old
  study, implementation, Git or actor effects are granted.
- Read-only `/root/ac_generation_design` reviews the new rebuild launch
  contract, frozen implementation/settings equivalence, source separation and
  coordinator preflight before actors. It may inspect source/plans/code but
  does not author or grade new semantic content.

All V3 source, other sessions' reviews, the old study, common implementation
and old semantic assessment material are read-only. Actual Graphify recovery,
native validation, custody and coverage checks establish their stated bounds;
they do not establish semantic acceptance or whole-method conformance.

## Completed construction

The current-version checkpoint is
`efae9c749275838029a871863f0b3ce7d7aba8b6`. The old study remains byte-identical.
The separate RC9 study acquired 93 selected source files from exact immutable
blobs and generated four new models. Its eight-cell comparison index includes
the preserved old Codex RC5 and Claude RC8 models under both authoring paths.

All 60 initial calls closed: 37 strict passes and 23 source/fragment failures.
Eighteen failed drafts were recovered mechanically, changing 27 grounding
entries with invariant non-grounding statements. One fresh Codex/Graphify
authoring attempt corrected an unsupported disposition ledger and still needed
grounding repair. Five grounding-repair calls completed successfully. All 66
calls and their usage, including failed drafts, are retained. The shared
three-call budget peaked at three and concurrency at four; all fresh authors
closed before any repair reservation.

All four assembled proposals account for every input chunk and pass native
validation/recovery. Both assisted models also recover unchanged through the
actual pinned Graphify backend. The generator, schemas, prompts, codec and
helpers remain unchanged from the tested checkpoint. The new source-bound
artifacts, rather than unchanged implementation unit tests, were verified.

`build_comparison.py --check` verifies all eight indexed models, carriers,
source files, selected inventories, model bases and artifact/result hashes.
Its separately reviewed manifest/source-binding repairs affect only this
post-build index; no frozen generation code or input was changed.

`README.md`, `COMPARISON.md`, `comparison.json`, `results.json` and retained
evidence under `dogfood/stdo-v3-generation-rc9/` are the return. The new models
remain ungraded semantically; older fidelity grades qualify only their older
source-bound subjects. No overall-performance test verdict, whole-calculus conformance,
operational qualification, acceptance or publication is asserted.

The independent resource/custody/index gate closed with no actionable defect:
all 66 raw calls, 93 selected source members, 444 freeze pin records, 14 new
and 14 old proposal-file hashes, and all eight index rows reproduce. Its
closed scope is retained in `evidence/resource-audit.json`. Final source
worktree reobservation remains clean at both selected RC9 custody heads.
