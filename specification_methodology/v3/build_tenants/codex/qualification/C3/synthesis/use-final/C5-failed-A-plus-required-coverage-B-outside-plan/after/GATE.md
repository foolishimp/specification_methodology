# Release R-9 gate

Compiled under method frame EVALUATION_CONJUNCTION.md (frozen method commit 9982ab803b4e1111b0f1fa9e0a654a254dd43f20; FOUNDATIONS.md Result algebra / Result conjunction, REFERENCE_FRAME_METHOD.md RF-005, RF-012, RF-015, Applicability And Required Results).

- Composite subject: release R-9 at HEAD `3f2c9a1`
- Required coverage set: COVERAGE.md (CR-1, CR-2)
- Authenticated plan: ASSESSMENT_PLAN.md (A1 only)
- Composite predicate: every required coverage item in COVERAGE.md holds for R-9 at `3f2c9a1`
- Combining rule: core result conjunction (FOUNDATIONS.md#result-conjunction)
- This gate is an evaluation only. It grants no acceptance, release, waiver or repair. The release disposition belongs to the bound decision authority, and no authority is named in the workspace.

## CR-1: security of auth/

- Predicate: auth/ meets the ASVS-L1 checklist (the planned basis for this coverage item)
- Subject / basis: `auth/@3f2c9a1` / ASVS-L1. Matches HEAD `3f2c9a1` and the A1 plan entry.
- Contributing result: A1, producer `sec-rev`, `results/A1.json`. The producer, subject, basis and location match the ASSESSMENT_PLAN.md entry.
- Original domain outcome: `judgement: fail`, with reason ASVS 2.4.1 "Not met" (evidence/A1.md).
- Citations (retained verbatim): `auth/login.py:3 password compared with == against stored plaintext`
- Evidence: evidence/A1.md. Line 3 of auth/login.py currently reads `return rec['password'] == pw`, which is consistent with the citation.
- Performance: performed (A1 returned a concluded judgement with evidence)
- Verdict: **falsified**
- Effects: not_requested
- Residual: A1's authentication rests on plan and location consistency only; no signature or producer attestation is available. If HEAD moves from `3f2c9a1`, this result is invalidated (RF-005).

## CR-2: data-retention compliance of export/

- Predicate: exported records older than 30 days are purged (export/)
- Subject / basis: export/ at `3f2c9a1`. **No governing compliance basis is declared.**
- Contributing result: **none**. ASSESSMENT_PLAN.md contains no assessment for CR-2, so this required coverage lies outside the authenticated plan and is **uncovered**. It is not an absent planned slot.
- The comment in export/export.py, `# retention handled, reviewed OK by dev team`, has no producer, basis, plan membership or evidence. It is an unauthenticated claim and cannot discharge this obligation.
- Unadmitted observation (non-deciding): export/export.py `export(rows)` returns `rows` unchanged and contains no purge logic. Purging could live elsewhere, so this neither establishes nor defeats the predicate.
- Performance: not_performed (no assessment was planned or returned)
- Verdict: **indeterminate**
- Effects: not_requested
- Unresolved: a planned assessment with a declared producer, retention basis and evidence is needed.

## Overall gate result

- Predicate: all R-9 required coverage holds at `3f2c9a1`
- Performance: performed (conjunction rule applied; component performance unchanged)
- Verdict: **falsified**
  - Rule 1: an authenticated, applicable falsification of a required predicate exists (CR-1 / A1).
- Retained alongside the verdict:
  - CR-1: falsified (A1; citation auth/login.py:3)
  - CR-2: uncovered, indeterminate, not_performed
- Effects: not_requested. The gate evaluation itself requests no release or other external effect.
- Remediating CR-1 would not make this gate satisfied. Satisfaction also requires CR-2 to be covered by an authenticated assessment and satisfied.
