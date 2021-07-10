# ontologia/unicode

> TODO: note to self, read these ones
>
> - http://www.unicode.org/reports/tr51/ (UNICODE EMOJI)
  - <http://www.unicode.org/reports/tr9/> (UNICODE BIDIRECTIONAL ALGORITHM)
  - <s><http://unicode.org/reports/tr35/> (UNICODE LOCALE DATA MARKUP LANGUAGE (LDML), Part 1, Core)</s>
    - <https://unicode.org/reports/tr35/tr35-general.html> (Part 2: General (display names & transforms, etc.))
    - <s><https://unicode.org/reports/tr35/tr35-numbers.html> (Part 3: Numbers (number & currency formatting))</s>
    - <https://unicode.org/reports/tr35/tr35-dates.html> (Part 4: Dates (date, time, time zone formatting))
    - <https://unicode.org/reports/tr35/tr35-collation.html> (Part 5: Collation (sorting, searching, grouping))
    - <https://unicode.org/reports/tr35/tr35-info.html> (Part 6: Supplemental (supplemental data))
    - <https://unicode.org/reports/tr35/tr35-keyboards.html> (Part 7: Keyboards (keyboard mappings))

## Language frontents for unicode parsing


### JavaScript

- https://github.com/node-unicode/node-unicode-data

> Note: note tested this library yet.

- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize

> Note: this is not same as unicodedata to extract metadata

### Python

#### Standard libraries

- https://docs.python.org/3/library/unicodedata.html

Perfect. Python have built in functionality for this!

### Racket

- https://docs.racket-lang.org/srfi/srfi-std/srfi-13.html
- https://lists.racket-lang.org/users/archive/2013-May/057844.html
  - https://gist.github.com/dyoo/5586470
- https://docs.racket-lang.org/guide/regexp-chars.html
- https://docs.racket-lang.org/srfi/srfi-std/srfi-14.html

> TODO: test these or any other existing alternatives to parse Unicode metadata
  later

### Unicode reports

Do exist several reports and guides from Unicode (see
http://www.unicode.org/reports/), these are a few ones:

- Unicode® Standard Annex #44: UNICODE CHARACTER DATABASE
  - <http://www.unicode.org/reports/tr44/>
- Unicode® Standard Annex #24 UNICODE SCRIPT PROPERTY
  - <http://www.unicode.org/reports/tr24/>
- UNICODE LOCALE DATA MARKUP LANGUAGE (LDML)
  <http://unicode.org/reports/tr35/> (Part 1, Core)


#### Some very quick notes

> "For example, the Russian language is written with a distinctive set of
  letters, as well as other marks or symbols that together form a subset of
  the Cyrillic script. Other languages using the Cyrillic script, such as
  Ukrainian or Serbian, employ a different subset of those letters.
  (...)
  A script may also explicitly borrow letters from another script. For example,
  some writing systems that use the Cyrillic script have borrowed letter
  forms from the Latin script. Furthermore, letter forms may show accidental
  similarity in shapes: a simple line or circle used as a letter, for example,
  could have been independently created many times in the history of the
  development of writing systems." -- <http://www.unicode.org/reports/tr24>

> "2.2 Relation to ISO 15924 Codes (...) **In some cases the match between the
  Script property values and the ISO 15924 codes is not precise, because the
  goals are somewhat different. ISO 15924 is aimed primarily at the
  bibliographic identification of scripts**; consequently, it occasionally
  identifies varieties of scripts that may be useful for book cataloging, but
  that are not considered distinct scripts in the Unicode Standard.
  For example, ISO 15924 has separate script codes for the Fraktur and Gaelic
  varieties of the Latin script. Such codes for script varieties are shown
  in parentheses in Table 3." -- <http://www.unicode.org/reports/tr24>
