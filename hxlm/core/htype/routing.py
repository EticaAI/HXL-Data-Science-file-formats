"""hxlm.core.htype.routing
- @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from dataclasses import dataclass

from typing import (
    Union
)

from ipaddress import (
    IPv4Address,
    IPv6Address
)


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

    hxl_attribute: str = 'routinghtype'
    # @see https://en.wikipedia.org/wiki/List_of_HTTP_header_fields

    #: Union[str, IPv4Address]: external ipv4 (if any)
    ipv4: Union[str, IPv4Address] = None

    #: Union[str, IPv6Address]: external ipv6 (if any)
    ipv6: Union[str, IPv6Address] = None
