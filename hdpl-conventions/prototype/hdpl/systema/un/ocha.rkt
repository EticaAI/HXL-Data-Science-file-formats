#lang racket
;; File: /hdpl/systema/un/un-cod-services.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

; (require net/url)
; (require json)

(provide org.ocha.cod->ab org.ocha.cod->ps)


;;; New beta API ---------------------------------------------------------------

(define (org.ocha.cod->ab optionem)
  (writeln "TODO: org.ocha.cod->ab (administrative boundary)"))

(define (org.ocha.cod->ps optionem)
  (writeln "TODO: org.ocha.cod->ps (population statistics)"))

;;; This return a full XLSX spreadsheet XLSX
; https://beta.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/bgd/versions/current/XLSX/1


;;; shows those countries with population statistics datasets
; https://beta.itos.uga.edu/CODV2API/api/v1/Themes/Population%20Statistics
; > {"theme_name":"Population Statistics","comment":null,"countries":["ton","bgd","tha","ssd","ecu"],"Total":0}  


;;; Public API -----------------------------------------------------------------
; https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External
 


;(define (extract str)
;  (substring str 4 7))

;(extract "the cat out of the bag")

;;; Example from https://medium.com/chris-opperwall/practical-racket-using-a-json-rest-api-3d85eb11cc2d
;(define IPHONE_7_TEARDOWN "https://www.ifixit.com/api/2.0/guides/67382")
;(require net/url)
;(require json)
;(define (get-json url)
;   (call/input-url (string->url url)
;                   get-pure-port
;                   (compose string->jsexpr port->string)))
;(define guide-data (get-json IPHONE_7_TEARDOWN))
;(map (lambda (tool)
;            (hash-ref tool 'text))
;   (hash-ref guide-data 'tools))