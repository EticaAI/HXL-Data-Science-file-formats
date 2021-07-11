#!/bin/sh
#===============================================================================
#
#          FILE:  manuale-testum.sh
#
#         USAGE:  ./testum/hxltm/manuale-testum.sh
#
#   DESCRIPTION:  Manual testum for hxltmcli.
#                 This file can also be used to undestand how the output
#                 of testum/hxltm/resultatum was created
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
#       CREATED:  2021-07-03 03:08 UTC
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
# set -e

#### Variables ________________________________________________________________
ROOTDIR="$(pwd)"

# For HXLTM-Exemplum
# @see https://docs.google.com/spreadsheets/d/1isOgjeRJw__nky-YY-IR_EAZqLI6xQ96DKbD4tf0ZO8/edit#gid=0

HXLTM_EXEMPLUM_XLSX_LOCAL="HXLTM-Exemplum.xlsx"
HXLTM_EXEMPLUM_XLSX_GSHEETS="https://docs.google.com/spreadsheets/d/1isOgjeRJw__nky-YY-IR_EAZqLI6xQ96DKbD4tf0ZO8/export?format=xlsx"

# HXLTM_EXEMPLUM_LINGUAM_LOCAL="${ROOTDIR}/hxltm-linguam.tm.hxl.csv"
HXLTM_EXEMPLUM_LINGUAM_LOCAL="hxltm-exemplum-linguam.tm.hxl.csv"
HXLTM_EXEMPLUM_LINGUAM_GSHEETS="https://docs.google.com/spreadsheets/d/1isOgjeRJw__nky-YY-IR_EAZqLI6xQ96DKbD4tf0ZO8/edit#gid=1241276648"

HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_TMX_LOCAL="resultatum/hxltm-exemplum-linguam.tmx"
HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_XLIFF_LOCAL="resultatum/hxltm-exemplum-linguam.xlf"

# .gitignore: Do not save production test files to save space outside hapi.etica.ai
# Hapi_schemam_un_htcds
Hapi_schemam_un_htcds="schemam-un-htcds.tm.hxl.csv"
Hapi_schemam_un_htcds_RESULTATUM_TMX_LOCAL="resultatum/schemam-un-htcds.tmx"
Hapi_schemam_un_htcds_RESULTATUM_XLIFF_LOCAL="resultatum/schemam-un-htcds.xlf"
Hapi_schemam_un_htcds_RESULTATUM_BILINGUAL_HXL_CSV_LOCAL="resultatum/schemam-un-htcds_eng-Latn_por-Latn.hxl.csv"

#### Init testum and chechs _____________________________________________________
cd "$ROOTDIR/testum/hxltm" || exit

if [ ! -f "$HXLTM_EXEMPLUM_XLSX_LOCAL" ]; then
    echo "$HXLTM_EXEMPLUM_XLSX_LOCAL not found."
    echo "$HXLTM_EXEMPLUM_XLSX_GSHEETS download now..."
    wget -qO- "$HXLTM_EXEMPLUM_XLSX_GSHEETS" > "$HXLTM_EXEMPLUM_XLSX_LOCAL"
# else
    #echo "$HXLTM_EXEMPLUM_XLSX_LOCAL exists"
fi

#### main ______________________________________________________________________

printf "\n\n\n\tTESTUM 001 HXLTM_EXEMPLUM_LINGUAM_GSHEETS\n\n"
echo "hxltmcli $HXLTM_EXEMPLUM_LINGUAM_GSHEETS | grep L10N_ego_codicem"
hxltmcli "$HXLTM_EXEMPLUM_LINGUAM_GSHEETS" | grep L10N_ego_codicem

printf "\n\n\n\tTESTUM 002 HXLTM_EXEMPLUM_LINGUAM_LOCAL\n\n"
echo "hxltmcli $HXLTM_EXEMPLUM_LINGUAM_LOCAL | grep L10N_ego_codicem"
hxltmcli "$HXLTM_EXEMPLUM_LINGUAM_LOCAL" | grep L10N_ego_codicem

printf "\n\n\n\tTESTUM 003 HXLTM_EXEMPLUM_XLSX_LOCAL\n\n"
echo "hxltmcli --sheet 2 $HXLTM_EXEMPLUM_XLSX_LOCAL | grep L10N_ego_codicem" 
hxltmcli --sheet 2 "$HXLTM_EXEMPLUM_XLSX_LOCAL" | grep L10N_ego_codicem

# printf "\n\n\n\tTESTUM 004 HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_TMX_LOCAL\n\n"
# echo hxltmcli "$HXLTM_EXEMPLUM_LINGUAM_LOCAL" "$HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_TMX_LOCAL" --objectivum-TMX
# hxltmcli "$HXLTM_EXEMPLUM_LINGUAM_LOCAL" "$HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_TMX_LOCAL" --objectivum-TMX

printf "\n\n\n\tTESTUM 005 HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_XLIFF_LOCAL\n\n"
echo hxltmcli "$HXLTM_EXEMPLUM_LINGUAM_LOCAL" "$HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_XLIFF_LOCAL" --objectivum-XLIFF
hxltmcli "$HXLTM_EXEMPLUM_LINGUAM_LOCAL" "$HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_XLIFF_LOCAL" --objectivum-XLIFF

# hxltmcli hxltm-exemplum-glossarium-minimum.tm.hxl.csv

## The hxltmcli fails with non HXLated input
#     hxltmcli csv-3-exemplum.csv
## This is one way to prepare the input using hxltag (libhxl-python tool)
#     hxltag -m en-GB#item+rem+i_en+i_eng+is_latn -m pt-PT#item+rem+i_pt+i_por+is_latn -m Comment#meta csv-3-exemplum.csv
#     hxltag -m en-GB#item+rem+i_en+i_eng+is_latn -m pt-PT#item+rem+i_pt+i_por+is_latn -m Comment#meta csv-3-exemplum.csv | hxltmcli
## ... --JSON-kv
#     hxltag -m en-GB#item+rem+i_en+i_eng+is_latn -m pt-PT#item+rem+i_pt+i_por+is_latn -m Comment#meta csv-3-exemplum.csv | hxltmcli -f eng-Latn@en-GB -o por-Latn@pt-PT --JSON-kv
#     hxltag -m en-GB#item+rem+i_en+i_eng+is_latn -m pt-PT#item+rem+i_pt+i_por+is_latn -m Comment#meta csv-3-exemplum.csv | hxltmcli -f eng-Latn@en-GB -o por-Latn@pt-PT --JSON-kv > resultatum/json/pt.csv
## ... --CSV-3
#     hxltag -m en-GB#item+rem+i_en+i_eng+is_latn -m pt-PT#item+rem+i_pt+i_por+is_latn -m Comment#meta csv-3-exemplum.csv | hxltmcli -f eng-Latn@en-GB -o por-Latn@pt-PT --CSV-3
#     hxltag -m en-GB#item+rem+i_en+i_eng+is_latn -m pt-PT#item+rem+i_pt+i_por+is_latn -m Comment#meta csv-3-exemplum.csv | hxltmcli -f eng-Latn@en-GB -o por-Latn@pt-PT --CSV-3 > resultatum/csv-3-exemplum.csv

printf "\n\n\n\tTESTUM 010 Hapi_schemam_un_htcds\n\n"
echo hxltmcli "$Hapi_schemam_un_htcds" "$Hapi_schemam_un_htcds_RESULTATUM_TMX_LOCAL" --objectivum-TMX
hxltmcli "$Hapi_schemam_un_htcds" "$Hapi_schemam_un_htcds_RESULTATUM_TMX_LOCAL" --objectivum-TMX

printf "\n\n\n\tTESTUM 011 Hapi_schemam_un_htcds\n\n"
echo hxltmcli "$Hapi_schemam_un_htcds" "$Hapi_schemam_un_htcds_RESULTATUM_BILINGUAL_HXL_CSV_LOCAL" --objectivum-CSV-HXLated-XLIFF --fontem-linguam eng-Latn@en --objectivum-linguam por-Latn@pt
hxltmcli "$Hapi_schemam_un_htcds" "$Hapi_schemam_un_htcds_RESULTATUM_BILINGUAL_HXL_CSV_LOCAL" --objectivum-CSV-HXLated-XLIFF --fontem-linguam eng-Latn@en --objectivum-linguam por-Latn@pt

printf "\n\n\n\tTESTUM 012 Hapi_schemam_un_htcds\n\n"
echo hxltmcli "$Hapi_schemam_un_htcds" "$Hapi_schemam_un_htcds_RESULTATUM_XLIFF_LOCAL" --objectivum-XLIFF --fontem-linguam eng-Latn@en --objectivum-linguam por-Latn@pt
hxltmcli "$Hapi_schemam_un_htcds" "$Hapi_schemam_un_htcds_RESULTATUM_XLIFF_LOCAL" --objectivum-XLIFF --fontem-linguam eng-Latn@en --objectivum-linguam por-Latn@pt

# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/testum/hxltm$ hxltmcli schemam-un-htcds.tm.hxl.csv resultatum/schemam-un-htcds.xlf --objectivum-XLIFF --fontem-linguam eng-Latn@en


# To revert only one file that keeps changing even with same input
# git checkout -- testum/hxltm/resultatum/hxltm-exemplum-linguam.tmx

exit 0
