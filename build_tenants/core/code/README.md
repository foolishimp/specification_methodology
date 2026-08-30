# Core Code

`ac.py` is the complete MVP executable surface. It validates a program against
a URI Binding Set, emits a logical constraint map only when validation is
valid, and joins an ordered list of caller-supplied labels and text.

```sh
python3 build_tenants/core/code/ac.py validate \
  --program dogfood/self/axiomatic-program.json \
  --bindings dogfood/self/bindings.json \
  --output dogfood/self/validation-report.json \
  --emit-map dogfood/self/logical-constraint-map.json

python3 build_tenants/core/code/ac.py join \
  --input dogfood/abg/executive-sections.json \
  --output dogfood/abg/executive-request.txt

python3 -m unittest discover -s build_tenants/core/code -p 'test_*.py' -v
```

The executable does not call an LLM or modify an authored program. The LLM is
the harness, uses diagnostics to author a new candidate, and supplies every
label, text section, and ordering choice to the joiner.
