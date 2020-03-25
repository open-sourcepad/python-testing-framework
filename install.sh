#!/usr/bin/env bash
echo "Installing required packages"

type virtualenv >/dev/null 2>&1 || { echo >&2 "No suitable python virtual env tool found, aborting"; exit 1; }
# rm -rf .venv
virtualenv -p python3 .venv
source .venv/bin/activate
pip3 install -r requirements.txt
echo "Done"
