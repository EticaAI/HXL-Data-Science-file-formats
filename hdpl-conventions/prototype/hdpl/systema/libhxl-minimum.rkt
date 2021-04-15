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


; (define generic-csv-reader "TODO")


; (define hxl-reader "TODO")

; (csv->sxml (open-input-file "ontologia/codicem/codicem.numerum.hxl.csv"))
(csv->list (open-input-file "ontologia/codicem/codicem.numerum.hxl.csv"))