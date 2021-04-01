"""hxlm.ontologia.python.commune contain common data classes used on HXLm


See also:
  - hxlm.ontologia.python.hdp.aux
    - Classes related to data sharing (but more focused on only HDP) are on
      this other python module
  - hxlm.core.types
    - This other module contains information that could be moved here.


Trivia:
  - "communis"
    - https://en.wiktionary.org/wiki/communis#Latin
    - https://en.wiktionary.org/wiki/commune#Latin
    - Latin, Etymology, From Old Latin co(m)moinis, from Proto-Italic
      *kommoinis, from Proto-Indo-European *ḱom-moy-ni-s, from
      *mey- (“to change”). Cognate with Proto-Germanic *gamainiz (“shared,
      communal; common”), related to immūnis, mūnia, mūnis, mūnus
      (compare Proto-Italic *moinos (“service”)).
  - Adjective (from Wikitionary):
    - 1. common, ordinary, commonplace, universal; Synonym: vulgāris
      (common, ordinary)
    - 3. democratic; representing the common sentiment

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""
from dataclasses import dataclass
from typing import Any


@dataclass(repr=False)
class Factum:
    """Encapsulate contextual messages for smarter L10N output (S-expressions!)

    The ideal usage og Factum is, with processing of some external function,
    convert terms like the 'vkg.attr.descriptionem' to what would have meaning
    to the user.

    Since Factum can also be used even for debug program (or or the
    Vocabulary Knowledge Graph may not be ready) is possible to do a raw
    print() of contents. Not ideal, but a fallback.

>>> Factum("Testing")
(vkg.attr.factum (vkg.attr.descriptionem "Testing"))
>>> Factum("Testing", linguam="ENG")
(vkg.attr.factum (vkg.attr.descriptionem (ENG "Testing")))
>>> Factum("Testing", datum=[1, 2])
(vkg.attr.factum (vkg.attr.descriptionem "Testing")(vkg.attr.datum "[1, 2]"))
    """

    descriptionem: str
    """Textual information about the fact. Strongly recommended not omit"""

    fontem: Any = None
    """Source of the message to be presented to end user. Can be ommited.

    Try keep it short. Must be something that can be converted to string.
    """

    datum: Any = None
    """Extra context about the message. Can be ommited."""

    linguam: str = None
    """When descriptionem is an natural language, this can explicit this"""

    # TODO: implement type of Factum (like if is error, or informative message)

    def __repr__(self):
        """Export an string representation without user translation of terms

        Please consider using helpers instead of export objects directly.
        """

        if self.linguam is None:
            desc = '"' + self.descriptionem + '"'
        else:
            desc = '(' + self.linguam + ' "' + self.descriptionem + '")'

        resultatum = "(vkg.attr.factum "
        resultatum += '(vkg.attr.descriptionem ' + desc + ')'

        if self.fontem is not None:
            resultatum += '(vkg.attr.fontem "' + str(self.fontem) + '")'

        if self.datum is not None:
            resultatum += '(vkg.attr.datum "' + str(self.datum) + '")'

        resultatum += ")"

        return resultatum
