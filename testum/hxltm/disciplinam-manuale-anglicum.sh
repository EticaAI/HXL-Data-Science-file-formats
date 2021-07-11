#!/bin/sh
# shellcheck disable=SC2002
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

# _[eng-Latn] Output hxltmcli --help to a file (used on online documentation
# [eng-Latn]_
hxltmcli --help > hxltmcli--help_eng-Latn.txt

# tag::HXLTM_CSV[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# These examples may help you undestand the basics of how command  line works.
# Most data can be downloaded from:
# - https://github.com/EticaAI/HXL-Data-Science-file-formats/tree/main/testum/hxltm
#
# All examples on this page will reuse either this folder or online spredsheets
# used by HXL-CPLP on the HXL-CPLP/Auxilium-Humanitarium-API project.
# [eng-Latn]_

#    wget https://github.com/EticaAI/HXL-Data-Science-file-formats/archive/refs/heads/main.zip
#    unzip main.zip
#    cd HXL-Data-Science-file-formats-main/testum/hxltm

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_
hxltmcli hxltm-exemplum-linguam.tm.hxl.csv

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli

### III ------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print save data from input on the
# output.
# [eng-Latn]_
hxltmcli hxltm-exemplum-linguam.tm.hxl.csv output-file.tm.hxl.csv

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli > output-file.tm.hxl.csv

### IV ------------------------------------------------------------------------
# _[eng-Latn]
# Since the HXLTM CSV/XLSX reference format act as a container of
# several languages (e.g a 'main' file), most commands tend to be
# related to export to other formats. They are documented on other
# sections.
#
# Is also possible to manipulate (like filter, or renerate other
# HXLated datasets from an HXLTM main file using HXL cli tools
# or the HXL-Proxy. These advanced cases will be not covered here.
# But see:
#   - https://hxlstandard.org/
#   - https://proxy.hxlstandard.org/
#   - https://github.com/HXLStandard/libhxl-python/wiki
# [eng-Latn]_


# end::HXLTM_CSV[]

#### CSV-HXL-XLIFF _____________________________________________________________
# tag::CSV-HXL-XLIFF[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# TODO: CSV-HXL-XLIFF; This section is a draft
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-CSV-HXL-XLIFF

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-CSV-HXL-XLIFF

### III ------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: they save the input data on a file on
# disk.
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.xliff.hxl.csv \
  --objectivum-CSV-HXL-XLIFF

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-CSV-HXL-XLIFF > resultatum/hxltm-exemplum-linguam.xliff.hxl.csv

### III ------------------------------------------------------------------------
# _[eng-Latn]
# TODO: explain how to select the source and target language
# [eng-Latn]_

### IV ------------------------------------------------------------------------
# _[eng-Latn]
# TODO: explain how to select alternative languages
# [eng-Latn]_

# end::CSV-HXL-XLIFF[]

#### CSV-3 _____________________________________________________________________
# tag::CSV-3[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# TODO: CSV-3; This section is a draft
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-CSV-3

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-CSV-3

### III ------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: they save the input data on a file on
# disk.
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.xliff.hxl.csv \
  --objectivum-CSV-3

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-CSV-3 > resultatum/hxltm-exemplum-linguam.xliff.hxl.csv

### III ------------------------------------------------------------------------
# _[eng-Latn]
# TODO: explain how to select the source and target language
# [eng-Latn]_

# end::CSV-3[]

#### TMX _______________________________________________________________________
# tag::TMX[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# TODO: TMX; This section is a draft
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-TMX

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-TMX

### III ------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: they save the input data on a file on
# disk.
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.tmx \
  --objectivum-TMX

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-TMX > resultatum/hxltm-exemplum-linguam.tmx

### III ------------------------------------------------------------------------
# _[eng-Latn]
# TODO: docupent eventual new options to the --objectivum-TMX here.
# [eng-Latn]_

# end::TMX[]


#### XLIFF _____________________________________________________________________
# tag::XLIFF[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# TODO: XLIFF; This section is a draft
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-XLIFF

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-XLIFF

### III ------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: they save the input data on a file on
# disk.
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.xlf \
  --objectivum-XLIFF

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-XLIFF > resultatum/hxltm-exemplum-linguam.xlf

### VI ------------------------------------------------------------------------
# _[eng-Latn]
# Silence errors with --silentium.
#
# Sometimes may be necessary ignore errors (like missing source term to
# translate) and generate output format, even if invalid. The use of --silentium
# can help ignore some warnings.
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.xlf \
  --objectivum-XLIFF \
  --silentium

### III ------------------------------------------------------------------------
# _[eng-Latn]
# TODO: docupent eventual new options to the --objectivum-XLIFF here.
# [eng-Latn]_

# end::XLIFF[]

# hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-XLIFF -AL por-Latn -AL spa-Latn --expertum-metadatum
# To revert only one file that keeps changing even with same input
# git checkout -- testum/hxltm/resultatum/hxltm-exemplum-linguam.tmx

exit 0
