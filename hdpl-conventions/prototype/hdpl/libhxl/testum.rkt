#lang racket/base
;; File: hdpl/libhxl/testum.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

; Quick tests
; racket hdpl-conventions/prototype/hdpl/libhxl/testum.rkt

 
;; https://docs.racket-lang.org/rackunit/quick-start.html

 
(require rackunit
         "hxl.rkt")

(check-equal? (my-+ 1 1) 2 "Simple addition")
; (check-equal? (my-* 1 2) 2 "Simple multiplication")
