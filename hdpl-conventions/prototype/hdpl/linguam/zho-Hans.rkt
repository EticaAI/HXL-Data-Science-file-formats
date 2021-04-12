#lang racket
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

(provide salve-mundi)

;; - zho
;;   - https://en.wikipedia.org/wiki/ISO_639-3
;;   - https://iso639-3.sil.org/code/zho
;; - Hans
;;   - https://en.wikipedia.org/wiki/ISO_15924
;;   - https://en.wikipedia.org/wiki/Simplified_Chinese_characters


(define salve-mundi (list-ref '("喂!" "你好！") (random 2)))