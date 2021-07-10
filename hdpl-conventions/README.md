# HDPLisp conventions (early draft)

---
<!-- TOC -->

- [HDPLisp conventions (early draft)](#hdplisp-conventions-early-draft)
    - [High level goals](#high-level-goals)
        - [Internationalization and localization as core feature](#internationalization-and-localization-as-core-feature)
        - [Internationalized auditability core feature](#internationalized-auditability-core-feature)
        - [Cultural neutrality as core feature](#cultural-neutrality-as-core-feature)
        - [(draft) Implementation decisions](#draft-implementation-decisions)
- [Implementation reference](#implementation-reference)
    - [Proofs of Concept](#proofs-of-concept)
    - [prototype](#prototype)
- [IDEs support](#ides-support)
        - [HDPLisp with .rkt extension on DrRacket](#hdplisp-with-rkt-extension-on-drracket)
        - [HDPLisp with .rkt extension on VSCode](#hdplisp-with-rkt-extension-on-vscode)
        - [magic-racket](#magic-racket)
            - [Workarounds](#workarounds)

<!-- /TOC -->

---


Compared to other Lisps, the HDPLisp is more likely to be an interpreted Lisp
that is focused and able to be converted from natural languages and then
be executed either on platforms that process HPD files. This is why the
average environment that could be HDPLisp compliant does not be
_optimized for speed_(*), but for translation with 100% equivalence.

If you hear sayings like "Lisp is a Programmable Programming Language" HDPLisp
already ships with knowledge graphs that put all the effort of equivalence
between natural languages on files that could be updated by non programmers.
**In fact, what is called "HDP Lisp" is an very early draft and is strongly
based on how potential strategy to make implementation of the high level HDP
(see [../hdp-conventions/README.md](../hdp-conventions/README.md))**. So it may
actually be easier build this approach to not make HDP implementations too
focused on an unterlining platform, like Python and still allow auditability.

_(*): If raw speed is important, that would be better done using HDPLisp for
stage of import/export from other natural languages to a more traditional
enviroment like Lisp/Scheme/Racket/Clojure._

## High level goals

> High level goals still early draft

### Internationalization and localization as core feature

- General concept:
  - https://www.w3.org/International/questions/qa-i18n
  - https://en.wikipedia.org/wiki/Internationalization_and_localization
- HDPLisp aware tools must let most localized verbs in formats (like YAML)
  that could allow individuals without any need of underlining
  implementations. It must also allow upgradability of "wrong" translations
  (like allow synonyms when reading old files) but in such cases it just
  has a canonical term when generating a new one from other languages since
  it's important anyone from other regions be able to generate versions at
  any time.
- Problems that affect HDPLisp bootstrapping, quality of review/debug by
  non-native speakers or daily usage of potential contributors from target
  languages are considered a core problem. It means either restrict core
  features for every other natural language (since some would be in
  disvantage) or as strong moral recommendation for any user of HDPLisp
  take as equally Important
  - As 2021-04-07, non-Latin writing systems, in special Right-To-Left
    scripts, while do exist support for decades on Unicode and most
    Operational systems may just need extra fonts, some common used tools
    and platforms, like GitHub and Visual Studio Code, have serious
    usability issues already reported by non-humanitarian developers.
  - Early adopters, in special from regions outside of the main usage of
    these languages, are encouraged to not depend on the ability of users of
    target language also know other natural languages and
    **complaint direct to such organizations in special if you already work
    on humanitarian area of make use of such tool for life and death
    situations**. The HDPLisp + HXLm try it's best to be flexible (like
    allow upgrade on vocabularies by request) but these usability issues
    are not taking serious enough.

### Internationalized auditability core feature

> Context: most of this feature is relevant if HDPLisp be used as
  plugin/extension for HDP files;  while HDP is expected to abstract access
  to datasets, one complex usage is deal with a task is authorized or not
  based on context without (both for who create/review HDP / HDPLisp) allow
  access to real data. **Usages outside of this context (like complex
  individual programs) are unlikely to optimized**

- Assuming being viable have an baseline way to convert HDPLisp (like already
  do proofs of concepts with HDP) between human natural languages, this
  means that even an military grade signed file code in an an complete
  different natural language could be audited by someone from a completely
  different region.
  - At bare minimum, both verbs described to construct a Turing-complete
    Lisp plus all representations of some vocabularies (like representation
    `true`, `false`, `nil`/`None`, `null`, numbers, keys to represent
    counties or UN P-Codes, etc) are granted to be 100% granted to be
      translatable.
  - Please note that if it is already hard for people to agree with
    individual verbs, **name of functions** (not so much the internals)
    would never be unanimous. This doesn't mean that HDPLisp must be so
    minimalist to a point of not being usable! But when user functions
    may be exported as part of something bigger, to not enforce cultural bias
    even on function names, they may need to be exported either as raw value
    or by long hash.
    - In theory, to improve user experience, either who could port function
      from other Lisps dialects or have support from either students or
      University professors to build localized versions (with documentation,
      well planned localized name, etc; **note that Lisp/Scheme/Racket are
      very popular on courses to teach students, so this is relevant** ) and
      have these functions on local disk (something that would be required
      anyway for aid autocomplete of user functions), instead of HDPLisp
      aware tools show ugly hash, could show the reference of the know
      function on disk.

### Cultural neutrality as core feature

- **A localized version of HDPL must be able to allow ANY writing system (e.g.
  letters, even number, to represent verbs.** And, this is important, **adding
  a new localized version (e.g. an [ISO 639-3](https://iso639-3.sil.org/)
  plus [ISO 15924](https://en.wikipedia.org/wiki/ISO_15924)) MUST be as easier
  as change some human friendly text file** without need of programming
  knowledge.
  - The syntax can use printable computer characters like `()`, `[]`, `{}`,
    `,`, `/\`, `$`, `!?%#` and/or others to make work of tool implementers
    easier.
    - Note that localized versions to be called `HDPLisp` could be
      required to at least support a subset of all characters.


### (draft) Implementation decisions
- **Syntax of HDPLisp**
  - (TODO)

> To document, cite and/or remove this draft:
> - https://clojure.org/reference/lisps


# Implementation reference

## Proofs of Concept

- [proof-of-concept/](proof-of-concept/)

## prototype
- [prototype/](prototype/)

# IDEs support

### HDPLisp with .rkt extension on DrRacket
It works.

### HDPLisp with .rkt extension on VSCode

### magic-racket

- <https://github.com/Eugleo/magic-racket/>
- <https://marketplace.visualstudio.com/items?itemName=evzen-wybitul.magic-racket>

#### Workarounds
> Note to self: Follow this topic <https://github.com/Eugleo/magic-racket/issues/13>
  Since we're using S-expressions, it should be possible
  (Emerson Rocha, 2021-04-12 23:40 UTC)

The Eugleo/magic-racket works for Racket files using `#lang racket`, but we're
starting to use `#lang hdpl/linguam/lat-Latn` et al.

One way to temporary disable is with `"magic-racket.lsp.enabled": false` on
VSCode configurations.
