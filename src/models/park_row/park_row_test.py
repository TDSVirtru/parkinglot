"""Test model class Parkrow."""

import pytest  # noqa: F401

from .park_row import ParkRow

from ..park_space import ParkSpace
from ..car import Car


# @pytest.mark.skip()
def test_park_row_construction_empty():
    foo = ParkRow("Fred")
    assert type(foo) is ParkRow
    assert foo.name == "Fred"
    assert len(foo.spaces) == 0


# @pytest.mark.skip()
def test_park_row_construct_with_spaces():
    space1 = ParkSpace("One")
    space2 = ParkSpace("Two")
    space3 = ParkSpace("Three")
    foo = ParkRow("Fred", [space1, space2, space3])
    assert type(foo) is ParkRow
    assert foo.name == "Fred"
    assert len(foo.spaces) == 3
    assert space1 in foo.spaces
    assert space2 in foo.spaces
    assert space3 in foo.spaces


# @pytest.mark.skip()
def test_park_row_no_spaces_status():
    """Check the degenerate case.

    If no spaces then the row is both full and empty.
    """
    foo = ParkRow("Fred")
    assert foo.is_empty()
    assert foo.is_full()


# @pytest.mark.skip()
def test_park_row_status_with_spaces():
    space = ParkSpace("One")
    foo = ParkRow("Fred", [space])
    assert foo.is_empty()
    assert not foo.is_full()
    car = Car()
    foo.park(car)
    assert not foo.is_empty()
    assert foo.is_full()
    

@pytest.mark.skip()
def test_park_row_park_qualified_car():
    space1 = ParkSpace("One")
    space2 = ParkSpace("Two")
    space3 = ParkSpace("Three")
    foo = ParkRow("Fred", [space1, space2, space3])
    car1 = Car()
    car2 = Car()
    car3 = Car()
    assert foo.is_empty()
    assert foo.park(car1) == "Fred-One"
    assert not foo.is_full()
    assert not foo.is_empty()


@pytest.mark.skip()
def test_park_row_reject_park_if_full():
    foo = ParkRow("Fred", [])  # A regular Row with no attributes
    car1 = Car()  # a regular car with no attributes
    car2 = Car()  # a regular car with no attributes
    foo.park(car1)
    assert foo.park(car2) is None
