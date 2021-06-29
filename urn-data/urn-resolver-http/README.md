# urn-data/urn-resolver-http/README.md

> See also
> - [../../prepare-urnresolver-http.sh](../../prepare-urnresolver-http.sh)
> - [EticaAI/forum/#94: EticaAI urn:data: URN Resolver; MVP of HTTP redirect (maybe urn.etica.ai or urn.etica.dev)](https://github.com/EticaAI/forum/issues/94)
> - [EticaAI/HXL-Data-Science-file-formats#13: urnresolver: Uniform Resource Names - URN Resolver 13](https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/13)

## Internal notes
### `https://urn.etica.ai`
- Additional notes on [../../prepare-urnresolver-http.sh](../../prepare-urnresolver-http.sh)


```bash
# cd urn-data/urn-resolver-http || exit

# rsync --archive --verbose passenger_wsgi.py urneticaai@urn-real-ips.etica.ai:/home/urneticaai/urn.etica.ai/passenger_wsgi.py
# rsync --archive --verbose things.py urneticaai@urn-real-ips.etica.ai:/home/urneticaai/urn.etica.ai/things.py

rsync --archive --verbose urn-data/urn-resolver-http/ urneticaai@urn-real-ips.etica.ai:/home/urneticaai/urn.etica.ai/

```

Debug
```bash
## Debugging
ssh urneticaai@urn-real-ips.etica.ai
source venv/bin/activate
(venv) $ touch /home/urneticaai/tmp/restart.txt
(venv) $ tail logs/urn.etica.ai/http/error.log

## Logs
tail -f /home/urneticaai/logs/urn.etica.ai/http/error.log
tail -f /home/urneticaai/logs/urn.etica.ai/http/access.log

# @see https://help.dreamhost.com/hc/en-us/articles/215317698-Django-troubleshooting
(venv) $ pkill python3
(venv) $ touch /home/urneticaai/urn.etica.ai/passenger_wsgi.py
(venv) $ touch /home/urneticaai/tmp/restart.txt
(venv) $ touch /home/urneticaai/urn.etica.ai/tmp/restart.txt
```

```bash

# Noop; Dreamhost do not allow direct access after be aware that cloudflare is serving

curl --insecure -I https://urn.etica.ai/things --resolve urn.etica.ai:69.163.219.57
# curl --insecure -I https://urn.etica.ai/things --resolve urn.etica.ai:443:69.163.219.57

## Disable cloudflare temporary

sudo vim /etc/hosts
# 69.163.219.57   urn.etica.ai
curl --insecure -I https://urn.etica.ai/things
```