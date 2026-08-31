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
