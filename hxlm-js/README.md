# EticaAI/HXL-Data-Science-file-formats/hxlm-js

<!--
Notes to self: when working on localhost, the url is hxlm-js/index-src.html
               (http://git.workspace.localhost/EticaAI/HXL-Data-Science-file-formats/hxlm-js/index-src.html)
               not hxlm-js/index.html. To build that page, the
               ./prepare-hxlm-relsease.sh needs to be executed to create
               the hashes of the javascripts and etc.

@TODO: automate the generation of SRI Hash (https://www.srihash.org/) without
       need to go to that site or something. The bash version do output
       SHA-384, but SRI are not as good

-->


This folders contains a subset of HXLm.HDP and, at some extend, HXLm.lisp.
While this may not be a full implementation of the python interface, this
_at least_ help to not make
[hdp-conventions/README.md](hdp-conventions/README.md) too focused on an single
programming language.

## Test page
For convenience, the <https://hpd.etica.ai> domain as created to allow test the javascript
parts of HXLm. Still recommended look at the GitHub (and maybe the source
code) that do have a lot of comments.

- [hxlm-js/index.html](hxlm-js/index.html)
  - [https://hpd.etica.ai/hxlm-js/index.html]

## Ontologia

- [hxlm/ontologia/](hxlm/ontologia/)
- [hxlm/ontologia/core.lkg.yml](hxlm/ontologia/core.lkg.yml)
  - [hxlm/ontologia/json/core.lkg.json](hxlm/ontologia/json/core.lkg.json)
    - [https://hpd.etica.ai/hxlm/ontologia/json/core.lkg.json](https://hpd.etica.ai/hxlm/ontologia/json/core.lkg.json)
- [hxlm/ontologia/core.vkg.yml](hxlm/ontologia/core.vkg.yml)
  - [hxlm/ontologia/json/core.vkg.json](hxlm/ontologia/json/core.vkg.json)
    - [https://hpd.etica.ai/hxlm/ontologia/json/core.vkg.json](https://hpd.etica.ai/hxlm/ontologia/json/core.vkg.json)



<!--
- https://cirw.in/gpg-decoder/
- https://github.com/tasn/webext-signed-pages


## To check GPG signatures (integrity check, not encryption)

> NOTE: this is an **advanced usage** for the worst case scenario were an
  individual cannot use full-offline processing (like an pre-downloaded app,
  that as 2021-04-04 did not exist) **AND** (this is important) you did not
  trust the HTTPS encryption layer or are using VPN (because VPNs have power
  to break HTTPS).

- Use Chromium or Gecko (firefoxes) variant of this extension
  - https://github.com/tasn/webext-signed-pages
- After installing the extension, you will need to manually add (not replace)
  these configurations, INCLUDING the very specific huge sign key, on the
  a new field.

### First, check if the extension is working

- This page should return OK/Good green icon
  - https://stosb.com/~tom/signed-pages/good.html
- This page should return Not ok, bad, red icon
  - https://stosb.com/~tom/signed-pages/bad.html

Note that even if the developer pages of the extension did not work, you're
likely to not make it work here.


### To use with on hdp.etica.ai/hxlm-js/

Settings:

Pattern (watch out for html escaping!):
*://hdp.etica.ai/hxlm-js/*
*://git.workspace.localhost/EticaAI/HXL-Data-Science-file-formats/hxlm-js/*


Pubkey:

Contents from https://www.fititnt.org/gpg/rocha.pub

-->
