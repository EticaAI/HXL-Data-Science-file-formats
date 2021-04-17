#lang racket
;; File: hdpl/systema/libhxl-minimum.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

;; HXLStandard do not (at the moment) have underlining implementation on Racket
;; so this file mostly is a very simple port of minimum functionality.

;; Projects that do use CSV
; - https://docs.racket-lang.org/csv-reading
; - https://docs.racket-lang.org/data-frame/
;   - https://github.com/alex-hhh/data-frame/blob/master/private/csv.rkt


;; https://docs.racket-lang.org/csv-reading/index.html
(require csv-reading)

(define make-hxl-simple-csv-reader
  (make-csv-reader-maker
    '((separator-chars #\,))))


;; Reference example from https://rosettacode.org/wiki/CSV_data_manipulation#Racket
; #lang racket
; (require (planet neil/csv:1:=7) net/url)
 
; (define make-reader
;   (make-csv-reader-maker
;    '((separator-chars              #\,)
;      (strip-leading-whitespace?  . #t)
;      (strip-trailing-whitespace? . #t))))
 
; (define (all-rows port)
;   (define read-row (make-reader port))
;   (define head (append (read-row) '("SUM")))
;   (define rows (for/list ([row (in-producer read-row '())])
;                  (define xs (map string->number row))
;                  (append row (list (~a (apply + xs))))))
;   (define (->string row) (string-join row "," #:after-last "\n"))
;   (string-append* (map ->string (cons head rows))))


; (define hxl-reader "TODO")

; (csv->sxml (open-input-file "ontologia/codicem/codicem.numerum.hxl.csv"))
(csv->list (open-input-file "ontologia/codicem/codicem.numerum.hxl.csv"))



;; Print each line of a file; Uses https://docs.racket-lang.org/csv-reading/index.html
; Change the "ontologia/codicem/codicem.numerum.hxl.csv"
(csv-for-each
  (lambda(x)
      (writeln(string-join x)))
  (make-csv-reader (open-input-file "ontologia/codicem/codicem.numerum.hxl.csv")))

;; See https://rosettacode.org/wiki/CSV_data_manipulation#Racket