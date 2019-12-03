"""Test model class ParkSpace."""

import pytest  # noqa: F401

from .park_space import ParkSpace


# @pytest.mark.skip()
def test_park_space_construction():
    assert type(ParkSpace()) is ParkSpace
