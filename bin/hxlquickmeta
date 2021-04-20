#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  hxlquickmeta
#
#         USAGE:  hxlquickmeta hxlated-data.hxl my-exported-file.example
#                 cat hxlated-data.hxl | hxlquickmeta > my-exported-file.csv
#
#                 ### To expose proxy via web (uses hug + ngrok)
#                 # 1.A If is a file on bin/hxlquickmeta
#                     hug -f bin/hxlquickmeta
#                 # 1.B If was installed with pip3 install hdp-toolchain
#                     hug -f "$(which hxlquickmeta)"
#                 # 2. To expose via web, on a different terminal, do this:
#                     ngrok http 8000
#
#   DESCRIPTION:  hxlquickmeta output information about a local or remote
#                 dataset. If the file already is HXLated, it will print
#                 even more information.
#
#                 Hug API can be used to create an ad-hoc web interface to your
#                 script. This can be both useful if you are using an software
#                 that accepts an URL as data source and you don't want to use
#                 this script to save a file locally.
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                     - libhxl (https://pypi.org/project/libhxl/)
#                     - hug (https://github.com/hugapi/hug/)
#                     - pandas (https://github.com/pandas-dev/pandas)
#                     - orange3 (https://github.com/biolab/orange3)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.2.0
#       CREATED:  2021-02-17 03:55 UTC
#      REVISION:  2021-02-20 04:59 UTC v1.0.0 MVP, basic (HTTP still with bugs)
#                 2021-02-20 23:46 UTC v1.1.0 added overview with Pandas
#                 2021-04-20 00:59 UTC v1.2.0 installable via pip hdp-toolchain
# ==============================================================================

import sys
import os
import logging
import argparse
import re

# @see https://github.com/HXLStandard/libhxl-python
#    pip3 install libhxl --upgrade
# Do not import hxl, to avoid circular imports
import hxl.converters
import hxl.filters
import hxl.io
# from hxl.model import Dataset

import csv
import tempfile

# @see https://github.com/hugapi/hug
#     pip3 install hug --upgrade
import hug

# Required by HXLMetaExtras
import pandas as pd
# import numpy as np
import Orange

# import meta.hxltype.base
# print(meta.hxltype.base.test())

# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer


class HXLQuickMeta:
    """
    HXLQuickMeta is the main class used on hxlquickmeta. (...)
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the HXLQuickMeta object.
        """
        self.hxlhelper = None
        self.args = None
        self.hxlmeta = HXLMeta()

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args_hxlquickmeta(self):

        self.hxlhelper = HXLUtils()
        parser = self.hxlhelper.make_args(
            description=("hxlquickmeta  output information about a local or " +
                         "remote dataset. If the file already is HXLated, " +
                         "it will print even more information."))

        # TODO: implement draft of --hxlmeta-rebuild/--hxlmeta-path
        # parser.add_argument(
        #     '--hxlmeta-rebuild',
        #     help='Re-build local database of Vocabularies/Taxonomies/(...)',
        #     # metavar='quickhashtag',
        #     default=None,
        #     nargs='?'
        # )

        # parser.add_argument(
        #     '--hxlmeta-path',
        #     help='Explicitly define the path for HXLMeta local database',
        #     # metavar='quickhashtag',
        #     default=None,
        #     nargs='?'
        # )

        parser.add_argument(
            '--hxlquickmeta-hashtag',
            help='Output debug information for just one hashtag (inline)',
            # metavar='quickhashtag',
            default=None,
            nargs='?'
        )

        parser.add_argument(
            '--hxlquickmeta-value',
            help='Output debug information for just one value (inline)',
            # metavar='quickhashtag',
            default=None,
            nargs='?'
        )

        self.args = parser.parse_args()
        return self.args

    def execute_cli(self, args, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr, hxlmeta=False):
        """
        The execute_cli is the main entrypoint of hxlquickmeta when used via
        command line interface.
        """

        if args.hxlquickmeta_hashtag:
            # print(args.hxlquickmeta_hashtag)
            # print(self.hxlmeta.HXL_REFERENCE)
            self.hxlmeta.get_hashtag_info(
                args.hxlquickmeta_hashtag, args.hxlquickmeta_value)
            return self.EXIT_OK

        # If the user specified an output file, we will save on
        # self.original_outfile. The args.outfile will be used for temporary
        # output
        if args.outfile:
            self.original_outfile = args.outfile
            self.original_outfile_is_stdout = False

        # # TODO: remove this block after MVP of HXLMetaDataset ---------------
        # temp2 = tempfile.NamedTemporaryFile()
        # args.outfile = temp2.name
        # with self.hxlhelper.make_source(args, stdin) as source, \
        #         self.hxlhelper.make_output(args, stdout) as output:
        #     hxl.io.write_hxl(output.output, source,
        #                      show_tags=not args.strip_tags,
        #                      show_headers=False)

        # # print('source', source)
        # # print('output.output', output.output)
        # hxlmetadataset = HXLMetaDataset(output.output.name)
        # hxlmetadataset.parse_input()
        # print('hxlmetadataset', hxlmetadataset)
        # print('hxlmetadataset._input', hxlmetadataset._input)
        # return 1
        # TODO: remove this block after MVP of HXLMetaDataset -----------------

        try:
            temp = tempfile.NamedTemporaryFile()
            args.outfile = temp.name

            print('> Connection overview')
            print(' >> TODO: implement raw connection, HTTP headers, etc')
            print(' >>       (this should output debug information even')
            print(' >>       for inputs that would break libhxl)')

            try:

                # TODO: as hotfix, we're simply ignoring any original Non
                #       HXLated heading from the local file as quick hack to
                #       not break Orange checks with show_headers=False.
                #       This should be improved
                with self.hxlhelper.make_source(args, stdin) as source, \
                        self.hxlhelper.make_output(args, stdout) as output:
                    # hxl.io.write_hxl(output.output, source,
                    #                  show_tags=not args.strip_tags)
                    hxl.io.write_hxl(output.output, source,
                                     show_tags=not args.strip_tags,
                                     show_headers=False)

                    # # self.hxlhelper.make_source return hxl.io.data
                    # # hxl.io.data returns HXLReader
                    # hxldataset = HXLDataset(source)
                    # print('source', source.count())
                    # # print('hxldataset', hxldataset)
                    # print('hxldataset', hxldataset.tags)
                    # return 1

                print(' ')
                print('> lihxl-python overview')
                print(' >> output.output', output.output)
                print(' >> source', source)
                # print('source.columns', source.headers())
                hxlmeta = HXLMeta(local_hxl_file=output.output.name)
                hxlmeta.debuginfo()
                hxlmetaextras = HXLMetaExtras(
                    local_hxl_file=output.output.name)
                hxlmetaextras.debuginfo()
            except Exception as error:
                print("ERROR! libhxl and/or HXLmeta/HXLMetaExtras failed",
                      error)
                print("Ok. Trying harder now with HXLMetaExtras...")

                try:
                    hxlmetaextras = HXLMetaExtras(
                        local_hxl_file=args.infile)

                    hxlmetaextras.debuginfo()
                except Exception as error:
                    print("ERROR! Even HXLMetaExtras failed miserably.",
                          error)

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
                # self.hxl2tab(temp_input.name, temp_output.name, False)

                result_file = open(temp_input.name, 'r')
                return result_file.read()

        finally:
            temp_input.close()
            temp_output.close()

        return self.EXIT_OK


class HXLMeta:
    """
    HXLMeta is (...)

    Author: Multiple Authors
    License: Public Domain
    Version: v0.6.5


    See also:
      - github.com/HXLStandard/libhxl-python/blob/master/hxl/datatypes.py
      - github.com/HXLStandard/libhxl-python/blob/master/hxl/model.py
      - github.com/HXLStandard/libhxl-python/blob/master/hxl/validation.py
    """

    # From libhxl v4.22, hxl.datatypes.TOKEN_PATTERN) # TODO: remove if unused
    TOKEN_PATTERN = r'[A-Za-z][_0-9A-Za-z]*'
    """A regular expression matching a single string token.
    """

    # From libhxl v4.22, hxl.datatypes._WHITESPACE_PATTERN
    _WHITESPACE_PATTERN = re.compile(r'\s+', re.MULTILINE)

    # From libhxl v4.22, hxl.TagPattern.PATTERN  # TODO: remove if not used
    PATTERN = r'^\s*#?({token}|\*)((?:\s*[+-]{token})*)\s*(!)?\s*$'.format(
        token=hxl.datatypes.TOKEN_PATTERN)
    """Constant: regular expression to match a HXL tag pattern.
    """

    GLOSSARY = {
        # @see EticaAI-Data_HXL-Data-Science-file-formats_HXLMeta_Glossary
        #      https://docs.google.com/spreadsheets/d/
        #      1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1066910203
        'DataType': {
            'name': "HXL Data Type (Official HXL Standard Data Type)",
            'description': "Since the HXL standard is meant to be easy to " +
                           "write also by information managers in the field," +
                           "most Data Types are implicit and some base " +
                           "hashtags enforce beyond the generic ‘text’. " +
                           "(#date assumes +date, affected assumes " +
                           "+num/number).",
            'table': "https://docs.google.com/spreadsheets/d/" +
            "1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=717813523",
            # HXLStandard use no prefix for DataType and, as 2021-02-17,
            # some tools actually use hints like +num for change options for
            # users. The '+td_' is mere for when have to differenciate
            'attribute_prefix': 'td_',
            'attribute_prefix_optional': True,
            'values': [
                'text',  # (+text)
                'number',  # (+num)
                'url',  # (+url)
                'email',  # (+emal)
                'phone',  # (+phone)
                'date',  # (+date)
                'bool',  # (+bool); Note: bool is an convention, but not
                         # part of the HXLStandard 1.1
            ],
            'value_aliases': {
                'num': "number"
            },
            # Since DataType are part of the HXLStandard, they're expliclity
            # not extensible without changes on this code. This helps to
            # optimize for speed
            'values_extensible': False
        },
        'StorageType': {
            'name': "Variable Storage Type",
            'description': "Storage Type is one way to document low level" +
                           "storage type more specific to official HXL Data" +
                           "Types",
            'table': "https://docs.google.com/spreadsheets/d/" +
            "1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=211012023",
            # ts_ (NEEDS REVISION, conflict with StatisticalType)
            'attribute_prefix': 'tsx_',
            'attribute_prefix_optional': False,
            'values': [
                'TODO'  # See EticaAI-Data_HXL-Data-Science-file-formats_
                        #     HXLMeta_StorageType
                        # Not implemented yet as usable code
            ],
            # StorageType are not part of the HXLStandard, but since
            # they are are expected to at least depend on one or more
            # implementations in code, we will define they as None (Null).
            # Implementers may choose to consider None as False or True.
            'values_extensible': None
        },
        'StatisticalType': {
            'name': "Variable Statistical Data Type",
            'description': "In statistics, groups of individual data points " +
                           "may be classified as belonging to any of various "
                           "statistical data types, e.g. categorical (red, "
                           "blue, green), real number (1.68, -5, 1.7e+6), "
                           "odd number(1,3,5) etc. -- Wikipedia",
            'table': "https://docs.google.com/spreadsheets/d/" +
            "1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1566300457",
            'values': [
                'binary',
                'categorical',
                'ordinal',
                'realvaluedadditive',
                'realvaluedmultiplicative',
            ],
            # StatisticalType are not part of the HXLStandard, but since
            # they are are expected to at least depend on one or more
            # implementations in code, we will define they as None (Null).
            # Implementers may choose to consider None as False or True.
            'values_extensible': None
        },
        'LevelType': {
            'name': "Variable Level of measurement Type",
            'description': "Level of measurement or scale of measure is a " +
                           "classification that describes " +
                           "the nature of information within the values " +
                           " assigned to variables. Psychologist Stanley " +
                           " Smith Stevens developed the best-known " +
                           "classification with four levels, or scales, of " +
                           "measurement: nominal, ordinal, interval, "
                           "and ratio. -- Wikipedia. "
                           "Note: while the current tables document only " +
                           "Stanley Smith Stevens classification, the " +
                           "LevelType actually could be used to represent " +
                           " other typologies if enough users could test " +
                           " them.",
            'table': "https://docs.google.com/spreadsheets/d/" +
            "1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1053765950",
            'values': [
                'nominal',
                'ordinal',
                'interval',
                'ratio'
            ],
            'value_aliases': {
                'target': "focus",  # PSPP/SPSS/SAS/WPA ...
                'class': "focus",  # Weka/Orange3/...
            },
            # LevelType are explicitly extensible
            'values_extensible': True
        },
        'UsageType': {
            'name': "Variable Usage Type",
            'description': "HXLMeta Usage Types can be used to define how " +
                           "external tools should use the variable (data on " +
                           "the column). The most common type that cannot " +
                           "be automatically safely detected is canonically " +
                           "called 'focus'/'focusN' (some softwares like " +
                           "PSPP/SPSS/SAS/WPA Analytics uses 'target', and " +
                           " Weka/Orange use 'class'; that's why these are " +
                           " considered direct aliases). ",
            'table': "https://docs.google.com/spreadsheets/d/" +
            "1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=617579056",
            'values': [
                'focus',
                'focusN',
                'meta'
            ],
            'value_aliases': {
                'target': "focus",  # PSPP/SPSS/SAS/WPA ...
                'class': "focus"  # Weka/Orange3/...
            },
            # UsageType are explicitly extensible
            'values_extensible': True
        },
        'WeightLevel': {
            'name': "Variable Weight",
            'description': "WeightLevel defines for both HXL-Aware tools " +
                           "or for exported files based on HXLated datasets" +
                           "the weight of one observation (a data row). " +
                           "This is intended mostly for statistical" +
                           "analysis, but most tools would treat this as " +
                           "meta information. The default weight is 1. " +
                           "Weight 0 means ignore. Negative weight (while " +
                           "allowed on HXL) are likely to raise errors on " +
                           "external tools.",
            'table': "https://docs.google.com/spreadsheets/d/" +
            "1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1507056660"
        },
        'VariableLabel': {
            'description': "TODO: write here"
        },
        'VariableDescription': {
            'description': "TODO: write here"
        },
        'OriginaHashtag': {
            'description': "TODO: write here"
        }
    }

    # Uses HXL v1.1-final
    # @see https://hxlstandard.org/standard/1-1final/dictionary/
    # @see https://docs.google.com/spreadsheets/d/
    #      1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/edit#gid=319251406
    # @see https://en.wikipedia.org/wiki/Statistical_data_type
    HXL_REFERENCE = {
        # 'hxl_core_datatypes': [
        #     'text', 'number', 'url', 'email', 'phone', 'date'
        # ]
        'hashtag': {
            # x_example | This is just an example hashtag with all options.
            #             and better documentation.
            'x_example': {
                'DataType': "text",  # text, number, url, email, phone, date
                'StorageType': "varchar",  # int32, int64, float32, ...
                'StatisticalType': "meta",  # binary, categorical, ordinal...
                'LevelType': "meta",  # nominal, ordinal, interval, ratio,...
                'UsageType': "meta",  # meta, focus/target/class, input
                # HXLStandard only attribute an default vocabulary when tag
                # also have an +code attribute. On this case an
                # '#x_example +code' would use the HashtagVocab v_example, but
                # '#x_example +code +v_acme' would use +v_acme
                'HashtagVocab': None,
                'default_if__code': {
                    'HashtagVocab': "v_example",
                },
                'default_if__v_acme': {
                    'StorageType': 'char8',
                    'LevelType': "nominal",
                    'UsageType': "focus",
                },
            },
            # access
            # activity
            # adm1 | Top-level subnational administrative area (e.g. a
            #        governorate in Syria). Since HXL 1.0.
            #        Defaults to +v_pcode with the +code attribute if you do
            #        not specify a vocabulary.
            'adm1': {
                'default_if__code': {
                    'HashtagVocab': "v_pcode",
                },
                'default_if__v_pcode': {
                    # BR310620005 (12 chars) would be 'Código de Subdistrito
                    # Completo for Belo Horizonte' if added as P-Code, but
                    # on a quick look, most PCodes seesm to be 10 or less
                    # characters (exact bytes)
                    # Lets just put 16 to be safe
                    'StorageType': "varchar16"  # TODO: Maybe varchar12?
                }
            },
            # adm2 | Second-level subnational administrative area (e.g. a
            #        subdivision in Bangladesh). Since HXL 1.0.
            #        Defaults to +v_pcode with the +code attribute if you do
            #        not specify a vocabulary.
            'adm2': {
                'default_if__code': {
                    'HashtagVocab': "v_pcode",
                },
                'default_if__v_pcode': {
                    'StorageType': "varchar16"  # TODO: Maybe varchar12?
                }
            },
            # adm3 | Third-level subnational administrative area (e.g. a
            #        subdistrict in Afghanistan). Since HXL 1.0.
            #        Defaults to +v_pcode with the +code attribute if you do
            #        not specify a vocabulary.
            'adm3': {
                'default_if__code': {
                    'HashtagVocab': "v_pcode",
                },
                'default_if__v_pcode': {
                    'StorageType': "varchar16"  # TODO: Maybe varchar12?
                }
            },
            # adm4 | Fourth-level subnational administrative area (e.g. a
            #        barangay in the Philippines). Since HXL 1.0.
            #        Defaults to +v_pcode with the +code attribute if you do
            #        not specify a vocabulary.
            'adm4': {
                'default_if__code': {
                    'HashtagVocab': "v_pcode",
                },
                'default_if__v_pcode': {
                    'StorageType': "varchar16"  # TODO: Maybe varchar12?
                }
            },
            # adm5 | Fifth-level subnational administrative area (e.g. a
            #        ward of a city). Since HXL 1.0.
            #        Defaults to +v_pcode with the +code attribute if you do
            #        not specify a vocabulary.
            'adm5': {
                'default_if__code': {
                    'HashtagVocab': "v_pcode",
                },
                'default_if__v_pcode': {
                    'StorageType': "varchar16"  # TODO: Maybe varchar12?
                }
            },
            # affected | Number of people or households affected by an
            #            emergency
            'affected': {
                'DataType': "number",
                'StatisticalType': "count",
            },
            # beneficiary
            # capacity
            # cause
            # channel
            # contact | Contact information for the subject of a data record
            #           (e.g. an activity).
            #           Since HXL 1.0.
            # country | Country (often left implied in a dataset). Also
            #           sometimes known as admin level 0. Since HXL 1.0.
            # @see https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
            'country': {
                'default_if__code': {
                    'HashtagVocab': "v_iso3",
                },
                'default_if__v_iso3': {
                    'StorageType': "char3"  # BRA/076 (BR?) ...
                }
            },
            # crisis | A humanitarian emergency. Since HXL 1.0.
            #          Defaults to +v_glide with the +code attribute if you do
            #          not specify a vocabulary.
            'crisis': {
                'default_if__code': {
                    'HashtagVocab': "v_glide",
                },
                'default_if__v_glide': {
                    # TODO: what storage do GLIDE use?
                    'StorageType': "char18"  # EQ-2021-000015-JPN ...
                }
            },
            # currency | Name or ISO 4217 currency code for all financial
            #            #value cells in the row (e.g. “EUR”). Typically used
            #            together with #value in financial or cash data.
            #            Since HXL 1.1.
            'currency': {
                # @see https://en.wikipedia.org/wiki/ISO_4217
                'default_if__code': {
                    'HashtagVocab': 'v_iso4217',
                    'UsageType': 'input',
                },
                'default_if__v_iso4217': {
                    'StorageType': 'char3',  # USD/840, VES/928, BRL/986, ...
                }
            },
            # date | Date related to the data in the record applies.
            #        Preferred format is ISO 8610 (e.g. "2015-06-01",
            #        "2015-Q1", etc.)
            #        Since HXL 1.0.
            #        Note to self: date be viewed both as discrete and as
            #        continuous
            #        @see https://stats.stackexchange.com/questions/220812/
            #           time-is-a-continuous-or-discrete-variables
            'date': {
                'DataType': "date"
            },
            # delivery
            # description | Long description for a data record. Since HXL 1.0.
            #
            # Implementers notes (Without extra context) we decide to:
            #   - varcharu: enforce any size, but must accept Unicode
            #   - meta: While do exist cases (like text mining, sentiment
            #     analysis, etc) that #description could be input, we default
            #     to meta.
            'description': {
                'DataType': "text",
                'StorageType': "varcharu",
                'StatisticalType': "meta",
                'LevelType': "meta",
                'UsageType': "meta",
            },
            # event
            # frequency | The frequency with which something occurs.
            #             Since HXL 1.1.
            #             Note to self: need to check better if 95% of the time
            #             this is right
            #             @see https://en.wikipedia.org/wiki/Ordinal_data
            'frequency': {
                'StatisticalType': "ordinal"
            },
            # geo
            # group
            # impact
            # indicator
            # inneed | Number of people or households in need of humanitarian
            #         assistance.
            'inneed': {
                'DataType': "number",
                'StatisticalType': "count",
            },
            # item
            # loc
            # meta
            'meta': {
                'UsageType': "meta",
                'datafeature_orange': "meta",
            },
            # modality
            # need
            # operations
            # org
            # output
            # population | General population number for an area or location,
            #             regardless of their specific humanitarian needs.
            #             Since HXL 1.0.
            'population': {
                'DataType': "number",
                'StatisticalType': "count",
            },
            # reached | Number of people or households reached with
            #           humanitarian assistance. Subset of #targeted.
            #           Since HXL 1.0.
            'reached': {
                'DataType': "number",
                'StatisticalType': "count",
            },
            # region
            # respondee
            # sector | A humanitarian cluster or sector. Since HXL 1.0.
            #          Defaults to +v_ocha_clusters with the +code attribute
            #          if you do not specify a vocabulary.
            'sector': {
                'default_if__code': {
                    'HashtagVocab': 'v_ocha_clusters',
                    'UsageType': 'input',
                },
                'default_if__v_ocha_clusters': {
                    # 'StorageType': '???',  # TODO: check v_ocha_clusters
                    #                                maximum storage usage
                }
            },
            # service
            # severity
            # status
            # subsector
            # targeted | Number of people or households targeted for
            #            humanitarian assistance. Subset of #inneed; superset
            #            of #reached.
            #            Since HXL 1.0.
            'targeted': {
                'DataType': "number",
                'StatisticalType': "count",
            },
            # value | A monetary value, such as the price of goods in a market,
            #         a project budget, or the amount of cash transferred to
            #         beneficiaries. May be used together with #currency in
            #         financial or cash data.
            #         Since HXL 1.1.
            'value': {
                'DataType': "number"
                # TODO: see currency. We could consider do some advanced
                #       Check here to more specific StorageType if the user
                #       does not choose to do full dataset column analysis
            },
        },
        'attributes': {
            # ### HXL official Core attributes ________________________________
            # @see https://docs.google.com/spreadsheets/d/
            # 1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/edit#gid=1810309357
            # +code
            'code': {
                # 'DataType': "text" # Codes may not be text (but most are)
            },
            # +coord
            # +dest
            # +displaced
            # +elevation
            # +email (also an HXL Core Data Type)
            # +id | Unique identifier for a data record
            #       Use with #meta to provide internal identifiers for data
            #       records.
            # Notes to implementers (without extra explicitl context):
            #   - meta: for data mining, most of the time +id are so unique
            #     that are very likely to be meta.
            'id': {
                'StatisticalType': "meta",
                'LevelType': "meta",
                'UsageType': "meta",
            },
            # +label | Is a narrative label
            #          Text labels (for a table or chart).
            # Notes to implementers (without extra explicitl context):
            #   - meta: for data mining, most of the time +name/+label, in
            #     specia if already exist a column with +code/+type, to
            #     consider as meta.
            'label': {
                'DataType': "text",
                'StatisticalType': "meta",
                'LevelType': "meta",
                'UsageType': "meta",
            },
            # +lat
            # +lon
            # +name | Is a name or title
            #         Human-readable name, title, or label.
            # Notes to implementers (without extra explicitl context):
            #   - meta: for data mining, most of the time +name/+label, in
            #     specia if already exist a column with +code/+type, to
            #     consider as meta.
            'name': {
                'DataType': "text",
                'StatisticalType': "meta",
                'LevelType': "meta",
                'UsageType': "meta",
            },
            # +num
            'num': {
                'DataType': "number"
            },
            # +pct
            # +phone (also an HXL Core Data Type)
            # +start
            # +text  (also an HXL Core Data Type)
            # +type
            # +url  (also an HXL Core Data Type)
            # ### HXL Data Types ______________________________________________
            # text
            'text': {
                'DataType': "text"
            },
            # number
            'number': {
                'DataType': "number"
            },
            # url | Is a web link (URL)
            #       The data consists of web links related to the main hashtag
            #       (e.g. for an #org, #service, #activity, #loc, etc).
            # Notes to implementers (without extra explicitl context):
            #   - meta: url/email/phone are very likely to be meta
            #   - varcharu: url/email MAY contain unicode characters
            'url': {
                'DataType': "url",
                'StorageType': "varcharu",
                'StatisticalType': "meta",
                'LevelType': "meta",
                'UsageType': "meta",
            },
            # email | Is an e-mail address
            #         Email address.
            # Notes to implementers (without extra explicitl context):
            #   - meta: url/email/phone are very likely to be meta
            #   - varcharu: url/email MAY contain unicode characters
            'email': {
                'DataType': "email",
                'StorageType': "varcharu",  # TODO: maybe varcharu128?
                'StatisticalType': "meta",
                'LevelType': "meta",
                'UsageType': "meta",
            },
            # phone | Is a phone number
            #         The data consists of #contact phone numbers.
            #   - meta: url/email/phone are very likely to be meta
            #   - varchar: phone is unlikely to unicode characters (but can
            #     " ", "(", ")", "-", ".", as example)
            'phone': {
                'DataType': "phone",
                'StorageType': "varchar",  # TODO: maybe varchar24?
                'StatisticalType': "meta",
                'LevelType': "meta",
                'UsageType': "meta",
            },
            # date | see #data (HXL Core attributes do not have an +date)
            # Notes to implementers (without extra explicitl context):
            #   - date/number/pct are likely to be input (sometimes focus)
            #     even when they may be considered as meta by the standard.
            'date': {
                'DataType': "date"
            },
        }
    }

    def __init__(self, local_hxl_file=None):
        """
        Constructs all the necessary attributes for the HXLMeta
        object.
        """

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

        # TODO: Use some abstraction instead of access directly the file
        self.local_hxl_file = local_hxl_file
        self.text_headers = None
        self.hxl_headers = None
        self.HXLMetaType = HXLMetaType()
        # self.hxlmeta

    def _parse_heading(self, heading):
        # @see https://stackoverflow.com/questions/8270092/
        #      remove-all-whitespace-in-a-string
        # pattern = re.compile(r'\s+')
        heading1 = re.sub(self._WHITESPACE_PATTERN, '', heading)
        return heading1

    def debuginfo(self):
        print(' ')
        print('> HXLMeta debuginfo')
        with open(self.local_hxl_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_1st = next(csv_reader)
            line_2nd = next(csv_reader)
            # line_start = -1

            if line_1st[0].find('#') == -1 and line_2nd[0].find('#') == 0:
                self.text_headers = line_1st
                self.hxl_headers = line_2nd
                # line_start = 1
            elif line_1st[0].find('#') == 0:
                self.text_headers = None
                self.hxl_headers = line_1st
                # line_start = 0
            else:
                raise Exception("HXLMetaUnknownSourceException")

            # for line in csv_reader:
            #    txt_writer.writerow(line)

            # Hotfix: skip first non-HXL header. Ideally I think the already
            # exported HXlated file should already save without headers.
            print(' >> HXLMeta.text_headers', self.text_headers)
            print(' >> HXLMeta.hxl_headers', self.hxl_headers)

            for header in self.hxl_headers:
                self.get_hashtag_info(header)

            # header_original = next(csv_reader)
            # print('header_original', header_original)

    def get_data_type(self, values, hashtag=None):
        raise NotImplementedError('TODO')

    # hxlquickmeta --hxlquickmeta-hashtag="#adm2+code"
    #              --hxlquickmeta-value="BR3106200"

    # TODO: implement some type of external webservice checking to print
    #       more information when an value is an PCode. Maybe
    #       https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External
    #       have this?
    def get_hashtag_info(self, hashtag, value=None):
        print('> get_hashtag_info [', hashtag, ']', '[', value, ']')
        print('>> hashtag:', hashtag)
        print('>>> HXLMeta._parse_heading:', self._parse_heading(hashtag))
        print('>>> HXLMeta.is_hashtag_base_valid:',
              self.is_hashtag_base_valid(hashtag))
        print('>>> libhxl_is_token', self.HXLMetaType.libhxl_is_token(hashtag))

        if value is not None:
            print('>> value:', value)
            print('>>> libhxl_is_empty',
                  self.HXLMetaType.libhxl_is_empty(value))
            print('>>> libhxl_is_date', self.HXLMetaType.libhxl_is_date(value))
            print('>>> libhxl_is_number',
                  self.HXLMetaType.libhxl_is_number(value))
            print('>>> libhxl_is_string',
                  self.HXLMetaType.libhxl_is_string(value))
            print('>>> libhxl_is_token',
                  self.HXLMetaType.libhxl_is_token(hashtag))
            print('>>> libhxl_is_truthy',
                  self.HXLMetaType.libhxl_is_truthy(value))
            print('>>> libhxl_typeof',
                  self.HXLMetaType.libhxl_typeof(value))

    def get_level_type(self, values, hashtag=None):
        raise NotImplementedError('TODO')

    def get_statistical_type(self, values, hashtag=None):
        raise NotImplementedError('TODO')

    def get_storage_type(self, values, hashtag=None):
        raise NotImplementedError('TODO')

    def get_usage_type(self, values, hashtag=None):
        raise NotImplementedError('TODO')

    def get_weight_level(self, values, hashtag=None):
        raise NotImplementedError('TODO')

    def is_hashtag_base_valid(self, term, strict=True):
        if strict:
            return hxl.datatypes.is_token(term)
        # @see docs.python.org/3/library/exceptions.html#exception-hierarchy
        raise NotImplementedError('Less strict validation not implemented')


# class HXLDataset(hxl.model.Dataset):
# class HXLDataset(hxl.io.HXLReader):
class HXLMetaDataset(object):
    """
    HXLMetaDataset parse one already well HXLated file on local disk and
    then extra information. It cannot work with stream data.

    Note to self: Learn more Python (fititnt, 2021-02-20 22:34 BRT)
    TODO: ideally this shoud extend the hxl.model.Dataset or something
          but for now I think will just bootstrap and assume an perfect
          HXLated dataset on the disk and focus more on the first rows
          (fititnt, 2021-02-21 01:27 BRT)
    NOTE: Wow. hxl.model.Dataset / hxl.io.HXLReader are optimized to work with
          data streaming. That's why is memory efficient while very
          complicated to extend for do full analysis. HXLDataset was
          renamed to HXLMetaDataset and may never extend
          hxl.model.Dataset (fititnt, 2021-02-21 01:54 BRT)

    See
      - github.com/HXLStandard/libhxl-python/blob/master/hxl/model.py
      - github.com/HXLStandard/libhxl-python/blob/master/hxl/io.py
    """
    # TODO: do the draft

    def __init__(self, input):
        # """
        # Args:
        #     input (hxl.io.AbstractInput): an input source for raw data rows

        # """
        self._input = input
        # # TODO - for repeatable raw input, start a new iterator each time
        # # TODO - need to figure out how to handle columns in a repeatable sit
        # self._iter = iter(self._input)
        # self._columns = None
        # self._source_row_number = -1 # TODO this belongs in the iterator

    def parse_input(self):
        print('parse_input self._input', self._input)

        with open(self._input) as csvfile:
            print('parse_input open csvfile', csvfile)
            # csv_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                print('row', row)

            # import time
            # time.sleep(30)
            print('parse_input end')


class BooleanHXLtype:
    """
    BooleanHXLtype at this moment is just an meta example of a class in python
    to deal with more details on single booleans with even more valid values
    than libraries like Pandas. This is not optimized for performance.

    THIS IS NOT A REAL HXL DATATYPE!

    See https://github.com/HXL-CPLP/forum/issues/49
    See https://docs.google.com/spreadsheets/d/
        1hGUxMN2ywWNv8ONQ59Pp9Q4nG-eTRnAs0SyWunFZUDg/edit#gid=214068544

    """
    # TODO: do the draft


class HXLMetaExtras:
    """
    HXLMetaExtras adds extra functionality to HXLMeta that requires more
    complex dependencies to be installed than ones already required by
    libhxl-python.

    Author: Emerson Rocha
    License: Public Domain
    Version: v0.6.7

    Requires
    --------
    pandas
    orange
    """

    def __init__(self, local_hxl_file=None):

        self.logger = logging.getLogger(__name__)

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

        # self.path_file_csv = path_file_csv
        self.local_hxl_file = local_hxl_file
        self.df = None

    def debuginfo(self):
        print(' ')
        print(' >> HXLMetaExtras: Pandas DataFrame ')

        try:

            self.df = pd.read_csv(self.local_hxl_file)
            # self.df = pd.read_csv(self.local_hxl_file, sep="\t")
            # self.df = pd.read_csv(self.local_hxl_file, header=1)
            print('   >>> DataFrame')
            print(self.df)
            print('   >>> DataFrame.T')
            print(self.df.T)
            print('   >>> DataFrame.describe')
            print(self.df.describe())
        except Exception:
            print('   >>> DataFrame failed; Ignoring...')

        print(' ')
        print(' >> HXLMetaExtras: Orange Data Mining')
        # data = Orange.data.Table(self.local_hxl_file)
        # data = Orange.data.Table('tests/files/iris_hxlated-tab.tab')
        # print(data)
        # print('data.domain', data.domain)
        # print('data.columns', data.columns)

        data = Orange.data.Table.from_file(self.local_hxl_file)
        print('data.domain', data.domain)
        print('data.columns', data.columns)
        # print(data)

        # raise NotImplementedError('TODO')

    @staticmethod
    def get_pandas_dataframe(path_file_csv):
        raise NotImplementedError('TODO')

    @staticmethod
    def get_pandas_dataframe_overview(df):
        raise NotImplementedError('TODO')


class HXLMetaType:
    """
    HXLMetaType is a wrapper both to libhxl-python datatype-like functions and
    the new experimental ones used on HXLMeta.

    While HXLMeta may return *Types based on already HXLated columns, the
    HXLMeta can be used directly on a values themselves.

    Author: Emerson Rocha
    License: Public Domain
    Version: v0.6.6

    See also:
      - github.com/HXLStandard/libhxl-python/blob/master/hxl/datatypes.py
      - github.com/HXLStandard/libhxl-python/blob/master/hxl/model.py
      - github.com/HXLStandard/libhxl-python/blob/master/hxl/validation.py
    """

    @staticmethod
    def get_boolean_value(value):
        raise NotImplementedError('TODO')

    @staticmethod
    def get_storage_type_int_size(value):
        # https://stackoverflow.com/questions/14329794/
        # get-size-of-integer-in-python
        raise NotImplementedError('TODO')

    @staticmethod
    def is_boolean(value):
        raise NotImplementedError('TODO')

    @staticmethod
    def libhxl_is_empty(value):
        return hxl.datatypes.is_empty(value)

    @staticmethod
    def libhxl_is_date(value):
        return hxl.datatypes.is_date(value)

    # @staticmethod
    # def libhxl_is_dict(value):
    #     return hxl.datatypes.is_dict(value)

    @staticmethod
    def libhxl_is_number(value):
        return hxl.datatypes.is_number(value)

    @staticmethod
    def libhxl_is_string(value):
        return hxl.datatypes.is_string(value)

    @staticmethod
    def libhxl_is_token(value):
        return hxl.datatypes.is_token(value)

    @staticmethod
    def libhxl_is_truthy(value):
        return hxl.datatypes.is_truthy(value)

    @staticmethod
    def libhxl_typeof(value):
        return hxl.datatypes.typeof(value)


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

    hxlquickmeta = HXLQuickMeta()
    args = hxlquickmeta.make_args_hxlquickmeta()

    hxlquickmeta.execute_cli(args)


def exec_from_console_scripts():
    hxlquickmeta_ = HXLQuickMeta()
    args_ = hxlquickmeta_.make_args_hxlquickmeta()

    hxlquickmeta_.execute_cli(args_)


@hug.format.content_type('text/csv')
def output_csv(data, response):
    if isinstance(data, dict) and 'errors' in data:
        response.content_type = 'application/json'
        return hug.output_format.json(data)
    response.content_type = 'text/csv'
    if hasattr(data, "read"):
        return data

    return str(data).encode("utf8")


@hug.get('/hxlquickmeta_output.csv', output=output_csv)
def api_hxlquickmeta_output(source_url):
    """hxlquickmeta_output
    (@see https://github.com/EticaAI/HXL-Data-Science-file-formats)

    Example:
    http://localhost:8000/hxlquickmeta_output.csv?source_url=https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833

    """

    hxlquickmeta = HXLQuickMeta()

    return hxlquickmeta.execute_web(source_url)


@hug.get('/hxlmeta')
def api_hxlmeta(source_url):
    """hxlmeta (@see https://github.com/EticaAI/HXL-Data-Science-file-formats)

    Example:
    http://localhost:8000/hxlmeta?source_url=https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833

    """

    hxlquickmeta = HXLQuickMeta()

    return hxlquickmeta.execute_web(source_url=source_url, hxlmeta=True)

# TODO: https://chardet.github.io/
