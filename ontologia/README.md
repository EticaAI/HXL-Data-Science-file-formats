# The heart of the HXLm ontologies

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

- [Knowledge Graph](#knowledge-graph)
    - [Localization Knowledge Graph](#localization-knowledge-graph)
        - [core.lkg.yml](#corelkgyml)
        - [json/core.lkg.json](#jsoncorelkgjson)
    - [Vocabulary Knowledge Graph](#vocabulary-knowledge-graph)
        - [core.vkg.yml](#corevkgyml)
        - [json/core.vkg.json](#jsoncorevkgjson)
- [JSON Schema](#json-schema)
    - [Latin](#latin)
    - [Other natural languages](#other-natural-languages)
- [Platform dependent ontologies](#platform-dependent-ontologies)
    - [Python Data classes](#python-data-classes)
    - [Other programming languages](#other-programming-languages)
- [To Do's](#to-dos)

<!-- /TOC -->

---

## Knowledge Graph

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

## JSON Schema

> - [JSON Schema Specification](https://json-schema.org/specification.html)
> - Using JSON Schemas to validate/help create HDP files
>    - [VSCode YAML extension](https://github.com/redhat-developer/vscode-yaml)
>    - _Note: other code editors are likely to have equivalent alternatives_


### Latin

- [hdp.json-schema.json](hdp.json-schema.json)

### Other natural languages

> TODO: explain more about it  (Emerson Rocha, 2021-03 09:46 UTC)

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