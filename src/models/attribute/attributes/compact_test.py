"""Test model attribute class compact."""

import pytest  # noqa: F401

from .compact import Compact

from .compact import COMPACT

from ..attribute import ACCEPTS


# @pytest.mark.skip()
def test_compact_construction():
    foo = Compact()
    assert type(foo) is Compact
    assert foo.attribute == COMPACT

# TODO - Implement Car and Space, then revisit these tests


def test_attribute_compact_permits():
    foo = Compact()
    assert foo.permits(None) is False


def test_attribute_compact_desires():
    foo = Compact()
    assert foo.desires(None) is ACCEPTS
