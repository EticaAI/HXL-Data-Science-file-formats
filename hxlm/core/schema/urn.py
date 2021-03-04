"""hxlm.core.schema.urn.HURN

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


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from typing import (
    Type,
    Union
)

__all__ = ['HURN']

HXLM_CORE_SCHEMA_URN_PREFIX = "urn:x-hurn:"


class HURN:
    """URN is an abstraction to Uniform Resource Name (URN)
    @see https://tools.ietf.org/html/rfc2141
    @see https://www.iana.org/assignments/urn-namespaces/urn-namespaces.xhtml
    """

    def __init__(self):
        self.kind: str = 'HURN'

    @staticmethod
    def is_valid(urn: Union[str, Type['HURN']], strict=True):
        """Check if is an valid HXLM-like URN (must have x-hurn)

        @see urn:ietf:rfc:2141

        Args:
            urn (Union[str, Type['HURN']]): The item to check if is valid
            strict (bool): Check if is not just an urn: but an hurn

        Returns:
            [type]: [description]
        """
        if isinstance(urn, HURN):
            return True

        if isinstance(urn, str):
            urn_lower = urn.lower()
            if not strict and urn_lower.startswith('urn:'):
                return True
            if urn_lower.startswith(HXLM_CORE_SCHEMA_URN_PREFIX):
                return True

        return False
