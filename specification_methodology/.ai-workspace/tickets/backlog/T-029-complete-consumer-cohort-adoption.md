# T-029 - Complete Consumer Cohort Adoption

- id: T-029
- type: bug
- status: backlog
- owner: specification_methodology
- created_at: 2026-09-05
- change_class: requirement_reprice
- re_entry_point: specification/standards/SPEC_METHOD.md#shared-installed-release-basis-and-toolchain-manager
- authority: user-reported updater gap during ABIogenesis RC4 consumption
- execution_status: not_admitted
- target_release: unselected_successor_after_v2.5.0-rc.4

## Reported Failure

The user instructed: "there should be an rc4 representation update abg with
that, its a failing of the updater that it didnt do all of it", then required
the repair to follow STDO with one truth surface and rejected a consumer-local
checker or updater mechanics in ABIogenesis PRODUCT.md.

ABIogenesis selected and verified STDO RC4 while its Product Definition's
composition still selected bootstrap Representation and Axiom Indexer RC1.
Both Development Product links and the Codex/Claude native skill routes
resolved to those old installs. Its local ABI map retained RC1 source routes
and stale source digests. `stdo status --verify` returned valid for the STDO
basis while these companion relations remained incomplete.

## Owning Boundary

Exact STDO RC4 SPEC_METHOD.md, "Shared Installed Release Basis And Toolchain Manager",
limits mutating adoption to the definition's basis and basis-relative schema
locator. The released manager implements that boundary in
`src/stdo_toolchain/product_definition.py`, `sync_definition` and
`adopt_definition`. This is a gap in complete consumer updating; the current
basis-only command must not silently acquire a wider contract.

The shared STDO method and toolchain own any successor update contract. The
consumer Product Definition supplies selected dependency relations. Exact
upstream cohort and Product release records supply immutable member and
dependency identities. Consumer instructions route to those owners. No local
checker, duplicate lock, or copied Product law supplies another truth surface.

## Proposed Outcome For Owning Re-entry

Select one shared consumer-update contract that handles the explicitly bound
cohort and reports whether its complete selected dependency relation is ready.
It should resolve and verify exact companion releases, update only authorized
consumer bindings and native routes, and expose any stale derived context that
requires source-grounded re-authoring. It must not infer arbitrary composition
from directory proximity or treat mechanical regeneration as semantic review.

The owning re-entry decides how this relates to the existing narrow `adopt`
contract before implementation. This ticket does not select an API or amend
released RC4 law.

## Required Evidence

1. Reproduce the ABI case: current STDO basis with stale companion selections,
   installed links, skill routes, and project-map sources.
2. Complete the authorized selected cohort through the shared update path and
   verify the exact installed Product members and source-bound derived assets.
3. Refuse missing, mismatched, or changed companion bytes without reporting a
   complete update; retain prior usable consumer state on failure.
4. Detect source drift and preserve explicit semantic re-entry when a project
   map cannot be updated mechanically.
5. Preserve unrelated consumer changes, historical installs, and immutable RCs.
6. Establish that ordinary consumer updating requires no new consumer-local
   verification implementation or Product-definition prose edits.

## Disposition

Recorded for shared-method selection. Implementation, source-standard changes,
release, and fleet propagation remain unselected. ABIogenesis's immediate
RC4 install and binding repair is a separate, user-authorized consumption
action; it does not close this updater obligation.
