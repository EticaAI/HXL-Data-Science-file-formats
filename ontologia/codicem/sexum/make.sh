#!/bin/sh
# shellcheck disable=SC2002
#===============================================================================
#
#          FILE:  ontologia/codicem/sexum/make.sh
#
#         USAGE:  ./ontologia/codicem/sexum/make.sh
#
#   DESCRIPTION:  Download files to ontologia/codicem/sexum/
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - sh
#                 - wget
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2021-04-28 01:53 UTC v1.0 created
#      REVISION:  ---
#===============================================================================

ROOTDIR="$(pwd)"

# @see https://github.com/HXL-CPLP/forum/issues/50
# @see https://docs.google.com/spreadsheets/d/1AvYEV8a-X9gZrxrPH0wPgoGHO8ENxWJuVA3z1RpcC5k/edit#gid=764269111

# @see https://en.wikipedia.org/wiki/ISO/IEC_5218
# @see https://docs.google.com/spreadsheets/d/1AvYEV8a-X9gZrxrPH0wPgoGHO8ENxWJuVA3z1RpcC5k/edit#gid=214068544
ONTOLOGIA_CODICEM_SEXUM_BINARIUM="https://proxy.hxlstandard.org/data.csv?dest=data_edit&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1AvYEV8a-X9gZrxrPH0wPgoGHO8ENxWJuVA3z1RpcC5k%2Fedit%23gid%3D214068544"

# @see https://en.wikipedia.org/wiki/ISO/IEC_5218
# @see https://docs.google.com/spreadsheets/d/1AvYEV8a-X9gZrxrPH0wPgoGHO8ENxWJuVA3z1RpcC5k/edit#gid=214068544
ONTOLOGIA_CODICEM_SEXUM_NON_BINARIUM="https://proxy.hxlstandard.org/data.csv?dest=data_edit&filter01=expand&filter-label01=%2Blist+split&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1AvYEV8a-X9gZrxrPH0wPgoGHO8ENxWJuVA3z1RpcC5k%2Fedit%23gid%3D530571590"

# @see https://confluence.hl7.org/display/VOC/Gender+Coding+with+International+Data+Exchange+Standards
# @see https://docs.google.com/spreadsheets/d/1AvYEV8a-X9gZrxrPH0wPgoGHO8ENxWJuVA3z1RpcC5k/edit#gid=1946656528
# @see https://confluence.hl7.org/

# Download terminologia-anatomica.hxl.csv (ignored by .gitignore)
wget -qO- "$ONTOLOGIA_CODICEM_SEXUM_BINARIUM" > "${ROOTDIR}/ontologia/codicem/sexum/binarium.hxl.csv"
wget -qO- "$ONTOLOGIA_CODICEM_SEXUM_NON_BINARIUM" > "${ROOTDIR}/ontologia/codicem/sexum/non-binarium.hxl.csv"

# # Get a sample on terminologia-anatomica-EXEMPLUM.hxl.csv
# cat "${ROOTDIR}/ontologia/codicem/anatomiam/terminologia-anatomica.hxl.csv" | head -n11 > "${ROOTDIR}/ontologia/codicem/anatomiam/terminologia-anatomica-EXEMPLUM.hxl.csv"