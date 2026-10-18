# Source-first Graphify a_c creation review

2026-10-18. Source-first creation is implemented and exercised. Both direct and
Graphify-generated representations preserve all 24 sampled distinctions for
each frozen candidate; the independent assessments detected no quality
difference on those probes. Graphify is a viable optional creation tenant.
Overall cost reduction and semantic compression remain unestablished.

The Graphify build tenant now creates a proposed a_c representation directly
from documentary source. F_P authoring belongs inside that workflow. An existing
native interpretation or committed compiler account is not a prerequisite.
This corrects the workload tested by the earlier
[I5 model-consumption evaluation](../stdo-v3-i5-evaluation/README.md), whose
findings remain limited to consuming existing representations.

## Exact subjects and implementation

Inputs were selected as the latest clean cuts available at the freeze on
2026-10-18 02:12 UTC. They remain fixed while the candidate workstreams continue.

| Subject | Source cut | Owner input |
|---|---|---|
| Codex RC5 | `5a5b5ad80f0ba4b56b83aadd42ac130de53ba803` | 44 files; 1,269,082 bytes; 795 sections; 11 chunks |
| Claude candidate 8 / RC8 | `9aee01ffa76cfbde1a6b8f1153a25bd6d71c216e` | 49 files; 2,147,228 bytes; 810 sections; 19 chunks |

[Source custody](evidence/source-custody.json) and the
[Codex](corpora/codex/manifest.json) and [Claude](corpora/claude/manifest.json)
manifests bind the exact Git blobs, package custody and exclusions. Inputs are
owner standards, schemas and templates. Derived frames, authority compressions,
verification material, plugin interaction layers, existing a_c programs,
compiler accounts, maps, signatures, reviews and old trial answers are excluded.
The final read-only source check verified all 96 frozen artifacts with zero
writes.

The independent a_c Product still selects published STDO v2.5.1-rc.2, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
The V3 documents, including their calculus, are subjects rather than operating
authority. Neither V3 candidate depends on this implementation.

The preferred `graphify-ac` path is:

```text
exact source -> actual Graphify structural discovery
             -> one initial a_c-aware F_P extraction/authoring pass per chunk
             -> checked source-linked a_c proposal
             -> actual Graphify carrier export and exact recovery
```

This is a custom a_c extraction profile. The stock generic Graphify semantic
prompt is not a second mandatory pass. The `direct` control uses the same exact
chunks, authoring contract, output schema and native codec without Graphify
context. All authors use `gpt-6-astra`, `high`, default service, Codex CLI 0.162.1;
the candidate names identify source corpora, not model families. Fresh isolated
contexts have tools, project instruction injection, memory and MCPs disabled.
The [protocol](PROTOCOL-V2.md), [execution choices](EXECUTION-V2.md) and
[pre-answer freeze](freeze-v2.json) retain the detailed controls.

## Construction and repair evidence

All source characters were dispatched, with explicit dispositions for each
source section. Both Graphify structural input passes completed with no failed
source files. The resulting source graphs contain 877 Codex nodes and 897 Claude
nodes. Source processing is separate from semantic completeness.

The 60 initial calls produced 29 strict passes, seven drafts recoverable through
the separately frozen F_D quotation/range operation, 20 drafts needing F_P
citation repair and four needing fresh authoring. Those four retries produced
three strict passes and one further citation-repair case. All 21 citation
repairs completed within scope. Final chunk selection is 32 strictly valid
drafts, seven verified F_D derivations and 21 verified F_P repair derivations.

Every initial failure remains in the evidence. There are **85 model calls**:
60 initial authors, four fresh authors and 21 grounding repairs. No chunk exceeds
the shared three-call limit, and at most four calls ran concurrently. The
[F_D](GROUNDING-ADDENDUM.md) and [F_P](REPAIR-ADDENDUM.md) operations retain their
separate freezes, parent chains and measured resources. F_P patches may select
new documentary evidence while keeping every non-grounding authored field
unchanged; that invariant does not prove semantic equivalence.

Across the 59 schema-valid returned initial drafts, 7,438 of 7,491 grounding
entries passed strictly: **99.3%**. The 53 defective entries comprise 28 unique
same-section quotation/range recoveries, 19 subject-prefix errors with matching
source path/heading, and six quotations without a same-section whitespace
equivalent. No discovery-node identity was observed being used as a source
section identity. These are locator findings, not statement-fidelity judgments.
The [full initial diagnostics](evidence/grounding-diagnostics-initial-all-60.json)
and [initial outcomes](evidence/initial-mechanical-outcomes.json) retain the
details. A single invalid citation can refuse an entire chunk.

All four final proposals pass the native codec and exact carrier recovery. Both
assisted proposals also pass actual Graphify build/export/recovery at upstream
`fe085cedddde3a18554f8749b230bfe47f3dcce7`. Their exported graphs have 24,338 and
36,532 nodes respectively. The unchanged tenant suite passes all
[107 tests](evidence/tenant-tests-with-repair.json), including actual upstream
compatibility checks. [Assembly evidence](evidence/assembly-summary.json)
records exact model/file identities and processing scope.

## Independent fidelity assessment

The oracle was selected from source and frozen before generated V3 answers:
six probes and 24 required distinctions per candidate, with candidate-specific
law and prohibited distortions. Fresh nonauthor assessors receive neutral-label
copies of the exact models and frozen source. Explicit treatment disclosures
must be recorded; neutral labels alone do not guarantee blinding.

Both fresh nonauthor assessments are closed. The
[Codex grades](grading/codex/grades.json) and
[Claude grades](grading/claude/grades.json) retain every criterion, source locus,
generated record/field citation, prohibited-distortion check and limitation.

| Subject/path | Preserved distinctions | Preserved probes | Prohibited distortions found |
|---|---:|---:|---:|
| Codex Graphify | 24/24 | 6/6 | 0/22 |
| Codex direct | 24/24 | 6/6 | 0/22 |
| Claude Graphify | 24/24 | 6/6 | 0/23 |
| Claude direct | 24/24 | 6/6 | 0/23 |

The probes cover functor kinds and authority; performance/result/conjunction
distinctions; conditional acquisition; residuals and closure; dependency-based
reuse and surviving gates; and assurance independence, dependence and numerical
limits. Each candidate's laws were assessed separately. This includes the
different Codex and Claude treatment of unperformed evaluations; one candidate's
result algebra was not imposed on the other.

All protected input hashes, grading coverage and cited record/field/source
coordinates [pass](evidence/assessment-coordinate-check.json). Both grade files
were closed and their identities [recorded](evidence/closed-fidelity-assessment.json)
before the treatment map was consumed. The
[unblinded summary](evidence/fidelity-summary.json) records 96 preserved criterion
grades, 24 preserved probe grades and 90 absent prohibited-distortion checks.
Neither assessor identified a treatment arm; the Claude assessor recorded the
shared `a_c.graphify.model/1` carrier profile without treating it as an arm label.
Complete blinding is not claimed.

Those mechanical checks prove coverage and resolving coordinates, not an
assessor's semantic judgment. The assessors read substantive authored fields
and applicable explicit references; source quotations alone did not count as
preservation. They retained the limits on unresolved cross-chunk governing
joins and unexecuted operational behavior. This is bounded documentary fidelity
evidence, with semantic acceptance explicitly not issued.

## Measured construction resources

The [complete results](results.json) and [stage breakdown](evidence/resource-breakdown.json)
include failed attempts and all repairs. A separate nonauthor
[resource audit](evidence/resource-audit.json) reconstructed all counters, timings,
sizes and proposal-file identities without an actionable reporting defect.
Input includes cached input; reasoning is already included in output and is not
added again.

| Subject/path | Calls | Reported input | Cached input | Reported output | Sum of actor minutes | Model MiB |
|---|---:|---:|---:|---:|---:|---:|
| Codex Graphify | 12 | 955,101 | 339,584 | 585,828 | 168.3 | 5.23 |
| Codex direct | 13 | 894,586* | 205,440* | 555,175* | 176.5 | 5.27 |
| Claude Graphify | 30 | 2,531,742 | 251,648 | 777,599 | 223.0 | 6.98 |
| Claude direct | 30 | 2,129,152 | 286,848 | 850,259 | 251.0 | 6.86 |

\* One original Codex direct call timed out after 1,200.026 seconds without
reported backend usage. Its time is counted; its tokens remain unknown. Its
cause is unresolved. Reported Codex token totals therefore do not establish
the exact resource ordering.

For Claude, Graphify used **18.9% more input**, **8.5% less output**, and
**11.2% fewer recorded actor seconds**. The direct path needed two full redrafts;
their 23.9 actor-minutes account for most of the 28.0-minute observed difference.
The corresponding Codex actor-time difference is 4.7%, with the timeout retained.
One paired generation per candidate does not establish a general timing effect
or attribute these differences causally to Graphify.

Graphify structural discovery took 0.264 seconds for Codex and 0.333 seconds for
Claude. Final verified assembly/export took 74.0 versus 5.7 seconds for Codex and
129.7 versus 8.2 seconds for Claude, assisted versus direct. Recorded F_D
normalization journal time is separately retained. The dominant measured work
is F_P interpretation. Actor-minute sums are not concurrent wall time. Billing,
unrecorded verification/orchestration, engineering, synthetic smokes, oracle
construction, assessment and owner acceptance cost are outside these totals.
Cached-input subtraction is not a billing formula; no dollar saving is inferred.

The delivered models occupy 5.5–7.3 MB, with 25.6–37.5 MB assisted Graphify graph
exports in addition to carriers and evidence. These formats retain grounding
and provenance and expand the raw owner corpora. This trial establishes no
semantic compression gain.

## Use and limits

The [artifact index](README.md) links all four representations, coverage ledgers,
source discovery graphs and retained evidence. The generic
[generation design](../../build_tenants/graphify/design/generation.md) and
[tenant commands](../../build_tenants/graphify/README.md) describe source-first
creation independently of these V3 clients.

This initial descriptive profile authors objects/concepts, constraints,
relations, latitude and residuals. Traversals, transformations and judgments
are explicitly empty; unsupported operational meaning remains documentary data
or declared residual work. Cross-chunk consolidation, whole-model governing
sufficiency, complete calculus conformance, whole-method fidelity, installed
qualification, acceptance and release remain unqualified. Explicit retained,
residual and omitted dispositions make that boundary inspectable.

The observed creation workflow is usable without a prior native model. The
extra structural graph and Graphify carrier are available for discovery and
navigation, while both treatments still read the same full source and perform
F_P interpretation. This trial measures initial full-corpus creation with graph
cues; selective graph-driven reading, incremental refresh and repeated-use
savings were not tested.

Keep Graphify as an optional implementation choice on this evidence. The tested
meanings are conserved with either path. The observed actor-time savings are
useful pilot data, but higher reported input, conditional repair differences,
unequal cache histories, one unknown-usage timeout and a single paired trial
prevent a general cost-saving conclusion. Repeated use can establish whether
its discovery and navigation capabilities repay their added context and backend
cost. All work is local dogfood; no Git effects were performed by this session.
