"""Test model class ParkLevel."""

import pytest  # noqa: F401

from .park_level import ParkLevel

from ..park_row import ParkRow
from ..park_space import ParkSpace
from ..car import Car


# @pytest.mark.skip()
def test_park_level_construction_empty():
    foo = ParkLevel("Fred")
    assert type(foo) is ParkLevel
    assert foo.name == "Fred"
    assert len(foo.parks) == 0


# @pytest.mark.skip()
def test_park_level_construct_with_rows():
    space11 = ParkSpace("S1")
    space12 = ParkSpace("S2")
    row1 = ParkRow("R1", [space11, space12])
    space21 = ParkSpace("S1")
    space22 = ParkSpace("S2")
    row2 = ParkRow("R2", [space21, space22])
    foo = ParkLevel("L1", [row1, row2])
    assert type(foo) is ParkLevel
    assert foo.name == "L1"
    assert len(foo.parks) == 2
    assert row1 in foo.parks
    assert row2 in foo.parks


# @pytest.mark.skip()
def test_park_level_no_rows_status():
    """Check the degenerate case of no spaces."""
    foo = ParkLevel("Fred")
    assert foo.is_empty()
    assert foo.is_full()


# @pytest.mark.skip()
def test_park_level_fill_status():
    space11 = ParkSpace("S1")
    space12 = ParkSpace("S2")
    row1 = ParkRow("R1", [space11, space12])
    space21 = ParkSpace("S1")
    space22 = ParkSpace("S2")
    row2 = ParkRow("R2", [space21, space22])
    foo = ParkLevel("L1", [row1, row2])
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
    assert not foo.is_full()
    foo.park(Car())
    assert not foo.is_empty()
    assert foo.is_full()


# @pytest.mark.skip()
def test_park_row_reject_park_if_full():
    space11 = ParkSpace("S1")
    space12 = ParkSpace("S2")
    row1 = ParkRow("R1", [space11, space12])
    space21 = ParkSpace("S1")
    space22 = ParkSpace("S2")
    row2 = ParkRow("R2", [space21, space22])
    foo = ParkLevel("L1", [row1, row2])
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    assert foo.is_full()
    assert foo.park(Car()) is None


# @pytest.mark.skip()
def test_park_row_check_return_address():
    space1 = ParkSpace("S1")
    row1 = ParkRow("R1", [space1])
    foo = ParkLevel("L1", [row1])
    assert foo.park(Car()) == "L1-R1-S1"


# @pytest.mark.skip()
def test_park_level_factory_method():
    foo = ParkLevel.create({
        'name': "levelA",
        'rows': [
            {
                'name': "row1",
                'spaces': [
                    {'name': "42", 'attr': []},
                    {'name': "43", 'attr': []},
                ]
            },
            {
                'name': "row2",
                'spaces': [
                    {'name': "44", 'attr': []},
                    {'name': "45", 'attr': []}
                ]
            }
        ]
    })
    assert foo.name == "levelA"
    assert len(foo.parks) == 2
