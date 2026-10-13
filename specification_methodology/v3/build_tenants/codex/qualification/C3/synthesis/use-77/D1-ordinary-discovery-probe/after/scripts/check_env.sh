#!/bin/sh
# APP_TOKEN is the deprecated name for APP_API_TOKEN; still accepted as a fallback.
: "${APP_API_TOKEN:=${APP_TOKEN-}}"
: "${APP_API_TOKEN:?missing}"
echo ok
