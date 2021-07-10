"""hxlm.core.internal.integrity contains hash-like functions

See also:
- https://en.wikipedia.org/wiki/Comparison_of_cryptographic_hash_functions
- https://en.wikipedia.org/wiki/Hash_function_security_summary
- https://en.wikipedia.org/wiki/Preimage_attack
- https://en.wikipedia.org/wiki/Length_extension_attack

For Python libraries
- https://docs.python.org/3/library/hmac.html
  - https://tools.ietf.org/html/rfc2104.html
- https://docs.python.org/3/library/hashlib.html

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from hashlib import md5, sha224, sha256, sha3_256, sha3_512, blake2b
from binascii import crc32

from typing import (
    Union
)

import json

__all__ = ['get_hashable', 'get_hashable_json', 'is_json_string']


def _get_hash_blake2(hashable_data, digest_size: int = 32) -> str:
    """BLACKE2

    See https://docs.python.org/3/library/hashlib.html#blake2

    From https://en.wikipedia.org/wiki/BLAKE_(hash_function), as 2021-03-22:
        "The design goal was to replace the widely used, but broken, MD5 and
        SHA-1 algorithms in applications requiring high performance in
        software. BLAKE2 was announced on December 21, 2012.[2] A reference
        implementation is available under CC0, the OpenSSL License, and the
        Apache Public License 2.0.[3][4]

        BLAKE2b is faster than MD5, SHA-1, SHA-2, and SHA-3, on 64-bit x86-64
        and ARM architectures.[3] BLAKE2 provides better security than SHA-2
        and similar to that of SHA-3: immunity to length extension,
        indifferentiability from a random oracle, etc.[5]"


    From https://docs.python.org/3/library/hashlib.html#personalization:
        "Personalization: Sometimes it is useful to force hash function to
        produce different digests for the same input for different purposes.
        Quoting the authors of the Skein hash function:
            "We recommend that all application designers seriously consider
            doing this; we have seen many protocols where a hash that is
            computed in one part of the protocol can be used in an entirely
            different part because two hash computations were done on similar
            or related data, and the attacker can force the application to
            make the hash inputs the same. Personalizing each hash function
            used in the protocol summarily stops this type of attack.

    See Also
    - https://www.blake2.net/
    - https://eprint.iacr.org/2013/322.pdf


    Examples:
        >>> _get_hash_blake2('')
        '0e5751c026e543b2e8ab2eb06099daa1d1e5df47778f7787faab45cdf12fe3a8'
        >>> _get_hash_blake2('HDP')
        '473beba8f44318ccc91aa68a307c904feb8dfbf6cb62cf1fba7049e7f62dd28c'
        >>> # Size of an MD5 hash
        >>> _get_hash_blake2('HDP', digest_size=16)
        '3ff6fd4134b4d72daa6fc99334bb779b'

    """
    preapred_data = str(hashable_data).encode('utf-8')
    return blake2b(preapred_data, digest_size=digest_size).hexdigest()


def _get_hash_blake3():
    """BLAKE 3"""
    raise NotImplementedError(
        "(2021-03-21): BLAKE 3 as current date, are not availible on Python " +
        "standard library"
    )


def _get_hash_md5(thing: str) -> str:
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


def _get_hash_sha2_224(thing: str) -> str:
    """SHA-2 224

    If SHA-3 is not availible, consider using SHA-2 224 and not SHA-2 256

    From https://en.wikipedia.org/wiki/SHA-2 (text from 2021-03-22):
        "SHA-2 (Secure Hash Algorithm 2) is a set of cryptographic hash
        functions designed by the United States National Security Agency
        (NSA) and first published in 2001.

        Currently, the best public attacks break preimage resistance for
        52 out of 64 rounds of SHA-256 or 57 out of 80 rounds of SHA-512,
        and collision resistance for 46 out of 64 rounds of SHA-256."

    Examples:
        >>> _get_hash_sha2_224('')
        'd14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f'
        >>> _get_hash_sha2_224('HDP')
        '5ce59f45cf22350ddf4236f3a586188f06c0cb96e2bcd767d3004139'
    """

    return sha224(str(thing).encode('utf-8')).hexdigest()


def _get_hash_sha2_256(thing: str, im_sure: bool = False) -> str:
    """SHA-2 256

    Note: <s>while SHA-2 256 is acceptable secure (as 2021) when SHA-3 is
          availible, consider using the _get_hash_sha3_256() as it's the same
          of the output (see 'Length extension attack')</s>
    Note 2: use SHA-2 224. Even for test this functon will require
          im_sure = True

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
        >>> _get_hash_sha2_256('', im_sure=True)
        'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        >>> _get_hash_sha2_256('HDP', im_sure=True)
        '804298d5d3b29aa172fbaa735674d3649ab13d8d3e07c1a313a0aee8be625a41'
    """

    if not im_sure:
        raise ValueError('im_sure is false. Use _get_hash_sha2_224')

    return sha256(str(thing).encode('utf-8')).hexdigest()


def _get_hash_sha3_256(thing: str) -> str:
    """SHA-3 256

    From https://en.wikipedia.org/wiki/SHA-3 (text from 2021-03-22):
        "SHA-3 (Secure Hash Algorithm 3) is the latest member of the Secure
        Hash Algorithm family of standards, released by NIST on August 5,
        2015.[4][5][6] Although part of the same series of standards, SHA-3
        is internally different from the MD5-like structure of SHA-1 and SHA-2.

    Args:
        thing ([str]): thing to hash

    Returns:
        str: SHA-3 256 hash (64 characters)

    Examples:
        >>> _get_hash_sha3_256('')
        'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'
        >>> _get_hash_sha3_256('HDP')
        'f08ee8fa919306e05246e42cf31f4035e4e31da86a1962a15c96a469a0a7a36f'

    """

    return sha3_256(str(thing).encode('utf-8')).hexdigest()


def _get_hash_sha3_512(thing: str) -> str:
    """SHA-3 512

    From https://en.wikipedia.org/wiki/SHA-3 (text from 2021-03-22):
        "SHA-3 (Secure Hash Algorithm 3) is the latest member of the Secure
        Hash Algorithm family of standards, released by NIST on August 5,
        2015.[4][5][6] Although part of the same series of standards, SHA-3
        is internally different from the MD5-like structure of SHA-1 and SHA-2.

    Args:
        thing ([str]): thing to hash

    Returns:
        str: SHA-3 512 hash (128 characters)

    Examples:
        >>> len(_get_hash_sha3_512(''))
        128
        >>> # 'a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475...
        >>> len(_get_hash_sha3_512('HDP'))
        128
        >>> # 4c94a19a4fcfa5c428a834d86eb93bec797fda166bda50988fa6a2b5ea1b...
    """

    return sha3_512(str(thing).encode('utf-8')).hexdigest()


def get_checksum_crc32(thing: Union[str, dict, list]) -> int:
    hashable = get_hashable(thing)
    return crc32(bytes(hashable.encode('utf-8')))


def get_hashable(thing: Union[str, dict, list]) -> str:
    """Get an normalized string ready to generate an hash

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

    return get_hashable_json(thing)


def get_hashable_json(thing: Union[dict, list]) -> str:
    """Convert an dict or list to an input ready to be hashable.

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
    return json.dumps(thing, indent=None, ensure_ascii=False, sort_keys=True)


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
