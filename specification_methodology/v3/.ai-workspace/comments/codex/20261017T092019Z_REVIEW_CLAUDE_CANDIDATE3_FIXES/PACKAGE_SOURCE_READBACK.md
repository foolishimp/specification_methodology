# Package, conformance and interpretation entry readback

Subject and authority are those in [the activation](ACTIVATION_AND_EXPECTATIONS.md).
These parent conclusions were recorded after reading frozen source and the
independent package probe, before reading `REVIEW-PACKAGE-RC3.md` or treating
the author's qualification reports as evidence of repair correctness.

**R1: original missing-input defect repaired.** The manifest recorded at B
admits all 62 files under the candidate's standards tree, including the
Product Definition schema and template, and all 17 plugin files. The
independently written [probe](package_probe.py) reproduced all 81 file hashes
(including license and release note), the member-set digest, tree coordinates
and recorded tag's target. Standards, plugins and a_c are unchanged between
A and B. The manifest validates against its admitted schema. In a new scratch
directory containing only admitted package files, a filled Product Definition
template validates against its admitted schema and all four prescribed
entrypoints exist. The [receipt](PACKAGE_PROBE.json) binds exact inputs.
This closes the absent schema/template case, not native installer, complete
bootstrap semantics, ordinary-use qualification or release acceptance.

**R6: original false standalone/provenance-only claim repaired by narrowing
the surface.** CONFORMANCE.md:3–15 and 149–156 now expressly classify section 5
as the qualification map for constructing this corpus. The expected
distinctions remain owned by the construction specification, which is
explicitly outside this package and must be acquired for that qualification.
The text no longer claims those distinctions have been restated or are mere
provenance. It also expressly denies that an adopting Product's rules depend
on section 5. The ordinary README review route does not overturn that scope.
The L-19 row is correctly treated as a route for this construction review,
not a complete oracle within an installed package. This repairs the reported
false dependency classification; it does not make whole-corpus qualification
standalone. Physical relocation of the map could simplify the surface, but
this affected readback found no new required adopting-Product determination
that needs its external oracle. No new defect is inferred merely from the
file's location.

**R7: obsolete main entry repaired; one small wording residual.** The root
a_c entry now names the current i3 set, extended at I5, and its actual 155
clauses and five indexes. The independent probe confirms those counts, zero
residual records and the declared rc.2 calculus basis; source references name
the current standards namespace. This does not prove full encoding coverage
or semantic fidelity. `a_c/i3/README.md:56` still says “four task scopes” above
a five-row table at 62–66. This is a Low wording defect, not a reason to rerun
the interpretation suite. The same entry openly limits its offered coverage.

The probe's first execution stopped in the reviewer-written scratch-path
guard because macOS resolves the temporary directory's parent through
`/private`. Resolving both sides repaired the probe; the successful receipt
above follows that change. This was a reviewer harness issue, not a
candidate failure. No source or installed store was modified.

Review limits: selected changed producers and their stated dependencies were
read; no whole-corpus rereading, host activation or comparative trial was
performed. Truncated search output is not counted as source read. Parent
authorship/interest and delegated reviewer limits remain as disclosed in the
activation.
