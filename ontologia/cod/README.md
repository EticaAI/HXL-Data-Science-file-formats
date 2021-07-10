# ontologia/cod: Common Operational Datasets

**Note: the folder ontologia/cod/ do not contain the CODs themselves; This is
a taxonomy about how to parse COD files, in special COD-AB.**

> This is a DRAFT! (Emerson Rocha, 2021-04-22 21:56 UTC

> Trivia:
> - "commūne"
>   - https://en.wiktionary.org/wiki/communis#Latin
> - "opus"
>   - https://en.wiktionary.org/wiki/opus#Latin
> - "datum"
>   - https://en.wiktionary.org/wiki/datum#English
> - "filum"
>   - https://en.wiktionary.org/wiki/filum#Latin
>   - https://en.wiktionary.org/wiki/file#English
>     - "File": English -> Etymology -> From Latin fīlum (“thread”). Doublet of file.
> - "typum"
>   - https://en.wiktionary.org/wiki/typus#Latin
> - "statisticum" **(WARNING: this is new latin; needs revision)**
>   - https://en.wiktionary.org/wiki/statistics#English
> - "populātiōnem"
>   - https://en.wiktionary.org/wiki/populatio#Latin
> - "administrātum"
>   - https://en.wiktionary.org/wiki/administratus#Latin
> - "thēsaurum"
>   - https://en.wiktionary.org/wiki/thesaurus#Latin
> - "rēgulāre"
>   - https://en.wiktionary.org/wiki/regularis#Latin
>   - English: "regular expression"
> - "expressiōnem"
>   - https://en.wiktionary.org/wiki/expressio#Latin
>   - English: "regular expression"

> TODO: discover term for "boundary" (https://en.wiktionary.org/wiki/boundary).
>       We may need to force some good back-formation for this term
>       (Emerson Rocha, 2021-04-22 21:08 UTC)

## What are CODs?

[![](http://img.youtube.com/vi/CFUs8S0MPIY/0.jpg)](http://www.youtube.com/watch?v=CFUs8S0MPIY "Common Operational Datasets (CODs)")

- https://cod.unocha.org/

## Data set providers

> Note: this list contains generic dataset providers, not just OCHA.

### `COD-AB`: Administrative Boundaries

```yaml
# urnresolver --all urn:data:xz:eticaai:cod:ab?fontem
- urn: "urn:data:xz:eticaai:cod:ab?fontem"
  source:
    - https://cod.unocha.org/
    - https://data.humdata.org/search?ext_cod=1
    - https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External
    - https://beta.itos.uga.edu/CODV2API/
    - https://www.geoboundaries.org/api.html
    - https://gadm.org/

```

### `COD-PS`: Population Statistics

> TODO: `COD-PS`: Population Statistics

#### CODV2API, Population Statistics

> https://beta.itos.uga.edu/CODV2API/api/v1/Themes/Population%20Statistics
> TODO: https://beta.itos.uga.edu/CODV2API/api/v1/Themes


### (IGNORE THIS PART) Temp, remove

> https://github.com/UGA-ITOSHumanitarianGIS/mapservicedoc/blob/master/Data/hdxCODData.json

> - https://beta.itos.uga.edu/CODV2API/api/v1/locations/HN01