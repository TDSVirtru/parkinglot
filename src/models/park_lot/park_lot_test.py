"""Test model class ParkLot."""

import pytest  # noqa: F401

from .park_lot import ParkLot


# @pytest.mark.skip()
def test_park_lot_construction():
    assert type(ParkLot()) is ParkLot
