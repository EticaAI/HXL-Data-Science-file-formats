"""hxlm.core.internal.integrity contains hash-like functions

See also:
- https://en.wikipedia.org/wiki/Comparison_of_cryptographic_hash_functions
- https://en.wikipedia.org/wiki/Hash_function_security_summary
- https://en.wikipedia.org/wiki/Preimage_attack
- https://en.wikipedia.org/wiki/Length_extension_attack

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from hashlib import md5, sha256, sha3_256

from typing import (
    Union
)

import json

__all__ = ['get_hashable', 'get_hashable_json', 'is_json_string']


def _get_hash_md5(thing) -> str:
    """MD5 hash (inly for data integrity / detect unintentional corruption)

    See also 'Fast Collision Attack on MD5', 2013 on
    https://eprint.iacr.org/2013/170.pdf

    From https://en.wikipedia.org/wiki/MD5 (text from 2021-03-22):
        "The MD5 message-digest algorithm is a widely used hash function
        producing a 128-bit hash value. Although MD5 was initially designed
        to be used as a cryptographic hash function, it has been found
        to suffer from extensive vulnerabilities.

        It can still be used as a checksum to verify data integrity,
        but only against unintentional corruption"

    From https://en.wikipedia.org/wiki/Hash_function_security_summary:
       "This attack (MD5) takes seconds on a regular PC. Two-block
        collisions in 218, single-block collisions in 241.[1]

    Examples:
        >>> _get_hash_md5('')
        'd41d8cd98f00b204e9800998ecf8427e'
        >>> _get_hash_md5('HDP')
        'd1e69b52369d7fa1405842045c06376c'
    """
    return md5(str(thing).encode('utf-8')).hexdigest()


def _get_hash_sha2_256(thing) -> str:
    """SHA-2 256

    Note: while SHA-2 256 is acceptable secure (as 2021) when SHA-3 is
          availible, consider using the _get_hash_sha3_256() as it's the same
          of the output (see 'Length extension attack')

    From https://en.wikipedia.org/wiki/SHA-2 (text from 2021-03-22):
        "SHA-2 (Secure Hash Algorithm 2) is a set of cryptographic hash
        functions designed by the United States National Security Agency
        (NSA) and first published in 2001.

        Currently, the best public attacks break preimage resistance for
        52 out of 64 rounds of SHA-256 or 57 out of 80 rounds of SHA-512,
        and collision resistance for 46 out of 64 rounds of SHA-256."

    From https://en.wikipedia.org/wiki/Length_extension_attack (2021-03-22):
        "In cryptography and computer security, a length extension attack is
        a type of attack where an attacker can use Hash(message1) and the
        length of message1 to calculate Hash(message1 ‖ message2) for an
        attacker-controlled message2, without needing to know the content of
        message1. Algorithms like MD5, SHA-1 and most of SHA-2 that are based
        on the Merkle–Damgård construction are susceptible to this kind of
        attack.[1][2][3]

        When a Merkle–Damgård based hash is misused as a message
        authentication code with construction H(secret ‖ message),[1] and
        message and the length of secret is known, a length extension attack
        allows anyone to include extra information at the end of the message
        and produce a valid hash without knowing the secret."

    Examples:
        >>> _get_hash_sha2_256('')
        'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        >>> _get_hash_sha2_256('HDP')
        '804298d5d3b29aa172fbaa735674d3649ab13d8d3e07c1a313a0aee8be625a41'
    """

    return sha256(str(thing).encode('utf-8')).hexdigest()


def _get_hash_sha3_256(thing) -> str:
    """SHA-3 256

    From https://en.wikipedia.org/wiki/SHA-3 (text from 2021-03-22):
        "SHA-3 (Secure Hash Algorithm 3) is the latest member of the Secure
        Hash Algorithm family of standards, released by NIST on August 5,
        2015.[4][5][6] Although part of the same series of standards, SHA-3
        is internally different from the MD5-like structure of SHA-1 and SHA-2.

    Examples:
        >>> _get_hash_sha3_256('')
        'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'
        >>> _get_hash_sha3_256('HDP')
        'f08ee8fa919306e05246e42cf31f4035e4e31da86a1962a15c96a469a0a7a36f'

    """

    return sha3_256(str(thing).encode('utf-8')).hexdigest()


def _get_hash_sha3_512(thing) -> str:
    """SHA-3 512
    """
    raise NotImplementedError(
        "(2021-03-21): Is this really necessary? Alternative algorithms " +
        "are likely to be more useful than just increase length."
    )


def get_hashable(thing: Union[str, dict, list]) -> str:
    """Get an normalized string ready to be normalized

    Args:
        thing (Union[str, dict, list]): Input source

    Returns:
        str: String ready to be hashed

    Examples:
        >>> import hxlm.core.internal.integrity as HDP_i
        >>> HDP_i.get_hashable('test string')
        'test string'
        >>> HDP_i.get_hashable(12345)
        '12345'
    """
    if isinstance(thing, str):
        jsonlike = is_json_string(thing)
        if not jsonlike:
            return thing
        else:
            return get_hashable_json(jsonlike)
        return thing
    if isinstance(thing, int):
        return str(thing)

    return get_hashable_json(jsonlike)


def get_hashable_json(thing: Union[dict, list]) -> str:
    """[summary]

    Args:
        thing (Union[dict, list]): [description]

    Returns:
        str: An JSON string ideal for hashing
    Examples:
        >>> import hxlm.core.internal.integrity as HDP_i
        >>> HDP_i.get_hashable_json(['test'])
        '["test"]'
    """
    # json_object = json.load(thing)
    return json.dumps(thing, indent=None, sort_keys=True)


def is_json_string(thing: str) -> Union[bool, str]:
    """Check if is an JSON-like string and return as JSON object if yes

    Args:
        thing (str): The input

    Returns:
        Union[bool, str]: Either False (not JSON-like input) or the result
    """
    try:
        json_object = json.loads(thing)
        return json_object
    # except ValueError as err:
    except ValueError:
        return False
    return None
