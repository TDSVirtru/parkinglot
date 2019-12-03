"""Test model class Attribute."""

import pytest  # noqa: F401

from .attribute import Attribute


# @pytest.mark.skip()
def test_Attribute_construction():
    assert type(Attribute()) is Attribute
