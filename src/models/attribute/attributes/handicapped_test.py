"""Test model class handicapped."""

import pytest  # noqa: F401

from .handicapped import Handicapped

from .handicapped import HANDICAPPED

from ..attribute import PREFERS
from ..attribute import ACCEPTS
from ..attribute import REJECTS


# @pytest.mark.skip()
def test_handicapped_construction():
    foo = Handicapped()
    assert type(foo) is Handicapped
    assert foo.attribute == HANDICAPPED

# TODO - Implement Car and Space, then revisit these tests


def test_attribute_handicapped_permits():
    foo = Handicapped()
    assert foo.permits(None) is False


def test_attribute_handicapped_desires():
    foo = Handicapped()
    assert foo.desires(None) is ACCEPTS
