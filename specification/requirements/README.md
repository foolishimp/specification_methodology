# STDO Representation Requirements

These active requirement families define the constitutional WHAT shared by
every build tenant:

1. [`REQ-P-BASIS-AND-IDENTITY.md`](REQ-P-BASIS-AND-IDENTITY.md) binds exact
   source, carrier, profile, index-content, and Product identity.
2. [`REQ-P-REPRESENTATION-ALGEBRA.md`](REQ-P-REPRESENTATION-ALGEBRA.md) defines
   the closed `a_c` `I/O/E/C/L/X/V/T/J + ResolutionSet_M` model algebra.
3. [`REQ-P-FP-CONSUMPTION.md`](REQ-P-FP-CONSUMPTION.md) binds the fundamental
   generic `a_c` `F_D`, `F_P`, and `F_H` traversal functor kinds and defines the `F_P`
   semantic-compilation and downstream LLM reasoning contracts.
4. [`REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md`](REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md)
   defines authorized Executive frame assignment and least-closure context
   packets for Executive, Worker, and Reviewer targets.
5. [`REQ-P-SELECTION-AND-ACCEPTANCE.md`](REQ-P-SELECTION-AND-ACCEPTANCE.md)
   separates the `F_P[v_compile]` compilation proposal from the external
   `F_H[v_select]`
   semantic-selection ledger and acceptance boundary.
6. [`REQ-P-COMPRESSION-VERIFICATION.md`](REQ-P-COMPRESSION-VERIFICATION.md)
   separates deterministic construction and cost measurement from probabilistic
   usefulness observations.

The programmatic semantic-index algebra is normative Product law, not a common
serialized intermediate representation. Each tenant realizes it directly in
its carrier. Tenant design may define syntax, layout, canonical bytes, loading,
and mapping mechanisms; it may not turn an `F_P`-classified compiler or
consumer traversal into an `F_D` semantic assessor, replace `F_H[v_select]`
selection with compiler output or
deterministic extraction, or grant its carrier Source STDO authority.

HoG execution, ABG runtime admission, deterministic workspace assessment, and
runtime truth are not embedded in the programmatic-index payload. A consuming
Product may supply those external traversal realizations under its own
authority.
