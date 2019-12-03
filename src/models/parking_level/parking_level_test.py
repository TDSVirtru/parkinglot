"""Test model class ParkingLevel."""

import pytest  # noqa: F401

from .parking_level import ParkingLevel


# @pytest.mark.skip()
def test_parking_level_construction():
    assert type(ParkingLevel()) is ParkingLevel
