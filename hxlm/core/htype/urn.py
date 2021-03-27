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
- https://pypi.org/project/rfc3987/

# TODO: for things that need to be named by hashes (think security or
#       validation) instead of urn: the ni: could be used
#       @see https://tools.ietf.org/html/rfc6920
#       (Emerson Rocha, 2021-03-05 16:57 UTC)

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# from dataclasses import dataclass, field, InitVar
from dataclasses import dataclass, InitVar

from typing import (
    Type,
    Union
)
# __all__ = ['HURN', 'GenericUrnHtype']

# HXLM_CORE_SCHEMA_URN_PREFIX = "urn:x-hdp:"
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

    if urn_lower.startswith('urn:data:') or \
            urn_lower.startswith('urn:data--i:') or \
            urn_lower.startswith('urn:data--p:'):
        return DataUrnHtype(value=urn)

    if urn_lower.startswith('urn:x-hdp:') or urn_lower.startswith('urn:hdp:'):
        return HdpUrnHtype(value=urn)

    if urn_lower.startswith('urn:ietf:'):
        return IetfUrnHtype(value=urn)

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

    #: the namespace identifier, and may include letters, digits, and -.
    nid: InitVar[str] = None  # Example: 'ietf' on 'urn:ietf:rfc:2141'

    # Used by DataUrnHtype
    # nid_attr: InitVar[str] = None  # Example: 'i' on 'urn:data--i:un:locode'
    # nid_attr_spliter: InitVar[str] = '--'  # Example: '--' on 'urn:data--i:'

    #: <NSS> is the Namespace Specific String
    nss: InitVar[str] = None  # Example: 'rfc:2141' on 'urn:ietf:rfc:2141'

    #: The nss broken in logical parts. Varies by implementation
    nss_parsed: InitVar[dict] = {}

    #: The string value of the URN
    value: str = None

    def about(self, key: str = None):
        """Quick summary of the current object.

        Args:
            key (str, optional): Exact key to return.

        Returns:
            dict|Any: Simple python dictionary
        """
        about = {}
        about['nid'] = self.nid
        about['nss'] = self.nss
        if key:
            if key in about:
                return about[key]
            return None
        return about

    def prepare(self, strict: bool = True):
        """Prepare the current URN NSS (Namespace Specific String)

        Args:
            strict (bool, optional): If raise SyntaxError. Defaults to True.

        Raises:
            SyntaxError: raise if the value is not valid

        Returns:
            [self, False]: Return self (allow chaining) or false if less strict
        """
        if self.is_valid():
            parts = self.value.split(':')
            self.nss = self.value.replace('urn:' + parts[1] + ':', '', 1)
            self.nid = parts[1].lower()
            self.nss_parsed['nid'] = self.nid
            self.nss_parsed['nss'] = self.nss
            # self.nss_parsed['_raw'] = self.nss
        elif strict:
            raise SyntaxError(self.value + ' not is_valid()')
        else:
            return False

        return self

    @staticmethod
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
        """Check if current URN is valid (defaults to x-hdp)

        Returns:
            bool: if the current URN is valid
        """

        if self.value:
            urn_lower = self.value.lower()
            return urn_lower.startswith(self.valid_prefix)
        return False


class DataUrnHtype(GenericUrnHtype):
    """Parses URNs prefixed with 'urn:data:', 'urn:data-i:' and 'urn:data-p:'

    TODO: draft some sort of Augmented Backus–Naur form ABNF for `urn:data:`
          @see https://tools.ietf.org/html/rfc5234
          @see https://cs.stackexchange.com/questions/127499
          @see https://tools.ietf.org/tools/bap/abnf.cgi
          @see http://www.quut.com/abnfgen/
          (Emerson Rocha, 2021-03-05 21:03 UTC)

Temp, delete this
http://www.quut.com/abnfgen/:
cat /workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/GRAMMA
ring = 1*12("ding" SP) "dong"
abnfgen /workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/GRAMMAR
    Ding dinG dINg DONg

https://github.com/antlr/antlr4/blob/master/doc/getting-started.md


Maybe?
- comparisons
  - https://en.wikipedia.org/wiki/Comparison_of_parser_generators
- BNF,EBNF & ABNF
  - https://github.com/igochkov/vscode-ebnf
  - https://github.com/kaby76/AntlrVSIX/
    - Requires run on Windows (but is more complete)
  - https://dwheeler.com/essays/dont-use-iso-14977-ebnf.html
  - https://www.grammarware.net/text/2012/bnf-was-here.pdf
  - https://condor.depaul.edu/ichu/csc447/notes/wk3/BNF.pdf
  - https://github.com/erikrose/parsimonious
  - https://github.com/lys-lang/node-ebnf
- Generic
  - https://github.com/Engelberg/instaparse
    - https://github.com/taoroalin/instaparseVScode
    - https://github.com/Engelberg/instaparse/blob/master/docs/ABNF.md
- Lark
  - https://github.com/lark-parser/lark
  - https://marketplace.visualstudio.com/items?itemName=dirk-thomas.vscode-lark
  - https://lark-parser.github.io/lark/ide/app.html
- Generic online quick parser for EBNF
  - https://planetcalc.com/6385/
    - Take examples from
      - en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form

    Args:
        GenericUrnHtype (GenericUrnHtype): The UrnHtype to extend
    """

    valid_prefix: InitVar[str] = 'urn:data'
    # valid_prefix examples needs to accept like:
    #   - 'urn:data:' and 'urn:data--d' (implicit, default of 'urn:data:)
    #   - urn:data--i:
    #   - urn:data--p:

    #: The default concept of 'urn:data' is about datasets (nid_attr = 'd')
    nid_attr: InitVar[str] = 'd'
    # nid_attr example:
    #   - 'i' on 'urn:data--i:un:locode' (information about how to get this)
    #   - 'p' on 'urn:data--i:un:locode' (acceptable-policy-usage)

    # #: If more than one attribute is given
    # nid_attr_all: InitVar[list] = ['d']

    nid_attr_spliter: InitVar[str] = '--'
    # nid_attr_spliter example
    #   - '--' on 'urn:data--i:'
    #   - '--' on 'urn:data--d--ckan:' (not implemented, may be deprecated)

    #: Baseline parser global identifier (ISO 3166-1 alpha-2)
    bpgp: InitVar[str] = ''
    # bpgp examples
    #   - 'br' on 'urn:data:br:sus:covid-19-vacinacao'
    #   - 'un' on 'urn:data--i:un:locode'
    #   - 'xz' on 'urn:data--i:xz:hxlcplp:fod:bool'

    #: Baseline parser localized identifier
    bpln: InitVar[str] = ''
    # bpln examples
    #   - 'sus' on 'urn:data:br:sus:covid-19-vacinacao'
    #   -  for 'urn:data:br:__saude.gov.br__:covid-19-vacinacao'
    #     - bpln is ''saude.gov.br'
    #     - bpln_isdn is True
    #   - 'locode' on 'urn:data--i:un:locode'
    #   - 'hxlcplp' on 'urn:data--i:xz:hxlcplp:fod:bool'

    #: Baseline parser localized identifier was an domain name?
    bpln_isdn: InitVar[bool] = False

    bpnss: InitVar[str] = ''
    # bpln examples
    #   - '' on 'urn:data--i:un:locode'
    #   - 'fod:bool' on 'urn:data--i:xz:hxlcplp:fod:bool'

    def _search_paths(self):
        """Return list of search paths to look for this object

        If you are not only searching, but trying automate save an object,
        then consider the first result as ideal one.

        Returns:
            list: list of (default) search paths
        """
        paths = []
        if not self.bpln_isdn:
            paths.append(self.bpgp + '/' + self.bpln + '/')
        else:
            paths.append(self.bpgp + '/' + self.bpln + '/')

        return paths

    def _search_object_names(self):
        """Return list of search object names to look (without file extension)

        If you are not only searching, but trying automate save an object,
        then consider the first result as ideal one.

        Returns:
            list: list of (default) search object names
        """
        paths = []
        if not self.bpln_isdn:
            paths.append(self.bpln)
        else:
            paths.append(self.bpln)

        return paths

    def about(self, key: str = None):
        """Quick summary of the current object.

        Args:
            key (str, optional): Exact key to return.

        Returns:
            dict|Any: Simple python dictionary
        """
        about = {}
        about['nid'] = self.nid
        about['nid_attr'] = self.nid_attr
        # about['bpgp'], about['bpln'], *_ = self.nss.split(":")
        about['bpgp'] = self.bpgp
        about['bpln'] = self.bpln
        if self.bpln_isdn:
            about['bpln_isdn'] = self.bpln_isdn

        # if self.nid_attr_all != ['d']:
        #     about['nid_attr_all'] = self.nid_attr_all

        about['nss'] = self.nss

        # # print('_', _)
        # if about['bpln'].find('__') != -1:
        #     about['bpln'] = about['bpln'].replace('__', '')
        #     self.bpln_isdn = True
        #     about['bpln_isdn'] = self.bpln_isdn
        if key:
            # We don't expose search paths by default. uses need to call
            # myurn.about('base_paths')
            if key == 'base_paths':
                return self._search_paths()
            if key == 'object_names':
                return self._search_object_names()
            if key in about:
                return about[key]
            return None
        return about

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

    def prepare(self, strict: bool = True):
        """Prepare the current URN NSS (Namespace Specific String) for urn:data

        Args:
            strict (bool, optional): If raise SyntaxError. Defaults to True.

        Raises:
            SyntaxError: raise if the value is not valid

        Returns:
            [self, False]: Return self (allow chaining) or false if less strict
        """
        if self.is_valid():
            parts = self.value.split(':')
            self.nss = self.value.replace('urn:' + parts[1] + ':', '', 1)

            if parts[1].lower().find(self.nid_attr_spliter) != -1:
                self.nid, self.nid_attr = parts[1].lower().split(
                    self.nid_attr_spliter)
            else:
                self.nid = parts[1].lower()

            # if parts[1].lower().find(self.nid_attr_spliter) != -1:
            #     print('')
            #     print('')
            #     parts2 = parts[1].lower().split(self.nid_attr_spliter)
            #     self.nid = parts2.pop()
            #     print('self.nidaaaaaaaaaaaaaaaaa', self.nid)
            #     self.nid_attr = parts2[0]
            #     self.nid_attr_all = parts2
            #     # parts[1].lower().split(self.nid_attr_spliter)
            # else:
            #     self.nid = parts[1].lower()

            self.bpgp, self.bpln, *_ = self.nss.split(":")
            # print('_', _)
            if self.bpln.find('__') != -1:
                self.bpln = self.bpln.replace('__', '')
                self.bpln_isdn = True

            self.nss_parsed['nid'] = self.nid
            self.nss_parsed['nss'] = self.nss
            # self.nss_parsed['_raw'] = self.nss
        elif strict:
            raise SyntaxError(self.value + ' not is_valid()')
        else:
            return False

        return self

# TODO: check some nice way to work with dataclasses allowing override
#       valid_prefix.
#       See https://www.infoworld.com/article/3563878
#       /how-to-use-python-dataclasses.html
#       (Emerson Rocha, 2021-03-04 17:54 YTC)


class HdpUrnHtype(GenericUrnHtype):
    """Parses URNs prefixed with 'urn:x-hdp:'

    TODO: should we use or not the x-? Maybe we use -x just for short term.
          https://tools.ietf.org/html/rfc6648
          https://www.rfc-editor.org/pipermail/rfc-dist/2012-June/003402.html
          (Emerson Rocha, 2021-03-04 20:27 UTC)


    TODO: at this moment the HdpUrnHtype is too generic. But ideally should
          allow several more specific namespaces AFTER the baseline
          functionality be implemented.
          (Emerson Rocha, 2021-03-04 18:34 UTC)

    Args:
        GenericUrnHtype (GenericUrnHtype): The generic UrnHtype to extend
    """

    valid_prefix: str = 'urn:x-hdp:'

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

    @see https://tools.ietf.org/html/rfc2648

    TODO: do an MVP (Emerson Rocha, 2021-03-04 19:48 UTC)

    Examples:
        urn:ietf:rfc:2141
        urn:ietf:std:50
        urn:ietf:id:ietf-urn-ietf-06
        urn:ietf:mtg:41-urn

    Args:
        GenericUrnHtype (GenericUrnHtype): The generic UrnHtype to extend
    """

    valid_prefix: str = 'urn:ietf:'

    def _get_fallback(self):
        urls = [
            'https://www.ietf.org/',
            'https://www.ietf.org/standards/rfcs/'
        ]
        return urls

    def _get_rfc(self, rfc_number: Union[int, str]):
        """For an RFC format, return the multiple output formats

        Args:
            rfc_number (Union[int, str]): the RFC number

        Returns:
            list: Array with direct link for multiple RFC formats
        """
        urls = [
            # https://www.rfc-editor.org/rfc/rfc2141.txt
            'https://www.rfc-editor.org/rfc/rfc' + rfc_number + '.txt',
            # https://www.rfc-editor.org/pdfrfc/rfc2141.txt.pdf
            'https://www.rfc-editor.org/rfc/rfc' + rfc_number + '.txt.pdf',
            # https://www.rfc-editor.org/rfc/rfc2141.html
            'https://www.rfc-editor.org/rfc/rfc' + rfc_number + '.html',
            # https://www.rfc-editor.org/info/rfc2141
            'https://www.rfc-editor.org/info/rfc' + rfc_number,
        ]
        return urls

    @staticmethod
    def get_resolver_documentation() -> dict:
        result = {
            'urls': [
                "https://tools.ietf.org/html/rfc2648",
            ]
        }
        return result

    def get_resources(self) -> dict:
        """Return resources associated with the current IETF URN.

        Since baseline functionality with URNs (in special without API calls
        to external webservices) may be hard, the get_resources always
        return a dict.

        Returns:
            dict: Result
        """

        super().prepare()  # Call post init of A
        result = {}

        # print('prepare 1', self.nid, self.nss, self.nss_parsed)
        # 'nss': 'rfc:2141', '_blocks': ['rfc', '2141']
        urn_ietf_parts = self.nss.split(':')
        if urn_ietf_parts[0] == 'rfc':
            result['urls'] = self._get_rfc(urn_ietf_parts[1])
            result['message'] = 'OK'
        else:
            result['urls'] = self._get_fallback()
            result['message'] = 'No specific result found. ' + \
                'Try manually with the urls'

        return result

    def get_url(self) -> str:
        """Return an single URL if do exist an exact match

        See self.get_resources() for more complete alternative

        Returns:
            str: exact match, if any
        """
        result = self.get_resources()
        if result['message'] == 'OK':
            return result['urls'][0]
        else:
            return ''

# TODO: Maybe do an proof of concept of IATI (seems more easy than HDX)
#       http://datastore.iatistandard.org/query/
#       http://datastore.iatistandard.org/api/1/access/activity
#       /by_country.csv?recipient-country=MZ
#       (Emerson Rocha, 2021-03-04 17:54 YTC)

# TODO: do an MVP of ISO https://tools.ietf.org/html/rfc5141
#       (Emerson Rocha, 2021-03-04 17:54 YTC)
