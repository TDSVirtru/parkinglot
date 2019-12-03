"""Test class ParkingLot."""

import pytest  # noqa: F401

from .parking_lot import ParkingLot


# @pytest.mark.skip()
def test_parking_lot_construction():
    assert type(ParkingLot()) is ParkingLot
