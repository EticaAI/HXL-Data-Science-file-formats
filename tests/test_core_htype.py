# import hxlm.core.base
from hxlm.core.htype.data import (
    textDataHtype,
    emailDataHtype,
    numberDataHtype,
    urlDataHtype,
    phoneDataHtype,
    dateDataHtype
)


def test_textDataHtype():
    example1 = textDataHtype(value="Lorem ipsum")
    assert example1.value == "Lorem ipsum"


def test_numberDataHtype():
    # TODO: maybe test type? And if input was string?
    example1 = numberDataHtype(value=3.14159265358979323)
    assert example1.value == 3.14159265358979323


def test_urlDataHtype():
    example1 = urlDataHtype(value="https://example.org")
    assert example1.value == "https://example.org"


def test_emailDataHtype():
    example1 = emailDataHtype(value="me@example.org")
    assert example1.value == "me@example.org"


def test_phoneDataHtype():
    example1 = phoneDataHtype(value="+55 51 99999-9999")
    assert example1.value == "+55 51 99999-9999"


def test_dateDataHtype():
    example1 = dateDataHtype(value="25/01/1986")
    assert example1.value == "25/01/1986"
