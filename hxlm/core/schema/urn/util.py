"""hxlm.core.schema.urn.util is (TODO: document this)
"""

import os
import csv
from pathlib import Path
# import glob

from typing import (
    Type
)

from typing import (
    List
)

from hxlm.core.htype.urn import (
    GenericUrnHtype
)

__all__ = ['get_urn_vault_local_info', 'get_urn_vault_local_info']


_HOME = str(Path.home())

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


HXLM_DATA_URN_EXTENSIONS = ('urn.csv', 'urn.json', 'urn.yml', 'urn.txt')
"""HXLM_DATA_URN_EXTENSIONS Must be a python truple"""

HXLM_DATA_URN_EXTENSIONS_ENCRYPTED = (
    'urn.csv.enc', 'urn.csv.gpg',
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
# ./hxlm/core/bin/urnresolver.py urn:data:xz:hxl:std:core:hashtag


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
    with open(urn_file, 'r') as open_urn_file:
        x = csv.reader(open_urn_file)
        print('get_urn_resolver_from_csv')
        print(x, list(x))
    # pass


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
        result_files.append(Path(local_file_or_path).read_text())
        return result_files
    elif required:
        raise RuntimeError(
            'local_file_or_path [' + local_file_or_path + '] not found')

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
            print('skiping ', str(file_))
            continue
        if str(file_.name).endswith(HXLM_DATA_URN_EXTENSIONS):
            result_files.append(str(file_))

    # print('result_files', result_files)
    print('sorted result_files', sorted(result_files))
    the_thing = []
    for filepath in result_files:
        if filepath.endswith('.csv'):
            the_thing.append(get_urn_resolver_from_csv(filepath))

    return result_files

    # print('pitr', pitr)
    # # print('list(pitr)', list(pitr))
    # print('list(pitr.glob(*)', list(pitr.glob('*')))

    # files_ = Path(lpath).glob('*urn.[csv|json|yml]')
    # files_ = [Path(lpath).glob('*urn.csv')
    # files_ = Path(lpath).glob('*.[csv][xl][ts]*')
    # files_ = Path(lpath).glob('*.{json}')
    # urnfiles = []

    # for file_ in

    # exts = ["urn.csv", ".json", ".yml", ".urn.txt", ".ppt"]
    # files_ = (str(i) for i in map(Path, os.listdir(lpath))
    #             print('i', i)
    #           if i.suffix.lower() in exts and not i.stem.startswith("~"))

    # print('filelist', filelist)

    # files = [p for p in Path(mainpath).iterdir() if p.suffix in exts]
    # files_ = Path(lpath).glob('*.json')
    # for file_ in files_:
    #     print('files', file_)


def get_urn_resolver_remote(iri_or_domain: str,
                            required: bool = False) -> List[str]:
    """Return instructions for an remote resolver

    Args:
        iri_or_domain (str): [description]
        required (bool, optional): Raise error if missing. Defaults to False.

    Raises:
        NotImplementedError: [description]

    Returns:
        List[str]: list of raw contents for each resolver instructions files
    """
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
