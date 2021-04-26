# Uniform Resource Name DATA, `urn:data`, early drafts.

> Note: urn-data/ is a working draft

---

<!-- TOC depthFrom:2 -->

- [Relevant RFCs](#relevant-rfcs)
- [Relevant implementations/references](#relevant-implementationsreferences)
    - [Internal notes](#internal-notes)

<!-- /TOC -->

---

<!--

cat "$(urnresolver urn:data:xz:eticaai:ontologia:codicem:locum)" | head -n3
hxlcut --include country+code+v_iso2 "$(urnresolver urn:data:xz:eticaai:ontologia:codicem:locum)"

hxlselect --query valid_vocab+default=+v_pcode "$(urnresolver urn:data:xz:eticaai:ontologia:codicem:locum)"

urn:data:xz:eticaai:ontologia:codicem:locum?=|$(hxlcut --include=country+code+v_iso2)

cat "$(urnresolver urn:data:xz:eticaai:ontologia:codicem:locum)" | hxlcut --include=country+code+v_iso2
cat "$(urnresolver urn:data:xz:eticaai:ontologia:codicem:locum)" | hxlcut --include=country+code+v_iso2,country+code+v_iso3,country+code+num+v_m49

# urn:data:xz:eticaai:ontologia:codicem:scriptum?=|$(hxlcut --include=vocab+code+v_iso15924+text)
cat "$(urnresolver urn:data:xz:eticaai:ontologia:codicem:scriptum)" | hxlcut --include=vocab+code+v_iso15924+text
# urn:data:xz:eticaai:ontologia:codicem:scriptum?=|$(hxlcut --include=vocab+code+v_iso15924+number)
cat "$(urnresolver urn:data:xz:eticaai:ontologia:codicem:scriptum)" | hxlcut --include=vocab+code+v_iso15924+text,vocab+code+v_iso15924+number

#vocab+code+v_iso15924+text
urn:data:xz:eticaai:ontologia:codicem:locum?=|$(hxlcut --include=country+code+v_iso2)


-->
## Relevant RFCs

- **Uniform Resource Names (URNs)**
  - https://tools.ietf.org/html/rfc8141
- (work in progress) **"A Uniform Resource Name (URN) Namespace for
  Sources of Law (LEX)"**
  - https://tools.ietf.org/html/draft-spinosa-urn-lex-13
- **Dynamic Delegation Discovery System (DDDS) Part Four: The Uniform Resource
   Identifiers (URI) Resolution Application**
   - https://www.rfc-editor.org/rfc/rfc3404.html


## Relevant implementations/references

- **"Regex which matches URN by rfc8141"**
  - https://stackoverflow.com/questions/59032211/regex-which-matches-urn-by-rfc8141
  - https://regex101.com/r/SxOh4R/1

### Internal notes

> q-component
>
> (...)
>
>  Consider the hypothetical example of passing parameters to an
   application that returns weather reports from different regions or
   for different time periods.  This could perhaps be accomplished by
   specifying latitude and longitude coordinates and datetimes in the
   URN's q-component, resulting in URNs such as the following.
>
>      urn:example:weather?=op=map&lat=39.56
>         &lon=-104.85&datetime=1969-07-21T02:56:15Z
>
>   If this example resolved to an HTTP URI, the result might look like:
>
>      https://weatherapp.example?op=map&lat=39.56
>         &lon=-104.85&datetime=1969-07-21T02:56:15Z
>
> Source: rfc8141 https://tools.ietf.org/html/rfc8141#section-2.3.2


> 2.3.3.  f-component
>
> (...)
>
>  Consider the hypothetical example of obtaining resources that are
   part of a larger entity (say, the chapters of a book).  Each part
   could be specified in the f-component, resulting in URNs such as:
>
>   urn:example:foo-bar-baz-qux#somepart
>
> Source: rfc8141 https://tools.ietf.org/html/rfc8141#section-2.3.3

<!--

- https://tools.ietf.org/html/draft-spinosa-urn-lex-13
- https://github.com/greg-hellings/dnszone
- https://github.com/rthalley/dnspython
- https://pypi.org/project/designate/
  - https://docs.openstack.org/api-ref/dns/
-->
<!--

 ## (ignore this part) Draft


- This folder **may** have some extra information about `urn:data:` / 
  `urn:data--i:` / `urn:data--p:` as used by the [urnresolver command line interface tool](https://github.com/EticaAI/HXL-Data-Science-file-formats/blob/main/hxlm/core/bin/urnresolver.py)
- The content drafted on urn-data-specification/ is not meant to be used
  as averange explanation. _But_ do exist so many ISOs and RFCs that
  is not trivial to keep record of most of them.


> This entire section is just a draft

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

-->