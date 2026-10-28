# Optional F_D grounding recovery

`code/ac_grounding.py` is a separate, optional construction-support layer over an
unchanged frozen `ac_generate.py` plan. It invokes no model and changes no source,
original actor answer, invocation, result, failure, usage or validation artifact.
It does not reinterpret predicates, conditions, exceptions, identities, references,
section selection, dispositions, residual meaning or limitations.

## Bounded source-anchor operation

The only writable fields of a derived draft are `quote`, `start_line` and
`end_line` inside the five known top-level record families' grounding arrays.
Every grounding's `section_id`, every other authored field, array order and record
population remain unchanged. A canonical JSON comparison masks only those three
permitted anchor fields and proves the remaining payload byte-semantically equal.

A strict-valid original anchor is unchanged and receives no recovery claim.
Otherwise the operation searches the **same exact supplied source section**:

1. Collapse each maximal Unicode whitespace run to one ASCII space and trim only
   outer whitespace for search. Preserve every non-whitespace character, case,
   punctuation and internal whitespace boundary. This is not whitespace deletion:
   `in valid` differs from `invalid`, and `a b` differs from `ab`.
2. Require exactly one occurrence in the complete normalized section. A unique
   exact quote does not win if another whitespace-equivalent occurrence exists.
   Repeated, lexically different and outside-section quotations refuse.
3. Map that unique occurrence back to its exact literal source substring and
   original absolute line range. Record old/new fields, section digest, normalized
   quote digest, normalized offsets, literal source offsets and uniqueness witness.
   Offset mapping uses the same `splitlines(keepends=True)` convention as source
   preparation and strict validation, including accepted Unicode line separators.
4. Run the unchanged complete `author_check` against the derived draft. Any other
   defect, including a misspelled or unknown section identity, refuses. An earlier
   quote failure may have hidden later non-anchor defects; fixing the first error
   does not make a complete draft usable automatically.

This operation recovers exact source re-entry coordinates for an already authored
F_P proposal. It supplies no additional semantic judgment. A well-shaped quotation
can still support an incorrect interpretation; independent semantic review remains
necessary. The resulting model has a new content identity because grounding and
provenance are part of its exact representation.

## Original actor and source custody

Before deriving or consuming a draft, the layer rechecks the exact frozen source,
source manifest, chunk plan, generator, unchanged codec and generation assets.
Graphify treatments also recheck discovery graph and extraction custody.

Original actor eligibility uses the same custody gate as ordinary generation
reuse, with only the failed-draft eligibility below enabled for this layer.
It requires retained answer, result, invocation, prompt,
event stream, stderr and usage. Their hashes must agree. The invocation must use
the pinned author schema, exactly the frozen chunk's recomputed `author_prompt`,
the frozen CLI version and settings, an ephemeral read-only empty workspace, all
required tool/document isolation flags and no enabled MCP. Actual event item types
and usage are checked, rather than trusting an isolation summary alone.

A completed clean CLI draft is eligible. A failed result is eligible only when
its sole recorded failure is `source_or_semantic_fragment_validation`, with zero
CLI exit code, no timeout, no schema/isolation failure, unchanged configuration
and genuine reported usage. Its recorded source-validation error must equal exact
recomputation against the original draft. A completed CLI call is not retroactively
made a successfully validated original actor by this layer.

Newer unfinished actor attempts block selection and assembly. A newer completed
attempt invalidates a previously selected normalization proof. No fallback hides
a failed or active retry. Appending repair instructions to a frozen actor prompt
is outside this profile and refuses; supported fresh retries use the exact same
frozen prompt unless a later, separately declared F_P repair contract is adopted.

## Immutable evidence and assembly

`normalize` writes a fresh directory for each selected completed source chunk:

- `normalization/CHUNK/derived-answer.json` when the complete derived draft passes;
- `normalization/CHUNK/journal.json` with `derived_validated`, `validated_original`
  for a no-op, or `refused`.

The journal pins the normalizer code and policy, exact original actor evidence,
source/chunk coordinates, original failure, original usage, old/new anchor changes,
the non-grounding equality proof and derived bytes. Refusals retain selected
original-attempt coordinates and raw digests as **unverified** when full evidence
validation cannot finish. F_D normalization and verification timing are measured
separately; no new F_P usage or price is invented.

Proof verification repeats custody and deterministic recovery, compares the full
derived answer and witness, rechecks non-grounding equality and reruns the unchanged
strict validator. Refreshing a changed derived answer's hash does not repair its
meaning or make a modified witness lawful. Source, schema, code, evidence or
derived-content drift refuses. Existing files are never overwritten.

`assemble` consumes strict originals and/or verified normalized drafts and uses the
unchanged `model_from_answers`, validator and proposal codec. Graphify modes also
build/export through actual pinned upstream and recover the exact generated model.
Outputs go to separate `grounded-proposal/`; the ordinary `proposal/` is untouched.
Provenance links original answers and normalization journals. All original actor
attempts and their cost remain available for generation-cost assessment.

Normal assembly requires every selected source chunk. Explicit `--allow-partial`
can exclude missing, ineligible or explicitly refused drafts, retain the refusal
and available original evidence, and create `grounded-partial-proposal/` with
`processing_complete=false`. The adapter marks the excluded source sections
`refused`. This option never ignores corruption in a supposedly successful
normalization proof, changed source, schema or discovery custody.

## Commands and coordinator API

From `a_c/`, using the already prepared frozen run:

```sh
.venv/bin/python build_tenants/graphify/code/ac_grounding.py normalize --output RUN
.venv/bin/python build_tenants/graphify/code/ac_grounding.py assemble --output RUN --upstream UPSTREAM
```

`normalize --chunk CHUNK` selects one chunk. Journals are immutable, including
refusals. After a new F_P attempt, choose a fresh
`--normalization-directory normalization-2`; normalize the final selected drafts
into that common fresh directory before final assembly. This retains prior
attempts and failed normalization evidence. No model run is automatically retried.

The coordinator may import:

- `normalize_answer(answer, chunk) -> (derived, changes)` for pure anchor checking;
- `normalize(output, name="normalization", chunk_id=None)` for full evidence and
  immutable journal creation;
- `verify_normalization(output, plan, chunk, folder) -> (derived, journal)` before
  consuming a proof;
- `assemble(output, name="normalization", allow_partial=False, upstream=None)` for
  the separate proposed-model and carrier result.

Tests cover lexical boundaries, case/punctuation, wrapped indentation, coordinate
recovery, normalized ambiguity, field preservation, unknown sections, source/evidence
drift, misleading failure flags, appended prompts, active retries, immutable original
usage, explicit partial scope and actual upstream carrier recovery. Synthetic actor
fixtures are mechanical test data, not evidence of model quality or acceptance.
