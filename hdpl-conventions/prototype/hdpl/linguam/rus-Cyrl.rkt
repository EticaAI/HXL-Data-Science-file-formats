#lang racket
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

(provide salve-mundi)

;; - rus
;;   - https://en.wikipedia.org/wiki/ISO_639-3
;;   - https://iso639-3.sil.org/code/rus
;; - Cyrl
;;   - https://en.wikipedia.org/wiki/ISO_15924
;;   - https://en.wikipedia.org/wiki/Cyrillic_script
;;   - https://en.wikipedia.org/wiki/Cyrillic_alphabets

(define salve-mundi (list-ref '("Ну!" "Эй!" "Привет!") (random 3)))