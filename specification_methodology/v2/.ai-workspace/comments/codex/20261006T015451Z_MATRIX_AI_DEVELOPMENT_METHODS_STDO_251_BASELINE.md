# MATRIX: AI Development Methods and the STDO 2.5.1 Baseline

**Author**: Codex
**Date**: 2026-10-06T01:54:51Z
**Updated**: 2026-10-06T02:53:07Z
**Status**: Draft evaluation; Product evidence for discussion
**Addresses**: [STDO 3.0 working Product definition](20261006T010215Z_STRATEGY_STDO_3_0_WORKING_PRODUCT_DEFINITION.md)
**Evaluation date**: 2026-10-06

## Summary

Jim has selected an early competitive evaluation of current STDO 2.5.1 to help
define the shape and correctness of STDO 3.0. This post provides a first-pass
feature-by-method grid and proposed decisions and trials derived from it.

The comparison covers 14 current candidates, including STDO, against 30 shared
criteria. It records STDO 3.0 separately as draft target direction. The
[editable workbook](assets/20261006_AI_DEVELOPMENT_METHODS_STDO_251_BASELINE.xlsx) provides the classic grid, criteria, candidate
scopes, an evidence note and source IDs for every cell, a source catalogue, and
14 standards or protocol entries.

Scores assess published method coverage. They do not establish that the method
is correct, that an installed implementation fulfils it, or that it improves
outcomes. Those claims require the trials proposed below.

## Analysis

### Subject and evidence boundaries

The STDO baseline is the locally verified complete **2.5.1 RC2** release:
`stdo://releases/v2.5.1-rc.2/`, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
The corresponding source standards matched that installed cut at inspection.
The authoring Product's operative predecessor remains separately selected by
its Product Definition; the comparison does not change that selection.

External entries use the primary publications and documentation inspected on
2026-10-06. Academic results refer to the authors' declared task, version and
metric scopes. Current documentation URLs are mutable; this first pass is not
an independently reproduced comparison on frozen external installations.

The candidates occupy different scopes. Specification methods are the closest
substitutes for STDO's specification process. Coding harnesses supply practical
execution and attention controls and may implement a method selected above
them. General orchestrators and narrow repair procedures expose useful
computational alternatives. These products can be composed, so a capability
comparison does not assume they are mutually exclusive choices.

### Candidates

| ID | Candidate / publisher | Published scope | Process or mechanism | Reviewed basis |
|---|---|---|---|---|
| ST25 | STDO 2.5.1 RC2 / STDO | General governed product/software construction | Goals → Intent → Product definition → Requirements → Design → Code → Evidence → Gap/reprice | Verified installed RC2 |
| CODEX | Codex workflow / OpenAI | Coding and broader sustained work | Outcome/constraints → durable plan → edit/check/repair → evidence-based continuation | Current long-horizon/Goals guidance |
| CLAUDE | Claude Code workflow / Anthropic | Agent-assisted engineering and general tool work | Explore → plan → implement/verify → commit/PR; fresh SPEC session for large features | Current best-practice guidance |
| GOOGLE | Antigravity 2.0 / Google | Agent-assisted development, research and audit | Explore → implementation plan → approval → execute → verify/iterate | Current 2.0 documentation |
| SPECKIT | GitHub Spec Kit / GitHub / Microsoft | Specification-led engineering; extensible beyond software | Constitution → Specify → Plan → Tasks → Implement → Converge | Current quickstart and workflow reference |
| KIRO | Kiro specs/workflows / Amazon / Kiro | Features, bug fixes and delegated engineering | Requirements/bug analysis → design → tasks → isolated workflow execution/review | Current specs/workflows, October 2026 |
| BMAD | BMad Method / BMad Code | Software ideas, product planning and bounded delivery | Analysis → planning → solutioning → session-sized build/review; short paths supported | Current V6 documentation |
| OPENSPEC | OpenSpec / OPSX / Fission AI | Incremental, brownfield and cross-repository changes | Explore → propose → apply → sync → archive; Verify in expanded profile | Current OPSX; Stores beta |
| QWEN | Qwen Code / Alibaba / Qwen | Coding, research and extensible native work | Define observable Goal → execute turns → completion/blocked claim → verifier decision | Current workflow/Goals documentation |
| BUDDY | CodeBuddy workflows / Tencent | Agent-assisted planning, implementation and review | Clarify → solution → confirm → execute → archive; CLI explore/plan/build/verify | Official Chinese Plan/CLI docs |
| TRAE | TRAE Chinese workflows / TRAE | Coding and reusable task/data-analysis skills | Agent: requirements → PRD/technical solution → code → preview; alternative Plan/Spec/Goal workflows | TraeCode Chinese docs; not merged with international branding |
| METAGPT | MetaGPT / FoundationAgents / research | Structured software development with role handoffs | Requirement → PRD → architecture/interfaces → tasks → code → QA/test feedback | ICLR 2024 method; November 2024 paper revision; stable v0.8 docs and mutable main |
| DEVALL | ChatDev 2.0 / DevAll / OpenBMB / research | Configurable software, charting, research and other workflows | Declared graph → dependency/cycle-aware scheduling → context transfer → node results/evaluation | Current published DevAll; latest release v2.2.0; September 2026 preprint and mutable main docs |
| AGENTLESS | Agentless / OpenAutoCoder / research | Repository issue localization and patch repair | Localize → sample repairs → reproduction/regression filtering → select patch | Public v1.5 and October 2024 paper; later model-specific results |


The direct specification-method comparison includes GitHub/Microsoft Spec Kit,
Amazon Kiro, BMad and OpenSpec. Vendor execution comparisons include OpenAI,
Anthropic, Google, Alibaba/Qwen, Tencent/CodeBuddy and TRAE's Chinese workflows.
MetaGPT and ChatDev/DevAll are research-based multi-agent approaches; Agentless
is a deliberately narrow repository-repair procedure.

### Score interpretation

| Mark | Meaning | Rule |
|---|---|---|
| 3 | Strong explicit coverage | First-class method capability with defined procedures, contracts or documented execution support. |
| 2 | Explicit scoped coverage | Repeatable process or supported configuration, with narrower or optional scope. |
| 1 | Basic coverage | Guidance, convention, limited example or partial implementation. |
| 0 | Not prescribed | Outside or not provided by the inspected published method; not an ecosystem-wide absence claim. |
| U | Insufficient evidence | Reviewed primary sources do not establish the property. |
| T | Draft 3.0 target | Intended capability in the working definition; not an achieved score. |
| ? | Open 3.0 decision | Target capability, boundary or success criterion remains to be defined. |


Optional reviews, controls or profiles receive credit at their documented
scope. A method's instructions and a tool's enforcement remain different
forms of evidence. A release of the tool itself does not prove that its method
qualifies and governs adoption of the products constructed with it.

The feature grid retains the individual ratings. The appended Provisional Tier
List uses an explicitly provisional equal-weight tally. Primary users and
priority weights remain Product decisions, and the methods have materially
different scopes. The Evidence tab records the basis and limitation behind each
ordinal judgment.

### Classic evaluation grid

Columns use the candidate IDs above. ST3 is draft STDO 3.0 target direction.

| Feature | ST25 | CODEX | CLAUDE | GOOGLE | SPECKIT | KIRO | BMAD | OPENSPEC | QWEN | BUDDY | TRAE | METAGPT | DEVALL | AGENTLESS | ST3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 Intent and success criteria | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | T |
| F02 Product definition and scope | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 1 | 0 | T |
| F03 Requirements before construction | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 1 | T |
| F04 Design separated from requirements | 3 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 0 | T |
| F05 Traceability across stages | 3 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | T |
| F06 Domain concepts and identity | 3 | 0 | 0 | U | 1 | 2 | 2 | 2 | U | U | 1 | 1 | 2 | 1 | T |
| F07 Explicit inputs, outputs and contracts | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | T |
| F08 Invariants and semantic constraints | 3 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | T |
| F09 Composition and formal reasoning | 3 | 0 | 0 | 1 | 2 | 2 | 1 | 2 | 1 | U | 1 | 1 | 2 | 0 | T |
| F10 Relevant context selection | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | T |
| F11 Attention fit and proportionality | 3 | 2 | 3 | 2 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | T |
| F12 Bounded probabilistic construction | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | T |
| F13 Decomposition and recursive workflows | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | T |
| F14 Durable state and resumption | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 1 | T |
| F15 Observation and next-action feedback | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | T |
| F16 Uncertainty, stops and re-entry | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | T |
| F17 Permissions and effect boundaries | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 1 | 3 | 3 | 2 | 1 | 2 | 1 | T |
| F18 Independent assessment | 3 | 2 | 2 | 2 | 3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | ? |
| F19 Operational and negative tests | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | ? |
| F20 Claim and evidence separation | 3 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | T |
| F21 Provenance and auditability | 3 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | T |
| F22 Change impact and specification revision | 3 | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 1 | 1 | 1 | U | U | 0 | T |
| F23 Versioned release and adoption | 3 | 0 | 0 | U | 2 | U | U | 1 | U | U | U | U | U | 0 | ? |
| F24 Reuse and extensibility | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | T |
| F25 Process use beyond software | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 0 | ? |
| F26 Self-application | 2 | 1 | 1 | U | 3 | 1 | U | 3 | U | U | U | U | U | U | T |
| F27 AI-native method representation | 1 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 1 | 2 | 1 | T |
| F28 Onboarding and reader guidance | 1 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | ? |
| F29 Evidence of effectiveness | 1 | 1 | 1 | U | 1 | 1 | 1 | 1 | U | U | U | 2 | 2 | 2 | ? |
| F30 Work and resource measurement | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 3 | 1 | U | 3 | 3 | 3 | ? |


### Evaluation criteria


| ID | Group | Criterion |
|---|---|---|
| F01 | Purpose and specification | The process establishes a desired outcome and observable success conditions. |
| F02 | Purpose and specification | The process records capabilities, users, boundaries and exclusions beyond a task prompt. |
| F03 | Purpose and specification | Requirements or a specification guide construction and can be clarified before implementation. |
| F04 | Purpose and specification | Structural design and implementation choices are distinguished from required outcomes. |
| F05 | Purpose and specification | Requirements, design decisions, tasks, results and checks have recoverable connections. |
| F06 | Meaning and contracts | The method defines contextual concepts, identity and ownership of meaning. |
| F07 | Meaning and contracts | Bounded work has declared inputs, prerequisites, outputs and acceptance or result contracts. |
| F08 | Meaning and contracts | The process states conditions that a valid construction must preserve. |
| F09 | Meaning and contracts | Operations have explicit compatibility, composition or derivation laws beyond task sequencing. |
| F10 | Bounded computation | The process selects task-relevant sources and dependencies instead of relying on ambient memory. |
| F11 | Bounded computation | Work is sized to actor/context capacity and additional process is justified by its benefit. |
| F12 | Bounded computation | AI reasoning operates within a defined task or traversal with explicit scope and results. |
| F13 | Bounded computation | Larger work can be refined, delegated, branched and composed through bounded subtasks. |
| F14 | Bounded computation | Work, decisions and progress can survive a session or actor change. |
| F15 | Bounded computation | Observed results or gaps drive an explicit next action rather than blind repetition. |
| F16 | Bounded computation | Ambiguity, insufficient evidence, blockers, partial progress and upstream revision have explicit treatment. |
| F17 | Evaluation and control | Actions, tools and side effects are limited by declared authority or enforceable permissions. |
| F18 | Evaluation and control | The process provides assessment with meaningful separation from construction. |
| F19 | Evaluation and control | Checks address actual behavior, material failure cases and end-to-end outcomes where applicable. |
| F20 | Evaluation and control | Structural validity, observed behavior, semantic satisfaction and acceptance are distinguished. |
| F21 | Evaluation and control | Results and judgments retain their subject, basis, origin and supporting observations. |
| F22 | Evaluation and control | Changed intent, requirements or evidence revise affected work while retaining valid unaffected results. |
| F23 | Lifecycle and use | The method governs release identity, qualification and explicit adoption of a changed basis. |
| F24 | Lifecycle and use | Reusable operations, skills, roles or workflows can be adapted across projects and implementations. |
| F25 | Lifecycle and use | The published process is applicable to non-coding work, not merely developing an AI model. |
| F26 | Lifecycle and use | The method is used to define, develop or improve itself; internal tool use alone is weaker evidence. |
| F27 | Lifecycle and use | An agent can acquire structured method context with stable source routes and targeted retrieval. |
| F28 | Lifecycle and use | Readers receive clear entry points, task guidance and worked examples. |
| F29 | Lifecycle and use | Published observations or evaluations support the process, with the measured scope stated. |
| F30 | Lifecycle and use | The process exposes work, token/time costs or budgets relevant to its claims. |


### Findings that inform the 3.0 Product

These are analyst inferences from the declared coverage and inspected evidence,
not findings from a common operational experiment.

**Preserve explicit meaning and justification.** STDO gives unusually explicit
ownership to contextual identity, invariants, typed composition, claim scope,
evidence and acceptance. These are candidate strengths in F06-F09 and F20-F23.
The 3.0 structure should make them easier to acquire and apply while preserving
their material distinctions. The verified baseline supplies the clauses; an
improved layout still needs semantic-fidelity assessment.

**Improve the route from theory to useful work.** Practical competitors provide
short entry routes, persistent specifications or plans, isolated working
contexts, feedback loops and ordinary worked examples. Relevant starting points
include [Claude Code guidance](https://code.claude.com/docs/en/best-practices),
[BMad project context](https://docs.bmad-method.org/existing-codebases/set-and-maintain-project-context/)
and [Kiro workflows](https://kiro.dev/docs/workflows/). STDO's reader route and
partial current a_c.STDO representation remain weaker evidence in F27-F28.
Reducing reconstruction cost is a measurable Product aim.

**Self-application needs a stronger claim than self-use.**
[Spec Kit documents its own specification-led development](https://github.github.com/spec-kit/guides/agentic-sdlc.html),
and [OpenSpec identifies its own live specs and changes](https://github.com/Fission-AI/OpenSpec).
STDO's use of a released predecessor to develop a successor provides a lawful
recursive relation. The distinguishing 3.0 claim should concern coherent
self-definition, preserved governing meaning and demonstrated usefulness under
finite attention. Self-application alone does not establish an advantage.

**Make bounded computation explicit in the native representation.** The method
needs a recoverable account of context selection, capacity fit, candidate
construction, observation, gap evaluation, next action, stopping and re-entry.
The current working post identifies source meaning that required fuller
reconstruction than the current a_c view supplied. A 3.0 representation should
be judged on successful fresh-context recovery and application of that meaning.
Execution platforms can provide policies and persistence through explicit
bindings; the generic calculus retains its own semantic obligations.

**Test the evaluator as well as the constructor.** In the
[Agentless paper](https://arxiv.org/html/2407.01489), generated tests reproduced
213 of 300 original issues, but only 94 recognised resolution when the benchmark's
ground-truth patches were applied. This is scoped experimental evidence, not a
statement about every testing method. It demonstrates why producing a failing
test is insufficient evidence of a correct acceptance oracle. STDO's existing
claim/evidence distinction should become visible in its worked examples and
conformance trials.

**Introduce shared effectiveness evidence.** Current sources demonstrate
documented procedures, internal adoption and scoped research results. They do
not establish a common whole-method winner. F29-F30 should drive STDO's
qualification claims: what task was completed, which material errors were
detected, what the actor needed, and what time, compute and human attention the
result cost. More documents or more context do not themselves prove improvement.

**Remove redundant reconstruction and unjustified ceremony.** Apply the
existing proportionality principle to the method itself. Retain a distinction
when it resolves a material ambiguity, preserves a necessary relation or enables
a sufficient bounded computation. The feature grid does not justify copying
every competitor feature or adding a universal runtime architecture.

### Proposed common trials

These trials are proposed Product-evaluation work. No trials have been run as
part of this comparison, and numeric thresholds remain open.

| Trial | Shared task | Observable result |
|---|---|---|
| Fresh-context recovery | A new actor recovers and applies the bounded computational model from the published method. | Material definitions, dependencies and stopping conditions recovered correctly; context and interpretation cost recorded. |
| Context cap and decomposition | The full required source basis exceeds one actor's declared context cap, while sufficient local frames can fit; repeat with tighter caps and a coupled case that cannot fit. | Bounded refinement preserves the complete outer contract under independent assessment; insufficient capacity produces an explicit limit or lawful escalation. |
| Intent to usable result | Construct a small useful feature from an incomplete but sufficient intent, with a material ambiguity. | Ambiguity is resolved or kept explicit; the installed result satisfies independently owned acceptance conditions. |
| Composition conservation | Combine two individually valid bounded transformations under a governing outer contract. | The actual composition preserves all required inputs, constraints, judgments and evidence; incompatible composition is refused. |
| Failure and missing assessment | Supply one observed failure plus one required obligation with no assessment. | The result retains both states and cannot report complete success or erase the unassessed obligation. |
| Compaction and actor change | Pause after partial progress, clear context and resume with a new actor. | Valid progress and basis are recovered; unsupported completion claims and unnecessary restarts are detected. |
| Changed governing requirement | Revise one requirement after partial construction with unaffected work present. | Affected claims are reopened; valid unaffected results are reused with explicit dependencies. |
| Defective acceptance oracle | Give a candidate that passes structural checks or an incomplete test but violates required behaviour. | Assessment detects the material defect or reports its evidential limit; structural green does not become semantic acceptance. |
| Broader process use | Produce and revise a sourced decision analysis containing uncertainty and stale evidence. | Facts, assumptions, judgments and authority remain distinct; the result can be independently assessed and revised. |


Compare STDO 2.5.1, selected competitor procedures and the eventual 3.0 candidate
on the same tasks with declared models, tools, source cuts and budgets. Include
a simple plan/build/review baseline. Repeat probabilistic trials and vary task
order. Keep acceptance criteria independent of the constructing actor and,
where practicable, keep assessors unaware of the candidate method.

Declare a per-actor context cap and total-work budget before each trial. Include
a required source basis larger than that cap and vary caps across repeats.
Count transferred context and resource use across every delegated actor, not
only the coordinator. Context size is a measurable constraint; it is only a
proxy for attention capacity. Vary the complexity of relationships that must
be considered together and judge the complete outer result independently.
Record task applicability before comparison: Agentless's repair claims, for
example, are assessed on repair tasks.

Record semantic satisfaction, material errors missed or caught, provenance
accuracy, permitted effects, successful resumption and preserved obligations.
Also record human interventions, source rereads, transferred context, elapsed
time, tokens/compute, measured cost and unnecessary reconstruction. These
measures test different claims and should remain separate before Product
priorities justify any combined score.

### Standards and the evolving landscape

The inspected landscape has mature lifecycle and assurance references and
evolving agent interoperability work. It does not establish one consolidated,
widely adopted standard for the complete AI-driven specification-to-realisation
method that STDO proposes.

Lifecycle standards govern processes and obligations. Risk frameworks provide
governance overlays. Protocols govern communication and tool access. Research
frameworks propose mechanisms and publish task-scoped results. Each can inform
or support a methodology without supplying the whole methodology.

| Reference | Kind and status | Actual scope | Relationship to STDO |
|---|---|---|---|
| [ISO/IEC/IEEE 12207:2026](https://www.iso.org/standard/90219.html) | Software lifecycle process standard; Published April 2026; 2017 withdrawn | Software lifecycle processes; does not prescribe a methodology. | AI-assisted software can use the lifecycle framework. |
| [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html) | System lifecycle process standard; Published May 2023 | Stakeholders and system lifecycle processes. | Broader systems reference; not an agent execution method. |
| [ISO/IEC 5338:2023](https://www.iso.org/standard/81118.html) | AI system lifecycle standard; Published December 2023 | AI-system lifecycle definition, control, management, execution and improvement; usable in development/acquisition. | Building AI systems differs from using agents to build arbitrary products. |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) | AI management system requirements; Published December 2023 | Organisational governance of developing, providing or using AI. | Applies to AI use governance; not specification-to-code instructions. |
| [NIST AI RMF 1.0 / AI 100-1](https://www.nist.gov/itl/ai-risk-management-framework) | Voluntary risk framework; January 2023; revision underway | Govern, Map, Measure and Manage AI risks. | Governance overlay for building and using AI. |
| [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Generative AI risk profile; July 2024 | Generative-AI profile of AI RMF. | Risk overlay, not a complete development methodology. |
| [NIST SSDF v1.1 / SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) | Secure software process framework; Final February 2022 | Secure development practices integrated into an SDLC. | Current final assurance reference for AI-produced software. |
| [NIST SSDF v1.2 / SP 800-218 Rev. 1](https://csrc.nist.gov/pubs/sp/800/218/r1/ipd) | Secure software process draft; Initial public draft December 2025 | Proposed revision of secure software development practices. | Evolving draft; do not treat as the final published framework. |
| [NIST SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final) | AI development SSDF profile; Final July 2024 | AI model/system producers and acquirers. | Primarily building/acquiring AI, not generic AI-assisted construction. |
| [MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) | Tool/data interoperability protocol; Released July 2026 | Stateless protocol core, schemas and optional extensions. | A potential adapter; does not define product acceptance. |
| [A2A v1.0.1](https://a2a-protocol.org/v1.0.1/specification/) | Agent interoperability protocol; Current stable; May 2026 release | Discovery, delegation, task states, messages and artifacts. | Task completion is not independent product qualification. |
| [AGENTS.md](https://agents.md/) | Open repository instruction convention; Current open convention; no mandatory fields | Repository and scoped instructions for coding agents. | Attention/distribution surface, not a typed lifecycle methodology. |
| [NIST AI Agent Standards Initiative](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative) | Standards programme; Launched February 2026 | Protocols, identity/authentication and evaluation research. | Evolving initiative, not a completed universal methodology. |
| [AAIF](https://aaif.io/blog/a2a-joins-aaif) | Open-source standards governance foundation; A2A joined August 2026 | Hosts distinct agent instructions, runtimes and interoperability projects. | Governance home; no single consolidated development method. |


[ISO/IEC/IEEE 12207:2026](https://www.iso.org/standard/90219.html) expressly leaves
methodology selection open. The
[NIST AI Agent Standards Initiative](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative)
addresses industry standardisation, interoperability, identity and evaluation.
Neither establishes that a protocol-compliant agent has satisfied a Product's
semantic acceptance conditions.

Related broader-process publications that merit a later scoped comparison
include [Anthropic's effective-agent patterns](https://www.anthropic.com/engineering/building-effective-agents)
and [OpenAI's agent improvement loop](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop).
Their recipes are distinct from the coding workflows scored here.

### Sources and limitations

The workbook uses these IDs to attach primary-source routes to every cell.
STDO source links below resolve to the inspected workspace copies of the
verified RC2 documents; the immutable release identity above fixes the subject.

| ID | Publisher | Primary source / route | Evidence scope |
|---|---|---|---|
| SS | STDO | [SPEC_METHOD](../../../specification/standards/SPEC_METHOD.md) | Locally verified complete STDO 2.5.1 RC2; manifest 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782 |
| SD | STDO | [DESIGN_MODULE_METHOD](../../../specification/standards/DESIGN_MODULE_METHOD.md) | Locally verified complete STDO 2.5.1 RC2; manifest 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782 |
| SF | STDO | [REFERENCE_FRAME_METHOD](../../../specification/standards/REFERENCE_FRAME_METHOD.md) | Locally verified complete STDO 2.5.1 RC2; manifest 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782 |
| SA | STDO | [AXIOMATIC_CALCULUS](../../../specification/standards/AXIOMATIC_CALCULUS.md) | Locally verified complete STDO 2.5.1 RC2; manifest 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782 |
| SB | STDO | [STDO_REFERENCE_FRAME_BASELINE](../../../specification/standards/STDO_REFERENCE_FRAME_BASELINE.md) | Locally verified complete STDO 2.5.1 RC2; manifest 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782 |
| ST | STDO | [TICKET_METHOD](../../../specification/standards/TICKET_METHOD.md) | Locally verified complete STDO 2.5.1 RC2; manifest 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782 |
| SR | STDO | [RELEASE_METHOD](../../../specification/standards/RELEASE_METHOD.md) | Locally verified complete STDO 2.5.1 RC2; manifest 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782 |
| SW | STDO | [WRITING_GUIDE](../../../specification/standards/WRITING_GUIDE.md) | Locally verified complete STDO 2.5.1 RC2; manifest 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782 |
| SM | STDO Representation | [a_c.STDO RC2 program](../../../../stdo_representation/build_tenants/axiom_indexer/representation/stdo-v2.5.1-rc.2/axiomatic-program.json) | Inspected source program: 31 symbols, 116 clauses, 13 residuals, 6 frame indexes |
| SQ | STDO source project | [Current Goals and retained native outcomes](../../../specification/GOALS.md) | Workspace record read 2026-10-06; bounded qualification records, not an independent rerun |
| S3 | Jim / STDO | [STDO 3.0 working Product definition](20261006T010215Z_STRATEGY_STDO_3_0_WORKING_PRODUCT_DEFINITION.md) | Draft target; includes Codex structure proposal for discussion |
| O1 | OpenAI | [Long-horizon Codex work](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex) | Current documentation, accessed 2026-10-06 |
| O2 | OpenAI | [Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) | Current documentation, accessed 2026-10-06 |
| O3 | OpenAI | [AGENTS.md instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Current documentation, accessed 2026-10-06 |
| O4 | OpenAI | [Code review](https://learn.chatgpt.com/docs/code-review) | Current documentation, accessed 2026-10-06 |
| O5 | OpenAI | [Approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security) | Current documentation, accessed 2026-10-06 |
| A1 | Anthropic | [Claude Code best practices](https://code.claude.com/docs/en/best-practices) | Current documentation, accessed 2026-10-06 |
| A2 | Anthropic | [Claude Code execution loop](https://code.claude.com/docs/en/how-claude-code-works) | Current documentation, accessed 2026-10-06 |
| A3 | Anthropic | [Project memory](https://code.claude.com/docs/en/memory) | Current documentation, accessed 2026-10-06 |
| A4 | Anthropic | [Permissions](https://code.claude.com/docs/en/permissions) | Current documentation, accessed 2026-10-06 |
| A5 | Anthropic | [Custom subagents](https://code.claude.com/docs/en/sub-agents) | Current documentation, accessed 2026-10-06 |
| G1 | Google | [Antigravity CLI practices](https://antigravity.google/docs/cli/best-practices/) | Current documentation, accessed 2026-10-06 |
| G2 | Google | [Artifact review](https://antigravity.google/docs/artifact-review) | Current documentation, accessed 2026-10-06 |
| G3 | Google | [Custom subagents](https://antigravity.google/docs/subagents/) | Current documentation, accessed 2026-10-06 |
| G4 | Google | [Agent settings](https://antigravity.google/docs/agent-settings) | Current documentation, accessed 2026-10-06 |
| K1 | GitHub / Microsoft | [Spec Kit quickstart](https://github.github.com/spec-kit/quickstart.html) | Current documentation, accessed 2026-10-06 |
| K2 | GitHub / Microsoft | [Workflow reference](https://github.github.com/spec-kit/reference/workflows.html) | Current documentation, accessed 2026-10-06 |
| K3 | GitHub / Microsoft | [Spec Kit develops Spec Kit](https://github.github.com/spec-kit/guides/agentic-sdlc.html) | Current documentation, accessed 2026-10-06 |
| K4 | GitHub / Microsoft | [Spec Kit overview](https://github.github.com/spec-kit/) | Current documentation, accessed 2026-10-06 |
| I1 | Amazon / Kiro | [Specs](https://kiro.dev/docs/specs/) | Current documentation, accessed 2026-10-06 |
| I2 | Amazon / Kiro | [Workflows](https://kiro.dev/docs/workflows/) | Current documentation, accessed 2026-10-06 |
| I3 | Amazon / Kiro | [Workflow authoring](https://kiro.dev/docs/workflows/authoring/) | Current documentation, accessed 2026-10-06 |
| B1 | BMad Code | [Requirements and specification](https://docs.bmad-method.org/plan/define-requirements-and-a-specification/) | Current documentation, accessed 2026-10-06 |
| B2 | BMad Code | [Independent code review and triage](https://docs.bmad-method.org/build/review-a-change/) | Current documentation, accessed 2026-10-06 |
| B3 | BMad Code | [Project context](https://docs.bmad-method.org/existing-codebases/set-and-maintain-project-context/) | Current documentation, accessed 2026-10-06 |
| B4 | BMad Code | [Autonomous development loops](https://docs.bmad-method.org/build/autonomous-development-loops/) | Current documentation, accessed 2026-10-06 |
| B5 | BMad Code | [Workflow map](https://docs.bmad-method.org/workflow-map-diagram.html) | Current documentation, accessed 2026-10-06 |
| P1 | Fission AI | [OpenSpec overview](https://openspec.dev/) | Current documentation, accessed 2026-10-06 |
| P2 | Fission AI | [OpenSpec README and self-use](https://github.com/Fission-AI/OpenSpec) | Current documentation, accessed 2026-10-06 |
| P3 | Fission AI | [OPSX artifact-guided workflow](https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/opsx.md) | Current documentation, accessed 2026-10-06 |
| P4 | Fission AI | [Workflow modes and artifact lifecycle](https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/workflows.md) | Current documentation, accessed 2026-10-06 |
| Q1 | Alibaba / Qwen | [Common workflows](https://qwenlm.github.io/qwen-code-docs/en/users/common-workflow/) | Current documentation, accessed 2026-10-06 |
| Q2 | Alibaba / Qwen | [Goals and transcript verifier](https://qwenlm.github.io/qwen-code-docs/en/users/features/goals/) | Current documentation, accessed 2026-10-06 |
| Q3 | Alibaba / Qwen | [Subagents](https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/) | Current documentation, accessed 2026-10-06 |
| Q4 | Alibaba / Qwen | [Approval modes](https://qwenlm.github.io/qwen-code-docs/en/users/features/approval-mode/) | Current documentation, accessed 2026-10-06 |
| C1 | Tencent | [CodeBuddy Plan Mode](https://www.codebuddy.cn/docs/ide/Features/Plan-Mode) | Current documentation, accessed 2026-10-06 |
| C2 | Tencent | [CodeBuddy CLI practices](https://www.codebuddy.cn/docs/cli/best-practices) | Current documentation, accessed 2026-10-06 |
| T1 | TRAE | [Chinese Plan, Spec and Goal workflows](https://docs.trae.cn/ide_built-in-workflows) | Current documentation, accessed 2026-10-06 |
| T2 | TRAE | [Built-in agent](https://docs.trae.cn/ide_built-in-agent) | Current documentation, accessed 2026-10-06 |
| T3 | TRAE | [Skills](https://docs.trae.cn/ide_skills) | Current documentation, accessed 2026-10-06 |
| T4 | TRAE | [Code review](https://docs.trae.cn/ide_agent-powered-code-review) | Current documentation, accessed 2026-10-06 |
| M1 | MetaGPT researchers | [MetaGPT paper](https://arxiv.org/html/2308.00352) | November 2024 paper revision; evaluated task scopes, not a whole-lifecycle qualification |
| M2 | FoundationAgents | [MetaGPT repository](https://github.com/FoundationAgents/MetaGPT) | Current documentation, accessed 2026-10-06 |
| M3 | MetaGPT | [Multi-agent tutorial](https://docs.deepwisdom.ai/main/en/guide/tutorials/multi_agent_101.html) | Current documentation, accessed 2026-10-06 |
| M4 | MetaGPT | [Breakpoint recovery](https://docs.deepwisdom.ai/main/en/guide/in_depth_guides/breakpoint_recovery.html) | Current documentation, accessed 2026-10-06 |
| D1 | OpenBMB researchers | [ChatDev 2.0 / DevAll paper](https://arxiv.org/html/2609.00714) | September 2026 preprint; author-reported workflow metrics |
| D2 | OpenBMB | [DevAll release v2.2.0](https://github.com/OpenBMB/ChatDev/releases/tag/v2.2.0) | Current documentation, accessed 2026-10-06 |
| D3 | OpenBMB | [Workflow authoring](https://github.com/OpenBMB/ChatDev/blob/main/docs/user_guide/en/workflow_authoring.md) | Current documentation, accessed 2026-10-06 |
| D4 | OpenBMB | [Memory modules](https://github.com/OpenBMB/ChatDev/blob/main/docs/user_guide/en/modules/memory.md) | Current documentation, accessed 2026-10-06 |
| L1 | Agentless researchers | [Agentless paper](https://arxiv.org/html/2407.01489) | October 2024 paper revision; bounded issue-repair results and costs |
| L2 | OpenAutoCoder | [Agentless repository](https://github.com/OpenAutoCoder/Agentless) | Current documentation, accessed 2026-10-06 |



- First-pass analyst assessment of documented method coverage as of 2026-10-06. Scores are editable and require further task-level validation.
- A score does not certify semantic correctness, effectiveness, safety or operational qualification. Evidence of effectiveness has its own criterion.
- Columns compare stated method scopes, not every possible capability of a provider ecosystem. Configurable review or checks are not automatically mandatory.
- STDO 2.5.1 scores concern the verified RC2 documents. Consumer-owned runtimes and the partial a_c.text representation are distinguished from method law.
- STDO 3.0 remains draft target direction. Its T/? entries do not enter numeric comparisons.
- The appended tier list is a provisional equal-weight summary of documented coverage. Product priority weights are not selected and method scopes differ. Agentless is a repair procedure, DevAll a general orchestrator.
- Academic benchmark results use different tasks, models, versions and metrics. They are not a common head-to-head experiment.
- OpenAI ExecPlans is archived. Anthropic earlier sprint-contract harness is not current universal best practice.
- Spec Kit quickstart includes Converge although an illustrative workflow example still ends at Implement.
- Qwen approval defaults conflict across its page; only available modes are credited. Its Goal verifier checks transcript evidence, not live files.
- CodeBuddy Dynamic Workflows claims were not scored because source retrieval failed. TRAE Chinese workflows are not conflated with international branding.
- ISO scope comes from public catalogue abstracts, not a paid clause-by-clause audit. Formal standards and protocols are listed separately.
- Bounded independent audits corrected vendor and academic cells against the same criteria; optional patterns and unestablished release/revision claims were narrowed.


## Recommended Action

Use this baseline as Product evidence while developing the 3.0 working
definition. Refine the target users, material capabilities and success criteria
against the grid and the shared trials. Preserve the distinction between
documented method coverage, semantic fidelity and demonstrated operational
benefit. The proposed document structure should follow those decisions through
Intent, Product, Specification and Realisation.

## Provisional Tier List

Using **equal weight across all 30 criteria**, this is the provisional tier list
for **documented methodological coverage**. Numeric scores are summed against
90 available points. The bands are analyst choices for a rough grouping; they
are not empirically calibrated quality levels.

| Tier | Points out of 90 | Products and scores |
|---|---:|---|
| **S** | 80–90 | **STDO 2.5.1 RC2 — 80** |
| **A** | 70–79 | **GitHub Spec Kit — 76**, **Kiro — 74**, **BMad — 72** |
| **B** | 60–69 | **OpenSpec — 69**, **Claude Code — 64**, **Qwen Code — 63**, **MetaGPT — 63**, **Codex — 62**, **ChatDev/DevAll — 62**, **CodeBuddy — 61** |
| **C** | 50–59 | **TRAE — 57**, **Google Antigravity — 56** |
| **D** | Below 50 | **Agentless — 46** |

Unknown cells currently earn no documented points. Additional evidence could
lift Qwen, MetaGPT, DevAll and CodeBuddy into A, and TRAE or Antigravity into B.
Agentless's narrow repair scope explains much of its lower placement.

**STDO earns S through its explicit treatment of meaning, contracts,
composition, evidence, authority and lifecycle.** The criteria favour a
comprehensive methodology, and these scores assess published coverage.

Its practical delivery is considerably weaker. Across **native representation,
onboarding, effectiveness evidence and resource measurement** (F27–F30), STDO
scores **4/12**, compared with **Spec Kit's 8/12** and **Kiro's 9/12**.

That gives 3.0 a clear direction: **preserve the methodological depth, improve
acquisition and application, and demonstrate useful results under finite
attention.** Its effectiveness ranking remains open until shared trials are
run. STDO 3.0 itself remains an unranked target.
