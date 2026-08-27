# STDO Representation Requirements

These active requirement families define the constitutional WHAT shared by
every build tenant:

1. [`REQ-P-BASIS-AND-IDENTITY.md`](REQ-P-BASIS-AND-IDENTITY.md) binds exact
   source, carrier, profile, program-content, and Product identity.
2. [`REQ-P-REPRESENTATION-ALGEBRA.md`](REQ-P-REPRESENTATION-ALGEBRA.md) defines
   the closed pure graph-and-constraint algebra.
3. [`REQ-P-FP-CONSUMPTION.md`](REQ-P-FP-CONSUMPTION.md) defines the LLM `F_P`
   consumer and workspace reasoning boundary.
4. [`REQ-P-COMPRESSION-VERIFICATION.md`](REQ-P-COMPRESSION-VERIFICATION.md)
   separates deterministic construction and cost measurement from probabilistic
   usefulness observations.

The graph-and-constraint algebra is normative Product law, not a common
serialized intermediate representation. Each tenant realizes it directly in
its carrier. Tenant design may define syntax, layout, canonical bytes, loading,
and mapping mechanisms; it may not turn the `F_P` consumer into an `F_D`
semantic assessor or grant its carrier Source STDO authority.

HoG traversal, ABG runtime admission, deterministic workspace assessment, and
runtime truth remain outside this requirements surface.
