"""urn-data/urn-resolver-http/passenger_wsgi.py
FILE: /home/urneticaai/urn.etica.ai/passenger_wsgi.py

See also:
- https://hpincket.com/falcon-framework-api-on-dreamhosts-passenger-wsgi.html
"""

# import os, sys
import os
import sys
import falcon
import things

# Virtual Env
INTERP = os.path.join(os.environ['HOME'], 'urn.etica.ai', 'venv', 'bin', 'python3')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Let's get this party started
# import falcon
# import things

# falcon.API instances are callable WSGI apps
api = application = falcon.API()

# Resources are represented by long-lived class instances
things_res = things.ThingsResource()

# things will handle all requests to the '/things' URL path
api.add_route('/things', things_res)
