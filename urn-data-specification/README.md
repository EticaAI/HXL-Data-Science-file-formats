# Uniform Resource Name DATA, `urn:data`, early drafts.

- This folder **may** have some extra information about `urn:data:` / 
  `urn:data--i:` / `urn:data--p:` as used by the [urnresolver command line interface tool](https://github.com/EticaAI/HXL-Data-Science-file-formats/blob/main/hxlm/core/bin/urnresolver.py)
- The content drafted on urn-data-specification/ is not meant to be used
  as averange explanation. _But_ do exist so many ISOs and RFCs that
  is not trivial to keep record of most of them.

### Copy from EticaAI/HXL-Data-Science-file-formats/README.md

###### Why use URN to identify resources is more than naming convention

While find _good_ URNs conventions to be used for typical datasets used on
humanitarian context is more complex than the
[ISO URN](https://tools.ietf.org/html/rfc5141) or even the
[LEX URN](https://en.wikipedia.org/wiki/Lex_(URN)) (this one
[already used in Brazil](https://www.lexml.gov.br/urn/urn:lex:br:federal:constituicao:1988-10-05;1988)),
one goal of the `urnresolver` is accept that most data shared are VERY
sensitive and private, so this this actually is the challenge. So in addition
to converting some well known public datasets related to HXL, we're already
designing to eventually be used as abstraction to scripts and tools that
without this would need to have access to real datasets.

By using URNs, at _worst case_ we're creating documentations and scripts
that a new user would need to replace by the real one of its use case. But the
ideal case is to allow exchange scripts or, when an issue happens in a new
region, the personel who prepare the data could do it and then publish also
on _private_ URN listing so others could reuse.

Note that the URN Resolver, even if it does have links to resources and not
just the contact page, the links themselves to download the real data could
still require authentication case by case. Also same URNs, if you manage to
have contact with several peers, in special for datasets that are not already
an COD, but are often needed, are likely to exist with more than one option
to use.

Deeper integration with CKAN instances and/or awareness of encrypted data
still not implemented on the current version (v0.7.3)

###### Diagrams

- See also:
  - **Uniform Resource Names (URNs)**
    - <https://tools.ietf.org/html/rfc8141>
  - **Universal Resource Identifiers in WWW**
    - <https://tools.ietf.org/html/rfc1630>

> TODO: eventually add visual diagrams here

###### Security (and privacy) considerations (for `URN:DATA`)
Since the main goal of URNs is also help with auditing and sharing of
scripts and even how to reference "best acceptable use" of exchanced data
(with special focus for private/sensitive), while the `URN:DATA` themselves
are mean to be NOT a secret and could be published on official documents, the
local implementations (aka how to resolve/redirect these URNs for real data)
need to take in account concepts that the "perfect optimization" (think
"secure from misuse" vs "protect privacy from legitimate use") often is
contraditory.

TODO: add more context

###### Disclaimer (for `URN:DATA`)

> Note: while this project, in addition to CLI tools to convert URNs to
usable tool (_"the implementation"_), also draft the logic about how to
construct potentially useful URNs reusable at International level (e.g.
what may seem as drafted _"an standard"_, think ISO, or an
_Best Current Practice_, think IETF) please do not take
EticaAI/HXL-Data-Science-file-formats... as endorsed by any organization.

> Also, authors from @EticaAI / @HXL-CPLP (both past and future ones who
cooperate directly with this project) explicitly release both software and
drafted 'how to Implement' under public domain-like licenses. Under
_ideal circumstances_ `data global namespace` (the ZZ on
`urn:data:ZZ:example`) may have more specific rules