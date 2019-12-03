"""Test model class Adjudicator."""

import pytest  # noqa: F401

from .adjudicator import Adjudicator


# @pytest.mark.skip()
def test_adjudicator_construction():
    assert type(Adjudicator()) is Adjudicator
