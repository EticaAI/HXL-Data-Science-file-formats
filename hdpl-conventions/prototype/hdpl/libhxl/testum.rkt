#lang racket/base
;; File: hdpl/libhxl/testum.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

; Quick tests
; racket hdpl-conventions/prototype/hdpl/libhxl/testum.rkt

 
;; https://docs.racket-lang.org/rackunit/quick-start.html

(require "hxl.rkt")
; (require (file "hxl.rkt"))

 
; (require rackunit
;          "hxl.rkt")

; https://github.com/HXLStandard/hxl-cookbook/
; https://raw.githubusercontent.com/HXLStandard/hxl-cookbook/master/docs/examples/filtering-rows-01.csv
;   Province, Organisation, Cluster
;   #adm1, #org, #sector
;   Coast Province, Org A, WASH
;   Plains Province, Org B, WASH
;   Mountains Province, Org A, WASH
(define filtering-rows-01 "Province, Organisation, Cluster\n#adm1, #org, #sector\nCoast Province, Org A, WASH\nPlains Province, Org B, WASH\nMountains Province, Org A, WASH")

; (display filtering-rows-01)

(hxl->list filtering-rows-01)
; '(("Province" " Organisation" " Cluster") ("#adm1" " #org" " #sector") ("Coast Province" " Org A" " WASH") ("Plains Province" " Org B" " WASH") ("Mountains Province" " Org A" " WASH"))


(hxl->sxml filtering-rows-01)
; (check-equal? (my-+ 1 1) 2 "Simple addition")
; (check-equal? (my-* 1 2) 2 "Simple multiplication")
