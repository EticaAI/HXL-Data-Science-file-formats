"""hxlm.core.model.hdp contains HDP class

This is used by the HDP Declarative Programming Command Line Interface


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os
from urllib.request import urlopen

from typing import (
    Union,
    List,
    Tuple,
)

import json
import yaml


__all__ = ['HDP']


class HDP:
    """Class used by HDP Declarative Programming Command Line Interface
    """

    _debug: bool = False

    _hdp: dict = None
    # TODO: what name to use? Maybe Knowledge base?
    #       https://en.wikipedia.org/wiki/Knowledge_base
    #       (Emerson Rocha, 2021-03-13 00:59 UTC)

    _hdp_raw: Union[str, dict] = None

    _online_unrestricted_init: bool = False
    """For requests that implicitly ask for not-only localhost data, should
    we implicitly initiate HDP?

    Defaults to False (for security reasons)
    """

    _safer_zone_hosts: Tuple = (
        'localhost'
    )
    """Tuple of hostnames that even if under restrictions are considered safe
    The name 'safer' does not mean that is 100% safe if an resource on the
    listed item already is compromised
    """

    _safer_zone_list: Tuple = [
        '127.0.0.1',
        '::1'
    ]
    """Tuple of IPv4 or IPv6 that even if under restrictions are considered safe
    The name 'safer' does not mean that is 100% safe if an resource on the
    listed item already is compromised.
    """

    HDP_JSON_EXTENSIONS: Tuple = (
        '.hdp.json',
        '.hdpd.json',
        '.hdpr.json',
        # '.urn.json' # See urnresolver
    )

    HDP_YML_EXTENSIONS: Tuple = (
        '.hdp.yml',
        '.hdpd.yml',
        '.hdpr.yml',
        # '.urn.yml' # See urnresolver
    )

    def __init__(self, hdp_entry_point: str = None,
                 yml_string: str = None,
                 json_string: str = None,
                 online_unrestricted_init: bool = False,
                 safer_zone_hosts: Tuple = None,
                 safer_zone_list: Tuple = None,
                 debug: bool = False
                 ):
        """
        Constructs all the necessary attributes for the HDPCLI object.
        """

        self._online_unrestricted_init = online_unrestricted_init
        self._debug = debug

        if safer_zone_hosts:
            self._safer_zone_hosts = safer_zone_hosts
        if safer_zone_list:
            self._safer_zone_list = safer_zone_list

        if hdp_entry_point:
            self._prepare(hdp_entry_point=hdp_entry_point, is_startup=True)
        if json_string:
            self._prepare_from_string(json_string=json_string)
        if yml_string:
            self._prepare_from_string(yml_string=yml_string)

    def _get_urnresolver_iri(self, urn: str) -> str:
        return 'http://localhost/?not-implemented-yet#' + urn

    def _prepare(self, hdp_entry_point: str, is_startup: bool = False) -> bool:

        if self._debug:
            print('HDP._prepare', hdp_entry_point)

        # First things first: try to resolve the URN. Maybe already is local
        if hdp_entry_point.startswith('urn:'):
            hdp_entry_point = self._get_urnresolver_iri(hdp_entry_point)

        if hdp_entry_point.startswith(('http://', 'https://')):
            return self._prepare_from_remote_iri(hdp_entry_point,
                                                 is_startup=is_startup)

        if os.path.isfile(hdp_entry_point):
            return self._prepare_from_local_file(hdp_entry_point)

        if os.path.isdir(hdp_entry_point):
            return self._prepare_from_local_directory(hdp_entry_point)

        raise RuntimeError('unknow entrypoint [' + hdp_entry_point + ']')

    def _prepare_from_local_directory(self, dir_path: str):
        if self._debug:
            print('HDP._prepare_from_local_directory dir_path', dir_path)
        return False

    def _prepare_from_local_file(self, file_path: str):
        if self._debug:
            print('HDP._prepare_from_local_file file_path', file_path)
            print('HDP._prepare_from_local_file type file_path',
                  type(file_path))

        with open(file_path, mode="r") as filestring:
            if file_path.endswith(self.HDP_JSON_EXTENSIONS):
                return self._prepare_from_string(json_string=filestring)
            if file_path.endswith(self.HDP_YML_EXTENSIONS):
                return self._prepare_from_string(yml_string=filestring)

        return False

    def _prepare_from_remote_iri(self, iri: str, is_startup: bool = False):
        if self._debug:
            print('HDP._prepare_from_remote_iri iri', iri)
            print('HDP._prepare_from_remote_iri is_startup', is_startup)
            print('HDP._online_unrestricted_init',
                  self._online_unrestricted_init)

        if (is_startup and self._online_unrestricted_init) or \
                self.is_remote_allowed(iri):
            response = urlopen(iri)
            filestring = response.read()
            if iri.endswith(self.HDP_JSON_EXTENSIONS):
                return self._prepare_from_string(json_string=filestring)
            if iri.endswith(self.HDP_YML_EXTENSIONS):
                return self._prepare_from_string(yml_string=filestring)
        else:
            # if self._debug:
            # print('HDP.is_remote_allowed iri', iri)
            raise RuntimeError('remote iri not allowed [' + iri + ']')

        return False

    def _prepare_from_string(self,
                             json_string: str = None,
                             yml_string: str = None):
        if json_string:
            self._hdp_raw = json_string
            self._hdp = json.loads(json_string)
            return True

        if yml_string:
            self._hdp_raw = yml_string
            self._hdp = yaml.safe_load(yml_string)
            return True

        raise RuntimeError('json_string or yml_string are required')

    def _prepare_hrecipe_item(self, recipe: List) -> List:
        """Prepare an individual iten from HXL data processing specs

        Notes:
            1. If an recipe does have example iri (likely to be an remote
            resource) or exemplum data (often inline) the FIRST item of the
            array will not have these values, but the second will.
            2. If you have several examples, EACH example (plus an output)
            without the input/output data, will create result on an item.

        See also:
            self.export_json_processing_specs()

        Args:
            recipe (List): An individual item from an hrecipe

        Returns:
            List: The result list
        """

        # Note: for convention, the first recipe always will not use any
        #       example input (this can make easyer for reuse). But old
        #       examples will need to be updated
        recipe_without_examplum = {
            'recipe': recipe['_recipe']
        }
        result = [recipe_without_examplum]

        if 'exemplum' in recipe:
            loop = 0

            while True:
                # print('exemplum loop, inside', loop, recipe['exemplum'][loop]['fontem'])  # noqa
                recipeitem = {
                    'recipe': recipe['_recipe']
                }
                if 'iri' in recipe['exemplum'][loop]['fontem']:
                    recipeitem['input'] = recipe['exemplum'][loop]['fontem']['iri']  # noqa
                if '_sheet_index' in recipe['exemplum'][loop]['fontem']:
                    recipeitem['sheet_index'] = recipe['exemplum'][loop]['fontem']['_sheet_index']  # noqa
                if 'datum' in recipe['exemplum'][loop]['fontem']:
                    recipeitem['input_data'] = recipe['exemplum'][loop]['fontem']['datum']  # noqa
                if 'objectivum' in recipe['exemplum'][loop] and 'datum' in recipe['exemplum'][loop]['objectivum']:  # noqa
                    recipeitem['output_data'] = recipe['exemplum'][loop]['objectivum']['datum']  # noqa
                result.append(recipeitem)
                loop = loop + 1
                if loop >= len(recipe['exemplum']):
                    break

        return result

    # def _prepare_from_yml_string(self, hdp_yml_string):
    #     self._hdp_raw = hdp_yml_string
    #     self._hdp = yaml.safe_load(hdp_yml_string)

    def export_json(self) -> str:
        """Export the current HDP internal metadata in an YAML format

        Returns:
            str: The entire HDP internal metadata
        """
        # TODO: check potential privacy issues with objects that could contain
        #       access credentials. Or maybe we should put such things
        #       in an place outside HDP internal metadata?
        #       (Emerson Rocha, 2021-03-13 01:00 UTC)

        return json.dumps(self._hdp, indent=4, sort_keys=True)

    def export_json_processing_specs(self, options=None) -> str:
        """Export JSON processing specs for HXL data (as an array)

        Note: the result is an Array, but HXL-Proxy and hxlspec expects an
              single result. You may need to manually decide which item to use.
              If the result already is only one item, remove the starting '['
              and the last ']'. The jq command line utility can deal with this!

        Example:
            # Via command line
            hxlspec myspec.json > data.hxl.csv
            # Test on HXL-proxy
            https://proxy.hxlstandard.org/api/from-spec.html

        See also:
            self._prepare_hrecipe_item()
        Args:
            options ([type], optional): Select more specific recipes.
                                        Defaults to None.

        Raises:
            NotImplementedError: options is not implemented... yet

        Returns:
            List of JSON processing specs for HXL data
        """

        if options:
            raise NotImplementedError('options not implemented yet')

        result = []
        for hsilo in self._hdp:
            if 'hrecipe' in hsilo:
                for hrecipeitem in hsilo['hrecipe']:
                    # result.append(self._prepare_hrecipe_item(hrecipeitem))
                    result.extend(self._prepare_hrecipe_item(hrecipeitem))

        return json.dumps(result, indent=4, sort_keys=True)

    def export_yml(self) -> str:
        """Export the current HDP internal metadata in an YAML format

        Returns:
            str: The entire HDP internal metadata
        """
        # TODO: check potential privacy issues with objects that could contain
        #       access credentials. Or maybe we should put such things
        #       in an place outside HDP internal metadata?
        #       (Emerson Rocha, 2021-03-13 01:00 UTC)

        return yaml.dump(self._hdp, Dumper=Dumper)

    def is_remote_allowed(self, iri: str) -> bool:
        """Based on current context explain if the resource is allowed to fetch

        Args:
            iri (str): an resolvable remote resource (not an URN)

        Returns:
            bool: True allowed
        """

        if self._debug:
            print('HDP.is_remote_allowed iri', iri)

        # TODO: implement self._safer_zone_hosts & self._safer_zone_list.
        #       While this should work for common cases, still hardcoded.
        #       (Emerson Rocha, 2021-03-13 03:31 UTC)
        if iri.startswith((
            'http://localhost',
            'http://127.0.0.1',
            'http://::1'
        )):
            return True
        return False


class Dumper(yaml.Dumper):
    """Force identation on pylint, https://github.com/yaml/pyyaml/issues/234
    TODO: check on future if this still need
          (Emerson Rocha, 2021-02-28 10:56 UTC)
    """

    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)
