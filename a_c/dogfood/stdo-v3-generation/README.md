# Source-first a_c Graphify creation

Completed dogfood construction and independent fidelity assessment, 2026-10-18.
The Graphify tenant now creates a proposed a_c representation directly from
source, with F_P authoring inside the workflow and no prior native model.
Fresh Graphify and direct representations of both selected V3 cuts are below.

Both paths preserve all **24 sampled distinctions per candidate** in the fresh
nonauthor assessments. This demonstrates bounded documentary fidelity, with no
quality difference detected on those probes. Overall cost reduction and semantic
compression remain unestablished. The [full review](REVIEW.md) explains the
findings, resource tradeoffs, retained failures and limits.

```text
frozen source documents
  -> actual Graphify structural source graph
  -> fresh a_c-aware F_P extraction/authoring
  -> source/shape checks and conditional, measured citation repair
  -> checked proposed a_c model and actual Graphify representation
```

This is a custom a_c extraction profile. The matching `direct` control uses the
same source chunks, authoring contract, schema and model settings without
Graphify context. All authors use gpt-6-astra/high/default; Codex and Claude name
the source corpora, not different author models.

## Representations

| Subject/path | a_c model | Graph/carrier | Coverage and limits |
|---|---|---|---|
| Codex Graphify | [model](runs-v2/codex/graphify-ac/repaired-proposal/model.json) | [actual Graphify graph](runs-v2/codex/graphify-ac/repaired-proposal/graph.json) | [coverage](runs-v2/codex/graphify-ac/repaired-proposal/coverage.json) |
| Codex direct baseline | [model](runs-v2/codex/direct/repaired-proposal/model.json) | [native carrier](runs-v2/codex/direct/repaired-proposal/carrier.json) | [coverage](runs-v2/codex/direct/repaired-proposal/coverage.json) |
| Claude Graphify | [model](runs-v2/claude/graphify-ac/repaired-proposal/model.json) | [actual Graphify graph](runs-v2/claude/graphify-ac/repaired-proposal/graph.json) | [coverage](runs-v2/claude/graphify-ac/repaired-proposal/coverage.json) |
| Claude direct baseline | [model](runs-v2/claude/direct/repaired-proposal/model.json) | [native carrier](runs-v2/claude/direct/repaired-proposal/carrier.json) | [coverage](runs-v2/claude/direct/repaired-proposal/coverage.json) |

The separate structural discovery graphs used during authoring are
[Codex](runs-v2/codex/graphify-ac/discovery/graph.json) and
[Claude](runs-v2/claude/graphify-ac/discovery/graph.json). Structural links do not
mechanically become normative dependencies or authority.

## Exact source cuts

These were the latest clean inputs selected at the freeze on
2026-10-18 02:12 UTC. They remain fixed while the V3 workstreams continue.

| Candidate | Source cut | Custody checkpoint |
|---|---|---|
| Codex RC5 | `5a5b5ad80f0ba4b56b83aadd42ac130de53ba803` | `87512593de6ec60660f2ad9e040241d67a4108d7` |
| Claude candidate 8 / RC8 | `9aee01ffa76cfbde1a6b8f1153a25bd6d71c216e` | `1db13bfeb0675fc95de04aceccb214f5b76873fc` |

[Source custody](evidence/source-custody.json) binds 44 Codex owner files
(1,269,082 bytes) and 49 Claude owner files (2,147,228 bytes). Standards, schemas
and templates are included. Derived frames, authority compressions, verification
material, plugin interaction layers, existing a_c interpretations, compiler
accounts, maps, reviews and old trial answers are excluded from generation.
The independent implementation basis remains published STDO v2.5.1-rc.2; each
V3 corpus, including its calculus, is subject data. No V3 dependency is created.

## Evidence and conclusion

All four proposals pass native validation and exact carrier recovery. Both
assisted outputs also recover exactly through actual Graphify at pinned upstream
`fe085cedddde3a18554f8749b230bfe47f3dcce7`. All
[107 tenant tests](evidence/tenant-tests-with-repair.json) pass. The fresh
[Codex](grading/codex/grades.json) and [Claude](grading/claude/grades.json)
assessments preserve all 96 criterion grades across four models; none of the 90
prohibited-distortion checks was asserted. Protected inputs, complete grading
coverage and evidence coordinates [pass](evidence/assessment-coordinate-check.json).

The [complete resource record](results.json) and separate
[nonauthor audit](evidence/resource-audit.json) include all 85 calls: 60 initial
authors, four fresh retries and 21 citation repairs. For Claude, Graphify used
18.9% more input, 8.5% less output and 11.2% fewer summed actor seconds. Codex's
observed actor-time difference is 4.7%, but one direct timeout has unknown token
usage. A single pair per corpus and unequal cache/repair histories establish no
general cost saving. The delivered models occupy 5.5–7.3 MB; compression remains
unqualified.

The implementation therefore fits the intended creation workflow. Its optional
structural discovery and Graphify carrier can support navigation and later use;
this trial found no additional quality benefit on the selected probes. Repeated
use, refresh and selective acquisition need their own evidence.

This initial descriptive profile has five active families: objects/concepts,
constraints, relations, latitude and residuals. Traversals, transformations and
judgments are explicitly empty. Cross-chunk consolidation, governing sufficiency,
complete calculus conformance, whole-method fidelity, installed qualification,
acceptance and release remain unqualified. The artifacts are local dogfood;
this session performed no Git effects.

## Implementation and reproducibility

The [generic generator](../../build_tenants/graphify/code/ac_generate.py),
[generation design](../../build_tenants/graphify/design/generation.md) and
[tenant commands](../../build_tenants/graphify/README.md) implement source-first
creation independently of these V3 clients. The active
[protocol](PROTOCOL-V2.md), [execution choices](EXECUTION-V2.md),
[pre-answer freeze](freeze-v2.json) and
[T-005](../../.ai-workspace/tickets/active/T-005-source-first-graphify-generation.md)
bind the run. [F_D recovery](GROUNDING-ADDENDUM.md) and
[F_P citation repair](REPAIR-ADDENDUM.md) retain separate freezes, exact parent
chains and measured resources. All initial failures remain visible.

The earlier [I5 evaluation](../stdo-v3-i5-evaluation/README.md) tested consuming
already-authored models. Its retrieval findings do not answer source generation;
its original evidence is unchanged. The superseded two-pass prototype and
synthetic smoke are retained separately under `archive/` and `smoke/`; their
usage is excluded from V3 construction totals.
