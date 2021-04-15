#lang racket/base
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

;; TODO: implement lazy evaluation on relevant parts
;        https://docs.racket-lang.org/reference/Delayed_Evaluation.html
;        but see also
;        - https://stackoverflow.com/questions/42012842/racket-lazy-evaluation-within-some-scope
;        - https://docs.racket-lang.org/reference/streams.html?q=tsreams  
;        - https://docs.racket-lang.org/reference/streams.html?q=tsreams  

(module+ test
  (require rackunit))

;; Notice
;; To install (from within the package directory):
;;   $ raco pkg install
;; To install (once uploaded to pkgs.racket-lang.org):
;;   $ raco pkg install <<name>>
;; To uninstall:
;;   $ raco pkg remove <<name>>
;; To view documentation:
;;   $ raco docs <<name>>
;;
;; For your convenience, we have included LICENSE-MIT and LICENSE-APACHE files.
;; If you would prefer to use a different license, replace those files with the
;; desired license.
;;
;; Some users like to add a `private/` directory, place auxiliary files there,
;; and require them in `main.rkt`.
;;
;; See the current version of the racket style guide here:
;; http://docs.racket-lang.org/style/index.html

;; Code here

; (require "radix.rkt")
; (require "linguam/lat-Latn.rkt")
; (require "linguam/mis-Qaaa.rkt")

; (provide salve-mundi)

(module+ test
  ;; Any code in this `test` submodule runs when this file is run using DrRacket
  ;; or with `raco test`. The code here does not run when this file is
  ;; required by another module.

  (check-equal? (+ 2 2) 4))

(module+ main
  ;; (Optional) main submodule. Put code here if you need it to be executed when
  ;; this file is run using DrRacket or the `racket` executable.  The code here
  ;; does not run when this file is required by another module. Documentation:
  ;; http://docs.racket-lang.org/guide/Module_Syntax.html#%28part._main-and-test%29

  (require racket/cmdline)
  (define who (box "world"))
  (command-line
    #:program "my-program"
    #:once-each
    [("-n" "--name") name "Who to say hello to" (set-box! who name)]
    #:args ()
    (printf "hello ~a~n" (unbox who))))


; ;; @see https://docs.racket-lang.org/guide/language-collection.html
; (module reader racket
;   (require syntax/strip-context)
 
;   (provide (rename-out [literal-read read]
;                        [literal-read-syntax read-syntax]))
 
;   (define (literal-read in)
;     (syntax->datum
;      (literal-read-syntax #f in)))
 
;   (define (literal-read-syntax src in)
;     (with-syntax ([str (port->string in)])
;       (strip-context
;        #'(module anything racket
;            (provide data)
;            (define data 'str))))))