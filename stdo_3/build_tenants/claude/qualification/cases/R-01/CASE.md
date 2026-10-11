# R-01 Fresh-context activation and R-02 No private knowledge

Identity: urn:stdo-3:claude:case:R-01. One fixture serving the two
CONFORMANCE §3 rows and the thread T4 discriminating case in
[DOCUMENT_STRUCTURE](../../../design/DOCUMENT_STRUCTURE.md): a fresh actor
recovers a bounded activation from the documents; fidelity and
reconstruction cost measured, against the rc.2 corpus as baseline. Status:
designed; runs and assessments are listed at the end.

## Expectations owner

The expected distinctions are taken from sources the tenant did not author,
read at input commit `80b46944f1c1`:

- the common [capability questions](../../../../../specification/requirements/CAPABILITIES.md)
  "Method usability" (can fresh actors apply the documents without private
  validator knowledge or unnecessary whole-corpus loading?) and "Bounded
  work" (can an actor obtain sufficient context, refine work, compose
  results and select a truthful unknown/stop?);
- the common [conformance discriminators](../../../../../specification/conformance/README.md)
  "A parse or map succeeds" (the claim remains mechanical until
  independently sufficient semantic evidence exists) and "Carrier/process
  churn is proposed as new law";
- the comparative-baseline trial "Fresh-context recovery" (a new actor
  recovers and applies the bounded computational model from the published
  method; material definitions, dependencies and stopping conditions
  recovered correctly; context and interpretation cost recorded) and its
  criteria F27–F30 in the matrix post
  (`specification_methodology/.ai-workspace/comments/codex/20261006T015451Z_MATRIX_AI_DEVELOPMENT_METHODS_STDO_251_BASELINE.md`).

The tenant's CONFORMANCE rows and EVALUATION §7 are author material. An
assessor records expectations from the common sources before opening any
run record.

## Subject under test

The whole document set as frozen for T4, identified by digest in the T4
record under [a_c/](../../../a_c/README.md) and committed on
`tenant/claude/c3` as the freeze commit named in the runs table. The
baseline is the installed rc.2 cut `stdo://releases/v2.5.1-rc.2/`
(manifest `3d860ff4…2782`).

## Test subject and fixture material

- `subject/TASK.md`: a bounded evaluation task over a small fixture status
  record (feature F-7: one requirement with attached evidence on another
  build, two rows labelled PROVEN with PENDING measurements under them, a
  100% coverage figure, a reviewer's "all green" note, a release candidate
  that is not the build tested). The claim to decide is that the feature
  satisfies all three requirements and is ready for release. The record is
  invented; it is a test subject, not evidence about any product.
- [RECOVERY_CARD.md](RECOVERY_CARD.md): the card every actor receives. It
  asks for a record under seven headings (intake, context fit, results,
  facts, stop, handoff, cost) and tells the actor to follow the METHOD
  blocks where they direct and to say where it had no method source.
- [run_variants.py](run_variants.py): the fixture operator. Each variant
  is one fresh headless step actor through the generic instrument, whose
  whole context is the card, the variant's METHOD blocks and the TASK
  block, measured and logged before the actor exists.

| Variant | METHOD blocks | Measured context at design time |
|---|---|---|
| V0 | none (control: what the documents add) | 4,069 bytes |
| V1 | the STDO 3 route for an evaluation step: README, FOUNDATIONS, CALCULUS §1–3, EVALUATION | 38,220 bytes |
| V2 | the whole STDO 3 set, seven files | 70,702 bytes |
| V3 | rc.2 README plus seventeen rc.2 sections the author selected as the ones a bounded evaluation step needs (UP-020, UP-001, UP-008, UP-022, Probabilistic Work Boundary, RF-002, RF-007, RF-012, RF-014, engagement, AC-007, AC-010, AC-011, AC-014, baseline work result and reviewer, UP-007); the selection is private knowledge of the author, declared as such | 38,354 bytes |
| V4 | rc.2 README and the four members a reader of that README would open for construction and evaluation, whole: SPEC_METHOD, REFERENCE_FRAME_METHOD, AXIOMATIC_CALCULUS, STDO_REFERENCE_FRAME_BASELINE | 391,516 bytes |

V3 is the baseline with an oracle route; V4 is the baseline with the
whole-member loading the rc.2 README implies. R-02's withholding (no
validator folklore, no author memory, no whole-corpus loading) holds for
V1 by construction: the actor has no tools, no memory and only the route.

## Runs

Each variant runs twice (the trial is probabilistic), model `sonnet`,
cap 400,000 bytes per step, with one calibration step per run recording
the headless CLI's framework overhead. Allowance per run: 11 actor starts
and 30 minutes wall. The operator judges nothing; it records.

## Measurement and accounting

Per step: measured bytes, context tokens, output tokens, list cost, API
duration, model id, as the instrument logs them. Per run: the calibration
overhead and totals. Reconstruction cost per variant is the context
transferred in bytes and tokens, the API time and the list cost; the
output's fidelity is the assessor's.

## Expected distinctions

| Id | Distinction | Source |
|---|---|---|
| E1 | In V1 and V2 the record names the intake fields (outcome, affected set, basis by identity, grant, re-entry), records the context measurement as taken before reading, returns one of the five members per requirement with quoted evidence, never satisfied for a PENDING row or for the label alone, a composite that is not satisfied, step-produced facts, one stop state and an executable handoff, and cites the document and section for each; the assessor judges that these are the governing relations of CALCULUS §1–3 and EVALUATION §1–2 and §5, recovered. | capability question (method usability, bounded work); matrix trial |
| E2 | V0 shows what the documents add: where V0's record lacks a distinction that V1's carries (fit measurement before read, the five-member result, claim/evidence/authority separation, labels are not acceptance, re-entry to the owner), the difference is attributable to the documents, not to the actor. | matrix trial (F29) |
| E3 | V3 and V4 recover the same distinctions from the rc.2 corpus or do not; the record states which rc.2 clauses the actor cited and which parts it produced without a source. The assessor compares fidelity across V1, V3 and V4 on the same relation population. | EVALUATION §7; matrix trial (F27, F28) |
| E4 | Reconstruction cost is recorded per variant with its measurement source; V1's context is smaller than V4's and comparable to V3's; the difference between V1 and V3 is explained by the route (V3 needed an author's selection, V1 a README route). | matrix trial (F30); common discriminator (churn) |
| E5 | No record reports claim K satisfied; any record that does is a material error the assessor records against the variant. | common discriminator (a parse or map succeeds) |

## Assessment

An assessor other than the author, under a review Jim authorises, reads
the run directory at a named commit, records expectations from the common
sources first, and returns a review result per EVALUATION §4 over E1–E5,
judging the fidelity of each record against the relation population above
and the costs as logged. The assessor makes no repair. The author's
structural check of the records (headings present, result words, citation
counts) is mechanical evidence under EVALUATION §2, not assessment.

## Runs and assessments

| Run | Operator | Record | Assessment |
|---|---|---|---|
