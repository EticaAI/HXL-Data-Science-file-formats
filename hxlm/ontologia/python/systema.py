"""hxlm.ontologia.python.systema

This module, like hxlm.ontologia.python.commune, contains generic data classes
when implementing HXLm in python. But one main difference is that on this
module... the initial author have no idea good naming in Latin! But note that
most of what is here was created on last 100 years, so we may need to keep
as it is.


Trivia:
  - "systēma"
    - https://en.wiktionary.org/wiki/systema#Latin
    - Latin, Etymology: From Ancient Greek σύστημα (sústēma,
      “organised whole, body”), from σύν (sún, “with, together”) + ἵστημι
      (hístēmi, “I stand”).
    - Noun, systēma n (genitive systēmatis); third declension,
      - 1. system
      - 2. harmony

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""


from dataclasses import InitVar, dataclass
# from typing import NamedTuple, TypedDict
from enum import Enum
from typing import Any, Union

__all__ = ['EntryPointType', 'FileType', 'RemoteType',  'ResourceWrapper',
           'URNType']


class EntryPointType(Enum):
    """Typehints for entry points to resources (the 'pointer', not content)"""

    # TODO: webdav?

    # https://tools.ietf.org/html/rfc1738 (File protocol)

    FTP = 'ftp'
    """FTP/FTPS protocol https://tools.ietf.org/html/rfc959"""

    GIT = 'git://'
    """Git protocol (abstracton over SSH)

    See:
      - https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols
    """

    HTTP = "http"
    """Generic HTTP/HTTPS entrypoint, https://tools.ietf.org/html/rfc2616"""

    # https://english.stackexchange.com/questions/113606
    # /difference-between-folder-and-directory

    LOCAL_DIR = "file://localhost/dir/"
    """Local directory"""

    LOCAL_FILE = "file://localhost/file"
    """Local file"""

    NETWORK_DIR = "file://remotehost/dir/"
    """Directory acessible via access to an non-localhost hostname"""

    NETWORK_FILE = "file://remotehost/file"
    """File acessible via access to an non-localhost hostname"""

    PYDICT = "PyDict"
    """Entrypoint already is Python Dict object"""

    PYLIST = "PyList"
    """Entrypoint already is Python List object"""

    # Note: hxlm.core, at least for entrypoint type, mostly use python list
    #       and in some cases dict. So at the moment we will not implement
    #       other internal types

    SSH = 'ssh://'
    """Secure Shell (SSH), https://tools.ietf.org/html/rfc4253"""

    # https://docs.python.org/3/library/asyncio-stream.html
    STREAM = "STREAM"
    """Data stream"""

    STRING = "STRING"
    """Generic raw string ready to be immediately parsed (see STREAM"""

    UNKNOW = "?"
    """Unknow entrypoint"""

    URN = "URN"
    """Uniform Resource Name, see https://tools.ietf.org/html/rfc8141"""


@dataclass(repr=False)
class Factum:
    """Encapsulate contextual messages for smarter L10N output (S-expressions!)

    The ideal usage og Factum is, with processing of some external function,
    convert terms like the 'vkg.attr.descriptionem' to what would have meaning
    to the user.

    Since Factum can also be used even for debug program (or or the
    Vocabulary Knowledge Graph may not be ready) is possible to do a raw
    print() of contents. Not ideal, but a fallback.

>>> Factum("Testing")
(vkg.attr.factum (vkg.attr.descriptionem "Testing"))
>>> Factum("Testing", linguam="ENG")
(vkg.attr.factum (vkg.attr.descriptionem (ENG "Testing")))
>>> Factum("Testing", datum=[1, 2])
(vkg.attr.factum (vkg.attr.descriptionem "Testing")(vkg.attr.datum "[1, 2]"))
    """

    descriptionem: str
    """Textual information about the fact. Strongly recommended not omit"""

    fontem: Any = None
    """Source of the message to be presented to end user. Can be ommited.

    Try keep it short. Must be something that can be converted to string.
    """

    datum: Any = None
    """Extra context about the message. Can be ommited."""

    linguam: str = None
    """When descriptionem is an natural language, this can explicit this"""

    # TODO: implement type of Factum (like if is error, or informative message)

    def __repr__(self):
        """Export an string representation without user translation of terms

        Please consider using helpers instead of export objects directly.
        """

        if self.linguam is None:
            desc = '"' + self.descriptionem + '"'
        else:
            desc = '(' + self.linguam + ' "' + self.descriptionem + '")'

        resultatum = "(vkg.attr.factum "
        resultatum += '(vkg.attr.descriptionem ' + desc + ')'

        if self.fontem is not None:
            resultatum += '(vkg.attr.fontem "' + str(self.fontem) + '")'

        if self.datum is not None:
            resultatum += '(vkg.attr.datum "' + str(self.datum) + '")'

        resultatum += ")"

        return resultatum


class FileType(Enum):
    """File formats

    See:
      - https://en.wikipedia.org/wiki/File_format
      - https://en.wikipedia.org/wiki/Container_format_(computing)
      - https://en.wikipedia.org/wiki/Delimiter#Delimiter_collision
    """

    CSV = '.csv?'
    """Generic CSV (allows non-strict), https://tools.ietf.org/html/rfc4180

    Can be used when the content is likely to be CSV, but the file was not
    processed yet
    """

    # TODO: zip
    # TODO: gz

    CSV_RFC4180 = '.csv'
    """An CSV strict compliant with https://tools.ietf.org/html/rfc4180"""

    JSON = '.json'
    """JSON JavaScript Object Notation, https://tools.ietf.org/html/rfc8259"""

    JSON5 = '.json5'
    """ JSON5 Data Interchange Format (JSON5), https://json5.org/"""

    TSV = '.tsv'  # .tsv, .tab
    """Tab-separated values, a more strict CSV type (No RFC for this one)
    See:
      - https://en.wikipedia.org/wiki/Tab-separated_values
    """

    YAML = '.yml'  # .yml, .yaml
    """An YAML 'YAML Ain't Markup Language' container, https://yaml.org/"""


# Class definition: Almost the same
@dataclass
class L10NContext:
    """Localization Context for current user, see hxlm.core.localization

    This dataclass is mostly an wrapper around the context of current user (so
    it will try to localize/translate based on users know languages) but
    can be also used when exporting or explicitly requiting an different
    localization.

    """

    available: list
    """Available languages (lid) on loaded VKG"""

    user: list
    """Orderen know languages of the user"""

    def about(self, key: str = None):
        """Export values"""
        about = {
            'available': self.available,
            'user': self.user,
        }
        if key:
            if key in about:
                return about[key]
            return None
        return about


class RemoteType(Enum):
    """Typehints for specialization of entrypoints"""

    # TODO: S3
    # TODO: Google Spreadsheet
    # TODO: CKAN
    # TODO: HXL-Proxy
    # TODO: FTP strict / FTPS

    HTTP = "http://"
    """Generic HTTP without HTTPS"""

    HTTPS = "https://"
    """Generic HTTPS"""

    UNKNOW = "?"
    """Unknow entrypoint"""


# Class definition: Almost the same
@dataclass(init=True, eq=True)
class ResourceWrapper:
    """An Resource Wrapper"""

    content: Union[dict, list, str] = None
    """If the entrypoint already is not an RAW string/object, the content"""

    entrypoint: InitVar[Any] = None

    entrypoint_t: InitVar[EntryPointType] = None

    log: InitVar[list] = []
    """Log of messages. Can be used when failed = True or for verbose output"""

    failed: bool = False
    """If this resource tried to be loaded, bug failed"""

    remote_t: InitVar[RemoteType] = None

    # def about(self, key: str = None):
    #     """Export values"""
    #     about = {
    #         'failed': self.failed,
    #         'log': self.log,
    #         'entrypoint': self.entrypoint,
    #         'entrypoint_t': self.entrypoint_t,
    #         'remote_t': self.remote_t,
    #         'content': self.content,
    #     }
    #     if key:
    #         if key in about:
    #             return about[key]
    #         return None
    #     return about


class URNType(Enum):
    """Uniform Resource Name, see https://tools.ietf.org/html/rfc8141

    See also hxlm/core/htype/urn.py (not fully implemented yet with this)
    """

    DATA = "urn:data"
    """URN Data
    See:
      - https://github.com/EticaAI/HXL-Data-Science-file-formats/tree/main
        /urn-data-specification
    """

    HDP = "urn:hdp"
    """HDP Declarative Programming URN"""

    IETF = "urn:ietf"
    """IETF URN, see https://tools.ietf.org/html/rfc2648"""

    ISO = "urn:ietf"
    """..., see https://tools.ietf.org/html/rfc5141"""

    UNKNOW = "?"
    """Unknow URN type"""
