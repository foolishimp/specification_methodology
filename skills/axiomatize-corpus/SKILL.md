---
name: axiomatize-corpus
description: Convert source documents into a source-linked axiomatic program that instantiates as a logical constraint map. Use when asked to axiomatize or semantically compress a corpus, extract its operative symbols and constraints, validate or repair an axiomatic program, use a compact program instead of repeatedly loading prose, or join an Executive's ordered labeled context into an agent request. Do not use for prose summaries or byte compression.
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
path, and unresolved residuals. For joining, return the sections path, request
path or stdout status, join status, and selected frame URIs. Validation proves
only declared structure and resolution, never truth, completeness, fidelity,
or unique interpretation.
