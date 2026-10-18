# Prescribed Graphify-use workflow probe

This is a separately reported exploratory followup, designed after observing
primary tool uptake and the R03 timeout, before grading primary answers. The
primary study stays unchanged. Most assisted primary runs chose ordinary
retrieval; actual-use answer quality was therefore still unobserved. The
nonauthor design reviewer recommends this bounded probe.

Run one fresh direct and one fresh prescribed-assisted workflow for each
candidate: F01 Codex direct, F02 Claude assisted, F03 Codex assisted, F04 Claude
direct. Reuse the complete original C3/L3 question and its frozen oracle. These
are repeats of two existing questions, selected for their crosscutting
reuse/change-impact/assurance concerns. No new source expectations or favorable
answer examples are introduced. This is not an independent task sample.

Use the same native baselines, source allowlist, tools, original schema,
CLI/model/settings, fresh ephemeral isolation and 24-call/160,000-byte envelope.
Retain the original 720-second ceiling. The smaller task workload supplies
time for explicit Graphify use. Compare within this probe only; its time/token
results are not pooled with the four-question primary runs.

Direct uses ordinary common tools. Prescribed-assisted must make at least one
successful `graph_query`, at least one successful `graph_select` in manifest
mode (`materialize=false`), and a subsequent successful exact documentary
`read_source` before answering. Additional materialization is optional. This
tests discovery plus the tenant's closure/acquisition support as one workflow.
All starting task keywords/source/selector hints are identical; neither arm
receives privileged coordinates.

Mechanical compliance requires those three ordered successful responses with
nonzero emitted payload and no isolation/resource failure. Calls refused by
budget, unknown anchors or other errors do not qualify. Query and selection
relevance is assessed separately against their recorded question, selector
scope and source routes. Ignoring the workflow or choosing irrelevant scope is
a recorded failure; no replacement run. A manifest does not mean native record
payload was acquired. Trace actual native/source reads and preserve unknown
context where needed.

Keep source-content grading condition blind with new random labels and no
tool/usage logs, using the original eight expected criteria, four critical
criteria, three prohibitions and original citation rule for C3/L3. Assessors
do not author actor answers. Mechanical compliance is joined only after the
blind content grades freeze. Preserve original answers and all failures.

Report every run, source-content grade, protocol/workflow compliance, query/
selector relevance, calls, bytes, exact backend usage, graph startup and elapsed
time. Missing backend usage stays unknown. Use the same score weights and
passing threshold as the primary study. Threshold passing does not grant
acceptance or complete semantic coverage. This probe can demonstrate a usable
prescribed path and locate costs or failures; it cannot establish a population
quality gain, isolate Graphify from closure support, or qualify total cost to
obtain an accepted result.
