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
#
#                 ## Using as part os another command
#                 hxlquickimport "$(urnresolver urn:data:xz:eticaai:pcode:br)"
#
#                 hxlselect #valid_vocab+default=+v_pcode \
#                    "$(urnresolver urn:data:xz:hxl:standard:core:hashtag)"
#                 hxlselect --query valid_vocab+default=+v_pcode \
#                     "$(urnresolver urn:data:xz:hxl:standard:core:hashtag)"
#
#                 ## Know URN list (without complex/recursive resolving)
#                 urnresolver --urn-list
#
#                 ## Same as --urn-list, but filter results (accept multiple)
#                 urnresolver --urn-list-filter un --urn-list-filter br
#
#                 ## Same as --urn-list-pattern, but python regexes
#                 urnresolver --urn-list-pattern "un|br" --urn-list-pattern "b"
#
#                 ## Resolve something know at random
#                 urnresolver --urn-list | sort -R | urnresolver
#
#                 ## Explain how a query was resolved (-?)
#                 urnresolver -? urn:data:xz:hxl:standard:core:attribute
#
#                 ## List itens that marked thenselves as reference on a
#                 ## subject
#                 urnresolver --urn-explanandum-list
#
#                 ## Print who is marked explicity as reference to something
#                 urnresolver -?? +v_iso15924
#                 urnresolver -?? country+code+v_iso2
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
#       VERSION:  v1.2.3
#       CREATED:  2021-03-05 15:37 UTC v0.7.3 started (based on hxl2example)
#      REVISION:  2021-04-20 06:21 UTC v1.1.0 added --urn-list
#                 2021-04-20 07:27 UTC v1.2.0 added --urn-list-filter &
#                                                   --urn-list-pattern
#                 2021-04-26 01:41 UTC v1.2.1 added --version
#                 2021-04-28 06:13 UTC v1.2.2 added -? (details about URN)
#                 2021-04-28 07:28 UTC v1.2.3 added -?? (reverse search) and
#                                             --urn-explanandum-list
# ==============================================================================

__version__ = "v1.2.3"

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
import re

import json

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

from hxlm.core import (
    __version__ as hxlm_version
)

from hxlm.core.constant import (
    HXLM_ROOT
)

from hxlm.core.internal.formatter import (
    beautify
)

# import yaml

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
        parser.add_argument(
            '--explanandum',
            '-?',
            help='Print explanation information about a URN',
            metavar='explanandum',
            action='store_const',
            const=True,
            default=False
        )

        parser.add_argument(
            '--referens',
            '-??',
            help='Print resources are marked as explanation for a tag. ' +
            'For example "urnresolver -?? +v_iso15924"',
            metavar='referens',
            type=str,
            action='append'
        )

        parser.add_argument(
            '--version',
            help='Show version and exit',
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
            '--all',
            '-a',
            help='Return all anternatives for an exact URN',
            metavar='all',
            action='store_const',
            const=True,
            default=False
        )

        parser.add_argument(
            '--urn-list',
            help='List all know URNs (without recursion/complex remote calls)',
            metavar='urn_list',
            action='store_const',
            const=True,
            default=False
        )

        parser.add_argument(
            '--urn-explanandum-list',
            help='List all explanandum attributes [urn<TAB>expitem]'
            ' (hints for what a dataset explicity mark itsef as reference)',
            metavar='urn_explanandum_list',
            action='store_const',
            const=True,
            default=False
        )

        parser.add_argument(
            '--urn-list-filter',
            help='List know URNs by filter (simple string match)',
            metavar='urn_list_filter',
            action='append',
            type=str
        )

        parser.add_argument(
            '--urn-list-pattern',
            help='List know URNs by pattern (accepts python regex)',
            metavar='urn_list_pattern',
            action='append',
            type=str
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

        if args.version is True:
            print('URNResolver ' + __version__)
            print('hdp-toolchain ' + hxlm_version)
            print('')
            print('URN providers:')

            # We will exit later, but will print what was loaded
            # return self.EXIT_OK

        # Test commands:
        # urnresolver --debug urn:data:xz:hxl:standard:core:hashtag
        # urnresolver urn:data:xz:hxl:standard:core:hashtag
        #                --urn-file tests/urnresolver/all-in-same-dir/
        # hxlquickimport $(urnresolver urn:data:xz:hxl:standard:core:hashtag
        #                      --urn-file tests/urnresolver/all-in-same-dir/)
        #

        # if sys.stdin.isatty():
        #     print('urnresolver --help')
        #     return self.EXIT_ERROR

        # if 'debug' in args and args.debug:
        #     print('DEBUG: CLI args [[', args, ']]')

        # print('args.infile', args.infile, stdin)

        urnrslr_options = []

        # return "fin"
        # print('args', args)

        if 'urn_index_local' in args and args.urn_index_local \
                and len(args.urn_index_local) > 0:
            for file_or_path in args.urn_index_local:

                if args.version is True:
                    print('[urn_index_local[' + file_or_path + ']]')

            # We will exit later, but will print what was loaded
            # return self.EXIT_OK

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
            if Path(HXLM_CONFIG_BASE + 'urn/').is_dir():
                opt_ = get_urn_resolver_local(HXLM_CONFIG_BASE + 'urn/')

                if args.version is True:
                    print('[user_defaults[' + HXLM_CONFIG_BASE + 'urn/' + ']]')

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
                if args.version is True:
                    print('[user_defaults[]]')

                if 'debug' in args and args.debug:
                    print(
                        'DEBUG: HXLM_CONFIG_BASE/urn/ [[' + HXLM_CONFIG_BASE +
                        '/urn/]] do not exist. This could be used to store ' +
                        'local urn references'
                    )

        # If user is not asking to disable load 'urnresolver-default.urn.yml'
        if not args.no_urn_vendor_defaults:
            urnrslvr_def = HXLM_ROOT + '/core/bin/' + \
                'urnresolver-default.urn.yml'
            opt_ = get_urn_resolver_local(urnrslvr_def)
            for item_ in opt_:
                if item_ not in urnrslr_options:
                    urnrslr_options.append(item_)
            # urnrslr_options = get_urn_resolver_local(urnrslvr_def)

            if args.version is True:
                print('[vendor_defaults[' + urnrslvr_def + ']]')

        if args.version is True:
            # Now we exit
            print('[DDDS-NAPTR-Private[not-implemented]]')
            print('[DDDS-NAPTR-Public[not-implemented]]')
            return self.EXIT_OK

        # urnresolver --! +v_iso15924
        if 'referens' in args and args.referens:
            # print('referens', args.referens)
            for item in urnrslr_options:
                # print(item)
                # if 'explanandum' in item and item.explanandum and \
                if 'explanandum' in item and item['explanandum'] and \
                        len(item['explanandum']) > 0:

                    # TODO: implement AND (this is an OR)
                    for exitem in item['explanandum']:
                        if exitem in args.referens:
                            print(item['urn'])
                            # print(item['urn'] + "\t" + exitem)
                        # Inverse:
                        # print(exitem + "\t" + item['urn'])
                    # print(item)

            return self.EXIT_OK

        # urnresolver --urn-explanandum-list
        if 'urn_explanandum_list' in args and args.urn_explanandum_list:
            # print('urn_explanandum_list', args.urn_explanandum_list)
            for item in urnrslr_options:
                # print(item)
                # if 'explanandum' in item and item.explanandum and \
                if 'explanandum' in item and item['explanandum'] and \
                        len(item['explanandum']) > 0:

                    for exitem in item['explanandum']:
                        print(item['urn'] + "\t" + exitem)
                        # Inverse:
                        # print(exitem + "\t" + item['urn'])
                    # print(item)

            return self.EXIT_OK

            # urnresolver --urn-list-filter un --urn-list-filter br
        if 'urn_list_filter' in args and args.urn_list_filter:
            # print('urn_list_filter', args.urn_list_filter)
            if urnrslr_options and len(urnrslr_options) > 0:
                matches = []
                expl_items = []
                for item in urnrslr_options:
                    for sitem in args.urn_list_filter:
                        if item['urn'].find(sitem) > -1:
                            matches.append(item['urn'])

                            # TODO: deal with duplicate items
                            expl_items.append(item)

                # urnresolver --? --urn-list-filter un --urn-list-filter br
                if args.explanandum:
                    # print(matches)
                    print(beautify(json.dumps(expl_items,
                                              indent=4), 'json'))
                    return self.EXIT_ERROR

                matches = set(matches)
                for result in matches:
                    print(result)

            return self.EXIT_OK

        # print('args.urn_list_pattern', args.urn_list_pattern)

        # urnresolver --urn-list-pattern something
        if 'urn_list_pattern' in args and args.urn_list_pattern:
            # print('urn_list_pattern', args.urn_list_pattern)
            cptterns = []

            for lptn in args.urn_list_pattern:
                # print('urn_list_pattern lptn', lptn)
                cptterns.append(re.compile(lptn))

            if urnrslr_options and len(urnrslr_options) > 0:
                matches = []
                expl_items = []
                for item in urnrslr_options:
                    for cptn in cptterns:

                        # print('cptn', cptn, item['urn'])
                        if cptn.search(item['urn']):
                            matches.append(item['urn'])

                            # TODO: deal with duplicate items
                            expl_items.append(item)

                matches = set(matches)

                # urnresolver --? --urn-list-pattern un --urn-list-pattern br
                if args.explanandum:
                    # print(matches)
                    print(beautify(json.dumps(expl_items,
                                              indent=4), 'json'))
                    return self.EXIT_ERROR

                for result in matches:
                    print(result)

            return self.EXIT_OK

        # urnresolver --urn-list
        if 'urn_list' in args and args.urn_list is True:
            # print('urn_list')
            if urnrslr_options and len(urnrslr_options) > 0:

                # urnresolver --? urn:data:zz:example
                if args.explanandum:
                    print(beautify(json.dumps(urnrslr_options,
                                              indent=4), 'json'))
                    return self.EXIT_ERROR

                matches = []
                for item in urnrslr_options:
                    print(item['urn'])

            return self.EXIT_OK

        urn_string = args.infile

        if urn_string:
            urn_item = HUrn.cast_urn(urn=urn_string)
            urn_item.prepare()
        else:
            data = sys.stdin.readlines()
            if len(data) > 0:
                urn_string = str(data[0]).rstrip()

                # print('urn_string', urn_string)

                urn_item = HUrn.cast_urn(urn=urn_string)
                urn_item.prepare()

            else:
                urn_item = None
            # print ("Counted", len(data), "lines.")
            # print('data', data)

            # # let's try take the first line from stdin
            # for line in sys.stdin:
            #     print(line, )

            # urn_item = None

        if 'debug' in args and args.debug:
            print('')
            print('DEBUG: stdin [[', stdin, ']]')
            print('DEBUG: stdin.read() [[', stdin.read(), ']]')
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

            # urnresolver --? urn:data:zz:example
            if args.explanandum:
                if len(matches) > 0:
                    # print(matches)
                    # beautify(str(matches), 'json', terminal)
                    # print('oi1')
                    print(beautify(json.dumps(matches, indent=4), 'json'))
                    # print('oi2')
                else:
                    if 'debug' in args and args.debug:
                        print("no matches")
                return self.EXIT_ERROR

            if len(matches) > 0:
                if args.all:
                    for sitem in matches[0]['fontem']:
                        print(sitem)
                    # print('all...')
                else:
                    print(matches[0]['fontem'][0])
                return self.EXIT_OK

        stderr.write("ERROR: urn [" + str(urn_string) +
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
