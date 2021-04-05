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
            - [The `<< >>`, `<<! !>>`, , `<<!! !!>>`, , `<<!!! !!!>>`](#the----------)
- [Collaborative work](#collaborative-work)
- [Security considerations](#security-considerations)

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

Note: Remove `\` from `\{\{` and `\}\}` if this document is renderized with
them.

- **HDP internationalized vocab**: No token
  - Description:
    - No token means an word that is perfectly valid HDP vocab that should be
      able to be translated to EVERY know natural language enabled by
      as it is.
  - Examples:
    - `hsilo`<sub><em>linguam: LAT</em></sub>
      - `silo`<sub><em>linguam: ENG|SPA|LAT|POR</em></sub>
    - `linguam`<sub><em>linguam: LAT</em></sub>
      - `language` <sub><em>linguam: ENG</em></sub>
      - `язык`<sub><em>linguam: RUS</em></sub>
- **HDP internationalized vocab with metadata**: `[` <sup>prefix</sup>,
  `[[` <sup>prefix</sup> , `]` <sup>suffix</sup>, `]]` <sup>suffix</sup>
  - Description:
    - TODO
  - Examples:
    - TODO
  - Notes:
    - Reserved undocumented token.
- **HDP vocab with digitaly signed values**: `{` <sup>prefix</sup>,
  `\{\{` <sup>prefix</sup> , `}` <sup>suffix</sup>, `\}\}` <sup>suffix</sup>
  - Description:
    - Token to explicitly mention that the content of this key are digitally
      signed
    - Removing the [`{`, `\{\{`, `\}\}`, `}`], the resulting term must be
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
  - Examples:
    - `\{\{datum\}\}`<sub><em>linguam: LAT</em></sub> <sup>contents digitally
      signed and recently verified</sup>
    - `{?{datum}?}`<sub><em>linguam: LAT</em></sub> <sup>contents digitally
      signed, but not verified yet or this computer can't do automated
      verification</sup>
    - `{!!!{datum}!!!}`<sub><em>linguam: LAT</em></sub> <sup>contents
      digitally signed, but with 1) error, 2) explicitly untrusted or 3) this
      environment do not tolerate `{?{datum}?}`</sup>
- **Eval**: `(` <sup>prefix</sup>, `((` <sup>prefix</sup> , `)` <sup>suffix</sup>,
  `))` <sup>suffix</sup>
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

##### The `<< >>`, `<<! !>>`, , `<<!! !!>>`, , `<<!!! !!!>>`

> Draft from v0.8.3

- `<< >>`,  `<(.*)<  >(.*)>`
  - For sake of convention, we could use this more for user-related comments
  - the _(.*)_ means that something can be put betwen `<<`/`>>`, like
    `<POR<Meu comentário aqui em Português>>`
- `<<! !>>`
  - When processing HDP files, internal functions often need to pass
    information that is essential for functionality (or at least to speed
    up). This extra ! could be used for this type of internal comment
    - Maybe we could allow user expose this with 'verbose' parameters?
- `<<!! !!>>`, `<<!!! !!!>>`
  - Similar to `<<! !>>`, but for higher level of information that is not
    necessary for end user, but may be for who would work with the library
    - Maybe we could allow user expose this with 'debug' parameters?

> Issue: `!` character is sometimes used to mean 'encrypted', so maybe we
  should choose another character

<!--
      - [`(`, `((`, `)`, `))`] are not recommended for generic comments
-->

## Collaborative work

See [collaborative-work.md](collaborative-work.md)

## Security considerations

See [security-considerations.md](security-considerations.md)

<!--

Software internal error messages could use "math language"; They are not good
for end user (even for the HDP specification itself) but for internal software
exceptions it could at least be somewhat based

- https://www.rapidtables.com/math/symbols/Logic_Symbols.html


Error messages symbols using math:
  - '∀' ∀(x)
    - "given any" or "for all"
    - https://en.wikipedia.org/wiki/Universal_quantification
  - '∃' ∃(x)
    - "there exists", "there is at least one"
    - https://en.wikipedia.org/wiki/Existential_quantification
  - Etc
    - https://en.wikipedia.org/wiki/List_of_logic_symbols
    - https://en.wikipedia.org/wiki/Mathematical_operators_and_symbols_in_Unicode

-->