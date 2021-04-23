#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  data-urn-arpa.py
#
#         USAGE:  data-urn-arpa.py (...)
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                     - https://github.com/rthalley/dnspython
#                     - https://github.com/greg-hellings/dnszone
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  Etica.AI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v0.1
#       CREATED:  2021-04-23 22:05 UTC v0.1 started
#      REVISION:  ---
# ==============================================================================

# https://github.com/rthalley/dnspython/blob/master/dns/rdtypes/IN/NAPTR.py

# ./urn-data/data.urn.arpa/data-urn-arpa.py

# print('oi oi oi')

# https://github.com/rthalley/dnspython/blob/master/examples/name.py

import dns.name

n = dns.name.from_text('www.dnspython.org')
o = dns.name.from_text('dnspython.org')
print(n.is_subdomain(o))         # True
print(n.is_superdomain(o))       # False
print(n > o)                     # True
rel = n.relativize(o)            # rel is the relative name www
n2 = rel + o
print(n2 == n)                   # True
print(n.labels)                  # ['www', 'dnspython', 'org', '']


import dns.reversename
n = dns.reversename.from_address("127.0.0.1")
print(n)
print(dns.reversename.to_address(n))