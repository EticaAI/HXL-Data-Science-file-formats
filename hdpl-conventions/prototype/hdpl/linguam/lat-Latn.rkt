#lang racket
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

; (provide salve-mundi)

;; - lat
;;   - https://iso639-3.sil.org/code/lat
;;   - https://en.wikipedia.org/wiki/ISO_639-3
;; - Latn
;;   - https://en.wikipedia.org/wiki/ISO_15924
;;   - https://en.wikipedia.org/wiki/Latin_alphabet

; (define salve-mundi (list-ref '("Heus!" "Salve!" "Ave!") (random 3)))


; ;; https://docs.racket-lang.org/guide/syntax_module-reader.html
; ; #lang racket
; (provide (except-out (all-from-out racket) lambda)
;          (rename-out [lambda function]))

;; @see https://docs.racket-lang.org/guide/language-collection.html
;; Instead of 'data' this export 'data-lat-Latn'
(module reader racket
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
           (provide data-lat-Latn)
           (define data-lat-Latn 'str))))))