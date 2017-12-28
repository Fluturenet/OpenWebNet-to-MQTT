#!/bin/bash
set -e

CONFIG_PATH=/data/options.json

#USB=$(jq --raw-output ".UsbPath" $CONFIG_PATH)

python /byn/ownserver.py
