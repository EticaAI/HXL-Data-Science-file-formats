"""hxlm.routing is (TODO: document)
"""

from requests import get
import hxlm.core.htype.routing as hrouting


def routing_info():
    print('We <3 MANRS')


def get_external_ip():
    ip = get('https://api64.ipify.org/').text
    return ip


def request_cache_resource(hpeer: str, me=None, url: str = None):
    """(draft) Prepare an request for an peer

    Example:
        please = request_cache_resource(
            url='https://example.org/dataset/data.csv',
            hpeer='192.0.2.0'))

    Args:
        url (str): URL to ask to cache
        hpeer (str): A single HRouting peer
        me (str): External url of this Hproxy

    Returns:
        PleaseRoutingHtype: An PleaseRoutingHtype abstraction
    """

    if not me:
        me = get_external_ip()

    me = hrouting.RoutingHtype(ipv4=me)
    hpeer = hrouting.RoutingHtype(ipv4=hpeer)
    url_ = hrouting.ResourceRoutingHtype(url=url)

    please = hrouting.PleaseRoutingHtype(
        requester=me, requested=hpeer, please='HRCACHE', resources=url_)
    return please.as_object()


def request_priority_access(requester: str, trusted_by: str = None,
                            url: str = None):
    """(draft) Request priority to access data (eg Overloaded server allow you)

    Example:
        please = hxlm.routing.request_priority_access(
                    url='https://example.org/dataset/data.csv',
                    requester='192.0.2.0')

    Args:
        requester (str): For which external IP priority is requested
        trusted_by (str): Reference who can trust you
        url (str): Specify an resource. Optional.

    Returns:
        PleaseRoutingHtype: An PleaseRoutingHtype abstraction
    """
    trusted_by_ = None
    url_ = None

    if not requester:
        requester = get_external_ip()

    requester_ = hrouting.RoutingHtype(ipv4=requester)

    if trusted_by:
        trusted_by_ = hrouting.RoutingHtype(ipv4=trusted_by)
    if url:
        url_ = hrouting.ResourceRoutingHtype(url=url)

    please = hrouting.PleaseRoutingHtype(
        requester=requester_, trusted_by=trusted_by_, please='HRQOSME',
        resources=url_)
    return please.as_object()

# TODO: draft
#         - https://github.com/peeringdb/peeringdb-py
#         - https://github.com/peeringdb/peeringdb-py
#         - https://www.ripe.net/manage-ips-and-asns/db
#         - https://github.com/RIPE-NCC/ripe-atlas-cousteau
#         - https://pypi.org/project/geoip2/
