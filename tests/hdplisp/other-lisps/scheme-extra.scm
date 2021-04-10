;; https://rosettacode.org/wiki/Hello_world/Text#Scheme
;; https://en.wikipedia.org/wiki/Scheme_(programming_language)

;; R5RS
(display "Hello world!")

;; R7RS
(import (scheme base)
        (scheme write))
(display "Hello world!")