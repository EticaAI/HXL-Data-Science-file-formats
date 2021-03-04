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

# from dataclasses import dataclass, field, InitVar
from dataclasses import dataclass, InitVar

from typing import (
    Type,
    Union
)
# __all__ = ['HURN']

HXLM_CORE_SCHEMA_URN_PREFIX = "urn:x-hurn:"
# HXLM_CORE_URN_DICT = {
#     'urn:': cast_urn
# }


def cast_urn(urn: Union[str,
                        Type['GenericUrnHtype']]) -> Type['GenericUrnHtype']:
    """Helper to cast an string to the most specific UrnHtype abstraction know

    If you are extending this library consider implement your own custom
    cast_urn. In theory would be possible to discover all classes that
    extend GenericUrnHtype and try somewhat bruteforce the more specific type
    but this, if not a bit slower, may require deeper safety checks.

    Example:
        urn_ago = cast_urn('urn:x-hdp:cod:ps:ago')
        print(urn_ago.get_resources())
        # {'urls': ['https://data.humdata.org/'],
        #   'message': 'No specific result found. Try manually with the urls'}

    Returns:
        Type['GenericUrnHtype']: Return the more specific UrnHtype know upfront
    """
    if isinstance(urn, GenericUrnHtype):
        # print('DEBUG: cast_urn already is an instance. Ok.')
        return urn

    urn_lower = urn.lower()

    if urn_lower.startswith('urn:x-hdp:') or urn_lower.startswith('urn:hdp:'):
        return HdpUrnHtype(value=urn)

    if urn_lower.startswith('urn:'):
        return GenericUrnHtype(value=urn)

    return None


def is_urn(urn: Union[str, Type['GenericUrnHtype']],
           prefix: str = 'urn:') -> bool:
    """Check if an item is a valid formatted URN

    If the urn is object from a direct or indirect class based on URNHtype
    will use urn.is_valid()

    Args:
        urn (Union[str, Type['URNHtype']):  The item to check if is valid
        prefix (str, optional): URN prefix. Defaults to 'urn:'

    Returns:
        boolean: if is an valid URN
    """

    if isinstance(urn, GenericUrnHtype):
        return urn.is_valid()
    if isinstance(urn, str):
        urn_lower = urn.lower()
        return urn_lower.startswith(prefix)
    return False


# TODO: check some nice way to work with dataclasses allowing override
#       valid_prefix.
#       See https://www.infoworld.com/article/3563878
#       /how-to-use-python-dataclasses.html
#       (Emerson Rocha, 2021-03-04 17:54 YTC)

@dataclass(init=True, eq=True)
class GenericUrnHtype:
    """GenericUrnHtype is an abstraction to Uniform Resource Name (URN)

    Since the GenericUrnHtype is more optionated, users are likely to preffer
    this one if do not want to replace the entire HrnHtype abstractions.


    @see https://tools.ietf.org/html/rfc2141
    @see https://www.iana.org/assignments/urn-namespaces/urn-namespaces.xhtml
    """

    #: all URNs must start with 'urn:', so we initialize with this
    valid_prefix: InitVar[str] = 'urn:'

    #: The string value of the URN
    value: str = None

    @staticmethod
    # def get_resolver_documentation(self) -> dict:
    def get_resolver_documentation() -> dict:
        result = {
            'urls': [
                "https://tools.ietf.org/html/rfc1737",
                "https://tools.ietf.org/html/rfc2141",
                "https://www.iana.org/assignments/urn-namespaces",
            ]
        }
        return result

    # def get_resources(self) -> dict:
    def get_resources(self):
        """Return resources assciated to this URN

        Raises:
            NotImplementedError: Implement-me
        """
        raise NotImplementedError

    def is_valid(self):
        """Check if current URN is valid (defaults to x-hurn)

        Returns:
            bool: if the current URN is valid
        """
        if self.value:
            urn_lower = self.value.lower()
            return urn_lower.startswith(self.valid_prefix)
            # if self.valid_prefix:
            #     return urn_lower.startswith(self.valid_prefix)
            # else:
            #     return urn_lower.startswith('urn:')
        return False


class HdpUrnHtype(GenericUrnHtype):
    """Parses URNs prefixed with 'urn:x-hdp:'

    TODO: at this moment the HdpUrnHtype is too generic. But ideally should
          allow several more specific namespaces AFTER the baseline
          functionality be implemented.
          (Emerson Rocha, 2021-03-04 18:34 UTC)

    Args:
        GenericUrnHtype (GenericUrnHtype): The generic UrnHtype
    """

    valid_prefix: str = 'urn:x-hurn:'

    def get_resolver_documentation(self) -> dict:
        result = {
            'urls': [
                "https://github.com/EticaAI/HXL-Data-Science-file-formats",
                # "https://tools.ietf.org/html/rfc1737",
                # "https://tools.ietf.org/html/rfc2141",
                # "https://www.iana.org/assignments/urn-namespaces",
            ]
        }

        return result

    def get_resources(self) -> dict:
        """Return resources associated with the current URN.

        Since baseline functionality with URNs (in special without API calls
        to external webservices) may be hard, the get_resources always
        return a dict.

        Returns:
            dict: Result
        """

        result = {
            'urls': [
                "https://data.humdata.org/",
                # "https://tools.ietf.org/html/rfc1737",
                # "https://tools.ietf.org/html/rfc2141",
                # "https://www.iana.org/assignments/urn-namespaces",
            ],
            'message': "No specific result found. Try manually with the urls",
        }
        return result


class IetfUrnHtype(GenericUrnHtype):
    """Parses URNs prefixed with 'urn:ietf:'

    TODO: do an MVP (Emerson Rocha, 2021-03-04 19:48 UTC)

    Args:
        GenericUrnHtype (GenericUrnHtype): The generic UrnHtype
    """

    valid_prefix: str = 'urn:ietf:'
