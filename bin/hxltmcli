#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  hxltmcli.py
#
#         USAGE:  hxltmcli un-htcds.tm.hxl.csv un-htcds.xliff
#                 cat un-htcds.tm.hxl.csv | hxltmcli > un-htcds.xliff
#
#   DESCRIPTION:  _[eng-Latn] The HXLTM reference implementation in python.
#                             While this can installed with hdp-toolchain:
#                                 pip install hdp-toolchain
#                             The one--big-file hxltmcli.py (along with the
#                             cor.hxltm.yml) can be customized as single
#                             python script. But on this case, you will need
#                             to install at least the hard dependencies
#                             of hxltmcli:
#                                 pip install libhxl langcodes pyyaml
#                 [eng-Latn]_
#                 @see http://docs.oasis-open.org/xliff/xliff-core/v2.1
#                      /os/xliff-core-v2.1-os.html
#                 @see https://www.gala-global.org/lisa-oscar-standards
#                 @see https://github.com/HXL-CPLP/forum/issues/58
#                 @see https://github.com/HXL-CPLP/Auxilium-Humanitarium-API
#                      /issues/16
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                     - libhxl (@see https://pypi.org/project/libhxl/)
#                       - pip3 install libhxl
#                     - langcodes (@see https://github.com/rspeer/langcodes)
#                       - pip3 install langcodes
#                     - pyyaml (@see https://github.com/yaml/pyyaml)
#                       - pip3 install pyyaml
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v0.8.2
#       CREATED:  2021-06-27 19:50 UTC v0.5, de github.com/EticaAI
#                     /HXL-Data-Science-file-formats/blob/main/bin/hxl2example
#      REVISION:  2021-06-27 21:16 UTC v0.6 de hxl2tab
#      REVISION:  2021-06-27 23:53 UTC v0.7 --archivum-extensionem=.csv
#                 2021-06-29 22:29 UTC v0.8 MVP of --archivum-extensionem=.tmx
#                                    Translation Memory eXchange format (TMX).
#                 2021-06-29 23:16 UTC v0.8.1 hxltm2xliff renamed to hxltmcli;
#                      Moved from github.com/HXL-CPLP/Auxilium-Humanitarium-API
#                       to github.com/EticaAI/HXL-Data-Science-file-formats
#                 2021-07-04 04:35 UTC v0.8.2 Configurations on cor.hxltm.yml
# ==============================================================================

# Tests
# Exemplos: https://github.com/oasis-tcs/xliff-xliff-22/blob/master/xliff-21
#          /test-suite/core/valid/allExtensions.xlf
# ./_systema/programma/hxltmcli.py --help
# ./_systema/programma/hxltmcli.py _hxltm/schemam-un-htcds.tm.hxl.csv
# ./_systema/programma/hxltmcli.py _hxltm/schemam-un-htcds-5items.tm.hxl.csv
# ./_systema/programma/hxltmcli.py _hxltm/schemam-un-htcds.tm.hxl.csv \
#    --fontem-linguam=eng-Latn
# ./_systema/programma/hxltmcli.py _hxltm/schemam-un-htcds-5items.tm.hxl.csv \
#    --fontem-linguam=eng-Latn --archivum-extensionem=.tmx
# ./_systema/programma/hxltmcli.py _hxltm/schemam-un-htcds-5items.tm.hxl.csv \
#    _hxltm/schemam-un-htcds-5items.tmx --fontem-linguam=eng-Latn \
#    --archivum-extensionem=.tmx
# python3 -m doctest ./_systema/programma/hxltmcli.py
# python3 -m doctest bin/hxltmcli
# python3 -m doctest hxlm/core/bin/hxltmcli.py

# from re import S
import sys
import os
import logging
import argparse
from pathlib import Path

import csv
import tempfile

from functools import reduce
from typing import (
    Any,
    Dict,
    List,
    Type,
    Union,
)

from dataclasses import dataclass, InitVar

import json
import yaml

# @see https://github.com/HXLStandard/libhxl-python
#    pip3 install libhxl --upgrade
# Do not import hxl, to avoid circular imports
import hxl.converters
import hxl.filters
import hxl.io
import hxl.datatypes

# @see https://github.com/rspeer/langcodes
# pip3 install langcodes
import langcodes

__VERSION__ = "v0.8.2"

# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer

_HOME = str(Path.home())

# TODO: clean up redundancy from hxlm/core/schema/urn/util.py
HXLM_CONFIG_BASE = os.getenv(
    'HXLM_CONFIG_BASE', _HOME + '/.config/hxlm')
# ~/.config/hxlm/cor.hxltm.yml
# This can be customized with enviroment variable HXLM_CONFIG_BASE


# Since hpd-toolchain is not a hard requeriment, we first try to load
# hdp-toolchain lib, but if hxltmcli is a standalone script with
# only libhxl, yaml, etc installed, we tolerate it
try:
    from hxlm.core.constant import (
        HXLM_ROOT
    )
    HXLTM_SCRIPT_DIR = HXLM_ROOT + '/core/bin'
except ImportError:
    HXLTM_SCRIPT_DIR = str(Path(__file__).parent.resolve())

HXLTM_RUNNING_DIR = str(Path().resolve())


class HXLTMCLI:
    """
    _[eng-Latn] hxltmcli is an working draft of a tool to
                convert prototype of translation memory stored with HXL to
                XLIFF v2.1
    [eng-Latn]_
    """

    def __init__(self):
        """
        _[eng-Latn] Constructs all the necessary attributes for the
                    HXLTMCLI object.
        [eng-Latn]_
        """
        self.hxlhelper = None
        self.args = None
        self.conf = {}  # Crudum, raw file
        self.otlg = None  # HXLTMOntologia object
        self.objectivum_typum = None
        self.fontem_linguam: HXLTMLinguam = None
        self.objectivum_linguam: HXLTMLinguam = None
        self.alternativum_linguam: List[HXLTMLinguam] = []
        self.linguam: List[HXLTMLinguam] = []
        self.datum: HXLTMDatum = None
        # self.meta_archivum_fontem = {}
        self.meta_archivum_fontem = {}
        self.errors = []

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

        self.original_outfile = None
        self.original_outfile_is_stdout = True

    def _objectivum_typum_from_outfile(self, outfile):
        """Uses cor.hxltm.yml fontem_archivum_extensionem to detect output
        format without user need to explicitly inform the option.

        This is not used if the result is stdout

        Args:
            outfile ([str]): Path string of output file

        Returns:
            [str]: A valid cor.hxltm.yml formatum
        """
        outfile_lower = outfile.lower()

        if self.conf and self.conf['fontem_archivum_extensionem']:
            for key in self.conf['fontem_archivum_extensionem']:
                if outfile_lower.endswith(key):
                    return self.conf['fontem_archivum_extensionem'][key]

        return 'INCOGNITUM'

    def _initiale(self, args,  is_debug=False):
        """Trivia: initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        """
        # if args.expertum_metadatum_est:
        #     self.expertum_metadatum_est = args.expertum_metadatum_est

        if args.fontem_linguam:
            self.fontem_linguam = HXLTMLinguam(args.fontem_linguam)
            if is_debug:
                print('fontem_linguam', self.fontem_linguam.v())

        if args.objectivum_linguam:
            self.objectivum_linguam = HXLTMLinguam(args.objectivum_linguam)
            if is_debug:
                print('objectivum_linguam', self.objectivum_linguam.v())

        if args.alternativum_linguam and len(args.alternativum_linguam) > 0:
            unicum = set(args.alternativum_linguam)
            for rem in unicum:
                rem_obj = HXLTMLinguam(rem)
                if is_debug:
                    print('alternativum_linguam', rem_obj.v())
                self.alternativum_linguam.append(rem_obj)

        if args.linguam and len(args.linguam) > 0:
            unicum = set(args.linguam)
            for rem in unicum:
                rem_obj = HXLTMLinguam(rem)
                if is_debug:
                    print('linguam', rem_obj.v())
                self.linguam.append(rem_obj)

        # if is_debug:
        #     print('fontem_linguam', self.fontem_linguam.v())
        #     print('objectivum_linguam', self.objectivum_linguam.v())
        #     print('alternativum_linguam')
        #     if len(self.alternativum_linguam):
        #         for rem in

    def _initiale_meta_archivum_fontem_hxlated(self, archivum: str) -> bool:
        """Pre-populate metadata about source file

        Requires already HXLated file saved on disk.

        Args:
            archivum (str): Path to an already HXLated file on disk

        Returns:
            bool: If okay.
        """

        mAF = {
            # 'rem_I_textum_caput_est': None,
            'rem_I_hxl_caput_est': None,
            'rem_I': [],
            # 'rem_II_textum_caput_est': None,
            'rem_II_hxl_caput_est': None,
            'rem_II': [],
            # 'rem_III_textum_caput_est': None,
            'rem_III_hxl_caput_est': None,
            'rem_III': [],
            'rem_crudum_initialle': [],
            'rem_crudum_finale': [],
        }

        rem_crudum = []

        with open(archivum) as arch:
            rem_crudum = arch.read().splitlines()

        mAF['rem_crudum_initialle'] = \
            rem_crudum[:5]

        if len(rem_crudum) > 5:
            mAF['rem_crudum_finale'] = \
                rem_crudum[-5:]

        # @see https://docs.python.org/3/library/csv.html
        with open(archivum, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            mAF['rem_I'] = next(csv_reader)
            mAF['rem_I_hxl_caput_est'] = \
                HXLTMDatumMetaCaput.quod_est_hashtag_caput(
                    mAF['rem_I'])

            mAF['rem_II'] = next(csv_reader)
            mAF['rem_II_hxl_caput_est'] = \
                HXLTMDatumMetaCaput.quod_est_hashtag_caput(
                    mAF['rem_II'])

            mAF['rem_III'] = next(csv_reader)
            mAF['rem_III_hxl_caput_est'] = \
                HXLTMDatumMetaCaput.quod_est_hashtag_caput(
                    mAF['rem_III'])

        self.meta_archivum_fontem = mAF

    def make_args_hxltmcli(self):

        self.hxlhelper = HXLUtils()
        parser = self.hxlhelper.make_args(
            #     description=("""
            # _[eng-Latn] hxltmcli is an working draft of a tool to
            #             convert prototype of translation memory stored with
            #             HXL to XLIFF v2.1
            # [eng-Latn]_
            # """)
            description=(
                "_[eng-Latn] hxltmcli " + __VERSION__ + " " +
                "is an working draft of a tool to " +
                "convert prototype of translation memory stored with HXL to " +
                "XLIFF v2.1 [eng-Latn]_"
            )
        )

        # TODO: implement example using index number (not language) as
        #       for very simple cases (mostly for who is learning
        #       or doing very few languages) know the number is easier

        parser.add_argument(
            '--expertum-metadatum',
            help='(Expert mode) Return metadata of the operation ' +
            'in JSON format instead of generate the output. ' +
            'Good for debugging.',
            # dest='fontem_linguam',
            metavar='expertum_metadatum_est',
            action='store_const',
            const=True,
            default=False
        )

        # TODO: --expertum-HXLTM-ASA is a draft.
        parser.add_argument(
            '--expertum-HXLTM-ASA',
            help='(Expert mode) Save an Abstract Syntax Tree  ' +
            'in JSON format to a file path. ' +
            'With --venandum-insectum-est output entire dataset data. ' +
            'Good for debugging.',
            # dest='fontem_linguam',
            metavar='hxltm_asa_archivum',
            action='store',
            default='arb-Arab',
            nargs='?'
        )

        parser.add_argument(
            '--fontem-linguam', '-FL',
            help='(For bilingual operations) Source natural language ' +
            '(use if not auto-detected). ' +
            'Must be like {ISO 639-3}-{ISO 15924}. Example: lat-Latn. ' +
            'Accept a single value.',
            # dest='fontem_linguam',
            metavar='fontem_linguam',
            action='store',
            default='lat-Latn',
            nargs='?'
        )

        parser.add_argument(
            '--objectivum-linguam', '-OL',
            help='(For bilingual operations) Target natural language ' +
            '(use if not auto-detected). ' +
            'Must be like {ISO 639-3}-{ISO 15924}. Example: arb-Arab. ' +
            'Requires: mono or bilingual operation. ' +
            'Accept a single value.',
            metavar='objectivum_linguam',
            action='store',
            default='arb-Arab',
            nargs='?'
        )

        # --alternativum-linguam is a draft. Not 100% implemented
        parser.add_argument(
            '--alternativum-linguam', '-AL',
            help='(Planned, but not implemented yet) ' +
            'Alternative source languages (up to 5) to be added ' +
            'as metadata (like XLIFF <note>) for operations that ' +
            'only accept one source language. ' +
            'Requires: bilingual operation. ' +
            'Accepts multiple values.',
            metavar='alternativum_linguam',
            action='append',
            nargs='?'
        )

        # --linguam is a draft. Not 100% implemented
        parser.add_argument(
            '--linguam', '-L',
            help='(Planned, but not implemented yet) ' +
            'Restrict working languages to a list. Useful for ' +
            'HXLTM to HXLTM or multilingual formats like TMX. ' +
            'Requires: multilingual operation. ' +
            'Accepts multiple values.',
            metavar='linguam',
            action='append',
            nargs='?'
        )

        # --non-linguam is a draft. Not 100% implemented
        parser.add_argument(
            '--non-linguam', '-non-L',
            help='(Planned, but not implemented yet) ' +
            'Inverse of --non-linguam. Document one or more languages that ' +
            'should be ignored if they exist. ' +
            'Requires: multilingual operation.' +
            'Accept a single value.',
            metavar='non_linguam',
            action='append',
            nargs='?'
        )

        parser.add_argument(
            '--objectivum-HXLTM', '--HXLTM',
            help='Save output as HXLTM (default). Multilingual output format.',
            # metavar='objectivum_typum',
            dest='objectivum_typum',
            action='append_const',
            const='HXLTM'
        )

        parser.add_argument(
            '--objectivum-TMX', '--TMX',
            help='Export to Translation Memory eXchange (TMX) v1.4b. ' +
            ' Multilingual output format',
            # metavar='objectivum_typum',
            dest='objectivum_typum',
            action='append_const',
            const='TMX'
        )

        parser.add_argument(
            '--objectivum-TBX-Basim', '--TBX-Basim',
            help='(Planned, but not implemented yet) ' +
            'Export to Term Base eXchange (TBX). ' +
            ' Multilingual output format',
            # metavar='objectivum_typum',
            dest='objectivum_typum',
            action='append_const',
            const='TBX-Basim'
        )

        parser.add_argument(
            '--objectivum-UTX', '--UTX',
            help='(Planned, but not implemented yet) ' +
            'Export to Universal Terminology eXchange (UTX). ' +
            ' Multilingual output format',
            # metavar='objectivum_typum',
            dest='objectivum_typum',
            action='append_const',
            const='UTX'
        )

        parser.add_argument(
            '--objectivum-XLIFF', '--XLIFF', '--XLIFF2',
            help='Export to XLIFF (XML Localization Interchange File Format)' +
            ' v2.1. ' +
            '(mono or bi-lingual support only as per XLIFF specification)',
            dest='objectivum_typum',
            action='append_const',
            const='XLIFF'
        )

        parser.add_argument(
            '--objectivum-XLIFF-obsoletum', '--XLIFF-obsoletum', '--XLIFF1',
            help='(Not implemented) ' +
            'Export to XLIFF (XML Localization Interchange ' +
            'File Format) v1.2, an obsolete format for lazy developers who ' +
            'don\'t implemented XLIFF 2 (released in 2014) yet.',
            dest='objectivum_typum',
            action='append_const',
            const='XLIFF1'
        )

        parser.add_argument(
            '--objectivum-CSV-3', '--CSV-3',
            help='(Not implemented yet) ' +
            'Export to Bilingual CSV with BCP47 headers (source to target)' +
            ' plus comments on last column ',
            dest='objectivum_typum',
            action='append_const',
            const='CSV-3'
        )

        parser.add_argument(
            '--objectivum-CSV-HXL-XLIFF', '--CSV-HXL-XLIFF',
            help='(experimental) ' +
            'HXLated bilingual CSV (feature compatible with XLIFF)',
            dest='objectivum_typum',
            action='append_const',
            const='CSV-HXL-XLIFF'
        )

        parser.add_argument(
            '--objectivum-JSON-kv', '--JSON-kv',
            help='(Not implemented yet) ' +
            'Export to Bilingual JSON. Keys are ID (if available) or source '
            'natural language. Values are target language. '
            'No comments are exported. Monolingual/Bilingual',
            dest='objectivum_typum',
            action='append_const',
            const='JSON-kv'
        )

        # # deprecated
        # parser.add_argument(
        #     '--archivum-extensionem',
        #     help='File extension. .xlf, .csv or .tmx',
        #     action='store',
        #     # default='.xlf',
        #     default=None,
        #     nargs='?'
        # )

        # Trivia: caput, https://en.wiktionary.org/wiki/caput#Latin
        # --rudum-objectivum-caput is a draft. Not 100% implemented
        parser.add_argument(
            '--crudum-objectivum-caput',
            help='(Advanced override for tabular output, like CSV). ' +
            'Explicit define first line of output (separed by ,) ' +
            'Example: "la,ar,Annotationem"',
            metavar='fon_hxlattrs',
            action='store',
            default=None,
            nargs='?'
        )

        # --crudum-fontem-linguam-hxlattrs is a draft. Not 100% implemented
        parser.add_argument(
            '--crudum-fontem-linguam-hxlattrs', '--fon-hxlattrs',
            help='(Advanced override for --fontem-linguam). ' +
            'Explicit HXL Attributes for source language. ' +
            'Example: "+i_la+i_lat+is_latn"',
            metavar='fon_hxlattrs',
            action='store',
            default=None,
            nargs='?'
        )

        # --crudum-fontem-linguam-bcp47 is a draft. Not 100% implemented
        parser.add_argument(
            '--crudum-fontem-linguam-bcp47', '--fon-bcp47',
            help='(Advanced override for --fontem-linguam). ' +
            'Explicit IETF BCP 47 language tag for source language. ' +
            'Example: "la"',
            metavar='fon_bcp47',
            action='store',
            default=None,
            nargs='?'
        )

        # --crudum-objectivum-linguam-hxlattrs is a draft. Not 100% implemented
        parser.add_argument(
            '--crudum-objectivum-linguam-hxlattrs', '--obj-hxlattrs',
            help='(Advanced override for --objectivum-linguam). ' +
            'Explicit HXL Attributes for target language. ' +
            'Example: "+i_ar+i_arb+is_arab"',
            metavar='obj_hxlattrs',
            action='store',
            default=None,
            nargs='?'
        )

        # --crudum-objectivum-linguam-bcp47 is a draft. Not 100% implemented
        parser.add_argument(
            '--crudum-objectivum-linguam-bcp47', '--obj-bcp47',
            help='(Advanced override for --objectivum-linguam). ' +
            'Explicit IETF BCP 47 language tag for target language. ' +
            'Example: "ar"',
            metavar='obj_bcp47',
            action='store',
            default=None,
            nargs='?'
        )

        # https://hdp.etica.ai/ontologia/cor.hxltm.yml
        parser.add_argument(
            '--archivum-configurationem',
            help='Path to custom configuration file (The cor.hxltm.yml)',
            action='store_const',
            const=True,
            default=None
        )

        parser.add_argument(
            '--silentium',
            help='Silence warnings? Try to not generate any warning. ' +
            'May generate invalid output',
            action='store_const',
            const=True,
            default=False
        )

        parser.add_argument(
            # '--venandum-insectum-est, --debug',
            '--venandum-insectum-est', '--debug',
            help='Enable debug? Extra information for program debugging',
            metavar="venandum_insectum_est",
            action='store_const',
            const=True,
            default=False
        )

        self.args = parser.parse_args()
        return self.args

    def execute_cli(self, args,
                    stdin=STDIN, stdout=sys.stdout, stderr=sys.stderr):
        """
        The execute_cli is the main entrypoint of HXLTMCLI. When
        called will convert the HXL source to example format.
        """

        # # NOTE: the next lines, in fact, only generate an csv outut. So you
        # #       can use as starting point.
        # with self.hxlhelper.make_source(args, stdin) as source, \
        #         self.hxlhelper.make_output(args, stdout) as output:
        #     hxl.io.write_hxl(output.output, source,
        #                      show_tags=not args.strip_tags)

        # return self.EXIT_OK

        self._initiale(args, args.venandum_insectum_est)

        self.conf = HXLTMUtil.load_hxltm_options(
            args.archivum_configurationem,
            args.venandum_insectum_est
        )

        self.otlg = HXLTMOntologia(self.conf)

        # print(self.otlg.hxl_de_aliud_nomen_breve())
        # raise RuntimeError('JUST TESTING, remove me')

        # If the user specified an output file, we will save on
        # self.original_outfile. The args.outfile will be used for temporary
        # output
        if args.outfile:
            self.original_outfile = args.outfile
            self.original_outfile_is_stdout = False
            self.objectivum_typum = self._objectivum_typum_from_outfile(
                self.original_outfile)

        if args.objectivum_typum:
            if len(args.objectivum_typum) > 1:
                raise RuntimeError("More than 1 output format. see --help")
            self.objectivum_typum = args.objectivum_typum[0]

        try:
            temp = tempfile.NamedTemporaryFile()
            temp_csv4xliff = tempfile.NamedTemporaryFile()
            args.outfile = temp.name

            # print(temp_csv4xliff)
            # print(temp_csv4xliff.name)

            with self.hxlhelper.make_source(args, stdin) as source, \
                    self.hxlhelper.make_output(args, stdout) as output:
                # Save the HXL TM locally. It will be used by either in_csv
                # or in_csv + in_xliff
                hxl.io.write_hxl(output.output, source,
                                 show_tags=not args.strip_tags)

            self.datum = HXLTMDatum(args.outfile, self.otlg)
            self._initiale_meta_archivum_fontem_hxlated(args.outfile)

            if args.expertum_metadatum:
                self.in_expertum_metadatum(args.outfile,
                                           self.original_outfile,
                                           self.original_outfile_is_stdout,
                                           args)
                return self.EXIT_OK

            # if archivum_extensionem == '.csv':
            #     # print('CSV!')
            #     self.in_csv(args.outfile, self.original_outfile,
            #                    self.original_outfile_is_stdout, args)
            if self.objectivum_typum == 'TMX':
                # print('TMX')
                self.in_tmx(args.outfile, self.original_outfile,
                            self.original_outfile_is_stdout, args)

            elif self.objectivum_typum == 'TBX-Basim':
                raise NotImplementedError('TBX-Basim not implemented yet')

            elif self.objectivum_typum == 'UTX':
                raise NotImplementedError('UTX not implemented yet')

            elif self.objectivum_typum == 'XLIFF1':
                raise NotImplementedError('XLIFF1 not implemented')

            elif self.objectivum_typum == 'CSV-3':
                # raise NotImplementedError('CSV-3 not implemented yet')
                self.in_csv3(args.outfile, self.original_outfile,
                             self.original_outfile_is_stdout, args)

            elif self.objectivum_typum == 'CSV-HXL-XLIFF':
                # raise NotImplementedError('CSV-3 not implemented yet')
                self.in_csv(args.outfile, self.original_outfile,
                            self.original_outfile_is_stdout, args)

            elif self.objectivum_typum == 'JSON-kv':
                self.in_jsonkv(args.outfile, self.original_outfile,
                               self.original_outfile_is_stdout, args)
                # raise NotImplementedError('JSON-kv not implemented yet')

            elif self.objectivum_typum == 'XLIFF':
                # print('XLIFF (2)')
                self.in_csv(args.outfile, temp_csv4xliff.name,
                            False, args)
                self.in_xliff(temp_csv4xliff.name, self.original_outfile,
                              self.original_outfile_is_stdout, args)

            elif self.objectivum_typum == 'HXLTM':
                # print('HXLTM')
                self.in_noop(args.outfile, self.original_outfile,
                             self.original_outfile_is_stdout)

            elif self.objectivum_typum == 'INCOGNITUM':
                # print('INCOGNITUM')
                raise ValueError(
                    'INCOGNITUM (objetive file output based on extension) ' +
                    'failed do decide what you want. Check --help and ' +
                    'manually select an output format, like --TMX'
                )
            else:
                # print('default / unknow option result')
                # Here maybe error?
                # self.hxl2tab(args.outfile, self.original_outfile,
                #              self.original_outfile_is_stdout, args)

                # self.in_csv(args.outfile, temp_csv4xliff.name,
                #                False, args)
                # print('noop')
                self.in_noop(args.outfile, self.original_outfile,
                             self.original_outfile_is_stdout)

        finally:
            temp.close()
            temp_csv4xliff.close()

        return self.EXIT_OK

    def in_expertum_metadatum(
            self, hxlated_input: str, tab_output: str, is_stdout: bool, args):
        """in_expertum_metadatum

        Trivia:
        - in, https://en.wiktionary.org/wiki/in#Latin
        - expertum, https://en.wiktionary.org/wiki/expertus#Latin
        - meta
          - https://en.wiktionary.org/wiki/meta#English
            - https://en.wiktionary.org/wiki/metaphysica#Latin
        - datum, https://en.wiktionary.org/wiki/datum#Latin

        Args:
            hxlated_input ([str]): Path to input data on disk
            tab_output ([str]): If not stdout, path to output on disk
            is_stdout (bool): If is stdout
        """
        resultatum = {
            '_typum': 'HXLTMExpertumMetadatum',
            'argumentum': {
                'fontem_linguam': self.fontem_linguam.v(),
                'objectivum_linguam': self.objectivum_linguam.v(),
                'alternativum_linguam': [],
                'linguam': []
            },
            'archivum_fontem': self.meta_archivum_fontem,
            'archivum_fontem_m': {},
            'archivum_objectivum': {},
        }

        resultatum['archivum_fontem_m'] = self.datum.v()

        if len(self.alternativum_linguam) > 0:
            for rem in self.alternativum_linguam:
                resultatum['argumentum']['alternativum_linguam'].append(
                    rem.v())

        if len(self.linguam) > 0:
            for rem in self.linguam:
                resultatum['argumentum']['linguam'].append(rem.v())

        if not args.venandum_insectum_est:
            venandum_insectum_est_notitia = {
                '__annotatianem': "optio --venandum-insectum-est requirere"
            }

            resultatum['archivum_fontem'] = venandum_insectum_est_notitia

        json_out = json.dumps(
            resultatum, indent=4, sort_keys=False, ensure_ascii=False)

        # TODO: maybe implement option to save the metadata on a different
        #       file (or allow generate the metadata even if actual result
        #       final output was generated)
        print(json_out)

    def in_noop(self, hxlated_input, tab_output, is_stdout):
        """
        in_noop only export whatever the initial HXL input was.

        Requires that the input must be a valid HXLated file
        """

        with open(hxlated_input, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            if is_stdout:
                # txt_writer = csv.writer(sys.stdout, delimiter='\t')
                txt_writer = csv.writer(sys.stdout)
                # txt_writer.writerow(header_new)
                for line in csv_reader:
                    txt_writer.writerow(line)
            else:

                tab_output_cleanup = open(tab_output, 'w')
                tab_output_cleanup.truncate()
                tab_output_cleanup.close()

                with open(tab_output, 'a') as new_txt:
                    txt_writer = csv.writer(new_txt)
                    for line in csv_reader:
                        txt_writer.writerow(line)

    def in_csv(self, hxlated_input, tab_output, is_stdout, args):
        """
        in_csv pre-process the initial HXL TM on a intermediate format that
        can be used alone or as requisite of the in_xliff exporter
        """

        with open(hxlated_input, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            # TODO: fix problem if input data already only have HXL hashtags
            #       but no extra headings (Emerson Rocha, 2021-06-28 01:27 UTC)

            # Hotfix: skip first non-HXL header. Ideally I think the already
            # exported HXlated file should already save without headers.
            next(csv_reader)
            header_original = next(csv_reader)
            header_new = self.in_csv_header(
                header_original,
                fontem_linguam=args.fontem_linguam,
                objectivum_linguam=args.objectivum_linguam,
            )

            if is_stdout:
                # txt_writer = csv.writer(sys.stdout, delimiter='\t')
                txt_writer = csv.writer(sys.stdout)
                txt_writer.writerow(header_new)
                for line in csv_reader:
                    txt_writer.writerow(line)
            else:

                tab_output_cleanup = open(tab_output, 'w')
                tab_output_cleanup.truncate()
                tab_output_cleanup.close()

                with open(tab_output, 'a') as new_txt:
                    # txt_writer = csv.writer(new_txt, delimiter='\t')
                    txt_writer = csv.writer(new_txt)
                    txt_writer.writerow(header_new)
                    for line in csv_reader:
                        txt_writer.writerow(line)

    def hxl2tab(self, hxlated_input, tab_output, is_stdout, args):
        """
        (deprecated hxl2tab)
        """

        with open(hxlated_input, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Hotfix: skip first non-HXL header. Ideally I think the already
            # exported HXlated file should already save without headers.
            next(csv_reader)
            header_original = next(csv_reader)
            header_new = self.in_csv_header(
                header_original,
                fontem_linguam=args.fontem_linguam,
                objectivum_linguam=args.objectivum_linguam,
            )

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

    def in_csv3(self, hxlated_input, file_output, is_stdout, args):
        """Convert HXLTM to output 'CSV-3'

        Args:
            hxlated_input ([str]): Path to HXLated CSV
            tmx_output ([str]): Path to file to write output (if not stdout)
            is_stdout (bool): Flag to tell the output is stdout
            args ([type]): python argparse
        """

        # fon_ling = HXLTMUtil.linguam_2_hxlattrs(args.fontem_linguam)
        fon_bcp47 = HXLTMUtil.bcp47_from_linguam(args.fontem_linguam)
        # obj_ling = HXLTMUtil.linguam_2_hxlattrs(args.objectivum_linguam)
        obj_bcp47 = HXLTMUtil.bcp47_from_linguam(args.objectivum_linguam)

        data_started = False
        fon_index = None
        obj_index = None
        meta_index = None
        datum = []
        with open(hxlated_input, 'r') as csvfile:
            lines = csv.reader(csvfile)
            for row in lines:
                if not data_started:
                    if row[0].startswith('#'):
                        fon_index = 0
                        obj_index = 1
                        meta_index = 2
                        # TODO: get exact row IDs without hardcoded
                        data_started = True
                        datum.append([fon_bcp47, obj_bcp47, ''])
                    continue
                datum.append([row[fon_index], row[obj_index], row[meta_index]])
                # print(', '.join(row))

        if is_stdout:
            txt_writer = csv.writer(sys.stdout)
            for line in datum:
                txt_writer.writerow(line)
        else:
            old_file = open(file_output, 'w')
            old_file.truncate()
            old_file.close()

            with open(file_output, 'a') as new_txt:
                txt_writer = csv.writer(new_txt)
                for line in datum:
                    txt_writer.writerow(line)

    def in_jsonkv(self, hxlated_input, file_output, is_stdout, args):
        """Convert HXLTM to output 'JSON-kv'

        Args:
            hxlated_input ([str]): Path to HXLated CSV
            tmx_output ([str]): Path to file to write output (if not stdout)
            is_stdout (bool): Flag to tell the output is stdout
            args ([type]): python argparse
        """

        # fon_ling = HXLTMUtil.linguam_2_hxlattrs(args.fontem_linguam)
        # fon_bcp47 = HXLTMUtil.bcp47_from_linguam(args.fontem_linguam)
        # obj_ling = HXLTMUtil.linguam_2_hxlattrs(args.objectivum_linguam)
        # obj_bcp47 = HXLTMUtil.bcp47_from_linguam(args.objectivum_linguam)

        data_started = False
        fon_index = None
        obj_index = None
        # meta_index = None
        datum = {}
        with open(hxlated_input, 'r') as csvfile:
            lines = csv.reader(csvfile)
            for row in lines:
                if not data_started:
                    if row[0].startswith('#'):
                        fon_index = 0
                        obj_index = 1
                        # meta_index = 2
                        # TODO: get exact row IDs without hardcoded
                        data_started = True
                        # datum.append([fon_bcp47, obj_bcp47, ''])
                    continue
                datum[row[fon_index]] = row[obj_index]
                # print(', '.join(row))
        json_out = json.dumps(
            datum, indent=4, sort_keys=True, ensure_ascii=False)

        if is_stdout:
            # print(json_out)
            for line in json_out.split("\n"):
                print(line)
                # sys.stdout.write(line + "\n")

        else:
            old_file = open(file_output, 'w')
            old_file.truncate()
            old_file.close()

            # TODO: test this part better.
            with open(file_output, 'a') as new_txt:
                new_txt.write(json_out)
                # txt_writer = csv.writer(new_txt)
                # for line in datum:
                #     txt_writer.writerow(line)

    def in_tmx(self, hxlated_input, tmx_output, is_stdout, args):
        """
        in_tmx is  is the main method to de facto make the conversion.

        TODO: this is a work-in-progress at this moment, 2021-06-28
        @see https://en.wikipedia.org/wiki/Translation_Memory_eXchange
        @see https://www.gala-global.org/lisa-oscar-standards
        @see https://cloud.google.com/translate/automl/docs/prepare
        @see http://xml.coverpages.org/tmxSpec971212.html
        """

        datum = []

        with open(hxlated_input, 'r') as csv_file:
            # TODO: fix problem if input data already only have HXL hashtags
            #       but no extra headings (Emerson Rocha, 2021-06-28 01:27 UTC)

            # Hotfix: skip first non-HXL header. Ideally I think the already
            # exported HXlated file should already save without headers.
            next(csv_file)

            csvReader = csv.DictReader(csv_file)

            # Convert each row into a dictionary
            # and add it to data
            for item in csvReader:

                datum.append(HXLTMUtil.tmx_item_relevan_options(item))

        resultatum = []
        resultatum.append("<?xml version='1.0' encoding='utf-8'?>")
        resultatum.append('<!DOCTYPE tmx SYSTEM "tmx14.dtd">')
        resultatum.append('<tmx version="1.4">')
        # @see https://www.gala-global.org/sites/default/files/migrated-pages
        #      /docs/tmx14%20%281%29.dtd
        resultatum.append(
            '  <header creationtool="hxltm" creationtoolversion="' +
            __VERSION__ + '" ' +
            'segtype="sentence" o-tmf="UTF-8" ' +
            'adminlang="en" srclang="en" datatype="PlainText"/>')
        # TODO: make source and adminlang configurable
        resultatum.append('  <body>')

        num = 0

        for rem in datum:
            num += 1

            # unit_id = rem['#item+id'] if '#item+id' in rem else num
            if '#item+id' in rem:
                unit_id = rem['#item+id']
            elif '#item+conceptum+codicem' in rem:
                unit_id = rem['#item+conceptum+codicem']
            else:
                unit_id = num

            resultatum.append('    <tu tuid="' + str(unit_id) + '">')
            if '#item+wikidata+code' in rem and rem['#item+wikidata+code']:
                resultatum.append(
                    '      <prop type="wikidata">' +
                    rem['#item+wikidata+code'] + '</prop>')

            if '#meta+item+url+list' in rem and rem['#meta+item+url+list']:
                resultatum.append(
                    # TODO: improve naming
                    '      <prop type="meta_urls">' + \
                    rem['#meta+item+url+list'] + '</prop>')

            hattrsl = HXLTMUtil.hxllangattrs_list_from_item(rem)
            # print(hattrsl)
            for langattrs in hattrsl:
                # print(langattrs)

                if '#item' + langattrs in rem:
                    keylang = '#item' + langattrs
                elif '#item+rem' + langattrs in rem:
                    keylang = '#item+rem' + langattrs
                else:
                    keylang = 'no-key-found-failed'

                if keylang in rem:
                    bcp47 = HXLTMUtil.bcp47_from_hxlattrs(langattrs)
                    resultatum.append('      <tuv xml:lang="' + bcp47 + '">')
                    resultatum.append(
                        '        <seg>' + rem[keylang] + '</seg>')
                    resultatum.append('      </tuv>')

            resultatum.append('    </tu>')

        resultatum.append('  </body>')
        resultatum.append('</tmx>')

        if is_stdout:
            for ln in resultatum:
                print(ln)
        else:
            tmx_output_cleanup = open(tmx_output, 'w')
            tmx_output_cleanup.truncate()
            tmx_output_cleanup.close()

            with open(tmx_output, 'a') as new_txt:
                for ln in resultatum:
                    new_txt.write(ln + "\n")
                    # print (ln)

    def in_xliff(self, hxlated_input, xliff_output, is_stdout, args):
        """
        in_xliff is  is the main method to de facto make the conversion.

        TODO: this is a work-in-progress at this moment, 2021-06-28
        """

        datum = []

        with open(hxlated_input, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file)

            # Convert each row into a dictionary
            # and add it to data
            for item in csvReader:

                datum.append(HXLTMUtil.xliff_item_relevant_options(item))

        resultatum = []
        resultatum.append('<?xml version="1.0"?>')
        resultatum.append(
            '<xliff xmlns="urn:oasis:names:tc:xliff:document:2.0" ' +
            'version="2.0" srcLang="en" trgLang="fr">')
        resultatum.append('  <file id="f1">')

        num = 0

        for rem in datum:
            num += 1
            if '#x_xliff+unit+id' in rem and rem['#x_xliff+unit+id']:
                unit_id = rem['#x_xliff+unit+id']
            else:
                unit_id = num
            # unit_id = rem['#x_xliff+unit+id'] if rem['#x_xliff+unit+id'] \
            #               else num
            resultatum.append('      <unit id="' + str(unit_id) + '">')

            resultatum.append('        <segment>')

            xsource = HXLTMUtil.xliff_item_xliff_source_key(rem)
            if xsource:
                if not rem[xsource]:
                    resultatum.append(
                        '          <!-- ERROR source ' + str(unit_id) +
                        ', ' + xsource + '-->')
                    if not args.silentium:
                        print('ERROR:', unit_id, xsource)
                        # TODO: make exit status code warn about this
                        #       so other scripts can deal with bad output
                        #       when --silentium is not used
                    # continue
                else:
                    resultatum.append('          <source>' +
                                      rem[xsource] + '</source>')

            xtarget = HXLTMUtil.xliff_item_xliff_target_key(rem)
            if xtarget and rem[xtarget]:
                resultatum.append('          <target>' +
                                  rem[xtarget] + '</target>')

            resultatum.append('        </segment>')

            resultatum.append('      </unit>')

        resultatum.append('  </file>')
        resultatum.append('</xliff>')

        if is_stdout:
            for ln in resultatum:
                print(ln)
        else:
            xliff_output_cleanup = open(xliff_output, 'w')
            xliff_output_cleanup.truncate()
            xliff_output_cleanup.close()

            with open(xliff_output, 'a') as new_txt:
                for ln in resultatum:
                    new_txt.write(ln + "\n")
                    # print (ln)

    def in_xliff_old(self, hxlated_input, xliff_output, is_stdout, args):
        """
        in_xliff is  is the main method to de facto make the conversion.

        TODO: this is a work-in-progress at this moment, 2021-06-28
        """

        datum = []

        with open(hxlated_input, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file)

            # Convert each row into a dictionary
            # and add it to data
            for item in csvReader:

                datum.append(HXLTMUtil.xliff_item_relevant_options(item))

        resultatum = []
        resultatum.append('<?xml version="1.0"?>')
        resultatum.append(
            '<xliff xmlns="urn:oasis:names:tc:xliff:document:2.0" ' +
            'version="2.0" srcLang="en" trgLang="fr">')
        resultatum.append('  <file id="f1">')

        num = 0

        for rem in datum:
            num += 1
            if '#x_xliff+unit+id' in rem and rem['#x_xliff+unit+id']:
                unit_id = rem['#x_xliff+unit+id']
            else:
                unit_id = num
            # unit_id = rem['#x_xliff+unit+id'] if rem['#x_xliff+unit+id'] \
            #               else num
            resultatum.append('      <unit id="' + str(unit_id) + '">')

            resultatum.append('        <segment>')

            xsource = HXLTMUtil.xliff_item_xliff_source_key(rem)
            if xsource:
                if not rem[xsource]:
                    resultatum.append(
                        '          <!-- ERROR source ' + str(unit_id) +
                        ', ' + xsource + '-->')
                    if not args.silentium:
                        print('ERROR:', unit_id, xsource)
                        # TODO: make exit status code warn about this
                        #       so other scripts can deal with bad output
                        #       when --silentium is not used
                    # continue
                else:
                    resultatum.append('          <source>' +
                                      rem[xsource] + '</source>')

            xtarget = HXLTMUtil.xliff_item_xliff_target_key(rem)
            if xtarget and rem[xtarget]:
                resultatum.append('          <target>' +
                                  rem[xtarget] + '</target>')

            resultatum.append('        </segment>')

            resultatum.append('      </unit>')

        resultatum.append('  </file>')
        resultatum.append('</xliff>')

        if is_stdout:
            for ln in resultatum:
                print(ln)
        else:
            xliff_output_cleanup = open(xliff_output, 'w')
            xliff_output_cleanup.truncate()
            xliff_output_cleanup.close()

            with open(xliff_output, 'a') as new_txt:
                for ln in resultatum:
                    new_txt.write(ln + "\n")
                    # print (ln)

    def in_csv_header(
            self, hxlated_header, fontem_linguam, objectivum_linguam):
        """
        _[eng-Latn] Convert the Main HXL TM file to a single or source to
                    target XLIFF translation pair
        [eng-Latn]_

# item+id                         -> #x_xliff+unit+id
# meta+archivum                   -> #x_xliff+file
# item+wikidata+code              -> #x_xliff+unit+note+note_category__wikidata
# meta+wikidata+code              -> #x_xliff+unit+note+note_category__wikidata
# meta+item+url+list              -> #x_xliff+unit+notes+note_category__url
# item+type+lat_dominium+list     -> #x_xliff+group+group_0
#                             (We will not implement deeper levels  than 0 now)

    [contextum: XLIFF srcLang]
# item(*)+i_ZZZ+is_ZZZZ            -> #x_xliff+source+i_ZZZ+is_ZZZZ
# status(*)+i_ZZZ+is_ZZZZ+xliff
                            -> #meta+x_xliff+segment_source+state+i_ZZZ+is_ZZZZ
                                   (XLIFF don't support)
# meta(*)+i_ZZZ+is_ZZZZ            -> #x_xliff+unit+note+note_category__source
# meta(*)+i_ZZZ+is_ZZZZ+list       -> #x_xliff+unit+notes+note_category__source

    [contextum: XLIFF trgLang]
# item(*)+i_ZZZ+is_ZZZZ            -> #x_xliff+target+i_ZZZ+is_ZZZZ
# status(*)+i_ZZZ+is_ZZZZ+xliff    -> #x_xliff+segment+state+i_ZZZ+is_ZZZZ
# meta(*)+i_ZZZ+is_ZZZZ            -> #x_xliff+unit+note+note_category__target
# meta(*)+i_ZZZ+is_ZZZZ+list       -> #x_xliff+unit+notes+note_category__target

        _[eng-Latn] TODO:
- Map XLIFF revisions back MateCat back to HXL TM
  @see http://docs.oasis-open.org/xliff/xliff-core/v2.1/os
       /xliff-core-v2.1-os.html#revisions
        [eng-Latn]_
        """

        # TODO: improve this block. I'm very sure there is some cleaner way to
        #       do it in a more cleaner way (fititnt, 2021-01-28 08:56 UTC)

        fon_ling = HXLTMUtil.linguam_2_hxlattrs(fontem_linguam)
        fon_bcp47 = HXLTMUtil.bcp47_from_hxlattrs(fontem_linguam)
        obj_ling = HXLTMUtil.linguam_2_hxlattrs(objectivum_linguam)
        obj_bcp47 = HXLTMUtil.bcp47_from_hxlattrs(objectivum_linguam)

        for idx, _ in enumerate(hxlated_header):

            if hxlated_header[idx].startswith('#x_xliff'):
                # Something explicitly was previously defined with #x_xliff
                # So we will intentionally ignore on this step.
                # This could be useful if someone is trying to translate twice
                continue

            elif hxlated_header[idx] == '#item+id' or \
                    hxlated_header[idx] == '#item +conceptum +codicem':
                hxlated_header[idx] = '#x_xliff+unit+id'
                continue

            elif hxlated_header[idx] == '#meta+archivum':
                hxlated_header[idx] = '#x_xliff+file'
                continue

            elif hxlated_header[idx] == '#meta+item+url+list':
                hxlated_header[idx] = '#x_xliff+unit+notes+note_category__url'
                continue

            elif hxlated_header[idx] == '#item+wikidata+code' or \
                    hxlated_header[idx] == '#meta+wikidata+code' or \
                    hxlated_header[idx] == '#meta+conceptum+codicem+alternativum':  # noqa
                hxlated_header[idx] = \
                    '#x_xliff+unit+note+note_category__wikidata'
                continue

            elif hxlated_header[idx] == '#item+type+lat_dominium+list' or \
                    hxlated_header[idx] == '#item+conceptum+dominium':
                hxlated_header[idx] = '#x_xliff+group+group_0'
                continue

            elif hxlated_header[idx].startswith('#item'):

                if hxlated_header[idx].find(fon_ling) > -1 and \
                        not hxlated_header[idx].find('+list') > -1:
                    hxlated_header[idx] = '#x_xliff+source' + \
                        fon_bcp47 + fon_ling
                elif hxlated_header[idx].find(obj_ling) > -1 and \
                        not hxlated_header[idx].find('+list') > -1:
                    hxlated_header[idx] = '#x_xliff+target' + obj_ling

                continue

            elif hxlated_header[idx].startswith('#status'):
                if hxlated_header[idx].find(fon_ling) > -1 and \
                        not hxlated_header[idx].find('+list') > -1:
                    # TODO: maybe just ignore source state? XLIFF do not
                    #       support translations from source languages that
                    #       are not ideally ready yet
                    if hxlated_header[idx].find('+xliff') > -1:
                        hxlated_header[idx] = '#x_xliff+segment+state' + \
                            fon_bcp47 + fon_ling
                elif hxlated_header[idx].find(obj_ling) > -1 and \
                        not hxlated_header[idx].find('+list') > -1:
                    if hxlated_header[idx].find('+xliff') > -1:
                        hxlated_header[idx] = '#x_xliff+segment+state' + \
                            obj_bcp47 + obj_ling
                if hxlated_header[idx] != '#status':
                    print('#status ERROR?, FIX ME', hxlated_header[idx])
                continue

            elif hxlated_header[idx].startswith('#meta'):
                # @see http://docs.oasis-open.org/xliff/xliff-core/v2.1/os
                #      /xliff-core-v2.1-os.html#category

                if hxlated_header[idx].find(fon_ling) > -1:
                    if hxlated_header[idx].find('+list') > -1:
                        hxlated_header[idx] = \
                            '#x_xliff+unit+notes+note_category__source'
                    else:
                        hxlated_header[idx] = \
                            '#x_xliff+unit+note+note_category__source'
                    continue

                if hxlated_header[idx].find(obj_ling) > -1:
                    if hxlated_header[idx].find('+list') > -1:
                        hxlated_header[idx] = \
                            '#x_xliff+unit+notes+note_category__target'
                    else:
                        hxlated_header[idx] = \
                            '#x_xliff+unit+note+note_category__target'
                    continue

                # We will ignore other #metas
                continue

        return hxlated_header


@dataclass
class HXLTMDatum:
    """
    _[eng-Latn]
    HXLTMDatum is a python wrapper for the an HXLated HXLTM dataset.

    While this class does not use libhxl directly, it assumes that the dataset
    already was saved on local disk and is CSV valid with hashtags. (We will
    not reimplement too much low level logic here).

    One limitation (that is unlikely to be a problem) is, similar to
    softwares like Pandas (and unlikely libhxl, that play nice with streams)
    this class requires load all the data on the memory instead of process
    row by row.
    [eng-Latn]_
    """

    # crudum: InitVar[List] = []
    crudum_caput: InitVar[List] = []
    crudum_hashtag: InitVar[List] = []
    meta: InitVar[Type['HXLTMDatumMetaCaput']] = None
    # datum_rem: InitVar[List] = []
    columnam: InitVar[List] = []
    ontologia: InitVar[Type['HXLTMOntologia']] = None
    venandum_insectum_est: InitVar[bool] = False

    def __init__(self,
                 archivum: str,
                 ontologia: Type['HXLTMOntologia'],
                 venandum_insectum_est: bool = False):
        """
        _[eng-Latn] Constructs all the necessary attributes for the
                    HXLTMDatum object.
        [eng-Latn]_
        """

        self.ontologia = ontologia
        self.venandum_insectum_est = venandum_insectum_est

        # print('oi')

        self._initialle(archivum)

    def _initialle(self, archivum: str):
        """
        Trivia: initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        """
        crudum_titulum = []
        crudum_hashtag = []
        datum_rem = []
        datum_rem_brevis = []

        with open(archivum, 'r') as hxl_archivum:
            csv_lectorem = csv.reader(hxl_archivum)
            rem_prius = None
            for _ in range(25):
                rem_nunc = next(csv_lectorem)
                if HXLTMDatumMetaCaput.quod_est_hashtag_caput(rem_nunc):
                    if rem_prius is not None:
                        crudum_titulum = rem_prius
                    crudum_hashtag = rem_nunc
                    break
                rem_prius = rem_nunc
            if len(crudum_hashtag) == 0:
                # This is not supposed to happen, since the file should
                # already be parsed previously by libhxl
                raise SyntaxError('HXLTMDatum quod archīvum HXL hashtags?')

            for rem in csv_lectorem:
                datum_rem.append(rem)
        # print(datum_rem)
        # print('oooi')
        # print(len(datum_rem[0]))

        if len(datum_rem) > 0:
            # self.datum_rem = datum_rem
            datum_rem_brevis = datum_rem[:5]
            for item_num in range(len(datum_rem[0])):
                # print('oi2', item_num)
                col_rem_val = HXLTMDatumColumnam.reducendum_de_datum(
                    datum_rem, item_num)
                self.columnam.append(HXLTMDatumColumnam(
                    col_rem_val
                ))
                # print(type(self.columnam[0]))

        self.meta = HXLTMDatumMetaCaput(
            crudum_titulum=crudum_titulum,
            crudum_hashtag=crudum_hashtag,
            datum_rem_brevis=datum_rem_brevis,
            columnam_collectionem=self.columnam,
            venandum_insectum_est=self.venandum_insectum_est
        )

        # self._initialle_meta_caput(crudum_hashtag, crudum_caput)

    # def _initialle_meta_caput(self,
    #                           crudum_hashtag: List,
    #                           crudum_caput: List):
    #     """
    #     Trivia:
    #      - initiāle, https://en.wiktionary.org/wiki/initialis#Latin
    #     - meta
    #       - https://en.wiktionary.org/wiki/meta#English
    #         - https://en.wiktionary.org/wiki/metaphysica#Latin
    #     - caput, https://en.wiktionary.org/wiki/caput#Latin
    #     """
    #     print('TODO _initialle_meta_caput')

    def v(self, verbosum: bool = None):  # pylint: disable=invalid-name
        """Ego python Dict

        Trivia:
         - valendum, https://en.wiktionary.org/wiki/valeo#Latin
           - Anglicum (English): value (?)
         - verbosum, https://en.wiktionary.org/wiki/verbosus#Latin

        Args:
            verbosum (bool): Verbosum est? Defallo falsum.

        Returns:
            [Dict]: Python objectīvum
        """
        if verbosum is not False:
            verbosum = verbosum or self.venandum_insectum_est

        resultatum = {
            '_typum': 'HXLTMDatum',
            # 'crudum_caput': self.crudum_caput,
            # 'crudum_hashtag': self.crudum_hashtag,
            'meta': self.meta.v(verbosum),
            # optio --venandum-insectum-est requirere
            # 'columnam': []
        }

        if verbosum:
            resultatum['crudum_caput'] = self.crudum_caput
            resultatum['crudum_hashtag'] = self.crudum_hashtag
            resultatum['columnam'] = \
                [item.v(verbosum) if item else None for item in self.columnam]

        # return self.__dict__
        return resultatum


@dataclass
class HXLTMDatumColumnam:
    """HXLTM Datum columnam summārius

    Trivia:
    - HXLTM, https://hdp.etica.ai/hxltm
    - Datum, https://en.wiktionary.org/wiki/datum#Latin
    - Columnam, https://en.wiktionary.org/wiki/columna#Latin
    - summārius, https://en.wiktionary.org/wiki/summary#English
    - valendum, https://en.wiktionary.org/wiki/valeo#Latin
      - 'value' , https://en.wiktionary.org/wiki/value#English
    - quantitātem , https://en.wiktionary.org/wiki/quantitas
    """
    # pylint: disable=too-many-instance-attributes

    _typum: InitVar[str] = None   # Used only when output JSON
    datum_typum: InitVar['str'] = None
    quantitatem: InitVar[int] = None
    _valendum: InitVar[List] = None

    # self._typum = 'HXLTMRemCaput'  # Used only when output JSON

    def __init__(self, valendum: List):

        self._typum = 'HXLTMDatumColumnam'
        # self._valendum = valendum
        self.quantitatem = len(valendum) if valendum is not None else 0
        self.datum_typum = HXLTMTypum.collectionem_datum_typum(valendum)

    @staticmethod
    def reducendum_de_datum(datum: List, columnam: int) -> List:
        """Redūcendum Columnam de datum

        Args:
            datum (List): Datum [rem x col]
            columnam (int): Numerum columnam in datum

        Returns:
            List: Unum columnam
        """
        resultatum = []
        if datum is not None and len(datum) > 0:
            for rem_num, _ in enumerate(datum):  # numero de linhas
                # for col_num in enumerate(datum[0]): # Número de colunas
                resultatum.append(datum[rem_num][columnam])
                # resultatum.append(datum[rem_num])
        # pass # redūcendum_Columnam_de_datum
        return resultatum

    def v(self, verbosum: bool = False):  # pylint: disable=invalid-name
        """Ego python Dict

        Trivia:
         - valendum, https://en.wiktionary.org/wiki/valeo#Latin
           - Anglicum (English): value (?)
         - verbosum, https://en.wiktionary.org/wiki/verbosus#Latin

        Args:
            verbosum (bool): Verbosum est? Defallo falsum.

        Returns:
            [Dict]: Python objectīvum
        """
        resultatum = {
            '_typum': self._typum,
            'quantitatem': self.quantitatem,
            'datum_typum': self.datum_typum,
        }

        # return self.__dict__
        return resultatum


@dataclass
class HXLTMDatumMetaCaput:  # pylint: disable=too-many-instance-attributes
    """
    _[eng-Latn]
    HXLTMDatumMetaCaput contains data about hashtags, raw headings (if they
    exist on original dataset) of a dataset
    [eng-Latn]_

        Testum:

>>> rem = HXLTMDatumMetaCaput(
...   ['id', 'Nōmen', 'Annotātiōnem'],
...   ['#item+id', '#item+lat_nomen', ''],
...   [
...      [1, 'Marcus canem amat.', 'Vērum!'],
...      [2, 'Canem Marcus amat.', ''],
...      [3, 'Amat canem Marcus.', 'vērum? vērum!']
...   ])
>>> rem.quod_datum_rem_correctum_est()
True
>>> rem.quod_datum_rem_correctum_est([[4, 'Marcus amat canem.', '']])
True
>>> rem.quod_datum_rem_correctum_est([['Canem amat Marcus.', '']])
False
>>> rem.titulum_de_columnam(0)
'id'
>>> rem.titulum_de_columnam(1)
'Nōmen'
>>> rem.titulum_de_columnam(2)
'Annotātiōnem'
>>> rem.titulum_de_columnam(9999)
False
>>> rem.hxl_hashtag_de_columnam(0)
'#item+id'
>>> rem.hxl_hashtag_de_columnam(1)
'#item+lat_nomen'
>>> rem.hxl_hashtag_de_columnam(2) is None
True
    """

    # crudum: InitVar[List] = []
    rem: InitVar[List] = []
    crudum_hashtag: InitVar[List] = []
    datum_rem_brevis: InitVar[List] = []
    numerum_optionem: InitVar[int] = 0
    numerum_optionem_hxl: InitVar[int] = 0
    numerum_optionem_hxl_unicum: InitVar[int] = 0
    numerum_optionem_nomen: InitVar[int] = 0
    numerum_optionem_nomen_unicum: InitVar[int] = 0
    venandum_insectum_est: InitVar[bool] = False

    def __init__(
            self,
            crudum_titulum: List,
            crudum_hashtag: List,
            datum_rem_brevis: List,
            columnam_collectionem: List[Type['HXLTMDatumColumnam']] = None,
            venandum_insectum_est: bool = False
    ):

        self.crudum_titulum = crudum_titulum
        self.crudum_hashtag = crudum_hashtag
        self.datum_rem_brevis = datum_rem_brevis
        self.venandum_insectum_est = venandum_insectum_est

        # self.rem = [123]

        self._initialle(
            crudum_titulum, crudum_hashtag,
            datum_rem_brevis, columnam_collectionem)

    def _initialle(
        self,
        crudum_titulum: List,
        crudum_hashtag: List,
        datum_rem_brevis: List,
        columnam_collectionem: List[Type['HXLTMDatumColumnam']] = None
    ):
        """
        Trivia: initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        """
        # self.quod_est_hashtag_caput

        non_vacuum_nomen = list(filter(len, crudum_titulum))
        # print(crudum_titulum)
        # print(crudum_hashtag)

        self.datum_rem_brevis = datum_rem_brevis
        # _[eng-Latn]
        # crudum_hashtag also have empty spaces, so it still can be used to
        # know how many columns do exist
        # [eng-Latn]_
        self.numerum_optionem = len(crudum_hashtag)
        self.numerum_optionem_hxl = \
            self.quod_est_hashtag_caput(crudum_hashtag)
        self.numerum_optionem_hxl_unicum = \
            self.quod_est_hashtag_caput(set(crudum_hashtag))
        self.numerum_optionem_nomen = len(non_vacuum_nomen)
        self.numerum_optionem_nomen_unicum = \
            len(set(non_vacuum_nomen))

        # self.rem = [123]

        # Note:
        # print('columnam_collectionem', columnam_collectionem)
        # print('columnam_collectionem', len(columnam_collectionem))
        for item_num in range(self.numerum_optionem):
            # if columnam_collectionem is not None and item_num in
            if columnam_collectionem is not None:
                col_meta = columnam_collectionem[item_num]
                # print('acerto')
            else:
                # print('erro')
                col_meta = None
            self.rem.append(HXLTMRemCaput(
                columnam=item_num,
                columnam_meta=col_meta,
                hashtag=self.hxl_hashtag_de_columnam(item_num),
                titulum=self.titulum_de_columnam(item_num),
            ))
            # print(col)

    def hxl_hashtag_de_columnam(self, numerum: int) -> Union[str, None]:
        """HXL hashtag dē columnam numerum

        Trivia:
          - HXL, https://hxlstandard.org/
          - hashtag, https://en.wiktionary.org/wiki/hashtag
          - dē, https://en.wiktionary.org/wiki/de#Latin
          - columnam, https://en.wiktionary.org/wiki/columna#Latin
          - numerum, https://en.wiktionary.org/wiki/numerus#Latin

        Args:
            numerum (int): Numerum de columnam. Initiāle 0.

        Returns:
            Union[str, None, False]:
                HXL Hashtag aut python None aut python False
        """

        if numerum < 0 or numerum >= len(self.crudum_hashtag):
            # _[eng-Latn]Called on a wrong, invalid, index[eng-Latn]_
            return False
        if len(self.crudum_hashtag[numerum]) == 0:
            return None
        # print('oi1', self.crudum_hashtag)
        # print('oi2', self.crudum_hashtag[numerum])
        return self.crudum_hashtag[numerum]

    def quod_datum_rem_correctum_est(
            self, datum_rem_brevis: List = None) -> bool:
        """Quod datum rem corrēctum est?

        _[eng-Latn]
        Very basic check to test if the number of numerum_optionem is exact
        the number of data rows. While we do tolerate rows without
        any text heading name or HXL hashtag, the number of rows (tagged or
        not) must match. Without this is very likely we will put data on
        wrong place when trying to relate they by index number (order they
        appear on the dataset)
        [eng-Latn]_

        Args:
            datum_rem_brevis (List):
                _[eng-Latn]
                List of list of custom data to test. Can be used to test
                new data from a previous created item.
                The default is use the initial data provide when
                constructing the data object.
                [eng-Latn]_

        Returns:
            bool: Verum: rem corrēctum est.
        """
        if datum_rem_brevis is None:
            datum_rem_brevis = self.datum_rem_brevis

        if len(datum_rem_brevis) == 0:
            # _[eng-Latn] Empty data is acceptable [eng-Latn]_
            return True

        return self.numerum_optionem == len(datum_rem_brevis[0])

    @staticmethod
    def quod_est_hashtag_caput(rem: List) -> Union[bool, int]:
        """HXL hashtag caput est?

        @see hxl.HXLReader.parse_tags()
              https://github.com/HXLStandard/libhxl-python/blob/main/hxl/io.py

        Args:
            rem (List):
                _[eng-Latn] List to test [eng-Latn]_

        Returns:
            Union[bool, int]:
                _[eng-Latn]
                False if not seems to be a HXLated; int with total
                number of columns started with #
                [eng-Latn]_
        """
        # Same as FUZZY_HASHTAG_PERCENTAGE = 0.5 from libhxl
        min_limit = 50
        total = 0
        hashtag_like = 0
        for item in rem:
            total += 1
            if item.startswith('#'):
                hashtag_like += 1

        est_hashtag = (hashtag_like > 0) and \
            ((total / hashtag_like * 100) > min_limit)

        return hashtag_like if est_hashtag else False

    def linguam_de_columnam(self, numerum: int) -> Type['HXLTMLinguam']:
        """Nōmen dē columnam numerum

        Trivia:
          - linguam, https://en.wiktionary.org/wiki/lingua#Latin
          - dē, https://en.wiktionary.org/wiki/de#Latin
          - columnam, https://en.wiktionary.org/wiki/columna#Latin
          - numerum, https://en.wiktionary.org/wiki/numerus#Latin

        Args:
            numerum (int): Numerum de columnam. Initiāle 0.

        Returns:
            Union[str, None]: linguam aut python None
        """
        # https://en.wiktionary.org/wiki/columna#Latin
        print('TODO')

    def titulum_de_columnam(self, numerum: int) -> Union[str, None]:
        """Nomen dē columnam numerum

        Trivia:
          - nōmen, https://en.wiktionary.org/wiki/nomen#Latin
          - dē, https://en.wiktionary.org/wiki/de#Latin
          - columnam, https://en.wiktionary.org/wiki/columna#Latin
          - numerum, https://en.wiktionary.org/wiki/numerus#Latin

        Args:
            numerum (int): Numerum de columnam. Initiāle 0.

        Returns:
            Union[str, None, False]: nōmen aut python None aut python False
        """
        # https://en.wiktionary.org/wiki/columna#Latin
        if numerum < 0 or numerum >= len(self.crudum_titulum):
            # _[eng-Latn]Called on a wrong, invalid, index[eng-Latn]_
            return False
        if len(self.crudum_titulum[numerum]) == 0:
            return None

        return self.crudum_titulum[numerum]

    def v(self, verbosum: bool = None):  # pylint: disable=invalid-name
        """Ego python Dict

        Trivia:
         - valendum, https://en.wiktionary.org/wiki/valeo#Latin
           - Anglicum (English): value (?)
         - verbosum, https://en.wiktionary.org/wiki/verbosus#Latin

        Args:
            verbosum (bool): Verbosum est? Defallo falsum.

        Returns:
            [Dict]: Python objectīvum
        """
        if verbosum is not False:
            verbosum = verbosum or self.venandum_insectum_est

        resultatum = {
            'caput': [item.v(verbosum) if item else None for item in self.rem],
            # 'crudum_titulum': self.crudum_titulum,
            # 'crudum_hashtag': self.crudum_hashtag,
            'numerum_optionem': self.numerum_optionem,
            'numerum_optionem_hxl': self.numerum_optionem_hxl,
            'numerum_optionem_hxl_unicum': self.numerum_optionem_hxl_unicum,
            'numerum_optionem_nomen': self.numerum_optionem_nomen,
            'numerum_optionem_nomen_unicum':
            self.numerum_optionem_nomen_unicum,
            # 'venandum_insectum_est': self.venandum_insectum_est,
        }

        if verbosum:
            resultatum['crudum_titulum'] = self.crudum_titulum
            resultatum['crudum_hashtag'] = self.crudum_hashtag

        # return self.__dict__
        return resultatum


class HXLTMOntologia:
    """
    _[eng-Latn] HXLTMOntologia is a python wrapper for the cor.hxltm.yml.
    [eng-Latn]_

    """

    def __init__(self, ontologia):
        """
        _[eng-Latn] Constructs all the necessary attributes for the
                    HXLTMOntologia object.
        [eng-Latn]_
        """
        self.crudum = ontologia
        self.initialle()

    def initialle(self):
        """
        Trivia: initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        """
        # print('TODO')

    def hxl_de_aliud_nomen_breve(self, structum=False):
        """HXL attribūtum de aliud nōmen breve (cor.hxltm.yml)

        Trivia:
        - aliud, https://en.wiktionary.org/wiki/alius#Latin
        - nōmen, https://en.wiktionary.org/wiki/nomen#Latin
        - breve, https://en.wiktionary.org/wiki/brevis

        _[eng-Latn] For each item that have both __nomen_breve and __HXL,
                    create a flatten dictionary (only a key and value)
                    with the equivalent HXL hashtags.

                    This approach allows pass much more control logic to the
                    YAML file.
        [eng-Latn]_

        Returns:
            [Dict]: Dictionary
        """
        resultatum = {}
        # pylint: disable=invalid-name

        def recursionem(rem):
            # Trivia:
            # - recursiōnem, https://en.wiktionary.org/wiki/recursio#Latin
            for _k, v in rem.items():
                if isinstance(v, dict):
                    recursionem(v)
                else:
                    if '__HXL' in rem and '__nomen_breve' in rem:

                        if structum and rem['__nomen_breve'] in resultatum:
                            # TODO: improve this message
                            print('K [' + rem['__nomen_breve'] + ']')

                        resultatum[rem['__nomen_breve']] = \
                            ''.join(rem['__HXL'].split())

        recursionem(self.crudum['ontologia'])
        # print(resultatum)
        return resultatum

    def hxlhashtag(self, objectivum: Union[Dict, None], strictum=False):
        """Get __HXL non-whitespace value from an Dict

        Args:
            objectivum ([Dict]): an object with __HXL
            strictum (bool, optional): Raise error?. Defaults to False.

        Raises:
            RuntimeError: [description]

        Returns:
            [str]: an HXL hashtag without spaces
        """
        if objectivum is not None:
            if '__HXL' in objectivum:
                return ''.join(objectivum['__HXL'].split())

        if strictum:
            raise RuntimeError('HXLTMOntologia.hxlhashtag error')
        return None

    def de(self, dotted_key: str,  # pylint: disable=invalid-name
           default: Any = None, fontem: dict = None) -> Any:
        """
        Trivia: dē, https://en.wiktionary.org/wiki/de#Latin

        Examples:
            >>> exemplum = {'a': {'a2': 123}, 'b': 456}
            >>> otlg = HXLTMOntologia(exemplum)
            >>> otlg.de('a.a2', fontem=exemplum)
            123

        Args:
            dotted_key (str): Dotted key notation
            default ([Any], optional): Value if not found. Defaults to None.
            fontem (dict): An nested object to search

        Returns:
            [Any]: Return the result. Defaults to default
        """
        if fontem is None:
            fontem = self.crudum

        keys = dotted_key.split('.')
        return reduce(
            lambda d, key: d.get(
                key) if d else default, keys, fontem
        )


class HXLTMBCP47:
    """HXLTM BCP47 auxilium programmi

    _[eng-Latn] A non-dictionary aware BCP47 converter
                Note: this on this version depends on langcodes,
                <https://github.com/rspeer/langcodes>,
                So you need
                    pip3 install langcodes
    [eng-Latn]_


    Author:
            Emerson Rocha <rocha[at]ieee.org>
    Creation date:
            2021-06-09
    """

    def __init__(self, textum_bcp47: str):
        """

        """
        self.crudum = textum_bcp47

    @staticmethod
    def testum(textum: str) -> str:
        """testum est (...)

        Example:
            >>> HXLTMBCP47.testum('eng_US')
            'en-US'
            >>> HXLTMBCP47.testum('en-UK')
            'en-GB'

        Args:
            textum (str): [description]

        Returns:
            str: [description]
        """
        resultatum = langcodes.standardize_tag(textum)
        return resultatum

    @staticmethod
    def iso6392a3(textum: str) -> str:
        """iso6392a3, ISO 639-2 alphabētum 3 de BCP47 textum

        Example:
            >>> HXLTMBCP47.iso6392a3('eng_US')
            'eng'
            >>> HXLTMBCP47.iso6392a3('en-UK')
            'eng'
            >>> HXLTMBCP47.iso6392a3('en-UK')
            'eng'
            >>> HXLTMBCP47.iso6392a3('yue')
            'yue'

            # Romany [rom], https://iso639-3.sil.org/code/rom
            >>> HXLTMBCP47.iso6392a3('rom')
            'rom'

            # >>> HXLTMBCP47.iso6392a3('zh-TW')
            # '...'

        Args:
            textum (str): BCP47 language code string

        Returns:
            str: ISO 639-3 language code
        """
        L = langcodes.Language.get(textum)
        if L.is_valid():
            return L.to_alpha3()
            # resultatum = L.to_alpha3()
        return None


@dataclass
class HXLTMLinguam:  # pylint: disable=too-many-instance-attributes
    """HXLTM linguam auxilium programmi

    Testum:
        >>> HXLTMLinguam('lat-Latn@la-IT@IT')
        HXLTMLinguam()

        >>> HXLTMLinguam('lat-Latn@la-IT@IT').v()
        {'_typum': 'HXLTMLinguam', \
'crudum': 'lat-Latn@la-IT@IT', 'linguam': 'lat-Latn', \
'bcp47': 'la-IT', 'imperium': 'IT', 'iso6391a2': 'la', 'iso6393': 'lat', \
'iso115924': 'Latn'}

        >>> HXLTMLinguam('lat-Latn@la-IT@IT').a()
        '+i_la+i_lat+is_latn+ii_it'

        # Kalo Finnish Romani, Latin script (no ISO 2 language)
        >>> HXLTMLinguam('rmf-Latn').v()
        {'_typum': 'HXLTMLinguam', 'crudum': 'rmf-Latn', \
'linguam': 'rmf-Latn', 'iso6393': 'rmf', 'iso115924': 'Latn'}

        # Kalo Finnish Romani, Latin script (no ISO 2 language, so no attr)
        >>> HXLTMLinguam('rmf-Latn').a()
        '+i_rmf+is_latn'

# Private use language tags: se use similar pattern of BCP 47.
# (https://tools.ietf.org/search/bcp47)
>>> HXLTMLinguam('lat-Latn-x-privatum').a()
'+i_lat+is_latn+ix_privatum'

>>> HXLTMLinguam('lat-Latn-x-privatum-tag8digt').a()
'+i_lat+is_latn+ix_privatum+ix_tag8digt'

# If x-private is only on BCP, we ignore it on HXL attrs. Tools may still
# use this for other processing (like for XLIFF), but not for generated
# Datasets.
>>> HXLTMLinguam(
... 'cmn-Latn@zh-Latn-CN-variant1-a-extend1-x-wadegile-private1').a()
'+i_zh+i_cmn+is_latn'

# To force a x-private language tag, it must be on linguam (first part)
# even if it means repeat.
# Also, we create attributes shorted by ASCII alphabet, as BCP47 would do
>>> HXLTMLinguam(
... 'cmn-Latn-x-wadegile-private1@zh-CN-x-wadegile-private1').a()
'+i_zh+i_cmn+is_latn+ix_private1+ix_wadegile'

>>> HXLTMLinguam(
... 'lat-Latn-x-caesar12-romanum1@la-IT-x-caesar12-romanum1@IT').a()
'+i_la+i_lat+is_latn+ii_it+ix_caesar12+ix_romanum1'

    """

    # Exemplum: lat-Latn@la-IT@IT, arb-Arab@ar-EG@EG
    _typum: InitVar[str] = None  # 'HXLTMLinguam'
    crudum: InitVar[str] = None
    linguam: InitVar[str] = None     # Exemplum: lat-Latn, arb-Arab
    bcp47: InitVar[str] = None       # Exemplum: la-IT, ar-EG
    imperium: InitVar[str] = None    # Exemplum: IT, EG
    iso6391a2: InitVar[str] = None     # Exemlum: la, ar
    iso6393: InitVar[str] = None     # Exemlum: lat, arb
    iso115924: InitVar[str] = None   # Exemplum: Latn, Arab
    privatum: InitVar[List[str]] = None  # Exemplum: [privatum]
    vacuum: InitVar[str] = False

    # https://tools.ietf.org/search/bcp47#page-2-12

    def __init__(self, linguam: str, strictum=False, vacuum=False):
        """HXLTMLinguam initiāle

        Args:
            linguam (str): Textum linguam
            strictum (bool, optional): Strictum est?.
                       Trivia: https://en.wiktionary.org/wiki/strictus#Latin
                       Defallo falsum.
            vacuum (bool, optional): vacuum	est?
                       Trivia: https://en.wiktionary.org/wiki/vacuus#Latin.
                       Defallo falsum.
        """
        # super().__init__()
        self._typum = 'HXLTMLinguam'  # Used only when output JSON
        self.crudum = linguam
        if not vacuum:
            self.initialle(strictum)
        else:
            self.vacuum = vacuum

    def initialle(self, strictum: bool):
        """
        Trivia: initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        """

        term = self.crudum
        # Hackysh way to discover if private use is the linguam
        # tag or if is the BCP47 x-private use tag
        # Good example '4.4.2.  Truncation of Language Tags'
        # at https://tools.ietf.org/search/bcp47
        if self.crudum.find('x-') > -1:
            # print('Do exist a private-use tag')
            if self.crudum.find('@') > -1:
                parts = self.crudum.split('@')
                # print('parte1', parts)
                if parts[0].find('x-') > -1:
                    # _, privatumtext = parts[0].split('-x-')
                    part0, privatumtext = parts[0].split('-x-')
                    self.privatum = privatumtext.split('-')
                    parts.pop(0)
                    term = part0 + "@" + '@'.join(parts)
                    # print('term2', term)
                    # TODO: handle private use on linguan tag when
                    #       also BCP47 is used
            else:
                part0, privatumtext = self.crudum.split('-x-')
                self.privatum = privatumtext.split('-')
                term = part0

        if term.find('@') == -1:
            # Non @? Est linguam.
            self.linguam = term

            # self.iso6393, self.iso115924 = \
            #     list(self.linguam.split('-'))
        elif term.find('@@') > -1:
            # @@? Est linguam et imperium
            self.linguam, self.imperium = list(term.split('@@'))

            # self.iso6393, self.iso115924 = \
            #     list(self.linguam.split('-'))
        elif term.count('@') == 1:
            # Unum @? Est linguam et bcp47
            self.linguam, self.bcp47 = list(term.split('@'))

        elif term.count('@') == 2:
            # rem@rem@rem ? Est linguam, bcp47, imperium
            self.linguam, self.bcp47, self.imperium = \
                list(term.split('@'))
            # self.iso6393, self.iso115924 = \
            #     list(self.linguam.split('-'))
        elif strictum:
            raise ValueError('HXLTMLinguam [' + term + ']')
        else:
            return False

        if self.bcp47:
            parts = self.bcp47.split('-')
            if len(parts[0]) == 2:
                self.iso6391a2 = parts[0].lower()

        self.iso6393, self.iso115924 = \
            list(self.linguam.split('-'))

        self.iso6393 = self.iso6393.lower()
        self.iso115924 = self.iso115924.capitalize()
        self.linguam = self.iso6393 + '-' + self.iso115924
        if self.imperium:
            self.imperium = self.imperium.upper()

        if self.privatum is not None and len(self.privatum) > 0:
            # https://tools.ietf.org/search/bcp47#page-2-12
            # '4.5.  Canonicalization of Language Tags'
            # We short the keys
            # privatum_est = sorted(self.imperium, key=str.upper)

            # print('antes', self.imperium)
            privatum_est = sorted(self.privatum)

            # print('depois', self.privatum)
            self.privatum = privatum_est

        return True

    def a(self):  # pylint: disable=invalid-name
        """HXL attribūtum

        Exemplum:
            >>> HXLTMLinguam('lat-Latn@la-IT@IT').a()
            '+i_la+i_lat+is_latn+ii_it'

        Returns:
            [str]: textum HXL attribūtum
        """
        resultatum = []

        if self.iso6391a2:
            resultatum.append('+i_' + self.iso6391a2)
        if self.iso6393:
            resultatum.append('+i_' + self.iso6393)
        if self.iso115924:
            resultatum.append('+is_' + self.iso115924)
        if self.imperium:
            resultatum.append('+ii_' + self.imperium)
        if self.privatum and len(self.privatum) > 0:
            for item in self.privatum:
                resultatum.append('+ix_' + item)

        return ''.join(resultatum).lower()

    def designo(self, clavem: str, rem: Any) -> Type['HXLTMLinguam']:
        """Designo clavem rem

        _[eng-Latn] The HXLTMLinguam.designo() can be useful for create empty
                    languages with HXLTMLinguam('', vacuum=True) and then
                    manually defining what attributes would like when search
                    by hashtags
        [eng-Latn]_

       Args:
            clavem (str): clāvem, https://en.wiktionary.org/wiki/clavis#Latin
            rem (Any): rem, https://en.wiktionary.org/wiki/res#Latin

        Returns:
            [HXLTMLinguam]: HXLTMLinguam to allow method chaining

        Exemplum:
>>> rem_vacuum = HXLTMLinguam('', vacuum=True)
>>> rem = rem_vacuum.designo('iso115924', 'Latn')
>>> collectionem = [
...    '#item+conceptum+codicem',
...    '#item+rem+i_la+i_lat+is_latn',
...    '#item+definitionem+i_la+i_lat+is_latn',
...    '#item+rem+i_ar+i_arb+is_arab',
...    '#item+definitionem+i_ar+i_arb+is_arab'
... ]
>>> rem.intra_collectionem_est(collectionem)
['#item+rem+i_la+i_lat+is_latn', '#item+definitionem+i_la+i_lat+is_latn']


        """
        setattr(self, clavem, rem)
        return self

    def h(self, formatum: str):  # pylint: disable=invalid-name
        """HXL hashtag de fōrmātum

        Exemplum:
>>> HXLTMLinguam('lat-Latn@la-IT@IT').h('#item+rem__linguam__')
'#item+rem+i_la+i_lat+is_latn+ii_it'

>>> HXLTMLinguam('lat-Latn-x-privatum').h('#item+rem__linguam__')
'#item+rem+i_lat+is_latn+ix_privatum'

        Returns:
            [str]: textum HXL hashtag
        """
        linguam_attrs = self.a()

        if formatum.find('__linguam__') > -1:
            return formatum.replace('__linguam__', linguam_attrs)

        if formatum.find('__linguam_de_imperium__') > -1:
            return formatum.replace('__linguam_de_imperium__', linguam_attrs)

        raise ValueError('HXLTMLinguam fōrmātum errōrem [' + formatum + ']')

    def intra_collectionem_est(
            self, collectionem: List, formatum: str = None) -> List:
        """Intrā collēctiōnem est?

        Trivia:
        - intrā, https://en.wiktionary.org/wiki/intra#Latin
        - collēctiōnem, https://en.wiktionary.org/wiki/collectio#Latin
        - est, https://en.wiktionary.org/wiki/est#Latin


        Args:
            collectionem (List): List of HXL hashtags
            formatum (str): An formatted template.

        Returns:
            [List]: List of HXL hashtags that match the search

        Tests:

>>> rem = HXLTMLinguam('lat-Latn@la')
>>> collectionem = [
...    '#item+conceptum+codicem',
...    '#item+rem+i_la+i_lat+is_latn',
...    '#item+definitionem+i_la+i_lat+is_latn',
...    '#item+rem+i_ar+i_arb+is_arab',
...    '#item+definitionem+i_ar+i_arb+is_arab'
... ]

>>> rem.intra_collectionem_est(collectionem)
['#item+rem+i_la+i_lat+is_latn', '#item+definitionem+i_la+i_lat+is_latn']

>>> rem.intra_collectionem_est(collectionem, '#item+rem__linguam__')
['#item+rem+i_la+i_lat+is_latn']
>>> rem.intra_collectionem_est(collectionem,'#status+rem+accuratum__linguam__')
[]

>>> rem_vacuum = HXLTMLinguam('', vacuum=True)
>>> rem_vacuum.intra_collectionem_est(collectionem)
['#item+conceptum+codicem', \
'#item+rem+i_la+i_lat+is_latn', \
'#item+definitionem+i_la+i_lat+is_latn', \
'#item+rem+i_ar+i_arb+is_arab', \
'#item+definitionem+i_ar+i_arb+is_arab']

>>> rem_vacuum.intra_collectionem_est(collectionem, '#item+rem__linguam__')
['#item+rem+i_la+i_lat+is_latn', '#item+rem+i_ar+i_arb+is_arab']

        """
        resultatum = []
        if formatum:
            indaginem = self.h(formatum)
        else:
            indaginem = self.a()

        for rem in collectionem:
            if rem.find(indaginem) > -1:
                resultatum.append(rem)

        return resultatum

    def v(self, _verbosum: bool = None):  # pylint: disable=invalid-name
        """Ego python Dict

        Trivia:
         - valendum, https://en.wiktionary.org/wiki/valeo#Latin
           - Anglicum (English): value (?)
         - verbosum, https://en.wiktionary.org/wiki/verbosus#Latin

        Args:
            _verbosum (bool): Verbosum est? Defallo falsum.

        Returns:
            [Dict]: Python objectīvum
        """
        return self.__dict__


class HXLTMRemCaput(HXLTMLinguam):
    """HXLTMRemCaput HXLTMLinguam et HXLTMDatumMetaCaput metadatum

    Args:
        HXLTMLinguam ([HXLTMLinguam]): HXLTMLinguam
    """

    columnam: InitVar[int] = -1
    valendum_meta: InitVar[Dict] = None
    datum_typum: InitVar['str'] = None
    hashtag: InitVar[str] = None
    titulum: InitVar[str] = None

    # @see https://github.com/PyCQA/pylint/issues/3505
    # pylint: disable=super-init-not-called
    # pylint: disable=non-parent-init-called
    # pylint: disable=too-many-arguments
    def __init__(
            self,
            columnam: int = -1,
            columnam_meta: Dict = None,  # HXLTMDatumColumnam.v()
            hashtag: str = '',
            titulum: str = '',
            strictum=False):
        """HXLTMRemCaput initiāle

        Args:
            columnam (int): Numerum columnam
            columnam_meta (HXLTMDatumColumnam): HXLTMDatumColumnam
            hashtag (str): Textum hashtag. Defallo: ''
            titulum (str): Textum titulum. Defallo: ''
            strictum (bool, optional): Strictum est?.
                       Trivia: https://en.wiktionary.org/wiki/strictus#Latin
                       Defallo falsum.
        """

        linguam = HXLTMUtil.linguam_de_hxlhashtag(hashtag) if hashtag else ''
        # _[eng-Latn]
        # While on HXLTMLinguam the user must explicitly force vacuum=False
        # to not tolerate malformated requests, the HXLTMRemCaput
        # have to deal with pretty much anything as header. So we assume
        # empty HXL hashtag means HXLTMLinguam vacuum=True
        # [eng-Latn]_
        vacuum = bool(linguam is None or len(linguam) == 0)

        HXLTMLinguam.__init__(self, linguam, strictum, vacuum)

        self._typum = 'HXLTMRemCaput'  # Used only when output JSON

        self.columnam = columnam
        self.hashtag = hashtag
        self.titulum = titulum
        if columnam_meta is not None:
            self.valendum_meta = columnam_meta.v(False)


class HXLTMTypum:
    """HXLTM Data typum

    _[eng-Latn]
    Recommendation for proposes of new types to HXLTMTypum (if over the years)
    this happens:

    Add yourself to the Author of the individual functions and (even if need
    help for the documentation) add inline documentation about the naming of
    the funcion.

    You can also write non eng-Latn comments.
    [eng-Latn]_

    Author:
        Emerson Rocha <rocha[at]ieee.org>
        David Megginson
            (HXLTMTypum based also on from hxl.datatypes)
    Creation date:
            2018-04-07 hxl.datatypes
                       (@see https://github.com/HXLStandard/libhxl-python
                        /blob/main/hxl/datatypes.py)
            2021-06-12 HXLTMTypum

    Testum:
>>> HXLTMTypum.hoc_est_numerum(1234)
True
>>> HXLTMTypum.hoc_est_numerum("1234")
True
>>> HXLTMTypum.collectionem_datum_typum([1])
'numerum'
>>> HXLTMTypum.collectionem_datum_typum([1, "2", "tribus"])
'textum'
>>> HXLTMTypum.collectionem_datum_typum(["", "   ", "	"])
'vacuum'
    """

    @staticmethod
    def datum_typum(rem: Type[Any], _annotationem=None) -> str:
        """Datum typum

        Trivia:
        - datum, https://en.wiktionary.org/wiki/datum#Latin
        - typum, https://en.wiktionary.org/wiki/typus#Latin
        - rem, https://en.wiktionary.org/wiki/res#Latin

        Args:
            rem (Type[Any]): Rem

        Returns:
            str: Textum datum typum
        """
        # TODO: this is a draft

        if HXLTMTypum.hoc_est_numerum(rem):
            return 'numerum'
        if HXLTMTypum.hoc_est_vacuum(rem):
            return 'vacuum'

        return 'textum'

    @staticmethod
    def collectionem_datum_typum(
            colloctionem_rem,  # : List,
            _annotationem=None) -> str:
        """Datum typum

        Trivia:
        - collēctiōnem, https://en.wiktionary.org/wiki/collectio#Latin
        - datum, https://en.wiktionary.org/wiki/datum#Latin
        - typum, https://en.wiktionary.org/wiki/typus#Latin
        - rem, https://en.wiktionary.org/wiki/res#Latin
        - incognitum, https://en.wiktionary.org/wiki/incognitus#Latin

        Args:
            rem (Type[Any]): Rem

        Returns:
            str: Textum datum typum
        """
        # TODO: this is a draft
        resultatum = set()

        try:
            iter(colloctionem_rem)
            # print('iteration will probably work')
        except TypeError:
            return 'incognitum'
            # print('not iterable')
        for rem in colloctionem_rem:
            resultatum.add(HXLTMTypum.datum_typum(rem))
        resultatum = list(resultatum)

        if len(resultatum) == 1:
            return resultatum[0]

        if 'vacuum' in resultatum:
            resultatum.remove('vacuum')
            if len(resultatum) == 1:
                return resultatum[0]

        if 'textum' in resultatum:
            return 'textum'
        return 'incognitum'

    @staticmethod
    def hoc_est_numerum(rem: Type[Any]) -> bool:
        """Hoc est numerum?

        _[eng-Latn]
        hxl.datatypes.is_number()

        By duck typing, test if a value contains something recognisable as
        a number.
        [eng-Latn]_

        Trivia:
          - rem, https://en.wiktionary.org/wiki/res#Latin
          - hoc, https://en.wiktionary.org/wiki/hoc#Latin
          - est, https://en.wiktionary.org/wiki/est#Latin
          - numerum, https://en.wiktionary.org/wiki/numerus#Latin

        Args:
            rem ([Any]): Rem

        Returns:
            [str]: Datum typum de rem
        """
        try:
            float(rem)
            return True
        except ValueError:
            return False

    @staticmethod
    def hoc_est_vacuum(rem: Type[Any]) -> bool:
        """Hoc est numerum?

        _[eng-Latn]
        hxl.datatypes.is_empty()

        None, empty string, or whitespace only counts as empty; anything else
        doesn't.
        [eng-Latn]_

        Trivia:
          - rem, https://en.wiktionary.org/wiki/res#Latin
          - hoc, https://en.wiktionary.org/wiki/hoc#Latin
          - est, https://en.wiktionary.org/wiki/est#Latin
          - vacuum, https://en.wiktionary.org/wiki/vacuus#Latin

        Args:
            rem ([Any]): Rem

        Returns:
            [str]: Datum typum de rem
        """
        # TODO: implement the '∅' that we use for intentionaly mark
        #       a value that is okay to be empty

        return rem is None or rem == '' or str(rem).isspace()

    @staticmethod
    def in_numerum(rem: Union[int, str]) -> Union[int, float]:
        """Trānslātiōnem: rem in numerum

        Trivia:
          - rem, https://en.wiktionary.org/wiki/res#Latin
          - in, https://en.wiktionary.org/wiki/in#Latin
          - numerum, https://en.wiktionary.org/wiki/numerus#Latin

        Args:
            rem ([Any]): Rem

        Returns:
            [int, float]: Rem in numerum
        """
        # _[eng-Latn]
        # TODO: is a draft. We have so many types of numbers that this will
        #       need lots of funcions. In special to convert, for example
        #       I = 1, V = 5, IX = 9, ... and other textum types
        #       (Emerson Rocha, 2021-07-13 04:14 UTC)
        # [eng-Latn]_
        return HXLTMTypum.in_numerum_simplex(rem)

    @staticmethod
    def in_textum_json(
            rem: Any,
            formosum: Union[bool, int] = None,
            clavem_sortem: bool = False,
            imponendum_praejudicium: bool = False
    ) -> str:
        """Trānslātiōnem: rem in textum JSON

        Trivia:
          - rem, https://en.wiktionary.org/wiki/res#Latin
          - in, https://en.wiktionary.org/wiki/in#Latin
          - json, https://www.json.org/
          - fōrmōsum, https://en.wiktionary.org/wiki/formosus
          - impōnendum, https://en.wiktionary.org/wiki/enforcier#Old_French
          - praejūdicium, https://en.wiktionary.org/wiki/praejudicium#Latin
          - sortem, https://en.wiktionary.org/wiki/sors#Latin
          - clāvem, https://en.wiktionary.org/wiki/clavis#Latin

        Args:
            rem ([Any]): Rem

        Returns:
            [str]: Rem in JSON textum

        Testum:
>>> rem = {"b": 2, "a": ['ت', 'ツ', '😊']}

>>> HXLTMTypum.in_textum_json(rem)
'{"b": 2, "a": ["ت", "ツ", "😊"]}'

>>> HXLTMTypum.in_textum_json(rem, clavem_sortem=True)
'{"a": ["ت", "ツ", "😊"], "b": 2}'

>>> HXLTMTypum.in_textum_json(rem, imponendum_praejudicium=True)
'{"b": 2, "a": ["\\\u062a", "\\\u30c4", "\\\ud83d\\\ude0a"]}'

>>> HXLTMTypum.in_textum_json(rem, formosum=True)
'{\\n    "b": 2,\\n    \
"a": [\\n        "ت",\\n        "ツ",\\n        "😊"\\n    ]\\n}'

        """

        # print = json.dumps()

        if formosum is True:
            formosum = 4

        json_textum = json.dumps(
            rem,
            indent=formosum,
            sort_keys=clavem_sortem,
            ensure_ascii=imponendum_praejudicium
        )

        return json_textum

    @staticmethod
    def in_numerum_simplex(rem: Union[int, str]) -> int:
        """Rem in numerum simplex?

        _[eng-Latn]
        See also hxl.datatypes.normalise_number()

        Attempt to convert a value to a number.

        Will convert to int type if it has no decimal places.
        [eng-Latn]_

        Author:
            David Megginson

        Trivia:
          - rem, https://en.wiktionary.org/wiki/res#Latin
          - in, https://en.wiktionary.org/wiki/in#Latin
          - numerum, https://en.wiktionary.org/wiki/numerus#Latin
          - simplex, https://en.wiktionary.org/wiki/simplex#Latin
          - disciplīnam manuāle
            - https://en.wikipedia.org/wiki/IEEE_754

        Args:
            rem ([Any]): Rem

        Returns:
            [Union[int, float]]: Rem in numerum IEEE integer aut IEEE 754

        Testum:
            >>> HXLTMTypum.in_numerum_simplex('1234')
            1234
            >>> HXLTMTypum.in_numerum_simplex('1234.0')
            1234
        """
        # pylint: disable=invalid-name,no-else-return

        try:
            n = float(rem)
            if n == int(n):
                return int(n)
            else:
                return n
        except Exception as expt:
            raise ValueError(
                "Non numerum trānslātiōnem: {}".format(rem)) from expt

    @staticmethod
    def magnitudinem_de_byte(rem: str) -> int:
        """Magnitūdinem dē byte

        Trivia:
          - rem, https://en.wiktionary.org/wiki/res#Latin
          - magnitūdinem, https://en.wiktionary.org/wiki/est#Latin
          - dē, https://en.wiktionary.org/wiki/de#Latin
          - byte
            - https://en.wiktionary.org/wiki/byte#English
            - https://en.wikipedia.org/wiki/Byte

        Args:
            rem (str): Rem textum

        Returns:
            int: Numerum

        Testum:
            >>> HXLTMTypum.magnitudinem_de_byte('Testīs')
            7
        """
        if rem is None:
            return -1

        # @see https://stackoverflow.com/questions/30686701
        #      /python-get-size-of-string-in-bytes
        # TODO: This is a draft. Needs work.
        return len(rem.encode('utf-8'))

    @staticmethod
    def magnitudinem_de_numerum(rem: str) -> int:
        """Magnitūdinem dē numerum

        Trivia:
          - rem, https://en.wiktionary.org/wiki/res#Latin
          - magnitūdinem, https://en.wiktionary.org/wiki/est#Latin
          - dē, https://en.wiktionary.org/wiki/de#Latin
          - numerum, https://en.wiktionary.org/wiki/numerus#Latin

        Args:
            rem (str): Rem textum

        Returns:
            int: Numerum
        """
        print('TODO')

    @staticmethod
    def magnitudinem_de_textum(rem: str) -> int:
        """magnitūdinem dē textum

        Trivia:
          - rem, https://en.wiktionary.org/wiki/res#Latin
          - magnitūdinem, https://en.wiktionary.org/wiki/est#Latin
          - dē, https://en.wiktionary.org/wiki/de#Latin
          - textum, https://en.wiktionary.org/wiki/textus#Latin

        Args:
            rem (str): Rem textum

        Returns:
            int: Numerum

        Testum:
        >>> HXLTMTypum.magnitudinem_de_textum('Testīs')
        6
        """
        if rem is None:
            return -1

        # TODO: This is a draft. Needs work.
        return len(rem)


class HXLTMUtil:
    """HXL Trānslātiōnem Memoriam auxilium programmi

    Author:
            Emerson Rocha <rocha[at]ieee.org>
    Creation date:
            2021-06-09
    """

    @staticmethod
    def bcp47_from_hxlattrs(hashtag: Union[str, None]) -> str:
        """From a typical HXLTM hashtag, return only the bcp47 language code
        without require a complex table equivalence.

        Example:
            >>> HXLTMUtil.bcp47_from_hxlattrs('#item+i_ar+i_arb+is_arab')
            'ar'
            >>> HXLTMUtil.bcp47_from_hxlattrs('#item+i_arb+is_arab')
            ''

        Args:
            linguam ([String]): A linguam code

        Returns:
            [String]: HXL Attributes
        """
        if hashtag and isinstance(hashtag, str):
            parts = hashtag.lower().split('+i_')
            for k in parts:
                if len(k) == 2:
                    return k

        return ''

    @staticmethod
    def bcp47_from_linguam(linguam: Union[str, None]) -> str:
        """From am linguam with hint about BCP47, get the BCP47 code
        Returns empty if no hint exist

        Example:
            >>> HXLTMUtil.bcp47_from_hxlattrs('por-Latn')
            ''
            >>> HXLTMUtil.bcp47_from_linguam('por-Latn@pt')
            'pt'
            >>> HXLTMUtil.bcp47_from_linguam('por-Latn@pt-BR')
            'pt-BR'

        Args:
            linguam ([String]): A linguam code

        Returns:
            [String]: HXL Attributes
        """
        if linguam.find('@') > -1:
            _linguam, bcp47 = list(linguam.split('@'))
            return bcp47

        return ''

    @staticmethod
    def hxllangattrs_list_from_item(item):
        """hxllangattrs_list_from_item get only the raw attr string part
        that is repeated severa times and mean the same logical group.

        Example:
            >>> item = {'#item+i_pt+i_por+is_latn':
            ...          '','#item+i_pt+i_por+is_latn+alt+list': '',
            ...           '#meta+item+i_pt+i_por+is_latn': ''}
            >>> HXLTMUtil.hxllangattrs_list_from_item(item)
            {'+i_pt+i_por+is_latn'}

        Args:
            item ([Dict]): An dict item
        Returns:
            [Set]: Set of unique HXL language attributes
        """
        result = set()

        for k in item:
            rawstr = ''
            bcp47 = HXLTMUtil.bcp47_from_hxlattrs(k)
            iso6393 = HXLTMUtil.iso6393_from_hxlattrs(k)
            iso115924 = HXLTMUtil.iso115924_from_hxlattrs(k)
            if bcp47:
                rawstr += '+i_' + bcp47
            if iso6393:
                rawstr += '+i_' + iso6393
            if iso115924:
                rawstr += '+is_' + iso115924
            # print('   ', k, '   ', rawstr)
            result.add(rawstr)
        return result

    @staticmethod
    def iso6393_from_hxlattrs(hashtag: Union[str, None]) -> str:
        """From a typical HXLTM hashtag, return only the ISO 639-3 language
        code without require a complex table equivalence.

        Example:
>>> HXLTMUtil.iso6393_from_hxlattrs('#item+i_ar+i_arb+is_arab')
'arb'
>>> HXLTMUtil.iso6393_from_hxlattrs('#item+i_ar')
''
>>> HXLTMUtil.iso6393_from_hxlattrs('#item+i_pt+i_por+is_latn+alt+list')
'por'

        Args:
            hashtag ([String]): A hashtag string

        Returns:
            [String]: HXL Attributes
        """
        if hashtag and isinstance(hashtag, str):
            # parts = hashtag.lower().split('+i_')
            parts = hashtag.lower().split('+')
            # '#item+i_ar+i_arb+is_arab' => ['#item', 'ar', 'arb+is_arab']
            # print(parts)
            for k in parts:
                # if len(k) == 5 and k.find('+i_') == 0:
                if len(k) == 5 and k.startswith('i_'):
                    # print(k.find('i_'))
                    return k.replace('i_', '')

        return ''

    @staticmethod
    def iso115924_from_hxlattrs(hashtag: Union[str, None]) -> str:
        """From a typical HXLTM hashtag, return only the ISO 115924
        writting system without require a complex table equivalence.

        Example:
            >>> HXLTMUtil.iso115924_from_hxlattrs('#item+i_ar+i_arb+is_arab')
            'arab'
            >>> HXLTMUtil.iso115924_from_hxlattrs('#item+i_ar')
            ''

        Args:
            hashtag ([String]): A linguam code

        Returns:
            [String]: HXL Attributes
        """
        if hashtag and isinstance(hashtag, str):
            parts = hashtag.lower().split('+')
            for k in parts:
                if k.startswith('is_'):
                    return k.replace('is_', '')

        return ''

    @staticmethod
    def linguam_2_hxlattrs(linguam):
        """linguam_2_hxlattrs

        Example:
            >>> HXLTMUtil.linguam_2_hxlattrs('por-Latn')
            '+i_por+is_latn'
            >>> HXLTMUtil.linguam_2_hxlattrs('por-Latn@pt')
            '+i_pt+i_por+is_latn'
            >>> HXLTMUtil.linguam_2_hxlattrs('por-Latn@pt-BR')
            '+i_pt+i_por+is_latn'
            >>> HXLTMUtil.linguam_2_hxlattrs('arb-Arab')
            '+i_arb+is_arab'

        Args:
            linguam ([String]): A linguam code

        Returns:
            [String]: HXL Attributes
        """
        if linguam.find('@') == -1:
            iso6393, iso115924 = list(linguam.lower().split('-'))
            return '+i_' + iso6393 + '+is_' + iso115924

        linguam, bcp47 = list(linguam.lower().split('@'))
        iso6393, iso115924 = list(linguam.split('-'))

        if bcp47.find('-') == -1:
            return '+i_' + bcp47 + '+i_' + iso6393 + '+is_' + iso115924

        # TODO: decide how to express country with hashtags
        iso6391, _adm = list(bcp47.split('-'))

        return '+i_' + iso6391 + '+i_' + iso6393 + '+is_' + iso115924

    @staticmethod
    def linguam_de_hxlhashtag(
            hxl_hashtag: str,
            non_obsoletum: bool = False,
            non_patriam: bool = False,
            non_privatum: bool = False) -> Union[str, None]:
        """Linguam de HXL hashtag

        Args:
            linguam ([str]): _[eng-Latn] An HXL hashtag [eng-Latn]_
            non_obsoletum ([bool]): Non bcp47?
            non_patriam ([bool]): Non patriam codicem??
            non_privatum ([bool]): Non privatum codicem?

        Returns:
            [Union[str, None]]: Linguam codicem aut python None

        Example:
            >>> HXLTMUtil.linguam_de_hxlhashtag(
            ...    '#meta+item+i_la+i_lat+is_latn')
            'lat-latn@la'
        """
        rawstr = ''
        bcp47 = HXLTMUtil.bcp47_from_hxlattrs(hxl_hashtag)
        iso6393 = HXLTMUtil.iso6393_from_hxlattrs(hxl_hashtag)
        iso115924 = HXLTMUtil.iso115924_from_hxlattrs(hxl_hashtag)

        if non_patriam:
            # TODO: implement +ii_ (region with political influence attribute)
            raise NotImplementedError('non_patriam')
        if non_privatum:
            # TODO: implement +ix_ (private attributes)
            raise NotImplementedError('non_privatum')

        if iso6393:
            rawstr += iso6393
        if iso115924:
            rawstr += '-' + iso115924
        if bcp47 and not non_obsoletum:
            rawstr += '@' + bcp47

        return rawstr if rawstr else None

    @staticmethod
    def load_hxltm_options(custom_file_option=None, is_debug=False):
        """Load options from cor.hxltm.yml

        Args:
            custom_file_option ([str], optional): Custom options.
                    Defaults to None.
            is_debug (bool, optional): Is debug enabled? Defaults to False.

        Returns:
            [Dict]: Dictionary of cor.hxltm.yml contents
        """
        # pylint: disable=using-constant-test
        if is_debug:
            print('load_hxltm_options')
            print('HXLM_CONFIG_BASE', HXLM_CONFIG_BASE)
            print('HXLTM_SCRIPT_DIR', HXLTM_SCRIPT_DIR)
            print('HXLTM_RUNNING_DIR', HXLTM_RUNNING_DIR)

        if custom_file_option is not None:
            if Path(custom_file_option).exists():
                return HXLTMUtil._load_hxltm_options_file(
                    custom_file_option, is_debug)
            raise RuntimeError("Configuration file not found [" +
                               custom_file_option + "]")

        if Path(HXLTM_RUNNING_DIR + '/cor.hxltm.yml').exists():
            return HXLTMUtil._load_hxltm_options_file(
                HXLTM_RUNNING_DIR + '/cor.hxltm.yml', is_debug)

        if Path(HXLM_CONFIG_BASE + '/cor.hxltm.yml').exists():
            return HXLTMUtil._load_hxltm_options_file(
                HXLM_CONFIG_BASE + '/cor.hxltm.yml', is_debug)

        if Path(HXLTM_SCRIPT_DIR + '/cor.hxltm.yml').exists():
            return HXLTMUtil._load_hxltm_options_file(
                HXLTM_SCRIPT_DIR + '/cor.hxltm.yml', is_debug)
        # print('oioioi')

        raise RuntimeError(
            "ERROR: no cor.hxltm.yml found (not even default one).")

    @staticmethod
    def _load_hxltm_options_file(file, is_debug=False):
        if is_debug:
            print('_load_hxltm_options_file: [' + file + ']')

        with open(file, "r") as read_file:
            data = yaml.safe_load(read_file)
            return data

    @staticmethod
    def xliff_item_relevant_options(item):
        """From an dict (python object) return only keys that start with
        # x_xliff

        Args:
            item ([Dict]): An non-filtered dict (python object) represent a row

        Returns:
            [Dict]: A filtered object. ∅ is replaced by python None
        """
        item_neo = {}

        for k in item:
            if k.startswith('#x_xliff'):
                if item[k] == '∅':
                    item_neo[k] = None
                else:
                    item_neo[k] = item[k]

        return item_neo

    @staticmethod
    def tmx_item_relevan_options(item):
        return item
        # item_neo = {}

        # for k in item:
        #     if k.startswith('#x_xliff'):
        #         if item[k] == '∅':
        #             item_neo[k] = None
        #         else:
        #             item_neo[k] = item[k]

        # return item_neo

    @staticmethod
    def xliff_item_xliff_source_key(item):
        for k in item:
            if k.startswith('#x_xliff+source'):
                return k

        return None

    @staticmethod
    def xliff_item_xliff_target_key(item):
        for k in item:
            if k.startswith('#x_xliff+target'):
                return k

        return None


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

    hxltmcli = HXLTMCLI()
    args = hxltmcli.make_args_hxltmcli()

    hxltmcli.execute_cli(args)


def exec_from_console_scripts():
    hxltmcli_ = HXLTMCLI()
    args_ = hxltmcli_.make_args_hxltmcli()

    hxltmcli_.execute_cli(args_)
