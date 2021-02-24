"""[summary]
@see https://vocabulary.unocha.org/
@see https://docs.google.com/spreadsheets/d
    /1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY/edit#gid=1088874596
"""

import hxl

HXLM_TAXONOMY_ADM0_URL = ("https://docs.google.com/spreadsheets/d/" +
                          "1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY/" +
                          "edit#gid=1088874596")


def get_adm0():
    dataset = hxl.data(HXLM_TAXONOMY_ADM0_URL)
    return dataset
