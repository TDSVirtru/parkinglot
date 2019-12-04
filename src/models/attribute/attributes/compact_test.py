"""Test model attribute class compact."""

import pytest  # noqa: F401

from .compact import Compact
from .electric import Electric
from .handicapped import Handicapped

from .compact import COMPACT

from ..attribute import ACCEPTS

from models.car import Car
from models.park_space import ParkSpace


# @pytest.mark.skip()
def test_compact_construction():
    foo = Compact()
    assert type(foo) is Compact
    assert foo.attribute == COMPACT


# @pytest.mark.skip()
def test_attribute_compact_permits_car_with_compact():
    space_attribute = Compact()
    car = Car([Compact(), Electric()])
    assert space_attribute.permits(car) is True


# @pytest.mark.skip()
def test_attribute_compact_permits_without_compact():
    space_attribute = Compact()
    car = Car([Electric()])
    assert space_attribute.permits(car) is False


# @pytest.mark.skip()
def test_attribute_compact_space_preferences():
    car_attribute = Compact()
    r_space = ParkSpace("regular", [])
    c_space = ParkSpace("compact", [Compact()])
    e_space = ParkSpace("electric", [Electric()])
    h_space = ParkSpace("handicapped", [Handicapped()])
    assert car_attribute.desires(r_space) is ACCEPTS
    assert car_attribute.desires(c_space) is ACCEPTS
    assert car_attribute.desires(e_space) is ACCEPTS
    assert car_attribute.desires(h_space) is ACCEPTS
