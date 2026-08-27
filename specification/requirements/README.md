# STDO Representation Requirements

These active requirement families define the constitutional WHAT shared by
every build tenant:

1. [`REQ-P-BASIS-AND-IDENTITY.md`](REQ-P-BASIS-AND-IDENTITY.md) binds the exact
   source corpus, semantic-address census, and immutable Product coordinates.
2. [`REQ-P-REPRESENTATION-ALGEBRA.md`](REQ-P-REPRESENTATION-ALGEBRA.md) defines
   the carrier-independent domains, relations, operations, and laws.
3. [`REQ-P-PROJECTION-AND-CONFORMANCE.md`](REQ-P-PROJECTION-AND-CONFORMANCE.md)
   defines coverage, projection, measurement, comparison, regeneration, and
   disposition rules.

The algebra is normative semantic law, not a common serialized object model.
Each tenant realizes it directly in its carrier. Tenant design may define
syntax, layout, canonical bytes, and mapping mechanisms; it may not add,
remove, weaken, or reinterpret these requirements.

Execution, HoG traversal, and ABG runtime realization are outside this
requirements surface.
