#lang racket

;; TODO: make this example with Racket
;;       https://simonbjohnson.github.io/COD_demos/mongolia/


(require hdpl/systema/un/ocha)
(require hdpl/systema/redcross/uk-org-redcross)
(require hdpl/commune/servitium)

(org.ocha.cod->ab "BGD")

(uk.org.redcross->ab "BGD")

; servitium-org-geoboundaries
(servitium/org-geoboundaries->patriam "AGO")
; (servitium-org-geoboundaries->patriam)


(define Example1 (force servitium/org-geoboundaries))

; https://beta.itos.uga.edu/CODV2API/api/v1/locations/mng

(define [hash-have-this-key? hash key val]
  ;  (print hash))
  ;  (hash-keys hash))

  (and
   [hash-has-key? hash key]
   [equal? (hash-ref hash key) val]))
;   [eq? (hash-ref hash key) val]))
;   [hash-has-key? hash (quote key)]
;   [eq? (hash-ref hash (quote key)) val]))



;(first Example1)
;(first (hash-keys (first Example1)))
;'boundaryISO
;
;(hash-have-this-key? (first Example1) 'boundaryISO "AFG")

;; Note to self: hash keys are symbols, but values tend to be string/number


;; TODO: remove this later
(define [servitium/org-geoboundaries->patriam_test patriam]
  ; uses external Example1


  ; local function iter:
  (define [iter lst resultum]
    (cond
      [(empty? lst) resultum]
      [else (iter (rest lst) (
                              cond
                               [(hash-have-this-key? (first lst) 'boundaryISO patriam) (cons resultum (first lst))]
                               [else resultum]

                               ))]))

  ; body calls iter:
  (iter Example1 '()))

(println "testing AFG...")
;(servitium/org-geoboundaries->patriam_test "AFG")
;(servitium/org-geoboundaries->index "AFG")
(force (servitium/org-geoboundaries->index "AFG"))


(println "testing BRA...")
;(servitium/org-geoboundaries->patriam_test "BRA")
(force (servitium/org-geoboundaries->index "BRA"))


(println "testing non-existent like XPTO...")
;(servitium/org-geoboundaries->patriam_test "XPTO")
(force (servitium/org-geoboundaries->index "XPTO"))

;(define [servitium-org-geoboundaries->patriam_test patriam]
;  (for/fold ([acc '()]
;             [seen '()]
;             #:result (reverse acc))
;            ([x (in-list Example1)])
;    (cond
;      [(hash-ref seen patriam #f)
;       (values acc seen)]
;      [else (values (cons patriam acc)
;                    (hash-set seen patriam #t))]))
;  )
;
;
;(servitium-org-geoboundaries->patriam_test "AFG")
;(servitium-org-geoboundaries->patriam_test "BRA222")
