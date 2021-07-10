"""hxlm.ontologia.python.hdp

By order of importance for someone reading (or debuggin) the code. This is the
quick start


- abst (Latin: Abstractum):
  - This file contains 'abstract' (or base) python classes which are
    inherited by the other groups in the ontologia hxlm.ontologia.python.hdp
  - Part of this module DOES represents direct implementation of some parts of
    VKG/LKGs (to avoid repetition)

- radix (Latin: rādīcem; English: root)
  -  This module contains classes related either to root objects on HDP file
     (like hdatum, hsilo, htransformare...) or pseudo objets that are not
     documented to the end user, but act as somewhat wrapper.
  - Part (not all) of module DOES represents direct implementation of VKG/LKGs

- attr (Latin: Attributus):
  - This file contains classes related to HDP attributes'.
    Most of the time this is an syntatic sugar for who create code with HXLm
    do not work with plain objects (it helps with code autocomplete)
  - This module DOES represents direct implementation of some parts of VKG/LKGs

- aux (Latin: Auxilium):
    - Data that needs to be exchanged when manipulating data are described
      here.
    - This module do not represents direct implementation of some parts of
      VKG/LKGs. But may show off a lot when investigating errors.


Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# attr: https://en.wiktionary.org/wiki/attributus#Latin
# abstr: https://en.wiktionary.org/wiki/abstractus#Latin

# Etc
# - alternative to root/radicem
#    - https://en.wiktionary.org/wiki/fundatio#Latin

# TODO: these imports needs more testing

import hxlm.ontologia.python.hdp.abst  # noqa
import hxlm.ontologia.python.hdp.attr  # noqa
import hxlm.ontologia.python.hdp.radix  # noqa
