"""Test abstract model class Park."""

import pytest  # noqa: F401

from .park import Park
from ..adjudicator import Adjudicator


# @pytest.mark.skip()
def test_park_construction_empty():
    with pytest.raises(Exception):
        Park()


# @pytest.mark.skip()
def test_park_construction_with_name():
    foo = Park("One")
    assert type(foo) is Park
    assert foo.name == "One"
    assert type(foo.adjudicator) is Adjudicator


# @pytest.mark.skip()
def test_park_name_durability():
    foo = Park("One")
    with pytest.raises(Exception):
        foo.name = "Not one"


# @pytest.mark.skip()
def test_park_method_park_abstraction():
    foo = Park("One")
    with pytest.raises(Exception):
        foo.park()


# @pytest.mark.skip()
def test_park_method_full_abstraction():
    foo = Park("One")
    with pytest.raises(Exception):
        foo.is_full()


# @pytest.mark.skip()
def test_park_method_empty_abstraction():
    foo = Park("One")
    with pytest.raises(Exception):
        foo.is_empty()
