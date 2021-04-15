#lang racket
;; File: hdpl/commune/vkg.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD
;;
;; Trivia
;; - "vocābulārium"
;;  - hhttps://en.wiktionary.org/wiki/vocabularium#Latin
;; - "Knowledge graph"
;;  - https://en.wikipedia.org/wiki/Knowledge_graph


(require json)
(provide VKGDictionarium)

(define VKGDictionarium (read-json (open-input-file "ontologia/json/core.vkg.json")))

; VKGDictionarium