"""Test model class ParkingSpace."""

import pytest  # noqa: F401

from .parking_space import ParkingSpace


# @pytest.mark.skip()
def test_parking_space_construction():
    assert type(ParkingSpace()) is ParkingSpace
