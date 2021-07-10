#!/usr/bin/env python3

# To output even more verbose results
#     ./tests/test_core_bin_urnresolver.py
#
# To test directly
#     pytest -vv ./tests/test_core_bin_urnresolver.py

from hxlm.core.schema.urn.util import (
    get_urn_resolver_from_csv,
    get_urn_resolver_from_json,
    get_urn_resolver_from_yml,
    # get_urn_resolver_local,
)
import os
import pathlib
TESTDIR = str(pathlib.Path(__file__).parent.absolute()) + '/urnresolver'
TEST_SIG_A = 'urn:data:xz:hxl:standard:core:hashtag'


def search_by_urn(urnkey, urnindex):
    """thanks user334856! https://stackoverflow.com/questions/8653516"""
    return [element for element in urnindex if element['urn'] == urnkey]


def test_core_bin_urnresolver_csv():
    result = get_urn_resolver_from_csv(TESTDIR + '/csv/urn.csv')
    # urn:data:un:locode -> urn:data:un:unece:locode
    result2 = search_by_urn('urn:data:un:locode', result)[0]['source'][0]

    assert result[0]['urn'] == TEST_SIG_A
    assert result[0]['urnref'] == "urn.csv"
    assert result2 == "urn:data:un:unece:locode"


def test_core_bin_urnresolver_json():
    result = get_urn_resolver_from_json(TESTDIR + '/json/urn.json')
    # urn:data:un:locode -> urn:data:un:unece:locode
    result2 = search_by_urn('urn:data:un:locode', result)[0]['source'][0]

    assert result[0]['urn'] == TEST_SIG_A
    assert result[0]['urnref'] == "urn.json"
    assert result2 == "urn:data:un:unece:locode"


def test_core_bin_urnresolver_yml():
    result = get_urn_resolver_from_yml(TESTDIR + '/yml/urn.yml')

    # urn:data:un:locode -> urn:data:un:unece:locode
    result2 = search_by_urn('urn:data:un:locode', result)[0]['source'][0]

    assert result[0]['urn'] == TEST_SIG_A
    assert result[0]['urnref'] == "urn.yml"
    assert result2 == "urn:data:un:unece:locode"


test_core_bin_urnresolver_csv()
# test_core_bin_urnresolver_json()
# test_core_bin_urnresolver_yml()
