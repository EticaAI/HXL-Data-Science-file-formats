#lang racket
;; File: hdpl/commune/constans.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD
;;
;; Trivia
;; - "cōnstāns"
;;   - https://en.wiktionary.org/wiki/constans#Latin

(require csv-reading)
(require data-frame)
(require hdpl/commune/structuram)

;; org.ocha.vocabulary->adm0
; https://docs.google.com/spreadsheets/d/1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY/edit#gid=1088874596

(define Constans->PS->adm0
  "https://docs.google.com/spreadsheets/d/1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY/edit#gid=1088874596")


;; HXL-CPLP-Vocab_Scriptum (ISO 15924 et al)
;; https://docs.google.com/spreadsheets/d/1B9lzzJC124GvUMbPT-6S9FQiIeO6pHsnHdQib-bcPkg/edit#gid=214068544
(define Constans->Scriptum
  "https://docs.google.com/spreadsheets/d/1B9lzzJC124GvUMbPT-6S9FQiIeO6pHsnHdQib-bcPkg/edit#gid=214068544")

;; HXL-CPLP-Vocab_Linguam (ISO 639-3 et al)
;; https://github.com/HXL-CPLP/forum/issues/38
(define Constans->Linguam
  "https://docs.google.com/spreadsheets/d/12k4BWqq5c3mV9ihQscPIwtuDa_QRB-iFohO7dXSSptI/edit#gid=0")


(provide Constans->PS->adm0 Constans->Scriptum Constans->Linguam)


;;; Temporary code
; (require csv-reading)

; (define make-food-csv-reader
;   (make-csv-reader-maker
;    '((separator-chars            #\|)
;      (strip-leading-whitespace?  . #t)
;      (strip-trailing-whitespace? . #t))))


;; TODO: maybe cache things like this https://docs.racket-lang.org/memo/index.html

; (define CodicemLinguam (df-read/csv "ontologia/codicem/codicem.linguam.hxl.csv"))
; ; (define CodicemLinguam (csv->list (open-input-file "ontologia/codicem/codicem.numerum.hxl.csv")))
; (define CodicemLocum (df-read/csv "ontologia/codicem/codicem.locum.hxl.csv"))
; (define CodicemNumerum (df-read/csv "ontologia/codicem/codicem.numerum.hxl.csv"))
; (define CodicemScriptum (df-read/csv "ontologia/codicem/codicem.scriptum.hxl.csv"))


; ; (writeln "CodicemLinguam")
; (df-describe CodicemLinguam)
; (write CodicemLinguam)

; (writeln "CodicemLocum")
; (df-describe CodicemLocum)

; (writeln "CodicemNumerum")
; (df-describe CodicemNumerum)

; (writeln "CodicemScriptum")
; (df-describe CodicemScriptum)


; (csv->sxml (open-input-file "ontologia/codicem/codicem.numerum.hxl.csv"))


;; https://rosettacode.org/wiki/CSV_data_manipulation#Racket

;; Example of how to print line by line an CSV
(csv-for-each
  (lambda(x)
      (writeln(string-join x)))
  (make-csv-reader (open-input-file "ontologia/codicem/codicem.linguam.hxl.csv")))