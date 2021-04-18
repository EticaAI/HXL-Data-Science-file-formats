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


(define (my-+ a b)
  (if (zero? a)
      b
      (my-+ (sub1 a) (add1 b))))
 
(define (my-* a b)
  (if (zero? a)
      b
      (my-* (sub1 a) (my-+ b b))))
 
(provide my-+
         my-*)