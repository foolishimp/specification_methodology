# Finite closure and projection design

This HOW realizes [FR-001..007](../../../specification/requirements/formalisation.md)
under T-011. The selected calculus is exactly the installed v2.5.1-rc.2
`AXIOMATIC_CALCULUS.md`; [SOURCE_CORRESPONDENCE.md](SOURCE_CORRESPONDENCE.md)
binds the selected clauses. The 3.0.2 supplement is immutable subject input.

`AC.Model` distinguishes eight `Family` constructors. A `Record` has a finite
local key, exact source identity, family, context, owner, scope, basis and the
entire canonical JSON payload. `Model.envelope` retains every source field
outside the eight populations, including signature, basis, interpretation,
selection ledger and dependency declaration. Empty populations are recovered
from the fixed total family mapping. `Reference` preserves each occurrence,
its typed path, local/external target, declared governing flag and domain.
`PathStep.field "0"` and `PathStep.index 0` are distinct. Local indices are source
positions, not a replacement for source-owned semantic identities.

`Model.WellFormed` checks local key and identity uniqueness, external identity
uniqueness, local/external disjointness and every imported edge/reference
endpoint. Full signature/type/coverage checks are performed separately by the
bounded importer; the kernel does not prove the JSON parser or schema mapping.
The importer reconstructs the entire original model and validates both frozen
carrier forms independently. Its details and exact two supported signatures
are in [IMPORTER.md](IMPORTER.md).

A dependency edge `a → b` means retaining record `a` requires `b` under the exact
imported relation. Required pairs come from governing local references,
selected governing relation records and constraint/latitude/residual
attachments. Duplicate pairs may collapse for reachability, while parallel
relation records, repeated occurrences and full source content remain distinct.
Ordinary discovery and provenance do not automatically supply required edges.

The untrusted search produces a discovery trace. `Witness` recursively checks
that every added record has an incoming required edge from an already reached
record. `traceSet` begins with the seeds and inserts those records. The finite
checker also checks nonempty/local seeds, local result membership and closure
under every required outgoing edge. Cycles need no special induction hypothesis:
each successful trace has finite length, and the output is a finite set.

The generic proofs use Mathlib `Finset` membership/subset algebra and
`Relation.ReflTransGen`. `certificate_exact_reachability` proves both directions
of the membership/reachability equivalence. `certificate_least` proves inclusion
in every seed-containing closed finite set. `certificate_fixed_point` proves
the stated seed-union-required fixed-point equation. `certificate_unique` is
uniqueness of successful least-closure certificates, not uniqueness of every
fixed point (disconnected cycles can form larger fixed points).

`project` checks the imported finite model and certificate before returning a
projection. The budget unit is the number of distinct local records in the
whole required closure. `project_ok_properties` eliminates an actual successful
return into the checks, budget bound and exact constructed projection;
`project_ok_exact_reachability` connects that return to the reachability theorem.
The sole budget-failure branch returns an error; it cannot return a prefix.

`makeProjection` filters the parent list without constructing replacement
records. Its retained membership equivalence preserves every field and source
ordering; named authority/basis conservation follows from whole-record equality.
The view carries exact parent coordinates/envelope/seeds, included/excluded
keys, selected external tuples, omitted local references, retained unresolved
residuals and separately excluded residual records, plus invalidation content.
`projection_all_residuals_accounted` names every parent residual in one of those
two unresolved boundary classes. It issues no disposition.

`AC.Fixture` and `AC.Toy` are deterministic generated imports. Every selector's
check and exact set is proved with `decide +kernel`, then generic soundness and
success/refusal theorems are instantiated. `AC.Audit` pins the expected generic
propositions and requests all deciding theorem axioms. `AC.Run` executes the
same `project` definition and serializes its actual output; the integration
check compares full payloads, coordinates and boundaries with the independently
recovered source. Compiler execution and serialization are tested boundaries,
not silently treated as proof of their own correctness.
