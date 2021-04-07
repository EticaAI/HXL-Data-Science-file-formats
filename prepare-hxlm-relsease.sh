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

ROOTDIR="$(pwd)"
# echo "$ROOTDIR"

#### Build JSON Knowledge Graph from YAML ______________________________________

### YAML to JSON ---------------------------------------------------------------
echo "> YAML to JSON"

# Generate hxlm/ontologia/json/core.vkg.json
yq < hxlm/ontologia/core.vkg.yml > hxlm/ontologia/json/core.vkg.json

# Generate hxlm/ontologia/json/core.lkg.json
yq < hxlm/ontologia/core.lkg.yml > hxlm/ontologia/json/core.lkg.json

#### webext-signed-pages _______________________________________________________
# @see https://github.com/tasn/webext-signed-pages
cd "$ROOTDIR"

do_page_signer()
{
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

    echo "GPG sign of hxlm-js/index.html from hxlm-js/index-src.html ..."
    echo "You will be asked to allow GPG sign your smartcard on this moment"
    echo "${page_signer}" "${ROOTDIR}/hxlm-js/index-src.html" "${ROOTDIR}/hxlm-js/index.html"

    "${page_signer}" "${ROOTDIR}/hxlm-js/index-src.html" "${ROOTDIR}/hxlm-js/index.html"
}

# TODO: calculate the SRIHashs and put on index.html
do_simply_copy()
{
    echo "do_simply_copy..."
    ts="$(date +"%T")"
    cp "$ROOTDIR/hxlm-js/index.html" "$ROOTDIR/hxlm-js/index.$ts.old.html"
    cp "$ROOTDIR/hxlm-js/index-src.html" "$ROOTDIR/hxlm-js/index.html"
}

echo "page_signer (full GPG sign) disabled at the moment"
do_simply_copy


#### SHA-384 ___________________________________________________________________
echo "> SHA-384"

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
sha384sum --tag index-src.html > hxlm-js.sum
sha384sum --tag bootstrapper/hdpb-aux.mjs >> hxlm-js.sum
sha384sum --tag bootstrapper/hdpb-minimam.mjs >> hxlm-js.sum
sha384sum --tag bootstrapper/lisp/hdpb-lisp.mjs >> hxlm-js.sum
sha384sum --tag bootstrapper/testum.mjs >> hxlm-js.sum

## Check the hashes
sha384sum --check hxlm-js.sum

# echo "> SRI Hash Generator (https://www.srihash.org/)"
# echo "@TODO: automate better. At the moment these hashes need to be written on"
# echo "       the hxlm-js/index-src.html before using the page_signer to"
# echo "       generate the hxlm-js/index.html"
# echo ""

# sri_hdp_aux="$(openssl dgst -sha384 -binary bootstrapper/hdpb-aux.mjs | openssl base64 -A)"
# echo "<script src=\"./bootstrapper/hdp-aux.js\" integrity=\"sha384-${sri_hdp_aux}\" crossorigin=\"anonymous\"></script>"

# sri_hdp_miniman="$(openssl dgst -sha384 -binary bootstrapper/hdpb-minimam.mjs | openssl base64 -A)"
# echo "<script src=\"./bootstrapper/hdp-minimam.mjs\" integrity=\"sha384-${sri_hdp_miniman}\" crossorigin=\"anonymous\"></script>"

# sri_hdplisp="$(openssl dgst -sha384 -binary bootstrapper/hdpb-lisp.mjs | openssl base64 -A)"
# echo "<script src=\"./bootstrapper/hdplisp.js\" integrity=\"sha384-${sri_hdplisp}\" crossorigin=\"anonymous\"></script>"

# echo "bootstrapper/hdp-aux.js"
# openssl dgst -sha384 -binary bootstrapper/hdp-aux.js | openssl base64 -A
# echo ""

# echo "bootstrapper/hdp-minimam.js"
# openssl dgst -sha384 -binary bootstrapper/hdp-minimam.js | openssl base64 -A
# echo ""


#### Additional commands _______________________________________________________
# cd "$ROOTDIR"
