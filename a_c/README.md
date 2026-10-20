# Axiomatic Calculus Implementations

`a_c` means **axiomatic calculus**. This independent source project builds
realizations of the carrier-neutral STDO calculus. Shared requirements define
the WHAT; each `build_tenants/` child binds those requirements to its own
computational representation and execution stack.

The first tenant is [Graphify](build_tenants/graphify/README.md). It is a
realization of the shared requirements. Axiom Indexer, STDO Representation and
Specification Methodology v3 are not prerequisites or composed Products.

Read [stdo_a_c.json](stdo_a_c.json), [Goals](specification/GOALS.md),
[Intent](specification/INTENT.md), [Product](specification/PRODUCT.md), and
[requirements](specification/requirements/README.md) before changing the project.
The exact calculus remains owned by the selected published STDO standard; this
project does not create a competing definition of `a_c`.

The additional [F_D support toolset](specification/PRODUCT.md#f_d-support-for-f_p-development-actors)
has a provisional public CLI/MCP implementation in the existing Graphify tenant.
STDO3.0 owns the methodology; a_c supports its exact caller-selected contracts.
The [current repair handoff](.ai-workspace/qualification/t008/review-fixes-001/README.md)
records seven implementation repairs, closed nonauthor reviews and fresh
303-test integration. [T-009](.ai-workspace/tickets/completed/T-009-review-repairs.md)
closes that bounded repair work; [T-008](.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md#current-review-repairs--t-009)
remains active for qualification, retaining partial/failed actor trials.
A [separate Claude-direct correction](dogfood/stdo-v3-generation-rc9-review-correction/README.md)
is an unaccepted proposal; the four frozen RC9 representations are unchanged.
[T-007](.ai-workspace/tickets/active/T-007-executive-lifecycle-tooling.md)
remains the historical specification-only increment. The installed builder,
Product composition and method binding are unchanged. Accepted-result benefit
remains Deferred/unqualified, and frozen methodology models are not a maintained
whole-workspace index.

This is a development candidate, with no Product acceptance or release claim.
See the tenant README for runnable commands and the bounded qualification claim.

The completed RC9 rebuild is
[T-006](.ai-workspace/tickets/active/T-006-rc9-rebuild-comparison.md):
[four fresh representations](dogfood/stdo-v3-generation-rc9/README.md) use
the same implementation and settings as the preserved earlier study. The
[older/newer comparison index](dogfood/stdo-v3-generation-rc9/COMPARISON.md)
provides eight Graphify/direct models across Codex and Claude source cuts.
Codex RC9's selected source equals RC5; Claude RC9 changes two owner files.
The new builds pass their mechanical checks; their semantic assessment and
the planned comparison tests remain separate work.

The earlier source-first creation increment is
[T-005](.ai-workspace/tickets/active/T-005-source-first-graphify-generation.md):
the [new Graphify representations and direct baselines](dogfood/stdo-v3-generation/README.md)
were generated from frozen Codex RC5 and Claude RC8 owner source. F_P is inside
this tenant workflow; an existing native a_c model is not a prerequisite.
Both paths preserve all 24 sampled distinctions per candidate in fresh
nonauthor assessments. The [review](dogfood/stdo-v3-generation/REVIEW.md) retains
all 85 construction calls, resource tradeoffs and limits; overall cost saving
and compression remain unestablished. The earlier I5 evaluation below measured
reading existing models and supplies no source-generation verdict.

From this `a_c/` directory, check the included example without installing a
runtime package:

```sh
python3 build_tenants/graphify/code/ac_graph.py validate build_tenants/graphify/test_env/fixtures/toy_model.json
```

The [implementation record](.ai-workspace/comments/codex/20261015_AC_GRAPHIFY_IMPLEMENTATION.md)
retains the initial frozen candidate's review, verification and qualification
boundaries. The consumer trial below records the current bounded codec repairs.

The [two I5 V3 Graphify versions](dogfood/stdo-v3-i5/README.md) separately
represent the completed Codex and Claude candidates selected on 2026-10-17.
They retain each line's authored coverage, complete selector closures and frozen
source custody, with actual Graphify graph/browser outputs. The candidate
worktrees and their independent reviews remain unchanged by these builds.

The [direct-LLM versus Graphify evaluation](dogfood/stdo-v3-i5-evaluation/README.md)
adds self-contained native baselines and matched source-grounded trials for
both candidates. The focused actual-use comparisons preserved quality in both
approaches, with higher Graphify input-token use and mixed elapsed times. This
supports optional discovery/acquisition use for that consumption workload;
quality improvement and lower total cost were not demonstrated there. The report retains all runs and blind
assessments, including the initial pilot's failed run and scope limits.

The historical [frozen v3 iteration-3 example](dogfood/stdo-v3-i3-c29b2be/README.md)
transports the completed Codex candidate's authored interpretation into a
separate Graphify representation, with source custody and complete selector
acquisition checks. It is a consumer example of this independent tenant.
