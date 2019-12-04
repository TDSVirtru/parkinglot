"""Test model class ParkSpace."""

import pytest  # noqa: F401

from .park_space import ParkSpace

from ..attribute import Compact
from ..attribute import Electric
from ..attribute import Handicapped

from ..car import Car


# @pytest.mark.skip()
def test_park_space_construction_empty():
    foo = ParkSpace("Fred")
    assert type(foo) is ParkSpace
    assert foo.name == "Fred"
    assert len(foo.attributes) == 0


# @pytest.mark.skip()
def test_park_space_construction_with_attributes():
    attr1 = Compact()
    attr2 = Handicapped()
    foo = ParkSpace("Fred", [attr1, attr2])
    assert type(foo) is ParkSpace
    assert foo.attributes == set([attr1, attr2])


# @pytest.mark.skip()
def test_park_space_durability_of_attributes1():
    attr1 = Compact()
    attr2 = Handicapped()
    foo = ParkSpace("Fred", [attr1])
    with pytest.raises(Exception):
        foo.attributes = [attr2]


# @pytest.mark.skip()
def test_park_space_durability_of_attributes2():
    attr1 = Compact()
    attr2 = Handicapped()
    foo = ParkSpace("Fred", [attr1])
    attr_copy = foo.attributes
    attr_copy.add(attr2)
    assert attr2 in attr_copy
    assert attr2 not in foo.attributes


# @pytest.mark.skip()
def test_park_space_park_qualified_car():
    foo = ParkSpace("Fred", [])  # A regular space with no attributes
    car = Car()  # a regular car with no attributes
    assert foo.is_empty()
    assert foo.park(car) == "Fred"
    assert foo.is_full()
    assert foo.car is car


# @pytest.mark.skip()
def test_park_space_reject_park_if_full():
    foo = ParkSpace("Fred", [])  # A regular space with no attributes
    car1 = Car()  # a regular car with no attributes
    car2 = Car()  # a regular car with no attributes
    foo.park(car1)
    assert foo.is_full()
    assert foo.park(car2) is None
    assert foo.is_full()
    assert foo.car is car1


@pytest.mark.skip()
def test_park_space_reject_park_not_preferred():
    foo = ParkSpace("Fred", [])  # A regular space with no attributes
    electric_car = Car([Electric()])  # electric cars prefer electric spaces
    assert foo.park(electric_car, True) is None
