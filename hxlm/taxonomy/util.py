"""[summary]
@see https://vocabulary.unocha.org/
@see https://docs.google.com/spreadsheets/d
    /1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY/edit#gid=1088874596
"""

import hxl
from hxlm.core.exception import (
    HXLmPoliticException
)

HXLM_TAXONOMY_ADM0_URL = ("https://docs.google.com/spreadsheets/d/" +
                          "1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY/" +
                          "edit#gid=1088874596")


def get_country():
    """get_country return country/territories information.

    Regional implementers may decide to extend this method.

    See:
        https://en.wikipedia.org/wiki/List_of_territorial_disputes

    Raises:
        HXLmPoliticalException: user friendly response
    """

    raise HXLmPoliticException('Not implemented. Response varies by ' +
                               'context. See https://en.wikipedia.org/' +
                               'wiki/List_of_territorial_disputes')
    # raise HXLmPoliticException('Not implemented. Response vary by context.', {
    #                              'see_also': 'hxlm.taxonomy.get_adm0'})


def get_adm0():
    """Administrative Boundaries 0

    Returns:
        hxl.io.HXLReader: An HXLReader object
    """
    dataset = hxl.data(HXLM_TAXONOMY_ADM0_URL)
    return dataset
