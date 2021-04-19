#lang racket
;; File: hdpl/libhxl/libhxl-minimum.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD
;;
;; References:
;; - The standard:
;;   - https://hxlstandard.org/
;; - Implementations
;;   - Python
;;     - https://github.com/HXLStandard/libhxl-python
;;   - JavaScript
;;     - https://github.com/HXLStandard/libhxl-js

 (require csv-reading)

 (provide hxl->wrap hxl->list hxl-map hxl-for-each hxl->sxml)

; (define (my-+ a b)
;   (if (zero? a)
;       b
;       (my-+ (sub1 a) (add1 b))))
 
; (define (my-* a b)
;   (if (zero? a)
;       b
;       (my-* (sub1 a) (my-+ b b))))
 
; (provide my-+
;          my-*)

;; https://github.com/HXLStandard/libhxl-js#create-a-dataset-from-array-data
; var rawData = [
;     [ "Organisation", "Cluster", "Province" ],
;     [ "#org", "#sector", "#adm1" ],
;     [ "Org A", "WASH", "Coastal Province" ],
;     [ "Org B", "Health", "Mountain Province" ],
;     [ "Org C", "Education", "Coastal Province" ],
;     [ "Org A", "WASH", "Plains Province" ],
; ];

; var dataset = hxl.wrap(rawData);

(define hxl->wrap csv->sxml)

;; https://docs.racket-lang.org/csv-reading/index.html
(define hxl->list csv->list)

;; https://docs.racket-lang.org/csv-reading/index.html
(define hxl-map csv-map)

;; https://docs.racket-lang.org/csv-reading/index.html
(define hxl-for-each csv-for-each)


;; TODO: implement some more specialize sxml for HXL
; @see https://en.wikipedia.org/wiki/SXML
;; https://docs.racket-lang.org/sxml/index.html
;; https://github.com/jbclements/sxml/blob/master/sxml/sxpath.rkt
(define hxl->sxml csv->sxml)
