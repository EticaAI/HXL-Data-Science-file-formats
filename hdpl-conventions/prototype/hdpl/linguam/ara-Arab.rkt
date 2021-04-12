#lang racket
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

(provide salve-mundi)

;; - ara
;;   - https://en.wikipedia.org/wiki/ISO_639-3
;;   - https://iso639-3.sil.org/code/ara
;; - Arab
;;   - https://en.wikipedia.org/wiki/ISO_15924
;;   - https://en.wikipedia.org/wiki/Arabic_script

(define salve-mundi (list-ref '("مرحبا!" "مهلا!") (random 2)))