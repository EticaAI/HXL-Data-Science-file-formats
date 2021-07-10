#lang racket
;; File: hdpl/systema/literal.rkt
;; Description: This is a just a debug helper. See these links
;;              - https://docs.racket-lang.org/guide/hash-lang_reader.html
;; Author: docs.racket-lang.org


(require syntax/strip-context)
 
(provide (rename-out [literal-read read]
                     [literal-read-syntax read-syntax]))
 
(define (literal-read in)
  (syntax->datum
   (literal-read-syntax #f in)))
 
(define (literal-read-syntax src in)
  (with-syntax ([str (port->string in)])
    (strip-context
     #'(module anything racket
         (provide data)
         (define data 'str)))))