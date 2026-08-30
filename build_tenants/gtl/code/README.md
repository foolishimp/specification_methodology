# GTL Tenant Code History

Status: retained prior-WHAT implementation and tests; excluded from STDO
Representation `0.1.0`

This package implements historical carrier, canonicalization, admission,
encoding, decoding, projection, and full-model validation experiments. It is
not invoked by the thin Product and contributes no Product member.

The active deterministic dependency is accepted Axiom Indexer
`v0.1.0-rc.1`. Do not extract a second resolver, validator, map builder, joiner,
automatic frame selector, or prompt engine from this package for `0.1.0`.

Historical tests remain useful only for the exact contracts and bases they
name. Passing them does not qualify the current authoring map or native skill.
