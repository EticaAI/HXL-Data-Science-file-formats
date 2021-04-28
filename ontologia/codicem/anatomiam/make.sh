#!/bin/sh
# shellcheck disable=SC2002
#===============================================================================
#
#          FILE:  ontologia/codicem/anatomiam/make.sh
#
#         USAGE:  ./ontologia/codicem/anatomiam/make.sh
#
#   DESCRIPTION:  Download files from ontologia/codicem/anatomiam/
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
#       CREATED:  2021-04-27 20:52 UTC v1.0 created
#      REVISION:  ---
#===============================================================================

# @see https://github.com/HXL-CPLP/forum/issues/44
# @see https://docs.google.com/spreadsheets/d/10axnLpDNtAc8Bh921dz5XPXCwo0FUXRcKS6-ermiu5w/edit#gid=1622293684
# @see https://proxy.hxlstandard.org/data/b02a5f

ONTOLOGIA_CODICEM_ANATOMIAM_TERMINOLOGIA_ANATOMICA="https://proxy.hxlstandard.org/data/b02a5f/download/HXL_CPLP-FOD_medicinae-legalis_humana-corpus.csv"
ROOTDIR="$(pwd)"


# Download terminologia-anatomica.hxl.csv (ignored by .gitignore)
wget -qO- "$ONTOLOGIA_CODICEM_ANATOMIAM_TERMINOLOGIA_ANATOMICA" > "${ROOTDIR}/ontologia/codicem/anatomiam/terminologia-anatomica.hxl.csv"

# Get a sample on terminologia-anatomica-EXEMPLUM.hxl.csv
cat "${ROOTDIR}/ontologia/codicem/anatomiam/terminologia-anatomica.hxl.csv" | head -n11 > "${ROOTDIR}/ontologia/codicem/anatomiam/terminologia-anatomica-EXEMPLUM.hxl.csv"