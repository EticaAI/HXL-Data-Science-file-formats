#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  urnresolver
#
#         USAGE:  urnresolver urn:data:un:locode
#                 urnresolver urn:data:un:locode
#                 urnresolver urn:data:xz:hxl:standard:core:hashtag
#                 urnresolver urn:data:xz:hxl:standard:core:attribute
#                 urnresolver urn:data:xz:eticaai:pcode:br
#                 hxlquickimport $(urnresolver urn:data:xz:eticaai:pcode:br)
#
#   DESCRIPTION:  urnresolver uses hxlm.core to resolve Uniform Resource Name
#                 (URI) to Uniform Resource Identifier (URI)
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                     - libhxl (@see https://pypi.org/project/libhxl/)
#                     - hxlm (github.com/EticaAI/HXL-Data-Science-file-formats)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  Etica.AI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v0.7.3
#       CREATED:  2021-03-05 15:37 UTC v0.7.3 started (based on hxl2example)
#      REVISION:  ---
# ==============================================================================

# ./hxlm/core/bin/urnresolver.py urn:data:un:locode
# echo $(./hxlm/core/bin/urnresolver.py urn:data:un:locode)

# Where to store data for local urn resolving?
# mkdir "$HOME/.config"
# mkdir "${HOME}/.config/hxlm"
# mkdir "${HOME}/.config/hxlm/urn"
# mkdir "${HOME}/.config/hxlm/urn/data"

# https://data.humdata.org/dataset/hxl-core-schemas
# urnresolver urn:data:xz:hxl:standard:core:hashtag
#    "$HOME/.config/hxlm/urn/data/xz/hxl/std/core/hashtag.csv"
# urnresolver urn:data:xz:hxl:standard:core:attribute
#    "$HOME/.config/hxlm/urn/data/xz/hxl/std/core/attribute.csv"
# urnresolver urn:data:un:locode
#     "$HOME/.config/hxlm/urn/data/un/locode/locode.csv"

# http://www.unece.org/cefact/locode/welcome.html
# https://github.com/datasets/un-locode
# https://datahub.io/core/un-locode

# tree /home/fititnt/.config/hxlm/urn/data
# /home/fititnt/.config/hxlm/urn/data
# ├── un
# │   └── locode
# │       ├── country.csv
# │       ├── function.csv
# │       ├── locode.csv
# │       ├── status.csv
# │       └── subdivision.csv
# └── xz
#     ├── eticaai
#     └── hxl
#         └── std
#             └── core
#                 ├── attribute.csv
#                 └── hashtag.csv

# The data:
#     ~/.local/var/hxlm/data
# The default place for all individual URNs (excluding the index one)
#     ~/.config/hxlm/urn

import sys
import os
import logging
import argparse
# import tempfile
from pathlib import Path

# @see https://github.com/HXLStandard/libhxl-python
#    pip3 install libhxl --upgrade
# Do not import hxl, to avoid circular imports
import hxl.converters
import hxl.filters
import hxl.io

import hxlm.core.htype.urn as HUrn
from hxlm.core.schema.urn.util import (
    get_urn_resolver_local,
    # get_urn_resolver_remote,
    HXLM_CONFIG_BASE
)
from hxlm.core.constant import (
    HXLM_ROOT
)

# @see https://github.com/hugapi/hug
#     pip3 install hug --upgrade
# import hug

# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer


class URNResolver:
    """
    Uurnresolver uses hxlm.core to resolve Uniform Resource Name (URI) to
    Uniform Resource Identifier (URI)
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the URNResolver object.
        """
        self.hxlhelper = None
        self.args = None

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args_urnresolver(self):

        self.hxlhelper = HXLUtils()
        parser = self.hxlhelper.make_args(
            description=("urnresolver uses hxlm.core to resolve Uniform " +
                         "Resource Name (URI) to Uniform Resource " +
                         "Identifier (URI)"))

        parser.add_argument(
            '--debug',
            help='instead of return the result, do full debug',
            action='store_const',
            const=True,
            default=False
        )

        # TODO: add unitary tests for --urn-index-local
        parser.add_argument(
            '--urn-index-local',
            help='Load URN index from local file/folder ' +
            '(accept multiple options)',
            metavar='urn_index_local',
            type=str,
            action='append'
            # action='store_const',
            # const=True,
            # default=False
        )

        # TODO: add unitary tests for --urn-index-remote
        parser.add_argument(
            '--urn-index-remote',
            help='Load URN index from exact URL (accept multiple options)',
            metavar='urn_index_remote',
            type=str,
            action='append'
            # action='store_const',
            # const=True,
            # default=False
        )

        parser.add_argument(
            '--no-urn-user-defaults',
            help='Disable load urnresolver URN indexes from ' +
            '~/.config/hxlm/urn/.',
            metavar='no_urn_user',
            action='store_const',
            const=True,
            default=False
        )

        parser.add_argument(
            '--no-urn-vendor-defaults',
            help='Disable load urnresolver urnresolver-default.urn.yml',
            metavar='no_urn_vendor_defaults',
            action='store_const',
            const=True,
            default=False
        )

        self.args = parser.parse_args()
        return self.args

    def execute_cli(self, args,
                    stdin=STDIN, stdout=sys.stdout, stderr=sys.stderr):
        """
        The execute_cli is the main entrypoint of URNResolver. When
        called will try to convert the URN to an valid IRI.
        """

        # Test commands:
        # urnresolver --debug urn:data:xz:hxl:standard:core:hashtag
        # urnresolver urn:data:xz:hxl:standard:core:hashtag
        #                --urn-file tests/urnresolver/all-in-same-dir/
        # hxlquickimport $(urnresolver urn:data:xz:hxl:standard:core:hashtag
        #                      --urn-file tests/urnresolver/all-in-same-dir/)
        #

        if 'debug' in args and args.debug:
            print('DEBUG: CLI args [[', args, ']]')

        # print('args', args)

        urn_string = args.infile

        urn_item = HUrn.cast_urn(urn=urn_string)
        urn_item.prepare()

        urnrslr_options = []

        if 'urn_index_local' in args and args.urn_index_local \
                and len(args.urn_index_local) > 0:
            for file_or_path in args.urn_index_local:
                opt_ = get_urn_resolver_local(file_or_path, required=True)
                # print('opt_ >> ', opt_ , '<<')
                # urnrslr_options.extend(opt_)
                for item_ in opt_:
                    if item_ not in urnrslr_options:
                        urnrslr_options.append(item_)

        # if 'urn_index_remote' in args and args.urn_index_remote \
        #         and len(args.urn_index_remote) > 0:
        #     for iri_or_domain in args.urn_index_remote:
        #         opt_ = get_urn_resolver_remote(iri_or_domain, required=True)
        #         # print('opt_ >> ', opt_ , '<<')
        #         # urnrslr_options.extend(opt_)
        #         for item_ in opt_:
        #             if item_ not in urnrslr_options:
        #                 urnrslr_options.append(item_)

        # If user is not asking to disable load ~/.config/hxlm/urn/
        if not args.no_urn_user_defaults:
            # print(get_urn_resolver_local(HXLM_CONFIG_BASE + '/urn/'))
            if Path(HXLM_CONFIG_BASE + '/urn/').is_dir():
                opt_ = get_urn_resolver_local(HXLM_CONFIG_BASE + '/urn/')
                if opt_:
                    urnrslr_options.extend(opt_)
                    # print(get_urn_resolver_local(HXLM_CONFIG_BASE + '/urn/'))
                    for item_ in opt_:
                        if item_ not in urnrslr_options:
                            urnrslr_options.append(item_)
                else:
                    print(
                        'DEBUG: HXLM_CONFIG_BASE/urn/ [[' + HXLM_CONFIG_BASE +
                        '/urn/]] exists. but no valid urn lists found'
                    )
            else:
                if 'debug' in args and args.debug:
                    print(
                        'DEBUG: HXLM_CONFIG_BASE/urn/ [[' + HXLM_CONFIG_BASE +
                        '/urn/]] do not exist. This could be used to store ' +
                        'local urn references'
                    )

        # If user is not asking to tisable load 'urnresolver-default.urn.yml'
        if not args.no_urn_vendor_defaults:
            urnrslvr_def = HXLM_ROOT + '/core/bin/' + \
                'urnresolver-default.urn.yml'
            opt_ = get_urn_resolver_local(urnrslvr_def)
            for item_ in opt_:
                if item_ not in urnrslr_options:
                    urnrslr_options.append(item_)
            # urnrslr_options = get_urn_resolver_local(urnrslvr_def)

        if 'debug' in args and args.debug:
            print('')
            print('DEBUG: urnrslr_options [[', urnrslr_options, ']]')
            print('')
            print('DEBUG: urn_item [[', urn_item, ']]')
            print('DEBUG: urn_item.about() [[', urn_item.about(), ']]')
            print('DEBUG: urn_item.about(base_paths) [[',
                  urn_item.about('base_paths'), ']]')
            print('DEBUG: urn_item.about(object_names) [[',
                  urn_item.about('object_names'), ']]')
            print('')
            print('')

        if urnrslr_options and len(urnrslr_options) > 0:
            matches = []
            for item in urnrslr_options:
                if item['urn'] == urn_string:
                    # print('great')
                    matches.append(item)

            if len(matches) > 0:
                print(matches[0]['source'][0])
                return self.EXIT_OK

        # if 'debug' in args and args.debug:
        #     # valt = HUrnUtil.get_urn_vault_local_info('un', 'locode')
        #     # HUrnUtil.debug_local_data('un', 'locode')
        #     # HUrnUtil.get_urn_vault_local_info(urn_item)

        #     # print('valt', valt)
        #     # print('args', args)
        #     print('args.infile', args.infile)
        #     print('urn_item', urn_item)
        #     print('about', urn_item.about())
        #     print('about base_paths', urn_item.about('base_paths'))
        #     print('about object_names', urn_item.about('object_names'))

        stderr.write("ERROR: urn [" + urn_string +
                     "] strict match not found \n")
        return self.EXIT_ERROR

        # print(urn_item.get_resources())

        # print('args', args)
        # print('args', args)

        # # NOTE: the next lines, in fact, only generate an csv outut. So you
        # #       can use as starting point.
        # with self.hxlhelper.make_source(args, stdin) as source, \
        #         self.hxlhelper.make_output(args, stdout) as output:
        #     hxl.io.write_hxl(output.output, source,
        #                      show_tags=not args.strip_tags)

        # return self.EXIT_OK


class HXLUtils:
    """
    HXLUtils contains functions from the Console scripts of libhxl-python
    (HXLStandard/libhxl-python/blob/master/hxl/scripts.py) with few changes
    to be used as class (and have one single place to change).
    Last update on this class was 2021-01-25.

    Author: David Megginson
    License: Public Domain
    """

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args(self, description, hxl_output=True):
        """Set up parser with default arguments.
        @param description: usage description to show
        @param hxl_output: if True (default), include options for HXL output.
        @returns: an argument parser, partly set up.
        """
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument(
            'infile',
            help='HXL file to read (if omitted, use standard input).',
            nargs='?'
        )
        if hxl_output:
            parser.add_argument(
                'outfile',
                help='HXL file to write (if omitted, use standard output).',
                nargs='?'
            )
        parser.add_argument(
            '--sheet',
            help='Select sheet from a workbook (1 is first sheet)',
            metavar='number',
            type=int,
            nargs='?'
        )
        parser.add_argument(
            '--selector',
            help='JSONPath expression for starting point in JSON input',
            metavar='path',
            nargs='?'
        )
        parser.add_argument(
            '--http-header',
            help='Custom HTTP header to send with request',
            metavar='header',
            action='append'
        )
        if hxl_output:
            parser.add_argument(
                '--remove-headers',
                help='Strip text headers from the CSV output',
                action='store_const',
                const=True,
                default=False
            )
            parser.add_argument(
                '--strip-tags',
                help='Strip HXL tags from the CSV output',
                action='store_const',
                const=True,
                default=False
            )
        parser.add_argument(
            "--ignore-certs",
            help="Don't verify SSL connections (useful for self-signed)",
            action='store_const',
            const=True,
            default=False
        )
        parser.add_argument(
            '--log',
            help='Set minimum logging level',
            metavar='debug|info|warning|error|critical|none',
            choices=['debug', 'info', 'warning', 'error', 'critical'],
            default='error'
        )
        return parser

    def add_queries_arg(
        self,
        parser,
        help='Apply only to rows matching at least one query.'
    ):
        parser.add_argument(
            '-q',
            '--query',
            help=help,
            metavar='<tagspec><op><value>',
            action='append'
        )
        return parser

    def do_common_args(self, args):
        """Process standard args"""
        logging.basicConfig(
            format='%(levelname)s (%(name)s): %(message)s',
            level=args.log.upper())

    def make_source(self, args, stdin=STDIN):
        """Create a HXL input source."""

        # construct the input object
        input = self.make_input(args, stdin)
        return hxl.io.data(input)

    def make_input(self, args, stdin=sys.stdin, url_or_filename=None):
        """Create an input object"""

        if url_or_filename is None:
            url_or_filename = args.infile

        # sheet index
        sheet_index = args.sheet
        if sheet_index is not None:
            sheet_index -= 1

        # JSONPath selector
        selector = args.selector

        http_headers = self.make_headers(args)

        return hxl.io.make_input(
            url_or_filename or stdin,
            sheet_index=sheet_index,
            selector=selector,
            allow_local=True,  # TODO: consider change this for execute_web
            http_headers=http_headers,
            verify_ssl=(not args.ignore_certs)
        )

    def make_output(self, args, stdout=sys.stdout):
        """Create an output stream."""
        if args.outfile:
            return FileOutput(args.outfile)
        else:
            return StreamOutput(stdout)

    def make_headers(self, args):
        # get custom headers
        header_strings = []
        header = os.environ.get("HXL_HTTP_HEADER")
        if header is not None:
            header_strings.append(header)
        if args.http_header is not None:
            header_strings += args.http_header
        http_headers = {}
        for header in header_strings:
            parts = header.partition(':')
            http_headers[parts[0].strip()] = parts[2].strip()
        return http_headers


class FileOutput(object):
    """
    FileOutput contains is based on libhxl-python with no changes..
    Last update on this class was 2021-01-25.

    Author: David Megginson
    License: Public Domain
    """

    def __init__(self, filename):
        self.output = open(filename, 'w')

    def __enter__(self):
        return self

    def __exit__(self, value, type, traceback):
        self.output.close()


class StreamOutput(object):
    """
    StreamOutput contains is based on libhxl-python with no changes..
    Last update on this class was 2021-01-25.

    Author: David Megginson
    License: Public Domain
    """

    def __init__(self, output):
        self.output = output

    def __enter__(self):
        return self

    def __exit__(self, value, type, traceback):
        pass

    def write(self, s):
        self.output.write(s)


if __name__ == "__main__":

    urnresolver = URNResolver()
    args = urnresolver.make_args_urnresolver()

    urnresolver.execute_cli(args)


def exec_from_console_scripts():
    urnresolver = URNResolver()
    args = urnresolver.make_args_urnresolver()

    urnresolver.execute_cli(args)
