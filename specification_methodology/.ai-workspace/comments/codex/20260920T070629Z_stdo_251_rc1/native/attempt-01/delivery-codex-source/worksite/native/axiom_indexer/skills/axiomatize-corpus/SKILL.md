---
name: axiomatize-corpus
description: Convert source documents into a source-linked axiomatic program and logical constraint map, or project explicitly selected source-grounded frame indexes. Use when asked to axiomatize a corpus, extract constraints and authored dependencies, validate or repair a program, obtain reference-only or materialized frame context, or join an Executive's ordered labeled request. Do not use for prose summaries, automatic frame selection or semantic acceptance.
---

# Axiomatize Corpus

Read [the output contract](references/output-contract.md) and its
[program schema](references/program.schema.json). Run the commands below from
the Axiom Indexer repository root that contains `build_tenants/`.

1. Resolve the exact `a_c` calculus, source, and frame URIs. Stop on an
   unresolved or ambiguous URI.
2. Capture only essential symbols, relations, constraints, and residuals.
3. Give every item a stable absolute URI and at least one source URI.
4. Link items only by URI. Never use line numbers, array positions, or counts as
   identity.
5. Preserve uncertainty as a residual. Do not invent missing meaning.
6. Sort URI sets and the symbol, clause, and residual arrays by URI.
7. Write the program, then run:

   ```sh
   python3 build_tenants/core/code/ac.py validate \
     --program <program.json> \
     --bindings <bindings.json> \
     --emit-map <constraint-map.json>
   ```

8. Repair the program from all diagnostics and validate again.
9. For later work, start from the validated map. Re-enter source only when the
   task, a residual, or an unresolved reference requires it.
   For a selected frame projection, author optional `frame_indexes` under the
   exact output contract. Ground the frame, scope and selected clause/residual
   roots in their source owner. Use existing ordered role/ref arguments for all
   supporting premises, conditions, exceptions and consequences; retain literal
   qualifications and uncertainty. Code does not discover missing dependencies.

   Select index identities explicitly from that exact map and run:

   ```sh
   python3 build_tenants/core/code/ac.py project \
     --program <program.json> --map <constraint-map.json> \
     --bindings <bindings.json> --frame-index <index-uri> \
     --mode reference-only --output <projection.json>
   ```

   Repeat `--frame-index` for overlapping selections; use `materialized` for
   the same closure with unchanged authored content. Both views preserve shared
   identities, dependencies, literals, residuals and source routes. Missing or
   stale map/source evidence refuses projection. Re-enter the actual source
   owner for semantic repair; a refreshed digest alone does not establish it.
   The agent judges applicability and task evidence: an unsatisfied premise,
   applicable exception or unknown fact cannot be turned into permission by
   materialization. Show the selected source frame, index identity and scope.
10. When acting as Executive, select reference frames from the map, author an
    ordered JSON list of `{"label": string, "text": string}` sections, and
    include a visible frame section naming each frame URI, purpose, and source
    route. Run:

    ```sh
    python3 build_tenants/core/code/ac.py join \
      --input <sections.json> \
      --output <request.txt>
    ```

    The joiner only concatenates the supplied strings. Choose all content and
    ordering yourself.

For authoring or validation, return the program path, validation status, map
path, and unresolved residuals. For projection, return exact program/map and
selected index identities, mode, output or refusal, and remaining uncertainty;
do not describe projected content as an accepted evaluation or grant.
For joining, return the sections path, request
path or stdout status, join status, and selected frame URIs. Validation proves
only declared structure and resolution, never truth, completeness, fidelity,
or unique interpretation.
