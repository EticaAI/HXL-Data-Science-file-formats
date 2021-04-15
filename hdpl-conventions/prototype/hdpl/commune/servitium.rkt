#lang lazy
; #lang racket
;; File: hdpl/commune/servitium.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD
;;
;; Trivia
;; - "servitium"
;;  - https://en.wiktionary.org/wiki/servitium#Latin
;; - "dictiōnārium"
;;  - https://en.wiktionary.org/wiki/dictionarium#Latin


;; TODO: considere this as option to implement lazy evaluation
;;       http://matt.might.net/articles/implementing-laziness/
;;       http://people.cs.aau.dk/~normark/prog3-03/html/notes/eval-order_themes-delay-stream-section.html

(require net/url)
(require racket/promise)

(require json)
(provide
  ServitumDictionarium
  ; GeoboundariesOrgServitumDictionarium
; )
  servitium-org-geoboundaries
  servitium-org-geoboundaries->patriam
  )


;; http://matt.might.net/articles/implementing-laziness/
; (define-syntax (define/by-need stx)
;   (syntax-case stx ()
;     [(_ (f v ...) body ...)
;      (with-syntax ([($f) (generate-temporaries #'(f))])
;        #'(begin
;            (define-syntax f
;              (syntax-rules ()
;                [(_ arg (... ...))
;                 ($f (delay arg) (... ...))]))
;            (define ($f v ...)
;              (let-syntax ([v (lambda (stx*)
;                                (syntax-case stx* ()
;                                  [(_ arg (... ...)) 
;                                   #'((force v) arg (... ...))]
;                                  [_ #'(force v)]))] ...)
;                body ...))))]))


(define ServitumDictionarium
  (delay (read-json (open-input-file "ontologia/json/servitium.hdplisp.json"))))

;;;; https://www.geoboundaries.org/api.html
;; https://www.geoboundaries.org/gbRequest.html?ISO=ALL
; (get-pure-port (string->url "https://www.geoboundaries.org/gbRequest.html?ISO=ALL"))

(define GeoboundariesOrgServitumDictionarium
  (lazy
    (read-json
      (get-pure-port (string->url "https://www.geoboundaries.org/gbRequest.html?ISO=ALL")))))


; Return list raw list of values
(define servitium-org-geoboundaries
  GeoboundariesOrgServitumDictionarium)

; List of ISO3 country codes
(define [servitium-org-geoboundaries->patriam patriam]
  (lazy "TODO: servitium-org-geoboundaries->patriam"))

; Does this country have any information?
(define servitium-org-geoboundaries->patriam?
  "TODO: servitium-org-geoboundaries->patriam?")

; Does this country have an adm1 level? (Note: all that do exist, have at least adm0)
(define servitium-org-geoboundaries->patriam-adm1?
  "TODO: servitium-org-geoboundaries->patriam-adm1?")

; Does this country have an adm2 level? (Note: all that do exist, have at least adm0)
(define servitium-org-geoboundaries->patriam-adm2?
  "TODO: servitium-org-geoboundaries->patriam-adm2?")

; TODO: other levels


; (force GeoboundariesOrgServitumDictionarium)

; (jsexpr? 'null)
; (jsexpr? (force GeoboundariesOrgServitumDictionarium))

; (force GeoboundariesOrgServitumDictionarium)

; (for (((key val) (in-hash (first (force GeoboundariesOrgServitumDictionarium)))))
;   (printf "~a = ~a~%" key val))


; (for ([item (force GeoboundariesOrgServitumDictionarium)] )
;   (for (((key val) (in-hash (item))))
;     (printf "~a = ~a~%" key val))
;  )

; (for ([item (force GeoboundariesOrgServitumDictionarium)] )
;   (display item)
; )


;;;; Helpers: example on how to print an array of dicts
; (define Example1
;   (delay 
;     (read-json
;       (get-pure-port (string->url "https://www.geoboundaries.org/gbRequest.html?ISO=ALL")))))

; (for ([item (force Example1)] )
;   (for (((key val) (in-hash item)))
;     (printf "~a = ~a~%" key val))
; )

; servitium-org-geoboundaries

