# ~/apitest.hpincket.com/things.py

import falcon

# Testing caches
# - https://docs.trafficserver.apache.org/en/latest/admin-guide/configuration/cache-basics.en.html
# - https://tools.ietf.org/html/rfc7234
# - https://support.cloudflare.com/hc/en-us/articles/115003206852-Understanding-Origin-Cache-Control

# - max-age=seconds
#   - Max age, but for browsers
# - s-maxage=seconds
#   - Indicates that, in shared caches, the maximum age specified by this
#     directive overrides the maximum age specified by either the max-age
#     directive or the Expires header field.
# - stale-while-revalidate=seconds
#   - When present in an HTTP response, indicates that caches may serve the
#     response in which it appears after it becomes stale, up to the indicated
#     number of seconds since the resource expired.
#  - stale-if-error=seconds
#    Indicates that when an error is encountered, a cached stale response may
#    be used to satisfy the request, regardless of other freshness information.
# - must-revalidate
#    Indicates that once it has become stale, a cache (client or proxy) must
#    not use the response to satisfy subsequent requests without successful
#    validation on the origin server.


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        # resp.set_header('cache-control', 'public, must-revalidate')
        resp.set_header('cache-control', 'public')
        resp.set_header('max-age', 120)  # 2min of cache (client side)

        resp.set_header('s-maxage', 600) # Cache proxies can keep resources
                                         # for 5 min max

        # If resource is stale, for at least 2 min serve to client as it is,
        # but revalidate for the next resource
        resp.set_header('stale-while-revalidate', 120)

        # On worst case scenario (total clusterf**k), serve as long as 7
        # Days any old content
        resp.set_header('stale-if-error', 604800)  # 7 days

        resp.delete_header('vary')

        resp.text = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

