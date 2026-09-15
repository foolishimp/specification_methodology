# STDO 2.5.0 RC7 Release Work

Status: complete RC7 cohort qualified, atomically published and freshly
reacquired from the public repository. External consumer adoption is not performed.

## Stage A Writer Activation

Recorded before release-preparation effects. The owner's instruction is
"release stdo - this would be RC7 ?". Executive `/root` selects the complete
`v2.5.0-rc.7` cohort under
[`STACK_RELEASE.md`](../../../../../STACK_RELEASE.md#meaning-of-a-release-request)
and activates `/root/stdo_exec_posture_worker` as sole Worker/Writer, xhigh, for
Stage A. Activation identity: `urn:stdo:activation:20260915:rc7:stage-a-worker:1`.
Intake selects the RC7 release work wave (`goal_reprice`); the prior accepted
requirement amendment is unchanged. Stage A prepares the source/plugin/docs,
qualifies the bounded source subject, freezes commit A and its one local
annotated STDO tag, installs/verifies that exact tag, then returns to Executive.

The initial Git root is `/Users/jim/src/apps/specification_methodology`, HEAD
`0a0cd85229ed5290b14459d727121ba3c987861f`. Executive verified the same public
`main`, RC6 as the highest cut for all three Products, RC6 selectors, no RC7 and
endpoint `https://github.com/foolishimp/specification_methodology.git`. Worker
confirmed HEAD and exactly the ten previously accepted dirty paths at entry.

### Exact Operations And Territory

New editing territory, relative to the Git root:

- root `README.md` and `STACK_RELEASE.md`, only current release-facing text;
- STDO child `README.md`, `QUICKSTART.md`, `specification/GOALS.md`,
  `releases/v2.5.0.md`, both `plugins/spec/.claude-plugin/plugin.json` and
  `plugins/spec/.codex-plugin/plugin.json`,
  `plugins/spec/references/GETTING_STARTED.md`,
  `tests/test_plugin_distribution.py`, `tests/test_getting_started_setup.py`;
- this new release-evidence directory, including bounded generated evidence
  and temporary preparation.

Previously accepted root `AGENTS.md`/`CLAUDE.md`, root README/STACK changes,
the STDO normative baseline, two compressions, reference-frame test and the two
prior amendment comments are authorized staging subjects. The baseline,
compressions, reference-frame test, agent bootstraps and prior comments receive
no new edits. All other source authorities, manager/code, peers, historical
release evidence and immutable Product bytes remain conserved.

Executive conditionally grants exact staging of those subjects and this new
evidence, commit A, create-only annotated
`refs/tags/specification_methodology/v2.5.0-rc.7`, and installation/verification
of that exact local tag after source checks pass, the admitted normative bytes
remain exact and no conflicting remote RC7 or unrelated edit exists. This is
Executive's bounded promotion decision, not author self-acceptance. The new
RC7 Install and normal manager registration/acquisition caches may be created;
old release bytes must not be overwritten.

No push, mutable selector/branch move, child tag/construction, native provider
call, consumer adoption, unrelated mutation or delegation is granted. A check
requiring other source changes or a conflicting RC7 returns to Executive.
Record exact staged paths before committing. Never amend or move the new tag.

## Basis And Conserved Independent Judgments

Worker frame `urn:stdo:reference-frame:specification-methodology:worker:v1`
remains selected by the accepted revision-2 source-project frame basis; its
acquisition route is
`stdo://releases/v2.5.0-rc.4/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame`.
The operative source definition remains RC4 manifest
`4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e`.
`stdo status --definition stdo_default.json --verify` returned valid/installed,
no failures at entry. RC7 is the release subject, not automatic source adoption.

Independent `/root/stdo_exec_posture_review` returned `satisfied`, no findings,
for the source/invariant and release-instruction amendments; Executive accepted
both in the preceding records. Worker verified their unchanged exact subjects:

| Subject | SHA-256 |
|---|---|
| baseline | `234172dd0d403d28a3fdee9dfe740ba35b1c7656e92c249aa6f70af67c408ee1` |
| bootstrap | `9542d4c95dba044a08e2f17b84a3b6ab513fac6d96b7600a32baa45646c8d410` |
| aggregate compression | `8d30240a4d1323d838aad19051326ec6126040313f580c5a7ebeb8c146d56fcf` |
| Executive-posture record | `18cb383a9811b4fc6479f082c30e9f805a13c9999504014ae1d52a14cb97ba8b` |
| release-instruction record | `58daf1b8df2921de01ad0b5b7035b0eff00adda5362e9ba356a594faad806828` |

Prior RC6 helpers/evidence are read-only precedent. Adapted preparation stays
here and uses existing manager/checker mechanics. Source tests and structural
checks do not supply new native qualification. Stage B must author and qualify
the affected Executive semantics and regenerate/rebind the matched
Representation. Unchanged Axiom mechanics need exact conservation and bindings,
not an inferred engine redesign.

## Stage A Evidence And Result

Source preparation and bounded checks are satisfied. The adapted
[`prepare_stdo_note.py`](prepare_stdo_note.py) preserves the RC6 helper's exact
inventory/refusal approach and writes only generated evidence here. The release
note is applied from its candidate through `apply_patch`, never by rewriting an
old release artifact. The source/projection review bytes and prior acceptance
records remain exact.

| Subject | Exact aggregate and RC6 comparison |
|---|---|
| standards | 52 members, 3 changed/49 conserved; `b4769e7e689274f29b9d5b48674bf2d774392cab7aeebfd93834e008d309ba1b` |
| plugin | 17 members, 3 changed/14 conserved; `6bbf0eb583375f535dd3fcabd92397590a1843793ca57265571e435e9f4ad8fd` |
| manager | 11 members, all conserved; `1fb19c280cf6c31e81ce872865595ab1d6e9786897ef439fdda5750be89a6f07` |
| release note | `f3e09e4fe81d6031b64f084d41bafa41b6b9192b57c68ad76c018c15ce7dd6e0` |

[`source-inventory.json`](source-inventory.json) binds every member and prior
digest. [`qualification.json`](qualification.json) records exact commands,
environment, results and limitations: 35 affected checks passed (18 reference
frame, 5 compression, 7 plugin and 5 setup); all 152 source tests passed in
129.040 seconds. The existing verified manager Python environment supplied
`jsonschema`; no dependency installation was needed. An initial guide line wrap
failed two literal assertions; preserving the existing phrase and placing the
publication qualifier separately corrected both without weakening tests.

[`check_source.py`](check_source.py) produced satisfied
[`source-checks.json`](source-checks.json): 46 local links/fragments resolve,
the exact generated inventory matches source/plugin/manager bytes, and admitted
subjects remain conserved. `git diff --check` passed. Generated test fixtures
were confined to a fresh directory here and cleaned by their existing runners;
the empty enclosing directory was removed with `rmdir`.

[`remote-preflight.txt`](remote-preflight.txt) records the direct endpoint read
after qualification: every Product's highest published ordinal remains RC6,
with no RC7 or later cut. HEAD is still the initial checkpoint and the index
was empty. No unrelated overlap was found.

### Exact Pre-Commit Staging Record

[`staged-paths.txt`](staged-paths.txt) names the complete 30-path commit-A set,
including itself, before staging. Only those explicit paths may enter commit A.
The previously declared Executive conditional grant is consumed after checking
exact staged membership, whitespace and admitted source identity. The local
STDO tag must be absent before create-only annotated creation; it is never
moved. Local installation/verification follows that exact tag and returns its
identity without publication or source-basis adoption.

## Closed Stage A Return

Executive's conditional promotion predicates passed. Only the recorded 30 paths
were staged; staged membership and admitted normative digests matched, the
index had no unrelated content, and staged whitespace checks passed. Commit A
was created once; the STDO tag was absent locally and remotely before its
create-only annotated creation. The working tree was clean immediately after
commit A. Neither tag nor committed release bytes were subsequently changed.

| Coordinate | Exact local result |
|---|---|
| commit A | `ddeb971da89ee47065359c99897a825b803eedd4` |
| STDO annotated tag object | `ac0e72b49814c30caf373fe87cedce585bdd36b8` |
| qualified immutable ref | `refs/tags/specification_methodology/v2.5.0-rc.7` |
| repository tree | `14792247cc305f830f5c6bd62797d0fc2b70961d` |
| Project Subtree tree | `3637df6d1e4d1cba4b7882c3a6c9b84ddd041aef` |
| standards tree | `3c34d4324cb3f7188d03e4aff434715a785094f9` |
| installed manifest SHA-256 | `1f56029380604b0879fe322047fa8b38060297ba86b54bc8db8450d01ec034ae` |

[`git-freeze.json`](git-freeze.json) binds the exact operations and staged set.
`stdo install v2.5.0-rc.7 --repository /Users/jim/src/apps/specification_methodology`
returned the exact local tag/commit and new Install at
`/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.7`.
[`stdo-install.json`](stdo-install.json) retains that result.
`stdo verify v2.5.0-rc.7 --manifest-sha256 1f56029380604b0879fe322047fa8b38060297ba86b54bc8db8450d01ec034ae`
returned `valid: true`, no failures, as retained in
[`stdo-verify.json`](stdo-verify.json). All 52 standards and 17 plugin members
bind the qualified inventories above. The installed release-note digest also
matches the frozen source declaration.

The source project's `stdo status --definition stdo_default.json --verify`
still returns valid RC4 with its original manifest. Final tag/peel and
source/plugin/release-note comparisons to commit A are exact; no staged delta
remains. Post-freeze worktree changes are only this README and the three new
evidence records `git-freeze.json`, `stdo-install.json`, `stdo-verify.json`.
They record later events outside the immutable commit-A subject and are not
retroactive source qualification.

Stage A returns `candidate_ready` / `satisfied` for the granted local-cut and
Install outcome. No peer construction, native calls, commit B, child tags,
mutable selector/release-branch moves, push or consumer adoption occurred.

## Bounded Stage B Proposal

This proposal is not a new Worker grant or release readiness claim. Executive
consumes the closed Stage A return and selects the next dependency-ready phase
within the existing complete-release mandate.

1. Bind both companion release subjects to exact RC7 and their owning Product
   authorities. The current Axiom revision-10 and Representation revision-18
   frame declarations are RC6-specific according to Executive's acquisition;
   resolve and authorize any required internal basis/frame adaptation at their
   owners. Do not silently retarget them, change the STDO source project's RC4
   basis, or migrate external consumers.
2. Re-author the affected Executive axioms and their supporting/exception
   closure for event-driven attention, bounded fallback supervision and
   no-progress decisions. Preserve steel-thread delivery and all conserved
   meaning. Bind exact RC7 source digests and regenerate the map, affected frame
   projections and complete source-corpus record. Conserve Axiom engine bytes
   unless new owning evidence establishes an actual mechanics change.
3. Reconcile same-version companion dependencies, native skills/discovery,
   release docs/links and complete Product inventories. Use RC6 helpers only as
   read-only precedent adapted in this release carrier.
4. Before native evaluation, declare exact cases and oracles for ordinary
   in-grant progress/waiting; lost notification or expired checkpoint; material
   failure and continuing supervision; changed-workspace evidence validity;
   repeated no-progress requiring a bounded decision; and closed-return,
   independence and closure duties. Scope assurance to changed relations and
   conserved claims, preserve original evidence limitations, and use `xhigh`
   for live Codex workers, not old helper `max` or Ultra settings. Native
   observations and independent judgments remain separate from source checks.
5. Return the exact peer/index/native candidate for independent assessment.
   Once Executive admits the sufficient candidate, freeze commit B with the
   complete cohort record and exact remote expectations; proceed through the
   existing content, local-ref-graph, atomic-publication and public-reacquisition
   gates under their own activations. No dependency phase needs a new user
   request merely because it crosses the already selected peer boundaries.

Worker stops here pending Executive's next activation.

## Stage B Worker Activation

Activation `urn:stdo:activation:20260915:rc7:stage-b-worker:1` resumes the sole
Worker/Writer at `xhigh` under Executive `/root`. The owner request is
"release stdo - this would be RC7 ?". This selects the existing complete
cohort relation, not another Product. Intake is the continuing `goal_reprice`
release wave plus exact-source/dependency `requirement_reprice`; Product shape,
generic mechanics and the STDO source project's operative RC4 remain unchanged.

Executive consumes the closed Stage A result: commit
`ddeb971da89ee47065359c99897a825b803eedd4`, annotated STDO tag
`ac0e72b49814c30caf373fe87cedce585bdd36b8`, installed manifest
`1f56029380604b0879fe322047fa8b38060297ba86b54bc8db8450d01ec034ae`.
The exact verified RC7 Install supplies represented meaning. Both peer live
Definitions verify as RC6 with manifest
`bed7535a5feddc5e874993ff96d1f5f27e2a0fff63f366fc3b1fec3e301dd9e0`;
their accepted declarations are Axiom revision 10 and Representation revision
18. Their current binding remains active throughout this construction grant.

Exact write territory is `stack_release.json`; current release-facing root
`README.md` and `STACK_RELEASE.md`; both peer `README.md`, `QUICKSTART.md`,
`specification/GOALS.md`, `specification/PRODUCT.md`, requirements' selected
source/dependency identities and release-facing passages, and
`releases/v2.5.0.md`; the new Representation
`build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.7/`; its canonical
`skills/stdo-representation/SKILL.md` and `references/frame-index-use.md` only
for exact current-cut routing or source-grounded instructions needed by this
delta; and this new RC7 evidence directory. Proposed successor frame
declarations, Product Definition overlays and bounded decision scope remain
inside this evidence directory, unactivated until independent conservation
review and Executive's exact decision. Live frame/overlay writes are excluded.

The exact seven-member Axiom construction candidate is selected for validation,
projection and stdout joining before child release. Adapted existing helpers
may generate evidence only within the granted candidate/evidence/temp roots.
No source law frozen in A, Axiom mechanics/contracts/skills, old representation,
historical evidence, external consumer, ABG, manager, shared checker, UI
metadata, other native instructions, Git commit/tag/ref/push or publication
effect is granted. Preserve the four dirty Stage A records at entry.

Native execution is exactly four fresh read-only contexts: Codex source and
map-first with `gpt-6-astra` / `xhigh`, and Claude source and map-first with the
verified supported host configuration. Each host's arms share task, evidence,
capabilities, model and output contract. The independent task and withheld
oracle are archived separately unchanged before exposure; its forwarding typo
is corrected to the Reviewer's original `stdo://` spelling. Native actors may
read bound fixtures and use the exact pure joiner on stdout; they may not
write worksite/source/install bytes, spawn actors, run construction, install,
publish or adopt. Existing transport timeout applies, every raw outcome is
retained, and no semantic retry or extra context is authorized. Transport-only
preflight corrections before exposure may stay within these evidence paths.

This Worker authors and self-checks candidates; it does not supply independent
semantic acceptance. Return one frozen candidate/evidence set to Executive
before commit B, with unresolved conditions and exact proposed next effects.

### Bounded Axiom Runtime Repair Grant

Executive consumes the retained runtime discriminator: Python 3.13.7 deletes
the preexisting projection when an attempted source is a symlink loop, while
the previously qualified Python 3.12.8 refuses and preserves it. Source and
ordinary input bytes remain conserved. This is an existing output-protection
contract defect, not only a diagnostic difference.

The additional exact Worker grant covers
`axiom_indexer/build_tenants/core/code/ac.py` and `test_ac.py` only for that
demonstrated resolution/refusal defect and focused regression checks, plus
resulting identity/qualification reconciliation in the already granted current
docs, inventories and evidence. Intake is `realization_refactor`: restore the
existing contract without feature, runtime, locking, persistence, security or
cross-version architecture expansion. Preserve the original failed logs and
both discriminators. Qualify normal/optimized suites and the direct regression
under observed Python 3.12.8 and 3.13.7; claim no unobserved runtime. Then resume
the original four native contexts against the new exact dependency candidate.
No commit/ref/push, source-A mutation, historical edit, extra native context or
consumer adoption is granted. Independent acceptance remains external.

## Shortest-Path Resumption

The owner reports allowance falling from 8% to 2% and directs:
"youre demoted to xhigh get it released shortest path". The preceding Worker
and four native process groups are stopped; their incomplete outputs are
retained and are not passes, including two Codex wrapper exit-zero results
without final answers. No public ref changes occur before resumption.

`/root` explicitly activates as release Worker/Writer at the owner's selected
effort. The effect grant covers this release evidence, the already selected
current release records/Goals and cohort carrier, exact independently reviewed
peer frame/overlay bindings with bounded decisions, exact staging and commits
B/C, create-only child RC7 tags, qualified mutable release refs, the existing
checker-emitted atomic publication and fresh public reacquisition. The frozen
STDO cut, historical evidence and external consumer pins remain unchanged.
No new feature work, source-law amendment or resilience expansion is selected.

Independent `/root/rc7_final_review` did not author candidate, task, oracle or
native outputs. Its bounded source/code review finds no blocker. It confirms
that two fresh map-first native completions plus independent exact-source
evaluation and applicable conserved RC6 comparative evidence satisfy the
selected changed relation without repeating a four-arm experiment. The exact
original task and oracle remain unchanged, including every S0–S7 case.
The new population and configuration are recorded in
`native-short/coverage-selection.json`: Codex xhigh, Claude high, no model or
cost-superiority claim. Each run has a 600-second execution ceiling. The copied
preparation helper's escaped-newline defect is corrected before exposure; the
failed preparation and earlier interrupted contexts remain retained.

Previously passing checks are reused on their exact frozen inputs: 152 STDO
source tests; 31 Axiom tests in normal and optimized execution on both observed
Python versions; direct loop/output-preservation regressions; valid cohort
content; identical regenerated report/map; ten exact frame projections; and
native skill structure. These checks do not substitute for the independent
source/native result or authorize publication before that result is consumed.

## Closed Candidate Result

The [independent final review](independent-final-review.md) is satisfied with
no S0–S2 findings. Both fresh native tasks complete and their seven-section
joined requests match actual tool output byte-for-byte. Claude's contained
write attempt and abbreviated result wording remain explicit S3 limitations.
The original four interrupted attempts remain incomplete, including exit-zero
wrappers with no final result. No fresh controlled performance comparison or
universal instruction-following claim is made.

Executive consumes the closed source/code/configuration/native result and
authorizes the existing checked commit-B/ref/atomic-publication procedure.
The two internal source-project Definitions verify against RC7; STDO source
continues on its separately selected RC4 and external consumers remain unchanged.

## Closed RC7 Result

The complete matched `v2.5.0-rc.7` cohort is published. Source commit A is
`ddeb971da89ee47065359c99897a825b803eedd4`; qualified companion/carrier commit B
is `4824d5a05619e6957110b7ac97464b42ac84c096`. Each Product has its own annotated
immutable RC7 tag; discovery selectors and release branches identify those cuts.

- [Independent source/code/configuration/native review](independent-final-review.md): satisfied, no S0–S2 findings; contained S3 observations retained.
- Source tests: 152 passing; Axiom: 31 passing normally and optimized on each of Python 3.12.8 and 3.13.7, plus direct output-preservation regressions.
- Fresh native completion: Codex and Claude map-first tasks, correct S0–S7 decisions and exact actual seven-section joins; no actual worksite changes.
- [Atomic publication](atomic-publication.json): the shared checker-emitted 13-ref transaction succeeds with exact leases and create-only immutable tags.
- [Public topology](cohort-published.json): valid, no failures.
- [Independent published-cut review](independent-public-review.md): satisfied, no findings.
- [Fresh public reacquisition](public-reacquisition.json): all three exact cuts, 52 source members, 17 plugin members, seven Axiom members, nine Representation members, installed manager conservation, map/report and ten selected projections verify.

The first public-install attempt used an absent historical helper default and
did not execute an installer. Its [failure](public-reacquisition-attempt1.json)
is retained. The successful command explicitly selects the already verified
current manager; no Product or tag repair occurs.

Final release status and public evidence are recorded in the subsequent
bookkeeping commit without moving immutable tags. STDO source retains its
separately selected RC4 basis; both internal companion Definitions use accepted
RC7 configurations. No ABG, fleet, marketplace or external consumer migration
is performed. No future work is selected by this release closure.
