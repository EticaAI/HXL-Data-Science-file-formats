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

#### Customizations, ___________________________________________________________

### Data pull configurations ---------------------------------------------------

# @see https://docs.google.com/spreadsheets/d/1NIlLAAhvuotq5QR2vGTrCe1ZuTT_k4vhCoEB3qjo7TU/edit#gid=1204322111
ONTOLOGIA_COD_THESAURUM="https://proxy.hxlstandard.org/data.csv?dest=data_edit&filter01=select&filter-label01=%23code%2Bwikidata+not+empty&select-query01-01=%23code%2Bwikidata%3D&select-reverse01=on&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1NIlLAAhvuotq5QR2vGTrCe1ZuTT_k4vhCoEB3qjo7TU%2Fedit%23gid%3D1204322111"
ONTOLOGIA_COD_SERVITIUM_AUXILIUM_MAPPAM="https://proxy.hxlstandard.org/data.csv?dest=data_edit&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1NIlLAAhvuotq5QR2vGTrCe1ZuTT_k4vhCoEB3qjo7TU%2Fedit%23gid%3D1420201282"
ONTOLOGIA_COD_SERVITIUM_AUXILIUM_POPULATIONEM_STATISTICUM="https://proxy.hxlstandard.org/data.csv?dest=data_edit&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1NIlLAAhvuotq5QR2vGTrCe1ZuTT_k4vhCoEB3qjo7TU%2Fedit%23gid%3D1207295802"

# @see https://docs.google.com/spreadsheets/d/1MFjopmmiBMWxxYEaypbWKiWhxvsH-2UVb_u1JN8RSkQ/edit#gid=764269111
ONTOLOGIA_URN_REGULARE_EXPRESSIONEM="https://proxy.hxlstandard.org/data.csv?dest=data_edit&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1MFjopmmiBMWxxYEaypbWKiWhxvsH-2UVb_u1JN8RSkQ%2Fedit%23gid%3D982460844"

ROOTDIR="$(pwd)"

#### DATA PULL _________________________________________________________________

# TODO: check first if remote resources are online (or if do exist network)
#       instead of save to disk. These " if true;" are placeholders

if true ; then
    wget -qO- "$ONTOLOGIA_COD_THESAURUM" > "${ROOTDIR}/ontologia/cod/thesaurum.hxl.csv"
fi
if true ; then
    wget -qO- "$ONTOLOGIA_COD_SERVITIUM_AUXILIUM_MAPPAM" > "${ROOTDIR}/ontologia/cod/servitium-auxilium-mappam.hxl.csv"
fi
if true ; then
    wget -qO- "$ONTOLOGIA_COD_SERVITIUM_AUXILIUM_POPULATIONEM_STATISTICUM" > "${ROOTDIR}/ontologia/cod/servitium-auxilium-populationem-statisticum.hxl.csv"
fi

if true ; then
    wget -qO- "$ONTOLOGIA_URN_REGULARE_EXPRESSIONEM" > "${ROOTDIR}/ontologia/urn/regulare-expressionem.hxl.csv"
fi


# ONTOLOGIA_COD_THESAURUM

#### Build JSON Knowledge Graph from YAML ______________________________________

### YAML to JSON ---------------------------------------------------------------
echo "> YAML to JSON"

# Generate ontologia/json/core.vkg.json
yq < ontologia/cor.hdplisp.yml > ontologia/json/cor.hdplisp.json

# Generate ontologia/json/core.vkg.json
yq < ontologia/core.vkg.yml > ontologia/json/core.vkg.json

# Generate ontologia/json/core.lkg.json
yq < ontologia/core.lkg.yml > ontologia/json/core.lkg.json

# Generate ontologia/servitium.hdplisp.yml
yq < ontologia/servitium.hdplisp.yml > ontologia/json/servitium.hdplisp.json

# Generate ontologia/servitium.hdplisp.yml
yq < ontologia/urn/defallo.urn.yml > ontologia/json/defallo.urn.json

# Generate ontologia/servitium.hdplisp.yml
yq < ontologia/cor.hxltm.yml > ontologia/json/cor.hxltm.json

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

### ontologia -------------------------------------------------------------
echo "> > ontologia"
## Create the hashes

cd ontologia/json/ || exit
sha384sum --tag cor.hdplisp.json > cor.hdplisp.json.sum
sha384sum --tag core.lkg.json > core.lkg.json.sum
sha384sum --tag core.vkg.json > core.vkg.json.sum
sha384sum --tag servitium.hdplisp.json > servitium.hdplisp.json.sum
sha384sum --tag defallo.urn.json > defallo.urn.json.sum
sha384sum --tag cor.hxltm.json > cor.hxltm.json.sum

## Check the hashes
sha384sum --check cor.hdplisp.json.sum
sha384sum --check core.lkg.json.sum
sha384sum --check core.vkg.json.sum
sha384sum --check servitium.hdplisp.json.sum
sha384sum --check defallo.urn.json.sum
sha384sum --check cor.hxltm.json.sum

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

#### pypi ______________________________________________________________________
### Upload, register step ------------------------------------------------------

## @see https://packaging.python.org/tutorials/packaging-projects/
# python3 -m pip install --upgrade build
# python3 -m build
## Note: create token a save on $HOME/.pypirc
##       the instructions will be from
#        - https://test.pypi.org/manage/account/token/
#        - https://pypi.org/manage/account/token/

## Test server
# python3 -m twine upload --repository testpypi dist/*
# >> https://test.pypi.org/project/hdp-toolchain/0.8.7/

## Production server
# python3 -m twine upload --repository pypi dist/*
# >> View at: https://pypi.org/project/hdp-toolchain/0.8.7/

### Upload, each new version ---------------------------------------------------
# rm dist/*
# python3 -m build
# python3 -m twine upload --repository pypi dist/*

### Upload, typical ------------------------------------------------------------

### Preparing symlinks, ontologia
# cd /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/ontologia || exit
# ln -s ../../ontologia/README.md ./README.md
# ln -s ../../ontologia/cor.hdplisp.yml ./cor.hdplisp.yml
# ln -s ../../ontologia/core.lkg.yml ./core.lkg.yml
# ln -s ../../ontologia/core.urn.yml ./core.urn.yml
# ln -s ../../ontologia/core.vkg.yml ./core.vkg.yml
# ln -s ../../ontologia/hdp.json-schema.json ./hdp.json-schema.json
# ln -s ../../ontologia/URNData.ebnf ./URNData.ebnf

# cd /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/ontologia/json || exit
# ln -s ../../../ontologia/json/cor.hdplisp.json ./cor.hdplisp.json
# ln -s ../../../ontologia/json/cor.hdplisp.json.sum ./cor.hdplisp.json.sum
# ln -s ../../../ontologia/json/core.lkg.json ./core.lkg.json
# ln -s ../../../ontologia/json/core.lkg.json.sum ./core.lkg.json.sum
# ln -s ../../../ontologia/json/core.vkg.json ./core.vkg.json
# ln -s ../../../ontologia/json/core.vkg.json.sum ./core.vkg.json.sum

# cd /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/data/baseline/hdataset/lang || exit
# mv /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/data/baseline/hdataset/lang/lang.csv /workspace/git/EticaAI/HXL-Data-Science-file-formats/ontologia/codicem-linguam.hxl.csv
# mv /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/data/baseline/hdataset/place/place.csv /workspace/git/EticaAI/HXL-Data-Science-file-formats/ontologia/codicem/codicem-locum.hxl.csv

# ln -s ../../../../../ontologia/codicem/codicem.locum.hxl.csv ./place.csv
# ln -s ../../../../../ontologia/codicem/codicem.linguam.hxl.csv ./lang.csv
# cd /workspace/git/EticaAI/HXL-Data-Science-file-formats/ontologia/iso || exit
# ln -s ../codicem/codicem.linguam.hxl.csv ./iso.639-3.hxl.csv
# ln -s ../codicem/codicem.locum.hxl.csv ./iso.3166.hxl.csv

# ln -s ../../../../ontologia/README.md hdpl-conventions/prototype/hdpl/ontologia/README.md

# ln -s ../../../../../ontologia/codicem/codicem.linguam.hxl.csv hdpl-conventions/prototype/hdpl/ontologia/codicem/codicem.linguam.hxl.csv
# ln -s ../../../../../ontologia/codicem/codicem.locum.hxl.csv hdpl-conventions/prototype/hdpl/ontologia/codicem/codicem.locum.hxl.csv
# ln -s ../../../../../ontologia/codicem/codicem.numerum.hxl.csv hdpl-conventions/prototype/hdpl/ontologia/codicem/codicem.numerum.hxl.csv
# ln -s ../../../../../ontologia/codicem/codicem.scriptum.hxl.csv hdpl-conventions/prototype/hdpl/ontologia/codicem/codicem.scriptum.hxl.csv

# ln -s ../../../../../ontologia/json/cor.hdplisp.json hdpl-conventions/prototype/hdpl/ontologia/json/cor.hdplisp.json
# ln -s ../../../../../ontologia/json/core.lkg.json hdpl-conventions/prototype/hdpl/ontologia/json/core.lkg.json
# ln -s ../../../../../ontologia/json/core.vkg.json hdpl-conventions/prototype/hdpl/ontologia/json/core.vkg.json
# ln -s ../../../../../ontologia/json/servitium.hdplisp.json hdpl-conventions/prototype/hdpl/ontologia/json/servitium.hdplisp.json

# urnresolver-default.urn.yml
# cd /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin || exit
# ln -s ../../../ontologia/urn/defallo.urn.yml hxlm/core/bin/urnresolver-default.urn.yml
# ln -s ../../../ontologia/servitium.urn.yml servitium.urn.yml
# cd /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/ontologia/urn || exit
# ln -s ../../../ontologia/urn/defallo.urn.yml defallo.urn.yml
# cd /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/ontologia/json || exit
# ln -s ../../../ontologia/json/defallo.urn.json defallo.urn.json

### Preparing symlinks, build scripts
# cd /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin || exit
# ln -s ../../../bin/hxl2tab hxl2tab.py
# ln -s ../../../bin/hxlquickimport hxlquickimport.py
# ln -s ../../../bin/hxlquickmeta hxlquickmeta.py

# ln -s /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin/urnprovider_local.py /workspace/bin/urnprovider-local
# cd /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin || exit
# ln -s ../../../ontologia/servitium.urn.yml servitium.urn.yml

# cor.hxltm.yml
# cd /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin || exit
# ln -s ../../../ontologia/cor.hxltm.yml cor.hxltm.yml
