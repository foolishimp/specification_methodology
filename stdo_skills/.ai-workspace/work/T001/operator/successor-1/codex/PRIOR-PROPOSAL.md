# Codex tenant design — T001 candidate 1

Recorded before implementation. Scope: build_tenants/codex only; construction authority is operator codex/TASK.md SHA256 eae576ac13cbf358889845b6532c62482d0cc593d9c669eb467a88911d01a9e0, grant urn:stdo-skills:T001:codex:construction:1. No Product acceptance, publication or installation is claimed.

## Basis and source ownership

STDO Skills common inventory a6d348b8385ea453ce29362fb9d74559304b1b91743b3c9ea31a83a9f02b5f2d governs this candidate. STDO stdo://releases/v3.0.1-rc.1/ manifest 60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8 owns the method. Its installed basis was verified by stdo status --definition stdo_skills.json --verify on 2026-10-25. The discovery channel does not select a newer basis.

Requirements SHA256 dcc2564e597d3d3c8fcff025a515f4a92a62e7f3aa2f7ba80af97f7db75f6acc and scenarios SHA256 089221fb9d7eee532f91c6ef40a4bfdaaa18c00fcc28bc2f538ddd6b6e3ff03e remain common external authority. The frame basis SHA256 00a91bb5a16ba8802cb2d3132c08677c978f3ef50d4e6c61d864c5afdb960baa is selected by this activation for construction, not accepted by this Worker. Method routing comes from specification/SOURCE_OWNERS.md SHA256 15300e9871b842cb6ab81b360fe9717766638e82abc2d1cf06c5cebc2febfca3. Installed deciding sections are acquired as needed; no copied methodology is installed.

## Algorithm and host binding

One skill, stdo-work, supplies task-based discovery for an already governed workspace and explicit setup requests. Its name and description remain available to Codex; automatic invocation stays enabled by omitting any disabling policy. Only the entrypoint and the relevant reference are acquired. References are packaged inside the skill, so copying the complete directory preserves their links.

| Requirements | Algorithm | Codex or tool mechanism | Finite proof |
|---|---|---|---|
| SK-01 | Route relevant task, ignore unrelated task, distinguish discovery from execution | SKILL.md frontmatter; repository .agents/skills/stdo-work; explicit $stdo-work | Q01, Q02, Q12 |
| SK-02 | Select one Product, verify exact installed basis, acquire bootstrap and deciding owner | stdo status --definition PATH --verify; public source.read with exact SourceRefs | Q03 |
| SK-03 | Reuse sufficient authority; choose direct Writer for a sufficient small effect; coordinate only on material boundary | Codex reasoning over acquired contract; host actors only where selected and admitted | Q04, Q05 |
| SK-04 | Discover exact schemas, call required operation, retain actual response and effect evidence | native a_c public MCP or explicitly configured CLI using complete request envelopes | Q01, Q06, Q08 |
| SK-05 | Preserve smallest deciding causal context including retained obligations and differing histories | exact SourceRefs, context.assemble when selected; activation carrier | Q05, Q07 |
| SK-06 | Bind child outcome, basis, territory, proof, consumer and stop; consume closed return before next activation | configured contract.preflight, dispatch.start/observe and return.capture/check where admitted; no invented tool | Q04, Q05 |
| SK-07 | Derive expected behavior from source before exact candidate; retain exposure and family limits | review.prepare where selected; fresh separately admitted reviewer; source.read | Q05, Q09 |
| SK-08 | Reacquire current evidence, reconcile uncertain effects before retry, retain unaffected evidence | workspace.observe, source.read, evidence.read, granted recovery path | Q07-Q10 |
| SK-09 | Separate candidate availability, assessment, consumer disposition, acceptance | declared closed return schema, original basis, explicit residuals and not_performed | Q06, Q09, Q10 |
| SK-10 | Prepare exact immutable candidate; act only on authorized release destination; scoped package install/update/remove | selected release tool discovered from its contract; file-copy deployment only with corresponding grant | Q11, Q12 |
| SK-11 | Package references together; inventory exact content; retain previous identity on update | read-only package verifier; owned-directory installation recipe | Q12 |
| SK-12 | Freeze substantive tasks and independent oracle, preserve every attempt and unknown costs | qualification plan and actual host traces, not keyword success grading | Q01-Q12 |

Codex mechanics are independently sourced in operator codex/HOST.md SHA256 6f940ea5514cf8ea3e0b359adbb0337d3ff020c414aca54c502befab9665213e: codex-cli 0.164.0, repository-local .agents/skills discovery, explicit $skill-name, relative references, restart when discovery is stale. Configured model/effort gpt-6-astra/max is inherited; actual resolution is unknown unless the run records it. No nested actor is launched in this construction.

## Tool boundary and failure behavior

Native method profile urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1 SHA256 a886047e50b8a45c3b47addea0f0809dca2a6c54ac35948df5e01893cc30bbf7 is selected. tools.describe reports provisional construction support, not qualification. Its builder identity v2.5.1-rc.2 is distinct from this selected operation binding. There is no supported native results.conjoin. Executive consumption is F_P under its granted relation; any decision must preserve required predicates, applicability, incompatible bases and unresolved contradictions.

Host reads, SHA256 computation and static package checks are declared auxiliary mechanics. They establish byte/structure facts only and never replace required source.read, workspace.observe, work.write, admission or assessment results. All current construction deliverables are written with work.write, own observation and exact preimage; postimage and OperationEvidence are then read. Unknown completion stops dependent writing pending reconciliation.

A failed required operation withholds its dependent claim. Independent work can continue under its existing grant. No automatic retries, authorization renewal or publication follow from successful transport. A missing installation or ambiguous Product is a basis problem, not a request to adopt latest. An unperformed assessment has no core result; performed inconclusive assessment is indeterminate; construction without an output is incomplete for candidate availability.

## Installation and qualification

README supplies a repository-local, single-directory copy recipe and explicit update/removal custody checks. No installer mutates host configuration implicitly. A read-only verifier checks packaged resources and optional observed inventory. It does not assess instruction semantics or host discovery.

Q01-Q12 actual host trials, source-first independent assessment, release and owner acceptance remain unperformed here. The qualification plan keeps each case/lane visible and preserves failures. Static checks support only packaging integrity; they do not justify automatic-selection reliability or efficiency claims.
