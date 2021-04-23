#!/usr/bin/env python3

# cd /home/data-urn/.local/share/urn/urn-http/
#     cd /home/fititnt/.local/share/urn/urn-http/

# https://stackabuse.com/serving-files-with-pythons-simplehttpserver-module/
# python3 urn-data/data.urn.arpa/home/data-urn/public_html/http-data-urn-arpa.py
# https://gunicorn.org/

# pip3 install gunicorn
# gunicorn -w 4 --bind 127.0.0.1:
# 8888 http_data_urn_arpa:app
# http://data.urn.arpa/


# https://docs.gunicorn.org/en/stable/run.html
def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    print(environ)
    print(start_response)
    return iter([data])
