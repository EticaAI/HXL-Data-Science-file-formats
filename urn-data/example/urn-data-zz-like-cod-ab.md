# urn-data-zz-like-cod-ab


## Quickstart

```bash

# At the moment, the Proof of Concept is only implemented on Python.
# Requires Python3 and Pip

# @see https://pypi.org/project/hdp-toolchain/

pip3 install hdp-toolchain
```


```bash

### This return an unique resource
urnresolver urn:data:xz:hxl:standard:core:hashtag
# > https://docs.google.com/spreadsheets/d/1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/pub?gid=319251406&single=true&output=csv

### What is in that file?
## Option 1: just download via browser and check it
## Option 2: using command line:
# wget -qO- (...)  = Download the thing
# (...) | head -n3  = Please 3 top lines!
wget -qO- 'https://docs.google.com/spreadsheets/d/1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/pub?gid=319251406&single=true&output=csv' | head -n3
#    Hashtag,Hashtag one-liner,Hashtag long description,Release status,Data type restriction,First release,Default taxonomy,Category,Sample HXL,Sample description
#    #valid_tag,#description +short +en,#description +long +en,#status,#valid_datatype,#meta +release,#valid_vocab +default,#meta +category,#meta +example +hxl,#meta +example +description +en
#    #access,Access ability/constraints,"Accessiblity and constraints on access to a market, distribution point, facility, etc.",Released,,1.1,,1.3. Responses and other operations,#access +type,type of access being described

### Examples using urnresolver as part of complex commands
# When using sh/bash/other terminals, one way to execute use urnresolver
#  "as alias" is with:
#     mycomand "$(urnresolver urn:data:zz:example)"
# NOTE: plase use "$( ... )" and never $( ... ), note the ""

## Using hxlselect (works with google spreadsheet, HDX, and a lot more)
# hxlselect, https://github.com/HXLStandard/libhxl-python/wiki/Select-rows-filter

hxlselect --query valid_vocab+default=+v_pcode "$(urnresolver urn:data:xz:hxl:standard:core:hashtag)"
#        Hashtag,Hashtag one-liner,Hashtag long description,Release status,Data type restriction,First release,Default taxonomy,Category,Sample HXL,Sample description
#        #valid_tag,#description+short+en,#description+long+en,#status,#valid_datatype,#meta+release,#valid_vocab+default,#meta+category,#meta+example+hxl,#meta+example+description+en
#        #adm1,Level 1 subnational area,Top-level subnational administrative area (e.g. a governorate in Syria).,Released,,1.0,+v_pcode,1.1. Places,#adm1 +code,administrative level 1 P-code
#        #adm2,Level 2 subnational area,Second-level subnational administrative area (e.g. a subdivision in Bangladesh).,Released,,1.0,+v_pcode,1.1. Places,#adm2 +name,administrative level 2 name
#        #adm3,Level 3 subnational area,Third-level subnational administrative area (e.g. a subdistrict in Afghanistan).,Released,,1.0,+v_pcode,1.1. Places,#adm3 +code,administrative level 3 P-code
#        #adm4,Level 4 subnational area,Fourth-level subnational administrative area (e.g. a barangay in the Philippines).,Released,,1.0,+v_pcode,1.1. Places,#adm4 +name,administrative level 4 name
#        #adm5,Level 5 subnational area,Fifth-level subnational administrative area (e.g. a ward of a city).,Released,,1.0,+v_pcode,1.1. Places,#adm5 +code,administrative level 5 name

## TODO: add more examples already using CODs
```

### URNResolver v1.2.1 (hdp-toolchain v0.8.7.2) tests using CODs

```bash

# urnresolver --version
    URNResolver v1.2.1
    hdp-toolchain v0.8.7.2

    URN providers:
    [user_defaults[/home/fititnt/.config/hxlm/urn/]]
    [vendor_defaults[/workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/bin/urnresolver-default.urn.yml]]
    [DDDS-NAPTR-Private[not-implemented]]
    [DDDS-NAPTR-Public[not-implemented]]


# urnresolver --urn-list-filter un:cod:ab
urn:data:un:cod:ab:{[ISO3166-1]Alpha-3}:adm1.geojson
urn:data:un:cod:ab:MOZ
urn:data:un:cod:ab:MOZ:adm1.topojson
urn:data:un:cod:ab:MOZ:adm1.geojson

# urnresolver urn:data:un:cod:ab:MOZ
https://beta.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/MOZ/versions/current/SHP/1

# urnresolver urn:data:un:cod:ab:MOZ --all
https://beta.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/MOZ/versions/current/SHP/1
https://geoboundaries.org/data/geoBoundaries-3_0_0/MOZ/ADM0/geoBoundaries-3_0_0-MOZ-ADM0-all.zip
https://biogeo.ucdavis.edu/data/gadm3.6/gpkg/gadm36_MOZ_gpkg.zip
https://geoboundaries.org/data/geoBoundaries-3_0_0/MOZ/ADM0/geoBoundaries-3_0_0-MOZ-ADM1.geojson


```

## TODO: remove this

```bash
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ urnresolver --urn-list-filter MOZ
urn:data:un:cod:ab:MOZ:adm1.geojson
urn:data:un:cod:ab:MOZ

# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ urnresolver urn:data:un:cod:ab:MOZ
https://beta.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/MOZ/versions/current/SHP/1


# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ urnresolver --all urn:data:xz:eticaai:cod:ab?fontem
https://cod.unocha.org/
https://data.humdata.org/search?ext_cod=1
https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External
https://beta.itos.uga.edu/CODV2API/
https://www.geoboundaries.org/api.html
https://gadm.org/


# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ urnresolver urn:data:un:cod:ab:MOZ
https://beta.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/MOZ/versions/current/SHP/1

# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ urnresolver urn:data:un:cod:ab:MOZ --all
https://beta.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/MOZ/versions/current/SHP/1
https://geoboundaries.org/data/geoBoundaries-3_0_0/MOZ/ADM0/geoBoundaries-3_0_0-MOZ-ADM0-all.zip
https://biogeo.ucdavis.edu/data/gadm3.6/gpkg/gadm36_MOZ_gpkg.zip
https://geoboundaries.org/data/geoBoundaries-3_0_0/MOZ/ADM0/geoBoundaries-3_0_0-MOZ-ADM1.geojson
```