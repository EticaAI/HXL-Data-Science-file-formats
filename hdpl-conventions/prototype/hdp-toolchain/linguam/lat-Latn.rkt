#lang racket

(provide salve-mundi)

;; - lat
;;   - https://iso639-3.sil.org/code/lat
;;   - https://en.wikipedia.org/wiki/ISO_639-3
;; - Latn
;;   - https://en.wikipedia.org/wiki/ISO_15924
;;   - https://en.wikipedia.org/wiki/Latin_alphabet

(define salve-mundi (list-ref '("Heus!" "Salve!" "Ave!") (random 3)))