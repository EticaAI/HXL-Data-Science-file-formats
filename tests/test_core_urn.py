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

from hxlm.core.schema.urn.util import (
    get_urn_resolver_local
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


def test_core_htype_urn_cast_a():
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


def test_core_htype_urn_cast_b():
    urn_locode1 = cast_urn('urn:data--i:un:locode')
    urn_locode1.prepare()
    urn_locode2 = cast_urn('URN:DATA--I:UN:LOCODE')
    urn_locode2.prepare()
    urn_locode3 = cast_urn('urn:data:un:locode')
    urn_locode3.prepare()
    urn_hxlcplp4 = cast_urn('urn:data--i:xz:hxlcplp:fod:bool')
    urn_hxlcplp4.prepare()

    urn_brsus5 = cast_urn('urn:data:br:__saude.gov.br__:covid-19-vacinacao')
    urn_brsus5.prepare()

    # https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao

    urn_brsus5b = cast_urn(
        'urn:data:br:__opendatasus.saude.gov.br__:__/dataset/covid-19-vacinacao__')
    urn_brsus5b.prepare()

    urn_brsus5c = cast_urn(
        'urn:data:br:__opendatasus.saude.gov.br__:__dataset/covid-19-vacinacao__')
    urn_brsus5c.prepare()

    # Note: there are some randon URLs from meant to be used
    # just to see if the library dont break on non-ASCII. Source of the tests:
    #  - http://www.i18nguy.com/markup/idna-examples.html
    #  - http://www.i18nguy.com/markup
    #    /Internationalizing%20Web%20Addresses-iuc27.pdf)

    # http://中国.icom.museum
    urn_unicode6 = cast_urn('urn:data--i:cn:__中国.icom.museum__:test')
    urn_unicode6.prepare()
    # http://россия.иком.museum
    urn_unicode7 = cast_urn('urn:data--i:ru:__россия.иком.museum__:test')
    urn_unicode7.prepare()
    # http://مصر.icom.museum
    urn_unicode8 = cast_urn('urn:data--i:eg:__مصر.icom.museum__:test')
    urn_unicode8.prepare()

    # http://www.i18nguy.com/markup/idna-examples.html

    print(urn_locode1, urn_locode1.about())
    print(urn_locode1.about('base_paths'), urn_locode1.about('object_names'))

    print(urn_locode2, urn_locode2.about())
    print(urn_locode2.about('base_paths'), urn_locode2.about('object_names'))

    print(urn_locode3, urn_locode3.about())
    print(urn_locode3.about('base_paths'), urn_locode3.about('object_names'))

    print(urn_hxlcplp4, urn_hxlcplp4.about())
    print(urn_hxlcplp4.about('base_paths'), urn_hxlcplp4.about('object_names'))

    print(urn_brsus5, urn_brsus5.about())
    print(urn_brsus5.about('base_paths'), urn_brsus5.about('object_names'))

    print(urn_brsus5b, urn_brsus5.about())
    print(urn_brsus5b.about('base_paths'), urn_brsus5b.about('object_names'))

    print(urn_unicode6, urn_unicode6.about())
    print(urn_unicode6.about('base_paths'), urn_unicode6.about('object_names'))

    print(urn_unicode7, urn_unicode7.about())
    print(urn_unicode7.about('base_paths'), urn_unicode7.about('object_names'))

    print(urn_unicode8, urn_unicode8.about())
    print(urn_unicode8.about('base_paths'), urn_locode1.about('object_names'))

    # @see https://data.humdata.org/api/3/action
    #      /package_show?id=hxl-core-schemas
    urn_hxl9 = cast_urn('urn:data:xz:hxl:standard:core:hashtag').prepare()
    print(urn_hxl9, urn_hxl9.about())
    # Site: data.humdata.org
    # Dataset id: hxl-core-schemas
    # Dataset resource name: hxl-core-hashtag-schema.csv
    urn_hxl10 = cast_urn(
        'urn:data:xz:__data.humdata.org__:hxl-core-schemas:hxl-core-hashtag-schema.csv').prepare()
    print(urn_hxl10, urn_hxl10.about())
    urn_hxl11 = cast_urn(
        'urn:data--d--ckan:xz:__data.humdata.org__:hxl-core-schemas:hxl-core-hashtag-schema.csv').prepare()
    print(urn_hxl11, urn_hxl11.about())

    assert urn_locode1.nid == 'data'
    assert urn_locode2.nid == 'data'
    assert urn_locode1.nid_attr == 'i'
    assert urn_locode3.nid_attr == 'd'
    # assert urn_locode5.nid_attr == 'd'

    # urn_ietf_teapot = cast_urn('urn:ietf:rfc:2324')

    # urn_hdp1 = cast_urn('urn:x-hdp:unocha:cod:ps:ago')
    # urn_hdp1.prepare()
    # urn_hdp2 = cast_urn('URN:X-HDP:UNOCHA:COD:PS:AGO')
    # urn_hdp2.prepare()

    # assert urn_ietf1.nid == 'ietf'
    # assert urn_ietf2.nid == 'ietf'
    # # print('oooooi', urn_ietf_teapot.get_resources()['urls'][0])
    # assert urn_ietf_teapot.get_resources()['urls'][0] == \
    #     'https://www.rfc-editor.org/rfc/rfc2324.txt'
    # assert urn_ietf_teapot.get_url() == \
    #     'https://www.rfc-editor.org/rfc/rfc2324.txt'

    # assert urn_hdp1.nid == 'x-hdp'
    # assert urn_hdp2.nid == 'x-hdp'
    # assert resul2 is False

# get_urn_resolver_local('/workspace/git/EticaAI/HXL-Data-Science-file-formats/tests/urnresolver/all-in-same-dir')

# test_core_htype_urn_cast_b()

# TODO:
#  - https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao

# Perfect result:
#     https://data.humdata.org/dataset
#     /angola-census-2014-final-and-preliminary-population-results
# urn_ago = cast_urn('urn:x-hdp:unocha:cod:ps:ago')
# print(urn_ago.get_resources())
# print('cast_urn urn_ago', urn_ago, urn_ago.get_resources())
# print('cast_urn urn_ago is_valid', urn_ago.is_valid())
# print('cast_urn urn_ago prepare', urn_ago.prepare())
# # TODO: https://www.lexml.gov.br/

# urn_ietf1 = cast_urn('urn:ietf:rfc:2141')
# urn_ietf1.prepare()
# print('cast_urn urn_ietf1', urn_ietf1.nid, urn_ietf1.get_resources())


# test_core_htype_urn_is_urn_generic_valid()
# test_core_htype_urn_is_urn_invalid()
# test_core_schema_urn_test1()
