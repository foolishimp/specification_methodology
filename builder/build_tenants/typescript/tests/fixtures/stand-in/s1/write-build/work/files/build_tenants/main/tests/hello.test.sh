#!/bin/sh
# REQ-HELLO-001: run with no arguments, the program prints hello, world and exits with code 0.
out=$(sh ../code/hello.sh)
code=$?
[ "$code" -eq 0 ] || { echo "exit code $code, not 0"; exit 1; }
[ "$out" = "hello, world" ] || { echo "printed '$out', not 'hello, world'"; exit 1; }
