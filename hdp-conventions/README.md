# HDP Declarative Programming conventions, early draft

**This is an draft. See <https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/16>.

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

> TODO: