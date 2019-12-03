"""Test model class Car."""

import pytest  # noqa: F401

from .car import Car


# @pytest.mark.skip()
def test_car_construction():
    assert type(Car()) is Car
