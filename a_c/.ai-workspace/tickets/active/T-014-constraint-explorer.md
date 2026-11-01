# T-014 Constraint explorer with a 3D option

Status: implementation and bounded local verification complete; independently
reviewed. Local changes are not committed or published.
Owner: Jim. Change class: `design_reframe` under AC-R-003–010 and AC-R-013.

## Owner instruction

“create a 3d option”; “the goal is to be able to read and follow the logical
reasoning”; “the constraints”. The outcome is a usable constraint reader with
3D navigation over the existing exact STDO representation.

## Activation and territory

Root completes Executive intake and explicitly changes to Worker/Writer for
this implementation. Grant: add the viewer generator, its local browser assets,
focused checks, design and usage documentation in `build_tenants/graphify/`;
write this ticket and `T014_CONSTRAINT_EXPLORER/` work/evidence; generate a new
application under `applications/stdo-constraint-explorer/`; link the viewer from
the a_c README. Frozen applications, models, release bundles, Lean proofs,
Product definitions, other work and Git history remain outside the write grant.
No commit, push or release is part of this increment.

The installed builder is v2.5.1-rc.2, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782` and calculus
`cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`, freshly
verified. Subject: the frozen common 35fb4824 proposal model used by T-013;
this is not a claim that it represents a later STDO release.

## Delivery predicates

1. Read full constraints, conditions, exceptions, source quotations and caveats.
2. Follow directed, labelled authored relations and required retention links;
   retain exact record identities and parallel occurrences. A navigation trail
   distinguishes connected steps from a new search selection.
3. Toggle 3D/2D, focus/expand a neighbourhood, search every record, and return
   through the trail. Filtering the picture does not truncate the source model.
4. Mark dependency/retention edges as such. Supply no invented inference,
   semantic acceptance or per-constraint Lean proof status.
5. Generate a portable local HTML artifact using a pinned existing renderer;
   no network access is needed to read it. Preserve a usable text reader when
   WebGL is unavailable.
6. Verify the actual large model and browser interaction, including search,
   constraint text, source access and navigation. Independently inspect the
   changed adapter and display boundary.

## Return

The [delivery record](../../work/T014_CONSTRAINT_EXPLORER/DELIVERY.md) binds the
artifact, tests, actual browser checks and closed independent review. The
[reader](../../../applications/stdo-constraint-explorer/index.html) and its
[usage guide](../../../applications/stdo-constraint-explorer/README.md) are
ready for local use. This fulfills the selected viewer increment; no source
interpretation, proof or release has been regenerated.
