# Data Science files exported from HXL (The Humanitarian Exchange Language)
**[public draft][Proof of concept] Common file formats used for Data Science
exported from HXL (The Humanitarian Exchange Language)**

---

<!-- TOC depthFrom:2 -->

- [HXL-Data-Science-file-formats](#hxl-data-science-file-formats)
    - [The main focus](#the-main-focus)
        - [Vocabulary/Taxonomies](#vocabularytaxonomies)
        - [`HXL2` Command line tools](#hxl2-command-line-tools)
    - [Reasons behind](#reasons-behind)
        - [Why?](#why)
        - [How?](#how)
        - [Non-goals](#non-goals)
- [Additional Guides](#additional-guides)
    - [Command line tools for CSV](#command-line-tools-for-csv)
    - [Alternatives to preview spreadsheets with over 1.000.000 rows](#alternatives-to-preview-spreadsheets-with-over-1000000-rows)

<!-- /TOC -->

---

## HXL-Data-Science-file-formats

### The main focus

#### Vocabulary/Taxonomies
- <https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1297379331>

This HXL Spreadsheet have live information about this proof of concept.

#### `HXL2` Command line tools
- See folder [bin/](bin/)
- See discussions at
  - <https://github.com/EticaAI/HXL-Data-Science-file-formats/issues>
  - <https://github.com/HXL-CPLP/forum/issues/52>

At the moment, beyond the [`hxl2example`](bin/hxl2example), this project does
not have usable command line tools to automate work.

### Reasons behind

#### Why?
The HXL already is used in production in special humanitarian areas (see
[The Humanitarian Data Exchange](https://data.humdata.org/)). With
[one line change](https://hxlstandard.org/how-it-works/) is possible to convert
most of already used spreadsheet-like data to be machine readable without need
to disturb end users as other alternatives. One notable implementation
(data visualization) powered by HXL is [HXLDash](https://hxldash.com/) (see 
[this HXLDash example video](https://www.youtube.com/watch?v=5ZmRjLfoS3k)).

The idea of this project is to try ways to convert HXLated datasets to be used
directly on open source **desktop** tools like the
[Orange Data Mining](https://orangedatamining.com/) and
[WEKA "The workbench for machine learning"](https://www.cs.waikato.ac.nz/ml/weka/)
**with the the minimum extra explanation on how to convert already existing HXL
datasets AND do exist tools that solve know issues that are likely to be
found**.

#### How?

> **NOTE: already is possible to use HXL on these tools!** For either who is
  leaning HXL or who is using in production for humanitarian intent, the
  HXL-proxy (https://proxy.hxlstandard.org/) with "Strip text headers" can
  serve live-updated CSV-like files. Other usages can still use the
  [HXL CLI tools](https://github.com/HXLStandard/libhxl-python/wiki/Command-line-tools])
  or run the [unocha/hxl-proxy with Docker](https://hub.docker.com/r/unocha/hxl-proxy)
  on your machine or an private public server.

One way to potentially be able to do this is do the bare minimum to convert some
proof of concetp datasets already HXLated to files know to work on these tools.

> TODO: add more context to _How?_.

#### Non-goals

> TODO: add Non-goals.

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

# License

[![Public Domain Dedication](img/public-domain.png)](UNLICENSE)

The [EticaAI](https://github.com/EticaAI) has dedicated the work to the
[public domain](UNLICENSE) by waiving all of their rights to the work worldwide
under copyright law, including all related and neighboring rights, to the extent
allowed by law. You can copy, modify, distribute and perform the work, even for
commercial purposes, all without asking permission.
