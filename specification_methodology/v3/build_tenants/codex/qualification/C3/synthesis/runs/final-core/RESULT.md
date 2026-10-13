# Re-review of the shared core at 875a56e3

**Scope.** I checked only the supplied COMMON, FOUNDATIONS and LIBRARY text. No consumer member was available, so this is a source-port judgement. It is not a complete-corpus judgement (see the last section).

## Remaining defect: the associativity claim is too broad

**Locus.** FOUNDATIONS, *Result conjunction*, the regrouping paragraph: "On that fixed domain … the above verdict/effect operations are associative."

The phrase "the above verdict operations" includes the declared-operator rule, which appears just before it. The next paragraph sends every sequential-composition result through "the operator rule above to the declared outer predicate", and says recovery paths need not be conjunctive. So the claim covers declared operators in general. Its listed conditions are basis, leaf predicates, joins, normalized effect parts, authentication, and no hidden intermediate basis failure. None of these fixes the composite predicate or requires the operator to be associative.

**Minimal counterexample.**
- Declared binary implication: truth `¬x ∨ y`, falsity `x ∧ ¬y`. This is disjoint and exhaustive, with no joins, so it is well-formed.
- Leaves `a`, `b`, `c` are each `performed`/`falsified` and authenticated.
- Basis is the same in both groupings, and all effects are `not_requested`.

| Grouping | Inner result | Outer result |
|---|---|---|
| `(a⇒b)⇒c` | `a⇒b` is satisfied | satisfied ⇒ falsified gives **falsified** |
| `a⇒(b⇒c)` | `b⇒c` is satisfied | falsified ⇒ satisfied gives **satisfied** |

Every stated regrouping condition holds, yet the verdicts differ. A satisfied result appears under one lawful-looking grouping.

**Minimal repair.** Limit the sentence to the conjunction precedence and the effect join. Alternatively, add "the same composite predicate, and a declared operator whose truth/falsity conditions are associative" to the conditions.

## Associativity under the conjunction-only reading: holds

- **Verdict.** On the union of components with a fixed required set, conjunction takes the maximum over the chain falsified > invalid_basis > out_of_frame > indeterminate > satisfied. Absent slots count as indeterminate. The falsification short-circuit is consistent with the chain. Taking a maximum over the union is associative.
- **Effect join.** It is the join of a finite join-semilattice:
  - not_requested is the bottom; not_started and completed sit above it;
  - reverted is above not_started; partial is above completed and reverted; unknown is the top;
  - completed ∨ not_started = partial, completed ∨ reverted = partial, not_started ∨ reverted = reverted.
  
  I checked every case in the text against this order. It is associative, commutative and idempotent.
- **Per-part resolution.** It is order-sensitive. It is recomputed from the retained contributing observations, with their ordering and supersession evidence, not from intermediate summaries ("retained component sets combine by union"). Resolution by the last supported observation on a fixed sequence is associative but not commutative. The text correctly refuses reordering without an effect-independence law.
- **Intermediate basis condition.** The "no intermediate basis failure" clause blocks the one non-associative path: an uninterpretable intermediate composite forcing invalid_basis over a falsification.
- **Disjunction.** It would also be associative under the operator rule, as a maximum over satisfied > invalid_basis > out_of_frame > indeterminate > falsified. So the narrow repair would not exclude a lawful case unnecessarily.

## Bounded checks that hold

| Exercise | Result |
|---|---|
| Aborted suite with authenticated failure | `(not_performed, falsified)` is a legal pair. The counterexample is to the bound predicate, independent of conclusion. Conjunction rule 1 gives falsified, and the unrun coverage stays explicit. Satisfied is unreachable without the conclusion. |
| No concluded procedure plus independently observed invalid basis | `(not_performed or unconfirmed, invalid_basis)` is legal, and the evidence is identified apart from any conclusion claim. In a conjunction, any authenticated falsification takes precedence; otherwise the result is invalid_basis. An invalid composite basis gives invalid_basis with component failures exposed, not erased. |
| Deploy, then rollback, then reapply on the same part | Local labels are not join inputs. The part resolves to reverted, then completed, with the rollback kept as evidence. A lost reapply acknowledgement or unsupported order (timestamp only) leaves the part unknown. A partial reapply gives partial. |
| Absent dispatched effect | A requested part with no sufficient observation, including one owned by an absent slot, is unknown. Dispatch proves neither completion nor absence. not_started needs evidence such as an authenticated pre-mutation rejection. The composite is unknown, and the verdict cannot be satisfied when the predicate needs a known effect state. |
| Irreversible external effect alongside local rollback | The external part must stay declared. Completed combined with reverted gives partial, which matches the single-effect definitions. Reverted is unreachable. |
| Unknown or conflicting supersession | Conflicting or insufficient observations, or ordering by timestamp alone, leave the part unknown. Contributing observations are retained. |
| Disjunction or negation with known failed joins | The operator's declaration must cover join failure on its admitted domain, or it is invalid_basis. Negation and disjunction evaluate a different predicate, so a failed leaf is retained and is never passed off as conjunction. A first-non-failure rule cannot turn an undecided fallback into success. |
| Overlapping or incomplete operator declarations | Both give invalid_basis and supply no satisfaction. Well-formedness over the declared leaf/join valuations is a finite check. Where it depends on an unresolved admitted domain, the falsification's applicability is unresolved, so rule 3 gives indeterminate. That case also cannot be satisfied. |
| Admission relation versus evaluated join | Each relation has one role per evaluation, so the same relation cannot be both. A failed admission condition gives invalid_basis on the predicate itself, with no substitute predicate. A failed join gives falsified. A relation can be an admission condition for a leaf and a join for the outer composite: the leaf is invalid_basis, the composite is falsified, and both are retained. Unresolved admission gives indeterminate through unresolved applicability. |
| Refinement standing (COMMON item 3) | A missing required reason gives indeterminate and is inadmissible as deciding support; it applies only to coarse outcomes. Non-performance, unconfirmed performance and unknown effects are never raised. The refinement map is single-valued into the record. |

Single ownership of result composition holds within the supplied members. FOUNDATIONS owns it, LIBRARY *Conjoin* and *Composition law* refer to it, and operation composition stays with UP-016/017 and AC-016.

## Source-port versus complete-corpus acceptance

**Source-port.** With the associativity sentence narrowed, I found no remaining contradiction in the supplied core for the exercises above.

**Complete corpus: not established by this review.** COMMON *Single Result Algebra* items 2 and 7 require every refinement to map into the core and every result-returning frame to carry it. Those consumers were not in the supplied source:
- RF-012;
- AC-007/013;
- the UP-020 disposition mapping;
- UP-016/021 admission outcomes and their admission/join role assignment;
- Baseline WorkerResult;
- Ticket and Release classifications.

Each consumer's total, reason-sensitive map and its role declarations need their own check before complete-corpus acceptance.
