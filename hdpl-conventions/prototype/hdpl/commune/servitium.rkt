#lang racket
;; File: hdpl/commune/servitium.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD
;;
;; Trivia
;; - "servitium"
;;  - https://en.wiktionary.org/wiki/servitium#Latin
;; - "dictiōnārium"
;;  - https://en.wiktionary.org/wiki/dictionarium#Latin

(require json)
(provide ServitumDictionarium)

(define ServitumDictionarium (read-json (open-input-file "ontologia/json/servitium.hdplisp.json")))
