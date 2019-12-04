"""Test model class Car."""

import pytest  # noqa: F401

from .car import Car

from ..attribute import Compact
from ..attribute import Electric
from ..attribute import Handicapped


# @pytest.mark.skip()
def test_car_construction_empty():
    foo = Car()
    assert type(foo) is Car
    assert len(foo.attributes) == 0


# @pytest.mark.skip()
def test_car_construction_with_attributes():
    attr1 = Compact()
    attr2 = Handicapped()
    foo = Car([attr1, attr2])
    assert type(foo) is Car
    assert foo.attributes == set([attr1, attr2])


# @pytest.mark.skip()
def test_car_durability_of_attributes1():
    attr1 = Compact()
    attr2 = Handicapped()
    foo = Car([attr1])
    with pytest.raises(Exception):
        foo.attributes = [attr2]


# @pytest.mark.skip()
def test_car_durability_of_attributes2():
    attr1 = Compact()
    attr2 = Handicapped()
    foo = Car([attr1])
    attr_copy = foo.attributes
    attr_copy.add(attr2)
    assert attr2 in attr_copy
    assert attr2 not in foo.attributes


# @pytest.mark.skip()
def test_car_factory_method():
    car = Car.create({'attrs': ["H", "C", "E"]})
    assert type(car) is Car
    assert len(car.attributes) == 3
    assert Compact() in car.attributes
    assert Electric() in car.attributes
    assert Handicapped() in car.attributes
