# Data Science files exported from HXL (The Humanitarian Exchange Language)
**[Proof of concept] Common file formats used for Data Science
exported from HXL (The Humanitarian Exchange Language)**

[![Standard HXL](https://img.shields.io/badge/Standard-HXL-%23F26459)](https://hxlstandard.org/)
![License](https://img.shields.io/github/license/EticaAI/HXL-Data-Science-file-formats)
[![Google Drive](https://img.shields.io/badge/Google%20Drive-Folder-yellowgreen)](https://drive.google.com/drive/u/1/folders/1qyTPaDgm7Ca-62blkdQjUox47WWKRwD3)

---

<!-- TOC depthFrom:2 -->

- [HXL-Data-Science-file-formats](#hxl-data-science-file-formats)
    - [1. The main focus](#1-the-main-focus)
        - [1.1 Vocabulary/Taxonomies](#11-vocabularytaxonomies)
        - [1.2 `HXL2` Command line tools](#12-hxl2-command-line-tools)
            - [1.2.1 `hxl2example`: create your own exporter/importer](#121-hxl2example-create-your-own-exporterimporter)
            - [1.2.2 `hxl2tab`: tab format, focused for compatibility with Orange Data Mining](#122-hxl2tab-tab-format-focused-for-compatibility-with-orange-data-mining)
            - [1.2.3 `hxlquickimport`: (like the `hxltag`)](#123-hxlquickimport-like-the-hxltag)
    - [2. Reasons behind](#2-reasons-behind)
        - [2.1 Why?](#21-why)
        - [2.2 How?](#22-how)
        - [2.3 Non-goals](#23-non-goals)
- [HXLated datasets to test](#hxlated-datasets-to-test)
    - [Production data on The Humanitarian Data Exchange ("HDX")](#production-data-on-the-humanitarian-data-exchange-hdx)
    - [Files from EticaAI-Data_HXL-Data-Science-file-formats](#files-from-eticaai-data_hxl-data-science-file-formats)
- [Additional Guides](#additional-guides)
    - [Command line tools for CSV](#command-line-tools-for-csv)
    - [Alternatives to preview spreadsheets with over 1.000.000 rows](#alternatives-to-preview-spreadsheets-with-over-1000000-rows)

<!-- /TOC -->

---

## HXL-Data-Science-file-formats

> In addition to this GitHub repository, check also the
  [EticaAI-Data_HXL-Data-Science-file-formats Google Drive folder](https://drive.google.com/drive/u/1/folders/1qyTPaDgm7Ca-62blkdQjUox47WWKRwD3).

### 1. The main focus

#### 1.1 Vocabulary/Taxonomies
- <https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1297379331>

This project either use explicit HXL +attributes (easy to implement, but more
verbose) or do inferences on well know HXLated datasets used on humanitaria
areas. To make this work, the main reference is not software implementation, but
reference tables.

#### 1.2 `HXL2` Command line tools
- See folder [bin/](bin/)
- See discussions at
  - <https://github.com/EticaAI/HXL-Data-Science-file-formats/issues>
  - <https://github.com/HXL-CPLP/forum/issues/52>
- See (not so docummented tests): [tests/manual-tests.sh](tests/manual-tests.sh)

##### 1.2.1 `hxl2example`: create your own exporter/importer
- Source code: [bin/hxl2example](bin/hxl2example)

The `hxl2example` is an example python script with generic functionality that
allow you to create your custom functions. Feel free to add your name, edit
license etc.

What it does: `hxl2example` accepts one HXLated dataset and save as .CSV.

##### 1.2.2 `hxl2tab`: tab format, focused for compatibility with Orange Data Mining 
- Main issue: <https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/2>
- Orange File Specification: <https://orange-data-mining-library.readthedocs.io/en/latest/reference/data.io.html>
- Source code: [bin/hxl2tab](bin/hxl2tab)

What it does: `hxl2tab` uses an already HXLated dataset and then, based on
`#hashtag+attributes`, generates an Orange Data Mining .tab format with extra
hints.

> The `hxl2tab` v2.0 has some usable functionality to use a web interface
instead of cli to generate the file. Uses [hug 🐨 🤗](https://github.com/hugapi/hug).

> If you want quick expose outside localhost, try [ngrok](https://ngrok.com/).

##### 1.2.3 `hxlquickimport`: (like the `hxltag`)
- Main issue: <https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/6>
- Source code: [bin/hxlquickimport](bin/hxlquickimport)

What it does: `hxlquickimport` is similar to the `hxltag` (cli tools that are
installed with `libhxl`) mostly only try to by default slugfy whatever was
before on the old headers and add it as HXL attribute. **Please consider using
the HXL-Proxy for serious usage. This quick script is more for internal
testing**

### 2. Reasons behind

#### 2.1 Why?
The HXL already is used in production in special humanitarian areas (see
[The Humanitarian Data Exchange](https://data.humdata.org/)). With
[one line change](https://hxlstandard.org/how-it-works/) is possible to convert
most of already used spreadsheet-like data to be machine readable without need
to disturb end users as other alternatives. One notable implementation
(data visualization) powered by HXL is [HXLDash](https://hxldash.com/) (see 
[this HXLDash example video](https://www.youtube.com/watch?v=5ZmRjLfoS3k)).

The idea of this project strategies to turn already HXLated datasets to be used
directly on open source **desktop** tools like the
[Orange Data Mining](https://orangedatamining.com/) and
[WEKA "The workbench for machine learning"](https://www.cs.waikato.ac.nz/ml/weka/)
**with the the minimum extra explanation on how to convert already existing HXL
datasets AND do exist tools that solve know issues that are likely to be found**.

#### 2.2 How?

> **NOTE: already is possible to use HXLated CSVs on these tools!** For either
  who is leaning HXL or who is using in production for humanitarian intent, the
  HXL-proxy (https://proxy.hxlstandard.org/) with "Strip text headers" can
  serve live-updated CSV-like files. Other usages can still use the
  [HXL CLI tools](https://github.com/HXLStandard/libhxl-python/wiki/Command-line-tools])
  or run the [unocha/hxl-proxy with Docker](https://hub.docker.com/r/unocha/hxl-proxy)
  on your machine or an private public server.

One way to implement this is to create minimum usable conversion tools that
are able to export already HXLated datasets with additional _hints_ to file
formats used by default by their applications.

In practice this is beyond just file conversion (like XLSX to CSV), since it
includes both "variable type" **AND "intent to use (on data mining)"**. This is
why this project also has the taxonomy/vocabulary reference table (and this 
ctually is more important than the implementation itself!). Without some extra
step HXLated datasets work as averange CSV (good, but is just not great).

But yes, some of these converted files, in special Weka (at least if compared
to Orange) are more strict on the tabular format it accepts, and this can be
infuriating EVEN for who actually would know how to debug these issues! But
this issue, at least, is more automatable.

> Note: one practical reason to use HXLated files as base instead of plain CSV
  or XLSX (beyond obviously being available in humanitarian context) is because
  the grammar of HXL +attributes are flexible to export to several different
  formats with freetom to choose other aspects of the tagging.

#### 2.3 Non-goals

- The software implementation for file formats not typically used by easy to use
  desktop applications is a non-goal
    - Yet, since as part of the HXL +attributes conversion tables, some of these
      proposed implementations may already be drafted. These reference tables
      are released under public domain licenses.
    - Note that often humans who already use these formats already are likely
      to have skill to manually concert from CSVs (so could convert from HXL)
- The software implementation (at least at the start) will not optimize for
  speed or low local disk usage
    - **but should work to convert large datasets with reasonable low memory
      usage**
- The software implementations assume an already HXLated input dataset to keep
  it simple
    - Note that it is possible to quickly convert already well formatted CSVs
      to HXL by changing the header line (first line of the CSV).
- While is technically possible to import back (reconstruct the original
  HXLated file) from exported files, this is an non-goal to be 100% compatible
    - This applicable in special cases for .arff exports: the default export
      may need to clean known issues with exported strings.

## HXLated datasets to test

### Production data on The Humanitarian Data Exchange ("HDX")
- Generic search query: https://data.humdata.org/search?vocab_Topics=hxl
- HXL data on HDX
  - Spreadsheet: <https://docs.google.com/spreadsheets/d/1nLahxXVhnSuhCOi1yxAJCS7jFp8sMJ7IFXs1JRbpyjE/edit#gid=0>
  - Crawler: <https://github.com/OCHA-DAP/hxl-hdx-stats>

The Humanitarian Data Exchange ("HDX") contains public datasets and part of
them already is HXLated and ready to test.

> PROTIP: on the <https://proxy.hxlstandard.org/data/source>, the
  _Option 2: choose from the cloud_ also have an icon "HDX" also can be used.
  This can be helpful if you are just looking around several datasets.

### Files from EticaAI-Data_HXL-Data-Science-file-formats

- [tests/files](tests/files)
- [tests/manual-tests.sh](tests/manual-tests.sh)
- Google Drive Folder: <https://drhttps://drive.google.com/drive/u/1/folders/1qyTPaDgm7Ca-62blkdQjUox47WWKRwD3ive.google.com/drive/u/1/folders/1qyTPaDgm7Ca-62blkdQjUox47WWKRwD3>

Both Google Drive Folder and this repository has some test files.
The not-so-documented manual tests may also give a quick idea on how it works.

## Additional Guides

> Note: these additional guides are not part of the main focus of this project

### Command line tools for CSV
- [guides/command-line-tools-for-csv.sh](guides/command-line-tools-for-csv.sh)

> NOTE: Often people who work with HXL simply use the HXL-proxy, including to
  convert from non-HXLated sources.

Here there is an an quick overview of different command line tools that
worth at least mention, in special if are dealing with raw formats already not
HXLated.

### Alternatives to preview spreadsheets with over 1.000.000 rows
- [guides/preview-huge-ammount-of-data.md](guides/preview-huge-ammount-of-data.md)

90% of the time 1.000.000 rows is likely to be enough even if you are dealing
with data science projects. So it means that there is no need to use command
line tools or use more complex solutions, like import to an database or pay for
enterprise solutions.

This guide if when you need to go over these limits without change too much your
tools.

<!--
- ## See Also
  - An Introduction to Data Science  http://www.saedsayad.com/

- ## File formats (comercial programs, SPSS/PSPP Stata, SAS, ...)
  - SPSS .sav 
    - There is no official documentation on fhe file format, but PSPP can be used
    - https://www.gnu.org/software/pspp/pspp-dev/html_node/System-File-Format.html
    - https://www.loc.gov/preservation/digital/formats/fdd/fdd000469.shtml
  - sas7bdat
    - https://cran.r-project.org/web/packages/sas7bdat/vignettes/sas7bdat.pdf
  - Stata .dta
    - Oficial file specification: https://www.stata.com/help.cgi?dta
  - Openclinica vs
    - SPSS https://docs.openclinica.com/3.1/openclinica-user-guide/spss-file-specifications
    - Stata https://docs.openclinica.com/3.1/openclinica-user-guide/importing-openclinica-data-stata
    - https://github.com/OpenClinica/OpenClinica
  - Comparações entre diferentes formatos
    - https://www.inwt-statistics.com/read-blog/comparison-of-r-python-sas-spss-and-stata.html
    - https://redebrasileirademea.ning.com/m/group/discussion?id=3549601%3ATopic%3A80523
  - RData
    - https://stackoverflow.com/questions/51722253/how-to-load-rs-rdata-files-into-python
    - https://github.com/ofajardo/pyreadr
  - Python for read SPSS, SAS and Stata
    - https://github.com/Roche/pyreadstat

- Etc
  - Line break online https://www.joydeepdeb.com/tools/line-break.html
-->

# License

[![Public Domain Dedication](img/public-domain.png)](UNLICENSE)

The [EticaAI](https://github.com/EticaAI) has dedicated the work to the
[public domain](UNLICENSE) by waiving all of their rights to the work worldwide
under copyright law, including all related and neighboring rights, to the extent
allowed by law. You can copy, modify, distribute and perform the work, even for
commercial purposes, all without asking permission.
