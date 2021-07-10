# tests/hdplisp/salve-mundi/

> This directory is an working draft (Emerson Rocha, 2021-04-06 19:06 UTC)

# MUST READ
- https://github.com/dear-github/dear-github/issues/147
- Other topics
  - https://www.w3.org/International/articles/strings-and-bidi/
  - https://w3c.github.io/i18n-discuss/notes/json-bidi.html
  - https://www.w3.org/TR/WCAG20-TECHS/H34.html

### Files on tests/hdplisp/salve-mundi/

### .qqq.hpdlisp.json

- [.qqq.hpdlisp.json](.qqq.hpdlisp.json)

#### About `qqq` as code
- <https://en.wikipedia.org/wiki/ISO_639-3>
  - <https://en.wikipedia.org/wiki/Constructed_language>
  - <https://www.kreativekorp.com/clcr/>

Reason:
 - ISO 639-3 allow usage from qaa-qtz for user defined languages
 - `qqq` is free
 - The idea behind `.qqq.hpdlisp.json` is be an
   [Abstract Syntax Tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
   and from the qaa-qtz namespace, qqq seems to be the most extreme naming for
   an constructed language _ever_.

## Tools to inspiect the files

```bash

### Command line tols
# Tips from
# stackoverflow.com/questions/1765311/how-to-view-files-in-binary-from-bash
hexdump tests/hdplisp/salve-mundi/.qqq.hpdlisp.json
xxd tests/hdplisp/salve-mundi/.qqq.hpdlisp.json

### Graphical user interfaces
## bless
# Bless GUI editor (using Debian-like OSs)
sudo apt install bless

bless tests/hdplisp/salve-mundi/.qqq.hpdlisp.json
bless tests/hdplisp/salve-mundi/with-rtl-mark.qqq.hpdlisp.json

```

From <https://unicode-table.com/en/200F/>

```txt
Encoding	hex	dec (bytes)	dec	binary
UTF-8	E2 80 8F	226 128 143	14844047	11100010 10000000 10001111
UTF-16BE	20 0F	32 15	8207	00100000 00001111
UTF-16LE	0F 20	15 32	3872	00001111 00100000
UTF-32BE	00 00 20 0F	0 0 32 15	8207	00000000 00000000 00100000 00001111
UTF-32LE	0F 20 00 00	15 32 0 0	253755392	00001111 00100000 00000000 00000000
```
> TODO: maybe format the table as markdown. or people just look on other sites

| Encoding | hex | dec (bytes) | binary |
| -- | -- | -- | -- |
| UTF-8 | E2 80 8F | 226 128 143 | 14844047	11100010 10000000 10001111 |



## TODOs
- https://askubuntu.com/questions/522512/switch-text-direction-in-gedit
- https://askubuntu.com/questions/380776/stabilizing-characters-like-and
  - Stabilizing characters like `< >`, `{ }` and `[ ]`

<!--


-->