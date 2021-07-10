#!/usr/sh
#===============================================================================
#
#          FILE:  command-line-tools-for-encoding.sh
#
#         USAGE:  cat command-line-tools-for-encoding.sh
#
#   DESCRIPTION:  EticaAI/HXL-Data-Science-file-formats/guides/command-line-tools-for-encoding.sh
#                 is an quick overview of different command line tools that
#                 worth at least mention, in special if are dealing with raw
#                 formats already not HXLated AND do not have UTF-8 encoding.
#
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  1. python3
#                 2. pip
#
#          BUGS:  ---
#         NOTES:  This guide is tested on Ubuntu 20.04.
#                   - Most tools here are availible on Linux/Mac/Windows+WSL,
#                     but you may need to change package names when installing.
#                   - Consider read the source documentation for how to install
#                     on other systems.
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2021-02-02 17:01 UTC
#      REVISION:  ---
#===============================================================================
echo "cat command-line-tools-for-encoding.sh"
exit 1


#### Encoding __________________________________________________________________

### uchardet -------------------------------------------------------------------
# " uchardet is an encoding detector library, which takes a sequence of bytes in
# an unknown character encoding without any additional information, and attempts
# to determine the encoding of the text. Returned encoding names are
# iconv-compatible."
# @see https://www.freedesktop.org/wiki/Software/uchardet/
sudo apt install uchardet

# fititnt@bravo:/workspace/data/brasil_inep_microdados-enem-2019/DADOS$ uchardet MICRODADOS_ENEM_2019.csv
# ISO-8859-1
# fititnt@bravo:/workspace/data/brasil_inep_microdados-enem-2019/DADOS$ file MICRODADOS_ENEM_2019.csv
# MICRODADOS_ENEM_2019.csv: ISO-8859 text, with very long lines

### iconv (convert encoding) ---------------------------------------------------
# @see https://stackoverflow.com/questions/64860/best-way-to-convert-text-files-between-character-sets/64889#64889
# 'uchardet' can be used to detect more exact encodign than the 'file'. Using as
# example ISO-8859-1

iconv --from-code=ISO-8859-1 --to-code UTF-8 file.csv > file_utf8.csv
# iconv --from-code=ISO-8859-1 --to-code UTF-8 MICRODADOS_ENEM_2019.csv > MICRODADOS_ENEM_2019_utf8.csv
# csvformat --out-delimiter=, MICRODADOS_ENEM_2019_utf8.csv > MICRODADOS_ENEM_2019_utf8__csvformat.csv
