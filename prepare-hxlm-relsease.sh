#!/bin/sh
# shellcheck disable=SC2129,SC2164
#===============================================================================
#
#          FILE:  prepare-hxlm-relsease.sh
#
#         USAGE:  ./prepare-hxlm-relsease.sh
#
#   DESCRIPTION:  Build scripts for EticaAI/HXL-Data-Science-file-formats
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - jq
#                     - https://stedolan.github.io/jq/
#                     - sudo apt install jq
#                 - yq
#                     - https://kislyuk.github.io/yq/
#                     - pip3 install jq yq
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0-draft
#       CREATED:  2021-04-03 16:00 UTC v1.0 created
#      REVISION:  ---
#===============================================================================

#### Build JSON Knowledge Graph from YAML ______________________________________

### YAML to JSON ---------------------------------------------------------------
echo "> YAML to JSON"

# Generate hxlm/ontologia/json/core.vkg.json
yq < hxlm/ontologia/core.vkg.yml > hxlm/ontologia/json/core.vkg.json

# Generate hxlm/ontologia/json/core.lkg.json
yq < hxlm/ontologia/core.lkg.yml > hxlm/ontologia/json/core.lkg.json


#### SHA-384 ___________________________________________________________________
echo "> SHA-384"
ROOTDIR="$(pwd)"
# echo "$ROOTDIR"

### hxlm/ontologia -------------------------------------------------------------
echo "> > hxlm/ontologia"
## Create the hashes

cd hxlm/ontologia/json/ || exit
sha384sum --tag core.lkg.json > core.lkg.json.sum
sha384sum --tag core.vkg.json > core.vkg.json.sum

## Check the hashes
sha384sum --check core.lkg.json.sum
sha384sum --check core.vkg.json.sum

### hxlm-js/ -------------------------------------------------------------------
echo "> > hxlm-js"
cd "$ROOTDIR"

## Create the hashes

cd hxlm-js/

# First file, clean old checksums
rm hxlm-js.sum


# Initialize
sha384sum --tag index.html > hxlm-js.sum

# The rest, append
sha384sum --tag bootstrapper/hdp-aux.js >> hxlm-js.sum
sha384sum --tag bootstrapper/hdp-minimam.mjs >> hxlm-js.sum
sha384sum --tag bootstrapper/hdplisp.js >> hxlm-js.sum

## Check the hashes
sha384sum --check hxlm-js.sum

#### webext-signed-pages _______________________________________________________
# @see https://github.com/tasn/webext-signed-pages
cd "$ROOTDIR"

echo "webext-signed-pages page-signer.js ..."

if [ ! -d "$ROOTDIR/temp/" ]; then
    echo "mkdir $ROOTDIR/temp/ ..."
    mkdir "$ROOTDIR/temp/"
else
    echo "OK $ROOTDIR/temp/"
fi
if [ ! -d "$ROOTDIR/temp/webext-signed-pages" ]; then
    git clone https://github.com/tasn/webext-signed-pages.git "$ROOTDIR/temp/webext-signed-pages"
    npm install minimize
else
    echo "OK $ROOTDIR/temp/webext-signed-pages"
fi

# mkdir "$ROOTDIR/temp/"
# git clone https://github.com/tasn/webext-signed-pages.git "$ROOTDIR/temp/webext-signed-pages"
# npm install minimize
page_signer="${ROOTDIR}/temp/webext-signed-pages/page-signer.js"

echo "GPG sign of hxlm-js/index.html ..."
echo "You will be asked to allow GPG sign your smartcard on this moment"
echo "${page_signer}" "${ROOTDIR}/hxlm-js/index.html" "${ROOTDIR}/hxlm-js/index-signed.html"

"${page_signer}" "${ROOTDIR}/hxlm-js/index.html" "${ROOTDIR}/hxlm-js/index-signed.html"

#### Additional commands _______________________________________________________
# cd "$ROOTDIR"
