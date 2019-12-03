"""Test model class ParkLevel."""

import pytest  # noqa: F401

from .park_level import ParkLevel


# @pytest.mark.skip()
def test_park_level_construction():
    assert type(ParkLevel()) is ParkLevel
