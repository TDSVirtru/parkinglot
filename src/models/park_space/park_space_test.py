"""Test model class ParkSpace."""

import pytest  # noqa: F401

from .park_space import ParkSpace

from ..attribute import Compact
from ..attribute import Handicapped


# @pytest.mark.skip()
def test_park_space_construction_empty():
    foo = ParkSpace()
    assert type(foo) is ParkSpace
    assert len(foo.attributes) == 0


# @pytest.mark.skip()
def test_park_space_construction_with_attributes():
    attr1 = Compact()
    attr2 = Handicapped()
    foo = ParkSpace([attr1, attr2])
    assert type(foo) is ParkSpace
    assert foo.attributes == set([attr1, attr2])


# @pytest.mark.skip()
def test_park_space_durability_of_attributes1():
    attr1 = Compact()
    attr2 = Handicapped()
    foo = ParkSpace([attr1])
    with pytest.raises(Exception):
        foo.attributes = [attr2]


# @pytest.mark.skip()
def test_park_space_durability_of_attributes2():
    attr1 = Compact()
    attr2 = Handicapped()
    foo = ParkSpace([attr1])
    attr_copy = foo.attributes
    attr_copy.add(attr2)
    assert attr2 in attr_copy
    assert attr2 not in foo.attributes
