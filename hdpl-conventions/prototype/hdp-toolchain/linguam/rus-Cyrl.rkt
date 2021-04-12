#lang racket

(provide salve-mundi)

;; - rus
;;   - https://en.wikipedia.org/wiki/ISO_639-3
;;   - https://iso639-3.sil.org/code/rus
;; - Cyrl
;;   - https://en.wikipedia.org/wiki/ISO_15924
;;   - https://en.wikipedia.org/wiki/Cyrillic_script
;;   - https://en.wikipedia.org/wiki/Cyrillic_alphabets

(define salve-mundi (list-ref '("Ну!" "Эй!" "Привет!") (random 3)))