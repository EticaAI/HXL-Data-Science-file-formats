# Data Science files exported from HXL (The Humanitarian Exchange Language)
**[Proof of concept] Common file formats used for Data Science
exported from HXL (The Humanitarian Exchange Language)**

[![Site](https://img.shields.io/badge/Site-hdp.etica.ai-blue)](https://hdp.etica.ai)
[![EticaAI/HXL-Data-Science-file-formats](https://img.shields.io/badge/GitHub-EticaAI%2FHXL--Data--Science--file--formats-lightgrey?logo=github&style=social)](https://github.com/EticaAI/HXL-Data-Science-file-formats)
[![Python Package: hdp-toolchain](https://img.shields.io/badge/python%20package-hdp--toolchain-brightgreen)](https://pypi.org/project/hdp-toolchain/)
[![Standard HXL](https://img.shields.io/badge/Standard-HXL-%23F26459)](https://hxlstandard.org/)
![License](https://img.shields.io/github/license/EticaAI/HXL-Data-Science-file-formats)
[![Google Drive](https://img.shields.io/badge/Google%20Drive-Folder-yellowgreen)](https://drive.google.com/drive/u/1/folders/1qyTPaDgm7Ca-62blkdQjUox47WWKRwD3)

---

<!-- TOC depthFrom:2 -->

- [HXL-Data-Science-file-formats](#hxl-data-science-file-formats)
    - [1. The main focus](#1-the-main-focus)
        - [1.1 Vocabulary, Taxonomies and URNs](#11-vocabulary-taxonomies-and-urns)
            - [1.1.1 Vocabulary & Taxonomies on HXL](#111-vocabulary--taxonomies-on-hxl)
            - [1.1.2 Uniform Resource Name on `URN:DATA`](#112-uniform-resource-name-on-urndata)
                - [Why use URN to identify resources is more than naming convention](#why-use-urn-to-identify-resources-is-more-than-naming-convention)
                - [Security (and privacy) considerations (for `URN:DATA`)](#security-and-privacy-considerations-for-urndata)
                - [Disclaimer (for `URN:DATA`)](#disclaimer-for-urndata)
            - [1.1.3 Ontologia](#113-ontologia)
                - [Why: focus on abstract complexity for users AND allow reuse by other projects](#why-focus-on-abstract-complexity-for-users-and-allow-reuse-by-other-projects)
                - [Distribution channels](#distribution-channels)
        - [1.2 `HXL2` Command line tools](#12-hxl2-command-line-tools)
            - [1.2.1 `hxl2example`: create your own exporter/importer](#121-hxl2example-create-your-own-exporterimporter)
            - [1.2.2 `hxl2tab`: tab format, focused for compatibility with Orange Data Mining](#122-hxl2tab-tab-format-focused-for-compatibility-with-orange-data-mining)
            - [1.2.3 `hxlquickmeta`: output information about local/remote datasets (even non HXLated yet)](#123-hxlquickmeta-output-information-about-localremote-datasets-even-non-hxlated-yet)
            - [1.2.4 `hxlquickimport`: (like the `hxltag`)](#124-hxlquickimport-like-the-hxltag)
        - [1.3 `URN` Command line tools](#13-urn-command-line-tools)
            - [1.3.1 `urnresolver`: convert Uniform Resource Name of datasets to real IRIs (URLs)](#131-urnresolver-convert-uniform-resource-name-of-datasets-to-real-iris-urls)
        - [1.4 `HDP` HDP Declarative Programming (early draft)](#14-hdp-hdp-declarative-programming-early-draft)
            - [1.4.1 HDP conventions (The YAML/JSON file structure)](#141-hdp-conventions-the-yamljson-file-structure)
            - [1.4.2 `hdpcli` (command line interface)](#142-hdpcli-command-line-interface)
            - [1.4.3 `HXLm.HDP` (python library subpackage) usage](#143-hxlmhdp-python-library-subpackage-usage)
        - [1.5 `HXLTM` HXL Trānslātiōnem Memoriam](#15-hxltm-hxl-trānslātiōnem-memoriam)
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

#### 1.1 Vocabulary, Taxonomies and URNs

##### 1.1.1 Vocabulary & Taxonomies on HXL

- <https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1297379331>

This project either use explicit HXL +attributes (easy to implement, but more
verbose) or do inferences on well know HXLated datasets used on humanitarian
areas. To make this work, the main reference is not software implementation, but
reference tables.

##### 1.1.2 Uniform Resource Name on `URN:DATA`

- **Extra content: [urn-data-specification/](urn-data-specification/)** <sup>(warning: its complicated)</sup>

###### Why use URN to identify resources is more than naming convention

While find _good_ URNs conventions to be used for typical datasets used on
humanitarian context is more complex than the
[ISO URN](https://tools.ietf.org/html/rfc5141) or even the
[LEX URN](https://en.wikipedia.org/wiki/Lex_(URN)) (this one
[already used in Brazil](https://www.lexml.gov.br/urn/urn:lex:br:federal:constituicao:1988-10-05;1988)),
one goal of the `urnresolver` is accept that most data shared are VERY
sensitive and private, so this this actually is the challenge. So in addition
to converting some well known public datasets related to HXL, we're already
designing to eventually be used as abstraction to scripts and tools that
without this would need to have access to real datasets.

By using URNs, at _worst case_ we're creating documentations and scripts
that a new user would need to replace by the real one of its use case. But the
ideal case is to allow exchange scripts or, when an issue happens in a new
region, the personel who prepare the data could do it and then publish also
on _private_ URN listing so others could reuse.

Note that the URN Resolver, even if it does have links to resources and not
just the contact page, the links themselves to download the real data could
still require authentication case by case. Also same URNs, if you manage to
have contact with several peers, in special for datasets that are not already
an COD, but are often needed, are likely to exist with more than one option
to use.

Deeper integration with CKAN instances and/or awareness of encrypted data
still not implemented on the current version (v0.7.3)

###### Security (and privacy) considerations (for `URN:DATA`)
Since the main goal of URNs is also help with auditing and sharing of
scripts and even how to reference "best acceptable use" of exchanced data
(with special focus for private/sensitive), while the `URN:DATA` themselves
are mean to be NOT a secret and could be published on official documents, the
local implementations (aka how to resolve/redirect these URNs for real data)
need to take in account concepts that the "perfect optimization" (think
"secure from misuse" vs "protect privacy from legitimate use") often is
contraditory.

TODO: add more context

###### Disclaimer (for `URN:DATA`)

> Note: while this project, in addition to CLI tools to convert URNs to
usable tool (_"the implementation"_), also draft the logic about how to
construct potentially useful URNs reusable at International level (e.g.
what may seem as drafted _"an standard"_, think ISO, or an
_Best Current Practice_, think IETF) please do not take
EticaAI/HXL-Data-Science-file-formats... as endorsed by any organization.

> Also, authors from @EticaAI / @HXL-CPLP (both past and future ones who
cooperate directly with this project) explicitly release both software and
drafted 'how to Implement' under public domain-like licenses. Under
_ideal circumstances_ `data global namespace` (the ZZ on
`urn:data:ZZ:example`) may have more specific rules


##### 1.1.3 Ontologia

> **See [ontologia/](ontologia/)**

> "In computer science and information science, an ontology encompasses a
  representation, formal naming and definition of the categories, properties
  and relations between the concepts, data and entities that substantiate one,
  many, or all domains of discourse. More simply, an ontology is a way of
  showing the properties of a subject area and how they are related, by
  defining a set of concepts and categories that represent the subject."
  -- [Wikipedia: Ontology (information science)](https://en.wikipedia.org/wiki/Ontology_(information_science)

The contents from [ontologia/](ontologia/) both contain some
selected datasets and (while not 100% converted) the main parts of how
command line tools and libraries released by this repository use.

###### Why: focus on abstract complexity for users AND allow reuse by other projects

When feasible, even if it make harder to do initial implementation or be
_a bit less efficient_ than use dedicated _"advanced"_ strategies with
state of the art tools, the internal parts of hxlm.core that deal with
[ontology](https://en.wikipedia.org/wiki/Ontology_(information_science)) will
be stored in this folder.

This strategy is likely to make it easier for non-developers to update
internals, like individuals interested in adding new languages or proposing
corrections.

###### Distribution channels

For production usage, these files are both availible via:

- Installable with [Python Pypi hdp-toolchain](https://pypi.org/project/hdp-toolchain/)
- The GitHub repository <https://github.com/EticaAI/HXL-Data-Science-file-formats>
- Public "CDN": GitHub hosted + CloudFlare cached endpoint at
[https://hdp.etica.ai/ontologia/](https://hdp.etica.ai/ontologia/)


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

**Quick examples**

```bash
### Basic examples

# This will output a local file to stdout (tip: you can disable local files)
hxl2example tests/files/iris_hxlated-csv.csv

# This will save to a local file
hxl2example tests/files/iris_hxlated-csv.csv my-local-file.example

# Since we use the libhxl-python, remote HXLated remote urls works too!
hxl2example https://docs.google.com/spreadsheets/d/1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/edit#gid=319251406

### Advanced usage (if you need to share work with others)

## Quick ad-hoc web proxy, local usage
# @see https://github.com/hugapi/hug

hug -f bin/hxl2example
# http://localhost:8000/ will how an JSON documentation of hug endpoints. TL;DR:
# http://localhost:8000/hxl2example.csv?source_url=http://example.com/remote-file.csv

## Expose local web proxy to others
# @see https://ngrok.com/
ngrok http 8000
```

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

**Installation**

This package can both be installed by doing a copy of
[bin/hxl2tab](bin/hxl2tab) to a place on your executable path and
installing dependencies manually.

The automated way to your path or as part of the
Python pypi package [hdp-toolchain](https://pypi.org/project/hdp-toolchain/)
already with extra dependencies is:

```bash
python3 -m pip install hdp-toolchain[hxl2tab]

# python3 -m pip install hdp-toolchain[full]
```

##### 1.2.3 `hxlquickmeta`: output information about local/remote datasets (even non HXLated yet)
- Main issue: <https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/6>
- Source code: [bin/hxlquickmeta](bin/hxlquickmeta)

What it does: `hxlquickmeta` output information about a local or remote
dataset. If the file already is HXLated, it will print even more information.

v1.1.0 added support to give an overview by default, equivalent to users of
[Python Pandas](https://github.com/pandas-dev/pandas).

**Installation**

This package can both be installed by doing a copy of
[bin/hxlquickmeta](bin/hxlquickmeta) to a place on your executable path and
installing dependencies manually.

The automated way to your path or as part of the
Python pypi package [hdp-toolchain](https://pypi.org/project/hdp-toolchain/)
already with extra dependencies is:

```bash
python3 -m pip install hdp-toolchain[hxlquickmeta]

# python3 -m pip install hdp-toolchain[full]
```

**Quick examples**

```bash
#### inline result for and hashtag and (optional) value ________________________

hxlquickmeta --hxlquickmeta-hashtag="#adm2+code" --hxlquickmeta-value="BR3106200"
# > get_hashtag_info
# >> hashtag: #adm2+code
# >>> HXLMeta._parse_heading: #adm2+code
# >>> HXLMeta.is_hashtag_base_valid: None
# >>> libhxl_is_token None
# >> value: BR3106200
# >>> libhxl_is_empty False
# >>> libhxl_is_date False
# >>> libhxl_is_number False
# >>> libhxl_is_string True
# >>> libhxl_is_token None
# >>> libhxl_is_truthy False
# >>> libhxl_typeof string

#### Output information for an file, and (if any) HXLated information __________
# Local file
hxlquickmeta tests/files/iris_hxlated-csv.csv

# Remove file
hxlquickmeta https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833


```

##### 1.2.4 `hxlquickimport`: (like the `hxltag`)
- Main issue: <https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/6>
- Source code: [bin/hxlquickimport](bin/hxlquickimport)

What it does: `hxlquickimport` is similar to the `hxltag` (cli tools that are
installed with `libhxl`) mostly only try to by default slugfy whatever was
before on the old headers and add it as HXL attribute. **Please consider using
the HXL-Proxy for serious usage. This quick script is more for internal
testing**

**Installation**

This package can both be installed by doing a copy of
[bin/hxlquickimport](bin/hxlquickimport) to a place on your executable path and
installing dependencies manually.

The automated way to your path or as part of the
Python pypi package [hdp-toolchain](https://pypi.org/project/hdp-toolchain/)
already with extra dependencies is:

```bash
python3 -m pip install hdp-toolchain[hxlquickimport]

# python3 -m pip install hdp-toolchain[full]
```

#### 1.3 `URN` Command line tools

**Installation**

The automated way to install is using the Python pypi package
[hdp-toolchain](https://pypi.org/project/hdp-toolchain/). urnresolver is
installed by default.

```bash
python3 -m pip install hdp-toolchain
```

##### 1.3.1 `urnresolver`: convert Uniform Resource Name of datasets to real IRIs (URLs)
- Main issue: <https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/13>
- Source code: [hxlm/core/bin/urnresolver.py](https://github.com/EticaAI/HXL-Data-Science-file-formats/blob/main/hxlm/core/bin/urnresolver.py)

The `urnresolver` is an proof of concept of an URN resolver. (see
[Uniform Resource Name (URN) on Wikipedia](https://pt.wikipedia.org/wiki/URN)).

**Examples (note: early working draft!)**
```bash
# Basic usage: based on local and (to be implemented) remote listing pages
# it translate one readable URN to one or more datasets
urnresolver urn:data:xz:hxl:standard:core:hashtag
# https://docs.google.com/spreadsheets/d/1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/pub?gid=319251406&single=true&output=csv

# Now, the more practical example: using to translate to other commands:
hxlselect "$(urnresolver urn:data:xz:hxl:standard:core:hashtag)" --query '#valid_vocab=+v_pcode'
#    Hashtag,Hashtag one-liner,Hashtag long description,Release status,Data type restriction,First release,Default taxonomy,Category,Sample HXL,Sample description
#    #valid_tag,#description+short+en,#description+long+en,#status,#valid_datatype,#meta+release,#valid_vocab+default,#meta+category,#meta+example+hxl,#meta+example+description+en
#    #adm1,Level 1 subnational area,Top-level subnational administrative area (e.g. a governorate in Syria).,Released,,1.0,+v_pcode,1.1. Places,#adm1 +code,administrative level 1 P-code
#    #adm2,Level 2 subnational area,Second-level subnational administrative area (e.g. a subdivision in Bangladesh).,Released,,1.0,+v_pcode,1.1. Places,#adm2 +name,administrative level 2 name
#    #adm3,Level 3 subnational area,Third-level subnational administrative area (e.g. a subdistrict in Afghanistan).,Released,,1.0,+v_pcode,1.1. Places,#adm3 +code,administrative level 3 P-code
#    #adm4,Level 4 subnational area,Fourth-level subnational administrative area (e.g. a barangay in the Philippines).,Released,,1.0,+v_pcode,1.1. Places,#adm4 +name,administrative level 4 name
#    #adm5,Level 5 subnational area,Fifth-level subnational administrative area (e.g. a ward of a city).,Released,,1.0,+v_pcode,1.1. Places,#adm5 +code,administrative level 5 name

hxlselect "$(urnresolver urn:data:xz:hxlcplp:fod:lang)" --query '#vocab+id+v_iso6393_3letter=por'
#    Id,Part2B,Part2T,Part1,Scope,Language_Type,Ref_Name,Comment
#    #vocab+id+v_iso6393_3letter,#vocab+code+v_iso3692_3letter+z_bibliographic,#vocab+code+v_3692_3letter+z_terminology,#vocab+code+v_6391,#status,#vocab+type,#vocab+name,#description+comment+i_en
#    por,por,por,pt,I,L,Portuguese,
```

#### 1.4 `HDP` HDP Declarative Programming (early draft)

- _[Big Picture]_ The main GitHUb issue:
  - https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/16
- https://en.wikipedia.org/wiki/Non-English-based_programming_languages#International_programming_languages
- Note: most of _the logic that matters_ of HDP is likely to be on
  Knowledge Graphs (YAML files that expand in memory).
  - See [hxlm/ontologia/](hxlm/ontologia/)
    - In special [ontologia/core.vkg.yml](https://github.com/EticaAI/HXL-Data-Science-file-formats/blob/main/hxlm/ontologia/core.vkg.yml)

**Installation**

The automated way to install is using the Python pypi package
[hdp-toolchain](https://pypi.org/project/hdp-toolchain/). All the relevand
parts, including bare minimal [ontologia](ontologia), are part of the default
installation.

```bash
python3 -m pip install hdp-toolchain
```

##### 1.4.1 HDP conventions (The YAML/JSON file structure)

- [hdp-conventions](hdp-conventions)


<!--
> "ALGOL 68 was the first (and possibly one of the last) major language for
  which a full formal definition was made before it was implemented."
  -- C. H. A. Koster
-->


##### 1.4.2 `hdpcli` (command line interface)

- [hxlm/core/bin/hdpcli.py](https://github.com/EticaAI/HXL-Data-Science-file-formats/blob/main/hxlm/core/bin/hdpcli.py)

##### 1.4.3 `HXLm.HDP` (python library subpackage) usage

- GitHub Gist
  - https://gist.github.com/fititnt/3dd12c61170d290fe94cafb1f672a0b5
- Google Colab (Jupyter Notebook)
  - File
  - Folder `HXL-CPLP-Publico/Datasets/EticaAI-Data/EticaAI-Data_HXL-Data-Science-file-formats/HDP-playbooks`
    - https://drive.google.com/drive/u/1/folders/1Zs-hw6y2ZHMgYXjGY1QbhrXn2UmheUEO

#### 1.5 `HXLTM` HXL Trānslātiōnem Memoriam

<a id="HXLTM" href="#HXLTM">§ HXLTM</a>

> **Dedicated documentation at <https://hdp.etica.ai/hxltm>**

The _Humanitarian Exchange Language Trānslātiōnem Memoriam_
(abbreviation: "HXLTM") is an HXLated valid HXL tabular format by
[HXL-CPLP](https://github.com/HXL-CPLP) to store community contributed
translations and glossaries.

The `hxltmcli` is an _(initial reference)_ of an public domain python cli tool
allow reuse by others interested in export HXLTM files to common formats
used by professional translators. But software developers interested in promote
use cases of HXL are encouraged to either collaborate to `hxltmcli` or create
other tools.

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
- [meta issue] HXL and data directly from and to SQL databases #10
  - https://sqlite.org/inmemorydb.html
  - https://github.com/wireservice/csvkit/blob/master/csvkit/utilities/csvsql.py
  - https://stackoverflow.com/questions/32833145/advantages-of-an-in-memory-database-in-sqlite/32833770
- Encryption/security
  - https://www.solarwindsmsp.com/blog/types-database-encryption-methods


- Etc
  - Line break online https://www.joydeepdeb.com/tools/line-break.html
  - https://dba.stackexchange.com/questions/243172/is-individual-column-and-row-level-encryption-possible-in-sql-server
-->

# License

[![Public Domain Dedication](img/public-domain.png)](UNLICENSE)

The [EticaAI](https://github.com/EticaAI) has dedicated the work to the
[public domain](UNLICENSE) by waiving all of their rights to the work worldwide
under copyright law, including all related and neighboring rights, to the extent
allowed by law. You can copy, modify, distribute and perform the work, even for
commercial purposes, all without asking permission.
