#!/bin/sh
# REQ-HELLO-001: run with no arguments, the program prints hello, world; run with --name Ada, it prints hello, Ada; each exits with code 0.
out=$(sh ../code/hello.sh)
code=$?
[ "$code" -eq 0 ] || { echo "exit code $code, not 0"; exit 1; }
[ "$out" = "hello, world" ] || { echo "printed '$out', not 'hello, world'"; exit 1; }
out=$(sh ../code/hello.sh --name Ada)
code=$?
[ "$code" -eq 0 ] || { echo "exit code $code with --name, not 0"; exit 1; }
[ "$out" = "hello, Ada" ] || { echo "printed '$out', not 'hello, Ada'"; exit 1; }
