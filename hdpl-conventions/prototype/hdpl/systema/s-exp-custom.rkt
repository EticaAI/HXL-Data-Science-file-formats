#lang racket
;; File: hdpl/systema/s-exp-custom
;; Description: This is a just a debug helper. See these links
;;              - https://docs.racket-lang.org/guide/syntax_module-reader.html
;; Author: docs.racket-lang.org

(provide (except-out (all-from-out racket) lambda)
         (rename-out [lambda function]))
