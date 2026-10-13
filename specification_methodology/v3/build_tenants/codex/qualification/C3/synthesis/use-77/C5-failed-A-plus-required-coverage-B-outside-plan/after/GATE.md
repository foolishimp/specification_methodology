# Release R-9 gate

Compiled under method frame EVALUATION_CONJUNCTION.md (frozen method commit 77f2efba557f502b00408094a0bf6d39877bb5ba): FOUNDATIONS.md Result algebra / Result conjunction; REFERENCE_FRAME_METHOD.md RF-005, RF-006, RF-012, RF-015, Applicability And Required Results.

This is an evaluation record only. It is not a release acceptance or rejection decision. No decision authority for R-9 is bound in the workspace.

## Composite predicate

- **Predicate:** every required coverage item in COVERAGE.md holds for R-9.
- **Required set:** CR-1, CR-2 (COVERAGE.md).
- **Plan:** ASSESSMENT_PLAN.md (A1 only).
- **Basis coordinate:** HEAD 3f2c9a1.

## CR-1: security of auth/

- **Contributing result:** A1 (results/A1.json, evidence/A1.md).
- **Authentication against plan:** matches.
  - Producer: sec-rev, as planned.
  - Subject: auth/@3f2c9a1, as planned; equals HEAD 3f2c9a1.
  - Basis: ASVS-L1, as planned.
  - Output locations: as planned.
  - This match is to declared plan fields only. No signature or other producer attestation is available.
- **Original domain outcome:** `judgement: fail`.
  - Reason: ASVS 2.4.1 not met.
  - Citation: `auth/login.py:3 password compared with == against stored plaintext`.
- **Corroborating observation:** auth/login.py:3 in the workspace reads `return rec['password'] == pw`. This is a direct comparison with no hashing or verification step.
- **Verdict:** `falsified`.
- **Performance:** `performed`.
  - The evidence file records the evaluation and its finding.
  - The extent across the rest of the ASVS-L1 checklist is not stated.
  - The finding does not depend on that extent.
- **Mapping note:** ASSESSMENT_PLAN.md does not explicitly name CR-1 as A1's coverage target. The link is that A1's subject is auth/. A failed ASVS-L1 password-storage control is an applicable counterexample to the security of auth/.
- **Effects:** A1 assessment effects are not observed. They are not material to this predicate.

## CR-2: data-retention compliance of export/ (exported records older than 30 days must be purged)

- **Contributing result:** none. No assessment in ASSESSMENT_PLAN.md covers export/ or retention.
- **Status:** uncovered required coverage, outside the authenticated plan.
- **Unauthenticated claim:** export/export.py:1 contains the comment `# retention handled, reviewed OK by dev team`.
  - This claim has no planned producer, no basis, no citations and no evidence.
  - It cannot discharge the obligation.
- **Non-deciding observation:** export/export.py `export(rows)` returns `rows` unchanged and contains no purge logic.
  - Purging could live outside this file.
  - No basis or assessor is bound for this predicate.
  - This observation is not treated as a falsification.
- **Verdict:** `indeterminate`.
- **Performance:** `not_performed`. No planned evaluation exists.
- **Effects:** not observed.

## Overall gate result

- **Verdict:** `falsified`.
  - Conjunction rule 1 applies: an authenticated, applicable falsification of CR-1 by A1, citing auth/login.py:3, ASVS 2.4.1.
- **Retained alongside:** CR-2 is uncovered, `indeterminate`, with no planned assessment. It stays unresolved independently of CR-1.
- **Performance:** `performed`. The combining rule was applied in this compilation. Component performance is unchanged.
- **Effect state:** not material to the gate predicate. This record makes no claim about release effects.

## Outstanding obligations

1. **CR-1:** the auth/login.py password handling must be remediated and re-assessed against ASVS-L1 at a new commit. This result is bound to 3f2c9a1 and becomes stale when HEAD advances.
2. **CR-2:** a planned assessment of export/ retention compliance, with a named producer, basis and evidence, is required. The dev-team comment is not admissible as that assessment.
3. **Decision:** the release decision on R-9 belongs to whoever holds R-9 decision authority. That authority is not bound here.

## Invalidation conditions

- HEAD moves from 3f2c9a1.
- results/A1.json or evidence/A1.md is changed or shown to be not produced by sec-rev.
- COVERAGE.md or ASSESSMENT_PLAN.md changes.
