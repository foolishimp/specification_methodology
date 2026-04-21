# /spec.refresh — Reload Specification Methodology Standards into Context

Read the canonical standard documents from `specification_methodology` and surface their full content into the active session. After this command, the session has the live constitutional text available for reasoning, not just stale memory.

## Usage

```
/spec.refresh [--doc <name>] [--list]
```

| Option | Description |
|--------|-------------|
| (none) | Load SPEC_METHOD.md (the baseline) |
| `--doc <name>` | Load a specific document by short name (see list below) |
| `--list` | Show available documents and their paths |

## Document Registry

| Short name | File | What it governs |
|------------|------|-----------------|
| `spec` | `specification/standards/SPEC_METHOD.md` | Constitutional baseline — authority chain, drift, repricing, sufficiency |
| `odd` | `specification/standards/ODD_METHOD.md` | Graph-native ODD product realization — covers graph substrate law, traversal, and ODD product-authoring over GTL/ABG (absorbed the prior `GRAPH_METHOD.md` on 2026-04-21) |
| `writing` | `specification/standards/WRITING_GUIDE.md` | Prose style and compression rules |
| `posting` | `specification/standards/POSTING_GUIDE.md` | Commentary and post format |
| `ticket` | `specification/standards/TICKET_METHOD.md` | Work item structure and triage |
| `release` | `specification/standards/RELEASE_METHOD.md` | Release cut and artifact rules |
| `identity` | `specification/standards/IDENTITY_METHOD.md` | Product and workspace identity rules |
| `world` | `specification/standards/WORLD_MODEL_METHOD.md` | World model and context surface |
| `glossary` | `specification/standards/GLOSSARY_GUIDE.md` | Canonical terminology |

## Instructions

### Step 1: Resolve workspace root

Locate the `specification_methodology` repo root. The standards live at:

```
<repo-root>/specification/standards/
```

Resolve the root by finding the directory that contains `specification/standards/SPEC_METHOD.md`. If this command is invoked from a downstream workspace (e.g., a project that has the methodology installed under `.genesis/docs/standards/`), read from the **source repo** path, not the installed copy. Installed copies under `.genesis/` are mirrors and may be stale.

If the source repo cannot be located, fall back to the installed copy and emit a warning:

```
[WARN] Source repo not found — loading installed copy from .genesis/docs/standards/.
       Installed copies may be stale. Locate specification_methodology to load authoritative text.
```

### Step 2: Resolve target document(s)

- No arguments → load `SPEC_METHOD.md`
- `--list` → print the Document Registry table above and stop
- `--doc <name>` → resolve the short name against the Document Registry; error if unknown

### Step 3: Read and surface the document

Read the full file content. Then output:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPEC REFRESH — <short name> (<filename>)
Source: <absolute path>
Last repriced: <extract from file header if present>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<full document content>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
END SPEC REFRESH — <short name>
This text is now active in your session context.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 4: Confirm active surface

After surfacing the document, output one line:

```
Active: <short name> loaded. Constitutional text is in context — reason from this, not from training memory.
```

## Notes

- This command is read-only. It never writes, emits events, or modifies workspace state.
- Run this at the start of any session that will edit, review, or reason about constitutional methodology text.
- If the source file has been updated since the last session, running this command picks up the current version automatically.
- Multiple `--doc` calls in sequence build up a multi-document context surface in the session.
