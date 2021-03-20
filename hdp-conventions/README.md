# HDP Declarative Programming conventions, early draft

**This is an draft. See <https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/16>.**

---

> Trivia:
> - HDP naming:
>   - **HDP = _'HDP Declarative Programming'_ is the default name.**
>     - When in doubt (or you or your tools can't detect intent of use in immediate context) this is a good way to call it. See Wikipedia for [Declarative programming](https://en.wikipedia.org/wiki/Declarative_programming) and [Recursive acronym](https://en.wikipedia.org/wiki/Recursive_acronym)
>   - **HDP = _'Humanitarian Declarative Programming'_** could be one way to call when the intent of the moment is **strictly humanitarian.**
>     - The definition of humanitarian is out of scope.

---

<!-- TOC depthFrom:2 -->

- [High level goals](#high-level-goals)
- [Conteiner format](#conteiner-format)
    - [Exchange of commands with foreign interface](#exchange-of-commands-with-foreign-interface)
    - [Conventions for identifiers (key names)](#conventions-for-identifiers-key-names)
        - [Tokens meaning on keys](#tokens-meaning-on-keys)

<!-- /TOC -->

---


## High level goals

> TODO: draft this

<!-- 1. The highest end goal of HDP is ... -->


## Conteiner format

1. The preferred container format is YAML (https://yaml.org/)
    1. Platforms specific features, like the functionality of loading native
       directly in HDP tools:
        1. Should be ignored in existing YAML files
        2. Should NOT be exported with HDP+YAML format, even if well behaved
           HDP+YAML parsers would likely to ignore.
2. JSON, in special for compatibility with other tools or for
   machine-to-machine HDP exchange or for specific low level calls, can be
   used as additional conteiner format.

### Exchange of commands with foreign interface

1. The recommended way of exposing HDP functionality to low level data
  processing that **already not native on HDP** is both exporting and
  accepting JSON format, without the full semantics of HDP (like
  translations of vocabulary)
    1. [INFORMATIONAL] Ansible uses JSON for data exchange of plugins.

### Conventions for identifiers (key names)

#### Tokens meaning on keys

```yaml
# Quick example 1
- hsilo:           # hsilo is an verb, without additional tokens
    linguam: LAT   # linguam is also an verb, LAT is an value

```

- **HDP internationalized vocab**: No token
  - Description:
    - No token means an word that is perfectly valid HDP vocab that should be
      able to be translated to EVERY know natural language enabled by
      as it is.
  - Examples:
    - `hsilo`<sup>LAT</sup>, `silo` <sup>ENG/SPA/LAT/POR</sup>
    - `linguam`<sup>LAT</sup>, `language` <sup>ENG</sup>, `язык` <sup>RUS</sup>
- **HDP internationalized vocab with metadata**: `[` <sup>prefix</sup>,
  `[[` <sup>prefix</sup> , `]` <sup>suffix</sup>, `]]` <sup>suffix</sup>
  - Description:
    - TODO
  - Examples:
    - TODO
  - Notes:
    - Reserved undocumented token.
- **Digitaly signed vocab**: `{` <sup>prefix</sup>, `{{` <sup>prefix</sup> ,
  `}` <sup>suffix</sup>, `}}` <sup>suffix</sup>
  - Description:
    - Token to explicitly mention that the content of this key are digitally
      signed
    - Removing the [`{`, `{{`, `}}`, `}`], the resulting term must be
      perfectly valid HDP vocab that should be able to be translated to EVERY
      know natural language enabled by as it is.
  - Notes:
    - For sake of simplicity, if an upper key already is digitally signed,
      interfaces do not need to show these tokens **if all contents**, with
      exception of [`<`, `<<`, `>>`, `>>`], are signed.
    - When tokes [`(`, `((`, `)`, `))`] are present, the explicit use of this
      token us not yet defined, since this meas that an outisde program
      also need to be evaluated.
      - Maybe this with [`(!(` term-here `))`] this notation could be good
        enough?
- **Eval**: `(` <sup>prefix</sup>, `((` <sup>prefix</sup> , `)` <sup>suffix</sup>,
  `))` <sup>suffix</sup>
  - Examples:
    - `{{hsilo}}`
  - Notes:
    - Reserved undocumented token.
- **Comment:** `<` <sup>prefix</sup>, `<<` <sup>prefix</sup> ,
  `>` <sup>suffix</sup>, `>>` <sup>suffix</sup>
  - Description:
    - This key can be used as comment
    - Do not evaluate. Can be safely ignored contents. Do not try to guess
      the core mesage
  - Examples:
     - `<<COMMENT>>`, `<ENG<COMMENT>>`, `<POR<COMENTARIO>>`

<!--
      - [`(`, `((`, `)`, `))`] are not recommended for generic comments
-->