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
    assert len(foo.parks) == 0


# @pytest.mark.skip()
def test_park_row_construct_with_spaces():
    space1 = ParkSpace("One")
    space2 = ParkSpace("Two")
    space3 = ParkSpace("Three")
    foo = ParkRow("Fred", [space1, space2, space3])
    assert type(foo) is ParkRow
    assert foo.name == "Fred"
    assert len(foo.parks) == 3
    assert space1 in foo.parks
    assert space2 in foo.parks
    assert space3 in foo.parks


# @pytest.mark.skip()
def test_park_row_no_spaces_status():
    """Check the degenerate case of no spaces."""
    foo = ParkRow("Fred")
    assert foo.is_empty()
    assert foo.is_full()


# @pytest.mark.skip()
def test_park_row_fill_status():
    space1 = ParkSpace("One")
    space2 = ParkSpace("Two")
    space3 = ParkSpace("Three")
    foo = ParkRow("Fred", [space1, space2, space3])
    assert foo.is_empty()
    assert not foo.is_full()
    foo.park(Car())
    assert not foo.is_empty()
    assert not foo.is_full()
    foo.park(Car())
    assert not foo.is_empty()
    assert not foo.is_full()
    foo.park(Car())
    assert not foo.is_empty()
    assert foo.is_full()


# @pytest.mark.skip()
def test_park_row_reject_park_if_full():
    space1 = ParkSpace("One")
    space2 = ParkSpace("Two")
    space3 = ParkSpace("Three")
    foo = ParkRow("Fred", [space1, space2, space3])
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    assert foo.is_full()
    assert foo.park(Car()) is None


# @pytest.mark.skip()
def test_park_row_check_return_address():
    foo = ParkRow("Fred", [ParkSpace("One")])
    assert foo.park(Car()) == "Fred-One"


# @pytest.mark.skip()
def test_park_row_factory_method():
    foo = ParkRow.create({
        'name': "row12",
        'spaces': [
            {'name': "42", 'attr': ["H"]},
            {'name': "43", 'attr': []},
            {'name': "44", 'attr': []},
            {'name': "45", 'attr': ["C"]},
            {'name': "46", 'attr': ["C"]}
        ]
    })
    assert foo.name == "row12"
    assert len(foo.parks) == 5
