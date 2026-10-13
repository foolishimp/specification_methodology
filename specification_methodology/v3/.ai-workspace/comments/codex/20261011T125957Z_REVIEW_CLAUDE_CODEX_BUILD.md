# Claude And Codex STDO 3 Build Review

State: CLOSED bounded build comparison; changes required before Claude T1
qualification. Jim authorised this comparison on 2026-10-12
Sydney time: “review claude build against yours.” Review began at
2026-10-11T12:59:57Z. No tenant implementation or common source is changed.
The separately declared recording Writer owns only this review and its own-tenant
review checkpoint in Codex territory.

## Frozen Scope

| Subject | Commit | Tenant subtree |
|---|---|---|
| Claude build | eca8cefa28cf33677cd224d43aa0f7642653c8af | cedfe3fe2260754140f648506c0ba5f604d9bb88 |
| Codex comparison | bfe4173ccd1f9169f6bf05be2398cf0c4ce80095 | 65a8c2a0295541a805e9f120274ef9f98897d976 |
| Common WHAT | 00be6b8e674d61d96ed31e744e1d85adcd456df4 | stdo_3/specification and stdo_3.json |

Installed builder stdo://releases/v2.5.1-rc.2/ was verified natively, valid with
no failures; manifest SHA256
3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782.
Candidate reads use named Git bodies, not peer working files. Later commits are
outside this review. Root authored parts of the Codex build; its comparison is
not an independent acceptance assessment of its own implementation.

## Expectations Before Opening Claude's Candidate

Recovered from the common Product, P1–P6, capability questions and conformance
discriminators at the common commit before candidate content:

1. Preserve purpose, interpretation, scoped identity and common WHAT/HOW;
   distinct lawful layouts or algorithms need not match Codex's design.
2. Preserve coupled material relations across context acquisition, refinement
   and composition; unsupported fit, evidence or basis remains non-success.
3. Separate evaluation, next action, permitted effects and owner acceptance;
   retain known failures, citations, uncovered coverage and unfinished judgment.
4. Continue over applicable current workspace progress, observe changed
   dependencies and uncertain effects, and diagnose the owning cause before retry.
5. Keep foundational hypotheses, generic method semantics, optional domain
   profiles, examples and deployment fixtures in their declared scopes.
6. Distinguish draft coverage, actual construction, independent source-first
   assessment, actual defect detection/repair, mechanical a_c checks, semantic
   fidelity, qualification and release. Self-report or supplied judgment alone
   cannot establish the stronger claim.
7. Assess usable source discovery and material whole-path cost on the supported
   outcome. Counts, smaller files and prompt bytes alone prove neither adequacy
   nor efficiency. Per-activation limits are not universal method law.
8. Compare corresponding supported claims and unresolved gaps, including
   limitations in Codex's own evidence. Recommend bounded owning repairs without
   rewriting either candidate or selecting a canonical tenant.

The root AGENTS requires bounded delegation for context-heavy evaluation.
Separate source-first semantic and proof evaluators return read-only findings;
their observations will be conjoined here. Planning allowance: 30 minutes
elapsed for this comparison; provider token/cost counters are unavailable.

## Result

**Claude is ahead in documentary breadth and a_c encoding; Codex is ahead in
the proved construction → assessment → defect → repair path. The architectural
direction agrees. Neither build establishes complete STDO 3.0 qualification.**

Claude's complete draft is a useful larger design surface, not evidence that
its wider semantics have been exercised. Codex's useful first slice has more
actual behavioral evidence, not proof that its eventual complete corpus will
be superior. The tasks differ, so their times and byte counts cannot decide a
performance winner. Selecting a canonical tenant remains Jim's decision.

Citation convention below: C is the frozen Claude commit, K the frozen Codex
commit in the table above. Paths begin under the named tenant unless explicitly
marked common or installed. Line numbers refer to those exact Git bodies, not
the current peer worktree.

## Corresponding Capabilities

| Concern | Claude | Codex | Assessment |
|---|---|---|---|
| Foundations and interpretation | FOUNDATIONS: ontology, P0–P6, algebra and hypotheses | FOUNDATIONS: purpose, identity, interpretation, conservation and supported formal fragment | Same direction; broader equivalence, universal meaning and Markov/runtime claims remain hypotheses. |
| Shared transformation library | Bounded step plus acquisition, refinement, judgment, conjunction, reuse and disposition relations | Bind, Acquire, Transform, Evaluate, Conjoin and Dispose families | Compatible designs. Sharing implementation does not merge semantic responsibility or authority. Different primitive names are not a gap. |
| WHAT/HOW and profiles | SPEC_METHOD and PROFILES drafted | Boundaries present in Foundations; complete Spec/profile slice scheduled for T2 and later threads | Claude has more implementation here; Codex has an explicit remaining build gap. |
| Context and graceful stops | Context closure/fit procedure and two route-checking runs | Full/view construction, composition, unavailable body, invalid digest and refusal trials | Both have contractual acquisition evidence, not native context-window stress. |
| Current-state restart | CALCULUS restart/invalidators/uncertain-effect rules; trial still pending | Actual useful partial work retained across fresh continuation | Prose agrees; Codex has current bounded execution evidence. Neither pilot proves recovery from an OS crash or an uncertain external operation. |
| Assessment and repair | Review/evidence rules drafted; genuine document findings retained, independent T1 assessment and repair pending | Independent baseline/final reports, actual policy omission, repair and unchanged-source/criteria retest | Codex has the more complete observed join, with the misses and fixture failure below retained. |
| a_c | Program/map/two projections; reported zero diagnostics, 74 symbols, 80 clauses, eight residuals | No execution claimed; separate later thread | Claude has real candidate artifacts; admissibility and independent fidelity remain open. |
| Whole-method successor/release | Draft dispositions and case inventory | Eight selected cases with bounded support; eighteen not run | Neither is fully qualified, accepted as canonical, adopted or released. |

Claude's library principle is explicit at C: `standards/FOUNDATIONS.md:177–181`.
Its judgment/decision split is explicit at C: `standards/EVALUATION.md:29–47`
and `standards/CALCULUS.md:98–106`. Its restart account at C:
`standards/CALCULUS.md:148–165` preserves current work, applicable support and
effect uncertainty rather than demanding every history body. These are
material agreements with Codex's library and recovery design.

## Material Findings And Owning Repairs

### 1. The large-cap trial compares the wrong context boundary

**Material T-01 qualification defect.** C:
`qualification/cases/T-01/CASE.md:45–58` defines the deciding basis as
FOUNDATIONS §3 plus its cited rc.2 sections. Run A's cap is 160,000 bytes
(`CASE.md:64`). The correction at `CASE.md:143–147` nevertheless uses the
423,548-byte total of five entire members to preserve the over-cap premise.

Two separate evaluators reproduced the actual required population with the
case's heading-fragment rule: FOUNDATIONS §3 is 5,443 bytes; its 22 linked
sections total 38,337 bytes. The entire defined source context is therefore
**at most 43,780 bytes and fits Run A's cap**. The run itself acknowledges that size at
C: `qualification/runs/T-01/20261011-A-claude-fresh-001/RETURN.md:158–172`.

Counterexample: a single activation can acquire the whole declared deciding
basis without decomposition and stay inside the cap. A demonstrates voluntary
projection and route checking; it does not demonstrate decomposition required
by an unfit context. Installed `SPEC_METHOD.md:2090–2100` (UP-022) requires the
assurance boundary to match the claim. The whole-member premise is a different
population from the actual selected material.

**Owner: T-01 case design.** Narrow A's credit to selective acquisition/checking,
or freeze a successor with a genuinely over-cap required closure and rerun it.
Keep the original run's subject and limit. No core algebra change is required.
Run B's refusal evidence remains separately assessable.

### 2. The result-algebra merger misstates its source and successor standing

**Material source-fidelity defect, already acknowledged by Claude.** C:
`standards/CALCULUS.md:94–97` says RF-012 and AC-007 name the same five outcomes.
Installed RF-012 (`REFERENCE_FRAME_METHOD.md:409–422`) defines satisfied,
falsified, indeterminate, out_of_frame and invalid_basis. Installed AC-007
(`AXIOMATIC_CALCULUS.md:412–417`) instead requires a constraint's declared
algebra to preserve failed, missing, indeterminate, out-of-scope and
invalid-basis pressure. It does not define an identical five-member enum.

The corpus also calls those clauses conserved at C:
`standards/FOUNDATIONS.md:128–136,203–206` and superseded at C:
`standards/CALCULUS.md:94–97,218`. Its own standing definitions distinguish
conservation from an **accepted** successor replacement
(`standards/FOUNDATIONS.md:9–16`). No accepted replacement is established by
this draft. Claude retains these inconsistencies at C:
`qualification/RETURNS.md:150–157` rather than silently repairing the subject.

Counterexample to the source claim: a constraint can have missing support
without a counterexample defeating its predicate. Renaming pressure without
retaining the original claim/cause can turn missing evidence into falsification.
This review found the false source assertion, not an observed runtime coercion.

**Owner: CALCULUS's result contract and the corresponding Foundation/disposition
views.** Define the compatible projection and preserve causes; distinguish
semantic conservation from a proposed replacement of publication ownership.
Codex already spells out this separation at K:
`standards/EVIDENCE_METHOD.md:38–45`. Claude can make the same distinction in
its own HOW without copying Codex's layout or adding a primitive.

### 3. Tagged a_c bytes do not meet the declared Install prerequisite

**Material dependency-admission gap.** Common
`specification/requirements/A_C_DEPENDENCY.md:13,37` requires verification
through the selected Install before mechanical use. C: `a_c/t1/README.md:37–42`
reports a scratch copy of the executable/schema/output contract, explicitly
states that no Install was selected, and awaits Jim's dependency selection.

The evidence evaluator reproduced the seven pinned member hashes, the inventory
digest and the program's canonical digest. Tool identity is well supported.
Those observations do not supply the required installed standing or selection.
Labelling the outputs candidate evidence does not satisfy that prerequisite.
The reviewed returns disclose no explicit owner waiver/rebinding of it; a later
such grant would change this disposition and must be bound explicitly.

**Owner: the selected dependency activation, with common contract changes
returned to its owner.** Verify the exact selected Install and repeat affected
mechanical checks under it, or obtain an explicit owner-selected amendment
permitting the intended source-tool experiment. Retain the existing artifacts
as candidate observations; do not relabel them admitted qualification. This
review does not request or perform installation.

## Decisions And Proof Limits To Resolve

**Actor-family independence remains a policy premise.** C:
`standards/EVALUATION.md:67–70` and `qualification/cases/T-01/CASE.md:120–124`
exclude same-family assessors by default. Accepted C1 at C:
`design/PRINCIPLES.md:386–390,448–449`, and the common principles
`requirements/PRINCIPLES.md:108–113`, leave that issue open for C2.
Non-authorship and claim-relative independence are required; the deciding
builder clauses do not make model-family identity a universal test.

A stricter family policy can be proposed and selected where its assurance claim
justifies it. It should not silently answer the common open question or report
an unresolved independence relation as a proved lack of independence. Keep the
distinction between “not demonstrated admissible” and “demonstrated correlated.”
This is an owner-policy premise to settle, not evidence that Codex's same-family
assessments provide stronger assurance or that self-review is independent.

**Planned assessment versus uncovered coverage needs the exact discriminator.**
Claude preserves failure A and uncovered B at C:
`standards/FOUNDATIONS.md:157–163`. Before running its T-04, distinguish an
uncovered required obligation from an omitted planned authenticated judgment,
as the common conformance contract requires. Codex states this distinction at
K: `standards/EVIDENCE_METHOD.md:70–90`, but its T1 does not execute the full
Q11/Q12 discriminator either. The semantic evaluator found no concrete erasure
counterexample in Claude's prose; this remains a proof gap, not an invented bug.

**Run B's cap has limited meaning.** It excludes 130,793 bytes of resident
method/projection basis from its 6,000-byte per-step source cap (C:
`qualification/runs/T-01/20261011-B-claude-fresh-001/RETURN.md:95–102`). Two
refusals depend on the unresolved paragraph-recharging rule; an rc.2 fragment
itself exceeds the cap for another route. Keep the supported contractual
read-budget refusal, resolve the case-owned measurement rule and withhold native
capacity claims. The method need not acquire a universal byte quota.

**The constructor saw the desired decomposition shape.** C: `CASE.md:62–65,80–83`
exposes it, and run A relies on it at `RETURN.md:517–523`. That can specify a
protocol-following test. It is weaker evidence for spontaneous reconstruction
of the method's fit/refinement operation. A stronger recoverability claim needs
its corresponding held-out material and independent assessment.

## Codex's Failures And Remaining Gaps

The evidence reviewer independently inspected Codex's actual negative policy:
at ba768ed2, `qualification/T1/runs/authority-omission-v2/HANDOFF.md:44,48–51,60–66`
admits a generic recorded decision. For A-17 at 5 C with intact seal, an unsigned
non-Mira decision passes that policy while violating SOURCE S4. The b812ede7
repair restores the required signed owner decision; its complete HANDOFF is
byte-identical to the adequate b82415b baseline. Source/criteria pins and commit
ancestry corroborate the named documentary sequence. This is stronger evidence
than accepting an author's green summary.

It still has important limits:

- The original refinement report asserted “No signed decision exists” where
  SOURCE only said none was supplied. The first independent reviewer missed it
  until successor exposure. K:
  `qualification/T1/assessments/COMPOSITION_PRESSURE.md:95–101` preserves the
  miss; no blind initial detection credit is available.
- The first isolated-O3 mutation also broke coupled O4. Its fixture expectation
  failed. A new v2 criterion was frozen before a new negative/repair; it cannot
  retroactively pass the original isolation trial.
- Fresh continuation was a planned interruption, not an OS-crash or uncertain
  external-effect test. Source allowances excluded governance/method/workspace
  bodies, so the fit trials do not establish native context capacity.
- Assessors were fresh nonauthor contexts in one model family. Exact Git
  artifacts and native-parent observations support the stated provenance;
  retained files do not independently prove every actor exposure event.
- Complete Spec, qualification and profile documents, a_c execution, the other
  eighteen cases and whole-method/release qualification remain outstanding.

These limits are retained in K: `qualification/T1/RETURN.md`; they do not
erase its useful bounded construction/repair evidence.

## Observed Cost And Next Work

Exact frozen inventories: Claude has seven standards totaling 60,007 bytes and
939 lines; its 92-line structure document explains the reported 1,031 lines in
all. Codex has four standards totaling 25,059 bytes and 433 lines. Claude's a_c
territory is 411,778 bytes across eight files; Codex's qualification territory
is 287,216 bytes across 34 files. These are artifact volumes, not runtime memory,
model traffic, semantic coverage or efficiency.

Claude reports draft construction in 7 min 20 s, run A in 9 min 23 s and run B
in 12 min 23 s. Codex's broader construction/repair/assessment observation is
70 min 29 s, exceeding its 60-minute planning allowance. Different tasks,
assurance paths, scope and unavailable/incomparable provider counters prevent
a speed comparison. Neither build has proved contraction against an adequate
equivalent predecessor outcome.

Recommended order: repair Claude's bounded case and result interpretation;
resolve the dependency/policy premises needed by the next claim; independently
assess the frozen runs/program; then complete one actual useful-construction,
genuine-defect and bounded-repair join. The task may differ from Codex's fixture.
For a direct tenant comparison, use one source-owned task and comparison
predicate with each tenant's lawful HOW, recording exposure and whole-path cost.
Do not combine or select either implementation from this static review alone.

## Review Coverage And Effects

The semantic evaluator read all seven Claude standards, entry/design and the
source-owned case, without Codex implementation, raw run outputs or evaluator
reports. It independently checked the required context population. The evidence
evaluator read both bounded proof paths, reproduced relevant pins/ancestry,
program identity and the actual policy defect/repair; it did not judge all
program clauses for fidelity or rerun the validator. Root recovered deciding
source and inspected entry/library/specification contracts, authored case and
current standing, then conjoined the closed evaluations. Root's comparison to
its own build remains an author disposition, not self-awarded acceptance.

No new trial, candidate execution, repair, Install, peer working-tree read,
common update, merge, push, tag or release was performed. The persistent review
effect is this file and its review checkpoint on Codex's tenant branch. Current
integrity/routing and elapsed checks are recorded below; they are not additional
behavioral proof.

At final content verification, 2026-10-11T13:17:45Z, elapsed review observation
was 17 min 48 s (1068 s), within the 30-minute planning allowance. The evidence
evaluator reported 7 min 25 s; activations overlap and are not summed as elapsed
wall time. Provider token/cost counters were unavailable. Final recording and
checkpoint effects follow this observation boundary.

The recording Writer verified UTF-8/LF, final newline and no trailing whitespace,
the exact frozen subtree identities, deciding citation locations, unchanged
main and candidate files, an empty index and this sole new own-territory path.
Named-body measurements and independent counterexamples support the findings;
format and Git checks alone do not.
