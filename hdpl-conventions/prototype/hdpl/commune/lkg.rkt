#lang racket
;; File: hdpl/commune/lkg.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD
;;
;; Trivia
;; - "localization"
;;  - https://en.wikipedia.org/wiki/Internationalization_and_localization
;; - "Knowledge graph"
;;  - https://en.wikipedia.org/wiki/Knowledge_graph


(require json)
(provide LKGDictionarium)

(define LKGDictionarium 
  (read-json (open-input-file "ontologia/json/core.lkg.json")))
