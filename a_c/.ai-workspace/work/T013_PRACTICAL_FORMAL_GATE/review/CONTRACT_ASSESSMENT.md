# T013 execution-contract assessment

No blocking defect found in the Writer contract. Reviewed ticket SHA-256
`7282a86c1e716f0c6b29bf2ddb2e94ff67d4d94f490e19aaa69a43fd4f1b4f3f`
and Writer closure SHA-256
`6b60f7913efdb6c4b0b995730abc6b628209a64ce5391b23ed392932ce4aae49`.
Every file named by that closure matched its recorded digest when inspected.

The contract selects a complete cold result on the existing full model and
actual supplied view before downstream execution claims. The preserved limits
include the public invocation's total bound, so process subdivision cannot
silently substitute for practical completion. `Model.WellFormed`, exact
reachability, full runtime correspondence and affected independent review remain
the deciding obligations. Source-selected expectations must still be recorded
before the full-size run; this contract does not claim they already exist.

The reuse clauses require establishment origin before replay removal, exact
deciding dependencies and current request bindings. Current Context and
authorization checks remain independent. The proposed optional local-origin
mechanism is adequate in principle under the conditions in
[REUSE_DESIGN_ASSESSMENT.md](REUSE_DESIGN_ASSESSMENT.md); its implementation is
not yet reviewed. In particular, origin material must be protected from both
request input retention and output overlap. The current cold implementation
copies accepted-digest input bytes into evidence before JSON parsing
(`build_tenants/lean/scripts/formal_gate.py:186–199`), so output-only protection
would be insufficient if a future private origin were readable as an input.
This is an implementation discriminator for the proposed mechanism, not a
finding against an existing cache implementation.

The bounded two-run task protocol requires actual F_P work, equal substantive
inputs, independent output assessment and complete cost observations. It leaves
general benefit unestablished when the pair cannot support it. The common
status/locator changes agree with this sequence and preserve the existing
Product requirements, historical evidence and builder selection. Closure and
package preparation do not confer owner acceptance or public release.

This assessment used source inspection, in-memory comparison and byte hashing.
No compiler, kernel, runtime proof, candidate, shared-cache or Git mutation was
performed. Only this Reviewer's granted review records were written. The
next review activation must identify the candidate and any dedicated proof
execution window; the Lean Worker retains the present heavy profiling window.
