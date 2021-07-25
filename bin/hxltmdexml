#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  hxltmdexml
#
#         USAGE:  Translation Memory eXchange format (TMX): -> HXLTM:
#                     hxltmdexml fontem.tmx objectivum.tm.hxl.csv
#                     cat fontem.tmx | hxltmdexml > objectivum.tm.hxl.csv
#
#                 TBX-Basic: TermBase eXchange (TBX) Basic: -> HXLTM:
#                     hxltmdexml fontem.tbx objectivum.tm.hxl.csv
#                     cat fontem.tbx | hxltmdexml > objectivum.tm.hxl.csv
#
#   DESCRIPTION:  hxltmdexml is an (not feature-by-feature) conversor
#                 from some XML formats to HXLTM tabular working file.
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                     - libhxl (@see https://pypi.org/project/libhxl/)
#                     - defusedxml (https://github.com/tiran/defusedxml)
#                       - pip3 install pyyaml
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:
#                 <@TODO: put additional non-anonymous names here>
#
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v0.2.0
#       CREATED:  2021-07-24 00:04 UTC v0.1.0 de hxl2example
#      REVISION:  2021-07-24 17:49 UTC v0.2.0 hxltmdexml at least read XML
# ==============================================================================
"""hxltmdexml.py: Humanitarian Exchange Language Trānslātiōnem Memoriam de XML

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

# import xml.etree.ElementTree as et
import sys
import os
import logging
import argparse
from pathlib import Path
import re
# import xml.etree.ElementTree as ET
import xml.etree.ElementTree as XMLElementTree

import csv
# import tempfile

from dataclasses import dataclass, InitVar
from typing import (
    Any,
    Dict,
    List,
    Type,
    Union,
)

from functools import reduce
from collections import OrderedDict

import yaml

# @see https://github.com/HXLStandard/libhxl-python
#    pip3 install libhxl --upgrade
# Do not import hxl, to avoid circular imports
import hxl.converters
import hxl.filters
import hxl.io

# @see https://github.com/rspeer/langcodes
# pip3 install langcodes
# import langcodes

__VERSION__ = "v0.2.0"

# _[eng-Latn]
# Note: If you are doing a fork and making it public, please customize
# __SYSTEMA_VARIANS__, even if the __VERSION__ keeps the same
# [eng-Latn]_
__SYSTEMA_VARIANS__ = "hxltmdexml.py;EticaAI+voluntārium-commūne"
# Trivia:
# - systēma, https://en.wiktionary.org/wiki/systema#Latin
# - variāns, https://en.wiktionary.org/wiki/varians#Latin
# - furcam, https://en.wiktionary.org/wiki/furca#Latin
# - commūne, https://en.wiktionary.org/wiki/communis#Latin
# - voluntārium, https://en.wiktionary.org/wiki/voluntarius#Latin

__DESCRIPTIONEM_BREVE__ = """
_[eng-Latn]
hxltmdexml {0} is an (not feature-by-feature) conversor from some
XML formats to HXLTM tabular working file.
[eng-Latn]_"
""".format(__VERSION__)

# tag::epilogum[]
__EPILOGUM__ = """
Exemplōrum gratiā:

Translation Memory eXchange format (TMX): -> HXLTM:
    hxltmdexml fontem.tmx objectivum.tm.hxl.csv

TBX-Basic: TermBase eXchange (TBX) Basic: -> HXLTM:
    hxltmdexml fontem.tbx objectivum.tm.hxl.csv
"""
# end::epilogum[]

# import tempfile


# @see https://github.com/hugapi/hug
#     pip3 install hug --upgrade
# import hug

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


class HXLTMDeXMLCli:
    """
    HXLTMDeXMLCli is a classe to export already HXLated data in the format
    example.
    """

    EXIT_OK = 0
    EXIT_ERROR = 1
    EXIT_SYNTAX = 2

    def __init__(self):
        """
        Constructs all the necessary attributes for the HXLTMDeXMLCli object.
        """
        self.hxlhelper = None
        self.args = None

        self._ontologia: Type['HXLTMOntologia'] = None

    def _initiale(self, pyargs):
        """Trivia: initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        """

        conf = HXLTMUtil.load_hxltm_options(
            pyargs.archivum_configurationem,
            pyargs.venandum_insectum
        )

        self._ontologia = HXLTMOntologia(conf)

    def make_args(self):

        self.hxlhelper = HXLUtils()
        parser = self.hxlhelper.make_args(
            description=__DESCRIPTIONEM_BREVE__,
            epilog=__EPILOGUM__
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
            '--venandum-insectum-est', '--debug',
            help='Enable debug? Extra information for program debugging',
            metavar="venandum_insectum",
            dest="venandum_insectum",
            action='store_const',
            const=True,
            default=False
        )

        self.args = parser.parse_args()

        return self.args

    def execute_cli(
        self, pyargs,
        stdin=STDIN,
        stdout=sys.stdout,
        _stderr=sys.stderr
    ):
        """
        The execute_cli is the main entrypoint of HXLTMDeXMLCli.
        """

        # NOTE: the next lines, in fact, only generate an csv outut. So you
        #       can use as starting point.
        # with self.hxlhelper.make_source(args, stdin) as source, \
        #         self.hxlhelper.make_output(args, stdout) as output:
        #     hxl.io.write_hxl(output.output, source,
        #                      show_tags=not args.strip_tags)

        self._initiale(pyargs)

        fontem_archivum = pyargs.infile if pyargs.infile else stdin
        objectvum_archivum = pyargs.outfile if pyargs.outfile else stdout

        # if pyargs.infile:
        #     fontem_archivum = pyargs.infile
        # else:
        #     # print('stdin')
        #     dexml = HXLTMdeXML(stdin)

        dexml = HXLTMdeXML(
            self._ontologia, fontem_archivum, objectvum_archivum)

        return dexml.in_archivum()

        # dexml.testum()

        # return self.EXIT_OK

# hxltmdexml resultatum/hxltm-exemplum-linguam.tmx
# hxltmdexml resultatum/hxltm-exemplum-linguam.tbx
# hxltmdexml /workspace/data/IATE_download/IATE_export.tbx
# hxltmdexml resultatum/hxltm-exemplum-linguam.por-Latn--spa-Latn.obsoletum.xlf
# hxltmdexml resultatum/schemam-un-htcds_eng-Latn--por-Latn.obsoletum.xlf
# This one we need very soom (need to import back MateCat)
# hxltmdexml resultatum/schemam-un-htcds_eng-Latn--por-Latn.DONE.obsoletum.xlf


class HXLTMdeXML:
    """HXLTM de  XML

    Trivia:
        - HXLTM:
        - HXLTM, https://hdp.etica.ai/hxltm
            - HXL, https://hxlstandard.org/
            - TM, https://www.wikidata.org/wiki/Q333761

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
        - fōrmātum, https://en.wiktionary.org/wiki/formatus#Latin
        - fontem, https://en.wiktionary.org/wiki/fons#Latin
        - 'id est', https://en.wiktionary.org/wiki/id_est
        - initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        - locum, https://en.wiktionary.org/wiki/locum#Latin
        - objectīvum, https://en.wiktionary.org/wiki/objectivus#Latin
        - resultātum, https://en.wiktionary.org/wiki/resultatum
        - rādīcem, https://en.wiktionary.org/wiki/radix#Latin

    Speciāle verbum in HXLTM:
        - 'Exemplōrum gratiā (et Python doctest, id est, testum automata)'
            - Exemplōrum gratiā
              - https://en.wikipedia.org/wiki/List_of_Latin_phrases_(full)
            - 'Python doctest' (non Latīnam)
                -https://docs.python.org/3/library/doctest.html
    """

    # Trivia:
    # - exitum, https://en.wiktionary.org/wiki/exitus#Latin
    # - errōrem, https://en.wiktionary.org/wiki/error#Latin
    # - syntaxim, https://en.wiktionary.org/wiki/syntaxis#Latin
    # - corrēctum, https://en.wiktionary.org/wiki/correctus#Latin
    #     - correct (de Anglicum)
    #         - OK (de anglicum),
    #            - https://en.wiktionary.org/wiki/OK#English
    #            - https://en.wiktionary.org/wiki/oll_korrect#English
    EXITUM_CORRECTUM = 0
    EXITUM_ERROREM = 1
    EXITUM_SYNTAXIM = 2

    # import xml.etree.ElementTree as XMLElementTree
    # arborem: Type['XMLElementTree'] = None
    arborem = None
    arborem_radicem = None
    # arborem: Dict = None
    xml_typum = None
    # referēns, https://en.wiktionary.org/wiki/referens#Latin
    xml_referens = None
    in_formatum = None

    # iterātiōnem, https://en.wiktionary.org/wiki/iteratio#Latin

    iteratianem = None

    def __init__(
        self,
        ontologia: Type['HXLTMOntologia'],
        fontem_archivum=sys.stdin.buffer,
        objectvum_archivum=sys.stdout
    ):
        """__init__

        Args:
            ontologia (HXLTMOntologia): ontologia
            fontem_archivum (): fomtem archīvum
            objectvum_archivum (): objectīvum archīvum
        """

        self._ontologia = ontologia

        if fontem_archivum:
            self.fontem_archivum = fontem_archivum
        else:
            self.fontem_archivum = sys.stdin.buffer

        if objectvum_archivum:
            self.objectvum_archivum = objectvum_archivum
        else:
            self.objectvum_archivum = sys.stdout

        self.in_formatum = XMLInFormatumHXLTM(
            self._ontologia
        )

        # TODO: test what happens if input is not XML or was compressed
        #       them deal with message errors for non-XML already on
        #       initialization
        self.iteratianem = XMLElementTree.iterparse(
            source=self.fontem_archivum,
            events=('start', 'end')
        )

        # # This load all on memory. Bad
        # self.arborem = XMLElementTree.parse(self.fontem_archivum)
        # self.arborem_radicem = self.arborem.getroot()

        # print(self.arborem_radicem)

        self._initiale()
        # self.xml_typum = self._ontologia.quod_xml_typum(
        #     self.arborem_radicem.tag,
        #     self.arborem_radicem.attrib
        # )

        # self.xml_referens = self._ontologia.quod_xml_typum_tag(
        #     self.xml_typum['hxltm_normam']
        # )

        # self.in_formatum = XMLInFormatumHXLTM(
        #     self._ontologia
        #     fontem_archivum,
        #     objectvum_archivum
        # )

        # self.in_formatum = XMLInFormatumHXLTM(
        #     self._ontologia
        #     # fontem_archivum,
        #     # objectvum_archivum
        # )
        # self.in_formatum.definitionem_linguam('pt')
        # self.in_formatum.definitionem_linguam('en')
        # self.in_formatum.definitionem_linguam('es')
        # self.in_formatum.definitionem_linguam('por-Latn@pt')
        # self.in_formatum.definitionem_linguam('eng-Latn@en')
        # self.in_formatum.definitionem_linguam('spa-Latn@es')

    def _initiale(self):
        """initiāle, https://en.wiktionary.org/wiki/initialis#Latin
        """

        # print(self.iteratianem)
        # ēventum, https://en.wiktionary.org/wiki/eventus#Latin
        # nōdum, https://en.wiktionary.org/wiki/nodus#Latin
        _eventum, nodum = next(self.iteratianem)

        # print('_initiale {0}, {1}, {2}'.format(
        #     _eventum, nodum, nodum.attrib))

        self.xml_typum = self._ontologia.quod_xml_typum(
            nodum.tag,
            nodum.attrib
        )

        self.xml_referens = self._ontologia.quod_xml_typum_tag(
            self.xml_typum['hxltm_normam']
        )

        _eventum2, nodum2 = next(self.iteratianem)

        # print('_initiale2 {0}, {1}'.format(_eventum2, nodum2))

        # print('zzzetas', self.xml_typum)

    def de_tbx(self):
        # pass
        # https://www.tbxinfo.net/validating-a-tbx-file/
        raise NotImplementedError('TODO de_tbx')
        # return self.EXITUM_CORRECTUM

    def de_xml(self):
        raise NotImplementedError('XML {0}'.format(str(self.xml_typum)))

    def de_tmx(self):
        """de_tmx De Translation Memory eXchange (TMX)

        Trivia:
            - Normam: https://www.gala-global.org/tmx-14b
            - DTD: https://www.gala-global.org/sites/default
                   /files/migrated-pages/docs/tmx14%20%281%29.dtd
        Returns:
            [int]:
        """

        # tmx_body = self.arborem_radicem.find('body')
        # print('tmx_body', tmx_body)
        # print('hxltmcsv', self.in_formatum.in_caput())

        raise NotImplementedError('TODO de_tmx')
        return self.EXITUM_CORRECTUM

    def de_xliff(self):

        raise NotImplementedError('TODO de_xliff')
        return self.EXITUM_CORRECTUM

    def de_xliff_obsoletum(self):

        raise NotImplementedError('TODO de_xliff_obsoletum')
        return self.EXITUM_CORRECTUM

    def quod_archivum_typum(self):
        """quod_archivum_typum [summary]

        Trivia:
        - quod, https://en.wiktionary.org/wiki/qui#Latin
        - archīvum, https://en.wiktionary.org/wiki/archivum
        - typum, https://en.wiktionary.org/wiki/typus#Latin

        Returns:
            [str]: archīvum typum
        """
        resultatum = 'xml'
        # todo: implement other checks
        return resultatum

    # def quod_archivum_xml_basim(self) -> Dict:
    #     resultatum = {}

    #     # print(self.arborem_radicem)
    #     # print(self.arborem_radicem.tag)
    #     # print(self.arborem_radicem.attrib)

    #     print(self._ontologia.quod_xml_typum(
    #         self.arborem_radicem.tag,
    #         self.arborem_radicem.attrib
    #     ))
    #     return resultatum

    def in_archivum(self):
        """in_archivum archīvum fontem in archīvum objectīvum

        Returns:
            [int]: EXITUM_CORRECTUM, EXITUM_ERROREM aut EEXITUM_SYNTAXIM
        """
        return self.in_archivum_formatum_hxltm()

    def in_archivum_formatum_hxltm(self):
        """in_archivum archīvum fontem in archīvum objectīvum fōrmātum HXLTM

        Returns:
            [int]: EXITUM_CORRECTUM, EXITUM_ERROREM aut EEXITUM_SYNTAXIM
        """
        # self.quod_archivum_xml_basim()
        print('self.xml_typum', self.xml_typum)
        if self.xml_typum and 'typum' in self.xml_typum:
            if self.xml_typum['typum'] == 'TBX':
                return self.de_tbx()
            if self.xml_typum['typum'] == 'TMX':
                return self.de_tmx()
            if self.xml_typum['typum'] == 'XLIFF':
                if 'version' in self.xml_typum:
                    if self.xml_typum['version'].startswith('2.'):
                        return self.de_xliff()
                    if self.xml_typum['version'].startswith('1.'):
                        return self.de_xliff_obsoletum()
                return self.de_xliff()
            if self.xml_typum['typum'] == 'XML':
                return self.de_xml()

            return self.de_xml()
        # self.testum()

        return self.EXITUM_ERROREM

    def testum(self):

        tree = XMLElementTree.parse(self.fontem_archivum)
        # tree = ET.parse(self.archivum)
        root = tree.getroot()

        # print(root.tag)

        self.xliff_obsoletum(root)
        self.xliff_testum2()

    def xliff_obsoletum(self, root):
        print('oi')

        print(root.findall('./{*}file/{*}body/{*}trans-unit'))
        print('')

    def xliff_testum2(self):
        # @see https://docs.python.org/3/library
        #      /xml.etree.elementtree.html#elementtree-xpath
        crudum = """<?xml version="1.0"?>
<actors xmlns:fictional="http://characters.example.com"
        xmlns="http://people.example.com">
    <actor>
        <name>John Cleese</name>
        <fictional:character>Lancelot</fictional:character>
        <fictional:character>Archie Leach</fictional:character>
    </actor>
    <actor>
        <name>Eric Idle</name>
        <fictional:character>Sir Robin</fictional:character>
        <fictional:character>Gunther</fictional:character>
        <fictional:character>Commander Clement</fictional:character>
    </actor>
</actors>
        """

        root = XMLElementTree.fromstring(crudum)

        print(root.findall("."))

        print(root.findall("./country/neighbor"))


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
         - valōrem, https://en.wiktionary.org/wiki/valor#Latin
         - verbosum, https://en.wiktionary.org/wiki/verbosus#Latin

        Args:
            _verbosum (bool): Verbosum est? Defallo falsum.

        Returns:
            [Dict]: Python objectīvum
        """
        return self.__dict__


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


#>>> ontologia.quod_rem_statum()
{'accuratum': None, 'crudum': [], 'crudum_originale': [], \
'XLIFF': 'initial', 'UTX': 'provisional'}


#>>> ontologia.quod_rem_statum(10, 'lat_rem_finale')
{'accuratum': 10, 'crudum': [], 'crudum_originale': ['lat_rem_finale'], \
'XLIFF': 'initial', 'UTX': 'provisional'}
#>>> ontologia.\
    quod_rem_statum(10, 'lat_rem_finale|UTX_provisional|XLIFF_initial')
{'accuratum': 10, 'crudum': [], 'crudum_originale': \
['lat_rem_finale', 'UTX_provisional', 'XLIFF_initial'], \
'XLIFF': 'initial', 'UTX': 'provisional'}


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

    def quod_aliud(self, aliud_typum: str, aliud_valorem: str) -> Dict:
        """Quod Aliud?

        Requīsītum:
            - *.hxmtm.yml:ontologia_aliud
            - *.hxmtm.yml:ontologia_aliud_familiam

        Args:
            aliud_typum (str):
                aliud valōrem
            aliud_valōrem (str):
                aliud valōrem

        Returns:
            Dict: Python Dict, de *.hxltm.yml

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

>>> ontologia = HXLTMTestumAuxilium.ontologia()
>>> 'UTX_adverb' in ontologia.\
    quod_aliud('partem_orationis', 'lat_adverbium')['aliud']
True

>>> ontologia.\
    quod_aliud('partem_orationis', 'lat_adverbium')['codicem_TBX']
'adverb'
        """
        if aliud_typum not in self.crudum['ontologia_aliud'] or \
                aliud_valorem not in \
                self.crudum['ontologia_aliud'][aliud_typum]:
            return None
        resultatum = self.crudum['ontologia_aliud'][aliud_typum][aliud_valorem]

        if '_aliud' in resultatum and resultatum['_aliud']:
            resultatum['aliud'] = \
                list(map(str.strip, resultatum['_aliud'].split('|')))
        else:
            # _[eng-Latn]Alias without aliases to other types?[eng-Latn]_
            resultatum['aliud'] = []

        aliud_familiam = self.crudum['ontologia_aliud_familiam'].keys()
        # print('aliud_familiam', aliud_familiam)
        for familiam in aliud_familiam:
            if aliud_valorem.startswith(familiam + '_'):
                resultatum['_aliud_familiam'] = familiam

            for aliud in resultatum['aliud']:
                # _[eng-Latn]
                # Only create a codicem_TTTT if *.hxmtl.yml already not have
                # one.
                # [eng-Latn]_

                if aliud.startswith(familiam + '_') and \
                        not 'codicem_' + familiam in resultatum:
                    resultatum['codicem_' + familiam] = \
                        aliud.replace(familiam + '_', '')

        # print('   > quod_aliud resultatum', resultatum)
        return resultatum

    def quod_aliud_de_multiplum(
        self,
        aliud_typum: str,
        aliud_valorem_multiplum: Union[List[str], str]
    ) -> Dict:
        """Quod Aliud de multiplum optiōnem?

        _[eng-Latn]
        HXLTM (when not working with RAW JSON) allows make simpler short
        aliases from multiple standards, like:
            'UTX_properNoun | TBX_noun'
        In such way that it actually allows to make inferences about other
        types implicitly even when some things are obvious
        (like a 'proper noun' must be a 'noun').

        When a field alredy not explicitly define an exact value, we
        'try smart inferences', but if the initial input do already have
        something wrong (but more specific for an output format) this
        method will not override the more explicity alias.

        Advanced checks (like bad tagging) should be done in another step.
        [eng-Latn]_

        Requīsītum:
            - *.hxmtm.yml:ontologia_aliud
            - *.hxmtm.yml:ontologia_aliud_familiam

        Args:
            aliud_typum (str):
                aliud valōrem
            aliud_valorem_multiplum (Union(List[str], str)):
                aliud valōrem

        Returns:
            Dict: Python Dict, de *.hxltm.yml

        Exemplōrum gratiā (et Python doctest, id est, testum automata):

>>> ontologia = HXLTMTestumAuxilium.ontologia()

>>> testum_I = ontologia.quod_aliud_de_multiplum(
...    'rem_statum',
...    ['lat_rem_finale', 'UTX_provisional', 'XLIFF_initial'])
>>> testum_I
{'_conjecturum': ['TBX_preferred'], '_crudum_originale': \
['lat_rem_finale', 'UTX_provisional', 'XLIFF_initial'], \
'codicem_TBX': 'preferred', \
'codicem_UTX': 'provisional', \
'codicem_XLIFF': 'initial', \
'codicem_lat': 'rem_finale'}


>>> testum_II = ontologia.quod_aliud_de_multiplum(
...    'rem_statum',
...    ['lat_rem_finale'])

>>> testum_II
{'_conjecturum': ['TBX_preferred', 'UTX_approved', 'XLIFF_final'], \
'_crudum_originale': ['lat_rem_finale'], \
'codicem_TBX': 'preferred', \
'codicem_UTX': 'approved', \
'codicem_XLIFF': 'final', \
'codicem_lat': 'rem_finale'}

        """
        if not aliud_valorem_multiplum or len(aliud_valorem_multiplum) == 0:
            return None

        if isinstance(aliud_valorem_multiplum, str):
            aliud_valorem_multiplum = list(map(
                str.strip,
                aliud_valorem_multiplum.split('|')))

        # aliud_valorem_multiplum.sort(key=str.lower)

        resultatum = {
            '_crudum_originale': aliud_valorem_multiplum,
            '_conjecturum': []
        }
        aliud_familiam = set(
            sorted(self.crudum['ontologia_aliud_familiam'].keys(),
                   key=str.lower)
        )

        aliud_secundum = set()
        for item in aliud_valorem_multiplum:
            rem = self.quod_aliud(aliud_typum, item)
            if rem is None or '_aliud_familiam' not in rem:
                # print('not in rem')
                continue
            resultatum['codicem_' + rem['_aliud_familiam']] = \
                rem['codicem_' + rem['_aliud_familiam']]
            aliud_familiam.discard(rem['_aliud_familiam'])
            if 'aliud' in rem and len(rem['aliud']) > 0:
                aliud_secundum.update(rem['aliud'])
            # print(rem['_aliud_familiam'])
            # aliud.append(rem)

        if len(aliud_secundum) > 0:
            # print('>0', aliud_secundum)
            for item in aliud_secundum:
                rem = self.quod_aliud(aliud_typum, item)
                if rem is None or '_aliud_familiam' not in rem:
                    continue
                if 'codicem_' + rem['_aliud_familiam'] in resultatum:
                    # print('iam exsistit: ', item)
                    continue

                # print('conjectūrum!: ', item)
                resultatum['_conjecturum'].append(item)
                resultatum['codicem_' + rem['_aliud_familiam']] = \
                    rem['codicem_' + rem['_aliud_familiam']]
                resultatum['_conjecturum'].sort(key=str.lower)

        resultatum = dict(OrderedDict(sorted(resultatum.items())))

        # print('')
        # print('resultatum', resultatum)
        # print('')

        return resultatum

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

    def quod_globum_valorem(self) -> Dict:
        """Quod globum valorem?

        _[eng-Latn]
        Return global variables (for Ontologia)
        [eng-Latn]_

        Trivia:
            - globum, https://en.wiktionary.org/wiki/globus#Latin
            - valōrem, https://en.wiktionary.org/wiki/valor#Latin

        Returns:
            Dict: globum valorem
        """
        # TODO: HXLTMOntologia.quod_globum_valorem is a draft.
        # resultatum = {}
        # return resultatum
        return self.crudum

    def quod_rem_statum(self,
                        statum_rem_accuratum: int = None,
                        statum_rem_textum: str = '',
                        rem_json: Union[str, Dict] = None
                        ) -> Dict:
        """[summary]

        Args:
            statum_rem_accuratum (int, optional):
                Statum rem accūrātum. Defallo Python None.
            statum_rem_textum (str, optional):
                Statum rem textum. Defallo vacuum textum.

        Returns:
            Dict: [description]
        """
        # TODO: make the defaults configurable

        resultatum = {
            # 1-10, TBX uses it
            'accuratum': statum_rem_accuratum,
            # 'crudum': [],
            'crudum_originale': [],
            # initial, translated, reviewed, final
            'XLIFF': 'initial',
            # provisional, approved, '', non-standard, rejected, obsolete
            'UTX': 'provisional'
        }
        if rem_json:
            raise NotImplementedError('quod_rem_statum rem_json')

        if statum_rem_textum != '':
            crudum_originale = statum_rem_textum.split('|')
            resultatum['crudum_originale'] = crudum_originale

        # scālam, https://en.wiktionary.org/wiki/scala#Latin

        # TODO: implement this check
        return resultatum

    def quod_xml_typum(self,
                       radicem_tag: str,
                       radicem_attributum: dict = None
                       ) -> Dict:
        """quod_xml_typum Quod XML typum est?

        _[eng-Latn]
        TODO: make this method actually load the references from the
        *.hxltm.yml, so the users could have at least some freedom
        (as they already have when exporting) but now to import.
        [eng-Latn]_

        Args:
            radicem_tag (str):
                XML rādīcem (textum)
            radicem_attributum (dict, optional):
                HXL attribūtum de rādīcem. Defallo Python None

        Returns:
            Dict: typum, versiōnem, variāns
        """
        resultatum = {
            'hxltm_normam': '',
            'typum': 'XML',
            # XLIFF 2.x may provide srcLang / trgLang on <xliff>
            'linguam_fontem': '',
            'linguam_objectivum': '',
            'radicem_attributum_crudum': {},
            # variāns, https://en.wiktionary.org/wiki/varians#Latin
            'varians': '',
            'versionem': -1
        }

        # def hxl_attr(clavem):
        #     if not clavem or clavem.find('}') == -1:
        #         return clavem
        #     return clavem.split('}')[-1]

        attributum = radicem_attributum if radicem_attributum else {}
        if radicem_attributum:
            for clavem in list(radicem_attributum):
                clavem_basim = HXLTMUtil.xml_clavem_breve(clavem)
                if clavem_basim != clavem:
                    attributum[clavem_basim] = radicem_attributum[clavem]

            resultatum['radicem_attributum_crudum'] = \
                radicem_attributum
        radicem_tag_basim = HXLTMUtil.xml_clavem_breve(radicem_tag)

        # print('attributum', attributum)

        # print('quod_xml_typum', radicem_tag, radicem_attributum,
        # resultatum, radicem_tag_basim)
        if radicem_tag_basim == 'tmx':
            resultatum['hxltm_normam'] = 'TMX'
            resultatum['typum'] = 'TMX'
            resultatum['versionem'] = '1.4'
        if radicem_tag_basim == 'martif':
            resultatum['hxltm_normam'] = 'TBX-Basim'
            resultatum['typum'] = 'TBX'
            resultatum['versionem'] = 'TBX-Basic'
        if radicem_tag_basim == 'tbx':
            resultatum['hxltm_normam'] = 'TBX-IATE'
            resultatum['typum'] = 'TBX'
            resultatum['versionem'] = 'TBX-IATE'
        if radicem_tag_basim == 'xliff':
            resultatum['typum'] = 'XLIFF'
            resultatum['versionem'] = '2.0'

        if 'version' in attributum:
            resultatum['versionem'] = attributum['version']

        if 'type' in attributum:
            resultatum['varians'] = attributum['type']

        if 'srcLang' in attributum:
            resultatum['linguam_fontem'] = attributum['srcLang']

        if 'trgLang' in attributum:
            resultatum['linguam_objectivum'] = attributum['trgLang']

        return resultatum

    def quod_xml_typum_tag(
        self,
        hxltm_normam: str
    ) -> Dict:
        """quod_xml_typum Quod XML typum est?

        _[eng-Latn]
        TODO: make this method actually load the references from the
        *.hxltm.yml, so the users could have at least some freedom
        (as they already have when exporting) but now to import.
        [eng-Latn]_

        Args:
            hxltm_normam (str):
                HXLTM normam (textum)

        Returns:
            Dict: typum, versiōnem, variāns
        """
        resultatum = {
            'conceptum': '',
            'conceptum_attributum': 'id',
            'fontem': '',
            'terminum': '',
            'objectivum': ''
        }

        if hxltm_normam == 'TBX-Basim':
            # <termEntry id="L10N_ego_codicem">
            #     <langSet xml:lang="la">
            #         <tig>
            #           <term>lat-Latn</term>
            #         </tig>
            #     </langSet>
            # </termEntry>
            resultatum['conceptum'] = 'termEntry'
            resultatum['terminum'] = 'langSet/tig/term'

        if hxltm_normam == 'TBX-IATE':
            # <conceptEntry id="254003">
            #     <descrip type="subjectField">linguistics</descrip>
            #     <langSec xml:lang="es">
            #         <termSec>
            #             <term>acto de habla indirecto</term>
            #             <termNote type="termType">fullForm</termNote>
            #             <descrip type="reliabilityCode">1</descrip>
            #         </termSec>
            #     </langSec>
            # </conceptEntry>
            resultatum['conceptum'] = 'conceptEntry'
            resultatum['terminum'] = 'langSec/termSec/term'
        if hxltm_normam == 'TMX':
            # <tu tuid="L10N_ego_codicem">
            #   <tuv xml:lang="la">
            #     <seg>lat-Latn</seg>
            #   </tuv>
            # </tu>
            resultatum['conceptum'] = 'tu'
            resultatum['conceptum_attributum'] = 'tuid'  # Non 'id'
            resultatum['terminum'] = 'tuv/seg'

        if hxltm_normam == 'XLIFF':
            # <unit id="L10N_ego_scriptum_nomen">
            #     <segment state="final">
            #         <source>Alfabeto latino</source>
            #         <target>Alfabeto latino</target>
            #     </segment>
            # </unit>
            resultatum['conceptum'] = 'unit'
            resultatum['fontem'] = 'segment/source'
            resultatum['objectivum'] = 'segment/target'

        if hxltm_normam == 'XLIFF-Obsoletum':
            # <trans-unit id="L10N_ego_codicem" translate="no" approved="yes">
            #     <source>por-Latn</source>
            #     <target state="final">spa-Latn</target>
            #     <note annotates="source" priority="2">
            #     _    [eng-Latn]eng-Latn[eng-Latn]_
            #     </note>
            # </trans-unit>
            resultatum['conceptum'] = 'trans-unit'
            resultatum['fontem'] = 'source'
            resultatum['objectivum'] = 'target'

        return resultatum

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

        if hxl_hashtag == '#meta+conceptum+codicem+alternativum':
            nomen_breve = 'codicem_alternativum'

        elif hxl_hashtag == '#item+conceptum+dominium':
            nomen_breve = 'conceptum_dominium'

        elif hxl_hashtag == '#meta+item+url+list':
            # conceptum.referens_situs_interretialis
            nomen_breve = 'referens_situs_interretialis'

        elif hxl_hashtag == '#item+conceptum+typum':
            nomen_breve = 'conceptum_typum'

        elif hxl_hashtag.startswith('#status+rem+accuratum+i_'):
            nomen_breve = 'accuratum__L__'

        elif hxl_hashtag.startswith('#status+rem+textum+i_'):
            nomen_breve = 'statum_rem_textum__L__'

        elif hxl_hashtag.startswith('#status+rem+json+i_'):
            nomen_breve = 'statum_rem_json__L__'

        elif hxl_hashtag.startswith('#item+rem+i_'):
            nomen_breve = 'rem__L__'

        return nomen_breve

    def quod_nomen_breve_de_id(self, _hxl_hashtag: str) -> str:
        """TODO quod_nomen_breve_de_id
        """
        return ''

    # def in_rem(self, focused_datum: List) -> Type['HXLTMRem']:
    #     # TODO: make a version of HXLTMRem that supports multiple values
    #     #       grouped, and already initialized with lanuage tag, not
    #     #       raw hashtag, since several terms would have
    #     #       several hashtags
    #     pass


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
                rawstr += '+i_' + bcp47.lower()
            if iso6393:
                rawstr += '+i_' + iso6393.lower()
            if iso115924:
                rawstr += '+is_' + iso115924.lower()
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
            >>> HXLTMUtil.iso115924_from_hxlattrs('#item+i_ar+i_arb+is_ARaB')
            'Arab'

            >>> HXLTMUtil.iso115924_from_hxlattrs('#item+i_pt')
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
                    # return k.replace('is_', '')
                    return k.replace('is_', '').capitalize()
                    # return k.replace('is_', '').lower()

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
            'lat-Latn@la'
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

    @staticmethod
    def xml_clavem_breve(clavem):
        """xml_clavem_breve XML clāvem non-NS

        Args:
            clavem ([str]): XML clāvem

        Returns:
            [str]:

            >>> HXLTMUtil.xml_clavem_breve(
            ...    '{urn:oasis:names:tc:xliff:document:2.0}version')
            'version'
        """
        if not clavem or clavem.find('}') == -1:
            return clavem
        return clavem.split('}')[-1]


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


class XMLInFormatumHXLTM():
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
        2021-07-24

    Revisions:

    License:
        Public Domain

    Args:
        ontologia (HXLTMOntologia):
            HXLTMASA objectīvum
        fontem_archivum (str):
        objectvum_archivum (str):
    """

    # # # ontologia/cor.hxltm.yml clāvem nomen
    # # ONTOLOGIA_FORMATUM = ''

    # # ontologia/cor.hxltm.yml basim extēnsiōnem
    # ONTOLOGIA_NORMAM: str = ''

    # # Trivia: speciāle, https://en.wiktionary.org/wiki/specialis#Latin
    # ontologia_normam_speciale = ''

    # hxltm_asa
    # ontologia

    linguam_collectionem = []
    linguam_fontem = None
    linguam_objectivum = None

    # TODO: remove this gambiarra
    temporary_fix = {
        'pt': 'por-Latn@pt',
        'en': 'eng-Latn@en',
        'es': 'spa-Latn@es',
        'eo': 'epo-Latn@eo',
        'sk': 'slk-Latn@sk',
    }

    # __commune_asa: InitVar[Type['HXLTMASA']] = None

    # @see https://docs.python.org/3/library/logging.html
    # @see https://docs.python.org/pt-br/dev/howto/logging.html

    def __init__(
        self,
        ontologia: Type['HXLTMOntologia']
    ):
        """__init__

        Args:
            ontologia (HXLTMOntologia): ontologia
        """

    def definitionem_linguam(
            self, linguam: str) -> Type['XMLInFormatumHXLTM']:
        """dēfīnītiōnem linguam

        _[eng-Latn]
        NOTE: all the languages need to be know upfront (even it if means)
        peak part of the XML file) to be able to generate output.

        Add new languages that were not defined will not work.

        Add a new language after the heading files was created, will also
        generate a CSV-like file with more columns (id est, invalid).
        [eng-Latn]_

        Returns:
            [XMLInFormatumHXLTM]:
        """

        if len(linguam) == 2 and linguam in self.temporary_fix:
            linguam = self.temporary_fix[linguam]
            # if linguam

        self.linguam_collectionem.append(
            HXLTMLinguam(linguam)
        )
        return self

    def definitionem_linguam_fontem(
            self, linguam: str) -> Type['XMLInFormatumHXLTM']:
        """dēfīnītiōnem linguam fontem

        Returns:
            [XMLInFormatumHXLTM]:
        """

        if len(linguam) == 2 and linguam in self.temporary_fix:
            linguam = self.temporary_fix[linguam]

        self.linguam_fontem = HXLTMLinguam(linguam)
        return self

    def definitionem_linguam_objectivum(
            self, linguam: str) -> Type['XMLInFormatumHXLTM']:
        """dēfīnītiōnem linguam objectivum

        Returns:
            [XMLInFormatumHXLTM]:
        """

        if len(linguam) == 2 and linguam in self.temporary_fix:
            linguam = self.temporary_fix[linguam]

        self.linguam_objectivum = HXLTMLinguam(linguam)
        return self

    def in_caput(self):
        resultatum = []
        resultatum.append('#item+conceptum+codicem')
        for linguam in self.linguam_collectionem:
            resultatum.append('#item+rem' + linguam.a())
            resultatum.append('#status+rem+accuratum' + linguam.a())
        return resultatum

    def in_lineam(self, conceptum_codicem: str, data: Dict):
        resultatum = [conceptum_codicem, data]
        return resultatum


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

# # data = []
# # # path = 'resultatum/hxltm-exemplum-linguam.tmx'
# # # path = 'resultatum/hxltm-exemplum-linguam.tbx'
# path = '/workspace/data/IATE_download/IATE_export.tbx'

# print('oi 0', path)
# with open(path) as xml_file:
#     for event, elem in XMLElementTree.iterparse(
#             source=xml_file, events=('start', 'end')):
#         # Must compare tag to qualified name
#         # if elem.tag == et.QName(ixid_uri, 'Journey'):
#         clavem_breve = HXLTMUtil.xml_clavem_breve(elem.tag)
#         print('event, tag', event, elem.tag,
#               HXLTMUtil.xml_clavem_breve(elem.tag))
#         if clavem_breve == 'conceptEntry':
#             print('okay', elem.attrib)
#             # print(elem.attrib['uid'])
#             # c.executemany('insert into foo values(?, ?, ?)',
#             #     [
#             #         (elem.attrib['uid'],
#             #         extract_local_tag(child.tag),
#             #         child.attrib.get('tpl', None))
#             #         for child in elem
#             #     ])
#             # conn.commit()
#             # Note: only clears <Journey> elements and their children.
#             # There is a memory leak of any elements not children of
#             # <Journey>
#             elem.clear()
# print('oi 1', path)
# # print(data)


if __name__ == "__main__":

    hxltmdexml = HXLTMDeXMLCli()
    args_ = hxltmdexml.make_args()

    hxltmdexml.execute_cli(args_)
