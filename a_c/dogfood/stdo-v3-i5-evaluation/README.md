# Direct LLM versus Graphify-assisted a_c

Completed dogfood evaluation, 2026-10-17. **The evidence supports retaining
Graphify as an optional discovery/acquisition backend. It does not establish
better semantic authoring or lower total cost than direct native access.**
Both actual-use comparisons preserved the tested meaning completely. Graphify
added relevant routing and exact selector manifests, with higher input-token
use and mixed elapsed-time results. F_P still supplied the semantic judgment.

The [paired baseline catalogue](paired-baselines.json) identifies both native
and Graphify representations. [Primary results](results.json) and
[prescribed-use results](followup/results.json) retain every run, grade,
critical omission, refusal, usage field and timing. No V3 source, prior
Graphify implementation or candidate artifact was changed by this evaluation. This creates no V3
dependency, acceptance, installed qualification or RC claim.

**What the baselines contain**

| Frozen candidate | Native baseline | Complete supplied program | Existing Graphify transport |
|---|---|---|---|
| Codex package `d1b33480b46f45bb46198a2f63ca197e84e40e55` | [manifest](baselines/codex/manifest.json), [program](baselines/codex/program.json), [signature](baselines/codex/signature.md), [coverage](baselines/codex/coverage.json) | 712 clauses, 5 residuals, 732 frame indexes; no symbols | [manifest](../stdo-v3-i5-codex/artifacts/manifest.json), [model](../stdo-v3-i5-codex/artifacts/model.json.gz), [carrier](../stdo-v3-i5-codex/artifacts/graph.json.gz) |
| Claude package `af3b8b7107c92a216cc53d629ddeefecd7f77fca` | [manifest](baselines/claude/manifest.json), [program](baselines/claude/program.json), [signature](baselines/claude/signature.md), [coverage](baselines/claude/coverage.json) | 39 symbols, 155 clauses, 5 frame indexes; no residuals | [manifest](../stdo-v3-i5-claude/artifacts/manifest.json), [model](../stdo-v3-i5-claude/artifacts/model.json.gz), [carrier](../stdo-v3-i5-claude/artifacts/graph.json.gz) |

Each new native baseline is self-contained: exact original program, lossless
family/ordinal record catalogue, signature, coverage and frozen source files.
The direct reader uses Python's standard library and imports no Graphify.
Archive/member SHA-256, Git blob identity and modes reproduce; catalogue
recovery preserves every supplied native record. An isolated archive tamper
trial refuses. See [build evidence](evidence/native-build.json) and
[custody counterexample](evidence/native-tamper.json).

The Claude program retains its declared partial interpretation: 24 sections
encoded in part across eight members, 182 unencoded sections and G5–G13 outside
the encoded scope. The Codex program retains its own coverage and five
residuals. These are different authoring scopes. Comparisons are within each
candidate; their counts and scores do not rank the competing methodologies.

Graphify carries the same authored native meaning. Both arms also have the
same ordinary source/native search and readers. Historical qualification and
fidelity-review answers are excluded. Assisted discovery uses an allowlisted
induced view of the actual pinned upstream graph, with excluded source objects
and metadata removed. Exact governing closure uses the unchanged complete
model/catalogue. This treatment bundles Graphify discovery with the a_c
tenant's acquisition support; the experiment cannot isolate their individual
contributions or a native backend with equivalent automatic closure tooling.

The fresh outputs are small structured semantic contracts and applied
judgments. They are not a new full-method interpretation or native a_c grammar
conformance demonstration. Historical LLM/F_P authoring and compilation of the
supplied programs are common prior work with unmeasured cost.

**Controlled initial pilot**

The [protocol](PROTOCOL.md), [source-only questions](private/tasks.json),
[source oracle](private/oracle.json), schema, tools, baseline pins and matched
prompts [froze before answers](freeze.json). A nonauthor
[design review](evidence/prelaunch-design-review.json) checked the setup.
All 47 unique oracle source coordinates reproduce exactly.

Eight fresh CLI actors used `gpt-6-astra`, `max`, default service tier and Codex
CLI 0.162.1: two runs per approach/candidate, four questions per run. The tasks
covered conditional adoption/activation, result/conjunction contracts, evidence
reuse/shared assurance, and design completion beyond a returned view. All
actors used the same model; “Codex” and “Claude” identify source candidates.
Each run had 24 attempted tool calls, 160,000 emitted UTF-8 JSON payload bytes
and a 720-second ceiling. Shell, web, apps, delegation, memories, project
instruction injection and unrelated MCP servers were disabled per invocation;
effective MCP inventory was checked before each run.

Fresh nonauthor assessors received anonymous answers and exact source, with no
condition mapping, invocation, usage or tool logs. Required source criteria
receive met/partial/missed/incorrect grades; critical criteria weigh 2, others
1, partial earns half credit. A strict task pass requires every critical
criterion fully met, no prohibited claim, at least 80% weighted credit and a
valid supporting documentary citation. This is a provisional source-completeness
rubric, not an owner-adopted acceptance contract. Noncritical omissions can
remain in a passing answer.

| Candidate | Access available | Usable runs | Rubric credit on returned answers | Strict task passes / attempted | Runs using graph tools |
|---|---|---:|---:|---:|---:|
| Codex | Direct | 2/2 | 93.23% | 5/8 | 0 |
| Codex | Assisted | 1/2 | 93.75% | 3/8 | 1 |
| Claude | Direct | 2/2 | 85.42% | 2/8 | 0 |
| Claude | Assisted | 2/2 | 85.94% | 2/8 | 0 |

These are four task purposes per candidate repeated across runs, not 32
independent questions. Seven runs returned valid outputs; R03 reached 720
seconds without a final answer. That run completed retrieval at about 117
seconds, including 13.80 seconds of graph startup. Its later generation did
not finish; the cause remains unresolved. Its four missing task answers count
as practical failures, with no assessed semantic contradiction. Its backend
usage was not returned and remains unknown. It was not replaced. See the
[failure observation](evidence/R03-failure.json).

The other three assisted runs used ordinary retrieval exclusively. Their cost
or quality differences therefore do not demonstrate a benefit from using graph
discovery. In particular, the Claude assisted runs reported fewer input tokens
and calls, but neither used Graphify. Cache-adjusted input also tells a
different story: input minus reported cached tokens totals 126,218 for direct
and 133,985 for assisted Claude runs. Codex assisted usage is incomplete and
cannot be compared as a two-run total.

The blind assessments found omissions rather than material contradictions or
asserted prohibited claims. Common gaps included carrying forward independently
applicable common obligations when design adoption is unresolved; exact work
activation versus durable adoption/grants; applicability/exclusion versus a
satisfied nonapplication disjunction; and conditions/limits of quantified
assurance. Some omissions concern explicit completeness of each separate
contract despite related statements elsewhere in the batch. The strict pass
counts should be read with the criterion-level reasons, rather than as a rate
of wrong scenario decisions. All supported P/F/U branches were preserved.

See [Codex grades](grading/codex/grades.json) and
[Claude grades](grading/claude/grades.json). The
[assessment/code freeze](evidence/analysis-freeze.json) precedes condition-level
score aggregation. No actor answer was repaired.

**Actual Graphify-use probe**

Low tool uptake left actual-use quality unresolved, so a separately
[reviewed](evidence/followup-design-review.json),
[frozen exploratory protocol](followup/PROTOCOL.md) repeated only C3/L3, one
run per approach/candidate. It used the unchanged source oracle, model, tools,
limits and schema. Assisted actors had to make a successful relevant graph
query, request a selector manifest and then read deciding documentary source.
Neither arm received privileged source or selector hints. The four runs are
reported separately from the initial pilot.

All four answers met all eight source criteria and asserted no prohibited
claim. Both prescribed workflows complied. Independent
[routing review](followup/evidence/relevance-review.json) found the queries,
selected scopes and subsequent source reads materially relevant. Codex's
change-impact selector was narrower than the whole question; supplementary
source reads covered assurance and conjunction. Both selected manifests rather
than materialized native closure payloads. Relevance and manifest success
alone establish no semantic sufficiency.

| Candidate | Workflow | Rubric credit | Input tokens | Cached input | Input minus cached | Output tokens | Calls | Payload bytes | Elapsed |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Codex | Direct | 100% | 190,155 | 158,848 | 31,307 | 9,009 | 13 | 95,888 | 214.27 s |
| Codex | Graphify prescribed | 100% | 311,374 | 256,256 | 55,118 | 7,293 | 14 | 116,889 | 200.95 s |
| Claude | Direct | 100% | 222,741 | 182,656 | 40,085 | 7,963 | 15 | 140,868 | 189.28 s |
| Claude | Graphify prescribed | 100% | 252,713 | 202,880 | 49,833 | 10,469 | 13 | 140,964 | 250.25 s |

Graphify used 63.75% more input for Codex and 13.46% more for Claude. Input
minus cached tokens rose 76.06% and 24.32%. Codex output tokens fell 19.05%;
Claude output rose 31.47%. Elapsed time fell 6.22% for Codex and rose 32.21%
for Claude. These single paired observations show neither a quality gain nor
a consistent resource saving. They do not support a timing/significance claim.
Both assisted actors first requested an out-of-range graph query budget and
recovered from an explicit refusal; those calls remain included.

The focused question also had four times the per-question reading envelope of
the original batch. Its better completeness cannot be attributed to Graphify:
both direct answers were also complete. See the separate
[Codex](followup/grading/codex/grades.json) and
[Claude](followup/grading/claude/grades.json) assessments and their
[pre-aggregation freeze](evidence/followup-assessment-freeze.json).

**Setup, storage and cost boundary**

| Measurement | Codex | Claude |
|---|---:|---:|
| Reproduce/verify native baseline | 0.23 s | 0.03 s |
| Fresh full transport build/export/reload/compression | 10.56 s | 1.71 s |
| Actual upstream graph build stage within that total | 2.00 s | 0.31 s |
| Cold graph startup in actual-use probe | 13.88 s | 2.05 s |
| Native program bytes | 14,403,693 | 220,494 |
| Full upstream graph export bytes | 82,282,887 | 11,276,154 |
| Native program gzip bytes | 1,247,024 | 20,513 |
| Full upstream export gzip bytes | 5,435,861 | 2,104,198 |

[Setup evidence](evidence/graph-setup.json) measures one local full T-003 build,
including historical Markdown excluded from actor discovery. Runtime graph
startup includes validation, closure-catalogue checking and discovery filtering;
it is separately metered and cached within a run. Shared upstream import took
0.15 seconds outside the per-candidate build totals. Source, model construction,
codec materialization, upstream build/export, reload and compression stages are
separate. Build-time Graphify operations made no LLM calls.

[Storage evidence](evidence/storage.json) distinguishes actual upstream export,
codec carrier and model files. The graph includes literal Markdown and
representation machinery beyond the native program, so these inventories are
not a content-equivalent compression ratio. Both actor arms share the full
native/source baseline; the graph is additional storage. No compression saving
was demonstrated by these representations.

Usage fields are exact CLI-reported actor counters, including reported cache
and reasoning fields. Input minus cached is an arithmetic diagnostic, not a
billing formula; reasoning output is reported separately in JSON and is not
added to output again. No dollar price, cache discount or backend invoice was
assumed. Experimental oracle/assessment/harness engineering and historical
semantic authoring are additional unmetered costs. The successful infrastructure
smoke's 31,786 input/15,232 cached/146 output tokens are excluded from task
comparisons; its earlier configuration failure made no model call. There was
no correction/retest cycle for actor answers and no owner acceptance. Total
cost to obtain an accepted result and any break-even point remain unqualified.

**Practical disposition**

Use direct native/source access as the current default for this semantic work.
Retain the independently built Graphify tenant for navigation, visualization
and optional declared acquisition. This pilot demonstrates faithful content
transport and usable source routing; it supplies no evidence that Graphify
reduces the F_P obligation to preserve conditions, result distinctions, scope
and unresolved meaning. The native checker already provides the closure
reference against which the graph was qualified, so closure preservation is
not a unique graph-library advantage.

Further value would need repeated representative work: broader discovery,
change impact across related models, graph reuse/refresh and repair effort to
obtain an accepted result. Compact source-coordinate views and clearer tool
argument bounds are useful candidates for a future measured iteration. Their
benefit is not established here. F-USEFULNESS remains open at that broader bar.

**Verification and reproduction**

The [17-test harness qualification](tests/qualification.json) passes, including
actual Graphify `fe085cedddde3a18554f8749b230bfe47f3dcce7` trials for both
candidates, complete selector catalogue checks, allowlist/source parity,
protocol, path escapes and budget refusals. The underlying T-003 transport and
737-selector evidence remain unchanged. All 12 actor invocations respected
tool/file isolation; one failed the wall/usable-output requirement. No study
actor or reader process remains running.
The [final verification](evidence/final-verification.json) binds the unchanged
input freezes, original artifacts, answer/grade identities and isolation checks.

All 279 citations across the 32 returned task answers match exact source
coordinates/quotes, and every quoted string was present in emitted evidence.
Mechanical checking initially rejected standard en-dash ranges and combined
heading/line strings. The checker was corrected uniformly to implement the
original section-or-line rule; exact range/quote checks remain mandatory.
Original packets, v2/v3 supplements and
[correction evidence](evidence/citation-parser-correction-v3.json) are retained.
No question, oracle criterion, weight, threshold or answer changed.

From this directory, reproduce the native baselines and deterministic
aggregation over the retained evidence:

```sh
python3 build_baselines.py
python3 summarize.py
python3 summarize.py --followup
```

The full actor CLI arguments and isolation checks are retained in each
`runs/<id>/execution/invocation.json` and
`followup/runs/<id>/execution/invocation.json`. Fresh LLM runs require a new
output directory and existing CLI authentication; nondeterministic answers and
usage will differ. The pinned-upstream test command is in the qualification
record. Keep the original freezes, prompts and evidence unchanged for review.

This is eight original questions, repeated to attempt 36 task answers across
12 fresh actors. Eleven actors returned 32 answers. Same-provider, condition-
blind nonauthor grading supplies bounded semantic evidence; it is not
independent-family validation, complete calculus conformance, Product
acceptance or release qualification.
