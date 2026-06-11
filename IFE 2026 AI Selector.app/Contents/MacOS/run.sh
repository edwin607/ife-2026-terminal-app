#!/bin/bash
DIR="$(cd "$(dirname "$0")/../Resources" && pwd)"
if [ -t 0 ]; then
  exec /usr/bin/env node "$DIR/script.js"
else
  exec osascript -e "tell application \"Terminal\" to do script \"cd '$DIR' && /usr/bin/env node 'script.js'\"" 
fi
