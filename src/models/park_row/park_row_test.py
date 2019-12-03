"""Test model class Parkrow."""

import pytest  # noqa: F401

from .park_row import ParkRow


# @pytest.mark.skip()
def test_park_row_construction():
    assert type(ParkRow()) is ParkRow
