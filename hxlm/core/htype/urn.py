"""hxlm.core.htype.urn

attr.urn:
 "A Uniform Resource Name (URN) is a Uniform Resource Identifier (URI)
  that uses the urn scheme. URNs are globally unique persistent
  identifiers assigned within defined namespaces so they will be
  available for a long period of time, even after the resource which
  they identify ceases to exist or becomes unavailable.[1] " -- Wikipedia
@see https://en.wikipedia.org/wiki/Uniform_Resource_Name
RFC:
@see https://tools.ietf.org/html/rfc1737
@see https://tools.ietf.org/html/rfc2141
Lex prefix by Brazil and Itally
Example: lexml.gov.br/urn/urn:lex:br:federal:lei:2008-06-19;11705
@see https://en.wikipedia.org/wiki/Lex_(URN)
ISO
@see https://tools.ietf.org/html/rfc5141

Other libraries to see
- https://github.com/lexml/lexml-vocabulary


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from dataclasses import dataclass

from typing import (
    Type,
    Union
)
# __all__ = ['HURN']

HXLM_CORE_SCHEMA_URN_PREFIX = "urn:x-hurn:"


def is_urn(urn: Union[str, Type['URNHtype']], prefix: str = 'urn:') -> bool:
    """Check if an item is a valid formatted URN

    If the urn is object from a direct or indirect class based on URNHtype
    will use urn.is_valid()

    Args:
        urn (Union[str, Type['URNHtype']):  The item to check if is valid
        prefix (str, optional): URN prefix. Defaults to 'urn:'

    Returns:
        boolean: if is an valid URN
    """

    if isinstance(urn, URNHtype):
        return urn.is_valid()
    if isinstance(urn, str):
        urn_lower = urn.lower()
        return urn_lower.startswith(prefix)
    return False


@dataclass(init=True, eq=True)
class URNHtype:
    """URNHtype is an abstraction to Uniform Resource Name (URN)

    Can be extended to use other prefixes (like the RFCs, e.g.
    urn:ietf:rfc:2141)

    @see https://tools.ietf.org/html/rfc2141
    @see https://www.iana.org/assignments/urn-namespaces/urn-namespaces.xhtml
    """

    # valid_prefix: str = 'urn'  # If want more generic check
    valid_prefix: str = 'urn:x-hurn:'
    value: str = None

    def is_valid(self):
        """Check if current URN is valid (defaults to x-hurn)

        Returns:
            bool: if the current URN is valid
        """
        if self.value:
            urn_lower = self.value.lower()
            return urn_lower.startswith(self.valid_prefix)
        return False


class URNResolver:
    """URN is an abstraction to Uniform Resource Name (URN)
    @see https://tools.ietf.org/html/rfc2141
    @see https://www.iana.org/assignments/urn-namespaces/urn-namespaces.xhtml
    """

    def __init__(self):
        self.kind: str = 'HURNResolver'


# class IETFHURNResolver(HURNResolver):
