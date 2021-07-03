#!/bin/sh
#===============================================================================
#
#          FILE:  download-hxltm-datum.sh
#
#         USAGE:  ./tests/hxltm/download-hxltm-datum.sh
#
#   DESCRIPTION:  Download data from Google Spreadsheets via HXL-Proxy
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2021-05-13 20:16 UTC started, based on EticaAI/
#                         HXL-Data-Science-file-formats/prepare-hxlm-relsease.sh
#      REVISION:  2021-07-03 03:08 UTC, started, based on
#    HXL-CPLP/Auxilium-Humanitarium-API/_systema/programma/download-hxl-datum.sh
#===============================================================================

# Trivia:
# - "download"
#   - Note: no idea what word use for 'download' not even in New Latin
#   - https://en.wiktionary.org/wiki/download
# - "HXLTM"
#   - https://github.com/HXL-CPLP/forum/issues/58
#     - HXL
#       - https://hxlstandard.org/
# - "datum"
#   - https://en.wiktionary.org/wiki/datum#Latin



#### HXLTM-Exemplum ____________________________________________________________
# @see https://docs.google.com/spreadsheets/d/1isOgjeRJw__nky-YY-IR_EAZqLI6xQ96DKbD4tf0ZO8/edit#gid=0

# @see https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1181688279
# Hapi_L10N="https://proxy.hxlstandard.org/data/download/L10n_hxl_csv.csv?dest=data_edit&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4%2Fedit%23gid%3D1181688279"
hxltm_exemplum_linguam="https://proxy.hxlstandard.org/data/download/hxltm-exemplum-linguam_tm_hxl.csv?dest=data_edit&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1isOgjeRJw__nky-YY-IR_EAZqLI6xQ96DKbD4tf0ZO8%2Fedit%23gid%3D1241276648"

ROOTDIR="$(pwd)"

#### DATA PULL _________________________________________________________________

# TODO: check first if remote resources are online (or if do exist network)
#       instead of save to disk. These " if true;" are placeholders

# TODO: check error codes if download fails

if true ; then
    echo ''
    echo "hxltm_linguam"
    echo "   Fontem:   [$hxltm_exemplum_linguam]"
    echo "   Archīvum: [${ROOTDIR}/tests/hxltm/hxltm-exemplum-linguam.tm.hxl.csv]"
    wget -qO- "$hxltm_exemplum_linguam" > "${ROOTDIR}/tests/hxltm/hxltm-exemplum-linguam.tm.hxl.csv"
fi

exit 0
