#!/bin/bash
# shellcheck disable=SC2002
#===============================================================================
#
#          FILE:  ontologia/codicem/locum/un-locode/make.sh
#
#         USAGE:  ./ontologia/codicem/locum/un-locode/make.sh
#
#   DESCRIPTION:  Download files from ontologia/codicem/locum/un-locode/
#                 Script based on work from @sabas, from
#  https://github.com/datasets/un-locode/blob/master/scripts/prepare_edition.sh
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - sh
#                 - wget
#                 - unzip
#                 - mdbtools (https://github.com/mdbtools/mdbtools)
#                 - csvkit (https://github.com/wireservice/csvkit)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#                 (Based @sabas Stefano work, github.com/datasets/un-locode)
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2021-04-28 23:18 UTC v1.0 started
#      REVISION:  ---
#===============================================================================

ROOTDIR="$(pwd)"

UNLOCODE_RELEASE="2020-2" # yyyy-r, "2020-2" on "2020-2 UNLOCODE CodeList.mdb"
UNLOCODE_DATE="2020-12"  # https://unece.org/sites/default/files/2020-12/loc202mdb.zip
UNLOCODE_UID="loc202"    # "loc202" on loc202mdb.zip

FONTEM_UNLOCODE_MDB_URL="https://unece.org/sites/default/files/${UNLOCODE_DATE}/${UNLOCODE_UID}mdb.zip"
# FONTEM_UNLOCODE_MDB_URL="https://unece.org/sites/default/files/2020-12/loc202mdb.zip"


# @see https://data.humdata.org/dataset/hxl-core-schemas
# ONTOLOGIA_CODICEM_LOCUM_UN_LOCODE="https://proxy.hxlstandard.org/data.csv?dest=data_edit&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI%2Fpub%3Fgid%3D319251406%26single%3Dtrue%26output%3Dcsv"
# ONTOLOGIA_CODICEM_HXL_STANDARD_CORE_ATTRIBUTE="https://proxy.hxlstandard.org/data.csv?dest=data_view&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI%2Fpub%3Fgid%3D1810309357%26single%3Dtrue%26output%3Dcsv&strip-headers=on"

# # @see https://data.humdata.org/dataset/hxl-master-vocabulary-list
# ONTOLOGIA_CODICEM_HXL_STANDARD_MASTER_VOCABULARY="https://proxy.hxlstandard.org/data.csv?dest=data_edit&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1dGPthewm3Dm5_IWBU4buJ370qJBnrVYPL3XbxZ0O-BY%2Fedit%3Fts%3D5a201f69%23gid%3D0"
# # @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/2
# # @see https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=245471857

# ONTOLOGIA_CODICEM_HXL_CPLP_HXL2TAB="https://proxy.hxlstandard.org/data.csv?dest=data_edit&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY%2Fedit%23gid%3D245471857"


# # Download terminologia-anatomica.hxl.csv (ignored by .gitignore)
# wget -qO- "$ONTOLOGIA_CODICEM_HXL_STANDARD_CORE_HASHTAG" > "${ROOTDIR}/ontologia/codicem/hxl/standard/core/hashtag.hxl.csv"
# wget -qO- "$ONTOLOGIA_CODICEM_HXL_STANDARD_CORE_ATTRIBUTE" > "${ROOTDIR}/ontologia/codicem/hxl/standard/core/attribute.hxl.csv"
# wget -qO- "$ONTOLOGIA_CODICEM_HXL_STANDARD_MASTER_VOCABULARY" > "${ROOTDIR}/ontologia/codicem/hxl/standard/master-vocabulary.hxl.csv"
# wget -qO- "$ONTOLOGIA_CODICEM_HXL_CPLP_HXL2TAB" > "${ROOTDIR}/ontologia/codicem/hxl/cplp/hxl2tab.hxl.csv"


#### Ignore after here ________________________________________________________
# https://github.com/mdbtools/mdbtools
# sudo apt install mdbtools

cd "${ROOTDIR}/ontologia/codicem/locum/un-locode/temp/" || exit

if [ ! -f "${UNLOCODE_UID}mdb.zip" ]; then
    wget -qO- "$FONTEM_UNLOCODE_MDB_URL" > "${UNLOCODE_UID}mdb.zip"
    unzip "${UNLOCODE_UID}mdb.zip"
fi

MDBFILE="${UNLOCODE_RELEASE} UNLOCODE CodeList.mdb" # "2020-2 UNLOCODE CodeList.mdb"

IN=$(mdb-tables -d ";" "$MDBFILE")
IFS=';' read -ra TABLES <<< "$IN"
for i in "${TABLES[@]}"; do
    mdb-export "$MDBFILE" "$i" > "mdb_$i.csv"
    csvclean "mdb_$i.csv"
done

gawk -v RS='"[^"]*"' -v ORS= '{gsub(/\n/, " ", RT); print $0  RT}' mdb_SubdivisionCodes_out.csv > subdivision-codes.tmp.csv
sed -i 's/ \{2,\}/ /g;s/[[:blank:]]*$//' subdivision-codes.tmp.csv
sed -i 's/\t/ /g' subdivision-codes.tmp.csv

# mdb_2020-2 UNLOCODE CodeList_out.csv

# gawk -v RS='"' 'NR % 2 == 0 { gsub(/\n/, "") } { printf("%s%s", $0, RT) }'  "mdb_${filename}_out.csv" > code-list.tmp.csv #remove newlines in data
gawk -v RS='"' 'NR % 2 == 0 { gsub(/\n/, "") } { printf("%s%s", $0, RT) }'  "mdb_${UNLOCODE_RELEASE} UNLOCODE CodeList_out.csv" > code-list.tmp.csv #remove newlines in data
csvgrep -c 3 -r "^$" -i code-list.tmp.csv > code-list.tmp2.csv #remove country headers

(head -n 1 code-list.tmp2.csv && tail -n +2 code-list.tmp2.csv | LC_ALL=C sort -t, -k2,2  -k4,4 --ignore-case) > code-list.csv # sort data by locode

# ls -lha ontologia/codicem/locum/un-locode/temp/
# total 50M
# drwxrwxr-x 2 fititnt fititnt 4,0K abr 28 21:40  .
# drwxrwxr-x 3 fititnt fititnt 4,0K abr 28 20:59  ..
# -rw-rw-r-- 1 fititnt fititnt  12M dez 10 15:34 '2020-2 UNLOCODE CodeList.mdb'
# -rw-rw-r-- 1 fititnt fititnt 219K dez 15 11:34 '2020-2 UNLOCODE SecretariatNotes.pdf'
# -rw-rw-r-- 1 fititnt fititnt 6,7M abr 28 21:40  code-list.csv
# -rw-rw-r-- 1 fititnt fititnt 6,7M abr 28 21:40  code-list.tmp2.csv
# -rw-rw-r-- 1 fititnt fititnt 6,7M abr 28 21:40  code-list.tmp.csv
# -rw-rw-r-- 1 fititnt fititnt 2,7M abr 28 21:06  loc202mdb.zip
# -rw-rw-r-- 1 fititnt fititnt 8,5M abr 28 21:40 'mdb_2020-2 UNLOCODE CodeList.csv'
# -rw-rw-r-- 1 fititnt fititnt 6,7M abr 28 21:40 'mdb_2020-2 UNLOCODE CodeList_out.csv'
# -rw-rw-r-- 1 fititnt fititnt 4,9K abr 28 21:40  mdb_CountryCodes.csv
# -rw-rw-r-- 1 fititnt fititnt 3,9K abr 28 21:40  mdb_CountryCodes_out.csv
# -rw-rw-r-- 1 fititnt fititnt  323 abr 28 21:40  mdb_FunctionClassifiers.csv
# -rw-rw-r-- 1 fititnt fititnt  289 abr 28 21:40  mdb_FunctionClassifiers_out.csv
# -rw-rw-r-- 1 fititnt fititnt  864 abr 28 21:40  mdb_StatusIndicators.csv
# -rw-rw-r-- 1 fititnt fititnt  812 abr 28 21:40  mdb_StatusIndicators_out.csv
# -rw-rw-r-- 1 fititnt fititnt 112K abr 28 21:40  mdb_SubdivisionCodes.csv
# -rw-rw-r-- 1 fititnt fititnt  85K abr 28 21:40  mdb_SubdivisionCodes_out.csv
# -rw-rw-r-- 1 fititnt fititnt  84K abr 28 21:40  subdivision-codes.tmp.csv

mv code-list.csv ../stagging/code-list.csv
mv mdb_CountryCodes_out.csv ../stagging/country-codes.csv
mv mdb_FunctionClassifiers_out.csv ../stagging/function-classifiers.csv
mv mdb_StatusIndicators_out.csv ../stagging/status-indicators.csv
mv subdivision-codes.tmp.csv ../stagging/subdivision-codes.csv
# rm ./*.csv

# Prepare

cat ../stagging/code-list.csv | head -n10 > ../stagging/code-list-EXEMPLUM.hxl.csv

# Move to public folder

cp ../stagging/code-list.csv ../code-list.hxl.csv
cp ../stagging/code-list-EXEMPLUM.hxl.csv ../code-list-EXEMPLUM.hxl.csv
cp ../stagging/country-codes.csv ../country-codes.hxl.csv
cp ../stagging/function-classifiers.csv ../function-classifiers.hxl.csv
cp ../stagging/status-indicators.csv ../status-indicators.hxl.csv
cp ../stagging/subdivision-codes.csv ../subdivision-codes.hxl.csv