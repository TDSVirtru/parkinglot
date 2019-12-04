"""Test model class Car."""

import pytest  # noqa: F401

from .car import Car

from ..attribute import Compact
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

#
# def __init__(self, attributes):
#     """Construct a car."""
#     # TODO - check to see if attributes are a list of Attributes
#     # TODO - assign a unique id for unpark operations
#     self.__attr_set = set(attributes)
#
# @property
# def attributes(self):
#     """Return the set of attributes for this car."""
#     return self.__attr_set.copy()  # do not hand out the master set
#
# @attributes.setter
# def attributes(self, value):
#     """Raise an exception if atttempt is made to set attributes."""
#     raise Exception("cannot set attributes on a car")
