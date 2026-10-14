# Docs pipeline
doc-gen step: completed per build/gen.log ("gen-docs 1.3: wrote build/api.md (3 operations)", "exit 0"). Generator success does not establish acceptance.
assessment: falsified against ACCEPTANCE.md (basis: spec/api.yaml, build/api.md, ACCEPTANCE.md as observed)
  - (a) every operation in spec/api.yaml has a section: falsified. spec/api.yaml declares 4 operations (GET /items, POST /items, GET /items/{id}, DELETE /items/{id}); build/api.md has 3 sections; DELETE /items/{id} has no section.
  - (b) no section contains TODO: falsified. Section "GET /items/{id}" contains "TODO: describe".
accepted: no. Criteria (a) and (b) both fail, so build/api.md is not accepted for publishing.
published: no. The publish copy was not started. publish/api.md is unchanged; it is an older partial copy containing only GET /items and does not reflect spec/api.yaml.
