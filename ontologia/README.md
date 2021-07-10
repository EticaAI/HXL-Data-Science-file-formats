# The heart of the HXLm, HDP and HDPLisp ontologies

> **Protip: if you cannot make local cache from the
  [GitHub repository](https://github.com/EticaAI/HXL-Data-Science-file-formats)
  or install the
  [Python Pypy package hdp-toolchain](https://pypi.org/project/hdp-toolchain/)
  the <https://hdp.etica.ai/ontologia/> is an public end point.**

When feasible, even if it make harder to do initial implementation or be
_a bit less efficient_ than use dedicated _"advanced"_ strategies with
state of the art tools, the internal parts of hxlm.core that deal with
[ontology](https://en.wikipedia.org/wiki/Ontology_(information_science)) will
be stored in this folder.

This strategy is likely to make it easier for non-developers to update
internals, like individuals interested in adding new languages or proposing
corrections.

---

<!-- TOC depthFrom:2 -->

- [Knowledge Graph and JSON Schemas](#knowledge-graph-and-json-schemas)
    - [Localization Knowledge Graph](#localization-knowledge-graph)
        - [core.lkg.yml](#corelkgyml)
        - [json/core.lkg.json](#jsoncorelkgjson)
    - [Vocabulary Knowledge Graph](#vocabulary-knowledge-graph)
        - [core.vkg.yml](#corevkgyml)
        - [json/core.vkg.json](#jsoncorevkgjson)
    - [JSON Schema](#json-schema)
        - [Latin](#latin)
        - [Other natural languages](#other-natural-languages)
    - [HXLTM](#hxltm)
- [Exchange Codes and terms](#exchange-codes-and-terms)
    - [Prebuild tables](#prebuild-tables)
        - [Common Operational Datasets](#common-operational-datasets)
        - [Gender/Sex codes](#gendersex-codes)
        - [HXL](#hxl)
        - [Human Anatomy](#human-anatomy)
        - [Language codes](#language-codes)
        - [Location codes](#location-codes)
            - [Location codes at adm0](#location-codes-at-adm0)
            - [Location at adm1, adm2, adm3, adm4, adm5](#location-at-adm1-adm2-adm3-adm4-adm5)
        - [Numbers (draft)](#numbers-draft)
        - [Writting system codes](#writting-system-codes)
    - [ISO](#iso)
        - [ISO 639-3](#iso-639-3)
        - [ISO 3166](#iso-3166)
            - [ISO 3166 country/territory codes](#iso-3166-countryterritory-codes)
        - [ISO 15924](#iso-15924)
- [URN resolver](#urn-resolver)
    - [The `URN:DATA` specification (early draft)](#the-urndata-specification-early-draft)
    - [Default values for the `urnresolver`](#default-values-for-the-urnresolver)
- [Platform dependent ontologies](#platform-dependent-ontologies)
    - [Python Data classes](#python-data-classes)
    - [Other programming languages](#other-programming-languages)
- [To Do's](#to-dos)

<!-- /TOC -->

---

## Knowledge Graph and JSON Schemas

> [Knowledge graph on Wikipedia](https://en.wikipedia.org/wiki/Knowledge_graph)

Note: contents of [ontologia/json/](ontologia/json/) are generated
from ontologia/ *.yml files with exception of
`ontologia/hdp.json-schema.json` that is not _yet_ automated

### Localization Knowledge Graph

#### core.lkg.yml
- [core.lkg.yml](core.lkg.yml)

#### json/core.lkg.json
- [json/core.lkg.json](json/core.lkg.json)

```bash
# Generate ontologia/json/core.vkg.json
yq < ontologia/core.vkg.yml > ontologia/json/core.vkg.json
```

### Vocabulary Knowledge Graph
#### core.vkg.yml
- [core.vkg.yml](core.vkg.yml)

#### json/core.vkg.json

- [json/core.vkg.json](json/core.vkg.json)

```bash
# Generate ontologia/json/core.lkg.json
yq < ontologia/core.lkg.yml > ontologia/json/core.lkg.json
```

### JSON Schema

> - [JSON Schema Specification](https://json-schema.org/specification.html)
> - Using JSON Schemas to validate/help create HDP files
>    - [VSCode YAML extension](https://github.com/redhat-developer/vscode-yaml)
>    - _Note: other code editors are likely to have equivalent alternatives_


#### Latin

- [hdp.json-schema.json](hdp.json-schema.json)

#### Other natural languages

> TODO: explain more about it  (Emerson Rocha, 2021-03 09:46 UTC)

### HXLTM

- <https://hdp.etica.ai/#HXLTM>
- Ontologia:
  - YAML: [cor.hxltm.yml](cor.hxltm.yml)
  - JSON: [json/cor.hxltm.json](json/cor.hxltm.json)

## Exchange Codes and terms

### Prebuild tables

#### Common Operational Datasets

- [cod/](cod/)

[![](http://img.youtube.com/vi/CFUs8S0MPIY/0.jpg)](http://www.youtube.com/watch?v=CFUs8S0MPIY "Common Operational Datasets (CODs)")

#### Gender/Sex codes

- [codicem/sexum/](codicem/sexum/)

#### HXL

- [codicem/hxl/](codicem/hxl/)

#### Human Anatomy

- [codicem/anatomiam/](codicem/anatomiam/)

#### Language codes

- [codicem/codicem.linguam.hxl.csv](codicem/codicem.linguam.hxl.csv)
- [HXL-CPLP/forum#38: HXL-CPLP-Vocab_Linguam (ISO 639-3 et al)](https://github.com/HXL-CPLP/forum/issues/38)

> TODO: add also the macrolanguages mapping https://iso639-3.sil.org/sites/iso639-3/files/downloads/iso-639-3-macrolanguages.tab

<!--

From [https://iso639-3.sil.org/code_tables/download_tables](https://iso639-3.sil.org/code_tables/download_tables):

```sql
CREATE TABLE [ISO_639-3] (
         Id      char(3) NOT NULL,  -- The three-letter 639-3 identifier
         Part2B  char(3) NULL,      -- Equivalent 639-2 identifier of the bibliographic applications 
                                    -- code set, if there is one
         Part2T  char(3) NULL,      -- Equivalent 639-2 identifier of the terminology applications code 
                                    -- set, if there is one
         Part1   char(2) NULL,      -- Equivalent 639-1 identifier, if there is one    
         Scope   char(1) NOT NULL,  -- I(ndividual), M(acrolanguage), S(pecial)
         Type    char(1) NOT NULL,  -- A(ncient), C(onstructed),  
                                    -- E(xtinct), H(istorical), L(iving), S(pecial)
         Ref_Name   varchar(150) NOT NULL,   -- Reference language name 
         Comment    varchar(150) NULL)       -- Comment relating to one or more of the columns
```
-->

#### Location codes

##### Location codes at adm0

- [codicem/codicem.locum.hxl.csv](codicem/codicem.locum.hxl.csv)

##### Location at adm1, adm2, adm3, adm4, adm5

> TODO: we should both explain how to obtain these without use HDPLisp (Emerson Rocha, 2021-04-13 22:28 UTC)

#### Numbers (draft)

- [codicem/codicem.numerum.hxl.csv](codicem/codicem.numerum.hxl.csv)
- [HXL-CPLP/forum#38: HXL-CPLP-Vocab_Numerum](https://github.com/HXL-CPLP/forum/issues/53)


#### Writting system codes

- [codicem/codicem.scriptum.hxl.csv](codicem/codicem.scriptum.hxl.csv)
- [HXL-CPLP/forum#54: HXL-CPLP-Vocab_Scriptum (ISO 15924 et al)](https://github.com/HXL-CPLP/forum/issues/54)


### ISO

The files on `ontologia/iso` contain symlinks to generated resources that are
based on then already [HXLated](https://hxlstandard.org/).

#### ISO 639-3
- Cached local file: [iso/iso.639-3.hxl.csv](iso/iso.639-3.hxl.csv)
- Official/Recommended source from ISO organization:
  - Search site: <https://iso639-3.sil.org/>
  - Download tables: <https://iso639-3.sil.org/code_tables/download_tables>

#### ISO 3166

> TODO: work around how to get at least some subdivisions (Emerson Rocha, 2021-04-13 23:55 UTC)

##### ISO 3166 country/territory codes

- Cached local file: [iso/iso.3166.hxl.csv](iso/iso.3166.hxl.csv)
- Official/Recommended source from ISO organization:
  - `¯\_(ツ)_/¯`
- Alternatives to official/recommended source:
  - Wikipedia: <https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes>
  - UN OCHA: <https://vocabulary.unocha.org/>

<!--
- https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
-->

#### ISO 15924
- Cached local file: [iso/iso.15924.hxl.csv](iso/iso.15924.hxl.csv)
- Live Updated version from HXL-Proxy
  - [Preview](https://proxy.hxlstandard.org/data?dest=data_edit&filter01=select&filter-label01=%23vocab%2Bcode%2Bv_iso15924%2Bnumber+not+empty&select-query01-01=%23vocab%2Bcode%2Bv_iso15924%2Bnumber%3E0&strip-headers=on&tagger-match-all=on&tagger-01-header=%23+code&tagger-01-tag=%23vocab%2Bcode%2Bv_iso15924%2Btext&tagger-02-header=ndeg&tagger-02-tag=%23vocab%2Bcode%2Bv_iso15924%2Bnumber&tagger-03-header=english+name&tagger-03-tag=%23vocab%2Bname%2Bi_eng&tagger-04-header=nom+francais&tagger-04-tag=%23vocab%2Bname%2Bi_fra&tagger-05-header=pva&tagger-05-tag=%23meta%2Bproperty_value_aliases&tagger-06-header=unicode+version&tagger-06-tag=%23meta%2Bunicode_version&tagger-07-header=date&tagger-07-tag=%23date&header-row=5&url=https%3A%2F%2Funicode.org%2Fiso15924%2Fiso15924.txt)
  - [CSV download](https://proxy.hxlstandard.org/data.csv?dest=data_edit&filter01=select&filter-label01=%23vocab%2Bcode%2Bv_iso15924%2Bnumber+not+empty&select-query01-01=%23vocab%2Bcode%2Bv_iso15924%2Bnumber%3E0&strip-headers=on&tagger-match-all=on&tagger-01-header=%23+code&tagger-01-tag=%23vocab%2Bcode%2Bv_iso15924%2Btext&tagger-02-header=ndeg&tagger-02-tag=%23vocab%2Bcode%2Bv_iso15924%2Bnumber&tagger-03-header=english+name&tagger-03-tag=%23vocab%2Bname%2Bi_eng&tagger-04-header=nom+francais&tagger-04-tag=%23vocab%2Bname%2Bi_fra&tagger-05-header=pva&tagger-05-tag=%23meta%2Bproperty_value_aliases&tagger-06-header=unicode+version&tagger-06-tag=%23meta%2Bunicode_version&tagger-07-header=date&tagger-07-tag=%23date&header-row=5&url=https%3A%2F%2Funicode.org%2Fiso15924%2Fiso15924.txt)
- Official/Recommended source from ISO organization:
  - Home page: https://unicode.org/iso15924/
  - Search online: https://unicode.org/iso15924/iso15924-codes.html
  - Changes: https://unicode.org/iso15924/codechanges.html
  - Download: https://unicode.org/iso15924/iso15924.txt
  - Download: https://www.unicode.org/Public/UCD/latest/ucd/PropertyValueAliases.txt
- Alternatives to official/recommended source:
  - Wikipedia: https://en.wikipedia.org/wiki/ISO_15924

<!--
#ISO 15924
#vocab+code+v_iso15924+text
#vocab+code+v_iso15924+number
#vocab+name+i_eng
#vocab+name+i_fra
#meta+property_value_aliases
#meta+unicode_version
#date

#vocab+id+v_iso6393_3letter,#vocab+code+v_iso3692_3letter+z_bibliographic,#vocab+code+v_iso3692_3letter+z_terminology,#vocab+code+v_iso6391,#status,#vocab+type,#vocab+name,#description+comment+i_en

-->

## URN resolver

### The `URN:DATA` specification (early draft)

- [../urn-data-specification/README.md](../urn-data-specification/README.md)


### Default values for the `urnresolver`

- [urn/defallo.urn.yml](urn/defallo.urn.yml)

When the command line util `urnresolver` does not have a user customized
specified file, this is the loaded file.

## Platform dependent ontologies

### Python Data classes

- [ontologia/python](python)

**Protip: even if you are not a python programmer, but is debugging some HXLm
implementation (or want to undestand more how the objects are related) this
folder can help you.** This also means that feedback from advanced users that
know other programming languages but do not know python could still be done
focusing on this folder

While not as portable, the contents of this uses an specialized Python type of
class called [dataclasses](https://docs.python.org/3/library/dataclasses.html).
The non-buzzword meaning of this is the code on this folder is (or should be)
more an representation on how data objects are manipulated, instead of being
classes that actually change behavior. _In theory_ they should more simple
to port to other programming languages.

### Other programming languages

- See also
  - [tests/transpile-python-to-javascript.sh](tests/transpile-python-to-javascript.sh)

> Note: at the moment (2021-04-01) there is no interest to implement
  non-portable underlining classes (at least form HXLm.core.HPD) on other
  languages like the HXL Standard (see
  [https://github.com/HXLStandard](https://github.com/HXLStandard) and
  [https://hxlstandard.org/developer-documentation/](https://hxlstandard.org/developer-documentation/)).

> Recommendation: if over the years do exist interest in porting some features,
  one good approach would be use the part of the ontologies that are platform
  independent. Also different implementations would have different approaches
  and minimal viable products could work faster without need to implement a
  more object oriented approach.

## To Do's

While the idea behind the hxlm.core project is output production-ready
toolchains (and, to make easier for localization, the number of core keywords
and how they are used is keep as as minimalist as possible) do already exist
other works, like the Perl Lingua::Romana::Perligata, that can at least help
with usages for internal terms in Latin.

- https://en.wikipedia.org/wiki/Non-English-based_programming_languages
  - This page have a lot of reference on non-english keyworkd based
    programming languages
- This one from Latin is very, very complex.
  - https://metacpan.org/pod/distribution/Lingua-Romana-Perligata/lib/Lingua/Romana/Perligata.pm
  - https://metacpan.org/source/DCONWAY/Lingua-Romana-Perligata-0.602/lib%2FLingua%2FRomana%2FPerligata.pm
