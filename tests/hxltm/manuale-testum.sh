#!/bin/sh
#===============================================================================
#
#          FILE:  manuale-testum.sh
#
#         USAGE:  ./tests/hxltm/manuale-testum.sh
#
#   DESCRIPTION:  Manual tests for hxltmcli.
#                 This file can also be used to undestand how the output
#                 of tests/hxltm/resultatum was created
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

HXLTM_EXEMPLUM_XLSX_LOCAL="HXLTM-Exemplum.xlsx"
HXLTM_EXEMPLUM_XLSX_GSHEETS="https://docs.google.com/spreadsheets/d/1isOgjeRJw__nky-YY-IR_EAZqLI6xQ96DKbD4tf0ZO8/export?format=xlsx"

# HXLTM_EXEMPLUM_LINGUAM_LOCAL="${ROOTDIR}/hxltm-linguam.tm.hxl.csv"
HXLTM_EXEMPLUM_LINGUAM_LOCAL="hxltm-exemplum-linguam.tm.hxl.csv"
HXLTM_EXEMPLUM_LINGUAM_GSHEETS="https://docs.google.com/spreadsheets/d/1isOgjeRJw__nky-YY-IR_EAZqLI6xQ96DKbD4tf0ZO8/edit#gid=1241276648"

HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_TMX_LOCAL="resultatum/hxltm-exemplum-linguam.tmx"
HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_XLIFF_LOCAL="resultatum/hxltm-exemplum-linguam.xlf"

#### Init tests and chechs _____________________________________________________
cd "$ROOTDIR/tests/hxltm" || exit

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

printf "\n\n\n\tTESTUM 004 HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_TMX_LOCAL\n\n"
echo hxltmcli "$HXLTM_EXEMPLUM_LINGUAM_LOCAL" "$HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_TMX_LOCAL" --objectivum-TMX
hxltmcli "$HXLTM_EXEMPLUM_LINGUAM_LOCAL" "$HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_TMX_LOCAL" --objectivum-TMX

printf "\n\n\n\tTESTUM 005 HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_XLIFF_LOCAL\n\n"
echo hxltmcli "$HXLTM_EXEMPLUM_LINGUAM_LOCAL" "$HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_XLIFF_LOCAL" --objectivum-XLIFF
hxltmcli "$HXLTM_EXEMPLUM_LINGUAM_LOCAL" "$HXLTM_EXEMPLUM_LINGUAM_RESULTATUM_XLIFF_LOCAL" --objectivum-XLIFF

# To revert only one file that keeps changing even with same input
# git checkout -- tests/hxltm/resultatum/hxltm-exemplum-linguam.tmx

exit 0
