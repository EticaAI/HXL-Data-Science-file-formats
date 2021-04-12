#lang racket
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

(provide salve-mundi)

;; - mis
;;   - https://en.wikipedia.org/wiki/ISO_639-3
;;   - https://iso639-3.sil.org/code/mis
;; - Zsye
;;   - https://en.wikipedia.org/wiki/ISO_15924
;;   - https://en.wikipedia.org/wiki/Mathematical_notation

; https://emojipedia.org/waving-hand/
; (define salve-mundi (list-ref '("+" "-") (random 2)))

(define salve-mundi (list-ref '("+" "-") (random 2)))
