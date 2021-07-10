#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  hxl2tab
#
#         USAGE:  cat hxlated-file.csv | hxl2tab
#                 hxl2tab hxlated-file.csv
#                 hxl2tab hxlated-file.csv orange-data-mining-file.tab
#
#                 ### To expose proxy via web (uses hug + ngrok)
#                 # 1.A If is a file on bin/hxl2tab
#                     hug -f bin/hxl2tab
#                 # 1.B If was installed with pip3 install hdp-toolchain
#                     hug -f "$(which hxl2tab)"
#                 # 2. To expose via web, on a different terminal, do this:
#                     ngrok http 8000
#
#   DESCRIPTION:  Convert an already HXLated file (local, remote like Google
#                 Docs...) to an Orange Data Mining .tab file format.
#                 Works both via cli and, with hug, allow export the usability
#                 via HTTP.
#
#       OPTIONS:  hxl2tab --help
#
#  REQUIREMENTS:  - python3
#                     - libhxl (https://pypi.org/project/libhxl/)
#                     - hug (https://github.com/hugapi/hug/)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v2.1
#       CREATED:  2021-01-24 01:25 UTC
#      REVISION:  2021-01-24 02:52 UTC changed from POSIX shell to python3
#                 2021-01-24 23:54 UTC nginxlogs2csv (from Alligo) used as base
#                                      for hxl2tab (Etica.AI)
#                 2021-01-25 23:34 UTC v1.2 imported from hxl2example
#                 2021-01-28 08:00 UTC v1.3 MVP of .tab (both file and stdout);
#                                      still need to add Orange extra hints
#                 2021-01-28 09:07 UTC v1.4 implement Orange Data Mining hints,
#                      uses EticaAI-Data_HXL-Data-Science-file-formats_hxl2tab,
#                      but for non-obvious cases, requires prefix +vt_orange_
#                 2021-02-06 22:26 UTC v1.5 added +vt_categorical
#                 2021-02-07 00:06 UTC v1.6 recognized +vt_* (like +vt_meta)
#                    are ommited from the output .tab, but infered attributes
#                    and base hashtags, not.
#                 2021-02-07 18:34 UTC v2.0 build in HTTP interface with hug!
#                 2021-04-20 00:59 UTC v2.1 installable with pip hdp-toolchain
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
import hxl.model

import csv
import tempfile

# @see https://github.com/hugapi/hug
#     pip3 install hug --upgrade
import hug

# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer


class HXL2Tab:
    """
    HXL2Tab is a classe to export already HXLated data in the format
    .tab
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the HXL2Tab object.
        """
        self.hxlhelper = None
        self.args = None

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

        self.original_outfile = None
        self.original_outfile_is_stdout = True

    def make_args_HXL2Tab(self):

        self.hxlhelper = HXLUtils()
        parser = self.hxlhelper.make_args(
            description=("HXL2Tab Convert an already HXLated file (local, "
                         "remote like Google Docs...) to an Orange Data "
                         "Mining .tab file format. Works both via cli and, "
                         " with hug, allow export the usability via HTTP."
                         ))

        parser.add_argument(
            "--hxlmeta",
            help="Don't print output, just the hxlmeta of the input",
            action='store_const',
            const=True,
            metavar='hxlmeta',
            default=False
        )

        self.args = parser.parse_args()

        return self.args

    def execute_cli(self, args, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr, hxlmeta=False):
        """
        The execute_cli is the main entrypoint of HXL2Tab when used via command
        line interface.
        """
        # hxltabconverter = HXLTabConverter()

        # print(hxltabconverter.ORANGE_REFERENCE)
        # print(hxltabconverter.HXL_REFERENCE)

        # If the user specified an output file, we will save on
        # self.original_outfile. The args.outfile will be used for temporary
        # output
        if args.outfile:
            self.original_outfile = args.outfile
            self.original_outfile_is_stdout = False

        try:
            temp = tempfile.NamedTemporaryFile()
            args.outfile = temp.name

            with self.hxlhelper.make_source(args, stdin) as source, \
                    self.hxlhelper.make_output(args, stdout) as output:
                hxl.io.write_hxl(output.output, source,
                                 show_tags=not args.strip_tags)

            if args.hxlmeta:
                print('TODO: hxlmeta')
                # print('output.output', output.output)
                # print('source', source)
                # # print('source.columns', source.headers())
                # hxlmeta = HXLMeta(local_hxl_file=output.output.name)
                # hxlmeta.debuginfo()
            else:
                self.hxl2tab(args.outfile, self.original_outfile,
                             self.original_outfile_is_stdout)

        finally:
            temp.close()

        return self.EXIT_OK

    def execute_web(self, source_url, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr, hxlmeta=False):
        """
        The execute_web is the main entrypoint of HXL2Tab when this class is
        called outside command line interface, like the build in HTTP use with
        hug
        """

        # TODO: the execute_web needs to output the tabfile with correct
        #       mimetype, compression, etc
        #       (fititnt, 2021-02-07 15:59 UTC)

        self.hxlhelper = HXLUtils()

        try:
            temp_input = tempfile.NamedTemporaryFile('w')
            temp_output = tempfile.NamedTemporaryFile('w')

            # TODO: implement other options beyond source_url
            webargs = type('obj', (object,), {
                "infile": source_url,
                "sheet_index": None,
                "selector": None,
                'sheet': None,
                'http_header': None,
                'ignore_certs': False
            })

            with self.hxlhelper.make_source(webargs, stdin) as source:
                for line in source.gen_csv(True, True):
                    temp_input.write(line)

                temp_input.seek(0)
                self.hxl2tab(temp_input.name, temp_output.name, False)

                result_file = open(temp_output.name, 'r')
                return result_file.read()

        finally:
            temp_input.close()
            temp_output.close()

        return self.EXIT_OK

    def hxl2tab(self, hxlated_input, tab_output, is_stdout):
        """
        hxl2tab is  is the main method to de facto make the conversion.
        """

        with open(hxlated_input, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Hotfix: skip first non-HXL header. Ideally I think the already
            # exported HXlated file should already save without headers.
            next(csv_reader)
            header_original = next(csv_reader)
            header_new = self.hxl2tab_header(header_original)

            if is_stdout:
                txt_writer = csv.writer(sys.stdout, delimiter='\t')
                txt_writer.writerow(header_new)
                for line in csv_reader:
                    txt_writer.writerow(line)
            else:

                tab_output_cleanup = open(tab_output, 'w')
                tab_output_cleanup.truncate()
                tab_output_cleanup.close()

                with open(tab_output, 'a') as new_txt:
                    txt_writer = csv.writer(new_txt, delimiter='\t')
                    txt_writer.writerow(header_new)
                    for line in csv_reader:
                        txt_writer.writerow(line)

    def hxl2tab_header(self, hxlated_header):
        """
        Add prefixes to an hxlated_header to work as typehints for Orange Data
        Mining

        orange.biolab.si/docs/latest/reference/rst/Orange.data.formats.html:

c for class feature            -> +vt_orange_flag_class|+vt_class
i for feature to be ignored    -> +vt_orange_flag_ignore
m for the meta attribute       -> +vt_orange_flag_meta|#meta
C for continuous-typed feature -> +vt_orange_type_continuous|+number
D for discrete feature         -> +vt_orange_type_discrete|+vt_categorical
S for string                   -> +vt_orange_type_string|+text|+name

        An example data file in this format is shown below:

C#sepal length	iC#sepal width	mC#petal length	mC#petal width	cD#iris
5.1	3.5	1.4	0.2	Iris-setosa
4.9	3.0	1.4	0.2	Iris-setosa
4.7	3.2	1.3	0.2	Iris-setosa
        """

        # TODO: improve this block. I'm very sure there is some cleaner way to
        #       do it in a more cleaner way (fititnt, 2021-01-28 08:56 UTC)

        # NOTE: +vt_orange_type_continuous (but not +number),
        #       +vt_orange_type_string (but not +text, +name)
        #       etc are replaced from the end result
        #       In other words: the very specific data types don't need to be
        #       added to the end result, but we keep generic ones to avoid
        #       potentially break other tools.

        for idx, _ in enumerate(hxlated_header):

            # feature types
            if hxlated_header[idx].find('+vt_orange_type_discrete') > -1 \
                    or hxlated_header[idx].find('+vt_categorical') > -1:

                hxlated_header[idx] = hxlated_header[idx].replace(
                    '+vt_orange_type_discrete', '')
                hxlated_header[idx] = hxlated_header[idx].replace(
                    '+vt_categorical', '')
                hxlated_header[idx] = 'D' + hxlated_header[idx]

            elif hxlated_header[idx].find('+vt_orange_type_continuous') > -1 \
                    or hxlated_header[idx].find('+number') > -1:

                hxlated_header[idx] = hxlated_header[idx].replace(
                    '+vt_orange_type_discrete', '')
                hxlated_header[idx] = 'C' + hxlated_header[idx]
            elif hxlated_header[idx].find('+vt_orange_type_string') > -1 or \
                    hxlated_header[idx].find('+text') > -1 or \
                    hxlated_header[idx].find('+name') > -1:

                hxlated_header[idx] = hxlated_header[idx].replace(
                    '+vt_orange_type_string', '')
                hxlated_header[idx] = 'S' + hxlated_header[idx]

            # optional flags
            if hxlated_header[idx].find('+vt_orange_flag_class') > -1 or \
                    hxlated_header[idx].find('+vt_class') > -1:

                hxlated_header[idx] = hxlated_header[idx].replace(
                    '+vt_orange_flag_class', '')
                hxlated_header[idx] = hxlated_header[idx].replace(
                    '+vt_class', '')
                hxlated_header[idx] = 'c' + hxlated_header[idx]

            elif hxlated_header[idx].find('+vt_orange_flag_meta') > -1 or \
                    hxlated_header[idx].find('+vt_meta') > -1 or \
                    hxlated_header[idx].find('#meta') > -1:

                hxlated_header[idx] = hxlated_header[idx].replace(
                    '+vt_orange_flag_meta', '')
                hxlated_header[idx] = hxlated_header[idx].replace(
                    '+vt_meta', '')
                hxlated_header[idx] = 'm' + hxlated_header[idx]

            elif hxlated_header[idx].find('+vt_orange_flag_ignore') > -1:

                hxlated_header[idx] = hxlated_header[idx].replace(
                    '+vt_orange_flag_ignore', '')
                hxlated_header[idx] = 'i' + hxlated_header[idx]

        # print('hxl2tab_header', hxlated_header)
        return hxlated_header


class HXLTabConverter:
    """
    HXLTabConverter is an class to export implement minimum functionality to
    export/import at least the most common cases of HXLated datasets to .tab
    format using the specification of the open source tool Orange Data Mining.
    The current version has some hardcoded values instead of using an external
    schema.

    @see https://orange-data-mining-library.readthedocs.io/en/latest/reference/
    data.io.html.

    Author: Emerson Rocha
    License: Public Domain
    Version: v0.1
    """

    # @see https://orange-data-mining-library.readthedocs.io/en/latest
    # /reference/data.io.html
    ORANGE_REFERENCE = {
        'orange_feature_type': {
            'discrete': {
                'key': "discrete",
                'keys': ["discrete", "d"],
                'short': "d",
            },
            'discrete_list': {
                'key': "discrete_list",
                'keys': [],
                'short': "d",
                'internal-comment': "not implemented"
            },
            'continuous': {
                'key': "continuous",
                'keys': ["continuous", "C"],
                'short': "C",
            },
            'string': {
                'key': "string",
                'keys': ["string", "text", "s"],
                'short': "s",
            },
            'time': {
                'key': "time",
                'keys': ["time", "t"],
                'short': "t",
            },
            'basket': {
                'key': "basket",
                'keys': ["basket"],
                'short': None,
                'internal-comment': "not implemented"
            }
        },
        'orange_flags': {
            'class': {
                'key': "class",
                'keys': ["class", "c"],
                'short': "c",
            },
            'meta': {
                'key': "meta",
                'keys': ["meta", "m"],
                'short': "m",
            },
            'weight': {
                'key': "weight",
                'keys': ["weight", "w"],
                'short': "w",
                'internal-comment': "not implemented"
            },
            'ignore': {
                'key': "ignore",
                'keys': ["ignore", "i"],
                'short': "i",
            },
            'custom-attributes': {
                'key': "custom-attributes",
                'keys': [],
                'short': None,
                'internal-comment': "not implemented"
            },
        }

    }

    def __init__(self):
        """
        Constructs all the necessary attributes for the HXLTabConverter
        object.
        """

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def is_tab_file(self):
        print("""Please just check if the file use tab as separator outside
              this class. For sake of simplicity, the HXLTabConverter assumes
              both exported HXL files and imported created outside would be
              saved in tab, so no extra checks would be need for Excel or
              CSVs""")

    def is_tablike_heading(self, header_group):
        """
        is_tab_heading can either receive a single list of headings or an group
        of 3 lines of headings.
        """
        print("TODO")

    def is_tablike_heading_single(self, header_line):
        """
        is_tablike_heading_single ...
        """
        print("TODO")

    def is_tablike_heading_three(self, header_group):
        """
        is_tablike_heading_three ...
        """
        print("TODO")

    def is_tab_hxlated_heading(self, header_group):
        """
        is_tab_heading can either receive a single list of headings or an group
        of 3 lines of headings.
        """
        print("TODO")


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

    hxl2tab = HXL2Tab()
    args = hxl2tab.make_args_HXL2Tab()

    hxl2tab.execute_cli(args)


def exec_from_console_scripts():
    hxl2tab_ = HXL2Tab()
    args_ = hxl2tab_.make_args_HXL2Tab()

    hxl2tab_.execute_cli(args_)


@hug.format.content_type('text/tab-separated-value')
def output_tab(data, response):
    if isinstance(data, dict) and 'errors' in data:
        response.content_type = 'application/json'
        return hug.output_format.json(data)
    response.content_type = 'text/tab-separated-values'
    if hasattr(data, "read"):
        return data

    return str(data).encode("utf8")


@hug.get('/hxl2tab.tab', output=output_tab)
def api_hxl2tab(source_url):
    """hxl2tab (@see https://github.com/EticaAI/HXL-Data-Science-file-formats)

    Example:
    http://localhost:8000/hxl2tab.tab?source_url=https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833

    """

    hxl2tab = HXL2Tab()

    return hxl2tab.execute_web(source_url)
