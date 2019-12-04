"""Test model class handicapped."""

import pytest  # noqa: F401

from .compact import Compact
from .electric import Electric
from .handicapped import Handicapped

from .handicapped import HANDICAPPED

from ..attribute import PREFERS
from ..attribute import REJECTS

from models.car import Car
from models.park_space import ParkSpace


# @pytest.mark.skip()
def test_handicapped_construction():
    foo = Handicapped()
    assert type(foo) is Handicapped
    assert foo.attribute == HANDICAPPED


# @pytest.mark.skip()
def test_attribute_handicapped_permits_car_with_handicapped():
    space_attribute = Handicapped()
    car = Car([Compact(), Handicapped()])
    assert space_attribute.permits(car) is True


# @pytest.mark.skip()
def test_attribute_handicapped_permits_without_handicapped():
    space_attribute = Handicapped()
    car = Car([Compact()])
    assert space_attribute.permits(car) is False


# @pytest.mark.skip()
def test_attribute_handicapped_space_preferences():
    car_attribute = Handicapped()
    r_space = ParkSpace("regular", [])
    c_space = ParkSpace("compact", [Compact()])
    e_space = ParkSpace("electric", [Electric()])
    h_space = ParkSpace("handicapped", [Handicapped()])
    assert car_attribute.desires(r_space) is REJECTS
    assert car_attribute.desires(c_space) is REJECTS
    assert car_attribute.desires(e_space) is REJECTS
    assert car_attribute.desires(h_space) is PREFERS
