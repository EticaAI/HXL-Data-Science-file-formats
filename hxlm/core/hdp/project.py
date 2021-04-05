"""hxlm.core.hdp.project


>>> import hxlm.core as HXLm
>>> # Loading single file
>>> hp = HXLm.HDP.project(HXLm.HDATUM_UDHR).load()
>>> isinstance(hp.okay(), HXLm.Ontologia.hdp.aux.AuxHDPExplanare)
True
>>> isinstance(hp.descriptionem(), HXLm.Ontologia.hdp.aux.AuxHDPDesc)
True
>>> hp.okay() == True
True

# >>> hp.okay()

#  >>> hp.info()
#  >>> hp.info('entry_point')
# >>> hp._log
# >>> hp.hdpraw[0].failed
# >>> hp.hdpraw[0].log

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os

# from dataclasses import asdict

from typing import (
    Any,
    List,
    # Union
)

from hxlm.core.hdp.exception import (
    HDPExceptionem,
    # l10n_descriptionem
)

from hxlm.ontologia.python.commune import (
    Factum
)

from hxlm.ontologia.python.systema import (
    # Factum,
    L10NContext
)
# from hxlm.core.util import (
#     get_value_if_key_exists
# )

from hxlm.core.io.util import (
    get_entrypoint
)

from hxlm.ontologia.python.hdp.aux import (
    AuxHDPDesc,
    AuxHDPExplanare,
    AuxLoadPolicy
)

from hxlm.ontologia.python.hdp.radix import (
    # HDPPolicyLoad,
    HSiloWrapper,
    HDPRaw
)

from hxlm.core.hdp.index import (
    # convert_resource_to_hdpindex,
    is_index_hdp
)
from hxlm.core.hdp.raw import (
    convert_resource_to_hdpraw,
    is_raw_hdp_item_syntax,
    ResourceWrapper
)
from hxlm.core.hdp.hazmat.policy import (
    get_policy_HDSL1,
    is_not_acceptable_load_this
)

from hxlm.core.localization.util import (
    l10n
)

__all__ = ['project']

# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))

# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))


class HDPProject:
    """Abstraction to an HDP Declarative Programming project

    While is possible to load individual YAML/JSON file to work with single
    resouce, the HDPProject is an way to deal with colletions of HDP files.

    It's an partial refactoring of the hxlm/core/model/hdp.py
    """

    _aup_loader: AuxLoadPolicy
    """Acceptable Use Policy for load HDP file projects (not the data)

    Note that each HDP file can have individual Acceptable Use Policy. This
    item is mostly used by advanced users who want to automate too much (not
    even need human intervention) or they want to share snippets with less
    experienced people while somewhat tolerating the person dealing HDP files
    from several places
    """

    _entrypoint: ResourceWrapper

    _entrypoint_str: str

    _l10n: L10NContext
    """Current active user context."""

    _log: list = []
    """Log of messages. Both for verbose and error messages"""

    _log_okay: list = []
    """Short, temporary most recent log if not okay"""

    hdpraw: List[HDPRaw] = []
    """HDPRaw is, informally speaking it is a crude representation of
    information in a disk file that MAY be an single hsilo or not.
    """

    hsilos: List[HSiloWrapper]
    """List of individual HSilo (one physical file could have multiple)"""

    _okay: bool = True
    """attr.okay indicates if this is, at bare minimum, working
    It does not mean perfect or great. But is opposite of bad. The perfect
    example is okay = True when something goes bad but the program know how to
    recover.
    """

    def __init__(self, entrypoint: Any,
                 user_l10n: L10NContext,
                 policy_loader: AuxLoadPolicy):
        self._entrypoint_str = entrypoint
        self._l10n = user_l10n
        self._aup_loader = policy_loader

        # return self

    def _parse_entrypoint(self, entrypoint: Any):
        """Generic parser for the initial entrypoint

        Args:
            entrypoint (Any):  Anything that hxlm.core.io.util.get_entrypoint
                               is able to undestand.
        """
        # TODO: at the moment, we're only parsing the raw input, but it should
        #       be loaded as an Silo

        # TODO: implement indexes based on user l10n
        indexes = [
            '.hdp.yml',
            '.lat.hdp.yml',
        ]

        self._entrypoint = get_entrypoint(entrypoint, indexes=indexes)

        if self._entrypoint.failed:
            self._okay = False
            fact = Factum('_parse_entrypoint failed: input [' +
                          str(entrypoint) + '] ResourceWrapper log [ ' +
                          str(self._entrypoint.log) + ']')
            self._log.append(fact)
            # self._log.append('_parse_entrypoint failed: input [' +
            #                  str(entrypoint) + '] ResourceWrapper log [ ' +
            #                  str(self._entrypoint.log) + ']')

        hdpraw1 = self._parse_resource(self._entrypoint)
        # print('oioioi', hdpraw1.failed, self._okay)
        if hdpraw1.failed:
            self._okay = False
            self._log.append(Factum('_parse_resource failed: input [' +
                                    str(entrypoint) + '] HDPRaw log [ ' +
                                    str(hdpraw1.log) + ']'))

    def _recursive_resource_parsing(
            self,
            resource: ResourceWrapper) -> 'HDPProject':
        """Method to do recursive parsing of files.

        While the simplest case (load a simple HDP file) may already have more
        than one HSilo, the fact that we allow HDPIndex files have
        _interesting_ usages, in special because both for performance and
        privacy of the user, full automated parsing may not be the default
        case

        Returns:
            [HDPProject]: An instance of this class itself
        """
        # TODO: _recursive_hdp_parsing is an draft and should be implemented.
        if resource.failed:
            self._okay = False
            self._log.append(Factum('resource.failed: [' +
                                    str(resource) + ']'))
        elif is_index_hdp(resource.content):
            print('TODO: is_index_hdp')

        elif is_raw_hdp_item_syntax(resource.content):
            print('TODO: is_index_hdp')
        else:
            self._okay = False
            self._log.append(Factum(
                'resource ¬ (is_index_hdp | is_raw_hdp_item_syntax) ['
                + str(resource) + ']'))

        return self

    def _parse_resource(self, resource: ResourceWrapper) -> bool:
        hdpraw = convert_resource_to_hdpraw(resource)
        self.hdpraw.append(hdpraw)
        return hdpraw

    def descriptionem(self) -> AuxHDPDesc:
        """Quick sumamary about current HDP project

        Args:
            okay (bool, optional): [description]. Defaults to True.

        Returns:
            HDPProjectInfo: The result
        """
        # print('oioioi', self._okay)
        info = AuxHDPDesc(
            aup_loader=None,
            # l10n=self._l10n,
            librum=self._log,
            okay=self._okay,
        )

        # if len(self._log_okay):
        #     info.log.extend(self._log_okay)

        return info

    def load(self):
        """Do, _de facto_ the (re-)loading of data by user request.

        load() and reload() are used to allow lazy-loading and/or user fix
        issues interactively without trow exceptions everywhere. The only hard
        requeriment are pretty puch the boostraping entrypoint

        Raises:
            SyntaxError: [description]

        Returns:
            [type]: [description]
        """
        self._log_okay = []
        if is_not_acceptable_load_this(self._entrypoint_str,
                                       self._aup_loader):
            raise HDPExceptionem(Factum('[' + self._entrypoint_str +
                                        '] ¬ is_acceptable_load_this [' +
                                        str(self._aup_loader) + ']'))
            # raise HDPExceptionem('[' + self._entrypoint_str +
            #                      '] ¬ is_acceptable_load_this [' +
            #                      str(self._aup_loader) + ']')
            # raise SyntaxError('[' + self._entrypoint_str +
            #                   '] ¬ is_acceptable_load_this [' +
            #                   str(self._aup_loader) + ']')
        self._parse_entrypoint(self._entrypoint_str)

        # print('oioioi', self._okay)

        return self

    def okay(self) -> AuxHDPExplanare:
        """Debug-like relevant information for end user know when is not okay

        Returns:
            AuxHDPExplanare: The result
        """
        if self._entrypoint:
            entry_ = self._entrypoint
        else:
            entry_ = self._entrypoint_str
        # print('oioioi', self._okay)
        okay_ = AuxHDPExplanare(
            trivium=entry_,
            hdpdescriptionem=self.descriptionem(),
            l10n=self._l10n,
        )

        return okay_

    def reload(self):
        self.load()
        return self


def project(entrypoint: str) -> HDPProject:
    """Initialize an HDP project (load collections of HDP files)

    Args:
        entry_point (str): Path to an entrypoint file

    Returns:
        HDPProject: An HDPProject instance
    """
    user_l10n = l10n()

    # TODO: eventually the policy should be configurable also on startup
    #       not only when running
    policy_loader = get_policy_HDSL1()
    result = HDPProject(entrypoint,
                        user_l10n=user_l10n,
                        policy_loader=policy_loader)
    return result
