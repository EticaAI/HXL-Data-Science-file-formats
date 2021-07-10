#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  hxlquickimport
#
#         USAGE:  hxlquickimport hxlated-data.csv my-exported-file.hxl
#                 cat hxlated-data.csv | hxlquickimport > my-exported-file.hxl
#
#                 ### To expose proxy via web (uses hug + ngrok)
#                 # 1.A If is a file on bin/hxlquickimport
#                     hug -p 9001 -f bin/hxlquickimport
#                 # 1.B If was installed with pip3 install hdp-toolchain
#                     hug -p 9001 -f "$(which hxlquickimport)"
#                 # 2. To expose via web, on a different terminal, do this:
#                     ngrok http 9001
#
#   DESCRIPTION:  hxlquickimport is a quick (and wrong) way to import
#                 non-HXL dataset (like an .csv or .xlsx, but requires headers
#                 already on the first row) without human intervention.
#                 It will try to slugify the original header and add as
#                 +attributefor a base hashtag like #meta.
#                 The result may be an HXL with valid syntax (that can be used
#                 for automated esting) but most HXL powered tools would still
#                 be human review.
#                 How does it work?
#                 "[Max Power] Kids: there's three ways to do things; the right
#                 way, the wrong way and the Max Power way!
#                 [Bart Simpson] Isn't that the wrong way?
#                 [Max Power] Yeah, but faster!
#                 (via https://www.youtube.com/watch?v=7P0JM3h7IQk)"
#                 How to do it the right way?
#                 Read the documentation on https://hxlstandard.org/.
#                 (Tip: both HXL Postcards and the hxl-hashtag-chooser are very
#                 helpful!)
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                     - libhxl (@see https://pypi.org/project/libhxl/)
#                     - hug (https://github.com/hugapi/hug/)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.2
#       CREATED: 2021-01-29 07:48 UTC
#      REVISION: 2021-01-29 17:34 UTC v1.0
#                2021-02-07 19:32 UTC v1.1 drafted HTTP interface with hug
#                2021-04-20 00:59 UTC v1.2 installable with pip hdp-toolchain
# ==============================================================================

import sys
import os
import logging
import argparse

# @see https://github.com/HXLStandard/libhxl-python
#    pip3 install libhxl --upgrade
# Do not import hxl, to avoid circular imports
import hxl.converters
import hxl.filters
import hxl.io

# @see https://github.com/hugapi/hug
#     pip3 install hug --upgrade
import hug

import csv
import tempfile
from slugify import slugify

# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer


class HXLQuickImport:
    """
    HXLQuickImport is a classe to export already HXLated data in the format
    example.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the HXLQuickImport object.
        """
        self.hxlhelper = None
        self.args = None

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args_hxlquickimport(self):

        self.hxlhelper = HXLUtils()
        parser = self.hxlhelper.make_args(
            description=("""
hxlquickimport is a quick (and wrong) way to import
non-HXL dataset (like an .csv or .xlsx, but requires headers already on the
first row) without human intervention. It will try to slugify the original
header and add as +attributefor a base hashtag like #meta.
The result may be an HXL with valid syntax (that can be used for automated
testing) but most HXL powered tools would still be human review.

How does it work?
"[Max Power] Kids: there's three ways to do things; the right way,
the wrong way and the Max Power way!
[Bart Simpson] Isn't that the wrong way?
[Max Power] Yeah, but faster!"
(via https://www.youtube.com/watch?v=7P0JM3h7IQk)

How to do it the right way?
Read the documentation on https://hxlstandard.org/.
(Tip: both HXL Postcards and the hxl-hashtag-chooser are very helpful!)
            """))

        self.args = parser.parse_args()
        return self.args

    def execute_cli(self, args,
                    stdin=STDIN, stdout=sys.stdout, stderr=sys.stderr):
        """
        The execute_cli is the main entrypoint of HXLQuickImport when executed
        via cli.
        """

        with self.hxlhelper.make_source(args, stdin) as source:
            self.hxlquickimport(source, args, True)

        return self.EXIT_OK

    def execute_web(self, source_url, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr):
        """
        The execute_web is the main entrypoint of HXL2Tab when this class is
        called outside command line interface, like the build in HTTP use with
        hug.

        NOTE: execute_web (at least on hxlquickimport v1.0) is just an
        placeholder, Still not implemented
        """

        # TODO: at bare minimum should at least output the content as the cli
        #       version, but sill not. (fititnt, 2021-02-07 19:32 UTC)
        # TODO: the execute_web needs to output the tabfile with correct
        #       mimetype, compression, etc
        #       (fititnt, 2021-02-07 15:59 UTC)

        self.hxlhelper = HXLUtils()

        try:
            temp_input = tempfile.NamedTemporaryFile('w')
            temp_output = tempfile.NamedTemporaryFile('w')

            webargs = type('obj', (object,), {
                "infile": source_url,
                "sheet_index": None,
                "selector": None,
                'sheet': None,
                'http_header': None,
                'ignore_certs': False
            })

            with self.hxlhelper.make_source(webargs, stdin) as source:
                for line in source.gen_raw(True, True):
                    temp_input.write(line)

                temp_input.seek(0)
                self.hxlquickimport(temp_input.name, temp_output.name, False)

                result_file = open(temp_output.name, 'r')
                return result_file.read()

        finally:
            temp_input.close()
            temp_output.close()

        return self.EXIT_OK

    def hxlquickimport(self, hxlated_input, tab_output, is_stdout):
        """
        hic sunt dracones
                           (__)    )
                           (..)   /|\\
                          (o_o)  / | \\
                          ___) \\/,-|,-\\|
                        //,-/_\\ )  '  '
                           (//,-'\\|
                           (  ( . \\_
                        gnv `._\\(___`.
                             '---' _)/
                                  `-'
        """

        header_original = hxlated_input._get_row()

        header_new = self.hxlquickimport_header(header_original)

        if not args.outfile:
            # txt_writer = csv.writer(sys.stdout, delimiter='\t')
            txt_writer = csv.writer(sys.stdout)
            txt_writer.writerow(header_new)
            # for line in hxlated_input:
            line = hxlated_input._get_row()

            while line:
                txt_writer.writerow(line)
                try:
                    line = hxlated_input._get_row()
                except Exception:
                    line = False

        else:

            tab_output_cleanup = open(args.outfile, 'w')
            tab_output_cleanup.truncate()
            tab_output_cleanup.close()

            with open(args.outfile, 'a') as new_txt:
                # txt_writer = csv.writer(new_txt, delimiter='\t')
                txt_writer = csv.writer(new_txt)
                txt_writer.writerow(header_new)

                line = hxlated_input._get_row()

                while line:
                    txt_writer.writerow(line)
                    try:
                        line = hxlated_input._get_row()
                    except Exception:
                        line = False

    def hxlquickimport_header(self, hxlated_header, basehashtag="#item"):
        """
        hhxlquickimport_header is a hackish to HXLate an CSV-like dataset
        without human intervention.

        How it works? It replaces the original header with the base
        hashtag and then slugify the original header as attribute, so

        ID_REGISTRO        -> #item+id_registro
        NACIONALIDAD       -> #item+nacionalidad

        The current version will not avoid 'conflicts' with HXL data types like

        BOOL               -> #item+bool
        number             -> #item+number
        phone              -> #item+phone
        """

        for idx, _ in enumerate(hxlated_header):
            hxlated_header[idx] = basehashtag + '+' \
                + slugify(hxlated_header[idx], separator="_")

        return hxlated_header


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
            allow_local=True,
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

    hxlquickimport = HXLQuickImport()
    args = hxlquickimport.make_args_hxlquickimport()

    hxlquickimport.execute_cli(args)


def exec_from_console_scripts():
    hxlquickimport_ = HXLQuickImport()
    args_ = hxlquickimport_.make_args_hxlquickimport()

    hxlquickimport_.execute_cli(args_)


@hug.format.content_type('text/csv')
def output_csv(data, response):
    if isinstance(data, dict) and 'errors' in data:
        response.content_type = 'application/json'
        return hug.output_format.json(data)
    response.content_type = 'text/csv'
    if hasattr(data, "read"):
        return data

    return str(data).encode("utf8")


@hug.get('/hxlquickimport.csv', output=output_csv)
def api_hxl2tab(source_url):
    """hxlquickimport
    (@see https://github.com/EticaAI/HXL-Data-Science-file-formats)

    Example:
    http://localhost:8000/hxlquickimport.csv?source_url=https://docs.google.com
    /spreadsheets/d/1GQVrCQGEetx7RmKaZJ8eD5dgsr5i1zNy_UJpX3_AgrE
    /edit#gid=1715408033
    """

    hxl2tab = HXLQuickImport()

    return hxl2tab.execute_web(source_url)
