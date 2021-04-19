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

; https://pkgs.racket-lang.org/package/sxml
 (require sxml)

; https://docs.racket-lang.org/sxml/sxpath.html
(require sxml/sxpath)
 
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


;; JSON-objects would be this way
;; https://proxy.hxlstandard.org/data.objects.json?dest=data_view&url=https%3A%2F%2Fraw.githubusercontent.com%2FHXLStandard%2Fhxl-cookbook%2Fmaster%2Fdocs%2Fexamples%2Ffiltering-rows-01.csv
; [
; {
;   "#adm1": "Coast Province",
;   "#org": " Org A",
;   "#sector": " WASH"
; },
; {
;   "#adm1": "Plains Province",
;   "#org": " Org B",
;   "#sector": " WASH"
; },
; {
;   "#adm1": "Mountains Province",
;   "#org": " Org A",
;   "#sector": " WASH"
; }
; ]

(define filtering-rows-01-sxml
  `(*TOP*
     (headers (col-0 "Province") (col-1 " Organisation") (col-2 " Cluster")) 
     (hashtags (col-0 "#adm1") (col-1 " #org") (col-2 " #sector"))
     (row (col-0 "Coast Province") (col-1 " Org A") (col-2 " WASH"))
     (row (col-0 "Plains Province") (col-1 " Org B") (col-2 " WASH"))
     (row (col-0 "Mountains Province") (col-1 " Org A") (col-2 " WASH"))))

; (display filtering-rows-01)

; (hxl->list filtering-rows-01)
; '(("Province" " Organisation" " Cluster") ("#adm1" " #org" " #sector") ("Coast Province" " Org A" " WASH") ("Plains Province" " Org B" " WASH") ("Mountains Province" " Org A" " WASH"))


(hxl->sxml filtering-rows-01)
; csv->sxml:
;   '(*TOP*
;      (row (col-0 "Province") (col-1 " Organisation") (col-2 " Cluster")) 
;      (row (col-0 "#adm1") (col-1 " #org") (col-2 " #sector"))
;      (row (col-0 "Coast Province") (col-1 " Org A") (col-2 " WASH"))
;      (row (col-0 "Plains Province") (col-1 " Org B") (col-2 " WASH"))
;      (row (col-0 "Mountains Province") (col-1 " Org A") (col-2 " WASH")))
; (not implemented) hxl->sxml maybe could be this?
;   '(*TOP*
;      (headers (col-0 "Province") (col-1 " Organisation") (col-2 " Cluster")) 
;      (hashtags (col-0 "#adm1") (col-1 " #org") (col-2 " #sector"))
;      (row (col-0 "Coast Province") (col-1 " Org A") (col-2 " WASH"))
;      (row (col-0 "Plains Province") (col-1 " Org B") (col-2 " WASH"))
;      (row (col-0 "Mountains Province") (col-1 " Org A") (col-2 " WASH")))

(writeln "test2")

((sxpath '(// row)) (hxl->sxml filtering-rows-01))


(writeln "test3")
; (check-equal? (my-+ 1 1) 2 "Simple addition")
; (check-equal? (my-* 1 2) 2 "Simple multiplication")
(define table
    `(*TOP*
      (table
       (tr (td "a") (td "b"))
       (tr (td "c") (td "d")))))


((sxpath '(// td)) table)