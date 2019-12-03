"""Test model class electric."""

import pytest  # noqa: F401

from .electric import Electric


# @pytest.mark.skip()
def test_electric_construction():
    assert type(Electric()) is Electric
