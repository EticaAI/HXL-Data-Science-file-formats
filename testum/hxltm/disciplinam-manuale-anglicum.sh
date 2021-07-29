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
hxltmcli --help > "hxltmcli--help_eng-Latn.txt"

# _[eng-Latn] Output hxltmdexml --help to a file (used on online documentation
# [eng-Latn]_
hxltmdexml --help > "hxltmdexml--help_eng-Latn.txt"

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

# NOTE: --CSV-HXL-XLIFF was removed on version v0.8.4. We may stick with
#       HXLTM CSV (for more complex metadata) and then CSV-3 or simpler or
#       customized versions (aka user use 'templated (shopfify) liquid' to
#       create own custom CSV versions)
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

# hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-CSV-HXL-XLIFF

# cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-CSV-HXL-XLIFF

### III ------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: they save the input data on a file on
# disk.
# [eng-Latn]_

# hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
#   resultatum/hxltm-exemplum-linguam.xliff.hxl.csv \
#   --objectivum-CSV-HXL-XLIFF

# cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-CSV-HXL-XLIFF > resultatum/hxltm-exemplum-linguam.xliff.hxl.csv

### III ------------------------------------------------------------------------
# _[eng-Latn]
# TODO: explain how to select the source and target language
# [eng-Latn]_

### IV ------------------------------------------------------------------------
# _[eng-Latn]
# TODO: explain how to select alternative languages
# [eng-Latn]_

# end::CSV-HXL-XLIFF[]


#### HXLTM-ASA __________________________________________________________________
# tag::HXLTM-ASA[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# The HXLTM-ASA is an not strictly documented Abstract Syntax Tree
# of an data conversion operation.
#
# These are quick examples. They reuse other examples on this guide, but also
# save data on a separate file.
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next example will generate an XLIFF, but we also will save the HXLTM-ASA.
#
# The '--expertum-HXLTM-ASA hxltm-asa/hxltm-exemplum-linguam.asa.hxltm.json'
# will generate an JSON output of the operation.
#
# The '--expertum-HXLTM-ASA hxltm-asa/hxltm-exemplum-linguam.asa.hxltm.yml'
# will generate an YAML output of the operation.
# [eng-Latn]_

# TODO: replace HXLTM ASA example from XLIFF to TBX or TMX

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.xlf \
  --expertum-HXLTM-ASA hxltm-asa/hxltm-exemplum-linguam.asa.hxltm.json \
  --objectivum-XLIFF

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.xlf \
  --expertum-HXLTM-ASA hxltm-asa/hxltm-exemplum-linguam.asa.hxltm.yml \
  --objectivum-XLIFF

# end::HXLTM-ASA[]

#### CSV-3 _____________________________________________________________________
# tag::CSV-3[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Documentation at cor.hxltm.yml:normam.CSV-3
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-CSV-3

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-CSV-3

### II -------------------------------------------------------------------------
# _[eng-Latn]
# Instead of use the default source (Latin) and objective (Arab, the classic
# one) on both examples is defined the source (first column) and objective
# second column):
# - XLIFF source language:
#     - Portuguese
# - XLIFF objective (target) language:
#     - Spanish
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  --fontem-linguam por-Latn@pt \
  --objectivum-linguam spa-Latn@es \
  --objectivum-CSV-3

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-CSV-3 --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es

### III ------------------------------------------------------------------------
# _[eng-Latn]
# Instead of use the default source (Latin) and objective (Arab, the classic
# one) on both examples is defined the source (first column) and objective
# second column):
# - XLIFF source language:
#     - Portuguese
# - XLIFF objective (target) language:
#     - Spanish
#
# but now, instead of print to stdout, save on the file
# resultatum/hxltm-exemplum-linguam.por-Latn_spa-Latn.csv
# [eng-Latn]_

# hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
#   resultatum/hxltm-exemplum-linguam.por-Latn_spa-Latn.csv \
#   --objectivum-CSV-3

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.por-Latn_spa-Latn.csv \
  --fontem-linguam por-Latn@pt \
  --objectivum-linguam spa-Latn@es \
  --objectivum-CSV-3

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-CSV-3 --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es > resultatum/hxltm-exemplum-linguam.por-Latn_spa-Latn.csv

### III ------------------------------------------------------------------------
# _[eng-Latn]
# TODO: explain how to select the source and target language
# [eng-Latn]_

# end::CSV-3[]

#### TSV-3 _____________________________________________________________________
# tag::TSV-3[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Documentation at cor.hxltm.yml:normam.TSV-3
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-TSV-3

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-TSV-3

### II -------------------------------------------------------------------------
# _[eng-Latn]
# Instead of use the default source (Latin) and objective (Arab, the classic
# one) on both examples is defined the source (first column) and objective
# second column):
# - XLIFF source language:
#     - Portuguese
# - XLIFF objective (target) language:
#     - Spanish
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  --fontem-linguam por-Latn@pt \
  --objectivum-linguam spa-Latn@es \
  --objectivum-TSV-3

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-TSV-3 --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es

### III ------------------------------------------------------------------------
# _[eng-Latn]
# Instead of use the default source (Latin) and objective (Arab, the classic
# one) on both examples is defined the source (first column) and objective
# second column):
# - XLIFF source language:
#     - Portuguese
# - XLIFF objective (target) language:
#     - Spanish
#
# but now, instead of print to stdout, save on the file
# resultatum/hxltm-exemplum-linguam.por-Latn_spa-Latn.csv
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.por-Latn_spa-Latn.tsv \
  --fontem-linguam por-Latn@pt \
  --objectivum-linguam spa-Latn@es \
  --objectivum-TSV-3

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-TSV-3 --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es > resultatum/hxltm-exemplum-linguam.por-Latn_spa-Latn.tsv
# end::TSV-3[]

#### TBX-Basim _________________________________________________________________
# tag::TBX-Basim[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Explanation about the format at cor.hxltm.yml:normam.TBX-Basim
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-TBX-Basim

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-TBX-Basim

### III ------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: they save the input data on a file on
# disk.
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.tbx \
  --objectivum-TBX-Basim

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-TBX-Basim > resultatum/hxltm-exemplum-linguam.tbx

### III ------------------------------------------------------------------------
# _[eng-Latn]
# TODO: docupent eventual new options to the --objectivum-TMX here.
# [eng-Latn]_

# end::TBX-Basim[]

#### TMX _______________________________________________________________________
# tag::TMX[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Explanation about the format at cor.hxltm.yml:normam.TMX
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
# @TODO: docupent eventual new options to the --objectivum-TMX here, like the
#        --agendum-linguam
# [eng-Latn]_

# end::TMX[]


#### UTX _______________________________________________________________________
# tag::UTX[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Explanation about the format at cor.hxltm.yml:normam.UTX
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-UTX

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-UTX

### III ------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: they save the input data on a file on
# disk.
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.utx \
  --objectivum-UTX

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-UTX > resultatum/hxltm-exemplum-linguam.utx

### III ------------------------------------------------------------------------
# _[eng-Latn]
# @TODO: docupent eventual new options to the --objectivum-TMX here, like the
#        --agendum-linguam
# [eng-Latn]_

# end::UTX[]

#### XML _______________________________________________________________________
# tag::XML[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Explanation about the format at cor.hxltm.yml:normam.XML
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-XML

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-XML

### III ------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: they save the input data on a file on
# disk.
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.hxltm.xml \
  --objectivum-XML

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-XML > resultatum/hxltm-exemplum-linguam.hxltm.xml

# end::XML[]

#### XLIFF _____________________________________________________________________
# tag::XLIFF[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Documentation at cor.hxltm.yml:normam.XLIFF
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
# - XLIFF source language:
#     - Portuguese
# - XLIFF objective (target) language:
#     - Spanish
# - Auxiliar languages (accept multiple options):
#     - Esperanto
#     - English
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.xlf \
  --fontem-linguam por-Latn@pt \
  --objectivum-linguam spa-Latn@es \
  --auxilium-linguam epo-Latn@eo,eng-Latn@en \
  --objectivum-XLIFF

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-XLIFF --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es --auxilium-linguam epo-Latn@eo,eng-Latn@en > resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.xlf

### VI ------------------------------------------------------------------------
# _[eng-Latn]
# Silence errors with --silentium.
#
# Sometimes may be necessary ignore errors (like missing source term to
# translate) and generate output format, even if invalid. The use of --silentium
# can help ignore some warnings.
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.xlf \
  --fontem-linguam por-Latn@pt \
  --objectivum-linguam spa-Latn@es \
  --auxilium-linguam epo-Latn@eo,eng-Latn@en \
  --objectivum-XLIFF \
  --silentium

# end::XLIFF[]

#### XLIFF-obsoletum ___________________________________________________________
# tag::XLIFF-obsoletum[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Documentation at cor.hxltm.yml:normam.XLIFF
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
# - XLIFF source language:
#     - Portuguese
# - XLIFF objective (target) language:
#     - Spanish
# - Auxiliar languages (accept multiple options):
#     - Esperanto
#     - English
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.obsoletum.xlf \
  --fontem-linguam por-Latn@pt \
  --objectivum-linguam spa-Latn@es \
  --auxilium-linguam epo-Latn@eo,eng-Latn@en \
  --objectivum-XLIFF-obsoletum

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-XLIFF-obsoletum --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es --auxilium-linguam epo-Latn@eo,eng-Latn@en > resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.obsoletum.xlf

### VI ------------------------------------------------------------------------
# _[eng-Latn]
# Silence errors with --silentium.
#
# Sometimes may be necessary ignore errors (like missing source term to
# translate) and generate output format, even if invalid. The use of --silentium
# can help ignore some warnings.
# [eng-Latn]_

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv \
  resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.obsoletum.xlf \
  --fontem-linguam por-Latn@pt \
  --objectivum-linguam spa-Latn@es \
  --auxilium-linguam epo-Latn@eo,eng-Latn@en \
  --objectivum-XLIFF-obsoletum \
  --silentium

# end::XLIFF-obsoletum[]

#### hxltmdexml XML ____________________________________________________________
# tag::hxltmdexml-XML[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Explanation about the format at cor.hxltm.yml:normam.XML
#
#     cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --objectivum-XML > resultatum/hxltm-exemplum-linguam.hxltm.xml
# [eng-Latn]_
# To generate:
### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

# hxltmdexml resultatum/hxltm-exemplum-linguam.hxltm.xml
hxltmdexml resultatum/hxltm-exemplum-linguam.hxltm.xml --agendum-linguam lat-Latn@la,por-Latn@pt,spa-Latn@es,eng-Latn@en

# end::hxltmdexml-XML[]

#### hxltmdexml TBX ____________________________________________________________
# tag::hxltmdexml-TBX[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Explanation about the format at cor.hxltm.yml:normam.TBX
# [eng-Latn]_

# To export all languages from TBX generated from IATE
# hxltmdexml IATE_export.tbx --agendum-linguam spa-Latn@es,eng-Latn@en,fra-Latn@fr,lat-Latn@la,por-Latn@pt,mul-Zyyy
# cat IATE_export.tbx | hxltmdexml --agendum-linguam por-Latn@pt,spa-Latn@es --agendum-linguam por-Latn@pt



### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# TBX-IATE:
# cat hxltmdexml IATE_export.tbx | (...)
#     hxltmdexml --agendum-linguam bul-Latn@bg --agendum-linguam ces-Latn@cs --agendum-linguam dan-Latn@da --agendum-linguam dut-Latn@nl --agendum-linguam ell-Latn@el --agendum-linguam eng-Latn@en --agendum-linguam est-Latn@et --agendum-linguam fin-Latn@fi --agendum-linguam fra-Latn@fr --agendum-linguam ger-Latn@de --agendum-linguam ger-Latn@de --agendum-linguam gle-Latn@ga --agendum-linguam hun-Latn@hu --agendum-linguam ita-Latn@it --agendum-linguam lav-Latn@lv --agendum-linguam lit-Latn@lt --agendum-linguam mlt-Latn@mt --agendum-linguam pol-Latn@pl --agendum-linguam por-Latn@pt --agendum-linguam ron-Latn@ro --agendum-linguam slk-Latn@sk --agendum-linguam slv-Latn@sl --agendum-linguam spa-Latn@es --agendum-linguam swe-Latn@sv
#
# [eng-Latn]_

hxltmdexml resultatum/hxltm-exemplum-linguam.tbx --agendum-linguam lat-Latn@la,por-Latn@pt,spa-Latn@es,eng-Latn@en

# ... | column -s, -t
# hxltmdexml resultatum/hxltm-exemplum-linguam.tbx --agendum-linguam lat-Latn@la,por-Latn@pt,spa-Latn@es,eng-Latn@en | column -s, -t

# https://github.com/saulpw/visidata
# pip3 install visidata
# ... | visidata -f csv
# hxltmdexml resultatum/hxltm-exemplum-linguam.tbx --agendum-linguam lat-Latn@la,por-Latn@pt,spa-Latn@es,eng-Latn@en | visidata -f csv

# hxltmdexml iate-exemplum.tbx --agendum-linguam lat-Latn@la,por-Latn@pt,spa-Latn@es,eng-Latn@en | visidata -f csv

# cat resultatum/hxltm-exemplum-linguam.tbx | hxltmdexml
# end::hxltmdexml-TBX[]

#### hxltmdexml TMX ____________________________________________________________
# tag::hxltmdexml-TMX[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Explanation about the format at cor.hxltm.yml:normam.TMX
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

# hxltmdexml resultatum/hxltm-exemplum-linguam.tmx
hxltmdexml resultatum/hxltm-exemplum-linguam.tmx --agendum-linguam lat-Latn@la,por-Latn@pt,spa-Latn@es,eng-Latn@en


# cat resultatum/hxltm-exemplum-linguam.tmx | hxltmdexml
# end::hxltmdexml-TMX[]

#### hxltmdexml XLIFF-obsoletum ________________________________________________
# tag::hxltmdexml-XLIFF-obsoletum[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Documentation at cor.hxltm.yml:normam.XLIFF-obsoletum
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

# hxltmdexml resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.obsoletum.xlf
hxltmdexml resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.obsoletum.xlf --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es

cat resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.obsoletum.xlf | hxltmdexml --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es

### III ------------------------------------------------------------------------
# _[eng-Latn]
# Similar to step II, but now we save the result to a file
# [eng-Latn]_

hxltmdexml resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.obsoletum.xlf \
    rursum/XLIFF-obsoletum/hxltm-exemplum-linguam.por-Latn--spa-Latn.tm.hxl.csv \
     --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es

cat resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.obsoletum.xlf | hxltmdexml > rursum/XLIFF-obsoletum/hxltm-exemplum-linguam.por-Latn--spa-Latn.tm.hxl.csv  --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es

# end::hxltmdexml-XLIFF-obsoletum[]

#### hxltmdexml XLIFF __________________________________________________________
# tag::hxltmdexml-XLIFF[]
### I -------------------------------------------------------------------------
# _[eng-Latn]
# Documentation at cor.hxltm.yml:normam.XLIFF
# [eng-Latn]_

### II -------------------------------------------------------------------------
# _[eng-Latn]
# The next 2 examples are equivalent: will print to stdout the result
# [eng-Latn]_

hxltmdexml resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.xlf --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es

cat resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.xlf | hxltmdexml --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es

### III ------------------------------------------------------------------------
# _[eng-Latn]
# Similar to step II, but now we save the result to a file
# [eng-Latn]_

hxltmdexml resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.xlf \
    rursum/XLIFF/hxltm-exemplum-linguam.por-Latn--spa-Latn.tm.hxl.csv \
    --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es

cat resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.xlf | hxltmdexml > rursum/XLIFF/hxltm-exemplum-linguam.por-Latn--spa-Latn.tm.hxl.csv --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es


# end::hxltmdexml-XLIFF-obsoletum[]

# tag::venandum_insectum_est[]
### Debug
# hxltmcli --expertum-metadatum --venandum-insectum-est
# end::venandum_insectum_est[]


# hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-XLIFF -AL por-Latn -AL spa-Latn --expertum-metadatum
### Profile, text
# @see see https://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script
#     cd ./testum/hxltm/
#     python3 -m cProfile -s time /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin/hxltmcli.py hxltm-exemplum-linguam.tm.hxl.csv --objectivum-XLIFF -AL por-Latn -AL spa-Latn --expertum-metadatum
#     python3 -m cProfile -s cumtime /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin/hxltmcli.py hxltm-exemplum-linguam.tm.hxl.csv --objectivum-XLIFF -AL por-Latn -AL spa-Latn --expertum-metadatum
#     python3 -m cProfile -s cumtime /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin/hxltmcli.py hxltm-exemplum-linguam.tm.hxl.csv --objectivum-XLIFF -AL por-Latn -AL spa-Latn --expertum-metadatum | grep hxltmcli.py

# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/testum/hxltm$ python3 -m cProfile -s cumtime /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin/hxltmcli.py hxltm-exemplum-linguam.tm.hxl.csv --objectivum-XLIFF -AL por-Latn -AL spa-Latn --expertum-metadatum | grep hxltmcli.py
#         1    0.000    0.000    0.787    0.787 hxltmcli.py:72(<module>)
#         1    0.000    0.000    0.233    0.233 hxltmcli.py:582(execute_cli)
#         1    0.000    0.000    0.226    0.226 hxltmcli.py:2489(load_hxltm_options)
#         1    0.000    0.000    0.226    0.226 hxltmcli.py:2531(_load_hxltm_options_file)
#         1    0.000    0.000    0.004    0.004 hxltmcli.py:289(make_args_hxltmcli)
#         1    0.000    0.000    0.002    0.002 hxltmcli.py:2701(make_source)
#         1    0.000    0.000    0.002    0.002 hxltmcli.py:2708(make_input)
#         1    0.000    0.000    0.002    0.002 hxltmcli.py:2613(make_args)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:719(in_expertum_metadatum)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1406(__init__)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1423(_initialle)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:230(_initiale_meta_archivum_fontem_hxlated)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1381(HXLTMDatum)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1497(HXLTMDatumMetaCaput)
#         7    0.000    0.000    0.000    0.000 hxltmcli.py:1646(quod_est_hashtag_caput)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:2770(__exit__)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:2733(make_output)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:2764(__init__)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1747(HXLTMOntologia)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1548(__init__)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1561(_initialle)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:191(_initiale)
#         4    0.000    0.000    0.000    0.000 hxltmcli.py:2003(__init__)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:2604(__init__)
#         4    0.000    0.000    0.000    0.000 hxltmcli.py:2021(initialle)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1937(HXLTMLinguam)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:2740(make_headers)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:134(HXLTMCLI)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:2304(HXLTMUtil)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:142(__init__)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:2593(HXLUtils)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1477(v)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1861(HXLTMBCP47)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1754(__init__)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:2755(FileOutput)
#         4    0.000    0.000    0.000    0.000 hxltmcli.py:2248(v)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:2261(HXLTMRemCaput)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:2774(StreamOutput)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1721(v)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:1763(initialle)
#         1    0.000    0.000    0.000    0.000 hxltmcli.py:2767(__enter__)


### Profile, visual
# @see see https://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script
#     cd ./testum/hxltm/
#     pip3 install graphviz
#     sudo apt-get install graphviz
#     pycallgraph -f graphviz -o pycallgraph-test.svg -- /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin/hxltmcli.py hxltm-exemplum-linguam.tm.hxl.csv --objectivum-XLIFF -AL por-Latn -AL spa-Latn --expertum-metadatum
#     pycallgraph graphviz -- /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin/hxltmcli.py hxltm-exemplum-linguam.tm.hxl.csv --objectivum-XLIFF -AL por-Latn -AL spa-Latn --expertum-metadatum
#     pycallgraph --max-depth 3 graphviz -- /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin/hxltmcli.py hxltm-exemplum-linguam.tm.hxl.csv --objectivum-XLIFF -AL por-Latn -AL spa-Latn --expertum-metadatum

# hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --objectivum-XLIFF -AL por-Latn -AL spa-Latn --expertum-metadatum

## TMX
# hxltmcli hxltm-exemplum-linguam.tm.hxl.csv resultatum/hxltm-exemplum-linguam.tmx --objectivum-TMX --experimentum-est --expertum-HXLTM-ASA hxltm-asa/hxltm-exemplum-linguam.asa.hxltm.yml --expertum-HXLTM-ASA-verbosum

## TBX-Basim
# hxltmcli hxltm-exemplum-linguam.tm.hxl.csv resultatum/hxltm-exemplum-linguam.tbx --objectivum-TBX-Basim --expertum-HXLTM-ASA hxltm-asa/hxltm-exemplum-linguam.asa.hxltm.yml

## XLIFF2
# hxltmcli hxltm-exemplum-linguam.tm.hxl.csv resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.xlf --objectivum-XLIFF --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es --auxilium-linguam eng-Latn@en,lat-Latn@la --experimentum-est --expertum-HXLTM-ASA hxltm-asa/hxltm-exemplum-linguam.por-Latn--spa-Latn.xlf.asa.hxltm.yml --expertum-HXLTM-ASA-verbosum

## XLIFF1
# hxltmcli hxltm-exemplum-linguam.tm.hxl.csv resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.xlf --objectivum-XLIFF-obsoletum --fontem-linguam por-Latn@pt --objectivum-linguam spa-Latn@es --auxilium-linguam eng-Latn@en,lat-Latn@la --experimentum-est --expertum-HXLTM-ASA hxltm-asa/hxltm-exemplum-linguam.por-Latn--spa-Latn.xlf.asa.hxltm.yml --expertum-HXLTM-ASA-verbosum

# To revert only one file that keeps changing even with same input
# git checkout -- testum/hxltm/resultatum/hxltm-exemplum-linguam.tmx

### Real test usage, start -----------------------------------------------------

# Download lastest schemam-un-htcds.tm.hxl from Google docs
# hxltmcli https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1292720422 schemam-un-htcds.tm.hxl.csv

# hxltmcli schemam-un-htcds.tm.hxl.csv \
#   resultatum/schemam-un-htcds_eng-Latn--por-Latn.xlf \
#   --fontem-linguam eng-Latn@en \
#   --objectivum-linguam por-Latn@pt \
#   --objectivum-XLIFF

# hxltmcli schemam-un-htcds.tm.hxl.csv \
#   resultatum/schemam-un-htcds_eng-Latn--slv-Latn.xlf \
#   --fontem-linguam eng-Latn@en \
#   --objectivum-linguam slv-Latn@sl \
#   --objectivum-XLIFF

# hxltmcli schemam-un-htcds.tm.hxl.csv \
#   resultatum/schemam-un-htcds_eng-Latn--por-Latn.obsoletum.xlf \
#   --fontem-linguam eng-Latn@en \
#   --objectivum-linguam por-Latn@pt \
#   --objectivum-XLIFF-obsoletum

# hxltmcli schemam-un-htcds.tm.hxl.csv \
#   resultatum/schemam-un-htcds_eng-Latn--slk-Latn.obsoletum.xlf \
#   --fontem-linguam eng-Latn@en \
#   --objectivum-linguam slk-Latn@sk \
#   --objectivum-XLIFF-obsoletum

# hxltmdexml resultatum/schemam-un-htcds_eng-Latn--por-Latn.DONE.obsoletum.xlf

# hxltmdexml resultatum/schemam-un-htcds_eng-Latn--por-Latn.DONE.obsoletum.xlf

# cat resultatum/schemam-un-htcds_eng-Latn--por-Latn.DONE.obsoletum.xlf | hxltmdexml 



### Real test usage, end -------------------------------------------------------

exit 0
