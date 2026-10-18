# STDO Refresh Procedure

Reload one complete registry entry from exactly one selected STDO basis. An
entry is the successor law of one standard. This is a read-only context
projection; it does not create a partial constitution.

## Inputs

Exactly one basis mode is required:

- `--installed`: discover the applicable Product Definition and use its pinned,
  verified installed basis;
- `--release <product-local-cut>`: resolve immutable product-local cut
  `v<version>-rc.<n>` through the STDO manager; or
- `--candidate`: load mutable methodology source and label it non-operative.

Optional `--doc <name>` selects one registry entry. `--list` prints the
registry and stops. With neither, load the `spec` entry.

## Registry

Each entry loads, in the listed order, every successor member that carries
the law its predecessor standard carried. A member listed without sections
loads in full. A listed section loads in full with all its subsections, up
to the next heading at its own level or shallower.

| Name | Members |
|---|---|
| `frame` | `REFERENCE_FRAME.md`; `FOUNDATIONS.md` §2 and §4; `ACTIVATION.md` §1 to §4 and §7; `EVALUATION.md` §7 |
| `frame-baseline` | `EXECUTIVE_BASELINE.md`; `ASSURANCE.md` §7 to §13; `EVALUATION.md` §4 |
| `spec` | `SPEC_METHOD.md`; `ACTIVATION.md`; `PRODUCT_DEFINITION.md`; `ASSURANCE.md`; `EVALUATION.md`; `TICKETS.md`; `FOUNDATIONS.md` §2 and §3; `PROFILES.md` §2 and §3 |
| `design` | `DESIGN_MODULE.md`; `ASSURANCE.md` §14 to §16; `ACTIVATION.md` §1, §4 and §6; `SPEC_METHOD.md` §2; `FOUNDATIONS.md` §4 |
| `odd` | `ODD.md` |
| `ux` | `UX.md`; `TICKETS.md` §3; `PROFILES.md` §2 |
| `writing` | `WRITING_GUIDE.md` |
| `posting` | `POSTING_GUIDE.md`; `SPEC_METHOD.md` §6 |
| `ticket` | `TICKETS.md`; `ACTIVATION.md` §1; `SPEC_METHOD.md` §3 and §7 |
| `release` | `RELEASE.md`; `FOUNDATIONS.md` §1 and §2; `PRODUCT_DEFINITION.md` §4; `EVALUATION.md` §5 |
| `identity` | `IDENTITY.md`; `RELEASE.md` §1, §3 and §8; `DESIGN_MODULE.md` §12 |
| `world` | `WORLD_MODEL.md`; `FOUNDATIONS.md` §3 |
| `glossary` | `GLOSSARY.md`; `PROFILES.md` §2 |
| `calculus` | `AXIOMATIC_CALCULUS.md` |
| `traversal` | `TRAVERSAL_OCCURRENCE.md`; `AXIOMATIC_CALCULUS.md` §8 |
| `library` | `README.md`; `PRODUCT_DEFINITION.md` §4 and §12; `RELEASE.md` §3 and §4 |

## Procedure

1. Resolve exactly one basis. For installed mode, require one Product
   Definition and verify its URI and manifest. For release mode, resolve the
   product-local cut through the manager; its Git transport may be
   project-qualified. Never substitute the moving selector. For candidate
   mode, emit:

   ```text
   [CANDIDATE] Mutable STDO authoring source loaded. This is not released consumer law.
   ```

2. Resolve the selected entry and each of its members and sections. Refuse
   unknown names and any fallback to a different install, local copy,
   mutable source, or nearby Product.
3. For each listed member or section, in order, read and surface it in full
   with its name, exact basis, resolved source, full content, and explicit
   end marker.
4. Conclude:

   ```text
   Active context: <name> from <basis>. The complete selected basis remains constitutional authority.
   ```

Multiple explicit calls may build a multi-document context. Daily workflow
skills should normally read only the smallest relevant source surface.
