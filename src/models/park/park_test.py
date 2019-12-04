"""Test abstract model class Park."""

import pytest  # noqa: F401

from .park import Park

from ..adjudicator import Adjudicator


# @pytest.mark.skip()
def test_park_construction_empty():
    with pytest.raises(Exception):
        Park()


# @pytest.mark.skip()
def test_park_construction_with_name_only():
    foo = Park("One")
    assert type(foo) is Park
    assert foo.name == "One"
    assert type(foo.adjudicator) is Adjudicator


# @pytest.mark.skip()
def test_park_construction_with_parks():
    park1 = Park("One")
    park2 = Park("Two")
    park3 = Park("Three")
    foo = Park("Fred", [park1, park2, park3])
    assert type(foo) is Park
    assert foo.name == "Fred"
    assert len(foo.parks) == 3
    assert park1 in foo.parks
    assert park2 in foo.parks
    assert park3 in foo.parks


# @pytest.mark.skip()
def test_park_name_durability():
    foo = Park("One")
    with pytest.raises(Exception):
        foo.name = "Not one"


# @pytest.mark.skip()
def test_park_parks_durability():
    one = Park("One")
    foo = Park("Foo")
    with pytest.raises(Exception):
        foo.parks = set([one])


# @pytest.mark.skip()
def test_park_method_park_abstraction():
    foo = Park("One")
    with pytest.raises(Exception):
        foo.park()


# TODO - build tests for these.  Will require mocks.
@pytest.mark.skip()
def test_park_method_full_abstraction():
    pass


@pytest.mark.skip()
def test_park_method_empty():
    pass
