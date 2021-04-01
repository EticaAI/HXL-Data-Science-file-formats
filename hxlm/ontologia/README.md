# The heart of the HXLm ongologies

When feasible, even if it make harder to do initial implementation or be
_a bit less efficient_ than use dedicated _"advanced"_ strategies with
state of the art tools, the internal parts of hxlm.core that deal with
[ontology](https://en.wikipedia.org/wiki/Ontology_(information_science)) will
be stored in this folder.

This strategy is likely to make it easier for non-developers to update
internals, like individuals interested in adding new languages or proposing
corrections.

## Knowledge Graph

> [Knowledge graph on Wikipedia](https://en.wikipedia.org/wiki/Knowledge_graph)

### Localization Knowledge Graph
- [core.lkg.yml](core.lkg.yml)

### Vocabulary Knowledge Graph
- [core.vkg.yml](core.vkg.yml)

## JSON Schema

> - [JSON Schema Specification](https://json-schema.org/specification.html)
> - Using JSON Schemas to validate/help create HDP files
>    - [VSCode YAML extension](https://github.com/redhat-developer/vscode-yaml)
>    - _Note: other code editors are likely to have equivalent alternatives_


### Latin

- [hdp.json-schema.json](hdp.json-schema.json)

### Other languages

> TODO: explain more about it  (Emerson Rocha, 2021-03 09:46 UTC)

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