#lang racket
;; File: /hdpl/systema/un/un-cod-services.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD


(provide extract)

(module nest racket
    (provide num-eggs)
    (define num-eggs 2))


(define (extract str)
  (substring str 4 7))

;(extract "the cat out of the bag")

;; Example from https://medium.com/chris-opperwall/practical-racket-using-a-json-rest-api-3d85eb11cc2d
(define IPHONE_7_TEARDOWN "https://www.ifixit.com/api/2.0/guides/67382")
(require net/url)
(require json)
(define (get-json url)
   (call/input-url (string->url url)
                   get-pure-port
                   (compose string->jsexpr port->string)))
(define guide-data (get-json IPHONE_7_TEARDOWN))
(map (lambda (tool)
            (hash-ref tool 'text))
   (hash-ref guide-data 'tools))