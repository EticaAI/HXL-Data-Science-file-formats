#!/bin/sh
#===============================================================================
#
#          FILE:  disciplinam-manuale-anglicum.sh
#
#         USAGE:  cd ./testum/hxltm/
#                 ./disciplinam-manuale-anglicum.sh
#
#   DESCRIPTION:  HXLTM disciplīnam manuāle in anglicum linguam
#
#                 Trivia:
#                 - HXLTM, https://hdp.etica.ai/hxltm
#                 - disciplīnam, https://en.wiktionary.org/wiki/disciplina#Latin
#                 - manuāle, https://en.wiktionary.org/wiki/disciplina#Latin
#                 - anglicum, https://en.wiktionary.org/wiki/anglicus#Latin
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#   TRANSLATORS:  ---
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedications
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2021-07-11 03:08 UTC
#      REVISION:  ---
#===============================================================================
# _[eng-Latn]Comment next line if not want to stop on first error[eng-Latn]_
set -e

hxltmcli --help > hxltmcli--help_eng-Latn.txt
