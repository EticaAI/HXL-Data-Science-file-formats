"""hxlm.core.types contain envelope to internal types that are not Htypes

- https://stackoverflow.com/questions/53409117
  /what-are-the-main-differences-of-namedtuple-and-typeddict-in-python-mypy
  /63218574#63218574

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# from dataclasses import dataclass
# from typing import NamedTuple, TypedDict
from enum import Enum


class EntryPointType(Enum):
    """Typehints for entry points to resources (the 'pointer', not content)"""

    # TODO: webdav?

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

    LOCAL_DIR = "/local/"
    """Local directory"""

    LOCAL_FILE = "/local/file"
    """Local file"""

    SSH = 'ssh://'
    """Secure Shell (SSH), https://tools.ietf.org/html/rfc4253"""

    # https://docs.python.org/3/library/asyncio-stream.html
    STREAM = "stream"
    """Data stream"""

    RAW_STRING = "RAW_STRING"
    """Generic raw string ready to be immediately parsed (see STREAM"""

    UNKNOW = "?"
    """Unknow entrypoint"""

    URN = "URN"
    """Uniform Resource Name, see https://tools.ietf.org/html/rfc8141"""


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
