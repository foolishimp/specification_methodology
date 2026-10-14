# Rebuilt core a_c interpretation return

The bounded qualification interpretation is ready for review against unchanged
product source `9bc8962e44aff2cd1dc29a9bac95356cdccf7cdd`. Structural and finite
checks pass. Independent review confirmed the substantive repairs within its
selected source frame; final declaration corrections were checked by the parent.
Whole-core implementation, family fidelity, member acceptance and release remain
open. This is the parent qualification Writer return under EC-CODEX-SYN-01.

## Findings and final disposition

Independent reviewers found defects despite earlier mechanical passes. Their
inputs, outputs and rejected interpretations remain. The
[repair ledger](a_c/REVIEW_DISPOSITIONS.md) records the individual findings.
The [preceding Writer return](AC_WRITER_RETURN_20261013T200910Z.md) is historical;
its pending-review statements and counts describe that earlier cut.

The [final counterexample review](runs/ac-final-counterexamples/RESULT.md)
confirmed N1's evidence boundary and the named R repairs, but demonstrated that
an incomplete effect boundary disabled its own completeness obligation. The
parent changed that guard, made premise links explicit, carried effect relevance
into the operator clause and distinguished unsupported positive combination from
inadmissibility. No product member changed.

The [targeted recheck](runs/ac-boundary-recheck/RESULT.md) confirms C1–C4, C6 and
C7, and the substance of C5/C8. Its remaining R-a–R-c findings were declaration
issues: stale test counts, incomplete description of finite conflict precedence
and residual-list drift. Those are corrected. R-d now has an explicit
composite-invalid premise. Parent inspection resolves R-e: result-binding
requires material effect observations on every reported result; omission is not
a conforming record. [FINAL_REPAIR_CHECK.json](a_c/FINAL_REPAIR_CHECK.json) records
these checks. No additional independent confirmation of those last textual
corrections is claimed.

The finite model's single-predicate conflict precedence is explicitly its own
policy, not a law derived from the source. Any mapped or admitted falsification
wins; otherwise an admitted diagnosis replaces the mapped verdict; otherwise
the mapped verdict remains. Both claims and conflict are retained. This supplies
no authority to resolve contradictory real evidence.

## Constructed subject and mechanics

[program.json](a_c/program.json) has 53 clauses, 14 symbols, five frame indexes
and three residuals. [SOURCE.md](a_c/SOURCE.md) declares the selected scope and
[SIGNATURE.md](a_c/SIGNATURE.md) its interpretation vocabulary. Eighteen library
and family clauses state consumption relationships; they do not establish full
family fidelity or implement every domain-outcome refinement.

[SOURCE_INVENTORY.json](a_c/SOURCE_INVENTORY.json) binds the product bytes to the
frozen source. [INSTALL_VERIFICATION.json](a_c/INSTALL_VERIFICATION.json) verifies
the exact RC2 Axiom Indexer identity, seven-member installation and fixed theory.
Its executable SHA-256 is
`5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8`.
The historical encoding calculus is distinct from the successor source; no
semantic equivalence between them is asserted.

[MECHANICAL_RESULT.json](a_c/MECHANICAL_RESULT.json) passes native validation,
reference/materialized projection parity, a 52-clause transitive configuration
selection, empty-selection and stale-map refusals, exact joining, source-stability
checks and all five archive manifests. It took 0.943 seconds in the recorded run.
The fixed tool checks structure and relations, not the semantic truth of clauses.

The earlier combined review consumed 99,512 bytes retained in its run's
PROMPT.txt. The final targeted review consumed 77,232 bytes, SHA-256
`4152d3a5bfafffb714bca9cb63c4270d3442346b2ec122c3ba70c8526dc12d70`.
Its [request manifest](a_c/FINAL_REPAIR_REQUEST.json) preserves the exact input.
The current mechanically regenerated REQUEST.txt is 103,413 bytes,
SHA-256 `05ae1dd1f1f0a1c9eab78f7df9810c9775a87afb623cefc4402b7b41cb2e14da`; it is a successor of the old request, not a claim that
reviewers consumed its current bytes. The standalone FINITE_REQUEST.txt remains
the historical pre-N1 input.

## Finite checks

[FINITE_RESULT.json](a_c/FINITE_RESULT.json) records:

| Check domain | Count |
|---|---:|
| Fixed oracle cases | 83 |
| Conjunction projection | 1,620 |
| Syntactic verdict/performance pairs | 15; 13 potentially legal |
| Evidence states / coordinate guards | 72 / 1,080 |
| Reason-sensitive refinement grid | 1,470 |
| Original-claim / separate-support grids | 17,640 each |
| Binding refusals / completion / support-status checks | 540 / 30 / 60 |
| Fixed N1 reviewer examples | 4 |
| Missing-reason and independent-support cases | 30 |
| Bound-predicate negation | 5 |
| Disjoint normalized effects / temporal cases | 216 / 15 |
| Boolean rows / operator counterexamples | 24 / 9 |
| Fixed conjunction verdict-precedence associativity | 125 |
| Executed faulty implementations detected | 9 |

These domains overlap; there is no grand total of independent tests. The same
Writer authored the finite model and oracle. Their agreement is consistency
evidence; fresh source-first review supplies a distinct, bounded judgment.

## Limits and reproduction

The model does not implement the whole result carrier, conjunction/effect
integration, retained-component union, arbitrary operators, full applicability,
independently supported negative nonperformed/unconfirmed conjunction slots or
missing/unauthenticated joins. Positive separate-evaluation combination is
unimplemented and explicitly reported. Subject, basis, independence and external
authentication are stipulated; predicate equality and provenance tokens do not
verify them.

Recovery checks five stipulated decision rows after current authority, effect
observation and idempotence are supplied. It proves no actual workspace
reacquisition, freshness, invalidation, reuse, construction, configuration or
recovery from context loss. Detailed family policy, complete source fidelity,
predecessor acceptance, categorical proof, practical superiority and release
remain residuals. Nine faulty functions are compared with expected outputs;
this is not a module-replacement mutation campaign.

Reproduce the mechanical and bounded finite checks from the Codex worktree:

```sh
python3 -B specification_methodology/v3/build_tenants/codex/qualification/C3/synthesis/a_c/qualify.py
```

A source change requires reinspection before regeneration. All product bytes
remain at the named source commit. Historical failures remain under the five
`pre-*` archives and the retained review runs; none earns current acceptance
merely because a mechanical check was green.
