# Claude candidate 5: reciprocal repair review

**Verdict: targeted changes required.** The four findings against candidate 3
are repaired. One retained material inconsistency remains in the wider intake
family: the Design profile can require structural repricing for a diagnosed
implementation-only defect. A separate Low concerns a helper's exit status;
the complete freeze command contains that failure. Neither finding calls for
an architectural rewrite or another broad qualification cycle.

The exact subject is Claude candidate 5, `3.0.0-rc.5`, source A
`4a63c9293ddaa568803b81f1ed5dcc1d3dc19cec`, with manifest and records at B
`a85f9ec98e43b942048a6c151aafd9662d2def90`. Candidate 4 was superseded before
review. Candidate numbers are tenant labels, not evidence of equal coverage
or acceptance. All source line references below are at A, relative to
`specification_methodology/v3/build_tenants/claude/`, unless B is named.

The common input is ratified C3-I5-06 at
`4c340f7adec9f3c893e3e267b23e4cadeb357854`. Installed builder v2.5.1-rc.2
was reverified valid against manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
The [activation and expectations](ACTIVATION_AND_EXPECTATIONS.md) preceded
candidate-body reads; each fresh Reviewer fixed its own expectations first.
Author tests did not supply semantic verdicts.

## Findings

**C5-01 — Medium: the Design surprise trigger still bypasses causal diagnosis.**

`standards/DESIGN_MODULE.md:553–557` says repeated or cross-cutting material
surprises establish that the design is underconstrained, require one
`design_reframe`, and leave retained code provisional until that reframe is
accepted. The offered Design frame repeats this at
`standards/frames/dm-task-d.md:161–165`.

The same section selects a prior design gate by unresolved material design
relations (`:508–540`) and calls it disproportionate when no materially
divergent architecture remains (`:559–565`). Its accepted-design reuse rule
(`:1582–1587`) permits an implementation refactor without new design
acceptance. Universal intake likewise permits repair under sufficient law
and preserves unknown causes (`standards/SPEC_METHOD.md:842–870,973–981`).

A concrete counterexample is a fully specified pure function adding two bits.
Its accepted design supplies the complete truth table, types, effects and
material boundaries. Successive implementations mistakenly use XOR and AND.
Both fail observed required cases; integer addition repairs them without
changing any design decision. Repetition does not establish a missing or
ambiguous design relation. The broad surprise rule nevertheless commands
`design_reframe`, whereas the governing diagnosis supports
`realization_refactor`.

This is a competing decision within the full source and its frame. It does
not prohibit inspecting design, gathering diagnostic evidence or activating
the separate gate when architectural ambiguity is actually established.
Reading “material surprises” narrowly as proven architectural ambiguity could
avoid the case, but that premise is absent from this independent trigger.
The risk is unnecessary structural work and renewed acceptance for an
implementation defect.

The clause is inherited and unchanged from candidate 3. The conservation
record honestly says it was conserved; that does not establish consistency
with the common construction requirement. Route this trigger through the
existing diagnostic owner and preserve the legitimate design-gap case.
Carry the resulting meaning into the affected frame, account and disposition;
do not repair just the displayed frame. Exact enclosing conditions, the finite
counterexample and the acquired consumers are in the
[intake review](INTAKE_REVIEW.md).

**C5-02 — Low: the standalone checker helper can report success after failing
to enumerate its projection work.**

`qualification/C3-ITER3/tools/run_ac.sh:8` obtains frame indexes in a command
substitution outside its `run` function and `FAIL` handling. If this separate
process fails after valid program validation, the loop runs zero times and
the helper exits zero. An independent fault injection over valid frozen
program bytes reproduced that behavior and retained a pre-existing projection
in the helper's output directory.

This does **not** produce a successful complete freeze:
`qualification/C3-ITER4/tools/freeze_ac.sh:9–12` removes the previous output
first and stops when the missing projection copy fails. The independent
enclosing probe returned nonzero before consumers ran. The original failed
control and validate/project propagation finding is repaired. Treat the
remaining helper case as a small failure-reporting correction, with its own
bounded adverse check. The injected interruption is a test condition, not an
observed production interruption. See the [tools review](TOOLS_REVIEW.md).

## Repairs established

| Prior finding or added repair | Current conclusion |
|---|---|
| C3-01, prior edge closure suppressed a new selection judgment | Repaired. Initial and post-closure typed no-actions retain their own predicate and core result; the preceding edge result remains distinct. Completed work with no new selection fabricates no result. Prose, function table, family argument, determination record and disposition summary agree. |
| C3-02, failed control could exit successfully through the freeze | Repaired. A forced failed identity control makes the complete frozen wrapper exit nonzero before its consumers; the normal wrapper succeeds. Validate/projection failures also propagate. C5-02 is the narrower helper residual, contained by that wrapper. |
| C3-03, recurrence's missing work-carrier dependency | Repaired. The Design family imports F13 and its recurrence row consumes the generic ticket rule while preserving the conditional Design refinement. |
| C3-04, four scopes stated above five | Repaired. The current interpretation entry names five scopes. |
| Constitutional chain, renewal, gap procedure and tenth drift signal | Repaired at all four named sites. A stable-direction requirements gap can re-enter Requirements; real direction changes retain Intent repricing. Their four changed predecessor determinations are proposed supersessions, not invented conservation or acceptance. C5-01 remains in the wider Design consumer. |

The [result review](RESULTS_REVIEW.md) also challenged stale evidence, an
unresolved reprice and uncertain external effects. No further defect was found
in that acquired relation. The current interpretation expressly leaves ODD
unencoded, and no offered frame copies its A4 rule. This source judgment
does not supply missing interpretation or actual-use qualification.

## Evidence and limits

The independent package checks reproduce all 81 manifest-admitted payload
files, plus the manifest itself, the source/tag/tree bindings and the packaged
bootstrap schema and template. Three changed frame bodies and their pins
match the frozen owners. Separate readback checked 235 declared owner-digest
occurrences and 44 selected shared-result/recovery paragraphs; those are copy
checks, not complete frame qualification.

The independent [record probe](record_probe.py) and
[receipt](RECORD_PROBE.json) reproduce the five affected intake/ODD rows'
predecessor and successor hashes, pending standing and counts. The current
record has 650 heading rows: 607 conserved author dispositions, 24 proposed
supersessions and 19 recorded bounded exclusions. Of the conserved rows, 423
remain without a current decided nonauthor reading. The older chain/renewal
readings are explicitly indeterminate rather than silently credited after
the repair. No count establishes semantic acceptance.

Verification-command probes ran in scratch copies. The initial default Python
lacked `jsonschema`; the affected install checks were repeated with the
existing installed-builder interpreter. That host limitation is not a
candidate defect. Positive materialization and failed-bootstrap/missing-anchor
paths were then checked. No dependency was installed and no actual candidate
worktree was used for mutation-capable commands.

The closed overall result is `falsified` for the bounded repair-family
consistency predicate because of C5-01. This retains the supported repairs and
the contained severity of C5-02. Whole-member/C3 acceptance, reserved owner
decisions, full interpretation, reduction, actual use and release standing
are not decided here. Existing owner deferrals retain their scope.

The parent authored the competing Codex implementation and parts of the common
WHAT. Three fresh Codex-family nonauthors performed the bounded readings of
Claude's source. The parent independently checked the material Design
counterexample and the helper's caller containment. These are not statistically
independent votes, and a donor cannot independently accept its own ported
contribution. Each report states acquisition and timing limits; native token
spend and active-context fit remain uninstrumented.

The timestamped review activation began at 13:55:55 UTC and the completed
report checks closed at 14:12:47 UTC on 2026-10-17: 16 minutes 52 seconds,
excluding preliminary repository discovery. No external paid actor calls were
made. All three delegated scopes returned within their progress checkpoints.

Only this Codex commentary directory and review scratch were written. No
candidate, common specification, ticket, index, branch, tag or installation was
changed. No commit, merge, push or publication was performed.

## Reciprocal subject

Claude's reciprocal review should read Codex RC4 package
`92fdb01c52bc4c6c7a7e265f92a668d0adb65098` and final records
`3d2708ef5a057d9bfbd2951b00b0e488285aaf89`, as identified in the
[visible handoff](../20261017T132252Z_HANDOVER_CODEX_V3_RC4.md).
That package already conditions the Design reframe on established Design
underconstraint at `successor/standards/DESIGN_MODULE_METHOD.md:482–488`.
This comparison identifies the current bytes; it is not an independent verdict
on the author's own candidate. No new Claude-authored review of that exact
package is claimed by this report.
