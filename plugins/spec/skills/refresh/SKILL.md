---
name: refresh
description: Reload one selected STDO standards basis into context
argument-hint: "(--installed | --release <version> | --candidate) [--doc <name>] [--list]"
disable-model-invocation: true
---

# /spec:refresh - Reload Specification Methodology Standards into Context

Read the standard documents from one explicitly selected STDO basis and surface
their full content into the active session. Loading a document is a context
projection of that complete basis; it does not create a partial constitution.

## Usage

```
/spec:refresh (--installed | --release <version> | --candidate) [--doc <name>] [--list]
```

| Option | Description |
|--------|-------------|
| `--installed` | Load from the consumer's pinned installed STDO cut |
| `--release <version>` | Load from the immutable released cut identified by `<version>` |
| `--candidate` | Load mutable authoring source as explicitly non-operative candidate context |
| `--doc <name>` | Load a specific document by short name (see list below) |
| `--list` | Show available documents and their paths |

## Document Registry

| Short name | File | What it governs |
|------------|------|-----------------|
| `spec` | `specification/standards/SPEC_METHOD.md` | Constitutional baseline — authority chain, drift, repricing, sufficiency |
| `design` | `specification/standards/DESIGN_MODULE_METHOD.md` | Ontology, IACS, Prime, three-view, and functional realization method |
| `odd` | `specification/standards/ODD_METHOD.md` | Graph-native ODD product realization — covers graph substrate law, traversal, and ODD product-authoring over GTL/ABG (absorbed the prior `GRAPH_METHOD.md` on 2026-04-21) |
| `ux` | `specification/standards/UX_METHOD.md` | UX state, message, transition, effect, replay, and carrier law |
| `writing` | `specification/standards/WRITING_GUIDE.md` | Prose style and compression rules |
| `posting` | `specification/standards/POSTING_GUIDE.md` | Commentary and post format |
| `ticket` | `specification/standards/TICKET_METHOD.md` | Work item structure and triage |
| `release` | `specification/standards/RELEASE_METHOD.md` | Release cut and artifact rules |
| `identity` | `specification/standards/IDENTITY_METHOD.md` | Product and workspace identity rules |
| `world` | `specification/standards/WORLD_MODEL_METHOD.md` | World model and context surface |
| `glossary` | `specification/standards/GLOSSARY_GUIDE.md` | Canonical terminology |

## Instructions

### Step 1: Resolve the selected basis

The command requires exactly one basis mode:

- `--installed`: resolve the consumer's installed cut and verify its selected
  version, immutable reference, and member-inventory identity;
- `--release <version>`: resolve the immutable released cut for that version;
- `--candidate`: resolve mutable `specification_methodology` authoring source
  and label it candidate-only.

Do not silently fall back between modes. Mutable source must never replace a
missing installed or released basis. If the selected basis cannot be verified,
stop and report the missing identity.

For `--candidate`, emit:

```
[CANDIDATE] Mutable STDO authoring source loaded. This is not released consumer law.
```

### Step 2: Resolve target document(s)

- No `--doc` argument -> load `SPEC_METHOD.md`
- `--list` → print the Document Registry table above and stop
- `--doc <name>` → resolve the short name against the Document Registry; error if unknown

### Step 3: Read and surface the document

Read the full file content. Then output:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPEC REFRESH — <short name> (<filename>)
Basis: <selected version or candidate identity>
Source: <resolved path>
Last repriced: <extract from file header if present>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<full document content>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
END SPEC REFRESH — <short name>
This document is now available as a projection of the selected complete basis.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 4: Confirm active surface

After surfacing the document, output one line:

```
Active context: <short name> from <basis>. The complete selected basis remains constitutional authority.
```

## Notes

- This command is read-only. It never writes, emits events, or modifies workspace state.
- Run this at the start of any session that will edit, review, or reason about constitutional methodology text.
- Released and installed modes never follow mutable source updates.
- Candidate mode follows mutable source and remains explicitly non-operative.
- Multiple `--doc` calls in sequence build up a multi-document context surface in the session.
