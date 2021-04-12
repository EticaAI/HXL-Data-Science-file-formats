#lang racket

;; @see https://docs.racket-lang.org/guide/syntax_module-reader.html
(provide (except-out (all-from-out racket) lambda)
         (rename-out [lambda function]))
