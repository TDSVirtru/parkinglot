"""Test model class handicapped."""

import pytest  # noqa: F401

from .handicapped import Handicapped


# @pytest.mark.skip()
def test_handicapped_construction():
    assert type(Handicapped()) is Handicapped
