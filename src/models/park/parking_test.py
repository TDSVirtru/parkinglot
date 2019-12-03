"""Test abstract model class Park."""

import pytest  # noqa: F401

from .park import Park


# @pytest.mark.skip()
def test_park_construction():
    assert type(Park()) is Park
