#lang racket
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

(provide salve-mundi)

;; - lat
;;   - https://iso639-3.sil.org/code/lat
;;   - https://en.wikipedia.org/wiki/ISO_639-3
;; - Latn
;;   - https://en.wikipedia.org/wiki/ISO_15924
;;   - https://en.wikipedia.org/wiki/Latin_alphabet

(define salve-mundi (list-ref '("Heus!" "Salve!" "Ave!") (random 3)))