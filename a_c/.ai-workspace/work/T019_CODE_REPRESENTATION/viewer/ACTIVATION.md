# T-019 reader Worker activation

Role: bounded Worker `/root/repair_project_origin`, activated by the Executive
after checkpoint `c034593eea08d46679a00ba7b196abac7e9e006a` was pushed.
Outcome: read an additive code-and-trace overlay in the shared offline reader,
preserving the native representation and its proof scope.

Basis: `a_c/stdo_a_c.json`, installed STDO `v2.5.1-rc.2`, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
Ordinary manager status with verification returned installed/valid and no
failures. Governing source: common CR-01–07, PU-03/04/06, the tenant
`design/code-realization.md` and existing constraint-explorer design.

Write territory: `viewer/explorer.html`, `explorer.js`, `explorer.css`,
`test_env/test_explorer_code.cjs` and this viewer evidence directory. The
conditionally granted `viewer/layered.js` is needed because its explicit
color/marker/description table otherwise omits the new edge layers and calls
them references. Only those presentations change; layout remains unchanged.
No Git, common WHAT, backend, frozen application or release mutation.

The backend owns overlay acquisition/schema and supplies a generated artifact.
Reader tests use synthetic fixtures and that artifact through jsdom already
available in the session. Source and raw observations remain text nodes. DOM,
geometry and stubbed-force tests do not establish browser/WebGL qualification.
