"""hxlm.core.hdp.project


>>> import hxlm.core as HXLm
>>> # Loading single file
>>> hp = HXLm.HDP.project(HXLm.HDATUM_UDHR).load()
>>> hp.ok
True

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
    Union
)

from hxlm.core.types import (
    L10NContext
)
from hxlm.core.util import (
    get_value_if_key_exists
)

from hxlm.core.io.util import (
    get_entrypoint
)

from hxlm.core.hdp.datamodel import (
    HDPPolicyLoad,
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

    _entrypoint: ResourceWrapper

    _entrypoint_str: str

    _l10n: L10NContext
    """Current active user context."""

    _log: list = []
    """Log of messages. Both for verbose and error messages"""

    hdpraw: List[HDPRaw] = []
    """HDPRaw is, informally speaking it is a crude representation of
    information in a disk file that MAY be an single hsilo or not.
    """

    hsilos: List[HSiloWrapper]
    """List of individual HSilo (one physical file could have multiple)"""

    ok: bool = True
    """Boolean to check if everyting is 100%.

    HDP project can still work with somewhat broken input (even if means
    allow user correct in running time)
    """

    policy_loader: HDPPolicyLoad
    """An HDP policy about what rules could be loaded
    (ex.: restrict domains)"""

    def __init__(self, entrypoint: Any,
                 user_l10n: L10NContext,
                 policy_loader: HDPPolicyLoad):
        self._entrypoint_str = entrypoint
        self._l10n = user_l10n
        self.policy_loader = policy_loader

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
            self.ok = False
            self._log.append('_parse_entrypoint failed: input [' +
                             str(entrypoint) + '] ResourceWrapper log [ ' +
                             str(self._entrypoint.log) + ']')

        hdpraw1 = self._parse_resource(self._entrypoint)

        if hdpraw1.failed:
            self.ok = False
            self._log.append('_parse_resource failed: input [' +
                             str(entrypoint) + '] HDPRaw log [ ' +
                             str(hdpraw1.log) + ']')

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
            self.ok = False
            self._log.append('resource.failed: [' + str(resource) + ']')
        elif is_index_hdp(resource.content):
            print('TODO: is_index_hdp')

        elif is_raw_hdp_item_syntax(resource.content):
            print('TODO: is_index_hdp')
        else:
            self.ok = False
            self._log.append(
                'resource ¬ (is_index_hdp | is_raw_hdp_item_syntax) ['
                + str(resource) + ']')

        return self

    def _parse_resource(self, resource: ResourceWrapper) -> bool:
        hdpraw = convert_resource_to_hdpraw(resource)
        self.hdpraw.append(hdpraw)
        return hdpraw

    def info(self, dotted_key: str = None) -> Union[dict, str, bool]:
        """Quick sumamary about current HDP project

        Args:
            dotted_key (str, optional): 'dotted.key' style filter.
                        Defaults to load all information

        Returns:
            Union[dict, str, bool]: Without dotted_key returns a dict. But
                        depending of filters, users can select inner values
                        with different structures
        """
        info = {
            'ok': self.ok,
            'log': self._log,
            # 'entrypoint': self._entrypoint,
            'l10n': self._l10n
            # 'l10n_user': asdict(self._l10n_user)
        }

        # raise SyntaxError(info)
        if dotted_key is not None:
            return get_value_if_key_exists(info, dotted_key)

        return info

    def load(self):
        if is_not_acceptable_load_this(self._entrypoint_str,
                                       self.policy_loader):
            raise SyntaxError('[' + self._entrypoint_str +
                              '] ¬ is_acceptable_load_this [' +
                              str(self.policy_loader) + ']')
        self._parse_entrypoint(self._entrypoint_str)

        return self

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
