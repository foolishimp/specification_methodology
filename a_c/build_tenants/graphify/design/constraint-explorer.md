# Constraint explorer

T-014 realizes AC-R-003–010 and AC-R-013 as a local reading surface. The CLI
accepts a native validated model or a fully decoded Graphify carrier and emits
one standalone HTML file. All exact record payloads remain available. The
existing codec owns validation and acquisition dependencies.

The view uses pinned `3d-force-graph` for 3D and planar layouts. The reading
panel presents structured predicates, conditions, exceptions, residuals and
recorded source quotations. Full original JSON is separately inspectable.
Search defaults to constraints, with all eight record families available.
Planar labels use depth zero because the renderer removes node depth in 2D;
3D labels use the node's actual finite depth. Missing required coordinates
remain pending instead of being rendered at an invented 3D position.

There are three explicit link layers: required retention dependencies from the
codec's projection index, authored semantic relation records with their exact
kind/direction/qualifications, and other typed references. These layers are
not interchangeable. An authored relation is inspectable as its own record,
including parallel and self-relations. Required dependencies are not logical
implications; graph layout, selection and path traversal establish no proof.

The default neighbourhood limits visual clutter. Expand and overview change
only visible nodes, with displayed counts; the complete model stays available
to search and reading. Following a connection appends its label and direction
to the reading trail. Unconnected selections explicitly begin a new trail.

Optional source embedding reads only source paths occurring in grounding,
confines them to the selected root, and records their content digests. Recorded
quotes are kept distinct from the supplied file and its line span. Source
comparison is factual text comparison, not interpretation fidelity. All source
and record content is displayed as text. Embedded JSON escapes HTML delimiters.

The generator refuses an existing destination and never edits the input or a
sealed release. Renderer bytes and license notices are pinned locally. The
artifact identifies the exact model and represented basis, and makes no new
release or acceptance claim. Lean proves the selected closure/projection
fragment elsewhere; this viewer does not label English constraints as proved.

## Source navigation

The Files flyout projects the exported source paths into expandable folders.
It indexes exact grounding occurrences per record and file, deduplicating only
the file-to-record discovery entry. All quotations remain available in the
reader. Embedded files with no grounded record remain browseable; paths whose
source is not embedded retain record discovery and an explicit unavailable
source state. No live workspace scan or new acquisition occurs in the browser.

Selecting a file supplies a separate discovery scope with all record families
visible initially, source access and a clear return to all records. A record
selection keeps that file as a navigation origin. Logical traversal may leave
the file's scope without changing the selected record or fabricating a source
dependency. The reader exposes exact source locations and Show in files actions;
revealing a location expands its ancestors and selects that file without clearing
the logical reading trail. Opening/closing the flyout does not reset either view.

Folder membership and line order organize discovery only. They do not infer
semantic relations, authority, complete source coverage or proof. File labels,
paths and all source content use text DOM nodes. The view remains standalone.

## Static layered renderer

T-018 adds `ac_explore.py --layout layered` alongside `--layout force` and the
default unified page. All renderers consume the identical `view_data`
projection of the same validated model/carrier and optional frozen sources.
Only presentation assets differ. The shared reader owns search, file discovery,
source access, exact record display and typed reading trails.

The layered renderer uses HTML node cards and SVG connections. Its layout follows
odd_manager's `visual-graph/layout.ts` strategy: condense strongly connected
components, rank the resulting DAG left to right, then position the original
nodes and retain all original edges. It is a local presentation adaptation, not
a runtime or Product dependency on odd_manager. An iterative traversal avoids
the browser call-stack bound. Layout does not create relations or infer proof.
Separate curves retain parallel, reciprocal and self-links; link inspection
retains the exact authored relation record and qualifications. Cycle badges
describe the displayed link graph only. Zoom and fit change coordinates, not
the selected records. All labels are text, including labels supplied by source.

Both exports are self-contained HTML, opened directly from disk. The layered
page embeds its script/CSS and all representation data; it needs neither WebGL
nor an external library, server or network. JavaScript handles local interaction.
An HTML export is a frozen snapshot; rebuilding from a changed representation
produces new documents. There is no live filesystem acquisition in the browser.

Public project builds emit one `explorer.html`, containing all three modes and
one `view_data` result. The middle-panel switch changes only renderer state:
selected identity, file scope, query, family/link filters, visible nodes/links,
reader and trail persist. Separate hosts preserve renderer instances; the force
engine initializes lazily and pauses while layered is displayed. Label animation
also stops while the force view is hidden. If WebGL is unavailable, layered and
the shared reader remain usable. The default initial mode is Layered.

The one page appears in the build artifact inventory and currentness checks.
Prior completed runs and explicit standalone exports retain their original
bytes and machinery identity. The two-page export was the preserved predecessor.
