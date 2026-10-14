# Matched ordinary-use comparison

All three initial passes are closed and frozen at
`6627800d30b14cfb862d82709bf8ec5c86ca0401`. Each returned six tasks and 21 cases.
Independent grading is closed: all three arms meet 30/30 fixed assertions,
with no forbidden outcome observed. These cases establish no correctness
advantage for the current candidate.

## Fixed comparison

| Arm | Selected method subject |
|---|---|
| A | Installed STDO v2.5.1-rc.2, manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`; 71 members. |
| B | Preceding Codex `3ad1fca31dc93ba0847bbbbf308312a554daa1f6`; 80 members. |
| C | Current Codex `3aaa2f2cf0d6f24a734a33c258373a58feceaf87`; 89 members. |

The input recording commit is `cb14a63a2e75815a535d913fe93a65d9cdfd5c0e`.
All arms receive the same task packet, SHA-256
`d6f7bcba133228ae74c3b54f0055696da191fb697b5151070049566c3baaa559`.
The independent oracle was frozen before any actor activation, SHA-256
`088aa6f69ff2c243a530deea11b23ab4d4901fd98cba254c78a8cca47526a461`.
The parent checked its digest without acquiring its expected answers.
The six families cover evaluation, construction, domain binding,
release/adoption, recovery and triage/carrier selection.

Each actor starts at its own `plugins/spec/skills/stdo-work/SKILL.md` and
uses the same [acquisition reader](harness/acquire.py). The
[explicit prompt template](harness/ACTOR_PROMPT.md) differs only in arm and
local output coordinates. One fresh native context is used per arm across
all six tasks; model configuration is inherited without an override.
[Dispatch observations](harness/DISPATCH.json) identify the actors and actual
staggered starts. The trial does not control host load or measure retained
context, model tokens, attention or inference spend.

Installed rc.2 governs the activation; each method subject is applied to the
same synthetic fixtures. The source candidates are not installed or adopted
by this exercise. Only requested local artifacts and automatic acquisition
logs are writable. Actual publication, dispatch, network, installation,
external paid actors and cross-arm reads are excluded from the grant.

## Preparation and measurement boundary

The [reader controls](harness/CHECK.json) check exact emissions and repeated
reads, source/task drift, path confinement and section extraction. Emissions,
file I/O, unique opened files and elapsed acquisition time are separate
quantities. A recorded emission does not prove the host delivered every byte;
actor truncation disclosures and bounded reacquisition remain evidence.

Three preparations preceded actor use. The first refused before fixture
creation because a repository-relative path was evaluated from the tenant
subdirectory. The second omitted the installed manifest's auxiliary release
note; the explicit member comparison detected it. The third had the correct
71/80/89 member sets but was superseded by the 67-field metadata repair before
any acquisition. The preparation records and two unstarted fixture sets remain
in this directory. No result or acquisition log existed in any replaced set.
The successful preparation uses the exact source identities above and the
unchanged tasks and oracle; none of these replacements is an actor retry.

The initial passes receive no feedback. The oracle author grades only frozen
returns and records each assertion, actual artifact behavior, ambiguity and
any disagreement. A missing answer or unavailable observation is not a pass.
Any failure is triaged before a retry; old answers and expectations remain
unchanged. Findings are bounded to these selected cases and source cuts.

## Recorded completion and acquisition

[Measurements](harness/MEASUREMENTS.json) bind all returned artifacts and the
acquisition logs. Wall times below are actor-recorded work intervals, not reader
call time or the shorter interval between first and last acquisition.

| Arm | Actor wall time | Successful reader calls | Method/navigation emitted bytes | Total emitted bytes |
|---|---:|---:|---:|---:|
| A: rc.2 | 16m 01s | 23 | 156,413 | 235,739 |
| B: preceding Codex | 20m 40s | 26 | 258,956 | 339,549 |
| C: current Codex | 19m 51s | 40 | 199,496 | 284,930 |

Total emissions include task and metadata responses, repeated acquisition and
content whose delivery was clipped. Method/navigation emissions include read,
search and list output; they are not just excerpts. Method read-content totals
are 69,960 / 227,489 / 163,020 bytes. Full source-file I/O totals are
2,360,196 / 1,141,547 / 1,939,851 bytes, respectively. Search opens many files
without emitting their full bodies. Source I/O is not model input.

The [A return](arms/A/result/RETURN.md), [B return](arms/B/result/RETURN.md) and
[C return](arms/C/result/RETURN.md) disclose truncations and bounded reacquisition.
C also records one refused out-of-range read, so its 41 attempted acquisitions
produce 40 successful logger events. B records an administrative finalization
syntax error; C records a rejected patch operation. Those operations did not
supply new fixture judgments or feedback-driven retries. Constructor self-check
totals use different groupings and are not comparative correctness scores.

The current candidate emitted less material than the preceding candidate and
more than rc.2 in these particular runs. Actor elapsed time has the same order.
One same-model pass per method, with uncontrolled host load and individual
acquisition choices, does not establish a causal or general performance ranking.
The practical reduction over rc.2 has not been demonstrated by these costs.

## Closed assessment

The original independent oracle author returned the
[assessment](assessment/native-use-grading-01/ASSESSMENT.md), SHA-256
`d5ec5a7aa5449f62be86b9d2fccd0577634c0f3151cdf7293590b44a76681120`.
[Per-assertion judgments](assessment/native-use-grading-01/GRADES.json)
record all 90 evaluations. Each arm meets 30 assertions; none is contradicted
or unestablished, and all 21 cases have an answer. Expected unknown effects
or missing authority remain unresolved work states, not missing test answers.

Independent copied-code probes reproduce the required K1–K3 outcomes; index,
label and configuration artifacts also match their fixed expectations.
[Replay instructions](assessment/native-use-grading-01/REPLAY.md) preserve the
probe boundary. All 71 result-artifact pins in the harness summary and 69
source/view citation records verify. The grader uses the frozen logger summary;
it does not independently recount raw acquisition traces.

The [protocol account](assessment/native-use-grading-01/PROTOCOL_AND_COMPARISON.json)
retains truncations, bounded reacquisition, local authoring errors and incomplete
host-context measurement. No event found leaves a required witness missing;
persisted records cannot prove complete host-context isolation. No semantic
failure requires repair or retry under this fixed comparison.

The grader is the oracle author, knows the arm identities and uses the same
model family as the actors. It is independent of candidate and answer authorship,
not a second independent adjudicator or a cross-family assessment. Its wall time
is 1,101.4 seconds. Grader retained context, tokens and inference spend are not
instrumented. The [freeze](assessment/native-use-grading-01/FREEZE.json) binds
its exact returned files, SHA-256
`278fb38f07b8e76e3b6456b27d0203e621fa00ddd9ea807fdf6263a8a465baea`.
No stronger efficiency, installed-v3 operation, full frame coverage, member
acceptance or categorical-steel-thread claim is made.
