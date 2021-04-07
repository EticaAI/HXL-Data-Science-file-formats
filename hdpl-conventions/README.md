# HDPLisp conventions

> Note: what is called "HDP Lisp" is an very early draft and is strongly based
  on how potential strategy to make implementation of the high level HDP (see
  [../hdp-conventions/README.md](../hdp-conventions/README.md)), that is mostly
  an DSL (Domain Specific Language) written in YAML, be feasible and portable
  across different systems **and, even if at more primitive level (like base
  verbs), be translatable**. The final name (if this go beyond early
  prototypes) may be different to avoid confusion.

## High level goals

- **Internationalization and localization as core feature**
  - https://www.w3.org/International/questions/qa-i18n
  - https://en.wikipedia.org/wiki/Internationalization_and_localization
- With exception of characters that have no past cultural meaning (like 
  `()`, `[]`, `{}`, `,`, `/\`, `$`, `!?%#` ...) allow localizations use any
  writting system to represent verbs.
  - In other words: some subset of terms may be need to _boostrap_ HDPLisp, and
    this may be need be done in ASCII Latin characters, but after that,
    developers provinding extensions to HDP may not need to work with other
    writting systems except for debugging or integrity check (e.g. see if hashs
    match).
- (...)

### (draft) Implementation decisions
- **Syntax of HDPLisp**
  - (TODO)


> To document, cite and/or remove this draft:
> - https://clojure.org/reference/lisps