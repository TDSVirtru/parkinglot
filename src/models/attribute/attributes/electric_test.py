"""Test model class electric."""

import pytest  # noqa: F401

from .electric import Electric

from .electric import ELECTRIC

from ..attribute import PREFERS
from ..attribute import ACCEPTS
from ..attribute import REJECTS


# @pytest.mark.skip()
def test_electric_construction():
    foo = Electric()
    assert type(foo) is Electric
    assert foo.attribute == ELECTRIC

# TODO - Implement Car and Space, then revisit these tests


def test_attribute_electric_permits():
    foo = Electric()
    assert foo.permits(None) is False


def test_attribute_electric_desires():
    foo = Electric()
    assert foo.desires(None) is ACCEPTS
