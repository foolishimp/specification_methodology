# Release R-9 gate

Compiled under method frame EVALUATION_CONJUNCTION.md (frozen method commit a746559e00ebfd6b98a7278b219b3ccc9c929341): FOUNDATIONS.md Result algebra and Result conjunction; REFERENCE_FRAME_METHOD.md RF-005, RF-012, RF-015, Applicability And Required Results.

This gate records evaluation results only. It is not a release decision. No release decision authority is bound in the workspace, and this compilation exercises none.

## Composite subject and basis

- Subject: release R-9, workspace HEAD `3f2c9a1`.
- Required coverage set: COVERAGE.md (CR-1, CR-2). This is the declared required set.
- Plan: ASSESSMENT_PLAN.md. A1 is the only planned assessment.
- Composite predicate: every required coverage item is satisfied on its basis at HEAD `3f2c9a1`.

## CR-1: security of auth/

- Predicate: auth/ meets the ASVS-L1 checklist.
- Subject and basis: `auth/@3f2c9a1`, ASVS-L1. The plan subject commit matches HEAD `3f2c9a1`.
- Contribution: planned assessment A1, `results/A1.json`.
- Authentication: A1 matches the plan on producer (sec-rev), subject (auth/@3f2c9a1), basis (ASVS-L1), result path and evidence path.
  - Residual: producer identity is asserted by the file contents only. No signature or other independent producer attestation is available.
- Original domain outcome: `judgement: "fail"`, with a stated reason.
  - Citation: `auth/login.py:3 password compared with == against stored plaintext`.
  - Evidence (`evidence/A1.md`): ASVS 2.4.1 "Not met".
- Corroboration: `auth/login.py` line 3 reads `return rec['password'] == pw`. This is consistent with the citation.
- Verdict: **falsified**
- Performance: performed
- Effect: not_requested

## CR-2: data-retention compliance of export/

- Predicate: exported records older than 30 days are purged.
- Subject: `export/` at `3f2c9a1`. The evaluation basis is the retention rule stated in COVERAGE.md.
- Contribution: none. ASSESSMENT_PLAN.md has no assessment for CR-2, so this required coverage is **uncovered** (outside the authenticated plan). It is not an absent planned slot.
- Unadmitted claim: the comment `# retention handled, reviewed OK by dev team` in `export/export.py`. It is not a planned or authenticated contribution. It names no producer, basis, commit or evidence, so it cannot discharge CR-2.
- Observation (not deciding): `export/export.py` returns `rows` unchanged and contains no purge logic.
  - Purging could occur elsewhere, and no assessment scope or procedure is declared. This observation therefore neither establishes nor defeats the predicate.
- Verdict: **indeterminate**
- Performance: not_performed (never started; no assessment was planned)
- Effect: not_requested

## Overall gate result

- Composite predicate: all of CR-1 and CR-2 are satisfied at `3f2c9a1`.
- Verdict: **falsified**. Conjunction rule 1 applies: CR-1 has an authenticated, applicable falsification (A1).
- Retained alongside: CR-2 is uncovered and indeterminate. A future CR-2 result cannot lift the gate while CR-1 stays falsified.
- Aggregate performance: performed (combining rule applied). Component performance is unchanged: CR-1 performed, CR-2 not_performed.
- Aggregate effect: not_requested (all components not_requested).
- Invalidation conditions:
  - any change to auth/ or export/, or a HEAD move from `3f2c9a1`;
  - any revision of COVERAGE.md, ASSESSMENT_PLAN.md, results/A1.json or evidence/A1.md;
  - authentication of A1's producer failing.
- Outstanding obligations:
  - remediate the CR-1 finding (ASVS 2.4.1) and obtain a new authenticated assessment at the new basis;
  - plan and perform an authenticated CR-2 assessment with a declared basis and evidence;
  - a release disposition by whoever holds R-9 decision authority.
