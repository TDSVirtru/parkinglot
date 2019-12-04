"""Test model class electric."""

import pytest  # noqa: F401

from .compact import Compact
from .electric import Electric
from .handicapped import Handicapped

from .electric import ELECTRIC

from ..attribute import PREFERS
from ..attribute import ACCEPTS

from models.car import Car
from models.park_space import ParkSpace


# @pytest.mark.skip()
def test_electric_construction():
    foo = Electric()
    assert type(foo) is Electric
    assert foo.attribute == ELECTRIC


# @pytest.mark.skip()
def test_attribute_electric_permits_car_with_electric():
    space_attribute = Electric()
    car = Car([Compact(), Electric()])
    assert space_attribute.permits(car) is True


# @pytest.mark.skip()
def test_attribute_electric_permits_without_electric():
    space_attribute = Electric()
    car = Car([Compact()])
    assert space_attribute.permits(car) is False


# @pytest.mark.skip()
def test_attribute_electric_space_preferences():
    car_attribute = Electric()
    r_space = ParkSpace("regular", [])
    c_space = ParkSpace("compact", [Compact()])
    e_space = ParkSpace("electric", [Electric()])
    h_space = ParkSpace("handicapped", [Handicapped()])
    assert car_attribute.desires(r_space) is ACCEPTS
    assert car_attribute.desires(c_space) is ACCEPTS
    assert car_attribute.desires(e_space) is PREFERS
    assert car_attribute.desires(h_space) is ACCEPTS
