"""hxlm.core.io.util


>>> import hxlm.core as HXLm

>>> ##### Raw dict/lists (not typical usage, but allowed)
>>> simpledict = HXLm.io.util.get_entrypoint({'key': 'val'})
>>> simpledict.entrypoint_t
<EntryPointType.PYDICT: 'PyDict'>

>>> simpledict = HXLm.io.util.get_entrypoint(['simple', 'list'])
>>> simpledict.entrypoint_t
<EntryPointType.PYLIST: 'PyList'>


>>> RAW_udhr_lat_file = HXLm.io.util.get_entrypoint(
...    HXLm.HDATUM_UDHR + 'udhr.lat.hdp.yml')
>>> RAW_udhr_lat_file
<class 'hxlm.ontologia.python.systema.ResourceWrapper'>
>>> RAW_udhr_lat_file.entrypoint_t
<EntryPointType.LOCAL_FILE: 'file://localhost/file'>


>>> RAW_udhr_lat_dir = HXLm.io.util.get_entrypoint(
...    HXLm.HDATUM_UDHR, indexes=['lat.hdp.yml'])
>>> RAW_udhr_lat_dir
<class 'hxlm.ontologia.python.systema.ResourceWrapper'>
>>> RAW_udhr_lat_dir.entrypoint_t
<EntryPointType.LOCAL_DIR: 'file://localhost/dir/'>
>>> RAW_udhr_lat_dir.content[0].keys()
dict_keys(['([Lingua Latina])', 'hsilo', 'hdatum'])


>>> ##### Remote url, exact file given
>>> URL_udhr_file = 'https://raw.githubusercontent.com/EticaAI/' + \
        'HXL-Data-Science-file-formats/main/hxlm/data/udhr/udhr.lat.hdp.yml'
>>> RAW_Rem_UDHR_file = HXLm.io.util.get_entrypoint(
...    URL_udhr_file, indexes=['lat.hdp.yml'])
>>> RAW_Rem_UDHR_file.content[0].keys()
dict_keys(['([Lingua Latina])', 'hsilo', 'hdatum'])

>>> ##### Remote url, infered url based on 'indexes' hint
>>> URL_udhr_dir = 'https://raw.githubusercontent.com/EticaAI/' + \
        'HXL-Data-Science-file-formats/main/hxlm/data/udhr/'
>>> RAW_Rem_UDHR_dir = HXLm.io.util.get_entrypoint(
...    URL_udhr_dir, indexes=['lat.hdp.yml'])
>>> RAW_Rem_UDHR_dir.content[0].keys()
dict_keys(['([Lingua Latina])', 'hsilo', 'hdatum'])

>>> ##### Raw string not implemented yet
>>> RAW_json = HXLm.io.util.get_entrypoint('{"json": "example"}')
Traceback (most recent call last):
...
NotImplementedError: get_entrypoint STRING

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import pathlib

from typing import (
    Any,
    List,
    # Union
)

from hxlm.ontologia.python.systema import (
    EntryPointType,
    # Factum,
    ResourceWrapper
)

from hxlm.ontologia.python.commune import (
    Factum
)

import hxlm.core.io.local
import hxlm.core.io.net
# import hxlm.core.io.local as load_local_file

# from hxlm.core.io.local import (
#     # is_local_file,
#     load_file as load_local_file
# )

__all__ = [
    'get_entrypoint',
    'strip_file_protocol'  # Useful if users want to strig file://host/
]


def _get_infered_filenames(indexes: List[str],
                           base_path: str = None,
                           full_path: bool = True,
                           only_prefixed: bool = False,
                           infer_index_prefix: bool = True) -> list:
    """Helper to build list of filenames to fetch when users give a directory

    IMPORTANT:
        If the base_path is a directory, is very important to end with slash /
        or this function will not be able to make good inferences about desired
        file to load

        GOOD: /tmp/my/directory/ , https://example.org/my/data/
        BAD:  /tmp/my/directory ,  https://example.org/my/data

    Args:
        indexes (List[str]): List of files (and/or suffix-like) strings
        base_path (str, optional): [description]. Defaults to None.
        full_path (bool, optional): If full path, not just names. Requires
                                    base_path defined.
        only_prefixed (bool, optional): [description]. Defaults to False.
        infer_index_prefix (bool, optional): [description]. Defaults to True.

    Returns:
        list: List of files (without the base_path) infered

    >>> _get_infered_filenames(['.hdp.yml'], 'file:///urn/data/xz/hxl/')
    ['file:///urn/data/xz/hxl/.hdp.yml', 'file:///urn/data/xz/hxl/hxl.hdp.yml']
    >>> _get_infered_filenames(['.hdp.yml'], 'http://example/hxl/')
    ['http://example/hxl/.hdp.yml', 'http://example/hxl/hxl.hdp.yml']
    >>> _get_infered_filenames(['.hdp.yml'],
    ... 'http://example/hxl/', only_prefixed=True, full_path=False)
    ['hxl.hdp.yml']
    >>> _get_infered_filenames(['.hdp.yml'])
    ['.hdp.yml']
    """

    if not infer_index_prefix or base_path is None:
        if not only_prefixed:
            return indexes
        return []

    # Note: if is passed a path to a file (not a dir/, it will get filename
    #       without extension. )
    path_ = pathlib.PurePath(base_path)
    infered_prefix = path_.name

    result = []

    # We use index prefixes as initial
    if not only_prefixed:
        result.extend(indexes)

    for suffix in indexes:
        if suffix.startswith('.'):
            result.append(infered_prefix + suffix)
        else:
            result.append(infered_prefix + '.' + suffix)

    if full_path:
        for idx, _ in enumerate(result):
            result[idx] = base_path + result[idx]

    return result


def get_entrypoint(entrypoint: Any,
                   indexes: List[str] = None,
                   infer_index_prefix: bool = True
                   ) -> ResourceWrapper:
    """From a genery entrypoint, discover and parse whatever is means

    IMPORTANT:
        If the entrypoint is a directory, is very important to end with slash /
        or this function will not be able to make good inferences about desired
        file to load

        GOOD: /tmp/my/directory/ , https://example.org/my/data/
        BAD:  /tmp/my/directory ,  https://example.org/my/data

    Args:
        entrypoint (Any): Any generic entrypoint
        indexes (List[str]): If loading directories, explicitly inform files
                    would called if they exist.
        infer_index_prefix (bool): when indexes is not None, if this method is
                    True, it will guess the imediate top level directory name
                    as additional prefix for each file.

    Returns:
        ResourceWrapper: The loaded resource with extra metadata
    """
    resw = ResourceWrapper
    resw.entrypoint = {'entrypoint': entrypoint, 'indexes': indexes}
    resw.entrypoint_t = get_entrypoint_type(entrypoint)

    # print('oioioi', resw.entrypoint)

    if resw.entrypoint_t in [EntryPointType.PYDICT, EntryPointType.PYDICT]:
        resw.content = entrypoint
    elif resw.entrypoint_t == EntryPointType.LOCAL_FILE:
        if hxlm.core.io.local.is_local_file(entrypoint):
            resw.content = hxlm.core.io.local.load_file(entrypoint)
            return resw
        resw.failed = True
        resw.log.append(Factum('[' + entrypoint + '] not is_local_file'))
    elif resw.entrypoint_t == EntryPointType.LOCAL_DIR:
        files = _get_infered_filenames(indexes=indexes,
                                       base_path=entrypoint,
                                       infer_index_prefix=True)
        try:
            resw.content = hxlm.core.io.local.load_any_file(files)
        except IOError as err:
            resw.log.append(Factum('[' + entrypoint +
                                   '] failed. Message: [' + str(err) + ']'))
    elif resw.entrypoint_t == EntryPointType.HTTP:
        try:
            if not entrypoint.endswith('/'):
                resw.content = hxlm.core.io.net.load_remote_file(entrypoint)
            else:
                iris = _get_infered_filenames(indexes=indexes,
                                              base_path=entrypoint,
                                              infer_index_prefix=True)
                resw.content = hxlm.core.io.net.load_remote_file(iris)
        except IOError as err:
            resw.failed = True
            resw.log.append(Factum('[' + entrypoint +
                                   '] failed. Message: [' + str(err) + ']'))
    elif resw.entrypoint_t == EntryPointType.STRING:
        raise NotImplementedError('get_entrypoint STRING')
    elif resw.entrypoint_t in [
        EntryPointType.FTP, EntryPointType.NETWORK_DIR,
        EntryPointType.NETWORK_FILE, EntryPointType.SSH, EntryPointType.STREAM,
        EntryPointType.UNKNOW, EntryPointType.URN
    ]:
        raise NotImplementedError('get_entrypoint ' + resw.entrypoint_t)

    # resw.failed = True

    # print(resw.content, resw.entrypoint_t, resw.log)

    # print(resw.entrypoint_t, resw.__dict__)

    return resw


def get_entrypoint_type(entrypoint: Any,
                        max_local_len: int = 4096,
                        max_remote_len: int = 65536,
                        max_urn_len: int = 4096) -> EntryPointType:
    """Get the entry point type of an VERY generic information

    Note: this function will not actually test if resource is availible on
    local or remote place. This is an generic quick check. Also both
    relative (path/to/file.csv) and absolute (path/to/file.csv) will return

    See
      - https://stackoverflow.com/questions/1661262
        /check-if-object-is-file-like-in-python
    Args:
        entrypoint (Any): Anything to be checket against EntryPointType Enum
        max_local_len (int): maximum size to check for local paths (include
                    network paths)
        max_remote_len (int): maximum size to check for remote URLs
        max_urn_len (int): maximum size to check for remote URNs

    Returns:
        EntryPointType: An EntryPointType value

    >>> get_entrypoint_type('https://urn.etica.ai/example.csv')
    <EntryPointType.HTTP: 'http'>
    >>> get_entrypoint_type('file:///urn/data/xz/hxl/std/hashtags.csv')
    <EntryPointType.LOCAL_FILE: 'file://localhost/file'>
    >>> get_entrypoint_type('file://host/path/')
    <EntryPointType.NETWORK_DIR: 'file://remotehost/dir/'>
    >>> get_entrypoint_type('file://host/path/file')
    <EntryPointType.NETWORK_FILE: 'file://remotehost/file'>
    >>> get_entrypoint_type('path/to/relative/directory')
    <EntryPointType.STRING: 'STRING'>
    >>> get_entrypoint_type('/path/to/absolute/file.csv')
    <EntryPointType.STRING: 'STRING'>
    """

    if isinstance(entrypoint, dict):
        return EntryPointType.PYDICT

    if isinstance(entrypoint, list):
        return EntryPointType.PYLIST

    if isinstance(entrypoint, str):
        ep_lower = entrypoint.lower()
        ep_len = len(entrypoint)
        can_loc = ep_len < max_local_len
        can_rem = ep_len < max_remote_len
        can_urm = ep_len < max_urn_len
        if ep_lower.startswith(('ftp://', 'ftps://')):
            return EntryPointType.FTP if can_rem else EntryPointType.UNKNOW
        if ep_lower.startswith('git://'):
            return EntryPointType.GIT if can_rem else EntryPointType.UNKNOW
        if ep_lower.startswith(('http://', 'https://')):
            return EntryPointType.HTTP if can_rem else EntryPointType.UNKNOW
        if ep_lower.startswith('ssh:'):
            return EntryPointType.SSH if can_rem else EntryPointType.UNKNOW
        if ep_lower.startswith('urn:'):
            return EntryPointType.URN if can_urm else EntryPointType.UNKNOW

        # file://path (implicitly localhost) is RFC wrong, but often tolerated
        # But we will be strict here
        if ep_lower.startswith(('file://localhost/', 'file:///')):
            if not can_loc:
                return EntryPointType.UNKNOW
            if ep_lower.endswith('/'):
                return EntryPointType.LOCAL_DIR
            return EntryPointType.LOCAL_FILE

        if ep_lower.startswith('file://'):
            if not can_loc:
                return EntryPointType.UNKNOW
            if ep_lower.endswith('/'):
                return EntryPointType.NETWORK_DIR
            return EntryPointType.NETWORK_FILE

        return EntryPointType.STRING

    # Streams and other things not tested yet
    return EntryPointType.UNKNOW


def get_concatenated_resources(
        resources: List[ResourceWrapper]) -> ResourceWrapper:
    """Concatenate the string result of list of resources

    Args:
        resources (List[ResourceWrapper]): [description]

    Returns:
        ResourceWrapper: [description]
    """
    print('TODO', resources)


def strip_file_protocol(path: str, strict: bool = True) -> str:
    """Strip (if necessary) file://host/ protocol from an local path

    See:
        - https://en.wikipedia.org/wiki/File_URI_scheme
        - https://tools.ietf.org/html/rfc3986

    Args:
        file_path (str): The file path
        strict (bool, optional): If raise exception or sillent ignore
                    non-standard prefixes. Defaults to True.

    Raises:
        SyntaxError: Raised with strict mode

    Returns:
        str: The same path, with protocol removed (if necessary)
    """

    if path.find('file:///') == 0:
        return path.replace('file://', '')
    if path.find('file://localhost/') == 0:
        return path.replace('file://', '')
    if path.find('file://') == 0:
        if strict:
            raise SyntaxError('file:// preffix for localhost or ' +
                              'non-localhost not supported at the moment')
        return path.replace('file:/', '')
    return path
