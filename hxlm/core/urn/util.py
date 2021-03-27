"""hxlm.core.urn.util

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from typing import (
    Any,
    List
)

from hxlm.core.types import (
    EntryPointType,
    ResourceWrapper
)


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
