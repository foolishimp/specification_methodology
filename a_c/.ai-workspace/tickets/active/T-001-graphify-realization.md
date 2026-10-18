# T-001 Independent Graphify Realization

Status: implementation complete; owner disposition unselected. Re-entry: product_reprice (new source-project
scope), followed by requirements and tenant design before realization.

## Owner instruction

The owner clarified that `a_c` means axiomatic calculus, Graphify is a
`build_tenant` implementation of it, and no dependency on the v3 work is wanted.
After reviewing the proposed common-WHAT/tenant-HOW structure, the owner said:
“ok i want you to implement”. This authorizes source construction and local
verification, not acceptance, release or publication.

## Scope and activations

- Initial worktree: main, clean, HEAD `9549bf2754c8cdde3260762c1102a0d4654c6c1f`; no
  source-project dependency or release-cohort change is selected.
- Executive `/root`: binds outcome/basis, coordinates bounded assessments and
  consumes results; it performs no mutation while in that role.
- Writer `/root`, bootstrap activation: create `a_c/` common source, Product
  Definition, project bootstrap, work record and tenant registry. Update only
  root README/AGENTS/CLAUDE discovery to include this child. This is an explicit
  role transition for those effects; return to Executive afterwards.
- A realization Worker receives a separately recorded grant for
  `a_c/build_tenants/graphify/` only, after the common source is available.
- A reviewer receives read-only authority over the exact resulting source,
  implementation and tests, with no acceptance or mutation authority.

The bootstrap Writer activation is complete; `/root` returns to Executive.
The realization Worker activation is `/root/ac_graphify_realization`, granted
design, code, fixtures, tests and tenant README effects only under
`a_c/build_tenants/graphify/`, based on the common requirements and exact
installed calculus named above. No sibling or common-source effects are granted.

Writer `/root`, local verification activation: create the ignored `a_c/.venv/`
and a fresh temporary upstream checkout outside repository source, install
verification-only Python packages there, and run exact upstream boundary trials.
Retain results under `a_c/.ai-workspace/comments/codex/`. No global installation,
Product dependency, remote publication or cohort effect is granted. Return to
Executive between named verification and evidence-writing effects.

The verification Worker `/root/ac_upstream_boundary` owns exactly
`a_c/build_tenants/graphify/test_env/check_upstream.py` and
`a_c/build_tenants/graphify/test_env/requirements-qualification.txt`; these are
excluded from the realization Worker's territory by explicit coordination.
Its grant also permits temporary test outputs and its final closed result;
source project/common requirements and other tenant files remain read-only.

Writer `/root`, common-review repair activation: clarify carrier admission as a
separate judgment which may be mechanical, and bind governing closure to exact
authored/signature roles in Product and requirements. These supported repairs
consume the nonauthor `/root/ac_contract_assessment` F-CONTRACT result. This
activation is complete; `/root` returns to Executive.

## Independent review and supported repair activation

`/root/ac_contract_assessment` reviewed a frozen 25-file snapshot with codec
SHA-256 `fb91d53c39047f883ffce26b138fa145c27cc359a2f8d28cb8a05dd293b344fa`.
The common contract passed its declared scope. The design's provenance-closure
finding was repaired with explicit governing reference roles.

Its code review established three P2 defects: authored signatures could weaken
fixed core reference-family restrictions; contradictory graph flags/profile
were accepted; and unused external identities could evade declared reference-
domain membership. Executive consumes those findings and activates the same
realization Worker for supported repairs and regression cases in its existing
tenant territory. The independent snapshot remains unchanged. A bounded
nonauthor reread and refreshed affected checks precede construction closure.

## Construction closure

Writer `/root`, final documentation/evidence activation: update this ticket,
Goals and README to reflect the verified candidate, and retain implementation,
review and qualification evidence under `a_c/.ai-workspace/comments/codex/`.
The operation does not change the common requirements or tenant implementation.

All three P2 repairs passed the targeted nonauthor reread on codec
`e8d3fcaa26bf724186d05ba245fa621bfc87c8f75c5d9294795d619a9467e1bb`.
The parent independently verified 41 passing unit tests, strict mypy on all
four Python files and all eight original review refusals. The final actual
upstream trial passed against Graphify `fe085cedddde3a18554f8749b230bfe47f3dcce7`.
The [implementation record](../../comments/codex/20261015_AC_GRAPHIFY_IMPLEMENTATION.md)
retains evidence and residual claims. The authorized implementation increment
is complete. Semantic acceptance, complete-calculus admission, matched cost
evidence, Product acceptance, release and downstream adoption remain unselected.

## Completion evidence

Common source and tenant design exist; a useful local path runs independently;
preservation/refusal tests and actual pinned-upstream compatibility checks pass;
supported review repairs land; results and remaining claims are recorded.
Efficiency gain, full calculus qualification, semantic/model acceptance and
release are not inferred from those checks.
