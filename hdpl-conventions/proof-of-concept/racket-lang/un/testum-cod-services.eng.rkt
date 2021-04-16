#lang racket

;; TODO: make this example with Racket
;;       https://simonbjohnson.github.io/COD_demos/mongolia/


(require hdpl/systema/un/ocha)
(require hdpl/systema/redcross/uk-org-redcross)
(require hdpl/commune/servitium)

(org.ocha.cod->ab "BGD")

(uk.org.redcross->ab "BGD")

; servitium-org-geoboundaries
(servitium-org-geoboundaries->patriam "AGO")
; (servitium-org-geoboundaries->patriam)


(define Example1 (force servitium-org-geoboundaries))

; (for ([item (force Example1)] )
;   (for (((key val) (in-hash item)))
;     (printf "~a = ~a~%" key val))
; )


;(define test-ago
;  (cond
;    (empty? 
;
;  )

;(filter  Example1]
;
;  (display item)
;  )


;(for/list [item Example1]
;  (print item)
;  )

; (apply println servitium-org-geoboundaries)

; https://beta.itos.uga.edu/CODV2API/api/v1/locations/mng

(length (list "hop" "skip" "jump"))

(list-ref (list "hop" "skip" "jump") 0) 

(member "fall" (list "hop" "skip" "jump")) 


(map sqrt (list 1 4 9 16))


(map (lambda (i)
       (string-append i "!"))
     (list "peanuts" "popcorn" "crackerjack"))


(filter string? (list "a" "b" 6))

(filter positive? (list 1 -2 6 7 0))


(cons "head" empty)


(cons "dead" (cons "head" empty))


;(define (my-length lst)
;  (cond
;   [(empty? lst) 0]
;   [else (+ 1 (my-length (rest lst)))]))



;(define (my-map f lst)
;  (cond
;   [(empty? lst) empty]
;   [else (cons (f (first lst))
;               (my-map f (rest lst)))]))
;
;
;(my-length (list "a" "b" "c"))

(define (my-length lst)
  ; local function iter:
  (define (iter lst len)
    (cond
      [(empty? lst) len]
      [else (iter (rest lst) (+ len 1))]))
  ; body of my-length calls iter:
  (iter lst 0))


(my-length (list "a" "b" "c"))



;(define (my-map f lst)
;  (define (iter lst backward-result)
;    (cond
;     [(empty? lst) (reverse backward-result)]
;     [else (iter (rest lst)
;                 (cons (f (first lst))
;                       backward-result))]))
;  (iter lst empty))

(define (my-map f lst)
  (for/list ([i lst])
    (f i)))

;
;(filter string? Example1)

;(filter (hash-has-key? v "AGO") Example1)

;(define (my-map f lst)
;  (define (iter lst backward-result)
;    (cond
;     [(empty? lst) (reverse backward-result)]
;     [else (iter (rest lst)
;                 (cons (f (first lst))
;                       backward-result))]))
;  (iter lst empty))

(for/list ([i '(1 2 3)]
           [j "abc"]
           #:when (odd? i)
           [k #(#t #f)])
  (list i j k))




(for/hash ([i '(1 2 3)])
  (values i (number->string i)))

;; @NlightNFotis: "A small naive implementation of map, filter and reduce in racket, implemented by myself."
; https://gist.github.com/NlightNFotis/b662a0368b5eea68ebfde1e4e4fb9787


(define  [hash-have-this-key? hash key val]
  ;  (print hash))
  ;  (hash-keys hash))

  (and
   [hash-has-key? hash key]
   [equal? (hash-ref hash key) val]))
;   [eq? (hash-ref hash key) val]))
;   [hash-has-key? hash (quote key)]
;   [eq? (hash-ref hash (quote key)) val]))



(first Example1)
(first (hash-keys (first Example1)))
'boundaryISO

(hash-have-this-key? (first Example1) 'boundaryISO "AFG")

;; Note to self: hash keys are symbols, but values tend to be string/number


(define [servitium-org-geoboundaries->patriam_test patriam]
  ; uses external Example1

;  ; local function iter: (almost there...)
;  (define [iter lst resultum]
;    (cond
;      [(empty? lst) resultum]
;      [else (iter (rest lst) (cons resultum 1))]))
  

  ; local function iter: (almost there...)
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
(servitium-org-geoboundaries->patriam_test "AFG")

(println "testing BRA...")
(servitium-org-geoboundaries->patriam_test "BRA")



(println "testing non-existent like XPTO...")
(servitium-org-geoboundaries->patriam_test "XPTO")
;(servitium-org-geoboundaries->patriam_test "BRA222")

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
