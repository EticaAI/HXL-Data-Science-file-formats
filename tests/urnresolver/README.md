# tests/urnresolver
The test files on this directory are used when you want to explicitly enforce
an exact match of an URN in offline mode.

# Local files

## CSV

## JSON

## YAML

# Remote access

## well-know
> TODO: we should also check the https://www.iana.org/assignments/well-known-uris/well-known-uris.xhtml
  (Emerson Rocha, 2021-03-03 07 12:01 UTC)

If an resource is at one web server (or the webserver is reference for
other servers) and the domain is example.org, default place to search for a
file would be https://example.org/.well-known/urn.txt

The recommended place to put actual reference for URNs that are meant to be
for public access would be under https://example.org/.well-known/urn/ directory.
