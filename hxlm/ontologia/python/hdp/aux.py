"""hxlm.ontologia.python.hdp.aux


- aux (Latin: Auxilium):
    - Data that needs to be exchanged when manipulating data are described
      here.
    - This module do not represents direct implementation of some parts of
      VKG/LKGs. But may show off a lot when investigating errors.

Trivia:
  - aux.py
    - auxilium: https://en.wiktionary.org/wiki/auxilium#Latin
  - "auxilium", Latin, Etymology:
    - From augeō (“spread, honor, promote”).
  - "trivium"
    - 'a crossroads or fork where three roads meet'
    - https://en.wiktionary.org/wiki/trivium#Latin

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from dataclasses import dataclass, field, InitVar
# from dataclasses import dataclass, field
from typing import (
    Any,
    List,
    Tuple,
    Type,
    # Union
)

from hxlm.ontologia.python.hdp.abst import AbstAux

from hxlm.ontologia.python.systema import (
    EntryPointType,
    L10NContext
)


@dataclass
class AuxHDPDesc(AbstAux):
    """HDP Dēscrīptiōnem Auxilium, HDP description helper
    """

    aup_loader: Type['AuxLoadPolicy'] = None
    """Acceptable Use Policy for load HDP file projects (not the data)

    Note that each HDP file can have individual Acceptable Use Policy. This
    item is mostly used by advanced users who want to automate too much (not
    even need human intervention) or they want to share snippets with less
    experienced people while somewhat tolerating the person dealing HDP files
    from several places
    """

    # entrypoint: Any = None
    # """The entrypoint"""
    trivium: Any = None
    """The entrypoint of the HDP resource

    Trivia:
      -  trivium: latin of 'a crossroads or fork where three roads meet'
    """

    # l10n: L10NContext = field(repr=False)
    # """Localization information"""

    # log: InitVar[list] = []
    # """Raw message log. Either used for debug or explain errors"""

    log_okay: InitVar[list] = []
    """Short, temporary most recent log if not okay"""

    # okay: bool = True
    # """attr.okay indicates if this is, at bare minimum, working
    # It does not mean perfect or great. But is opposite of bad. The perfect
    # example is okay = True when something goes bad but the program know how to
    # recover.
    # """

    # TODO: organize these next fields. Not all are necessary from HDPProject
    hdpraw: InitVar[List[Type['HDPRaw']]] = []
    """HDPRaw is, informally speaking it is a crude representation of
    information in a disk file that MAY be an single hsilo or not.
    """

    hsilos: InitVar[List[Type['HSiloWrapper']]] = []
    """List of individual HSilo (one physical file could have multiple)"""


@dataclass(init=False, eq=False)
class AuxHDPExplanare(AbstAux):
    """HDP Explanare Auxilium, "HDP (complex/debug) explainer helper"

    This is similar to AuxHDPDesc, but focused when used, focus on give more
    details, in special when things go wrong.

    Trivia:
    - "explānāre":
      - https://en.wiktionary.org/wiki/explano#Latin
      - https://en.wiktionary.org/wiki/explanare#Latin
    """

    # _entrypoint: Any = None
    # """The entrypoint"""
    # entrypoint: Any = None
    # """The entrypoint"""
    _trivium: Any = None
    """The entrypoint of the HDP resource

    Trivia:
      -  trivium: latin of 'a crossroads or fork where three roads meet'
    """

    _hdpdescriptionem: AuxHDPDesc = field(repr=False)
    """A HDPDescriptionem with full details of the project"""

    _l10n: L10NContext = field(repr=False)
    """Localization information"""

    # okay: bool = True
    # """attr.okay indicates if this is, at bare minimum, working
    # It does not mean perfect or great. But is opposite of bad. The perfect
    # example is okay = True when something goes bad but the program know how to
    # recover.
    # """

    def __init__(self,
                 trivium: Any,
                 hdpdescriptionem: AuxHDPDesc,
                 l10n: L10NContext):
        self._trivium = trivium
        self._hdpdescriptionem = hdpdescriptionem
        self._l10n = l10n
        self.okay = self._hdpdescriptionem.okay

    def __eq__(self, other):

        # TODO: implement syntatic sugars like
        #           hp = HXLm.HDP.project(HXLm.HDATUM_UDHR).load()
        #           hp.okay() is True
        #       To return bool instead of compare the HDPOkay itself
        # print(other)
        if isinstance(other, bool):
            return self.okay == other

        # if isinstance(other, HDPOkay):
        #     return self.okay == other
        # when comparing to something that is not an bool, raise error
        raise NotImplementedError

    # # https://en.wiktionary.org/wiki/examen#Latin
    # def examen(self) -> list:
    #     """Deeper cicurgical check for debug values from all subitems"""
    #     # TODO: this is a good candidate to move to somewhere else if
    #     #       datamodel.py (as expected) get bigger
    #     resultatum = []
    #     if isinstance(self._entrypoint, ResourceWrapper):
    #         resultatum = []

    #         self._entrypoint failed:

    #     return resultatum


@dataclass
class AuxLoadPolicy(AbstAux):
    """Policies about how resources (like HDP rules or data) are allowed

    Used by hxlm.core.hdp.hazmat to abstract not just what already is cached
    but also what should not be loaded without user request
    """

    # TODO: move the rest of the hxlm.core.model.hdp rules to here and to
    #       hxlm.core.hdp.hazmat (Emerson Rocha, 2021-03-30 17:57 UTC)

    allowed_entrypoint_type: InitVar[Tuple] = [
        EntryPointType.FTP,
        EntryPointType.GIT,
        EntryPointType.HTTP,
        EntryPointType.LOCAL_DIR,  # air-gapped compliant
        EntryPointType.LOCAL_FILE,  # air-gapped compliant
        EntryPointType.NETWORK_DIR,  # air-gapped compliant
        EntryPointType.NETWORK_FILE,  # air-gapped compliant
        EntryPointType.PYDICT,  # air-gapped compliant
        EntryPointType.PYLIST,  # air-gapped compliant
        EntryPointType.SSH,
        EntryPointType.STREAM,
        EntryPointType.STRING,  # air-gapped compliant
        # EntryPointType.UNKNOW,
        EntryPointType.URN  # air-gapped compliant (it's an resolver)
    ]
    """Tuple of EntryPointType"""

    debug_no_restrictions: bool = False
    """Debug Mode. This ask policy checkers to not enforce any other rule"""

    enforce_startup_generic_tests: bool = False
    """If, and only if, implementations could do generic check EVERY time
    an library start, this variable is the way to give a hint.

    The use case is, even if an HDP implementation like this python library
    would try to comply, actually do generic tests like if no network access
    is allowed, try to test if is possible to do HTTP requests and then refuse
    to run until this is fixed.
    """

    custom_allowed_domains: InitVar[Tuple] = ()
    """Allow list of strings that, if an suffix of an domain, are allowed"""

    # log: InitVar[list] = []
    # """Log of messages (if any)"""

    safer_zones_hosts: InitVar[Tuple] = (
        'localhost'
    )
    """Tuple of hostnames that even if under restrictions are considered safe
    The name 'safer' does not mean that is 100% safe if an resource on the
    listed item already is compromised
    """

    safer_zone_list: InitVar[Tuple] = (
        '127.0.0.1',
        '::1'
    )
    """Tuple of IPv4 or IPv6 that even if under restrictions are considered safe
    The name 'safer' does not mean that is 100% safe if an resource on the
    listed item already is compromised.
    """


@dataclass
class AuxLoadRecursion(AbstAux):
    """Abstraction to internals of hxlm.core.hdp.hazmat hdprecursion_resource
    """
    # log: InitVar[list] = []
    # """Log of messages (if any)"""
