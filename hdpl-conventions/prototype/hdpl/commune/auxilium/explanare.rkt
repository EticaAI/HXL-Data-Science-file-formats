#lang racket
;; NOTE: this file is just a group of examples of how to debug internal racket structures.
;;       it's not really intented to be used as part of the library
;; - "explanare":
;;   - explano: https://en.wiktionary.org/wiki/explano#Latin
;;   - explanare: https://en.wiktionary.org/wiki/explanare#Latin
;; - "auxilium":
;;   - https://en.wiktionary.org/wiki/auxilium

; (require hdpl/commune/structuram)
(require csv-reading)


;; Print each line of a file; Uses https://docs.racket-lang.org/csv-reading/index.html
; Change the "ontologia/codicem/codicem.numerum.hxl.csv"
(csv-for-each
  (lambda(x)
      (writeln(string-join x)))
  (make-csv-reader (open-input-file "ontologia/codicem/codicem.numerum.hxl.csv")))