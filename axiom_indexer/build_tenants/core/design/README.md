# Core Design

The MVP has four boundaries:

1. the native skill instructs an LLM to author an axiomatic program;
2. the resolver late-binds logical URIs to exact resources; and
3. the validator checks declared mechanics and derives a read-only logical map.
4. the Executive LLM chooses frames and ordered labeled text; the joiner only
   concatenates those strings.

No semantic acceptance service, carrier, orchestration runtime, automatic frame
selection, or prompt-template engine belongs in this cut.

## Monorepo Placement

The source project may reside at `axiom_indexer/` under a coordination-only
repository root. Its Product Definition, relative paths, tool behavior, and
canonical native skill remain project-local. A root discovery link may expose
that skill without copying it or granting authority. Co-location with
Specification Methodology or STDO Representation creates no Product identity,
composition, or permission to substitute mutable sibling source for an exact
released dependency.

## Release-Coupled Realization

The implementation remains generic and contains no embedded Source STDO
version switch. Each release candidate binds that unchanged mechanics payload
to one exact installed STDO cut and uses the same product-local cut suffix in
the distinct `axiom_indexer` release namespace.

STDO Representation supplies and owns the corpus-specific Axiomatic Program.
It invokes the exact released Axiom mechanics to validate that program and
instantiate its logical map. A changed Source STDO member can therefore require
semantic re-authoring and map regeneration in Representation without creating
an ad hoc semantic branch inside the Axiom implementation.
