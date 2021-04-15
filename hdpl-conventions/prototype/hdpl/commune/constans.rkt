#lang racket
;; File: hdpl/commune/constans.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD
;;
;; Trivia
;; - "cōnstāns"
;;   - https://en.wiktionary.org/wiki/constans#Latin


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