# Code and realization traces

This capability connects an exact source representation to selected project
code and tests. It extends [AC-R-001–015](README.md) and
[PU-01–09](project-use.md), using [FC-01–07](fd-composition.md) for acquisition
and disclosure. Those contracts retain their ownership; no new lifecycle,
admission rule or formal-proof claim is introduced.

## Required outcomes

**CR-01 — Exact selection and lawful acquisition.** Bind the nominated Product,
exact base representation and its source basis, and explicitly selected local
code/test files with their content identities. Directory selection records its
member set. Acquire only within the selected scope and existing permissions;
an import, graph edge, nearby folder or common repository creates no implicit
route into another Product. Unsupported acquisition routes refuse.

**CR-02 — Additive representation.** Supply a versioned code-and-trace overlay
bound to that exact base. Preserve the existing native model and carrier bytes,
record identities and declared dependency semantics. An unknown overlay version
or inconsistent base binding refuses. Existing validation and Lean evidence
retain their original subject and proof scope; adding an overlay does not extend
them to code or trace assertions.

**CR-03 — Distinct observations and interpretations.** Identify extracted
structural observations separately from caller-attributed F_P mappings such as
`implements`, `supports` and `tests`. Preserve the extractor's supported scope
and each mapping's declared author, origin and meaning. Unknown or ambiguous
endpoints, unsupported files and failed extraction remain inspectable; they
cannot be silently resolved by matching names or presented as an empty successful
extraction. A discovered call/import is not a normative dependency. No structural
observation or trace link establishes implementation correctness, requirement
satisfaction, test execution or result, semantic admission or formal proof.

**CR-04 — Recoverable identities and provenance.** Preserve record and directed
relation identities, distinct parallel/self-relations and repeated occurrences.
Bind code observations and mappings to exact source content, available source
coordinates and producing inputs/tools. Retain unresolved endpoint descriptions
and alternatives without substituting an arbitrary resolved target. Readers can
distinguish observed source, caller assertions and unavailable evidence.

**CR-05 — Readable trace navigation.** The same portable offline reader can
follow a selected requirement to its mapped code and tests, inspect the linked
source and return through the reading trail. Its views distinguish source-model
relations, code observations and F_P mappings, preserving selection when changing
renderers or moving between Files and logical views. Display missing or unresolved
links and extraction coverage honestly. No mapped test means only that no such
link is available in this selected representation, not that the project has no
test. Reading the export needs neither a service nor the extractor installation.

**CR-06 — Currentness and reuse.** Bind reuse to the base model/source, selected
code/test bytes and membership, mapping assertions, overlay profile and relevant
extraction/rendering machinery and options. A material change invalidates the
affected reusable result; report its scope and retain prior evidence as history.
Rechecking identity does not renew a semantic judgment or grant new access.

**CR-07 — Public-path evidence.** Provide documented public construction and
inspection operations using the existing project workflow. Independently assess
the actual supported extractor at an exact pinned version and the generated
reader, including source-to-observation samples and requirement→code→test
navigation. Exercise unresolved/ambiguous endpoints, unsupported/failed extraction,
parallel relations, base preservation and stale-input controls. Report checked
properties, coverage and remaining uncertainty. Semantic fidelity, test outcomes,
whole-project qualification and any quality or cost benefit require their own
evidence under the existing AC-R and PU contracts.

[T-019](../../.ai-workspace/tickets/active/T-019-code-representation.md) selects
the first public CLI/reader slice. Concrete languages, extractor, schema, commands
and storage belong to tenant HOW; this common contract does not mandate Graphify.
