# `obra/superpowers` vs `specification_methodology` — Feature Comparison

**Status**: Supplemental analysis
**Authority**: Pre-constitutional — comparative review, not specification.
**Date**: 2026-04-30
**Scope**: Side-by-side feature/product comparison of `github.com/obra/superpowers` (Jesse Vincent's Claude Code skills framework) against this repository's methodology stack.
**Relation**: Comparative input that may inform future repricing of how the methodology distributes, activates, and governs agent behavior. Does not change any constitutional surface.

## Executive Summary

The two artifacts assume different actor models, and almost every surface difference between them is downstream of that one assumption.

- **`obra/superpowers`** assumes a **human-assisted coder**. The human is the principal; the agent is an assistant inside an interactive session. Skills shape the collaboration so the human gets disciplined work without having to enforce discipline manually.
- **`specification_methodology`** assumes **agent-led product construction governed by ratified specification**, with humans entering at declared `F_H` gates per `ODD_METHOD`. Once intent, product, goals, and requirements are ratified, the agent traverses derivations under ABG runtime law, with humans approving, rejecting, or repricing rather than co-authoring each step.

That framing reorganizes the rest of the comparison:

- `superpowers` is rich at every step where the human and agent talk to each other: brainstorm questions, plan reviews, code-review loops, hard "user approval" gates inside skills. It optimizes the *interactive* experience.
- `specification_methodology` is rich at every step where the agent operates without continuous human supervision: trace closure, projection-over-events to detect drift, change classes for ratified repricing, multi-tenant `WHAT once / HOW many times` law. It optimizes the *autonomous-with-audit* experience.

Each could plausibly be used in the absence of the other, and they could plausibly be used together with a documented seam. But they are not competing answers to the same question. They are answering different questions:

- `superpowers` answers: "**how should this agent session go?**"
- `specification_methodology` answers: "**how does an automated coder produce a correct product across many sessions, audits, tenants, releases?**"

The strongest mutual learning opportunity remains: `specification_methodology` could borrow `superpowers`' distribution and auto-activation pattern (Skill tool + plugin marketplace) so its method documents activate per-task rather than relying on agents reading 11 standards manually. `superpowers` could borrow `specification_methodology`'s constitutional chain and `F_D`/`F_P`/`F_H` regime model to operate when the human is *not* the principal — though this is largely orthogonal to its design intent.

Below is the detail. The actor-model framing is treated explicitly in §2 before the side-by-side feature matrix; the rest of the document re-reads cleanly under that lens.

---

## 1. Actor Model — The Load-Bearing Distinction

### `superpowers` assumes a human-assisted coder

Read directly from the skill texts:

- `skills/brainstorming/SKILL.md` checklist (lines 24–34): "Ask clarifying questions — one at a time, understand purpose/constraints/success criteria … Propose 2-3 approaches with trade-offs and your recommendation … Present design in sections, get user approval after each section … User reviews written spec — ask user to review the spec file before proceeding."
- `skills/using-superpowers/SKILL.md`: "If CLAUDE.md, GEMINI.md, or AGENTS.md says 'don't use TDD' and a skill says 'always use TDD,' follow the user's instructions. The user is in control."
- `CLAUDE.md` (contributor guidelines): "Show your human partner the complete diff and get their explicit approval before submitting."
- README: "Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest. After you've signed off on the design, your agent puts together an implementation plan…"

Every load-bearing step is **a conversation turn between human and agent**. The agent's job is to make the human productive without forcing them to do the discipline-enforcement work themselves. "Without deviating from the plan you put together" — the plan is *yours*. Subagent-driven autonomy is bounded by a plan the human reviewed and signed off.

### `specification_methodology` + `ODD_METHOD` assumes agent-led automation under declared authority

Read from the standards:

- `SPEC_METHOD.md` Position: "In the age of LLMs, the system should primarily declare truths, structures, interfaces, constraints, and evidence surfaces, then let lawful processing derive and realize work from that declared surface."
- `ODD_METHOD.md` §5 Evaluator Regimes: `F_D` deterministic, `F_P` probabilistic (agent), `F_H` human. Three regimes; humans are one. Rule 4: "Evaluators attest contract satisfaction; operators perform work."
- `ODD_METHOD.md` §6 Recursive Runtime Contract: "selection chooses only from published lawful alternatives, … recursion progresses as tail-loop control over explicit continuation and child frontier, … parent truth is re-evaluated after rebind, … reset/reopen mints a fresh attempt identity."
- `ODD_METHOD.md` §1 Position: "let ABG own continuation and re-entry after each publish boundary; keep product commands and services as cooperative bounded-step subsystems that publish assets or evidence and return control to ABG; expose visible current state as projection over constructive history."

The actor model is the **graph-traversal runtime**: ABG iterates over published graph functions, dispatching `F_D`/`F_P`/`F_H` evaluators bound to each vector, admitting evidence, projecting state, and re-entering until convergence or lawful stop. Humans show up at declared `F_H` boundaries; the rest of the time the system is running.

This is why `specification_methodology` invests heavily in:

- **trace closure** (every shipping behavior must trace to constitutional authority — there's no human to re-justify the link in real time)
- **projection over events** (drift detection without continuous human supervision)
- **change classes and repricing** (typed re-entry points so the system knows where to come back to when something changes upstream)
- **multi-tenant law** (the same `WHAT` realized in many `HOW`s, with no human to manually port between tenants)
- **fixture portability and proof-last closure** (so closure claims survive when no human is in the loop to spot-check fixture coupling)

And it is why `superpowers` does not invest in any of those: the human in the loop carries that load by inspecting the diff, approving the plan, reviewing the spec.

### Where this actor-model split actually shows up

| Surface concern | `superpowers` (human-assisted) | `specification_methodology` (agent-led) |
|---|---|---|
| Who decides the design is acceptable? | The human reviewing the design doc | A ratified `requirement_reprice` or `design_reframe` ticket; the design must derive from requirements |
| Who detects drift? | The human noticing in conversation; the human re-reading | Projection over event log; delta computed automatically; gap analysis surfaces |
| Who handles unexpected state? | The human being asked questions in chat | `F_H` gate fires per declared regime; everything else is `F_D`/`F_P` admission |
| Who re-runs after upstream change? | The human starts a new session | Repricing class identifies the smallest lawful re-entry point; runtime restarts from there |
| Who maintains traceability? | The human, by writing good design docs and PR descriptions | Trace-closure law; missing traceability is a defect; ratification dates carry forward |
| Who decides when something is done? | The human reviewing code | Closure law in the ticket; `F_H` gate if declared; assurance fold over admitted evidence |
| Who writes the next plan? | The human starting the next conversation | Next vector selected by graph projection; next ticket triggered by gap analysis |

`superpowers`' tightest skills are exactly the ones a human IC would want during a session: brainstorming, planning, TDD, code review, branch hygiene, debugging. `specification_methodology`'s tightest method documents are exactly the ones an automated system needs in order to operate without human supervision: trace closure, change classes, projection law, repricing taxonomy, multi-tenant realization law.

### Implications

1. **`superpowers` cannot directly govern an autonomous coder.** The skills assume conversation turns. Without a human in the loop, "ask clarifying questions one at a time" has no answer. "Get user approval after each section" has no actor. `superpowers` could be adapted (the user persona substituted for an `F_H` gate or another agent), but that is a non-trivial reframe of the skill content.
2. **`specification_methodology` does not directly govern a one-session human-assisted coding experience.** It does not say what the agent should do mid-conversation when the human is sitting at the keyboard. It assumes the constitutional chain has been ratified separately and the agent is operating against it. A human IC asking "help me write a small feature" gets little direct guidance from the methodology — the methodology applies to the *product* the feature lands in, not to the per-session experience.
3. **The disagreements catalogued in §5 below** (TDD as iron law, single-project assumption, imperative vs declarative posture, granularity) all read more sharply under the actor-model frame. They are not arbitrary stylistic differences. Each is what a methodology *of that actor type* needs to be.

---

## 2. What Each One Is

### `specification_methodology`

Read from `README.md`, `specification/standards/`, and `strategy/README.md`:

- A **source-of-truth repository** for shared methodology. Other repositories (e.g., `abiogenesis`) install copies of `specification/standards/` into workspace-local locations like `.genesis/docs/standards/`, but those are distributions, not authority.
- Eleven ratified standard documents under `specification/standards/`:
  - `SPEC_METHOD.md` — philosophical baseline, constitutional chain, change classes, repricing, trace closure, fixture portability
  - `TICKET_METHOD.md` — durable work-item tracking complementary to `POSTING_GUIDE.md`
  - `POSTING_GUIDE.md` — commentary layer under `.ai-workspace/comments/`
  - `DESIGN_MODULE_METHOD.md` — design module discipline, projection-source coherence, Prime carriers, effect-shell
  - `ODD_METHOD.md` — graph-native ODD product law (GTL/ABG)
  - `UX_METHOD.md` — Elm-architecture-as-constitutional-UX-process
  - `RELEASE_METHOD.md` — release cuts
  - `IDENTITY_METHOD.md` — identity at boundaries
  - `WORLD_MODEL_METHOD.md` — world-model methodology
  - `WRITING_GUIDE.md`, `GLOSSARY_GUIDE.md` — writing and terminology
- **Templates** under `specification/standards/templates/` that downstream projects copy and customize: `INTENT_TEMPLATE.md`, `PRODUCT_TEMPLATE.md`, `GOALS_TEMPLATE.md`, `CLAUDE_TEMPLATE.md`, `AGENTS_TEMPLATE.md`, plus `requirements/`, `design/`, `build_tenants/`, `docs/` subtrees.
- A `strategy/` folder for pre-constitutional work that may graduate into `specification/`.
- A minimal `.claude-plugin/` registering one slash command, `/spec-refresh`.
- Versioned `releases/` (currently `v1.0.0` through `v1.3.0`).

### `obra/superpowers`

Read from `README.md`, `CLAUDE.md`, `skills/`, `commands/`, `hooks/`, and `package.json`:

- A **Claude Code plugin** (also packaged for Codex, Cursor, Gemini, opencode) that ships fourteen skill directories, three slash commands, one subagent definition, hooks, and a session-start script.
- The fourteen skills:
  - `using-superpowers` (kernel skill — establishes the Skill-tool invocation discipline)
  - `brainstorming` — pre-implementation design dialogue
  - `writing-plans`, `executing-plans` — plan composition and execution
  - `subagent-driven-development` — autonomous subagent work
  - `dispatching-parallel-agents` — parallel agent fan-out
  - `using-git-worktrees` — isolated agent workspaces
  - `test-driven-development` — TDD as iron law
  - `systematic-debugging` — disciplined debug loop
  - `verification-before-completion` — gate before claiming done
  - `finishing-a-development-branch` — branch hygiene
  - `requesting-code-review`, `receiving-code-review` — code-review loop
  - `writing-skills` — meta-skill for new skill authoring
- Three slash commands: `/brainstorm`, `/write-plan`, `/execute-plan`.
- Hooks: `hooks.json` config, a Cursor variant, a session-start script, a Windows hook runner.
- One subagent: `code-reviewer`.
- A self-imposed contribution discipline: 94% PR rejection rate; PR template enforcement; "no third-party dependencies" rule; "no compliance changes to skills without eval evidence".

---

## 3. Side-By-Side Feature Matrix

| Dimension | `specification_methodology` | `obra/superpowers` |
|---|---|---|
| **Primary unit** | Method document (constitutional standard) | Skill (behavioral trigger) |
| **Primary authority claim** | Specification as source; code derives from it | Skill invocation as mandatory; "you do not have a choice" |
| **Audience** | Methodology author + downstream projects vending the standards | Anyone using a coding agent |
| **Lifecycle scope** | Full SDLC: intent, product, requirements, design, realization, ticket tracking, posting, release, projection, repricing | Code-execution loop: brainstorm, plan, TDD, debug, review, branch hygiene |
| **Constitutional model** | Yes — explicit constitutional chain, repricing classes, ratified vs strategic surfaces | No — skills are imperative behavioral mandates without ratification ceremony |
| **Change-class taxonomy** | Six explicit classes: `goal_reprice`, `intent_reprice`, `product_reprice`, `requirement_reprice`, `design_reframe`, `realization_refactor` | None |
| **Tenant / multi-realization model** | Yes — `build_tenants/<family>/<variant>/` law for one shared `WHAT` realized in many `HOW`s | No — single project assumed |
| **Recursive product taxonomy** | Yes — Source Project / Release Cut / Product / Install / Artifact | No |
| **Trace closure law** | Yes — every requirement → design → code; missing traceability is a defect | No — TDD law substitutes for trace closure at the code/test level only |
| **Activation model** | Implicit — agents read the standards and apply them; one slash command (`/spec-refresh`) | Explicit — Skill tool invocation; auto-trigger via skill description matching; "1% chance a skill applies → invoke it" |
| **Distribution** | Source-of-truth repo; downstream installers vend copies; minimal Claude Code plugin (1 command) | Multi-platform plugins: Claude Code marketplace (official + obra), Codex CLI, Codex App, Cursor, Gemini, opencode |
| **Granularity** | 11 high-level method documents + templates | 14 narrow skills + 3 slash commands + 1 subagent + hooks |
| **Hooks / lifecycle integration** | None | Yes — `hooks.json` for Claude Code, Cursor variant, session-start script |
| **Subagent / parallel-agent support** | None native (downstream products may model it) | Yes — `dispatching-parallel-agents`, `subagent-driven-development`, `using-git-worktrees` |
| **Code-review model** | Implicit (POSTING_GUIDE for commentary; ratification for live surfaces) | Explicit — `requesting-code-review` / `receiving-code-review` skills + `code-reviewer` subagent |
| **TDD discipline** | Acknowledged at testing-strategy level (design/module vs UAT/acceptance) without iron-law strictness | Iron law: "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST. Write code before the test? Delete it. Start over." |
| **Spec/design artifact location** | Project-defined via templates (`PRODUCT.md`, `requirements/`, `design/`) | Hard-coded: `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` |
| **Versioning / releases** | Yes — `releases/v1.0.0..v1.3.0.md` with cut notes | Yes — `RELEASE-NOTES.md`; `package.json` version `5.0.7` |
| **Self-extensibility** | `WRITING_GUIDE.md` + standards templates; method stacking (`SPEC_METHOD ← ODD_METHOD ← UX_METHOD`) | `writing-skills` skill governs new-skill authoring; standalone-plugin model for domain-specific extensions |
| **Stance toward agents** | Declarative — "let lawful processing derive and realize work from declared surface" | Imperative — "you DO NOT have a choice. You MUST use it." |
| **Stance toward LLM era** | "In the age of LLMs, the system should primarily declare truths, structures, interfaces, constraints, and evidence surfaces" | "Skills override default system prompt behavior; user instructions always take precedence" |
| **Maturity signal** | 5 numbered releases; multi-amendment-history per method; ratification dates throughout | 94% PR-rejection rate self-claim; AI-agent contribution discipline; vendored test suite |

---

## 4. Where They Agree

Both share a small and important set of philosophical positions:

- **Spec/design before code.** `superpowers`' brainstorming → planning → implementation gate is morally identical to `SPEC_METHOD.md`'s "design must be derivable from requirements" rule, applied at session granularity. Both forbid jumping straight to code.
- **User-instructions outrank methodology.** `superpowers` `using-superpowers` skill states: "If CLAUDE.md, GEMINI.md, or AGENTS.md says 'don't use TDD' and a skill says 'always use TDD,' follow the user's instructions. The user is in control." `SPEC_METHOD` has the same disposition through repricing and the constitutional chain — methodology serves the project, not the other way around.
- **Methodology is contestable.** `specification_methodology` requires repricing for material changes; `superpowers` requires "extensive eval evidence" to modify behavior-shaping content. Both treat methodology as serious software, not casual prose.
- **Trace artifacts.** Both produce durable artifacts beyond the running agent: `specification_methodology` produces ratified specs and design records; `superpowers` produces design docs at known paths and plan files committed to repo. Neither relies on the agent's volatile memory.
- **Stand against speculative work.** `superpowers` "Speculative or theoretical fixes" and "Bulk or spray-and-pray PRs" rules are functionally `SPEC_METHOD.md`'s anti-drift rules at session level.

---

## 5. Where They Disagree

### 4a. TDD as iron law vs as one of many testing strategies

`superpowers/skills/test-driven-development/SKILL.md` says:

> NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
> Write code before the test? Delete it. Start over.

`SPEC_METHOD.md` (2026-04-24 amendment) takes a softer position:

> Testing strategy taxonomy made explicit: design/module tests prove realization conformance; UAT/acceptance tests derive from requirements and scenarios and must run as sandbox or equivalent composed-product proof, split into harnessed and live lanes.

These are not strictly incompatible — `SPEC_METHOD` admits TDD as a valid realization discipline at the design/module layer — but `superpowers` makes TDD the *only* admissible path, while `SPEC_METHOD` admits multiple test types whose composition satisfies the verification obligation. A team using both would need to declare which discipline owns the test layer in a given tenant.

### 4b. Single-project agent vs multi-tenant ratified product

`superpowers` assumes a project IC with one repo and one agent session at a time. The brainstorming skill writes to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` — a hard-coded single location.

`specification_methodology` is built for products that ratify shared `WHAT` and realize `HOW` across many tenants under `build_tenants/<family>/<variant>/`. Templates assume `PRODUCT.md`, `INTENT.md`, `GOALS.md`, `requirements/`, `design/`, `build_tenants/` with multiple HOW realizations. A `superpowers`-only team has no native model for "Python tenant" + "TypeScript tenant" of the same product; a `specification_methodology`-only project has no native model for "what should the agent's per-session brainstorming workflow look like."

### 4c. Imperative behavioral mandate vs declarative authority

`superpowers/skills/using-superpowers/SKILL.md`:

> If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.
> IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

`SPEC_METHOD.md`:

> Imperative procedure still exists, but it is subordinate to declared authority. […] In the age of LLMs, the system should primarily declare truths, structures, interfaces, constraints, and evidence surfaces, then let lawful processing derive and realize work from that declared surface.

These are different theories of agent governance. `superpowers` shapes per-utterance behavior. `specification_methodology` shapes the constitutional environment the agent operates in and trusts the agent to derive correct behavior from declared truth. The one that is "right" depends on the failure mode you fear most:

- If you fear agents skipping methodology steps, `superpowers`' imperative bite is stronger medicine.
- If you fear methodology drift / unratified change / loss of trace, `specification_methodology`'s constitutional posture is stronger medicine.

### 4d. Granularity of methodology unit

`specification_methodology` has eleven big methods; `superpowers` has fourteen narrow skills. The size of each unit reveals the design philosophy:

- A `specification_methodology` standard is read once, internalized, and cited from many tickets. `SPEC_METHOD.md` is ~400 lines of constitutional law that governs hundreds of subsequent ratifications.
- A `superpowers` skill is invoked per task. `test-driven-development/SKILL.md` is invoked literally every time the agent writes production code.

This is the same trade-off seen in language design: few large mandates vs many small triggers.

### 4e. Treatment of "what comes before code"

`specification_methodology` treats *intent → product → goals → requirements → design → code* as a chain of separate first-class artifacts, each ratified, each subject to its own change class.

`superpowers` collapses this into one phase called "brainstorming" that produces one design doc. There is no separate intent layer, no product-definition surface, no requirements stage, no goals layer. The brainstorming skill is rich (8 files in the directory, with checklist, process flow, anti-patterns) but it is a single-shot at the entire pre-code phase.

A team using `superpowers` for a multi-quarter product would feel this gap quickly: where do durable goals and intent live? Where does the SPEC_METHOD's "Goals → Intent → Product Definition → Requirements" chain land? `superpowers` answers "in your head, plus one design doc per task." `specification_methodology` answers "in `INTENT.md`, `PRODUCT.md`, `GOALS.md`, `requirements/*` — each ratified."

### 4f. Distribution and activation

`specification_methodology` distributes by file copy (downstream installers vend the standards tree). Activation is by the agent reading the standards and applying them.

`superpowers` distributes by Claude Code plugin marketplace (and Codex/Cursor/Gemini equivalents). Activation is automatic — the Skill tool surfaces relevant skills, and skill descriptions trigger invocation.

This is the most asymmetric capability gap. `specification_methodology`'s `.claude-plugin/` exposes one slash command. `superpowers`' plugin shape is far more developed: 14 skills auto-discoverable, 3 slash commands, hooks, subagent, session-start script. A user with `specification_methodology` installed must remember to apply it; a user with `superpowers` installed has the methodology activate without having to remember.

### 4g. Code-review and verification

`superpowers` has a complete code-review loop: `requesting-code-review`, `receiving-code-review`, `code-reviewer` subagent, `verification-before-completion` skill. This is a production-grade per-session quality gate.

`specification_methodology` has no native code-review surface. It has `POSTING_GUIDE.md` for commentary and ratification-by-supersession for constitutional surfaces. Code review at the realization layer is left to downstream projects.

### 4h. Subagent and parallel-agent support

`superpowers` has three skills devoted to multi-agent orchestration: `dispatching-parallel-agents`, `subagent-driven-development`, `using-git-worktrees`. The README claims "It's not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan."

`specification_methodology` has no native subagent or parallel-agent model. (The downstream `abiogenesis` substrate models attached F_P workers, but that is product-level, not method-level.)

---

## 6. Strengths and Weaknesses

### `specification_methodology` strengths

1. **Comprehensive constitutional coverage of the SDLC.** The Goals → Intent → Product → Requirements → Design → Code chain is thoroughly modeled, with explicit change classes for every layer.
2. **Multi-tenant law.** Build-tenants/ governance handles `WHAT once, HOW many times` natively. No competitor in this comparison addresses this.
3. **Repricing taxonomy.** Six explicit change classes (`goal_reprice` through `realization_refactor`) give every methodology change a typed re-entry point.
4. **Method stacking.** `SPEC_METHOD ← ODD_METHOD ← UX_METHOD` and `SPEC_METHOD ← TICKET_METHOD/POSTING_GUIDE` allow specialization without rival authorities.
5. **Trace closure law.** Missing traceability is a first-class defect. Every shipping behavior must trace to constitutional authority.
6. **Long-horizon stability.** Method documents have multi-amendment histories spanning months, with ratification dates per amendment.

### `specification_methodology` weaknesses

1. **High activation cost.** Eleven standard documents must be ingested before producing first artifacts. Agents and humans both face a tall first read.
2. **No native per-session execution discipline.** TDD, debugging, code review, branch hygiene, parallel-agent dispatch are not addressed at method level. Downstream projects must invent these.
3. **Implicit activation.** No tool-driven mechanism to ensure agents apply the methodology. Reliance on `CLAUDE.md`/`AGENTS.md` referencing the standards manually.
4. **Plugin shape is minimal.** One slash command. The auto-activation patterns proven by `superpowers` and similar frameworks are not yet adopted.
5. **No subagent / parallel-agent / worktree model.** Multi-agent autonomy is left entirely to downstream products.
6. **Heavy ceremony for small changes.** Constitutional ratification is overhead-intense. May discourage small but useful methodology updates.

### `superpowers` strengths

1. **Auto-activating skills.** Skill descriptions trigger invocation; the user does not need to remember to apply methodology.
2. **Tight code-execution loop.** Brainstorm → plan → TDD-implement → review → finish covers the full per-session journey with strong guard rails.
3. **Multi-platform distribution.** Claude Code (official + community), Codex CLI/App, Cursor, Gemini CLI, opencode all supported from one repo.
4. **Subagent-driven autonomy.** "Hours of autonomous work without deviating from the plan" claim, backed by `subagent-driven-development`, `dispatching-parallel-agents`, `using-git-worktrees`.
5. **Strong PR / contribution discipline.** 94% rejection rate, PR template enforcement, "speculative fixes will be closed" — methodology takes itself seriously enough to refuse low-quality contributions.
6. **Iron-law TDD.** Removes ambiguity from a recurring debate.
7. **Code-review loop built in.** `requesting-code-review` / `receiving-code-review` + `code-reviewer` subagent.

### `superpowers` weaknesses

1. **Code-execution loop only.** Nothing above code: no requirements layer, no intent, no product definition, no release method, no goals layer.
2. **Single-project assumption.** Hard-coded design path `docs/superpowers/specs/YYYY-MM-DD-*`; no multi-tenant model.
3. **No constitutional / repricing model.** When methodology disagrees with skill, conflict resolution is by precedence rule (user > skill > default), not by ratified change class.
4. **Imperative posture clashes with declarative agent design.** Some teams will find "you DO NOT have a choice" too coercive. (Some will find it exactly right; the friction is real.)
5. **Domain-specific skills are exiled to standalone plugins.** No native composability for product-specific extensions inside core.
6. **TDD as universal mandate** may not fit every codebase (legacy, exploratory, generated, infrastructure).
7. **Brainstorming is a single phase.** Long-running products with goals → intent → product → requirements would feel collapsed into "design doc per task."

---

## 7. Compatibility / Coexistence

The two are mostly orthogonal and could coexist in one workspace.

**Plausible composition pattern:**

- `specification_methodology` governs the constitutional layer: `INTENT.md`, `PRODUCT.md`, `GOALS.md`, `requirements/`, `design/`, `build_tenants/` realization, ticket tracking, posting, release.
- `superpowers` governs the per-session execution layer: brainstorm-to-design, plan-then-execute, TDD, code review, branch hygiene.

**Seam:** `superpowers/skills/brainstorming` writes to `docs/superpowers/specs/YYYY-MM-DD-*-design.md`. In a `specification_methodology` project this would be a *commentary surface* under `.ai-workspace/comments/` per `POSTING_GUIDE.md`, not a design artifact under `design/`. The brainstorming output becomes input to a `requirement_reprice` or `design_reframe` ticket, which is the lawful authoring path under `TICKET_METHOD.md`. The `superpowers` design doc satisfies the *one-design-doc-per-task* requirement at session level, but does not satisfy `SPEC_METHOD`'s trace-closure obligation on its own — the ratified design surface still has to land under `specification/` or under `build_tenants/<tenant>/design/`.

**Conflict points to declare in `CLAUDE.md` if both are active:**
- TDD strictness: pick one. Either `superpowers`' iron law applies, or `SPEC_METHOD`'s testing-strategy taxonomy applies.
- Design-doc location: `superpowers` writes to `docs/superpowers/specs/`; `specification_methodology` design lives in `specification/` or `build_tenants/<tenant>/design/`. Reconcile by treating `superpowers` outputs as commentary that informs ratified design.
- Activation precedence: per `using-superpowers`, the user's `CLAUDE.md` outranks any skill. So a `CLAUDE.md` clause stating "use SPEC_METHOD TDD policy" defeats `superpowers`' iron-law TDD when in conflict.

---

## 8. Mutual Learning Opportunities

### What `specification_methodology` could learn from `superpowers`

1. **Auto-activating skills as a delivery mechanism for method documents.** Currently the standards rely on agents manually reading them. A `specification_methodology` plugin with skills like `applying-spec-method`, `applying-ticket-method`, `posting-commentary`, `running-design-module-method`, etc., would make the methodology activate per-task rather than rely on read-and-remember. Skill descriptions could trigger on context (e.g., "when writing a ticket frontmatter," "when posting a review," "when tightening a design module").
2. **Plugin distribution.** A real Claude Code plugin (and Codex/Cursor/Gemini equivalents) would make `specification_methodology` adoption a one-command install rather than a vendor-the-standards-tree exercise.
3. **Per-session execution methodology.** The TDD, debugging, code-review, verification, branch-hygiene skills cover the gap between "ratified design exists" and "code lands." The methodology could either adopt these directly (vendor-friendly) or extend by reference (cleaner authority).
4. **Hooks integration.** A `session-start` hook that ensures the agent reads `INTENT.md` / `PRODUCT.md` / `GOALS.md` before producing first response would be a small but high-leverage addition.
5. **Subagent / parallel-agent model.** `dispatching-parallel-agents` + `using-git-worktrees` is exactly the substrate `abiogenesis` is reaching for at the runtime layer. Promoting it into method authority avoids each downstream project reinventing it.

### What `superpowers` could learn from `specification_methodology`

1. **Constitutional layer above code.** Adding intent, product, goals, requirements, release as first-class layers (even as optional skills) would let `superpowers` cover product-construction work, not just per-session execution.
2. **Repricing / change-class taxonomy.** Six change classes give methodology drift a typed re-entry surface. `superpowers` currently handles methodology updates by PR template + eval evidence; a typed change class would let core skill changes be ratified rather than re-evaluated each time.
3. **Multi-tenant / multi-realization model.** Hard-coding `docs/superpowers/specs/` rules out the `WHAT once, HOW many times` pattern. A tenant abstraction would broaden applicability.
4. **Method stacking.** `SPEC_METHOD ← ODD_METHOD` shows how a domain can refine a baseline method. `superpowers` could specialize for graph-native, ML-systems, distributed-systems, etc., without polluting core.
5. **Posting / commentary layer.** The 94% PR rejection rate suggests the value of a "this is commentary, not law" surface for half-baked thoughts. `POSTING_GUIDE.md` describes exactly that.
6. **Trace closure law.** TDD covers code-to-test traceability, but not requirement-to-code or design-to-code. Adding a generic trace-closure guard would catch a wider class of drift.

---

## 9. Recommendation Posture

This document is pre-constitutional analysis. It does not change any standard. If any of the mutual-learning opportunities are worth pursuing, the lawful path is:

- **From `specification_methodology` side**: open a candidate strategy artifact (here in `strategy/`) for "method-as-skills delivery," prototype the skill mappings, and graduate it through the `strategy/README.md` graduation path if it stabilizes. Likely candidates that would graduate cleanly: a `methodology-as-plugin` strategy doc, a `per-session-execution-methodology` strategy doc, and a `subagent-and-parallel-agent-dispatch` strategy doc.
- **From `superpowers` side**: not actionable from this side. `obra/superpowers` is upstream; we are downstream. We can adopt patterns; we don't ratify changes there.

The most valuable single action this analysis suggests for *this* repository is to evaluate whether shipping `specification_methodology` as a richer Claude Code plugin (skills + commands + hooks) — rather than the current minimal one-command shape — would meaningfully reduce activation cost for downstream agents. That evaluation belongs in its own `strategy/` artifact, not in this comparison.

---

## Closing

`obra/superpowers` and `specification_methodology` are good neighbors, not rivals. Both treat methodology as serious; both produce durable artifacts beyond the running agent; both subordinate methodology to user intent. They differ on which layer of the stack they govern (constitutional vs behavioral) and on which discipline they bring (declarative vs imperative). A team that adopted both, with a small reconciliation clause in `CLAUDE.md`, would have a stronger overall methodology than either alone — and the experience of running with `superpowers` for a sprint would generate concrete evidence about which of its patterns deserve to be adopted into `specification_methodology`'s plugin and skills layer.
