#lang racket
;; File: hdpl/commune/constans.rkt
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD
;;
;; Trivia
;; - "strūctūram"
;;   - https://en.wiktionary.org/wiki/structura#Latin
;; - "dictiōnārium"
;;    - https://en.wiktionary.org/wiki/dictionarium#Latin
;; - "scopum"
;;    - https://en.wiktionary.org/wiki/scopus#Latin
;; - "typum"
;;    - https://en.wiktionary.org/wiki/typus#Latin
;; - "nōmen"
;;    - https://en.wiktionary.org/wiki/nomen#Latin
;; - "versiōnem"
;;    - https://en.wiktionary.org/wiki/versio#Latin
;; - "dactylum"
;;    - https://en.wiktionary.org/wiki/dactylus#Latin
;; - "collēctiōnem"
;;    - https://en.wiktionary.org/wiki/collectio#Latin
;; - "coniūnctum"
;;    - https://en.wiktionary.org/wiki/coniunctus#Latin

; @see - https://docs.racket-lang.org/reference/structutils.html
; @see - https://beautifulracket.com/explainer/data-structures.html
; @see - https://docs.racket-lang.org/reference/data.html
;        - https://docs.racket-lang.org/reference/dicts.html
;        - https://docs.racket-lang.org/guide/contracts-struct.html
;        - https://docs.racket-lang.org/reference/contracts.html
; @see - https://docs.racket-lang.org/data-frame/index.html
;        - https://github.com/alex-hhh/data-frame/blob/master/private/df.rkt

; TODO: maybe use this in something. Uses CLDR, https://docs.racket-lang.org/gregor/index.html



; CREATE TABLE [ISO_639-3] (
;          Id      char(3) NOT NULL,  -- The three-letter 639-3 identifier
;          Part2B  char(3) NULL,      -- Equivalent 639-2 identifier of the bibliographic applications 
;                                     -- code set, if there is one
;          Part2T  char(3) NULL,      -- Equivalent 639-2 identifier of the terminology applications code 
;                                     -- set, if there is one
;          Part1   char(2) NULL,      -- Equivalent 639-1 identifier, if there is one    
;          Scope   char(1) NOT NULL,  -- I(ndividual), M(acrolanguage), S(pecial)
;          Type    char(1) NOT NULL,  -- A(ncient), C(onstructed),  
;                                     -- E(xtinct), H(istorical), L(iving), S(pecial)
;          Ref_Name   varchar(150) NOT NULL,   -- Reference language name 
;          Comment    varchar(150) NULL)       -- Comment relating to one or more of the columns
(struct CodicemLinguam (iso3693 iso6392b iso639t iso6391 scopum typum nomen_eng)
   #:guard (struct-guard/c symbol? (or/c symbol? empty?) (or/c symbol? empty?) (or/c symbol? empty?) symbol? symbol? string?))


;;; ISO 15924, Codes for the representation of names of scripts
; https://en.wikipedia.org/wiki/ISO_15924
; https://unicode.org/iso15924/iso15924.txt
; #
; # ISO 15924 - Codes for the representation of names of scripts
; #             Codes pour la représentation des noms d’écritures
; # Format: 
; #             Code;N°;English Name;Nom français;PVA;Unicode Version;Date
; #
(struct CodicemScriptum (iso15924 iso15924n nomen_eng nomen_fra unicode_pva unicode_versionem dactylum)
  #:guard (struct-guard/c symbol? number? string? string? (or/c symbol? empty?) (or/c number? empty?) symbol?))

;;; TODO: this table is huge. Just to make good naming will take time
; hdpl-conventions/prototype/hdpl/ontologia/codicem/codicem.locum.hxl.csv
; (struct CodicemLocum (TODO))

;; An data struct that have pointer for several structs related to Linguam
(struct ConiunctumLinguam (CodicemLinguamCollectionem)
  #:guard (struct-guard/c (or/c list? empty?))
  )

;; An data struct that have pointer for several structs related to Striptum
(struct ConiunctumScriptum (CodicemScriptumCollectionem)
  #:guard (struct-guard/c (or/c list? empty?))
  )


;; Example of creating the struct
(CodicemLinguam 'arb empty empty empty 'I 'L "Standard Arabic")

(CodicemScriptum 'Adlm 166 "Adlam" "adlam" 'Adlam 9.0 '2016-12-05)
(CodicemScriptum 'Kpel 436 "Kpelle" "kpèllé" empty empty '2016-12-05)

; Access specific item
(CodicemScriptum-iso15924 (CodicemScriptum 'Kpel 436 "Kpelle" "kpèllé" empty empty '2016-12-05))

