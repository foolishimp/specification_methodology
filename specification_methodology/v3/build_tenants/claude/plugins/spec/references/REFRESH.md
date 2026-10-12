# STDO Refresh Procedure

Reload one complete standard from exactly one selected STDO basis. This is a
read-only context projection; it does not create a partial constitution.

## Inputs

Exactly one basis mode is required:

- `--installed`: discover the applicable Product Definition and use its pinned,
  verified installed basis;
- `--release <product-local-cut>`: resolve immutable product-local cut
  `v<version>-rc.<n>` through the STDO manager; or
- `--candidate`: load mutable methodology source and label it non-operative.

Optional `--doc <name>` selects one registry member. `--list` prints the
registry and stops. With neither, load `SPEC_METHOD.md`.

## Registry

| Name | Member |
|---|---|
| `frame` | `REFERENCE_FRAME.md` |
| `frame-baseline` | `EXECUTIVE_BASELINE.md` |
| `spec` | `SPEC_METHOD.md` |
| `design` | `DESIGN_MODULE.md` |
| `odd` | `ODD.md` |
| `ux` | `UX.md` |
| `writing` | `WRITING_GUIDE.md` |
| `posting` | `POSTING_GUIDE.md` |
| `ticket` | `TICKETS.md` |
| `release` | `RELEASE.md` |
| `identity` | `IDENTITY.md` |
| `world` | `WORLD_MODEL.md` |
| `glossary` | `GLOSSARY.md` |

## Procedure

1. Resolve exactly one basis. For installed mode, require one Product
   Definition and verify its URI and manifest. For release mode, resolve the
   product-local cut through the manager; its Git transport may be
   project-qualified. Never substitute the moving selector. For candidate
   mode, emit:

   ```text
   [CANDIDATE] Mutable STDO authoring source loaded. This is not released consumer law.
   ```

2. Resolve the selected member. Refuse unknown names and any fallback to a
   different install, local copy, mutable source, or nearby Product.
3. Read and surface the full member with its name, exact basis, resolved source,
   full content, and explicit end marker.
4. Conclude:

   ```text
   Active context: <name> from <basis>. The complete selected basis remains constitutional authority.
   ```

Multiple explicit calls may build a multi-document context. Daily workflow
skills should normally read only the smallest relevant source surface.
