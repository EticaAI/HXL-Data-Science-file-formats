#!/bin/sh
#===============================================================================
#
#          FILE:  download-hxltm-datum.sh
#
#         USAGE:  ./testum/hxltm/download-hxltm-datum.sh
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

# hxltm-exemplum-glossarium-minimum.tm.hxl
hxltm_exemplum_glossarium_minimum="https://docs.google.com/spreadsheets/d/1isOgjeRJw__nky-YY-IR_EAZqLI6xQ96DKbD4tf0ZO8/export?format=csv&gid=453212251"

# TODO: hxltm-exemplum-glossarium.tm.hxl

# csv-3-exemplum
csv_3_exemplum="https://docs.google.com/spreadsheets/d/1isOgjeRJw__nky-YY-IR_EAZqLI6xQ96DKbD4tf0ZO8/export?format=csv&gid=800942839"

Hapi_schemam_un_htcds="https://proxy.hxlstandard.org/data/download/schemam-un-htcds_tm_hxl.csv?dest=data_edit&filter01=cut&filter-label01=Non+%23meta&cut-exclude-tags01=%23meta&cut-skip-untagged01=on&filter02=select&filter-label02=%23status%3E-1&select-query02-01=%23status%3E-1&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4%2Fedit%23gid%3D1292720422"


ROOTDIR="$(pwd)"

#### DATA PULL _________________________________________________________________

# TODO: check first if remote resources are online (or if do exist network)
#       instead of save to disk. These " if true;" are placeholders

# TODO: check error codes if download fails

if true ; then
    echo ''
    echo "hxltm_linguam"
    echo "   Fontem:   [$hxltm_exemplum_linguam]"
    echo "   Archīvum: [${ROOTDIR}/testum/hxltm/hxltm-exemplum-linguam.tm.hxl.csv]"
    wget -qO- "$hxltm_exemplum_linguam" > "${ROOTDIR}/testum/hxltm/hxltm-exemplum-linguam.tm.hxl.csv"

    # We ship some test files also with hdp-toolchain so python doc test
    # can be executed with Tox.
    echo "hxltm_linguam, hdp-toolchain package (used by python doctests"
    cp "${ROOTDIR}/testum/hxltm/hxltm-exemplum-linguam.tm.hxl.csv" "${ROOTDIR}/hxlm/data/exemplum/hxltm-exemplum-linguam.tm.hxl.csv"
fi

if true ; then
    echo ''
    echo "hxltm_exemplum_glossarium_minimum"
    echo "   Fontem:   [$hxltm_exemplum_glossarium_minimum]"
    echo "   Archīvum: [${ROOTDIR}/testum/hxltm/hxltm-exemplum-glossarium-minimum.tm.hxl.csv]"
    wget -qO- "$hxltm_exemplum_glossarium_minimum" > "${ROOTDIR}/testum/hxltm/hxltm-exemplum-glossarium-minimum.tm.hxl.csv"
fi

if true ; then
    echo ''
    echo "csv_3_exemplum"
    echo "   Fontem:   [$csv_3_exemplum]"
    echo "   Archīvum: [${ROOTDIR}/testum/hxltm/csv-3-exemplum.csv]"
    wget -qO- "$csv_3_exemplum" > "${ROOTDIR}/testum/hxltm/csv-3-exemplum.csv"
fi

# .gitignore: Do not save production test files to save space outside hapi.etica.ai
if true ; then
    echo ''
    echo "Hapi_schemam_un_htcds"
    echo "   Fontem: [$Hapi_schemam_un_htcds]"
    echo "   Filum:  [${ROOTDIR}/testum/hxltm/schemam-un-htcds.tm.hxl.csv"
    wget -qO- "$Hapi_schemam_un_htcds" > "${ROOTDIR}/testum/hxltm/schemam-un-htcds.tm.hxl.csv"
fi

exit 0
