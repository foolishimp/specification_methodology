# STDO 2.5.0 RC7 Release Work

Status: Stage A activated; no RC7 publication or consumer adoption.

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
