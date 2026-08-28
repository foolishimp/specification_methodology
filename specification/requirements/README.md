# STDO Representation Requirements

These active requirement families define the constitutional WHAT shared by
every build tenant:

1. [`REQ-P-BASIS-AND-IDENTITY.md`](REQ-P-BASIS-AND-IDENTITY.md) binds exact
   source, carrier, profile, index-content, and Product identity.
2. [`REQ-P-REPRESENTATION-ALGEBRA.md`](REQ-P-REPRESENTATION-ALGEBRA.md) defines
   the closed pure graph-and-constraint algebra.
3. [`REQ-P-FP-CONSUMPTION.md`](REQ-P-FP-CONSUMPTION.md) binds the fundamental
   ODD `F_D`, `F_P`, and `F_H` traversal functions and defines the external LLM
   reasoning contract.
4. [`REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md`](REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md)
   defines authorized Executive frame assignment and least-closure context
   packets for Executive, Worker, and Reviewer targets.
5. [`REQ-P-SELECTION-AND-ACCEPTANCE.md`](REQ-P-SELECTION-AND-ACCEPTANCE.md)
   defines the external `F_H` semantic-selection ledger and acceptance boundary.
6. [`REQ-P-COMPRESSION-VERIFICATION.md`](REQ-P-COMPRESSION-VERIFICATION.md)
   separates deterministic construction and cost measurement from probabilistic
   usefulness observations.

The programmatic semantic-index algebra is normative Product law, not a common
serialized intermediate representation. Each tenant realizes it directly in
its carrier. Tenant design may define syntax, layout, canonical bytes, loading,
and mapping mechanisms; it may not turn the `F_P` consumer into an `F_D`
semantic assessor, replace `F_H` selection with deterministic extraction, or
grant its carrier Source STDO authority.

HoG execution, ABG runtime admission, deterministic workspace assessment, and
runtime truth are not embedded in the programmatic-index payload. A consuming
Product may supply those external traversal realizations under its own
authority.
