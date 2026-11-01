# Nominated-project representation build

Implements the first public workflow slice of PU-01–09, selected by T-016 and
consumed by STDO Skills T-003. The existing generation, carrier, formal-gate and
viewer designs own their algorithms. `code/ac_project.py` binds and coordinates
them; it is not a new calculus or project lifecycle.

## Public operations

- `prepare --project ROOT --definition FILE --out NEW_RUN [--source REL ...]
  [--mode direct|graphify-ac] [--upstream PATH] [--title TEXT] [--stdo EXECUTABLE]`:
  verify the nominated definition with the ordinary manager, retain its exact
  method/source identity and freeze the selected UTF-8 corpus. Defaults select
  the Product's WHAT surfaces, resolved relative to the selected definition.
  Explicit sources replace that selection and are relative to the nominated root.
  Selection is local to this project and does not recursively acquire composed
  Products. Symlinks, missing sources, escaping paths and output overlap refuse.
  `direct` requires no upstream Graphify install; `graphify-ac` requires the
  pinned upstream and runs its actual structural discovery. This choice is
  visible, never silently changed. Default chunk envelope is 20,000 characters.
- `task --run RUN [--chunk ID]`: return the next unanswered chunk's authoring
  instructions, exact source, schema and task identity. Subject content is data.
  The host may use its ordinary tools to deliver the answer but cannot claim
  the batch runner's fresh isolated-actor evidence. No child process is needed.
- `submit --run RUN --chunk ID --answer FILE --author LABEL`: validate exact
  grounding, schema, identities and section dispositions using `author_check`;
  retain an immutable answer and caller-declared provenance. Matching retries
  are idempotent; a different submission cannot overwrite an accepted one.
- `build --run RUN`: require all chunks, recheck source/definition/implementation
  currentness and every submission; use the shared proposal emitter for model,
  carrier, coverage, actual upstream round trip when selected, and optional
  required formal checks. Generate one `explorer.html` with 3D, 2D and Layered
  modes over the same view-data projection of that exact model and frozen source.
  Switching modes preserves the reading/navigation state. The page embeds its
  records, links and sources and opens from disk without a service. Report
  produced bytes and checked scope. A complete receipt is
  written last. A matching completed build is inspected and reused; an interrupted
  partial output is retained and refused for automatic overwrite.
- `status --run RUN`: inspect pending chunks and verify a completed receipt's
  artifacts. Drift refuses current reuse; historical files are retained.

The optional required formal-checker path and trusted digest are selected during
prepare, using the existing gate configuration and its resource-root contract.
Neither a skills label nor an ordinary build result implies Lean ran.
When selected, its origin reservation applies before the project wrapper reads
the definition, source, submitted answers or retained artifacts, and before it
creates a run or output. It also guards directories before source traversal.
Resume resolves the inherited checker through generation's fixed operator-owned
startup metadata before reading `PROJECT.json` or its named paths. The public
project workflow selects the checker at prepare; adding a later selection to
an unselected checkpoint requires a fresh project run. The wrapper uses the
same exact-source adapter and refusal type as generation. Without a checker,
these operations perform no origin lookup and retain their local-file contract.

## Retained state and trust boundary

RUN contains the exact Product Definition, manager readback, source manifest,
generation checkpoint and corpus, host-session submissions and final artifacts.
The source selection, requested title/mode, provider machinery and task digests
bind reuse. Added/removed selected directory members also invalidate currentness.
It is a cooperative single-writer local workflow, not hostile-filesystem
confinement. Content pins detect changes relative to the retained record; they
are not signatures or proof of the caller's authority.

Project-specific source remains F_P interpretation. The five authorable families
and three empty operational families retain the existing bounded adapter's
meaning. Processing all chunks does not prove semantic completeness. Output is
a proposal, with omissions, residuals and source re-entry visible. The existing
isolated batch path and its stricter event evidence remain separate and usable.
