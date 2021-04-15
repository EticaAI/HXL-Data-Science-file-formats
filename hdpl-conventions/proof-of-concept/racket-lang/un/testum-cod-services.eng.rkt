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
