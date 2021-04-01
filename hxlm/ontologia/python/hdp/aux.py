"""hxlm.ontologia.python.hdp.attr

Trivia
------
- aux.py
  - auxilium: https://en.wiktionary.org/wiki/auxilium#Latin
- "auxilium", Latin, Etymology:
  - From augeō (“spread, honor, promote”).

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from dataclasses import dataclass, field, InitVar
# from dataclasses import dataclass, field
from typing import (
    Any,
    List,
    # Tuple,
    Type,
    # Union
)

from hxlm.core.types import (
    L10NContext
)

# from hxlm.ontologia.python.hdp.radix import (
#     HDPPolicyLoad,
#     HDPRaw,
#     HSiloWrapper
# )


@dataclass
class AuxLoadRecursion:
    """Abstraction to internals of hxlm.core.hdp.hazmat hdprecursion_resource
    """
    log: InitVar[list] = []
    """Log of messages (if any)"""


@dataclass
class AuxHDPDesc:
    """An quick summary about an current HDP object.
    """

    aup_loader: Type['HDPPolicyLoad']
    """Acceptable Use Policy for load HDP file projects (not the data)

    Note that each HDP file can have individual Acceptable Use Policy. This
    item is mostly used by advanced users who want to automate too much (not
    even need human intervention) or they want to share snippets with less
    experienced people while somewhat tolerating the person dealing HDP files
    from several places
    """

    entrypoint: Any = None
    """The entrypoint"""

    # l10n: L10NContext = field(repr=False)
    # """Localization information"""

    log: InitVar[list] = []
    """Raw message log. Either used for debug or explain errors"""

    log_okay: InitVar[list] = []
    """Short, temporary most recent log if not okay"""

    okay: bool = True
    """attr.okay indicates if this is, at bare minimum, working
    It does not mean perfect or great. But is opposite of bad. The perfect
    example is okay = True when something goes bad but the program know how to
    recover.
    """

    # TODO: organize these next fields. Not all are necessary from HDPProject
    hdpraw: InitVar[List[Type['HDPRaw']]] = []
    """HDPRaw is, informally speaking it is a crude representation of
    information in a disk file that MAY be an single hsilo or not.
    """

    hsilos: InitVar[List[Type['HSiloWrapper']]] = []
    """List of individual HSilo (one physical file could have multiple)"""


@dataclass(init=False, eq=False)
class AuxHDPOkay:
    """HDPOkay is an 'debug' dataclass for HDP projects
    """

    _entrypoint: Any = None
    """The entrypoint"""

    # TODO: hide this field when user is calling HDPOkay
    _hdpdescriptionem: AuxHDPDesc = field(repr=False)
    """A HDPDescriptionem with full details of the project"""

    _l10n: L10NContext = field(repr=False)
    """Localization information"""

    okay: bool = True
    """attr.okay indicates if this is, at bare minimum, working
    It does not mean perfect or great. But is opposite of bad. The perfect
    example is okay = True when something goes bad but the program know how to
    recover.
    """

    def __init__(self,
                 entrypoint: Any,
                 hdpdescriptionem: AuxHDPDesc,
                 l10n: L10NContext):
        self._entrypoint = entrypoint
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
