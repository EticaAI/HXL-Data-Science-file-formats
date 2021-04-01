"""hxlm.ontologia.python.hdp.abst

- abst (Latin: Abstractum):
  - This file contains 'abstract' (or base) python classes which are
    inherited by the other groups in the ontologia hxlm.ontologia.python.hdp
  - Part of this module DOES represents direct implementation of some parts of
    VKG/LKGs (to avoid repetition)


Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""
# abstractum
# https://en.wiktionary.org/wiki/abstract
# From Middle English abstract, borrowed from Latin abstractus, perfect passive
# participle of abstrahō (“draw away”),
# formed from abs- (“away”) + trahō (“to pull, draw”).
# The verbal sense is first attested in 1542.

from dataclasses import dataclass, InitVar
# from dataclasses import dataclass


@dataclass
class AbstAttr:
    """Abstractum Attribūtum, "Abstraction to (HDP) attributes"

    Trivia:
    - https://en.wiktionary.org/wiki/abstractum#Latin
    - https://en.wiktionary.org/wiki/attributum#Latin
    """
    # No customization at the moment


@dataclass
class AbstAux:
    """Abstractum Auxilium, "Abstraction to (HDP) raid/help"

    Trivia:
    - https://en.wiktionary.org/wiki/abstractum#Latin
    - https://en.wiktionary.org/wiki/attributum#Latin
    """
    # No customization at the moment

    librum: InitVar[list] = []
    """List of useful message logs

    Trivia:
      - "librum" means "book"
        - https://en.wiktionary.org/wiki/liber#Etymology_2_2
        - https://en.wiktionary.org/wiki/librum#Latin
    """

    okay: InitVar[bool] = True
    """attr.okay indicates if this is, at bare minimum, working
    It does not mean perfect or great. But is opposite of bad. The perfect
    example is okay = True when something goes bad but the program know how to
    recover.

    Trivia:
      - Okay (from OK in English)
        - 'It has been described as the most frequently spoken or written word
          on the planet.', source https://en.wikipedia.org/wiki/OK
        - So by using Okay, we're making translaton simpler
    """


@dataclass
class AbstRadix:
    """Abstractum Rādīcem, "Abstraction (HDP) root"

    Trivia:
    - https://en.wiktionary.org/wiki/abstractum#Latin
    - https://en.wiktionary.org/wiki/radix#Latin
    """

    librum: InitVar[list] = []
    """List of useful message logs

    Trivia:
      - "librum" means "book"
        - https://en.wiktionary.org/wiki/liber#Etymology_2_2
        - https://en.wiktionary.org/wiki/librum#Latin
    """

    okay: InitVar[bool] = True
    """attr.okay indicates if this is, at bare minimum, working
    It does not mean perfect or great. But is opposite of bad. The perfect
    example is okay = True when something goes bad but the program know how to
    recover.

    Trivia:
      - Okay (from OK in English)
        - 'It has been described as the most frequently spoken or written word
          on the planet.', source https://en.wikipedia.org/wiki/OK
        - So by using Okay, we're making translaton simpler
    """
