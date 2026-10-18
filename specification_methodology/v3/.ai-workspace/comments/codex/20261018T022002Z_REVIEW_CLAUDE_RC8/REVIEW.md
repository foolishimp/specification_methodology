# Independent review of Claude STDO v3 candidate 8

The material repairs hold in the affected paths. **One Low semantic
inconsistency remains.** RC8 no longer treats repeated implementation failure
as proof that the design must change, and its repaired tooling refuses the
failed and empty enumeration cases. The expanded diagnosis routes preserve
the governing authority and uncertainty distinctions in the cases examined.
ASSURANCE still overstates what a reported scenario failure establishes when
the observation itself may be faulty.

This is an affected readback, not acceptance of the whole candidate. It does
not support the claim that only the product owner's decisions remain:
conservation reading and actual-use qualification are still work to perform.

## Frozen subject and review basis

| Coordinate | Exact subject |
|---|---|
| RC8 source A | `9aee01ffa76cfbde1a6b8f1153a25bd6d71c216e` |
| RC8 records/package B | `1db13bfeb0675fc95de04aceccb214f5b76873fc` |
| Local annotated tag object | `08555a3b6f09df0a0297e59932dc7b6a967582bd`, verified to name A |
| Candidate 5 source | `4a63c9293ddaa568803b81f1ed5dcc1d3dc19cec` |
| Candidate 5 records | `a85f9ec98e43b942048a6c151aafd9662d2def90` |
| Common construction input | C3-I5-06, `4c340f7adec9f3c893e3e267b23e4cadeb357854` |
| Builder | Installed `v2.5.1-rc.2`, verified at manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782` |

Candidate paths below are relative to
`specification_methodology/v3/build_tenants/claude/` at source A unless B is
named. Common paths are relative to `specification_methodology/v3/` at the
common input. The review reads exact Git objects. It does not substitute the
author's explanation, command exits, or the candidate currently on main for
those objects.

[Expectations](ACTIVATION_AND_EXPECTATIONS.md) were recorded before candidate
body/diff acquisition. Two fresh-context readers separately examined semantic
behavior and tooling. The parent checked the affected records and frames and
independently reproduced the semantic counterexample against the common and
candidate owners. Codex has authored the competing tenant and the prior
findings; that interest is disclosed. This review did not author any Claude
repair. All effects are new review commentary and disposable scratch work.

## RC8-01 — Low: reported failure is still asserted to be actual disagreement

**Location:** `standards/ASSURANCE.md:62–68`; the same consequence appears in
its foundation-to-law row at `:96`. The determination and frontier account
carry that source meaning.

The clause says that when a scenario fails, actual behavior disagrees with its
expected outcome. Its next sentence correctly says that the observation may
be wrong. These statements do not cover the same cases.

Take a required and justified answer of 10. The implementation returns 10,
but a broken decoder records 1 and the scenario reports failure. Actual
behavior and expected outcome agree. The failure reports a discrepancy; it
does not yet establish a discrepancy in the actual behavior. With the decoder
unchecked, the latter remains unknown.

This is different from an incorrect expected answer. If the implementation
returns 10 and the test wrongly expects 11, there is actual disagreement with
the expectation, but it does not establish that the implementation violates
its requirement. RC8 handles that distinction correctly.

The governing common `specification/requirements/ASSURANCE.md:47` expressly
applies the observation limit to reported failures and requires support for
the observation binding. The candidate's own `standards/FOUNDATIONS.md:1272–1281`
states the same rule. The introductory consumer and its argument therefore
overclaim what their owner permits.

**Impact:** a reader can treat a failed measurement as an established behavior
mismatch. The following observation alternative, ASSURANCE §12 and the result
owners contain the error. No unauthorized repair, erroneous promotion or
runtime incident was demonstrated; this is a Low source inconsistency.

**Repair boundary:** align the ASSURANCE explanation and its argument with
their existing observation owner, then update the directly dependent records.
The case supplies no reason for another design, result system or broad test
campaign. No candidate edit is made by this review. Priority and disposition
remain with their owner.

The source routes and cases are recorded in
[SEMANTIC_REVIEW.md](SEMANTIC_REVIEW.md) and
[SEMANTIC_CASES.md](SEMANTIC_CASES.md).

## What the independent checks establish

| Repair or relationship | Evidence and conclusion |
|---|---|
| C5-01: repeated design surprises | `DESIGN_MODULE.md:553–562` distinguishes repeated realization errors under a complete accepted design from evidence that the design is underconstrained. The former permits `realization_refactor`; the latter retains `design_reframe` and the design gate. The changed argument at `:204` agrees. The original counterexample is repaired. |
| Litmus 11 and persistent delta | `SPEC_METHOD.md:329`, `:601–604`, intake triage and change classes preserve diagnosis, the observation/model alternatives, and re-entry at the owner of the actual change. A symptom no longer decides an upstream rewrite. |
| Missing scenario and wrong Product | `ASSURANCE.md:57–62` retains unverified operational meaning without inventing its cause. `EXECUTIVE_BASELINE.md:1690` separates a deviating realization from an insufficient governing definition. Required authority and design gates survive. The scenario-failure sentence has RC8-01 above. |
| C5-02: enumeration errors | Reviewer-injected failed enumeration, partial output followed by failure, and successful empty output each return 1 after real successful validation, with no projection. A complete freeze also propagates enumeration failure before copying tenant artifacts. |
| Freeze order | With a real change to generated consumers, complete freeze returns 0, produces ten projections and leaves all sixteen README pins equal to final bytes. A required-control failure returns 1 before consumer generation or README refresh. Earlier copies and the failure report remain; this is sequential failure handling, not rollback. |
| Package identity | B's manifest reproduces byte for byte: `2f3b79e0c7015887c471747b9d9ea6e298f66b5d2290124a09243e77018c2d7c`. All 62 standards and 17 plugin members, license and release note match A. Tag, repository tree, tenant subtree, standards tree and version labels agree. |
| Changed conservation records | All nine changed frontier records retain correct predecessor and successor pins. Their acceptance remains pending. Four newly superseded rows and the extended drift row are proposals, not silently conserved changes. |
| Determinations and consumers | All 56 changed determination records bind their current owner sections; 798 consumer-reference checks resolve. Semantic application was read for the affected causal routes. Link-derived native consumers explicitly remain semantically unresolved; their count supplies no independent proof. |
| Generated frames | All twelve frame identities and member pins match. Eleven change only digest text against candidate 5. The sole changed source excerpt in `dm-task-d` matches its owner literally after reversing relative-link rebasing; the remaining change is its byte-count presentation. This establishes affected copy fidelity, not task sufficiency. |

Tool evidence is in [TOOL_REVIEW.md](TOOL_REVIEW.md), with independently
selected fault injections and retained receipts. Record checks are replayable
with [record_probe.py](record_probe.py), whose result is
[record_probe.json](record_probe.json). Frame checks are replayable with
[frame_probe.py](frame_probe.py), whose result is
[frame_probe.json](frame_probe.json). None uses the author's green semantic
judgments as its oracle.

The two historically read conservation claims whose shared containing
section changed—ownership and downstream closure—retain their assessed
paragraphs unchanged. Their older readings remain bounded to those
paragraphs; they do not qualify the rewritten drift paragraph. The five
primary repaired frontier rows still record no nonauthor assessment and
pending acceptance. This review is evidence for its stated affected claims;
it does not edit that standing.

## Remaining work and disposition

The records support 650 heading rows: 603 marked conserved, 28 proposed
supersessions and 19 exclusions. Of the conserved rows, 419 remain unread by
a nonauthor. The 184 recorded readings comprise 182 `conserved` results and
two historical `changed` results whose disputed clauses are separately
proposed for replacement; they are not 184 whole-member acceptances.

At B, `qualification/C3-ITER5/RESULTS.md:18–31` also records an unrun shared
actual-use trial, 38 untraced deciding paths, and all six member criteria as
unresolved. Owner decisions on proposed replacement relations are a separate
dependency. Some wider interpretation and trial scope has expressly been
deferred by the owner; this review does not reopen it. It does distinguish
remaining qualification work from a request for owner decisions.

The bounded tooling and identity predicates are satisfied. The strict source
consistency predicate is falsified by RC8-01 even though its consequence is
Low. Neither result decides whole-candidate acceptance. The review finds no
new material blocker in the examined repairs, and provides no basis for
calling the complete candidate qualified.

The next useful action is a bounded correction of RC8-01 and completion of
the still-selected qualification work and owner dispositions. Repeating the
unchanged thirteen-command suite cannot supply those missing semantic
judgments or actual-use evidence. Any readback of the small correction can
remain at the changed source, argument and dependent records unless the
repair introduces a wider change.

## Limits and effects

This review covers the candidate-5-to-RC8 repair cone, its material owners,
consumers, generated records and local package identity. It is not a fresh
whole-corpus review, an installed-user trial, a comparative efficiency
measurement or an acceptance ruling. Earlier evidence is not promoted beyond
its stated scope. Remote publication was not checked; the local tag identity
was. The ordinary unchanged author suite was not rerun in full.

Tool executions used absolute disposable paths. The existing helper's
hardcoded checkout and relative-scratch portability limits are disclosed in
TOOL_REVIEW; no live peer writes were performed. No candidate, common
specification, branch, tag, commit, installed release or remote was changed.
Only this visible review directory was written. Host context and total model
token spend were not instrumented; scoped source-acquisition measurements and
their truncation limits are reported by the two readers. External paid actor
calls were zero.
