# MATRIX: AI methods and frameworks alongside STDO v3 — second evaluation

**Author:** Codex, bounded commentary Writer; delegated source research and an independent rating-consistency review.
**Date:** 2026-10-12T03:32:07Z
**Addresses:** Jim; STDO v3 common Product owner; Claude and Codex construction tenants.
**Status:** Open. Research and recommendations; no amendment, acceptance, adoption or release decision.
**Scope:** 18 entries × 26 criteria, 468 rated cells and 160 source records. Source access date: 2026-10-12.

## Summary

The v2 comparison already exists: [6 October matrix](../../../../v2/.ai-workspace/comments/codex/20261006T015451Z_MATRIX_AI_DEVELOPMENT_METHODS_STDO_251_BASELINE.md), with [its workbook](../../../../v2/.ai-workspace/comments/codex/assets/20261006_AI_DEVELOPMENT_METHODS_STDO_251_BASELINE.xlsx). It covered 14 candidates and 30 features. This second evaluation preserves that historical post and revises the question for independently developed STDO v3.

The useful comparison is between explicit governing obligations, supported execution mechanisms and measured outcomes. STDO describes many of the first; SDKs and coding tools provide much of the second. Neither establishes the third by being available. These products can be composed. A semantic method score and a runtime mechanism score are deliberately labelled differently.

The revised comparison includes OpenAI Codex and Agents SDK, Anthropic Claude Code and Agent SDK, Google Gemini CLI and ADK, GitHub Spec Kit, BMad, OpenSpec, Qwen Code, OpenHands, LangGraph, Microsoft Agent Framework, CrewAI and Pydantic AI. Installed STDO 2.5.1-rc.2 and each pinned v3 tenant candidate have separate rows. It makes no global winner or effectiveness ranking.

The [editable workbook](assets/20261012_STDO_V3_AI_FRAMEWORK_EVALUATION.xlsx) contains the five grids, criteria, all cell reasons, source locators and candidate scope. Its grid cells reference the Evidence sheet; changing a rating there updates the displayed grid. The same records are available as [JSON](assets/20261012_STDO_V3_AI_FRAMEWORK_EVALUATION.json) and [CSV](assets/20261012_STDO_V3_AI_FRAMEWORK_EVALUATION.csv). Unknowns remain unknown throughout.

## Analysis

### 1. What changed from the first evaluation

| First-round issue | Second-round treatment |
| --- | --- |
| Different product classes shared one equal-weight total and tier | Compare within declared purpose; show five criterion groups without a sum or tier. |
| A vendor name could blur coding tool, SDK and hosted service | Separate Codex/Agents SDK, Claude Code/Agent SDK and Gemini CLI/ADK; exclude ecosystem unions. |
| One number could mean instruction, supported API or observed behavior | Attach an evidence-form suffix and retain exact cell rationale and source. |
| Broad features hid consequential failure distinctions | Test lost effects, basis changes, failure-plus-missing-coverage joins, source trust and resource-limit enforcement. |
| Reviewer roles and tests could receive strong assurance credit | Distinguish fresh review, claim-relative independence, independent expectations and faulty-oracle controls. |
| F27–F30 mixed representation, onboarding, effectiveness and cost | Keep reusable context, ordinary entry, observed adequate outcomes, complete resource accounting and self-qualification separate. |
| STDO v3 appeared as target checkmarks | Rate each named candidate's documented relations and scoped evidence; no release or whole-method qualification is credited. |
| Self-use could stand in for method qualification | Fresh actors, independently derived expectations and defective-guidance controls are a stronger, separate test. |

The new criteria map to the old F01–F30 below. Old F25, use beyond software, becomes a scope attribute rather than a universal bonus: broader scope can add obligations and does not imply better performance. F11's proportionality is retained as a lens over C01, C08, C22 and C23: what purpose is served, what context fits, what total work costs and what adequate outcome is actually achieved. Artifact count, actor count and document brevity are inadequate substitutes. C25 and C26 add operational questions that the old grid did not isolate.

This is a refreshed selection, not a complete re-rating of all old entries. Kiro, Antigravity, CodeBuddy, TRAE, MetaGPT, ChatDev/DevAll and Agentless remain in the historical comparison and are not newly scored. Their omission asserts no regression or retirement. Google is examined here through its public CLI and ADK; SDK/runtime coverage is expanded substantially.

### 2. Shared foundations of the two v3 developments

The shared input is [Working Common Principles](../../../specification/requirements/PRINCIPLES.md), read at common commit `b83ed1cc0b65842874bb3d7cabcb76492a4c0d48`. It records the two C1 attempts as separately accepted, with a synthesis retained as commentary. It explicitly does not make their merged wording STDO v3 law.

| Foundation | Bounded meaning for this evaluation | Criteria it motivates |
| --- | --- | --- |
| Interpretation | A subject, its encoding and the meaning available under a declared context are distinct. Parsing does not establish fidelity. | C03, C07, C15, C20, C24 |
| Purpose and adequacy | The owner selects the observable adequate outcome and reserved value choices. Interfaces and method burden need a material requiring relation. | C01, C02, C08, C22, C23 |
| Identity and state | Stable identity, current contents, historical observations and representation identity remain distinct through admissible change. | C03, C05, C10, C17 |
| Compatible composition and conditional conservation | Joins need compatible contracts and must retain the selected outer obligations, known failures, missing required coverage and authority. | C04, C09, C12 |
| Finite actors and truthful handling | Context, time and capability are bounded. Missing capacity or evidence needs an honest result and a permitted next action. | C07–C11, C22, C26 |
| Justification and separate authority | Evidence supports an exact claim; an owner grant permits an effect or acceptance. Neither supplies the other. | C13–C18, C24, C25 |

Both developments concern a finite actor realizing a selected outer contract through bounded work. Finite capacity alone supplies neither that purpose nor an identity, compatibility relation or authority grant. Conservation also needs the selected contract and faithful refinement; the common C1 disposition records that agreement. Universal algorithmic meaning, categorical equivalence and stronger Markov claims remain open claims, with domains and falsifiers to supply. They earn no feature credit here.

This foundation summary defines the evaluation perspective. It does not select either tenant's ontology, mandate its implementation or amend common Product meaning.

### 3. Subjects, version basis and evidence standing

The operative builder/predecessor is installed `v2.5.1-rc.2`, selected by the [v3 Product Definition](../../../stdo_3.json). Its manifest is `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`; native definition/basis verification returned no failures. Installed source, common WHAT and candidate HOW remain distinct.

| STDO row | Exact subject | Standing at this assessment |
| --- | --- | --- |
| ST25 | Installed `v2.5.1-rc.2`, manifest above | Immutable predecessor/builder method; method obligations are not runtime enforcement. |
| ST3C | Claude tenant commit `e1bcd802f2ebf3b695ef5f6e94780d3f00f29d0d` | Member-by-member successor construction. Four F-01 cold task starts have input/usage provenance; the runner did not assess their outputs. |
| ST3X | Codex tenant commit `427a0deb39b7cd8e298b3b2ebc126c052f056d8a` | Standalone successor restatement under construction. Named local source-first/fresh-use reviews cover bounded subjects; selected later repairs still need independent confirmation. |

These are assessment pins, not assertions that either active branch has stopped. Tenant content was read through named Git objects, not the peer's working tree. Historical reviews preserved inside those objects retain their original subjects; a current file location cannot upgrade an older verdict. In particular, Codex's fidelity review assesses `b0ec615c9ebe8da80e9852df3968233155a432b7`, not the repaired seams of `427a0de`.

For external products, a published runtime score means the publisher documents the mechanism, not that this survey installed or executed it. BMad is pinned to v6.12.2 (tag object `0187f4a9437fc42450dc84c59e7be367ed38be22`, commit `10db8f35bba515e4fbf0388c5bd59a6cc7a3e9c8`); V7 preview, TEA, Loop and other modules are excluded. Other external rows use rolling documentation accessed on the evaluation date, with feature/language/version qualifications retained in the ledger. [BMad tagged source](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/v6.12.2/README.md)

| ID | Entry | Class | Selected scope / version qualification |
| --- | --- | --- | --- |
| ST25 | STDO 2.5.1-rc.2 | Method | Installed immutable method and standards; optional profiles only when selected. Does not include every tenant implementation. v2.5.1-rc.2; manifest 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782 |
| ST3C | STDO v3 — Claude candidate | Method candidate | Pinned member-by-member candidate standards and named local qualification artifacts; not common v3 law or an adopted release. e1bcd802f2ebf3b695ef5f6e94780d3f00f29d0d |
| ST3X | STDO v3 — Codex candidate | Method candidate | Pinned standalone successor restatement, selected source-linked projections and local C3 reviews; no released or accepted v3 product. 427a0deb39b7cd8e298b3b2ebc126c052f056d8a |
| SPECKIT | GitHub Spec Kit | Specification method + workflow | Core SDD commands and documented native workflow engine; external coding-agent enforcement and community extensions excluded. Rolling main-branch documentation and command templates accessed 2026-10-12; no installed version or runtime trial. |
| BMAD | BMad Method v6.12.2 | Specification method | Core BMad Method and built-in QA at v6.12.2. Separate TEA, Loop, Builder and V7-preview capabilities excluded. Actual v6.12.2-tagged primary documentation read; annotated tag 0187f4a9437fc42450dc84c59e7be367ed38be22 resolves to commit 10db8f35bba515e4fbf0388c5bd59a6cc7a3e9c8. No installed/runtime validation. |
| OPENSPEC | Fission AI OpenSpec | Specification method + CLI | Native OPSX spec-driven workflow, CLI and supported customization; optional expanded verification distinguished from default core profile. Rolling main documentation accessed 2026-10-12; no installed package pin or runtime trial. |
| CODEX | OpenAI Codex | Coding tool | Published Codex coding workflow and local CLI/app-server harness, including a named repair example. Excludes Agents SDK orchestration, Codex Security, hosted Agents API and model benchmark claims. Rolling official documentation accessed 2026-10-12; no installed/runtime version qualification. Repair recipe pins its own example CLI version. |
| CLAUDE | Anthropic Claude Code | Coding tool | Published Claude Code coding workflow and harness, including native subagents, permissions, checkpointing and monitoring. Excludes Managed Agents, Client SDK and Agent SDK-only integration claims. Rolling official documentation accessed 2026-10-12; no pinned installed CLI release or runtime qualification. |
| GEMINI | Google Gemini CLI | Coding tool | Official Gemini CLI planning/coding harness, native subagents, policy engine, checkpoints, telemetry and skills. Excludes ADK, Gemini API-only features and model benchmarks. Rolling official documentation accessed 2026-10-12; no pinned installed CLI version or runtime verification. |
| QWEN | Qwen Code | Coding tool | Qwen Code CLI/native Goals, review, subagents, skills and permission mechanisms; standalone Qwen model benchmarks and third-party ecosystem tools excluded. Rolling official docs/main accessed 2026-10-12; published SWE-bench comparison names CLI versions through 0.22.0. No installed/current-build pin or runtime trial. |
| OASDK | OpenAI Agents SDK | Agent SDK | Code-first Agents SDK in application-owned Python/TypeScript processes. Includes officially documented SDK trace/evaluation integration; excludes Codex and managed Agents API capabilities. Rolling official documentation accessed 2026-10-12; no pinned SDK release or installed/runtime verification. |
| CASDK | Anthropic Claude Agent SDK | Agent SDK | Python/TypeScript programmable Claude Code agent in a process the application operates. Includes SDK-specific permissions, hooks, sessions, delegation and cost semantics; excludes Anthropic Managed Agents and Client SDK features. Rolling official SDK documentation accessed 2026-10-12; platform.claude.com documentation redirects to code.claude.com. No pinned installed release or runtime verification. |
| ADK | Google Agent Development Kit | Agent SDK | ADK framework and explicitly documented language-specific workflow, resumability, callback, evaluation and experimental skill capabilities. Excludes Gemini CLI and cloud platform mechanisms not included in these sources. Rolling official docs accessed 2026-10-12; google.github.io/adk-docs redirects to adk.dev. Page-specific language/version support retained; no installed release qualification. |
| OPENHANDS | OpenHands Software Agent SDK | Coding-agent SDK | OpenHands SDK/default coding agent, native tools, conversations, workspaces and Agent Server. Canvas, automation, Cloud/Enterprise controls and third-party agents excluded. Rolling V1 SDK documentation/main repository accessed 2026-10-12; benchmark evidence refers to published SDK-linked configurations, not a pinned current build. |
| LANGGRAPH | LangGraph | Orchestration runtime | Python OSS LangGraph graph/state/runtime and installable checkpointers. LangChain agents, Deep Agents harnesses, Agent Server hosting and LangSmith are separate products. LangSmith evaluation is credited only as an explicitly optional composition. Application authors retain semantic contracts and product adoption authority; STDO can govern work executed by this runtime. Live official OSS documentation and publisher repository accessed 2026-10-12. Checkpointer documentation identifies langgraph>=1.2 for beta DeltaChannel and Graph API documents version-specific migration limits. No installed package, tag-pinned trial or common runtime experiment was performed. |
| MAF | Microsoft Agent Framework | Agent/workflow framework | Current Microsoft Agent Framework Python/.NET agent and workflow APIs, skills, core evaluation and native OpenTelemetry. Opt-in FIDES is marked scoped; Foundry cloud evaluators/hosting are separate integrations. AutoGen and Semantic Kernel are migration predecessors, not a feature union. STDO could supply governing semantic obligations around this runtime. Experimental FIDES credit is direct Python-agent-tool scope only; .NET/CodeAct nested capabilities are excluded. Official live docs/repositories accessed 2026-10-12. AutoGen and Semantic Kernel READMEs identify MAF 1.0 as a production-ready successor; current checkpoint guide separately identifies Python 1.13.0 changes. AutoGen explicitly entered maintenance/community management. Semantic Kernel's 2025 publisher support statement promises critical/security fixes while most new investment moves to MAF; it is not the same community-maintenance claim. Both official migration guides were opened. No package installed or tag-pinned execution trial. |
| CREWAI | CrewAI | Agent/workflow framework | OSS Python crews, agents, tasks, flows, skills, hooks, checkpointing and CLI testing. AMP visual builders, Enterprise hosting and external observability platforms are separate compositions and receive no blanket native credit. Application qualification and semantic authority may be supplied by STDO. Official concept/learn URLs redirected to v1.15.27 documentation on 2026-10-12. Publisher repository inspected for scope/license. This is a source-based current-docs comparison, not a pinned package execution trial. |
| PYDANTIC | Pydantic AI | Typed agent framework | Core Pydantic AI agents, typed dependencies/output, capabilities, deferred tools, AgentSpecs, usage/instrumentation and published durable-engine integrations. Pydantic Evals is a separately installed composition; Logfire is an optional backend. pydantic-ai-harness Skills and its 0.x coding/research harnesses are explicitly outside native runtime scoring. STDO could govern semantics and qualification around these mechanisms. Live official docs and publisher repository accessed 2026-10-12. Official version policy identifies stable V2.0 released June 23, 2026; this packet follows current V2 documentation without claiming an exact installed minor version. Harness Skills separately documents a 0.x package and is not unioned into core. |

Optional composition receives scoped credit and stays visible: LangSmith is separate from LangGraph; Pydantic Evals is a separate install and Logfire an optional backend; Foundry cloud services are separate from Microsoft Agent Framework. AutoGen and Semantic Kernel are migration predecessors, not a feature union. Experimental ADK Skills and opt-in Microsoft FIDES retain those qualifications. The selected OpenHands row is SDK/default-agent scope, not all Cloud/Enterprise/Canvas features. [LangGraph scope](https://docs.langchain.com/oss/python/langgraph/overview), [Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/), [Microsoft framework](https://github.com/microsoft/agent-framework), [ADK Skills](https://adk.dev/skills/), [OpenHands architecture](https://docs.openhands.dev/sdk/arch/overview)

Support lifecycle also matters: the OpenAI Evals platform cited as an optional evaluation composition becomes read-only on 31 October and is scheduled to shut down on 30 November 2026. This is an integration limitation; it does not deprecate Agents SDK. A later evaluation must refresh that composition instead of carrying this score forward. [Official deprecations](https://developers.openai.com/api/docs/deprecations)

### 4. Rating rules

| Rating | Interpretation |
| --- | --- |
| 3 | First-class explicit relation or supported mechanism meeting the criterion within its stated domain; boundaries are documented. |
| 2 | Explicit narrower/optional support; some material part remains with the caller or another named composition. |
| 1 | Guidance, example, convention or materially partial support. |
| 0 | Explicit lack/prohibition within scope, or omission from an inspected complete capability inventory. Limited source search cannot justify zero. |
| U | Evidence is insufficient. This is not a negative capability judgment and is never converted to zero. |
| NA | Outside the declared product purpose; the cell names the surrounding owner/composition. SDK package release is not constructed-product adoption. |

| Suffix | What the source establishes |
| --- | --- |
| D | Documented method obligation; a v3 candidate obligation remains candidate wording. |
| R | Published runtime/API mechanism, conditional on documented configuration and support. |
| G | Guidance or example. C19 can receive 3G for a supported entry path, without measured onboarding success. |
| L | Locally inspected artifact, observation or bounded measurement, at its named subject. |
| P | Public measured experiment, limited to its configuration and population. |

`3D` is not equivalent to `3R`, and neither means empirically qualified. C23 deliberately rates observed adequate outcomes; C21 rates evaluation capability; C24 can credit a documented self-qualification obligation without claiming it has been discharged. Numeric scores do not measure reliability, probability, security, speed or implementation quality. Confidence in the ledger describes support for the bounded analyst judgment, not confidence in an unrun product.

No total is supplied. Adding normative obligations, runtime mechanisms and outcome evidence would double-count some relations and reward scope breadth without owner-selected weights. Select a use case, inspect its relevant cells and unresolved seams, then qualify the chosen composition.

### 5. Criteria and distinguishing failure probes

| ID | Criterion | Required distinction | Failure probe | Prior mapping |
| --- | --- | --- | --- | --- |
| C01 | Owned outcome and scope | Outcome, exclusions, observable success and owner choices are explicit. | Local checks pass while the selected owner outcome or an exclusion is violated. | F01/F02 |
| C02 | Specification and realization separation | Requirements and implementation choices have recoverable traceability; a task prompt alone is weaker. | Implementation satisfies its own plan while contradicting a requirement. | F03/F04/F05 |
| C03 | Contextual meaning and identity | Subject, representation, identity, current state and interpretation remain distinguishable; typed JSON alone is weaker. | Equal labels/bytes occur under different owners, states or interpretations. | F06/F08 |
| C04 | Composition and obligation conservation | Compatible joins retain governing constraints, known failure and required missing coverage; sequencing alone is weaker. | Join a falsified A and an uncovered required B; both must remain visible. | F07/F09 |
| C05 | Change and support invalidation | Changed basis or requirements reopen affected support while retaining valid unaffected work; session replay alone is weaker. | Change a material premise; reusing the old green judgment must fail. | F22/F14 |
| C06 | Constructed product release and adoption | Governs identity, qualification and adoption of constructed products; releasing the SDK itself does not satisfy this. | Change a released member or basis without explicit qualification/adoption. | F23 |
| C07 | Targeted context acquisition | Selects required sources and scoped context without ambient memory; strong claims expose material exclusions. | Put necessary context in an excluded source and misleading instructions in ambient context. | F10/F27 |
| C08 | Envelope fit and capacity pressure | Declares actor/task capacity and truthful cannot-fit handling; counts actual required context. Compaction alone is partial. | A coupled required relation exceeds the declared cap; silently trim nothing. | F11 |
| C09 | Bounded decomposition and delegation | Supports sufficient subtasks, handoffs and joins preserving the outer task; named roles alone are insufficient. | A delegated result loses an outer obligation, source coordinate or known failure. | F12/F13 |
| C10 | Durable state and changed-actor resumption | Persists useful work/state and resumes with validity checks; retaining chat alone is partial. | Resume with a fresh actor after a material workspace/basis change. | F14/F15 |
| C11 | Unknowns refusal and next action | Separates success/failure/unknown or invalid basis from permitted next action; retry-until-success is weaker. | Exercise success, failure, insufficient evidence, missing capability and stale basis. | F16/F15 |
| C12 | Uncertain effects and safe replay | Supports reconciliation/idempotency boundaries or explicit unresolved effects before duplicate execution; checkpoints alone are weaker. | Commit an effect, lose the response, then resume; do not blindly repeat it. | F14/F17 split |
| C13 | Permission and effect boundaries | Defines or enforces exact grants and pre-effect controls including denied actions; post-effect guardrails are weaker. | Use a named owner with no exact grant; deny before the selected effect. | F17 |
| C14 | Claim-relative independent assessment | Defines author/reference/evidence separation where needed; reviewer names or human tool approval alone are weaker. | Author, reviewer or reference exposure violates the declared independence policy. | F18 |
| C15 | Independent expected outcomes and oracle checks | Expected answers independent of candidate output can expose faulty checkers; author-generated tests alone are weaker. | A faulty checker accepts a known bad candidate or rejects a lawful alternative. | F19 split |
| C16 | Claim evidence judgment and acceptance separation | Keeps mechanical/behavioral/semantic claims and owner acceptance distinct; generic approval buttons are partial. | A valid parse or tool approval is offered as semantic acceptance. | F20 |
| C17 | Exact provenance and verdict scope | Binds results to subject/basis/evidence and limits claim scope; traces alone are partial. | Evidence names the wrong subject/basis or generalizes beyond the measured population. | F21 |
| C18 | Negative cases and regression evaluation | Provides refusal/uncertainty/changed-basis cases and regression paths; happy-path demos alone are partial. | A happy path passes but a refusal/uncertainty/changed-basis branch is defective. | F19 |
| C19 | Onboarding and ordinary first use | Clear entry, supported examples and ordinary task path without private author/validator knowledge. | A fresh ordinary user follows the published route without private rescue. | F28 |
| C20 | Native reusable context and portability | Discoverable source-linked instructions/skills/schemas/frames reusable across tasks; opaque summaries are weaker. | Move/reuse a package while changing its source; stale/opaque instructions must be detectable. | F24/F27 |
| C21 | Evaluation and feedback integration | Reproducible evaluation, trace review, CI or feedback-to-source repair. Rates capability, not achieved effectiveness. | Observed failures feed a reproducible rerun and a correction at the owning source. | F15/F22 |
| C22 | Complete cost and resource observability | Exposes token semantics, time and delegated work where claimed; separates transfers, active context, critical path and aggregate work. | Hide delegated or failed-attempt cost, or conflate transferred bytes with active context. | F30/F11 proportionality lens |
| C23 | Scoped effectiveness evidence | Measured outcomes for the selected method/framework. Model benchmarks or eval tooling alone are insufficient; superiority needs matched controls. | Tool availability, internal use or a model leaderboard is offered as method effectiveness. | F29 |
| C24 | Method self-qualification and usable fidelity | Tests fresh actors using method against source-derived expectations and faulty guidance/oracle controls; self-use or unit tests alone are weaker. | Introduce faulty method guidance or oracle; fresh-use qualification must expose it. | F26/F27/F28 |
| C25 | Untrusted inputs and information boundaries | Documents or constrains authority of retrieved/context instructions and sensitive-data egress. Authorization alone is partial; no generic injection-prevention guarantee is assumed. | Retrieved text requests a grant override or secret egress; data must not silently become instruction authority. | New; sharpens F10/F17 |
| C26 | Enforced operational resource limits | Configured spend/token/time/turn/concurrency/retry controls and cancellation expose their scope, delegated coverage and hard versus approximate limits. Observation alone is weaker. | A child exhausts its allowance or ignores cancellation; distinguish a hard stop from a reporting-only/estimated budget. | New; splits F11/F12/F30 |

### 6. Evaluation grids

Each cell has a reason, confidence and exact source identifiers in the workbook's Evidence sheet and JSON/CSV ledger. Rows are grouped by purpose, not ordered by quality. Candidate code identifies the same scoped entry in every grid.

#### Purpose and meaning

| Entry | C01 | C02 | C03 | C04 | C05 | C06 |
| --- | --- | --- | --- | --- | --- | --- |
| ST25 | 3D | 3D | 3D | 3D | 3D | 3D |
| ST3C | 3D | 3D | 3D | 3D | 3D | 2D |
| ST3X | 3D | 3D | 3D | 3D | 3D | 3D |
| SPECKIT | 3D | 3D | 2D | 2D | 2G | U |
| BMAD | 3D | 3D | 2D | 2D | 2D | 1D |
| OPENSPEC | 3D | 3D | 2D | 1R | 1D | U |
| CODEX | 2G | 1G | 1R | U | 1G | NA |
| CLAUDE | 2G | 2G | 1R | U | 1R | NA |
| GEMINI | 2G | 2R | 1R | U | 1R | NA |
| QWEN | 2R | 2R | 2R | 2R | 2R | NA |
| OASDK | 2G | U | 1R | U | U | NA |
| CASDK | 2G | U | 1R | U | U | NA |
| ADK | 2G | U | 1R | U | 1D | NA |
| OPENHANDS | 1G | 1R | 2R | 1R | U | NA |
| LANGGRAPH | 1G | 1G | 1R | 1R | 1R | NA |
| MAF | 1R | 1R | 1R | 1R | 1R | NA |
| CREWAI | 2R | 1R | 1R | 1R | U | NA |
| PYDANTIC | 1R | 1R | 1R | 1R | 1G | NA |

C01 Owned outcome and scope; C02 Specification and realization separation; C03 Contextual meaning and identity; C04 Composition and obligation conservation; C05 Change and support invalidation; C06 Constructed product release and adoption.

#### Bounded work and recovery

| Entry | C07 | C08 | C09 | C10 | C11 | C12 |
| --- | --- | --- | --- | --- | --- | --- |
| ST25 | 3D | 2D | 3D | 3D | 3D | 2D |
| ST3C | 3D | 3D | 3D | 3D | 3D | 3D |
| ST3X | 3D | 2D | 3D | 3D | 3D | 3D |
| SPECKIT | 3D | 1D | 2R | 2R | 2D | 1R |
| BMAD | 3D | 2D | 3D | 2D | 3D | 1D |
| OPENSPEC | 2R | 1G | 1G | 2R | 2R | 3R |
| CODEX | 2R | 1R | 2R | 2R | 2R | 1R |
| CLAUDE | 2R | 1R | 2R | 2R | 2R | 1R |
| GEMINI | 2R | 1R | 2R | 2R | 2R | 1R |
| QWEN | 2R | 2R | 2R | 3R | 3R | 2R |
| OASDK | 2R | 1R | 2R | 2R | 2R | 1G |
| CASDK | 2R | 1R | 2R | 2R | 2R | 1R |
| ADK | 2R | U | 2R | 2R | 2R | 1G |
| OPENHANDS | 2R | 1R | 2R | 2R | 2R | 1R |
| LANGGRAPH | 2R | 1G | 2R | 3R | 2R | 2G |
| MAF | 2R | 1G | 2R | 3R | 2R | 2R |
| CREWAI | 2R | 2R | 2R | 2R | 1R | 1G |
| PYDANTIC | 2R | 2R | 2R | 2R | 2R | 2G |

C07 Targeted context acquisition; C08 Envelope fit and capacity pressure; C09 Bounded decomposition and delegation; C10 Durable state and changed-actor resumption; C11 Unknowns refusal and next action; C12 Uncertain effects and safe replay.

#### Assurance and authority

| Entry | C13 | C14 | C15 | C16 | C17 | C18 |
| --- | --- | --- | --- | --- | --- | --- |
| ST25 | 3D | 3D | 3D | 3D | 3D | 3D |
| ST3C | 3D | 3D | 3D | 3D | 3D | 3D |
| ST3X | 3D | 3D | 3D | 3D | 3D | 3D |
| SPECKIT | 2R | 1D | 1D | 2D | 2D | 2D |
| BMAD | 2D | 2D | 1D | 3D | 2D | 2D |
| OPENSPEC | 2R | 1D | 1D | 2D | 1R | 2D |
| CODEX | 3R | 1G | 1G | 1G | 2G | 2G |
| CLAUDE | 3R | 2G | 1G | 1G | 1R | 2G |
| GEMINI | 3R | 1R | U | 1R | 1R | 1G |
| QWEN | 3R | 2R | 2P | 3R | 3R | 2R |
| OASDK | 2R | 1R | 2R | 1R | 1R | 2R |
| CASDK | 3R | 1R | U | 1R | 1R | 1R |
| ADK | 2R | 1R | 2R | 1R | 1R | 2R |
| OPENHANDS | 2R | 2R | 2P | 1R | 2R | 2P |
| LANGGRAPH | 2R | U | 2R | 1R | 2R | 2R |
| MAF | 2R | U | 2R | 1R | 2R | 2R |
| CREWAI | 2R | U | 1R | 1R | 2R | 1G |
| PYDANTIC | 2R | U | 2R | 1R | 2R | 2R |

C13 Permission and effect boundaries; C14 Claim-relative independent assessment; C15 Independent expected outcomes and oracle checks; C16 Claim evidence judgment and acceptance separation; C17 Exact provenance and verdict scope; C18 Negative cases and regression evaluation.

#### Use and evidence

| Entry | C19 | C20 | C21 | C22 | C23 | C24 |
| --- | --- | --- | --- | --- | --- | --- |
| ST25 | 2G | 2D | 2D | 1D | U | 3D |
| ST3C | 2G | 2D | 2L | 2L | U | 3D |
| ST3X | 2G | 2D | 2L | 1L | 1L | 3D |
| SPECKIT | 3G | 3R | 2D | U | U | U |
| BMAD | 3G | 3D | 2D | U | U | U |
| OPENSPEC | 3G | 3R | 2D | U | U | 1G |
| CODEX | 3G | 3R | 2G | 2R | U | U |
| CLAUDE | 3G | 3R | 2R | 2R | U | U |
| GEMINI | 3G | 3R | 1R | 2R | U | U |
| QWEN | 3G | 3R | 3R | 2R | 2P | 2R |
| OASDK | 3G | 2R | 2R | 1R | U | U |
| CASDK | 3G | 3R | 1R | 2R | U | U |
| ADK | 3G | 2R | 3R | 2R | U | U |
| OPENHANDS | 3G | 3R | 3R | 2R | 2P | 1P |
| LANGGRAPH | 3G | 2R | 2R | 1R | U | U |
| MAF | 3G | 3R | 3R | 2R | U | U |
| CREWAI | 3G | 3R | 2R | 2R | U | U |
| PYDANTIC | 3G | 2R | 2R | 2R | U | U |

C19 Onboarding and ordinary first use; C20 Native reusable context and portability; C21 Evaluation and feedback integration; C22 Complete cost and resource observability; C23 Scoped effectiveness evidence; C24 Method self-qualification and usable fidelity.

#### Operational controls

| Entry | C25 | C26 |
| --- | --- | --- |
| ST25 | 1D | 1D |
| ST3C | 1D | 1D |
| ST3X | 1D | 1D |
| SPECKIT | 1G | 2R |
| BMAD | 1D | U |
| OPENSPEC | U | U |
| CODEX | 2R | 1R |
| CLAUDE | 2R | 2R |
| GEMINI | 1R | 2R |
| QWEN | 2R | 2R |
| OASDK | 1R | 1R |
| CASDK | 1R | 2R |
| ADK | 1R | 2R |
| OPENHANDS | 2R | 2R |
| LANGGRAPH | U | 2R |
| MAF | 3R | 2R |
| CREWAI | 1G | 2R |
| PYDANTIC | 1G | 2R |

C25 Untrusted inputs and information boundaries; C26 Enforced operational resource limits.

### 7. Findings that affect a v3 decision

**STDO's strongest documented contribution is the relation between meaning, obligations, evidence and authority.** Both candidates make failure conservation, scoped interpretation and truthful insufficient-context results explicit. That distinguishes a governing method from a graph or chat history. The high D cells establish source coverage of obligations, not that either candidate has qualified every inherited relation or produced better practical outcomes. Detailed owner contracts and local residuals remain in the source ledger.

**The v3 candidates make different context-fit choices.** Claude's ACTIVATION specifies pre-read byte measurement for selected context; Codex's Foundations/Frame Method preserve capability-fit law without imposing a universal numeric measurement gate. Under this criterion, semantic fit alone gets partial credit. Neither a paragraph byte cap nor a source-file total proves provider peak active context. The difference is a candidate design choice to assess against purpose and proportionality, not a common-law ruling.

**Native guidance and reusable context remain a practical STDO priority.** Coding tools provide discoverable skills, local instructions, ordinary setup and examples. Specification methods provide direct commands and feature/story workflows. STDO's named frame projections are useful candidate surfaces, but a new user still needs an ordinary route that acquires sufficient owning context without private author rescue. This question is separate from whether the corpus is semantically detailed. [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code entry](https://code.claude.com/docs/en/overview), [Gemini skills](https://geminicli.com/docs/cli/using-agent-skills/), [Spec Kit](https://github.com/github/spec-kit)

**Recovery and uncertain effects are separate capabilities.** LangGraph and Microsoft Agent Framework document durable state recovery; ADK explicitly permits repeated tool execution during resume. LangGraph tells authors to isolate or make replayed effects idempotent. OpenSpec documents a stronger bounded archive-recovery mechanism, but that does not protect arbitrary agent-side external effects. An integrating method needs a declared reconciliation boundary. [LangGraph checkpoints](https://docs.langchain.com/oss/python/langgraph/checkpointers), [Microsoft checkpoints](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints), [ADK resume](https://adk.dev/runtime/resume/), [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), [OpenSpec CLI](https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/cli.md)

**Fresh review can be supported without complete assurance independence.** Claude Code explicitly recommends a fresh-context adversarial reviewer. BMad's pinned core has fresh parallel review instructions. Qwen documents scoped review identity, finding ledgers and executing changed instructions in a disposable copy. These receive real scoped credit; none is automatically a qualified independent oracle for every semantic claim. [Claude best practices](https://code.claude.com/docs/en/best-practices), [BMad review](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/v6.12.2/docs/build/review-a-change.md), [Qwen review](https://qwenlm.github.io/qwen-code-docs/en/users/features/code-review/)

**Framework effectiveness is unresolved for most selected entries.** OpenHands publishes SDK-linked benchmark traces and a concrete reference-leakage discovery followed by repaired reruns; that supports bounded measured credit, not framework superiority. Qwen's publisher reports named CLI versions under fixed-model SWE-bench conditions; those are configuration-specific reported results. Model leaderboards, tool demonstrations, GitHub popularity and internal use otherwise earn no effectiveness credit. The two STDO developments are not a matched experiment: construction subjects, assistance, envelopes, methods and assessment coverage differ. [OpenHands evaluation repair](https://www.openhands.dev/blog/analyzing-and-improving-openhands-index), [Qwen Code evaluation](https://github.com/QwenLM/qwen-code#qwen-code-evaluation)

**Resource claims need correct accounting semantics.** Claude Agent SDK distinguishes parent-only usage from whole-tree model usage and describes cumulative resumed totals and client-estimated USD. CrewAI documents flow-level usage metrics; Pydantic AI documents delegated usage and optional pre-request limits. These are useful mechanisms, but transferred context, active context, billed tokens, cache subsets, critical-path time and summed actor time are different quantities. Claude's F-01 cold-input measurements are stronger evidence than the earlier contaminated activation counts, while output adequacy remains unassessed. Codex's bounded local reviews are not a complete provider/root cost account. [Claude SDK cost](https://code.claude.com/docs/en/agent-sdk/cost-tracking), [CrewAI flows](https://docs.crewai.com/en/concepts/flows), [Pydantic agents](https://pydantic.dev/docs/ai/core-concepts/agent/)

**Authorization, source trust and execution limits must stay distinct.** A pre-tool approval does not establish resistance to malicious retrieved instructions or prevent sensitive-data egress. Microsoft's opt-in FIDES is experimental and Python-only: credit covers direct agent tools. .NET is unsupported; Monty/Hyperlight CodeAct nested host calls and their file/network capabilities bypass enforcement and need host controls. Operational budgets also have scope and overshoot/cancellation limitations. STDO can govern these questions, but does not inherit a runtime protection merely by naming an invariant. [Microsoft security](https://learn.microsoft.com/en-us/agent-framework/agents/security), [OpenAI SDK guardrails](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)

### 8. Proposed common trial for the next evaluation

This survey researched sources and inspected existing evidence. It ran no new SDK, coding-agent or method effectiveness trial. The following is a proposed qualification protocol, not observed results or a selected spend grant.

| Trial | Independent expected distinction | Record |
| --- | --- | --- |
| Ordinary cold use | A fresh actor finds the ordinary entry, acquires necessary owner context and performs a task without private rescue. | Source/task/actor/configuration pin; every ambient instruction; acquisition and output artifacts; owner/independent adequacy judgment. |
| Capacity pressure | One coupled required relation exceeds the small envelope; refuse or lawfully reconfigure without silent omission. | Declared dimension and resident-context policy; whole input and provider usage; permitted fit choices and stop result. |
| Material/irrelevant change | A changed material premise reopens support; an unrelated change does not. | Before/after basis; invalidated and surviving claims; exact re-entry path. |
| Failure and missing coverage | A fails and required B is absent; the join retains both and cannot project success. | Original producer/basis/citations; uncovered set; composite result and next authority. |
| Lost response after effect | Observe an effect, suppress its response, then resume with a fresh actor. | Authentic external state and reconciliation; repeated-effect count; no fabricated no-effect assumption. |
| Defective guide and oracle | Source-derived expectations detect bad method guidance and a checker that green-lights a known bad candidate. | Independent expectations before candidate exposure; freeze; seeded defects and lawful alternative; assessor separation. |
| Untrusted retrieved instruction | A retrieved document tries to override grants or export a synthetic secret. | Trust/data boundary, scope-limited controls, attempted effects and egress observations. |
| Budget/cancellation | Delegation reaches a resource limit or cancellation boundary and returns a truthful stop. | Hard/estimated ceiling, overshoot, live children, canceled work and whole-tree cost. |

Use a shared fixed task/basis set, the same declared model/configuration when isolating method effects, randomized order, comparable cold starts and repeat runs sufficient to expose variance. Separate a matched fixed-model comparison from a product-best-configuration comparison. Freeze expected relations independently from the candidate's own CONFORMANCE table; withhold material answers/incumbents where earlier exposure defeats the claim. An assessor must acquire the governing basis, inspect the actual frozen outputs and state its exact population; the constructor cannot self-award adequate outcomes.

Predeclare how resident basis is charged, how composite non-success states map to next action, and who may choose a different fit option. Account for setup, source acquisition, every delegated actor, failed attempts, compaction, retries, assessment and repair. Report input/output/cache/reasoning token semantics, total transferred bytes, peak active context where available, list-price estimates versus authoritative spend, critical-path wall time and aggregate actor time. Record unavailable counters explicitly. Compare adequate outcomes and material errors against this complete resource boundary, not number of artifacts or the smallest visible prompt.

### 9. Source ledger and reproduction

All web sources are publisher repositories, official documentation or publisher experiment reports. They were opened and read for the cited scope; no search snippet is credited as implementation evidence. Rolling pages are access-date snapshots, not pinned executables. Public claims were not independently reproduced. Local sources use `stdo://` immutable release locators or exact `git show COMMIT:path` selectors; no unverified public commit URL is implied.

To inspect a tenant source, run its recorded `git show` selector from a repository containing those tenant Git objects. Tenant selectors are local evidence locators; remote acquisition requires those tenant refs separately. Immutable STDO locators require the selected installed cut. To challenge a rating, filter the workbook Evidence sheet by candidate and criterion, then acquire its listed source. Update the candidate version/status and affected cells together; retain the original evaluation as history. The JSON retains the independent-review corrections, and the CSV preserves numeric score fields versus U/NA text.

#### ST25 — STDO 2.5.1-rc.2

Strong explicit semantic, authority and assurance obligations; ordinary activation and instrumented effectiveness remain separate concerns.

Evidence boundary: No controlled experiment established for the installed release in this review.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| ST2-SPEC | [STDO 2.5.1-rc.2 Spec Method](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md) | Installed immutable builder, byte identity selected by verified Product Definition; normative obligations, not runtime enforcement. |
| ST2-AC | [STDO 2.5.1-rc.2 Axiomatic Calculus](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md) | Interpretation, scoped identity, judgment, basis and typed-composition laws. |
| ST2-RF | [STDO 2.5.1-rc.2 Reference Frame Method](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md) | Material closure, actor capability, closed results, frame functions and method self-qualification. |
| ST2-TICKET | [STDO 2.5.1-rc.2 Ticket Method](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md) | Execution admission and recorded judgment/owner-ruling continuity. |
| ST2-REL | [STDO 2.5.1-rc.2 Release Method](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md) | Constructed Product release/adoption and successor baseline conservation. |
| ST2-BASE | [STDO 2.5.1-rc.2 baseline and README](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md) | Ordinary entrypoints through installed README and bootstrap; baseline frames do not eliminate exact owner acquisition. |

#### ST3C — STDO v3 — Claude candidate

Explicit context construction and generic refinement/work-state relations; new cold-run resource evidence is not yet independently assessed.

Evidence boundary: Four frozen cold task starts with observed usage; output adequacy unassessed, no comparative effectiveness verdict.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| CLA-README | Claude candidate corpus entrypoint<br>`git show e1bcd802f2ebf3b695ef5f6e94780d3f00f29d0d:specification_methodology/v3/build_tenants/claude/standards/README.md` | Member-by-member construction; not released, installed or common law. |
| CLA-FOUND | Claude Foundations<br>`git show e1bcd802f2ebf3b695ef5f6e94780d3f00f29d0d:specification_methodology/v3/build_tenants/claude/standards/FOUNDATIONS.md` | Ontology, P0–P6, declared standing, frame tuple and conservation. |
| CLA-ACT | Claude Activation<br>`git show e1bcd802f2ebf3b695ef5f6e94780d3f00f29d0d:specification_methodology/v3/build_tenants/claude/standards/ACTIVATION.md` | Context construction, measured fit, refinement, work state, total results, scoped cost and reuse. |
| CLA-EVAL | Claude Evaluation<br>`git show e1bcd802f2ebf3b695ef5f6e94780d3f00f29d0d:specification_methodology/v3/build_tenants/claude/standards/EVALUATION.md` | Independent assessment, claim limits, fresh method qualification and recoverability benchmark. |
| CLA-SPEC | Claude Spec Method<br>`git show e1bcd802f2ebf3b695ef5f6e94780d3f00f29d0d:specification_methodology/v3/build_tenants/claude/standards/SPEC_METHOD.md` | Core Product construction and release/profile routes; successor corpus still under construction. |
| CLA-F01 | Claude F-01 cold run provenance<br>`git show e1bcd802f2ebf3b695ef5f6e94780d3f00f29d0d:specification_methodology/v3/build_tenants/claude/qualification/runs/F-01/RUNS.md` | Four measured cold contexts with frame identities, provider usage and output artifacts; runner expressly did not assess outputs. |

#### ST3X — STDO v3 — Codex candidate

Detailed source owners remain authoritative; selected fresh-use and mutation reviews expose failure and missing coverage while retaining qualification residuals.

Evidence boundary: Selected independently judged fresh-use and mutation cases; bounded local evidence, no common control or whole-method qualification.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| CDX-README | Codex successor corpus entrypoint<br>`git show 427a0deb39b7cd8e298b3b2ebc126c052f056d8a:specification_methodology/v3/build_tenants/codex/successor/standards/README.md` | Standalone successor construction cut, explanatory foundations/library plus detailed owners; not released or adopted. |
| CDX-FOUND | Codex successor Foundations<br>`git show 427a0deb39b7cd8e298b3b2ebc126c052f056d8a:specification_methodology/v3/build_tenants/codex/successor/standards/FOUNDATIONS.md` | Premises, identity, interpretation, conservation, truthful capacity response and uncertain-effect handling. |
| CDX-SPEC | Codex successor Spec Method<br>`git show 427a0deb39b7cd8e298b3b2ebc126c052f056d8a:specification_methodology/v3/build_tenants/codex/successor/standards/SPEC_METHOD.md` | Detailed construction authority, change classes, outcome, proportionality and UP-022 assurance owner. |
| CDX-RF | Codex successor Reference Frame Method<br>`git show 427a0deb39b7cd8e298b3b2ebc126c052f056d8a:specification_methodology/v3/build_tenants/codex/successor/standards/REFERENCE_FRAME_METHOD.md` | Detailed frame functions, capability fit, closed results, explicit exclusions and method qualification. |
| CDX-REL | Codex successor Release Method<br>`git show 427a0deb39b7cd8e298b3b2ebc126c052f056d8a:specification_methodology/v3/build_tenants/codex/successor/standards/RELEASE_METHOD.md` | Detailed constructed-Product release/adoption owner. |
| CDX-EXEC | Codex C3 execution and repair record<br>`git show 427a0deb39b7cd8e298b3b2ebc126c052f056d8a:specification_methodology/v3/build_tenants/codex/qualification/C3/EXECUTION.md` | 690-row predecessor frontier and named local reviews; post-repair independent confirmation remains open for selected seams. |
| CDX-DOMAIN | Codex fresh domain-use review<br>`git show 427a0deb39b7cd8e298b3b2ebc126c052f056d8a:specification_methodology/v3/build_tenants/codex/qualification/C3/use/domain/REVIEW.md` | Fresh non-author actor used supplied task/view; seeded violations found; exact limitations on source-byte/digest and broader claims retained. |
| CDX-FIDELITY | Codex a_c interpretation-fidelity review<br>`git show 427a0deb39b7cd8e298b3b2ebc126c052f056d8a:specification_methodology/v3/build_tenants/codex/qualification/C3/a_c/review/REVIEW.md` | Historical assessed subject b0ec615c; wrong-permission mutant falsified, admitted program indeterminate, finite model only partially supports source. Repairs at later pin need fresh confirmation. |

#### SPECKIT — GitHub Spec Kit

A specification-first method with explicit artifact relations and corrective convergence, plus a native workflow runtime. D scores describe agent instructions; R scores describe published engine behavior. Neither establishes successful execution or semantic adequacy in this survey.

Evidence boundary: Source-based capability inference only. Reviewed pages provide process documentation and examples; no common runtime experiment or measured whole-method superiority.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| SP01 | [Spec Kit README](https://github.com/github/spec-kit) | Purpose, process choices, installation, supported coding-agent entry, MIT license. |
| SP02 | [Agentic SDD reference](https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md) | Constitution, specify/plan/tasks, optional quality gates, implementation and convergence. |
| SP03 | [Analyze command template](https://github.com/github/spec-kit/blob/main/templates/commands/analyze.md) | Method instructions: minimal context, constitution authority, coverage inventory, findings and remediation. |
| SP04 | [Converge command template](https://github.com/github/spec-kit/blob/main/templates/commands/converge.md) | Method instructions: scoped intent inventory, code evidence, gap classification and append-only repair tasks. |
| SP05 | [Workflows reference](https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md) | Runtime composition, fan-out/in, gates, persisted execution and resume; explicitly no capability sandbox. |
| SP06 | [Evolving Specs in Existing Projects](https://github.github.io/spec-kit/guides/evolving-specs.html) | Alternative persistence models, upstream/downstream alignment and preservation of useful rationale. |
| SP07 | [Workflow Engine README](https://raw.githubusercontent.com/github/spec-kit/main/workflows/README.md) | Rolling main documentation: raw interpolation/allowlist guidance, loop limits, shell timeout, concurrency setting and abort behavior; no execution trial. |

#### BMAD — BMad Method v6.12.2

The frozen stable core specifies requirements, bounded stories, independent review attempts and evidence-based epic acceptance. These are documented method obligations, mediated by the host coding agent. V7-preview documentation and separately installed testing/orchestration modules contribute no scores.

Evidence boundary: No external experiment performed. Tagged core docs offer method guidance and examples; their comparative review claims and suggested A/B testing are not measurements.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| BM01 | [BMad v6.12.2 README](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/v6.12.2/README.md) | Core scope, prerequisites, first use, optional ecosystem modules and MIT license. |
| BM02 | [Build a Change](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/v6.12.2/docs/build/build-a-change.md) | One-goal scope, fresh context, plan approval, upstream correction and preserved implementation records. |
| BM03 | [Review a Change](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/v6.12.2/docs/build/review-a-change.md) | Separate reviewers/lenses, supplied intent, verified consequence triage and human choices. |
| BM04 | [Define Requirements and a Specification](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/v6.12.2/docs/plan/define-requirements-and-a-specification.md) | PRD/spec separation, capability IDs, non-goals, success conditions, input limits and story breakdown. |
| BM05 | [Break Work into Stories and Track It](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/v6.12.2/docs/plan/break-work-into-stories-and-track-it.md) | Readiness PASS/CONCERNS/FAIL, dependent-document checks, durable tracking and course correction. |
| BM06 | [Test Completed Work](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/v6.12.2/docs/build/test-completed-work.md) | Built-in QA generates from implemented code; heavier TEA assurance remains a separate add-on. |
| BM07 | [Set and Maintain Project Context](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/v6.12.2/docs/existing-codebases/set-and-maintain-project-context.md) | Verified source pointers, context exclusions, owner-approved edits, refresh and observed-pitfall feedback. |
| BM08 | [Finish an Epic](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/v6.12.2/docs/build/finish-an-epic.md) | Whole-epic evidence inventory, seam review, behavioral checks, acceptance verdict and owner override. |
| BM09 | [Autonomous Development Loops v6.12.2](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/v6.12.2/docs/build/autonomous-development-loops.md) | Pinned stable core worker contract: caller-only dispatch fields, one-unit ownership, halt outcomes and external orchestration; separate Loop add-on excluded. |

#### OPENSPEC — Fission AI OpenSpec

A portable spec layer separates agreed behavior, proposed change and technical realization. The CLI publishes concrete archive recovery mechanics. Its flexible update model and optional verify command provide reconciliation, not proof of upstream semantic invalidation or independent acceptance.

Evidence boundary: Source-based inference only. Self-use and examples are documented; no matched experiment establishes workflow effectiveness or superiority.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| OP01 | [OpenSpec README](https://github.com/Fission-AI/OpenSpec) | Spec-layer purpose, human review, setup, integrations, self-use and telemetry/license scope. |
| OP02 | [Getting Started](https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/getting-started.md) | Ordinary setup, change artifacts, core versus expanded command selection and first implementation. |
| OP03 | [Concepts](https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/concepts.md) | Behavior contracts, scenarios, current specs/proposed deltas, design/tasks and dependency schemas. |
| OP04 | [Workflows](https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/workflows.md) | Multiple changes, checkpointed task resumption, optional verification dimensions and non-blocking archive warnings. |
| OP05 | [CLI Reference](https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/cli.md) | Runtime status/validation/instructions and archive preconditions, destination claims, rollback and recovery. |
| OP06 | [Customization](https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/customization.md) | Reusable schemas, per-artifact rules and current context; operation guidance is explicitly advisory. |
| OP07 | [Editing and Iterating on a Change](https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/editing-changes.md) | Live artifact updates and spec/code reconciliation; no semantic support-invalidation mechanism established. |

#### CODEX — OpenAI Codex

Codex offers a mature coding execution surface with native instructions, skills, delegation and pre-effect controls. Published repair guidance adds bounded assurance practices; semantic obligation conservation remains unestablished.

Evidence boundary: Current official source-based capability assessment only. No common runtime trial, ordinary-task measurements or matched framework controls were run.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| CODEX-S1 | [Agent approvals & security](https://learn.chatgpt.com/docs/agent-approvals-security) | OS sandbox and approval controls; local, cloud and user-initiated execution have distinct boundaries. |
| CODEX-S2 | [Build skills](https://learn.chatgpt.com/docs/build-skills) | Native reusable skill format and progressive disclosure; does not establish semantic fidelity or full-context admission. |
| CODEX-S3 | [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | Scoped delegation and collected results; local Codex policy distinguished from ChatGPT Work behavior. |
| CODEX-S4 | [Codex App Server](https://learn.chatgpt.com/docs/app-server) | Thread/turn identity, resume, approvals, events and usage; experimental surfaces and execution exceptions documented. |
| CODEX-S5 | [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Layered source-file discovery and bounded loading; instructions are prompt guidance rather than enforced product qualification. |
| CODEX-S6 | [Build iterative repair loops with Codex](https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex) | Published bounded notebook repair recipe with distinct phases and records; guidance/example, not a general effectiveness experiment. |

#### CLAUDE — Anthropic Claude Code

Claude Code combines strong coding controls with unusually explicit guidance for fresh-context adversarial review. Recovery and context boundaries are documented, but stronger semantic qualification relations remain unestablished.

Evidence boundary: Official mechanisms and published practice inspected. Internal-use claims are not a common ordinary-task experiment; no runtime measurements were run.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| CLAUDE-S1 | [Overview](https://code.claude.com/docs/en/overview) | Supported coding surfaces, install and entry; broad product claims are not effectiveness measurements. |
| CLAUDE-S2 | [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) | Plan/implementation separation, explicit verification and fresh-context adversarial review; recommended practice rather than universal enforced method. |
| CLAUDE-S3 | [Create custom subagents](https://code.claude.com/docs/en/sub-agents) | Scoped tool/context delegation, inherited guidance and bounded execution; context defaults differ across built-in agent classes. |
| CLAUDE-S4 | [Configure permissions](https://code.claude.com/docs/en/permissions) | Runtime deny/ask/allow ordering and permission modes; pattern scopes and bypass behavior have documented limitations. |
| CLAUDE-S5 | [Checkpointing](https://code.claude.com/docs/en/checkpointing) | Durable direct-edit snapshots and conversation rewind; shell, external and most subagent edits are excluded. |
| CLAUDE-S6 | [Monitoring](https://code.claude.com/docs/en/monitoring-usage) | Token/cost/time counters and nested API/tool spans; opt-in detail and estimates are not a full semantic resource model. |
| CLAUDE-S7 | [Security](https://code.claude.com/docs/en/security) | Documents untrusted-content precautions, scoped network/filesystem isolation and credentials; interactive/headless and local/cloud controls differ, and no immunity is claimed. |

#### GEMINI — Google Gemini CLI

Gemini CLI has explicit planning artifacts, scoped delegation and pre-tool policy controls. Optional snapshots and telemetry support bounded recovery and observability without establishing safe replay or semantic qualification.

Evidence boundary: Official documentation inspected. No CLI runtime experiment, measured ordinary-task outcomes or matched framework controls were run.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| GEMINI-S1 | [Plan Mode](https://geminicli.com/docs/cli/plan-mode/) | Read-only research and reviewable Markdown plans before execution; policy customization and user approval govern scope. |
| GEMINI-S2 | [Subagents](https://geminicli.com/docs/core/subagents/) | Separate context loops, scoped tools, parent results, turn/time limits and recursion protection; runtime bounds do not prove task sufficiency. |
| GEMINI-S3 | [Policy engine](https://geminicli.com/docs/reference/policy-engine/) | Pre-tool allow/deny/ask decisions, priority tiers and subagent selectors; workspace policy tier currently disabled. |
| GEMINI-S4 | [Checkpointing](https://geminicli.com/docs/cli/checkpointing/) | Opt-in file/conversation/tool snapshots; restore re-proposes the original tool call, without generic external-effect reconciliation. |
| GEMINI-S5 | [Observability with OpenTelemetry](https://geminicli.com/docs/cli/telemetry/) | Token classes, API/tool durations, traces and compression events; opt-in monitoring does not establish complete required-context accounting. |
| GEMINI-S6 | [Managing Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/) | Discoverable reusable source directories and consent; standard skill artifacts do not establish semantic method fidelity. |

#### QWEN — Qwen Code

A general coding harness with increasingly explicit native review and Goal mechanisms. Current primary docs support scoped evidence judgment, exact PR resumption and deadline refusal. These capabilities can host an external specification method; they do not replace product semantics or adoption authority.

Evidence boundary: Official README reports 500 SWE-bench Verified tasks, three trials per named CLI version, with fixed Qwen 3.7 Max and specified limits. This supports bounded harness-version evidence, not model-independent or complete-method superiority. No experiment was run here.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| QW01 | [Qwen Code README and Evaluation](https://github.com/QwenLM/qwen-code) | CLI purpose, ordinary setup, Apache-2.0 license, self-use and fixed-model SWE-bench runs across named CLI versions. |
| QW02 | [Approval Mode](https://qwenlm.github.io/qwen-code-docs/en/users/features/approval-mode/) | Mode-specific pre-effect controls, deny rules, fail-closed classifier and manual fallback; default statements conflict. |
| QW03 | [Subagents](https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/) | Fresh versus forked contexts, tool restrictions, parent continuation and shared-workspace limitations. |
| QW04 | [Resident Context Cost](https://qwenlm.github.io/qwen-code-docs/en/users/features/context-cost/) | Actual prefix breakdown with residual, deferred tools and explicit cache/context distinctions. |
| QW05 | [Conversations writer locks and recovery](https://qwenlm.github.io/qwen-code-docs/en/users/conversations-recovery/) | Identity-bound writer leases, transcript-proof handoffs, fail-closed unknown ownership and operator fencing. |
| QW06 | [Agent Skills](https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/) | Source-derived reusable skills, supporting files, explicit invocation, progressive disclosure and path gating. |
| QW07 | [Code Review](https://qwenlm.github.io/qwen-code-docs/en/users/features/code-review/) | Scoped findings/verdict pipeline, exact PR resumption checks, independent passes, deadlines, CI distinctions and instruction execution. |
| QW08 | [Goals](https://qwenlm.github.io/qwen-code-docs/en/users/features/goals/) | Owner objectives, evidence-only verifier, unknown/stop handling, bounded transcript scope and explicitly incomplete usage meters. |
| QW09 | [Sandbox](https://qwenlm.github.io/qwen-code-docs/en/users/features/sandbox/) | Rolling docs: optional operator-owned Linux file/network confinement, explicit host/descriptor/integration exclusions and cancellation behavior; many extension paths are disabled. |

#### OASDK — OpenAI Agents SDK

The SDK supplies orchestration, resumable approval state and explicit blocking control options. Application code owns business meaning, storage, authorization decisions and assurance references.

Evidence boundary: Official SDK mechanisms and integration guidance inspected. No runtime trial or measured ordinary-task effectiveness was established.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| OASDK-S1 | [Agents SDK](https://developers.openai.com/api/docs/guides/agents/sdk) | SDK/application ownership explicitly separated from managed harness; repositories linked, runtime not installed. |
| OASDK-S2 | [Running agents](https://developers.openai.com/api/docs/guides/agents/running-agents) | Run loop, state strategies, streaming, limits and interrupted-turn continuity; conversation replay is not external-effect replay. |
| OASDK-S3 | [Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration) | Specialist ownership versus manager-owned agents-as-tools; history filtering and structured handoffs are language dependent. |
| OASDK-S4 | [Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) | Blocking guards and tool approval pause; parallel input checks can allow speculative agent work before rejection. |
| OASDK-S5 | [Results and state](https://developers.openai.com/api/docs/guides/agents/results) | Output, history, specialist identity, interruptions and serialized snapshots; caller owns subject validity and storage interpretation. |
| OASDK-S6 | [Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals) | SDK traces connect to graders, datasets and repeated evals; platform integration capability, not measured effectiveness. |
| OASDK-REF-EVAL | [Working with evals](https://developers.openai.com/api/docs/guides/evals) | Composed Evals API distinguishes generated sample output from human-labelled reference; deprecated platform, not native SDK-only support. |
| OASDK-EVAL-LIFECYCLE | [Official OpenAI deprecations — Evals platform](https://developers.openai.com/api/docs/deprecations) | Evals becomes read-only 2026-10-31; dashboard/API shutdown scheduled 2026-11-30. This does not deprecate Agents SDK. |

#### CASDK — Anthropic Claude Agent SDK

The SDK exposes the Claude Code loop with explicit permissions, durable sessions and bounded delegation. Its unusually detailed accounting documents several ways naive totals undercount or double-count work.

Evidence boundary: Current official SDK mechanisms inspected. No runtime experiment, ordinary-task effectiveness measurement or matched framework controls were run.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| CASDK-S1 | [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) | Explicit SDK/CLI/Client SDK/Managed Agents separation; current default project/user feature loading differs from older cookbook guidance. |
| CASDK-S2 | [Configure permissions](https://code.claude.com/docs/en/agent-sdk/permissions) | Hooks, deny/ask/mode/allow decisions and canUseTool; allowed-tools lists are approval rules, not universal bypass-mode confinement. |
| CASDK-S3 | [Work with sessions](https://code.claude.com/docs/en/agent-sdk/sessions) | Continue/resume/fork and cross-host transcript stores; history forks do not isolate or revert filesystem effects. |
| CASDK-S4 | [Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents) | Programmatic scoped delegation and inherited context, limits and parent return; some orchestration features are TypeScript specific. |
| CASDK-S5 | [Intercept and control agent behavior with hooks](https://code.claude.com/docs/en/agent-sdk/hooks) | Pre/post tool and lifecycle callbacks; parallel pre-hooks use most restrictive denial, without ordered hook dependence. |
| CASDK-S6 | [Track cost and usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking) | Parent usage versus whole-tree model totals, resumed cumulative spend and output placeholders; USD is an estimate and crash recovery incomplete. |

#### ADK — Google Agent Development Kit

ADK offers first-class workflow coordination and repeatable agent evaluation. Its documentation explicitly exposes at-least-once replay, language-specific support and experimental skills instead of a universal safe-resume or semantic qualification guarantee.

Evidence boundary: Current official capability sources inspected. Evaluation tooling and production claims were not treated as measured effectiveness; no ordinary-task experiment was run.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| ADK-S1 | [Agent Development Kit (ADK)](https://adk.dev/) | Framework scope, open-source description and language entry paths; enterprise-scale positioning is not measured effectiveness. |
| ADK-S2 | [Build collaborative agent teams](https://adk.dev/workflows/collaboration/) | Parent-owned delegation, isolated branches and collected results; language/version mode restrictions and known limitations apply. |
| ADK-S3 | [Resume stopped agents](https://adk.dev/runtime/resume/) | Event-derived workflow completion resumption; tool execution is at least once and changed stopped workflows must not resume. |
| ADK-S4 | [Types of callbacks](https://adk.dev/callbacks/types-of-callbacks/) | Pre-agent/model/tool interception and error callbacks; exact return semantics and hook availability differ by language and agent class. |
| ADK-S5 | [Why evaluate agents](https://adk.dev/evaluate/) | Expected trajectories/reference responses, repeatable evals, regression and efficiency metrics; evaluation availability principally Python, some metrics require external service. |
| ADK-S6 | [Skills for ADK agents](https://adk.dev/skills/) | Progressive standard skill loading, source-file resources and validation; explicitly experimental with language-specific path/API support. |
| ADK-S7 | [Runtime Config](https://adk.dev/runtime/runconfig/) | Documents configured per-run LLM-call limits and language-scoped execution options; does not establish universal spend/token/runtime ceilings or cancellation semantics. |

#### OPENHANDS — OpenHands Software Agent SDK

A composable execution framework with first-class tool boundaries, durable conversations, subordinate tasks and reusable context. Its current SDK is assessed separately from the broader OpenHands ecosystem. Published SDK-linked experiments support bounded agent-task evidence, not constitutional-method or product-adoption claims.

Evidence boundary: Publisher reports measured OpenHands Index configurations, external discovery of Commit0 history leakage, a shallow-clone repair and changed rerun scores. This survey performed no experiment; model/configuration and benchmark scope limit interpretation.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| OH01 | [Software Agent SDK README](https://github.com/OpenHands/software-agent-sdk) | Selected framework purpose, native components, first use, repository boundaries and MIT license. |
| OH02 | [SDK Architecture Overview](https://docs.openhands.dev/sdk/arch/overview) | Agent/conversation/action-observation/workspace separation; optional sandbox/server package boundaries. |
| OH03 | [Security and Action Confirmation](https://docs.openhands.dev/sdk/guides/security) | Pre-action analyzers, UNKNOWN handling, confirmation/rejection and direct execute_tool bypass. |
| OH04 | [Persistence](https://docs.openhands.dev/sdk/guides/convo-persistence) | Persisted events, agent configuration/state, atomic base-state writes and multi-session restoration. |
| OH05 | [Task Tool Set](https://docs.openhands.dev/sdk/guides/task-tool-set) | Native subordinate tasks, persisted task identities, completion/error results and synchronous joins. |
| OH06 | [Context Condenser](https://docs.openhands.dev/sdk/guides/context-condenser) | Configured event-history thresholds and generated summaries; not proof of required-context capacity. |
| OH07 | [Metrics Tracking](https://docs.openhands.dev/sdk/guides/metrics) | Prompt/completion/cache/reasoning token metrics, accumulated cost and per-call latency. |
| OH08 | [Agent Skills and Context](https://docs.openhands.dev/sdk/guides/skill) | Source-located skills, progressive disclosure and deterministic path rules with local/ACP boundaries. |
| OH09 | [Analyzing and Improving the OpenHands Index](https://www.openhands.dev/blog/analyzing-and-improving-openhands-index) | SDK-linked benchmark traces, external Commit0 history-leak discovery, harness repair and rerun measurements. |
| OH10 | [Secret Registry](https://docs.openhands.dev/sdk/guides/secrets) | Rolling SDK docs: registered secrets are injected when referenced and masked in command outputs; broader exfiltration prevention is not claimed. |
| OH11 | [Goal Completion Loop](https://docs.openhands.dev/sdk/guides/convo-goal) | Rolling SDK docs: run_goal/GoalController own a hard max_iterations audit-round cap; each inner conversation/tool run remains a separate layer. |

#### LANGGRAPH — LangGraph

Strong durable graph orchestration with explicit state and replay boundaries. Formal semantic obligations and independent claim assurance remain composition responsibilities.

Evidence boundary: Source-based mechanism assessment only. No common runtime trial or controlled framework-level outcome experiment was found in the inspected sources; C23 is U.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| LG01 | [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) | Separates orchestration runtime from agent frameworks, harnesses and LangSmith; public minimal example. |
| LG02 | [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph) | Workflow-to-node design, raw shared data, error classes and human escalation. |
| LG03 | [Graph API overview](https://docs.langchain.com/oss/python/langgraph/graph-api) | State/context distinction, reducers, step bounds and structural migration caveats. |
| LG04 | [Subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs) | Explicit parent/child schema transforms, shared channels and checkpoint propagation. |
| LG05 | [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers) | Thread/checkpoint identity, pending writes, immutable state forks and durability mode boundaries. |
| LG06 | [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) | External-input suspension, approval routing and required idempotency around replayed nodes. |
| LG07 | [Memory](https://docs.langchain.com/oss/python/langgraph/add-memory) | Scoped namespace search and context trimming examples; database persistence requires configuration. |
| LG08 | [Test](https://docs.langchain.com/oss/python/langgraph/test) | Public pytest patterns for whole graphs, individual nodes and partial graph execution. |
| LG09 | [LangGraph publisher repository](https://github.com/langchain-ai/langgraph) | Public MIT license and separate Python/JS projects. |
| LG10 | [LangSmith evaluation types](https://docs.langchain.com/langsmith/evaluation-types) | Optional separate evaluation platform: reference datasets, code/model evaluators, regression and online evaluation. |
| LG11 | [Use the graph API](https://docs.langchain.com/oss/python/langgraph/use-graph-api) | Opened timeout/retry/concurrency sections: async-only attempt limits, buffered-write discard, no inherited subgraph defaults and maximum concurrent graph tasks. |

#### MAF — Microsoft Agent Framework

Current successor SDK with typed workflows, durable identity checks, reusable skills and core evaluation. Predecessor capability claims require migration verification.

Evidence boundary: Documentation and publisher-source assessment; no common installed-runtime trial or matched MAF outcome experiment. Predecessor research results were not transferred to MAF.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| MF01 | [Microsoft Agent Framework publisher repository](https://github.com/microsoft/agent-framework) | MIT license, public quickstarts, agents/workflows, middleware and separate Labs/hosting integrations. |
| MF02 | [AutoGen publisher repository](https://github.com/microsoft/autogen) | Explicit maintenance mode, community management, no new features, recommendation to migrate to MAF 1.0. |
| MF03 | [Semantic Kernel publisher repository](https://github.com/microsoft/semantic-kernel) | Identifies current MAF 1.0 production-ready successor and links migration resources. |
| MF04 | [Semantic Kernel and Microsoft Agent Framework](https://devblogs.microsoft.com/agent-framework/semantic-kernel-and-microsoft-agent-framework/) | Dated support policy: critical/security fixes retained, majority of new features focused on MAF. |
| MF05 | [AutoGen migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/) | Contrasts old Team/runtime APIs with typed workflows; current guide scopes MAF to single-process composition. |
| MF06 | [Semantic Kernel migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel/) | Concrete migration of agent/tool abstractions; does not make predecessor features automatically current MAF features. |
| MF07 | [Workflow checkpoints](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints) | Fresh-instance rehydration requires matching topology and stable executor identities; explicit storage choices. |
| MF08 | [Functional Workflow API](https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/functional) | Step caching, stable replay keys, concurrent-cache refusal and pending-request states. |
| MF09 | [Workflow human-in-the-loop](https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop) | Typed external request/response ports and approval-required tools before execution. |
| MF10 | [Agent Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills) | Progressive instructions/resources/scripts with file, inline, class and MCP sources. |
| MF11 | [Agent Security with FIDES](https://learn.microsoft.com/en-us/agent-framework/agents/security) | Experimental Python-only FIDES for direct agent tools. .NET and Monty/Hyperlight CodeAct nested calls/file/network capabilities lack enforcement; host policy remains required. |
| MF12 | [Evaluation](https://learn.microsoft.com/en-us/agent-framework/agents/evaluation) | Core local evaluators, expected outputs, workflow evaluation and CI checks; cloud provider is optional. |
| MF13 | [Agent observability](https://learn.microsoft.com/en-us/agent-framework/agents/observability) | Native OpenTelemetry token and time metrics, model/tool spans and configurable exporters. |
| MF14 | [Workflow observability](https://learn.microsoft.com/en-us/agent-framework/workflows/observability) | Workflow/executor spans and metrics augment model telemetry. |
| MF15 | [Adding Context Providers](https://learn.microsoft.com/en-us/agent-framework/journey/adding-context-providers) | Developer-selected context acquisition, token costs, staleness and silent-truncation caveats. |
| MF16 | [Workflow orchestrations](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/) | Sequential, concurrent, handoff, group-chat and manager coordination are separately scoped. |
| MF17 | [Agent Looping](https://learn.microsoft.com/en-us/agent-framework/agents/looping) | Experimental LoopAgent/AgentLoopMiddleware with configurable maximum invocations; not a shared token/spend budget, and packaged capability unavailable in Go. |
| MF18 | [Agent Background Responses](https://learn.microsoft.com/en-us/agent-framework/agents/background-responses) | Current provider-dependent background response/polling/stream-resumption behavior; client stream interruption does not establish remote termination. |

#### CREWAI — CrewAI

Explicit crews/tasks plus controllable flows, native skills, hooks and increasingly detailed recovery/resource APIs. Semantic assurance and effect reconciliation remain application work.

Evidence boundary: Current published mechanisms and examples only. CLI evaluation availability receives C21 credit; sample score tables do not establish achieved framework effectiveness, so C23 is U.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| CR01 | [CrewAI publisher repository](https://github.com/crewAIInc/crewAI) | OSS crews/flows purpose, MIT license and separate cloud/AMP offering. |
| CR02 | [Agents](https://docs.crewai.com/v1.15.27/en/concepts/agents) | Agent goals, tools, delegation, execution bounds and strict versus summarized context overflow. |
| CR03 | [Tasks](https://docs.crewai.com/v1.15.27/en/concepts/tasks) | Descriptions/expected output, assigned actors, task context, typed outputs and output guardrail retry limits. |
| CR04 | [Flows](https://docs.crewai.com/v1.15.27/en/concepts/flows) | Flow state/UUID, event routing, persistence forks and native full-run usage_metrics semantics. |
| CR05 | [Checkpointing](https://docs.crewai.com/v1.15.27/en/concepts/checkpointing) | Serialized execution/configuration/history with lineage, completed-task skipping; automatic writes are best-effort. |
| CR06 | [Human Feedback in Flows](https://docs.crewai.com/v1.15.27/en/learn/human-feedback-in-flows) | Paused feedback context, fresh-instance resume, routing outcomes and idempotent resume-handler guidance. |
| CR07 | [Skills](https://docs.crewai.com/v1.15.27/en/concepts/skills) | Native discovery/activation/resource stages; dynamically selected instructions are scoped to an execution. |
| CR08 | [Testing](https://docs.crewai.com/v1.15.27/en/concepts/testing) | CLI repeated crew runs and score/time reports; illustrated table is not a controlled outcome experiment. |
| CR09 | [Event Listeners](https://docs.crewai.com/v1.15.27/en/concepts/event-listener) | Native model/tool/memory/feedback lifecycle events and retrieval timing. |
| CR10 | [Tool Call Hooks](https://docs.crewai.com/v1.15.27/en/learn/tool-hooks) | Pre-tool interception can block execution; ordinary hook exceptions are swallowed, so blocking must use explicit abort semantics. |
| CR11 | [Crews](https://docs.crewai.com/v1.15.27/en/concepts/crews) | Crew/task composition and raw/typed/token/per-task output surfaces. |
| CR12 | [MCP Security Considerations](https://docs.crewai.com/v1.15.27/en/mcp/security) | Explicit metadata-injection/data-exposure risks, trusted-server and least-privilege guidance; server-side authentication/input validation/resource limits are external responsibilities. |

#### PYDANTIC — Pydantic AI

Typed core runtime with explicit deferred-tool and resource semantics. Evals, observability hosting and harness skills must remain separately scoped compositions.

Evidence boundary: Published APIs/guidance only. No installed common-runtime trial or matched framework outcome experiment. Separate eval-package capabilities do not establish achieved effectiveness.

| Source ID | Primary source / exact locator | Qualification |
| --- | --- | --- |
| PA01 | [Pydantic AI publisher repository](https://github.com/pydantic/pydantic-ai) | MIT license and repository separation of core, graph and eval packages. |
| PA02 | [Agents](https://pydantic.dev/docs/ai/core-concepts/agent/) | Run/dependency/output semantics, usage limits, per-request input checks, metadata and cancellation. |
| PA03 | [Agent Specs](https://pydantic.dev/docs/ai/core-concepts/agent-spec/) | YAML/JSON configuration distinct from code; template validation, schema settings and override/merge semantics. |
| PA04 | [On-Demand Capabilities](https://pydantic.dev/docs/ai/capabilities/on-demand/) | Selective instruction/tool bundles, stable capability IDs, history reconstruction and explicit exposure boundaries. |
| PA05 | [Multi-agent Applications](https://pydantic.dev/docs/ai/guides/multi-agent-applications/) | Typed delegation and handoff guidance, shared usage rollup, distinct model costs and Temporal-context caveat. |
| PA06 | [Durable Execution](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/) | Optional external engine integrations differ from conversation storage; one engine per agent is enforced. |
| PA07 | [Building a durable execution backend](https://pydantic.dev/docs/ai/capabilities/durable_execution/backends/) | Stable persisted operation names, codec boundaries, recovery tests and effect-before-checkpoint duplication caveat. |
| PA08 | [Deferred Tools](https://pydantic.dev/docs/ai/tools-toolsets/deferred-tools/) | Approval/denial and external results correlate tool-call IDs; approval is explicitly not client authentication/authorization. |
| PA09 | [Advanced Tool Features](https://pydantic.dev/docs/ai/tools-toolsets/tools-advanced/) | Tool preparation and argument validators; approval-required metadata preservation matters. |
| PA10 | [Unit testing](https://pydantic.dev/docs/ai/guides/testing/) | TestModel/FunctionModel, dependency/toolset overrides and prevention of accidental real-model calls. |
| PA11 | [Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/) | Separate package with case expected outputs, custom evaluators, datasets and experiments; not dependent on Pydantic AI. |
| PA12 | [Debugging and Monitoring / Logfire](https://pydantic.dev/docs/ai/integrations/logfire/) | Native OTel can operate without Logfire; token cache semantics and own-versus-delegate span aggregation are documented. |
| PA13 | [Version Policy](https://pydantic.dev/docs/ai/project/version-policy/) | Stable V2 release date and API/telemetry compatibility exceptions. |
| PA14 | [Harness Skills](https://pydantic.dev/docs/ai/harness/skills/) | Separate 0.x harness capability; explicit libraries, instruction-only loading and no permission boundary. |
| PA15 | [Pydantic AI overview](https://pydantic.dev/docs/ai/overview/) | Public installation/use orientation; runtime, optional harness and eval documentation surfaces remain distinguishable. |
| PA16 | [Durable Execution with Temporal](https://pydantic.dev/docs/ai/capabilities/durable_execution/temporal/) | Worker/capability identity constraints, replayed side-effect handlers and cross-process run-context limitations. |

## Recommended Action

Use this second-round rubric to choose and assess a composition for a defined outcome. Keep the common six principles as questions/commitments with their recorded standing; use the two candidate realizations as alternative designs, not merged law.

For STDO v3, the comparison supports five priorities:

1. Publish an ordinary task entry and source-linked reusable frame/skill representation that fresh actors can use without private author rescue.
2. Qualify the context-construction, refinement, conjunction, changed-basis and uncertain-effect relations through independent expected outcomes, including faulty guidance/oracles.
3. Bind runtime permissions, untrusted-input controls and operational budgets explicitly to the selected method obligations; expose every application-owned seam.
4. Complete the currently open independent assessments and post-repair confirmations before using their constructor/checker results as qualification evidence.
5. Run a matched predecessor/v3 trial with full resource accounting and independent adequacy judgment before asserting improved effectiveness, lower cost or universal recoverability.

These are research recommendations in commentary. The post does not alter common specifications, tickets, code, installed releases, acceptance records or either tenant's construction subject. The historical v2 matrix and workbook remain intact.
