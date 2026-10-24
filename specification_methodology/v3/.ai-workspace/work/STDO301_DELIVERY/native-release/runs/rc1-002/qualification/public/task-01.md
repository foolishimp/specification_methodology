# Installed-route task 01: deterministic operation contracts. Assessment

**Standing.** This is a read-only test-use assessment by a fresh actor. It is not an acceptance or disposition: I can recommend, but the decision owner disposes (`standards/ACTIVATION.md:1051-1054`). I did not verify the commit, tag, manifest, inventory or installed-byte digests, and I ran no structural checks. I took the root's binding of the exact cut as given. All paths below are relative to the installed `RELEASE_ROOT`.

## Case 1: finite-table constructor returns `{n:2,double:4}`

**Kind eligibility.** On the stated facts the constructor can qualify for common `F_D`, but this run does not establish that.
- `F_D` covers deterministic construction (`standards/AXIOMATIC_CALCULUS.md:180`, choice column).
- **Predicate needed** (`standards/AXIOMATIC_CALCULUS.md:985-999`): a declared `f_B:D_B->Outcome_B` with:
  - closed domain `{0,1,2}`;
  - exact basis `B`;
  - all material state and dependencies, here only the table;
  - a termination argument;
  - exactly one declared outcome for every input.
- The traversal also needs a bound identity `[v]` (`standards/AXIOMATIC_CALCULUS.md:1065-1069`) and a `stop_states` mapping (`standards/AXIOMATIC_CALCULUS.md:969-971`).
- A finite lookup over three inputs supports a termination argument, but the argument must be *declared*. A missing required declaration is a contract violation (`standards/AXIOMATIC_CALCULUS.md:1075-1080`).
- **Evidence needed:** a performed eligibility assessment of that record. An exhaustive check of the three table rows would serve. Until an assessment is performed it has no result (`standards/AXIOMATIC_CALCULUS.md:1081-1084`). No invocation counts as qualifying `F_D` on an unestablished claim (`standards/AXIOMATIC_CALCULUS.md:1086`).
- **Gap:** the case gives no basis identity and no stop set. Whether an empty `Omega_v` meets the `stop_states` binding is my reading; no clause I read states it.

**What the result establishes.**
- **Availability only.** `{n:2,double:4}` is a candidate (`standards/ACTIVATION.md:1004-1006`). It gives `candidate_ready`, which is satisfied only for "a candidate is available" and never counts toward fitness or acceptance (`standards/ACTIVATION.md:1011`, `standards/ACTIVATION.md:1023-1024`).
  - Assumption: the construction step was lawfully admitted and activated. Otherwise there is no step and no result (`standards/ACTIVATION.md:991-995`, `standards/ACTIVATION.md:1017-1021`).
  - The output matches `2*n` for `n=2`. That is one data point, not a judgment of the output or of totality.
- **Assessment:** none. An assessment that was not performed has no result (`standards/AXIOMATIC_CALCULUS.md:1005-1006`, `standards/ACTIVATION.md:1027-1034`).
- **Admission and permission:** none. An `F_D` classification grants no semantic, evaluation, operation or decision authority (`standards/AXIOMATIC_CALCULUS.md:1025-1030`). A deterministic decision establishes no runtime admission, permission or quality (`standards/AXIOMATIC_CALCULUS.md:1008-1010`).
- **Ledger writing:** none. The actor holds only a construction grant.
  - If the work runs under the ODD profile (the case doesn't say), Product admission and ABG own admission into L/E (`standards/ODD.md:1084-1086`).
  - Direct ledger mutation is forbidden (`standards/ODD.md:737`), and the kind is no authority to admit (`standards/ODD.md:1094-1097`, `standards/ODD.md:1486-1488`).
- **Closure:** none. Closure is ABG's admitted `evaluate_action` fold (`standards/ODD.md:1087-1088`). No edge closes on raw process success (`standards/ODD.md:1103-1105`).

**Preserved restrictions.** The construction grant is not widened. Feeding the constructor into an evaluator keeps two traversal identities and both results (`standards/AXIOMATIC_CALCULUS.md:1111-1112`).

**Next lawful work.**
1. Record `v` with its domain, codomain, basis, dependencies, termination argument and `stop_states`.
2. Perform the eligibility assessment.
3. Have a separate evaluator, with its own contract, judge the candidate.
4. Route admission and closure to their owners, then disposition to the decision owner (`standards/ACTIVATION.md:1051-1058`).

## Case 2: evaluator sorts `[2,1]` and reports "the original was sorted"

**Decision.** The declared evaluation contract is violated. A judgment of that violation is `falsified`, and structural admission of the application returns `refusal(constraint)`. This follows `standards/AXIOMATIC_CALCULUS.md:1075-1080` together with `standards/AXIOMATIC_CALCULUS.md:1039`. I am treating the §5 evaluation-profile breach as one of the "contract violations" AC-015 refers to; that list's examples do not name it explicitly.

**Predicate.** The evaluation profile (`standards/AXIOMATIC_CALCULUS.md:1032-1039`) requires the evaluator to:
- name its subject, reads, witness output, writes, stops and authority;
- preserve the judged subject and not perform the construction it judges;
- obtain its own contract and grant for any construction or mutation.

"Reporting a changed subject's property as the original subject's property violates this evaluation contract." A judgment points to an unchanged subject (its `subject` and `subject_digest`), and issuing a judgment does not transform its subject (`standards/AXIOMATIC_CALCULUS.md:893-916`).

**Counterexample.** The evaluator sorted the list to `[1,2]` and attributed the sortedness of `[1,2]` to `[2,1]`.

**Subject judged vs subject constructed.**
- **Declared judged subject:** `[2,1]`, with its digest.
- **Constructed subject:** `[1,2]`, produced by a construction that has no contract or grant. It is a candidate in its own right, not the judged subject.
- **Unknown:** whether the sort was in place.
  - If in place, it also breaches the "may not change" write restriction, and the judged subject's digest no longer matches.
  - If on a copy, it is an unauthorised construction.
- **Result about the original:** the evaluator produced no lawful result about whether `[2,1]` is sorted. Separately, the claim is defeated on the stated data under ascending order (2 > 1). That is my own observation, and the case does not declare the order.

**Preserved restrictions.**
- Writing the witness log stays within the grant, and persisting a witness is not the judged construction (`standards/AXIOMATIC_CALCULUS.md:1036-1037`).
- Deterministic termination does not cure the violation. Kind classification gives no quality conclusion (`standards/EVALUATION.md:132`), and total handling does not qualify `F_D` (`standards/ACTIVATION.md:1175-1177`).
- Whether the evaluator is `F_D`-eligible is a separate question, and the case does not settle it.

**Next lawful work.**
1. Report the falsified contract judgment to the decision owner.
2. The owner repairs the evaluator into a non-mutating check, which is a new candidate (`standards/ACTIVATION.md:1067-1069`).
3. If a sorted list is wanted, declare a separate constructor with its own grant, composed under AC-016 (`standards/AXIOMATIC_CALCULUS.md:1104-1112`).
4. Re-evaluate the exact original `[2,1]`.

**Gap:** I found no installed restoration procedure for the case where the original was mutated in place.

## Case 3: legacy operation imported by adding only the unchanged-subject profile

**Decision.** Adding only the profile is not sufficient.
- The profile must be preserved, but "that profile alone does not establish the new kind's totality, closed dependencies or declared outcomes" (`standards/RELEASE.md:717-722`).
- The old deterministic definition supplies no general termination argument (`standards/RELEASE.md:723`).
- An old evaluator with unestablished termination or an undeclared material dependency takes row 2 or row 3 of the migration table, "even if it preserves the judged subject" (`standards/RELEASE.md:732-737`).
- Undeclared filesystem dependencies are outside `F_D` (`standards/AXIOMATIC_CALCULUS.md:990-992`). A demonstrated undeclared material dependency, or a missing termination argument, is a contract violation (`standards/AXIOMATIC_CALCULUS.md:1075-1080`).
- This does not say the operation diverges (`standards/AXIOMATIC_CALCULUS.md:1080-1081`), and it does not make it `F_P` (`standards/AXIOMATIC_CALCULUS.md:1044`, `standards/AXIOMATIC_CALCULUS.md:1092-1093`).

**Lawful migration standing.**
- **Row 3, as the case reads now** (`standards/RELEASE.md:730`). No remediation or successor classification has been selected. The operation keeps its exact legacy meaning and evidence, plus an explicit unresolved successor-classification obligation. It keeps only its standing on its exact old basis, gets neither `F_D` nor `F_P`, and the successor claim stays open.
- **Row 2, once the owner acts** (`standards/RELEASE.md:729`). This applies once the owner identifies the missing evidence and a remediation obligation, or declares a bounded successor. The migration is then pending, still with no successor `F_D` standing.
- Which row applies depends on the owner's record, which the case does not supply. Evidence alone need not choose the remediation (`standards/RELEASE.md:736`).
- The old ODD `f-d` URN stays historical and is not an alias. Only the explicit migration mapping licenses successor use (`standards/ODD.md:376-380`, `standards/ODD.md:337-341`, `standards/ODD.md:1553-1554`).
- Unresolved mappings block the affected successor claim (`standards/RELEASE.md:756-757`).

**Next lawful work.**
1. The owner records the old release, manifest, member, clauses and applicable row (`standards/RELEASE.md:752-754`).
2. The owner either declares and closes the filesystem dependency and supplies a termination argument, or declares a bounded successor. A bounded successor, such as a narrower domain or a fuel-bounded version, has its own identity, contract, exhaustion outcomes and preservation evidence. It proves nothing about the original (`standards/AXIOMATIC_CALCULUS.md:1046-1050`, `standards/RELEASE.md:729`).
3. Perform the eligibility assessment. Only an established result maps to row 1 (`standards/RELEASE.md:728`). An undecidable result stays `indeterminate` and unestablished (`standards/AXIOMATIC_CALCULUS.md:1081-1083`).

## Routes actually used, and gaps

**Read:**
- `standards/README.md` (whole file)
- `standards/AXIOMATIC_CALCULUS.md`: 176-219, 536-575, 891-918, 919-1116
- `standards/ACTIVATION.md`: 970-999, 1000-1084, 1160-1189
- `standards/ODD.md`: 325-384, 1068-1117, 1474-1563
- `standards/RELEASE.md`: 715-773
- `standards/EVALUATION.md`: 118-139

**Searched:** Grep for the key terms and section headings. ODD line 737 was seen only as a Grep match.

**Outside the expected three routes:** RELEASE §9 and EVALUATION §2. I followed them because AC §5 links to them as owners (`standards/AXIOMATIC_CALCULUS.md:1053`, `standards/AXIOMATIC_CALCULUS.md:204`).

**Not read:**
- FOUNDATIONS §4 Results. I used the core values only as AC-007 and ACTIVATION restate them.
- REFERENCE_FRAME §5.
- CONFORMANCE D301.
- `standards/examples/DETERMINISTIC_CONTRACTS.md`, which by its own index entry carries no authority (`standards/README.md:66`).
- All frames.

**Open questions:**
- Whether an empty stop set satisfies `stop_states` (case 1).
- Whether the sort in case 2 was in place, and how a mutated original would be restored.
- Which migration row applies in case 3; that depends on the owner's record.
- Whether the ODD profile is selected at all; the ODD conclusions apply only if it is.
