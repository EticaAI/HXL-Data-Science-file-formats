#!/usr/sh
#===============================================================================
#
#          FILE:  command-line-tools-for-csv.sh
#
#         USAGE:  cat command-line-tools-for-csv.sh
#
#   DESCRIPTION:  EticaAI/HXL-Data-Science-file-formats/guides/command-line-tools-for-csv.sh
#                 is an quick overview of different command line tools that
#                 worth at least mention, in special if are dealing with raw
#                 formats already not HXLated.
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
#       CREATED:  2021-01-27 05:08 UTC
#      REVISION:  ---
#===============================================================================
echo "cat command-line-tools-for-csv.sh"
exit 1

#### 1. About __________________________________________________________________
# On EticaAI/HXL-Data-Science-file-formats/guides/command-line-tools-for-csv.sh
# we share both 1) command line tools that use the libhxl-python that export
# HXlated datasets for other formats and 2) document how different formats
# compare to each other. The role of this guide is a very quick overview of
# other command line tools that may be used
#
# When installing libhxl-python, your system will also have HXL Command line
# tools to use. This guide will at least mention then.
#
# This guide will also mention some other tools, like strategies to solve
# encoding issues or deal with huge CSV files before even be able to use HXL.


#### 2. HXL ____________________________________________________________________

### HXL Quick links ------------------------------------------------------------
# @see https://pypi.org/project/libhxl/
# @see https://github.com/HXLStandard/libhxl-python/wiki
# @see https://github.com/HXLStandard/libhxl-python/wiki/Command-line-tools
# @see https://github.com/HXLStandard/libhxl-python/wiki/HXL-cookbook

### 2.1 HXL Command line tools -------------------------------------------------
#   - hxladd
#   - hxlappend
#   - hxlclean
#   - hxlcount
#   - hxlcut
#   - hxldedup
#   - hxlexpand
#   - hxlexplode
#   - hxlfill
#   - hxlhash
#   - hxlimplode
#   - hxlmerge
#   - hxlrename
#   - hxlreplace
#   - hxlselect
#   - hxlsort
#   - hxlspec
#   - hxltag
#   - hxlvalidate

### 2.2 Installation -----------------------------------------------------------
## REQUISITES
#   - python3
#   - pip

# The HXL command line tools are installed with the libhxl-python package via
# pip. Ubuntu uses pip3, Other systems may use pip

pip3 install libhxl
# pip install libhxl

#### 3 csvkit, agate, xsv ______________________________________________________
### 3. context for csvkit, agate, xsv ------------------------------------------
# In the words of the csvkit documentation:
#    "If you need to do more complex data analysis than csvkit can handle, use
#     agate. If you need csvkit to be faster or to handle larger files, you may
#     be reaching the limits of csvkit. Consider loading the data into SQL, or
#     using xsv."
#
#
# In the words of BurntSushi/xsv documentation:
#    "Here are several valid criticisms of this (xsv) project:
#      - You shouldn't be working with CSV data because CSV is a terrible format
#      - If your data is gigabytes in size, then CSV is the wrong storage type.
#      - Various SQL databases provide all of the operations available in xsv
#        with more sophisticated indexing support. And the performance is a
#        zillion times better.
#    "I'm sure there are more criticisms, but the impetus for this project was a
#     40GB CSV file that was handed to me. I was tasked with figuring out the
#     shape of the data inside of it and coming up with a way to integrate it
#     into our existing system. It was then that I realized that every single
#     CSV tool I knew about was woefully inadequate. They were just too slow or
#     didn't provide enough flexibility. (Another project I had comprised of a
#     few dozen CSV files. They were smaller than 40GB, but they were each
#     supposed to represent the same kind of data. But they all had different
#     column and unintuitive column names. Useful CSV inspection tools were
#     critical here—and they had to be reasonably fast."
#    "The key ingredients for helping me with my task were indexing, random
#     sampling, searching, slicing and selecting columns. All of these things
#     made dealing with 40GB of CSV data a bit more manageable (or dozens of
#     CSV files).
#    "Getting handed a large CSV file once was enough to launch me on this
#     quest. From conversations I've had with others, CSV data files this
#     large don't seem to be a rare event. Therefore, I believe there is room
#     for a tool that has a hope of dealing with data that large."
#
# Also deep in the documentation of csvkit
#    "To change field values (i.e. to run sed or awk-like commands on CSV
#     files), consider miller (mlr put).
#       - https://github.com/johnkerl/miller
#    "To transpose CSVs, consider csvtool. Install csvtool on Linux using your
#     package manager(...)"
#       - http://colin.maudry.com/csvtool-manual-page/
#    "To draw plots, consider jp."
#       - https://github.com/sgreben/jp
#    "To diff CSVs, consider daff."
#       - https://github.com/paulfitz/daff
#    "To explore CSVs interactively, consider VisiData."
#       - https://www.visidata.org/
#     "Alternatives to csvsql are q and textql."
#       - https://github.com/harelba/q
#       - https://github.com/dinedal/textql

### 3.1 csvkit -----------------------------------------------------------------
# @see https://csvkit.readthedocs.io/
# @see https://github.com/wireservice/csvkit
#
### 3.1.1 csvkit Command line tools --------------------------------------------
#
#  - INPUT DATA
#    - in2csv
#    - sql2csv
#  - PROCESSING
#    - csvclean
#    - csvcut
#    - csvgrep
#    - csvjoin
#    - csvsort
#    - csvstack
#  - OUTPUT AND ANALYSIS
#    - csvformat
#    - csvjson
#    - csvlook
#    - csvpy
#    - csvsql
#    - csvstat

## 3.1.2 Installing csvkit .....................................................
# csvkit, like libhxl, is also installable with pip.
pip3 install csvkit
# pip install csvkit
