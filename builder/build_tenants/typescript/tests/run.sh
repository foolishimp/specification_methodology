#!/bin/sh
# Runs every check of the build tenant: the compiler, the tests and the compliance checks.
# The tests that cut a release run after the other tests, apart from them: each cut builds, installs and walks the guide's tickets, and that load does not enter the tests that time the framework's own processes (D233).
# The scale test measures the framework's own time, so it runs alone, after the other tests, and their load does not enter its figure (D228).
cd "$(dirname "$0")/.." || exit 1
[ -d node_modules ] || pnpm install --frozen-lockfile --prefer-offline >/dev/null || exit 1
SCALE=tests/scale_repository.scenario.test.ts
CUTS="tests/bundle.test.ts tests/cut_changed.test.ts tests/cut_fails.test.ts tests/library.scenario.test.ts tests/release.test.ts tests/release_record.scenario.test.ts tests/s1.scenario.test.ts tests/setup_inside_repository.scenario.test.ts"
APART=""
for f in $CUTS $SCALE; do APART="$APART --exclude $f"; done
pnpm typecheck && pnpm test $APART && pnpm test $CUTS && pnpm test "$SCALE" && pnpm check:compliance
