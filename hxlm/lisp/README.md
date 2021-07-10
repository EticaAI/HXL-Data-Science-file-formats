# hxlm.lisp

> **NOTICE**: `hxlm.lisp` is not production-ready (and may explicitly
  designed to be as usage **outside** hxlm.*, even is acceptable stable).
  Most documentation here would be either for internal usage and to aid
  maintainers or external implementers trying to do low level implementations.
  (Emerson Rocha, 2021-03-31 17:26 UTC)
  
> **Suggestion** Even if eventually do exist interest to parse
  [S-expressions](https://en.wikipedia.org/wiki/S-expression) produced by any
  implementation, you could still use any Lisp-like interpreter of your
  preferred programming language. To simplify your work, just restrict the
  natural language.


## Internal notes

- hdp-conventions
  - [hdp-conventions/README.md](hdp-conventions/README.md)
  - Some characters used on HDP with YAML are likely to be inspired if the
    YAML/JSON would be transposed to raw Lisp/Scheme-like dialects
- About characters
  - https://docs.racket-lang.org/reference/reader.html
  - Racket allows use `[]` and `{}`, not just `()`. Good to know. Hummm...
- Lisp bootstrapper in assembly (only ~3500 lines of code)
  - https://github.com/oriansj/stage0/blob/master/stage2/lisp.s
  - _Note to self: so definitely a parser with high level bootstrapper
    language like Python is viable with S-expression syntax compared to
    others, which make s-expressions a good intermediate language to not
    require users to write directly on python or other programming
    languages on HDP files! (Emerson Rocha, 2021-03-31 17:43 UTC)_