#!/usr/bin/env python3
"""urn-data/urn-resolver-http/passenger_wsgi.py
FILE: /home/urneticaai/urn.etica.ai/passenger_wsgi.py

See also:
- https://hpincket.com/falcon-framework-api-on-dreamhosts-passenger-wsgi.html
"""

import os
import sys


# print (sys.version)

# Virtual Env
# INTERP = os.path.join(os.environ['HOME'], 'urn.etica.ai', 'venv', 'bin', 'python')
INTERP = "/home/urneticaai/venv/bin/python"
if sys.executable != INTERP:
    # print (sys.version)
    os.execl(INTERP, INTERP, *sys.argv)

# Let's get this party started
import falcon  # pylint: disable=wrong-import-position
import things  # pylint: disable=wrong-import-position

# falcon.API instances are callable WSGI apps
api = application = falcon.API()

# Resources are represented by long-lived class instances
things_res = things.ThingsResource()

# things will handle all requests to the '/things' URL path
api.add_route('/things', things_res)
