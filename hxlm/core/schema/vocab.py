"""hxlm.core.schema.vocab prepare internal vocabularies to be used by schema

PROTIP: is possible to test this file directly with
    python3 -m doctest -v hxlm/core/schema/vocab.py
    pytest -vv hxlm/ --doctest-modules --pyargs

This file is meant to accept 3 categories of internal vocabularies:

- ontologia/core.vkg.yml (default, always): the (lastest) default vocabulary
  inside the core of the library.
- core_vocab_deprecated_vNNN (not implemented, but may be used): if over time
  breaking chances do occur on the default ontologia/core.vkg.yml, an file may
  replace the old one
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
      core.vkg.yml for future auditing; even if such log is encrypted) may
      be taken in such cases by default, in special if do not exist an human
      capable of review.
    - Please note that such extra steps are not a signal of untrust; is much
      more likely that this can help debug errors or give trust to who would
      use such workflows that do exist and a chain of accountability.

TODO: implement https://docs.python.org/3/library/difflib.html to
      allow some way to diff customizations users done with vocabularies

TODO: maybe implement this for part of this method
      - https://stackoverflow.com/questions/3948873
        /prevent-function-overriding-in-python
      - https://stackoverflow.com/questions/321024
        /making-functions-non-override-able
      - https://www.python.org/dev/peps/pep-0591/

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

__all__ = ['ConversorHSchema', 'ItemHVocab', 'HVocabHelper',
           'VOCAB_RECURSION_LEAF']

import os
from dataclasses import dataclass
from typing import (
    Any,
    Type,
    Tuple
)

import functools

from copy import deepcopy
from difflib import Differ

import json

import yaml

from hxlm.core.exception import (
    HXLmException
)
from hxlm.core.hdp.util.common import (
    get_hdp_term_cleaned
)

# HXLM_CORE_SCHEMA_CORE_VOCAB = os.path.dirname(os.path.realpath(__file__)) + \
#     '/core_vocab.yml'
# """schema/core_vocab.yml is the reference vocabulary to internal commands"""
HXLM_CORE_SCHEMA_CORE_VOCAB = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__)))) + \
    '/ontologia/core.vkg.yml'
"""ontologia/core.vkg.yml is the reference vocabulary to internal commands"""

VOCAB_RECURSION_LEAF = (
    'hsilo.adm0',
    'hsilo.grupum',
    # 'hsilo.tag',
    '.tag',
    # 'htransformare.exemplum.fontem.datum',
    'fontem.datum',
)


class ConversorHSchema:
    """ConversorHSchema is (TODO: document)
    """

    def __init__(self, vocab_base=None, vocab_extension=None):
        self.kind: str = 'ConversorHSchema'
        self._vocab_base = vocab_base
        self._vocab_extension = vocab_extension


@dataclass(init=True, eq=True)
class ItemHVocab:
    """Class to abstract individual vocab required to hxlm.core work

    While at minimum implementation the ItemHVocab 'only' abstract use of
    ontologia/core.lkg.yml the implementation actually allows extend the vocab
    (like for an umplanned language) while requiring some minimum extra
    requeriments and making easier to know who requested change compared to
    ontologia/core.lkg.yml and how different was the new content.

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

    def diff(self, vocab: Type['ItemHVocab']) -> list:
        """Compare delta from current HVocab to a new ones.

        @see https://docs.python.org/3/library/difflib.html

        Args:
            vocab (ItemHVocab): another ItemHVocab-like item to diff

        Returns:
            list[str]: list of strings, Differ-like style
        """

        differ = Differ()
        result = list(differ.compare(self.to_yaml().splitlines(),
                                     vocab.to_yaml().splitlines()))

        return result

    def merge(self, vocab: Type['ItemHVocab'],
              strictly_safe: bool = True) -> bool:
        """Merge extend the current ItemHVocab in-place with a ItemHVocab

        While the ontologia/core.lkg.yml published on the web may have minimal
        functionality to enable work with the hxlm.core, we explicitly allow
        users (or who help users to convert content from new strings) to
        customize this. Since this customization itself can become a problem
        some special keys may be required when not using public vocabularies.

        While what to do with such customizations is up to compliance
        extensions the ItemHVocab can, at bare minimum, check if the author
        and contact e-mail of the old vocab was also updated.

        Args:
            vocab (Type['ItemHVocab']): An ItemHVocab-like class to extend this
            strictly_safe (bool, optional): Disable authorship check.
                                            Defaults to True.

        Returns:
            bool: [description]
        """

        original = deepcopy(self)

        # print('')
        # print('original.to_yaml')
        # print(original.to_yaml)
        # print('')

        # The merge itself
        # self.values = ChainMap(self.to_dict(), vocab.to_dict())
        self.values = {**self.to_dict(), **vocab.to_dict()}

        # print('')
        # print('self.to_yaml')
        # print(self.to_yaml)
        # print('')

        # diff = original.diff(self)
        # diff2 = self.diff(original)

        # print('ItemHVocab merge diff', diff)
        # print('')
        # print('')
        # print('ItemHVocab merge diff2', diff)
        # # print('ItemHVocab merge diff2', diff2)
        # print('')
        # print('')
        # TODO: implement here any check if this merge is valid
        #       (Emerson Rocha, 2021-03-03 14:23 UTC)

        strictly_safe = False
        if strictly_safe:
            diff = original.diff(self)
            print('TODO: merge strictly_safe', diff)

        return True

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


class HVocabHelper:
    """An Helper for ItemHVocab-like results

    NOTE: to test this file, is possible to use:
        python3 -m doctest -v hxlm/core/schema/vocab.py

    """

    _debug: bool = False
    """Debug enabled?"""

    _values: dict = None
    """An dict compatible with ItemHVocab().to_dict() output"""

    _ids_hsilo: list
    _ids_meta: list

    stopwords: Tuple = (
        'iri',
        'urn',
    )
    """Some terms are unreliable to guess language."""

    def __init__(self, vocab_values: dict = None, debug: bool = False) -> str:
        """Initialize

        Args:
            vocab_values (dict, optional): Explicitly load an vocab_values
                            compatible with ItemHVocab().to_dict() output. If
                            none is give, this will call the ItemHVocab()
                            with default values (e.g. without extending
                            vocabulary beyond what alreayd comes with the
                            core package)
        """

        self._debug = debug

        if vocab_values is None:
            vocab_values = ItemHVocab().to_dict()

        self._values = vocab_values

    def _parse_language_score_details(self,
                                      wordlist: list,
                                      score: dict,
                                      details: dict = None) -> dict:
        """Preprocess result from get_languages_of_words

        Args:
            wordlist (list): A list of words to search on loaded vocabulary
            score (dict): score from get_languages_of_words()
            details (dict, optional): details from get_languages_of_words()

        Returns:
            dict: an result
        """
        result = {
            'lang': 'UND',
            'langs': [],
            'score': {},
            'details': {}
        }
        ocorrences = []
        # print('scorescorescorescore', score)
        for lang_ in score:
            if score[lang_] is not None and score[lang_] > 0:
                ocorrences.append(lang_)
                result['score'][lang_] = score[lang_]
                result['langs'].append(lang_)
                if (details is not None) and (lang_ in details):
                    result['details'][lang_] = details[lang_]

        if (len(result['langs']) == 1) or \
                (len(wordlist) == result['score'][lang_]):
            result['lang'] = result['langs'][0]

        if self._debug:
            print('HVocabHelper()._parse_language_score_details',
                  result, wordlist, score, details)
            print('    ocorrences', ocorrences)
        return result

    def get_languages_of_hsilo(self,
                               hsilo: dict,
                               strict: bool = None) -> dict:
        """Bruteforce whatever keys an dict have to detect language is written

        Args:
            hsilo (dict): an HDPm single item. Accepts with urn as first key
            strict (bool, optional): If will check also metadata to detect
                                     an document written in one type of
                                     keywords, but hsilo.linguam says another.
                                     If strict = None, it will warn invalid
                                     input, but will not not stop everyting.
                                     If strict = False, it will tolerate most
                                     inputs, but will not check deeper

        Returns:
            dict: returns an dict. See self._parse_language_score_details()
        """

        # If there is an HDP wrapper, around a single element, parse it
        # If there is an wrapper around more than one, let it fail
        # if (len(hsilo.keys()) == 1 and
        #         str(list(hsilo.keys())[0]).lower().startswith('urn:')):
        #     hsilo = hsilo[list(hsilo.keys())[0]]
        if len(hsilo.keys()) == 1:
            key1 = str(list(hsilo.keys())[0]).lower()
            key1norm = get_hdp_term_cleaned(key1)
            if key1norm.startswith('urn:'):
                hsilo = hsilo[list(hsilo.keys())[0]]

        search_root = self.get_languages_of_words(
            wordlist=list(hsilo.keys()),
            verbose=True
        )
        thsilo = search_root['hsilo_term']

        # print('hsilo', hsilo)
        # print('hsilo.keys()', hsilo.keys())

        if self._debug:
            print('search_root', search_root)

        if not thsilo:
            if strict is not False:
                raise SyntaxWarning('hsilo_term not found for ' + str(hsilo))
            else:
                if self._debug:
                    print('hsilo_term not found for ' + str(hsilo))

        # print('   oooooooi', thsilo)
        # print('   oooooooi', hsilo[thsilo])
        # print('   oooooooi', type(hsilo[thsilo]))

        if strict is True:
            tlinguam = [
                self.get_value_of('attr.linguam.' +
                                  search_root['lang'] + '.id')]

            # TODO: when id_alts exist for root term, implement
            # tlinguam by list

            if tlinguam[0] in hsilo[thsilo]:
                vlinguam = hsilo[thsilo][tlinguam[0]]
                if vlinguam != search_root['lang']:
                    warning = 'WARNING: hsilo.linguam do not match [' + \
                        vlinguam + '] vs [' + search_root['lang'] + ']'
                    search_root['messages'] = []
                    search_root['messages'].append(warning)
                    if self._debug:
                        print(warning)

        return search_root

    def get_languages_of_words(self, wordlist: list,
                               search_root: bool = True,
                               search_attr: bool = False,
                               try_harder: bool = False,
                               try_even_harder: bool = False,
                               verbose: bool = False):
        """get_languages_of_words accept wordlist and guess the language

        Args:
            wordlist (list): A list of words to search on loaded vocabulary
            search_root (bool, optional): Search vocab.root?.
            search_attr (bool, optional): Search vocab.attr?.
            try_harder (bool, optional): Search id_alts.
            try_even_harder (bool, optional): Brute force search.
            verbose (bool, optional): Return more information.

        Examples:
            >>> from hxlm.core.schema.vocab import HVocabHelper
            >>> vhelper = HVocabHelper()
            >>> vhelper.get_languages_of_words(['lalala', 'not exist'])['lang']
            'UND'

        Raises:
            NotImplementedError: try_even_harder not implemented

        Returns:
            [dict]: Dictionary
        """

        if self._debug:
            print('HVocabHelper().get_languages_of_words START')
            print('   wordlist', wordlist)

        langs = self.get_languages_of_vocab()

        langs.append('UND')
        score = dict(zip(langs, ([0] * len(langs))))
        found_on_root = set()
        found_on_attr = set()
        details = None
        hsilo_term = ''

        for stopword in self.stopwords:
            if stopword in wordlist:
                if self._debug:
                    print('   >removed stopword', stopword, wordlist)
                wordlist.remove(stopword)

        if verbose:
            details = dict(zip(langs, ([None] * len(langs))))
            details['UND'] = []

        # For each root.TERM
        for idx, root_ in enumerate(self._values['root']):
            if not search_root:
                if self._debug:
                    print('   >> not search_root')
                break
            found = 0
            # print('   For each root.TERM...', root_)
            # For each root.term.LANG.id
            for idx2, lang_ in enumerate(self._values['root'][root_]):
                if lang_ == 'id':
                    continue
                val_ = self._values['root'][root_][lang_]['id']
                if self._debug:
                    print('   >>> For each root.term.LANG.id', val_)
                # print('   langs[lang_]', val_,  lang_)
                if val_ in wordlist:
                    score[lang_] += 1
                    found_on_root.add(val_)
                    if root_ == 'hsilo':
                        hsilo_term = val_
                    if verbose:
                        details[lang_] = {}
                        details[lang_][val_] = [
                            'root.' + root_ + '.' + lang_ + '.id']
                        found += 1
                        # print('found in lang', val_, lang_, found)
                        # print('found in details',  details)

                if not try_harder and not try_even_harder:
                    continue

                # For each root.term.LANG.id_alts
                if 'id_alts' in self._values['root'][root_][lang_]:

                    id_alts_ = self._values['root'][root_][lang_]['id_alts']
                    for id_alt_ in id_alts_:
                        if id_alt_ in wordlist:
                            score[lang_] += 1
                            found_on_root.add(id_alt_)
                            if root_ == 'hsilo':
                                hsilo_term = val_
                            if verbose:
                                if details[lang_] is None:
                                    details[lang_] = {}
                                details[lang_][id_alt_] = [
                                    'root.' + root_ + '.' +
                                    lang_ + '.id_alts']  # noqa
                            found += 1

        # For each root.TERM
        for idx, attr_ in enumerate(self._values['attr']):
            if not search_attr:
                if self._debug:
                    print('   not search_attr')
                break
            found = 0
            # For each root.term.LANG.id
            for idx2, lang_ in enumerate(self._values['attr'][attr_]):
                if lang_ == 'id':
                    continue
                val_ = self._values['attr'][attr_][lang_]['id']
                # print('langs[lang_]', langs, lang_)
                if val_ in wordlist:
                    score[lang_] += 1
                    found_on_attr.add(val_)
                    if verbose:
                        details[lang_] = {}
                        details[lang_][val_] = [
                            'attr.' + attr_ + '.' + lang_ + '.id']
                        found += 1
                        # print('found in lang', val_, lang_, found)
                        # print('found in details',  details)

                if not try_harder and not try_even_harder:
                    break

                # For each attr.term.LANG.id_alts
                if 'id_alts' in self._values['attr'][attr_][lang_]:

                    id_alts_ = self._values['attr'][attr_][lang_]['id_alts']
                    for id_alt_ in id_alts_:
                        if id_alt_ in wordlist:
                            score[lang_] += 1
                            found_on_attr.add(id_alt_)
                            found += 1
                            if verbose:
                                if details[lang_] is None:
                                    details[lang_] = {}
                                    details[lang_][id_alt_] = [
                                        'attr.' + attr_ + '.' +
                                        lang_ + '.id_alts']  # noqa

        for word in wordlist:
            if (word not in found_on_root) and (word not in found_on_attr):
                score['UND'] += 1
                if verbose:
                    details['UND'].append(word)
                if self._debug:
                    print('  not found found_on_root', found_on_root)
                    print('  not found wordlist', wordlist)
                    print('  not found score',  score)
                    print('  not found details',  details)
                    # print('not found', wordlist)
                    # print('not found', val_, score, details)

        # if verbose:
        #     print('verbose found_on_root', found_on_root)
        #     print('verbose hsilo_term', hsilo_term)
        #     print('verbose wordlist', wordlist)
        #     print('verbose score',  score)
        #     print('verbose details',  details)

        if try_even_harder:
            raise NotImplementedError('try_even_harder not implemented... yet')

        result = self._parse_language_score_details(wordlist=wordlist,
                                                    score=score,
                                                    details=details)
        result['hsilo_term'] = hsilo_term
        return result

    def get_languages_of_vocab(self):
        """Get know languages on current loaded vocabulary

        The bare minimum to add a new vocabulary is add an root.hsilo option.
        So this method abstract this. Note that this example uses the default
        vocabulary, but is possible to add new ones in runtime.

        Example:
        >>> from hxlm.core.schema.vocab import HVocabHelper
        >>> HVocabHelper().get_languages_of_vocab()
        ['ARA', 'ENG', 'FRA', 'SPA', 'LAT', 'POR', 'QAA', 'RUS', 'ZHO', 'QDP']

        Returns:
            [list]: list of all know languages in the current loaded vocab
        """

        hsilo_list = list(self._values['root']['hsilo'].keys())
        hsilo_list.remove('id')
        return hsilo_list

    def get_value_of(self, vocab_path: str):
        """Get an translation value, dot notation (get_value syntactic sugar)

        Examples:
            >>> from hxlm.core.schema.vocab import HVocabHelper
            >>> HVocabHelper().get_value_of('attr.datum.POR.id')
            'dados'
            >>> HVocabHelper().get_value_of('datum.POR.id')
            'dados'

        Args:
            vocab_path (str): Search path, with dot notation

        Returns:
            [str]: Value (if translation do exist)
        """

        if vocab_path.startswith(('root.', 'attr.')):
            return self.get_value(vocab_path)

        val = self.get_value('root.' + vocab_path)
        if val is None:
            val = self.get_value('attr.' + vocab_path)

        # keys = vocab_path.split('.')
        return val

    def get_value(self, dotted_key: str, default: Any = None) -> Any:
        """Get value by dot notation key

        Examples:
            >>> from hxlm.core.schema.vocab import HVocabHelper
            >>> HVocabHelper().get_value('datum.POR.id')
            >>> HVocabHelper().get_value('attr.datum.POR.id')
            'dados'

        Args:
            dotted_key (str): Dotted key notation
            default ([Any], optional): Value if not found. Defaults to None.

        Returns:
            [Any]: Return the result. Defaults to default
        """
        keys = dotted_key.split('.')
        return functools.reduce(
            lambda d, key: d.get(
                key) if d else default, keys, self._values
        )
