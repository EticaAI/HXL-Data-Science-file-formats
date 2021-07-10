"""hxlm.core.htype.routing
- @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9

The main objective is abstract non-core subpackage of hxlm to be used as
reference to Routing resources.

To implementers:
- While hxlm.core.htype.routing (and hxlm.routing) are early-drafts/
  working-drafts, the idea behind RoutingHtype (that professionals who work
  with internet routing) can help to protect sites who serve public HXLated
  content.
    - For "just" cache, you actually do not need at all to implement  this
      code or automate with other tools. In the middle of urgencies, do you
      think and make it work.
- The concept of a ideal of an HRouting work to proxy/filter data between
  different private networks require both knowledge of HXL and how to exchange
  data with very sensitive content. This means that even if implementations do
  become more than proof of concept, this may not become public.
    - At least not until do exist huge demand to a point of divide
      responsability of computers 'who route' from the ones 'who undestand'
      the HXL.

TODO: maybe rewrite from *RoutingHtype to HRouting
      (Emerson Rocha, 2021-02-27 04:53)

TODO: https://www.manrs.org/wp-content/uploads/2018/03/MANRS-BCOP-20170125.pdf
TODO: https://www.peeringdb.com/


Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from dataclasses import dataclass, asdict

from typing import (
    List,
    Type,
    Union
)

from ipaddress import (
    IPv4Address,
    IPv6Address
)

# from hxlm.core.constant import (
#     HDSL3
# )

HRCACHE = "HRCACHE"  # Please cache this resource (default? Maybe 1H? Max 24h?)
HRPURGE = "HRPURGE"  # Please purge this resource (if still have it)
HRQOSME = "HRQOSME"  # If you're under HEAVY LOAD, priorize-me to cache you


@dataclass(init=True, repr=True, eq=True)
class RoutingHtype:
    """RoutingHtype is an specialized X-Forward-By, "X-HRouting-By"

    The main objective is abstract non-core subpackage to be used as reference
    to Routing.

    See "Mutually Agreed Norms for Routing Security (MANRS)" (TL;DR: a global
    initiative, supported by the Internet Society, that provides crucial fixes
    to reduce the most common routing threats.)

    @see https://www.manrs.org/about/
    @see https://www.youtube.com/watch?v=nJINk5p-HEE
    @see https://www.youtube.com/watch?v=IuY6wqTm35U
    """

    #: Most Htype (when have) have more than one attribute.
    #  But RoutingHtype is simpler, so one is enough. Subclasses can override
    hxl_attribute: str = 'routinghtype'

    #: Union[str, IPv4Address]: external ipv4 (if any)
    ipv4: Union[str, IPv4Address] = None

    #: Union[str, IPv6Address]: external ipv6 (if any)
    ipv6: Union[str, IPv6Address] = None

    #: By default, since this class could be used in any X-Forward-By or
    #  proxy, so we default to False
    is_hrouting_aware: bool = False


@dataclass(init=True, eq=True)
class ResourceRoutingHtype:
    """Abstraction to an resource (often _just_ an URL)

    TODO: this is an draft. But is here as reference on how to abstract
          (Emerson Rocha, 2021-02-27 03:57 UTC)
    """

    url: str = None


@dataclass(init=True, repr=True, eq=True)
class PleaseRoutingHtype:
    """Abstraction of an request from one HRouting to other HRouting peers
    """
    #: me, an HRouting
    requester: Type[RoutingHtype] = None
    # resquested_by: ...
    trusted_by: Union[Type[RoutingHtype], ResourceRoutingHtype] = None
    requested: Type[RoutingHtype] = None
    resources: List[Type[ResourceRoutingHtype]] = None
    please: str = 'HRQOSME'

    def as_object(self):
        return asdict(self)


# @see https://www.peeringdb.com/advanced_search?country__in=BR&reftag=ix
