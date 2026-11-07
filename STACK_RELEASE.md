# Specification Stack coordinated release

## Meaning Of A Release Request

An owner's instruction to release STDO selects the complete candidate cohort
and all of its build, test, dependency, installed qualification, tag, push,
public artifact and readback phases, unless explicitly narrowed. A downstream
phase already selected by that instruction does not require another request.
Missing authority, a failed gate or a material unresolved decision remains a
real stop; merely crossing a Product boundary is not one.

For the selected 3.0.5-rc.1 cut on public version line 3.0.5, the cohort contains exactly five peer
Products: Specification Methodology v3, STDO Representation, a_c Implementations
(Graphify and Lean), Axiom Indexer and STDO Skills (Codex and Claude).
[RELEASE_PRODUCTS.md](RELEASE_PRODUCTS.md) states all required components.
`stack_release.json` binds their exact subjects, dependencies, current source
and qualified claims under the `rc-five-product-v1` profile. The
`stable-five-product-v1` checker remains available for its original subjects.

The root is coordination, not a Product. Equal versions do not merge Product
meaning, inventories, tags, qualification or acceptance. Every owned Product
and component uses the same exact RC version (the manager wheel's PEP 440
spelling is checked explicitly); third-party dependencies retain
independent exact pins. Consumer adoption remains separately selected.

## Current candidate and immutable history

A status of `assembling` declares unfinished construction. Only a complete
`candidate` may pass ready/content gates. No null field, placeholder, old
snapshot, historical graph/report, label change or source-only archive proves
required current membership or installed usability.

The exact previous root manifest is preserved in
`scripts/fixtures/stack_release-v2.5.1-rc.2.json`. Schema 1 remains the original
three-Product RC profile and is verified by the historical checker path.
Its frozen coordinates are interpreted against its original cut; it does not
become the current candidate. The former stable five-Product manifest is also
preserved exactly at `scripts/fixtures/stack_release-v3.0.5.json`.
All other published cuts, including standalone 3.0.4, remain unchanged.
The owner-authorized reset of the unadopted 3.0.5 line is the only exception:
its five old annotated tag objects are preserved under create-only archival
refs, and all five original asset bytes and qualification records remain
historical. No compatibility bridge or global store migration is selected.

## Source and dependency construction

1. Freeze semantic source S before dependent generation. Inventory every
   authoritative standards member and native workflow contract. Classify
   generated frames as routes to those owners. Explicitly exclude generated
   documentation and tool archives from semantic identity, while retaining
   them as mandatory native payload membership.
2. Build current representation, executable tools, both host packages, proof
   evidence and unified views from S. Bind exact source member digests and
   intended `stdo://releases/v3.0.5-rc.1/` URI. No generated payload embeds the
   still-unknown enclosing native manifest digest.
3. Freeze complete native A only after all required installed assets exist.
   Create its local annotated Product tag, install and verify it, and bind
   the native manifest. A includes current documentation/tooling; a native
   cut missing those assets does not satisfy this release.
4. Freeze external binding/carrier B with all five exact Product subjects,
   S→native A→installed manifest, dependency edges, required qualification
   evidence and publication expectations. This does not edit A. Every change
   to a qualifying source or component invalidates the affected evidence.

The cohort checker refuses an incomplete, extra, stale, mismatched, tampered
or source-incongruent subject. A Lean source file or proof-reader page is not
an executable verification result. Qualification names the actual candidate,
execution environment, installed operation, limits and result; historical
results retain their historical subjects.

## Promotion and publication

Use `scripts/check_stack_release.py --phase ready` for complete constructed
inputs and required evidence, then `--phase content --revision <B>` for the
exact frozen candidate. Independent source-first assessment is a separately
required claim, not inferred from those structural checks.

Prepare all five annotated immutable RC Product tags and five annotated
version selectors locally. This owner-selected cohort uses main and these
tags, with no extra branches. Its initial reset additionally archives the
five exact former stable tag objects. Fixed RC and archive refs are
create-only; each selector is leased against its recorded former object.
Ordinary later RC cuts require a selector at the greatest preceding RC.
The reset exception is restricted to the exact former 3.0.5 objects and
cannot authorize replacing another cut. `--phase refs --revision <B>` checks the complete
local graph, literal configured fetch/push endpoint, every expected remote
direct object or required absence, and preserved immutable cuts. It emits
an exact object-ID push vector and plan digest. Publish only that checked
vector, in one `git push --atomic` with an explicit compare-and-swap lease for
every mutable ref and create-only lease for every immutable tag. There is no
unguarded force or sequential fallback. Drift requires a fresh frozen plan
and repeated qualification, not an in-place waiver.

`--phase published` checks all remote objects and preserved cuts.
`--phase public --public-receipt <path> --public-receipt-sha256 <digest>`
additionally checks a separately retained post-publication receipt, reacquires
the exact public assets anonymously and checks fresh installed qualification
from the published subjects. The external cohort manifest is itself a public
asset; its own digest and later readback are outside its frozen contents, so
they introduce no self-reference. A normal GitHub release
becomes Latest only after required outputs and reviews pass. A later
bookkeeping commit records final results without moving a cut. Partial
publication withholds complete release status and needs explicit recovery;
it is never represented as a completed atomic cohort.

The Executive coordinates within the owner's selected grant. A separately
bound Writer performs effects; an independent Reviewer assesses the frozen
subject without repairing it. Exact operation assignment, evidence and
result consumption remain recorded in the current delivery carrier.

The normal GitHub release is attached to the immutable
`specification_methodology/v3.0.5-rc.1` tag, titled `STDO 3.0.5`, with
`prerelease=false`. Its assets and install instructions name that exact cut.
The former release is retained with its original assets, explicitly marked
superseded and bound to its archived tag object. The selector is a discovery
route; an adopted Product Definition still pins an exact RC URI and manifest.

For this transaction, a successful `refs(B)` execution also executes the
ready/content predicates through the checker's unconditional content path.
That explicit operator consolidation does not claim separate ready/content
commands or skip any predicate. Published and public gates still recheck
their selected live inputs and effects.
