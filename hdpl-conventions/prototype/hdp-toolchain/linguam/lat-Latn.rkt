#lang racket

(provide hello-world)


;; @see https://omniglot.com/language/phrases/latin.php
; (define salutation (list-ref '("Hi" "Hello") (random 2)))
(define hello-world (list-ref '("Heus!" "Salve!" "Ave!") (random 3)))