# https://stackabuse.com/serving-files-with-pythons-simplehttpserver-module/
# python3 urn-data/data.urn.arpa/home/data-urn/public_html/http-data-urn-arpa.py


import http.server
import socketserver

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()
