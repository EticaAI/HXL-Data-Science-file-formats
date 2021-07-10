#!/bin/sh
#===============================================================================
#
#          FILE:  prepare-urnresolver-http.sh
#
#         USAGE:  ./prepare-urnresolver-http.sh
#
#   DESCRIPTION:  (...)
#                 See also:
#                 - https://github.com/EticaAI/forum/issues/94
#                 - https://github.com/EticaAI
#                   /HXL-Data-Science-file-formats/issues/13
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2021-04-30 03:20 UTC started
#      REVISION:  ---
#===============================================================================

#### DNS preparation of urn.etica.ai ___________________________________________
# Note: the ideal usage would be create some more dedicated infrastructure.
#       But since the URNResolver, even for high demand, tend to be fast
#       This means we can use averange hosting. Not perfect, but works.

# Note 2: I'm aware of the irony of someone who know do all full stack thing
#         using shared hosting for this. But except by the IP that could be
#         changed, is possible to load balance more than one shared hosting.
#         So actually it could be more resilient than a single node on a
#         premium AWS/GCloud/Azure.

### Discovering the Direct IP of dreamhost -------------------------------------
# Using this guide https://help.dreamhost.com/hc/en-us/articles/215613517
# and very aware that it's not strictly recommended by the shared hosting
# Dreamhost to point directly to IP (instead of redirect ENTIRE etica.ai
# DNS to dreamhost) we do this tricky to discover what IP dreamhost
# would like to have
#     # fititnt@bravo:~$ dig +short urn.etica.ai @ns1.dreamhost.com
#     69.163.219.57
# Then, we defined
#     urn-real-ips.etica.ai A     69.163.219.57
#     urn.etica.ai          CNAME urn-real-ips.etica.ai  (Cloudflare proxy)

#### Shortcuts _________________________________________________________________
# ssh urneticaai@urn-real-ips.etica.ai

#### Initial setup _____________________________________________________________
# ssh urneticaai@urn-real-ips.etica.ai
# echo "https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/13" > /home/urneticaai/urn.etica.ai/public/index.html
# curl https://urn.etica.ai
#   https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/13
# python3 --version
#   Python 3.6.9
## Current version of python3 on Dreamhost is a bit old, lets use a custom
## @see https://help.dreamhost.com/hc/en-us/articles/115000702772-Installing-a-custom-version-of-Python-3
# cd ~
# mkdir tmp
# cd tmp
# wget https://www.python.org/ftp/python/3.9.4/Python-3.9.4.tgz
# tar zxvf Python-3.9.4.tgz 
# cd Python-3.9.4
# ./configure --prefix=$HOME/opt/python-3.9.4
#    (...)
#    If you want a release build with all stable optimizations active (PGO, etc),
#    please run ./configure --enable-optimizations
#    (...)
#    (Rocha note: ok, lets enable that instead of use Dreamhost commands)
# ./configure --prefix=$HOME/opt/python-3.9.4 --enable-optimizations
# make
# make install
# cd ~
# vi .bash_profile
#    export PATH=$HOME/opt/python-3.9.4/bin:$PATH
# . ~/.bash_profile
# which python3
#    /home/urneticaai/opt/python-3.9.4/bin/python3
# python3 --version
#    Python 3.9.4
# which pip3
#    /home/urneticaai/opt/python-3.9.4/bin/pip3

# python3 -m pip install virtualenv
# source venv/bin/activate
#    (venv) [culver]$

# $ (venv) python3 -m pip install --upgrade pip
# $ (venv) python3 -m pip install --upgrade hdp-toolchain
# $ (venv) python3 -m pip install falcon
# $ (venv) python3 -m pip install requests

## @see https://help.dreamhost.com/hc/en-us/articles/216137717-Python-overview
## @see https://help.dreamhost.com/hc/en-us/articles/215769578-Passenger-overview
## @see https://help.dreamhost.com/hc/en-us/articles/216385637-How-do-I-enable-Passenger-on-my-domain-
## @see https://uwsgi-docs.readthedocs.io/en/latest/tutorials/dreamhost.html
## @see https://hpincket.com/falcon-framework-api-on-dreamhosts-passenger-wsgi.html

# virtualenv venv
## Installing hdp-toolchain
# python3 -m pip install --upgrade hdp-toolchain

#### Framework (if use any) ____________________________________________________
# https://github.com/the-benchmarker/web-frameworks
#    - 87	python (3.9)	falcon (3.0)	72 561.68	80 688.49	82 140.99
#    - 100	python (3.9)	bottle (0.12)	59 473.70	63 308.93	63 999.63
#    - 104	python (3.9)	pyramid (2.0)	49 791.90	53 429.87	53 536.96
#    - 111	python (3.9)	hug (2.6)	48 227.19	51 875.27	51 585.28
#    - 114	python (3.9)	asgineer (0.8)	44 676.42	49 682.77	51 786.11
#    - 115	python (3.9)	apidaora (0.28)	44 578.72	50 726.73	51 123.79
#    - 155	python (3.9)	flask (1.1)	22 827.79	25 334.55	25 693.82
#    - 188	python (3.9)	cherrypy (18.6)	10 030.38	10 129.65	9 185.60
#    - 191	python (3.9)	tornado (6.1)	8 533.08	8 554.34	8 427.08
#    - 193	python (3.9)	django (3.2)	7 814.19	7 703.61	7 453.86
# Humm...
# Maybe https://github.com/falconry/falcon? even hug (thats is fast and we
# already use for ad-hoc expose the scripts) uses python falcon.
