#!/bin/sh

# cd urn-data/rfc/
# /make.sh

# @see https://github.com/cabo/kramdown-rfc2629

kramdown-rfc2629 draft-rocha-urn-data-00.md > draft-rocha-urn-data-00.xml

xml2rfc draft-rocha-urn-data-00.xml