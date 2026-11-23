#!/bin/sh
# Runs every test of Hello; exits with zero only when all pass.
cd "$(dirname "$0")" || exit 1
failed=0
for t in ./*.test.sh; do
  if sh "$t"; then echo "pass $t"; else echo "FAIL $t"; failed=1; fi
done
exit $failed
