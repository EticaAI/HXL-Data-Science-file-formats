"""hxlm.core.schema.urn.util is (TODO: document this)
"""

import os
import csv
import json
from pathlib import Path
# from urllib.parse import urlparse
# import requests

# import glob

from typing import (
    Type
)

from typing import (
    List
)

import yaml

from hxlm.core.htype.urn import (
    GenericUrnHtype
)

# __all__ = ['get_urn_vault_local_info', 'get_urn_vault_local_info']

_HOME = str(Path.home())

_VERBOSE = 0

# TODO: move these variables to somewere else
HXLM_CONFIG_BASE = os.getenv(
    'HXLM_CONFIG_BASE', _HOME + '/.config/hxlm/')

HXLM_DATA_POLICY_BASE = os.getenv(
    'HXLM_DATA_POLICY_BASE', _HOME + '/.config/hxlm/policy/')

HXLM_DATA_VAULT_BASE = os.getenv(
    'HXLM_DATA_VAULT_BASE', _HOME + '/.local/var/hxlm/data/')

HXLM_DATA_VAULT_BASE_ALT = os.getenv('HXLM_DATA_VAULT_BASE_ALT')
HXLM_DATA_VAULT_BASE_ACTIVE = os.getenv(
    'HXLM_DATA_VAULT_BASE_ACTIVE', HXLM_DATA_VAULT_BASE)


HXLM_DATA_URN_EXTENSIONS = ('urn.csv', 'urn.tsv',
                            'urn.json', 'urn.yml', 'urn.txt')
"""HXLM_DATA_URN_EXTENSIONS Must be a python truple"""

HXLM_DATA_URN_EXTENSIONS_ENCRYPTED = (
    'urn.csv.enc', 'urn.csv.gpg',
    'urn.tsv.enc', 'urn.tsv.gpg',
    'urn.json.enc', 'urn.json.gpg',
    'urn.yml.enc', 'urn.yml.gpg',
    'urn.txt.enc', 'urn.txt.gpg'
)
"""HXLM_DATA_URN_EXTENSIONS equivalent when encrypted.
While implementation is out of scope of this library (and even the cli
helper urnresolver) these naming conventions can be used when need to
encrypt even the urn resolvers at rest (or have no option but let an
public accessible URL online.)

The HXLM_DATA_URN_EXTENSIONS_ENCRYPTED can be used to an quick check if
some place explicitly point to an remote URN and the end of path ends with
this. So implementations can at least show an error like
'Access to this resource need manual intervetion by the user'
"""

# import json
# import yaml

# from hxlm.core.model.meta import (
#     HMeta
# )
# from hxlm.core.schema.vocab import (
#     ItemHVocab
# )

# __all__ = ['export_schema_yaml', 'export_schema_json', 'get_schema',
#            'get_schema_as_hmeta', 'get_schema_vocab']
# TODO: This path is obvlously hardcoded. Generalize it.
#       https://stackoverflow.com/questions/4028904
#       /how-to-get-the-home-directory-in-python

# _HXLM_BASE = str(Path.home() + "/.config/hxlm/"
# HXLM_CORE_URN_DATA_BASE_DEFAULT = str(Path.home() + "/.config/hxlm/urn/data/"

# ./hxlm/core/bin/urnresolver.py urn:data:xz:eticaai:pcode:br
# ./hxlm/core/bin/urnresolver.py urn:data:xz:hxl:standard:core:hashtag


def debug_local_data():
    """[summary]
    """
    print('is_urn_data_prepared', is_urn_data_prepared(required=True))
    print('HXLM_CONFIG_BASE', HXLM_CONFIG_BASE)
    print('HXLM_DATA_POLICY_BASE', HXLM_DATA_POLICY_BASE)
    print('HXLM_DATA_VAULT_BASE', HXLM_DATA_VAULT_BASE)
    print('HXLM_DATA_VAULT_BASE_ALT', HXLM_DATA_VAULT_BASE_ALT)
    print('HXLM_DATA_VAULT_BASE_ACTIVE', HXLM_DATA_VAULT_BASE_ACTIVE)


def get_urn_vault_local_info(urn: Type[GenericUrnHtype]):
    """[summary]

    Args:
        urn (Type[GenericUrnHtype]): [description]
    """
    print('HXLM_CONFIG_BASE', HXLM_CONFIG_BASE)
    print('HXLM_DATA_POLICY_BASE', HXLM_DATA_POLICY_BASE)
    print('HXLM_DATA_VAULT_BASE', HXLM_DATA_VAULT_BASE)
    print('HXLM_DATA_VAULT_BASE_ALT', HXLM_DATA_VAULT_BASE_ALT)
    print('HXLM_DATA_VAULT_BASE_ACTIVE', HXLM_DATA_VAULT_BASE_ACTIVE)
    print('TODO: urn', urn)


def get_urn_resolver_from_csv(urn_file: str,
                              delimiter: str = ',') -> List[dict]:
    """Parse an local CSV/TSV/TAB/TXT file to be used to resolve URNs

    TODO: we're doing an lazy way to check if the file is valid
          by assuming first row is an URN exact column and the
          second is the remote source URL. While this is flexible
          and works, it's obvously less strict than the definitions
          of the file formats and eventually could (or not) be improved
          to avoid people using this less strict way just because the
          software allow it.
          (Emerson Rocha, 2021-03-07 17:03)

    Args:
        urn_file (str): Path to an local CSV/TSV/TAB file
        delimiter (str, optional): CSV-like delimiter. Defaults to ','.
        urnref (str, optional): An hint to how to name this URN Index

    Returns:
        List[dict]: parsed result of the current file
    """

    # TODO: if an csv have two equivalent rules, convert back to an
    #       JSON/YAML-like style. This part is not just optionated
    #       (aka lazy), but wrong (Emerson Rocha, 2021-03-07 17:25)

    result = []

    # print('ttt', Path(urn_file).name)
    urnref = Path(urn_file).name
    # raise Exception(Path(urn_file).name)

    with open(urn_file, 'r') as open_urn_file:
        csvreader = csv.reader(open_urn_file, delimiter=delimiter)
        for row in csvreader:
            # print('row', delimiter, row)
            # print('row', row[0], row[1], row)
            if len(row) < 2 or not row[0].startswith('urn:data'):
                # print('get_urn_resolver_from_csv skiping...')
                continue

            item = {
                'urn': row[0],
                # 'source_remote': row[1]
                'source': [row[1]],
                'urnref': urnref
            }
            result.append(item)

        # print('get_urn_resolver_from_csv')
        # print(csvreader, list(csvreader))
    # print('result', result)
    return result


def get_urn_resolver_from_json(urn_file: str) -> List[dict]:
    """Parse an localJSON file to be used to resolve URNs

    Both urn.json and urn.yml are already expected to be the internal format
    so this check is a mere conversion.

    Args:
        urn_file (str): full path to local JSON file

    Returns:
        List[dict]: the resolver list of dictionaries to parse
    """

    # To help filter with several sources of URNs, we add an urnref to allow
    # filter on steps
    urnref = Path(urn_file).name

    with open(urn_file, "r") as read_file:
        data = json.load(read_file)

        for item in data:
            if 'urnref' not in item:
                item['urnref'] = urnref

        return data
    #     print('data', type(data), data)

    # pass


def get_urn_resolver_from_yml(urn_file: str) -> List[dict]:
    """Parse an YAML file to be used to resolve URNs

    Both urn.json and urn.yml are already expected to be the internal format
    so this check is a mere conversion.

    Args:
        urn_file (str): full path to local YAML (.yml) file

    Returns:
        List[dict]: the resolver list of dictionaries to parse
    """

    # To help filter with several sources of URNs, we add an urnref to allow
    # filter on steps
    urnref = Path(urn_file).name

    with open(urn_file, "r") as read_file:
        data = yaml.safe_load(read_file)
        # print('get_urn_resolver_from_yml data', data)

        for item in data:
            if 'urnref' not in item:
                item['urnref'] = urnref
        return data


def get_urn_resolver_from_any(filepath: str,
                              required: bool = False,
                              filetype: str = '') -> List[dict]:

    if filetype == '.csv' or filepath.endswith('.csv'):
        return get_urn_resolver_from_csv(filepath)
    elif filetype == '.tsv' or filepath.endswith('.tsv'):
        return get_urn_resolver_from_csv(filepath, '\t')
    elif filetype == '.txt' or filepath.endswith('.txt'):
        return get_urn_resolver_from_csv(filepath, ':')
    elif filetype == '.json' or filepath.endswith('.json'):
        return get_urn_resolver_from_json(filepath)
    elif filetype == '.yml' or filepath.endswith('.yml'):
        return get_urn_resolver_from_yml(filepath)
    elif required:
        raise RuntimeError(
            'local_file_or_path [' + filepath + '] not found')
    else:
        return None


def get_urn_resolver_local(local_file_or_path: str,
                           required: bool = False) -> List[str]:
    """From an exact local file or an folder, return URN resolver dictionary

    Args:
        local_file_or_path (str): Local file on disk or an folder to search
                                  (not recursive search)
        required (bool, optional): Raise error on missing. Defaults to False.

    Raises:
        RuntimeError: [description]

    Returns:
        List[str]: [description]
    """
    result_files = []
    if Path(local_file_or_path).is_dir():
        basepath = local_file_or_path
    elif Path(local_file_or_path).is_file():
        # result_files.append(Path(local_file_or_path).read_text())
        # return result_files
        return get_urn_resolver_from_any(local_file_or_path)
    elif required:
        raise RuntimeError(
            'local_file_or_path [' + local_file_or_path + '] not found')
    else:
        # print('get_urn_resolver_local', local_file_or_path)
        return None

    # pitr = Path(basepath)
    pitr = Path(basepath).glob('*')
    # result_files_ = []
    for file_ in pitr:
        # print('file_', file_)
        # print('file_ start ~', str(file_.name).startswith('~'))
        # print('file_ ends with csv', str(file_).endswith('.csv'))
        # print('file_ ends with HXLM_DATA_URN_EXTENSIONS',
        #       str(file_).endswith(HXLM_DATA_URN_EXTENSIONS))
        if str(file_.name).startswith('~'):
            if _VERBOSE:
                print('get_urn_resolver_local skiping ', str(file_))
            continue
        if str(file_.name).endswith(HXLM_DATA_URN_EXTENSIONS):
            result_files.append(str(file_))

    # print('result_files', result_files)
    # print('sorted result_files', sorted(result_files))
    urn_rules_all = []
    for filepath in result_files:

        if filepath.endswith('.csv'):
            urn_rules_all.extend(get_urn_resolver_from_csv(filepath))
        elif filepath.endswith('.tsv'):
            urn_rules_all.extend(get_urn_resolver_from_csv(filepath, '\t'))
        elif filepath.endswith('.txt'):
            # print('')
            # print('txt')
            # print('')
            urn_rules_all.extend(get_urn_resolver_from_csv(filepath, ':'))
        elif filepath.endswith('.json'):
            urn_rules_all.extend(get_urn_resolver_from_json(filepath))
        elif filepath.endswith('.yml'):
            urn_rules_all.extend(get_urn_resolver_from_yml(filepath))

    # print('')
    # print('')
    # print('')
    # print('')
    # print('')
    # print('urn_rules_all', urn_rules_all)
    # print('')
    # print('')
    # print('')
    # print('')
    # print('')

    if required and len(urn_rules_all) == 0:
        raise RuntimeError(
            '[' + local_file_or_path + '] without rules')

    # TODO: implement some clean up on the urn_rules_all, since may have
    #       repetitive instructions (Emerson Rocha, 2021-03-07 17:56)

    return urn_rules_all


def get_urn_resolver_remote(iri_or_domain: str,
                            required: bool = False,
                            headers=None) -> List[str]:
    """Return instructions for an remote resolver

    Args:
        iri_or_domain (str): [description]
        required (bool, optional): Raise error if missing. Defaults to False.

    Raises:
        NotImplementedError: [description]

    Returns:
        List[str]: list of raw contents for each resolver instructions files
    """

    # bare domain not implemented yet.

    # r = requests.get(iri_or_domain, headers=headers)
    # path = urlparse(iri_or_domain).path
    # ext = os.path.splitext(path)[1]

    # print('ext r', urlparse(iri_or_domain))
    # print('ext r', ext, r, r.text, os.path.splitext(path))

    # if ext == 'csv':
    #     return ...

    raise NotImplementedError(
        "get_urn_resolver_remote for iri_or_domain [" +
        iri_or_domain + "] not implemtend at the moment (but will)"
    )


def get_urn_resolver_remote_authenticated(iri_or_domain: str,
                                          required: bool = False) -> List[str]:
    """Return instructions for an remote resolver (with authentication)

    Args:
        iri_or_domain (str): [description]
        required (bool, optional): Raise error if missing. Defaults to False.

    Raises:
        NotImplementedError: [description]

    Returns:
        List[str]: list of raw contents for each resolver instructions files
    """

    raise NotImplementedError(
        "get_urn_resolver_remote_authenticated for iri_or_domain [" +
        iri_or_domain + "] not implemtend at the moment." +
        "TODO: https://requests.readthedocs.io/en/latest/user/authentication/"
    )


def is_urn_data_prepared(exact_path: str = None,
                         required: bool = False) -> str:
    """[summary]

    Args:
        exact_path (str, optional): [description]. Defaults to None.
        required (bool, optional): [description]. Defaults to False.

    Raises:
        RuntimeError: [description]
        RuntimeError: [description]

    Returns:
        str: [description]
    """
    if exact_path:
        if not os.path.exists(exact_path) and required:
            raise RuntimeError('Path [' + exact_path + '] required')
        return exact_path
    if HXLM_DATA_VAULT_BASE and os.path.exists(HXLM_DATA_VAULT_BASE):
        return HXLM_DATA_VAULT_BASE
    if HXLM_DATA_VAULT_BASE_ALT and os.path.exists(HXLM_DATA_VAULT_BASE_ALT):
        return HXLM_DATA_VAULT_BASE_ALT
    if HXLM_DATA_VAULT_BASE_ALT and os.path.exists(HXLM_DATA_VAULT_BASE_ALT):
        return HXLM_DATA_VAULT_BASE_ALT
    if required:
        raise RuntimeError(
            'Path HXLM_DATA_VAULT_BASE ['
            + str(HXLM_DATA_VAULT_BASE) + '] or ' +
            'HXLM_DATA_VAULT_BASE_ALT [' + str(HXLM_DATA_VAULT_BASE_ALT) +
            '] required for this operation. Aborting.')
    return None
