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

from pathlib import Path
# import datetime

import json
import yaml


__all__ = ['HDP']


class HDP:
    """Class used by HDP Declarative Programming Command Line Interface
    """

    _debug: bool = False

    _hdp: dict = {}
    # TODO: what name to use? Maybe Knowledge base?
    #       https://en.wikipedia.org/wiki/Knowledge_base
    #       (Emerson Rocha, 2021-03-13 00:59 UTC)

    # _hdp_raw: Union[str, dict] = None
    _hdp_raw: List = []

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

    def _get_hsilo_urn(self, hsilo_object: dict,
                       domain_base: str = 'local',
                       container_base: str = "default",
                       container_item_index: int = 0) -> str:
        # print('hsilo_object >>>', hsilo_object, '<<<<<')

        if 'urn' in hsilo_object:
            return hsilo_object.urn

        suffix = ''
        if container_item_index > 0:
            suffix = '-' + str(container_item_index)
        return ('urn:oo:hsilo:' + domain_base + ':' +
                container_base + suffix)

    def _update(self, hdp_rules: Union[List, dict],
                domain_base: str,
                container_base: str) -> bool:
        """Self update the internal metadata

        Args:
            hdp_rules (Union[List, dict]): The new information to add

        Returns:
            bool: True if ok
        """

        # TODO: create some simple hash for objects to use instead of timestamp
        #       (Emerson Rocha, 2021-03-15 01:37 UTC)

        self._hdp_raw.append(hdp_rules)
        # key =  hash(hdp_rules)
        # self._hdp[key] = hdp_rules
        # import datetime
        # print('type', type(hdp_rules))
        # if type(hdp_rules) == 'list':
        if isinstance(hdp_rules, list):
            loop = 0
            for hdp_rule in hdp_rules:
                # timestap = datetime.datetime.now().timestamp()
                # self._hdp[str(timestap)] = hdp_rule
                hashkey = self._get_hsilo_urn(
                    hdp_rule, domain_base=domain_base,
                    container_base=container_base, container_item_index=loop)
                # print('hashkey', hashkey)
                self._hdp[hashkey] = hdp_rule
                loop = loop + 1
        else:
            raise RuntimeError('Unknow hdp_rules [' + str(hdp_rules) + ']')

        return True

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

        raise RuntimeError('Unknow entrypoint [' + hdp_entry_point + ']')

    def _prepare_from_local_directory(self, dir_path: str) -> bool:
        if self._debug:
            print('HDP._prepare_from_local_directory dir_path', dir_path)

        result_status = True
        result_files = []
        pitr = Path(dir_path).glob('*')

        for file_ in pitr:
            # print('file_', file_)
            # print('file_ start ~', str(file_.name).startswith('~'))
            # print('file_ ends with csv', str(file_).endswith('.csv'))
            # print('file_ ends with HXLM_DATA_URN_EXTENSIONS',
            #       str(file_).endswith(HXLM_DATA_URN_EXTENSIONS))
            if str(file_.name).startswith('~'):
                if self._debug:
                    print('_prepare_from_local_directory skiping ', str(file_))
                continue
            if str(file_.name).endswith(self.HDP_YML_EXTENSIONS):
                result_files.append(str(file_))
            if str(file_.name).endswith(self.HDP_JSON_EXTENSIONS):
                result_files.append(str(file_))

        result_files_sorted = sorted(result_files)

        for filepath in result_files_sorted:
            if not self._prepare_from_local_file(filepath):
                if self._debug:
                    print('ERROR', str(filepath))
                result_status = False

        return result_status

    def _prepare_from_local_file(self, file_path: str):
        if self._debug:
            print('HDP._prepare_from_local_file file_path', file_path)
            print('HDP._prepare_from_local_file type file_path',
                  type(file_path))
            print('HDP._prepare_from_local_file os.path.split',
                  os.path.split(file_path))
            print('HDP._prepare_from_local_file os.path.split [1]',
                  os.path.split(file_path)[1])

        domain_base = 'local'
        container_base = os.path.split(file_path)[1]

        with open(file_path, mode="r") as filestring:
            if file_path.endswith(self.HDP_JSON_EXTENSIONS):
                return self._prepare_from_string(json_string=filestring,
                                                 domain_base=domain_base,
                                                 container_base=container_base)
            if file_path.endswith(self.HDP_YML_EXTENSIONS):
                return self._prepare_from_string(yml_string=filestring,
                                                 domain_base=domain_base,
                                                 container_base=container_base)

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
                             yml_string: str = None,
                             domain_base: str = 'local',
                             container_base: str = "default"):
        if json_string:
            # self._hdp_raw = json_string
            # self._hdp = json.loads(json_string)
            # return True
            parsed = json.loads(json_string)
            return self._update(parsed,
                                domain_base=domain_base,
                                container_base=container_base)

        if yml_string:
            # self._hdp_raw = yml_string
            # self._hdp = yaml.safe_load(yml_string)
            # return True
            parsed = yaml.safe_load(yml_string)
            return self._update(parsed,
                                domain_base=domain_base,
                                container_base=container_base)

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

        # print('aaaaaam ',self._hdp.keys())

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

        if self._debug:
            print('HDP.export_json_processing_specs self._hdp', self._hdp)

        result = []
        # for hsilo in self._hdp:
        #     if 'hrecipe' in hsilo:
        #         for hrecipeitem in hsilo['hrecipe']:
        #             # result.append(self._prepare_hrecipe_item(hrecipeitem))
        #             result.extend(self._prepare_hrecipe_item(hrecipeitem))
        for hdphash in self._hdp:
            if self._debug:
                print('HDP.export_json_processing_specs ...2',
                      self._hdp[hdphash])
            # for hsilo in self._hdp[hdphash]:
            # print('HDP.export_json_processing_specs ...3',
            #         self._hdp[hdphash][hsilo])
            if 'hrecipe' in self._hdp[hdphash]:
                # if self._debug:
                #     print('HDP.export_json_processing_specs ...4',
                #             hsilo)
                #     print('HDP.export_json_processing_specs ...5',
                #             hsilo['hrecipe'])
                for hrecipeitem in self._hdp[hdphash]['hrecipe']:
                    result.extend(self._prepare_hrecipe_item(hrecipeitem))
            else:
                if self._debug:
                    print('HDP....6 no hrecipe',
                          self._hdp[hdphash])

        return json.dumps(result, indent=4, sort_keys=True)

    def export_yml(self, hdp_filters: dict = None) -> str:
        """Export the current HDP internal metadata in an YAML format

        Returns:
            str: The entire HDP internal metadata
        """
        # TODO: check potential privacy issues with objects that could contain
        #       access credentials. Or maybe we should put such things
        #       in an place outside HDP internal metadata?
        #       (Emerson Rocha, 2021-03-13 01:00 UTC)

        # if hdp_filters:
        #     print('TODO hdp_filters')

        return yaml.dump(self._hdp, Dumper=Dumper,
                         encoding='utf-8', allow_unicode=True)

    def get_prepared_filter(self, args) -> dict:
        filters = {}
        for arg in vars(args):
            if (arg.startswith(('non_', 'verum_')) and
                    getattr(args, arg) is not None):
                print(arg, getattr(args, arg))
                filters[arg] = getattr(args, arg)
        # for a in vars(args.parse_args()):
        #     print('This arg is %s' % a)
        # for option in args:
        #     print('option', option)

        return filters

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
