#lang racket

(provide salve-mundi)

;; - zho
;;   - https://en.wikipedia.org/wiki/ISO_639-3
;;   - https://iso639-3.sil.org/code/zho
;; - Hans
;;   - https://en.wikipedia.org/wiki/ISO_15924
;;   - https://en.wikipedia.org/wiki/Simplified_Chinese_characters


(define salve-mundi (list-ref '("喂!" "你好！") (random 2)))