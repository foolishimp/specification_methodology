# Claude tenant: handoff for the C3 review

Written by the Claude tenant author for Jim and for whichever assessor he
authorises. It routes attention; it accepts nothing and judges nothing of
its own. Everything below is on `tenant/claude/c3`, read at the commit
named in each row; the working tree is not the subject.

## What exists

| Thread | Increment | Freeze commit | Program | Case | Runs (constructor output, unassessed) | Runs commit |
|---|---|---|---|---|---|---|
| T1.2 | FOUNDATIONS, CALCULUS §1–3, EVALUATION §1–4 | `cee1157` | [a_c/t1](../a_c/t1/README.md) | [T-01 CASE-2](cases/T-01/CASE-2.md) | A2 satisfied 23/23 after the closure was refused; B2 out_of_frame with three routes refused before any actor | `eb9b935` |
| T2 | CALCULUS §4–7, SPEC_METHOD | `97f1259` | [a_c/t2](../a_c/t2/README.md) | [T-03-04](cases/T-03-04/CASE.md) | A and B both falsified with R05 carried, uncovered routes listed, R_C refused | `f33e6ae` |
| T3 | EVALUATION §5–8, CONFORMANCE, PROFILES | `c539daa` | [a_c/t3](../a_c/t3/README.md) | [T-05](cases/T-05/CASE.md) | see the case's runs table | see RETURNS |
| T4 | README route; the set program | `6bc1692` | [a_c/set](../a_c/set/README.md) | [R-01](cases/R-01/CASE.md) | five variants twice; no record reports the claim satisfied; one earlier run abandoned and kept as evidence of the CLAUDE.md finding | the commit after `6bc1692`, named in RETURNS |

T1's first fixture and its two runs (`eca8cef`) were reviewed; the review
and its dispositions are under [received/](received/). Every later thread
followed the same shape: the author's pre-freeze route check by fresh
step actors, freeze by digest, encoding validated against the pinned
Axiom Indexer subject, a fixture with independently owned expectations,
runs by fresh constructors that the author did not repair or annotate,
and a return in [RETURNS.md](RETURNS.md).

## What a reviewer is asked to do

Under EVALUATION §3 and §4 of the tenant's own corpus, which is the method
under test: freeze the subject at the named commit; record expectations
from the common sources each case names before opening any run record;
return one core result per expected distinction with evidence, ranked
findings with their smallest corrections, residual uncertainty and
invalidation conditions; recommend a disposition. Make no repair. The
common sources are the conformance discriminators, the capability
questions and the matrix post at input commit `80b46944f1c1`.

Four kinds of judgment are open, in this order of consequence:

1. Assessment of the runs against each case's expected distinctions
   (T-01 CASE-2 E1–E5; T-03-04 E1–E6; T-05 E1–E6; R-01 E1–E5). The
   author's structural checks of the lifecycle logs are mechanical
   evidence and may be reused; the author's reading of the records may
   not.
2. Fidelity of the a_c programs to the documents (source-first,
   author-independent), for the set program first; the T1 program's
   failure on four points and its repair show what this judgment finds.
3. Standing of every clause against rc.2 (one standing per clause;
   conserved, reframed, superseded or new), where the pre-freeze route
   checks are the author's evidence and not a substitute.
4. Whether the documents answer the common capability questions, which is
   the C2 contract Jim has not yet fixed.

## What remains Jim's

- Selection and acceptance of the Axiom Indexer dependency's use
  (A_C_DEPENDENCY.md); every mechanical result here is candidate evidence
  bound to the byte-verified tagged subject, not to a selected Install.
- The C2 contract (capabilities, acceptance criteria, audiences), which the
  common GOALS still show as open; this tenant built ahead of it under
  his authorisation and nothing here fixes it.
- Authorising the assessor and any cross-tenant review; merging the
  branch on acceptance; rulings the runs requested of the case owner
  (listed in each case's runs table).

## Known open observations, carried not repaired

- Every step actor of T-01 CASE-2, T-03-04 and T-05 received the
  workspace's three CLAUDE.md files (about 12 KB, one carrying an STDO 2.x
  method compression) in its context beside the measured bytes, because
  the headless CLI loads them from the actor process's working directory,
  which was inside the repository. Found at T4 by the calibration step
  (6,907 tokens inside the repository against 2,247 outside). The
  judgments stand; the "whole context measured" claim of those fixtures
  is false by that amount; each case carries the finding at its end. The
  generic instrument is repaired for R-01; the T-01 instrument is left as
  used.
- The two T-03-04 constructors triaged the same seeded defect into
  different change classes with reasons; SPEC_METHOD §4 may need to say
  how a defect in a fixture copy of a standard is classed.
- The rc.2 manifest digest named in the case contracts is unverifiable
  under a constructor grant that forbids opening the install.
- A step actor on the real FOUNDATIONS §3 judged AC-016 out_of_frame and
  RF-010 indeterminate for P4a (T-05 fixture, step P4a), while the T-01
  A2 run judged both satisfied with the paragraph alone; the difference
  is the context given (whole section against one paragraph). This is a
  candidate finding against P4a's attribution of RF-010 and an
  observation about context sensitivity of the route judgment.
- P4b's claim that five clauses' nine statements "become one obligation"
  is a paragraph-level claim no route step judges (from T-01 A2).
- The per-boundary cost of the software-design derivation chain is a
  residual question for the profile's owner (PROFILES §3).
