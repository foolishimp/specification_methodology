# Core Code

`ac.py` is the complete MVP executable surface. It validates a program against
a URI Binding Set, emits a logical constraint map only when validation is
valid, projects explicitly selected frame indexes, and joins an ordered list
of caller-supplied labels and text.

```sh
python3 build_tenants/core/code/ac.py validate \
  --program dogfood/self/axiomatic-program.json \
  --bindings dogfood/self/bindings.json \
  --output dogfood/self/validation-report.json \
  --emit-map dogfood/self/logical-constraint-map.json

python3 build_tenants/core/code/ac.py join \
  --input dogfood/abg/executive-sections.json \
  --output dogfood/abg/executive-request.txt

python3 build_tenants/core/code/ac.py project \
  --program program.json --map map.json --bindings bindings.json \
  --frame-index urn:example:index:transfer \
  --mode materialized --output projection.json

python3 -m unittest discover -s build_tenants/core/code -p 'test_*.py' -v
```

The executable does not call an LLM or modify an authored program. The LLM is
the harness, uses diagnostics to author a new candidate, and supplies every
label, text section, and ordering choice to the joiner.

Projection requires a current exact program/map pair and explicit index/mode
selection. `reference-only` and `materialized` share one authored reference and
affected-residual closure. The latter copies original item content unchanged;
neither evaluates conditions or selects a task disposition. A stale source,
missing dependency, mismatched map or unsafe output route returns diagnostics.
Safe stale projection outputs are removed on refusal; input/source aliases are
preserved. Use stable read inputs and exclusive output scope for each invocation.
