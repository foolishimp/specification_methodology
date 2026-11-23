#!/bin/sh
# Runs every check of the build tenant: the compiler, the tests and the compliance checks.
cd "$(dirname "$0")/.." || exit 1
[ -d node_modules ] || pnpm install --frozen-lockfile --prefer-offline >/dev/null || exit 1
pnpm check
