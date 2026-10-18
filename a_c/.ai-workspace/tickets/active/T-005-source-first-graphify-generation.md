# T-005 Source-first Graphify representation generation

Status: bounded dogfood construction and independent fidelity assessment
complete. Owner correction supersedes T-004 as the answer to the
representation-generation question; T-004 remains frozen evidence about
consuming already-authored representations. Product acceptance and release are
outside this completed increment.

## Owner instruction and basis

Jim clarified: `stdo/V3/{claude, codex} -> a_c.graphify -> generate the
representation`, and that a Graphify implementation of a_c should facilitate
creation. He explicitly selected the most recent cuts because they have
iterated and repaired issues. This authorizes the missing source-first
generation workflow and fresh local construction using existing CLI
authentication. The work remains dogfood; no RC, acceptance, publication or
V3 dependency is selected.

The independent a_c Product Definition selects installed STDO v2.5.1-rc.2,
manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
Its status/manifest verification passed on 2026-10-18. Each V3 corpus is a
subject; its own calculus document does not replace this implementation basis.

Latest clean inputs selected at 2026-10-18 02:12 UTC:

- Codex RC5 package `5a5b5ad80f0ba4b56b83aadd42ac130de53ba803`, custody HEAD
  `87512593de6ec60660f2ad9e040241d67a4108d7`; successor source unchanged
  between package and custody checkpoints.
- Claude candidate 8 / RC8 source `9aee01ffa76cfbde1a6b8f1153a25bd6d71c216e`,
  custody HEAD `1db13bfeb0675fc95de04aceccb214f5b76873fc`; source standards
  and plugin unchanged between source and custody checkpoints.

Acquire immutable Git blobs, not mutable worktrees. Semantic generation inputs
are standards owner documents, schemas and templates, excluding derived
`frames/`, `authority_compressions/` and `verification_material/`.
Existing a_c interpretations, compiler accounts, maps, signatures, coverage,
reviews and old trial answers are excluded from generation input.

## Outcome and boundary

Provide a generic tenant-owned source creation path:

`exact source corpus -> Graphify structural + F_P semantic extraction -> real
upstream source graph -> fresh F_P a_c authoring -> structural validation ->
source-linked proposed a_c model and graph`.

F_P belongs inside this workflow. The owner does not require another compiler
to first create the semantic model. Graphify discovery confidence and inferred
edges are not automatically normative a_c relationships. Exact source remains
the deciding basis. Preserve per-source/section dispositions, applicability,
exceptions, latitude, unresolved meaning and incomplete work explicitly.

Existing transport mechanics remain available and unchanged. The generic
generation code has no knowledge of V3 paths or Product composition. A separate
dogfood client supplies the two frozen source corpora. Fresh direct-source
authoring under the same output contract is the control for any new causal
generation comparison; T-004 cannot establish generation quality or cost.

## Activations and territories

- Executive `/root` binds outcome, source cuts, protocol and results; no effects
  while acting as Executive.
- Writer `/root` owns this ticket, `a_c/dogfood/stdo-v3-generation/`, generation
  scope clarifications in common Product/requirements, and completion links in
  a_c README/Goals and tenant README generation commands. No Git, V3,
  old-study answer/grade/freeze, or original
  representation effects are granted.
- Read-only `/root/ac_generation_sources` resolved latest exact input cuts and
  custody; `/root/ac_generation_design` assessed actual source-generation APIs,
  source/calc boundaries and implementation traps. Their initial results are
  consumed before implementation.
- Writer `/root/ac_generation_sources` additionally owns only the new dogfood
  `freeze_sources.py`, `corpora/{codex,claude}/` and
  `evidence/source-custody.json`. Freeze the selected Git blobs and verify
  custody; no candidate or Git effects. `/root/ac_generation_design` is
  activated for read-only common-contract/code preflight and source-first
  scope assessment before real actor launches.
- Worker `/root/ac_generation_implementation` owns only tenant
  `code/ac_generate.py`, dedicated `code/generation/` schema/prompt helpers,
  `test_env/test_ac_generate.py` and `design/generation.md`. Implement generic
  source-first Graphify creation plus a direct control and immutable per-chunk
  run/usage evidence. Existing codec, fixtures, common source and V3 are read-only.
  No LLM actor launches before protocol and code preflight.
- Writer `/root` may run isolated CLI-authenticated source-generation sessions
  in fresh run directories after preflight, retaining all prompts, usage,
  failures and checkpoints. No global configuration/install or new paid provider.
  The existing ignored `a_c/.venv/` may receive local generation/verification
  dependencies. Its `numpy==2.2.6` and `rapidfuzz==3.13.0` additions support the
  real pinned upstream `build()` import path and are recorded in environment
  evidence; the ordinary codec remains unchanged.
- Nonauthor review receives separately bounded read-only source/code/output
  authority. Semantic assessment does not accept its own subject.
- Source-only oracle Writer `/root/ac_generation_oracle` owns only
  `private/source-probes.json` and `private/SOURCE_PROBES.md` in the new dogfood
  root. Before generated answers exist, select six material fidelity probes per
  candidate from exact owner source, retaining candidate-specific laws. This
  ledger is withheld from generation actors and assesses only bounded meaning
  conservation, not whole-method acceptance.

## Required evidence

Verify exact source inventory and exclusions; source chunk coverage; raw
Graphify extraction outputs and actual pinned upstream identity; fresh F_P
drafts and their exact documentary grounding; generated model structural
validation and proposal graph recovery; retained failure/partial-work states;
actual usage/timing separated by extraction/authoring/encoding; independent
implementation review. State interpretation-fidelity and coverage limits.

No old retrieval result supplies a generation verdict. No generation,
validation, source quotation, graph path or coverage ledger grants semantic
acceptance, complete calculus conformance, methodology acceptance or release.

## One-pass authoring refinement

The two-pass synthetic whole-path smoke succeeded from raw source: actual
Graphify concept extraction/build, fresh a_c authoring, checked proposal and
actual upstream carrier recovery. Its code/assets and frozen plans are retained
under `archive/two-pass-prototype/` and `smoke/`; no V3 actor ran under those plans.

Before full-corpus actors, independent design assessment established that two
semantic passes are an engineering choice, not a calculus or owner requirement.
The active creation/comparison uses `graphify-ac`: actual deterministic
Graphify source structure, ONE a_c-aware F_P extraction/authoring pass, then
checked a_c/Graphify representation. The matching direct control also has one
F_P pass. This is a custom tenant extraction profile, with the same authored
normative fields, not a claim to run the stock generic Graphify semantic prompt.

The implementation Worker's existing territory is activated for that bounded
mode extension, actual-upstream tests and design update. Root Writer owns
`PROTOCOL-V2.md`, `EXECUTION-V2.md`, separate `runs-v2/` and `freeze-v2.json`;
old frozen evidence stays unchanged. The nonauthor code reviewer must close
the affected launchgate before a one-pass smoke and full-corpus actors.

## Separate grounding recovery increment

After the four first-chunk drafts, both Codex drafts passed the frozen strict
checker. The Claude Graphify draft failed on changed indentation inside a
quotation; the direct draft named a section outside its chunk. All raw answers,
failures and measured usage remain immutable. No v2 plan, prompt, schema,
generator or original result is replaced by this increment.

Worker `/root/ac_generation_implementation` additionally owns only
`build_tenants/graphify/code/ac_grounding.py`, its dedicated
`test_env/test_ac_grounding.py`, and `design/grounding.md`: implement separately
qualified F_D source-locator recovery and proposal assembly. The operation may
change only quotation whitespace and line coordinates within the same exact
supplied section, with a unique whitespace-run-equivalent source occurrence and
unchanged non-grounding payload. `/root/ac_generation_design` independently
reviews that contract, implementation and provenance before use. No actor
launches or frozen-code changes are granted to this Worker increment.

Root Writer additionally owns the separate dogfood addendum, coordinator,
grounding evidence and result summaries under `dogfood/stdo-v3-generation/`.
The coordinator may dispatch remaining chunks and supported repair attempts
through the unchanged frozen actor functions with the same settings, schema,
source and treatment context. It must preserve at most four concurrent actors,
three total F_P attempts per chunk, every initial failure and actual usage.
It must not relabel mechanically recovered drafts as first-pass successes.

## Implementation preflight checkpoint

At 2026-10-18 03:04 UTC, source authoring generator `7002a794…`, unchanged core
codec `2f5de4d6…`, final grounding helper `bd60bb9e…` and coordinator `025c30ba…`
passed their bounded nonauthor preflight. Root independently ran all 91 tenant
tests with actual upstream Graphify `fe085ced…`; all passed. Exact identities,
test log and review scope are retained in the generation study evidence and
`grounding-freeze-final.json`. The first grounding snapshot was withdrawn before
use after a late integrity delta; its retained status names that event.

Both Codex first drafts pass strictly. Both Claude first drafts remain refused
because a grounding section identity contains a revision typo; a unique-source
whitespace operation cannot change that identity. The next Codex Graphify drafts
yield one strict pass and one mechanically recovered quotation/range, with all
authored meaning unchanged. Full generation, fresh retries where necessary,
bounded independent semantic assessment and resource comparison remain active.
This closes implementation preflight only; no model or Product is accepted.

## Bounded F_P grounding repair

The owner-authorized creation workflow also needs a supported repair path:
multiple closed drafts contain one or a few defective citations, while their
authored meaning fields are schema-valid. Repeating the entire interpretation
would spend another large output on source coordinates. The frozen initial
generator, source chunks, original authoring contract and existing F_D recovery
remain unchanged; initial outcomes stay in the paired evidence.

Worker `/root/ac_generation_implementation` is activated for new generic tenant
files only: `code/ac_repair.py`, a separate `code/grounding_repair/` prompt/schema
directory, `test_env/test_ac_repair.py` and `design/grounding_repair.md`. This
increment may ask a fresh isolated F_P actor to repair explicitly named grounding
entries using the same exact dispatched source and treatment discovery context.
It may change grounding section IDs, quotes and line coordinates, but must prove
every other authored value/order unchanged. It must refuse unsupported errors,
unknown patch paths, ambiguous/missing author targets, stale custody, semantic
field changes, failed actor isolation and unsupported incomplete evidence. It
must retain original and repair calls/answers/provenance/usage, apply the frozen
strict author checker to the complete derived draft, and require a separate
verified assembly with the unchanged codec and actual Graphify round trip.

The three-total-F_P-attempt ceiling is shared by original authoring, fresh
authoring retries and grounding repairs for each chunk. The global ceiling is
four generation/repair calls. No private semantic probe enters repair prompts.
The initial generator and final F_D helper are read-only; no repairs launch
before independent contract/code preflight. Root Writer owns the separate repair
addendum, scheduling/measurement and result integration in the new dogfood study.
`/root/ac_generation_design` independently evaluates this bounded contract and
implementation; it does not grade generated meaning or accept models.

## Independent fidelity assessment activation

After all four complete proposals exist, Root Writer may run the reviewed
`prepare_assessment.py` to create immutable neutral-label packets, exact model
copies and a separate protected treatment map. The source-only oracle remains
the pre-answer frozen subject; no probe-selected semantic repair is authorized
inside the paired generation trial.

Writer `/root/ac_generation_codex_fidelity` owns only
`dogfood/stdo-v3-generation/grading/codex/grades.json`; Writer
`/root/ac_generation_claude_fidelity` owns only the corresponding
`grading/claude/grades.json`. Each fresh nonauthor context assesses both exact
anonymous models for its candidate against all six source-selected probes and
every required distinction and prohibited distortion. The applicable frame is
bounded documentary meaning conservation, under the selected installed
v2.5.1-rc.2 implementation basis; each frozen V3 corpus remains subject data.

The graders may read their packet, its exact model files, the candidate's frozen
documentary source and required Product/basis bootstrap. Runs, code, usage,
private maps, historical interpretations and session memory are outside their
assessment frontier. Model or source wording may disclose treatment; preserve
the exact bytes and record explicit disclosures rather than claiming assured
blinding. Evidence must resolve to generated record identities and fields plus
exact source loci. No source/model repair, other writes, actor dispatch, Git,
owner acceptance or installed qualification is granted. Root consumes the
closed assessments, checks protected inputs and evidence coordinates, then
reports bounded fidelity and measured construction resources separately.

## Completion evidence

The [four new representations](../../../dogfood/stdo-v3-generation/README.md)
and [review](../../../dogfood/stdo-v3-generation/REVIEW.md) close this bounded
construction and comparison. Source-first creation, all source custody and
declared coverage, strict/native recovery and actual pinned Graphify recovery
pass. The tested code remains frozen; all 107 tenant tests pass.

The execution retains 60 initial author calls, four fresh author retries and
21 scoped F_P citation repairs. Every final chunk is supported by a strictly
valid draft, verified F_D derivation or verified F_P repair chain. The original
Codex direct timeout retains unknown backend usage and measured elapsed time.
The nonauthor resource audit reconstructed all 85 calls, raw counters, stage
timings, source copies and final file identities without an actionable defect.

Both fresh nonauthor semantic assessments preserve all 24 sampled distinctions
per model across six probes per candidate, with all 90 prohibited-distortion
checks absent. Protected input, grading coverage and evidence-coordinate checks
pass before treatment-map consumption. These are bounded documentary judgments;
semantic acceptance was not issued. Full governing joins, operational behavior,
whole-method fidelity, general efficiency, compression and installed
qualification remain outside this result. The work is local dogfood with no
Git effects, owner acceptance, RC or release selected.
