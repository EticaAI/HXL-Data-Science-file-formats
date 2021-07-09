# HXLM: Humanitarian Exchange Language Trānslātiōnem Memoriam

[![Site](https://img.shields.io/badge/Site-hdp.etica.ai%2Fhxltm-blue)](https://hdp.etica.ai/hxltm)
[![EticaAI/HXL-Data-Science-file-formats](https://img.shields.io/badge/GitHub-EticaAI%2FHXL--Data--Science--file--formats-lightgrey?logo=github&style=social)](https://github.com/EticaAI/HXL-Data-Science-file-formats)
[![Python Package: hdp-toolchain](https://img.shields.io/badge/python%20package-hdp--toolchain-brightgreen)](https://pypi.org/project/hdp-toolchain/)
[![Standard HXL](https://img.shields.io/badge/Standard-HXL-%23F26459)](https://hxlstandard.org/)
![License](https://img.shields.io/github/license/EticaAI/HXL-Data-Science-file-formats)
[![Google Drive](https://img.shields.io/badge/Google%20Drive-HXL--CPLP--Vocab_Auxilium--Humanitarium--API-yellowgreen)](https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=470146486)

The _Humanitarian Exchange Language Trānslātiōnem Memoriam_
(abbreviation: "HXLTM") is an HXLated valid HXL tabular format by
[HXL-CPLP](https://github.com/HXL-CPLP) to store community contributed
translations and glossaries.

The `hxltmcli` is an _(initial reference)_ of an public domain python cli tool
allow reuse by others interested in export HXLTM files to common formats
used by professional translators. But software developers interested in promote
use cases of HXL are encouraged to either collaborate to `hxltmcli` or create
other tools.


---

<!-- TOC depthFrom:2 -->

- [Quickstart](#quickstart)
    - [Installation](#installation)
- [File formats](#file-formats)
    - [HXLM: Humanitarian Exchange Language Trānslātiōnem Memoriam](#hxlm-humanitarian-exchange-language-trānslātiōnem-memoriam)
    - [TMX: Translation Memory eXchange v1.4b](#tmx-translation-memory-exchange-v14b)
    - [XLIFF: XML Localization Interchange File Format v2.1](#xliff-xml-localization-interchange-file-format-v21)
        - [HXLTM supported features of XLIFF](#hxltm-supported-features-of-xliff)
    - [Google Sheets](#google-sheets)
    - [Microsoft Excel](#microsoft-excel)
    - [CSV](#csv)
        - [1.5.6.1 CSV reference format, HXLated CSV (multilingual)](#1561-csv-reference-format-hxlated-csv-multilingual)
        - [1.5.6.2 CSV source + target format (bilingual)](#1562-csv-source--target-format-bilingual)
    - [UTX](#utx)
    - [1.5.8 PO, TBX, SRX](#158-po-tbx-srx)
- [Notable alternatives to HXL TM and `hxltmcli`](#notable-alternatives-to-hxl-tm-and-hxltmcli)
    - [1.5.9.1 Okapi Framework](#1591-okapi-framework)
    - [Translate Toolkit](#translate-toolkit)
- [FAQ](#faq)
    - [Save entire Translations Memory on Excel files](#save-entire-translations-memory-on-excel-files)
        - [Example data](#example-data)
    - [Advanced filter with HXL cli tools](#advanced-filter-with-hxl-cli-tools)
    - [Advanced filter with HXL-proxy (integration with Google Sheets and CSV/XLSX/etc avalible on web)](#advanced-filter-with-hxl-proxy-integration-with-google-sheets-and-csvxlsxetc-avalible-on-web)

<!-- /TOC -->

---


<!--

> TODO: see also <https://github.com/idimitriadis0/TranslateOnLinux/blob/master/TranslateOnLinux.md>

- Standard: **Translation Memory eXchange (TMX) v1.4b**
  - https://www.gala-global.org/lisa-oscar-standards
  - https://en.wikipedia.org/wiki/Translation_Memory_eXchange
  - Example of usages
    - https://cloud.google.com/translate/automl/docs/prepare
    - https://mymemory.translated.net/doc/from-empty-tm.php
    - https://site.matecat.com/faq/translation-memory/
- Issues:
  - **HXL-CPLP/forum/issues/**
    - [**_HXL-CPLP/forum/issues/58: Convenção de tags HXL em conjunto de dados para armazenar Memória de Tradução (eng: HXL translation memory TM) \#58_**](https://github.com/HXL-CPLP/forum/issues/58)
  - **HXL-CPLP/Auxilium-Humanitarium-API**
    - **[HXL-CPLP/Auxilium-Humanitarium-API: [Hapi versão Alpha] Fluxo de trabalho de de traduções até geração do Hapi (do website, dos schemas e das OpenAPI)](https://github.com/HXL-CPLP/Auxilium-Humanitarium-API/issues/13)**
    - **[HXL-CPLP/Auxilium-Humanitarium-API: [MVP] Exportar de formato "HXL TM" (eng: HXL translation memory) para um ou mais formatos já usados por softwares de localização](https://github.com/HXL-CPLP/Auxilium-Humanitarium-API/issues/16)**
  - **EticaAI/HXL-Data-Science-file-formats**
    - _**hxltm2xliff: HXL Trānslātiōnem Memoriam -> XLIFF Version 2.1 #19**_
- Test projects
  - https://github.com/UNMigration/HTCDS
  - https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1292720422
-->

## Quickstart

### Installation

`hxltmcli` uses Python 3. While is possible to just copy the `hxltmcli` file
and install manually dependencies, like the
[HXLStandard/libhxl-python](https://github.com/HXLStandard/libhxl-python),
you can install with the [hdp-toolchain](https://pypi.org/project/hdp-toolchain/).

```bash
# hxltmcli is installed with the hdp-toolchain, no extras required.
# @see https://pypi.org/project/hdp-toolchain/
pip install hdp-toolchain

hxltmcli --help

```

## File formats

### HXLM: Humanitarian Exchange Language Trānslātiōnem Memoriam

<a id="HXLTM" href="#HXLTM">§ HXLTM</a>

> TODO: draft this section

### TMX: Translation Memory eXchange v1.4b

<a id="HXLTM-TMX" href="#HXLTM-TMX">§ HXLTM-TMX</a>

- **Wikipedia**: <https://en.wikipedia.org/wiki/Translation_Memory_eXchange>
- **Specification**:
  - <https://www.gala-global.org/tmx-14b>
  - <https://www.gala-global.org/knowledge-center/industry-development/standards/lisa-oscar-standards>
- **TMX 1.4b DTD**
  - <https://www.gala-global.org/sites/default/files/migrated-pages/docs/tmx14%20%281%29.dtd>
- **Relevant GitHub issues**:
  - https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/20
  - https://github.com/HXL-CPLP/forum/issues/58
  - https://github.com/HXL-CPLP/Auxilium-Humanitarium-API/issues/16


```bash
## The next 2 examples are equivalent: will print to stdout the result
hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --TMX
#    (will print out TMX result of input HXLTM file)

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --TMX
#    (will print out TMX result of input HXLTM file)

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv resultatum/hxltm-exemplum-linguam.tmx --TMX
#    (Instead of print to stdout, save the contents to a single CSV file)
```

### XLIFF: XML Localization Interchange File Format v2.1

<a id="HXLTM-XLIFF" href="#HXLTM-XLIFF">§ HXLTM-XLIFF</a>

- **Wikipedia**: <https://en.wikipedia.org/wiki/XLIFF>
- **Specification**:
  - <http://docs.oasis-open.org/xliff/xliff-core/v2.1/os/xliff-core-v2.1-os.html>
- **Relevant GitHub issues**:
  - https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/19
  - https://github.com/HXL-CPLP/forum/issues/58
  - https://github.com/HXL-CPLP/Auxilium-Humanitarium-API/issues/16
- **Extra links**
  - Okapi about XLIFF: <https://okapiframework.org/wiki/index.php/XLIFF>


```bash
## The next 2 examples are equivalent: will print to stdout the result
hxltmcli hxltm-exemplum-linguam.tm.hxl.csv --XLIFF
#    (will print out TMX result of input HXLTM file)

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli --XLIFF
#    (will print out TMX result of input HXLTM file)

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv resultatum/hxltm-exemplum-linguam.xlf --XLIFF
#    (Instead of print to stdout, save the contents to a single CSV file)
```

**Extras: VSCode XLIFF extension**
Check also this VSCode extension
<https://marketplace.visualstudio.com/items?itemName=rvanbekkum.xliff-sync>.
While we do not checked yet, it seems to allow "merge" new translations from
a different XLIFF file to another one.


#### HXLTM supported features of XLIFF

> TODO: improve documentation of features HXLTM support export to XLIFF

### Google Sheets
The `hxltmcli` supports read directly from Google Sheets (no extra plugins
required).

**Read HXL TM data saved on Google Sheets**

```bash
hxltmcli https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1292720422
#    (will print out contents of Google Sheets, without exporting to other formats)

hxltmcli https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1292720422 | grep UN_codicem_anglicum_IOM_HTCDS_nomen
#    UN_codicem_anglicum_IOM_HTCDS_nomen,,,,13,1,UN,UN,codicem_anglicum,IOM,HTCDS,,,nomen,,,,,,,,,,,,,,∅,∅,Padrão de Dados de Casos de Tráfico Humano,∅,Revisão de texto requerida,Human Trafficking Case Data Standard,∅,∅,,∅,∅,,∅,∅,,∅,∅,,∅,∅

hxltmcli https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1292720422 schemam-un-htcds.tm.hxl.csv
#    (Instead of print to stdout, save the contents to a single CSV file)

```

**Write HXL TM data on Google Sheets**

Writting to Google Sheets is possible by using external tool to import the
CSV versions.

> TODO: document some external cli script that allow upload CSV to Google 
> Sheets.

### Microsoft Excel

<a id="HXLTM-XLSX" href="#HXLTM-XLSX">§ HXLTM-XLSX</a>

**Read HXL TM data saved on Excel**

The `hxltmcli` supports read directly from Microsoft Excel (no extra plugins
required).

```bash
# The HXL-CPLP-Vocab_Auxilium-Humanitarium-API.xlsx is a downloaded version of
# the Google Sheets entire groups of HXL TMs on 2021-06-29. New versions are
# likely to be a different number than --sheet 6
hxltmcli --sheet 6 HXL-CPLP-Vocab_Auxilium-Humanitarium-API.xlsx
#    (will print out contents of --sheet 6, without exporting to other formats)

hxltmcli --sheet 6 HXL-CPLP-Vocab_Auxilium-Humanitarium-API.xlsx | grep UN_codicem_anglicum_IOM_HTCDS_nomen
#    UN_codicem_anglicum_IOM_HTCDS_nomen,,,,13,1,UN,UN,codicem_anglicum,IOM,HTCDS,,,nomen,,,,,,,,,,,,,,∅,∅,Padrão de Dados de Casos de Tráfico Humano,∅,Revisão de texto requerida,Human Trafficking Case Data Standard,∅,∅,,∅,∅,,∅,∅,,∅,∅,,∅,∅

hxltmcli --sheet 6 HXL-CPLP-Vocab_Auxilium-Humanitarium-API.xlsx schemam-un-htcds.tm.hxl.csv
#    (Instead of print to stdout, save the contents to a single CSV file)
```

**Write HXL TM data on Microsoft Excel**

Writting to Microsoft Excel is possible by using external tool to import the
CSV versions. Here is just one example, but you are free to use alternatives.

Example using [unoconv](https://github.com/unoconv/unoconv). Tested with
Ubuntu 20.04 LTS and LibreOffice 6.4.

```bash
# One recommendedy way to install unoconv is via operational system packages
# not with pip.
sudo apt install unoconv

# Test data at EticaAI/HXL-Data-Science-file-formats/tests/hxltm/
unoconv --format xlsx hxltm-exemplum-linguam.tm.hxl.csv

# Note: in our tests, unoconv may have exporting bugs with unicode, see
# @see https://github.com/unoconv/unoconv/issues/271

```

### CSV

<a id="HXLTM-CSV" href="#HXLTM-CSV">§ HXLTM-CSV</a>

#### 1.5.6.1 CSV reference format, HXLated CSV (multilingual)
The default output of `hxltmcli` already is output an valid HXLated CSV without
data changes changes (with notable exception of normalize HXL hashtags, like
convert `#item +i_ar +i_arb +is_Arab` to `#item+i_ar+i_arb+is_arab`).


```bash
## The next 2 examples are equivalent: will print to stdout the result
hxltmcli hxltm-exemplum-linguam.tm.hxl.csv
#    (will print out contents of hxltm-exemplum-linguam.tm.hxl.csv)

cat hxltm-exemplum-linguam.tm.hxl.csv | hxltmcli
#    (will print out contents of hxltm-exemplum-linguam.tm.hxl.csv)

hxltmcli hxltm-exemplum-linguam.tm.hxl.csv output-file.tm.hxl.csv
#    (Instead of print to stdout, save the contents to a single CSV file)
```

**PROTIP**: You can chain several `hxltmcli` commands (ideally, the last
command to export) or the first command to import from something that already
is not HXL should be `hxltmcli`, but for advanced processing, see
<a href="#HXLTM-libhxl-cli-tools">HXLTM-libhxl-cli-tools</a>.

#### 1.5.6.2 CSV source + target format (bilingual)
> TODO: document minimal usage

```bash
# This is a draft.
# Tests from ./tests/hxltm/manuale-testum.sh

## CSV-3
fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/tests/hxltm$ hxltag -m en-GB#item+rem+i_en+i_eng+is_latn -m pt-PT#item+rem+i_pt+i_por+is_latn -m Comment#meta csv-3-exemplum.csv | hxltmcli -f eng-Latn@en-GB -o por-Latn@pt-PT --CSV-3 > resultatum/csv-3-exemplum.csv

## JSON-kv
hxltag -m en-GB#item+rem+i_en+i_eng+is_latn -m pt-PT#item+rem+i_pt+i_por+is_latn -m Comment#meta csv-3-exemplum.csv | hxltmcli -f eng-Latn@en-GB -o por-Latn@pt-PT --JSON-kv

hxltag -m en-GB#item+rem+i_en+i_eng+is_latn -m pt-PT#item+rem+i_pt+i_por+is_latn -m Comment#meta csv-3-exemplum.csv | hxltmcli -f eng-Latn@en-GB -o por-Latn@pt-PT --JSON-kv > resultatum/json-kv/pt.json

```

### UTX

<a id="HXLTM-UTX" href="#HXLTM-UTX">§ HXLTM-UTX</a>

- https://aamt.info/english/utx/
- Specification: <https://aamt.info/wp-content/uploads/2019/06/utx1.20-specification-e.pdf>

> TODO: maybe implement exporting to UTX (it's not complex than already done
> with CSV)

### 1.5.8 PO, TBX, SRX
> - About PO files: <https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html>
> - TBX:
>   - <http://www.ttt.org/oscarStandards/tbx/>
>     - TBX-Basic <http://www.ttt.org/oscarStandards/tbx/tbx-basic.html>

`hxltmcli` does not import or export **PO** files directly. Okapi Framework can be
used to export XLIFF created by  `hxltmcli`.

`hxltmcli` does not import or export **TBX** and **SRX** files directly. It's
not clear if possible to use any external to import/export from already
supported formats (like TMX and XLIFF) creted by `hxltmcli` without
implementing this feature directly on `hxltmcli`.

> TODO: we could consider supporting TBX (see https://en.wikipedia.org/wiki/TermBase_eXchange)
> since IATE seems to export glossaries on this format. See also
> <https://termcoord.eu/iate/download-iate-tbx/>.

<!--
Notes to self:
- Here have some sample spreadsheets with examples used on how a existing tool
  is able to convert glossaries to TBX-Min, See
  - https://www.tbxinfo.net/tbx-tools-v2/spreadsheet-glossary-converter/
    - https://www.tbxinfo.net/wp-content/uploads/2016/05/sampleSpreadsheets.zip
    - https://www.tbxinfo.net/wp-content/uploads/2016/06/Spreadsheet-to-TBX-Min-Tutorial.pdf
- TBX software https://www.tbxconvert.gevterm.net/tbx_supported_software.html

From http://www.terminorgs.net/downloads/TBX_Basic_Version_3.1.pdf:

  There are only two mandatory data categories in TBX-Basic: term, and language.
  Several of the remaining data categories, including definition, context, part of speech, and subject
  field are very important and should be included in a terminology whenever possible. The most
  important non-mandatory data category is part of speech.

OmegaT (testar TBX)
- sudo snap install omegat-cat

Testando Vitaal:
- Vide https://github.com/HXL-CPLP/forum/issues/58#issuecomment-872610790
-->

## Notable alternatives to HXL TM and `hxltmcli`
<!--
> - See also: <https://okapiframework.org/wiki/index.php/Open_Standards>
-->

> **Note**: all alternatives here tend to be very optimized **but only for mono
or bilingual localization files**.
>
> Some have advanced features, like merge/compare/update two different files
> (like 2 XLIFFs) seems to be documented for some of them. They also sometimes
> have exporters for multilingual formats, like UTX, TBX TMX, but often they
> still only work with maximum of 2 languages.
>
> One approach with `hxltmcli` would both focus on HXL and conversion for
> formats that existing tools don't do well, but this also means we do not
> waste time to create more exporters for mono or bilinguam files.

### 1.5.9.1 Okapi Framework

> TODO: this is a draft. Improve it.

- https://okapiframework.org/
  - http://okapiframework.org/wiki/index.php?title=Tikal

### Translate Toolkit

<a id="translate-toolkit" href="#translate-toolkit">§ Translate Toolkit</a>

**Options from Translate Toolkit**

From https://github.com/translate/translate:

```bash
### Installation----------------------------------------------------------------
# @see https://github.com/translate/translate
pip install translate-toolkit
# Install with XML support
# pip install translate-toolkit[XML]

# Install all optional dependencies
pip install translate-toolkit[all]

### Converters -----------------------------------------------------------------
oo2po    - convert between OpenOffice.org GSI files and PO
oo2xliff - convert between OpenOffice.org GSI files and XLIFF
moz2po   - convert between Mozilla files and PO
csv2po   - convert PO format to CSV for editing in a spreadsheet program
php2po   - PHP localisable string arrays converter.
ts2po    - convert Qt Linguist (.ts) files to PO
txt2po   - convert simple text files to PO
html2po  - convert HTML to PO (beta)
xliff2po - XLIFF (XML Localisation Interchange File Format) converter
prop2po  - convert Java .properties files to PO
po2wordfast - Wordfast Translation Memory converter
po2tmx   - TMX (Translation Memory Exchange) converter
pot2po   - PO file initialiser
csv2tbx  - Create TBX (TermBase eXchange) files from Comma Separated
           Value (CSV) files
ini2po   - convert .ini files to to PO
ical2po  - Convert iCalendar files (*.ics) to PO
sub2po   - Convert many subtitle files to PO
resx2po  - convert .Net Resource (.resx) files to PO

### Tools (Quality Assurance): -------------------------------------------------
pofilter - run any of the 40+ checks on your PO files
pomerge  - merge corrected translations from pofilter back into
           your existing PO files.
poconflicts - identify conflicting use of terms
porestructure - restructures po files according to poconflict directives
pogrep   - find words in PO files

### Tools (Other): -------------------------------------------------------------
pocompile - create a Gettext MO files from PO or XLIFF files
pocount   - count translatable file formats (PO, XLIFF)
podebug   - Create comment in your PO files msgstr which can
            then be used to quickly track down mistranslations
            as the comments appear in the application.
posegment - Break a PO or XLIFF files into sentence segments,
            useful for creating a segmented translation memory.
poswap    - uses a translation of another language that you
            would rather use than English as source language
poterminology - analyse PO or POT files to build a list of
                frequently occurring words and phrases
```

Without need to install the packages, you can check online documentation at
<http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/index.html>.

## FAQ

### Save entire Translations Memory on Excel files

#### Example data

- `HXLTM-Exemplum`: Generic test files:
  - Input files: [tests/hxltm/](/tests/hxltm/)
    - Live spreadsheet: <https://docs.google.com/spreadsheets/d/1isOgjeRJw__nky-YY-IR_EAZqLI6xQ96DKbD4tf0ZO8/edit#gid=0>
  - Output files: [tests/hxltm/resultatum/](tests/hxltm/resultatum/)
- Production files:
  - `HXL-CPLP-Vocab_Auxilium-Humanitarium-API`: Hapi project
    - GitHub:
      - https://github.com/HXL-CPLP/Auxilium-Humanitarium-API
    - Live Spreadsheet:
      - <https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=470146486>
      - Note: the project may eventually use other sources of data (and this
        link here may eventually not be up to date)

### Advanced filter with HXL cli tools

<a id="HXLTM-libhxl-cli-tools" href="#HXLTM-libhxl-cli-tools">§ HXLTM-libhxl-cli-tools</a>

- See **https://github.com/HXLStandard/libhxl-python/wiki/HXL-cookbook**

Since a HXLTM (before export) is a valid HXL file, advanced seleting is
possible by, instead of `hxltmcli input.hxl.csv output.hxl.csv` use
`hxlcut input.hxl.csv --exclude (...) | hxltmclioutput.hxl.csv`.

```bash
# libhxl already is installed with hdp-toolchain

hxlselect --help
#    Filter rows in a HXL dataset. (...)
hxlcut --help
#    Cut columns from a HXL dataset.

## Examples with HXL TM (used before pass data to hxltmcli)
hxlcut --exclude item+i_la+i_lat+is_Latn --sheet 6 HXL-CPLP-Vocab_Auxilium-Humanitarium-API.xlsx | hxltmcli
# Excludes Latin before pass to hxltmcli, from Microsoft Excel

hxlcut --exclude item+i_la+i_lat+is_Latn https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1292720422 | hxltmcli
# Excludes Latin before pass to hxltmcli, from Google Sheets

```
### Advanced filter with HXL-proxy (integration with Google Sheets and CSV/XLSX/etc avalible on web)

<a id="HXLTM-HXL-Proxy" href="#HXLTM-HXL-Proxy">§ HXLTM-HXL-Proxy</a>

In special if you are contributing for either tools for HXL, testing this tool
or helping in production (e.g. real time disaster response) please consider
usage of the public HXL-Proxy on https://proxy.hxlstandard.org/.

Most advanced features of the libhxl cli tools are availible via HXL-proxy.

**Note about heavy usage: use cache**
Both https://hapi.etica.ai/ and https://github.com/HXL-CPLP/Auxilium-Humanitarium-API
(and some links used on this documentation) may use the HXL-Proxy default
1 hour cache disabled. This is necessary because the HXL-proxy is used to build
static content based on latest translations.

It's a good practice if you are not only testing, but deployng in production,
to not disable HXL-Proxy cache (it's the default option if not copy and pasting
HXL-CPLP/Auxilium-Humanitarium-API internal build script links).

Also, even if you do not use the HXL-Proxy (but is using `hxltm` directly to
your own Google Spreadsheets) if you keep doing too much calls in short time
eventually the Google Docs may raise 400 errors since `hxltm` are not
authenticated requests. **Our recomendations on this case is:**

1. **download the entire Spreadsheet as .xlsx file and process the .xlsx file locally.**
2. **Download individual sheets as CSV files and save locally (this consumes less CPU than process .xlsx)**

# License

[![Public Domain Dedication](../img/public-domain.png)](UNLICENSE)

The [EticaAI](https://github.com/EticaAI) has dedicated the work to the
[public domain](../UNLICENSE) by waiving all of their rights to the work worldwide
under copyright law, including all related and neighboring rights, to the extent
allowed by law. You can copy, modify, distribute and perform the work, even for
commercial purposes, all without asking permission.
