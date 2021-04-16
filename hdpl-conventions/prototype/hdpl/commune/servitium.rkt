#lang racket
;#lang lazy
; #lang racket
;; File: hdpl/commune/servitium.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD
;;
;; Trivia
;; - "servitium"
;;    - https://en.wiktionary.org/wiki/servitium#Latin
;; - "dictiōnārium"
;;    - https://en.wiktionary.org/wiki/dictionarium#Latin
;; - "indicem"
;;    - https://en.wiktionary.org/wiki/index#Latin
;; - "praecīsiōnem"
;;    - https://en.wiktionary.org/wiki/praecisio#Latin

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
 servitium/org-geoboundaries
 servitium/org-geoboundaries->patriam
 servitium/org-geoboundaries->index
 )



;; Simple local helper
(define [hash-have-this-key? hash key val]
  (and
   [hash-has-key? hash key]
   [equal? (hash-ref hash key) val]))


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
(define servitium/org-geoboundaries
  GeoboundariesOrgServitumDictionarium)



(define [servitium/org-geoboundaries->index patriam [praecisionem empty] ]
  ; Note: uses GeoboundariesOrgServitumDictionarium

  ; TODO: implement also ADM level praecisionem

  ; local function iter:
  (define [iter lst resultum]
    (cond
      [(empty? lst) resultum]
      [else 
       (iter (rest lst)
             (cond
               [(hash-have-this-key? (first lst) 'boundaryISO patriam) (cons resultum (first lst))]
               [else resultum]
               ))]))

  ; body calls iter:
  (iter (force GeoboundariesOrgServitumDictionarium) '()))


; List of ISO3 country codes
(define [servitium/org-geoboundaries->patriam patriam]
  (lazy "TODO: servitium/org-geoboundaries->patriam"))

; Does this country have any information?
(define servitium/org-geoboundaries->patriam?
  "TODO: servitium/org-geoboundaries->patriam?")

; Does this country have an adm1 level? (Note: all that do exist, have at least adm0)
(define servitium/org-geoboundaries->patriam-adm1?
  "TODO: servitium/org-geoboundaries->patriam-adm1?")

; Does this country have an adm2 level? (Note: all that do exist, have at least adm0)
(define servitium/org-geoboundaries->patriam-adm2?
  "TODO: servitium/org-geoboundaries->patriam-adm2?")

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

