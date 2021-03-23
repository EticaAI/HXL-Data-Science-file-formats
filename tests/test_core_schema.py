#!/usr/bin/env python3

# To output even more verbose results
#     ./tests/test_core_schema.py
#     pytest -o log_cli=true --log-cli-level=DEBUG tests/test_core_schema.py

import os
# import logging
# LOGGER = logging.getLogger(__name__)

from hxlm.core.constant import (
    HXLM_ROOT
)


import hxlm.core.schema as schema

TESTS_BASE = os.path.dirname(os.path.realpath(__file__))
HXLM_BASE_BASELINE_PATH = HXLM_ROOT + '/data/baseline'


def test_core_schema_get_schema():
    schema_baseline = schema.get_schema(
        HXLM_BASE_BASELINE_PATH + '/baseline.hdpd.yml')
    # LOGGER.info('schema_baseline', str(schema_baseline))
    print('test_core_schema_get_schema', schema_baseline)

    assert schema_baseline is not None


def test_core_schema_export_schema_yaml():
    schema_baseline = schema.get_schema(
        HXLM_BASE_BASELINE_PATH + '/baseline.hdpd.yml')
    schema_baseline_yaml = schema.export_schema_yaml(schema_baseline)
    # LOGGER.info('schema_baseline', str(schema_baseline))
    print('test_core_schema_export_schema_yaml', schema_baseline_yaml)

    assert schema_baseline_yaml is not None


def test_core_schema_get_schema_vocab():
    vocab = schema.get_schema_vocab()

    assert vocab.to_dict()['root']['hcompliance']['ENG']['id'] == \
        'acceptable-use-policy'


def test_core_schema_vocab_diff():
    """test_core_schema_vocab_diff
    TODO: improve ItemHVocab().diff() and this test
    TODO: improve ItemHVocab().merge()  and this test
    """
    vocab = schema.get_schema_vocab()
    # vocab2 = schema.get_schema_vocab("{'hcompliance': '123'}")
    # vocab2 = schema.get_schema_vocab("{'root': {'attr': '123'}}")
    # vocab2 = schema.get_schema_vocab("{'root': 'invalid-test'}")
    vocab2 = schema.get_schema_vocab("{'attr': 'invalid-test'}")

    # print('vocab.diff', vocab.diff(vocab2))
    # print('vocab.merge', vocab.merge(vocab2))

    assert vocab2 is not None


# This part run only if called via
#    ./tests/test_schema.py
# pylint & tox execute only test_ directly
print('test_core_schema_get_schema')
test_core_schema_get_schema()

print('test_core_schema_export_schema_yaml')
test_core_schema_export_schema_yaml()

print('test_core_schema_get_schema_vocab')
test_core_schema_get_schema_vocab()

print('test_core_schema_vocab_diff')
test_core_schema_vocab_diff()

# print('')
# print('')
# print('')
# print('')
# print('')
# print('')

# schema_baseline = schema.get_schema('/workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/data/baseline/baseline.hdpd.yml')
# print('export_schema_yaml schema_baseline')
# print(schema.export_schema_yaml(schema_baseline))

# # example = schema.get_schema('/workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/data/baseline/hmeta.yml')
# example = schema.get_schema_as_hmeta('/workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/data/baseline/baseline.hdpd.yml')

# # print('get_schema (source file)')
# # print(example)
# # get_schema (source file)
# # {'$schema': 'https://raw.githubusercontent.com/EticaAI/HXL-Data-Science-file-formats/main/hxlm/core/schema/hxlm.schema.json', 'title': 'hxml.core.data.baseline', 'hdatums': [{'key': 'place', 'comments': 'HXL-CPLP-FOD_countries-territories.csv', 'source': 'https://docs.google.com/spreadsheets/d/12k4BWqq5c3mV9ihQscPIwtuDa_QRB-iFohO7dXSSptI/edit#gid=0', 'tags': ['ISO 3166', 'ISO 3166-2', 'ISO 3166-3']}, {'key': 'lang', 'comments': 'HXL-CPLP-FOD_languages', 'source': 'https://docs.google.com/spreadsheets/d/12k4BWqq5c3mV9ihQscPIwtuDa_QRB-iFohO7dXSSptI/edit#gid=0', 'tags': ['ISO 639-3', 'ISO 3692-2', 'ISO 3692-3']}], 'hfiles': [{'key': 'TODO.txt'}]}

# print('export_schema_yaml (string to export)')
# print(schema.export_schema_yaml(example))
# # print(schema.__dict__)
