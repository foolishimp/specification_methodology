#!/bin/bash
AC=$1; OUT=$2; cd "$(cd "$(dirname "$0")/../../.." && pwd)"  # the tenant root that holds this script, so a clean archive runs it unchanged (I5-05)
mkdir -p "$OUT/projections"; LOG=$OUT/commands.log; : > $LOG
FAIL=0
run(){ echo "$(date -u +%FT%TZ) $*" >> $LOG; python3 -I "$AC" "$@"; rc=$?; echo "exit=$rc" >> $LOG; [ $rc -eq 0 ] || FAIL=1; }
run validate --program a_c/i3/axiomatic-program.json --bindings a_c/i3/bindings.json --output "$OUT/validation-report.json" --emit-map "$OUT/logical-constraint-map.json"
# every frame index the program declares, in program order (I5-05: the list is no longer fixed at four)
IX=$(python3 -I -c "import json; print(' '.join(f['uri'].rsplit(':', 1)[-1] for f in json.load(open('a_c/i3/axiomatic-program.json'))['frame_indexes']))"); rc=$?
if [ $rc -ne 0 ] || [ -z "$IX" ]; then echo "frame-index enumeration exit=$rc indexes=${IX:-none}" >> $LOG; echo "run_ac.sh: no frame index enumerated (exit $rc)" >&2; exit 1; fi  # a failed or empty enumeration fails the run
for ix in $IX; do
 for mode in reference-only materialized; do
  run project --program a_c/i3/axiomatic-program.json --map "$OUT/logical-constraint-map.json" --bindings a_c/i3/bindings.json --frame-index urn:stdo-3:claude:i3:frame-index:$ix --mode $mode --output "$OUT/projections/projection-$ix-$mode.json"
 done; done
exit $FAIL  # a failed validate or projection fails the run; the log keeps every exit code
