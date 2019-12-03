"""Test class ParkingService."""

import pytest  # noqa: F401

from .parking_service import ParkingService


# @pytest.mark.skip()
def test_parking_service_construction():
    assert type(ParkingService()) is ParkingService
