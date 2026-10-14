# Fidelity Cases For The Iteration 3 Interpretation

Written by a same-family working reviewer before any judgment of the encoding. Same-family evidence is working evidence; it is not independent assessment.

## Basis and order

- Subject of the interpretation: the members at S2, commit `416bdb5` of the Claude build line, read only with `git show`. Line numbers below are lines of those member files at `416bdb5`.
- Order. These cases were written from the member prose and from `a_c/i3/README.md` only. Before they were saved I did not read `axiomatic-program.json`, `tools/spec.py`, `dispositions/`, `coverage.json`, `checker-commands.log`, `SIGNATURE.md` or `bindings.json`. I did, earlier in this activation and before the cases, (a) list the file names in `a_c/i3/` with `ls` and (b) list file sizes with `git ls-tree -l`, and (c) compute SHA-256 of the 22 files named in the README table (digest comparison only, no content shown). I read the README at S2 in full (7,221 bytes). No other `a_c/i3` content reached my context before this file was saved.
- README claims used to select the cases (a_c/i3/README.md "Coverage"): result algebra and conjunction, authority kinds, reuse and invalidation, promotion block, step-result refinements, AC-007 maps, boundaries (IDENTITY section 2), constraint surfaces (AXIOMATIC_CALCULUS section 9).
- Terms. A "clause" is one encoded statement in the program. A "maps-to clause" ties a refined value to one core value. A "policy-choice" clause records a choice that an owner makes and the premises leave open. "Modal force" means must, may, never, only when, necessary, and similar words.

Each case gives: the owner determination; the governing source sentence; what a faithful encoding must preserve; what would be a defect.

## FC-1 Result algebra and conjunction (FOUNDATIONS section 4)

- Governing sentences. FOUNDATIONS.md:953-955: "A conjunction with any item in the second or third input is never `satisfied`." FOUNDATIONS.md:1016-1024: "Where every mandatory returned result is `satisfied` and the declared basis relations disagree, the conjunction reports `invalid_basis` ... Where every mandatory returned result is `satisfied`, the declared basis relations agree and a gap remains, the conjunction reports `indeterminate`".
- Preserve. Scope: "any item" in the planned-assessment-without-result input or the uncovered-coverage input. Force: "never satisfied". Trigger: the second sentence applies only when every mandatory returned result is satisfied. Mapped values: basis disagreement gives `invalid_basis`; a remaining gap gives `indeterminate`; the kinds of gap (not performed, uncovered) stay distinct. The condition "every mandatory ... satisfied" must stay a condition and not be dropped.
- Defect. Gap maps to `indeterminate` unconditionally, including when a mandatory result is falsified. A conjunction with a gap can be `satisfied`. Not performed and uncovered are merged. `invalid_basis` is returned for a stale component held only on another basis (the source says that case is a gap, FOUNDATIONS.md:972-977).

## FC-2 Authority kinds (FOUNDATIONS section 2)

- Governing sentences. FOUNDATIONS.md:131-135: "Authority of any kind exists only by an admitted grant or an explicit authority decision of its owner, with an identifiable basis. None of the following mints, widens, transfers or reconstructs semantic, evaluation, operation or decision authority". FOUNDATIONS.md:146-147: "a passing check, a successful step, a completed review or a count of any of them". FOUNDATIONS.md:125-126: actor identity "is an identity and not an authority".
- Preserve. The four authority kinds (semantic, evaluation, operation, decision) plus frame-set authority; actor identity is not an authority kind; the negative list has all nine items; the four verbs (mints, widens, transfers, reconstructs); the exception that composition, delegation, adapters, wrappers and registries "may restrict admitted authority or carry it faithfully, and never widen its scope, add a role, increase its cardinality or change its kind" (FOUNDATIONS.md:152-154). "may coincide in a lawful case and never collapse by default" (FOUNDATIONS.md:126-127).
- Defect. A list item dropped (for example "a count of any of them"). "Creates no authority" turned into "is prohibited" or "is not permitted". Actor identity encoded as an authority kind. The exception turned into a permission to widen. "Never collapse by default" turned into "never coincide".

## FC-3 Reuse and invalidation (ACTIVATION section 7)

- Governing sentences. ACTIVATION.md:1464-1469: "A closed result is reused by an unchanged consumer that checks exact applicability; a role, conversation or resumption change alone invalidates nothing. An invalidator invalidates the affected result before reliance, even where the subject's own bytes are unchanged ... The invalidators are three". ACTIVATION.md:1473-1476: newly acquired evidence is a material input change "when it could change the result's value". ACTIVATION.md:1479-1480: a revising observation is one "that the result or judgment itself names". ACTIVATION.md:1486-1488: "A reused judgment does not satisfy a separately required independent judgment".
- Preserve. Reuse trigger is a check of exact applicability by an unchanged consumer. Exactly three invalidators (material input change, changed basis, declared revising observation) and no fourth; domain triggers are instances of one of the three. Materiality condition on evidence. The revising observation must be named by the result itself. Invalidation takes effect before reliance, even with unchanged bytes. The independent-judgment exception.
- Defect. Reuse licensed by an unchanged hash alone. A fourth invalidator, or any new evidence invalidating regardless of materiality. Any observation counting as a revising observation. A role or conversation change invalidating a result. Reused judgment satisfying a required independent judgment.

## FC-4 Promotion block (EVALUATION section 5, When a finding blocks promotion)

- Governing sentences. EVALUATION.md:295-296: "A finding can block current promotion only when it:" followed by four conditions (EVALUATION.md:297-303). EVALUATION.md:305: "These conditions are necessary. Which of them suffice is decided as follows". EVALUATION.md:310: a valid falsification of a mandatory claim governed by a non-waivable hard stop "blocks, whatever the assigned priority or the decision cutoff". EVALUATION.md:311: for other findings the decision owner decides blocking. EVALUATION.md:312: a finding meeting none of the four "does not block".
- Preserve. "only when" gives necessity, not sufficiency. The word "can" (not "must"). Blocking is the decision owner's act except for the non-waivable hard-stop case, which is mechanical. Cutoff and severity scales belong to the adopting Product and this member sets none (EVALUATION.md:316-317). An observation outside the exact reviewed claim does not block.
- Defect. Any one of the four conditions encoded as sufficient to block. Severity or priority deciding the block. The hard-stop exception lost (or applied to every hard stop, not only a non-waivable one). A cutoff value invented. "can block" encoded as "blocks".

## FC-5 Step-result maps of ACTIVATION section 3

- Governing sentences. ACTIVATION.md:832-833: "`incomplete` maps to `falsified` only for 'a candidate is available', never to `indeterminate`." ACTIVATION.md:842-844: "An assessing step that ends `incomplete` leaves each criterion it did not evaluate not performed: no result, never `falsified`." ACTIVATION.md:938: "`completion_unknown` never maps to `completed` or to `not_effected`" (map to `indeterminate` at ACTIVATION.md:933). ACTIVATION.md:850-853: a stop with both causes "records both and takes `re_entry_requested(basis)`".
- Preserve. Each refinement value maps to exactly one core value, for a named predicate ("a candidate is available", "the intended effect occurred", "the candidate is accepted at its declared boundary", "the declared ambiguity is resolved"). `incomplete` is `falsified` for availability only; unevaluated criteria have no result. `re_entry_requested` is split by cause with the basis cause taking precedence. `carried` and `blocked` are `falsified`, not `indeterminate` (ACTIVATION.md:910-912). Only `resolved`, `completed`, `candidate_ready` and `accept` map to `satisfied`.
- Defect. `incomplete` mapped to `indeterminate` or to two values. A value mapped without its predicate. Unperformed criteria given `falsified`. Both-cause stops left to the actor's preference. Any value other than the four above mapping to `satisfied`.

## FC-6 AC-007 outcome maps (AXIOMATIC_CALCULUS section 4)

- Governing sentences. AXIOMATIC_CALCULUS.md:560: `hold` maps to `indeterminate`. AXIOMATIC_CALCULUS.md:561: `gap` maps to `invalid_basis`. AXIOMATIC_CALCULUS.md:568-571: "A refusal that names a demonstrated violation of a declared law or constraint ... is `refusal(constraint)`, whatever condition of the basis it also names." AXIOMATIC_CALCULUS.md:597-600: a `gap` "is a closed result with the value invalid_basis; it is not the absence of a result". AXIOMATIC_CALCULUS.md:597: "An operation that was not applied has no outcome."
- Preserve. Predicate: "the operation yields its declared result on the exact basis". Cause precedence: a demonstrated violation makes `refusal(constraint)` (`falsified`) even when a basis condition is also named; the basis condition is reported beside it as its own `invalid_basis` result for a different predicate. `refusal(basis)` only when no violation is demonstrated. `hold` is `indeterminate`. A `gap` is a result, an unapplied operation is not.
- Defect. A refusal mapped to both values or chosen by wording. Basis precedence over violation (the reverse of the source). `hold` mapped to `falsified`. A `gap` treated as no result. The beside-record `invalid_basis` result dropped.

## FC-7 Boundaries in IDENTITY section 2

- Governing sentences. IDENTITY.md:130-133: an object's boundary "is a claim with a proof obligation ... not a property that its storage, schema or name establishes". IDENTITY.md:135-136: a boundary claim "holds only as far as that evidence goes". IDENTITY.md:136-140: a sufficiency claim "is not completeness, and it does not establish that the boundary screens the object's interior from everything outside it". IDENTITY.md:141-143: "a statistical Markov boundary, is a hypothesis ... no work relies on it as established".
- Preserve. A boundary claim names its object, its evidence and its basis (three parts). Scope of evidence limits the claim. Sufficiency is task-bounded (RF-003). The Markov boundary is a hypothesis; the force of "no work relies on it as established". A profile that uses the construct "states its epistemic status".
- Defect. Storage, schema or name accepted as boundary evidence. Sufficiency promoted to completeness or to the Markov property. The Markov boundary encoded as law, or "no work relies" softened to "should not". The profile duty dropped.

## FC-8 Constraint surfaces (AXIOMATIC_CALCULUS section 9)

- Governing sentences. AXIOMATIC_CALCULUS.md:1307-1312: "A residual, a `hold`, a `gap` or an external predicate not yet established keeps its source and its required acquisition, and it blocks every operation and result that depends on it until its premise is established. A missing premise or an omitted obligation never becomes permission or a satisfied result". AXIOMATIC_CALCULUS.md:1305-1306: "A policy choice keeps its owner, and a preference is never read as an obligation." AXIOMATIC_CALCULUS.md:1293 and 1296: "the closure imposes no tree shape and no execution order"; "what no obligation fixes and a latitude admits is the worker's choice".
- Preserve. The block applies to dependent operations and results only, and lasts until the premise is established. Unresolved never yields permission or satisfaction. Policy choice keeps its owner. Preference stays a preference. Latitude admits several solutions; no single solution, order or tree is imposed. The surface grants no authority (AXIOMATIC_CALCULUS.md:1297).
- Defect. An unresolved item blocking independent work, or treated as false (prohibited). An unresolved premise read as unrestricted freedom (permission). A preference or "not required" encoded as an obligation or as a prohibition. A tree or order imposed on the premises. The owner of a policy choice missing.

## What the judgment (review.md) must also check

- No clause turns "not required" into "prohibited", or a preference into an obligation (ORACLE C6, J18).
- No maps-to clause maps to more than one core value (ORACLE D7).
- No policy-choice clause is empty of its choice text or owner (hollow).
- Each heading section in `dispositions/` carries exactly one value, and the totals match the README (15 encoded, 8 no determination, 181 not-encoded-i3).
