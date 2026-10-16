#!/bin/bash
AC=$1; OUT=$2; cd /Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude
mkdir -p "$OUT/projections"; LOG=$OUT/commands.log; : > $LOG
run(){ echo "$(date -u +%FT%TZ) $*" >> $LOG; python3 -I "$AC" "$@"; echo "exit=$?" >> $LOG; }
run validate --program a_c/i3/axiomatic-program.json --bindings a_c/i3/bindings.json --output "$OUT/validation-report.json" --emit-map "$OUT/logical-constraint-map.json"
# every frame index the program declares, in program order (I5-05: the list is no longer fixed at four)
for ix in $(python3 -I -c "import json; print(' '.join(f['uri'].rsplit(':', 1)[-1] for f in json.load(open('a_c/i3/axiomatic-program.json'))['frame_indexes']))"); do
 for mode in reference-only materialized; do
  run project --program a_c/i3/axiomatic-program.json --map "$OUT/logical-constraint-map.json" --bindings a_c/i3/bindings.json --frame-index urn:stdo-3:claude:i3:frame-index:$ix --mode $mode --output "$OUT/projections/projection-$ix-$mode.json"
 done; done
