#lang racket

;; TODO: make this example with Racket
;;       https://simonbjohnson.github.io/COD_demos/mongolia/


(require hdpl/systema/un/ocha)
(require hdpl/systema/redcross/uk-org-redcross)

(org.ocha.cod->ab "BGD")

(uk.org.redcross->ab "BGD")


; https://beta.itos.uga.edu/CODV2API/api/v1/locations/mng