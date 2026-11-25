# Generic register example

This is an illustrative tool, not an additional standard or required file
format. [ODD §11.5D](../ODD.md#115d-evidence-and-bounded-decisions) owns the
tracking and reconciliation requirement. FOUNDATIONS P4b owns conservation
of needed step-produced facts; ACTIVATION and EVALUATION own acquisition,
evidence and decisions. An LLM or another tool may provide equivalent
functionality without using this register.

A register helps an actor keep track of the work and reconcile its account
with the authoritative workspace. It holds decisions and other facts a
later actor cannot recover, and points to sources and evidence that can be
re-acquired. It does not replace those sources, supply a new authority or
require every observation to be copied into it.

For example, a team is changing the accepted request sizes of an importer:

| Obligation or matter | Tracked account | Basis and evidence references | Reconciliation needed |
|---|---|---|---|
| Support the size limit in the adopted requirement | Implementation prepared; acceptance outstanding | Exact requirement revision, implementation subject and test result | Confirm the tested implementation still matches the current candidate and the requirement is still in force |
| An owner chose an error response for excessive input | Record the decision, its scope and authority reference | The owner's retained decision and the affected requirement | Re-enter if that decision is superseded; the register cannot choose a replacement |
| One environment was not exercised | Residual remains open | Test scope and the unperformed case | Keep the gap visible until evidence or an authorised disposition resolves it |

The column names and storage are incidental. A useful mechanism can answer
what is being pursued, what was decided and by whom, what evidence supports
the current claim, what remains unresolved, and what source change would
require reconciliation. When a material input changes, the affected account
is checked again; historical success is not carried forward as current
success merely because it was recorded.

An LLM-provided mechanism can serve the same purpose if the facts needed at
resumption or handoff remain available to the relevant actor and its claims
can be checked against the declared sources. Unavailable private state does
not meet that requirement. The method requires the functions, not a separate
register artifact or a universal event history.
