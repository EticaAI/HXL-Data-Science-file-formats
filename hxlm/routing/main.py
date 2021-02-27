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
    # 192.0.2.0 = TEST-NET-1
    # hpeer = hrouting.RoutingHtype(ipv4='192.0.2.0')
    hpeer = hrouting.RoutingHtype(ipv4=hpeer)
    url_ = hrouting.ResourceRoutingHtype(url=url)

    please = hrouting.PleaseRoutingHtype(
        requester=me, requested=hpeer, please='HRCACHE', resources=url_)
    # me.ipv4 = get_external_ip()
    # print(me, please)
    return please

# TODO: draft
#         - https://github.com/peeringdb/peeringdb-py
#         - https://github.com/peeringdb/peeringdb-py
#         - https://www.ripe.net/manage-ips-and-asns/db
#         - https://github.com/RIPE-NCC/ripe-atlas-cousteau
#         - https://pypi.org/project/geoip2/
