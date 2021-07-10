#lang info
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

(define collection "hdpl")

; TODO: remove temporary dependencies that would not be required later
; (define deps '("base" "lazy" "data-frame" "csv-reading" "rackunit-lib"))
; (define deps '("base" "data-frame" "csv-reading" "rackunit-lib"))
(define deps '("base" "data-frame" "csv-reading" "rackunit-lib" "sxml"))
(define build-deps '("scribble-lib" "racket-doc" "rackunit-lib"))
(define scribblings '(("scribblings/hdpl.scrbl" ())))
(define pkg-desc "HDP Declarative Programming (working draft)")
(define version "0.8.7")
(define pkg-authors '("Emerson Rocha"))
