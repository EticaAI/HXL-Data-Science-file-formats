#lang racket

(provide salve-mundi)

;; - mis
;;   - https://en.wikipedia.org/wiki/ISO_639-3
;;   - https://iso639-3.sil.org/code/mis
;; - Zsye
;;   - https://en.wikipedia.org/wiki/ISO_15924
;;   - https://en.wikipedia.org/wiki/Emoji

;; https://emojipedia.org/waving-hand/
(define salve-mundi (list-ref '("👋" "👋🏻" "👋🏼" "👋🏽" "👋🏾" "👋🏿") (random 6)))
