# STRATEGY: Axiomatic Context Over Prompt-as-Program

**Author**: Codex
**Date**: 2026-08-30T05:15:11Z
**Addresses**: Prompting-trend alignment of `STDO -> a_c -> a_c.STDO`
across Claude Fable 5 and GPT-5.6 Sol/Codex Ultra
**Status**: Historical commentary
**Authority**: Commentary only; this post selects no calculus, target profile,
carrier, model, artifact, or acceptance decision

## Claim

Current frontier-model prompting guidance supports the architectural direction
of Axiom Indexer.

Prompting is moving away from encoding the whole program in procedural prose.
The emerging pattern is:

```text
small invocation
  + structured external context
  + explicit authority and action boundaries
  + typed output contract
  + independent verification
```

`a_c.STDO` takes that pattern further. It makes the durable context an accepted,
content-addressed, source-reenterable semantic object rather than a prompt,
conversation summary, mutable memory note, or model-private representation.

Loading the assignment projection

```text
AP_v = (A|_v, V_A, v, H_v)
```

into an LLM context is axiomatic programming. The prompt becomes the invocation
of `v`; it is not where the constitutional program is restated.

This is a design thesis and evaluation target. It does not imply that a current
`a_c.STDO`, carrier, or Context Packet has been accepted.

## Model Terminology

GPT-5.6 Sol is a model. Codex Ultra is a multi-agent execution and orchestration
mode. They are separate controls:

```text
Sol   = probabilistic reasoner
Ultra = decomposition, parallel work and synthesis harness
```

The corresponding Axiom Indexer surfaces are different again:

```text
a_c.STDO = durable accepted semantic state
GTL      = carrier encoding of that state
ABG      = execution, event and runtime-truth owner
```

Neither stronger model reasoning nor multi-agent orchestration replaces a
shared external semantic substrate.

## The Three Operational Levels

### 1. Full STDO prose

STDO prose is the constitutional source and semantic recovery surface. It is
rich, legible and suitable for discovering missing law. Used as the ordinary
working context, however, it makes each model and each subagent reconstruct the
same semantic index probabilistically on every invocation.

The costs are repeated tokens, repeated interpretation, cross-run variance,
weak source addressability and divergent local compressions across agents.

### 2. `a_c.STDO`

`a_c` supplies the carrier-neutral signature, laws, permitted judgments and
lawful derivation relation. `a_c.STDO` is the accepted STDO program expressed
under that calculus, together with its source and selection relations.

The useful model context is not necessarily the entire raw index. It is:

```text
least frame projection of a_c.STDO
  + exact source fragments selected through re-entry
  + current task, workspace and evidence
  + exact activation and capability envelope
```

This is the expected prompt-context sweet spot. The model need not reconstruct
the constitution, but it can recover exact prose whenever compression alone is
insufficient.

### 3. ABG/GTL

GTL is a lossless carrier, not a semantic selector and not necessarily the most
model-readable rendering. A model-facing view may decode GTL into named records
and a small stable legend without changing the represented program.

ABG moves beyond prompt context. It owns applications, events, effects,
continuations, replay and runtime truth. At this level the LLM is one bounded
worker inside a typed system; it is no longer the system's memory or authority.

## Prompting-Trend Alignment

| Trend | Claude Fable 5 | GPT-5.6 Sol / Codex Ultra | `a_c.STDO` |
| --- | --- | --- | --- |
| Leaner instructions | Brief steering replaces long behavioral enumeration | State each instruction once and remove redundant prompt scaffolding | Prompt is a short traversal invocation; law lives in the accepted context and contracts |
| Durable context | Long-run memory and explicit state management | Cached context, persisted reasoning and repository instructions | Content-addressed, cross-model semantic state with exact source re-entry |
| Action boundaries | Explicitly constrain useful but unrequested action | Declare autonomy, approval and side-effect boundaries compactly | `F_P`, `F_D` and `F_H` have separate authority and stop relations |
| Structured inputs and outputs | XML document structure, metadata and schemas | Structured Outputs, tools and stable cached prefixes | Closed signature, typed model, provenance, projection and stop algebra |
| Verification | Ground progress in tool evidence and use fresh verifier agents | State success criteria and require tests or evidence | Construction, structural judgment and semantic acceptance remain distinct |
| Multi-agent consistency | Durable context across long-lived subagents | Ultra distributes independent work and synthesizes results | Every agent receives a projection of the same accepted parent index |

The alignment is architectural, not merely stylistic. Both vendors are moving
responsibility out of repeated prompt prose and into the harness: state,
schemas, tools, memory, evidence, boundaries and evaluation. Axiom Indexer
makes the semantic portion of that harness explicit and governable.

## Divergence

### Fable needs model-specific packet ordering

Anthropic recommends placing long documents before the query and instructions.
The current STDO semantic-compilation experiment places its terse task before
the full source population. That ordering should be treated as a Fable renderer
issue, not as calculus law.

A Fable-oriented envelope should use:

```text
stable system boundary
exact documents and metadata
accepted frame-purpose projection
operative task at the end
```

The source population should remain byte-identical. Only its transport envelope
and ordering are model-specific.

### Sol favors a stable prefix and dynamic tail

Sol's prompting and caching guidance favors stable context first and dynamic
material last. Normal consumption should therefore place the accepted index or
projection first, then exact supporting source fragments, then the current
`W`, intent, evidence and task.

This is compatible with the Fable ordering. One semantic Context Packet may
have separately qualified model renderings without acquiring different
meaning.

### Algebra can impose a decoding tax

Models are trained heavily on natural language and conventional code. Dense
custom symbols, URNs and tuple keys can be harder to use than the meaning they
compress. A model-facing transport outside `AP_v` may therefore include:

- one small stable legend derived from the exact carrier profile;
- readable record labels alongside exact identities;
- exact frame purpose and reason;
- direct source-reentry handles.

It must not include prose that merely restates every axiom. That would recreate
the prompt burden the index is meant to remove.

### Immutable semantic state is not experiential memory

Fable's cross-run lesson memory and Sol's persisted reasoning are mutable
operational aids. `a_c.STDO` is immutable accepted subject meaning. Progress,
observations, corrections and learned operational lessons belong in separate
memory or ABG occurrence/event surfaces.

### Model refusal is not calculus refusal

A provider API refusal, safety stop, timeout or tool failure is a transport or
execution observation. It cannot be silently mapped to the calculus's semantic
`hold`, `gap` or `refusal`. The invocation profile must preserve both relations.

## The Internal-Representation Question

An LLM may form a richer internal representation of prose during one
invocation than the external index presents. That does not make the internal
representation a Product substitute. It is opaque, transient, non-addressable,
non-reviewable, model-specific and unavailable to the next agent.

`a_c.STDO` should not try to replace latent reasoning. It should make the
accepted semantic state that must survive reasoning explicit.

If `a_c.STDO` performs worse than full prose, the first conclusion is that the
external representation system failed. Candidate causes include:

- semantic loss or mistyping during `F_P[v_compile]`;
- acceptance of a defective compression;
- an incomplete reference-frame projection;
- a model-hostile rendering;
- lost salience or examples that prose supplied through redundancy;
- unavailable or late source re-entry; or
- an evaluation that rewards structural validity rather than downstream
  Product quality.

Only after those causes are excluded would a superior model-private
reconstruction from prose be the supported explanation.

## Product Criterion

Level 2 must be non-inferior to level 1 on downstream Product quality and
superior on context management:

```text
Quality(a_c.STDO + projection + re-entry) >= Quality(full STDO prose)
ContextCost(a_c.STDO)                     << ContextCost(full STDO prose)
Variance(a_c.STDO)                        <  Variance(full STDO prose)
AuthorityErrors(a_c.STDO)                 <  AuthorityErrors(full STDO prose)
```

The controlled dogfood comparison is:

1. full STDO prose;
2. raw accepted `a_c.STDO`; and
3. frame-projected `a_c.STDO` plus exact source fragments.

Hold the model, effort, task, workspace and evaluator constant. Run Fable and
Sol separately. Test Ultra later as an independent orchestration factor.

Measure:

- downstream ABG/GTL correctness;
- constitutional and authority-boundary violations;
- dependency, constraint and contradiction detection;
- correct source re-entry;
- variance across fresh runs and models;
- input, reasoning and output tokens;
- latency and cost; and
- lawful holds instead of unsupported completion.

Option 3 is the Product hypothesis. Option 2 diagnoses whether the algebra is
intrinsically model-readable. Option 1 remains the source-authority baseline.

## Result

The prompting trend is:

```text
prompt as program          -> prompt as invocation
context window as memory   -> governed external semantic memory
each agent reinterprets    -> agents share one accepted projection
model self-certifies       -> independent construction, judgment and acceptance
```

`a_c.STDO` cannot contain more source truth than STDO. It can make accepted
STDO meaning substantially more usable by replacing repeated probabilistic
reconstruction with addressable, projectable semantic state.

The next evidence should come from computation and comparative dogfooding, not
from expanding the prompt or repeating the calculus in prose.

## External Prompting References

- [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [GPT-5.6 model and prompting guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [How OpenAI uses Codex](https://openai.com/business/guides-and-resources/how-openai-uses-codex/)
