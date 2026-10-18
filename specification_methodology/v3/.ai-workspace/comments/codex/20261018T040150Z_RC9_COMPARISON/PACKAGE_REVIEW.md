On package integrity and acquisition, I prefer **Codex as the release basis**, with publication qualification still required. Claude’s partial interpretation is deferred by the owner and is **not a baseline disqualifier**. The strongest concrete finding is a reproducible defect in Claude’s manifest generator.

Both handoff checkouts remained clean. I worked from exact archives and wrote only scratch artifacts.

| Verified dimension | Claude RC9 | Codex RC9 |
|---|---|---|
| Frozen content | `c2cfa9b9`; handoff `3a209713` | `5592168e`; handoff `c46e9f96` |
| Top-level standards | 23 files; 2,083,876 bytes | 18 files; 1,205,622 bytes |
| Complete standards tree | 62 files; 3,435,620 bytes | 62 files; 2,050,091 bytes |
| Plugin | 17 files; 77,032 bytes | 17 files; 73,402 bytes |
| Interpretation replay | Fragment generation and assembly byte-identical | Program, frames and mapping rows reproduce exactly from source account |
| Native checker | Validation passes; regenerated map byte-identical | Validation passes; regenerated map byte-identical |
| Encoding inventory | 155 clauses; 5 indexes | 709 determinations; 713 clauses; 733 indexes |
| Released installation | Manifest exists but fails current toolchain verification | No issued install manifest; installation qualification explicitly pending |

File sizes are inventory facts, not proof of semantic reduction.

**Concrete finding: Claude’s standards inventory digest is incompatible with the current toolchain.**

At [build_manifest.py:17](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/release/build_manifest.py:17), the generator hashes:

```text
<digest>  <relative path>
```

The installed `stdo 0.1.4` verifier requires:

```text
<digest>  specification/standards/<relative path>
```

I materialized the exact manifest-admitted files in scratch and called the actual `stdo_toolchain.manifest.verify_materialization`, not the tenant’s schema check.

Results:

- Unchanged manifest: namespace, subtree and member-set digest failures.
- Normalize only the tenant namespace/subtree to publication conventions: **member-set digest still fails**.
- Also apply the canonical digest recipe: **no failures**.

Declared digest: `22d52c1c11130c0a7f014d4080a7576f939f22a7499b36857e2290e079a76177`.

Required digest: `0d301189485014a35d3a873c98b4eab015d45afd257da64be593fb30bb75e3ae`.

This is a bounded packaging repair before publication, not a criticism of the method’s semantics. The tenant’s [check_install.py:57](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/release/check_install.py:57) explicitly does not use an installer/toolchain verifier; its passing result establishes a narrower claim.

The manifest also uses canonical `source_root: specification/standards` although the frozen tenant’s actual root is `standards/`, and a canonical release-note path absent from that tenant. These are further candidate-to-release layout work, not grounds to credit the current manifest as callable installation.

**Package boundaries and reproducibility.**

Claude’s 82 materialized files are **62 standards + 17 plugin + LICENSE + release note + manifest**. None is the interpretation. Its ordinary [“use the formal interpretation” route](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/standards/README.md:45) therefore leaves that package. Its install check records 15 missing relative targets; two are `X_v` notation false positives, leaving 13 actual link occurrences to interpretation, design, frontier and qualification files. These do not establish missing adopter law; the interpretation route is nevertheless unavailable in the declared installed set.

Codex keeps the interpretation inside its selected `successor/` package. Its [binding procedure](/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/successor/interpretation/bindings.py:9) accepts an explicit theory root and verifies documentary and carrier digests. I ran that published route successfully from a relocated archive.

Claude’s generated [bindings](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/a_c/i3/tools/assemble.py:197) hard-code Jim’s RC2 installation path. Its replay succeeds on this machine, but the published artifact does not establish machine-independent reacquisition. This belongs with the deferred interpretation packaging work.

Both deliberately retain RC2 as the separate **encoding/checker basis**. That is not evidence that successor method prose requires RC2 to remain operative.

**Ordinary navigation and native entry.**

Claude offers a broad, descriptive task table with routes for project setup, intake, construction, recovery, review and release. Codex’s shorter table emphasizes exact anchored owner sections and distinguishes optional broader excerpt assemblies. For the inspected intake, recovery, result-conjunction and disposition routes, both provide discoverable owner paths.

Codex’s [Product-basis instructions](/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/successor/plugins/spec/references/PRODUCT_BASIS.md:45) explain exactly how to resolve skill member references against the selected immutable basis and distinguish a source-candidate assessment root. This is useful practical precision. Both plugins require exactly one applicable Product Definition, verified identity, and an actual work grant; neither treats plugin installation as authority.

I did **not** invoke the skills in fresh native hosts. Neither candidate earns native trigger or release-installation qualification from this review. Codex explicitly acknowledges the unqualified minimum toolchain and host routes in [GETTING_STARTED.md:155](/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/successor/plugins/spec/references/GETTING_STARTED.md:155) and [line 346](/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/successor/plugins/spec/references/GETTING_STARTED.md:346).

**The larger Codex interpretation has a substantial acquisition-cost caveat.**

I executed the published materialized projection route for three matched subject areas:

| Selection | Claude output | Codex output |
|---|---:|---:|
| Result algebra and conjunction | 35,209 bytes | 298,312 bytes |
| Frame authority | 16,247 bytes | 1,182,585 bytes |
| Evidence reuse | 16,675 bytes | 369,562 bytes |

All six calls passed. Claude took roughly 0.18 seconds each; Codex roughly 9.2 seconds each on this machine.

These are **serialized carrier measurements**, not comparable task-sufficiency scores: Claude expressly omits material conditions from these indexes, while Codex carries broader structured meanings and dependencies. Nevertheless, Codex’s ordinary materialized output should not be described as demonstrably compact or context-fit without an actual actor trial. Its broader coverage is a maturity advantage with a significant usability tradeoff.

I respected the owner’s explicit deferral in [LEDGER.md:660](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/qualification/C3-SYNTHESIS/LEDGER.md:660). Missing complete encoding, five expectation sets and replacement compressions remain follow-on scope, not automatic baseline rejection.

Reproduction artifacts:

- [/tmp/stdo-rc9-package-2yi8m21l/replay.py](/tmp/stdo-rc9-package-2yi8m21l/replay.py) and [results](/tmp/stdo-rc9-package-2yi8m21l/replay-results.json).
- [Manifest positive controls and compiler replay](/tmp/stdo-rc9-package-2yi8m21l/controls.py), [results](/tmp/stdo-rc9-package-2yi8m21l/controls-results.json).
- [Projection replay](/tmp/stdo-rc9-package-2yi8m21l/projections.py), [results](/tmp/stdo-rc9-package-2yi8m21l/projection-results.json).

Run each with `/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python`. No paid calls, global installs, candidate repairs or acceptance claims were made.
