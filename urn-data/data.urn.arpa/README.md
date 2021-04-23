# urn-data/data.urn.arpa/README.md

> NOTE: All contents from urn-data/data.urn.arpa/ are drafts.

> NOTE: concents from urn-data/data.urn.arpa are not intented to be used on
        production. Or, even if they work, please do not use outside air-gapped
        network. (Emerson Rocha, 2021-04-23 04:09 UTC)



```bash

cd /home/fititnt/.local/share/urn/urn-http/
gunicorn -w 4 --bind 127.0.0.1:8888 http_data_urn_arpa:app

curl http://data.urn.arpa/urn:data:xz:eticaai:cod:ab?fontem
curl http://data.urn.arpa/urn:data:xz:hxl:standard:core:attribute

```