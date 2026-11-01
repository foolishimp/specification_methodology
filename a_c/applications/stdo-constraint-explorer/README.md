# STDO constraint explorer

Open [index.html](index.html) in a desktop browser. It is a standalone offline
HTML file: the 3D renderer, exact records and 58 referenced source files are
embedded. No account, Graphify installation, Lean process or backend is required.

If local HTML is blocked by an application, serve only this folder:

```sh
python3 -m http.server 8768 --bind 127.0.0.1 --directory applications/stdo-constraint-explorer
```

Then open <http://127.0.0.1:8768/>. Commands here are relative to `a_c/`.

## Reading the constraints

1. Search on the left. The default list contains all 841 constraints; select
   **All records** to find concepts, relation records, latitude and caveats too.
2. Read the full statement, conditions and exceptions on the right. The map
   begins with a small neighbourhood around the selected record.
3. Follow a labelled connection in the reader. The reading trail retains the
   exact connection and direction; **Back** returns to the previous record.
   Choosing an unrelated search result begins a new trail.
4. **Authored relationships** expose each relation's own kind and qualifications.
   **Must retain with this record** follows the acquisition dependency contract;
   **Required by** follows those links in reverse. Neither means a proved logical
   implication. Read attached caveats as part of the chain.
5. Open a source quotation to read its supplied file and highlighted lines.
   Recorded excerpts are compared with those lines; mismatches remain visible.
6. Use **3D / 2D**, **Focus**, **Expand one hop**, **Overview** and **Fit** to
   navigate. Drag empty map space to orbit, scroll to zoom, and click nodes to
   read. A click with several possible incoming links starts a new selection;
   use a labelled reader connection to select an exact edge.

Search and the reader remain usable if WebGL is unavailable. The map defaults
to retention and authored relations. Other typed references are an optional
layer. Filters affect the picture, not the model or the full record text.

## Exact subject and reproducibility

This is a new view of the frozen common source proposal at **35fb4824**, the
same 1,987-record representation used in T-013's Lean closure/projection work.
It is not a regenerated representation of STDO 3.0.2 or 3.0.3. The original
model and release bundles remain unchanged.

- Input: `../stdo-v3-common-35fb4824/run/repaired-proposal/model.json`
- Raw input SHA-256: `70feb48cf657bcb20231dbfffe0c2076e5e69b24aeb0f226a001a22957b7f56a`
- Canonical model SHA-256: `691c4ab0d0993312a31e7e2371070ea4758fdf74b32862ff4d5a32d05af79fbf`
- 1,987 local records; 1,021 external resolutions; 3,995 retention edges;
  186 authored relation records; 16,498 typed-reference occurrences.

Generate a current unified view of this same historical model with the reusable
tenant command:

```sh
python3 build_tenants/graphify/code/ac_explore.py \
  applications/stdo-v3-common-35fb4824/run/repaired-proposal/model.json \
  --source-root applications/stdo-v3-common-35fb4824/run/corpus \
  --focus urn:a-c:generation:0657852b6fd1fa48457c3f7d:record:bb792864114a40c2a0bbe3c265517dc0 \
  --title 'STDO · Read the constraints' \
  --layout unified \
  --out /tmp/stdo-constraints-new.html
```

Choose a fresh output path; existing files refuse. The same command accepts a
fully recoverable Graphify carrier as input. Omitting `--source-root` retains
recorded quotations without embedding full files. The pinned renderer is
`3d-force-graph` 1.80.1; license notices are included in the HTML and tenant
assets. No new model authoring or Lean proof run is performed by this command.
The current export includes Files navigation, repaired planar labels and the
3D/2D/Layered switch. Its presentation bytes differ from the frozen T-014
`index.html`; `VIEW.json` identifies that historical artifact's original
generator and asset cut. This command does not reproduce or replace those bytes.
