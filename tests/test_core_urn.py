#!/usr/bin/env python3

# To output even more verbose results
#     ./tests/test_core_urn.py
#
# To test directly
#     pytest -vv ./tests/test_core_urn.py

import os

from hxlm.core.constant import (
    HXLM_ROOT
)


# from hxlm.core.schema.urn import (
#     HURN
# )
from hxlm.core.htype.urn import (
    cast_urn,
    is_urn,
    GenericUrnHtype,
    HdpUrnHtype
)


# def test_core_schema_urn_example_valid():
#     example1 = 'urn:x-hdp:xz:eticaai:HXL-Data-Science-file-formats'

#     resul1 = HURN().is_valid(example1)

#     assert resul1 is True


# def test_core_schema_urn_example_invalid():
#     example1 = 'urn:hdp:xz:eticaai:HXL-Data-Science-file-formats'

#     resul1 = HURN().is_valid(example1)

#     assert resul1 is False


def test_core_htype_urn_is_urn_generic_valid():
    example1 = 'urn:x-hdp:xz:eticaai:HXL-Data-Science-file-formats'
    example2 = GenericUrnHtype(value=example1)

    resul1 = is_urn(example1)
    resul2 = is_urn(example2)
    # print('oooi222', resul2)

    assert resul1 is True
    assert resul2 is True


def test_core_htype_urn_is_urn_valid():
    example1 = 'urn:x-hdp:xz:eticaai:HXL-Data-Science-file-formats'
    example2 = HdpUrnHtype(value=example1)

    resul1 = is_urn(example1, 'urn:x-hdp:')
    resul2 = is_urn(example2)

    assert resul1 is True
    assert resul2 is True


def test_core_htype_urn_is_urn_invalid():
    example1 = 'urn:hdp:xz:eticaai:HXL-Data-Science-file-formats'
    example2 = HdpUrnHtype(value=example1)

    # print('oooi', example2, example2.is_valid())
    # print('oooi', example2.valid_prefix)

    resul1 = is_urn(example1, 'urn:x-hdp:')
    resul2 = is_urn(example2)

    assert resul1 is False
    assert resul2 is False


def test_core_htype_urn_cast():
    urn_ietf1 = cast_urn('urn:ietf:rfc:2141')
    urn_ietf1.prepare()
    urn_ietf2 = cast_urn('URN:IETF:RFC:2141')
    urn_ietf2.prepare()

    urn_ietf_teapot = cast_urn('urn:ietf:rfc:2324')

    urn_hdp1 = cast_urn('urn:x-hdp:unocha:cod:ps:ago')
    urn_hdp1.prepare()
    urn_hdp2 = cast_urn('URN:X-HDP:UNOCHA:COD:PS:AGO')
    urn_hdp2.prepare()

    assert urn_ietf1.nid == 'ietf'
    assert urn_ietf2.nid == 'ietf'
    # print('oooooi', urn_ietf_teapot.get_resources()['urls'][0])
    assert urn_ietf_teapot.get_resources()['urls'][0] == \
        'https://www.rfc-editor.org/rfc/rfc2324.txt'
    assert urn_ietf_teapot.get_url() == \
        'https://www.rfc-editor.org/rfc/rfc2324.txt'

    assert urn_hdp1.nid == 'x-hdp'
    assert urn_hdp2.nid == 'x-hdp'
    # assert resul2 is False


# Perfect result:
#     https://data.humdata.org/dataset
#     /angola-census-2014-final-and-preliminary-population-results
urn_ago = cast_urn('urn:x-hdp:unocha:cod:ps:ago')
print(urn_ago.get_resources())
print('cast_urn urn_ago', urn_ago, urn_ago.get_resources())
print('cast_urn urn_ago is_valid', urn_ago.is_valid())
print('cast_urn urn_ago prepare', urn_ago.prepare())
# TODO: https://www.lexml.gov.br/

urn_ietf1 = cast_urn('urn:ietf:rfc:2141')
urn_ietf1.prepare()
print('cast_urn urn_ietf1', urn_ietf1.nid, urn_ietf1.get_resources())


test_core_htype_urn_is_urn_generic_valid()
test_core_htype_urn_is_urn_invalid()
# test_core_schema_urn_test1()
