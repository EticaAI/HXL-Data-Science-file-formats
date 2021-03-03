"""


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

__all__ = ['ConversorHSchema', 'VocabHSchema']

import os
# import json
import yaml


class ConversorHSchema:
    """ConversorHSchema is (TODO: document)
    """

    def __init__(self, vocab_base=None, vocab_extension=None):
        self.kind: str = 'ConversorHSchema'
        self._vocab_base = vocab_base
        self._vocab_extension = vocab_extension


class VocabHSchema:
    """[summary]
    """

    def __init__(self, vocab_base=None):
        self.kind: str = 'VocabHSchema'
        if vocab_base:
            self._vocab_base = vocab_base
        else:
            core_vocab = os.path.dirname(os.path.realpath(__file__)) + \
                '/core_vocab.yml'
            print('vocab_file 0', core_vocab)
            self._vocab_base = self.parse_file_yaml(core_vocab)
            print('self._vocab_base', self._vocab_base)

    @staticmethod
    def parse_file_yaml(yaml_file):
        print('yaml_file 1', yaml_file)
        with open(yaml_file) as openfile:
            data = yaml.safe_load(openfile)
            # data = yaml.safe_load_all(file_)
            # print(data)
            return data
