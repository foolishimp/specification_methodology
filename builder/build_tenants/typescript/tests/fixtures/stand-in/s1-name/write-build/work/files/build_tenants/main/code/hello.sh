#!/bin/sh
# Hello. Carries out REQ-HELLO-001.
if [ "$1" = "--name" ] && [ -n "$2" ]; then
  printf 'hello, %s\n' "$2"
else
  printf 'hello, world\n'
fi
