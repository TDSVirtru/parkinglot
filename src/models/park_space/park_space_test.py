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
def test_park_space_park_unqualified_car():
    foo = ParkSpace("Fred", [Compact()])  # A regular space with no attributes
    car = Car()  # a regular car with no attributes
    assert foo.is_empty()
    assert foo.park(car) is None
    assert foo.is_empty()


# @pytest.mark.skip()
def test_park_space_park_picky_car():
    foo = ParkSpace("Fred", [])  # A regular space with no attributes
    car = Car([Electric()])  # a regular car with no attributes
    assert foo.is_empty()
    assert foo.park(car, True) is None
    assert foo.is_empty()


# @pytest.mark.skip()
def test_park_space_park_picky_car_settles():
    foo = ParkSpace("Fred", [])  # A regular space with no attributes
    car = Car([Electric()])  # a regular car with no attributes
    assert foo.is_empty()
    assert foo.park(car, False) == "Fred"
    assert foo.is_full()


# @pytest.mark.skip()
def test_park_space_rejects_if_full():
    foo = ParkSpace("Fred", [])  # A regular space with no attributes
    car1 = Car()  # a regular car with no attributes
    car2 = Car()  # a regular car with no attributes
    foo.park(car1)
    assert foo.is_full()
    assert foo.park(car2) is None
    assert foo.is_full()
    assert foo.car is car1


def test_factory_method():
    foo = ParkSpace.create({
        'name': "42",
        'attr': ["E", "H", "C"]
    })
    assert type(foo) is ParkSpace
    assert foo.name == "42"
    assert Electric() in foo.attributes
    assert Compact() in foo.attributes
    assert Handicapped() in foo.attributes
