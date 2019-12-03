"""Test model attribute class compact."""

import pytest  # noqa: F401

from .compact import Compact


# @pytest.mark.skip()
def test_compact_construction():
    assert type(Compact()) is Compact
