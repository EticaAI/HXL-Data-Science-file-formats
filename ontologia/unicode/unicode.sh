#!/bin/sh
#===============================================================================
#
#          FILE:  unicode.sh
#
#         USAGE:  ./unicode.sh
#                 cd ontologia/unicode/
#                 sh ./unicode.sh
#
#   DESCRIPTION:  ---
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
#       CREATED:  2021-04-14 01:32 UTC
#      REVISION:  ---
#===============================================================================

# Download 13.0
# DIR="$(pwd)"
# CACHE="${DIR}/cache"

# echo "$CACHE"

echo "See UNICODE CHARACTER DATABASE report; http://www.unicode.org/reports/tr44/"

echo "Building local cache for unicode.org/Public/13.0.0/ ..."

if [ ! -f "./13.0.0/ReadMe.txt" ]; then
    curl -o ./13.0.0/ReadMe.txt https://www.unicode.org/Public/13.0.0/ReadMe.txt
fi

if [ ! -f "./13.0.0/charts/Readme.txt" ]; then
    curl -o ./13.0.0/charts/Readme.txt https://www.unicode.org/Public/13.0.0/charts/Readme.txt
fi

echo "13.0.0/charts/CodeCharts.pdf is over 110 MB (and font license);; it will be commited on Git history"

if [ ! -f "./13.0.0/charts/CodeCharts.pdf" ]; then
    curl -o ./13.0.0/charts/CodeCharts.pdf https://www.unicode.org/Public/13.0.0/charts/CodeCharts.pdf
else
    echo "./13.0.0/charts/CodeCharts.pdf already cached"
fi

echo "13.0.0/charts/RSIndex.pdf is over 40 MB (and font license); it will be commited on Git history."

if [ ! -f "./13.0.0/charts/RSIndex.pdf" ]; then
    curl -o ./13.0.0/charts/RSIndex.pdf https://www.unicode.org/Public/13.0.0/charts/RSIndex.pdf
else
    echo "./13.0.0/charts/RSIndex.pdf already cached"
fi

echo "Local copy of https://github.com/unicode-org/cldr ..."

if [ ! -d "./cldr/unicode-org-cldr/" ]; then
    git clone --depth 1 https://github.com/unicode-org/cldr.git ./cldr/unicode-org-cldr/
else
    echo "./cldr/unicode-org-cldr/ already cached"
fi
echo "Local copy of https://github.com/unicode-org/cldr ..."

if [ ! -d "./cldr/unicode-org-cldr-json/" ]; then
    git clone --depth 1 https://github.com/unicode-org/cldr-json.git ./cldr/unicode-org-cldr-json/
else
    echo "./cldr/unicode-org-cldr-json/ already cached"
fi
