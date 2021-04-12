#lang racket

(provide salve-mundi)

;; - ara
;;   - https://en.wikipedia.org/wiki/ISO_639-3
;;   - https://iso639-3.sil.org/code/ara
;; - Arab
;;   - https://en.wikipedia.org/wiki/ISO_15924
;;   - https://en.wikipedia.org/wiki/Arabic_script

(define salve-mundi (list-ref '("مرحبا!" "مهلا!") (random 2)))