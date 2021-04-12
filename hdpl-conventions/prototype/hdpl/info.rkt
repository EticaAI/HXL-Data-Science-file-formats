#lang info
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

(define collection "hdp-toolchain")
(define deps '("base"))
(define build-deps '("scribble-lib" "racket-doc" "rackunit-lib"))
(define scribblings '(("scribblings/hdp-toolchain.scrbl" ())))
(define pkg-desc "HDP Declarative Programming (working draft)")
(define version "0.8.6")
(define pkg-authors '("Emerson Rocha"))
