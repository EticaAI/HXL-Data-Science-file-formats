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
#
#                             pip install libhxl langcodes pyyaml python-liquid
#
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
#                     - langcodes (@see https://github.com/jg-rp/liquid)
#                       - pip3 install python-liquid
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:
#                 <@TODO: put additional non-anonymous names here>
#
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v0.8.4
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
#                 2021-07-15 00:02 UTC v0.8.3 HXLTM ASA working draft
#                 2021-07-18 21:39 UTC v0.8.4 HXLTM ASA MVP (TMX and XLIFF 2)
#                 2021-07-19 17:50 UTC v0.8.5 HXLTM ASA MVP XLIFF 1, TBX-Basic
# ==============================================================================
"""hxltmcli.py: Humanitarian Exchange Language Trānslātiōnem Memoriam CLI

_[eng-Latn]

Crash course from names in Latin to English
----------

- datum:
    - Dataset
- columnam (or crudum columnam):
    - Column, spreadsheet column, variable (of a item)
- līneam (or crudum līneam):
    - row, spreadsheet row, line (used mostly for 'crudum rem', raw item)
- rem:
    - Thing (generic)
- conceptum
    - Concept (used on HXLTM to diferenciate what is translation, rem, from
      concept that applies to all language variants of the sabe thing)
- fontem:
    - Source
- objectīvum:
    - Objective, target (as in target language, output archive)
- linguam:
    - Language, natural language
- bilingue
    - bilingual (as used on operations with source to target language in XLIFF)
- multiplum linguam
    - 1 to n languages (as used on operations that work with many languages
      like TMX and TBX)
- collēctiōnem:
    - collection, List, array (not sure if exist better naming in Latin, sorry)
- obiectum
    - Object (or Python Dict)
- Caput
    - Header
- Vēnandum īnsectum
    - Debugging
- 'Exemplōrum gratiā (et Python doctest, id est, testum automata)'
    - 'For example (and python doctest, that is, automated testing)'
    - @see https://docs.python.org/3/library/doctest.html
        - python3 -m doctest hxltmcli-fork-from-marcus.py
        - python3 -m doctest hxlm/core/bin/hxltmcli.py

Some other very frequent generic terms:

- ad:
    - @see https://en.wiktionary.org/wiki/ad#Latin
        - (direction) toward, to
        - up to (indicating direction upwards)
        - in consequence of
        - for, to, toward (indicating purpose or aim)
        - in order to, to, for (indicating means)
        - (...)
- de:
    - @see https://en.wiktionary.org/wiki/de#Latin
        - of, concerning, about
        - from, away from, down from, out of
- in:
    - @see https://en.wiktionary.org/wiki/in#Latin
        - toward, towards, against, at
        - until, for
        - about
        - according to

> Tips:
> - HXL-CPLP-Vocab_Auxilium-Humanitarium-API spreadsheet have additional terms
> - Google _wiktionary term-in-english_. Sometimes Google Translate will
>   give the perfect term, but to keep consistent, we use:
>    - Accusative
>        - Singular
>            - Neuter (You know, inclusive language)
> - 'Marcus loves/likes his dog', in Latin (same meaning different emphasis):
>    - Marcus canem amat.
>    - Canem Marcus amat.
>    - Amat canem Marcus.
>    - Marcus amat canem.
>    - Canem amat Marcus.
>    - Amat Marcus canem.
>    - Marcum canis amat.
>    - Canis Marcum amat.
>    - Amat canis Marcum.
>    - Marcum amat canis.
>    - Canis amat Marcum.
>    - Amat Marcum canis.
> - Latin, while very expressive/verbose language (and great to use on
>   ontologies, naming animals, etc, and this is the reason to use a few terms
>   in Latin on hxltmcli.py), was not what 'the people' used because was
>   hard even for the first class citizen with elite education 2000 years ago.
>   - Most example usages with HXLTM will use the 'prestige dialect' for a
>     ISO 15924 script (like translate from lat-Latn to ara-Arab, zho-Hant,
>     rus-Cyrl, and etc...) even when in fact we, 'the people', will use
>     more specific language/dialects, like por-Latn.

Missing 'good' Latin terms to express meaning in English (for software)
----------

- value (as in variable value)
    - @see https://en.wiktionary.org/wiki/value
- array, list
    - @see https://en.wiktionary.org/wiki/array
    - Sometimes we use 'Python List' as in
        - "Rem collēctiōnem, id est, Python List"
- output (preferable some short word, not like prōductiōnem)
    - @see https://en.wiktionary.org/wiki/output#English
- input
    - @see https://en.wiktionary.org/wiki/input

To Do
---------
- Improve the terms used for 'questions', like
  'quid'/ 'quod'
    - @see https://dcc.dickinson.edu/grammar/latin/questions


[eng-Latn]_
"""
import sys
import os
import logging
import argparse
from pathlib import Path
import re
from abc import ABC, abstractmethod

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

# @see https://github.com/jg-rp/liquid
# pip3 install -U python-liquid
# from liquid import Template as LiquidTemplate
from liquid import Environment as LiquidEnvironment
from liquid.loaders import DictLoader as LiquiDictLoader
# TODO: implement a JSON filter
#       @see https://github.com/jg-rp/liquid-extra/blob/main/liquid_extra
#            /filters/additional.py
# template = LiquidTemplate("Hello, {{ you }}!")
# print(template.render(you="World"))  # "Hello, World!"

__VERSION__ = "v0.8.5"

# _[eng-Latn]
# Note: If you are doing a fork and making it public, please customize
# __SYSTEMA_VARIANS__, even if the __VERSION__ keeps the same
# [eng-Latn]_
__SYSTEMA_VARIANS__ = "hxltmcli.py;EticaAI+voluntārium-commūne"
# Trivia:
# - systēma, https://en.wiktionary.org/wiki/systema#Latin
# - variāns, https://en.wiktionary.org/wiki/varians#Latin
# - furcam, https://en.wiktionary.org/wiki/furca#Latin
# - commūne, https://en.wiktionary.org/wiki/communis#Latin
# - voluntārium, https://en.wiktionary.org/wiki/voluntarius#Latin

__DESCRIPTIONEM_BREVE__ = """
_[eng-Latn] hxltmcli {0} is an implementation of HXLTM tagging conventions
on HXL to manage and export tabular data to popular translation memories
and glossaries file formats with non-close standards.
[eng-Latn]_"
""".format(__VERSION__)

# tag::epilogum[]
__EPILOGUM__ = """
Exemplōrum gratiā:

HXLTM (csv) -> Translation Memory eXchange format (TMX):
    hxltmcli fontem.tm.hxl.csv objectivum.tmx --objectivum-TMX

HXLTM (xlsx; sheet 7) -> Translation Memory eXchange format (TMX):
    hxltmcli fontem.xlsx objectivum.tmx --sheet 7 --objectivum-TMX

HXLTM (xlsx; sheet 7, Situs interretialis) -> HXLTM (csv):
    hxltmcli https://example.org/fontem.xlsx --sheet 7 fontem.tm.hxl.csv

HXLTM (Google Docs) -> HXLTM (csv):
    hxltmcli https://docs.google.com/spreadsheets/(...) fontem.tm.hxl.csv

HXLTM (Google Docs) -> Translation Memory eXchange format (TMX):
    hxltmcli https://docs.google.com/spreadsheets/(...) objectivum.tmx \
--objectivum-TMX
"""
# end::epilogum[]

# systēma
# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer

_HOME = str(Path.home())

# TODO: clean up redundancy from hxlm/core/schema/urn/util.py
HXLM_CONFIG_BASE = os.getenv(
    'HXLM_CONFIG_BASE', _HOME + '/.config/hxlm')
# ~/.config/hxlm/cor.hxltm.yml

# _[eng-Latn]
# This can be customized with enviroment variable HXLM_CONFIG_BASE
#
# Since hpd-toolchain is not a hard requeriment, we first try to load
# hdp-toolchain lib, but if hxltmcli is a standalone script with
# only libhxl, yaml, etc installed, we tolerate it
# [eng-Latn]_
try:
    from hxlm.core.constant import (
        HXLM_ROOT,
        HDATUM_EXEMPLUM
    )
    HXLTM_SCRIPT_DIR = HXLM_ROOT + '/core/bin'
    HXLTM_TESTUM_BASIM_DEFALLO = str(HDATUM_EXEMPLUM).replace('file://', '')
except ImportError:
    HXLTM_SCRIPT_DIR = str(Path(__file__).parent.resolve())
    HXLTM_TESTUM_BASIM_DEFALLO = str(Path(
        HXLTM_SCRIPT_DIR + '/../../../testum/hxltm').resolve())

HXLTM_RUNNING_DIR = str(Path().resolve())


class HXLTMCLI:  # pylint: disable=too-many-instance-attributes
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
        # self.args = None
        self.conf = {}  # Crudum, raw file

        # Only for initialization. Use self.hxltm_asa.ontologia (if need)
        self._ontologia = None  # HXLTMOntologia object

        # Only for initialization. Use self.hxltm_asa.argumentum (if need)
        self._argumentum: Type['HXLTMArgumentum'] = None

        # TODO: replace self.datum by HXLTMASA
        # self.datum: HXLTMDatum = None
        self.hxltm_asa: Type['HXLTMASA'] = None
        # self.meta_archivum_fontem = {}
        self.meta_archivum_fontem = {}
        # self.errors = []

        # Posix exit codes
        self.EXIT_OK = 0  # pylint: disable=invalid-name
        self.EXIT_ERROR = 1  # pylint: disable=invalid-name
        self.EXIT_SYNTAX = 2  # pylint: disable=invalid-name

        self.original_outfile = None
        self.original_outfile_is_stdout = True

    # TODO: move _objectivum_formatum_from_outfile to HXLTMOntologia
    def _objectivum_formatum_from_outfile(self, outfile):
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

    def _initiale(self, pyargs):
        """Trivia: initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        """
        # if pyargs.expertum_metadatum_est:
        #     self.expertum_metadatum_est = pyargs.expertum_metadatum_est

        # TODO: migrate all this to HXLTMASA._initiale

        # pyargs.est_stdout = True

        if pyargs:
            self._argumentum = HXLTMArgumentum().de_argparse(pyargs)
        else:
            self._argumentum = HXLTMArgumentum()

        self.conf = HXLTMUtil.load_hxltm_options(
            pyargs.archivum_configurationem,
            pyargs.venandum_insectum
        )

        self._ontologia = HXLTMOntologia(self.conf)

    def _initiale_hxltm_asa(self, archivum: str) -> bool:
        """
        _[eng-Latn]
        Pre-populate metadata about source file

        Requires already HXLated file saved on disk.
        [eng-Latn]_

        Trivia:
        - initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        - HXLTM, https://hdp.etica.ai/hxltm
        - HXLTM ASA, https://hdp.etica.ai/hxltm/archivum/#HXLTM-ASA

        Args:
            archivum (str): Archīvum trivia
            argumentum (Dict):
                _[lat-Latn]
                Python argumentum,
                https://docs.python.org/3/library/argparse.html
                [lat-Latn]_
        Returns:
            bool: If okay.
        """

        # with open(archivum, 'r') as arch:
        #     hxltm_crudum = arch.read().splitlines()

        self.hxltm_asa = HXLTMASA(
            archivum,
            ontologia=self._ontologia,
            # argumentum=argumentum,
            argumentum=self._argumentum,
            # verbosum=argumentum.hxltm_asa_verbosum
        )

        # Only for initialization. Now use  self.hxltm_asa.ontologia (if need)
        self._ontologia = None

        # Only for initialization. Now use self.hxltm_asa.argumentum (if need)
        self._argumentum = None

    def make_args_hxltmcli(self):
        """make_args_hxltmcli
        """

        self.hxlhelper = HXLUtils()
        parser = self.hxlhelper.make_args(
            description=__DESCRIPTIONEM_BREVE__,
            epilog=__EPILOGUM__
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

        # --agendum-linguam is a draft. Not 100% implemented
        parser.add_argument(
            '--agendum-linguam', '-AL',
            help='(Planned, but not implemented yet) ' +
            'Restrict working languages to a list. Useful for ' +
            'HXLTM to HXLTM or multilingual formats like TMX. ' +
            'Requires: multilingual operation. ' +
            'Accepts multiple values.',
            metavar='agendum_linguam',
            type=lambda x: x.split(',')
            # action='append',
            # nargs='?'
        )

        # --non-agendum-linguam is a draft. Not 100% implemented
        parser.add_argument(
            '--non-agendum-linguam', '-non-AL',
            help='(Planned, but not implemented yet) ' +
            'Inverse of --agendum-linguam. Document one or more ' +
            'languages that should be ignored if they exist. ' +
            'Requires: multilingual operation. ' +
            'Accept multiple values.',
            metavar='non_agendum_linguam',
            # action='append',
            type=lambda x: x.split(',')
            # nargs='?'
        )

        # @see https://la.wikipedia.org/wiki/Lingua_auxiliaris_internationalis
        # --agendum-linguam is a draft. Not 100% implemented
        parser.add_argument(
            '--auxilium-linguam', '-AUXL',
            help='(Planned, but not implemented yet) '
            'Define auxiliary language. '
            'Requires: bilingual operation (and file format allow metadata). '
            'Default: Esperanto and Interlingua ' +
            'Accepts multiple values.',
            metavar='auxilium_linguam',
            # default='epo-Latn@eo',
            # action='append',
            type=lambda x: x.split(',')
            # nargs='?'
        )

        parser.add_argument(
            '--objectivum-HXLTM', '--HXLTM',
            help='Save output as HXLTM (default). Multilingual output format.',
            # metavar='objectivum_formatum',
            dest='objectivum_formatum',
            action='append_const',
            const='HXLTM'
        )

        parser.add_argument(
            '--objectivum-TMX', '--TMX',
            help='Export to Translation Memory eXchange (TMX) v1.4b. ' +
            ' Multilingual output format',
            # metavar='objectivum_formatum',
            dest='objectivum_formatum',
            action='append_const',
            const='TMX'
        )

        parser.add_argument(
            '--objectivum-TBX-Basim', '--TBX-Basim',
            help='(Working draft) ' +
            'Export to Term Base eXchange (TBX) Basic ' +
            ' Multilingual output format',
            # metavar='objectivum_formatum',
            dest='objectivum_formatum',
            action='append_const',
            const='TBX-Basim'
        )

        parser.add_argument(
            '--objectivum-UTX', '--UTX',
            help='(Planned, but not implemented yet) ' +
            'Export to Universal Terminology eXchange (UTX). ' +
            ' Multilingual output format',
            # metavar='objectivum_formatum',
            dest='objectivum_formatum',
            action='append_const',
            const='UTX'
        )

        parser.add_argument(
            '--objectivum-XLIFF', '--XLIFF', '--XLIFF2',
            help='Export to XLIFF (XML Localization Interchange File Format)' +
            ' v2.1. ' +
            '(mono or bi-lingual support only as per XLIFF specification)',
            dest='objectivum_formatum',
            action='append_const',
            const='XLIFF'
        )

        parser.add_argument(
            '--objectivum-XLIFF-obsoletum', '--XLIFF-obsoletum', '--XLIFF1',
            help='(Not implemented) ' +
            'Export to XLIFF (XML Localization Interchange ' +
            'File Format) v1.2, an obsolete format for lazy developers who ' +
            'don\'t implemented XLIFF 2 (released in 2014) yet.',
            dest='objectivum_formatum',
            action='append_const',
            const='XLIFF-obsoletum'
        )

        parser.add_argument(
            '--objectivum-CSV-3', '--CSV-3',
            help='(Not implemented yet) ' +
            'Export to Bilingual CSV with BCP47 headers (source to target)' +
            ' plus comments on last column ',
            dest='objectivum_formatum',
            action='append_const',
            const='CSV-3'
        )

        parser.add_argument(
            '--objectivum-CSV-HXL-XLIFF', '--CSV-HXL-XLIFF',
            help='(experimental) ' +
            'HXLated bilingual CSV (feature compatible with XLIFF)',
            dest='objectivum_formatum',
            action='append_const',
            const='CSV-HXL-XLIFF'
        )

        parser.add_argument(
            '--objectivum-JSON-kv', '--JSON-kv',
            help='(Not implemented yet) ' +
            'Export to Bilingual JSON. Keys are ID (if available) or source '
            'natural language. Values are target language. '
            'No comments are exported. Monolingual/Bilingual',
            dest='objectivum_formatum',
            action='append_const',
            const='JSON-kv'
        )

        parser.add_argument(
            '--limitem-quantitatem',
            help='(Advanced, large datasets) '
            'Customize the limit of the maximum number of raw rows can '
            'be in a single step. Try increments of 1 million.'
            'Use value -1 to disable limits (even if means exaust '
            'all computer memory require full restart). '
            'Defaults to 1048576 (but to avoid non-expert humans or '
            'automated workflows generate output with missing data '
            'without no one reading the warning messages '
            'if the --limitem-quantitatem was reached AND '
            'no customization was done on --limitem-initiale-lineam '
            'an exception will abort',
            metavar='limitem_quantitatem',
            type=int,
            default=1048576,
            nargs='?'
        )

        parser.add_argument(
            '--limitem-initiale-lineam',
            help='(Advanced, large datasets) ' +
            'When working in batches and the initial row to process is not '
            'the first one (starts from 0) use this option if is '
            'inviable increase to simply --limitem-quantitatem',
            metavar='limitem_initiale_lineam',
            type=int,
            default=-1,
            nargs='?'
        )

        parser.add_argument(
            '--non-securum-limitem', '--ad-astra-per-aspera',
            help='(For situational/temporary usage, as '
            'in "one weekend" NOT six months) '
            'Disable any secure hardware limits and make the program '
            'try harder tolerate (even if means '
            'ignore entire individual rows or columns) but still work with '
            'what was left from the dataset. '
            'This option assume is acceptable not try protect from exhaust '
            'all memory or disk space when working with large datasets '
            'and (even for smaller, but not well know from the '
            'python or YAML ontologia) the current human user evaluated that '
            'the data loss is either false positive or tolerable '
            'until permanent fix.',
            metavar='ad_astra',
            action='store_const',
            const=True,
            default=None
        )

        # sēlēctum

        # @see https://stackoverflow.com/questions/15459997
        #      /passing-integer-lists-to-python/15460288
        parser.add_argument(
            '--selectum-columnam-numerum',
            help='(Advanced) ' +
            'Select only columns from source HXLTM dataset by a list of '
            'index numbers (starts by zero). As example: '
            'to select the first 3 columns'
            'use "0,1,2" and NOT "1,2,3"',
            metavar='columnam_numerum',
            # type=lambda x: x.split(',')
            type=lambda x: map(int, x.split(','))
        )
        # @see https://stackoverflow.com/questions/15459997
        #      /passing-integer-lists-to-python/15460288
        parser.add_argument(
            '--non-selectum-columnam-numerum',
            help='(Advanced) ' +
            'Exclude columns from source HXLTM dataset by a list of '
            'index numbers (starts by zero). As example: '
            'to ignore the first ("Excel A"), and fifth ("Excel: E") column:'
            'use "0,4" and not "1,5"',
            metavar='non_columnam_numerum',
            # type=lambda x: x.split(',')
            type=lambda x: map(int, x.split(','))
        )

        # Trivia: caput, https://en.wiktionary.org/wiki/caput#Latin
        # --crudum-objectivum-caput is a draft. Not 100% implemented
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
        # TODO: --archivum-configurationem-appendicem
        parser.add_argument(
            '--archivum-configurationem-appendicem',
            help='(Not implemented yet)' +
            'Path to custom configuration file (The cor.hxltm.yml)',
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
            '--expertum-HXLTM-ASA',
            help='(Expert mode) Save an Abstract Syntax Tree  ' +
            'in JSON format to a file path. ' +
            'With --expertum-HXLTM-ASA-verbosum output entire dataset data. ' +
            'File extensions with .yml/.yaml = YAML output. ' +
            'Files extensions with .json/.json5 = JSONs output. ' +
            'Default: JSON output. ' +
            'Good for debugging.',
            # dest='fontem_linguam',
            metavar='hxltm_asa',
            dest='hxltm_asa',
            action='store',
            default=None,
            nargs='?'
        )

        # verbōsum, https://en.wiktionary.org/wiki/verbosus#Latin
        parser.add_argument(
            '--expertum-HXLTM-ASA-verbosum',
            help='(Expert mode) Enable --expertum-HXLTM-ASA verbose mode',
            # dest='fontem_linguam',
            metavar='hxltm_asa_verbosum',
            dest='hxltm_asa_verbosum',
            action='store_const',
            const=True,
            default=False
        )

        # Trivia: experīmentum, https://en.wiktionary.org/wiki/experimentum
        parser.add_argument(
            # '--venandum-insectum-est, --debug',
            '--experimentum-est',
            help='(Internal testing only) Enable undocumented feature',
            metavar="experimentum_est",
            action='store_const',
            const=True,
            default=False
        )

        parser.add_argument(
            # '--venandum-insectum-est, --debug',
            '--venandum-insectum-est', '--debug',
            help='Enable debug? Extra information for program debugging',
            metavar="venandum_insectum",
            dest="venandum_insectum",
            action='store_const',
            const=True,
            default=False
        )

        # self.args = parser.parse_args()
        est_args = parser.parse_args()
        return est_args

    def execute_cli(self, pyargs,
                    stdin=STDIN, stdout=sys.stdout, _stderr=sys.stderr):
        """
        The execute_cli is the main entrypoint of HXLTMCLI. When
        called will convert the HXL source to example format.
        """
        # pylint: disable=too-many-branches,too-many-statements

        self._initiale(pyargs)

        # _[eng-Latn]
        # If the user specified an output file, we will save on
        # self.original_outfile. The pyargs.outfile will be used for temporary
        # output
        # [eng-Latn]_
        if pyargs.outfile:
            self.original_outfile = pyargs.outfile
            self.original_outfile_is_stdout = False
            if not self._argumentum.objectivum_formatum:
                self._argumentum.est_objectivum_formatum(
                    self._objectivum_formatum_from_outfile(
                        self.original_outfile))

        # print(self._argumentum.v())

        try:
            temp = tempfile.NamedTemporaryFile()
            temp_csv4xliff = tempfile.NamedTemporaryFile()
            pyargs.outfile = temp.name

            with self.hxlhelper.make_source(pyargs, stdin) as source, \
                    self.hxlhelper.make_output(pyargs, stdout) as output:
                # _[eng-Latn]
                # Save the HXL TM locally. It will be used by either in_csv
                # or in_csv + in_xliff
                # [eng-Latn]_
                hxl.io.write_hxl(output.output, source,
                                 show_tags=not pyargs.strip_tags)

            hxlated_input = pyargs.outfile

            # _[eng-Latn]
            # This step will do raw analysis of the hxlated_input on a
            # temporary on the disk.
            # [eng-Latn]_
            self._initiale_hxltm_asa(hxlated_input)

            if pyargs.hxltm_asa:
                self.in_asa(pyargs.hxltm_asa)

            if self.original_outfile_is_stdout is True and \
                    self.hxltm_asa.argumentum.objectivum_formatum is None:
                self.hxltm_asa.argumentum.objectivum_formatum = 'HXLTM'

            if self.hxltm_asa.argumentum.objectivum_formatum == 'TMX':
                # print('TMX')
                if self.original_outfile_is_stdout:
                    archivum_objectivum = False
                else:
                    archivum_objectivum = self.original_outfile
                self.in_tmx_de_hxltmasa(archivum_objectivum)

            elif self.hxltm_asa.argumentum.objectivum_formatum == 'TBX-Basim':
                # raise NotImplementedError('TBX-Basim not implemented yet')
                if self.original_outfile_is_stdout:
                    return self.in_tbx_basim_de_hxltmasa(False)
                return self.in_tbx_basim_de_hxltmasa(self.original_outfile)

            elif self.hxltm_asa.argumentum.objectivum_formatum == 'UTX':
                raise NotImplementedError('UTX not implemented yet')

            elif self.hxltm_asa.argumentum.\
                    objectivum_formatum == 'XLIFF-obsoletum':
                # raise NotImplementedError('XLIFF1 not implemented')
                # print('oi xliff 1')
                if self.original_outfile_is_stdout:
                    archivum_objectivum = False
                else:
                    archivum_objectivum = self.original_outfile
                self.in_xliff1_de_hxltmasa(archivum_objectivum)

            elif self.hxltm_asa.argumentum.objectivum_formatum == 'CSV-3':
                # raise NotImplementedError('CSV-3 not implemented yet')
                self.in_csv3(hxlated_input, self.original_outfile,
                             self.original_outfile_is_stdout, pyargs)

            elif self.hxltm_asa.argumentum.\
                    objectivum_formatum == 'CSV-HXL-XLIFF':
                raise NotImplementedError('CSV-3 not implemented yet')
                # self.in_csv(hxlated_input, self.original_outfile,
                #             self.original_outfile_is_stdout, pyargs)

            elif self.hxltm_asa.argumentum.objectivum_formatum == 'JSON-kv':
                self.in_jsonkv(hxlated_input, self.original_outfile,
                               self.original_outfile_is_stdout, pyargs)
                # raise NotImplementedError('JSON-kv not implemented yet')

            elif self.hxltm_asa.argumentum.objectivum_formatum == 'XLIFF':
                # print('XLIFF (2)')
                if self.original_outfile_is_stdout:
                    archivum_objectivum = False
                else:
                    archivum_objectivum = self.original_outfile
                self.in_xliff_de_hxltmasa(archivum_objectivum)

            elif self.hxltm_asa.argumentum.objectivum_formatum == 'HXLTM':
                # print('HXLTM')
                self.in_noop(hxlated_input, self.original_outfile,
                             self.original_outfile_is_stdout)

            elif self.hxltm_asa.argumentum.objectivum_formatum == 'CRUDUM':
                # print('CRUDUM')
                self.in_noop(hxlated_input, self.original_outfile,
                             self.original_outfile_is_stdout)

            elif self.hxltm_asa.argumentum.objectivum_formatum == 'INCOGNITUM':
                # print('INCOGNITUM')
                raise ValueError(
                    'INCOGNITUM (objetive file output based on extension) ' +
                    'failed do decide what you want. Check --help and ' +
                    'manually select an output format, like --TMX'
                )
            else:
                # print(self.argumentum.objectivum_formatum)
                # print(pyargs)
                # print(self.argumentum.v())
                raise ValueError(
                    'INCOGNITUM2 (objetive file output based on extension) ' +
                    'failed do decide what you want. Check --help and ' +
                    'manually select an output format, like --TMX'
                )

        finally:
            temp.close()
            temp_csv4xliff.close()

        return self.EXIT_OK

    def in_asa(self, hxltm_asa: str):
        """HXLTM In Fōrmātum; abstractum Python classem

        Args:
            hxltm_asa (str): archīvum locum
        """

        if str(hxltm_asa).endswith(('.yml', '.yaml')):
            resultatum = HXLTMTypum.in_textum_yaml(
                self.hxltm_asa.v(), formosum=True, clavem_sortem=True)
        elif str(hxltm_asa).endswith(('.json', '.json5')):
            resultatum = HXLTMTypum.in_textum_json(
                self.hxltm_asa.v(), formosum=True, clavem_sortem=True)
        else:
            resultatum = HXLTMTypum.in_textum_json(
                self.hxltm_asa.v(), formosum=True, clavem_sortem=True)

        with open(hxltm_asa, 'w') as writer:
            writer.write(resultatum)

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

    def in_csv3(self, hxlated_input, file_output, is_stdout, pyargs):
        """Convert HXLTM to output 'CSV-3'

        TODO: make this format use the HXLTM ASA.

        Args:
            hxlated_input ([str]): Path to HXLated CSV
            tmx_output ([str]): Path to file to write output (if not stdout)
            is_stdout (bool): Flag to tell the output is stdout
            pyargs ([type]): python argparse
        """

        # fon_ling = HXLTMUtil.linguam_2_hxlattrs(args.fontem_linguam)
        fon_bcp47 = HXLTMUtil.bcp47_from_linguam(pyargs.fontem_linguam)
        # obj_ling = HXLTMUtil.linguam_2_hxlattrs(args.objectivum_linguam)
        obj_bcp47 = HXLTMUtil.bcp47_from_linguam(pyargs.objectivum_linguam)

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

    def in_jsonkv(self, hxlated_input, file_output, is_stdout, pyargs):
        """Convert HXLTM to output 'JSON-kv'

        Args:
            hxlated_input ([str]): Path to HXLated CSV
            tmx_output ([str]): Path to file to write output (if not stdout)
            is_stdout (bool): Flag to tell the output is stdout
            pyargs ([type]): python argparse
        """

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

    def in_tbx_basim_de_hxltmasa(self, archivum_objectivum: Union[str, None]):
        """HXLTM In Fōrmātum Translation Memory eXchange format (TMX) v1.4

        Args:
            archivum_objectivum (Union[str, None]):
                Archīvum locum, id est, Python file path
        """

        # print('in_tmx_de_hxltmasa')

        farmatum_tbx_basim = HXLTMInFormatumTBXBasim(self.hxltm_asa)
        # farmatum_tmx.asa(self.hxltm_asa)

        if archivum_objectivum is None or archivum_objectivum is False or \
                len(archivum_objectivum) == 0:
            return farmatum_tbx_basim.in_normam_exitum()

        farmatum_tbx_basim.in_archivum(archivum_objectivum)

    def in_tmx_de_hxltmasa(self, archivum_objectivum: Union[str, None]):
        """HXLTM In Fōrmātum Translation Memory eXchange format (TMX) v1.4

        Args:
            archivum_objectivum (Union[str, None]):
                Archīvum locum, id est, Python file path
        """

        # print('in_tmx_de_hxltmasa')

        farmatum_tmx = HXLTMInFormatumTMX(self.hxltm_asa)
        # farmatum_tmx.asa(self.hxltm_asa)

        if archivum_objectivum is None or archivum_objectivum is False or \
                len(archivum_objectivum) == 0:
            return farmatum_tmx.in_normam_exitum()

        farmatum_tmx.in_archivum(archivum_objectivum)

    def in_xliff_de_hxltmasa(self, archivum_objectivum: Union[str, None]):
        """HXLTM In Fōrmātum XML Localization Interchange File Format (XLIFF)
        v2.1

        Args:
            archivum_objectivum (Union[str, None]):
                Archīvum locum, id est, Python file path
        """

        farmatum_xliff = HXLTMInFormatumXLIFF(self.hxltm_asa)

        if archivum_objectivum is None or archivum_objectivum is False or \
                len(archivum_objectivum) == 0:
            return farmatum_xliff.in_normam_exitum()

        farmatum_xliff.in_archivum(archivum_objectivum)

    def in_xliff1_de_hxltmasa(self, archivum_objectivum: Union[str, None]):
        """HXLTM In Fōrmātum XML Localization Interchange File Format (XLIFF)
        v1.2

        Args:
            archivum_objectivum (Union[str, None]):
                Archīvum locum, id est, Python file path
        """

        farmatum_xliff = HXLTMInFormatumXLIFF1(self.hxltm_asa)

        if archivum_objectivum is None or archivum_objectivum is False or \
                len(archivum_objectivum) == 0:
            return farmatum_xliff.in_normam_exitum()

        farmatum_xliff.in_archivum(archivum_objectivum)


@dataclass
class HXLTMASA:
    """HXLTM Abstractum Syntaxim Arborem

    _[eng-Latn]
    The HXLTM-ASA is an not strictly documented Abstract Syntax Tree
    of an data conversion operation.

    This format, different from the HXLTM permanent storage, is not
    meant to be used by end users. And, in fact, either JSON (or other
    formats, like YAML) are more a tool for users debugging the initial
    reference implementation hxltmcli OR developers using JSON
    as more advanced input than the end user permanent storage.

    Warning: The HXLTM-ASA is not meant to be an stricly documented format
    even if HXLTM eventually get used by large public. If necessary,
    some special format could be created, but this would require feedback
    from community or some work already done by implementers.
    [eng-Latn]_

    Trivia:
        - abstractum, https://en.wiktionary.org/wiki/abstractus#Latin
        - syntaxim, https://en.wiktionary.org/wiki/syntaxis#Latin
        - arborem, https://en.wiktionary.org/wiki/arbor#Latin
        - conceptum de Abstractum Syntaxim Arborem
            - https://www.wikidata.org/wiki/Q127380

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

>>> datum = HXLTMTestumAuxilium.datum('hxltm-exemplum-linguam.tm.hxl.csv')
>>> ontologia = HXLTMTestumAuxilium.ontologia()

# TODO: fix this after refactoring HXLTMDatum
>>> asa = HXLTMASA(datum, ontologia=ontologia)
>>> asa
HXLTMASA()

>>> asa.limitem_initiale_lineam
-1

>>> asa.datum.asa().limitem_initiale_lineam=3
>>> asa.datum.asa().limitem_initiale_lineam
3

>>> asa.limitem_initiale_lineam
3

>>> asa is asa.datum.asa()
True

--- >>> id(asa) is id(asa.datum.asa())
--- False
    """

    # pylint: disable=too-many-instance-attributes

    datum: InitVar[Type['HXLTMDatum']] = None
    hxltm_crudum: InitVar[List] = []
    ontologia: InitVar[Type['HXLTMOntologia']] = None

    # TODO: migrade from HXLTMcli to HXLTMASA the
    # fontem_linguam, objectivum_linguam, alternativum_linguam, linguam
    # fontem_linguam: Type['HXLTMLinguam'] = None
    # objectivum_linguam: Type['HXLTMLinguam'] = None
    # alternativum_linguam: List[Type['HXLTMLinguam']] = None

    # @see https://la.wikipedia.org/wiki/Lingua_agendi
    # agendum_linguam: InitVar[List[Type['HXLTMLinguam']]] = []
    # linguam: List[Type['HXLTMLinguam']] = None

    columnam_numerum: InitVar[List] = []  # deprecated
    non_columnam_numerum: InitVar[List] = []  # deprecated

    # Trivia: līmitem, https://en.wiktionary.org/wiki/limes#Latin
    limitem_quantitatem: InitVar[int] = -1  # deprecated
    limitem_initiale_lineam: InitVar[int] = -1  # deprecated

    argumentum: InitVar[Type['HXLTMArgumentum']] = None
    _verbosum: InitVar[bool] = False  # deprecated

    def __init__(self,
                 fontem_crudum_datum: Union[List[List], str],
                 ontologia: Union[Type['HXLTMOntologia'], Dict] = None,
                 argumentum: Type['HXLTMArgumentum'] = None):
        """

        Args:
            hxltm_crudum (List[List]):
                _[lat-Latn]
                Crudum HXLTM Archīvum (in Python Array de Array)
                [lat-Latn]_
            ontologia (Union[Type['HXLTMOntologia'], Dict]):
                _[lat-Latn]
                HXLTM Cor Ontologia e.g. cor.hxltm.yml (in Python Dict)
                [lat-Latn]_
            argumentum (HXLTMArgumentum):
                _[lat-Latn]
                HXLTMArgumentum
                [lat-Latn]_
        """

        # self.hxltm_crudum = hxltm_crudum
        if ontologia:
            self.ontologia = ontologia
        else:
            self.ontologia = HXLTMOntologia({}, vacuum=True)

        if argumentum is not None:
            self.argumentum = argumentum
        else:
            self.argumentum = HXLTMArgumentum()

        self.datum = HXLTMDatum(
            fontem_crudum_datum,
            argumentum=self.argumentum,
            # ontologia=self.ontologia
        )
        self.datum.asa(hxltm_asa=self)
        self.datum.datum_parandum_statim()

    def quod_globum_valendum(self) -> Dict:
        """Quod globum valendum?

        _[eng-Latn]
        Return global variables (for Ontologia)
        [eng-Latn]_

        Trivia:
        - globum, https://en.wiktionary.org/wiki/globus#Latin
        - valendum, https://en.wiktionary.org/wiki/valeo#Latin

        Returns:
            Dict: globum valendum
        """
        # TODO: HXLTMASA.quod_globum_valendum is a draft.
        resultatum = {}
        globum_ontologia = self.ontologia.quod_globum_valendum()
        globum_argumentum = {'globum': self.argumentum.v()}
        resultatum = {**globum_argumentum, **globum_ontologia}

        # print(globum_ontologia)

        return resultatum
        # return {'globum': resultatum}

    def v(self, _verbosum: bool = None):  # pylint: disable=invalid-name
        """Ego python Dict

        Trivia:
         - valendum, https://en.wiktionary.org/wiki/valeo#Latin
           - Anglicum (English): value (?)
         - verbosum, https://en.wiktionary.org/wiki/verbosus#Latin

        Args:
            _verbosum (bool): Verbosum est? Defallo falsum.

        Returns:
            [Dict]: Python dict
        """

        asa = {
            # A TL;DR of what the ASA file is
            '__ASA__': {
                'asa_nomen': 'HXLTM Abstractum Syntaxim Arborem',
                'instrumentum_varians': __SYSTEMA_VARIANS__,
                'instrumentum_versionem': __VERSION__,
            },
            # Somewhat portable reference of how the HXLTM ASA was generate
            # from souce input. This can be used by each tool to define
            # it's own parameters. But is preferable to try to use options
            # that could be reused by others
            '__ASA__INSTRUMENTUM__': {
                # 'agendum_linguam': 'mul-Zyyy'
                # 'agendum_linguam': []
            },

            # Similar to __ASA__INSTRUMENTUM__ (a place for tools to put
            # metadata about the datum) but the main point here is this
            # can store information that is temporary and may not make
            # sense if the ASA is shared on other computers or for long term.
            # One example is the path for the hxltm CSV temporary file on
            # local disk.
            # Why store path to temporary file? Because if HXLTM ASA is used
            # to preprocess data for another tool, a tool could still do
            # raw reading of the CSV file on disk without need to enable
            # verbose modes.
            '__ASA__TEMPORARIUM__': {
                # archīvum, https://en.wiktionary.org/wiki/archivum
                'archivum_bytes': -1,
                'archivum_temporarium_locum': None,
                'columnam_crudum_quantitatem': -1,
                # TODO: maybe implement some way to make a cheapy full
                #       disk check for how many line breaks do a file have.
                #       This could be useful for tools trying to decode CSV
                #       without being aware that may exist line breaks inside
                #       row items (they are valid).
                # @see https://stackoverflow.com/questions/845058
                # /how-to-get-line-count-of-a-large-file-cheaply-in-python
                # /27518377#27518377
                'lineam_crudum_quantitatem': -1,
                'limitem_quantitatem': self.limitem_quantitatem,
                'limitem_initiale_lineam': self.limitem_initiale_lineam,
            },
            '_datum_meta_': {},
            # '_datum_meta_': {
            #     'caput': [],
            #     # columnam, https://en.wiktionary.org/wiki/columna#Latin
            #     'columnam_quantitatem': -1,
            #     # līneam, https://en.wiktionary.org/wiki/linea#Latin
            #     'columnam_quantitatem': -1,
            #     'rem_quantitatem': -1,
            # },
            'datum': {}
        }

        asa['_datum_meta_'] = self.datum.meta.v(self._verbosum)

        # if self.argumentum.fontem_linguam:
        #     asa['__ASA__INSTRUMENTUM__']['fontem_linguam'] = \
        #         self.argumentum.fontem_linguam.v(self._verbosum)

        # if self.argumentum.objectivum_linguam:
        #     asa['__ASA__INSTRUMENTUM__']['objectivum_linguam'] = \
        #         self.argumentum.objectivum_linguam.v(self._verbosum)

        # print(self.argumentum)
        asa['__ASA__INSTRUMENTUM__']['argumentum'] = self.argumentum.v()

        # if self.alternativum_linguam and len(self.alternativum_linguam) > 0:
        #     asa['__ASA__INSTRUMENTUM__']['alternativum_linguam'] = []
        #     for rem_al in self.alternativum_linguam:
        #         asa['__ASA__INSTRUMENTUM__']['alternativum_linguam'].append(
        #             rem_al.v(self._verbosum)
        #        )

        # if self.argumentum.agendum_linguam and \
        #         len(self.argumentum.agendum_linguam) > 0:
        #     asa['__ASA__INSTRUMENTUM__']['agendum_linguam'] = []
        #     for rem_al in self.argumentum.agendum_linguam:
        #         asa['__ASA__INSTRUMENTUM__']['agendum_linguam'].append(
        #             rem_al.v(self._verbosum)
        #         )
        # if self.argumentum.auxilium_linguam and \
        #         len(self.argumentum.auxilium_linguam) > 0:
        #     asa['__ASA__INSTRUMENTUM__']['auxilium_linguam'] = []
        #     for rem_al in self.argumentum.auxilium_linguam:
        #         asa['__ASA__INSTRUMENTUM__']['auxilium_linguam'].append(
        #             rem_al.v(self._verbosum)
        #         )

        return asa


@dataclass
class HXLTMArgumentum:
    """HXLTM Argūmentum

    Trivia:
        - HXLTM:
        - HXLTM, https://hdp.etica.ai/hxltm
            - HXL, https://hxlstandard.org/
            - TM, https://www.wikidata.org/wiki/Q333761
        - argūmentum, https://en.wiktionary.org/wiki/argumentum#Latin

    Intrōductōrium cursum de Latīnam linguam (breve glōssārium):
        - archīvum, https://en.wiktionary.org/wiki/archivum
        - agendum linguam
            - https://la.wikipedia.org/wiki/Lingua_agendi
        - collēctiōnem, https://en.wiktionary.org/wiki/collectio#Latin
        - columnam, https://en.wiktionary.org/wiki/columna#Latin
        - datum, https://en.wiktionary.org/wiki/datum#Latin
        - fontem, https://en.wiktionary.org/wiki/fons#Latin
        - fōrmātum, https://en.wiktionary.org/wiki/formatus#Latin
        - initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        - ignōrandum, https://en.wiktionary.org/wiki/ignoro#Latin
        - linguam, https://en.wiktionary.org/wiki/lingua#Latin
        - līmitem, https://en.wiktionary.org/wiki/limes#Latin
        - līneam, https://en.wiktionary.org/wiki/linea#Latin
        - multiplum linguam:
            - linguam
            - multiplum, https://en.wiktionary.org/wiki/multiplus#Latin
        - objectīvum, https://en.wiktionary.org/wiki/objectivus#Latin
        - quantitātem, https://en.wiktionary.org/wiki/quantitas
        - typum, https://en.wiktionary.org/wiki/typus#Latin
        - sēcūrum, https://en.wiktionary.org/wiki/securus#Latin
        - sēlēctum, https://en.wiktionary.org/wiki/selectus#Latin
        - sōlum, https://en.wiktionary.org/wiki/solus#Latin
        - silentium, https://en.wiktionary.org/wiki/silentium
        - Vēnandum īnsectum
          - https://www.wikidata.org/wiki/Q845566

    Args:
        agendum_linguam (List[HXLTMLinguam]):
            _[lat-Latn]
            Agendum linguam
            (Optiōnem in multiplum linguam aut bilingue operātiōnem)
            [lat-Latn]_
        auxilium_linguam (List[HXLTMLinguam]):
            _[lat-Latn]
            Lingua auxiliaris
            (Optiōnem in bilingue operātiōnem)
            [lat-Latn]_
        fontem_linguam (HXLTMLinguam):
            _[lat-Latn]
            Fontem linguam
            (Optiōnem sōlum in bilingue operātiōnem)
            [lat-Latn]_
        objectivum_linguam (HXLTMLinguam):
            _[lat-Latn]
            Objectīvum linguam
            (Optiōnem sōlum in bilingue operātiōnem)
            [lat-Latn]_
        objectivum_archivum_nomen (str):
            _[lat-Latn]
            Argūmentum dēfīnītiōnem ad objectīvum archīvum nomen

            Python None est Python stdout
            [lat-Latn]_
        objectivum_formatum (HXLTMLinguam):
            _[lat-Latn]
            Argūmentum dēfīnītiōnem ad objectīvum archīvum fōrmātum
            [lat-Latn]_
        columnam_numerum (List):
            _[lat-Latn] Datum sēlēctum columnam numerum [lat-Latn]_
        non_columnam_numerum (List):
            _[lat-Latn] Datum non sēlēctum columnam numerum [lat-Latn]_
        limitem_quantitatem (int):
            _[lat-Latn] Datum līmitem līneam quantitātem [lat-Latn]_
        limitem_quantitatem (int):
            _[lat-Latn] Datum līmitem līneam quantitātem [lat-Latn]_
        limitem_initiale_lineam (int):
            _[lat-Latn] Datum initiāle līneam [lat-Latn]_
        silentium (bool):
            _[lat-Latn]
            Argūmentum dēfīnītiōnem ad silentium
            [lat-Latn]_
        ad_astra (bool):
            _[lat-Latn]
            Argūmentum ad astra per aspera
            (Non sēcūrum. Ignōrandum Python Exception et computandum līmitem)
            [lat-Latn]_
        venandum_insectum (bool):
            _[lat-Latn]
            Argūmentum dēfīnītiōnem ad Vēnandum īnsectum
            [lat-Latn]_
    """
    agendum_linguam: InitVar[List[Type['HXLTMLinguam']]] = []
    auxilium_linguam: InitVar[List[Type['HXLTMLinguam']]] = []
    fontem_linguam: InitVar[Type['HXLTMLinguam']] = None
    objectivum_linguam: InitVar[Type['HXLTMLinguam']] = None
    objectivum_formatum: InitVar[str] = 'HXLTM'
    objectivum_archivum_nomen: InitVar[str] = None
    columnam_numerum: InitVar[List] = []
    non_columnam_numerum: InitVar[List] = []
    limitem_initiale_lineam: InitVar[int] = -1
    limitem_quantitatem: InitVar[int] = 1048576
    silentium: InitVar[bool] = False
    ad_astra: InitVar[bool] = False
    venandum_insectum: InitVar[bool] = False
    # crudum_argparse: InitVar[Dict] = {}

    # def de_argparse(self, args_rem: Type['ArgumentParser']):
    def de_argparse(self, args_rem: Dict = None):
        """Argūmentum de Python argparse

        Args:
            args_rem (Dict, optional):
                Python ArgumentParser. Defallo Python None

        Returns:
            [HXLTMArgumentum]: Ego HXLTMArgumentum
        """
        # print(args_rem)
        if args_rem is not None:
            if hasattr(args_rem, 'outfile'):
                self.objectivum_archivum_nomen = args_rem.outfile

            if hasattr(args_rem, 'agendum_linguam'):
                self.est_agendum_linguam(args_rem.agendum_linguam)

            if hasattr(args_rem, 'auxilium_linguam'):
                # print('oi auxilium_linguam', args_rem.auxilium_linguam)
                self.est_auxilium_linguam(args_rem.auxilium_linguam)
            else:

                # https://iso639-3.sil.org/code/epo
                # https://iso639-3.sil.org/code/ina
                self.est_auxilium_linguam(
                    ['ina-Latn@ia', 'epo-Latn@eo'],
                    {'annotationem': 'defallo'}
                )
            # print('oi3333 ', self.auxilium_linguam[0].v())
            # print('oi3333 ', self.auxilium_linguam[1].v())

            if hasattr(args_rem, 'fontem_linguam'):
                self.est_fontem_linguam(args_rem.fontem_linguam)
            if hasattr(args_rem, 'objectivum_linguam'):
                self.est_objectivum_linguam(args_rem.objectivum_linguam)

            if hasattr(args_rem, 'objectivum_formatum'):
                if isinstance(args_rem.objectivum_formatum, list):
                    # TODO: deal with multiple outputs
                    self.objectivum_formatum = args_rem.objectivum_formatum[0]
                else:
                    self.objectivum_formatum = args_rem.objectivum_formatum

            if hasattr(args_rem, 'columnam_numerum'):
                self.columnam_numerum = args_rem.columnam_numerum
            if hasattr(args_rem, 'non_columnam_numerum'):
                self.non_columnam_numerum = args_rem.non_columnam_numerum

            if hasattr(args_rem, 'limitem_quantitatem'):
                self.limitem_quantitatem = args_rem.limitem_quantitatem
            if hasattr(args_rem, 'limitem_initiale_lineam'):
                self.limitem_initiale_lineam = \
                    args_rem.limitem_initiale_lineam

            if hasattr(args_rem, 'silentium'):
                self.est_ad_astra(args_rem.silentium)

            if hasattr(args_rem, 'ad_astra'):
                self.est_ad_astra(args_rem.ad_astra)

            if hasattr(args_rem, 'venandum_insectum'):
                self.est_venandum_insectum(args_rem.venandum_insectum)

        return self

    def est_ad_astra(self, rem: bool):
        """Argūmentum ad astra per aspera

        (Non sēcūrum. Ignōrandum Python Exception et computandum līmitem)

        Args:
            rem (Union[str, HXLTMLinguam]): Rem

        Returns:
            [HXLTMArgumentum]: Ego HXLTMArgumentum
        """
        self.ad_astra = bool(rem)

        return self

    def est_agendum_linguam(self, rem: Union[str, list]):
        """Argūmentum dēfīnītiōnem ad agendum linguam

        (Optiōnem in multiplum linguam aut bilingue operātiōnem)

        Args:
            rem (Union[str, HXLTMLinguam]): Rem

        Returns:
            [HXLTMArgumentum]: Ego HXLTMArgumentum
        """
        if isinstance(rem, list):
            unicum = set(rem)
            for item in unicum:
                if isinstance(rem, HXLTMLinguam):
                    self.agendum_linguam.append(item)
                else:
                    self.agendum_linguam.append(HXLTMLinguam(item))
        elif isinstance(rem, str):
            collectionem = rem.split(',')
            unicum = set(collectionem)
            for item in collectionem:
                self.agendum_linguam.append(HXLTMLinguam(item.trim()))
        elif rem is None:
            # self.agendum_linguam.append(HXLTMLinguam())
            self.agendum_linguam = []
        else:
            raise SyntaxError('Rem typum incognitum {}'.format(str(rem)))

        return self

    def est_auxilium_linguam(self, rem: Union[str, list], meta: Dict = None):
        """Argūmentum dēfīnītiōnem ad auxilium linguam

        (Optiōnem in multiplum linguam aut bilingue operātiōnem)

        Args:
            rem (Union[str, HXLTMLinguam]): Rem

        Returns:
            [HXLTMArgumentum]: Ego HXLTMArgumentum
        """
        # print(rem)
        if isinstance(rem, list):
            unicum = set(rem)
            for item in unicum:
                if isinstance(rem, HXLTMLinguam):
                    self.auxilium_linguam.append(item)
                else:
                    self.auxilium_linguam.append(
                        HXLTMLinguam(item, meta=meta))

        elif isinstance(rem, str):
            collectionem = rem.split(',')
            # print(collectionem)
            unicum = set(collectionem)
            for item in collectionem:
                self.auxilium_linguam.append(
                    HXLTMLinguam(item.trim(), meta=meta))
        elif rem is None:
            # self.agendum_linguam.append(HXLTMLinguam())
            self.auxilium_linguam = []
        else:
            raise SyntaxError('Rem typum incognitum {}'.format(str(rem)))

        # print('oi3', self.auxilium_linguam[0].v())
        return self

    def est_fontem_linguam(self, rem: Union[str, Type['HXLTMLinguam']]):
        """Argūmentum dēfīnītiōnem ad fontem linguam

        (Optiōnem sōlum in bilingue operātiōnem)

        Args:
            rem (Union[str, HXLTMLinguam]): Rem

        Returns:
            [HXLTMArgumentum]: Ego HXLTMArgumentum
        """
        if isinstance(rem, HXLTMLinguam):
            self.fontem_linguam = rem
        else:
            self.fontem_linguam = HXLTMLinguam(rem)
        return self

    def est_objectivum_formatum(self, rem: str = 'HXLTM'):
        """Argūmentum dēfīnītiōnem ad objectīvum archīvum fōrmātum

        Args:
            rem (Union[str, HXLTMLinguam]): Rem

        Returns:
            [HXLTMArgumentum]: Ego HXLTMArgumentum
        """
        if rem is None or len(rem) == 0:
            self.objectivum_formatum = 'HXLTM'
        else:
            self.objectivum_formatum = rem

        return self

    def est_objectivum_linguam(self, rem: Union[str, Type['HXLTMLinguam']]):
        """Argūmentum dēfīnītiōnem ad objectīvum linguam

        (Optiōnem sōlum in bilingue operātiōnem)

        Args:
            rem (Union[str, HXLTMLinguam]): Rem

        Returns:
            [HXLTMArgumentum]: Ego HXLTMArgumentum
        """
        if isinstance(rem, HXLTMLinguam):
            self.objectivum_linguam = rem
        else:
            self.objectivum_linguam = HXLTMLinguam(rem)
        return self

    def est_silentium(self, rem: bool):
        """Argūmentum dēfīnītiōnem ad silentium

        Args:
            rem (bool): Rem

        Returns:
            [HXLTMArgumentum]: Ego HXLTMArgumentum
        """
        self.silentium = bool(rem)

        return self

    def est_venandum_insectum(self, rem: bool):
        """Argūmentum dēfīnītiōnem ad Vēnandum īnsectum

        Args:
            rem (bool): Rem

        Returns:
            [HXLTMArgumentum]: Ego HXLTMArgumentum
        """
        self.venandum_insectum = bool(rem)

        return self

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
        # TODO: add a commom helper of this for all other .v()
        # TODO: make it at least one level more deep (or recursive)

        # print('oi4', id(self), self.__dict__)

        resultatum = {}
        for clavem in self.__dict__:
            resultatum[clavem] = {}
            if isinstance(self.__dict__[clavem], list):
                resultatum[clavem] = []

                # print('list', clavem, len(self.__dict__[clavem]))
                if len(self.__dict__[clavem]) > 0:
                    for rem in self.__dict__[clavem]:
                        if hasattr(rem, 'v'):
                            resultatum[clavem].append(rem.v())
                        else:
                            resultatum[clavem].append(rem)
            elif hasattr(self.__dict__[clavem], 'v'):
                resultatum[clavem] = self.__dict__[clavem].v()
            else:
                # print('fallback', clavem)
                resultatum[clavem] = self.__dict__[clavem]

        # Hotfix, since code above is not recursive
        if self.auxilium_linguam is not None and \
                len(self.auxilium_linguam) > 0:
            resultatum['auxilium_linguam'] = \
                [item.v() for item in self.auxilium_linguam]

        if self.agendum_linguam is not None and \
                len(self.agendum_linguam) > 0:
            resultatum['agendum_linguam'] = \
                [item.v() for item in self.agendum_linguam]

        # resultatum['teste'] = self.auxilium_linguam

        # return self.__dict__
        return resultatum


@dataclass
class HXLTMDatum:
    """
    _[eng-Latn]
    HXLTMDatum is a python wrapper for the an HXLated HXLTM dataset. It
    either be initialized by a raw Python array of arrays (with 1st or 2nd)
    row with the HXL hashtags) or with a path for a file on local disk.

    One limitation (that is unlikely to be a problem) is, similar to
    softwares like Pandas (and unlikely libhxl, that play nice with streams)
    this class requires load all the data on the memory instead of process
    row by row.

    NOTE: see also HXLTMASA(). Both are similar but HXLTMASA() could in some
          cases to be implemented eventually hold more than one HXlated
          dataset in memory, so HXLTMDatum is somewhat a simplified version
          (whitout awareness of ontologia, for example).
    [eng-Latn]_

    Args:
        crudum_datum (Union[List[List], str]):
        argumentum (HXLTMArgumentum):
            _[lat-Latn]
            HXLTMArgumentum
            [lat-Latn]_
        argumentum (HXLTMArgumentum):
        ontologia (HXLTMArgumentum):

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

>>> crudum_datum = [
...   ['id', 'Nōmen', 'Annotātiōnem'],
...   ['#item+id', '#item+lat_nomen', ''],
...   [1, 'Marcus canem amat.', 'Vērum!'],
...   [2, 'Canem Marcus amat.', ''],
...   [3, 'Amat canem Marcus.', 'vērum? vērum!']
...   ]

#>>> crudum_datum
    """

    # crudum: InitVar[List] = []
    crudum_caput: InitVar[List] = []
    crudum_hashtag: InitVar[List] = []
    # conceptum = InitVar[List] = []
    # conceptum = InitVar[List[Type['HXLTMLinguam']]] = None
    # com = InitVar[List[Type['HXLTMDatumConceptumSaccum']]] = None
    meta: InitVar[Type['HXLTMDatumCaput']] = None

    # Data without headers, [līneam x columnam]
    datum: InitVar[List] = []
    conceptum: InitVar[List[Type['HXLTMDatumConceptumSaccum']]] = []
    columnam: InitVar[List] = []  # @deprecated
    ontologia: InitVar[Type['HXLTMOntologia']] = None
    argumentum: InitVar[Type['HXLTMArgumentum']] = None
    venandum_insectum: InitVar[bool] = False

    __crudum_datum: InitVar[Union[List[List], str]] = None
    __commune_asa: InitVar[Type['HXLTMASA']] = None

    def __init__(self,
                 crudum_datum: Union[List[List], str],
                 argumentum: Type['HXLTMArgumentum'] = None,
                 ontologia: Type['HXLTMOntologia'] = None):
        """[summary]

        Args:
            hxltm_crudum (str, List[List]): Datum
            argumentum (HXLTMArgumentum): HXLTMArgumentum
            ontologia (HXLTMOntologia): HXLTMOntologia
        """

        if argumentum is not None:
            self.argumentum = argumentum
        else:
            self.argumentum = HXLTMArgumentum()

        if ontologia is not None:
            self.ontologia = ontologia

        self.__crudum_datum = crudum_datum

        # if isinstance(crudum_datum, str):
        #     self._initialle_de_hxltm_archivum(crudum_datum)
        # elif isinstance(crudum_datum, list):
        #     self._initialle_de_hxltm_crudum(crudum_datum)
        # else:
        #     raise SyntaxError('HXLTMDatum crudum aut archivum non vacuum')
        # self._initiale_conceptum()

    def _initiale_conceptum(self) -> bool:
        """Initiāle conceptum de datum

        @see HXLTMDatumConceptumSaccum

        Returns:
            bool: Resultatum okay
        """
        if not self.datum or len(self.datum) == 0:
            return False

        crudum_grupum_conceptum = HXLTMDatumConceptumSaccum.\
            reducendum_grupum_indicem_de_datum(self.datum)
        # resultatum exemplum: {'C2': [1, 2, 3], 'C3': [4]}

        # print('crudum_grupum_conceptum', crudum_grupum_conceptum)

        for clavem in crudum_grupum_conceptum:
            crude_lineam = self.crudum_lineam_de_indicem(
                crudum_grupum_conceptum[clavem])

            # print('ooi', crudum_grupum_conceptum[clavem])
            # print('ooi', crude_lineam)
            lineam_grupum = HXLTMDatumConceptumSaccum.\
                reducendum_de_datum_saccum(self.meta, crude_lineam)
            # -> [HXLTMDatumLineam(), HXLTMDatumLineam(), HXLTMDatumLineam()]

            # print('indicem_grupum', indicem_grupum)
            # print('')
            # print('lineam_grupum', lineam_grupum)
            # break

            # print('oii', self.ontologia)

            # concept_saccum = HXLTMDatumConceptumSaccum(
            #     lineam_grupum, ontologia=self.ontologia)
            concept_saccum = HXLTMDatumConceptumSaccum(lineam_grupum)
            concept_saccum.asa(self.asa())
            # resultatum exemplum: HXLTMDatumConceptumSaccum
            self.conceptum.append(concept_saccum)

        return True

    def _initialle_de_hxltm_archivum(self, archivum: str):
        """
        Trivia: initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        """
        crudum_titulum = []
        crudum_hashtag = []
        # datum_rem = []
        self.datum = []
        datum_rem_brevis = []

        with open(archivum, 'r') as hxl_archivum:
            csv_lectorem = csv.reader(hxl_archivum)
            rem_prius = None
            for _ in range(25):
                rem_nunc = next(csv_lectorem)
                if HXLTMDatumCaput.quod_est_hashtag_caput(rem_nunc):
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
                self.datum.append(rem)

        if len(self.datum) > 0:
            # self.datum_rem = datum_rem
            datum_rem_brevis = self.datum[:5]
            for item_num in range(len(self.datum[0])):
                # print('oi2', item_num)

                # TODO: --non-selectum-columnam-numerum
                #         dont apply if item_num in self.non_columnam_numerum

                col_rem_val = HXLTMDatumColumnam.reducendum_de_datum(
                    self.datum,
                    item_num,
                    limitem_quantitatem=self.argumentum.limitem_quantitatem,
                    limitem_initiale_lineam=self.argumentum.limitem_initiale_lineam  # noqa
                )
                self.columnam.append(HXLTMDatumColumnam(
                    col_rem_val
                ))
                # print(type(self.columnam[0]))

        self.meta = HXLTMDatumCaput(
            crudum_titulum=crudum_titulum,
            crudum_hashtag=crudum_hashtag,
            datum_rem_brevis=datum_rem_brevis,
            columnam_collectionem=self.columnam,
            argumentum=self.argumentum
        )

    def _initialle_de_hxltm_crudum(self, hxltm_crudum: List):
        """
        Trivia: initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        """

        # Note: when using hxltm_crudum, the array of arrays must already
        #       be near strictly valid. We will only check where is the
        #       hashtag line and if do exist a heading line.
        crudum_titulum = []
        crudum_hashtag = []
        # datum_rem = []
        if HXLTMDatumCaput.quod_est_hashtag_caput(hxltm_crudum[0]):
            crudum_hashtag = hxltm_crudum[0]
            hxltm_crudum.pop(0)
        elif HXLTMDatumCaput.quod_est_hashtag_caput(hxltm_crudum[1]):
            crudum_titulum = hxltm_crudum[0]
            crudum_hashtag = hxltm_crudum[1]
            hxltm_crudum.pop(0)
            hxltm_crudum.pop(0)
        else:
            # print(hxltm_crudum[0])
            # print(hxltm_crudum[1])
            raise SyntaxError('HXLTMDatum quod crudum HXL hashtags?')

        # At this point, hxltm_crudum, if any, should have only data
        if len(hxltm_crudum) > 0:
            if len(crudum_hashtag) != len(hxltm_crudum[0]):
                raise SyntaxError(
                    'HXLTMDatum hashtag numerum [{}] non aequalis '
                    'datum numerum [{}]'.format(
                        len(crudum_hashtag),
                        len(hxltm_crudum[0])
                    ))

            self.datum = hxltm_crudum
            # datum_rem_brevis = hxltm_crudum[:5]
            for item_num in range(len(crudum_hashtag)):

                # TODO: --non-selectum-columnam-numerum
                #         dont apply if item_num in self.non_columnam_numerum

                col_rem_val = HXLTMDatumColumnam.reducendum_de_datum(
                    hxltm_crudum,
                    item_num,
                    limitem_quantitatem=self.argumentum.limitem_quantitatem,
                    limitem_initiale_lineam=self.argumentum.limitem_initiale_lineam)  # noqa
                self.columnam.append(HXLTMDatumColumnam(
                    col_rem_val
                ))

        self.meta = HXLTMDatumCaput(
            crudum_titulum=crudum_titulum,
            crudum_hashtag=crudum_hashtag,
            datum_rem_brevis=[],
            columnam_collectionem=self.columnam,
            # venandum_insectum=self.argumentum.venandum_insectum
        )

    def asa(self, hxltm_asa: Type['HXLTMASA'] = None) -> Type['HXLTMASA']:
        """HXLTMASA commūne objectīvum referēns

        _[eng-Latn]
        The asa() method allow to lazily inject a shared common reference to
        the global HXLTM ASA without actually using Python globals.

        This is unlikely to be a good design pattern, but get things done.
        And it still allow to use classes like this one when no advanced
        references of the ASA is necessary
        [eng-Latn]_

        Args:
            hxltm_asa (HXLTMASA): HXLTM Abstractum Syntaxim Arborem

        Returns:
            [HXLTMASA]: HXLTM Abstractum Syntaxim Arborem
        """
        if hxltm_asa is None:
            if not self.__commune_asa:
                raise ReferenceError('hxltm_asa not initialized yet')
            return self.__commune_asa
        elif self.__commune_asa is not None:
            raise ReferenceError('hxltm_asa already initialized')

        self.__commune_asa = hxltm_asa
        return self.__commune_asa

    def conceptum_de_indicem(
            self, indicem: int) -> Type['HXLTMDatumConceptumSaccum']:
        """Conceptum de indicem

        Args:
            indicem (HXLTMDatumConceptumSaccum): Conceptum

        Returns:
            [List]: valendum collēctiōnem, id est, crudum Python List
        """
        return self.conceptum[indicem]

    def conceptum_quantitatem(self) -> int:
        """Conceptum quantitatem tōtāle

        Trivia:
        - tōtāle, https://en.wiktionary.org/wiki/totalis#Latin

        Returns:
            int: quantitatem tōtāle
        """
        totale = 0
        if self.datum is not None:
            totale = len(self.datum)

        return totale

    def crudum_lineam_de_indicem(self, indicem: Union[int, list]) -> List:
        """Crudum līneam de indicem

        _[eng-Latn]
        Raw values of a row from the dataset by index
        [eng-Latn]_

        Args:
            indicem (Union[int, list]): indicem de līneam

        Returns:
            [List]: valendum collēctiōnem, id est, crudum Python List
        """
        if isinstance(indicem, int):
            return self.datum[indicem]
        resultatum = []
        for clavem in indicem:
            resultatum.append(self.datum[clavem])

        return resultatum

    def datum_parandum_statim(self) -> Type['HXLTMDatum']:
        """datum parandum  statim

        _[eng-Latn]
        Prepare the data immediately
        [eng-Latn]_
        """
        if isinstance(self.__crudum_datum, str):
            self._initialle_de_hxltm_archivum(self.__crudum_datum)
        elif isinstance(self.__crudum_datum, list):
            self._initialle_de_hxltm_crudum(self.__crudum_datum)
        else:
            raise SyntaxError('HXLTMDatum crudum aut archivum non vacuum')
        self._initiale_conceptum()

    def rem_iterandum(self) -> Type['HXLTMIterandumRem']:
        return HXLTMIterandumRem(self)
        # return HXLTMRemIterandum(self)

    def lineam_quantitatem(self) -> int:
        """Crudum līneam quantitatem tōtāle

        Trivia:
        - tōtāle, https://en.wiktionary.org/wiki/totalis#Latin

        Returns:
            int: quantitatem tōtāle
        """
        totale = 0

        if self.columnam is not None and len(self.columnam) > 0:
            totale = self.columnam[0].quantitatem
        return totale

    def v(self, verbosum: bool = None, clavem: str = None):
        """Ego python Dict

        Trivia:
         - valendum, https://en.wiktionary.org/wiki/valeo#Latin
           - Anglicum (English): value (?)
         - clāvem, https://en.wiktionary.org/wiki/clavis#Latin
         - verbosum, https://en.wiktionary.org/wiki/verbosus#Latin

        Args:
            verbosum (bool): Verbosum est? Defallo falsum.

        Returns:
            [Dict]: Python objectīvum
        """
        # pylint: disable=invalid-name

        if verbosum is not False:
            verbosum = verbosum or self.argumentum.venandum_insectum

        resultatum = {
            '_typum': 'HXLTMDatum',
            # 'crudum_caput': self.crudum_caput,
            # 'crudum_hashtag': self.crudum_hashtag,
            'meta': self.meta.v(verbosum),
            'limitem_quantitatem': self.argumentum.limitem_quantitatem,
            'limitem_initiale_lineam': self.argumentum.limitem_initiale_lineam,
            # optio --venandum-insectum-est requirere
            # 'columnam': []
        }

        if verbosum:
            resultatum['crudum_caput'] = self.crudum_caput
            resultatum['crudum_hashtag'] = self.crudum_hashtag
            resultatum['columnam'] = \
                [item.v(verbosum) if item else None for item in self.columnam]

        if clavem is not None:
            return resultatum['clavem']

        return resultatum


@dataclass
class HXLTMDatumCaput:  # pylint: disable=too-many-instance-attributes
    """
    Datum Caput

    _[eng-Latn]
    HXLTMDatumCaput contains data about hashtags, raw headings (if they
    exist on original dataset) of a dataset
    [eng-Latn]_

        Exemplōrum gratiā (et Python doctest, id est, testum automata):

>>> rem = HXLTMDatumCaput(
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

>>> rem.indicem_de_hxl_hashtag('#item+lat_nomen')
1

>>> rem.indicem_de_hxl_hashtag('#item')
0

>>> rem.indicem_de_hxl_hashtag('')
2
    """

    # crudum: InitVar[List] = []
    rem: InitVar[List] = []
    crudum_hashtag: InitVar[List] = []
    datum_rem_brevis: InitVar[List] = []  # Deprecated

    # TODO; allow conceptum_indicem not be hardcoded.
    # @see HXLTMDatumConceptumSaccum
    conceptum_indicem: InitVar[List] = [0]
    # conceptum_indicem = InitVar[List] = None
    columnam_quantitatem: InitVar[int] = 0
    columnam_quantitatem_hxl: InitVar[int] = 0
    columnam_quantitatem_hxl_unicum: InitVar[int] = 0
    columnam_quantitatem_nomen: InitVar[int] = 0
    columnam_quantitatem_nomen_unicum: InitVar[int] = 0
    lineam_quantitatem: InitVar[int] = -1
    argumentum: InitVar[Type['HXLTMArgumentum']] = None
    # venandum_insectum: InitVar[bool] = False

    def __init__(
            self,
            crudum_titulum: List,
            crudum_hashtag: List,
            datum_rem_brevis: List = None,
            columnam_collectionem: List[Type['HXLTMDatumColumnam']] = None,
            argumentum: Type['HXLTMArgumentum'] = None
    ):
        """Datum Caput

        Args:
            crudum_titulum (List):
                Crūdum titulum in Python List
            crudum_hashtag (List):
                Crūdum HXL Hashtag in Python List
            columnam_collectionem (List[HXLTMDatumColumnam]):
                HXLTMDatumColumnam in Python List
            argumentum (HXLTMArgumentum):
                HXLTMArgumentum
        """

        self.crudum_titulum = crudum_titulum
        self.crudum_hashtag = crudum_hashtag
        # self.datum_rem_brevis = datum_rem_brevis
        if argumentum is not None:
            self.argumentum = argumentum
        else:
            self.argumentum = HXLTMArgumentum()
        # self.venandum_insectum = venandum_insectum

        # self.rem = [123]

        self._initialle(
            crudum_titulum, crudum_hashtag,
            datum_rem_brevis, columnam_collectionem)

    def _initialle(
        self,
        crudum_titulum: List,
        crudum_hashtag: List,
        datum_rem_brevis: List = None,  # deprecated
        columnam_collectionem: List[Type['HXLTMDatumColumnam']] = None
    ):
        """
        Trivia: initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        """
        # self.quod_est_hashtag_caput

        non_vacuum_nomen = list(filter(len, crudum_titulum))
        # print(crudum_titulum)
        # print(crudum_hashtag)

        if datum_rem_brevis is not None:
            self.datum_rem_brevis = datum_rem_brevis
        # _[eng-Latn]
        # crudum_hashtag also have empty spaces, so it still can be used to
        # know how many columns do exist
        # [eng-Latn]_
        self.columnam_quantitatem = len(crudum_hashtag)
        self.columnam_quantitatem_hxl = \
            self.quod_est_hashtag_caput(crudum_hashtag)
        self.columnam_quantitatem_hxl_unicum = \
            self.quod_est_hashtag_caput(set(crudum_hashtag))
        self.columnam_quantitatem_nomen = len(non_vacuum_nomen)
        self.columnam_quantitatem_nomen_unicum = \
            len(set(non_vacuum_nomen))

        # self.rem = [123]

        # Note:
        # print('columnam_collectionem', columnam_collectionem)
        # print('columnam_collectionem', len(columnam_collectionem))
        for item_num in range(self.columnam_quantitatem):
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

        _[eng-Latn]
        Returns the hashtag for each column index.
        '' (empty string) if no hashtag exist for that column.
        [eng-Latn]_

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
        Very basic check to test if the number of columnam_quantitatem is exact
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

        return self.columnam_quantitatem == len(datum_rem_brevis[0])

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

    def linguam_de_columnam(self, _numerum: int) -> Type['HXLTMLinguam']:
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

    def indicem_de_hxl_hashtag(
            self, hxl_hashtag: str, exactum: bool = False,
            strictum=False) -> Union[int, None]:
        """Indicem dē HXL Hashtag de datum

        Trivia:
            - indicem, https://en.wiktionary.org/wiki/index#Latin
            - dē, https://en.wiktionary.org/wiki/de#Latin
            - hxl hashtag, https://hxlstandard.org/
            - exāctum, https://en.wiktionary.org/wiki/exactus#Latin
            - strictum, https://en.wiktionary.org/wiki/strictus#Latin

        Args:
            hxl_hashtag (str): [description]
            exactum (bool): Exāctum est? Defallo Falsum.
            strictum (bool): Strictum est? Defallo Falsum.

        Returns:
            Union[int, None]: Resultatum
        """
        # exactum_indicem = self.crudum_hashtag.find(hxl_hashtag)
        # if exactum_indicem > -1:
        #     return exactum_indicem

        if hxl_hashtag in self.crudum_hashtag:
            return self.crudum_hashtag.index(hxl_hashtag)

        if exactum and strictum:
            raise ValueError

        for rem in self.crudum_hashtag:
            if rem.startswith(hxl_hashtag):
                return self.crudum_hashtag.index(rem)

        return None

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
            verbosum = verbosum or self.argumentum.venandum_insectum

        resultatum = {
            'caput': [item.v(verbosum) if item else None for item in self.rem],
            # 'crudum_titulum': self.crudum_titulum,
            # 'crudum_hashtag': self.crudum_hashtag,
            'columnam_quantitatem': self.columnam_quantitatem,
            'columnam_quantitatem_hxl': self.columnam_quantitatem_hxl,
            'columnam_quantitatem_hxl_unicum': \
            self.columnam_quantitatem_hxl_unicum,
            'columnam_quantitatem_nomen': self.columnam_quantitatem_nomen,
            'columnam_quantitatem_nomen_unicum':
            self.columnam_quantitatem_nomen_unicum,
            # 'venandum_insectum': self.venandum_insectum,
        }

        if verbosum:
            resultatum['crudum_titulum'] = self.crudum_titulum
            resultatum['crudum_hashtag'] = self.crudum_hashtag

        # return self.__dict__
        return resultatum


@dataclass
class HXLTMDatumColumnam:
    """HXLTM Datum columnam

    Trivia:
        - HXLTM, https://hdp.etica.ai/hxltm
        - Datum, https://en.wiktionary.org/wiki/datum#Latin
        - Columnam, https://en.wiktionary.org/wiki/columna#Latin
         - summārius, https://en.wiktionary.org/wiki/summary#English
        - valendum, https://en.wiktionary.org/wiki/valeo#Latin
            - 'value' , https://en.wiktionary.org/wiki/value#English
        - quantitātem , https://en.wiktionary.org/wiki/quantitas

    """

    _typum: InitVar[str] = None
    datum_typum: InitVar['str'] = None
    datum_columnam: InitVar[List] = None
    # indicem: InitVar[int] = -1
    quantitatem: InitVar[int] = 0

    def __init__(self, datum_columnam: List = None):
        """HXLTMRemCaput initiāle

        Args:
            datum_columnam (int): Datum de columnam
        """

        self._typum = 'HXLTMDatumColumnam'

        if datum_columnam is not None:
            self.quantitatem = len(datum_columnam)
        else:
            self.datum_columnam = []
        self.datum_typum = HXLTMTypum.collectionem_datum_typum(datum_columnam)

    @staticmethod
    def reducendum_de_datum(
            datum: List,
            columnam: int,
            limitem_quantitatem: int = 1048576,
            limitem_initiale_lineam: int = -1) -> List:
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

                if limitem_initiale_lineam != -1:
                    limitem_quantitatem += limitem_initiale_lineam

                # TODO: test if is not off-by-one
                if (rem_num >= limitem_initiale_lineam) and \
                        (rem_num <= limitem_quantitatem):
                    resultatum.append(datum[rem_num][columnam])

        return resultatum

    def v(self, _verbosum: bool = False):  # pylint: disable=invalid-name
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
class HXLTMDatumConceptumSaccum:
    """HXLTM Conceptum Saccum

    Trivia:
        - HXLTM, https://hdp.etica.ai/hxltm
        - Datum, https://en.wiktionary.org/wiki/datum#Latin
        - datum saccum
            - saccum, https://en.wiktionary.org/wiki/saccus#Latin
            - "Data chunk", https://en.wikipedia.org/wiki/Chunk_(information)
        - conceptum, https://en.wiktionary.org/wiki/conceptus#Latin
        - grupum, https://en.wiktionary.org/wiki/grupus#Latin
        - obiectum, https://en.wiktionary.org/wiki/obiectum#Latin
        - redūcendum, https://en.wiktionary.org/wiki/reducendus#Latin

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

>>> ontologia = HXLTMTestumAuxilium.ontologia()
>>> crudum_titulum = ['id', 'Nōmen', 'Annotātiōnem']
>>> crudum_hashtag = [
...    '#item+conceptum+codicem',
...    '#item+rem+i_la+i_lat+is_Latn',
...    '#meta+rem+annotationem+i_la+i_lat+is_latn']
>>> datum_solum = [
...      ['', 'Salvi mundi!', ''],
...      ['C2', 'Marcus canem amat.', 'Vērum!'],
...      ['C2', 'Canem Marcus amat.', ''],
...      ['C2', 'Amat canem Marcus.', 'vērum? vērum!'],
...      ['C3', 'Vēnandum īnsectum.', ''],
...   ]
>>> caput = HXLTMDatumCaput(
...            crudum_titulum=crudum_titulum,
...            crudum_hashtag=crudum_hashtag
...        )

        _[eng-Latn]
        Do not create crudum_hxltm_asa this way. HXLTMASA do not have
        a vaccum option to create an empty object.
        [eng-Latn]_

>>> crudum_hxltm_asa = HXLTMASA([crudum_titulum] + [crudum_hashtag], ontologia)

>>> crudum_grupum_conceptum = HXLTMDatumConceptumSaccum\
    .reducendum_grupum_indicem_de_datum(
...        datum_solum
...     )
>>> crudum_grupum_conceptum
{'C2': [1, 2, 3], 'C3': [4]}

>>> crudum_grupum_conceptum.keys()
dict_keys(['C2', 'C3'])

        _[eng-Latn]
        Do not use this Conceptum_C2 way of slice. This is just to direct test
        [eng-Latn]_


>>> Conceptum_C2_datum = [datum_solum[1]] + [datum_solum[2]] + [datum_solum[3]]
>>> Conceptum_C2_datum
[['C2', 'Marcus canem amat.', 'Vērum!'], \
['C2', 'Canem Marcus amat.', ''], \
['C2', 'Amat canem Marcus.', 'vērum? vērum!']]

>>> Conceptum_C2_lineam = HXLTMDatumConceptumSaccum\
        .reducendum_de_datum_saccum(caput, Conceptum_C2_datum)
>>> Conceptum_C2_lineam
[HXLTMDatumLineam(), HXLTMDatumLineam(), HXLTMDatumLineam()]

>>> Conceptum_C2 = HXLTMDatumConceptumSaccum(Conceptum_C2_lineam)
>>> Conceptum_C2.asa(crudum_hxltm_asa)
HXLTMASA()

>>> Conceptum_C2.v(verbosum=False)
{'_typum': 'HXLTMDatumConceptumSaccum', 'conceptum_nomen': 'C2', \
'rem': {'de_id': {}, 'de_linguam': {'lat-Latn': \
{'rem': 'Marcus canem amat.', '_typum': 'HXLTMRemCaput', \
'crudum': 'lat-latn@la', 'linguam': 'lat-Latn', 'bcp47': 'la', \
'iso6391a2': 'la', 'iso6393': 'lat', 'iso115924': 'Latn'}}, \
'de_nomen_breve': {'conceptum_codicem': 'C2', \
'rem__L__': 'Marcus canem amat.'}, 'hxl': {'#item+conceptum+codicem': 'C2', \
'#item+rem+i_la+i_lat+is_Latn': 'Marcus canem amat.', \
'#meta+rem+annotationem+i_la+i_lat+is_latn': 'Vērum!'}, \
'indicem': ['C2', 'Marcus canem amat.', 'Vērum!'], 'titulum': {\
'id': 'C2', 'Nōmen': 'Marcus canem amat.', 'Annotātiōnem': 'Vērum!'}}, \
'lineam_collectionem': [], 'vacuum': False}

    """

    _typum: InitVar[str] = None
    # conceptum_nomen: InitVar[str] = ''
    datum_caput: InitVar[Type['HXLTMDatumCaput']] = None
    # ontologia: InitVar[Type['HXLTMOntologia']] = None
    lineam_collectionem: InitVar[List[Type['HXLTMDatumLineam']]] = []
    vacuum: InitVar[str] = False
    __commune_asa: InitVar[Type['HXLTMASA']] = None

    def __init__(
            self,
            lineam_collectionem: List[Type['HXLTMDatumLineam']] = None,
            # ontologia: Type['HXLTMOntologia'] = None,
            vacuum: InitVar[str] = False
    ):
        self._typum = 'HXLTMDatumConceptumSaccum'
        self.vacuum = vacuum

        if not self.vacuum:
            if lineam_collectionem is None or len(lineam_collectionem) == 0:
                raise ValueError('columnam_quantitatem vacuum est?')

            if not isinstance(lineam_collectionem[0], HXLTMDatumLineam):
                raise ValueError(
                    'lineam_collectionem non HXLTMDatumLineam est?')

            self.lineam_collectionem = lineam_collectionem

            self.datum_caput = lineam_collectionem[0].datum_caput

        # if ontologia is None:
        #     self.ontologia = HXLTMOntologia(None, vacuum=True)
        # else:
        #     self.ontologia = ontologia
            # print('nao é noneeeee')
        #     if vacuum:
        #         self.lineam_collectionem = \
        #             [None] * self.datum_caput.columnam_quantitatem
        #     else:
        #         raise ValueError('columnam_quantitatem vacuum est?')
        # else:
        #     self.lineam = lineam

    def asa(self, hxltm_asa: Type['HXLTMASA'] = None) -> Type['HXLTMASA']:
        """HXLTMASA commūne objectīvum referēns

        _[eng-Latn]
        The asa() method allow to lazily inject a shared common reference to
        the global HXLTM ASA without actually using Python globals.

        This is unlikely to be a good design pattern, but get things done.
        And it still allow to use classes like this one when no advanced
        references of the ASA is necessary
        [eng-Latn]_

        Args:
            hxltm_asa (HXLTMASA): HXLTM Abstractum Syntaxim Arborem

        Returns:
            [HXLTMASA]: HXLTM Abstractum Syntaxim Arborem
        """
        if hxltm_asa is None:
            if not self.__commune_asa:
                raise ReferenceError('hxltm_asa not initialized yet')
            return self.__commune_asa
        elif self.__commune_asa is not None:
            raise ReferenceError('hxltm_asa already initialized')

        self.__commune_asa = hxltm_asa
        return self.__commune_asa

    def contextum(self) -> Dict:
        """[summary]

        Returns:
            Dict: [description]
        """
        contextum = {}
        contextum['rem'] = self.quod_clavem_et_valendum()
        return contextum

    @staticmethod
    def reducendum_de_datum_saccum(
            datum_caput: Type['HXLTMDatumCaput'],
            datum_saccum: List[List]) -> List[Type['HXLTMDatumLineam']]:
        """Redūcendum līneam collēctiōnem de datum saccum

        Args:
            datum_caput (HXLTMDatumCaput):
            datum_saccum (List): Datum saccum [rem x col]

        _[eng-Latn]
        Please use reducendum_grupum_indicem_de_datum to already filter
        the logical lines that reflect a concept.
        [eng-Latn]_

        Returns:
            List[HXLTMDatumLineam]:
        """
        resultatum = []
        for item in datum_saccum:
            resultatum.append(HXLTMDatumLineam(
                datum_caput=datum_caput,
                lineam=item))

        return resultatum

    # https://en.wikipedia.org/wiki/Chunk_(information)
    @staticmethod
    def reducendum_grupum_indicem_de_datum(
            datum_saccum: List[List],
            columnam_conceptum_indicem: List[int] = None) -> Dict:
        """Redūcendum grupum de Conceptum (obiectum indicem)

        _[eng-Latn]
        The reducendum_grupum_indicem_de_datum can be used to break small
        chunks of raw data values in logical blocks.

        The columnam_conceptum_indicem (default = [0]) give a hint of
        which columns could reflect what is (after concanetated) each
        concept.
        [eng-Latn]_

        Args:
            datum_saccum (List):
                Datum [lineam x columnam] de Python List[List]
            columnam_conceptum_indicem (List[int], optional):
                columnam conceptum indicem collēctiōnem.
                Defallo [0] (initiāle columnam).

        Returns:
            Dict: Exemplum: {'conceptum_I': [1, 2], 'conceptum_II', [3]}
        """

        resultatum = {}
        if columnam_conceptum_indicem is None:
            cci = [0]
        else:
            cci = columnam_conceptum_indicem

        # in: lineam de datum
        for indicem_lineam, lineam in enumerate(datum_saccum):
            clavem = ''

            # in: columnam de lineam
            for conceptum_indicem in cci:
                # print(conceptum_indicem)

                # in: conceptum (columnam de lineam)
                if lineam[conceptum_indicem]:
                    # print(conceptum_indicem)
                    # print(lineam[conceptum_indicem])
                    clavem += str(lineam[conceptum_indicem])
                # indicem_lineam_collectionem.append(indicem_lineam)

            if clavem != '':
                if clavem not in resultatum:
                    resultatum[clavem] = []
                resultatum[clavem].append(indicem_lineam)

        return resultatum

    def quod_clavem_et_valendum(self) -> Dict:
        """Quod clāvem et valendum

        _[eng-Latn]
        Return a simple flat (one level) Python dictionary with variables that
        could be used to be processed by liquid template

        TODO: this version is only using the first line and ignoring concepts
              that do have more than one line (like old versions).
              The behavior of just consider the first line actually is likely
              to be the default one when no advanced schema is detected
              (like without Ontologa that matches the data).
        [eng-Latn]_

        Returns:
            [Dict]: [description]
        """

        # NOTE: the agendum-linguam should already be filtered steps before
        #       this method would try to check it.

        resultatum = {
            'de_id': {},
            'de_linguam': {},
            'de_nomen_breve': {},
            'hxl': {},
            'indicem': [],
            'titulum': {}
        }

        # print('oi3333')
        # print('oi456', self.asa().argumentum.fontem_linguam)

        fon_l = None
        obj_l = None
        aux_l = None
        # TODO: these options should only be availible if is bilingual.
        #       and do not setup it on other cases

        if self.asa().argumentum.fontem_linguam:
            fon_l = self.asa().argumentum.fontem_linguam.linguam
            resultatum['de_fontem_linguam'] = None

        if self.asa().argumentum.objectivum_linguam:
            obj_l = self.asa().argumentum.objectivum_linguam.linguam
            resultatum['de_objectivum_linguam'] = None

        if self.asa().argumentum.auxilium_linguam and \
                len(self.asa().argumentum.auxilium_linguam) > 0:
            aux_l = []
            for item in self.asa().argumentum.auxilium_linguam:
                # aux_l_nomen = item.linguam
                # aux_l[aux_l_nomen] = item
                aux_l.append(item.linguam)
            resultatum['de_auxilium_linguam'] = []

            # obj_L = self.asa().argumentum.objectivum_linguam.linguam
            # resultatum['de_auxilium_linguam'] = {}

        # print(self.ontologia.crudum)
        # print(self.ontologia.hxl_de_aliud_nomen_breve())

        for col in range(self.datum_caput.columnam_quantitatem):
            nomen_breve = ''
            # print(col)
            # print(self.lineam_collectionem[0])
            nunc_valendum = self.lineam_collectionem[0].valendum_de_index(col)

            # '#_0', '#_2', '#_3', '#_4', ...
            # resultatum['#_' + str(col)] = nunc_valendum
            resultatum['indicem'].append(nunc_valendum)
            titulum = self.datum_caput.titulum_de_columnam(col)
            if titulum:
                resultatum['titulum'][titulum] = nunc_valendum

            hxl_hashtag = self.datum_caput.hxl_hashtag_de_columnam(col)

            if hxl_hashtag:
                resultatum['hxl'][hxl_hashtag] = nunc_valendum
                # resultatum[hxl_hashtag] = nunc_valendum
                nomen_breve = \
                    self.asa().ontologia.quod_nomen_breve_de_hxl(hxl_hashtag)

            if nomen_breve:

                resultatum['de_nomen_breve'][nomen_breve] = nunc_valendum

            # TODO: make this non-hardcoded ASAP (via HXLTMOntologia)
            # print('oooi')
            if nomen_breve and nomen_breve == 'rem__L__':
                # print('nunc_valendum', nunc_valendum)
                # resultatum['rem'] = []
                nunc_valendum_rem = HXLTMRem(
                    hashtag=hxl_hashtag,
                    rem=nunc_valendum
                ).v()

                # print('fon_l', fon_l)

                if fon_l is not None and fon_l == nunc_valendum_rem['linguam']:
                    resultatum['de_fontem_linguam'] = nunc_valendum_rem

                if obj_l is not None and obj_l == nunc_valendum_rem['linguam']:
                    resultatum['de_objectivum_linguam'] = nunc_valendum_rem

                if aux_l is not None and nunc_valendum_rem['linguam'] in aux_l:
                    resultatum['de_auxilium_linguam'].append(nunc_valendum_rem)
                #     print('yay', aux_l, nunc_valendum_rem['linguam'])
                # else:
                #     print('noop', aux_l, nunc_valendum_rem['linguam'])

                resultatum['de_linguam'][nunc_valendum_rem['linguam']] = \
                    nunc_valendum_rem

            # print(col)
            # print(resultatum)

        return resultatum

    def quod_nomen(self) -> str:
        conceptum_index = [0]  # TODO: make it not hardcoded
        conceptum_nomen = ''

        if self.lineam_collectionem and len(self.lineam_collectionem) > 0:
            for vindex in conceptum_index:
                conceptum_nomen += str(
                    self.lineam_collectionem[0].valendum_de_index(vindex))

        return conceptum_nomen

    def v(self, verbosum: bool = False):  # pylint: disable=invalid-name
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
        # if verbosum is not False:
        #     verbosum = verbosum or self.argumentum.venandum_insectum

        resultatum = {
            '_typum': self._typum,
            'conceptum_nomen': self.quod_nomen(),
            'rem': self.quod_clavem_et_valendum(),
            'lineam_collectionem': [],
            'vacuum': self.vacuum,
        }

        if verbosum:
            if self.lineam_collectionem and len(self.lineam_collectionem) > 0:
                resultatum['lineam_collectionem'] = \
                    [item.v(verbosum) if item else None
                        for item in self.lineam_collectionem]

        return resultatum


@dataclass
class HXLTMDatumLineam:
    """HXLTM Datum līneam

    Trivia:
        - HXLTM, https://hdp.etica.ai/hxltm
        - Datum, https://en.wiktionary.org/wiki/datum#Latin
        - līneam, https://en.wiktionary.org/wiki/linea#Latin
        - valendum, https://en.wiktionary.org/wiki/valeo#Latin
            - 'value' , https://en.wiktionary.org/wiki/value#English
        - quantitātem , https://en.wiktionary.org/wiki/quantitas

        Exemplōrum gratiā (et Python doctest, id est, testum automata):

>>> crudum_titulum = ['id', 'Nōmen', 'Annotātiōnem']
>>> crudum_hashtag = ['#item+id', '#item+lat_nomen', '']
>>> datum_solum = [
...      [1, 'Marcus canem amat.', 'Vērum!'],
...      [2, 'Canem Marcus amat.', ''],
...      [3, 'Amat canem Marcus.', 'vērum? vērum!']
...   ]
>>> datum_lineam_III = datum_solum[2]
>>> datum_lineam_III
[3, 'Amat canem Marcus.', 'vērum? vērum!']

>>> datum = [crudum_titulum] + [crudum_hashtag] + datum_solum
>>> caput = HXLTMDatumCaput(crudum_titulum, crudum_hashtag)
>>> caput.quod_datum_rem_correctum_est()
True

>>> lineam_obj_a = HXLTMDatumLineam(datum_caput=caput, vacuum=True)
>>> lineam_obj_a.v()
{'_typum': 'HXLTMDatumLineam', 'indicem': -1, \
'lineam': [None, None, None], 'vacuum': True}


>>> lineam_obj_b = HXLTMDatumLineam(datum_caput=caput, lineam=datum_lineam_III)
>>> lineam_obj_b.v()
{'_typum': 'HXLTMDatumLineam', 'indicem': -1, \
'lineam': [3, 'Amat canem Marcus.', 'vērum? vērum!'], 'vacuum': False}

>>> lineam_obj_b.valendum_de_index(lineam_indicem = 2)
'vērum? vērum!'

>>> lineam_obj_b.valendum_de_hxl('#item+lat_nomen')
'Amat canem Marcus.'

>>> datum_lineam_III_red = HXLTMDatumLineam.reducendum_de_datum(
...    datum_lineam_III, 2)
>>> datum_lineam_III_red
'vērum? vērum!'
    """

    _typum: InitVar[str] = None
    datum_caput: InitVar[Type['HXLTMDatumCaput']] = None
    lineam: InitVar[List] = None
    indicem: InitVar[int] = -1
    vacuum: InitVar[str] = False
    # quantitatem: InitVar[int] = 0

    def __init__(
        self,
        datum_caput: Type['HXLTMDatumCaput'],
        lineam: List = None,
        indicem: int = -1,
        vacuum: bool = False
    ):
        """HXLTMRemCaput initiāle

        Args:
            datum_columnam (int): Datum de columnam
        """

        self._typum = 'HXLTMDatumLineam'

        self.datum_caput = datum_caput
        self.vacuum = vacuum

        if lineam is None or len(lineam) == 0:
            if vacuum:
                self.lineam = \
                    [None] * self.datum_caput.columnam_quantitatem
            else:
                raise ValueError('lineam vacuum est?')
        else:
            self.lineam = lineam

        self.indicem = indicem

    @staticmethod
    def reducendum_de_datum(
            datum: List,
            lineam_indicem: int) -> List:
        """Redūcendum Columnam de datum

        Args:
            datum (List): Datum [rem x col]
            columnam (int): Numerum columnam in datum

        Returns:
            List: Unum columnam
        """
        # resultatum = []
        if datum is not None and len(datum) > 0:
            for rem_num, _ in enumerate(datum):  # numero de linhas
                if rem_num == lineam_indicem:
                    return datum[rem_num]

        raise ValueError('lineam non indicem ad datum?')

    def v(self, _verbosum: bool = False):  # pylint: disable=invalid-name
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
            'indicem': self.indicem,
            'lineam': self.lineam,
            'vacuum': self.vacuum,
        }
        # resultatum['datum_caput'] = self.datum_caput

        # return self.__dict__
        return resultatum

    def valendum_de_index(self, lineam_indicem: int):
        """Valendum dē indicem

        Trivia:
            - valendum	https://en.wiktionary.org/wiki/valeo#Latin
            - dē, https://en.wiktionary.org/wiki/de#Latin
            - indicem, https://en.wiktionary.org/wiki/index#Latin

        Args:
            hxl_hashtag (str): HXL Hashtag
            lineam_indicem (int): Indicem numerum
        """

        # print('self.v()', self.v(True))
        # print('lineam_indicem', lineam_indicem)
        # print('self.lineam', self.lineam)
        # print('self.lineam[1]', self.lineam[1])
        # print('self.lineam len', len(self.lineam))
        return self.lineam[lineam_indicem]

    def valendum_de_hxl(
        self, hxl_hashtag: str, exactum: bool = False, strictum=False
    ):
        """Valendum de HXL hashtag

        Trivia:
            - valendum	https://en.wiktionary.org/wiki/valeo#Latin
            - indicem, https://en.wiktionary.org/wiki/index#Latin
            - dē, https://en.wiktionary.org/wiki/de#Latin
            - hxl hashtag, https://hxlstandard.org/
            - exāctum, https://en.wiktionary.org/wiki/exactus#Latin
            - strictum, https://en.wiktionary.org/wiki/strictus#Latin

        Args:
            hxl_hashtag (str): HXL Hashtag
            exactum (bool): Exāctum est? Defallo Falsum
            strictum (bool): Strictum est? Defallo Falsum.
        """
        indicem = self.datum_caput.indicem_de_hxl_hashtag(
            hxl_hashtag, exactum=exactum, strictum=strictum)
        if indicem:
            # print(self.lineam)
            return self.lineam[indicem]

        if strictum:
            raise ValueError

        return None


class HXLTMIterandumRem:
    """HXLTM Iterandum Rem, de Python Iterator

    Trivia:
        - HXLTM:
        - HXLTM, https://hdp.etica.ai/hxltm
            - HXL, https://hxlstandard.org/
            - TM, https://www.wikidata.org/wiki/Q333761
        - iterandum, https://en.wiktionary.org/wiki/itero#Latin
        - disciplīnam manuāle
            - https://docs.python.org/3/library/itertools.html

    Raises:
        StopIteration: fīnāle
    """

    # @see https://en.wiktionary.org/wiki/iterator
    # @see https://en.wiktionary.org/wiki/itero#Latin

    def __init__(self, hxltm_datum: Type['HXLTMDatum'] = None):
        self.hxltm_datum = hxltm_datum

        self.rem_hoc = 0
        self.rem_quantitatem = hxltm_datum.conceptum_quantitatem()

    def __iter__(self):
        return self

    def __next__(self):
        self.rem_hoc += 1
        if self.rem_hoc < self.rem_quantitatem:
            # return self.hxltm_datum.crudum_lineam_de_indicem(self.rem_hoc)
            return self.hxltm_datum.conceptum_de_indicem(self.rem_hoc)
        raise StopIteration


# class HXLTMRem:

#     def __init__(self, hxltm_datum: Type['HXLTMDatum'], rem_numerum: int):
#         self.hxltm_datum = hxltm_datum

#         # TODO: implement HXLTMRem by, via the item FIRST row number of a
#         #       grouped rem and point to hxltm_datum, generate a Row
#         #       with only HXLTMRemCaput (future HXLTMDatumCaput) plus
#         #       the data of grouped rem

#         self.rem_hoc = 0
#         self.rem_quantitatem = hxltm_datum.rem_quantitatem()

class HXLTMRemIterandum:
    """HXLTM

    @deprecated use HXLTMIterandumRem

    Trivia:
        - HXLTM:
        - HXLTM, https://hdp.etica.ai/hxltm
            - HXL, https://hxlstandard.org/
            - TM, https://www.wikidata.org/wiki/Q333761
        - disciplīnam manuāle
            - https://docs.python.org/3/library/abc.html

    Raises:
        StopIteration: fīnāle
    """

    # @see https://en.wiktionary.org/wiki/iterator
    # @see https://en.wiktionary.org/wiki/itero#Latin

    def __init__(self, hxltm_datum: Type['HXLTMDatum'] = None):
        self.hxltm_datum = hxltm_datum

        self.rem_hoc = 0
        self.rem_quantitatem = hxltm_datum.rem_quantitatem()

    def __iter__(self):
        return self

    def __next__(self):
        self.rem_hoc += 1
        if self.rem_hoc < self.rem_quantitatem:
            return self.hxltm_datum.rem_de_numerum(self.rem_hoc)
        raise StopIteration

    # def __next__(self):
    #     # Column
    #     self.rem_hoc += 1
    #     if self.rem_hoc < self.rem_quantitatem:
    #         return self.hxltm_datum.rem_de_numerum(self.rem_hoc)
    #     raise StopIteration

# for c in HXLTMRemIterandum():
#     print(c)

# fōrmātum	https://en.wiktionary.org/wiki/formatus#Latin


class HXLTMInFormatum(ABC):
    """HXLTM In Fōrmātum; abstractum Python classem

    Trivia:
        - HXLTM:
        - HXLTM, https://hdp.etica.ai/hxltm
            - HXL, https://hxlstandard.org/
            - TM, https://www.wikidata.org/wiki/Q333761
        - in, https://en.wiktionary.org/wiki/in-#Latin
        - fōrmātum, https://en.wiktionary.org/wiki/formatus#Latin
        - abstractum Python classem
            - abstractum, https://en.wiktionary.org/wiki/abstractus#Latin
            - Python, https://docs.python.org/
            - classem, https://en.wiktionary.org/wiki/classis#Latin
        - disciplīnam manuāle
            - https://docs.python.org/3/library/abc.html

    Intrōductōrium cursum de Latīnam linguam (breve glōssārium):
        - archīvum, https://en.wiktionary.org/wiki/archivum
        - datum, https://en.wiktionary.org/wiki/datum#Latin
        - contextum, https://en.wiktionary.org/wiki/contextus#Latin
        - corporeum, https://en.wiktionary.org/wiki/corporeus#Latin
        - collēctiōnem, https://en.wiktionary.org/wiki/collectio#Latin
            - id est: Python List
        - dē, https://en.wiktionary.org/wiki/de#Latin
        - errōrem, https://en.wiktionary.org/wiki/error#Latin
        - fīnāle, https://en.wiktionary.org/wiki/finalis#Latin
        - 'id est', https://en.wiktionary.org/wiki/id_est
        - initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        - locum, https://en.wiktionary.org/wiki/locum#Latin
        - resultātum, https://en.wiktionary.org/wiki/resultatum

    Speciāle verbum in HXLTM:
        - 'Exemplōrum gratiā (et Python doctest, id est, testum automata)'
            - Exemplōrum gratiā
              - https://en.wikipedia.org/wiki/List_of_Latin_phrases_(full)
            - 'Python doctest' (non Latīnam)
                -https://docs.python.org/3/library/doctest.html

    Author:
        Multis Clanculum Civibus

    Collaborators:
        Emerson Rocha <rocha[at]ieee.org>

    Creation Date:
        2021-07-14

    Revisions:

    License:
        Public Domain
    """

    # ontologia/cor.hxltm.yml clāvem nomen
    ONTOLOGIA_FORMATUM = ''

    # ontologia/cor.hxltm.yml basim extēnsiōnem
    ONTOLOGIA_FORMATUM_BASIM = ''

    __commune_asa: InitVar[Type['HXLTMASA']] = None

    # @see https://docs.python.org/3/library/logging.html
    # @see https://docs.python.org/pt-br/dev/howto/logging.html

    def __init__(self, hxltm_asa: Type['HXLTMASA']):
        """HXLTM In Farmatum initiāle

        Args:
            hxltm_asa (HXLTMASA): HXLTMASA objectīvum
        """
        self.hxltm_asa = hxltm_asa
        self.ontologia = hxltm_asa.ontologia
        self.globum = self.quod_globum_valendum()
        self.normam = self.globum['normam']

    def datum_initiale(self) -> List:
        """Datum initiāle de fōrmātum Lorem Ipsum vI.II

        Trivia:
            - datum, https://en.wiktionary.org/wiki/datum#Latin
            - initiāle, https://en.wiktionary.org/wiki/initialis#Latin

        Returns:
            List: Python List, id est: rem collēctiōnem
        """
        resultatum = []

        # TODO: move this block to HXLTMASA or HXLTMOntologia
        if 'formatum' in self.normam and 'initiale' in self.normam['formatum']:
            liquid_template = self.normam['formatum']['initiale']
            liquid_context = {}
            resultatum.append(
                self.de_liquid(liquid_template, liquid_context)
            )

        return resultatum

    @abstractmethod
    def datum_corporeum(self) -> List:
        """Datum corporeum de fōrmātum Lorem Ipsum vI.II

        Trivia:
            - datum, https://en.wiktionary.org/wiki/datum#Latin
            - corporeum, https://en.wiktionary.org/wiki/corporeus#Latin

        Returns:
            List: Python List, id est: rem collēctiōnem
        """
        # _[eng-Latn]
        # The datum_corporeum() is a hard requeriment to implement a
        # file exporter.
        # [eng-Latn]_
        resultatum = []
        resultatum.append('<!-- 🚧 Opus in progressu 🚧 -->')
        resultatum.append('<!-- ' + __class__.__name__ + ' -->')
        resultatum.append('<!-- 🚧 Opus in progressu 🚧 -->')
        return resultatum

    def datum_finale(self) -> List:
        """Datum fīnāle de fōrmātum Lorem Ipsum vI.II

        Trivia:
            - datum, https://en.wiktionary.org/wiki/datum#Latin
            - fīnāle, https://en.wiktionary.org/wiki/finalis#Latin

        Returns:
            List: Python List, id est: rem collēctiōnem
        """
        resultatum = []

        if 'formatum' in self.normam and 'finale' in self.normam['formatum']:
            liquid_template = self.normam['formatum']['finale']
            liquid_context = {}
            resultatum.append(
                self.de_liquid(liquid_template, liquid_context)
            )

        return resultatum

    def de_lineam(self) -> Type['HXLTMRemIterandum']:
        """Generandum līneam de datum

        _[eng-Latn]
        Used to generate a raw line, without deeper processing of meaning
        like generandum_rem()
        [eng-Latn]_

        Trivia:
        - 'generandum'
            - https://en.wiktionary.org/wiki/genero#Latin
            - https://en.wikipedia.org/wiki/Generator_(computer_programming)
        - līneam, https://en.wiktionary.org/wiki/linea#Latin
        - datum, https://en.wiktionary.org/wiki/datum#Latin

        Returns:
            HXLTMRemIterandum:
        """

        # Draft. Using rem_iterandum for now
        return self.hxltm_asa.rem_iterandum()

    def de_liquid(self,
                  liquid_formatum: str, liquid_contextum: Dict = None) -> str:
        """De liquid

        _[eng-Latn]
        Generate text output based on liquid templates. Global variables from
        HXLTMASA (used from Ontologia plus arguments) are availible, but
        the ideal usage is provide a dictionary with extra variables
        (like the ones provide each row interation) so the template can
        allow use them per concept bag.
        [eng-Latn]_

        Trivia:
            - Shopify liquid, https://shopify.github.io/liquid/
            - python-liquid, https://github.com/jg-rp/liquid

        Args:
            liquid_formatum (str):
                Liquid template est
            liquid_contextum (Dict, optional):
                Contextum notitia

        Returns:
            str: [description]

>>> datum = HXLTMTestumAuxilium.datum('hxltm-exemplum-linguam.tm.hxl.csv')
>>> ontologia = HXLTMTestumAuxilium.ontologia()
>>> tmx = HXLTMInFormatumTMX(HXLTMASA(datum, ontologia=ontologia))
>>> tmx.de_liquid("\
{%- for i in (1..3) -%}\
Salvi, {{ i }}! \
{% endfor -%}\
")
'Salvi, 1! Salvi, 2! Salvi, 3! '

>>> tmx.de_liquid('Salvi, {{ testum | plus: 50 }}!', {"testum": 100} )
'Salvi, 150!'
        """
        # @see https://github.com/jg-rp/liquid#quick-start
        formatum_excerptum = LiquiDictLoader(
            self.ontologia.quod_formatum_excerptum())
        globum_valendum = self.quod_globum_valendum()

        env = LiquidEnvironment(
            globals=globum_valendum,
            loader=formatum_excerptum
        )
        liquid_template = env.from_string(liquid_formatum)
        contextum = liquid_contextum if liquid_contextum else {}

        return liquid_template.render(contextum)

    def de_rem(self) -> Type['HXLTMRemIterandum']:
        """Generandum līneam de rem

        _[eng-Latn]
        For concepts where a a thing actually is more than one line on
        HXLTM tabular representation the de_rem() could be used
        instead of de_lineam()
        [eng-Latn]_

        Trivia:
        - 'generandum'
            - https://en.wiktionary.org/wiki/genero#Latin
            - https://en.wikipedia.org/wiki/Generator_(computer_programming)
        - rem	https://en.wiktionary.org/wiki/res#Latin
        - datum, https://en.wiktionary.org/wiki/datum#Latin

        Returns:
            HXLTMRemIterandum:
        """

        # @see https://gist.github.com/drmalex07/6e040310ab9ac12b4dfd
        # @see https://dzone.com/articles/python-look-ahead-multiple
        return self.hxltm_asa.datum.rem_iterandum()

    def in_archivum(self, archivum_locum: str) -> None:
        """Resultātum in Archīvum

        Args:
            archivum_locum (str): Archīvum locum, id est, Python file path
        """
        resultatum = self.in_collectionem()

        # print(archivum_locum)

        with open(archivum_locum, 'w') as archivum_punctum:
            for rem in resultatum:
                archivum_punctum.write(rem + "\n")

    def in_collectionem(self) -> List:
        """Resultātum in collēctiōnem, id est Python List

        Returns:
            List: Python List, id est: rem collēctiōnem
        """
        # @see https://stackoverflow.com/questions/1720421
        #      /how-do-i-concatenate-two-lists-in-python
        resultatum = self.datum_initiale()
        corporeum = self.datum_corporeum()
        finale = self.datum_finale()

        resultatum += corporeum
        resultatum += finale

        return resultatum

    def in_exportandum(self):
        """Resultātum in defallo

        Raises:
            NotImplementedError:
        """
        raise NotImplementedError

    def in_textum(self) -> str:
        """Resultātum in textum, id est Python str

        Returns:
            str: Python str, id est: textum
        """
        return self.in_collectionem().join("\n")

    # def in_norman_errōrem(self) -> None
    # https://en.wiktionary.org/wiki/error#Latin

    def in_normam_exitum(self) -> None:
        """Resultātum in normam exitum, id est: Python stdout

        Trivia:
        - normam, https://en.wiktionary.org/wiki/norma#Latin
        - exitum, https://en.wiktionary.org/wiki/productio#Latin
        - etymologiam:
          - stdout, Standard output
            - https://en.wiktionary.org/wiki/stdout
            - https://en.wikipedia.org/wiki/Standard_streams
        - disciplīnam manuāle
            - https://docs.python.org/3/library/sys.html#sys.stdout
        """
        # TODO: _[eng-Latn]
        #       The current version of in_normam_exitum, since depends on
        #       HXLTMInFormatum.in_collectionem(), is not optimized for
        #       large inputs that do not fit in memory. Do exist room
        #       for improvement here if someone else is interested.
        #       (Emerson Rocha, 2021-07-14 09:52 UTC)
        #       [eng-Latn]_

        initiale = self.datum_initiale()

        if len(initiale) > 0:
            for rem in initiale:
                print(rem)

        corporeum = self.datum_corporeum()

        if len(corporeum) > 0:
            for rem in corporeum:
                print(rem)

        finale = self.datum_finale()

        if len(finale) > 0:
            for rem in finale:
                print(rem)

    def quod_globum_valendum(self) -> Dict:
        """Quod globum valendum?

        _[eng-Latn]
        Return global variables (the ones that do no varies with each row)
        [eng-Latn]_

        Trivia:
        - globum, https://en.wiktionary.org/wiki/globus#Latin
        - valendum, https://en.wiktionary.org/wiki/valeo#Latin

        Returns:
            Dict: globum valendum
        """
        globum = self.hxltm_asa.quod_globum_valendum()
        summam = {}

        # print(globum.keys())

        if 'normam' in globum:
            basim = self.ONTOLOGIA_FORMATUM_BASIM
            ext = self.ONTOLOGIA_FORMATUM
            if basim not in globum['normam']:
                raise ValueError(
                    "{0}: non [normam.{1}] in "
                    "cor.hxltm.yml aut ego.hxltm.yml".format(
                        __class__.__name__, basim
                    ))

            if ext in globum['normam']:
                summam['normam'] = \
                    {**globum['normam'][basim], **globum['normam'][ext]}
            else:
                summam['normam'] = globum['normam'][basim]

            globum = {**globum, **summam}

        return globum

    # def rem(self) -> Type['HXLTMRemIterandum']:

    #     # @see https://gist.github.com/drmalex07/6e040310ab9ac12b4dfd
    #     # @see https://dzone.com/articles/python-look-ahead-multiple
    #     return self.hxltm_asa.datum.rem_iterandum()


class HXLTMInFormatumTBX(HXLTMInFormatum):
    """HXLTM In Fōrmātum TermBase eXchange (TBX)

    Trivia:
    - HXLTM:
    - HXLTM, https://hdp.etica.ai/hxltm
        - HXL, https://hxlstandard.org/
        - TM, https://www.wikidata.org/wiki/Q333761
    - in, https://en.wiktionary.org/wiki/in-#Latin
    - fōrmātum, https://en.wiktionary.org/wiki/formatus#Latin
    - TBX, <https://en.wikipedia.org/wiki/TermBase_eXchange>

    Normam:
    - http://www.terminorgs.net/downloads/TBX_Basic_Version_3.1.pdf
    - http://www.ttt.org/oscarStandards/tbx/TBXBasic.zip
    - https://www.gala-global.org/knowledge-center/industry-development
        /standards/lisa-oscar-standards
    - gala-global.org/sites/default/files/migrated-pages/docs/tbx_oscar_0.pdf

    Author:
        Emerson Rocha <rocha[at]ieee.org>

    Collaborators:
        (_[eng-Latn] Additional names here [eng-Latn]_)

    Creation Date:
        2021-07-19

    Revisions:

    License:
        Public Domain
    """

    # _[eng-Latn]
    # NOTE: some IDs, like
    #       <termEntry id="I18N_०१२३४५६७८९_〇一二三四五六七八九十百
    #           千万亿_-1+2/3*4_٩٨٧٦٥٤٣٢١٠_零壹贰叁肆伍陆柒捌玖拾佰仟萬億_I18N">
    #       will generate errors to validate TBX with TBXBasiccoreStructV02.dtd
    #       from http://www.ttt.org/oscarStandards/tbx/TBXBasic.zip
    #       The problemtic part is '+2/3*': '*', '+', '/'
    # [eng-Latn]_

    # ONTOLOGIA_FORMATUM = 'TBX-Basim'

    ONTOLOGIA_FORMATUM_BASIM = 'TBX'  # ontologia/cor.hxltm.yml clāvem nomen

    def datum_corporeum(self) -> List:
        """Datum corporeum de fōrmātum XML Localization Interchange File Format
        (XLIFF)

        Trivia:
            - datum, https://en.wiktionary.org/wiki/datum#Latin
            - corporeum, https://en.wiktionary.org/wiki/corporeus#Latin

        Returns:
            List: Python List, id est: rem collēctiōnem
        """
        resultatum = []

        liquid_template = self.normam['formatum']['corporeum']

        for rem in self.de_rem():
            liquid_context = {'rem': str(rem)}
            liquid_context = rem.contextum()
            resultatum.append(
                self.de_liquid(liquid_template, liquid_context)
            )
        return resultatum


class HXLTMInFormatumTBXBasim(HXLTMInFormatumTBX):
    """See cor.hxltm.yml:normam.TBX-Basim"""

    ONTOLOGIA_FORMATUM_BASIM = 'TBX-Basim'


class HXLTMInFormatumTMX(HXLTMInFormatum):
    """HXLTM In Fōrmātum Translation Memory eXchange format (TMX) v1.4

    Trivia:
        - HXLTM:
        - HXLTM, https://hdp.etica.ai/hxltm
            - HXL, https://hxlstandard.org/
            - TM, https://www.wikidata.org/wiki/Q333761
        - in, https://en.wiktionary.org/wiki/in-#Latin
        - fōrmātum, https://en.wiktionary.org/wiki/formatus#Latin
        - TMX, https://www.wikidata.org/wiki/Q1890189

    Normam:
        - https://www.gala-global.org/tmx-14b

    Author:
        Emerson Rocha <rocha[at]ieee.org>

    Collaborators:
        (_[eng-Latn] Additional non-anonymous names here [eng-Latn]_)

    Creation Date:
        2021-07-14

    Revisions:

    License:
        Public Domain
    """

    # ONTOLOGIA_FORMATUM = ''

    ONTOLOGIA_FORMATUM_BASIM = 'TMX'  # ontologia/cor.hxltm.yml clāvem nomen

    def datum_corporeum(self) -> List:
        """Datum corporeum de fōrmātum Translation Memory eXchange format
        (TMX) v1.4

        Trivia:
            - datum, https://en.wiktionary.org/wiki/datum#Latin
            - corporeum, https://en.wiktionary.org/wiki/corporeus#Latin

        Returns:
            List: Python List, id est: rem collēctiōnem
        """
        resultatum = []

        liquid_template = self.normam['formatum']['corporeum']

        # for numerum, rem in self.rem():
        # for rem, rem2 in self.rem():
        for rem in self.de_rem():
            # resultatum.append(rem.v())
            # print(rem)
            liquid_context = {'rem': str(rem)}
            liquid_context = rem.contextum()
            # resultatum.append(str(rem))
            resultatum.append(
                self.de_liquid(liquid_template, liquid_context)
            )
        return resultatum


class HXLTMInFormatumXLIFF(HXLTMInFormatum):
    """HXLTM In Fōrmātum XML Localization Interchange File Format (XLIFF) v2.1

    Trivia:
        - HXLTM:
        - HXLTM, https://hdp.etica.ai/hxltm
            - HXL, https://hxlstandard.org/
            - TM, https://www.wikidata.org/wiki/Q333761
        - in, https://en.wiktionary.org/wiki/in-#Latin
        - fōrmātum, https://en.wiktionary.org/wiki/formatus#Latin
        - XLIFF, <https://en.wikipedia.org/wiki/XLIFF>
        - disciplīnam manuāle
            - <https://docs.oasis-open.org/xliff/xliff-core/v2.1/>

    Normam:
        - <https://docs.oasis-open.org/xliff/xliff-core/v2.1/>

    Author:
        Emerson Rocha <rocha[at]ieee.org>

    Collaborators:
        (_[eng-Latn] Additional names here [eng-Latn]_)

    Creation Date:
        2021-07-14

    Revisions:

    License:
        Public Domain
    """

    # ONTOLOGIA_FORMATUM = ''

    ONTOLOGIA_FORMATUM_BASIM = 'XLIFF'  # ontologia/cor.hxltm.yml clāvem nomen

    def datum_corporeum(self) -> List:
        """Datum corporeum de fōrmātum XML Localization Interchange File Format
        (XLIFF)

        Trivia:
            - datum, https://en.wiktionary.org/wiki/datum#Latin
            - corporeum, https://en.wiktionary.org/wiki/corporeus#Latin

        Returns:
            List: Python List, id est: rem collēctiōnem
        """
        resultatum = []

        liquid_template = self.normam['formatum']['corporeum']

        for rem in self.de_rem():
            liquid_context = {'rem': str(rem)}
            liquid_context = rem.contextum()
            resultatum.append(
                self.de_liquid(liquid_template, liquid_context)
            )
        return resultatum


class HXLTMInFormatumXLIFF1(HXLTMInFormatum):
    """HXLTM In Fōrmātum XML Localization Interchange File Format (XLIFF) v1.2

    Trivia:
        - HXLTM:
        - HXLTM, https://hdp.etica.ai/hxltm
            - HXL, https://hxlstandard.org/
            - TM, https://www.wikidata.org/wiki/Q333761
        - in, https://en.wiktionary.org/wiki/in-#Latin
        - fōrmātum, https://en.wiktionary.org/wiki/formatus#Latin
        - XLIFF, <https://en.wikipedia.org/wiki/XLIFF>
        - disciplīnam manuāle
            - <https://docs.oasis-open.org/xliff/xliff-core/xliff-core.html>

    Normam:
        - <https://docs.oasis-open.org/xliff/xliff-core/xliff-core.html>

    Author:
        Emerson Rocha <rocha[at]ieee.org>

    Collaborators:
        (_[eng-Latn] Additional names here [eng-Latn]_)

    Creation Date:
        2021-07-18

    Revisions:

    License:
        Public Domain
    """

    # ONTOLOGIA_FORMATUM = ''

    ONTOLOGIA_FORMATUM_BASIM = 'XLIFF1'  # ontologia/cor.hxltm.yml clāvem nomen

    def datum_corporeum(self) -> List:
        """Datum corporeum de fōrmātum XML Localization Interchange File Format
        (XLIFF1)

        Trivia:
            - datum, https://en.wiktionary.org/wiki/datum#Latin
            - corporeum, https://en.wiktionary.org/wiki/corporeus#Latin

        Returns:
            List: Python List, id est: rem collēctiōnem
        """
        resultatum = []

        liquid_template = self.normam['formatum']['corporeum']

        for rem in self.de_rem():
            liquid_context = {'rem': str(rem)}
            liquid_context = rem.contextum()
            resultatum.append(
                self.de_liquid(liquid_template, liquid_context)
            )
        return resultatum


class HXLTMOntologia:
    """HXLTM Ontologia

    Trivia:
        - HXLTM:
        - HXLTM, https://hdp.etica.ai/hxltm
            - HXL, https://hxlstandard.org/
            - TM, https://www.wikidata.org/wiki/Q333761
        - Ontologia
            - https://www.wikidata.org/wiki/Q44325
            - https://la.wikipedia.org/wiki/Ontologia
            - Jacob Lorhard (1561-1609): The Creator of the Term "Ontologia"
                - https://www.ontology.co/jacob-lorhard.htm

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

>>> ontologia = HXLTMTestumAuxilium.ontologia()
>>> 'HXLTM' in list(ontologia.de('normam').keys())
True
>>> 'genus_grammaticum' in list(ontologia.de('ontologia_aliud').keys())
True
>>> 'partem_orationis' in list(ontologia.de('ontologia_aliud').keys())
True
>>> ontologia.quid_est_hashtag_circa_conceptum('#item+conceptum+codicem')
True
>>> ontologia.quid_est_hashtag_circa_conceptum('#rem+rem+i_la+i_lat+is_latn')
False
>>> ontologia.quid_est_hashtag_circa_linguam('#item+conceptum+codicem')
False
>>> ontologia.quid_est_hashtag_circa_linguam('#rem+rem+i_la+i_lat+is_latn')
True

    """

    def __init__(self, ontologia: Dict, vacuum: bool = False):
        """
        _[eng-Latn] Constructs all the necessary attributes for the
                    HXLTMOntologia object.
        [eng-Latn]_
        """
        if vacuum:
            self.crudum = {}
        else:
            self.crudum = ontologia

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

        # print(self.crudum)
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

    def quod_formatum_excerptum(self) -> Dict:
        """Quod fōrmātum excerptum?

        _[eng-Latn]
        Return fōrmātum excerptum (the formatum_excerptum from Ontologia)
        [eng-Latn]_

        Trivia:
            - fōrmātum, https://en.wiktionary.org/wiki/formatus#Latin
            - excerptum, https://en.wiktionary.org/wiki/excerptus#Latin

        Returns:
            Dict: fōrmātum excerptum
        """
        if self.crudum and 'formatum_excerptum' in self.crudum:
            return self.crudum['formatum_excerptum']
        return {}

    def quod_globum_valendum(self) -> Dict:
        """Quod globum valendum?

        _[eng-Latn]
        Return global variables (for Ontologia)
        [eng-Latn]_

        Trivia:
            - globum, https://en.wiktionary.org/wiki/globus#Latin
            - valendum, https://en.wiktionary.org/wiki/valeo#Latin

        Returns:
            Dict: globum valendum
        """
        # TODO: HXLTMOntologia.quod_globum_valendum is a draft.
        # resultatum = {}
        # return resultatum
        return self.crudum

    @staticmethod
    def quid_est_hashtag_circa_conceptum(
            hxl_hashtag: str) -> Union[bool, None]:
        """Quid est hashtag circa +conceptum?

        _[eng-Latn]
        Is this hashtag about concept level?
        [eng-Latn]

        Args:
            hxl_hashtag (str): Hashtag ad textum

        Returns:
            bool:
        """
        # TODO: make this actually read the cor.hxltm.yml. This hardcoded
        #       part is just a quick fix

        if HXLTMOntologia.quid_est_hashtag_circa_linguam(hxl_hashtag):
            return False

        if hxl_hashtag.find('+conceptum') > -1:
            return True

        return False

    @staticmethod
    def quid_est_hashtag_circa_linguam(hxl_hashtag: str) -> bool:
        """Quid est hashtag circa linguam?

        _[eng-Latn]
        Is this hashtag about language term?
        [eng-Latn]

        Args:
            hxl_hashtag (str): Hashtag ad textum

        Returns:
            bool:
        """
        # TODO: make this actually read the cor.hxltm.yml. This hardcoded
        #       part is just a quick fix

        if hxl_hashtag.startswith('#item+rem+i_'):
            return True
        if hxl_hashtag.startswith('#meta+rem+i_'):
            return True
        if re.match(r"\#.*(\+i_).*(\+is_).*", hxl_hashtag):
            # # +i_ +is_
            return True
        return False

    def quod_nomen_breve_de_hxl(self, hxl_hashtag: str) -> str:
        # TODO: make this actually read the cor.hxltm.yml. This hardcoded
        #       part is just a quick fix

        # TODO: some types on cor.hxltm.yml are actually not string, but
        #       lists. This means when asked, we should allow give
        #       hints to let these values be converted
        nomen_breve = ''
        if hxl_hashtag == '#item+conceptum+codicem':
            nomen_breve = 'conceptum_codicem'
        elif hxl_hashtag == '#item+conceptum+dominium':
            nomen_breve = 'conceptum_dominium'
        elif hxl_hashtag == '#item+conceptum+typum':
            nomen_breve = 'conceptum_typum'
        elif hxl_hashtag.startswith('#item+rem+i_'):
            nomen_breve = 'rem__L__'

        return nomen_breve

    def quod_nomen_breve_de_id(self, _hxl_hashtag: str) -> str:
        """TODO quod_nomen_breve_de_id
        """
        return ''

    def in_rem(self, focused_datum: List) -> Type['HXLTMRem']:
        # TODO: make a version of HXLTMRem that supports multiple values
        #       grouped, and already initialized with lanuage tag, not
        #       raw hashtag, since several terms would have
        #       several hashtags
        pass


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

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

>>> HXLTMLinguam('lat-Latn@la-IT@IT')
HXLTMLinguam()

>>> HXLTMLinguam('lat-Latn@la-IT@IT').v()
{'_typum': 'HXLTMLinguam', \
'crudum': 'lat-Latn@la-IT@IT', 'linguam': 'lat-Latn', \
'bcp47': 'la-IT', 'imperium': 'IT', 'iso6391a2': 'la', 'iso6393': 'lat', \
'iso115924': 'Latn'}

>>> HXLTMLinguam('lat-Latn@la-IT@IT', meta={'testum': 123}).v()
{'_typum': 'HXLTMLinguam', '_vanandum_insectum_meta': {'testum': 123}, \
'crudum': 'lat-Latn@la-IT@IT', 'linguam': 'lat-Latn', 'bcp47': 'la-IT', \
'imperium': 'IT', 'iso6391a2': 'la', 'iso6393': 'lat', 'iso115924': 'Latn'}

>>> HXLTMLinguam('lat-Latn@la-IT@IT').a()
'+i_la+i_lat+is_latn+ii_it'

        Kalo Finnish Romani, Latin script (no ISO 2 language)

>>> HXLTMLinguam('rmf-Latn').v()
{'_typum': 'HXLTMLinguam', 'crudum': 'rmf-Latn', \
'linguam': 'rmf-Latn', 'iso6393': 'rmf', 'iso115924': 'Latn'}

        Kalo Finnish Romani, Latin script (no ISO 2 language, so no attr)

>>> HXLTMLinguam('rmf-Latn').a()
'+i_rmf+is_latn'

        Private use language tags: se use similar pattern of BCP 47.
        (https://tools.ietf.org/search/bcp47)

>>> HXLTMLinguam('lat-Latn-x-privatum').a()
'+i_lat+is_latn+ix_privatum'

>>> HXLTMLinguam('lat-Latn-x-privatum-tag8digt').a()
'+i_lat+is_latn+ix_privatum+ix_tag8digt'

        If x-private is only on BCP, we ignore it on HXL attrs.
        Tools may still use this for other processing (like for XLIFF),
        but not for generated Datasets.

>>> HXLTMLinguam(
... 'cmn-Latn@zh-Latn-CN-variant1-a-extend1-x-wadegile-private1').a()
'+i_zh+i_cmn+is_latn'

        To force a x-private language tag, it must be on linguam (first part)
        even if it means repeat. Also, we create attributes shorted by
        ASCII alphabet, as BCP47 would do

>>> HXLTMLinguam(
... 'cmn-Latn-x-wadegile-private1@zh-CN-x-wadegile-private1').a()
'+i_zh+i_cmn+is_latn+ix_private1+ix_wadegile'


>>> HXLTMLinguam(
... 'lat-Latn-x-caesar12-romanum1@la-IT-x-caesar12-romanum1@IT').a()
'+i_la+i_lat+is_latn+ii_it+ix_caesar12+ix_romanum1'

    """

    # Exemplum: lat-Latn@la-IT@IT, arb-Arab@ar-EG@EG
    _typum: InitVar[str] = None  # 'HXLTMLinguam'
    _vanandum_insectum_meta: InitVar[Dict] = None
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

    # def __init__(self, linguam: str, strictum=False, vacuum=False):
    def __init__(self, linguam: str,
                 strictum=False, vacuum=False, meta=None):
        """HXLTMLinguam initiāle

        Args:
            linguam (str): Textum linguam
            strictum (bool, optional): Strictum est?.
                       Trivia: https://en.wiktionary.org/wiki/strictus#Latin
                       Defallo falsum.
            vacuum (bool, optional): vacuum	est?
                       Trivia: https://en.wiktionary.org/wiki/vacuus#Latin.
                       Defallo falsum.
            meta (Dict, optional):
                    Metadatum ad Vēnandum īnsectum.Defallo vacuum.
        """
        # super().__init__()
        self._typum = 'HXLTMLinguam'  # Used only when output JSON
        if meta is not None:
            self._vanandum_insectum_meta = meta
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


class HXLTMRem(HXLTMLinguam):

    # columnam: InitVar[int] = -1
    # valendum_meta: InitVar[Dict] = None
    # datum_typum: InitVar['str'] = None
    hashtag: InitVar[str] = None
    titulum: InitVar[str] = None
    rem: InitVar[str] = None
    annotationem: InitVar[str] = None
    partem_orationis: InitVar[str] = None
    genus_grammaticum: InitVar[str] = None

    # @see https://github.com/PyCQA/pylint/issues/3505
    # pylint: disable=super-init-not-called
    # pylint: disable=non-parent-init-called
    # pylint: disable=too-many-arguments
    def __init__(
        self,
        # columnam: int = -1,
        # columnam_meta: Dict = None,  # HXLTMDatumColumnam.v()
        hashtag: str,
        rem: str = '',
        # titulum: str = '',
        strictum=False
    ):
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

        self.rem = rem

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

        # self.columnam = columnam
        # self.hashtag = hashtag
        # self.titulum = titulum
        # if columnam_meta is not None:
        #     self.valendum_meta = columnam_meta.v(False)


class HXLTMRemCaput(HXLTMLinguam):
    """HXLTMRemCaput HXLTMLinguam et HXLTMDatumCaput metadatum

    TODO: maybe rename to HXLTMDatumCaput

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


class HXLTMTestumAuxilium:
    """HXLTM Testum Auxilium

    _[eng-Latn]
    This class only contains static methods to help test the rest of the huge
    hxltmcli.py file.

    Every time lines start with ">>> python-code-here" this actually is an
    python doctest operation that can be executed with something like

        python3 -m doctest hxlm/core/bin/hxltmcli.py

    So the HXLTMTestumAuxilium contain test helpers.
    [eng-Latn]_

    Trivia:
    - testum, https://en.wiktionary.org/wiki/testum
    - auxilium, https://en.wiktionary.org/wiki/auxilium#Latin
    - disciplīnam manuāle
      - Python doctest
        - https://docs.python.org/3/library/doctest.html
    """

    @staticmethod
    def testum_praefixum(archivum: str = None) -> str:
        """Testum basim

        _[eng-Latn]
        Note: this will try check if the enviroment variable
        HXLTM_TESTUM_BASIM and only fallback to assume the entire
        hdp-toolchain installation (or a fork from
        EticaAI/HXL-Data-Science-file-formats) on local disk.

        Since the hxltmclitm v0.8.2 can be used in standalone more, users
        may want to run tests from other paths (in special if they
        eventually want to propose for the public project)
        [eng-Latn]_

        Trivia:
        - archīvum, https://en.wiktionary.org/wiki/archivum
        - praefīxum, https://en.wiktionary.org/wiki/praefixus#Latin

        Returns:
            str:
                _[eng-Latn]
                Directory containing test files.
                [eng-Latn]_
        """

        # if HDATUM_EXEMPLUM:
        # hxltmtestum = str(Path(
        #     HXLTM_SCRIPT_DIR + '/../../../testum/hxltm').resolve())

        praefixum = os.getenv('HXLTM_TESTUM_BASIM', HXLTM_TESTUM_BASIM_DEFALLO)

        if archivum:
            return praefixum + '/' + archivum

        return praefixum

    @staticmethod
    def datum(
        exemplum_archivum: str = 'hxltm-exemplum-linguam.tm.hxl.csv'
    ) -> List:
        """Crudum HXLTM exemplum datum

        Returns:
            List: Crudum HXLTM exemplum datum
        """
        if not os.path.isfile(exemplum_archivum):
            exemplum_archivum = HXLTMTestumAuxilium.testum_praefixum(
                exemplum_archivum)

        if not os.path.isfile(exemplum_archivum):
            raise RuntimeError(
                'HXLTMTestumAuxilium non-datum [{}]. '
                'Requīsītum: dēfīnītiōnem HXLTM_TESTUM_BASIM. Exemplum:'
                '> HXLTM_TESTUM_BASIM="/home/marcus/testum/" '
                'python3 -m doctest hxltmcli-de-marcus.py'
                ' <'.format(exemplum_archivum))

        hxltm_crudum = []
        with open(exemplum_archivum, 'r') as arch:
            csv_lectorem = csv.reader(arch)
            for rem in csv_lectorem:
                hxltm_crudum.append(rem)
            # hxltm_crudum = arch.read().splitlines()

        # print(hxltm_crudum)
        return hxltm_crudum

    @staticmethod
    def ontologia() -> Dict:
        """HXLTM Ontologia 'cor.hxltm.yml'

        Returns:
            Dict: HXLTM Ontologia
        """
        conf = HXLTMUtil.load_hxltm_options()
        # print(ontologia.keys())
        # print(ontologia)
        # print(HXLTMUtil.load_hxltm_options()['normam'])
        # return HXLTMUtil.load_hxltm_options()
        return HXLTMOntologia(conf)


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

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

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

        Exemplōrum gratiā (et Python doctest, id est, testum automata):

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
    def in_textum_yaml(
            rem: Any,
            formosum: Union[bool, int] = None,
            clavem_sortem: bool = False,
            imponendum_praejudicium: bool = False
    ) -> str:
        """Trānslātiōnem: rem in textum YAML

        Trivia:
          - rem, https://en.wiktionary.org/wiki/res#Latin
          - in, https://en.wiktionary.org/wiki/in#Latin
          - YAML, https://yaml.org/
          - fōrmōsum, https://en.wiktionary.org/wiki/formosus
          - impōnendum, https://en.wiktionary.org/wiki/enforcier#Old_French
          - praejūdicium, https://en.wiktionary.org/wiki/praejudicium#Latin
          - sortem, https://en.wiktionary.org/wiki/sors#Latin
          - clāvem, https://en.wiktionary.org/wiki/clavis#Latin

        Args:
            rem ([Any]): Rem

        Returns:
            [str]: Rem in JSON textum

        Exemplōrum gratiā (et Python doctest, id est, testum automata):

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

        # TODO: in_textum_yaml is a draft.

        # print = json.dumps()

        if formosum is True:
            formosum = 4

        yaml_textum = yaml.dump(
            rem, Dumper=HXLTMTypumYamlDumper,
            encoding='utf-8',
            allow_unicode=not imponendum_praejudicium
        )

        # json_textum = json.dump(
        #     rem,
        #     indent=formosum,
        #     sort_keys=clavem_sortem,
        #     ensure_ascii=imponendum_praejudicium
        # )

        # return yaml_textum
        # @see https://pyyaml.org/wiki/PyYAMLDocumentation
        return str(yaml_textum, 'UTF-8')

    # @staticmethod
    # @see also hxlm/core/io/converter.py
    # def to_yaml(thing: Any) -> str:
    #     """Generic YAML exporter

    #     Returns:
    #         str: Returns an YAML formated string
    #     """

    #     return yaml.dump(thing, Dumper=HXLTMTypumYamlDumper,
    #                     encoding='utf-8', allow_unicode=True)

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

        Exemplōrum gratiā (et Python doctest, id est, testum automata):

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

        Exemplōrum gratiā (et Python doctest, id est, testum automata):

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

        Exemplōrum gratiā (et Python doctest, id est, testum automata):

            >>> HXLTMTypum.magnitudinem_de_textum('Testīs')
            6
        """
        if rem is None:
            return -1

        # TODO: This is a draft. Needs work.
        return len(rem)


class HXLTMTypumYamlDumper(yaml.Dumper):
    """Force identation on pylint, https://github.com/yaml/pyyaml/issues/234
    TODO: check on future if this still need
          (Emerson Rocha, 2021-02-28 10:56 UTC)
    """

    def increase_indent(self, flow=False, *args, **kwargs):  # noqa
        return super().increase_indent(flow=flow, indentless=False)


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

    # def make_args(self, description, hxl_output=True):
    def make_args(self, description, epilog=None, hxl_output=True):
        """Set up parser with default arguments.

        NOTE:
            2021-07-14: Change from libhxl make_args: added epilog option

        @param description: usage description to show
        @param hxl_output: if True (default), include options for HXL output.
        @returns: an argument parser, partly set up.
        """
        if epilog is None:
            parser = argparse.ArgumentParser(description=description)
        else:
            parser = argparse.ArgumentParser(
                description=description,
                formatter_class=argparse.RawDescriptionHelpFormatter,
                epilog=epilog
            )

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
    pyargs_ = hxltmcli.make_args_hxltmcli()

    hxltmcli.execute_cli(pyargs_)


def exec_from_console_scripts():
    hxltmcli_ = HXLTMCLI()
    args_ = hxltmcli_.make_args_hxltmcli()

    hxltmcli_.execute_cli(args_)
