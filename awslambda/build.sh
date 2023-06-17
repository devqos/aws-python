#!/bin/bash

pack_directory() {
  local directory=$1
  local zipName="${directory}.zip"
  zip -r "$zipName" "$directory"
}

directories=$(find . -maxdepth 1 -type d)

for dir in $directories; do
  if [ "$dir" != "." ]; then
    pack_directory "$dir"
  fi
done
