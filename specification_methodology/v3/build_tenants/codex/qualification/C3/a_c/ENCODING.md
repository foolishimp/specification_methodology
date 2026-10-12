# Finite interpretation latitude and evidence

The owner identities A/B and token identities t0/t1 are the exact finite domain
selected in SOURCE.md. Integer indices 0/1 encode t0/t1 in Python; the two-tuple
representation assigns exactly one owner to each token. Label strings label:A
and label:B encode names with no grant. The Boolean observation flag encodes
known/unknown current observation before an operation, not uncertain completion
of a previously issued effect. This representation is model-local.

The normal program carries the assignment-only and inspect-refusal distinction,
missing or unauthenticated A, and B as uncovered rather than an omitted slot.
The mutant program deliberately replaces exact permission with naming/label
permission. The executable mutant correspondingly permits label strings, while
retaining refusal of absent, mismatched or inspect grants. The flag selecting
that mutant is test machinery, not an admitted source operation.

FINITE_RESULT.json binds source, normal program, mutant program and helper bytes.
That binding plus independent comparison supports their declared correspondence;
the Python helper does not interpret or execute an a_c program. It exhausts
608 single-step token cases and one selected resumption trace. All other program
relations remain qualitative source comparisons. Uncertain post-effect
completion, stale observations, grant consumption and multistep exhaustive
recovery are outside this finite proof. A failed or optimized invocation supplies
no current success; a previous receipt stays bound to its original bytes.
