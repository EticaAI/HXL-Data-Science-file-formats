#lang racket
;; File: radix.rkt
;; Trivia:
;; - "rādīcem"
;;   - "rādīx"
;;     - https://en.wiktionary.org/wiki/radix#Latin
;;
;; Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
;; License: Public Domain / BSD Zero Clause License
;; SPDX-License-Identifier: Unlicense OR 0BSD

;; TODO: this is a draft. Put here the "base" (minimum to boostrap HDPL) even when no natural
;;       language was loaded


;; This is an draft of what neutral name could be used
; b:
;   ATOM:
;     _*_
;   CAR:
;     _^_ (How this will behave on Right-to-left languages when compose like CADR _^~_ & CDAR _~^_ ?)
;   CDR:
;     _~_ (How this will behave on Right-to-left languages when compose like CADR _^~_ & CDAR _~^_ ?)
;   COND:
;     _?_
;   CONS:
;     _*_
;   EQ:
;     _=_
;   LAMBDA:
;     _λ_   (Not ideal, is an alphabed for an writting system)
;     ___   (3 _ seems anonymous enough and is neutral)
;   PRINT:
;     _:_
;   QUOTE:
;     _"_
;   READ:
;     ???  (TODO: think about)
;   DEFINE, DEF, DEFN, etc:
;     _#_
;   L:
;     _ISO369-3_ltr-text
;     rtl-text_ISO369-3_
;           (Note: non-Latin alphabets may need some work to discover how to use term for them)
;   "+":
;   "-":
;   "*":
;   "/":

;; From https://en.wikipedia.org/wiki/Hashtag
; "Languages that do not use word dividers handle hashtags differently. In China,
; microblogs Sina Weibo and Tencent Weibo use a double-hashtag-delimited #HashName#
; format, since the lack of spacing between Chinese characters necessitates a closing tag.
; Twitter uses a different syntax for Chinese characters and orthographies with similar spacing
; conventions: the hashtag contains unspaced characters, separated from preceding and following
; text by spaces (e.g., '我 #爱 你' instead of '我#爱你')[30] or by zero-width non-joiner characters
; before and after the hashtagged element, to retain a linguistically natural appearance
; (displaying as unspaced '我‌#爱‌你', but with invisible non-joiners delimiting the hashtag).[31]

; (provide (except-out (all-from-out racket) lambda)
;          (rename-out [lambda function]))

; (module reader racket
;     (provide (except-out (all-from-out racket) lambda)
;             (rename-out [lambda function])))

(module reader racket
  (require syntax/strip-context)

  (provide (rename-out [literal-read read]
                       [literal-read-syntax read-syntax]))

  (define (literal-read in)
    (syntax->datum
     (literal-read-syntax #f in)))

  (define (literal-read-syntax src in)
    (with-syntax ([str (port->string in)])
      (strip-context
       #'(module anything racket
           (provide data)
           (define data 'str))))))
