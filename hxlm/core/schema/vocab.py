"""hxlm.core.schema.vocab prepare internal vocabularies to be used by schema

This file is meant to accept 3 categories of internal vocabularies:

- core_vocab.yml (default, always): the (lastest) default vocabulary inside
  the core of the library.
- core_vocab_deprecated_vNNN (not implemented, but may be used): if over time
  breaking chances do occur on the default core_vocab.yml, an file may replace
  the old one
    - This approach may be the ideal to allow faster changes at cost of
      additional logic (to be used outside the core library).
    - Note that the fixes may also be provided, just not on the core library
    - Note that this file may force reload and discard (or merge) the core
      library after a new file is parsed; does not need to be explained upfront
- user_localized_translation.yml (optional, needs to be given together with
  the original AUP): for both new languages not supported, or for
  errors/misspelling on hcompliance rules were is unviable to ask from source
  to update, the tool can explicitly allow am separate file where an human
  acceptable the legal responsibility.
    - Special measures (like at least by default log chances compared to the
      core_vocab.yml for future auditing; even if such log is encrypted) may
      be taken in such cases by default, in special if do not exist an human
      capable of review.
    - Please note that such extra steps are not a signal of untrust; is much
      more likely that this can help debug errors or give trust to who would
      use such workflows that do exist and a chain of accountability.

TODO: implement https://docs.python.org/3/library/difflib.html to
      allow some way to diff customizations users done with vocabularies

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

__all__ = ['ConversorHSchema', 'ItemHVocab']

import os
from dataclasses import dataclass

import json
import yaml

from hxlm.core.exception import (
    HXLmException
)

HXLM_CORE_SCHEMA_CORE_VOCAB = os.path.dirname(os.path.realpath(__file__)) + \
    '/core_vocab.yml'
"""schema/core_vocab.yml is the reference vocabulary to internal commands"""


class ConversorHSchema:
    """ConversorHSchema is (TODO: document)
    """

    def __init__(self, vocab_base=None, vocab_extension=None):
        self.kind: str = 'ConversorHSchema'
        self._vocab_base = vocab_base
        self._vocab_extension = vocab_extension


@dataclass(init=True, eq=True)
class ItemHVocab:
    """An individual vocabulary item
    """

    values: dict = None

    def __init__(self, vocab=HXLM_CORE_SCHEMA_CORE_VOCAB, allow_local=False):
        if isinstance(vocab, dict):
            self.values = vocab
        elif os.path.isfile(vocab):
            if allow_local or vocab == HXLM_CORE_SCHEMA_CORE_VOCAB:
                self.values = self.parse_yaml(vocab)
            else:
                raise HXLmException('allow_local must be true to open ' +
                                    vocab)
        else:
            self.values = self.parse_yaml(vocab)

    @staticmethod
    def parse_yaml(yaml_item):
        """Parse an YAML file. Can be used statically

        Args:
            yaml_item ([str]): path to a local file or an string

        Returns:
            [dict]: YAML result
        """
        if os.path.isfile(yaml_item):
            with open(yaml_item, 'r') as openfile:
                data = yaml.safe_load(openfile)
                return data
        else:
            data = yaml.safe_load(yaml_item)
            return data

    def to_dict(self) -> dict:
        """Convert current vocab to Python dict

        Returns:
            dict: Dict representation
        """

        return self.values

    def to_json(self) -> str:
        """Convert current vocab to JSON string

        Returns:
            str: String representation in YAML format
        """

        return json.dumps(self.values)

    def to_yaml(self) -> str:
        """Convert current vocab to YAML string

        Returns:
            str: String representation in YAML format
        """

        return yaml.dump(self.values)
