# T-003 Nominated-project representation build

The two existing skill tenants now execute a representation build for the user's
selected STDO project. Codex enters through `$stdo-work`; Claude enters through
`/stdo-tool-operations` or the representation route in `stdo-workspace-change`.
The host authors the source interpretation in its own session. Both consume the
same a_c public provider; neither requires the other coding host.

## Use

Install the selected tenant using its existing package guide. Supply an available
STDO manager, the a_c provider's `ac_project.py` path and a compatible Python
interpreter. `AC_PROJECT_TOOL` and `AC_PROJECT_PYTHON` can select those paths.
Then ask, for example:

> Build an a_c representation of `/path/to/project`, using its `stdo_project.json`.
> Put the run in `.ai-workspace/representations/review-01`.

The skill verifies the nominated definition's exact installed STDO 3.x basis,
selects its declared WHAT source, and executes prepare → task → author → submit →
build → status. Explicit source selections replace that default. The returned
artifacts are `model.json`, `carrier.json`, `coverage.json` and an offline
`explorer.html` with source text, constraints and graph navigation.

Direct mode is the default. Graphify-assisted discovery needs the explicitly
selected pinned upstream. A required formal checker needs its selected trusted
configuration. An ordinary build does not imply that Lean ran. The caller must
have an eligible local source route; this entry does not implement the separate
mediated FD acquisition boundary.

To resume, nominate the existing run. Currentness is checked before pending
authoring or completed-build reuse. Changed source, invalid grounding, missing
chunks or changed artifacts withhold completion/current reuse. Accepted answers
are immutable and partial effects remain visible.

## Evidence and disposition

[TESTS.json](TESTS.json) records the root-observed results: 14 project-entry tests
and 30 existing generation tests passed, with zero skips and actual pinned
Graphify execution. The Claude package repair suite passed all 16 tests.
Both final package validators and all three changed skill-frontmatter checks
passed; actual results are in [FINAL-PACKAGE-CHECKS.json](FINAL-PACKAGE-CHECKS.json).
These are finite checks of the stated paths, not a semantic-completeness score.

The independent [repair closure](reviewer-fixtures/provider-review-mj3epoat/CLOSURE.json)
closed three S2 findings: trailing-slash source locators, definition-relative WHAT
selection, and contradictory completion metadata. Provider manifest and
source-fidelity follow-up are retained beside that record. Source and package
selection are bound by the [provider manifest](../../../specification/composition/REPRESENTATION_MANIFEST.json)
and the tenant inventories. The final metadata refresh changes construction
references, not the executed skill instructions or provider algorithms.

Native trials used exact installed skill copies in two disposable invoice
projects, with ordinary host tools and explicit invocation. Both original calls
reached a 240-second cap; their reports and events are preserved. Codex had built
its artifacts before interruption, and its separate resume returned checked reuse
and final status `built` with exit 0 after 137.073 seconds. Claude resumed the
pending authoring, submitted its actual answer, built all four artifacts and
returned final status `built` with exit 0 after 380.335 seconds. Neither resume
timed out; selected source remained unchanged. [NATIVE-RESULTS.json](NATIVE-RESULTS.json)
binds both original reports, resumes and artifact paths. Initial fixture attempts
failed manager validation before either actor launched; those observations are
retained and are not actor failures.

The source sample requires ordered CSV columns, exact decimal digits, a prohibition
on binary floating-point conversion, header-only empty output and an unresolved
rounding policy. The independent reader checks those meanings in the authored
model, not merely record counts or command names. The
[final independent closure](reviewer-fixtures/provider-review-mj3epoat/FINAL-CLOSURE.json)
finds no open material defect in the provider, skill workflows or those selected
invoice distinctions. Both host traces establish actual authoring/build or reuse
and returned artifact links; source, carrier, model and viewer bindings match.
[HOST-CUSTODY.json](HOST-CUSTODY.json) records the exact installed trial resources
and the later Codex construction-metadata refresh.

The generated examples can be opened directly:
[Codex explorer](host-codex-02/invoice-project/.ai-workspace/representations/invoice-01/generation/proposal/explorer.html)
and [Claude explorer](host-claude-02/invoice-project/.ai-workspace/representations/invoice-01/generation/proposal/explorer.html).

The changed representation route has explicit invocation evidence; automatic
discovery reliability, large-project cost, recursive composed-project delivery,
general semantic adequacy and the older Claude Q05 handoff remain separate.
No new Lean proof, accepted Product release, global installation, commit or push
is claimed. This is the first usable public workflow slice of a_c T-015; the
broader product and STDO 3.0.3 release work retain their own obligations.
