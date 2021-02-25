#!/usr/bin/env python3
# This is just a quick test. Can be ignored (fititnt, 2021-02-22 02:19 UTC)

import sys

import hxlm.core.base
from hxlm.core.htype.data import (
    emailDataHtype,
    numberDataHtype,
    urlDataHtype,
    phoneDataHtype,
    dateDataHtype
)
from hxlm.core.util import (
    debug
)

# from hxlm.core.htype.level import *
# from hxlm.core.htype.storage import *
# from hxlm.core.htype.usage import *
# from hxlm.core.htype.weight import *

# print(hxlm.xa_lgpd.meta.HXLM_PLUGIN_META)
# print(hxlm.core)
# print(hxlm.xa_eticaai)
# import hxlm.xa_amnesty
# print(hxlm.xa_amnesty)
# import hxlm.xz_eticaai
# import hxlm.xz_eticaai.meta
# print(hxlm.xz_eticaai)
# print(hxlm.xz_eticaai.meta)

# from pkgutil import iter_modules

# def list_submodules(module):
#     for submodule in iter_modules(module.__path__):
#         print(submodule.name)

# list_submodules(hxlm)
# import hxlm.core.internal.util
# hxlm.core.internal.util._get_plugins()

print('')
print('>> hxlm.core.util.debug')
hxlm.core.util.debug()

import hxlm.taxonomy.util
import hxlm.core.util
# import pprint
print('')
# print('>> hxlm.taxonomy.util')
# print(hxlm.taxonomy.util.get_country())
# print(hxlm.taxonomy.util.get_adm0())
print('>> hxlm.taxonomy.util')
# print(hxlm.taxonomy.util.get_country())
# print(hxlm.taxonomy.util.get_lang())  # hxl.io.HXLReader
# hxlm.core.util.hxl_info(hxlm.taxonomy.util.get_lang())  # print to stdout
# print(hxlm.core.util.hxl_info(hxlm.taxonomy.util.get_lang()))  # print to stdout
#print(list(hxlm.taxonomy.util.get_lang()))  # print to stdout

print('cmp_sensitive_level')
print(hxlm.core.util.cmp_sensitive_level('HDSL1'))
print('cmp_sensitive_level HDSL1 HDSLU')
print(hxlm.core.util.cmp_sensitive_level('HDSL1', 'HDSLU'))
print('cmp_sensitive_level HDSL1 HDSL1')
print(hxlm.core.util.cmp_sensitive_level('HDSL1', 'HDSL1'))
print('cmp_sensitive_level HDSL4 HDSL1')
print(hxlm.core.util.cmp_sensitive_level('HDSL4', 'HDSL1'))
print(hxlm.core.util.cmp_sensitive_level('HDSL1', 'HDSL1'))
print('cmp_sensitive_level HDSL1 HDSL4')
print(hxlm.core.util.cmp_sensitive_level('HDSL1', 'HDSL4'))

print('')
print('>> examples')
example_text = emailDataHtype(value="Lorem ipsum")
print('example_text', example_text.value)
print('sys.getsizeof', sys.getsizeof(example_text))

example_number = numberDataHtype(value=3.14)
print('example_number', example_number.value)
print('sys.getsizeof', sys.getsizeof(example_number))

example_url = urlDataHtype(value="https://example.org")
print('example_url', example_url.value)
print('sys.getsizeof', sys.getsizeof(example_url))

example_email = emailDataHtype(value="https://example.org")
print('example_email', example_email.value)
print('sys.getsizeof', sys.getsizeof(example_email))

example_phone = phoneDataHtype(value="+55 51 99999-9999")
print('example_phone', example_phone.value)
print('sys.getsizeof', sys.getsizeof(example_phone))

example_date = dateDataHtype(value="25/01/1986")
print('example_date', example_date.value)
print('sys.getsizeof', sys.getsizeof(example_date))

# hxltype.base.test()

# v1 = hxltype.data.DataHXLt(1, 1, 1)
# v2 = hxltype.data.DataHXLt2(1, 1, 1)
# v22 = hxltype.data.DataHXLt22(name=1, lat=1, lon=1)

# print('sys.getsizeof', sys.getsizeof(v1))
# print('sys.getsizeof2', sys.getsizeof(v2))
# print('sys.getsizeof22', sys.getsizeof(v22))

# var1 = hxltype.data.DataHXLt(1, 1, 1)
# print('sys.getsizeofvar1', sys.getsizeof(var1))
# print(var1)

#### pynacl
# @see https://pynacl.readthedocs.io/en/latest/public/#examples

## We will use system libsodium
# SODIUM_INSTALL=system pip3 install pynacl
## This would be the option without system libsodium
#  pip3 install pynacl

print('')
print('>>> libsodium tests (delete later)')

import nacl.utils
from nacl.public import PrivateKey, Box

# Generate Bob's private key, which must be kept secret
skbob = PrivateKey.generate()

# Bob's public key can be given to anyone wishing to send
#   Bob an encrypted message
pkbob = skbob.public_key

# Alice does the same and then Alice and Bob exchange public keys
skalice = PrivateKey.generate()
pkalice = skalice.public_key

# Bob wishes to send Alice an encrypted message so Bob must make a Box with
#   his private key and Alice's public key
bob_box = Box(skbob, pkalice)

# This is our message to send, it must be a bytestring as Box will treat it
#   as just a binary blob of data.
message = b"Hello pynacl"

# Encrypt our message, it will be exactly 40 bytes longer than the
#   original message as it stores authentication information and the
#   nonce alongside it.
encrypted = bob_box.encrypt(message)

# This is a nonce, it *MUST* only be used once, but it is not considered
#   secret and can be transmitted or stored alongside the ciphertext. A
#   good source of nonces are just sequences of 24 random bytes.
nonce = nacl.utils.random(Box.NONCE_SIZE)

encrypted = bob_box.encrypt(message, nonce)

# Alice creates a second box with her private key to decrypt the message
alice_box = Box(skalice, pkbob)

# Decrypt our message, an exception will be raised if the encryption was
#   tampered with or there was otherwise an error.
plaintext = alice_box.decrypt(encrypted)
print(plaintext.decode('utf-8'))

from hxlm.plugin.xz_eticaai.meta import HXLM_PLUGIN_META
print(hxlm.plugin.xz_eticaai.meta.HXLM_PLUGIN_META)